"""
Session 2.18 -- Automated Real-Outcome Grading (Pick'em, NFL)
Session 2.26 -- Generalized to a per-sport GradingAdapter, MLB added

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
every scored prop, for a different purpose (estimating a probability
BEFORE the game). Once a flagged prop's game_start_time has passed, the
exact same real, final stat line answers whether the flag actually won --
no user action required for the common case. This script adds that
missing loop-closer, writing into outcome_tracker.py's existing
outcome_log.csv schema (adding one new column, graded_by, to distinguish
"auto" rows from "manual" ones) rather than inventing a second log.

SESSION 2.26 -- WHY THIS GOT GENERALIZED, NOT JUST COPY-PASTED PER SPORT
--------------------------------------------------------------------------
Session 2.18 was NFL-only by explicit, stated scope. The user found live
(2026-09-15) that 9,801 of 9,810 open Pick'em flags on the frontend --
MLB, soccer, tennis, NBA combined -- have never been checked against a
real outcome, because only NFL had this loop closed. Four more sports
(MLB this session; soccer/CFB/tennis in Sessions 2.27-2.29) need the same
treatment. Rather than copy this whole file per sport (the original plan,
matching how the *estimation* plug-ins were each their own session), this
session extracts the one real per-sport variable -- HOW to find a given
player's real game row for a given calendar date -- into a small
GradingAdapter per sport, registered in ADAPTERS below. Everything else
(candidate selection, stat resolution via resolved_stat_key, grading,
writing outcome_log.csv) is already sport-agnostic, because it already
reused pickem_model.py's own sport-agnostic build_name_lookup() /
resolved_stat_key_for() logic even in the NFL-only version -- the only
thing that was actually hardcoded to NFL was the schedule-join matching
step and the direct NFL_PLUGIN references. NFL's own adapter reproduces
its exact pre-Session-2.26 behavior unchanged (same schedule-join logic,
just moved into NFL_ADAPTER.find_game_row); this was checked by diffing a
dry run before/after the refactor -- see this session's SESSION_LOG.md
entry.

WHY MLB DID NOT NEED NFL'S SCHEDULE-FILE JOIN AT ALL
--------------------------------------------------------
NFL's clv_log.csv game_id is PrizePicks/Underdog's own internal id, not
directly joinable to nflverse's game ids -- Session 2.18 worked around
this by joining on (player's own team + week) against nflverse/nfldata's
public schedule file to recover the real calendar date. MLB Stats API's
own gameLog response already reports each game's real calendar date
directly on every split (`split["date"]`) -- Session 2.26 added a
`game_date` column to pickem_sport_plugins/mlb.py's fetch_stats() output
to carry it through (a small, additive change; does not affect
sort_key-based pre-game estimation logic, which is unchanged). MLB's
adapter therefore matches a flag straight to its real game_date, with no
external schedule file and no extra API calls.

SESSION 2.27 -- SOCCER/EPL ADDED, ONE SHARED ADAPTER FOR BOTH
-------------------------------------------------------------------
Confirming Session 2.26's generalization actually paid off: adding
soccer/EPL took one new column per plug-in (`game_date_utc`, threaded
through from data both sources already return -- ESPN's scoreboard
`date`, FPL's `kickoff_time`) and one new find_game_row function in this
file, not a near-duplicate script. Soccer (ESPN, 5 leagues) and EPL (FPL)
share one function, find_soccer_or_epl_game_row, because both real
sources report only a raw UTC instant rather than an already-localized
civil date -- see that function's own docstring for why this reuses the
NFL/MLB pipeline's existing Eastern-conversion helper rather than adding
a third per-league timezone table.

WHAT THIS DOES NOT DO (stated gap, not a silent one)
-------------------------------------------------------
- Grades only sports with a registered adapter in ADAPTERS below: NFL,
  MLB, soccer/EPL, as of this session. CFB and tennis are explicitly left
  ungraded until Sessions 2.28-2.29 register their own adapters -- each of
  those sessions' whole job should be "add one GradingAdapter and its
  find_game_row logic," not touching this file's shared logic again.
  NBA has an estimation plug-in but is not scheduled for grading yet
  (ROADMAP.md Session 2.26 card: NBA's season hasn't started, nothing
  real to validate against right now). Manual `outcome_tracker.py
  --record` stays available for every ungraded sport in the meantime.
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
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Callable, Optional

import pandas as pd
import requests
from zoneinfo import ZoneInfo

BASE_DIR = Path(__file__).resolve().parents[2]

# Reuse pickem_model.py's own name-matching and plug-in machinery directly
# -- same pattern sportsbook_props_model.py (Track 5) already established
# for reusing Track 1's NFL logic across a different pipeline.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "estimation"))
from pickem_model import build_name_lookup, normalize_name  # noqa: E402
from pickem_sport_plugins import SportPlugin  # noqa: E402
from pickem_sport_plugins.epl import EPL_PLUGIN  # noqa: E402
from pickem_sport_plugins.mlb import MLB_PLUGIN  # noqa: E402
from pickem_sport_plugins.nfl import NFL_PLUGIN  # noqa: E402
from pickem_sport_plugins.soccer import SOCCER_PLUGIN  # noqa: E402
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
# 1999, updated as the real season progresses. Only NFL's adapter uses
# this -- MLB's doesn't need a schedule file at all (see module docstring).
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
# and fixed in Session 2.18 (71 real flags initially fell through as
# `no_game_match` for exactly this reason). Converting to America/New_York
# explicitly, regardless of the source offset, is correct for both cases.
# MLB games are also played on US soil; the same Eastern-conversion rule
# is applied uniformly to every sport below rather than assuming it's an
# NFL-only quirk -- there is no reason MLB's own Underdog/PrizePicks rows
# would behave differently.
LOCAL_TZ = ZoneInfo("America/New_York")


def game_local_date(game_start_time: str) -> date:
    dt = datetime.fromisoformat(game_start_time)
    if dt.tzinfo is None:
        return dt.date()
    return dt.astimezone(LOCAL_TZ).date()


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
# NFL schedule fetch + cache (same stale-cache-on-failure pattern as
# pickem_sport_plugins/tennis.py's _download_matches()). Only NFL_ADAPTER
# calls this -- it is not part of the generic per-sport contract.
# ---------------------------------------------------------------------------
def load_nfl_schedule() -> pd.DataFrame:
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


def find_nfl_game_row(
    stats_df: pd.DataFrame, schedule_df: pd.DataFrame, player_id: str, flag_date: date
) -> Optional[pd.Series]:
    """Among this player's own real game rows this season (one per week
    they played), finds the one whose scheduled date matches the flag's
    real game_start_time date -- the platform's own game_id is not
    reliably joinable to nflverse's, so date is the real join key (see
    module docstring)."""
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


def find_mlb_game_row(
    stats_df: pd.DataFrame, context: object, player_id: str, flag_date: date
) -> Optional[pd.Series]:
    """MLB Stats API's gameLog already reports each game's real calendar
    date directly (mlb.py's fetch_stats() carries it through as
    `game_date`) -- no schedule-file join needed, `context` is unused."""
    player_rows = stats_df[stats_df["player_id"] == player_id]
    if player_rows.empty or "game_date" not in player_rows.columns:
        return None
    flag_date_str = flag_date.isoformat()
    match = player_rows[player_rows["game_date"] == flag_date_str]
    if match.empty:
        return None
    return match.iloc[0]


def find_soccer_or_epl_game_row(
    stats_df: pd.DataFrame, context: object, player_id: str, flag_date: date
) -> Optional[pd.Series]:
    """Session 2.27: unlike MLB Stats API's gameLog (already a local civil
    date) or nflverse's schedule file (already the game's own Eastern
    `gameday`), neither ESPN's soccer scoreboard `date` nor FPL's
    `kickoff_time` carries a "local calendar date" concept at all -- both
    are a raw UTC instant on a match played somewhere in Europe/North
    America, not a date the source itself has already localized (see
    soccer.py/epl.py's own docstrings for the real field values). Rather
    than invent a second, competition-specific "local" timezone per league
    (a real can of worms -- La Liga is Madrid time, MLS is US Eastern/
    Central/Pacific depending on the home team, EPL is UK time), this
    reuses the exact same UTC-to-America/New_York conversion
    (`game_local_date`) already applied to `flag_date` on the other side
    of this join. Checked live (2026-09-15): every real soccer/EPL
    kickoff time falls within 11:00-22:00 UK/CET local, i.e. comfortably
    after 04:00 UTC, so converting to Eastern (UTC-4/-5) never rolls the
    calendar date backward across a match's own kickoff -- this join is
    safe in practice, not just consistent in theory. `context` is unused,
    same as MLB's adapter."""
    player_rows = stats_df[stats_df["player_id"] == player_id]
    if player_rows.empty or "game_date_utc" not in player_rows.columns:
        return None
    flag_date_str = flag_date.isoformat()
    for _, prow in player_rows.iterrows():
        raw = prow.get("game_date_utc")
        if not isinstance(raw, str) or not raw.strip():
            continue
        try:
            if game_local_date(raw).isoformat() == flag_date_str:
                return prow
        except ValueError:
            continue
    return None


@dataclass
class GradingAdapter:
    """The one real per-sport variable in auto-grading: how to find a
    given player's real game row for a given calendar date. Everything
    else (candidate selection, stat resolution, grading, writing the
    outcome log) is already sport-agnostic -- see module docstring."""

    plugin: SportPlugin
    # Called once per run, before any per-season stats fetch -- e.g. NFL's
    # schedule file. Returns whatever `find_game_row` needs as `context`;
    # sports with no such dependency (MLB) just return None.
    load_context: Callable[[], object]
    find_game_row: Callable[[pd.DataFrame, object, str, date], Optional[pd.Series]]


NFL_ADAPTER = GradingAdapter(
    plugin=NFL_PLUGIN, load_context=load_nfl_schedule, find_game_row=find_nfl_game_row
)
MLB_ADAPTER = GradingAdapter(
    plugin=MLB_PLUGIN, load_context=lambda: None, find_game_row=find_mlb_game_row
)
SOCCER_ADAPTER = GradingAdapter(
    plugin=SOCCER_PLUGIN, load_context=lambda: None, find_game_row=find_soccer_or_epl_game_row
)
EPL_ADAPTER = GradingAdapter(
    plugin=EPL_PLUGIN, load_context=lambda: None, find_game_row=find_soccer_or_epl_game_row
)

# Session 2.28-2.29 each add one adapter here (CFB, tennis) -- that should
# be the only change this file needs per new sport, per the module
# docstring's whole point in generalizing this.
ADAPTERS: list[GradingAdapter] = [NFL_ADAPTER, MLB_ADAPTER, SOCCER_ADAPTER, EPL_ADAPTER]


# ---------------------------------------------------------------------------
# Stat resolution -- reads resolved_stat_key (already written by
# pickem_model.py's resolved_stat_key_for()) back into either a computed
# formula name or a list of that plugin's stats-source columns to sum.
# Sport-agnostic: reads whichever plugin is passed in.
# ---------------------------------------------------------------------------
def resolve_stat_key(plugin: SportPlugin, resolved_stat_key: str) -> Optional[tuple[str, list[str]]]:
    """Session 2.26 fix: resolved_stat_key_for() (pickem_model.py) writes
    real stats-source column names verbatim, case included -- NFL's own
    nflverse columns happen to already be lowercase (passing_yards, ...),
    which is why lowercasing this string before using it as a column name
    was silently harmless for NFL-only. MLB's real MLB Stats API columns
    are camelCase (baseOnBalls, homeRuns, ...); lowercasing broke the
    lookup for every MLB walks/home-runs-keyed flag until this fix (caught
    live during this session's dry run: 'mlb data missing expected
    column(s): [\'baseonballs\']'). computed_stat_types keys ARE always
    lowercase (resolve_stat_spec() lowercases stat_type before generating
    them), so only that branch still compares lowercased."""
    raw = resolved_stat_key.strip()
    if raw.lower() in plugin.computed_stat_types:
        return "computed", [raw.lower()]
    columns = [c for c in raw.split("+") if c]
    if not columns:
        return None
    return "columns", columns


def compute_actual_value(
    plugin: SportPlugin, kind: str, columns: list[str], game_row: pd.Series
) -> Optional[float]:
    single_row_df = pd.DataFrame([game_row])
    if kind == "computed":
        stat_key = columns[0]
        required = plugin.computed_required_columns[stat_key]
        missing = [c for c in required if c not in single_row_df.columns]
        if missing:
            log.warning(
                "%s data missing columns required for computed stat '%s': %s",
                plugin.name, stat_key, missing,
            )
            return None
        return float(plugin.computed_stat_types[stat_key](single_row_df).iloc[0])

    missing = [c for c in columns if c not in single_row_df.columns]
    if missing:
        log.warning("%s data missing expected column(s): %s", plugin.name, missing)
        return None
    return float(single_row_df[columns].sum(axis=1).iloc[0])


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
def find_gradable_candidates(
    clv_df: pd.DataFrame, sport_labels: frozenset[str], already_graded: set[str]
) -> pd.DataFrame:
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

    is_sport = clv_df["sport"].fillna("").str.strip().str.lower().isin(sport_labels)
    is_closed = clv_df["status"] == "closed"
    has_stat_key = clv_df["resolved_stat_key"].notna()
    not_graded = ~clv_df["flag_id"].isin(already_graded)
    is_past_mask = clv_df["game_start_time"].apply(is_past)

    return clv_df.loc[is_sport & is_closed & has_stat_key & not_graded & is_past_mask]


def _build_outcome_row(
    flag_row: pd.Series, result: str, actual_value: float, reported_at: str, source_note: str
) -> dict:
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
        "notes": source_note,
        "context_lookup_status": "ok",
        "graded_by": "auto",
    }


