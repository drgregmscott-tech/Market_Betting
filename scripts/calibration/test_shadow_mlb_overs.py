"""Tests for the Session 2.65 shadow measure (run with pytest)."""

import sys
from pathlib import Path
from unittest import mock

import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
import auto_grade_outcomes as grader  # noqa: E402
import clv_logger  # noqa: E402
import shadow_mlb_overs as shadow  # noqa: E402


def _est(**kw):
    row = {
        "platform": "prizepicks", "source_line_id": "s1", "player_name": "A Hitter", "team": "NYY",
        "sport": "mlb", "stat_type": "Hits", "resolved_stat_key": "hits", "line": 0.5,
        "odds_type": "standard", "game_id": "g1", "game_start_time": "2099-01-01T20:00:00Z",
        "status": "active", "pulled_at": "2026-09-19T12:00:00Z", "model_status": "estimated",
        "season_avg": 1.0, "recent_form": 1.0, "model_mean": 1.0, "model_sigma": 0.8, "games_used": 30,
        "prob_over": 0.62, "prob_under": 0.38, "implied_prob_over": 0.5491, "implied_prob_under": 0.5491,
        "edge_over": None, "edge_under": 0.0,
    }
    row.update(kw)
    return row


def _empty_log():
    return pd.DataFrame(columns=clv_logger.CLV_LOG_COLUMNS_PICKEM, dtype=object)


def test_build_keeps_only_prizepicks_mlb_standard_and_computes_the_over_edge():
    df = pd.DataFrame([
        _est(source_line_id="keep"),
        _est(source_line_id="nfl", sport="nfl"),
        _est(source_line_id="ud", platform="underdog"),
        _est(source_line_id="demon", odds_type="demon"),
        _est(source_line_id="unscored", model_status="unsupported_odds_type"),
        _est(source_line_id="noprob", prob_over=None),
    ])
    out = shadow.build_shadow_estimates(df)
    assert list(out["source_line_id"]) == ["keep"]
    assert out["edge_over"].iloc[0] == pytest.approx(0.62 - 0.5491)
    assert out["edge_under"].isna().all()


def test_shadow_run_flags_the_over_that_the_real_rule_refuses():
    est = pd.DataFrame([_est()])
    real = clv_logger.process_run_pickem(est.assign(edge_over=None), _empty_log(), "2026-09-19T12:00:00Z")
    assert real.empty  # the real path computes no over edge, flags nothing
    shadow_log = clv_logger.process_run_pickem(
        shadow.build_shadow_estimates(est), _empty_log(), "2026-09-19T12:00:00Z", unflagged_sides=frozenset()
    )
    assert len(shadow_log) == 1 and shadow_log.iloc[0]["flagged_side"] == "over"
    # and the shadow flag stays open on the next run instead of being retired by the real rule
    again = clv_logger.process_run_pickem(
        shadow.build_shadow_estimates(est), shadow_log, "2026-09-19T13:00:00Z", unflagged_sides=frozenset()
    )
    assert again.iloc[0]["status"] == "open"


def test_below_threshold_over_is_not_a_shadow_flag():
    est = pd.DataFrame([_est(prob_over=0.56)])  # edge 0.0109 < 0.03
    out = clv_logger.process_run_pickem(
        shadow.build_shadow_estimates(est), _empty_log(), "2026-09-19T12:00:00Z", unflagged_sides=frozenset()
    )
    assert out.empty


def _outcomes(n, wins, games=40):
    return pd.DataFrame({
        "flag_id": [f"f{i}" for i in range(n)],
        "result": ["win"] * wins + ["loss"] * (n - wins),
        "first_flagged_model_prob": 0.6,
    }), pd.DataFrame({"flag_id": [f"f{i}" for i in range(n)], "game_id": [f"g{i % games}" for i in range(n)]})


def test_summary_needs_enough_legs_and_games_before_any_verdict():
    assert shadow.summarize(*_outcomes(0, 0))["verdict"] == "insufficient_data"
    assert shadow.summarize(*_outcomes(100, 40))["verdict"] == "insufficient_data"
    assert shadow.summarize(*_outcomes(400, 160, games=10))["verdict"] == "insufficient_data"  # 10 games only


def test_summary_verdicts():
    assert shadow.summarize(*_outcomes(2000, 900, games=100))["verdict"] == "still_below"   # 45%
    assert shadow.summarize(*_outcomes(2000, 1240, games=100))["verdict"] == "recovered"    # 62%
    assert shadow.summarize(*_outcomes(300, 165, games=40))["verdict"] == "inconclusive"    # 55%, wide interval


def test_grade_writes_only_to_the_shadow_outcome_file(tmp_path, monkeypatch):
    monkeypatch.setattr(shadow, "SHADOW_OUTCOME_LOG_PATH", tmp_path / "shadow_outcome_log.csv")
    monkeypatch.setattr(shadow, "SHADOW_CLV_LOG_PATH", tmp_path / "shadow_clv_log.csv")
    real_outcomes = grader.OUTCOME_LOG_PATH
    before = real_outcomes.stat().st_mtime if real_outcomes.exists() else None
    canned = [{"flag_id": "x", "reported_at": "t", "result": "win"}]
    with mock.patch.object(grader, "_run_adapter", return_value=(canned, {"graded": 1})) as run_adapter:
        shadow.grade()
    assert (tmp_path / "shadow_outcome_log.csv").exists()
    assert run_adapter.call_args.args[0] is grader.MLB_ADAPTER          # MLB only
    assert (real_outcomes.stat().st_mtime if real_outcomes.exists() else None) == before  # real log untouched
