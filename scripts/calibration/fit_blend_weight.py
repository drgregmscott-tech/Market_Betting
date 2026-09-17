"""
Session 2.41c -- Blend Weight Fit (SEASON_AVG_BLEND_WEIGHT / RECENT_FORM_BLEND_WEIGHT)

WHAT THIS SCRIPT IS
--------------------
pickem_model.py's model_mean has always been a flat, never-fitted 50/50
blend of season_avg and recent_form (see that file's own "not claimed to be
optimal" docstring note). Session 2.41c's ROADMAP.md card names this as a
real, separate gap from SIGMA_CALIBRATION_FACTOR: the blend weight controls
WHICH mean feeds prob_over(), not how extreme the resulting probability is,
so re-fitting sigma (fit_sigma_recalibration.py) says nothing about whether
50/50 is actually the best blend. This script fits it for the first time
against real graded outcomes.

WHY THIS NEEDS A DIFFERENT DATA SOURCE THAN THE SIGMA FIT
------------------------------------------------------------
fit_sigma_recalibration.py can recover everything it needs (a single
recovered z per leg) from outcome_log.csv/clv_log.csv alone, because
rescaling sigma is a pure function of the ALREADY-BLENDED z-score. Changing
the blend weight is not -- it requires season_avg and recent_form as two
SEPARATE numbers per leg, and outcome_log.csv/clv_log.csv only ever stored
the final blended probability (first_flagged_model_prob), never its two
component means. Those two components ARE written per-row by
pickem_model.py's process_props() to its own output snapshots
(output/estimation/pickem_estimates_*.csv -- season_avg, recent_form,
model_sigma columns), so this script joins outcome_log.csv (via clv_log.csv,
for source_line_id/first_flagged_at) back to whichever RETAINED estimates
snapshot covers that leg's flag date, to recover season_avg/recent_form.

REAL, STATED LIMITATION -- NOT EVERY GRADED LEG HAS A RETAINED SNAPSHOT
--------------------------------------------------------------------------
output/estimation/ only retains a subset of historical snapshot files (this
project's disk-management behavior, not something this script controls) --
26 pickem_estimates_*.csv files exist locally, spanning 2026-08-31 through
2026-09-16, versus 65,865 real logged flags in clv_log.csv. This script can
therefore only fit against the real graded legs whose flag date happens to
fall on a day a snapshot survived -- a real, smaller sample than the sigma
fit's, reported plainly below rather than glossed over. Confirmed directly
before relying on this (see the day-level dedup note in load_snapshots())
that season_avg/recent_form/model_sigma are stable for a given
(platform, source_line_id) across every snapshot taken on the same UTC
calendar day -- the underlying player game log only changes once real games
finish, not intra-day -- so matching at day granularity (not exact
timestamp, which clv_log.csv's first_flagged_at and the estimates file's own
pulled_at never share -- they're written by two separate process runs,
seconds to minutes apart) recovers the correct component values without
needing exact-timestamp alignment.

REAL, STATED APPROXIMATION -- SIGMA IS HELD FIXED, NOT RE-DERIVED PER w
----------------------------------------------------------------------------
model_sigma in the retained snapshot is the PRODUCTION sample_sigma() (at
whatever calibration factor was active then) computed using the PRODUCTION
50/50 model_mean -- sample_sigma()'s only mean-dependence is the
MIN_GAMES_FOR_ESTIMATE-only floor (SIGMA_FLOOR_FRACTION * |model_mean|).
This script holds model_sigma fixed across the whole w grid rather than
re-deriving the floor for each counterfactual w (doing so would require the
player's raw per-game series, not retained in any snapshot). This only
matters for the narrow subset of legs with exactly 2 games AND an
implausibly small observed sigma -- stated here as a real, second-order
approximation, not hidden.

METHOD
------
For every real graded (win/loss) leg with a joinable snapshot: recompute
model_mean = w * season_avg + (1 - w) * recent_form for a grid of w in
[0, 1], step 0.05 (SEASON_AVG_BLEND_WEIGHT + RECENT_FORM_BLEND_WEIGHT are
required to sum to 1 in pickem_model.py already, so this is a single free
parameter, not two). Recompute z = (line - model_mean) / model_sigma (sigma
held fixed, see above), take the probability of the SIDE THAT WAS ACTUALLY
FLAGGED (flagged_side column -- matches clv_logger.py's own
determine_flagged_side_pickem() convention, same as fit_sigma_recalibration.py's
docstring notes for isotonic calibration), and score Brier against the real
win/loss outcome. The w minimizing Brier score across the whole joined
sample is the fit result. A w=0.5 sanity check (recomputed probability
should closely match the real, stored first_flagged_model_prob for the same
rows) is printed first, to prove the join/recompute pipeline is actually
reconstructing the same numbers production used, not silently mismatched
rows.

USAGE
-----
python scripts/calibration/fit_blend_weight.py
    Loads outcome_log.csv + clv_log.csv + every retained
    output/estimation/pickem_estimates_*.csv, fits w, prints the sanity
    check and the before/after Brier comparison, and appends a dated row to
    data/pickem/blend_weight_recalibration_log.csv -- a durable, queryable
    record matching sigma_recalibration_log.csv's own pattern.
"""

