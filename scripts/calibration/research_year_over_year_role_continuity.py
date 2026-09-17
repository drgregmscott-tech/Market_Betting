"""
Session 2.44 follow-up -- Year-Over-Year Role Continuity as an Early-Season
Usage Prior

WHY THIS EXISTS
----------------
Session 2.44's own research (research_target_share_usage_trend.py) found a
real, held-out-validated usage_trend signal, but could not wire it into
pickem_model.py this project's own real legs are ALL Week 1 2026, and
usage_trend needs >= 3 real PRIOR games in the SAME season -- structurally
uncomputable before Week 4.

A follow-up question from the user (2026-09-17 chat): rather than waiting on
in-season data to accumulate, can a player's LAST season's own role (e.g.
Justin Jefferson's or Ja'Marr Chase's real, well-established target share)
stand in as an early-season prior for a player whose SITUATION did not
change? This is a different claim from Session 2.41/2.43's team-level
scoring-environment carryover (which failed on a real, checked offseason-
turnover mismatch) -- an individual STAR receiver's role is plausibly far
more stable year-over-year than a TEAM's scoring environment is, but only
for players whose real situation (team, and implicitly their offense) did
not change. This script tests that claim directly, not on faith.

METHOD
------
1. Real 2024 REG season stats_player_week -> each player's real full-season
   target_share average (the "prior"), restricted to players with a real,
   meaningful 2024 role (>= MIN_2024_GAMES games AND >= MIN_2024_TARGETS
   total targets -- excludes bit-part/injury-replacement noise from the
   prior itself).
2. Real 2025 REG season stats_player_week -> each such player's real
   average target_share across weeks 1-4 (WEEKS_TO_PREDICT) -- the exact
   early-season window this project's own model currently has the least
   real signal for (season_avg/recent_form need real 2025 games to exist
   first).
3. Real TEAM CONTINUITY flag: same real team in 2024 (player's most common
   2024 team) as their real 2025 Week 1 team. A player who changed teams in
   free agency/trade is real evidence their 2024 role may not transfer
   (different offense, different competing targets) -- checked directly via
   nflverse's own `team` column, not assumed.
4. Reports, separately for continuity=True and continuity=False:
   - corr(2024 target_share, 2025 weeks-1-4 target_share)
   - corr(2024 target_share, 2025 weeks-1-4 receiving_yards) and
     receptions -- the actual downstream stats a prop bets on, not just
     the share metric itself.
   - n players in each group.
   A materially stronger correlation for continuity=True than
   continuity=False is real evidence the hypothesis holds and the prior is
   usable ONLY when situation is unchanged, not universally.
5. A second real check: does last year's target_share level ALONE (with
   zero 2025 games) already beat the information available from a single
   real 2025 Week 1 game alone (what a Week-2 prediction has to work with
   today)? Reports corr(2025 week 1 target_share alone, 2025 weeks 2-4
   average) as that real baseline, for the same comparison.

REAL, STATED LIMITATIONS (not hidden)
---------------------------------------
- "Team continuity" is a coarse proxy for "situation continuity" -- it does
  not capture a same-team player whose role still changed because of a new
  QB, a new competing weapon added via the draft/free agency, a coordinator
  change, or their own injury history. A finer-grained continuity flag
  (QB continuity, new-weapon-added flag) is real future work, not attempted
  here.
- Uses 2024 -> 2025 (not 2025 -> 2026) because 2026 Week 1-4 team_share data
  does not fully exist yet at the time of this research pass; the
  methodology transfers directly once 2025 full-season data plus real 2026
  weeks 1-4 exist.

USAGE
-----
python scripts/calibration/research_year_over_year_role_continuity.py
    Prints the 2024-role-audit, the continuity vs. non-continuity
    correlation tables, and the single-game-baseline comparison. Writes
    nothing -- research-only, matching this project's "measure before
    wiring in" precedent.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

PLAYER_STATS_URL_TEMPLATE = (
    "https://github.com/nflverse/nflverse-data/releases/download/"
    "stats_player/stats_player_week_{season}.parquet"
)

MIN_2024_GAMES = 8  # a real, meaningful 2024 role, not a few injury-replacement games
MIN_2024_TARGETS = 20  # excludes players who barely saw the field
WEEKS_TO_PREDICT = (1, 2, 3, 4)
MIN_ROWS_FOR_CORRELATION = 15


def fetch_reg_season(season: int) -> pd.DataFrame:
    df = pd.read_parquet(PLAYER_STATS_URL_TEMPLATE.format(season=season))
    return df[df["season_type"] == "REG"].copy()


def player_2024_role(df24: pd.DataFrame) -> pd.DataFrame:
    """Real per-player 2024 profile: target_share average, games played,
    total targets, and most-common (mode) team -- restricted to players
    with a real, meaningful role (see module docstring thresholds)."""
    grouped = df24.groupby("player_id").agg(
        player_display_name=("player_display_name", "first"),
        games_2024=("week", "count"),
        targets_2024=("targets", "sum"),
        target_share_2024=("target_share", "mean"),
        team_2024=("team", lambda s: s.mode().iat[0] if not s.mode().empty else None),
    )
    grouped = grouped.loc[
        (grouped["games_2024"] >= MIN_2024_GAMES) & (grouped["targets_2024"] >= MIN_2024_TARGETS)
    ]
    return grouped.reset_index()


def player_2025_early_season(df25: pd.DataFrame) -> pd.DataFrame:
    """Real per-player 2025 weeks-1-4 average target_share/receiving_yards/
    receptions, plus their real Week 1 team (for the continuity check) and
    their real Week 1 target_share alone (for the single-game baseline
    check)."""
    week1 = df25.loc[df25["week"] == 1, ["player_id", "team", "target_share"]].rename(
        columns={"team": "team_2025_wk1", "target_share": "target_share_wk1"}
    )
    early = df25.loc[df25["week"].isin(WEEKS_TO_PREDICT)]
    early_agg = early.groupby("player_id").agg(
        target_share_early_2025=("target_share", "mean"),
        receiving_yards_early_2025=("receiving_yards", "mean"),
        receptions_early_2025=("receptions", "mean"),
        n_early_games=("week", "count"),
    ).reset_index()

    weeks_2_4 = df25.loc[df25["week"].isin(WEEKS_TO_PREDICT[1:])]
    late_agg = weeks_2_4.groupby("player_id").agg(
        target_share_wk2_4=("target_share", "mean"),
    ).reset_index()

    out = early_agg.merge(week1, on="player_id", how="left").merge(
        late_agg, on="player_id", how="left"
    )
    return out


def report_group(df: pd.DataFrame, label: str) -> None:
    print(f"  [{label}, n={len(df)}]")
    if len(df) < MIN_ROWS_FOR_CORRELATION:
        print(f"    below {MIN_ROWS_FOR_CORRELATION}-player floor, skipped")
        return
    for prior_col, actual_col in [
        ("target_share_2024", "target_share_early_2025"),
        ("target_share_2024", "receiving_yards_early_2025"),
        ("target_share_2024", "receptions_early_2025"),
    ]:
        sub = df.dropna(subset=[prior_col, actual_col])
        if len(sub) < MIN_ROWS_FOR_CORRELATION:
            print(f"    {prior_col} -> {actual_col:<26} below floor (n={len(sub)})")
            continue
        r = sub[prior_col].corr(sub[actual_col])
        print(f"    {prior_col} -> {actual_col:<26} n={len(sub):>4}  corr={r:+.3f}")


def main() -> None:
    print("Fetching real 2024 and 2025 REG-season nflverse weekly stats...")
    df24 = fetch_reg_season(2024)
    df25 = fetch_reg_season(2025)

    role24 = player_2024_role(df24)
    print(f"Players with a real, meaningful 2024 role "
          f"(>= {MIN_2024_GAMES} games, >= {MIN_2024_TARGETS} targets): {len(role24)}")

    early25 = player_2025_early_season(df25)

    merged = role24.merge(early25, on="player_id", how="inner")
    merged = merged.dropna(subset=["team_2025_wk1"])  # must have actually played in 2025
    merged["continuity"] = merged["team_2024"] == merged["team_2025_wk1"]
    print(f"Matched to a real 2025 Week 1 appearance: {len(merged)} "
          f"({merged['continuity'].sum()} same-team, {(~merged['continuity']).sum()} team-changed)")
    print()

    print("Real known-role examples (sanity check before trusting the aggregate numbers):")
    for name in ["Justin Jefferson", "Ja'Marr Chase", "CeeDee Lamb"]:
        row = merged.loc[merged["player_display_name"] == name]
        if not row.empty:
            r = row.iloc[0]
            print(f"  {name:<18} 2024 target_share={r['target_share_2024']:.3f}  "
                  f"2025 wks1-4 target_share={r['target_share_early_2025']:.3f}  "
                  f"continuity={r['continuity']}")
    print()

    print("2024 target_share as a prior for 2025 weeks 1-4, by team continuity:")
    report_group(merged.loc[merged["continuity"]], "SAME team 2024->2025")
    report_group(merged.loc[~merged["continuity"]], "CHANGED team 2024->2025")
    print()

    print("Baseline comparison -- does last year's role already beat a single real")
    print("2025 Week 1 game alone (what a Week-2 prediction has to work with today)?")
    same_team = merged.loc[merged["continuity"]]
    baseline = same_team.dropna(subset=["target_share_wk1", "target_share_wk2_4"])
    if len(baseline) >= MIN_ROWS_FOR_CORRELATION:
        r_prior = same_team.dropna(subset=["target_share_2024", "target_share_wk2_4"])
        r_prior_corr = r_prior["target_share_2024"].corr(r_prior["target_share_wk2_4"])
        r_wk1_corr = baseline["target_share_wk1"].corr(baseline["target_share_wk2_4"])
        print(f"  corr(2024 season target_share, 2025 weeks 2-4)        = {r_prior_corr:+.3f} (n={len(r_prior)})")
        print(f"  corr(2025 Week 1 alone,        2025 weeks 2-4)        = {r_wk1_corr:+.3f} (n={len(baseline)})")
    print()

    print("A materially stronger correlation for SAME-team players than CHANGED-team")
    print("players is real evidence this prior is usable only when situation is")
    print("unchanged, not universally -- exactly the Jefferson/Chase-style case named in")
    print("the user's question, not a blanket 'carry over last year' rule.")


if __name__ == "__main__":
    main()
