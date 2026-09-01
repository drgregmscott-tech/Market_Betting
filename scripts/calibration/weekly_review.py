"""
Session 2.5 -- Weekly Review & Recalibration Check

WHAT THIS SCRIPT IS
--------------------
This is the recurring half of Session 2.5, built after the user decided
directly (see chat / SESSION_LOG.md for this session) that ~3,725 graded
legs (sample_size_methodology.md, Section 3) is too large a number to treat
as a single all-or-nothing gate. Instead, this script runs on a **weekly**
cadence, indefinitely, starting as soon as real graded data exists in
data/pickem/outcome_log.csv (built by outcome_tracker.py, this same
session). Each run does two things:

1. REPORTS real performance -- this week's graded legs, plus the running
   cumulative total -- always shown next to the two fixed reference points
   from sample_size_methodology.md: the 57.7% real breakeven win rate
   (Section 2) and the 3,725-leg full-strength sample size (Section 3).
2. CHECKS whether the model itself looks like it needs recalibrating, using
   two real, computable signals (see "Recalibration checks" below). This
   produces a RECOMMENDATION only -- it does not modify pickem_model.py's
   blend weights or clv_logger.py's FLAG_EDGE_THRESHOLD. A person decides
   whether to act on it, per this project's standing "flags and sizes,
   does not place bets" design principle (ROADMAP.md, Background &
   Approach) -- applied here to model changes, not just bet placement.

Every review's summary is appended as a permanent row to a new file,
data/pickem/review_log.csv -- so the review history itself becomes a real,
growing, queryable record (matching this project's "durable/queryable log"
standard from Sessions 2.2/2.4), not something recomputed and thrown away
each week.

WHY 30 GRADED LEGS IS THE INTERIM FLOOR
------------------------------------------
Below 30 graded legs, even a directional read is not reported as
"meaningful" -- this mirrors Session 2.4's own "15+ new flags before
reporting anything" standard (clv_methodology.md), applied here to graded
OUTCOMES instead of raw flags. A review run with fewer than 30 cumulative
graded legs still runs and still writes a row to review_log.csv (so the
history is complete), but is explicitly labeled "insufficient sample" in
both the printed summary and the log, rather than silently reporting a real
number, sample size, alongside a normal-looking recommendation.

RECALIBRATION CHECKS -- WHAT THEY ACTUALLY TEST
---------------------------------------------------
1. CALIBRATION GAP: compares the model's own average stated confidence
   (first_flagged_model_prob, averaged across all graded legs) against the
   real observed win rate. If the model says "60% on average" but the real
   win rate is 50%, the model is running overconfident by 10 points -- a
   real, computable signal that Session 2.3's blend weights (season average
   / recency-weighted form, currently 50/50) may need revisiting. This does
   NOT diagnose *which* weight is wrong, only that a gap exists -- that
   diagnosis is a real, separate piece of future work, not guessed at here.
2. EDGE-THRESHOLD EFFECTIVENESS: splits graded legs into two groups by
   whether their first_flagged_edge was above or below the graded sample's
   own median edge, and compares each group's real win rate. If
   higher-edge flags are not winning more often than lower-edge flags, that
   is real evidence Session 2.4's FLAG_EDGE_THRESHOLD (currently a stated,
   unvalidated placeholder of 0.03 -- see clv_logger.py's own docstring)
   is not doing real work, and should be revisited.

Both checks require a minimum sample to be worth running at all (default:
20 graded legs per group being compared) -- below that, the check is
skipped and reported as "insufficient sample for this check," not run on
too few points and presented with false confidence.

USAGE
-----
pip install pandas --break-system-packages
python weekly_review.py --run
    Runs a review covering everything graded since the last review (or all
    graded data, on the very first run), prints the summary, and appends a
    row to data/pickem/review_log.csv.

python weekly_review.py --history
    Prints every past review's summary row, so the trend across weeks is
    visible at a glance (is cumulative win rate holding steady, drifting up,
    drifting down as sample size grows?).

Intended to be run manually once a week, matching the current state of the
rest of Track 1's pipeline (per outcome_tracker.py and clv_logger.py's own
docstrings -- none of Track 1 is wired into scheduled automation yet; that
is Session 2.7's job).
"""

from __future__ import annotations

import argparse
import logging
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import pandas as pd

# ---------------------------------------------------------------------------
# Paths -- matching the existing repo-relative pattern from Sessions 2.2/2.4/2.5.
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parents[2]
OUTCOME_LOG_PATH = BASE_DIR / "data" / "pickem" / "outcome_log.csv"
REVIEW_LOG_PATH = BASE_DIR / "data" / "pickem" / "review_log.csv"
LOG_PATH = BASE_DIR / "logs" / "weekly_review.log"

# Fixed reference points from sample_size_methodology.md -- not recomputed
# here, only compared against. If these ever change, update both this file
# and the methodology doc together, not just one.
BREAKEVEN_WIN_RATE = 0.5774          # Section 2
FULL_SAMPLE_SIZE_THRESHOLD = 3725    # Section 3
INTERIM_REPORTING_FLOOR = 30         # Section 6

