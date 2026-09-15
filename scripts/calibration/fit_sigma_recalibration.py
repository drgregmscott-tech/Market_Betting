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
    calibration gap and Brier score, and writes a dated record to
    docs/calibration/sigma_recalibration_log.md (append-only, so the fit
    history itself is a durable record, matching this project's log
    standard elsewhere).
"""

from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "estimation"))
from pickem_model import normal_cdf  # noqa: E402

BASE_DIR = Path(__file__).resolve().parents[2]
OUTCOME_LOG_PATH = BASE_DIR / "data" / "pickem" / "outcome_log.csv"
FIT_LOG_PATH = BASE_DIR / "docs" / "calibration" / "sigma_recalibration_log.md"

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
    df = pd.read_csv(OUTCOME_LOG_PATH)
    graded = df.loc[df["result"].isin(["win", "loss"])].copy()
    graded = graded.dropna(subset=["first_flagged_model_prob"])
    graded["win"] = (graded["result"] == "win").astype(int)
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


def append_fit_log(result: dict) -> None:
    FIT_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    is_new = not FIT_LOG_PATH.exists()
    with open(FIT_LOG_PATH, "a", encoding="utf-8") as f:
        if is_new:
            f.write("# Sigma Recalibration Fit Log\n\n")
            f.write(
                "Append-only record of every fit_sigma_recalibration.py run. "
                "Each row is a real fit against the graded sample available at "
                "that time -- see scripts/calibration/fit_sigma_recalibration.py "
                "for method.\n\n"
            )
            f.write(
                "| run_at | n_legs | real_win_rate | baseline_avg_conf | "
                "baseline_gap | baseline_brier | fitted_k | fitted_avg_conf | "
                "fitted_gap | fitted_brier |\n"
            )
            f.write("|---|---|---|---|---|---|---|---|---|---|\n")
        f.write(
            f"| {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')} | "
            f"{result['n_legs']} | {result['real_win_rate']:.4f} | "
            f"{result['baseline_avg_confidence']:.4f} | "
            f"{result['baseline_calibration_gap']:.4f} | "
            f"{result['baseline_brier']:.4f} | "
            f"{result['fitted_k']:.3f} | "
            f"{result['fitted_avg_confidence']:.4f} | "
            f"{result['fitted_calibration_gap']:.4f} | "
            f"{result['fitted_brier']:.4f} |\n"
        )


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
