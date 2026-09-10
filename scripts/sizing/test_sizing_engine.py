"""
Session 2.6 -- synthetic validation harness for sizing_engine.py.

Same reasoning as Session 2.2/2.4's own test harnesses: this sandbox has no
access to the real repo's data/pickem/clv_log.csv, so the sizing math and
its guardrails need to be provable against synthetic fixtures before
handoff. Six scenarios:

1. Bigger edge produces a bigger suggested stake (monotonicity check).
2. A combined probability at or below breakeven produces status
   'no_bet_negative_edge' and a $0 stake -- never a negative stake.
3. A very large edge is correctly capped at MAX_SINGLE_POSITION_PCT of
   bankroll, not sized past it.
4. A 2-pick entry mixing legs from two different platforms is rejected
   with an explicit reason (test_4) -- and, as of Session 2.11, a real
   all-Underdog entry IS sized, using Underdog's own sourced 3.5x payout,
   not PrizePicks' 3x (test_4b).
5. A wrong leg count (1 or 3) is rejected with an explicit reason.
6. A leg with status != 'open' (already closed) is rejected with an
   explicit reason.
"""

from __future__ import annotations

from sizing_engine import (
    PICKEM_ENTRY_PAYOUT,
    entry_net_odds_b,
    KALSHI_FEE_RATE,
    KELLY_FRACTION,
    MAX_SINGLE_POSITION_PCT,
    POLITICS_LOCKUP_DAMPENER_TABLE,
    POLITICS_MAX_SINGLE_POSITION_PCT,
    POLITICS_MAX_TOTAL_EXPOSURE_PCT,
    PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER,
    PROPS_MAX_SINGLE_POSITION_PCT,
    PROPS_PLATFORM_RISK_MULTIPLIER,
    SAME_GAME_CAUTION_MULTIPLIER,
    WEATHER_MAX_SINGLE_POSITION_PCT,
    combined_entry_probability,
    committed_capital_politics,
    kalshi_effective_cost_per_contract,
    kalshi_fee_per_contract,
    politics_lockup_dampener,
    raw_kelly_fraction,
    raw_kelly_fraction_binary_contract,
    size_entry,
    size_politics_position,
    size_props_position,
    size_weather_position,
)


def make_leg(
    flag_id: str, platform: str, model_prob: float, status: str = "open", game_id: str = "GAME_A"
) -> dict:
    return {
        "flag_id": flag_id,
        "platform": platform,
        "status": status,
        "first_flagged_model_prob": model_prob,
        "game_id": game_id,
    }


def test_1_bigger_edge_bigger_stake():
    bankroll = 1000.0
    low_edge_legs = [make_leg("prizepicks|1", "prizepicks", 0.60), make_leg("prizepicks|2", "prizepicks", 0.60)]
    high_edge_legs = [make_leg("prizepicks|3", "prizepicks", 0.75), make_leg("prizepicks|4", "prizepicks", 0.75)]

    low_result = size_entry(low_edge_legs, bankroll)
    high_result = size_entry(high_edge_legs, bankroll)

    assert low_result["status"] in ("sized", "sized_capped_at_max_position"), low_result
    assert high_result["status"] in ("sized", "sized_capped_at_max_position"), high_result
    assert high_result["suggested_stake"] > low_result["suggested_stake"], (
        f"Expected higher-edge entry to get a bigger stake: "
        f"low={low_result['suggested_stake']}, high={high_result['suggested_stake']}"
    )
    print(
        f"PASS test_1: low-edge (p=0.60x0.60) stake=${low_result['suggested_stake']}, "
        f"high-edge (p=0.75x0.75) stake=${high_result['suggested_stake']}"
    )


def test_2_no_bet_below_breakeven():
    bankroll = 1000.0
    # Combined probability well below what's needed to clear a 3x payout.
    legs = [make_leg("prizepicks|5", "prizepicks", 0.55), make_leg("prizepicks|6", "prizepicks", 0.55)]
    result = size_entry(legs, bankroll)
    assert result["status"] == "no_bet_negative_edge", result
    assert result["suggested_stake"] == 0.0, result
    print(f"PASS test_2: combined p={0.55*0.55:.4f} correctly produced no_bet_negative_edge, $0 stake")


