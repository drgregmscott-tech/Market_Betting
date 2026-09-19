"""Tests for the Session 2.62 breakeven correction in pickem_model_validity_audit.py.
Run with pytest."""

import math
import sys
from pathlib import Path

import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
import pickem_model_validity_audit as audit  # noqa: E402


def _frame(rows):
    return pd.DataFrame(rows, columns=["platform", "odds_bucket", "breakeven"])


def test_prizepicks_standard_uses_the_reference_entry_not_the_logged_half():
    df = audit.apply_breakeven_reference(_frame([("prizepicks", "standard", 0.5)]))
    assert df["breakeven"].iloc[0] == pytest.approx(19 ** (-1 / 5))
    assert df["breakeven_logged"].iloc[0] == 0.5


def test_prizepicks_demon_and_goblin_have_no_breakeven():
    df = audit.apply_breakeven_reference(_frame([
        ("prizepicks", "demon", 0.472), ("prizepicks", "goblin", 0.305)]))
    assert df["breakeven"].isna().all()
    assert list(df["breakeven_logged"]) == [0.472, 0.305]


def test_underdog_keeps_its_logged_breakeven():
    df = audit.apply_breakeven_reference(_frame([("underdog", "underdog", 0.44)]))
    assert df["breakeven"].iloc[0] == 0.44


def _graded(n, wins, breakeven):
    return pd.DataFrame({
        "result": ["win"] * wins + ["loss"] * (n - wins),
        "breakeven": breakeven,
        "game_id": [f"g{i % 20}" for i in range(n)],
    })


def test_cell_with_no_breakeven_is_labeled_no_valid_breakeven_not_scored():
    stats = audit.cell_stats(_graded(200, 120, math.nan))
    assert stats["verdict"] == "no_valid_breakeven"


def test_small_cell_is_still_not_enough_evidence_first():
    assert audit.cell_stats(_graded(10, 6, math.nan))["verdict"] == "not_enough_evidence"


def test_same_win_rate_flips_from_beats_to_below_when_the_breakeven_is_corrected():
    win_rate_legs, wins = 400, 216  # 54% won
    old = audit.cell_stats(_graded(win_rate_legs, wins, 0.5))
    new = audit.cell_stats(_graded(win_rate_legs, wins, audit.PRIZEPICKS_STANDARD_BREAKEVEN))
    assert old["verdict"] == "beats_breakeven"
    assert new["verdict"] in ("inconclusive", "below_breakeven")
