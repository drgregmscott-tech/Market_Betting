"""
Session 2.40 -- Distribution-Shape Fix: Isotonic (Nonparametric) Calibration
Per-Stat, Replacing the Gaussian-Shape Assumption Where It's Confirmed Wrong

WHY THIS EXISTS
----------------
Session 2.37's full audit confirmed, directly against real graded
`actual_value`s, that many stats this project flags are zero-inflated or
heavily right-skewed (MLB home runs: 89.3% real zero-rate; stolen bases
88.1%; RBI 70.7%; NFL def_sacks 77.2%; receiving_yards real skew +1.54;
30 of 49 checked sport/stat cells flagged non-Gaussian in total). prob_over()
(pickem_model.py:546) is a plain normal-distribution CDF -- no sigma
multiplier, however well fit, changes the SHAPE of that curve, only its
width. A zero-inflated stat's real win/loss curve as a function of z-score
does not look like a normal CDF, no matter how sigma is tuned.

WHY ISOTONIC REGRESSION, NOT A NEGATIVE-BINOMIAL/ZERO-INFLATED-POISSON FIT
------------------------------------------------------------------------------
The obvious alternative is to model the stat's real count distribution
directly (negative binomial, zero-inflated Poisson). That requires
choosing and fitting a specific parametric family per stat -- exactly the
kind of "guessed, unnamed" modeling choice this project's own standard
tries to avoid, and it would need real per-stat validation before trusting
it. Isotonic regression sidesteps this: it makes NO assumption about the
outcome distribution's shape at all -- it only assumes the model's
existing z-score correctly RANKS legs from least to most likely to win
(the mean-estimation part of the model, which nothing in Session 2.37
questioned), and fits the loosest possible monotonic curve mapping that
rank to a real, empirical win rate (via the standard pool-adjacent-
violators algorithm, PAVA -- reimplemented here directly in numpy, no new
dependency). This is standard ML practice for exactly this failure mode
(a scoring function that ranks well but whose probability SCALE is
miscalibrated in a shape-dependent, not just uniformly-shifted, way) --
Platt scaling assumes a sigmoid-shaped correction; isotonic regression
assumes nothing but monotonicity, which is the more defensible choice when
the miscalibration's own shape (zero-inflation) is not sigmoid-like.

A REAL, USEFUL PROPERTY: THIS IS ROBUST TO SIGMA_CALIBRATION_FACTOR'S OWN
PROBLEMS
------------------------------------------------------------------------------
Session 2.37's own open items flagged that SIGMA_CALIBRATION_FACTOR=1.61
(pickem_model.py:278) was fit (Session 2.22) on an 8,196-leg sample from
BEFORE the 2026-09-17 dedup/closing-line fix -- likely contaminated by the
exact same measurement bugs and distribution-shape artifacts this session
is investigating. That contamination does not undermine THIS fix: isotonic
regression only depends on the RANK ORDER of z-scores within a stat group,
and rescaling every leg's sigma by the same constant factor (which is what
SIGMA_CALIBRATION_FACTOR does -- it is applied uniformly to every stat
except the 6 SIGMA_CALIBRATION_FACTOR_BY_STAT overrides) never changes
that rank order. Whatever sigma factor was in effect when a leg's stored
first_flagged_model_prob was computed, the isotonic fit below recovers and
uses only its rank-preserving z-score, so a wrong historical sigma factor
does not bias this fit -- it only would have biased the (now-superseded)
raw baseline probability, which this fit corrects for exactly by design.

METHOD
------
1. Load every graded leg with a usable first_flagged_model_prob (reuses
   fit_sigma_recalibration.load_graded_legs()).
2. Recover each leg's z-score via the same inverse_normal_cdf() round-trip
   fit_sigma_recalibration.py already uses.
3. Per resolved_stat_key with n >= MIN_GROUP_SIZE_FOR_DIAGNOSTIC (30,
   matching this project's interim-evidence floor elsewhere), fit an
   isotonic regression of real win/loss (0/1) on z via PAVA.
4. Compare Brier score: baseline (raw stored probability) vs. the current
   production global-sigma-corrected probability vs. this isotonic fit,
   IN-SAMPLE (same caveat fit_sigma_recalibration.py already states for
   its own fit -- this is a diagnostic fit, not validated on held-out
   data; do not treat a good in-sample Brier score alone as proof this
   generalizes).
5. **Held-out validation, not just in-sample Brier (added after the first
   run of this script found isotonic "improves" 47/47 stats in-sample --
   expected by construction, since isotonic regression is the L2-optimal
   fit against whatever sample it is given; that number alone is not
   evidence of generalization and is not reported as if it were).** Each
   stat's graded legs are joined back to clv_log.csv for their real
   first_flagged_at timestamp, sorted chronologically, and split
   70%-train / 30%-test (a temporal split, matching how this system
   actually operates -- fit on the past, apply going forward -- not a
   random k-fold, which would leak future information backward). The
   isotonic step function is fit on the TRAIN legs only, then evaluated
   (Brier score) against the real outcomes of the TEST legs only, and
   compared against the current production global-sigma-corrected
   probability's Brier score on that SAME held-out test set. Only a real,
   held-out improvement is evidence this generalizes.
6. Writes every stat's FULL-SAMPLE fitted step function (z breakpoints +
   calibrated probability per block, fit on all graded legs, not just the
   70% train split -- the split above is for honest evaluation only) to
   data/pickem/isotonic_calibration_by_stat.csv -- a stat is marked
   ready_to_apply=True only once it (a) clears n >=
   MIN_GROUP_SIZE_FOR_PRODUCTION (200 -- deliberately higher than the
   30-leg diagnostic floor, since a nonparametric step-function fit has
   many more effective degrees of freedom than a single scalar like
   SIGMA_CALIBRATION_FACTOR and can overfit a small group's noise) AND
   (b) actually improved Brier score on the HELD-OUT test split, not just
   in-sample.

USAGE
-----
python scripts/calibration/fit_isotonic_calibration.py
    Prints the per-stat comparison table and writes
    data/pickem/isotonic_calibration_by_stat.csv. Does not modify
    pickem_model.py -- applying a fitted table to live scoring is a
    separate, deliberate step (pickem_model.py's apply_isotonic_calibration()),
    matching fit_sigma_recalibration.py's own "no silent recalibration"
    precedent.
"""