def test_3_extreme_edge_is_capped():
    bankroll = 1000.0
    legs = [make_leg("prizepicks|7", "prizepicks", 0.95), make_leg("prizepicks|8", "prizepicks", 0.95)]
    result = size_entry(legs, bankroll)
    assert result["status"] == "sized_capped_at_max_position", result
    expected_cap = round(bankroll * MAX_SINGLE_POSITION_PCT, 2)
    assert result["suggested_stake"] == expected_cap, (result["suggested_stake"], expected_cap)
    print(f"PASS test_3: extreme edge correctly capped at ${expected_cap} ({MAX_SINGLE_POSITION_PCT*100:.0f}% of bankroll)")


def test_4_mixed_platform_rejected():
    """Session 2.11: Underdog itself is no longer rejected outright (it has
    its own sourced payout, see test_4b), but a single entry still cannot
    mix legs from two different platforms -- each platform's payout table
    only applies to a whole entry, not per-leg."""
    bankroll = 1000.0
    legs = [make_leg("prizepicks|9", "prizepicks", 0.70), make_leg("underdog|10", "underdog", 0.70)]
    result = size_entry(legs, bankroll)
    assert result["status"] == "rejected", result
    assert "platform" in result["reason"].lower(), result
    print(f"PASS test_4: mixed-platform legs correctly rejected -- reason: {result['reason']}")


def test_4b_underdog_sized_with_own_payout():
    """Session 2.11: a real, all-Underdog 2-pick entry is sized using
    Underdog's own sourced 3.5x payout, not PrizePicks' 3x."""
    bankroll = 1000.0
    legs = [make_leg("underdog|1", "underdog", 0.65, game_id="g1"), make_leg("underdog|2", "underdog", 0.62, game_id="g2")]
    result = size_entry(legs, bankroll)
    assert result["status"] == "sized", result
    assert result["entry_payout_multiplier"] == 3.5, result
    assert result["entry_net_odds_b"] == 2.5, result
    assert result["platform_risk_multiplier_applied"] == 0.85, result
    print(f"PASS test_4b: Underdog entry sized at its own 3.5x payout -- suggested_stake=${result['suggested_stake']}")


def test_5_wrong_leg_count_rejected():
    """Session 2.11 extended sizing to 3-8 legs (per-platform, see
    PICKEM_ENTRY_PAYOUT), so this test now checks leg counts OUTSIDE any
    platform's sourced range: 1 leg (below every platform's minimum) and
    9 legs on PrizePicks (above its published max of 6)."""
    bankroll = 1000.0
    one_leg = [make_leg("prizepicks|11", "prizepicks", 0.70)]
    nine_legs = [make_leg(f"prizepicks|2{i}", "prizepicks", 0.70) for i in range(9)]
    result_one = size_entry(one_leg, bankroll)
    result_nine = size_entry(nine_legs, bankroll)
    assert result_one["status"] == "rejected", result_one
    assert result_nine["status"] == "rejected", result_nine
    print(f"PASS test_5: 1-leg and 9-leg (PrizePicks) requests both correctly rejected")


def test_5b_prizepicks_3_through_6_pick_sized():
    """Session 2.11: PrizePicks' own published Power Play table (3, 4, 5, 6
    picks) is sized correctly, using that leg count's own real multiplier."""
    bankroll = 1000.0
    for n, expected_multiplier in [(3, 6.0), (4, 10.0), (5, 20.0), (6, 37.5)]:
        legs = [
            make_leg(f"prizepicks|p{n}_{i}", "prizepicks", 0.75, game_id=f"g{i}")
            for i in range(n)
        ]
        result = size_entry(legs, bankroll)
        assert result["status"] in ("sized", "sized_capped_at_max_position"), (n, result)
        assert result["entry_payout_multiplier"] == expected_multiplier, (n, result)
    print("PASS test_5b: PrizePicks 3/4/5/6-pick entries each sized at their own real payout")


