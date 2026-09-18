"""
Session 2.44 follow-up v3 -- leg-level probability check of a 2024 blend.

The 395 graded NFL receiving_yards/receptions legs were scored using the full
2025 season as history, so this tests blending each player's 2024 per-game
average into that 2025-based mean: mean' = (n/(n+k))*model_mean + (k/(n+k))*
prior_2024, n = games_used, sigma held fixed. Brier is scored on the side that
was flagged, against the real win/loss (line vs actual, no money involved).
k is fit on the earliest 70% of legs and evaluated on the latest 30%.
Indirect evidence only: production will blend 2025 into 2026 games.
Research-only; writes nothing.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "estimation"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import fit_shrinkage as fs  # noqa: E402
from pickem_model import build_name_lookup, normal_cdf, normalize_name  # noqa: E402
from pickem_sport_plugins.nfl import NFL_PLUGIN  # noqa: E402

STATS = ["receiving_yards", "receptions"]
K_GRID = [0.0, 1, 2, 4, 6, 8, 12, 20, 40]


def probs(df: pd.DataFrame, k: float) -> np.ndarray:
    n = df["games_used"].to_numpy(float)
    prior = df["prior"].to_numpy(float)
    mean = df["model_mean"].to_numpy(float)
    if k > 0:
        w = np.where(np.isnan(prior), 0.0, k / (n + k))
        mean = (1 - w) * mean + w * np.nan_to_num(prior)
    z = (df["line"].to_numpy(float) - mean) / df["model_sigma"].to_numpy(float)
    p_over = np.array([1.0 - normal_cdf(x) for x in z])
    return np.where(df["flagged_side"].to_numpy() == "over", p_over, 1.0 - p_over)


def brier(df: pd.DataFrame, k: float) -> float:
    return float(np.mean((probs(df, k) - df["win"].to_numpy()) ** 2))


def main() -> None:
    fs.load_excluded_stats = lambda: set()
    snap, _ = fs.load_snapshots()
    j = fs.load_joined_legs(snap)
    legs = j[(j["sport"].str.lower() == "nfl") & j["resolved_stat_key"].isin(STATS)].copy()

    d24 = NFL_PLUGIN.fetch_stats(2024)
    lookup = build_name_lookup(d24)
    means = d24.groupby("player_id")[STATS].mean()
    pid = legs["player_name"].map(lambda n: lookup.get(normalize_name(n)))
    legs["prior"] = [
        means.at[p, s] if p in means.index else np.nan for p, s in zip(pid, legs["resolved_stat_key"])
    ]
    print(f"Legs: {len(legs)}; with a 2024 prior: {legs['prior'].notna().sum()}")
    legs = legs.sort_values("first_flagged_at").reset_index(drop=True)
    cut = int(len(legs) * 0.7)
    train, test = legs.iloc[:cut], legs.iloc[cut:]

    print("\nBrier by k (lower is better), k=0 is current production:")
    for k in K_GRID:
        print(f"  k={k:<4} train {brier(train, k):.6f}  test {brier(test, k):.6f}  all {brier(legs, k):.6f}")
    best = min(K_GRID, key=lambda k: brier(train, k))
    print(f"\nFit on train: k={best}. Held-out Brier {brier(test, 0):.6f} -> {brier(test, best):.6f}")
    for s in STATS:
        t = test[test["resolved_stat_key"] == s]
        print(f"  {s:<16} n={len(t):>3}  {brier(t, 0):.6f} -> {brier(t, best):.6f}")
    with_prior = test[test["prior"].notna()]
    print(f"  only legs with a prior n={len(with_prior)}  {brier(with_prior, 0):.6f} -> {brier(with_prior, best):.6f}")


if __name__ == "__main__":
    main()