from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "estimation"))
from pickem_model import SIGMA_CALIBRATION_FACTOR, normal_cdf  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fit_sigma_recalibration import (  # noqa: E402
    brier_score,
    inverse_normal_cdf,
    load_graded_legs,
)

BASE_DIR = Path(__file__).resolve().parents[2]
CLV_LOG_PATH = BASE_DIR / "data" / "pickem" / "clv_log.csv"
OUT_PATH = BASE_DIR / "data" / "pickem" / "isotonic_calibration_by_stat.csv"

MIN_GROUP_SIZE_FOR_DIAGNOSTIC = 30  # matches this project's interim-evidence floor elsewhere
MIN_GROUP_SIZE_FOR_PRODUCTION = 200  # higher bar -- a step-function fit overfits small n easily
TRAIN_FRACTION = 0.70  # temporal split -- earliest-flagged legs train, most recent test


def isotonic_regression(x: np.ndarray, y: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Pool-adjacent-violators algorithm (PAVA): the L2-optimal
    non-decreasing fit of y as a function of x, x already sorted
    ascending. Returns (block_x_lo, block_x_hi, block_value) -- one row
    per merged block, monotonically non-decreasing in block_value. Pure
    numpy, no new dependency (equivalent to sklearn.isotonic.IsotonicRegression,
    reimplemented directly per this project's stated no-new-dependency
    posture, e.g. pickem_model.py's own normal_cdf() via math.erf instead
    of scipy)."""
    n = len(y)
    block_val = list(y.astype(float))
    block_w = [1.0] * n
    block_lo = list(range(n))
    block_hi = list(range(n))

    i = 0
    stack_val: list[float] = []
    stack_w: list[float] = []
    stack_lo: list[int] = []
    stack_hi: list[int] = []
    for i in range(n):
        stack_val.append(block_val[i])
        stack_w.append(block_w[i])
        stack_lo.append(block_lo[i])
        stack_hi.append(block_hi[i])
        while len(stack_val) > 1 and stack_val[-2] > stack_val[-1]:
            v2, w2, lo2, hi2 = stack_val.pop(), stack_w.pop(), stack_lo.pop(), stack_hi.pop()
            v1, w1, lo1, hi1 = stack_val.pop(), stack_w.pop(), stack_lo.pop(), stack_hi.pop()
            merged_v = (v1 * w1 + v2 * w2) / (w1 + w2)
            stack_val.append(merged_v)
            stack_w.append(w1 + w2)
            stack_lo.append(lo1)
            stack_hi.append(hi2)

    block_x_lo = np.array([x[i] for i in stack_lo])
    block_x_hi = np.array([x[i] for i in stack_hi])
    block_value = np.array(stack_val)
    return block_x_lo, block_x_hi, block_value


def expand_fitted(x: np.ndarray, block_x_lo: np.ndarray, block_x_hi: np.ndarray, block_value: np.ndarray) -> np.ndarray:
    """In-sample fitted value for every original (sorted) x -- one value
    per row, for Brier-score comparison against the real outcomes."""
    out = np.empty(len(x))
    idx = 0
    for lo, hi, val in zip(block_x_lo, block_x_hi, block_value):
        count = int(np.searchsorted(x, hi, side="right") - idx)
        out[idx: idx + count] = val
        idx += count
    return out


def predict_isotonic(
    z_query: np.ndarray, block_lo: np.ndarray, block_hi: np.ndarray, block_val: np.ndarray
) -> np.ndarray:
    """Out-of-sample prediction from a fitted step function -- for each
    query z, finds which training block it falls into (flat extrapolation
    beyond the training range, the standard isotonic-regression
    convention: a z below every training block gets the lowest block's
    value, a z above every training block gets the highest block's)."""
    edges = block_hi[:-1]  # right edge of each block except the last
    idx = np.searchsorted(edges, z_query, side="right")
    idx = np.clip(idx, 0, len(block_val) - 1)
    return block_val[idx]


def load_graded_legs_with_timestamp() -> pd.DataFrame:
    """load_graded_legs() plus the leg's real first_flagged_at (from
    clv_log.csv, joined on flag_id) -- needed for a real temporal
    train/test split, not available in outcome_log.csv itself."""
    graded = load_graded_legs()
    clv = pd.read_csv(CLV_LOG_PATH, low_memory=False, usecols=["flag_id", "first_flagged_at"])
    merged = graded.merge(clv, on="flag_id", how="left")
    return merged.dropna(subset=["first_flagged_at"])


def fit_stat(stat_key: str, group: pd.DataFrame) -> dict:
    group = group.sort_values("first_flagged_at")
    z_all = group["first_flagged_model_prob"].apply(inverse_normal_cdf).to_numpy()
    outcomes_all = group["win"].to_numpy()
    baseline_all = group["first_flagged_model_prob"].to_numpy()

    n = len(group)
    split = int(n * TRAIN_FRACTION)
    # A temporal split needs both sides non-trivial to mean anything.
    can_validate = split >= MIN_GROUP_SIZE_FOR_DIAGNOSTIC and (n - split) >= 10

    held_out_result = None
    if can_validate:
        train_z, test_z = z_all[:split], z_all[split:]
        train_y, test_y = outcomes_all[:split], outcomes_all[split:]
        test_baseline = baseline_all[split:]

        train_order = np.argsort(train_z)
        block_lo_tr, block_hi_tr, block_val_tr = isotonic_regression(
            train_z[train_order], train_y[train_order]
        )
        test_order = np.argsort(test_z)
        test_z_sorted = test_z[test_order]
        test_y_sorted = test_y[test_order]
        test_baseline_sorted = test_baseline[test_order]

        iso_pred_test = predict_isotonic(test_z_sorted, block_lo_tr, block_hi_tr, block_val_tr)
        global_pred_test = np.array([normal_cdf(zi / SIGMA_CALIBRATION_FACTOR) for zi in test_z_sorted])

        held_out_result = {
            "n_train": len(train_z), "n_test": len(test_z),
            "held_out_baseline_brier": brier_score(test_baseline_sorted, test_y_sorted),
            "held_out_global_brier": brier_score(global_pred_test, test_y_sorted),
            "held_out_isotonic_brier": brier_score(iso_pred_test, test_y_sorted),
        }
        held_out_result["isotonic_beats_global_held_out"] = (
            held_out_result["held_out_isotonic_brier"] < held_out_result["held_out_global_brier"]
        )

    # Full-sample fit (what actually gets exported/applied) -- in-sample
    # Brier reported alongside for transparency, but the held-out numbers
    # above are what should drive the ready_to_apply decision.
    order = np.argsort(z_all)
    z_sorted, outcomes_sorted = z_all[order], outcomes_all[order]
    baseline_sorted = baseline_all[order]
    baseline_brier = brier_score(baseline_sorted, outcomes_sorted)
    global_corrected = np.array([normal_cdf(zi / SIGMA_CALIBRATION_FACTOR) for zi in z_sorted])
    global_brier = brier_score(global_corrected, outcomes_sorted)
    block_lo, block_hi, block_val = isotonic_regression(z_sorted, outcomes_sorted)
    fitted = expand_fitted(z_sorted, block_lo, block_hi, block_val)
    isotonic_brier = brier_score(fitted, outcomes_sorted)

    ready = (
        n >= MIN_GROUP_SIZE_FOR_PRODUCTION
        and held_out_result is not None
        and held_out_result["isotonic_beats_global_held_out"]
    )

    return {
        "stat_key": stat_key,
        "n": n,
        "real_win_rate": float(outcomes_sorted.mean()),
        "baseline_brier": baseline_brier,
        "global_corrected_brier": global_brier,
        "isotonic_brier": isotonic_brier,
        "n_blocks": len(block_val),
        "block_lo": block_lo, "block_hi": block_hi, "block_val": block_val,
        "held_out": held_out_result,
        "ready_to_apply": ready,
    }


def main() -> None:
    graded = load_graded_legs_with_timestamp()
    print(f"Total graded legs with usable model_prob and a real first_flagged_at: {len(graded)}")
    print(f"Production SIGMA_CALIBRATION_FACTOR: {SIGMA_CALIBRATION_FACTOR}")
    print(f"Diagnostic floor: {MIN_GROUP_SIZE_FOR_DIAGNOSTIC} legs | "
          f"Production-ready floor: {MIN_GROUP_SIZE_FOR_PRODUCTION} legs")
    print()

    counts = graded["resolved_stat_key"].value_counts()
    results = []
    for stat_key, n in counts.items():
        if n < MIN_GROUP_SIZE_FOR_DIAGNOSTIC:
            continue
        group = graded.loc[graded["resolved_stat_key"] == stat_key]
        results.append(fit_stat(stat_key, group))

    header = (
        f"{'stat_key':<38} {'n':>6} {'win%':>6} {'in-samp base':>12} {'in-samp glob':>12} "
        f"{'in-samp iso':>11} || {'held-out glob':>13} {'held-out iso':>12} {'HELD-OUT':>9} {'ready':>6}"
    )
    print(header)
    print("(in-sample columns are NOT evidence of generalization -- isotonic regression is")
    print(" the in-sample-optimal fit by construction. HELD-OUT columns are the real check:")
    print(" fit on the earliest 70% of each stat's real flags by first_flagged_at, scored")
    print(" against the most recent 30%, never seen during the fit.)")
    print("-" * len(header))
    rows_out = []
    with_holdout = [r for r in results if r["held_out"] is not None]
    without_holdout = [r for r in results if r["held_out"] is None]
    for r in sorted(
        with_holdout,
        key=lambda x: x["held_out"]["held_out_global_brier"] - x["held_out"]["held_out_isotonic_brier"],
        reverse=True,
    ) + without_holdout:
        ho = r["held_out"]
        if ho is not None:
            ho_str = (
                f"{ho['held_out_global_brier']:>13.4f} {ho['held_out_isotonic_brier']:>12.4f} "
                f"{'YES' if ho['isotonic_beats_global_held_out'] else 'no':>9}"
            )
        else:
            ho_str = f"{'n/a':>13} {'n/a':>12} {'too small':>9}"
        print(
            f"{r['stat_key']:<38} {r['n']:>6} {r['real_win_rate']*100:>5.1f}% "
            f"{r['baseline_brier']:>12.4f} {r['global_corrected_brier']:>12.4f} "
            f"{r['isotonic_brier']:>11.4f} || {ho_str} {'YES' if r['ready_to_apply'] else 'no':>6}"
        )
        for lo, hi, val in zip(r["block_lo"], r["block_hi"], r["block_val"]):
            rows_out.append({
                "resolved_stat_key": r["stat_key"], "n_total": r["n"],
                "z_lo": lo, "z_hi": hi, "calibrated_prob": val,
                "ready_to_apply": r["ready_to_apply"],
                "fit_date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
            })

    out_df = pd.DataFrame(rows_out)
    out_df.to_csv(OUT_PATH, index=False)
    print()
    print(f"Wrote {len(out_df)} calibration block(s) across {len(results)} stat(s) to {OUT_PATH}")

    n_validated = len(with_holdout)
    n_beat_held_out = sum(1 for r in with_holdout if r["held_out"]["isotonic_beats_global_held_out"])
    n_ready = sum(1 for r in results if r["ready_to_apply"])
    print(f"{n_validated} of {len(results)} stats had enough legs for a real held-out check; "
          f"isotonic beat the current global-sigma-corrected model on held-out data for "
          f"{n_beat_held_out} of those {n_validated}. {n_ready} stat(s) clear BOTH the "
          f"{MIN_GROUP_SIZE_FOR_PRODUCTION}-leg floor AND a real held-out improvement -- "
          f"only those are marked ready_to_apply=True in the output CSV.")


if __name__ == "__main__":
    main()