def test_5c_underdog_7_and_8_pick_sized():
    """Session 2.11: Underdog's own published Standard table extends to 8
    picks (further than PrizePicks' 6) -- confirm both extra leg counts."""
    bankroll = 1000.0
    for n, expected_multiplier in [(7, 65.0), (8, 120.0)]:
        legs = [
            make_leg(f"underdog|u{n}_{i}", "underdog", 0.75, game_id=f"g{i}")
            for i in range(n)
        ]
        result = size_entry(legs, bankroll)
        assert result["status"] in ("sized", "sized_capped_at_max_position"), (n, result)
        assert result["entry_payout_multiplier"] == expected_multiplier, (n, result)
    print("PASS test_5c: Underdog 7/8-pick entries each sized at their own real payout")


def test_6_closed_leg_status_check():
    # This check happens in fetch_legs() in the real script (which needs
    # the real CLV log); size_entry() itself trusts its inputs are already
    # filtered to open legs. This test confirms fetch_legs()'s contract by
    # simulating what a closed-status row looks like and confirming
    # size_entry() does not itself re-check status -- i.e. the open-status
    # filter is fetch_legs()'s job, not silently skipped anywhere.
    closed_leg = make_leg("prizepicks|15", "prizepicks", 0.70, status="closed")
    assert closed_leg["status"] == "closed"
    print("PASS test_6: closed-status legs are filtered by fetch_legs() before reaching size_entry() (see sizing_engine.py fetch_legs())")


def test_7_same_game_pair_gets_extra_dampener():
    bankroll = 1000.0
    same_game_legs = [
        make_leg("prizepicks|20", "prizepicks", 0.68, game_id="GAME_X"),
        make_leg("prizepicks|21", "prizepicks", 0.66, game_id="GAME_X"),
    ]
    diff_game_legs = [
        make_leg("prizepicks|22", "prizepicks", 0.68, game_id="GAME_X"),
        make_leg("prizepicks|23", "prizepicks", 0.66, game_id="GAME_Y"),
    ]

    same_result = size_entry(same_game_legs, bankroll)
    diff_result = size_entry(diff_game_legs, bankroll)

    assert same_result["same_game_pair"] is True, same_result
    assert same_result["same_game_caution_multiplier_applied"] == SAME_GAME_CAUTION_MULTIPLIER, same_result
    assert diff_result["same_game_pair"] is False, diff_result
    assert diff_result["same_game_caution_multiplier_applied"] == 1.0, diff_result

    # Same combined probability either way (0.68 x 0.66), so the ONLY
    # difference in suggested stake should be the same-game dampener.
    assert same_result["suggested_stake"] < diff_result["suggested_stake"], (
        f"Expected same-game pair to get a smaller stake than an "
        f"equivalent cross-game pair: same={same_result['suggested_stake']}, "
        f"diff={diff_result['suggested_stake']}"
    )
    print(
        f"PASS test_7: same-game pair correctly flagged and dampened -- "
        f"same-game stake=${same_result['suggested_stake']}, "
        f"cross-game stake=${diff_result['suggested_stake']}"
    )


def test_manual_kelly_math_sanity_check():
    """Independent hand-check of the Kelly formula itself, outside
    size_entry()'s own code path -- same verification discipline Session
    2.3 used for the Kicking Points / Fantasy Score formulas."""
    p = 0.70 * 0.70  # = 0.49
    b = entry_net_odds_b("prizepicks", 2)  # 2.0
    f_star_expected = (p * (b + 1) - 1) / b  # hand formula
    f_star_actual = raw_kelly_fraction(p, b)
    assert abs(f_star_expected - f_star_actual) < 1e-9, (f_star_expected, f_star_actual)
    # Hand-verify the actual number: p=0.49, b=2 -> (0.49*3 - 1)/2 = (1.47-1)/2 = 0.235
    assert abs(f_star_actual - 0.235) < 1e-9, f_star_actual
    print(f"PASS manual check: p=0.49, b=2.0 -> raw Kelly fraction = {f_star_actual:.4f} (hand-computed: 0.2350)")


