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
   from sample_size_methodology.md: the 55.5% real breakeven win rate
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

SESSION 2.23 ADDITION -- POST-FIT DRIFT CHECK AND RECALIBRATION NUDGE
------------------------------------------------------------------------
Session 2.22 fit and shipped a real sigma-calibration factor
(pickem_model.py's SIGMA_CALIBRATION_FACTOR) against the graded sample as
of 2026-09-15, closing the calibration gap this script found from 0.0674 to
0.0008 on that sample. But `calibration_gap` above is computed over ALL
cumulative graded legs, most of which were flagged BEFORE that fit shipped
(using the old, uncalibrated sigma) -- so it will keep reading close to the
old ~0.067 gap for a while after the fix, purely because old legs are still
rolling through grading, not because the fix failed. Comparing that number
against a threshold would either never fire (if the threshold is loose) or
fire immediately and permanently for the wrong reason (if it's tight).

This addition adds a SECOND, narrower calibration check --
`post_fit_calibration_gap` -- restricted to legs whose `reported_at` falls
on or after the most recent row in data/pickem/sigma_recalibration_log.csv
(i.e., only legs actually scored under the CURRENT sigma factor). Once that
subset reaches MIN_GROUP_SIZE_FOR_CHECK legs, if its calibration gap exceeds
RECALIBRATION_GAP_THRESHOLD, the recommendation explicitly and
unmissably flags that a re-fit is warranted (`recalibration_suggested=True`
in review_log.csv), rather than relying on a person remembering to
periodically re-check this by hand. Session 2.23's own
pickem_weekly_review.yml addition surfaces this flag as a GitHub Issue --
see that workflow file's header comment -- so it does not depend on anyone
opening review_log.csv or the dashboard to notice.

SESSION 2.41e FIX -- "only legs actually scored under the CURRENT sigma
factor" ABOVE WAS NOT ACTUALLY TRUE
------------------------------------------------------------------------------
Found directly while checking Session 2.41c/2.41d's re-fit for drift: the
post-fit filter above used outcome_log.csv's `reported_at` (when a leg
finished GRADING) instead of clv_log.csv's `first_flagged_at` (when it was
actually SCORED by pickem_model.py). A leg flagged under the OLD constants
can easily finish grading well after a same-day recalibration -- so the
original filter was silently mixing old-model legs into a check whose whole
point is "does the CURRENT model look calibrated." Checking this directly
(2026-09-17) found 0 graded legs had actually been FLAGGED since the
2.41c/2.41d fit, versus 487 that merely finished GRADING since then -- the
old code was reading those 487 old-model legs as if they validated the new
one, and reported a reassuring "no re-fit needed" that had not actually been
tested yet. `_attach_first_flagged_at()` now joins the real flag time from
clv_log.csv and `check_post_fit_calibration_gap()` filters on that instead --
see both functions' own docstrings.

SESSION 2.42 ADDITION -- SAME POST-FIT CHECK, NOW ALSO FOR SHRINKAGE
------------------------------------------------------------------------
Session 2.42 added a second constant that changes the model's scored
probabilities, `SHRINKAGE_PRIOR_STRENGTH_K` (pickem_model.py), fit and
held-out-validated by the new `scripts/calibration/fit_shrinkage.py`. Before
this addition, this script's post-fit check only ever looked at
`sigma_recalibration_log.csv` -- a real drift in the shrinkage constant
specifically would have been invisible here, silently absorbed into (or
diluted by) the sigma-fit-scoped check even though the two constants were
last fit at different times. `check_post_shrinkage_calibration_gap()` mirrors
`check_post_fit_calibration_gap()` exactly (same calibration-gap definition,
same `first_flagged_at`-based filter, same `MIN_GROUP_SIZE_FOR_CHECK` floor),
scoped instead to `shrinkage_recalibration_log.csv`'s own most recent fit
time. Both checks share the same underlying helper
(`_check_post_fit_calibration_gap()`) to avoid duplicating that logic twice.
Confirmed directly (2026-09-17, right after Session 2.42 shipped): 0 real
legs have been flagged since `SHRINKAGE_PRIOR_STRENGTH_K` went live, so this
check correctly reports "insufficient post-fit sample" for now -- an honest
"too soon to tell," not a false green light. It will report a real number
once enough legs are flagged and graded under the new constant.
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
CLV_LOG_PATH = BASE_DIR / "data" / "pickem" / "clv_log.csv"
REVIEW_LOG_PATH = BASE_DIR / "data" / "pickem" / "review_log.csv"
SIGMA_FIT_LOG_PATH = BASE_DIR / "data" / "pickem" / "sigma_recalibration_log.csv"
SHRINKAGE_FIT_LOG_PATH = BASE_DIR / "data" / "pickem" / "shrinkage_recalibration_log.csv"
LOG_PATH = BASE_DIR / "logs" / "weekly_review.log"

