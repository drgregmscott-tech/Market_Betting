"""
Session 2.50 -- Held-Out Test of Per-Sport Blend Weights

WHY THIS EXISTS
----------------
Session 2.41c measured the season-average blend weight w per sport (MLB
about 1.0, NFL 0.8, FIFA 0.65) but shipped one pooled 0.95. Session 2.48
showed the pooled train-fit w moving between 0.85 and 0.95 across folds.
This script asks: does a per-sport w beat the pooled w on legs the fit
never saw?

METHOD
------
Same legs and component rebuild as validate_sigma_held_out.py (imported).
Rolling-origin, four expanding-window folds over the last half of the legs
(test predictions pooled). In each fold, two arms are fit on TRAIN only:
  pooled     one w, then one global sigma factor
  per_sport  a w per sport that has MIN_TRAIN_LEGS_PER_SPORT train legs
             (other sports use the pooled w), then one global factor
Per-stat factors are left out so the test isolates the blend weight.
Compared on TEST Brier with a paired per-leg difference and a
game-clustered standard error. Also prints the per-sport train-fit w in
each fold, to show how stable it is.

USAGE
-----
python scripts/calibration/validate_per_sport_blend.py [--league-cache PATH]
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "estimation"))
import pickem_model as pm  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate_sigma_held_out import (  # noqa: E402
    BLEND_GRID,
    GLOBAL_GRID,
    flagged_prob,
    leg_loss,
    load_data,
    paired,
)

MIN_TRAIN_LEGS_PER_SPORT = 100
MIN_TEST_LEGS_PER_SPORT = 50
CUTS = [0.5, 0.625, 0.75, 0.875, 1.0]


def w_vector(df: pd.DataFrame, w_by_sport: dict, w_default: float) -> np.ndarray:
    return np.array([w_by_sport.get(s, w_default) for s in df["sport"]])


def prob(df: pd.DataFrame, w: np.ndarray, factor: float, k: float) -> np.ndarray:
    """flagged_prob() takes one w; apply it per sport group and reassemble."""
    out = np.empty(len(df))
    ones = np.ones(len(df))
    for wv in np.unique(w):
        m = w == wv
        out[m] = flagged_prob(df.loc[m], float(wv), ones[m] * factor, k)
    return out


def fit_arms(train: pd.DataFrame) -> dict:
    k = pm.SHRINKAGE_PRIOR_STRENGTH_K
    y = train["win"].to_numpy(float)
    ones = np.ones(len(train))
    g0 = pm.SIGMA_CALIBRATION_FACTOR
    w_pool = float(min(BLEND_GRID, key=lambda w: leg_loss(flagged_prob(train, w, ones * g0, k), y).mean()))
    w_sport = {}
    for sport, g in train.groupby("sport"):
        if len(g) < MIN_TRAIN_LEGS_PER_SPORT:
            continue
        gy, go = g["win"].to_numpy(float), np.ones(len(g))
        w_sport[sport] = float(min(BLEND_GRID, key=lambda w: leg_loss(flagged_prob(g, w, go * g0, k), gy).mean()))
    wp = w_vector(train, {}, w_pool)
    ws = w_vector(train, w_sport, w_pool)
    g_pool = float(min(GLOBAL_GRID, key=lambda g: leg_loss(prob(train, wp, g, k), y).mean()))
    g_sport = float(min(GLOBAL_GRID, key=lambda g: leg_loss(prob(train, ws, g, k), y).mean()))
    return {"w_pool": w_pool, "w_sport": w_sport, "g_pool": g_pool, "g_sport": g_sport}


def verdict(m: float, se: float) -> str:
    return "first better" if m + 1.96 * se < 0 else ("second better" if m - 1.96 * se > 0 else "not distinguishable")


def main(cache: str | None) -> None:
    df = load_data(cache)
    n = len(df)
    k = pm.SHRINKAGE_PRIOR_STRENGTH_K
    print(f"Legs: {n}; by sport: {df['sport'].value_counts().to_dict()}")
    ys, cls, sports, pp, ps, pprod = [], [], [], [], [], []
    for lo, hi in zip(CUTS[:-1], CUTS[1:]):
        train, test = df.iloc[: int(n * lo)], df.iloc[int(n * lo): int(n * hi)]
        f = fit_arms(train)
        print(f"  fold train {len(train)} test {len(test)} "
              f"({test['first_flagged_at'].min().date()} to {test['first_flagged_at'].max().date()}): "
              f"pooled w={f['w_pool']:.2f} g={f['g_pool']:.2f}; per-sport w="
              f"{ {s: round(v, 2) for s, v in f['w_sport'].items()} } g={f['g_sport']:.2f}")
        pp.append(prob(test, w_vector(test, {}, f["w_pool"]), f["g_pool"], k))
        ps.append(prob(test, w_vector(test, f["w_sport"], f["w_pool"]), f["g_sport"], k))
        pprod.append(prob(test, w_vector(test, {}, pm.SEASON_AVG_BLEND_WEIGHT), pm.SIGMA_CALIBRATION_FACTOR, k))
        ys.append(test["win"].to_numpy(float))
        cls.append(test["game_id"].astype(str).to_numpy())
        sports.append(test["sport"].to_numpy())
    y, cl, sp = np.concatenate(ys), np.concatenate(cls), np.concatenate(sports)
    P = {"pooled (train-fit)": np.concatenate(pp), "per_sport (train-fit)": np.concatenate(ps),
         "production w=0.95, g=2.681 (in-sample ref)": np.concatenate(pprod)}
    print(f"\nPooled held-out: {len(y)} legs, {len(set(cl))} games, win rate {y.mean():.4f}")
    for name, p in P.items():
        print(f"  {name:<44} brier={leg_loss(p, y).mean():.5f} gap={p.mean() - y.mean():+.4f}")
    a, b = P["per_sport (train-fit)"], P["pooled (train-fit)"]
    m, se = paired(leg_loss(a, y), leg_loss(b, y), cl)
    print(f"\nper_sport vs pooled: diff={m:+.5f} se={se:.5f}  {verdict(m, se)}  (negative = per-sport better)")
    print("By sport (test legs >= %d):" % MIN_TEST_LEGS_PER_SPORT)
    for s in sorted(set(sp)):
        mk = sp == s
        if mk.sum() < MIN_TEST_LEGS_PER_SPORT:
            continue
        m, se = paired(leg_loss(a[mk], y[mk]), leg_loss(b[mk], y[mk]), cl[mk])
        print(f"  {s:<10} n={int(mk.sum()):>5} games={len(set(cl[mk])):>3} diff={m:+.5f} se={se:.5f}  {verdict(m, se)}")


if __name__ == "__main__":
    cache = sys.argv[sys.argv.index("--league-cache") + 1] if "--league-cache" in sys.argv else None
    main(cache)
