"""
Session 6.1 — DraftKings Sportsbook Player Props Ingestion

REAL API CONFIRMED THIS SESSION (2026-09-09) — REPLACES AN EARLIER, WRONG GUESS
---------------------------------------------------------------------------------
The first version of this script guessed `sportsbook.draftkings.com/sites/
US-SB/api/v5/eventgroups/{id}` — a pattern from independent, non-official
scraping documentation. That guess returned a real `403 Forbidden` on every
attempt (confirmed live, 3/3 retries) even after adding browser-identity
headers (Referer/Origin/Accept-Language) — a stronger signal than a simple
missing-header problem.

The user then captured DK's REAL current API directly via Chrome DevTools
(Network tab, "Copy Response" on the real requests DK's own site makes while
browsing NFL odds) — the same fallback procedure Session 2.1 documented for
DK Pick6, now actually exercised and successful. The real API is entirely
different from the old guess:

  - Real domain: sportsbook-nash.draftkings.com (NOT sportsbook.draftkings.com)
  - Real site code: state-specific, e.g. "US-KS-SB" for Kansas (NOT "US-SB")
  - Real site name: "dkusks" (embedded in the nav URL path)
  - Real path structure: /api/sportscontent/... (NOT /api/v5/eventgroups/...)
  - Real NFL league ID: 88808 — this one part of the original guess WAS
    correct, independently confirmed twice more in captured real traffic
    (inside a `selectionId` string, and as the `leagueId` field on every
    real event/market/selection record).

THREE REAL, CONFIRMED ENDPOINTS (response bodies captured directly, not
guessed):
  1. Navigation — league's event list:
     GET /sites/{site}/api/sportscontent/navigation/{siteName}/v2/nav/leagues/{leagueId}
     Returns: {"events": [{id, name, participants, startEventDate, ...}, ...]}
  2. Markets for one event + one subcategory:
     GET /sites/{site}/api/sportscontent/controldata/event/eventSubcategory/v1/markets
         ?isBatchable=false&templateVars={eventId},{subCategoryId}
         &marketsQuery=$filter=eventId eq '{eventId}' AND clientMetadata/subCategoryId eq '{subCategoryId}' AND tags/all(t: t ne 'SportcastBetBuilder')
         &entity=markets
     Returns: {"markets": [...], "selections": [...]}

A REAL, IMPORTANT SCHEMA MISMATCH FOUND FROM THE CAPTURED DATA
-----------------------------------------------------------------
schema_props.py was built assuming every prop is a two-sided Over/Under
(matching the pick'em platforms' shape) — an unverified assumption. The
real captured data for subCategoryId 12438 ("Anytime TD Scorer", "First TD
Scorer", "2+ TDs") is NOT that shape: each market has ONE selection PER
PLAYER (e.g. "Bhayshul Tuten +650"), not a two-sided Over/Under pair. This
is a "will this specific player do X" market, priced against the field, not
a line with an over/under side. Confirmed directly from real captured JSON
(the `selections` array — no `stat_value`/handicap, no over/under runner
pairing at all, just one American-odds price per player per market).

**v1 scope, resolved from this real finding:** normalize these as
`over_american_odds` = the player's real captured price (this player scores
= "yes"), `under_american_odds` = None (there's no priced "no" side per
player in this market shape — the true "no" is implicit across the whole
field). `line` is left None (there is no numeric line in this market type).
This is a stated, deliberate v1 boundary, not a guess: TD-scorer markets
are supported as single-sided "yes" prices; a numeric-line market type
(e.g. Passing Yards Over/Under, visibly present on FanDuel's real data)
requires DK's own subcategory ID for that stat — NOT YET DISCOVERED, since
that requires clicking into that specific tab in DK's UI to capture its
real subCategoryId the same way 12438 was captured for TD scorers. Named
explicitly as an open item, not silently unsupported.

WHAT THIS SCRIPT DOES NOT DO YET
---------------------------------
- Only pulls subCategoryId 12438 (Anytime/First TD Scorer, 2+ TDs) — the
  one subcategory actually captured from real traffic this session. Other
  real prop categories (Passing/Rushing/Receiving Yards, etc. — all
  visibly present on FanDuel's real pull) need their own DK subCategoryId
  captured the same way before they can be added here.
- `DK_SITE` ("US-KS-SB") is specific to the real browser session that
  captured this traffic (Kansas). A different real state may need a
  different site code — unconfirmed for other states.
- Pulls only the first N events returned by the navigation call (see
  `MAX_EVENTS_PER_RUN`) to keep a single run's real request count bounded
  while this is still a single-subcategory v1.

WHERE OUTPUT GOES
------------------
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

DK_DOMAIN = "sportsbook-nash.draftkings.com"
DK_SITE = "US-KS-SB"          # see module docstring — state-specific, unconfirmed elsewhere
DK_SITE_NAME = "dkusks"
DK_LEAGUE_ID = "88808"        # NFL — confirmed three separate ways this session
DK_TD_SUBCATEGORY_ID = "12438"  # Anytime/First TD Scorer, 2+ TDs — only subcategory captured so far

NAV_URL = (
    f"https://{DK_DOMAIN}/sites/{DK_SITE}/api/sportscontent/navigation/"
    f"{DK_SITE_NAME}/v2/nav/leagues/{DK_LEAGUE_ID}"
)
MARKETS_URL = (
    f"https://{DK_DOMAIN}/sites/{DK_SITE}/api/sportscontent/controldata/"
    f"event/eventSubcategory/v1/markets"
)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json",
    "Referer": f"https://{DK_DOMAIN}/",
}

MAX_RETRIES = 2
RETRY_BACKOFF_SECONDS = 3
REQUEST_TIMEOUT_SECONDS = 15
MAX_EVENTS_PER_RUN = 8  # see module docstring — keeps v1 request count bounded


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


def fetch_dk_events() -> dict:
    return _fetch_with_retries(NAV_URL)


def fetch_dk_markets(event_id: str, subcategory_id: str) -> dict:
    marketsQuery = (
        f"$filter=eventId eq '{event_id}' AND "
        f"clientMetadata/subCategoryId eq '{subcategory_id}' AND "
        f"tags/all(t: t ne 'SportcastBetBuilder')"
    )
    params = {
        "isBatchable": "false",
        "templateVars": f"{event_id},{subcategory_id}",
        "marketsQuery": marketsQuery,
        "entity": "markets",
    }
    return _fetch_with_retries(MARKETS_URL, params=params)


def normalize_dk_markets(
    payload: dict, event: dict, pulled_at: str
) -> list[NormalizedSportsbookProp]:
    """Normalizes one event's real captured markets/selections response.
    Defensive by design, same posture as every other normalizer in this
    project: a missing/renamed field causes a per-record skip with a
    logged warning, never a whole-run crash. See module docstring for why
    under_american_odds is always None for this subcategory (no priced
    "no" side exists per player in this real market shape)."""
    rows: list[NormalizedSportsbookProp] = []

    markets = payload.get("markets")
    selections = payload.get("selections")
    if not isinstance(markets, list) or not isinstance(selections, list):
        log.error(
            "DraftKings markets response missing expected 'markets'/'selections' "
            "lists — schema may have changed. Skipping this event/subcategory."
        )
        return rows

    markets_by_id = {str(m.get("id")): m for m in markets}
    event_id = str(event.get("id", ""))
    event_name = event.get("name")
    event_start = event.get("startEventDate")

    for selection in selections:
        try:
            market_id = str(selection.get("marketId"))
            market = markets_by_id.get(market_id, {})
            market_name = market.get("name") or ""

            american_raw = (selection.get("displayOdds") or {}).get("american")
            over_odds = _american_str_to_int(american_raw)

            player_name = selection.get("label")
            # DK marks non-player outcomes (e.g. "JAX Jaguars D/ST", "No
            # Touchdown Scorer") with no "participants" list — real,
            # confirmed in captured data. Kept (not dropped) since it's a
            # real priced outcome, just not tied to an individual player.
            participants = selection.get("participants") or []
            team = None
            if not participants and player_name:
                team = player_name  # team/defense or field outcome

            rows.append(
                NormalizedSportsbookProp(
                    platform="draftkings",
                    source_event_id=event_id,
                    source_market_id=market_id,
                    source_selection_id=str(selection.get("id", "")),
                    player_name=player_name if participants else None,
                    team=team,
                    sport="NFL",
                    stat_type=market_name or None,
                    prop_category="player_touchdown",
                    line=None,  # see module docstring — no numeric line in this subcategory
                    over_american_odds=over_odds,
                    under_american_odds=None,  # see module docstring
                    game_id=event_id,
                    game_start_time=event_start,
                    status=None,
                    pulled_at=pulled_at,
                )
            )
        except Exception as exc:  # noqa: BLE001
            log.warning("Skipped one malformed DraftKings selection: %s", exc)
            continue

    return rows


def _american_str_to_int(value) -> Optional[int]:
    """DK's real displayOdds.american field is a string like "+650" or
    "-114" (confirmed in captured data) — strips the leading '+' (int()
    doesn't accept it) and converts."""
    if value is None:
        return None
    try:
        return int(str(value).replace("+", ""))
    except (TypeError, ValueError):
        return None


def save_raw_snapshot(payload: dict, pulled_at_compact: str, suffix: str) -> Path:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    out_path = RAW_DIR / f"draftkings_{suffix}_{pulled_at_compact}.json"
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
        "events_pulled": 0,
    }

    log.info("=== DraftKings props ingestion run starting ===")

    all_rows: list[NormalizedSportsbookProp] = []
    try:
        nav_payload = fetch_dk_events()
        save_raw_snapshot(nav_payload, pulled_at_compact, "nav")
        events = nav_payload.get("events") or []
        if not events:
            log.error(
                "DraftKings navigation response returned no events — "
                "schema may have changed."
            )
        events = events[:MAX_EVENTS_PER_RUN]

        for event in events:
            event_id = str(event.get("id", ""))
            if not event_id:
                continue
            try:
                markets_payload = fetch_dk_markets(event_id, DK_TD_SUBCATEGORY_ID)
                save_raw_snapshot(
                    markets_payload, pulled_at_compact, f"markets_{event_id}"
                )
                rows = normalize_dk_markets(markets_payload, event, pulled_at)
                all_rows.extend(rows)
            except Exception as exc:  # noqa: BLE001 — one event's failure
                # must not block the rest of the run.
                log.warning(
                    "Skipped markets pull for DraftKings event %s: %s",
                    event_id,
                    exc,
                )
                continue

        summary["draftkings_ok"] = True
        summary["events_pulled"] = len(events)
        summary["draftkings_rows"] = len(all_rows)
        log.info(
            "DraftKings: %d normalized rows across %d events",
            len(all_rows),
            len(events),
        )
    except Exception as exc:  # noqa: BLE001
        log.error("DraftKings ingestion failed for this run: %s", exc)

    snapshot_path = NORMALIZED_DIR / f"dk_props_{pulled_at_compact}.csv"
    latest_path = NORMALIZED_DIR / "dk_latest.csv"
    write_normalized_csv(snapshot_path, all_rows)
    write_normalized_csv(latest_path, all_rows)

    log.info(
        "=== DraftKings props ingestion run complete: %d rows (%s) ===",
        len(all_rows),
        "OK" if summary["draftkings_ok"] else "FAILED",
    )

    summary["snapshot_path"] = str(snapshot_path)
    return summary


if __name__ == "__main__":
    result = run()
    print(json.dumps(result, indent=2))