# Fixed reference points from sample_size_methodology.md -- not recomputed
# here, only compared against. If these ever change, update both this file
# and the methodology doc together, not just one.
BREAKEVEN_WIN_RATE = 0.5549          # Section 2 (5-pick 19x; was 0.5774 before Session 2.57)
FULL_SAMPLE_SIZE_THRESHOLD = 3725    # Section 3
# Legs from one game are correlated (measured design effect 3.49), so games
# are the real unit of evidence: about 3,300 real legs = about 100 games.
# See sample_size_methodology.md, Session 2.57 correction note.
FULL_SAMPLE_GAMES_THRESHOLD = 100
INTERIM_REPORTING_FLOOR = 30         # Section 6

# Minimum legs required in EACH group before a recalibration check is run
# on that comparison -- see module docstring, "Recalibration checks."
MIN_GROUP_SIZE_FOR_CHECK = 20

# Session 2.23: how far the POST-FIT calibration gap (see module docstring
# addition) is allowed to drift before this script explicitly recommends
# re-running fit_sigma_recalibration.py, rather than leaving that judgment
# to someone remembering to check. Chosen as roughly half of the real,
# pre-fit gap Session 2.20 first measured (0.0674) -- large enough that a
# few noisy weeks of a modest sample won't false-trigger it, small enough
# to catch real drift well before it re-approaches the original problem.
RECALIBRATION_GAP_THRESHOLD = 0.03

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
    "n_games_cumulative",
    "pct_of_games_target_reached",
    "sample_status",
    "calibration_gap",
    "calibration_check_status",
    "post_fit_calibration_gap",
    "post_fit_check_status",
    "post_shrinkage_calibration_gap",
    "post_shrinkage_check_status",
    "recalibration_suggested",
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
    df = pd.read_csv(OUTCOME_LOG_PATH, parse_dates=["reported_at"], low_memory=False)
    df = _attach_first_flagged_at(df)
    return df


def _attach_first_flagged_at(df: pd.DataFrame) -> pd.DataFrame:
    """Session 2.41e fix: the post-fit drift check needs to know when each
    leg was actually SCORED (first_flagged_at, from clv_log.csv), not when
    it finished grading (reported_at, outcome_log.csv's own column). A leg
    flagged under the OLD constants can easily finish grading (reported_at)
    well AFTER a same-day recalibration fit -- filtering on reported_at, as
    this script originally did, silently mixes old-model legs into what is
    supposed to be a "scored under the CURRENT constants" check, producing a
    false-looking-clean drift read for a fit that has not actually been
    exercised by any real flag yet. Found directly (2026-09-17): re-checking
    the Session 2.41c/2.41d re-fit this way showed 0 graded legs had
    actually been FLAGGED since that fit, versus 487 that merely finished
    GRADING since then -- the original reported_at-based check was reading
    those 487 old-model legs as if they validated the new constants."""
    if not CLV_LOG_PATH.exists() or "flag_id" not in df.columns:
        df["first_flagged_at"] = pd.NaT
        return df
    # game_id is joined here too (Session 2.59) so run_review can count games.
    wanted = ["flag_id", "first_flagged_at", "game_id"]
    clv = pd.read_csv(CLV_LOG_PATH, usecols=lambda c: c in wanted)
    if "game_id" not in clv.columns:
        clv["game_id"] = pd.NA
    clv = clv.drop_duplicates("flag_id")
    clv["first_flagged_at"] = pd.to_datetime(clv["first_flagged_at"], utc=True, errors="coerce")
    df = df.merge(clv, on="flag_id", how="left")
    return df


