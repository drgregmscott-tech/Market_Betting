"""Tests for the Session 6.12 props validity audit (run with pytest)."""

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import props_model_validity_audit as audit  # noqa: E402


def _clv(n, platform="draftkings", odds=300, prob=0.3, price=0.05, games=10):
    return pd.DataFrame({
        "flag_id": [f"{platform}{i}" for i in range(n)], "status": "closed", "platform": platform,
        "stat_type": "Anytime TD Scorer", "game_id": [f"g{i % games}" for i in range(n)],
        "over_american_odds": odds, "first_flagged_model_prob": prob, "first_flagged_market_price": price,
        "implied_prob_includes_field_vig": False,
    })


def _outcomes(clv, wins):
    res = ["win" if i < wins else "loss" for i in range(len(clv))]
    return pd.DataFrame({"flag_id": clv["flag_id"], "result": res})


def test_american_odds_to_breakeven():
    assert audit.american_to_implied(300) == 0.25
    assert abs(audit.american_to_implied(-200) - 2 / 3) < 1e-9
    assert audit.american_to_implied(None) is None


def test_profit_uses_the_quoted_payout():
    clv = _clv(4)  # +300 pays 3 units on a win
    df = audit.load_joined(clv, _outcomes(clv, 1), {})
    assert sorted(df["profit"]) == [-1.0, -1.0, -1.0, 3.0]


def test_break_even_win_rate_gives_no_verdict_of_edge():
    clv = _clv(200, games=40)
    df = audit.load_joined(clv, _outcomes(clv, 50), {})  # 25% at +300 = exactly breakeven
    row = audit.cell_stats(df)
    assert abs(row["roi"]) < 1e-9 and row["verdict"] == "inconclusive"
    assert row["worth_building_on"] is False


def test_clear_edge_and_clear_loss_verdicts():
    assert audit.verdict(0.05, 0.4, 100, 30) == "beats"
    assert audit.verdict(-0.4, -0.05, 100, 30) == "below"
    assert audit.verdict(0.05, 0.4, 29, 30) == "insufficient"
    assert audit.verdict(0.05, 0.4, 100, 7) == "insufficient"


def test_ungraded_flags_are_counted_as_losses_in_the_sensitivity():
    clv = _clv(200, games=40)
    outc = _outcomes(clv, 100)  # 50% win at +300: big edge
    outc = outc.iloc[:120]      # 80 flags left ungraded
    df = audit.load_joined(clv, outc, {})
    row = audit.cell_stats(df)
    assert row["ungraded"] == 80 and row["legs"] == 120


def test_missing_odds_fall_back_to_snapshot_then_drop_from_profit():
    clv = _clv(3)
    clv.loc[0, "over_american_odds"] = np.nan
    clv.loc[1, "over_american_odds"] = np.nan
    df = audit.load_joined(clv, _outcomes(clv, 3), {"draftkings1": 300.0})
    by_id = df.set_index("flag_id")
    assert by_id.loc["draftkings1", "quoted_breakeven"] == 0.25
    assert np.isnan(by_id.loc["draftkings0", "profit"])


def test_calibration_bands_and_field_vig_counts():
    clv = _clv(60, prob=0.3, games=12)
    df = audit.load_joined(clv, _outcomes(clv, 15), {})
    bands = audit.calibration_bands(df)
    assert list(bands["band"]) == ["25-35%"] and bands.iloc[0]["legs"] == 60
    assert audit.field_vig_counts(df)["flags"].sum() == 60