# Minimum legs required in EACH group before a recalibration check is run
# on that comparison -- see module docstring, "Recalibration checks."
MIN_GROUP_SIZE_FOR_CHECK = 20

REVIEW_LOG_COLUMNS = [
    "review_id",
    "run_at",
    "period_start",
    "period_end",
    "n_graded_this_period",
    "n_wins_this_period",
    "win_rate_this_period",
    "n_graded_cumulative",
    "n_wins_cumulative",
    "win_rate_cumulative",
    "breakeven_win_rate",
    "pct_of_full_sample_reached",
    "sample_status",
    "calibration_gap",
    "calibration_check_status",
    "edge_threshold_effectiveness",
    "edge_check_status",
    "recommendation",
]


def setup_logging() -> logging.Logger:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("weekly_review")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()

    file_handler = logging.FileHandler(LOG_PATH, mode="a", encoding="utf-8")
    console_handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s UTC | %(levelname)s | %(message)s")
    formatter.converter = time.gmtime
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger


log = setup_logging()


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def load_outcome_log() -> pd.DataFrame:
    if not OUTCOME_LOG_PATH.exists():
        raise FileNotFoundError(
            f"{OUTCOME_LOG_PATH} not found. Run outcome_tracker.py --record "
            f"at least once first (Session 2.5) so there is real graded data "
            f"to review."
        )
    df = pd.read_csv(OUTCOME_LOG_PATH, parse_dates=["reported_at"])
    return df


def load_review_log() -> pd.DataFrame:
    if REVIEW_LOG_PATH.exists():
        df = pd.read_csv(REVIEW_LOG_PATH)
        for col in REVIEW_LOG_COLUMNS:
            if col not in df.columns:
                df[col] = None
        return df[REVIEW_LOG_COLUMNS]
    return pd.DataFrame(columns=REVIEW_LOG_COLUMNS)


def last_period_end() -> Optional[pd.Timestamp]:
    review_log = load_review_log()
    if review_log.empty:
        return None
    return pd.to_datetime(review_log["period_end"]).max()


# ---------------------------------------------------------------------------
# Recalibration checks
# ---------------------------------------------------------------------------
def check_calibration_gap(graded: pd.DataFrame) -> tuple[Optional[float], str]:
    """Compares the model's average stated confidence against the real
    observed win rate across ALL cumulative graded legs (not just this
    period -- calibration is a property of the model, best judged on the
    largest sample available). Returns (gap, status)."""
    usable = graded.dropna(subset=["first_flagged_model_prob"])
    if len(usable) < MIN_GROUP_SIZE_FOR_CHECK:
        return None, f"insufficient sample (n={len(usable)}, need {MIN_GROUP_SIZE_FOR_CHECK}+)"
    avg_stated_confidence = usable["first_flagged_model_prob"].mean()
    real_win_rate = (usable["result"] == "win").mean()
    gap = round(avg_stated_confidence - real_win_rate, 4)
    return gap, "ok"


def check_edge_threshold_effectiveness(graded: pd.DataFrame) -> tuple[Optional[dict], str]:
    """Splits cumulative graded legs into above-median-edge and
    below-median-edge groups and compares real win rates. Returns
    (result_dict, status)."""
    usable = graded.dropna(subset=["first_flagged_edge"])
    if len(usable) < (MIN_GROUP_SIZE_FOR_CHECK * 2):
        return None, f"insufficient sample (n={len(usable)}, need {MIN_GROUP_SIZE_FOR_CHECK * 2}+)"

    median_edge = usable["first_flagged_edge"].median()
    high_edge = usable.loc[usable["first_flagged_edge"] >= median_edge]
    low_edge = usable.loc[usable["first_flagged_edge"] < median_edge]

    if len(high_edge) < MIN_GROUP_SIZE_FOR_CHECK or len(low_edge) < MIN_GROUP_SIZE_FOR_CHECK:
        return None, (
            f"insufficient sample per group (high={len(high_edge)}, "
            f"low={len(low_edge)}, need {MIN_GROUP_SIZE_FOR_CHECK}+ each)"
        )

    high_win_rate = (high_edge["result"] == "win").mean()
    low_win_rate = (low_edge["result"] == "win").mean()

    result = {
        "median_edge_split": round(median_edge, 4),
        "n_high_edge": len(high_edge),
        "win_rate_high_edge": round(high_win_rate, 4),
        "n_low_edge": len(low_edge),
        "win_rate_low_edge": round(low_win_rate, 4),
        "high_minus_low": round(high_win_rate - low_win_rate, 4),
    }
    return result, "ok"


