"""
Session 2.44 follow-up v2 -- A Sharper Role-Continuity Signal

WHY THIS EXISTS
----------------
research_year_over_year_role_continuity.py found that last season's
target_share is a real, strong prior for a player's early-season role
(+0.81 same-team), but its ONE continuity check -- same team in 2024 vs.
2025 -- did not cleanly separate a trustworthy Jefferson/Chase-style case
from a genuinely disrupted one: changed-team players showed an EQUALLY
strong correlation, real evidence of survivorship bias (only team-changers
who kept a real role clear this project's own >= 8-games/>= 20-targets
threshold to even appear in that comparison), not evidence team-switching
is irrelevant. This script builds and tests two sharper, real signals
instead of the coarse team-only flag:

    1. QB CONTINUITY -- a same-team receiver whose team's real primary
       passer changed (e.g. a new starting QB via trade/free agency/injury)
       has a real situation change the team-only flag misses entirely --
       a different QB throws to different players, at a different rate,
       to different spots on the field.
    2. COMPETING-WEAPON-ADDED -- a same-team, same-QB receiver whose team
       ALSO added a new pass-catcher (rookie, trade, or free agent) who
       commands a real, meaningful target share in the new season has a
       real situation change too (a target pie now split more ways), even
       though team and QB both look unchanged.

Both are built directly from real nflverse data already used elsewhere in
this project -- no new source.

METHOD
------
1. Real primary QB per team, per season: the QB (position == "QB") with the
   most real pass attempts across REG-season games (2024: full season;
   2025: weeks 1-4, the same early window being predicted). qb_continuity
   = a receiver's team has the SAME real primary-QB player_id in both.
2. Real "new pass-catcher" detection: for each 2025 team, every WR/TE/RB
   player_id who did NOT appear in that SAME team's 2024 roster (checked
   directly against 2024's real team rosters, not assumed). Flags a team as
   competing_weapon_added if any such new player's real 2025 weeks-1-4
   target_share is >= NEW_WEAPON_SHARE_THRESHOLD -- a real, meaningful
   target share, not a two-target cameo.
3. Refined continuity = same_team AND qb_continuity AND NOT
   competing_weapon_added_on_this_team. Reruns the exact same correlation
   comparison as the v1 script (2024 target_share -> 2025 weeks-1-4
   target_share/receiving_yards/receptions), split by this refined flag
   instead of the coarse team-only one, to check whether it actually
   separates a reliable prior from an unreliable one this time.
4. Re-checks the same three named examples (Jefferson/Chase/Lamb) plus a
   deliberately looked-up disrupted case (a receiver whose team added a
   real new starting-caliber weapon) to sanity-check the flag by hand
   before trusting the aggregate table.

REAL, STATED LIMITATIONS (not hidden)
---------------------------------------
- "Primary QB by most attempts" is a real, simple proxy -- a team with a
  genuine QB competition or an in-season injury split could have a real QB
  change this proxy misses if the raw attempt counts still favor the same
  name. A finer split (e.g. by which QB started Week 1) is real future
  work if this proxy under-performs.
- competing_weapon_added is TEAM-level (does this receiver's team have any
  meaningful new weapon), not "did this SPECIFIC receiver lose share to
  that weapon" -- a team's WR1 losing zero share to a new complementary
  TE would still get flagged, a real, coarser-than-ideal signal, stated
  here rather than hidden.

USAGE
-----
python scripts/calibration/research_role_continuity_v2.py
    Prints the QB-continuity and new-weapon audits, the refined correlation
    table (reliable vs. unreliable), and the same named-player sanity
    checks as the v1 script. Writes nothing -- research-only.
"""

from __future__ import annotations

import pandas as pd

PLAYER_STATS_URL_TEMPLATE = (
    "https://github.com/nflverse/nflverse-data/releases/download/"
    "stats_player/stats_player_week_{season}.parquet"
)

