"""
Session 2.48 -- Held-Out Validation of the Sigma Settings and Blend Weight

WHY THIS EXISTS
----------------
Sessions 2.41c and 2.41d set SIGMA_CALIBRATION_FACTOR = 2.681, 21
SIGMA_CALIBRATION_FACTOR_BY_STAT overrides and SEASON_AVG_BLEND_WEIGHT = 0.95.
All were same-sample Brier-minimizing fits (the same caveat the original 6
overrides carried), never held out. This script applies Session 2.40's
temporal held-out method to them.

METHOD
------
Legs and per-leg components come from the same snapshot join Session 2.47's
refit uses (graded legs joined to retained output/estimation snapshots; raw
sigma recovered as snapshot model_sigma / the factor in force when written;
season_avg, recent_form, games_used, current league_avg for shrinkage k).
Everything is recomputed from components, so any configuration can be scored
on any leg.

Legs are sorted by first_flagged_at; the earliest 70% train, the latest 30%
test. On the TEST set only, compared by Brier score of the flagged side's
Gaussian probability against the real win/loss:
  current   the constants now in pickem_model.py (fit on all data, so this
            is in-sample for the test legs; shown as a reference, not a fair
            competitor)
  refit     every constant re-fit on TRAIN legs only with the same grid
            search: blend weight, then global factor, then a per-stat factor
            for each stat with enough train legs
  global    train-fit blend + train-fit global factor, no per-stat factors
  old       the pre-2.41c configuration (1.61, 0.5/0.5, original 6 overrides)
A paired per-leg loss difference with a game-clustered standard error is
reported for the comparisons that matter. Stats covered by the Session 2.47
isotonic tables are excluded (their final probability is isotonic, not this
Gaussian).

STATED APPROXIMATIONS: same as refit_isotonic_current_config.py (current
league_avg; wind and prior-season blend not reconstructed; the 2-game sigma
floor is not re-derived).

USAGE
-----
python scripts/calibration/validate_sigma_held_out.py [--league-cache PATH]
    --league-cache stores/reads the live league averages (slow to compute).
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "estimation"))
import pickem_model as pm  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
from refit_isotonic_current_config import (  # noqa: E402
    FACTOR_BY_STAT_OLD,
    FACTOR_GLOBAL_OLD,
    factor_in_force,
    load_legs,
    load_snapshots,
)
from fit_shrinkage import compute_league_averages_for_sample  # noqa: E402

TRAIN_FRACTION = 0.70
MIN_TRAIN_LEGS_PER_STAT = 30
MIN_TEST_LEGS_PER_STAT = 15
GLOBAL_GRID = np.arange(0.5, 6.0001, 0.05)
STAT_GRID = np.arange(0.4, 6.0001, 0.05)
BLEND_GRID = np.arange(0.0, 1.0001, 0.05)

_erf = np.vectorize(math.erf)


def p_over(z: np.ndarray) -> np.ndarray:
    return 1.0 - 0.5 * (1.0 + _erf(z / math.sqrt(2.0)))


def load_data(cache: str | None) -> pd.DataFrame:
    snap, _ = load_snapshots()
    j = load_legs(snap)
    if cache and Path(cache).exists():
        league = json.loads(Path(cache).read_text())
    else:
        league = compute_league_averages_for_sample(j)
        if cache:
            Path(cache).write_text(json.dumps(league))
    j["league_avg"] = j["resolved_stat_key"].map(league)
    old_f = np.array([factor_in_force(s, t) for s, t in zip(j["resolved_stat_key"], j["pulled_ts"])])
    j["sigma_raw"] = j["model_sigma"].to_numpy(dtype=float) / old_f
    j["first_flagged_at"] = pd.to_datetime(j["first_flagged_at"], utc=True)
    gid = pd.read_csv(pm.BASE_DIR / "data" / "pickem" / "clv_log.csv", usecols=["flag_id", "game_id"], low_memory=False)
    j = j.merge(gid, on="flag_id", how="left")
    j["game_id"] = j["game_id"].astype(str).where(j["game_id"].notna(), "nogame_" + j["flag_id"].astype(str))

    iso = pd.read_csv(pm.ISOTONIC_CALIBRATION_PATH)
    covered = set(iso.loc[iso["ready_to_apply"] == True, "resolved_stat_key"])  # noqa: E712
    j = j.loc[~j["resolved_stat_key"].isin(covered)].copy()
    return j.sort_values("first_flagged_at").reset_index(drop=True)


def flagged_prob(df: pd.DataFrame, w: float, factor: np.ndarray, k: float) -> np.ndarray:
    raw = w * df["season_avg"].to_numpy(float) + (1 - w) * df["recent_form"].to_numpy(float)
    n = df["games_used"].to_numpy(float)
    la = df["league_avg"].to_numpy(float)
    wt = np.where(np.isnan(la) | (k <= 0), 0.0, k / (n + k))
    mean = np.where(np.isnan(la), raw, (1 - wt) * raw + wt * la)
    z = (df["line"].to_numpy(float) - mean) / (df["sigma_raw"].to_numpy(float) * factor)
    po = p_over(z)
    return np.where(df["flagged_side"].to_numpy() == "over", po, 1.0 - po)


def leg_loss(p: np.ndarray, y: np.ndarray) -> np.ndarray:
    return (p - y) ** 2


def stat_factors(df: pd.DataFrame, table: dict, default: float) -> np.ndarray:
    return np.array([table.get(s, default) for s in df["resolved_stat_key"]])


def fit_train(train: pd.DataFrame) -> dict:
    y = train["win"].to_numpy(float)
    k = pm.SHRINKAGE_PRIOR_STRENGTH_K
    ones = np.ones(len(train))
    # blend weight first (at the current global factor), then the global
    # factor at that weight, then per-stat factors -- coordinate fit.
    best_w = min(BLEND_GRID, key=lambda w: leg_loss(
        flagged_prob(train, w, ones * pm.SIGMA_CALIBRATION_FACTOR, k), y).mean())
    best_g = min(GLOBAL_GRID, key=lambda g: leg_loss(
        flagged_prob(train, best_w, ones * g, k), y).mean())
    per_stat = {}
    for stat, g in train.groupby("resolved_stat_key"):
        if len(g) < MIN_TRAIN_LEGS_PER_STAT:
            continue
        gy = g["win"].to_numpy(float)
        gones = np.ones(len(g))
        per_stat[stat] = float(min(STAT_GRID, key=lambda f: leg_loss(
            flagged_prob(g, best_w, gones * f, k), gy).mean()))
    return {"w": float(best_w), "global": float(best_g), "per_stat": per_stat}


def paired(a: np.ndarray, b: np.ndarray, clusters: np.ndarray) -> tuple[float, float]:
    """Mean of (a - b) per leg and its game-clustered standard error."""
    d = a - b
    n = len(d)
    m = d.mean()
    s = pd.Series(d - m).groupby(clusters).sum().to_numpy()
    c = len(s)
    se = math.sqrt((c / max(c - 1, 1)) * float((s ** 2).sum()) / n ** 2)
    return float(m), se



def rolling_origin(df: pd.DataFrame) -> None:
    """Four expanding-window temporal folds (train on everything before the
    test block; test blocks are consecutive 12.5% slices of the last half),
    with test predictions pooled. Less dependent on a single cut than the
    70/30 split, which here has a test window of only two days."""
    k = pm.SHRINKAGE_PRIOR_STRENGTH_K
    n = len(df)
    cuts = [0.5, 0.625, 0.75, 0.875, 1.0]
    pooled = {name: [] for name in ["current", "refit_per_stat", "refit_global", "current_global", "old"]}
    ys, cls, stats_, per = [], [], [], []
    for lo, hi in zip(cuts[:-1], cuts[1:]):
        train, test = df.iloc[: int(n * lo)], df.iloc[int(n * lo): int(n * hi)]
        fit = fit_train(train)
        y = test["win"].to_numpy(float)

        def cfg(w, table, default, k_=k):
            return flagged_prob(test, w, stat_factors(test, table, default), k_)

        pooled["current"].append(cfg(pm.SEASON_AVG_BLEND_WEIGHT, pm.SIGMA_CALIBRATION_FACTOR_BY_STAT, pm.SIGMA_CALIBRATION_FACTOR))
        pooled["refit_per_stat"].append(cfg(fit["w"], fit["per_stat"], fit["global"]))
        pooled["refit_global"].append(cfg(fit["w"], {}, fit["global"]))
        pooled["current_global"].append(cfg(pm.SEASON_AVG_BLEND_WEIGHT, {}, pm.SIGMA_CALIBRATION_FACTOR))
        pooled["old"].append(cfg(0.5, FACTOR_BY_STAT_OLD, FACTOR_GLOBAL_OLD, 0.0))
        ys.append(y)
        cls.append(test["game_id"].astype(str).to_numpy())
        stats_.append(test["resolved_stat_key"].to_numpy())
        print(f"  fold train<{int(n*lo)} test {len(test)} legs "
              f"({test['first_flagged_at'].min().date()} to {test['first_flagged_at'].max().date()}, "
              f"{test['game_id'].nunique()} games): train-fit blend {fit['w']:.2f}, global {fit['global']:.2f}")
    y = np.concatenate(ys)
    cl = np.concatenate(cls)
    st = np.concatenate(stats_)
    P = {k_: np.concatenate(v) for k_, v in pooled.items()}
    print(f"\nROLLING-ORIGIN pooled held-out: {len(y)} legs, {len(set(cl))} games, win rate {y.mean():.4f}")
    for name, pr in P.items():
        print(f"  {name:<18} brier={leg_loss(pr, y).mean():.5f} gap={pr.mean() - y.mean():+.4f}")
    print("Paired differences (negative = first better), game-clustered SE:")
    for label, a, b in [("current vs old", "current", "old"),
                        ("current per-stat vs current global-only", "current", "current_global"),
                        ("refit per-stat vs refit global-only", "refit_per_stat", "refit_global"),
                        ("current vs refit per-stat", "current", "refit_per_stat")]:
        m, se = paired(leg_loss(P[a], y), leg_loss(P[b], y), cl)
        v = "first better" if m + 1.96 * se < 0 else ("second better" if m - 1.96 * se > 0 else "not distinguishable")
        print(f"  {label:<42} diff={m:+.5f} se={se:.5f}  {v}")
    print("Per overridden stat, pooled held-out (override vs current global factor):")
    L_over, L_glob = leg_loss(P["current"], y), leg_loss(P["current_global"], y)
    rows = []
    for stat in pm.SIGMA_CALIBRATION_FACTOR_BY_STAT:
        m_ = st == stat
        if m_.sum() < 15:
            continue
        d, se = paired(L_over[m_], L_glob[m_], cl[m_])
        rows.append((stat, int(m_.sum()), pm.SIGMA_CALIBRATION_FACTOR_BY_STAT[stat], d, se))
    for stat, cnt, f_, d, se in sorted(rows, key=lambda r: r[3]):
        v = "override better" if d + 1.96 * se < 0 else ("global better" if d - 1.96 * se > 0 else "-")
        print(f"  {stat:<34} n={cnt:>4} factor={f_:<6} diff={d:+.4f} se={se:.4f}  {v}")
    print(f"  overrides better by >1.96 SE: {sum(1 for r in rows if r[3] + 1.96*r[4] < 0)}; "
          f"global better by >1.96 SE: {sum(1 for r in rows if r[3] - 1.96*r[4] > 0)}; of {len(rows)} testable")


def main(cache: str | None) -> None:
    df = load_data(cache)
    print("ROLLING-ORIGIN FOLDS")
    rolling_origin(df)
    print("\nSINGLE 70/30 SPLIT")
    n = len(df)
    split = int(n * TRAIN_FRACTION)
    train, test = df.iloc[:split].copy(), df.iloc[split:].copy()
    print(f"Legs (isotonic-covered stats excluded): {n}; train {len(train)} "
          f"({train['first_flagged_at'].min().date()} to {train['first_flagged_at'].max().date()}), "
          f"test {len(test)} ({test['first_flagged_at'].min().date()} to {test['first_flagged_at'].max().date()})")
    print(f"Distinct games: train {train['game_id'].nunique()}, test {test['game_id'].nunique()}")

    fit = fit_train(train)
    print(f"\nTrain-only fit: blend w={fit['w']:.2f}, global factor={fit['global']:.3f}, "
          f"{len(fit['per_stat'])} per-stat factors")
    print(f"Current production: blend w={pm.SEASON_AVG_BLEND_WEIGHT}, global factor="
          f"{pm.SIGMA_CALIBRATION_FACTOR}, {len(pm.SIGMA_CALIBRATION_FACTOR_BY_STAT)} per-stat overrides")

    k = pm.SHRINKAGE_PRIOR_STRENGTH_K
    y = test["win"].to_numpy(float)
    cl = test["game_id"].astype(str).to_numpy()

    def cfg(w, table, default, k_=k):
        return flagged_prob(test, w, stat_factors(test, table, default), k_)

    p = {
        "current (in-sample ref)": cfg(pm.SEASON_AVG_BLEND_WEIGHT, pm.SIGMA_CALIBRATION_FACTOR_BY_STAT,
                                       pm.SIGMA_CALIBRATION_FACTOR),
        "refit on train, per-stat": cfg(fit["w"], fit["per_stat"], fit["global"]),
        "refit on train, global only": cfg(fit["w"], {}, fit["global"]),
        "current global, no overrides": cfg(pm.SEASON_AVG_BLEND_WEIGHT, {}, pm.SIGMA_CALIBRATION_FACTOR),
        "old (1.61, 0.5, orig 6)": cfg(0.5, FACTOR_BY_STAT_OLD, FACTOR_GLOBAL_OLD, 0.0),
        "no calibration (factor 1)": cfg(pm.SEASON_AVG_BLEND_WEIGHT, {}, 1.0),
    }
    print("\nHELD-OUT (test set) Brier, and mean prob - win rate (calibration gap):")
    for name, pr in p.items():
        print(f"  {name:<32} brier={leg_loss(pr, y).mean():.5f}  gap={pr.mean() - y.mean():+.4f}")
    print(f"  (test win rate {y.mean():.4f}, n={len(y)})")

    print("\nPaired held-out differences (negative = first is better), game-clustered SE:")
    pairs = [
        ("current vs old", "current (in-sample ref)", "old (1.61, 0.5, orig 6)"),
        ("current vs refit-per-stat", "current (in-sample ref)", "refit on train, per-stat"),
        ("refit per-stat vs refit global-only", "refit on train, per-stat", "refit on train, global only"),
        ("current per-stat vs current global-only", "current (in-sample ref)", "current global, no overrides"),
        ("current global-only vs factor 1", "current global, no overrides", "no calibration (factor 1)"),
    ]
    for label, a, b in pairs:
        m, se = paired(leg_loss(p[a], y), leg_loss(p[b], y), cl)
        verdict = "first better" if m + 1.96 * se < 0 else ("second better" if m - 1.96 * se > 0 else "not distinguishable")
        print(f"  {label:<42} diff={m:+.5f} se={se:.5f}  {verdict}")

    print("\nPer stat, held-out Brier: production override vs current global 2.681 vs train-refit factor")
    print(f"  {'stat':<34}{'n_test':>7}{'override':>10}{'global':>9}{'refit':>9}{'prod_f':>8}{'refit_f':>8}")
    rows = []
    for stat, g in test.groupby("resolved_stat_key"):
        if len(g) < MIN_TEST_LEGS_PER_STAT:
            continue
        gy = g["win"].to_numpy(float)
        one = np.ones(len(g))
        prod_f = pm.SIGMA_CALIBRATION_FACTOR_BY_STAT.get(stat)
        ref_f = fit["per_stat"].get(stat)
        b_glob = leg_loss(flagged_prob(g, pm.SEASON_AVG_BLEND_WEIGHT, one * pm.SIGMA_CALIBRATION_FACTOR, k), gy).mean()
        b_over = leg_loss(flagged_prob(g, pm.SEASON_AVG_BLEND_WEIGHT, one * prod_f, k), gy).mean() if prod_f else np.nan
        b_ref = leg_loss(flagged_prob(g, fit["w"], one * ref_f, k), gy).mean() if ref_f else np.nan
        rows.append((stat, len(g), b_over, b_glob, b_ref, prod_f, ref_f))
    for stat, m_, bo, bg, br, pf, rf in sorted(rows, key=lambda r: -r[1]):
        f = lambda v: "" if v is None or (isinstance(v, float) and np.isnan(v)) else f"{v:.4f}"
        print(f"  {stat:<34}{m_:>7}{f(bo):>10}{bg:>9.4f}{f(br):>9}{'' if pf is None else pf:>8}"
              f"{'' if rf is None else round(rf, 2):>8}")
    ov = [r for r in rows if r[2] == r[2]]
    if ov:
        wins = sum(1 for r in ov if r[2] < r[3])
        print(f"\nOverridden stats with a test check: {len(ov)}; override beats the global factor "
              f"held-out for {wins} of them.")
    nov = [r for r in rows if r[5] is None]
    if nov:
        better = [(r[0], r[3], r[4], r[6]) for r in nov if r[4] == r[4] and r[4] < r[3]]
        print(f"Stats WITHOUT an override scored on the global factor: {len(nov)}; a train-fit factor beats it "
              f"held-out for {len(better)}: {[b[0] for b in better]}")


if __name__ == "__main__":
    cache = sys.argv[sys.argv.index("--league-cache") + 1] if "--league-cache" in sys.argv else None
    main(cache)
