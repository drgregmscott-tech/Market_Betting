"""
Session 2.44 -- Target Share / Usage Role as a Predictive Input, Research

WHY THIS EXISTS
----------------
ROADMAP.md Session 2.44: real research named target share / route
participation TREND (is a player's role trending up or down over their last
few games) as a primary predictor specifically for receiving props. Unlike
Session 2.42 (a new statistical technique) or Session 2.43 (a new data
source), this is about using EXISTING nflverse columns as a LEADING
INDICATOR rather than only as the thing being predicted (this project's NFL
plug-in, pickem_sport_plugins/nfl.py, already fetches these columns for
every player-week -- it just never reads them for anything other than
season_avg/recent_form of the SAME stat the prop asks about).

STEP 1 -- REAL COLUMN AUDIT (done live, 2026-09-17, before designing anything)
-------------------------------------------------------------------------------
Fetched stats_player_week_2026.parquet directly and listed every column.
Confirmed nflverse ALREADY computes real, share-normalized usage columns on
every player-week row, at no extra fetch cost (same file this project
already pulls in nfl.py):
    target_share      -- player's targets / team's total targets that game
    air_yards_share    -- player's air yards / team's total air yards
    wopr                -- "weighted opportunity rating" (1.5*target_share +
                           0.7*air_yards_share), an nflverse-published
                           composite usage metric
    carries             -- raw rush-attempt count (no team-normalized
                           "carry share" column exists in this file --
                           stated gap, see CARRIES LIMITATION below)
Grepped this project's own scripts/ directory (excluding tests) and
confirmed target_share/air_yards_share/wopr/racr are referenced NOWHERE, and
carries is referenced NOWHERE either (NFL_STAT_TYPE_MAP maps prop wordings
to rushing_yards/rushing_tds/attempts/completions/targets/receptions, but
never to carries) -- a real, confirmed gap, not a guessed one. targets IS
already used, but only as an OUTCOME stat when a prop directly asks for
"rec targets" -- never read as a leading indicator for a DIFFERENT prop
(e.g. receiving_yards).

CARRIES LIMITATION (stated, not hidden)
----------------------------------------
target_share is already team-normalized by nflverse. No equivalent
"carries_share" column exists in this file, and computing one would require
summing every team's total rush attempts per game -- a real, larger join
this session keeps out of scope. carries is tested here as a raw trend
(more/fewer carries per game, not more/fewer as a SHARE of the backfield),
a real, named approximation for the rushing side.

TREND FEATURE DESIGN
---------------------
`usage_trend(series)` = the OLS slope of a usage metric (target_share,
carries, or wopr) against game order, over up to the last TREND_WINDOW
games strictly BEFORE the game being predicted. This is deliberately NOT
recent_form() (pickem_model.py's own recency-weighted AVERAGE, which
captures LEVEL) -- a rising trend and a flat trend at the same level get
the same recent_form but a different slope. `usage_level(series)` (the
plain mean over the same window) is also computed, purely so this script
can check whether trend adds anything BEYOND level via a partial
correlation, not just restate it.

WHY FULL 2025 SEASON, NOT 2026 WEEK 1 GRADED LEGS
---------------------------------------------------
Session 2.41/2.43 were both structurally limited to Week 1 2026 (this
project's only graded NFL legs so far), forcing a prior-SEASON baseline
across a real offseason roster/scheme gap -- the likely reason both found
weak signals. A role-TREND feature needs several PRIOR GAMES WITHIN THE
SAME SEASON to even be computable, so Week 1 (no 2026 prior games exist
yet) cannot test this hypothesis at all. This script instead uses the full
2025 REG season (18 weeks, real nflverse data, no offseason gap inside the
window) -- for every player-week with enough real prior games, it computes
the trend from strictly earlier weeks and checks it against that week's
real outcome. This sidesteps 2.41/2.43's limitation entirely rather than
inheriting it, and gives a much larger real sample (thousands of
player-weeks vs. hundreds of graded legs).

METHOD
------
1. Fetch real stats_player_week_2025.parquet (REG season only).
2. Per player, sort games by week. For every week w with at least
   MIN_GAMES_FOR_TREND real games strictly before it, compute usage_trend
   and usage_level over up to the last TREND_WINDOW of those prior games,
   for target_share (receiving side) and carries (rushing side).
3. Pair each trend/level with the REAL stat value actually produced at week
   w (receiving_yards/receptions/targets/receiving_tds for target_share;
   rushing_yards/rushing_tds/carries for carries), never a future value.
4. Reports, per stat: corr(trend, actual), corr(level, actual), n, and the
   partial correlation of trend with actual CONTROLLING for level (does
   trend add real information beyond level, or just restate it).
5. Repeats the whole check on an explicit temporal split -- first 70% of
   weeks (1-12) vs. last 30% (13-18) -- so a real held-out consistency
   check exists, same discipline as fit_shrinkage.py's train/held-out split.

USAGE
-----
python scripts/calibration/research_target_share_usage_trend.py
    Prints the column audit, the trend-vs-level correlation tables (full
    season, then early/late split), and a stated go/no-go read. Writes
    nothing -- research-only, matching this project's "measure before
    wiring in" precedent (Sessions 2.40-2.43).
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]

PLAYER_STATS_URL_TEMPLATE = (
    "https://github.com/nflverse/nflverse-data/releases/download/"
    "stats_player/stats_player_week_{season}.parquet"
)

TREND_WINDOW = 5  # matches pickem_model.py's RECENCY_WEIGHTS length
MIN_GAMES_FOR_TREND = 3  # need at least 3 points for a slope to mean anything
MIN_ROWS_FOR_CORRELATION = 15  # below this, a correlation coefficient is not meaningful

# usage_metric -> the real outcome columns it's a plausible leading
# indicator for (receiving-shaped stats for target_share, rushing-shaped
# stats for carries). Checked directly against stats_player_week's real
# column list above before being used here.
USAGE_METRIC_TARGETS: dict[str, list[str]] = {
    "target_share": ["receiving_yards", "receptions", "targets", "receiving_tds"],
    "carries": ["rushing_yards", "rushing_tds"],
}


def usage_trend(values: np.ndarray) -> float | None:
    """OLS slope of `values` (already sorted oldest->newest, at most the
    last TREND_WINDOW games) against game order. None if fewer than
    MIN_GAMES_FOR_TREND points."""
    if len(values) < MIN_GAMES_FOR_TREND:
        return None
    x = np.arange(len(values), dtype=float)
    slope, _ = np.polyfit(x, values, 1)
    return float(slope)


def usage_level(values: np.ndarray) -> float | None:
    if len(values) < MIN_GAMES_FOR_TREND:
        return None
    return float(np.mean(values))


def build_trend_rows(season_df: pd.DataFrame, usage_col: str, outcome_cols: list[str]) -> pd.DataFrame:
    """For every player-week with >= MIN_GAMES_FOR_TREND real prior games
    in the same real season, computes usage_trend/usage_level from the up-
    to-TREND_WINDOW games strictly before it, paired with that week's real
    outcome value(s). No future data ever enters the trend/level window --
    only games with a strictly smaller `week` than the predicted row."""
    rows = []
    for _pid, games in season_df.groupby("player_id"):
        games = games.sort_values("week")
        weeks = games["week"].to_numpy()
        usage_vals = games[usage_col].to_numpy(dtype=float)
        for i in range(len(games)):
            prior_usage = usage_vals[:i]
            prior_usage = prior_usage[~np.isnan(prior_usage)]
            if len(prior_usage) < MIN_GAMES_FOR_TREND:
                continue
            window = prior_usage[-TREND_WINDOW:]
            trend = usage_trend(window)
            level = usage_level(window)
            if trend is None or level is None:
                continue
            row = {
                "week": weeks[i],
                "usage_trend": trend,
                "usage_level": level,
            }
            for col in outcome_cols:
                row[col] = games.iloc[i][col]
            rows.append(row)
    return pd.DataFrame(rows)


def partial_corr(trend: pd.Series, level: pd.Series, actual: pd.Series) -> float:
    """Partial correlation of trend with actual, controlling for level --
    isolates whether the SLOPE carries information the plain LEVEL doesn't
    already capture."""
    r_ta = trend.corr(actual)
    r_tl = trend.corr(level)
    r_la = level.corr(actual)
    denom = np.sqrt((1 - r_tl**2) * (1 - r_la**2))
    if denom == 0 or denom != denom:
        return float("nan")
    return float((r_ta - r_tl * r_la) / denom)


def report_correlations(df: pd.DataFrame, outcome_cols: list[str], label: str) -> None:
    print(f"  [{label}, n_player-weeks={len(df)}]")
    for col in outcome_cols:
        sub = df.dropna(subset=[col, "usage_trend", "usage_level"])
        if len(sub) < MIN_ROWS_FOR_CORRELATION:
            print(f"    {col:<18} below {MIN_ROWS_FOR_CORRELATION}-row floor (n={len(sub)}), skipped")
            continue
        r_trend = sub["usage_trend"].corr(sub[col])
        r_level = sub["usage_level"].corr(sub[col])
        r_partial = partial_corr(sub["usage_trend"], sub["usage_level"], sub[col])
        print(
            f"    {col:<18} n={len(sub):>5}  corr(trend,actual)={r_trend:+.3f}  "
            f"corr(level,actual)={r_level:+.3f}  partial(trend|level)={r_partial:+.3f}"
        )


def main() -> None:
    season = 2025
    print(f"Fetching real stats_player_week_{season}.parquet (REG season only)...")
    df = pd.read_parquet(PLAYER_STATS_URL_TEMPLATE.format(season=season))
    df = df[df["season_type"] == "REG"].copy()
    print(f"Real rows: {len(df)}, real weeks: {sorted(df['week'].unique().tolist())}")
    print()

    print("REAL COLUMN AUDIT (confirmed live, not assumed):")
    for col in ["target_share", "air_yards_share", "wopr", "carries", "targets"]:
        present = col in df.columns
        non_null = df[col].notna().sum() if present else 0
        print(f"  {col:<16} present={present}  non-null rows={non_null}")
    print()

    for usage_col, outcome_cols in USAGE_METRIC_TARGETS.items():
        print(f"=== usage metric: {usage_col} ===")
        trend_df = build_trend_rows(df, usage_col, outcome_cols)

        print("Full 2025 season (all weeks with enough real prior games):")
        report_correlations(trend_df, outcome_cols, "full season")

        early = trend_df[trend_df["week"] <= 12]
        late = trend_df[trend_df["week"] > 12]
        print("Temporal split -- weeks 1-12 (train-side):")
        report_correlations(early, outcome_cols, "weeks 1-12")
        print("Temporal split -- weeks 13-18 (held-out):")
        report_correlations(late, outcome_cols, "weeks 13-18")
        print()

    print("A real, consistent partial correlation (trend adding signal beyond level) on")
    print("BOTH the full season and the held-out weeks 13-18 split would be evidence this")
    print("feature is worth wiring into pickem_model.py. A weak, inconsistent, or")
    print("level-redundant result is real evidence not to wire it in yet -- same")
    print("'measure before wiring in' standard as Sessions 2.40-2.43.")


if __name__ == "__main__":
    main()
