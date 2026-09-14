"""
Session 2.18 -- Automated Real-Outcome Grading (Pick'em, NFL)

WHY THIS EXISTS -- a real, checked-live finding, not a hypothesis
------------------------------------------------------------------
Checked directly, 2026-09-11: data/pickem/clv_log.csv had 7,035 closed
flags and zero real-money outcomes ever recorded anywhere in this repo --
data/pickem/outcome_log.csv (the file outcome_tracker.py/weekly_review.py
both require) did not exist. outcome_tracker.py requires the user to
manually report every single graded leg by hand, one at a time, by
flag_id -- and in practice that has produced zero real records. Manual
entry is not closing this loop at the volume this pipeline produces
(thousands of flags), and there is no reason to expect it will going
forward.

THE REAL FIX -- reusing data this pipeline already fetches
-------------------------------------------------------------
pickem_model.py already pulls the real, final per-player stat line for
every scored NFL prop from nflverse, for a different purpose (estimating
a probability BEFORE the game). Once a flagged prop's game_start_time has
passed, the exact same real, final stat line answers whether the flag
actually won -- no user action required for the common case. This script
adds that missing loop-closer: it does not re-fetch anything new that
isn't already part of this project's existing NFL data source, and it
writes into outcome_tracker.py's existing outcome_log.csv schema (adding
one new column, graded_by, to distinguish "auto" rows from "manual"
ones) rather than inventing a second log.

Scope: NFL only, same real limitation pickem_model.py's own v1 has.
Every other sport's flags are left ungraded here -- a real, stated gap,
not a silent one -- until a future session gives those sports' own
plug-ins (MLB, EPL/soccer, CFB, tennis, NBA) the same treatment. Manual
`outcome_tracker.py --record` stays available for those in the meantime.

HOW A FLAG GETS MATCHED TO ITS REAL GAME
-------------------------------------------
clv_log.csv's own game_id is each PLATFORM's internal id (PrizePicks'
game relationship id, or Underdog's match id) -- not nflverse's, and not
directly joinable to it (checked directly: PrizePicks game_id values look
nothing like nflverse's "2026_01_NE_SEA" format). What IS reliable is
game_start_time (a real ISO timestamp from the platform) plus the
player's own identity. This script:
  1. Resolves the player to nflverse's player_id, the exact same
     normalize_name()/build_name_lookup() logic pickem_model.py already
     uses (imported directly, not reimplemented).
  2. Reads resolved_stat_key (Session 2.4's canonical stat name, already
     written to every clv_log.csv row) to know which nflverse column(s)
     -- or which computed formula -- answers this prop, again reusing
     pickem_model.py's own plug-in objects rather than re-deriving the
     stat maps.
  3. For that player's OWN real game rows this season (each carrying its
     own `week` and `team`), joins against nflverse's public schedule
     file (nflverse/nfldata's games.csv -- the same project family, a
     natural place to look, and confirmed live to carry exactly
     season/week/team/gameday) to find which one week's game happened on
     the same calendar date as the flag's game_start_time. This
     disambiguates which of the player's several real games this season
     is the one the flag was about, without ever needing to trust the
     platform's own game_id.
Verified live (this session): Drake Maye's real "Pass+Rush Yds" Under
374.5 flag (game_start_time 2026-09-09T20:20:00-04:00) matches nflverse's
real Week 1 NE @ SEA game_id "2026_01_NE_SEA" (games.csv: gameday
2026-09-09, gametime 20:20) -- Maye's real week-1 line (178 passing + 47
rushing = 225) grades as a real win for the Under side. See this session's
SESSION_LOG.md entry for the full verification record, including a second
real flag (plain Pass Yards) checked the same way.

WHAT THIS DOES NOT DO (stated gap, not a silent one)
-------------------------------------------------------
- Does not grade any sport besides NFL (see Scope above).
- Does not grade a flag whose player can't be matched to nflverse (the
  same real, honest `no_player_match`-equivalent gap pickem_model.py
  already names for scoring), or whose real game can't be found on the
  expected calendar date yet (nflverse has not posted that week's file,
  or a genuine data gap) -- these are left ungraded, not force-graded on
  stale/missing data, and are simply picked up again on a later run once
  real data exists.
- Does not overwrite or re-grade a flag_id that already has ANY recorded
  outcome (manual or auto) -- idempotent by construction: it only
  considers clv_log.csv rows whose flag_id is not already present in
  outcome_log.csv.
- Does not place bets, and does not invent a stake/payout for an auto
  grade -- these flags were never confirmed as a real placed bet, so
  `stake`/`payout`/`net_profit` stay blank, same as any
  `outcome_tracker.py --record` call made without them.

USAGE
-----
Run for real, writing to data/pickem/outcome_log.csv:
    python auto_grade_outcomes.py --run

Preview what WOULD be graded, without writing anything:
    python auto_grade_outcomes.py --run --dry-run
"""

