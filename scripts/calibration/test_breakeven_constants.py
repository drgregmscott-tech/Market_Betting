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