def count_games(graded: pd.DataFrame) -> int:
    """Distinct games behind the graded legs: platform + game_id. Ids from
    different platforms are not comparable, so one real game on both
    platforms counts twice (a slight overcount). Legs with no game_id are
    not counted, so this can only undercount."""
    if "game_id" not in graded.columns:
        return 0
    known = graded.loc[graded["game_id"].notna()]
    platform = known["platform"].astype(str) if "platform" in known.columns else ""
    return int((platform + "|" + known["game_id"].astype(str)).nunique())


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


def last_sigma_fit_at() -> Optional[pd.Timestamp]:
    """Session 2.23: most recent run_at in sigma_recalibration_log.csv, i.e.
    when the sigma factor currently live in pickem_model.py was fit. None if
    fit_sigma_recalibration.py has never been run."""
    if not SIGMA_FIT_LOG_PATH.exists():
        return None
    fit_log = pd.read_csv(SIGMA_FIT_LOG_PATH)
    if fit_log.empty:
        return None
    fit_log["run_at"] = pd.to_datetime(fit_log["run_at"], utc=True)
    return fit_log["run_at"].max()


def last_shrinkage_fit_at() -> Optional[pd.Timestamp]:
    """Session 2.42: most recent run_at in shrinkage_recalibration_log.csv,
    i.e. when SHRINKAGE_PRIOR_STRENGTH_K currently live in pickem_model.py
    was fit. None if fit_shrinkage.py has never been run. Mirrors
    last_sigma_fit_at() exactly -- see that function's own docstring."""
    if not SHRINKAGE_FIT_LOG_PATH.exists():
        return None
    fit_log = pd.read_csv(SHRINKAGE_FIT_LOG_PATH)
    if fit_log.empty:
        return None
    fit_log["run_at"] = pd.to_datetime(fit_log["run_at"], utc=True)
    return fit_log["run_at"].max()


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


def _check_post_fit_calibration_gap(
    graded: pd.DataFrame, fit_at: Optional[pd.Timestamp], no_fit_message: str
) -> tuple[Optional[float], str]:
    """Session 2.23 (sigma), generalized in Session 2.42 to also back
    check_post_shrinkage_calibration_gap(): same comparison as
    check_calibration_gap, but restricted to legs flagged on or after the
    given fit time -- i.e. only legs actually scored under whichever
    constant currently live in pickem_model.py this call is checking. This
    is the number that should stay near zero on an ongoing basis;
    check_calibration_gap's all-time figure will keep reflecting a mix of
    pre- and post-fit legs for a while after any fit.

    SESSION 2.41e FIX (originally sigma-only, applies equally here): filters
    on first_flagged_at (when the leg was actually scored), not reported_at
    (when it finished grading) -- see _attach_first_flagged_at()'s own
    docstring for why the original reported_at filter let old-model legs
    silently pass as if they validated a brand new fit."""
    if fit_at is None:
        return None, no_fit_message
    usable = graded.dropna(subset=["first_flagged_model_prob", "first_flagged_at"])
    usable = usable.loc[usable["first_flagged_at"] >= fit_at]
    if len(usable) < MIN_GROUP_SIZE_FOR_CHECK:
        return None, (
            f"insufficient post-fit sample (n={len(usable)}, need "
            f"{MIN_GROUP_SIZE_FOR_CHECK}+ legs FLAGGED since the last fit at "
            f"{fit_at.strftime('%Y-%m-%d %H:%M UTC')} -- grading lag means this "
            f"can legitimately stay at 0 for a while after a same-day fit)"
        )
    avg_stated_confidence = usable["first_flagged_model_prob"].mean()
    real_win_rate = (usable["result"] == "win").mean()
    gap = round(avg_stated_confidence - real_win_rate, 4)
    return gap, "ok"