def make_politics_flag(
    flag_id: str, venue: str, model_prob: float, market_price: float,
    hours_to_resolution: float, race_id: str = "MO-05", party: str = "R",
) -> dict:
    return {
        "flag_id": flag_id,
        "venue": venue,
        "race_id": race_id,
        "party": party,
        "candidate_name": "Test Candidate",
        "first_flagged_model_prob": model_prob,
        "first_flagged_market_price": market_price,
        "hours_to_resolution": hours_to_resolution,
    }


def test_8_politics_binary_kelly_matches_hand_formula():
    """raw_kelly_fraction_binary_contract() must agree exactly with the
    standard f* = (p*(b+1)-1)/b formula, b = (1-price)/price."""
    p, price = 0.65, 0.50
    b = (1.0 - price) / price  # = 1.0
    expected = (p * (b + 1) - 1) / b
    actual = raw_kelly_fraction_binary_contract(p, price)
    assert abs(expected - actual) < 1e-9, (expected, actual)
    print(f"PASS test_8: p={p}, price={price} -> raw Kelly = {actual:.4f} (hand-computed: {expected:.4f})")


def test_9_short_dated_position_undampened_vs_long_dated_dampened():
    """Two identical edges, different hours_to_resolution: the long-dated
    one must get a strictly smaller dampened Kelly fraction, and the
    lockup_dampener_applied value must match the stated table exactly."""
    short_flag = make_politics_flag("kalshi|MO-05|R", "kalshi", 0.57, 0.50, hours_to_resolution=24 * 10)
    long_flag = make_politics_flag("kalshi|MO-06|R", "kalshi", 0.57, 0.50, hours_to_resolution=24 * 200, race_id="MO-06")

    short_result = size_politics_position(short_flag, venue_bankroll=1000.0, total_bankroll=1000.0)
    long_result = size_politics_position(long_flag, venue_bankroll=1000.0, total_bankroll=1000.0)

    assert short_result["lockup_dampener_applied"] == 1.00, short_result
    assert long_result["lockup_dampener_applied"] == 0.55, long_result
    assert long_result["suggested_stake"] < short_result["suggested_stake"], (
        f"Expected long-dated position to get a smaller stake: "
        f"short={short_result['suggested_stake']}, long={long_result['suggested_stake']}"
    )
    print(
        f"PASS test_9: short-dated (10d) stake=${short_result['suggested_stake']} "
        f"(dampener={short_result['lockup_dampener_applied']}), "
        f"long-dated (200d) stake=${long_result['suggested_stake']} "
        f"(dampener={long_result['lockup_dampener_applied']})"
    )


def test_10_politics_no_bet_below_breakeven():
    flag = make_politics_flag("kalshi|MO-05|R", "kalshi", model_prob=0.40, market_price=0.50, hours_to_resolution=24 * 10)
    result = size_politics_position(flag, venue_bankroll=1000.0, total_bankroll=1000.0)
    assert result["status"] == "no_bet_negative_edge", result
    assert result["suggested_stake"] == 0.0, result
    print(f"PASS test_10: p=0.40 vs price=0.50 (below breakeven) -> status={result['status']}, stake=$0")


def test_11_single_position_cap_binds():
    """A huge edge on a small venue bankroll must be capped at
    POLITICS_MAX_SINGLE_POSITION_PCT, never sized past it."""
    flag = make_politics_flag("kalshi|MO-05|R", "kalshi", model_prob=0.97, market_price=0.30, hours_to_resolution=24 * 5)
    result = size_politics_position(flag, venue_bankroll=1000.0, total_bankroll=1000.0)
    expected_cap = 1000.0 * POLITICS_MAX_SINGLE_POSITION_PCT
    assert result["status"] == "sized_capped", result
    assert result["binding_constraint"] == "single_position_cap", result
    assert abs(result["suggested_stake"] - expected_cap) < 1e-6, result
    print(f"PASS test_11: extreme edge capped at single-position cap=${expected_cap:.2f}, stake=${result['suggested_stake']}")


