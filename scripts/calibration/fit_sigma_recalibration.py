"""
Session 2.22 -- Sigma Recalibration Fit (Pick'em)

WHAT THIS SCRIPT IS
--------------------
Session 2.20's weekly_review.py found a real, persistent calibration gap:
pickem_model.py's flagged legs state ~74% average confidence but win ~67%
of the time (calibration_gap ~0.063, first observed on the 7,659-leg
2026-09-14 review; still ~0.067 on the fuller 8,225-leg sample this script
was fit against). Per that script's own design, it only FLAGS this --
diagnosing and fixing the actual model is separate, deliberate work,
originally slated for Session 8.3 (Ongoing Recalibration Cadence) but
pulled forward here at the user's explicit request once the graded sample
was judged large enough to trust (2026-09-15: ~28,000 pickem props already
analyzed cumulatively; 8,225 of those graded win/loss).

WHY THIS TARGETS SIGMA, NOT THE SEASON-AVG/RECENT-FORM BLEND
--------------------------------------------------------------
weekly_review.py's own recommendation text suggests "revisiting blend
weights" as a generic pointer, but its calibration-gap check only measures
one thing: whether stated confidence (a probability, i.e. how far into the
normal CDF's tail a leg's z-score falls) tracks real win rate. The blend
weight (SEASON_AVG_BLEND_WEIGHT / RECENT_FORM_BLEND_WEIGHT, pickem_model.py)
controls WHICH mean is used -- it does not control how extreme the resulting
probability is. sigma (pickem_model.py's sample_sigma()) is what controls
that: a systematically too-small sigma inflates every z-score, pushing
probabilities toward 0%/100% regardless of which mean feeds it, producing
exactly the flat, direction-agnostic overconfidence weekly_review found
(the gap is a single positive number across the whole graded population,
not evidence that one side is mispredicted more than the other, which is
what a bad blend weight would look like). This is also the exact
recalibration shape named as prior art in this project's own background
(the DFS_Optimizer sibling repos' fit_sigma_recalibration.py, referenced in
SESSION_LOG.md Session 0.1) -- a single scalar multiplier on sigma, fit
against real graded outcomes.

METHOD
------
Every graded row already stores first_flagged_model_prob -- the model's
probability for the FLAGGED side, at flag time, using the sigma pickem_model.py
computed then. Since prob_over = 1 - Phi(z) with z = (line - mean) / sigma,
and every flagged leg's stored probability is for the side the model favored,
each row's implied |z| is recoverable exactly via the inverse of the same
normal_cdf() pickem_model.py uses (matched here, not scipy's, so the
recovered z is exact given the same erf-based approximation, not a slightly
different one): z_i = Phi^-1(first_flagged_model_prob_i).

If the TRUE sigma is k times pickem_model.py's sigma (k > 1 means sigma was
too small, i.e. overconfident), the correctly-calibrated probability for
that same row would have been Phi(z_i / k). This script fits a single k
(grid search, no scipy, same "no unnamed black-box factors" and
no-new-dependency posture as pickem_model.py's own normal_cdf()) by
minimizing the Brier score (mean squared error between recalibrated
probability and the real win/loss outcome) across all graded win/loss legs
-- not just matching the average confidence to the average win rate, which
would fix the mean gap but say nothing about whether individual
probabilities are well-ordered. Brier score checks both.

USAGE
-----
python scripts/calibration/fit_sigma_recalibration.py
    Loads data/pickem/outcome_log.csv, fits k, prints the before/after
    calibration gap and Brier score, and appends a dated row to
    data/pickem/sigma_recalibration_log.csv -- a durable, queryable record
    (CSV, not prose, matching review_log.csv/clv_log.csv's own pattern in
    this project) that Session 2.23's weekly_review.py reads directly, to
    know when the sigma factor currently in pickem_model.py was last fit
    and restrict its own post-fit drift check to legs flagged since then.

SESSION 2.41c ADDITION -- EXCLUDES STATS THAT DON'T USE THE GLOBAL FACTOR
------------------------------------------------------------------------
load_graded_legs() now excludes the 12 Session 2.40 isotonic-covered stats
and the 6 SIGMA_CALIBRATION_FACTOR_BY_STAT stats before fitting -- see
load_excluded_stats()'s own docstring for why mixing them in would distort
the fit for every other stat. This is a real, necessary correction to this
script's method, not a style change: it was written (Session 2.22) before
either exclusion existed.
"""

from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "estimation"))
from pickem_model import SIGMA_CALIBRATION_FACTOR_BY_STAT, normal_cdf  # noqa: E402

BASE_DIR = Path(__file__).resolve().parents[2]
OUTCOME_LOG_PATH = BASE_DIR / "data" / "pickem" / "outcome_log.csv"
FIT_LOG_PATH = BASE_DIR / "data" / "pickem" / "sigma_recalibration_log.csv"
ISOTONIC_CALIBRATION_PATH = BASE_DIR / "data" / "pickem" / "isotonic_calibration_by_stat.csv"