from __future__ import annotations

import glob
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "estimation"))
from pickem_model import normal_cdf  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fit_sigma_recalibration import load_excluded_stats  # noqa: E402

BASE_DIR = Path(__file__).resolve().parents[2]
OUTCOME_LOG_PATH = BASE_DIR / "data" / "pickem" / "outcome_log.csv"
CLV_LOG_PATH = BASE_DIR / "data" / "pickem" / "clv_log.csv"
ESTIMATES_GLOB = str(BASE_DIR / "output" / "estimation" / "pickem_estimates_*.csv")
FIT_LOG_PATH = BASE_DIR / "data" / "pickem" / "blend_weight_recalibration_log.csv"

SNAPSHOT_COLUMNS = [
    "platform", "source_line_id", "pulled_at", "model_status",
    "season_avg", "recent_form", "model_sigma", "line", "resolved_stat_key",
]

# Grid search range for w (SEASON_AVG_BLEND_WEIGHT); RECENT_FORM_BLEND_WEIGHT
# is always 1 - w, matching pickem_model.py's existing constraint that the
# two weights sum to 1.
W_GRID = np.round(np.arange(0.0, 1.0001, 0.05), 2)

FIT_LOG_COLUMNS = [
    "run_at", "n_legs", "n_snapshot_files_used",
    "sanity_check_mean_abs_diff_at_w050",
    "baseline_brier_at_w050", "fitted_w", "fitted_brier",
    "current_production_w",
]


def load_snapshots() -> tuple[pd.DataFrame, int]:
    files = sorted(glob.glob(ESTIMATES_GLOB))
    frames = []
    used = 0
    for f in files:
        try:
            df = pd.read_csv(f, usecols=lambda c: c in SNAPSHOT_COLUMNS, low_memory=False)
        except ValueError:
            continue  # old-format snapshot missing a needed column
        required = {"platform", "source_line_id", "pulled_at", "model_status",
                    "season_avg", "recent_form", "model_sigma", "line"}
        if not required.issubset(df.columns):
            continue
        df = df.loc[df["model_status"] == "estimated"].copy()
        if df.empty:
            continue
        df["source_line_id"] = df["source_line_id"].astype(str)
        df["snapshot_date"] = pd.to_datetime(df["pulled_at"], utc=True).dt.date
        frames.append(df)
        used += 1
    if not frames:
        raise SystemExit("No usable pickem_estimates_*.csv snapshots found under output/estimation/.")
    snap = pd.concat(frames, ignore_index=True)
    # Confirmed directly (see module docstring) that season_avg/recent_form/
    # model_sigma never vary across multiple same-day snapshots for the same
    # (platform, source_line_id) -- keep one row per day, arbitrary which.
    snap = snap.drop_duplicates(subset=["platform", "source_line_id", "snapshot_date"], keep="first")
    return snap, used