def check_post_fit_calibration_gap(
    graded: pd.DataFrame, fit_at: Optional[pd.Timestamp]
) -> tuple[Optional[float], str]:
    """Post-fit calibration gap scoped to the most recent SIGMA_CALIBRATION_
    FACTOR fit. See _check_post_fit_calibration_gap()'s own docstring for
    the shared logic."""
    return _check_post_fit_calibration_gap(
        graded, fit_at, "no sigma fit on record yet -- run fit_sigma_recalibration.py first"
    )


def check_post_shrinkage_calibration_gap(
    graded: pd.DataFrame, fit_at: Optional[pd.Timestamp]
) -> tuple[Optional[float], str]:
    """Session 2.42: post-fit calibration gap scoped to the most recent
    SHRINKAGE_PRIOR_STRENGTH_K fit, mirroring check_post_fit_calibration_gap()
    exactly but keyed off shrinkage_recalibration_log.csv instead of
    sigma_recalibration_log.csv -- see the module docstring's "SESSION 2.42
    ADDITION" section for why sigma's own post-fit check could not stand in
    for this (the two constants are not necessarily fit at the same time,
    so "legs flagged since the sigma fit" is not the same population as
    "legs flagged since the shrinkage fit"). Uses the same general
    calibration-gap definition (stated confidence vs. real win rate) as
    every other check here, a deliberate, stated design choice -- not the
    Brier-score-delta-vs-no-shrinkage metric fit_shrinkage.py itself used to
    validate k=5.0, which needs a counterfactual (unshrunk) probability this
    script does not have stored per leg. A real drift in EITHER direction
    (shrinkage making calibration worse, or the general model drifting for
    an unrelated reason) will still show up here as a real gap."""
    return _check_post_fit_calibration_gap(
        graded, fit_at, "no shrinkage fit on record yet -- run fit_shrinkage.py first"
    )


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
    post_fit_gap: Optional[float],
    post_fit_status: str,
    post_shrinkage_gap: Optional[float],
    post_shrinkage_status: str,
    edge_result: Optional[dict],
    edge_status: str,
) -> tuple[str, bool]:
    """Returns (recommendation_text, recalibration_suggested)."""
    if sample_status != "ok":
        return (
            f"Sample below the {INTERIM_REPORTING_FLOOR}-leg interim reporting "
            f"floor -- no recalibration recommendation this cycle. Keep grading.",
            False,
        )

    notes = []
    recalibration_suggested = False

    if calibration_status == "ok" and calibration_gap is not None:
        if abs(calibration_gap) >= 0.05:
            direction = "overconfident" if calibration_gap > 0 else "underconfident"
            notes.append(
                f"All-time model confidence looks {direction} by {abs(calibration_gap):.1%} "
                f"on average (stated confidence vs. real win rate, across every graded leg "
                f"ever, including ones flagged before the last sigma fit -- see the post-fit "
                f"figure below for the number that actually matters right now)."
            )
        else:
            notes.append("All-time stated confidence tracks real win rate reasonably well.")
    else:
        notes.append(f"All-time calibration check: {calibration_status}.")

    if post_fit_status == "ok" and post_fit_gap is not None:
        if abs(post_fit_gap) >= RECALIBRATION_GAP_THRESHOLD:
            direction = "overconfident" if post_fit_gap > 0 else "underconfident"
            notes.append(
                f"RECALIBRATION SUGGESTED: since the last sigma fit, real legs show the "
                f"model is {direction} by {abs(post_fit_gap):.1%} on average -- above the "
                f"{RECALIBRATION_GAP_THRESHOLD:.0%} threshold. Run "
                f"`python scripts/calibration/fit_sigma_recalibration.py` to refit "
                f"SIGMA_CALIBRATION_FACTOR against current data."
            )
            recalibration_suggested = True
        else:
            notes.append(
                f"Post-fit calibration gap ({post_fit_gap:+.1%}) is within the "
                f"{RECALIBRATION_GAP_THRESHOLD:.0%} threshold -- no re-fit needed yet."
            )
    else:
        notes.append(f"Post-fit calibration check: {post_fit_status}.")

    if post_shrinkage_status == "ok" and post_shrinkage_gap is not None:
        if abs(post_shrinkage_gap) >= RECALIBRATION_GAP_THRESHOLD:
            direction = "overconfident" if post_shrinkage_gap > 0 else "underconfident"
            notes.append(
                f"RECALIBRATION SUGGESTED: since the last shrinkage fit, real legs show "
                f"the model is {direction} by {abs(post_shrinkage_gap):.1%} on average -- "
                f"above the {RECALIBRATION_GAP_THRESHOLD:.0%} threshold. Run "
                f"`python scripts/calibration/fit_shrinkage.py` to refit "
                f"SHRINKAGE_PRIOR_STRENGTH_K against current data."
            )
            recalibration_suggested = True
        else:
            notes.append(
                f"Post-shrinkage-fit calibration gap ({post_shrinkage_gap:+.1%}) is within "
                f"the {RECALIBRATION_GAP_THRESHOLD:.0%} threshold -- no re-fit needed yet."
            )
    else:
        notes.append(f"Post-shrinkage-fit calibration check: {post_shrinkage_status}.")

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

    return " ".join(notes), recalibration_suggested


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

    n_games_cumulative = count_games(graded_all)

    sample_status = "ok" if n_cumulative >= INTERIM_REPORTING_FLOOR else "insufficient_sample"

    calibration_gap, calibration_status = check_calibration_gap(graded_all)
    fit_at = last_sigma_fit_at()
    post_fit_gap, post_fit_status = check_post_fit_calibration_gap(graded_all, fit_at)
    shrinkage_fit_at = last_shrinkage_fit_at()
    post_shrinkage_gap, post_shrinkage_status = check_post_shrinkage_calibration_gap(
        graded_all, shrinkage_fit_at
    )
    edge_result, edge_status = check_edge_threshold_effectiveness(graded_all)

    recommendation, recalibration_suggested = build_recommendation(
        sample_status,
        calibration_gap,
        calibration_status,
        post_fit_gap,
        post_fit_status,
        post_shrinkage_gap,
        post_shrinkage_status,
        edge_result,
        edge_status,
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
        "n_games_cumulative": n_games_cumulative,
        "pct_of_games_target_reached": round(100 * n_games_cumulative / FULL_SAMPLE_GAMES_THRESHOLD, 2),
        "sample_status": sample_status,
        "calibration_gap": calibration_gap,
        "calibration_check_status": calibration_status,
        "post_fit_calibration_gap": post_fit_gap,
        "post_fit_check_status": post_fit_status,
        "post_shrinkage_calibration_gap": post_shrinkage_gap,
        "post_shrinkage_check_status": post_shrinkage_status,
        "recalibration_suggested": recalibration_suggested,
        "edge_threshold_effectiveness": edge_result,
        "edge_check_status": edge_status,
        "recommendation": recommendation,
    }

    review_log = pd.concat([review_log, pd.DataFrame([new_row])], ignore_index=True)
    REVIEW_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    review_log.to_csv(REVIEW_LOG_PATH, index=False)

    log.info(
        "Review %s complete: %d graded this period (%d cumulative, %d games). "
        "sample_status=%s. Recommendation: %s",
        review_id, n_this_period, n_cumulative, n_games_cumulative, sample_status, recommendation,
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
        "n_games_cumulative", "pct_of_games_target_reached", "sample_status", "recommendation",
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
