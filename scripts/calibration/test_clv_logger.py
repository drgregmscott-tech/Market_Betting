"""
Session 2.4 -- Validation harness for clv_logger.py, using synthetic
fixtures shaped like real pickem_model.py output (same reasoning as Session
2.2's test_ingest_pickem.py: this sandbox's network does not reach the real
pick'em endpoints or nflverse, so the logger's own matching/open/close/
idempotency logic needs to be provable without live data before handoff).

Six scenarios:
1. A new flag is created correctly, WITH a real cross-platform consensus match.
2. A new flag is created correctly, WITHOUT a consensus match available.
3. A row below FLAG_EDGE_THRESHOLD is never flagged.
4. An open flag is refreshed (not duplicated) across a second run where the
   prop is still present, including when its own line has moved.
5. A flag transitions to "closed" once its prop disappears from a run, with
   closing values frozen and clv_edge_at_close computed correctly.
6. Running the exact same estimates file through the logger twice in a row
   does not create duplicate or double-updated rows (idempotency).
"""

import shutil
import tempfile
from pathlib import Path

import pandas as pd

import clv_logger


def _base_row(**overrides):
    row = {
        "platform": "prizepicks",
        "source_line_id": "pp_1",
        "player_name": "Patrick Mahomes",
        "team": "KC",
        "sport": "nfl",
        "stat_type": "Pass Yards",
        "resolved_stat_key": "passing_yards",
        "line": 275.5,
        "over_payout_multiplier": None,
        "under_payout_multiplier": None,
        "game_id": "game_1",
        "game_start_time": "2026-09-07T17:00:00Z",
        "status": "active",
        "pulled_at": "2026-09-01T10:00:00Z",
        "model_status": "estimated",
        "season_avg": 270.0,
        "recent_form": 280.0,
        "model_mean": 275.0,
        "model_sigma": 30.0,
        "games_used": 5,
        "prob_over": 0.60,
        "prob_under": 0.40,
        "implied_prob_over": 0.50,
        "implied_prob_under": 0.50,
        "edge_over": 0.10,
        "edge_under": -0.10,
    }
    row.update(overrides)
    return row


def scenario_1_new_flag_with_consensus():
    pp_row = _base_row()
    ud_row = _base_row(
        platform="underdog",
        source_line_id="ud_1",
        line=270.5,
        over_payout_multiplier=1.9,
        under_payout_multiplier=1.9,
        implied_prob_over=0.5,
        implied_prob_under=0.5,
        edge_over=0.10,
        edge_under=-0.10,
    )
    estimates_df = pd.DataFrame([pp_row, ud_row])
    log_df = clv_logger.process_run(estimates_df, clv_logger.load_clv_log(), "2026-09-01T10:00:00Z")

    # Both platforms independently clear the edge threshold here, so both
    # get logged, each pointing at the other as its consensus match.
    assert len(log_df) == 2, f"expected 2 flags (both platforms clear threshold), got {len(log_df)}"
    r = log_df[log_df["flag_id"] == "prizepicks|pp_1"].iloc[0]
    assert r["flagged_side"] == "over"
    assert r["consensus_available"] == True  # noqa: E712
    assert r["consensus_platform"] == "underdog"
    assert abs(r["consensus_implied_prob_same_side"] - 0.5) < 1e-9
    assert abs(r["consensus_edge"] - (0.60 - 0.5)) < 1e-9
    assert r["status"] == "open"
    print("PASS: scenario_1_new_flag_with_consensus")


def scenario_2_new_flag_without_consensus():
    pp_row = _base_row(game_id="game_solo")
    estimates_df = pd.DataFrame([pp_row])
    log_df = clv_logger.process_run(estimates_df, clv_logger.load_clv_log(), "2026-09-01T10:00:00Z")

    assert len(log_df) == 1
    r = log_df.iloc[0]
    assert r["consensus_available"] == False  # noqa: E712
    assert pd.isna(r["consensus_edge"])
    print("PASS: scenario_2_new_flag_without_consensus")


def scenario_3_below_threshold_not_flagged():
    pp_row = _base_row(
        source_line_id="pp_small_edge",
        prob_over=0.51, prob_under=0.49,
        edge_over=0.01, edge_under=-0.01,
    )
    estimates_df = pd.DataFrame([pp_row])
    log_df = clv_logger.process_run(estimates_df, clv_logger.load_clv_log(), "2026-09-01T10:00:00Z")
    assert len(log_df) == 0, f"expected 0 flags below threshold, got {len(log_df)}"
    print("PASS: scenario_3_below_threshold_not_flagged")


