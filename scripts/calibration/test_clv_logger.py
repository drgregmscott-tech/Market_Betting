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


def _empty_pickem_log() -> pd.DataFrame:
    """An isolated, empty pickem CLV log fixture -- every scenario below
    must start from this, never from `clv_logger.load_clv_log_pickem()`
    directly. That function reads the real, ever-growing production file
    at `data/pickem/clv_log.csv` (thousands of real rows as of Session
    6.x), which made every scenario's row-count assertions fail against
    live data instead of proving the logic in isolation -- a real,
    pre-existing test-isolation bug found 2026-09-10 while fixing an
    unrelated props display bug. Matches the isolation pattern
    `_empty_props_log()` already used for the props scenarios below."""
    return pd.DataFrame(columns=clv_logger.CLV_LOG_COLUMNS_PICKEM, dtype=object)


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
    log_df = clv_logger.process_run_pickem(estimates_df, _empty_pickem_log(), "2026-09-01T10:00:00Z")

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
    log_df = clv_logger.process_run_pickem(estimates_df, _empty_pickem_log(), "2026-09-01T10:00:00Z")

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
    log_df = clv_logger.process_run_pickem(estimates_df, _empty_pickem_log(), "2026-09-01T10:00:00Z")
    assert len(log_df) == 0, f"expected 0 flags below threshold, got {len(log_df)}"
    print("PASS: scenario_3_below_threshold_not_flagged")


def scenario_4_refresh_open_flag_line_moves():
    pp_row_run1 = _base_row(source_line_id="pp_refresh", line=275.5)
    estimates_run1 = pd.DataFrame([pp_row_run1])
    log_after_run1 = clv_logger.process_run_pickem(estimates_run1, _empty_pickem_log(), "2026-09-01T10:00:00Z")
    assert len(log_after_run1) == 1
    assert log_after_run1.iloc[0]["last_seen_line"] == 275.5

    # Run 2: same prop still present, but the platform's own line has moved.
    pp_row_run2 = _base_row(source_line_id="pp_refresh", line=278.0)
    estimates_run2 = pd.DataFrame([pp_row_run2])
    log_after_run2 = clv_logger.process_run_pickem(estimates_run2, log_after_run1, "2026-09-01T11:00:00Z")

    assert len(log_after_run2) == 1, "refresh must not create a duplicate row"
    r = log_after_run2.iloc[0]
    assert r["status"] == "open"
    assert r["last_seen_line"] == 278.0
    assert r["first_flagged_line"] == 275.5, "first_flagged_line must never change on refresh"
    assert r["last_seen_at"] == "2026-09-01T11:00:00Z"
    print("PASS: scenario_4_refresh_open_flag_line_moves")


def scenario_5_flag_closes_when_prop_disappears():
    """SESSION 2.19 UPDATE: this scenario now uses Underdog, not PrizePicks
    -- PrizePicks' clv_edge_at_close/line_moved are always None at close
    per the Session 2.19 fix (see scenario_5b below), so they can no
    longer prove a real "the price moved and CLV was computed from that
    real movement" case. Underdog's real per-side payout multipliers
    (over_payout_multiplier/under_payout_multiplier) are what actually
    move -- the point line (`line`) itself is not the signal
    clv_edge_at_close is computed from (that was Session 2.19's second
    bug: line_moved used to compare the wrong field)."""
    ud_row_run1 = _base_row(
        platform="underdog", source_line_id="ud_close_me", line=275.5, prob_over=0.60,
        over_payout_multiplier=1.9, under_payout_multiplier=1.9,
        implied_prob_over=0.50, implied_prob_under=0.50,
    )
    estimates_run1 = pd.DataFrame([ud_row_run1])
    log_after_run1 = clv_logger.process_run_pickem(estimates_run1, _empty_pickem_log(), "2026-09-01T10:00:00Z")

    # Run 2: still open, but the platform's real payout multipliers move
    # (its implied probability shifts from 0.50 to ~0.5645) -- the point
    # line itself stays 275.5, unchanged.
    ud_row_run2 = _base_row(
        platform="underdog", source_line_id="ud_close_me", line=275.5, prob_over=0.60,
        over_payout_multiplier=1.55, under_payout_multiplier=2.0,
        implied_prob_over=0.5634, implied_prob_under=0.4366,
    )
    estimates_run2 = pd.DataFrame([ud_row_run2])
    log_after_run2 = clv_logger.process_run_pickem(estimates_run2, log_after_run1, "2026-09-01T11:00:00Z")

    # Run 3: prop is gone (empty estimates for this flag_id -- game locked).
    other_row = _base_row(source_line_id="pp_unrelated", game_id="game_other")
    estimates_run3 = pd.DataFrame([other_row])
    log_after_run3 = clv_logger.process_run_pickem(estimates_run3, log_after_run2, "2026-09-01T12:00:00Z")

    closed = log_after_run3[log_after_run3["flag_id"] == "underdog|ud_close_me"].iloc[0]
    assert closed["status"] == "closed"
    assert closed["closing_line"] == 275.5, "the point line never moved -- only the implied price did"
    assert closed["closing_pulled_at"] == "2026-09-01T11:00:00Z"
    assert abs(closed["closing_implied_prob"] - 0.5634) < 1e-9
    assert closed["line_moved"] == True, (  # noqa: E712
        "line_moved must reflect the real IMPLIED-PROBABILITY move (0.50 -> "
        "0.5634), not the unchanged point line -- this is Session 2.19's "
        "second bug fix"
    )
    expected_clv_edge = 0.60 - closed["closing_implied_prob"]
    assert abs(closed["clv_edge_at_close"] - expected_clv_edge) < 1e-9
    print("PASS: scenario_5_flag_closes_when_prop_disappears")


