"""
Session 2.54 -- tests for weekly_review.py.

WHY THIS FILE EXISTS
---------------------
weekly_review.py runs unattended every week (pickem_weekly_review.yml) and
decides whether to tell a person to recalibrate the model. It had no tests.
These tests fix the behavior of its checks and of the file it writes, using
small synthetic data in a temporary folder. They never touch the real
outcome, clv or review logs.

Run: python -m pytest scripts/calibration/test_weekly_review.py -v
"""

import logging
import sys
from pathlib import Path

import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
import weekly_review as wr  # noqa: E402

wr.log = logging.getLogger("weekly_review_test")  # keep tests out of logs/weekly_review.log


def _legs(n_win: int, n_loss: int, prob: float = 0.6, edge: float = 0.05, flagged: str = "2026-09-10T12:00:00Z"):
    rows = [{"result": "win"}] * n_win + [{"result": "loss"}] * n_loss
    df = pd.DataFrame(rows)
    df["first_flagged_model_prob"] = prob
    df["first_flagged_edge"] = edge
    df["first_flagged_at"] = pd.Timestamp(flagged)
    return df


# --- check_calibration_gap --------------------------------------------------
def test_calibration_gap_is_stated_confidence_minus_win_rate():
    gap, status = wr.check_calibration_gap(_legs(30, 70, prob=0.60))  # win rate 0.30
    assert status == "ok"
    assert gap == pytest.approx(0.30)


def test_calibration_gap_needs_minimum_sample():
    gap, status = wr.check_calibration_gap(_legs(5, 5))
    assert gap is None and status.startswith("insufficient sample")


def test_calibration_gap_ignores_rows_without_a_stated_probability():
    df = _legs(30, 30)
    df.loc[:9, "first_flagged_model_prob"] = None  # the first 10 rows are wins
    gap, status = wr.check_calibration_gap(df)
    assert status == "ok"
    assert gap == pytest.approx(0.60 - 20 / 50)  # 50 usable rows, 20 wins


# --- post-fit checks (Session 2.41e: filter on flag time, not grade time) ---
def test_post_fit_gap_only_counts_legs_flagged_after_the_fit():
    old = _legs(40, 0, prob=0.9, flagged="2026-09-10T12:00:00Z")  # flagged before the fit
    new = _legs(15, 15, prob=0.5, flagged="2026-09-15T12:00:00Z")  # flagged after
    fit_at = pd.Timestamp("2026-09-12T00:00:00Z")
    gap, status = wr.check_post_fit_calibration_gap(pd.concat([old, new], ignore_index=True), fit_at)
    assert status == "ok"
    assert gap == pytest.approx(0.0)  # old legs must not leak in


def test_post_fit_gap_reports_insufficient_when_no_leg_was_flagged_since_fit():
    graded = _legs(40, 0, flagged="2026-09-10T12:00:00Z")
    gap, status = wr.check_post_fit_calibration_gap(graded, pd.Timestamp("2026-09-12T00:00:00Z"))
    assert gap is None and "insufficient post-fit sample" in status


def test_post_fit_gap_without_a_fit_on_record():
    gap, status = wr.check_post_fit_calibration_gap(_legs(40, 40), None)
    assert gap is None and "no sigma fit" in status
    gap, status = wr.check_post_shrinkage_calibration_gap(_legs(40, 40), None)
    assert gap is None and "no shrinkage fit" in status


# --- edge threshold check ---------------------------------------------------
def test_edge_check_splits_at_the_median_and_compares_win_rates():
    high = _legs(30, 10, edge=0.10)  # 75% wins
    low = _legs(15, 25, edge=0.01)  # 37.5% wins
    result, status = wr.check_edge_threshold_effectiveness(pd.concat([high, low], ignore_index=True))
    assert status == "ok"
    assert result["n_high_edge"] == 40 and result["n_low_edge"] == 40
    assert result["high_minus_low"] == pytest.approx(0.375)


def test_edge_check_needs_enough_legs():
    result, status = wr.check_edge_threshold_effectiveness(_legs(10, 10))
    assert result is None and status.startswith("insufficient sample")