def scenario_4_refresh_open_flag_line_moves():
    pp_row_run1 = _base_row(source_line_id="pp_refresh", line=275.5)
    estimates_run1 = pd.DataFrame([pp_row_run1])
    log_after_run1 = clv_logger.process_run(estimates_run1, clv_logger.load_clv_log(), "2026-09-01T10:00:00Z")
    assert len(log_after_run1) == 1
    assert log_after_run1.iloc[0]["last_seen_line"] == 275.5

    # Run 2: same prop still present, but the platform's own line has moved.
    pp_row_run2 = _base_row(source_line_id="pp_refresh", line=278.0)
    estimates_run2 = pd.DataFrame([pp_row_run2])
    log_after_run2 = clv_logger.process_run(estimates_run2, log_after_run1, "2026-09-01T11:00:00Z")

    assert len(log_after_run2) == 1, "refresh must not create a duplicate row"
    r = log_after_run2.iloc[0]
    assert r["status"] == "open"
    assert r["last_seen_line"] == 278.0
    assert r["first_flagged_line"] == 275.5, "first_flagged_line must never change on refresh"
    assert r["last_seen_at"] == "2026-09-01T11:00:00Z"
    print("PASS: scenario_4_refresh_open_flag_line_moves")


def scenario_5_flag_closes_when_prop_disappears():
    pp_row_run1 = _base_row(source_line_id="pp_close_me", line=275.5, prob_over=0.60)
    estimates_run1 = pd.DataFrame([pp_row_run1])
    log_after_run1 = clv_logger.process_run(estimates_run1, clv_logger.load_clv_log(), "2026-09-01T10:00:00Z")

    # Run 2: line moves while still open.
    pp_row_run2 = _base_row(source_line_id="pp_close_me", line=277.0, prob_over=0.60)
    estimates_run2 = pd.DataFrame([pp_row_run2])
    log_after_run2 = clv_logger.process_run(estimates_run2, log_after_run1, "2026-09-01T11:00:00Z")

    # Run 3: prop is gone (empty estimates for this flag_id -- game locked).
    other_row = _base_row(source_line_id="pp_unrelated", game_id="game_other")
    estimates_run3 = pd.DataFrame([other_row])
    log_after_run3 = clv_logger.process_run(estimates_run3, log_after_run2, "2026-09-01T12:00:00Z")

    closed = log_after_run3[log_after_run3["flag_id"] == "prizepicks|pp_close_me"].iloc[0]
    assert closed["status"] == "closed"
    assert closed["closing_line"] == 277.0
    assert closed["closing_pulled_at"] == "2026-09-01T11:00:00Z"
    assert closed["line_moved"] == True  # noqa: E712 -- 277.0 != 275.5
    expected_clv_edge = 0.60 - closed["closing_implied_prob"]
    assert abs(closed["clv_edge_at_close"] - expected_clv_edge) < 1e-9
    print("PASS: scenario_5_flag_closes_when_prop_disappears")


def scenario_6_idempotent_same_file_twice():
    pp_row = _base_row(source_line_id="pp_idempotent")
    estimates_df = pd.DataFrame([pp_row])
    log_after_first = clv_logger.process_run(estimates_df, clv_logger.load_clv_log(), "2026-09-01T10:00:00Z")
    assert len(log_after_first) == 1

    # Re-run the SAME file against the SAME timestamp -- must not duplicate
    # or double-count the flag.
    log_after_second = clv_logger.process_run(estimates_df, log_after_first, "2026-09-01T10:00:00Z")
    assert len(log_after_second) == 1, f"expected idempotent single row, got {len(log_after_second)}"
    print("PASS: scenario_6_idempotent_same_file_twice")


def run_all():
    # Redirect logging to a throwaway location so the test doesn't write
    # into a real repo's logs/ directory.
    tmp_dir = Path(tempfile.mkdtemp())
    clv_logger.LOG_PATH = tmp_dir / "clv_logging.log"
    clv_logger.log = clv_logger.setup_logging()

    scenario_1_new_flag_with_consensus()
    scenario_2_new_flag_without_consensus()
    scenario_3_below_threshold_not_flagged()
    scenario_4_refresh_open_flag_line_moves()
    scenario_5_flag_closes_when_prop_disappears()
    scenario_6_idempotent_same_file_twice()

    shutil.rmtree(tmp_dir, ignore_errors=True)
    print("\nAll 6 scenarios passed.")


if __name__ == "__main__":
    run_all()