def scenario_5b_prizepicks_clv_not_available_at_close():
    """SESSION 2.19: PrizePicks' closing_implied_prob is always the flat,
    constant PRIZEPICKS_ASSUMED_IMPLIED_PROB (0.5) -- the same number used
    to compute first_flagged_edge -- so clv_edge_at_close would always be
    mathematically guaranteed to equal first_flagged_edge (a tautology,
    not real evidence). Locks in the fix: both clv_edge_at_close and
    line_moved must be reported as not-available (None) for PrizePicks at
    close, not a fabricated "real" number."""
    pp_row_run1 = _base_row(source_line_id="pp_no_clv", line=275.5, prob_over=0.60)
    estimates_run1 = pd.DataFrame([pp_row_run1])
    log_after_run1 = clv_logger.process_run_pickem(estimates_run1, _empty_pickem_log(), "2026-09-01T10:00:00Z")

    # Prop disappears next run -- game locked.
    other_row = _base_row(source_line_id="pp_unrelated", game_id="game_other")
    estimates_run2 = pd.DataFrame([other_row])
    log_after_run2 = clv_logger.process_run_pickem(estimates_run2, log_after_run1, "2026-09-01T11:00:00Z")

    closed = log_after_run2[log_after_run2["flag_id"] == "prizepicks|pp_no_clv"].iloc[0]
    assert closed["status"] == "closed"
    assert closed["closing_line"] == 275.5, "closing_line/closing_implied_prob are still recorded for reference"
    assert pd.isna(closed["closing_implied_prob"]) is False  # the raw value is still logged...
    assert closed["line_moved"] is None, "must be reported not-available, never a fabricated real/false value"
    assert closed["clv_edge_at_close"] is None, "must be reported not-available -- this was the tautology bug"
    print("PASS: scenario_5b_prizepicks_clv_not_available_at_close")


def scenario_6_idempotent_same_file_twice():
    pp_row = _base_row(source_line_id="pp_idempotent")
    estimates_df = pd.DataFrame([pp_row])
    log_after_first = clv_logger.process_run_pickem(estimates_df, _empty_pickem_log(), "2026-09-01T10:00:00Z")
    assert len(log_after_first) == 1

    # Re-run the SAME file against the SAME timestamp -- must not duplicate
    # or double-count the flag.
    log_after_second = clv_logger.process_run_pickem(estimates_df, log_after_first, "2026-09-01T10:00:00Z")
    assert len(log_after_second) == 1, f"expected idempotent single row, got {len(log_after_second)}"
    print("PASS: scenario_6_idempotent_same_file_twice")


def _props_base_row(**overrides):
    row = {
        "platform": "draftkings",
        "source_event_id": "evt_1",
        "source_market_id": "mkt_1",
        "source_selection_id": "sel_dk_1",
        "player_name": "Patrick Mahomes",
        "team": "KC",
        "sport": "nfl",
        "stat_type": "Pass Yards",
        "prop_category": "player_performance",
        "resolved_stat_key": "passing_yards",
        "line": 275.5,
        "game_id": "game_1",
        "game_start_time": "2026-09-07T17:00:00Z",
        "model_status": "estimated",
        "prob_over": 0.60,
        "prob_under": 0.40,
        "implied_prob_over": 0.50,
        "implied_prob_under": 0.50,
        "implied_prob_includes_field_vig": False,
        "edge_over": 0.10,
        "edge_under": -0.10,
        "over_american_odds": -110,
        "under_american_odds": -110,
    }
    row.update(overrides)
    return row