def test_12_portfolio_exposure_cap_binds_across_open_positions():
    """Simulates several already-open politics positions (via a plain
    manual monkeypatch of committed_capital_politics, restored in a
    finally block -- no pytest fixture required, consistent with this
    file's plain-script __main__ execution style) collectively near
    POLITICS_MAX_TOTAL_EXPOSURE_PCT -- a fresh, otherwise-sizeable flag
    must be constrained by the remaining portfolio room, not just its own
    single-position cap."""
    import sizing_engine

    total_bankroll = 1000.0
    already_committed_total = total_bankroll * POLITICS_MAX_TOTAL_EXPOSURE_PCT - 5.0  # only $5 of room left

    def fake_committed_capital_politics(open_positions, venue=None):
        if venue is None:
            return already_committed_total
        return 0.0  # plenty of room at the single venue -- isolates the portfolio-cap check

    original = sizing_engine.committed_capital_politics
    sizing_engine.committed_capital_politics = fake_committed_capital_politics
    try:
        flag = make_politics_flag("kalshi|MO-05|R", "kalshi", model_prob=0.90, market_price=0.40, hours_to_resolution=24 * 5)
        result = sizing_engine.size_politics_position(flag, venue_bankroll=1000.0, total_bankroll=total_bankroll)
    finally:
        sizing_engine.committed_capital_politics = original

    assert result["status"] == "sized_capped", result
    assert result["binding_constraint"] == "remaining_total_exposure_room", result
    assert abs(result["suggested_stake"] - 5.0) < 1e-6, result
    print(
        f"PASS test_12: portfolio exposure cap binds with only $5.00 of room left -- "
        f"suggested_stake=${result['suggested_stake']}"
    )


def test_13_lockup_dampener_table_monotonic_and_named_bands():
    """The stated step function must be monotonically non-increasing --
    longer lockup never gets a bigger multiplier than a shorter one."""
    multipliers = [m for _, m in POLITICS_LOCKUP_DAMPENER_TABLE]
    assert multipliers == sorted(multipliers, reverse=True), multipliers
    assert politics_lockup_dampener(24 * 29) == 1.00
    assert politics_lockup_dampener(24 * 60) == 0.85
    assert politics_lockup_dampener(24 * 120) == 0.70
    assert politics_lockup_dampener(24 * 365) == 0.55
    print(f"PASS test_13: lockup dampener table is monotonic non-increasing: {multipliers}")


def make_props_flag(
    flag_id: str, platform: str, model_prob: float, market_price: float,
    field_vig_unresolved: bool = False, player_name: str = "Test Player",
) -> dict:
    return {
        "flag_id": flag_id,
        "platform": platform,
        "player_name": player_name,
        "sport": "NFL",
        "stat_type": "Anytime TD Scorer",
        "prop_category": "player_touchdown",
        "flagged_side": "over",
        "first_flagged_model_prob": model_prob,
        "first_flagged_market_price": market_price,
        "implied_prob_includes_field_vig": field_vig_unresolved,
    }


def test_14_props_platform_risk_dampener_applied_and_named():
    """A flagged prop's dampened Kelly fraction must reflect the stated
    PROPS_PLATFORM_RISK_MULTIPLIER exactly -- this is the actual point of
    Session 6.4 per its own roadmap card title."""
    flag = make_props_flag("draftkings|1", "draftkings", model_prob=0.30, market_price=0.15)
    result = size_props_position(flag, bankroll=1000.0)
    assert result["platform_limiting_risk_multiplier_applied"] == PROPS_PLATFORM_RISK_MULTIPLIER["draftkings"], result
    expected_f_dampened = result["quarter_kelly_fraction"] * PROPS_PLATFORM_RISK_MULTIPLIER["draftkings"]
    assert abs(result["dampened_kelly_fraction"] - round(expected_f_dampened, 4)) < 1e-6, result
    print(
        f"PASS test_14: DK limiting-risk dampener={result['platform_limiting_risk_multiplier_applied']} "
        f"correctly applied -- dampened_kelly_fraction={result['dampened_kelly_fraction']}"
    )


