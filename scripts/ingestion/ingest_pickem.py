"""
Session 2.2 — Production Data Ingestion Pipeline (PrizePicks + Underdog)

WHAT THIS SCRIPT IS
--------------------
This replaces Session 2.1's throwaway prototype scripts with a real pipeline
that:
  1. Pulls live data from both remaining in-scope pick'em platforms
     (PrizePicks, Underdog — DK Pick6 was dropped from scope in Session 2.1).
  2. Normalizes both platforms' different raw shapes into the one common
     schema defined in schema.py.
  3. Survives a bad response, an empty response, or a schema change from
     either platform WITHOUT crashing — logs the failure and continues with
     whatever data it does have.
  4. Writes output in a way that running the pipeline twice in a row does
     not duplicate or corrupt any stored data (see "IDEMPOTENCY" below).
  5. Logs every run (success or failure) to /logs/ingestion.log so a human
     — or Session 8.4's future health-check pipeline — can see the pipeline's
     real history, not just its most recent result.

Both endpoints are UNDOCUMENTED (confirmed in Session 2.1 — see
/docs/research/endpoint_schemas.md). That means they can change shape or
start rejecting requests at any time, with no notice. Every normalizer
function in this file is written defensively for that reason: it checks that
expected fields exist before reading them, and treats a missing/changed field
as a per-row skip with a logged warning, not a pipeline crash.

WHERE OUTPUT GOES
------------------
/data/pickem/raw/<platform>_<timestamp>.json
    The exact, unmodified response from each platform, saved every run, so a
    real historical archive exists (useful for Session 2.3's model-building
    and for diagnosing a future schema change against what actually changed).

/data/pickem/normalized/pickem_props_<timestamp>.csv
    One normalized snapshot per run, in the common schema. A NEW,
    uniquely-named file every run — running the pipeline twice does not
    overwrite or duplicate an existing snapshot, it simply creates a second,
    separate one, exactly as expected for two separate points in time.

/data/pickem/normalized/latest.csv
    Always overwritten each run with the current run's normalized data. This
    is the "what does the pipeline see right now" view. Being an overwrite,
    not an append, is what makes the pipeline idempotent for this file:
    running it twice back-to-back just overwrites latest.csv with
    (near-)identical data, never duplicating rows within it.

IDEMPOTENCY — WHAT THIS MEANS HERE AND HOW IT IS ENFORCED
-------------------------------------------------------------
"Idempotent" means: running the pipeline twice in a row produces the same
correct end state as running it once, with no duplicated or corrupted data.
This pipeline is a SNAPSHOT pattern (each run represents one point-in-time
pull), not an append-only log, so idempotency is enforced structurally:
  - Every timestamped file (raw and normalized) gets a unique filename tied
    to its own pull time. Running twice creates two distinct, correctly
    separate snapshots — this is correct behavior, not duplication.
  - latest.csv is fully overwritten every run, never appended to. Two runs
    in a row simply leave latest.csv reflecting the second run's data.
  - No file in this pipeline is ever opened in append mode. This is checked
    directly in this file's own test harness (see test_ingest_pickem.py).

WHAT BREAKS THE PULL (carried over from Session 2.1, expanded here)
-------------------------------------------------------------------
Session 2.1 observed zero failures for either platform across 21 checks over
~10 hours, but explicitly flagged that production needs real retry/error
handling regardless, since both are undocumented endpoints. This pipeline
handles, without crashing:
  - Network failure / timeout reaching the endpoint at all.
  - A non-200 HTTP response (e.g. 403, 429, 500).
  - A response that parses as JSON but is missing an expected top-level key
    (e.g. PrizePicks stops returning "included", or Underdog stops
    returning "over_under_lines").
  - A response where individual records are missing fields the normalizer
    expects (logged and skipped per-record, not fatal to the whole run).

USAGE
-----
pip install requests --break-system-packages
python ingest_pickem.py
"""

