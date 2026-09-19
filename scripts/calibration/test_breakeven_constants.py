"""Keeps the dashboard breakeven constants equal to the sizing table.

The same reference breakeven is written in three places (outcome_tracker.py,
weekly_review.py, frontend/app.js). If a payout in sizing_engine.py changes
and these are not updated, the dashboards silently compare against a stale
number (this happened once: 0.5774 from a 2-pick 3x payout that does not
exist). Run with pytest.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "calibration"))
sys.path.insert(0, str(ROOT / "scripts" / "sizing"))

import outcome_tracker  # noqa: E402
import weekly_review  # noqa: E402
from sizing_engine import breakeven_win_rate_per_leg  # noqa: E402

REFERENCE_ENTRY_LEGS = 5  # see docs/sample_size_methodology.md


def test_python_constants_match_sizing_table():
    expected = round(breakeven_win_rate_per_leg("prizepicks", REFERENCE_ENTRY_LEGS), 4)
    assert outcome_tracker.BREAKEVEN_WIN_RATE == expected
    assert weekly_review.BREAKEVEN_WIN_RATE == expected


def test_frontend_constant_matches_sizing_table():
    expected = round(breakeven_win_rate_per_leg("prizepicks", REFERENCE_ENTRY_LEGS), 4)
    js = (ROOT / "frontend" / "app.js").read_text(encoding="utf-8")
    match = re.search(r"const BREAKEVEN_WIN_RATE = ([0-9.]+);", js)
    assert match is not None
    assert float(match.group(1)) == expected


def _js_payout_table(platform: str) -> dict:
    js = (ROOT / "frontend" / "app.js").read_text(encoding="utf-8")
    block = re.search(r"const PICKEM_ENTRY_PAYOUT = \{(.*?)\n\};", js, re.S).group(1)
    line = re.search(platform + r": \{([^}]*)\}", block).group(1)
    return {int(k): float(v) for k, v in re.findall(r"(\d+):\s*([0-9.]+)", line)}


def test_frontend_payout_tables_match_the_sizing_engine():
    """Until Session 2.61 the frontend still sized PrizePicks entries at
    3/6/10/20/37.5x after the Python table moved to 2/4.75/9/19/36.5x."""
    from sizing_engine import PICKEM_ENTRY_PAYOUT
    for platform in ("prizepicks", "underdog"):
        assert _js_payout_table(platform) == PICKEM_ENTRY_PAYOUT[platform], platform


def test_frontend_flag_threshold_matches_the_logger():
    import clv_logger
    js = (ROOT / "frontend" / "app.js").read_text(encoding="utf-8")
    match = re.search(r"const FLAG_EDGE_THRESHOLD = ([0-9.]+);", js)
    assert float(match.group(1)) == clv_logger.FLAG_EDGE_THRESHOLD_PICKEM


def test_frontend_props_dampener_text_matches_the_sizing_engine():
    """Session 6.13: the props badges in app.js quote the sizing constants in
    their tooltips. If sizing_engine.py changes a value, this fails."""
    from sizing_engine import PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER, PROPS_PLATFORM_RISK_MULTIPLIER
    js = (ROOT / "frontend" / "app.js").read_text(encoding="utf-8")
    risk = re.search(r"PROPS_PLATFORM_RISK_MULTIPLIER = ([0-9.]+)", js)
    field = re.search(r"PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER \(([0-9.]+)\)", js)
    assert risk is not None and field is not None
    assert set(PROPS_PLATFORM_RISK_MULTIPLIER.values()) == {float(risk.group(1))}
    assert float(field.group(1)) == PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER
