"""
Session 2.41 -- Opponent/Matchup Adjustment Research (NFL First)

WHY THIS EXISTS
----------------
pickem_model.py's own docstring names this as a stated v1 gap: "No
opponent/matchup adjustment, no injury/role status, no home/away split,
no pace/usage adjustment." (pickem_model.py:111-113) -- the single
biggest named difference between this project's model (a plain season-
average + recent-form blend) and what a real sharp props model typically
uses. This script is the research step, per this project's "measure
before wiring in" precedent (same discipline as fit_isotonic_calibration.py
and fit_sigma_recalibration.py): does a real, sourced opponent-strength
signal actually predict real outcomes, BEFORE any production code change.

DATA SOURCE -- SAME TRUSTED FAMILY ALREADY WIRED IN, NO NEW DEPENDENCY
--------------------------------------------------------------------------
nflverse-data publishes real, free, no-API-key team-level weekly stats
(github.com/nflverse/nflverse-data, release tag "stats_team",
stats_team_week_{season}.parquet) -- the same project family as this
project's existing NFL_PLUGIN player-stats pull and auto_grade_outcomes.py's
schedule pull. Each row is one team's own offensive output in one real
game; from the OPPONENT's perspective, that same row is "yards/stats
allowed" -- grouping by opponent_team and averaging gives each team's
real defense-allowed rate per stat, with zero new data source risk.

WHY THIS SESSION USED 2025 (PRIOR-SEASON) DATA, NOT 2026 IN-SEASON DATA
--------------------------------------------------------------------------
Checked directly: 100% of this project's real graded NFL legs (1,972 of
1,972) are Week 1 of the 2026 season (see SESSION_LOG.md Session 2.38).
Week 1 has, by definition, ZERO real in-season defensive data available
at flag time for any opponent -- the only real, already-observed signal
available before a Week 1 game is the OPPONENT's prior (2025) full-season
defense-allowed rate. This is a weaker, stopgap signal (a full offseason
of roster/scheme turnover sits between it and the current game) compared
to the in-season, several-weeks-of-current-data signal a standard
matchup-adjustment design would normally use -- stated directly, not
glossed over, since it materially affects how to read this session's
result.

METHOD
------
1. Real 2025 team-level weekly stats -> each team's real average
   stat-allowed (grouped by opponent_team) across the full REG season,
   for 10 volume/yardage-shaped stats where "allowed" is the natural
   interpretation (passing_yards, rushing_yards, receiving_yards,
   receptions, targets, completions, attempts, passing_tds, rushing_tds,
   receiving_tds). Deliberately excludes def_sacks/passing_interceptions/
   fg_made/kicking points -- those need the OPPONENT'S OWN defensive-
   generation rate, not an "allowed" reframing, a different mapping this
   session did not build (a stated v1 gap, not silently skipped).
2. matchup_factor = opponent's real 2025 average allowed / real league
   average allowed, per stat -- 1.0 = league-average defense, >1.0 =
   real, sourced evidence this opponent allows more of this stat than
   average, <1.0 = allows less.
3. For every real graded NFL leg, resolves the player's real Week 1 2026
   team (nflverse stats_player_week_2026.parquet) and real opponent (the
   real 2026 schedule, nflverse/nfldata's games.csv -- published in
   advance, so this is genuinely available before the game, not
   hindsight), then joins that opponent's real matchup_factor for the
   leg's own resolved_stat_key.
4. Real, direct check: does matchup_factor correlate with the leg's real
   actual_value, computed SEPARATELY per stat (never pooled across
   different stats/scales)?

REAL RESULT (2026-09-17, all 1,972 real graded NFL legs resolved a real
opponent; 1,128 had both a resolved opponent and a covered "allowed"
stat_key) -- see this script's own printed output for the exact numbers
on a re-run, recorded here so the headline finding is not lost to a
stale docstring: correlation was weak-to-negative for 8 of 10 stats
checked (receiving_yards -0.035 n=317, receptions -0.103 n=315,
rushing_yards -0.039 n=149, targets -0.162 n=123, attempts -0.221 n=52,
completions -0.303 n=25, passing_yards -0.094 n=55, passing_tds +0.135
n=47, receiving_tds +0.049 n=19) -- only rushing_tds showed a real
positive correlation (+0.547 n=26), on a small, zero-inflated,
unreliable sample. THIS FEATURE WAS NOT WIRED INTO pickem_model.py -- a
prior-season-only matchup signal does not show real predictive value on
the only real data available to check it against (Week 1). See
SESSION_LOG.md Session 2.41 for the full, honest writeup of why this is
a legitimate, valuable negative result, not a failed session.

USAGE
-----
python scripts/calibration/research_nfl_matchup_adjustment.py
    Prints the matchup-factor range and the per-stat correlation table.
    Writes nothing -- research-only, matching this project's "measure
    before wiring in" precedent.
"""

from __future__ import annotations

import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "estimation"))
from pickem_model import normalize_name  # noqa: E402

BASE_DIR = Path(__file__).resolve().parents[2]
CLV_LOG_PATH = BASE_DIR / "data" / "pickem" / "clv_log.csv"
OUTCOME_LOG_PATH = BASE_DIR / "data" / "pickem" / "outcome_log.csv"

TEAM_STATS_URL_TEMPLATE = (
    "https://github.com/nflverse/nflverse-data/releases/download/"
    "stats_team/stats_team_week_{season}.parquet"
)
PLAYER_STATS_URL_TEMPLATE = (
    "https://github.com/nflverse/nflverse-data/releases/download/"
    "stats_player/stats_player_week_{season}.parquet"
)
SCHEDULE_URL = "https://raw.githubusercontent.com/nflverse/nfldata/master/data/games.csv"

LOCAL_TZ = ZoneInfo("America/New_York")

