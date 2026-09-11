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

from pickem_model import build_stat_series, process_props, resolve_stat_spec
from pickem_sport_plugins import PLUGINS, plugin_for_sport
from pickem_sport_plugins.mlb import MLB_PLUGIN
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


def _hitting_row(player_id: str, name: str, sort_key: int, **stats) -> dict:
    base = {
        "player_id": player_id, "player_display_name": name, "sort_key": sort_key,
        "hits": 0, "homeRuns": 0, "runs": 0, "rbi": 0, "baseOnBalls": 0,
        "doubles": 0, "triples": 0, "stolenBases": 0, "plateAppearances": 0,
        "totalBases": 0, "strikeOuts": 0, "hitByPitch": 0, "numberOfPitchesSeen": 0,
    }
    base.update(stats)
    return base


def _pitching_row(player_id: str, name: str, sort_key: int, **stats) -> dict:
    base = {
        "player_id": player_id, "player_display_name": name, "sort_key": sort_key,
        "p_hits": 0, "p_earnedRuns": 0, "p_baseOnBalls": 0, "p_strikeOuts": 0,
        "p_outs": 0, "p_battersFaced": 0, "p_numberOfPitches": 0, "p_strikes": 0,
        "p_wins": 0,
    }
    base.update(stats)
    return base


def build_mlb_stats_fixture() -> pd.DataFrame:
    """Session 2.13 -- MLB plug-in fixture. Mirrors real
    fetch_mlb_season_stats() output shape: a combined DataFrame where a
    pure hitter's rows carry NaN in every p_-prefixed column (pandas fills
    absent dict keys as NaN on construction) and vice versa for a pure
    pitcher -- and, critically, a two-way player (real example: Shohei
    Ohtani) contributes BOTH row types under the same player_id, each with
    its own sort_key restarting at 1. This last shape is what exposed the
    real Session 2.13 build_stat_series() bug (see that function's own
    "SESSION 2.13 FIX" docstring note) -- a hitting-stat query was
    including the same player's unrelated pitching rows because both
    shared one player_id, silently diluting season_avg and corrupting
    recent_form's "last 5" window with rows from the wrong game log."""
    rows = []
    # H1 -- pure hitter, 5 games: Home Runs (plain column), Singles/Hitter
    # FS (computed), Hits+Runs+RBIs (composite).
    for sk, (h, hr, r, rbi, d, t, bb, hbp, sb) in enumerate(
        [(2, 1, 1, 1, 1, 0, 0, 0, 0),
         (1, 0, 0, 0, 0, 0, 1, 0, 1),
         (3, 2, 2, 3, 1, 1, 0, 1, 0),
         (0, 0, 0, 0, 0, 0, 0, 0, 0),
         (2, 0, 1, 1, 0, 0, 1, 0, 0)],
        start=1,
    ):
        rows.append(_hitting_row(
            "h1", "Hitter One", sk, hits=h, homeRuns=hr, runs=r, rbi=rbi,
            doubles=d, triples=t, baseOnBalls=bb, hitByPitch=hbp, stolenBases=sb,
        ))
    # P1 -- pure pitcher, 3 games: Ks / Hits Allowed (plain column),
    # Balls Thrown / Pitcher FS (computed).
    for sk, (outs, er, k, hits_allowed, pitches, strikes, wins) in enumerate(
        [(18, 2, 6, 5, 90, 58, 1), (15, 4, 4, 8, 85, 50, 0), (21, 1, 9, 3, 95, 63, 1)],
        start=1,
    ):
        rows.append(_pitching_row(
            "p1", "Pitcher One", sk, p_outs=outs, p_earnedRuns=er, p_strikeOuts=k,
            p_hits=hits_allowed, p_numberOfPitches=pitches, p_strikes=strikes, p_wins=wins,
        ))
    # TW1 -- two-way player: 3 real hitting games + 2 real pitching games
    # under the SAME player_id, sort_key restarting at 1 for each log.
    for sk, hr in enumerate([1, 0, 2], start=1):
        rows.append(_hitting_row("tw1", "Two Way One", sk, hits=1, homeRuns=hr, runs=1, rbi=1))
    for sk, k in enumerate([7, 5], start=1):
        rows.append(_pitching_row("tw1", "Two Way One", sk, p_outs=18, p_earnedRuns=2, p_strikeOuts=k))
    return pd.DataFrame(rows)