def _run_props(estimates_df: pd.DataFrame, existing_log: pd.DataFrame, run_pulled_at: str) -> pd.DataFrame:
    candidates = clv_logger.build_props_candidates(estimates_df)
    present_ids, rows_by_id = clv_logger.build_props_present_and_prices(estimates_df)
    return clv_logger.generic_process_run(
        "props", candidates, present_ids, clv_logger.price_for_side_props(rows_by_id),
        existing_log, run_pulled_at, clv_logger.CLV_LOG_COLUMNS_PROPS, clv_logger.PROPS_EXTRA_COLUMNS,
        odds_for_side_fn=clv_logger.odds_for_side_props(rows_by_id),
    )


def _empty_props_log() -> pd.DataFrame:
    return pd.DataFrame(columns=clv_logger.CLV_LOG_COLUMNS_PROPS, dtype=object)


def scenario_7_props_new_flag_with_consensus():
    dk_row = _props_base_row()
    fd_row = _props_base_row(
        platform="fanduel",
        source_event_id="evt_1_fd",
        source_market_id="mkt_1_fd",
        source_selection_id="sel_fd_1",
        implied_prob_over=0.52,
        implied_prob_under=0.48,
    )
    estimates_df = pd.DataFrame([dk_row, fd_row])
    log_df = _run_props(estimates_df, _empty_props_log(), "2026-09-01T10:00:00Z")

    assert len(log_df) == 2, f"expected 2 flags (both platforms clear threshold), got {len(log_df)}"
    r = log_df[log_df["flag_id"] == "draftkings|mkt_1|sel_dk_1"].iloc[0]
    assert r["flagged_side"] == "over"
    assert r["consensus_available"] == True  # noqa: E712
    assert r["consensus_label"] == "fanduel"
    assert abs(r["consensus_price"] - 0.52) < 1e-9
    assert abs(r["consensus_edge"] - (0.60 - 0.52)) < 1e-9
    assert r["status"] == "open"
    print("PASS: scenario_7_props_new_flag_with_consensus")


def scenario_8_props_new_flag_without_consensus():
    dk_row = _props_base_row(game_id="game_solo")
    estimates_df = pd.DataFrame([dk_row])
    log_df = _run_props(estimates_df, _empty_props_log(), "2026-09-01T10:00:00Z")

    assert len(log_df) == 1
    r = log_df.iloc[0]
    assert r["consensus_available"] == False  # noqa: E712
    assert pd.isna(r["consensus_edge"]) or r["consensus_edge"] is None
    print("PASS: scenario_8_props_new_flag_without_consensus")


def scenario_9_props_below_threshold_not_flagged():
    dk_row = _props_base_row(
        source_selection_id="sel_small_edge",
        prob_over=0.51, prob_under=0.49,
        edge_over=0.01, edge_under=-0.01,
    )
    estimates_df = pd.DataFrame([dk_row])
    log_df = _run_props(estimates_df, _empty_props_log(), "2026-09-01T10:00:00Z")
    assert len(log_df) == 0, f"expected 0 flags below threshold, got {len(log_df)}"
    print("PASS: scenario_9_props_below_threshold_not_flagged")