def build_recommendation(
    sample_status: str,
    calibration_gap: Optional[float],
    calibration_status: str,
    edge_result: Optional[dict],
    edge_status: str,
) -> str:
    if sample_status != "ok":
        return (
            f"Sample below the {INTERIM_REPORTING_FLOOR}-leg interim reporting "
            f"floor -- no recalibration recommendation this cycle. Keep grading."
        )

    notes = []
    if calibration_status == "ok" and calibration_gap is not None:
        if abs(calibration_gap) >= 0.05:
            direction = "overconfident" if calibration_gap > 0 else "underconfident"
            notes.append(
                f"Model looks {direction} by {abs(calibration_gap):.1%} on average "
                f"(stated confidence vs. real win rate) -- consider revisiting "
                f"pickem_model.py's blend weights."
            )
        else:
            notes.append("Model's stated confidence tracks real win rate reasonably well so far.")
    else:
        notes.append(f"Calibration check: {calibration_status}.")

    if edge_status == "ok" and edge_result is not None:
        if edge_result["high_minus_low"] <= 0.02:
            notes.append(
                f"High-edge flags (avg {edge_result['win_rate_high_edge']:.1%}) are not "
                f"clearly outperforming low-edge flags (avg {edge_result['win_rate_low_edge']:.1%}) "
                f"-- consider revisiting clv_logger.py's FLAG_EDGE_THRESHOLD (currently 0.03)."
            )
        else:
            notes.append(
                f"High-edge flags are outperforming low-edge flags by "
                f"{edge_result['high_minus_low']:.1%} -- the edge threshold looks like it's "
                f"doing real work so far."
            )
    else:
        notes.append(f"Edge-threshold check: {edge_status}.")

    return " ".join(notes)


# ---------------------------------------------------------------------------
# Core action
# ---------------------------------------------------------------------------
def run_review() -> dict:
    outcome_log = load_outcome_log()
    graded_all = outcome_log.loc[outcome_log["result"].isin(["win", "loss"])].copy()

    period_start = last_period_end()
    run_at = datetime.now(timezone.utc)
    if period_start is None:
        this_period = graded_all
        period_start_str = "beginning" if graded_all.empty else str(graded_all["reported_at"].min())
    else:
        this_period = graded_all.loc[graded_all["reported_at"] > period_start]
        period_start_str = str(period_start)

    n_this_period = len(this_period)
    n_wins_this_period = int((this_period["result"] == "win").sum())
    win_rate_this_period = (n_wins_this_period / n_this_period) if n_this_period > 0 else None

    n_cumulative = len(graded_all)
    n_wins_cumulative = int((graded_all["result"] == "win").sum())
    win_rate_cumulative = (n_wins_cumulative / n_cumulative) if n_cumulative > 0 else None

    sample_status = "ok" if n_cumulative >= INTERIM_REPORTING_FLOOR else "insufficient_sample"

    calibration_gap, calibration_status = check_calibration_gap(graded_all)
    edge_result, edge_status = check_edge_threshold_effectiveness(graded_all)

    recommendation = build_recommendation(
        sample_status, calibration_gap, calibration_status, edge_result, edge_status
    )

    review_log = load_review_log()
    review_id = f"review_{run_at.strftime('%Y%m%dT%H%M%SZ')}"
    new_row = {
        "review_id": review_id,
        "run_at": run_at.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "period_start": period_start_str,
        "period_end": run_at.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "n_graded_this_period": n_this_period,
        "n_wins_this_period": n_wins_this_period,
        "win_rate_this_period": win_rate_this_period,
        "n_graded_cumulative": n_cumulative,
        "n_wins_cumulative": n_wins_cumulative,
        "win_rate_cumulative": win_rate_cumulative,
        "breakeven_win_rate": BREAKEVEN_WIN_RATE,
        "pct_of_full_sample_reached": round(100 * n_cumulative / FULL_SAMPLE_SIZE_THRESHOLD, 2),
        "sample_status": sample_status,
        "calibration_gap": calibration_gap,
        "calibration_check_status": calibration_status,
        "edge_threshold_effectiveness": edge_result,
        "edge_check_status": edge_status,
        "recommendation": recommendation,
    }

    review_log = pd.concat([review_log, pd.DataFrame([new_row])], ignore_index=True)
    REVIEW_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    review_log.to_csv(REVIEW_LOG_PATH, index=False)

    log.info(
        "Review %s complete: %d graded this period (%d cumulative). "
        "sample_status=%s. Recommendation: %s",
        review_id, n_this_period, n_cumulative, sample_status, recommendation,
    )
    return new_row


def print_history() -> None:
    review_log = load_review_log()
    if review_log.empty:
        print("No reviews recorded yet. Run --run first.")
        return
    cols = [
        "review_id", "period_end", "n_graded_this_period", "win_rate_this_period",
        "n_graded_cumulative", "win_rate_cumulative", "pct_of_full_sample_reached",
        "sample_status", "recommendation",
    ]
    print(review_log[cols].to_string(index=False))


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", action="store_true", help="Run this week's review.")
    parser.add_argument("--history", action="store_true", help="Print all past review summaries.")
    args = parser.parse_args()

    if args.run:
        result = run_review()
        print(result)
    elif args.history:
        print_history()
    else:
        parser.error("Specify --run or --history")
