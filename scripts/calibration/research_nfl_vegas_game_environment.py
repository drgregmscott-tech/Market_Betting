"""
Session 2.43 -- Vegas Game Environment (Implied Team Total) Research

WHY THIS EXISTS
----------------
ROADMAP.md Session 2.43: real research (2026-09-17 chat conversation) named
Vegas-implied game environment (a game's real point total and spread, which
together imply how many total plays/points each team is expected to produce)
as one of the top drivers of player prop outcomes in professional models.
This project's NFL model (pickem_model.py) has no game-context signal at
all today -- confirmed directly, same "measure before wiring in" discipline
as research_nfl_matchup_adjustment.py (Session 2.41).

REAL DATA SOURCE CONFIRMED THIS SESSION (2026-09-17) -- NO NEW DEPENDENCY
--------------------------------------------------------------------------
This project does NOT currently ingest full-game Vegas odds anywhere --
confirmed directly: Track 5's DK/FD/Rotowire ingestion (ingest_dk_props.py,
ingest_fd_props.py, ingest_rotowire_betmgm_props.py) only pulls PLAYER PROP
odds, no game lines.

The fix needs no new source, though: `https://raw.githubusercontent.com/
nflverse/nfldata/master/data/games.csv` -- the exact schedule URL this
project ALREADY uses (research_nfl_matchup_adjustment.py's SCHEDULE_URL,
Session 2.41) -- carries real spread_line/total_line/moneyline columns on
every row, confirmed live this session (2026-09-17): fetched directly,
verified non-null for 2026 Week 1 (historical, closing lines) AND Week 2/3
(current/upcoming, live lines as of today). The nflverse-data release
mirror (`github.com/nflverse/nflverse-data/releases/download/schedules/
games.csv` -- NOT tag "games", a wrong guess that 404s; the real tag is
"schedules") carries the identical columns, confirmed byte-identical on a
spot check, but this script uses the already-relied-upon nfldata URL to
introduce zero new source risk.

REAL SIGN-CONVENTION SPOT CHECK (done by hand, 2026-09-17, before trusting
the formula below on any real row):
    KC_MIA (away=KC, home=MIA): away_moneyline=-455 (KC big favorite),
    home_moneyline=+350, spread_line=-8.5, total_line=44.5.
    home_implied = 44.5/2 + (-8.5)/2 = 18.0   (MIA, real underdog -- low)
    away_implied = 44.5/2 - (-8.5)/2 = 26.5   (KC, real favorite -- high)
    26.5 - 18.0 = 8.5 == |spread_line| and 26.5 + 18.0 = 44.5 == total_line.
    ATL_GB (away=ATL, home=GB): home_moneyline=-310 (GB favorite),
    spread_line=+6.5 (positive => home favored, consistent).
    BAL_DAL (away=BAL, home=DAL): away_moneyline=-155 (BAL favorite),
    spread_line=-3 (negative => away favored, consistent).
Confirms: spread_line is signed from the HOME team's perspective (positive
= home favored). Formula:
    home_implied_total = total_line / 2 + spread_line / 2
    away_implied_total = total_line / 2 - spread_line / 2

WHY WEEK 1 ONLY, AGAIN (same real constraint as Session 2.41)
------------------------------------------------------------------
Checked directly (2026-09-17): all 1,972 real graded NFL legs are still
Week 1 (game dates 2026-09-09 through 2026-09-15) -- there is no in-season
"real season-average points scored" for any 2026 team yet at Week 1. This
script uses each team's real, full 2025 REG-season average points scored
(from the same games.csv) as the season-average denominator, exactly the
same prior-season fallback Session 2.41 used for matchup_factor, for the
same real, stated reason (Week 1 has no current-season baseline).

METHOD
------
1. Real 2025 REG-season scores (games.csv, season 2025) -> each team's real
   average points scored across the full season (home_score if home,
   away_score if away).
2. Real 2026 Week 1 schedule -> each team's real implied_total for their
   Week 1 game via the sign-checked formula above.
3. scaling_factor = week1 implied_total / team's real 2025 season-average
   points scored. >1.0 = real, sourced evidence this team was in a
   higher-scoring environment than their own established real baseline;
   <1.0 = lower.
4. For every real graded NFL leg with a volume-shaped stat_key (yardage/
   attempt/target/completion/TD counting stats -- the "player's volume-
   based stats" the roadmap names, not e.g. a kicker's made-FG count),
   resolves the player's real Week 1 team and joins that team's real
   scaling_factor, then checks the real, direct correlation against the
   leg's real actual_value, computed separately per stat (never pooled
   across different stats/scales -- same discipline as Session 2.41).

USAGE
-----
python scripts/calibration/research_nfl_vegas_game_environment.py
    Prints the implied-total sign-check, the scaling_factor range, and the
    per-stat correlation table. Writes nothing -- research-only, matching
    this project's "measure before wiring in" precedent (Session 2.40,
    2.41, 2.42).
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "estimation"))
from pickem_model import normalize_name  # noqa: E402

BASE_DIR = Path(__file__).resolve().parents[2]
CLV_LOG_PATH = BASE_DIR / "data" / "pickem" / "clv_log.csv"
OUTCOME_LOG_PATH = BASE_DIR / "data" / "pickem" / "outcome_log.csv"

SCHEDULE_URL = "https://raw.githubusercontent.com/nflverse/nfldata/master/data/games.csv"
PLAYER_STATS_URL_TEMPLATE = (
    "https://github.com/nflverse/nflverse-data/releases/download/"
    "stats_player/stats_player_week_{season}.parquet"
)

# "Volume-based" stats -- the roadmap's own phrase -- covers yardage,
# attempt/target/completion counting stats, and TD counting stats. Kicking
# stats (fg_made) are deliberately excluded: a kicker's attempt volume is
# not driven by team implied total the same way an offense's play volume is.
VOLUME_STAT_COLS = [
    "passing_yards", "rushing_yards", "receiving_yards", "receptions", "targets",
    "completions", "attempts", "passing_tds", "rushing_tds", "receiving_tds",
]
MIN_LEGS_FOR_CORRELATION = 15  # below this, a correlation coefficient is not meaningful


def team_season_avg_points(season: int) -> pd.Series:
    """Real per-team average points scored across one full REG season."""
    sched = pd.read_csv(SCHEDULE_URL, low_memory=False)
    sched = sched.loc[(sched["season"] == season) & (sched["game_type"] == "REG")]
    home = sched[["home_team", "home_score"]].rename(
        columns={"home_team": "team", "home_score": "points"}
    )
    away = sched[["away_team", "away_score"]].rename(
        columns={"away_team": "team", "away_score": "points"}
    )
    long = pd.concat([home, away], ignore_index=True)
    return long.groupby("team")["points"].mean()


def week1_scaling_factors(game_season: int, season_avg_points: pd.Series) -> pd.Series:
    """Real per-team scaling_factor = Week 1 implied_total / prior-season
    real average points scored. Also prints the sign-check spot-check for
    a few real games so a re-run keeps re-verifying the formula, not just
    trusting the docstring."""
    sched = pd.read_csv(SCHEDULE_URL, low_memory=False)
    week1 = sched.loc[
        (sched["season"] == game_season) & (sched["week"] == 1) & (sched["game_type"] == "REG")
    ].copy()
    week1["home_implied"] = week1["total_line"] / 2 + week1["spread_line"] / 2
    week1["away_implied"] = week1["total_line"] / 2 - week1["spread_line"] / 2

    print("Real sign-check spot-check (Week 1 implied totals, a few real games):")
    for _, row in week1.head(3).iterrows():
        print(
            f"  {row['away_team']} @ {row['home_team']}: total_line={row['total_line']}, "
            f"spread_line={row['spread_line']:+.1f} -> "
            f"away_implied={row['away_implied']:.1f}, home_implied={row['home_implied']:.1f}"
        )
    print()

    home = week1[["home_team", "home_implied"]].rename(
        columns={"home_team": "team", "home_implied": "implied_total"}
    )
    away = week1[["away_team", "away_implied"]].rename(
        columns={"away_team": "team", "away_implied": "implied_total"}
    )
    implied = pd.concat([home, away], ignore_index=True).set_index("team")["implied_total"]

    factor = implied / season_avg_points
    return factor.dropna()


def resolve_teams(legs: pd.DataFrame, game_season: int, week: int) -> pd.DataFrame:
    """Adds a real `team` column -- the player's real team for their real
    Week `week` game (nflverse stats_player_week_{game_season}.parquet)."""
    player_stats = pd.read_parquet(PLAYER_STATS_URL_TEMPLATE.format(season=game_season))
    player_stats = player_stats.loc[player_stats["week"] == week]
    name_col = "player_display_name" if "player_display_name" in player_stats.columns else "player_name"
    name_to_team = {
        normalize_name(row[name_col]): row["team"] for _, row in player_stats.iterrows()
    }
    legs = legs.copy()
    legs["team"] = legs["player_name"].map(lambda n: name_to_team.get(normalize_name(n)))
    return legs


def main() -> None:
    prior_season, game_season, week = 2025, 2026, 1

    print(f"Building real team season-avg points from {prior_season} REG season...")
    season_avg = team_season_avg_points(prior_season)
    print(season_avg.agg(["min", "max", "mean"]))
    print()

    print(f"Building real {game_season} Week {week} scaling_factor "
          f"(implied_total / {prior_season} season-avg points)...")
    factor = week1_scaling_factors(game_season, season_avg)
    print("Real scaling_factor range:")
    print(factor.agg(["min", "max", "mean"]))
    print()

    clv = pd.read_csv(CLV_LOG_PATH, low_memory=False)
    outcome = pd.read_csv(OUTCOME_LOG_PATH, low_memory=False)
    nfl_graded = outcome.loc[(outcome["sport"] == "NFL") & (outcome["result"].isin(["win", "loss"]))]
    merged = nfl_graded.merge(clv[["flag_id", "game_start_time"]], on="flag_id", how="left")

    print(f"Resolving real teams for {len(merged)} real graded NFL legs "
          f"({game_season} Week {week})...")
    merged = resolve_teams(merged, game_season, week)
    n_resolved = merged["team"].notna().sum()
    print(f"Resolved a real team for {n_resolved} of {len(merged)} legs.")

    usable = merged.loc[
        merged["team"].notna() & merged["resolved_stat_key"].isin(VOLUME_STAT_COLS)
    ].copy()
    usable["scaling_factor"] = usable["team"].map(factor)
    usable = usable.dropna(subset=["scaling_factor"])
    print(f"Usable rows (real team + a covered volume stat_key): {len(usable)}")
    print()

    print(f"{'stat_key':<20} {'n':>5} {'corr(scaling_factor, actual_value)':>36}")
    print("-" * 62)
    any_meaningful = False
    for stat_key, group in usable.groupby("resolved_stat_key"):
        if len(group) < MIN_LEGS_FOR_CORRELATION:
            continue
        any_meaningful = True
        corr = group["scaling_factor"].corr(group["actual_value"])
        print(f"{stat_key:<20} {len(group):>5} {corr:>+35.3f}")

    print()
    if not any_meaningful:
        print(f"No stat cleared the {MIN_LEGS_FOR_CORRELATION}-leg floor -- no real read possible yet.")
    else:
        print("A real, positive, consistent correlation across multiple stats would be evidence")
        print("this signal is worth wiring into pickem_model.py. A weak or negative correlation")
        print("is real evidence NOT to wire it in yet, at least not from this prior-season-")
        print("baseline, Week-1-only sample (same caveat as Session 2.41's matchup_factor).")


if __name__ == "__main__":
    main()