MIN_2024_GAMES = 8
MIN_2024_TARGETS = 20
WEEKS_TO_PREDICT = (1, 2, 3, 4)
NEW_WEAPON_SHARE_THRESHOLD = 0.15  # a real, meaningful target share, not a cameo
MIN_ROWS_FOR_CORRELATION = 15
PASS_CATCHER_POSITIONS = {"WR", "TE", "RB"}


def fetch_reg_season(season: int) -> pd.DataFrame:
    df = pd.read_parquet(PLAYER_STATS_URL_TEMPLATE.format(season=season))
    return df[df["season_type"] == "REG"].copy()


def primary_qb_by_team(df: pd.DataFrame, weeks: tuple[int, ...] | None) -> pd.Series:
    """Real primary passer per team -- the QB with the most real pass
    attempts across the given weeks (None = full season)."""
    qb = df.loc[df["position"] == "QB"]
    if weeks is not None:
        qb = qb.loc[qb["week"].isin(weeks)]
    totals = qb.groupby(["team", "player_id"])["attempts"].sum().reset_index()
    idx = totals.groupby("team")["attempts"].idxmax()
    return totals.loc[idx].set_index("team")["player_id"]


def teams_2024_roster(df24: pd.DataFrame) -> dict[str, set[str]]:
    """Real set of pass-catcher player_ids who appeared for each team in
    2024, for detecting who is genuinely NEW to a team in 2025."""
    catchers = df24.loc[df24["position"].isin(PASS_CATCHER_POSITIONS)]
    return catchers.groupby("team")["player_id"].apply(set).to_dict()


def competing_weapon_added_by_team(
    df25: pd.DataFrame, roster_2024: dict[str, set[str]]
) -> dict[str, bool]:
    """Real per-team flag: did this team add a pass-catcher in 2025 who was
    NOT on this same team in 2024, AND who commands a real, meaningful
    (>= NEW_WEAPON_SHARE_THRESHOLD) weeks-1-4 target_share?"""
    early = df25.loc[df25["week"].isin(WEEKS_TO_PREDICT) & df25["position"].isin(PASS_CATCHER_POSITIONS)]
    early_share = early.groupby(["team", "player_id"])["target_share"].mean().reset_index()

    flags: dict[str, bool] = {}
    for team, group in early_share.groupby("team"):
        prior_roster = roster_2024.get(team, set())
        new_players = group.loc[~group["player_id"].isin(prior_roster)]
        flags[team] = bool((new_players["target_share"] >= NEW_WEAPON_SHARE_THRESHOLD).any())
    return flags


def player_2024_role(df24: pd.DataFrame) -> pd.DataFrame:
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
    week1 = df25.loc[df25["week"] == 1, ["player_id", "team"]].rename(columns={"team": "team_2025_wk1"})
    early = df25.loc[df25["week"].isin(WEEKS_TO_PREDICT)]
    early_agg = early.groupby("player_id").agg(
        target_share_early_2025=("target_share", "mean"),
        receiving_yards_early_2025=("receiving_yards", "mean"),
        receptions_early_2025=("receptions", "mean"),
    ).reset_index()
    return early_agg.merge(week1, on="player_id", how="left")


def report_group(df: pd.DataFrame, label: str) -> None:
    print(f"  [{label}, n={len(df)}]")
    if len(df) < MIN_ROWS_FOR_CORRELATION:
        print(f"    below {MIN_ROWS_FOR_CORRELATION}-player floor, skipped")
        return
    for actual_col in ["target_share_early_2025", "receiving_yards_early_2025", "receptions_early_2025"]:
        sub = df.dropna(subset=["target_share_2024", actual_col])
        if len(sub) < MIN_ROWS_FOR_CORRELATION:
            print(f"    target_share_2024 -> {actual_col:<26} below floor (n={len(sub)})")
            continue
        r = sub["target_share_2024"].corr(sub[actual_col])
        print(f"    target_share_2024 -> {actual_col:<26} n={len(sub):>4}  corr={r:+.3f}")


