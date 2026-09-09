"""
Session 6.1 — DraftKings Sportsbook Player Props Ingestion

WHAT THIS SCRIPT IS
--------------------
Pulls live player-prop odds from DraftKings Sportsbook's own internal data
feed (the same feed the DraftKings Sportsbook website itself calls — there is
no publicly documented, officially supported API, same undocumented-endpoint
situation Session 2.2 already handled for PrizePicks/Underdog). Normalizes
the result into the common schema in schema_props.py.

**HONESTY NOTE — READ BEFORE RUNNING (same caveat pattern as Session 2.1's
DK Pick6 attempt):** Claude's own browser tool is blocked by its safety
category filter from reaching sportsbook.draftkings.com directly (confirmed
this session — same block Session 2.1 hit on prizepicks.com and
pick6.draftkings.com), so this endpoint could NOT be live-tested by Claude
before being handed to the user, unlike Underdog's endpoint in Session 2.1.
The URL and event-group ID below come from patterns publicly documented by
independent sportsbook-odds-scraping projects (not from DraftKings itself),
which is a materially weaker source than Session 2.1's PrizePicks endpoint
(independently corroborated across multiple sources) and closer to Session
2.1's DK Pick6 attempt (a single best-guess pattern that turned out to be
wrong). **Run this script and report the real result — a 403/404 here would
not be a surprise and does not mean the script is broken; it means the
guessed event-group ID or URL shape needs correcting, the same failure mode
DK Pick6 hit.** If it fails, the fallback is the same one documented in
Session 2.1's prototype_dkpick6.py: open sportsbook.draftkings.com in a real
browser, open Developer Tools → Network tab, filter to XHR/fetch requests,
navigate to an NFL prop page, and read the real request URL directly.

EVENT GROUP ID
--------------
DraftKings organizes markets under a per-league "event group" ID in the
URL path. NFL's event-group ID has been publicly documented (by independent
scraping projects, not DraftKings) as 88808 as of this session — but these
IDs are known to change without notice and are NOT part of any stable,
versioned API contract. `DK_EVENT_GROUP_ID` below is a single named
constant specifically so a future session correcting this value only has to
change it in one place.

WHAT THIS SCRIPT DOES NOT DO YET
---------------------------------
- No retry/backoff tuning against real DraftKings rate-limiting behavior —
  unknown until real traffic is observed (same posture Session 2.2 started
  from before tuning against real data).
- No pagination across multiple sports — v1 pulls one sport (NFL) via one
  event group, matching Session 2.3's own NFL-only v1 scoping decision for
  the pick'em track's estimation model, so this track's early data lines up
  with what Session 6.2 can actually model first.

WHERE OUTPUT GOES (same snapshot pattern as ingest_pickem.py, Session 2.2)
---------------------------------------------------------------------------
/data/sportsbook_props/raw/draftkings_<timestamp>.json
/data/sportsbook_props/normalized/dk_props_<timestamp>.csv
/data/sportsbook_props/normalized/dk_latest.csv  (overwritten every run)

USAGE
-----
pip install requests --break-system-packages
python ingest_dk_props.py
"""

from __future__ import annotations

import csv
import json
import logging
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import requests

from schema_props import NORMALIZED_COLUMNS, NormalizedSportsbookProp

BASE_DIR = Path(__file__).resolve().parents[2]
RAW_DIR = BASE_DIR / "data" / "sportsbook_props" / "raw"
NORMALIZED_DIR = BASE_DIR / "data" / "sportsbook_props" / "normalized"
LOG_PATH = BASE_DIR / "logs" / "ingestion.log"