from __future__ import annotations

import argparse
import logging
import sys
import time
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Optional

import pandas as pd
import requests
from zoneinfo import ZoneInfo

BASE_DIR = Path(__file__).resolve().parents[2]

# Reuse pickem_model.py's own name-matching and plug-in machinery directly
# -- same pattern sportsbook_props_model.py (Track 5) already established
# for reusing Track 1's NFL logic across a different pipeline.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "estimation"))
from pickem_model import build_name_lookup, normalize_name  # noqa: E402
from pickem_sport_plugins.nfl import NFL_PLUGIN  # noqa: E402
from season_utils import current_pickem_season  # noqa: E402

# Reuse outcome_tracker.py's existing log-loading/schema logic directly --
# this script writes into the SAME outcome_log.csv, not a second one. It
# deliberately does NOT call outcome_tracker.record_outcome() per flag:
# that function re-reads and re-writes the entire CSV from disk on every
# single call (fine for a human typing one `--record` at a time, but
# O(n^2) I/O at this pipeline's real volume -- thousands of flags per
# run). This script builds every graded row in memory instead and writes
# the whole batch once, in the exact same OUTCOME_LOG_COLUMNS shape.
from outcome_tracker import (  # noqa: E402
    OUTCOME_LOG_COLUMNS,
    OUTCOME_LOG_PATH,
    load_clv_log,
    load_outcome_log,
)

LOG_PATH = BASE_DIR / "logs" / "auto_grade_outcomes.log"

# nflverse/nfldata's public schedule file -- same project family as
# pickem_sport_plugins/nfl.py's own nflverse-data pull, confirmed live to
# carry season/week/team/gameday/gametime for every real NFL game back to
# 1999, updated as the real season progresses.
SCHEDULE_URL = "https://raw.githubusercontent.com/nflverse/nfldata/master/data/games.csv"
SCHEDULE_CACHE_DIR = BASE_DIR / "data" / "pickem" / "cache" / "nfl_schedule"
SCHEDULE_CACHE_PATH = SCHEDULE_CACHE_DIR / "games.csv"
SCHEDULE_REFRESH_HOURS = 6  # same order of magnitude as tennis.py's cache

# All real NFL games are played on US soil and nflverse/nfldata's schedule
# reports `gameday` as the game's own LOCAL (Eastern) calendar date -- e.g.
# a real Sunday Night Football game starting 2026-09-13 20:20 ET is filed
# under gameday 2026-09-13, even though its kickoff is 2026-09-14 00:20
# UTC. Ingested game_start_time values are NOT consistently already in
# Eastern: PrizePicks' real rows carry an explicit "-04:00"/"-05:00"
# offset (already Eastern), but Underdog's real rows are plain UTC ("Z").
# Naively taking the ISO string's own date portion silently misdates every
# UTC-reported late-window/SNF/MNF game one day early -- a real bug found
# and fixed this session (71 real flags initially fell through as
# `no_game_match` for exactly this reason). Converting to America/New_York
# explicitly, regardless of the source offset, is correct for both cases.
NFL_LOCAL_TZ = ZoneInfo("America/New_York")


def game_local_date(game_start_time: str) -> date:
    dt = datetime.fromisoformat(game_start_time)
    if dt.tzinfo is None:
        return dt.date()
    return dt.astimezone(NFL_LOCAL_TZ).date()


def setup_logging() -> logging.Logger:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("auto_grade_outcomes")
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


# ---------------------------------------------------------------------------
# Schedule fetch + cache (same stale-cache-on-failure pattern as
# pickem_sport_plugins/tennis.py's _download_matches()).
# ---------------------------------------------------------------------------
def load_schedule() -> pd.DataFrame:
    needs_fetch = True
    if SCHEDULE_CACHE_PATH.exists():
        age_hours = (time.time() - SCHEDULE_CACHE_PATH.stat().st_mtime) / 3600
        needs_fetch = age_hours >= SCHEDULE_REFRESH_HOURS

    if needs_fetch:
        try:
            resp = requests.get(SCHEDULE_URL, timeout=30)
            resp.raise_for_status()
            SCHEDULE_CACHE_DIR.mkdir(parents=True, exist_ok=True)
            SCHEDULE_CACHE_PATH.write_bytes(resp.content)
        except requests.exceptions.RequestException as exc:
            if SCHEDULE_CACHE_PATH.exists():
                log.warning(
                    "Could not refresh nflverse schedule (%s) -- using stale cache.", exc,
                )
            else:
                raise RuntimeError(
                    f"Failed to fetch nflverse schedule from {SCHEDULE_URL} and no "
                    f"cached copy exists: {exc}"
                ) from exc

    df = pd.read_csv(SCHEDULE_CACHE_PATH, low_memory=False)
    return df[["season", "week", "gameday", "home_team", "away_team"]]