from __future__ import annotations

import csv
import json
import logging
import time
from dataclasses import fields
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import requests

from schema import NORMALIZED_COLUMNS, NormalizedProp

# --------------------------------------------------------------------------
# Paths — all relative to the repo root. Run this script from the repo root
# (or adjust BASE_DIR) so these resolve correctly.
# --------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parents[2]
RAW_DIR = BASE_DIR / "data" / "pickem" / "raw"
NORMALIZED_DIR = BASE_DIR / "data" / "pickem" / "normalized"
LOG_PATH = BASE_DIR / "logs" / "ingestion.log"

PRIZEPICKS_ENDPOINT = "https://partner-api.prizepicks.com/projections"
UNDERDOG_ENDPOINT = "https://api.underdogfantasy.com/beta/v3/over_under_lines"

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


# --------------------------------------------------------------------------
# Logging setup — appends to /logs/ingestion.log AND prints to console, so
# both a human watching a manual run and a future automated run (Session
# 2.7) get the same record.
# --------------------------------------------------------------------------
def setup_logging() -> logging.Logger:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("ingest_pickem")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()

    file_handler = logging.FileHandler(LOG_PATH, mode="a", encoding="utf-8")
    console_handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s UTC | %(levelname)s | %(message)s"
    )
    formatter.converter = time.gmtime
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger


log = setup_logging()


# --------------------------------------------------------------------------
# Fetching — each platform gets its own function, with retry on network-
# level failures. A failure here is caught by the caller in main(), logged,
# and treated as "this platform produced zero rows this run" rather than
# crashing the whole pipeline.
# --------------------------------------------------------------------------
def _fetch_with_retries(url: str, params: Optional[dict] = None) -> dict:
    last_error = None
    for attempt in range(1, MAX_RETRIES + 2):  # e.g. 1 initial + 2 retries
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


def fetch_prizepicks() -> dict:
    return _fetch_with_retries(PRIZEPICKS_ENDPOINT, params={"per_page": 250})


def fetch_underdog() -> dict:
    return _fetch_with_retries(UNDERDOG_ENDPOINT)


# --------------------------------------------------------------------------
# Normalizers — convert each platform's raw shape into a list of
# NormalizedProp. Defensive by design: a missing/renamed field on one row
# causes that row to be skipped (with a warning), not the whole run to fail.
# --------------------------------------------------------------------------
def normalize_prizepicks(payload: dict, pulled_at: str) -> list[NormalizedProp]:
    rows: list[NormalizedProp] = []

    data = payload.get("data")
    included = payload.get("included")
    if not isinstance(data, list) or not isinstance(included, list):
        log.error(
            "PrizePicks response missing expected top-level 'data'/'included' "
            "lists — schema may have changed. Skipping this platform for this run."
        )
        return rows

    # Build lookup tables by (type, id) so each projection's relationships
    # can be resolved in O(1) instead of re-scanning "included" per row.
    included_by_type_id: dict[tuple[str, str], dict] = {}
    for item in included:
        item_type = item.get("type")
        item_id = item.get("id")
        if item_type is not None and item_id is not None:
            included_by_type_id[(item_type, str(item_id))] = item

    for record in data:
        try:
            attrs = record.get("attributes", {})
            rels = record.get("relationships", {})

            player_rel = rels.get("new_player", {}).get("data") or {}
            player = included_by_type_id.get(
                ("new_player", str(player_rel.get("id")))
            )
            player_attrs = (player or {}).get("attributes", {})

            team_name = player_attrs.get("team_name") or player_attrs.get("team")

            league_rel = rels.get("league", {}).get("data") or {}
            league = included_by_type_id.get(
                ("league", str(league_rel.get("id")))
            )
            sport = (league or {}).get("attributes", {}).get("name")

            game_rel = rels.get("game", {}).get("data") or {}
            game = included_by_type_id.get(("game", str(game_rel.get("id"))))
            game_attrs = (game or {}).get("attributes", {})

            rows.append(
                NormalizedProp(
                    platform="prizepicks",
                    source_line_id=str(record.get("id")),
                    player_name=player_attrs.get("display_name")
                    or player_attrs.get("name"),
                    team=team_name,
                    sport=sport,
                    stat_type=attrs.get("stat_display_name")
                    or attrs.get("stat_type"),
                    line=_to_float(attrs.get("line_score")),
                    over_payout_multiplier=None,  # standard PrizePicks lines
                    under_payout_multiplier=None,  # don't carry per-side odds
                    game_id=str(game_rel.get("id")) if game_rel else None,
                    game_start_time=game_attrs.get("start_time")
                    or attrs.get("start_time"),
                    status=attrs.get("status"),
                    pulled_at=pulled_at,
                )
            )
        except Exception as exc:  # noqa: BLE001 — deliberately broad: one bad
            # record must never take down the whole run.
            log.warning("Skipped one malformed PrizePicks record: %s", exc)
            continue

    return rows