def _run_adapter(
    adapter: GradingAdapter,
    clv_df: pd.DataFrame,
    already_graded: set[str],
    dry_run: bool,
) -> tuple[list[dict], dict]:
    plugin = adapter.plugin
    candidates = find_gradable_candidates(clv_df, plugin.sport_labels, already_graded)
    log.info(
        "%s: %d real closed flag(s) with a resolved stat key are not yet graded; "
        "checking each against %s's real, published results.",
        plugin.name, len(candidates), plugin.name,
    )

    context = adapter.load_context()
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
            stats_cache[season] = plugin.fetch_stats(season)
            lookup_cache[season] = build_name_lookup(stats_cache[season])
        stats_df = stats_cache[season]
        name_lookup = lookup_cache[season]

        player_id = name_lookup.get(normalize_name(row["player_name"]))
        if player_id is None:
            no_player_match += 1
            continue

        parsed = resolve_stat_key(plugin, row["resolved_stat_key"])
        if parsed is None:
            bad_stat_key += 1
            continue
        kind, columns = parsed

        game_row = adapter.find_game_row(stats_df, context, player_id, flag_date)
        if game_row is None:
            no_game_match += 1
            continue

        actual_value = compute_actual_value(plugin, kind, columns, game_row)
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
            new_rows.append(_build_outcome_row(
                row, result, actual_value, reported_at,
                f"Auto-graded from {plugin.name}'s real stats (Session 2.18/2.26).",
            ))
        graded += 1

    summary = {
        "sport": plugin.name,
        "candidates": len(candidates),
        "graded": graded,
        "no_player_match": no_player_match,
        "no_game_match": no_game_match,
        "no_stat_value": no_stat_value,
        "bad_stat_key": bad_stat_key,
    }
    return new_rows, summary


def run(dry_run: bool = False) -> dict:
    clv_df = load_clv_log()
    outcome_df = load_outcome_log()
    already_graded = set(outcome_df["flag_id"])

    all_new_rows: list[dict] = []
    per_sport_summary: list[dict] = []

    for adapter in ADAPTERS:
        new_rows, summary = _run_adapter(adapter, clv_df, already_graded, dry_run)
        all_new_rows.extend(new_rows)
        per_sport_summary.append(summary)
        # A flag_id graded by one adapter this run must not be reconsidered
        # by a later one in the same run (defensive; sport_labels already
        # keep adapters from overlapping in practice).
        already_graded.update(row["flag_id"] for row in new_rows)

    if all_new_rows:
        combined = pd.concat([outcome_df, pd.DataFrame(all_new_rows)], ignore_index=True)
        combined = combined[OUTCOME_LOG_COLUMNS]
        OUTCOME_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
        combined.to_csv(OUTCOME_LOG_PATH, index=False)
        log.info("Wrote %d new auto-graded row(s) to %s.", len(all_new_rows), OUTCOME_LOG_PATH)

    summary = {
        "dry_run": dry_run,
        "total_graded": sum(s["graded"] for s in per_sport_summary),
        "by_sport": per_sport_summary,
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