def scenario_10_props_refresh_and_close():
    row_run1 = _props_base_row(source_selection_id="sel_lifecycle")
    log1 = _run_props(pd.DataFrame([row_run1]), _empty_props_log(), "2026-09-01T10:00:00Z")
    assert len(log1) == 1
    assert log1.iloc[0]["last_seen_market_price"] == 0.50
    assert log1.iloc[0]["over_american_odds"] == -110

    # Run 2: still present, own price AND own displayed American odds
    # move (a real line move, e.g. DK's Anytime TD Scorer price for a
    # player shortening from a long-shot price to a short one as the game
    # approaches -- the real, live bug this scenario locks in: the
    # frontend's Odds column must track the CURRENT line, not the price
    # at first-flag time).
    row_run2 = _props_base_row(
        source_selection_id="sel_lifecycle", implied_prob_over=0.55, implied_prob_under=0.45,
        over_american_odds=-150,
    )
    log2 = _run_props(pd.DataFrame([row_run2]), log1, "2026-09-01T11:00:00Z")
    assert len(log2) == 1, "refresh must not create a duplicate row"
    r = log2.iloc[0]
    assert r["status"] == "open"
    assert r["last_seen_market_price"] == 0.55
    assert r["first_flagged_market_price"] == 0.50, "first_flagged_market_price must never change on refresh"
    assert r["over_american_odds"] == -150, (
        "over_american_odds must refresh to the current run's live price on an "
        "already-open flag -- a real bug found 2026-09-10 (Puka Nacua/DK Anytime "
        "TD Scorer displaying a frozen +970 from first-flag time on the frontend "
        "while DK's real live price had moved to +115) shipped because this "
        "column was written once at flag creation and never refreshed."
    )

    # Run 3: prop disappears (game locked / market pulled).
    other_row = _props_base_row(source_selection_id="sel_unrelated", game_id="game_other")
    log3 = _run_props(pd.DataFrame([other_row]), log2, "2026-09-01T12:00:00Z")
    closed = log3[log3["flag_id"] == "draftkings|mkt_1|sel_lifecycle"].iloc[0]
    assert closed["status"] == "closed"
    assert closed["closing_market_price"] == 0.55
    assert closed["closing_pulled_at"] == "2026-09-01T11:00:00Z"
    assert closed["price_moved"] == True  # noqa: E712
    expected_clv_edge = 0.60 - closed["closing_market_price"]
    assert abs(closed["clv_edge_at_close"] - expected_clv_edge) < 1e-9
    print("PASS: scenario_10_props_refresh_and_close")


def scenario_11_props_idempotent_same_file_twice():
    dk_row = _props_base_row(source_selection_id="sel_idempotent")
    estimates_df = pd.DataFrame([dk_row])
    log_after_first = _run_props(estimates_df, _empty_props_log(), "2026-09-01T10:00:00Z")
    assert len(log_after_first) == 1

    log_after_second = _run_props(estimates_df, log_after_first, "2026-09-01T10:00:00Z")
    assert len(log_after_second) == 1, f"expected idempotent single row, got {len(log_after_second)}"
    print("PASS: scenario_11_props_idempotent_same_file_twice")


def scenario_12_props_betmgm_selection_id_collision():
    """Real bug found 2026-09-10: BetMGM (via Rotowire) reuses the same
    plain numeric source_selection_id across genuinely different real
    markets for the same player -- e.g. Jahmyr Gibbs' real id 16808 was
    simultaneously his Anytime TD Scorer market AND his separate
    rushing+receiving yards market. flag_id built from platform+
    selection_id alone silently collapsed both onto one CLV-log row, each
    overwriting the other's price/status on every refresh. This locks in
    the fix: flag_id must also include source_market_id."""
    anytd_row = _props_base_row(
        platform="betmgm", source_event_id="evt_gibbs", source_market_id="anytd",
        source_selection_id="16808", stat_type="anytd", over_american_odds=-325,
        under_american_odds=None,
    )
    rushrec_row = _props_base_row(
        platform="betmgm", source_event_id="evt_gibbs", source_market_id="rushrec",
        source_selection_id="16808",  # same real selection_id, different real market
        stat_type="rushrec", line=124.5, over_american_odds=-120, under_american_odds=110,
        implied_prob_over=0.52, implied_prob_under=0.48,
    )
    estimates_df = pd.DataFrame([anytd_row, rushrec_row])
    log_df = _run_props(estimates_df, _empty_props_log(), "2026-09-01T10:00:00Z")

    assert len(log_df) == 2, (
        f"expected 2 distinct flags (same selection_id, different market) -- "
        f"got {len(log_df)}, meaning the collision bug is back"
    )
    flag_ids = set(log_df["flag_id"])
    assert flag_ids == {"betmgm|anytd|16808", "betmgm|rushrec|16808"}, flag_ids
    anytd = log_df[log_df["flag_id"] == "betmgm|anytd|16808"].iloc[0]
    rushrec = log_df[log_df["flag_id"] == "betmgm|rushrec|16808"].iloc[0]
    assert anytd["over_american_odds"] == -325
    assert rushrec["over_american_odds"] == -120
    print("PASS: scenario_12_props_betmgm_selection_id_collision")


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
    scenario_5b_prizepicks_clv_not_available_at_close()
    scenario_6_idempotent_same_file_twice()
    scenario_7_props_new_flag_with_consensus()
    scenario_8_props_new_flag_without_consensus()
    scenario_9_props_below_threshold_not_flagged()
    scenario_10_props_refresh_and_close()
    scenario_11_props_idempotent_same_file_twice()
    scenario_12_props_betmgm_selection_id_collision()

    shutil.rmtree(tmp_dir, ignore_errors=True)
    print("\nAll 13 scenarios passed.")


if __name__ == "__main__":
    run_all()
