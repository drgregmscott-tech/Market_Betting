"""
Session 2.44 follow-up v3 -- Does blending last year's role into the model's
mean actually reduce prediction error? (Item 1 of the follow-up plan.)

WHAT THIS TESTS
---------------
Earlier follow-ups showed last season's target_share CORRELATES with early-
season role, and built a refined continuity flag (same team + same primary QB
+ no new meaningful weapon). Correlation is not the same as "improves the
model's prediction". This script backtests the improvement directly.

For each qualifying receiver and each of weeks 1-4 of the new season, it
predicts that week's real receiving_yards / receptions two ways:
  BASELINE -- the model's own style of estimate from ONLY that season's prior
              games: 0.95*season_avg + 0.05*recent_form (pickem_model.py's
              current blend constants, imported). Undefined at week 1 (no
              prior games), so week 1 is scored separately (see below).
  BLENDED  -- shrinks the baseline toward the player's real prior-season
              per-game average of the same stat with weight
              k/(n+k), n = games already played this season (same form as
              Session 2.42's shrinkage, keyed to the player's own history
              instead of a league average). At week 1 (n=0) the blend is the
              prior alone.
Applied ONLY to players with refined_continuity=True (research_role_
continuity_v2.py); the rest keep the baseline. Error metric: MAE and RMSE
against the real value.

HELD-OUT DESIGN: k is fit on the 2023->2024 season pair and evaluated,
unchanged, on the 2024->2025 pair. Week 1 has no baseline, so it is scored
against a "group mean" baseline (mean of the qualifying players' prior-season
averages) -- the best a model with no player history could do.

USAGE: python scripts/calibration/research_prior_blend_backtest.py
Research-only; writes nothing.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from research_role_continuity_v2 import (  # noqa: E402
    WEEKS_TO_PREDICT,
    competing_weapon_added_by_team,
    fetch_reg_season,
    player_2024_role,
    primary_qb_by_team,
    teams_2024_roster,
)

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "estimation"))
from pickem_model import RECENCY_WEIGHTS, RECENT_FORM_BLEND_WEIGHT, SEASON_AVG_BLEND_WEIGHT  # noqa: E402

STATS = ["receiving_yards", "receptions"]
K_GRID = [0.0, 0.5, 1, 2, 3, 4, 6, 8, 12, 20, 1000]  # 1000 ~ prior only


def model_style_mean(prior_games: np.ndarray) -> float:
    last = prior_games[-len(RECENCY_WEIGHTS):]
    w = np.array(RECENCY_WEIGHTS[: len(last)])
    w = w / w.sum()
    recent = float(np.dot(last[::-1], w))
    return SEASON_AVG_BLEND_WEIGHT * float(prior_games.mean()) + RECENT_FORM_BLEND_WEIGHT * recent


def build_rows(prior_season: int, new_season: int) -> pd.DataFrame:
    prior_df = fetch_reg_season(prior_season)
    new_df = fetch_reg_season(new_season)

    qb_prior = primary_qb_by_team(prior_df, weeks=None)
    qb_new = primary_qb_by_team(new_df, weeks=WEEKS_TO_PREDICT)
    weapon = competing_weapon_added_by_team(new_df, teams_2024_roster(prior_df))

    role = player_2024_role(prior_df)  # generic despite its name: any prior season
    prior_stat = prior_df.groupby("player_id")[STATS].mean().add_suffix("_prior")
    role = role.merge(prior_stat, on="player_id")

    wk1_team = new_df.loc[new_df["week"] == 1].set_index("player_id")["team"]
    role["team_new"] = role["player_id"].map(wk1_team)
    role = role.dropna(subset=["team_new"])
    role["reliable"] = (
        (role["team_2024"] == role["team_new"])
        & (role["team_new"].map(qb_new) == role["team_2024"].map(qb_prior))
        & ~role["team_new"].map(weapon).fillna(False).astype(bool)
    )

    rows = []
    early = new_df.loc[new_df["week"].isin(WEEKS_TO_PREDICT)]
    for _, p in role.iterrows():
        games = new_df.loc[new_df["player_id"] == p["player_id"]].sort_values("week")
        for _, g in early.loc[early["player_id"] == p["player_id"]].iterrows():
            prev = games.loc[games["week"] < g["week"]]
            for stat in STATS:
                rows.append({
                    "season": new_season, "player_id": p["player_id"], "week": int(g["week"]),
                    "stat": stat, "actual": g[stat], "reliable": bool(p["reliable"]),
                    "prior": p[f"{stat}_prior"], "n": len(prev),
                    "base": model_style_mean(prev[stat].to_numpy(dtype=float)) if len(prev) else np.nan,
                })
    df = pd.DataFrame(rows)
    df["group_mean"] = df.groupby("stat")["prior"].transform("mean")
    return df


def predict(df: pd.DataFrame, k: float) -> np.ndarray:
    n = df["n"].to_numpy(float)
    base = df["base"].to_numpy(float)
    prior = df["prior"].to_numpy(float)
    if k >= 1000:
        blend = prior
    else:
        wt = np.where(n + k > 0, k / np.maximum(n + k, 1e-9), 1.0)
        blend = np.where(n > 0, (1 - wt) * base + wt * prior, prior)
    fallback = np.where(np.isnan(base), df["group_mean"].to_numpy(float), base)
    return np.where(df["reliable"].to_numpy(), blend, fallback)


def errors(df: pd.DataFrame, pred: np.ndarray) -> tuple[float, float]:
    e = pred - df["actual"].to_numpy(float)
    return float(np.mean(np.abs(e))), float(np.sqrt(np.mean(e**2)))


def main() -> None:
    fit = build_rows(2023, 2024)
    test = build_rows(2024, 2025)
    for label, d in (("FIT 2023->2024", fit), ("TEST 2024->2025", test)):
        print(f"{label}: {len(d)} rows, reliable share {d['reliable'].mean():.2f}")

    print("\nFitting k (blend strength) on 2023->2024, reliable players only, by RMSE:")
    best_k, best = 0.0, None
    fit_rel = fit.loc[fit["reliable"]]
    for k in K_GRID:
        mae, rmse = errors(fit_rel, predict(fit_rel, k))
        print(f"  k={k:<6} MAE={mae:.3f} RMSE={rmse:.3f}")
        if best is None or rmse < best:
            best, best_k = rmse, k
    print(f"Chosen k = {best_k}\n")

    print("HELD-OUT 2024->2025, reliable players only (baseline vs blended):")
    for stat in STATS:
        for label, sub in (
            ("weeks 2-4 (baseline has >=1 game)", test[(test.stat == stat) & test.reliable & (test.n > 0)]),
            ("week 1 (baseline = group mean)", test[(test.stat == stat) & test.reliable & (test.n == 0)]),
        ):
            b_mae, b_rmse = errors(sub, np.where(np.isnan(sub["base"]), sub["group_mean"], sub["base"]))
            n_mae, n_rmse = errors(sub, predict(sub, best_k))
            print(f"  {stat:<16} {label:<36} n={len(sub):>4}  "
                  f"baseline MAE {b_mae:.3f}/RMSE {b_rmse:.3f}  ->  blended MAE {n_mae:.3f}/RMSE {n_rmse:.3f}")

    print("\nSame test on NOT-reliable players (should show little or no gain, or harm):")
    for stat in STATS:
        sub = test[(test.stat == stat) & ~test.reliable & (test.n > 0)]
        forced = sub.copy()
        forced["reliable"] = True
        b = errors(sub, np.where(np.isnan(sub["base"]), sub["group_mean"], sub["base"]))
        f = errors(forced, predict(forced, best_k))
        print(f"  {stat:<16} n={len(sub):>4}  baseline RMSE {b[1]:.3f}  ->  blend-if-applied RMSE {f[1]:.3f}")


if __name__ == "__main__":
    main()
