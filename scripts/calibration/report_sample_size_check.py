"""
Session 2.57 -- Empirical check of the "full sample" threshold.

WHAT THIS IS
Read-only report. It answers: how many graded PrizePicks legs do we need
before a win-rate verdict is trustworthy, given how the real legs behave?
It prints (1) the design effect measured on real graded legs, (2) each
slice's win rate with a game-clustered 95% interval against the per-leg
breakeven of every Standard entry size, and (3) the legs and games needed
to detect a target true win rate at the measured design effect.

WHY IT EXISTS
docs/sample_size_methodology.md derived 3,725 legs assuming every leg is
independent. Legs from one game share weather, lineups and game flow, so
they are not. The design effect (DEFF) is how many times larger the real
variance is than the independent-leg variance. Measured here: about 3.5 for
PrizePicks Standard.

RUN
python scripts/calibration/report_sample_size_check.py
Writes nothing. Safe to run any time.
"""

from __future__ import annotations

import sys
from math import sqrt
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parents[0] / "sizing"))

import pickem_model_validity_audit as audit  # noqa: E402
from sizing_engine import PICKEM_ENTRY_PAYOUT, breakeven_win_rate_per_leg  # noqa: E402

Z_ALPHA = 1.96   # two-sided 5% false-positive rate
Z_POWER = 0.84   # 80% power
TARGET_TRUE_WIN_RATE = 0.60   # the accuracy the model's flags need to show
REFERENCE_ENTRY_LEGS = 5      # the hurdle used by the dashboards; see doc
MIN_GAMES_FOR_VERDICT = 30    # below this, clustered intervals are unreliable


def independent_n(p0: float, p1: float) -> float:
    """Legs needed if every leg were independent (one-sample test)."""
    num = (Z_ALPHA * sqrt(p0 * (1 - p0)) + Z_POWER * sqrt(p1 * (1 - p1))) ** 2
    return num / (p1 - p0) ** 2


def design_effect(y: np.ndarray, clusters: np.ndarray) -> tuple[float, int]:
    """Clustered variance divided by independent-leg variance."""
    n = len(y)
    p = y.mean()
    residual = y - p
    sums = pd.Series(residual).groupby(clusters).sum().to_numpy()
    c = len(sums)
    if c < 2 or p in (0.0, 1.0):
        return float("nan"), c
    clustered_var = (c / (c - 1)) * float(np.sum(sums**2)) / n**2
    return clustered_var / (p * (1 - p) / n), c


def main() -> None:
    df = audit.graded_only(audit.load_joined())
    df["y"] = (df["result"] == "win").astype(float)
    game = df["game_id"].astype(str).where(df["game_id"].notna(), "na_" + df.index.astype(str))
    df["cluster"] = game
    pp = df[(df["platform"] == "prizepicks") & (df["odds_bucket"] == "standard")]

    hurdles = {n: breakeven_win_rate_per_leg("prizepicks", n) for n in sorted(PICKEM_ENTRY_PAYOUT["prizepicks"])}
    print("Per-leg breakeven by all-Standard entry size:",
          {n: round(h, 4) for n, h in hurdles.items()})

    print("\n1. Win rate, game-clustered 95% interval, and design effect (PrizePicks Standard)")
    print(f"{'slice':16s}{'legs':>7s}{'games':>7s}{'win%':>8s}{'CI low':>8s}{'CI high':>9s}{'DEFF':>6s}  verdict vs 5-pick / 6-pick")
    slices = [("all", pp)] + [(f"sport={s}", g) for s, g in pp.groupby("sport")] + \
             [(f"side={s}", g) for s, g in pp.groupby("flagged_side")]
    for name, g in slices:
        if len(g) < 100:
            continue
        y = g["y"].to_numpy()
        lo, hi, games = audit.clustered_ci(y, g["cluster"].to_numpy())
        deff, _ = design_effect(y, g["cluster"].to_numpy())
        def verdict(h: float) -> str:
            return "below" if hi < h else "above" if lo > h else "inconclusive"
        note = "" if games >= MIN_GAMES_FOR_VERDICT else "  (few games: interval unreliable)"
        print(f"{name:16s}{len(g):7d}{games:7d}{y.mean()*100:8.1f}{lo*100:8.1f}{hi*100:9.1f}{deff:6.2f}  "
              f"{verdict(hurdles[5])} / {verdict(hurdles[6])}{note}")

    y_all = pp["y"].to_numpy()
    deff_all, games_all = design_effect(y_all, pp["cluster"].to_numpy())
    legs_per_game = len(pp) / games_all
    print(f"\n2. Measured design effect {deff_all:.2f}; {legs_per_game:.1f} legs per game. "
          f"{len(pp)} legs carry the information of about {len(pp)/deff_all:.0f} independent legs.")

    print(f"\n3. Legs and games needed to detect a true win rate of {TARGET_TRUE_WIN_RATE:.0%} "
          f"(5% false positive, 80% power, DEFF {deff_all:.2f})")
    print(f"{'entry':>6s}{'hurdle':>8s}{'independent legs':>18s}{'real legs':>11s}{'games':>7s}")
    for n, h in hurdles.items():
        if h >= TARGET_TRUE_WIN_RATE:
            print(f"{n:>6d}{h:8.4f}{'target is below hurdle':>36s}")
            continue
        ind = independent_n(h, TARGET_TRUE_WIN_RATE)
        print(f"{n:>6d}{h:8.4f}{ind:18.0f}{ind*deff_all:11.0f}{ind*deff_all/legs_per_game:7.0f}")


if __name__ == "__main__":
    main()