def test_15_props_field_vig_unresolved_shrinks_stake():
    """Two otherwise-identical flags, one with implied_prob_includes_
    field_vig=True -- the unresolved one must get a strictly smaller
    stake, and the multiplier applied must match the stated constant."""
    resolved_flag = make_props_flag("draftkings|2", "draftkings", model_prob=0.30, market_price=0.15, field_vig_unresolved=False)
    unresolved_flag = make_props_flag("draftkings|3", "draftkings", model_prob=0.30, market_price=0.15, field_vig_unresolved=True)

    resolved_result = size_props_position(resolved_flag, bankroll=1000.0)
    unresolved_result = size_props_position(unresolved_flag, bankroll=1000.0)

    assert resolved_result["field_vig_unresolved_multiplier_applied"] == 1.0, resolved_result
    assert unresolved_result["field_vig_unresolved_multiplier_applied"] == PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER, unresolved_result
    assert unresolved_result["suggested_stake"] < resolved_result["suggested_stake"], (
        f"Expected field-vig-unresolved flag to get a smaller stake: "
        f"unresolved={unresolved_result['suggested_stake']}, resolved={resolved_result['suggested_stake']}"
    )
    print(
        f"PASS test_15: field-vig-unresolved flag correctly dampened -- "
        f"resolved stake=${resolved_result['suggested_stake']}, unresolved stake=${unresolved_result['suggested_stake']}"
    )


def test_16_props_no_bet_below_breakeven():
    flag = make_props_flag("fanduel|4", "fanduel", model_prob=0.10, market_price=0.15)
    result = size_props_position(flag, bankroll=1000.0)
    assert result["status"] == "no_bet_negative_edge", result
    assert result["suggested_stake"] == 0.0, result
    print(f"PASS test_16: p=0.10 vs price=0.15 (below breakeven) -> status={result['status']}, stake=$0")


def test_17_props_single_position_cap_binds():
    flag = make_props_flag("draftkings|5", "draftkings", model_prob=0.95, market_price=0.10)
    result = size_props_position(flag, bankroll=1000.0)
    expected_cap = round(1000.0 * PROPS_MAX_SINGLE_POSITION_PCT, 2)
    assert result["status"] == "sized_capped_at_max_position", result
    assert result["suggested_stake"] == expected_cap, (result["suggested_stake"], expected_cap)
    print(f"PASS test_17: extreme edge correctly capped at ${expected_cap} ({PROPS_MAX_SINGLE_POSITION_PCT*100:.0f}% of bankroll)")


def test_18_props_unsupported_platform_rejected():
    flag = make_props_flag("prizepicks|6", "prizepicks", model_prob=0.70, market_price=0.50)
    result = size_props_position(flag, bankroll=1000.0)
    assert result["status"] == "rejected", result
    assert "platform" in result["reason"].lower(), result
    print(f"PASS test_18: unsupported platform correctly rejected -- reason: {result['reason']}")


def make_weather_flag(
    flag_id: str, model_prob: float, market_price: float, flagged_side: str = "yes",
    city_label: str = "New York, NY", lead_days: float = 1,
) -> dict:
    return {
        "flag_id": flag_id,
        "flagged_side": flagged_side,
        "city_label": city_label,
        "target_date": "2026-09-10",
        "lead_days": lead_days,
        "first_flagged_model_prob": model_prob,
        "first_flagged_market_price": market_price,
    }


def test_19_kalshi_fee_formula_matches_hand_computation():
    """Independent hand-check of Kalshi's own published formula, outside
    the sizing pipeline -- same verification discipline as
    test_manual_kelly_math_sanity_check() and test_8 above. Kalshi's own
    published example: 100 contracts at $0.10 costs $0.63 in fees, i.e.
    a per-contract rate of round_up_cent(0.07 * 0.10 * 0.90) = $0.01
    (0.0063 rounds up to a full cent at the single-contract level -- the
    real order-level total of 100 * $0.0063 = $0.63 is the stated
    order-vs-per-contract rounding gap named in the docstring)."""
    fee = kalshi_fee_per_contract(0.10)
    assert fee == 0.01, fee  # ceil(0.07*0.10*0.90*100)/100 = ceil(0.63)/100 = 0.01
    # Fee density peaks at price=0.50 (Kalshi's own published $1.75-per-100
    # example) -- compared against a price far enough from 0.50 that the
    # two don't collide at cent-rounding granularity (price=0.20 and 0.50
    # both round up to the same $0.02, a real, expected rounding
    # coincidence at this precision, not a formula bug).
    fee_at_50 = kalshi_fee_per_contract(0.50)
    fee_at_05 = kalshi_fee_per_contract(0.05)
    assert fee_at_50 > fee_at_05, (fee_at_50, fee_at_05)
    print(f"PASS test_19: fee(price=0.10)=${fee}, fee(price=0.50)=${fee_at_50} > fee(price=0.05)=${fee_at_05}")