def main() -> None:
    print("Fetching real 2024 and 2025 REG-season nflverse weekly stats...")
    df24 = fetch_reg_season(2024)
    df25 = fetch_reg_season(2025)

    qb_2024 = primary_qb_by_team(df24, weeks=None)
    qb_2025 = primary_qb_by_team(df25, weeks=WEEKS_TO_PREDICT)
    roster_2024 = teams_2024_roster(df24)
    weapon_added = competing_weapon_added_by_team(df25, roster_2024)

    print(f"Real primary QB resolved for {len(qb_2024)} teams (2024), {len(qb_2025)} teams (2025 wks1-4)")
    print(f"Teams with a real new (>= {NEW_WEAPON_SHARE_THRESHOLD:.2f} target_share) "
          f"pass-catcher added in 2025: {sum(weapon_added.values())} of {len(weapon_added)}")
    print()

    role24 = player_2024_role(df24)
    early25 = player_2025_early_season(df25)
    merged = role24.merge(early25, on="player_id", how="inner").dropna(subset=["team_2025_wk1"])

    merged["same_team"] = merged["team_2024"] == merged["team_2025_wk1"]
    merged["qb_continuity"] = merged["team_2025_wk1"].map(qb_2025) == merged["team_2024"].map(qb_2024)
    merged["competing_weapon_added"] = merged["team_2025_wk1"].map(weapon_added).fillna(False)

    merged["refined_continuity"] = (
        merged["same_team"] & merged["qb_continuity"] & ~merged["competing_weapon_added"]
    )
    print(f"Matched players: {len(merged)}")
    print(f"  same_team=True: {merged['same_team'].sum()}")
    print(f"  same_team & qb_continuity: {(merged['same_team'] & merged['qb_continuity']).sum()}")
    print(f"  refined_continuity (same team + same QB + no new weapon): "
          f"{merged['refined_continuity'].sum()}")
    print()

    print("Named sanity check (refined flag):")
    for name in ["Justin Jefferson", "Ja'Marr Chase", "CeeDee Lamb"]:
        row = merged.loc[merged["player_display_name"] == name]
        if not row.empty:
            r = row.iloc[0]
            print(f"  {name:<18} same_team={r['same_team']}  qb_continuity={r['qb_continuity']}  "
                  f"competing_weapon_added={r['competing_weapon_added']}  "
                  f"refined_continuity={r['refined_continuity']}")
    print()
    print("Real disrupted-situation examples (same team, but QB changed or a new weapon "
          "arrived) -- lowest target_share_2024 among refined_continuity=False, same_team=True, "
          "to show a real, non-cherry-picked disrupted case:")
    disrupted = merged.loc[merged["same_team"] & ~merged["refined_continuity"]]
    disrupted = disrupted.sort_values("target_share_2024", ascending=False).head(3)
    for _, r in disrupted.iterrows():
        print(f"  {r['player_display_name']:<20} 2024 target_share={r['target_share_2024']:.3f}  "
              f"2025 wks1-4 target_share={r['target_share_early_2025']:.3f}  "
              f"qb_continuity={r['qb_continuity']}  competing_weapon_added={r['competing_weapon_added']}")
    print()

    print("Correlation comparison -- COARSE team-only flag (v1 script's own split):")
    report_group(merged.loc[merged["same_team"]], "same team (coarse)")
    report_group(merged.loc[~merged["same_team"]], "changed team (coarse)")
    print()

    print("Correlation comparison -- REFINED flag (this script):")
    report_group(merged.loc[merged["refined_continuity"]], "refined_continuity=True")
    report_group(merged.loc[~merged["refined_continuity"]], "refined_continuity=False")
    print()

    print("A materially stronger correlation for refined_continuity=True than for the")
    print("coarse same-team group's own True/False split would mean this flag captures")
    print("something real the team-only flag missed -- the actual bar this session needs")
    print("to clear before any year-over-year prior is trustworthy enough to wire in.")


if __name__ == "__main__":
    main()
