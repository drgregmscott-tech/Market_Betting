"""Tests for Session 6.11 props outcome grading (run with pytest)."""

import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import auto_grade_outcomes as grader  # noqa: E402
import clv_logger  # noqa: E402
import grade_props_outcomes as props  # noqa: E402
import props_sample_report as report  # noqa: E402


def _flag(name, stat_type, platform="draftkings", start="2026-09-13T17:00:00Z", flag_id=None, **kw):
    row = {
        "flag_id": flag_id or f"{platform}|{name}|{stat_type}", "track": "props", "flagged_side": "over",
        "first_flagged_at": "2026-09-10T12:00:00Z", "first_flagged_model_prob": 0.3,
        "first_flagged_market_price": 0.2, "first_flagged_edge": 0.1, "consensus_available": False,
        "status": "closed", "clv_edge_at_close": 0.1, "platform": platform, "player_name": name,
        "sport": "NFL", "stat_type": stat_type, "resolved_stat_key": "rushing_tds+receiving_tds",
        "game_id": "g1", "game_start_time": start,
    }
    row.update(kw)
    return row


class _Plugin:
    name = "nfl"
    sport_labels = frozenset({"nfl"})
    computed_stat_types: dict = {}
    computed_required_columns: dict = {}

    def fetch_stats(self, season):
        return pd.DataFrame({
            "player_id": ["A", "B", "C"], "player_name": ["Scorer One", "Scorer Two", "Blank Bob"],
            "season": [2026] * 3, "week": [1] * 3, "team": ["X", "X", "X"],
            "rushing_tds": [1, 0, 0], "receiving_tds": [1, 2, 0],
        })


def _adapter():
    return grader.GradingAdapter(
        plugin=_Plugin(),
        load_context=lambda: pd.DataFrame({
            "season": [2026], "week": [1], "gameday": ["2026-09-13"], "home_team": ["X"], "away_team": ["Y"],
        }),
        find_game_row=props.find_props_nfl_game_row,
    )


def _grade(flags, monkeypatch, tmp_path):
    monkeypatch.setattr(grader, "build_name_lookup", lambda df: dict(zip(
        df["player_name"].str.lower().str.replace(" ", ""), df["player_id"])))
    monkeypatch.setattr(grader, "normalize_name", lambda n: n.lower().replace(" ", ""))
    monkeypatch.setattr(grader, "current_pickem_season", lambda d: 2026)
    out_path = tmp_path / "outcome_log.csv"
    props.run(clv_df=pd.DataFrame(flags), outcome_df=props.load_props_outcomes(out_path),
              outcome_path=out_path, adapters=[_adapter()])
    return pd.read_csv(out_path) if out_path.exists() else pd.DataFrame(columns=["flag_id", "result"])


def test_anytime_td_win_and_loss(monkeypatch, tmp_path):
    out = _grade([_flag("Scorer One", "Anytime TD Scorer"), _flag("Blank Bob", "Anytime TD Scorer")],
                 monkeypatch, tmp_path)
    res = dict(zip(out["flag_id"], out["result"]))
    assert res["draftkings|Blank Bob|Anytime TD Scorer"] == "loss"
    assert res["draftkings|Scorer One|Anytime TD Scorer"] == "win"


def test_two_plus_tds_uses_line_1_5_and_is_not_voided_by_anytime(monkeypatch, tmp_path):
    flags = [
        _flag("Scorer Two", "Anytime TD Scorer"), _flag("Scorer Two", "2+ TDs"),
        _flag("Scorer One", "2+ TDs"),  # 1 rushing + 1 receiving = 2
        _flag("Blank Bob", "2+ TDs"),
    ]
    out = _grade(flags, monkeypatch, tmp_path)
    res = dict(zip(out["flag_id"], out["result"]))
    assert res["draftkings|Scorer Two|Anytime TD Scorer"] == "win"
    assert res["draftkings|Scorer Two|2+ TDs"] == "win"  # 2 receiving TDs
    assert res["draftkings|Scorer One|2+ TDs"] == "win"
    assert res["draftkings|Blank Bob|2+ TDs"] == "loss"
    assert "void" not in set(out["result"])


def test_player_with_no_game_row_stays_ungraded(monkeypatch, tmp_path):
    assert _grade([_flag("Nobody Here", "Anytime TD Scorer")], monkeypatch, tmp_path).empty


def test_no_pushes_on_half_point_lines():
    assert props.props_line_for("anytd") == 0.5 and props.props_line_for("2+ TDs") == 1.5
    assert grader.grade_result("over", 0.5, 0.0) == "loss" and grader.grade_result("over", 1.5, 2.0) == "win"


def test_futures_and_unknown_markets_are_left_ungraded(monkeypatch, tmp_path):
    flags = [_flag("Scorer One", "Rushing Yards - Season"), _flag("Scorer One", "First TD Scorer")]
    assert props.prepare_props_flags(pd.DataFrame(flags)).empty
    assert _grade(flags, monkeypatch, tmp_path).empty


def test_betmgm_missing_start_time_uses_next_scheduled_game(monkeypatch, tmp_path):
    out = _grade([_flag("Scorer One", "anytd", platform="betmgm", start=None)], monkeypatch, tmp_path)
    assert list(out["result"]) == ["win"]


def test_betmgm_flag_after_the_game_finds_no_game(monkeypatch, tmp_path):
    flags = [_flag("Scorer One", "anytd", platform="betmgm", start=None, first_flagged_at="2026-09-20T12:00:00Z")]
    assert _grade(flags, monkeypatch, tmp_path).empty


def test_grading_twice_does_not_duplicate(monkeypatch, tmp_path):
    flags = [_flag("Scorer One", "Anytime TD Scorer")]
    _grade(flags, monkeypatch, tmp_path)
    assert len(_grade(flags, monkeypatch, tmp_path)) == 1


def test_report_counts_real_graded_legs(tmp_path):
    clv = pd.DataFrame([
        _flag("A", "anytd", flag_id="f1", game_id="g1"), _flag("B", "anytd", flag_id="f2", game_id="g2"),
        _flag("C", "anytd", flag_id="f3", game_id="g2"),
    ])
    path = tmp_path / "o.csv"
    pd.DataFrame({"flag_id": ["f1", "f2", "f3"], "result": ["win", "loss", "void"]}).to_csv(path, index=False)
    r = report.summarize_graded(clv, path)
    assert (r["graded_legs"], r["graded_games"], r["wins"], r["losses"], r["closed_but_ungraded"]) == (2, 2, 1, 1, 1)


def test_clv_logger_props_carries_model_components():
    est = pd.DataFrame([{
        "platform": "draftkings", "source_market_id": 1.0, "source_selection_id": "s", "player_name": "P",
        "sport": "NFL", "stat_type": "Anytime TD Scorer", "resolved_stat_key": "rushing_tds+receiving_tds",
        "model_status": "estimated", "prob_over": 0.4, "implied_prob_over": 0.2, "edge_over": 0.2,
        "edge_under": None, "season_avg": 0.5, "recent_form": 0.6, "model_mean": 0.55, "games_played": 3,
    }])
    cands = clv_logger.build_props_candidates(est)
    assert cands[0]["model_mean"] == 0.55 and cands[0]["games_played"] == 3
    assert "model_mean" in clv_logger.CLV_LOG_COLUMNS_PROPS