# --- build_recommendation ---------------------------------------------------
def _rec(**kw):
    args = dict(
        sample_status="ok", calibration_gap=0.0, calibration_status="ok",
        post_fit_gap=0.0, post_fit_status="ok", post_shrinkage_gap=0.0, post_shrinkage_status="ok",
        edge_result={"high_minus_low": 0.10, "win_rate_high_edge": 0.6, "win_rate_low_edge": 0.5},
        edge_status="ok",
    )
    args.update(kw)
    return wr.build_recommendation(**args)


def test_recommendation_below_sample_floor_never_suggests_recalibration():
    text, suggested = _rec(sample_status="insufficient_sample", post_fit_gap=0.5)
    assert suggested is False and "interim reporting floor" in text


def test_recommendation_flags_sigma_drift_at_the_threshold():
    text, suggested = _rec(post_fit_gap=wr.RECALIBRATION_GAP_THRESHOLD)
    assert suggested is True and "fit_sigma_recalibration.py" in text


def test_recommendation_flags_shrinkage_drift_in_either_direction():
    text, suggested = _rec(post_shrinkage_gap=-0.05)
    assert suggested is True and "underconfident" in text and "fit_shrinkage.py" in text


def test_recommendation_quiet_when_everything_is_within_threshold():
    text, suggested = _rec(post_fit_gap=0.02, post_shrinkage_gap=-0.02)
    assert suggested is False and "no re-fit needed" in text


def test_recommendation_warns_when_high_edge_flags_do_not_outperform():
    text, _ = _rec(edge_result={"high_minus_low": 0.01, "win_rate_high_edge": 0.51, "win_rate_low_edge": 0.50})
    assert "FLAG_EDGE_THRESHOLD" in text


# --- run_review, end to end on temporary files ------------------------------
@pytest.fixture
def tmp_logs(tmp_path, monkeypatch):
    monkeypatch.setattr(wr, "OUTCOME_LOG_PATH", tmp_path / "outcome_log.csv")
    monkeypatch.setattr(wr, "CLV_LOG_PATH", tmp_path / "clv_log.csv")
    monkeypatch.setattr(wr, "REVIEW_LOG_PATH", tmp_path / "review_log.csv")
    monkeypatch.setattr(wr, "SIGMA_FIT_LOG_PATH", tmp_path / "sigma_fit.csv")
    monkeypatch.setattr(wr, "SHRINKAGE_FIT_LOG_PATH", tmp_path / "shrink_fit.csv")
    return tmp_path


def _write_outcomes(tmp, n=60, reported="2026-09-16T00:00:00Z"):
    rows = [{
        "flag_id": f"f{i}", "reported_at": reported, "result": "win" if i % 2 == 0 else "loss",
        "first_flagged_model_prob": 0.55, "first_flagged_edge": 0.04 + (i % 5) * 0.01,
    } for i in range(n)]
    pd.DataFrame(rows).to_csv(tmp / "outcome_log.csv", index=False)
    pd.DataFrame({"flag_id": [f"f{i}" for i in range(n)], "first_flagged_at": ["2026-09-15T12:00:00Z"] * n}
                 ).to_csv(tmp / "clv_log.csv", index=False)


def test_run_review_writes_a_row_and_second_run_reports_only_new_legs(tmp_logs):
    _write_outcomes(tmp_logs, n=60)
    first = wr.run_review()
    assert first["n_graded_cumulative"] == 60 and first["n_graded_this_period"] == 60
    assert first["sample_status"] == "ok"
    assert first["win_rate_cumulative"] == pytest.approx(0.5)
    assert first["post_fit_check_status"].startswith("no sigma fit")

    second = wr.run_review()  # nothing graded after the first run's period_end
    assert second["n_graded_this_period"] == 0 and second["win_rate_this_period"] is None
    log_df = pd.read_csv(tmp_logs / "review_log.csv")
    assert len(log_df) == 2 and list(log_df.columns) == wr.REVIEW_LOG_COLUMNS


def test_run_review_below_floor_still_logs_but_says_insufficient(tmp_logs):
    _write_outcomes(tmp_logs, n=10)
    row = wr.run_review()
    assert row["sample_status"] == "insufficient_sample" and row["recalibration_suggested"] is False
    assert len(pd.read_csv(tmp_logs / "review_log.csv")) == 1


def test_run_review_without_an_outcome_log_raises(tmp_logs):
    with pytest.raises(FileNotFoundError):
        wr.run_review()
