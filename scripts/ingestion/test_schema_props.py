"""
Session 6.4 -- synthetic-fixture tests for schema_props.py's field-vig
normalization helpers (same-precedent test file every other project script
already has).

Run: python test_schema_props.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from schema_props import (
    american_odds_to_implied_probability,
    normalize_field_vig,
    same_market_group_key,
)


def test_normalize_field_vig_sums_to_one():
    # Three real-shaped prices, each with its own vig baked in -- summed
    # raw they are well over 1.0 (the field vig).
    raw = [
        american_odds_to_implied_probability(-114),
        american_odds_to_implied_probability(+650),
        american_odds_to_implied_probability(+900),
    ]
    normalized = normalize_field_vig(raw)
    assert abs(sum(normalized) - 1.0) < 1e-9
    # Order/relative ranking must be preserved -- the shortest (most
    # favored) real price stays the largest normalized share.
    assert normalized[0] > normalized[1] > normalized[2]
    print("PASS: test_normalize_field_vig_sums_to_one")


def test_normalize_field_vig_empty_list_returns_empty():
    assert normalize_field_vig([]) == []
    print("PASS: test_normalize_field_vig_empty_list_returns_empty")


def test_normalize_field_vig_zero_total_returns_input_unchanged():
    # Defensive case -- should never happen with real American-odds
    # probabilities (always > 0), but must never divide by zero.
    assert normalize_field_vig([0.0, 0.0]) == [0.0, 0.0]
    print("PASS: test_normalize_field_vig_zero_total_returns_input_unchanged")


def test_same_market_group_key_is_stable_and_distinct():
    key_a = same_market_group_key("draftkings", "12345", "999")
    key_b = same_market_group_key("draftkings", "12345", "999")
    key_c = same_market_group_key("draftkings", "12345", "888")  # different market
    assert key_a == key_b
    assert key_a != key_c
    print("PASS: test_same_market_group_key_is_stable_and_distinct")


if __name__ == "__main__":
    test_normalize_field_vig_sums_to_one()
    test_normalize_field_vig_empty_list_returns_empty()
    test_normalize_field_vig_zero_total_returns_input_unchanged()
    test_same_market_group_key_is_stable_and_distinct()
    print("\nAll tests passed.")