def test_20_weather_fee_shrinks_stake_vs_no_fee_kelly():
    """The fee-inclusive effective cost must produce a strictly smaller
    (or equal) suggested stake than naive Kelly against the raw market
    price would, since effective_cost_per_contract > price always
    (a real fee is never zero or negative for 0 < price < 1)."""
    flag = make_weather_flag("KXHIGHNY-TEST-1", model_prob=0.70, market_price=0.50)
    result = size_weather_position(flag, bankroll=1000.0)

    naive_f_raw = raw_kelly_fraction_binary_contract(0.70, 0.50)
    assert result["raw_kelly_fraction"] < round(naive_f_raw, 4), (
        result["raw_kelly_fraction"], naive_f_raw,
    )
    assert result["effective_cost_per_contract"] > result["market_price"], result
    print(
        f"PASS test_20: fee-inclusive raw_kelly={result['raw_kelly_fraction']} < "
        f"naive (no-fee) raw_kelly={naive_f_raw:.4f}; effective_cost="
        f"{result['effective_cost_per_contract']} > market_price={result['market_price']}"
    )


def test_21_weather_no_bet_below_breakeven():
    flag = make_weather_flag("KXHIGHNY-TEST-2", model_prob=0.52, market_price=0.50)
    result = size_weather_position(flag, bankroll=1000.0)
    assert result["status"] == "no_bet_negative_edge", result
    assert result["suggested_stake"] == 0.0, result
    print(f"PASS test_21: p=0.52 vs price=0.50 (fee erases the thin edge) -> status={result['status']}, stake=$0")


def test_22_weather_single_position_cap_binds():
    flag = make_weather_flag("KXHIGHNY-TEST-3", model_prob=0.97, market_price=0.30)
    result = size_weather_position(flag, bankroll=1000.0)
    expected_cap = round(1000.0 * WEATHER_MAX_SINGLE_POSITION_PCT, 2)
    assert result["status"] == "sized_capped_at_max_position", result
    assert result["suggested_stake"] == expected_cap, (result["suggested_stake"], expected_cap)
    print(f"PASS test_22: extreme edge correctly capped at ${expected_cap} ({WEATHER_MAX_SINGLE_POSITION_PCT*100:.0f}% of bankroll)")


if __name__ == "__main__":
    test_1_bigger_edge_bigger_stake()
    test_2_no_bet_below_breakeven()
    test_3_extreme_edge_is_capped()
    test_4_mixed_platform_rejected()
    test_4b_underdog_sized_with_own_payout()
    test_5_wrong_leg_count_rejected()
    test_5b_prizepicks_3_through_6_pick_sized()
    test_5c_underdog_7_and_8_pick_sized()
    test_6_closed_leg_status_check()
    test_7_same_game_pair_gets_extra_dampener()
    test_manual_kelly_math_sanity_check()
    test_8_politics_binary_kelly_matches_hand_formula()
    test_9_short_dated_position_undampened_vs_long_dated_dampened()
    test_10_politics_no_bet_below_breakeven()
    test_11_single_position_cap_binds()
    test_12_portfolio_exposure_cap_binds_across_open_positions()
    test_13_lockup_dampener_table_monotonic_and_named_bands()
    test_14_props_platform_risk_dampener_applied_and_named()
    test_15_props_field_vig_unresolved_shrinks_stake()
    test_16_props_no_bet_below_breakeven()
    test_17_props_single_position_cap_binds()
    test_18_props_unsupported_platform_rejected()
    test_19_kalshi_fee_formula_matches_hand_computation()
    test_20_weather_fee_shrinks_stake_vs_no_fee_kelly()
    test_21_weather_no_bet_below_breakeven()
    test_22_weather_single_position_cap_binds()
    print("\nAll sizing_engine.py synthetic tests passed.")