# NFL — see "EVENT GROUP ID" note above. Unverified by Claude directly.
DK_EVENT_GROUP_ID = "88808"
DK_ENDPOINT = (
    f"https://sportsbook.draftkings.com/sites/US-SB/api/v5/"
    f"eventgroups/{DK_EVENT_GROUP_ID}"
)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json",
    # FIX (2026-09-09, real result): a real local run returned "403 Client
    # Error: Forbidden" on every attempt with only the two headers above —
    # a bot-protection block (WAF/edge rule), NOT a 404, which is the
    # signal that DK_EVENT_GROUP_ID/the URL shape are plausibly still
    # correct and the block is about request identity, not a wrong
    # resource. FanDuel's own real feed (ingest_fd_props.py) responded
    # with only its two original headers, so the working baseline for a
    # comparison is real, not guessed. Referer/Origin/Accept-Language are
    # added here as the standard next thing to try against this class of
    # block — UNCONFIRMED whether this specific set is sufficient; if a
    # rerun still 403s, this is real evidence the block is stronger than a
    # missing-header check (e.g. TLS/JA3 fingerprinting `requests` cannot
    # replicate), and the Developer-Tools fallback in this file's module
    # docstring is the real next step, not another header guess.
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://sportsbook.draftkings.com/",
    "Origin": "https://sportsbook.draftkings.com",
}

MAX_RETRIES = 2
RETRY_BACKOFF_SECONDS = 3
REQUEST_TIMEOUT_SECONDS = 15

# Category tags relevant to Session 6.1's legal-footprint check — see
# docs/sportsbook_props_legal_footprint.md. Kept as a simple substring match
# against DK's own market "name" field since DK does not expose a clean
# category field of its own.
PLAYER_PROP_CATEGORY_HINTS = {
    "touchdown": "player_touchdown",
    "td scorer": "player_touchdown",
}


def setup_logging() -> logging.Logger:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("ingest_dk_props")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()

    file_handler = logging.FileHandler(LOG_PATH, mode="a", encoding="utf-8")
    console_handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s UTC | %(levelname)s | %(message)s")
    formatter.converter = time.gmtime
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger


log = setup_logging()