# "Allowed" stats only -- see module docstring for why def_sacks/
# passing_interceptions/fg_made/kicking points are excluded from this pass.
ALLOWED_STAT_COLS = [
    "passing_yards", "rushing_yards", "receiving_yards", "receptions", "targets",
    "completions", "attempts", "passing_tds", "rushing_tds", "receiving_tds",
]
MIN_LEGS_FOR_CORRELATION = 15  # below this, a correlation coefficient is not meaningful


def game_local_date(game_start_time: str):
    dt = datetime.fromisoformat(game_start_time)
    if dt.tzinfo is None:
        return dt.date()
    return dt.astimezone(LOCAL_TZ).date()


def build_matchup_factor_table(prior_season: int) -> tuple[pd.DataFrame, pd.Series]:
    """Real per-team, per-stat matchup_factor from a full prior REG season
    (see module docstring for why prior-season, not in-season, for now)."""
    team_stats = pd.read_parquet(TEAM_STATS_URL_TEMPLATE.format(season=prior_season))
    team_stats = team_stats.loc[team_stats["season_type"] == "REG"]
    allowed = team_stats.groupby("opponent_team")[ALLOWED_STAT_COLS].mean()
    league_avg = team_stats[ALLOWED_STAT_COLS].mean()
    factor = allowed.div(league_avg, axis=1)
    return factor, league_avg


def resolve_opponents(
    legs: pd.DataFrame, game_season: int, week: int
) -> pd.DataFrame:
    """Adds a real `opponent` column -- the player's real opponent team for
    their real Week `week` game, resolved via the real, published-in-advance
    schedule (nflverse/nfldata games.csv) and the player's own real team
    (nflverse stats_player_week_{game_season}.parquet, same `week`)."""
    player_stats = pd.read_parquet(PLAYER_STATS_URL_TEMPLATE.format(season=game_season))
    player_stats = player_stats.loc[player_stats["week"] == week]

    name_col = "player_display_name" if "player_display_name" in player_stats.columns else "player_name"
    name_to_team = {
        normalize_name(row[name_col]): row["team"] for _, row in player_stats.iterrows()
    }

    schedule = pd.read_csv(SCHEDULE_URL, low_memory=False)
    schedule = schedule.loc[(schedule["season"] == game_season) & (schedule["week"] == week)]

    def find_opponent(player_name: str, game_start_time: str) -> object:
        team = name_to_team.get(normalize_name(player_name))
        if team is None:
            return None
        try:
            gdate = game_local_date(game_start_time).isoformat()
        except ValueError:
            return None
        row = schedule.loc[
            (schedule["gameday"] == gdate)
            & ((schedule["home_team"] == team) | (schedule["away_team"] == team))
        ]
        if row.empty:
            return None
        row = row.iloc[0]
        return row["away_team"] if row["home_team"] == team else row["home_team"]

    legs = legs.copy()
    legs["opponent"] = legs.apply(
        lambda r: find_opponent(r["player_name"], r["game_start_time"]), axis=1
    )
    return legs


def main() -> None:
    prior_season, game_season, week = 2025, 2026, 1
    print(f"Building real matchup_factor table from {prior_season} REG season "
          f"(prior-season, not in-season -- see module docstring for why).")
    factor, league_avg = build_matchup_factor_table(prior_season)
    print(f"Real matchup_factor range per stat (opponent's {prior_season} "
          f"defense-allowed avg / league avg):")
    print(factor.agg(["min", "max", "mean"]).T)
    print()

    clv = pd.read_csv(CLV_LOG_PATH, low_memory=False)
    outcome = pd.read_csv(OUTCOME_LOG_PATH, low_memory=False)
    nfl_graded = outcome.loc[(outcome["sport"] == "NFL") & (outcome["result"].isin(["win", "loss"]))]
    merged = nfl_graded.merge(clv[["flag_id", "game_start_time"]], on="flag_id", how="left")

    print(f"Resolving real opponents for {len(merged)} real graded NFL legs "
          f"({game_season} Week {week})...")
    merged = resolve_opponents(merged, game_season, week)
    n_resolved = merged["opponent"].notna().sum()
    print(f"Resolved a real opponent for {n_resolved} of {len(merged)} legs.")

    usable = merged.loc[
        merged["opponent"].notna() & merged["resolved_stat_key"].isin(ALLOWED_STAT_COLS)
    ].copy()
    usable["matchup_factor"] = usable.apply(
        lambda r: factor.loc[r["opponent"], r["resolved_stat_key"]]
        if r["opponent"] in factor.index else np.nan,
        axis=1,
    )
    usable = usable.dropna(subset=["matchup_factor"])
    print(f"Usable rows (real opponent + a covered 'allowed' stat_key): {len(usable)}")
    print()

    print(f"{'stat_key':<20} {'n':>5} {'corr(matchup_factor, actual_value)':>36}")
    print("-" * 62)
    any_meaningful = False
    for stat_key, group in usable.groupby("resolved_stat_key"):
        if len(group) < MIN_LEGS_FOR_CORRELATION:
            continue
        any_meaningful = True
        corr = group["matchup_factor"].corr(group["actual_value"])
        print(f"{stat_key:<20} {len(group):>5} {corr:>+35.3f}")

    print()
    if not any_meaningful:
        print(f"No stat cleared the {MIN_LEGS_FOR_CORRELATION}-leg floor -- no real read possible yet.")
    else:
        print("A real, positive, consistent correlation across multiple stats would be evidence")
        print("this signal is worth wiring into pickem_model.py. A weak or negative correlation")
        print("(as found 2026-09-17 -- see module docstring) is real evidence NOT to wire it in")
        print("yet, at least not from prior-season-only data on a Week-1-only sample.")


if __name__ == "__main__":
    main()