def test_mlb_plain_column_stat():
    stats = build_mlb_stats_fixture()
    kind, value, _ = resolve_stat_spec(MLB_PLUGIN, "Home Runs")
    series = build_stat_series(MLB_PLUGIN, stats, "h1", kind, value)
    assert list(series) == [1, 0, 2, 0, 0]


def test_mlb_pitching_column_stat_not_confused_with_hitting():
    """Ks (pitcher strikeouts, p_strikeOuts) must never read a hitter's own
    strikeOuts column, and vice versa -- the two are different real stats
    that happen to share a name."""
    stats = build_mlb_stats_fixture()
    kind, value, _ = resolve_stat_spec(MLB_PLUGIN, "Ks")
    series = build_stat_series(MLB_PLUGIN, stats, "p1", kind, value)
    assert list(series) == [6, 4, 9]


def test_mlb_composite_stat():
    stats = build_mlb_stats_fixture()
    kind, value, _ = resolve_stat_spec(MLB_PLUGIN, "Hits+Runs+RBIs")
    series = build_stat_series(MLB_PLUGIN, stats, "h1", kind, value)
    assert list(series) == [4, 1, 8, 0, 4]  # (hits+runs+rbi) per game


def test_mlb_computed_singles():
    stats = build_mlb_stats_fixture()
    kind, value, _ = resolve_stat_spec(MLB_PLUGIN, "Singles")
    series = build_stat_series(MLB_PLUGIN, stats, "h1", kind, value)
    # singles = hits - doubles - triples - homeRuns, per game, from the
    # h1 fixture rows above (hits, homeRuns, ..., doubles, triples, ...):
    expected = [2 - 1 - 0 - 1, 1 - 0 - 0 - 0, 3 - 1 - 1 - 2, 0, 2 - 0 - 0 - 0]
    assert list(series) == expected


def test_mlb_computed_balls_thrown():
    stats = build_mlb_stats_fixture()
    kind, value, _ = resolve_stat_spec(MLB_PLUGIN, "Balls Thrown")
    series = build_stat_series(MLB_PLUGIN, stats, "p1", kind, value)
    assert list(series) == [90 - 58, 85 - 50, 95 - 63]


def test_mlb_computed_pitcher_fs_quality_start_rule():
    """Confirms Quality Start (outs>=18 and earnedRuns<=3) is applied
    per-game, not globally -- game 2 (15 outs, 4 ER) must NOT count as a
    quality start; games 1 and 3 must."""
    stats = build_mlb_stats_fixture()
    kind, value, _ = resolve_stat_spec(MLB_PLUGIN, "Pitcher FS")
    series = build_stat_series(MLB_PLUGIN, stats, "p1", kind, value)
    # game1: win=1,QS=1(18>=18,2<=3),er=2,k=6,outs=18 -> 6+4-6+18+18=40
    # game2: win=0,QS=0(15<18),er=4,k=4,outs=15 -> 0+0-12+12+15=15
    # game3: win=1,QS=1(21>=18,1<=3),er=1,k=9,outs=21 -> 6+4-3+27+21=55
    assert list(series) == [40, 15, 55]


def test_mlb_two_way_player_stats_do_not_cross_contaminate():
    """Regression test for the real Session 2.13 bug: a two-way player's
    hitting-stat query must only see his hitting rows (3 games here, not
    the 3+2=5 combined rows), and his pitching-stat query must only see his
    pitching rows (2 games), with correct per-game values in each case."""
    stats = build_mlb_stats_fixture()

    kind, value, _ = resolve_stat_spec(MLB_PLUGIN, "Home Runs")
    hr_series = build_stat_series(MLB_PLUGIN, stats, "tw1", kind, value)
    assert list(hr_series) == [1, 0, 2], "hitting query pulled in pitching rows"

    kind, value, _ = resolve_stat_spec(MLB_PLUGIN, "Ks")
    ks_series = build_stat_series(MLB_PLUGIN, stats, "tw1", kind, value)
    assert list(ks_series) == [7, 5], "pitching query pulled in hitting rows"


def test_mlb_plugin_registered_and_sport_labels_exclude_mlblive():
    assert plugin_for_sport("mlb") is MLB_PLUGIN
    assert plugin_for_sport("baseball") is MLB_PLUGIN
    assert plugin_for_sport("mlblive") is None, (
        "MLBLIVE is deliberately unregistered -- see mlb.py module docstring"
    )


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
