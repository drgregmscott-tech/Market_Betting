"""
Session 6.1 — FanDuel Sportsbook Player Props Ingestion

WHAT THIS SCRIPT IS
--------------------
Pulls live player-prop odds from FanDuel Sportsbook's own internal data
feed (same undocumented-endpoint situation as ingest_dk_props.py — no
officially supported public API). Normalizes the result into the common
schema in schema_props.py.

**HONESTY NOTE — READ BEFORE RUNNING (same caveat as ingest_dk_props.py):**
Claude's own browser tool is blocked by its safety category filter from
reaching sportsbook.fanduel.com / *.sportsbook.fanduel.com directly
(confirmed this session), so this endpoint could NOT be live-tested by
Claude before being handed to the user. The URL shape below is a pattern
publicly documented by independent sportsbook-odds-scraping projects, not
FanDuel itself — treat a real run's result (success OR a 403/404) as new
information, not a confirmation either way. **Run this script and report
the real result.** If it fails, the fallback is the same one Session 2.1
documented for DK Pick6: open sportsbook.fanduel.com in a real browser,
open Developer Tools → Network tab, filter to XHR/fetch requests, navigate
to an NFL prop page, and read the real request URL and its `_ak` query
parameter directly (FanDuel's feed requires this API-key-shaped query
parameter to respond — it is NOT a login credential, it is a public,
static value embedded in FanDuel's own website JavaScript, but it is
required for a 200 response and IS the single most likely reason a
best-guess value here fails).

REGION / STATE PREFIX
----------------------
FanDuel's feed hostname is region-prefixed (e.g. `sbapi.va.sportsbook.
fanduel.com` for Virginia). `FD_REGION` below is a single named constant
for the same reason `DK_EVENT_GROUP_ID` is in ingest_dk_props.py — a wrong
guess only needs correcting in one place. "va" is used as the v1 default
since it has been the most consistently documented region prefix across
independent sources; this is a guess, not a confirmed value.

WHAT THIS SCRIPT DOES NOT DO YET
---------------------------------
- No pagination across multiple sports — v1 pulls one sport (NFL), same
  scoping reason as ingest_dk_props.py.
- No handling for FanDuel's `_ak` value going stale/rotating — unknown
  until real behavior is observed; a real research task, not a guess.

WHERE OUTPUT GOES
------------------
/data/sportsbook_props/raw/fanduel_<timestamp>.json
/data/sportsbook_props/normalized/fd_props_<timestamp>.csv
/data/sportsbook_props/normalized/fd_latest.csv  (overwritten every run)

USAGE
-----
pip install requests --break-system-packages
python ingest_fd_props.py
"""

from __future__ import annotations

import csv
import json
import logging
import re
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

# See "REGION / STATE PREFIX" note above — unverified guess.
FD_REGION = "va"
# Publicly documented as a static, non-account-specific value embedded in
# FanDuel's own site JavaScript — NOT a login credential. See module
# docstring's fallback instructions if this value has since rotated.
FD_AK = "FhMFpcPWXMeyZxOx"
FD_ENDPOINT = f"https://sbapi.{FD_REGION}.sportsbook.fanduel.com/api/content-managed-page"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json",
}

MAX_RETRIES = 2
RETRY_BACKOFF_SECONDS = 3
REQUEST_TIMEOUT_SECONDS = 15

PLAYER_PROP_CATEGORY_HINTS = {
    "touchdown": "player_touchdown",
    "td scorer": "player_touchdown",
}

# FIX (2026-09-09, real live-data finding): the real response's per-runner
# "handicap" field is 0 for these season-long prop markets — the ACTUAL
# line only appears as free text in runnerName (e.g. "Aaron Rodgers Over
# 3050.5"), confirmed against a real live pull. Relying on "handicap" alone
# (the original v1 assumption, unverified before this) silently produced
# line=0.0 for every real row. This regex extracts the real numeric line
# from that text instead; "handicap" is kept only as a fallback for a
# market type where it might genuinely carry the value.
_FD_RUNNER_LINE_PATTERN = re.compile(r"(?:Over|Under)\s+([\d.]+)", re.IGNORECASE)