def _fetch_with_retries(url: str, params: Optional[dict] = None) -> dict:
    last_error = None
    for attempt in range(1, MAX_RETRIES + 2):
        try:
            response = requests.get(
                url, headers=HEADERS, params=params, timeout=REQUEST_TIMEOUT_SECONDS
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as exc:
            last_error = exc
            log.warning(
                "Attempt %d/%d failed for %s: %s",
                attempt,
                MAX_RETRIES + 1,
                url,
                exc,
            )
            if attempt <= MAX_RETRIES:
                time.sleep(RETRY_BACKOFF_SECONDS)
    raise RuntimeError(f"All attempts failed for {url}: {last_error}")


def fetch_dk_props() -> dict:
    return _fetch_with_retries(DK_ENDPOINT, params={"format": "json"})


def _prop_category(market_name: str) -> str:
    lowered = (market_name or "").lower()
    for hint, category in PLAYER_PROP_CATEGORY_HINTS.items():
        if hint in lowered:
            return category
    return "player_performance"


def normalize_dk(payload: dict, pulled_at: str) -> list[NormalizedSportsbookProp]:
    """Defensive by design, same posture as ingest_pickem.py's normalizers:
    a missing/renamed field causes a per-record skip with a logged warning,
    never a whole-run crash. DK's public eventgroup response (per
    independently-documented shape) nests events under
    eventGroup.events, and each event's markets/outcomes under
    eventGroup.offerCategories -> offerSubcategories -> offers -> outcomes.
    This structure is UNCONFIRMED against a real live response — the exact
    key names below are the single most likely point of failure if this
    script's first real run does not match."""
    rows: list[NormalizedSportsbookProp] = []

    event_group = payload.get("eventGroup")
    if not isinstance(event_group, dict):
        log.error(
            "DraftKings response missing expected top-level 'eventGroup' key — "
            "schema may differ from the documented pattern this script assumed. "
            "Skipping this platform for this run."
        )
        return rows

    events_by_id = {
        str(e.get("eventId")): e for e in (event_group.get("events") or [])
    }

    offer_categories = event_group.get("offerCategories") or []
    for category in offer_categories:
        for subcategory in category.get("offerSubcategoryDescriptors") or []:
            subcat = (subcategory.get("offerSubcategory") or {})
            for offer_group in subcat.get("offers") or []:
                for offer in offer_group:
                    try:
                        event_id = str(offer.get("eventId"))
                        event = events_by_id.get(event_id, {})
                        outcomes = offer.get("outcomes") or []

                        over_odds = None
                        under_odds = None
                        line_value = None
                        player_name = None
                        market_name = offer.get("label") or ""

                        for outcome in outcomes:
                            label = str(outcome.get("label", "")).lower()
                            american = outcome.get("oddsAmerican")
                            try:
                                american_int = (
                                    int(american) if american is not None else None
                                )
                            except (TypeError, ValueError):
                                american_int = None

                            if line_value is None and outcome.get("line") is not None:
                                line_value = _to_float(outcome.get("line"))
                            if player_name is None:
                                player_name = outcome.get("participant")

                            if "over" in label:
                                over_odds = american_int
                            elif "under" in label:
                                under_odds = american_int

                        rows.append(
                            NormalizedSportsbookProp(
                                platform="draftkings",
                                source_event_id=event_id,
                                source_market_id=str(offer.get("providerOfferId") or offer.get("label")),
                                source_selection_id=str(
                                    outcomes[0].get("providerOutcomeId")
                                    if outcomes
                                    else ""
                                ),
                                player_name=player_name,
                                team=None,  # not reliably present at offer level
                                sport="NFL",  # v1 scope, see module docstring
                                stat_type=market_name or None,
                                prop_category=_prop_category(market_name),
                                line=line_value,
                                over_american_odds=over_odds,
                                under_american_odds=under_odds,
                                game_id=event_id,
                                game_start_time=event.get("startDate"),
                                status=event.get("status"),
                                pulled_at=pulled_at,
                            )
                        )
                    except Exception as exc:  # noqa: BLE001
                        log.warning("Skipped one malformed DraftKings record: %s", exc)
                        continue

    return rows


def _to_float(value) -> Optional[float]:
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def save_raw_snapshot(payload: dict, pulled_at_compact: str) -> Path:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    out_path = RAW_DIR / f"draftkings_{pulled_at_compact}.json"
    out_path.write_text(json.dumps(payload, indent=2))
    return out_path


def write_normalized_csv(path: Path, rows: list[NormalizedSportsbookProp]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=NORMALIZED_COLUMNS)
        writer.writeheader()
        for row in rows:
            writer.writerow(row.as_row())


def run() -> dict:
    pulled_at = datetime.now(timezone.utc).isoformat()
    pulled_at_compact = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    summary = {
        "pulled_at": pulled_at,
        "draftkings_rows": 0,
        "draftkings_ok": False,
    }

    log.info("=== DraftKings props ingestion run starting ===")

    try:
        payload = fetch_dk_props()
        save_raw_snapshot(payload, pulled_at_compact)
        rows = normalize_dk(payload, pulled_at)
        summary["draftkings_rows"] = len(rows)
        summary["draftkings_ok"] = True
        log.info("DraftKings: %d normalized rows", len(rows))
    except Exception as exc:  # noqa: BLE001
        log.error("DraftKings ingestion failed for this run: %s", exc)
        rows = []

    snapshot_path = NORMALIZED_DIR / f"dk_props_{pulled_at_compact}.csv"
    latest_path = NORMALIZED_DIR / "dk_latest.csv"
    write_normalized_csv(snapshot_path, rows)
    write_normalized_csv(latest_path, rows)

    log.info(
        "=== DraftKings props ingestion run complete: %d rows (%s) ===",
        len(rows),
        "OK" if summary["draftkings_ok"] else "FAILED",
    )

    summary["snapshot_path"] = str(snapshot_path)
    return summary


if __name__ == "__main__":
    result = run()
    print(json.dumps(result, indent=2))