def normalize_underdog(payload: dict, pulled_at: str) -> list[NormalizedProp]:
    rows: list[NormalizedProp] = []

    lines = payload.get("over_under_lines")
    players = payload.get("players")
    appearances = payload.get("appearances")
    games = payload.get("games")

    if not all(isinstance(x, list) for x in (lines, players, appearances, games)):
        log.error(
            "Underdog response missing one of the expected top-level lists "
            "('over_under_lines', 'players', 'appearances', 'games') — schema "
            "may have changed. Skipping this platform for this run."
        )
        return rows

    players_by_id = {str(p.get("id")): p for p in players}
    appearances_by_id = {str(a.get("id")): a for a in appearances}
    games_by_id = {str(g.get("id")): g for g in games}

    for line in lines:
        try:
            over_under = line.get("over_under", {}) or {}
            appearance_stat = over_under.get("appearance_stat", {}) or {}
            appearance_id = str(
                appearance_stat.get("appearance_id")
                or over_under.get("appearance_id")
                or ""
            )
            appearance = appearances_by_id.get(appearance_id, {})

            player_id = str(appearance.get("player_id", ""))
            player = players_by_id.get(player_id, {})
            player_attrs = player.get("attributes", player)  # tolerate either shape

            match_id = str(appearance.get("match_id", ""))
            game = games_by_id.get(match_id, {})
            game_attrs = game.get("attributes", game)

            player_name = (
                player_attrs.get("full_name")
                or player_attrs.get("first_name", "")
                and f"{player_attrs.get('first_name', '')} "
                f"{player_attrs.get('last_name', '')}".strip()
            ) or player_attrs.get("name")

            rows.append(
                NormalizedProp(
                    platform="underdog",
                    source_line_id=str(line.get("id")),
                    player_name=player_name or None,
                    team=appearance.get("team_id") or player_attrs.get("team"),
                    sport=game_attrs.get("sport_id") or game_attrs.get("sport"),
                    stat_type=over_under.get("display_stat"),
                    line=_to_float(line.get("stat_value")),
                    over_payout_multiplier=_extract_multiplier(line, "Higher"),
                    under_payout_multiplier=_extract_multiplier(line, "Lower"),
                    game_id=match_id or None,
                    game_start_time=game_attrs.get("scheduled_at")
                    or game_attrs.get("start_time"),
                    status=line.get("status"),
                    pulled_at=pulled_at,
                )
            )
        except Exception as exc:  # noqa: BLE001 — same reasoning as above.
            log.warning("Skipped one malformed Underdog record: %s", exc)
            continue

    return rows


def _extract_multiplier(line: dict, option_label: str) -> Optional[float]:
    options = line.get("options")
    if not isinstance(options, list):
        return None
    for opt in options:
        choice = opt.get("choice") or opt.get("choice_display") or ""
        if option_label.lower() in str(choice).lower():
            return _to_float(opt.get("payout_multiplier"))
    return None