def load_excluded_stats() -> set[str]:
    """Session 2.41c: stats that do NOT go through the single global
    SIGMA_CALIBRATION_FACTOR path this script fits, and must be excluded
    from the global fit or they'd distort it for every other stat:
    - the 12 Session 2.40 isotonic-covered stats, whose stored
      first_flagged_model_prob (for legs flagged after that shipped) is an
      isotonic-calibrated probability, not normal_cdf(z/factor) -- recovering
      a "z" from it via inverse_normal_cdf() is not meaningful.
    - the 6 SIGMA_CALIBRATION_FACTOR_BY_STAT stats, which use their own
      independently-fit per-stat multiplier instead of the global one.
    See pickem_calibration_by_stat.py's matching exclusion for the per-stat
    diagnostic version of this same fix."""
    excluded = set(SIGMA_CALIBRATION_FACTOR_BY_STAT.keys())
    if ISOTONIC_CALIBRATION_PATH.exists():
        iso = pd.read_csv(ISOTONIC_CALIBRATION_PATH)
        if "ready_to_apply" in iso.columns:
            excluded |= set(iso.loc[iso["ready_to_apply"] == True, "resolved_stat_key"].unique())  # noqa: E712
    return excluded

FIT_LOG_COLUMNS = [
    "run_at",
    "n_legs",
    "real_win_rate",
    "baseline_avg_confidence",
    "baseline_calibration_gap",
    "baseline_brier",
    "fitted_k",
    "fitted_avg_confidence",
    "fitted_calibration_gap",
    "fitted_brier",
]

# Grid search range for k (sigma multiplier). 1.0 = no change. Real-data
# fits so far land well inside this range; widen only if a future fit hits
# either edge (that would itself be worth a second look before trusting it).
K_GRID_MIN = 0.5
K_GRID_MAX = 3.0
K_GRID_STEP = 0.005


def inverse_normal_cdf(p: float, lo: float = -8.0, hi: float = 8.0, tol: float = 1e-10) -> float:
    """Bisection inverse of pickem_model.normal_cdf -- exact match to the
    same erf-based CDF, deliberately not scipy.stats.norm.ppf (which uses a
    slightly different implementation), so a round-trip through this
    function and normal_cdf() recovers the original z used at flag time."""
    if p <= 0.0:
        return lo
    if p >= 1.0:
        return hi
    while hi - lo > tol:
        mid = (lo + hi) / 2.0
        if normal_cdf(mid) < p:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def load_graded_legs() -> pd.DataFrame:
    df = pd.read_csv(OUTCOME_LOG_PATH, low_memory=False)
    graded = df.loc[df["result"].isin(["win", "loss"])].copy()
    graded = graded.dropna(subset=["first_flagged_model_prob"])
    graded["win"] = (graded["result"] == "win").astype(int)
    excluded = load_excluded_stats()
    if excluded:
        graded = graded.loc[~graded["resolved_stat_key"].isin(excluded)]
    return graded


def brier_score(probs: np.ndarray, outcomes: np.ndarray) -> float:
    return float(np.mean((probs - outcomes) ** 2))


def fit_k(graded: pd.DataFrame) -> dict:
    z = graded["first_flagged_model_prob"].apply(inverse_normal_cdf).to_numpy()
    outcomes = graded["win"].to_numpy()

    baseline_probs = graded["first_flagged_model_prob"].to_numpy()
    baseline_gap = float(baseline_probs.mean() - outcomes.mean())
    baseline_brier = brier_score(baseline_probs, outcomes)

    best_k = 1.0
    best_brier = baseline_brier
    k = K_GRID_MIN
    while k <= K_GRID_MAX + 1e-9:
        recalibrated = np.array([normal_cdf(zi / k) for zi in z])
        b = brier_score(recalibrated, outcomes)
        if b < best_brier:
            best_brier = b
            best_k = k
        k += K_GRID_STEP

    fitted_probs = np.array([normal_cdf(zi / best_k) for zi in z])
    fitted_gap = float(fitted_probs.mean() - outcomes.mean())

    return {
        "n_legs": len(graded),
        "real_win_rate": float(outcomes.mean()),
        "baseline_avg_confidence": float(baseline_probs.mean()),
        "baseline_calibration_gap": baseline_gap,
        "baseline_brier": baseline_brier,
        "fitted_k": best_k,
        "fitted_avg_confidence": float(fitted_probs.mean()),
        "fitted_calibration_gap": fitted_gap,
        "fitted_brier": best_brier,
    }


def load_fit_log() -> pd.DataFrame:
    if FIT_LOG_PATH.exists():
        df = pd.read_csv(FIT_LOG_PATH)
        for col in FIT_LOG_COLUMNS:
            if col not in df.columns:
                df[col] = None
        return df[FIT_LOG_COLUMNS]
    return pd.DataFrame(columns=FIT_LOG_COLUMNS)


def append_fit_log(result: dict) -> None:
    fit_log = load_fit_log()
    new_row = {
        "run_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "n_legs": result["n_legs"],
        "real_win_rate": result["real_win_rate"],
        "baseline_avg_confidence": result["baseline_avg_confidence"],
        "baseline_calibration_gap": result["baseline_calibration_gap"],
        "baseline_brier": result["baseline_brier"],
        "fitted_k": result["fitted_k"],
        "fitted_avg_confidence": result["fitted_avg_confidence"],
        "fitted_calibration_gap": result["fitted_calibration_gap"],
        "fitted_brier": result["fitted_brier"],
    }
    fit_log = pd.concat([fit_log, pd.DataFrame([new_row])], ignore_index=True)
    FIT_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    fit_log.to_csv(FIT_LOG_PATH, index=False)


if __name__ == "__main__":
    graded = load_graded_legs()
    if len(graded) < 30:
        raise SystemExit(
            f"Only {len(graded)} graded legs with a usable model_prob -- below "
            f"the 30-leg interim floor this project uses elsewhere "
            f"(weekly_review.py). Not fitting on a sample this small."
        )
    result = fit_k(graded)
    append_fit_log(result)
    print(result)