# FIX (2026-09-09, real live-data finding): "player_name" was being read
# from market.get("marketType") (e.g. "REGULAR_SEASON_PROPS_-_QUARTERBACKS"
# — a category code, not a player), confirmed wrong against real data. The
# real player (or team, for a team-level market like "Regular Season Wins")
# is embedded in "marketName" text instead. These two patterns split it
# back out. Team-level markets (e.g. "Arizona Cardinals - Regular Season
# Wins 2026-27") are recognized separately so they are NOT miscounted as a
# player prop.
_FD_PLAYER_MARKET_PATTERN = re.compile(
    r"^(?P<player>.+?)\s+Regular Season\s+(?P<stat>.+?)\s+\d{4}-\d{2}$"
)
_FD_TEAM_MARKET_PATTERN = re.compile(
    r"^(?P<team>.+?)\s+-\s+Regular Season\s+(?P<stat>.+?)\s+\d{4}-\d{2}$"
)


def _parse_market_name(market_name: str) -> tuple[Optional[str], Optional[str], str]:
    """Returns (player_name, team, clean_stat_type) parsed from FanDuel's
    real marketName text. Falls back to (None, None, market_name) for any
    shape this session hasn't seen yet, so an unrecognized format is a
    visible None rather than a silently wrong guess."""
    team_match = _FD_TEAM_MARKET_PATTERN.match(market_name)
    if team_match:
        return None, team_match.group("team"), team_match.group("stat")

    player_match = _FD_PLAYER_MARKET_PATTERN.match(market_name)
    if player_match:
        player = player_match.group("player")
        # FIX (2026-09-09, real live-data finding): a league-wide market
        # like "Worst Regular Season Record 2026-27" also matches this
        # pattern (player="Worst", stat="Record") since it has no team-
        # style " - " separator either. A real player's full name always
        # has an internal space (first + last); a single bare word here is
        # a real signal this isn't actually a player market. Confirmed
        # against real data: this is the only real false-positive case
        # found in a live pull.
        if " " in player:
            return player, None, player_match.group("stat")

    return None, None, market_name


def _extract_line_from_runners(runners: list) -> Optional[float]:
    for runner in runners:
        match = _FD_RUNNER_LINE_PATTERN.search(str(runner.get("runnerName", "")))
        if match:
            return _to_float(match.group(1))
    return None


def setup_logging() -> logging.Logger:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("ingest_fd_props")
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


def fetch_fd_props() -> dict:
    return _fetch_with_retries(
        FD_ENDPOINT,
        params={"page": "CUSTOM", "customPageId": "nfl", "_ak": FD_AK},
    )


def _prop_category(market_name: str) -> str:
    lowered = (market_name or "").lower()
    for hint, category in PLAYER_PROP_CATEGORY_HINTS.items():
        if hint in lowered:
            return category
    return "player_performance"


