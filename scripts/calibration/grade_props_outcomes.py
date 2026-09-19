"""
Session 6.11 -- Props Outcome Grading

WHAT THIS IS
The props log (data/sportsbook_props/clv_log.csv) records every player-prop
flag the model raised. A flag is "closed" when the book stops offering it.
Closed is not the same as won or lost. Before this session no props flag had
ever been checked against the real game result, so nothing about the props
model could be judged.

This script checks each closed flag against real NFL results (nflverse) and
writes win or loss into data/sportsbook_props/outcome_log.csv. It reuses
auto_grade_outcomes.run(), the same code that grades pick'em flags.

HOW A PROP BECOMES A LINE
Touchdown props have no numeric line in the log. Each market is a "score at
least N touchdowns" bet on the OVER side. The grader gets an equivalent line:
  Anytime TD Scorer / anytd  -> line 0.5  (win if rushing+receiving TDs >= 1)
  2+ TDs                     -> line 1.5  (win if rushing+receiving TDs >= 2)
The stat is rushing_tds+receiving_tds, the same definition the model uses.
A half-point line cannot tie, so these markets have no pushes.

BETMGM ROWS HAVE NO GAME DATE
Rotowire (the BetMGM source) gives no kickoff time, so game_start_time is
blank on all of these rows. For them the grader uses the NEXT scheduled game
of the player's team on or after the day the flag was first logged, taken
from the nflverse schedule. If that game has no stat row yet (not played, or
the player did not play), the flag stays ungraded.

WHAT STAYS UNGRADED (on purpose)
- Any market not in TD_MARKET_LINES: FanDuel season-long futures (they settle
  after the season, about January 2027) and any new market. They stay pending.
- First TD Scorer: the model does not price it (model_status
  unsupported_market_first_scorer), so it is never flagged and never logged.
  Grading it would need play-by-play data.
- A player with no game row (did not play, name not matched): left ungraded
  and counted, never guessed. He can be graded on a later run.

USAGE
    python grade_props_outcomes.py --run            grade and write
    python grade_props_outcomes.py --run --dry-run  show what would be graded
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Optional

import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))

import auto_grade_outcomes as grader  # noqa: E402
from outcome_tracker import OUTCOME_LOG_COLUMNS  # noqa: E402

PROPS_CLV_LOG_PATH = BASE_DIR / "data" / "sportsbook_props" / "clv_log.csv"
PROPS_OUTCOME_LOG_PATH = BASE_DIR / "data" / "sportsbook_props" / "outcome_log.csv"

# stat_type (lowercased) -> equivalent numeric line for the OVER side.
TD_MARKET_LINES: dict[str, float] = {
    "anytime td scorer": 0.5,
    "anytd": 0.5,
    "2+ tds": 1.5,
}


def props_line_for(stat_type: object) -> Optional[float]:
    if not isinstance(stat_type, str):
        return None
    return TD_MARKET_LINES.get(stat_type.strip().lower())


def find_props_nfl_game_row(
    stats_df: pd.DataFrame, schedule_df: pd.DataFrame, player_id: str, flag_date,
    flag_row: pd.Series,
) -> Optional[pd.Series]:
    """Date-known flags (DraftKings) use the normal NFL join. Date-unknown
    flags (BetMGM) use the player's team's next scheduled game on or after
    the flag date, and grade only if the player has a stat row for exactly
    that game."""
    if not bool(flag_row.get("date_is_proxy")):
        return grader.find_nfl_game_row(stats_df, schedule_df, player_id, flag_date, flag_row)

    player_rows = stats_df[stats_df["player_id"] == player_id]
    flag_iso = flag_date.isoformat()
    best: Optional[tuple[str, pd.Series]] = None
    for _, prow in player_rows.iterrows():
        team_games = schedule_df[
            (schedule_df["season"] == prow["season"])
            & ((schedule_df["home_team"] == prow["team"]) | (schedule_df["away_team"] == prow["team"]))
        ]
        upcoming = team_games[team_games["gameday"].astype(str) >= flag_iso]
        if upcoming.empty:
            continue
        next_game = upcoming.sort_values("gameday").iloc[0]
        if int(next_game["week"]) != int(prow["week"]):
            continue  # the team's next game is a different week than this stat row
        day = str(next_game["gameday"])
        if best is None or day < best[0]:
            best = (day, prow)
    return best[1] if best else None


PROPS_NFL_ADAPTER = grader.GradingAdapter(
    plugin=grader.NFL_PLUGIN,
    load_context=grader.load_nfl_schedule,
    find_game_row=find_props_nfl_game_row,
)


def prepare_props_flags(clv_df: pd.DataFrame) -> pd.DataFrame:
    """Keeps only gradable markets and adds the columns the shared grader
    reads (first_flagged_line, first_flagged_implied_prob, odds_type)."""
    df = clv_df.copy()
    lines = df["stat_type"].map(props_line_for)
    df = df.loc[lines.notna()].copy()
    df["first_flagged_line"] = lines.loc[df.index].astype(float)
    df["first_flagged_implied_prob"] = df["first_flagged_market_price"]
    # The shared grader treats flags with the same player+stat+game+odds_type
    # as one market re-priced and voids the earlier ones. Anytime TD and 2+ TDs
    # share a stat key, so the market name goes in odds_type to keep them apart.
    df["odds_type"] = df["platform"].astype(str) + "|" + df["stat_type"].astype(str).str.lower()
    missing_time = df["game_start_time"].isna() | (df["game_start_time"].astype(str).str.strip() == "")
    df["date_is_proxy"] = missing_time
    df.loc[missing_time, "game_start_time"] = df.loc[missing_time, "first_flagged_at"]
    return df


def load_props_outcomes(path: Path = PROPS_OUTCOME_LOG_PATH) -> pd.DataFrame:
    if path.exists():
        df = pd.read_csv(path)
        for col in OUTCOME_LOG_COLUMNS:
            if col not in df.columns:
                df[col] = None
        return df[OUTCOME_LOG_COLUMNS]
    return pd.DataFrame(columns=OUTCOME_LOG_COLUMNS)


def run(
    dry_run: bool = False,
    clv_df: Optional[pd.DataFrame] = None,
    outcome_df: Optional[pd.DataFrame] = None,
    outcome_path: Path = PROPS_OUTCOME_LOG_PATH,
    adapters: Optional[list] = None,
) -> dict:
    if clv_df is None:
        clv_df = pd.read_csv(PROPS_CLV_LOG_PATH) if PROPS_CLV_LOG_PATH.exists() else pd.DataFrame()
    if clv_df.empty:
        return {"dry_run": dry_run, "total_graded": 0, "by_sport": [], "ungraded_markets": 0}
    prepared = prepare_props_flags(clv_df)
    summary = grader.run(
        dry_run=dry_run,
        clv_df=prepared,
        outcome_df=load_props_outcomes(outcome_path) if outcome_df is None else outcome_df,
        outcome_path=outcome_path,
        adapters=[PROPS_NFL_ADAPTER] if adapters is None else adapters,
    )
    summary["ungraded_markets"] = int(len(clv_df) - len(prepared))
    return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if not args.run:
        parser.error("Specify --run (optionally with --dry-run).")
    print(run(dry_run=args.dry_run))