def load_joined_legs(snap: pd.DataFrame) -> pd.DataFrame:
    outcome = pd.read_csv(OUTCOME_LOG_PATH, low_memory=False)
    graded = outcome.loc[outcome["result"].isin(["win", "loss"])].copy()
    graded = graded.dropna(subset=["first_flagged_model_prob", "flag_id", "flagged_side"])
    graded["win"] = (graded["result"] == "win").astype(int)

    clv = pd.read_csv(CLV_LOG_PATH, usecols=["flag_id", "platform", "source_line_id", "first_flagged_at"])
    clv["source_line_id"] = clv["source_line_id"].astype(str)
    merged = graded.merge(clv, on="flag_id", how="left", suffixes=("", "_clv"))
    merged = merged.dropna(subset=["source_line_id", "first_flagged_at"])
    merged["flag_date"] = pd.to_datetime(merged["first_flagged_at"], utc=True).dt.date

    joined = merged.merge(
        snap.drop(columns=["resolved_stat_key"]),
        left_on=["platform", "source_line_id", "flag_date"],
        right_on=["platform", "source_line_id", "snapshot_date"],
        how="inner",
    )
    joined = joined.dropna(subset=["season_avg", "recent_form", "model_sigma", "line"])
    joined = joined.loc[joined["model_sigma"] > 0].copy()
    # Session 2.41c: same exclusion as fit_sigma_recalibration.py, for
    # consistency (isotonic-covered stats' first_flagged_model_prob is not
    # a plain Gaussian value; per-stat-override stats use their own
    # independent sigma path) -- the recomputed-probability approach here
    # isn't invalidated by isotonic the same way the z-recovery method is,
    # but fitting one shared blend weight across stats whose SIGMA path is
    # already handled separately is the same kind of population-mixing this
    # session's sigma fit avoids.
    excluded = load_excluded_stats()
    if excluded:
        joined = joined.loc[~joined["resolved_stat_key"].isin(excluded)]
    return joined


def brier_score(probs: np.ndarray, outcomes: np.ndarray) -> float:
    return float(np.mean((probs - outcomes) ** 2))


def prob_for_flagged_side(joined: pd.DataFrame, w: float) -> np.ndarray:
    model_mean = w * joined["season_avg"] + (1.0 - w) * joined["recent_form"]
    z = (joined["line"] - model_mean) / joined["model_sigma"]
    p_over = np.array([1.0 - normal_cdf(zi) for zi in z])
    return np.where(joined["flagged_side"].to_numpy() == "over", p_over, 1.0 - p_over)


def fit_w(joined: pd.DataFrame) -> dict:
    outcomes = joined["win"].to_numpy()

    p_at_050 = prob_for_flagged_side(joined, 0.5)
    stored = joined["first_flagged_model_prob"].to_numpy()
    sanity_diff = float(np.mean(np.abs(p_at_050 - stored)))
    baseline_brier = brier_score(p_at_050, outcomes)

    best_w = 0.5
    best_brier = baseline_brier
    for w in W_GRID:
        probs = prob_for_flagged_side(joined, float(w))
        b = brier_score(probs, outcomes)
        if b < best_brier:
            best_brier = b
            best_w = float(w)

    return {
        "n_legs": len(joined),
        "sanity_check_mean_abs_diff_at_w050": sanity_diff,
        "baseline_brier_at_w050": baseline_brier,
        "fitted_w": best_w,
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


def append_fit_log(result: dict, n_snapshot_files_used: int) -> None:
    fit_log = load_fit_log()
    new_row = {
        "run_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "n_legs": result["n_legs"],
        "n_snapshot_files_used": n_snapshot_files_used,
        "sanity_check_mean_abs_diff_at_w050": result["sanity_check_mean_abs_diff_at_w050"],
        "baseline_brier_at_w050": result["baseline_brier_at_w050"],
        "fitted_w": result["fitted_w"],
        "fitted_brier": result["fitted_brier"],
        "current_production_w": 0.5,
    }
    fit_log = pd.concat([fit_log, pd.DataFrame([new_row])], ignore_index=True)
    FIT_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    fit_log.to_csv(FIT_LOG_PATH, index=False)


if __name__ == "__main__":
    snap, n_files = load_snapshots()
    joined = load_joined_legs(snap)
    if len(joined) < 30:
        raise SystemExit(
            f"Only {len(joined)} graded legs joined to a retained snapshot -- below "
            f"the 30-leg interim floor this project uses elsewhere (weekly_review.py, "
            f"fit_sigma_recalibration.py). Not fitting on a sample this small. "
            f"({n_files} snapshot files were usable.)"
        )
    result = fit_w(joined)
    append_fit_log(result, n_files)
    print(f"Snapshot files used: {n_files}")
    print(f"Joined graded legs: {result['n_legs']}")
    print(f"Sanity check (mean |recomputed w=0.5 prob - stored first_flagged_model_prob|): "
          f"{result['sanity_check_mean_abs_diff_at_w050']:.6f}")
    print(f"Baseline (current 50/50) Brier on joined sample: {result['baseline_brier_at_w050']:.6f}")
    print(f"Fitted w (SEASON_AVG_BLEND_WEIGHT): {result['fitted_w']}")
    print(f"Fitted Brier: {result['fitted_brier']:.6f}")