def normalize_fd(payload: dict, pulled_at: str) -> list[NormalizedSportsbookProp]:
    """Defensive by design, same posture as ingest_dk_props.py's normalizer.
    FanDuel's documented content-managed-page shape nests events under
    attachments.events, and markets under attachments.markets (each with a
    runners list carrying the actual odds). This structure is UNCONFIRMED
    against a real live response — same caveat as ingest_dk_props.py."""
    rows: list[NormalizedSportsbookProp] = []

    attachments = payload.get("attachments")
    if not isinstance(attachments, dict):
        log.error(
            "FanDuel response missing expected top-level 'attachments' key — "
            "schema may differ from the documented pattern this script assumed. "
            "Skipping this platform for this run."
        )
        return rows

    events = attachments.get("events") or {}
    markets = attachments.get("markets") or {}

    for market_id, market in markets.items():
        try:
            market_name = market.get("marketName") or ""
            event_id = str(market.get("eventId", ""))
            event = events.get(event_id, {}) if isinstance(events, dict) else {}

            runners = market.get("runners") or []
            player_name, team_name, clean_stat_type = _parse_market_name(market_name)

            # FIX (2026-09-09, real live-data finding): the "nfl" custom
            # page returns team/game markets alongside real player props —
            # Moneyline, Spread, Total Points, Super Bowl Winner,
            # playoff-qualification markets, and team-level season-win
            # totals (e.g. "Arizona Cardinals - Regular Season Wins"),
            # none of which are a "player prop" by this track's own
            # definition (ROADMAP.md, Phase 6 header — DK/FD PLAYER props).
            # Only rows where a real player name was parsed are kept; every
            # team-level or unmatched market is skipped here rather than
            # stored as a misleading row.
            if player_name is None:
                log.info("Skipped non-player-prop market: %s", market_name)
                continue

            over_odds = None
            under_odds = None
            # Real line lives in runnerName text, not the "handicap" field
            # (see _FD_RUNNER_LINE_PATTERN fix note above) — try that first,
            # fall back to a nonzero handicap if the text parse fails.
            line_value = _extract_line_from_runners(runners)
            if line_value is None:
                for runner in runners:
                    handicap = runner.get("handicap")
                    if handicap:
                        line_value = _to_float(handicap)
                        break

            for runner in runners:
                result_type = str(runner.get("result", {}).get("type", "")).lower()

                odds_obj = runner.get("winRunnerOdds", {}) or {}
                american = odds_obj.get("americanDisplayOdds", {}).get("americanOdds")
                try:
                    american_int = int(american) if american is not None else None
                except (TypeError, ValueError):
                    american_int = None

                runner_name = str(runner.get("runnerName", "")).lower()
                if "over" in runner_name or "over" in result_type:
                    over_odds = american_int
                elif "under" in runner_name or "under" in result_type:
                    under_odds = american_int

            rows.append(
                NormalizedSportsbookProp(
                    platform="fanduel",
                    source_event_id=event_id,
                    source_market_id=str(market_id),
                    source_selection_id=str(
                        runners[0].get("selectionId") if runners else ""
                    ),
                    player_name=player_name,
                    team=team_name,
                    sport="NFL",  # v1 scope, see module docstring
                    stat_type=clean_stat_type or None,
                    prop_category=_prop_category(market_name),
                    line=line_value,
                    over_american_odds=over_odds,
                    under_american_odds=under_odds,
                    game_id=event_id,
                    game_start_time=event.get("openDate"),
                    status=event.get("inPlayStatus") or event.get("status"),
                    pulled_at=pulled_at,
                )
            )
        except Exception as exc:  # noqa: BLE001
            log.warning("Skipped one malformed FanDuel record: %s", exc)
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
    out_path = RAW_DIR / f"fanduel_{pulled_at_compact}.json"
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
        "fanduel_rows": 0,
        "fanduel_ok": False,
    }

    log.info("=== FanDuel props ingestion run starting ===")

    try:
        payload = fetch_fd_props()
        save_raw_snapshot(payload, pulled_at_compact)
        rows = normalize_fd(payload, pulled_at)
        summary["fanduel_rows"] = len(rows)
        summary["fanduel_ok"] = True
        log.info("FanDuel: %d normalized rows", len(rows))
    except Exception as exc:  # noqa: BLE001
        log.error("FanDuel ingestion failed for this run: %s", exc)
        rows = []

    snapshot_path = NORMALIZED_DIR / f"fd_props_{pulled_at_compact}.csv"
    latest_path = NORMALIZED_DIR / "fd_latest.csv"
    write_normalized_csv(snapshot_path, rows)
    write_normalized_csv(latest_path, rows)

    log.info(
        "=== FanDuel props ingestion run complete: %d rows (%s) ===",
        len(rows),
        "OK" if summary["fanduel_ok"] else "FAILED",
    )

    summary["snapshot_path"] = str(snapshot_path)
    return summary


if __name__ == "__main__":
    result = run()
    print(json.dumps(result, indent=2))
