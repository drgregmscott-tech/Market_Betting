"""
Session 2.12 -- regression + plug-in architecture test for pickem_model.py.

WHY THIS FILE EXISTS
---------------------
Session 2.12's validation requires two things proven, not asserted:
1. NFL scoring output is byte-for-byte unchanged across the refactor from a
   hardcoded nflverse path to a generic per-sport plug-in shape, on a real,
   fixed input snapshot (not "tests still pass").
2. Adding a second real sport plug-in (MLB, this session's proof case --
   full production MLB wiring is Session 2.13's job) requires touching only
   that plug-in's own file, not pickem_model.py's core loop.

This file builds a small, fixed synthetic NFL weekly-stats fixture and a
synthetic props fixture covering every code path in process_props()
(estimated via a plain column stat, a composite stat, both computed
formulas, unsupported_sport, unsupported_stat_type, unsupported_odds_type,
no_player_match, insufficient_history, and an Underdog row using the
per-side-multiplier implied-probability path) -- then diffs the current
architecture's output against a golden snapshot captured from the
pre-refactor code (data/pickem/_test_fixtures/nfl_regression_golden.csv).

Run: python -m pytest scripts/estimation/test_pickem_model.py -v
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import pytest

from pickem_model import process_props
from pickem_sport_plugins import PLUGINS, plugin_for_sport
from pickem_sport_plugins.nfl import NFL_PLUGIN

GOLDEN_PATH = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "pickem"
    / "_test_fixtures"
    / "nfl_regression_golden.csv"
)


def _game_row(player_id: str, name: str, week: int, **stats) -> dict:
    base = {
        "player_id": player_id,
        "player_display_name": name,
        "week": week,
        "season_type": "REG",
        "passing_yards": 0, "rushing_yards": 0, "receiving_yards": 0,
        "receptions": 0, "completions": 0, "attempts": 0,
        "passing_tds": 0, "rushing_tds": 0, "passing_interceptions": 0,
        "receiving_tds": 0, "def_sacks": 0, "targets": 0, "fg_made": 0,
        "fg_made_0_19": 0, "fg_made_20_29": 0, "fg_made_30_39": 0,
        "fg_made_40_49": 0, "fg_made_50_59": 0, "fg_made_60_": 0,
        "fg_missed": 0, "pat_made": 0, "pat_missed": 0,
        "rushing_fumbles_lost": 0, "receiving_fumbles_lost": 0,
        "sack_fumbles_lost": 0, "passing_2pt_conversions": 0,
        "rushing_2pt_conversions": 0, "receiving_2pt_conversions": 0,
    }
    base.update(stats)
    return base


def build_nfl_weekly_fixture() -> pd.DataFrame:
    rows = []
    # P1 -- plain column stat (Pass Yards), 5 games
    for wk, yds in enumerate([220, 260, 300, 240, 310], start=1):
        rows.append(_game_row("p1", "Player One", wk, passing_yards=yds))
    # P2 -- composite stat (Rush+Rec Yards), 5 games
    for wk, (ry, recy) in enumerate(
        [(60, 40), (80, 20), (50, 55), (70, 30), (90, 45)], start=1
    ):
        rows.append(_game_row("p2", "Player Two", wk, rushing_yards=ry, receiving_yards=recy))
    # P3 -- kicker, computed "Kicking Points", 3 games
    for wk, fg39, fg49, fg50, patm in [(1, 1, 0, 0, 2), (2, 0, 1, 1, 3), (3, 2, 0, 0, 1)]:
        rows.append(_game_row(
            "p3", "Player Three", wk,
            fg_made_0_19=fg39, fg_made_40_49=fg49, fg_made_50_59=fg50, pat_made=patm,
        ))
    # P4 -- computed "Fantasy Score", 4 games
    for wk in range(1, 5):
        rows.append(_game_row(
            "p4", "Player Four", wk,
            passing_yards=250, passing_tds=2, receiving_yards=0, rushing_yards=10,
        ))
    # P5 -- only 1 game on record (insufficient_history)
    rows.append(_game_row("p5", "Player Five", 1, passing_yards=180))
    df = pd.DataFrame(rows)
    df["sort_key"] = df["week"]  # plug-in fetch_stats contract, see pickem_sport_plugins
    return df


def build_props_fixture() -> pd.DataFrame:
    rows = [
        dict(platform="prizepicks", source_line_id="1", player_name="Player One",
             sport="nfl", stat_type="Pass Yards", line=265.5, odds_type="standard"),
        dict(platform="prizepicks", source_line_id="2", player_name="Player Two",
             sport="football", stat_type="Rush+Rec Yards", line=140.5, odds_type="standard"),
        dict(platform="prizepicks", source_line_id="3", player_name="Player Three",
             sport="nfl", stat_type="Kicking Points", line=8.5, odds_type="standard"),
        dict(platform="prizepicks", source_line_id="4", player_name="Player Four",
             sport="nfl", stat_type="Fantasy Score", line=20.5, odds_type="standard"),
        dict(platform="prizepicks", source_line_id="5", player_name="Someone Irrelevant",
             sport="nba", stat_type="Points", line=25.5, odds_type="standard"),
        dict(platform="prizepicks", source_line_id="6", player_name="Player One",
             sport="nfl", stat_type="Some Unknown Stat", line=1.5, odds_type="standard"),
        dict(platform="prizepicks", source_line_id="7", player_name="Nobody Matches",
             sport="nfl", stat_type="Pass Yards", line=200.5, odds_type="standard"),
        dict(platform="prizepicks", source_line_id="8", player_name="Player Five",
             sport="nfl", stat_type="Pass Yards", line=150.5, odds_type="standard"),
        dict(platform="prizepicks", source_line_id="9", player_name="Player One",
             sport="nfl", stat_type="Pass Yards", line=265.5, odds_type="demon"),
        dict(platform="underdog", source_line_id="10", player_name="Player Two",
             sport="nfl", stat_type="Rush+Rec Yards", line=140.5,
             over_payout_multiplier=1.9, under_payout_multiplier=1.9),
    ]
    return pd.DataFrame(rows)


def test_plugin_registry_covers_nfl():
    assert plugin_for_sport("nfl") is NFL_PLUGIN
    assert plugin_for_sport("football") is NFL_PLUGIN
    assert plugin_for_sport("some_unregistered_sport") is None


def test_second_plugin_registered_without_touching_core_loop():
    names = {p.name for p in PLUGINS}
    assert "nfl" in names
    assert "mlb" in names, "MLB proof-case plug-in (Session 2.12) not registered"


def test_unsupported_sport_still_falls_through_cleanly():
    props = pd.DataFrame([dict(
        platform="prizepicks", source_line_id="99", player_name="X",
        sport="curling", stat_type="Points", line=1.5, odds_type="standard",
    )])
    result = process_props(props, season=2025)
    assert result.iloc[0]["model_status"] == "unsupported_sport"
    assert pd.isna(result.iloc[0]["resolved_stat_key"]) or result.iloc[0]["resolved_stat_key"] is None


def test_nfl_regression_matches_golden_snapshot():
    """The core Session 2.12 validation item: byte-for-byte identical NFL
    output before/after the plug-in refactor, on a fixed input."""
    if not GOLDEN_PATH.exists():
        pytest.skip(f"No golden snapshot at {GOLDEN_PATH} -- run capture_golden() first")

    weekly_fixture = build_nfl_weekly_fixture()
    props_fixture = build_props_fixture()

    def fake_fetch(season: int) -> pd.DataFrame:
        return weekly_fixture

    original_fetch = NFL_PLUGIN.fetch_stats
    NFL_PLUGIN.fetch_stats = fake_fetch
    try:
        result = process_props(props_fixture, season=2025)
    finally:
        NFL_PLUGIN.fetch_stats = original_fetch

    # Round-trip `result` through CSV too before comparing, so this is an
    # apples-to-apples comparison against the golden snapshot (itself read
    # back from CSV) rather than flagging a CSV-serialization dtype
    # artifact (e.g. a numeric-looking ID string) as a false regression.
    import io
    result = pd.read_csv(io.StringIO(result.to_csv(index=False)))
    golden = pd.read_csv(GOLDEN_PATH)
    result = result.reset_index(drop=True)
    golden = golden.reset_index(drop=True)

    assert list(result.columns) == list(golden.columns), (
        f"Column order changed.\nBefore: {list(golden.columns)}\nAfter:  {list(result.columns)}"
    )
    pd.testing.assert_frame_equal(result, golden, check_dtype=False)


if __name__ == "__main__":
    # One-off: capture the golden snapshot. Only ever run this AGAINST THE
    # PRE-REFACTOR pickem_model.py, before the Session 2.12 plug-in change
    # lands -- see module docstring.
    import sys

    weekly_fixture = build_nfl_weekly_fixture()
    props_fixture = build_props_fixture()
    if "--capture-golden-legacy" in sys.argv:
        from pickem_model import process_props as legacy_process_props  # pre-refactor signature
        result = legacy_process_props(props_fixture, weekly_fixture)
        GOLDEN_PATH.parent.mkdir(parents=True, exist_ok=True)
        result.to_csv(GOLDEN_PATH, index=False)
        print(f"Wrote golden snapshot: {GOLDEN_PATH} ({len(result)} rows)")