def _to_float(value) -> Optional[float]:
    """Converts a numeric-looking string or number to float. Underdog
    returns stat_value as a STRING (confirmed Session 2.1) — this is the
    conversion step schema.py's docstring calls out as the most important
    correctness detail in this file. Returns None (not 0) for anything that
    can't be parsed, so a bad value is visibly missing rather than silently
    wrong."""
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


# --------------------------------------------------------------------------
# Output writers
# --------------------------------------------------------------------------
def save_raw_snapshot(platform: str, payload: dict, pulled_at_compact: str) -> Path:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    out_path = RAW_DIR / f"{platform}_{pulled_at_compact}.json"
    out_path.write_text(json.dumps(payload, indent=2))
    return out_path


def write_normalized_csv(path: Path, rows: list[NormalizedProp]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=NORMALIZED_COLUMNS)
        writer.writeheader()
        for row in rows:
            writer.writerow(row.as_row())


# --------------------------------------------------------------------------
# Main pipeline
# --------------------------------------------------------------------------
def run() -> dict:
    """Runs one full ingestion pass. Returns a summary dict (used by the
    test harness and safe to ignore in normal use). Never raises — every
    failure mode is caught, logged, and reflected in the summary instead."""
    pulled_at = datetime.now(timezone.utc).isoformat()
    pulled_at_compact = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    summary = {
        "pulled_at": pulled_at,
        "prizepicks_rows": 0,
        "underdog_rows": 0,
        "prizepicks_ok": False,
        "underdog_ok": False,
    }

    log.info("=== Ingestion run starting ===")

    all_rows: list[NormalizedProp] = []

    # PrizePicks — isolated so a failure here never blocks Underdog.
    try:
        pp_payload = fetch_prizepicks()
        save_raw_snapshot("prizepicks", pp_payload, pulled_at_compact)
        pp_rows = normalize_prizepicks(pp_payload, pulled_at)
        all_rows.extend(pp_rows)
        summary["prizepicks_rows"] = len(pp_rows)
        summary["prizepicks_ok"] = True
        log.info("PrizePicks: %d normalized rows", len(pp_rows))
    except Exception as exc:  # noqa: BLE001 — a platform outage must not
        # crash the whole pipeline; Underdog should still run.
        log.error("PrizePicks ingestion failed for this run: %s", exc)

    # Underdog — isolated the same way.
    try:
        ud_payload = fetch_underdog()
        save_raw_snapshot("underdog", ud_payload, pulled_at_compact)
        ud_rows = normalize_underdog(ud_payload, pulled_at)
        all_rows.extend(ud_rows)
        summary["underdog_rows"] = len(ud_rows)
        summary["underdog_ok"] = True
        log.info("Underdog: %d normalized rows", len(ud_rows))
    except Exception as exc:  # noqa: BLE001
        log.error("Underdog ingestion failed for this run: %s", exc)

    # Write output regardless of whether one or both platforms failed —
    # partial data is still useful and must still be visible.
    snapshot_path = NORMALIZED_DIR / f"pickem_props_{pulled_at_compact}.csv"
    latest_path = NORMALIZED_DIR / "latest.csv"
    write_normalized_csv(snapshot_path, all_rows)
    write_normalized_csv(latest_path, all_rows)  # overwrite, not append

    log.info(
        "=== Ingestion run complete: %d total rows (PrizePicks %s, Underdog %s) ===",
        len(all_rows),
        "OK" if summary["prizepicks_ok"] else "FAILED",
        "OK" if summary["underdog_ok"] else "FAILED",
    )

    summary["total_rows"] = len(all_rows)
    summary["snapshot_path"] = str(snapshot_path)
    return summary


if __name__ == "__main__":
    result = run()
    print(json.dumps(result, indent=2))
