"""
Session 2.24 -- Per-Stat-Type Calibration Breakdown (Pick'em)

WHAT THIS SCRIPT IS
--------------------
Session 2.22 fit a single global SIGMA_CALIBRATION_FACTOR = 1.61 against all
8,196 real graded legs combined, closing the aggregate calibration gap to
~0.0008. That aggregate fit could still be masking real, stat-type-specific
miscalibration -- a low-count discrete stat like receptions does not
necessarily behave like a normal distribution the same way a continuous
stat like passing_yards does (a gap named but never checked in
docs/research/pickem_estimation_model_spec.md's "How the probability is
computed" section). Averaging across all stat types could hide a subset
still badly calibrated even after the global fix.

This script is research/measurement only. It does not modify
pickem_model.py. It reuses fit_sigma_recalibration.py's exact method
(recover each leg's z-score from its logged first_flagged_model_prob via
the inverse of pickem_model.normal_cdf(), grid-search a sigma multiplier
minimizing Brier score) but grouped by resolved_stat_key instead of over
the whole population.

METHOD
------
For each resolved_stat_key with at least MIN_GROUP_SIZE (20, matching the
interim floor weekly_review.py already uses elsewhere in this project):

1. BASELINE -- calibration gap and Brier score using the raw, stored
   first_flagged_model_prob values (i.e. before any sigma correction --
   these legs were all flagged before SIGMA_CALIBRATION_FACTOR shipped).
2. GLOBAL-CORRECTED -- what the current production model would have shown
   for this group, i.e. applying the single global k=1.61 factor
   (normal_cdf(z / 1.61)) to every leg in the group. This is the number
   that matters: it answers "does this stat type still have a real gap
   even after the fix everyone is currently relying on."
3. PER-STAT FIT -- an independent grid search of k restricted to this
   group only (same K_GRID_MIN/MAX/STEP as fit_sigma_recalibration.py),
   showing what a stat-type-specific multiplier would look like *if* one
   were warranted.

A group's GLOBAL-CORRECTED gap magnitude past RECALIBRATION_GAP_THRESHOLD
(0.03, same threshold weekly_review.py uses for the post-fit drift check)
is flagged as still-miscalibrated-after-the-global-fix.

CAVEATS THIS SCRIPT DOES NOT PAPER OVER
----------------------------------------
- A per-stat sigma fit is still fitting a NORMAL approximation more
  tightly to each group's data -- it is not a count-data (e.g. Poisson/
  negative-binomial) model. For a low-count discrete stat (receptions,
  targets, attempts, def_sacks, rushing_tds, receiving_tds,
  passing_interceptions, completions), a tighter-fitting k narrows the
  SAME wrong-shaped distribution; it does not fix discreteness itself.
  Any per-stat k proposed for those stats should be read as "best normal
  fit available," not "this stat is now correctly modeled."
- Grid-searching k per group on report is not the same as validating it
  on held-out data. A per-stat k below is a diagnostic finding, not a
  recommendation to ship without a train/test split -- especially for the
  smaller groups (targets: 127, passing_tds: 118, passing_interceptions:
  63, completions: 43, rushing_tds: 27, receiving_tds: 20 are all close to
  or only just past the 20-leg floor; a Brier-minimizing k fit on that few
  points can overfit noise).

USAGE
-----
python scripts/calibration/pickem_calibration_by_stat.py
    Loads data/pickem/outcome_log.csv, prints a table (one row per
    resolved_stat_key with n >= MIN_GROUP_SIZE), does not write any file.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "estimation"))
from pickem_model import SIGMA_CALIBRATION_FACTOR, normal_cdf  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fit_sigma_recalibration import (  # noqa: E402
    K_GRID_MAX,
    K_GRID_MIN,
    K_GRID_STEP,
    brier_score,
    inverse_normal_cdf,
    load_graded_legs,
)

MIN_GROUP_SIZE = 20  # matches weekly_review.py's MIN_GROUP_SIZE_FOR_CHECK
RECALIBRATION_GAP_THRESHOLD = 0.03  # matches weekly_review.py

# Session 2.24 follow-up: the first pass's per-group grid search (bounded by
# fit_sigma_recalibration.py's K_GRID_MAX=3.0, the same ceiling the global
# fit uses) hit that ceiling for two groups (targets,
# rushing_yards+receiving_yards) -- meaning their true best-fit k was only
# lower-bounded, not found. This widened ceiling applies ONLY inside this
# diagnostic script, on a per-group basis, and is not proposed as a change
# to fit_sigma_recalibration.py's own grid (which fits the single global
# factor actually shipped in pickem_model.py).
EXTENDED_K_GRID_MAX = 8.0


def fit_k_for_group(
    z: np.ndarray, outcomes: np.ndarray, k_grid_max: float = K_GRID_MAX
) -> tuple[float, float, bool]:
    """Grid search k (sigma multiplier) minimizing Brier score for one group.
    Returns (best_k, best_brier, hit_ceiling). Same grid as
    fit_sigma_recalibration.py unless k_grid_max is widened by the caller."""
    best_k = 1.0
    best_brier = brier_score(np.array([normal_cdf(zi) for zi in z]), outcomes)
    k = K_GRID_MIN
    while k <= k_grid_max + 1e-9:
        recalibrated = np.array([normal_cdf(zi / k) for zi in z])
        b = brier_score(recalibrated, outcomes)
        if b < best_brier:
            best_brier = b
            best_k = k
        k += K_GRID_STEP
    hit_ceiling = best_k >= k_grid_max - 1e-9
    return best_k, best_brier, hit_ceiling


def analyze_group(stat_key: str, group: pd.DataFrame) -> dict:
    baseline_probs = group["first_flagged_model_prob"].to_numpy()
    outcomes = group["win"].to_numpy()
    z = group["first_flagged_model_prob"].apply(inverse_normal_cdf).to_numpy()

    baseline_gap = float(baseline_probs.mean() - outcomes.mean())
    baseline_brier = brier_score(baseline_probs, outcomes)

    global_corrected_probs = np.array(
        [normal_cdf(zi / SIGMA_CALIBRATION_FACTOR) for zi in z]
    )
    global_gap = float(global_corrected_probs.mean() - outcomes.mean())
    global_brier = brier_score(global_corrected_probs, outcomes)

    per_stat_k, per_stat_brier, hit_ceiling = fit_k_for_group(z, outcomes)
    if hit_ceiling:
        # Re-fit with a widened grid so the reported k is the true optimum,
        # not an artifact of the standard grid's ceiling.
        per_stat_k, per_stat_brier, hit_ceiling = fit_k_for_group(
            z, outcomes, k_grid_max=EXTENDED_K_GRID_MAX
        )
    per_stat_probs = np.array([normal_cdf(zi / per_stat_k) for zi in z])
    per_stat_gap = float(per_stat_probs.mean() - outcomes.mean())

    return {
        "stat_key": stat_key,
        "n": len(group),
        "real_win_rate": float(outcomes.mean()),
        "baseline_gap": baseline_gap,
        "baseline_brier": baseline_brier,
        "global_corrected_gap": global_gap,
        "global_corrected_brier": global_brier,
        "flagged": abs(global_gap) > RECALIBRATION_GAP_THRESHOLD,
        "per_stat_k": per_stat_k,
        "per_stat_gap": per_stat_gap,
        "per_stat_brier": per_stat_brier,
        "per_stat_hit_ceiling": hit_ceiling,
    }


def main() -> None:
    graded = load_graded_legs()
    print(f"Total graded legs with usable model_prob: {len(graded)}")
    print(f"Global SIGMA_CALIBRATION_FACTOR currently in production: {SIGMA_CALIBRATION_FACTOR}")
    print(f"Flag threshold (|global-corrected gap|): {RECALIBRATION_GAP_THRESHOLD}")
    print()

    counts = graded["resolved_stat_key"].value_counts()
    results = []
    skipped = []
    for stat_key, n in counts.items():
        group = graded.loc[graded["resolved_stat_key"] == stat_key]
        if len(group) < MIN_GROUP_SIZE:
            skipped.append((stat_key, len(group)))
            continue
        results.append(analyze_group(stat_key, group))

    header = (
        f"{'stat_key':<45} {'n':>5} {'win%':>7} {'base_gap':>9} {'base_brier':>10} "
        f"{'glob_gap':>9} {'glob_brier':>10} {'flag':>5} {'fit_k':>6} {'fit_gap':>8} {'fit_brier':>10}"
    )
    print(header)
    print("-" * len(header))
    for r in sorted(results, key=lambda x: -abs(x["global_corrected_gap"])):
        k_str = f"{r['per_stat_k']:.3f}" + ("*" if r["per_stat_hit_ceiling"] else "")
        print(
            f"{r['stat_key']:<45} {r['n']:>5} {r['real_win_rate']*100:>6.1f}% "
            f"{r['baseline_gap']:>+9.4f} {r['baseline_brier']:>10.4f} "
            f"{r['global_corrected_gap']:>+9.4f} {r['global_corrected_brier']:>10.4f} "
            f"{'FLAG' if r['flagged'] else '':>5} "
            f"{k_str:>7} {r['per_stat_gap']:>+8.4f} {r['per_stat_brier']:>10.4f}"
        )
    if any(r["per_stat_hit_ceiling"] for r in results):
        print(f"* = still hit the widened grid ceiling ({EXTENDED_K_GRID_MAX}) -- true optimum unresolved")

    if skipped:
        print()
        print(f"Skipped (below {MIN_GROUP_SIZE}-leg floor):")
        for stat_key, n in sorted(skipped, key=lambda x: -x[1]):
            print(f"  {stat_key:<45} n={n}")

    flagged = [r for r in results if r["flagged"]]
    print()
    if flagged:
        print(f"{len(flagged)} stat type(s) flagged past the {RECALIBRATION_GAP_THRESHOLD} threshold:")
        for r in flagged:
            print(
                f"  {r['stat_key']}: global-corrected gap={r['global_corrected_gap']:+.4f} "
                f"(n={r['n']}, real_win_rate={r['real_win_rate']*100:.1f}%)"
            )
    else:
        print("No stat type flagged past threshold -- global fix holds up per-stat-type too.")


if __name__ == "__main__":
    main()