# ---------------------------------------------------------------------------
# Stat resolution -- reads resolved_stat_key (already written by
# pickem_model.py's resolved_stat_key_for()) back into either a computed
# formula name or a list of nflverse columns to sum.
# ---------------------------------------------------------------------------
def resolve_stat_key(resolved_stat_key: str) -> Optional[tuple[str, list[str]]]:
    key = resolved_stat_key.strip().lower()
    if key in NFL_PLUGIN.computed_stat_types:
        return "computed", [key]
    columns = [c for c in key.split("+") if c]
    if not columns:
        return None
    return "columns", columns


def compute_actual_value(kind: str, columns: list[str], game_row: pd.Series) -> Optional[float]:
    single_row_df = pd.DataFrame([game_row])
    if kind == "computed":
        stat_key = columns[0]
        required = NFL_PLUGIN.computed_required_columns[stat_key]
        missing = [c for c in required if c not in single_row_df.columns]
        if missing:
            log.warning(
                "nflverse data missing columns required for computed stat '%s': %s",
                stat_key, missing,
            )
            return None
        return float(NFL_PLUGIN.computed_stat_types[stat_key](single_row_df).iloc[0])

    missing = [c for c in columns if c not in single_row_df.columns]
    if missing:
        log.warning("nflverse data missing expected column(s): %s", missing)
        return None
    return float(single_row_df[columns].sum(axis=1).iloc[0])


# ---------------------------------------------------------------------------
# Matching a flag to its real game row
# ---------------------------------------------------------------------------
def find_player_game_row(
    stats_df: pd.DataFrame, schedule_df: pd.DataFrame, player_id: str, flag_date: date
) -> Optional[pd.Series]:
    """Among this player's own real game rows this season (one per week
    they played), finds the one whose scheduled date matches the flag's
    real game_start_time date -- see module docstring for why this,
    rather than the platform's own game_id, is the reliable join."""
    player_rows = stats_df[stats_df["player_id"] == player_id]
    if player_rows.empty:
        return None

    flag_date_str = flag_date.isoformat()
    for _, prow in player_rows.iterrows():
        season = prow["season"]
        week = prow["week"]
        team = prow["team"]
        sched_match = schedule_df[
            (schedule_df["season"] == season)
            & (schedule_df["week"] == week)
            & ((schedule_df["home_team"] == team) | (schedule_df["away_team"] == team))
        ]
        if sched_match.empty:
            continue
        if str(sched_match.iloc[0]["gameday"]) == flag_date_str:
            return prow
    return None


def grade_result(flagged_side: str, line: float, actual_value: float) -> str:
    if actual_value == line:
        return "push"
    side = (flagged_side or "").strip().lower()
    if side == "over":
        return "win" if actual_value > line else "loss"
    if side == "under":
        return "win" if actual_value < line else "loss"
    raise ValueError(f"Unrecognized flagged_side: {flagged_side!r}")


# ---------------------------------------------------------------------------
# Main run
# ---------------------------------------------------------------------------
def find_gradable_candidates(clv_df: pd.DataFrame, already_graded: set[str]) -> pd.DataFrame:
    now = datetime.now(timezone.utc)

    def is_past(game_start_time: object) -> bool:
        if not isinstance(game_start_time, str) or not game_start_time.strip():
            return False
        try:
            dt = datetime.fromisoformat(game_start_time)
        except ValueError:
            return False
        if dt.tzinfo is None:
            return True  # no timezone info -- trust status=="closed" alone
        return dt.astimezone(timezone.utc) < now

    is_nfl = clv_df["sport"].fillna("").str.strip().str.lower().isin(NFL_PLUGIN.sport_labels)
    is_closed = clv_df["status"] == "closed"
    has_stat_key = clv_df["resolved_stat_key"].notna()
    not_graded = ~clv_df["flag_id"].isin(already_graded)
    is_past_mask = clv_df["game_start_time"].apply(is_past)

    return clv_df.loc[is_nfl & is_closed & has_stat_key & not_graded & is_past_mask]


def _build_outcome_row(flag_row: pd.Series, result: str, actual_value: float, reported_at: str) -> dict:
    """Builds one outcome_log.csv row directly from the clv_log.csv row
    that produced it -- this IS the context row (unlike a manually
    reported outcome, which has to look flag_id back up), so every
    context field is populated from real, already-in-hand data, not a
    fresh lookup. Same column shape as outcome_tracker.record_outcome()'s
    new_row, marked graded_by='auto'."""
    return {
        "outcome_id": f"{flag_row['flag_id']}|{reported_at}",
        "flag_id": flag_row["flag_id"],
        "reported_at": reported_at,
        "platform": flag_row.get("platform"),
        "player_name": flag_row.get("player_name"),
        "team": None,  # clv_log.csv does not carry a team column
        "sport": flag_row.get("sport"),
        "stat_type": flag_row.get("stat_type"),
        "resolved_stat_key": flag_row.get("resolved_stat_key"),
        "flagged_side": flag_row.get("flagged_side"),
        "first_flagged_line": flag_row.get("first_flagged_line"),
        "first_flagged_model_prob": flag_row.get("first_flagged_model_prob"),
        "first_flagged_implied_prob": flag_row.get("first_flagged_implied_prob"),
        "first_flagged_edge": flag_row.get("first_flagged_edge"),
        "clv_edge_at_close": flag_row.get("clv_edge_at_close"),
        "consensus_available": flag_row.get("consensus_available"),
        "result": result,
        "actual_value": actual_value,
        "entry_type": None,
        "stake": None,
        "payout": None,
        "net_profit": None,
        "notes": "Auto-graded from nflverse weekly stats (Session 2.18).",
        "context_lookup_status": "ok",
        "graded_by": "auto",
    }


def run(dry_run: bool = False) -> dict:
    clv_df = load_clv_log()
    outcome_df = load_outcome_log()
    already_graded = set(outcome_df["flag_id"])

    candidates = find_gradable_candidates(clv_df, already_graded)
    log.info(
        "%d real closed NFL flag(s) with a resolved stat key are not yet graded; "
        "checking each against nflverse's real, published results.",
        len(candidates),
    )

    schedule_df = load_schedule()
    stats_cache: dict[int, pd.DataFrame] = {}
    lookup_cache: dict[int, dict[str, str]] = {}

    graded = 0
    no_player_match = 0
    no_game_match = 0
    no_stat_value = 0
    bad_stat_key = 0
    new_rows: list[dict] = []

    for _, row in candidates.iterrows():
        flag_date = game_local_date(row["game_start_time"])
        season = current_pickem_season(flag_date)

        if season not in stats_cache:
            stats_cache[season] = NFL_PLUGIN.fetch_stats(season)
            lookup_cache[season] = build_name_lookup(stats_cache[season])
        stats_df = stats_cache[season]
        name_lookup = lookup_cache[season]

        player_id = name_lookup.get(normalize_name(row["player_name"]))
        if player_id is None:
            no_player_match += 1
            continue

        parsed = resolve_stat_key(row["resolved_stat_key"])
        if parsed is None:
            bad_stat_key += 1
            continue
        kind, columns = parsed

        game_row = find_player_game_row(stats_df, schedule_df, player_id, flag_date)
        if game_row is None:
            no_game_match += 1
            continue

        actual_value = compute_actual_value(kind, columns, game_row)
        if actual_value is None:
            no_stat_value += 1
            continue

        result = grade_result(row["flagged_side"], row["first_flagged_line"], actual_value)

        if dry_run:
            log.info(
                "[dry-run] flag_id=%s player=%s stat=%s line=%s side=%s actual=%s -> %s",
                row["flag_id"], row["player_name"], row["resolved_stat_key"],
                row["first_flagged_line"], row["flagged_side"], actual_value, result,
            )
        else:
            reported_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
            new_rows.append(_build_outcome_row(row, result, actual_value, reported_at))
        graded += 1

    if new_rows:
        combined = pd.concat([outcome_df, pd.DataFrame(new_rows)], ignore_index=True)
        combined = combined[OUTCOME_LOG_COLUMNS]
        OUTCOME_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
        combined.to_csv(OUTCOME_LOG_PATH, index=False)
        log.info("Wrote %d new auto-graded row(s) to %s.", len(new_rows), OUTCOME_LOG_PATH)

    summary = {
        "candidates": len(candidates),
        "graded": graded,
        "no_player_match": no_player_match,
        "no_game_match": no_game_match,
        "no_stat_value": no_stat_value,
        "bad_stat_key": bad_stat_key,
        "dry_run": dry_run,
    }
    log.info("Auto-grading run complete: %s", summary)
    return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", action="store_true", help="Run the auto-grading pass.")
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Compute and log what WOULD be graded without writing to outcome_log.csv.",
    )
    args = parser.parse_args()

    if not args.run:
        parser.error("Specify --run (optionally with --dry-run).")

    print(run(dry_run=args.dry_run))
