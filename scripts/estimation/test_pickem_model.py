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
from unittest import mock

import pandas as pd
import pytest
import requests

from pickem_model import (
    MLB_STARTER_STATUS_CONFIRMED,
    MLB_STARTER_STATUS_DIFFERENT,
    MLB_STARTER_STATUS_NOT_YET_CONFIRMED,
    build_stat_series,
    compute_mlb_starter_status,
    process_props,
    resolve_stat_spec,
)
from pickem_sport_plugins import PLUGINS, plugin_for_sport
from pickem_sport_plugins.cfb import CFB_PLUGIN, _flatten_game_players
from pickem_sport_plugins.epl import EPL_PLUGIN, _fetch_player_history
from pickem_sport_plugins.mlb import (
    MLB_PLUGIN,
    _fetch_active_roster,
    _fetch_player_game_log,
    fetch_confirmed_lineup,
    fetch_probable_pitchers,
    fetch_schedule_games,
    find_scheduled_game,
)
from pickem_sport_plugins.nfl import NFL_PLUGIN
from pickem_sport_plugins.soccer import SOCCER_PLUGIN, _fetch_event_player_rows

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
        # HOTFIX (2026-09-12): this row's job is to be some genuinely
        # UNREGISTERED sport, so it must always fall through to
        # model_status="unsupported_sport" without touching the network.
        # It used "nba" originally (Session 2.12), which was true until a
        # real NBA plug-in was registered (Session 2.15) -- at that point
        # this row silently started dispatching to the real NBA plug-in
        # and making live ESPN network calls inside what is supposed to be
        # a fast, fully offline regression test (discovered when this test
        # started taking ~9 minutes instead of under a second). "curling"
        # is not a registered sport anywhere in this project and is the
        # same placeholder test_unsupported_sport_still_falls_through_
        # cleanly() already uses below.
        dict(platform="prizepicks", source_line_id="5", player_name="Someone Irrelevant",
             sport="curling", stat_type="Points", line=25.5, odds_type="standard"),
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


# ---------------------------------------------------------------------------
# Session 2.14 -- Soccer (EPL via the FPL plug-in, everything else via the
# ESPN plug-in). Offline fixtures shaped like each plug-in's real
# fetch_stats() output -- no live network calls in this file (the real,
# live end-to-end proof is in SESSION_LOG.md's Session 2.14 section, per
# this project's standing "prove it against real data separately, keep unit
# tests offline" pattern already used for NFL/MLB).
# ---------------------------------------------------------------------------
def _epl_row(player_id: str, name: str, sort_key: int, **stats) -> dict:
    base = {
        "player_id": player_id, "player_display_name": name, "sort_key": sort_key,
        "goals_scored": 0, "assists": 0, "tackles": 0, "saves": 0, "goals_conceded": 0,
    }
    base.update(stats)
    return base


def build_epl_stats_fixture() -> pd.DataFrame:
    rows = []
    # E1 -- attacker: Goals (plain column), Goal + Assist (composite), 4 gws.
    for sk, (g, a) in enumerate([(1, 0), (0, 1), (2, 1), (0, 0)], start=1):
        rows.append(_epl_row("e1", "Attacker One", sk, goals_scored=g, assists=a))
    # E2 -- goalkeeper: Goalie Saves, Goals Allowed, 3 gws.
    for sk, (sv, gc) in enumerate([(3, 1), (5, 0), (2, 2)], start=1):
        rows.append(_epl_row("e2", "Keeper Two", sk, saves=sv, goals_conceded=gc))
    return pd.DataFrame(rows)


def test_epl_plugin_registered_sport_label():
    assert plugin_for_sport("epl") is EPL_PLUGIN


def test_epl_plain_column_and_composite_stats():
    stats = build_epl_stats_fixture()
    kind, value, _ = resolve_stat_spec(EPL_PLUGIN, "Goals")
    assert list(build_stat_series(EPL_PLUGIN, stats, "e1", kind, value)) == [1, 0, 2, 0]

    kind, value, _ = resolve_stat_spec(EPL_PLUGIN, "Goal + Assist")
    assert list(build_stat_series(EPL_PLUGIN, stats, "e1", kind, value)) == [1, 1, 3, 0]


def test_epl_goalie_stats():
    stats = build_epl_stats_fixture()
    kind, value, _ = resolve_stat_spec(EPL_PLUGIN, "Goalie Saves")
    assert list(build_stat_series(EPL_PLUGIN, stats, "e2", kind, value)) == [3, 5, 2]

    kind, value, _ = resolve_stat_spec(EPL_PLUGIN, "Goals Allowed")
    assert list(build_stat_series(EPL_PLUGIN, stats, "e2", kind, value)) == [1, 0, 2]


def test_epl_shots_and_fantasy_score_stay_unsupported():
    """A real, substantial stated gap (see epl.py docstring) -- FPL's real
    per-gameweek data has no shot/foul counts and can't source PrizePicks'
    real outfield Fantasy Score formula. Must resolve to None, not a
    guessed value."""
    for stat in ("Shots", "SOT", "Fouls", "Fantasy Score", "Goalie Fantasy Score"):
        kind, _, reason = resolve_stat_spec(EPL_PLUGIN, stat)
        assert kind is None and reason == "unsupported_stat_type", stat


def _soccer_row(player_id: str, name: str, sort_key: int, **stats) -> dict:
    base = {
        "player_id": player_id, "player_display_name": name, "sort_key": sort_key,
        "starter": True, "totalGoals": 0, "goalAssists": 0, "totalShots": 0,
        "shotsOnTarget": 0, "foulsCommitted": 0, "foulsSuffered": 0,
        "yellowCards": 0, "redCards": 0, "saves": 0, "goalsConceded": 0,
    }
    base.update(stats)
    return base


def build_soccer_stats_fixture() -> pd.DataFrame:
    rows = []
    # S1 -- outfield player: Shots/SOT (plain column), Goal + Assist and
    # Cards (composite), 3 games.
    for sk, (g, a, sh, sot, yc, rc) in enumerate(
        [(1, 0, 3, 1, 1, 0), (0, 1, 2, 0, 0, 0), (2, 1, 5, 3, 1, 1)], start=1
    ):
        rows.append(_soccer_row(
            "s1", "Outfield One", sk, totalGoals=g, goalAssists=a, totalShots=sh,
            shotsOnTarget=sot, yellowCards=yc, redCards=rc,
        ))
    # S2 -- goalkeeper: Goalie Saves, Goalie Fantasy Score, across a
    # started+clean-sheet game, a started+conceded game, and a benched game.
    for sk, (starter, sv, gc) in enumerate(
        [(True, 4, 0), (True, 2, 2), (False, 0, 0)], start=1
    ):
        rows.append(_soccer_row("s2", "Keeper Two", sk, starter=starter, saves=sv, goalsConceded=gc))
    return pd.DataFrame(rows)


def test_soccer_plugin_registered_sport_labels():
    assert plugin_for_sport("soccer") is SOCCER_PLUGIN
    assert plugin_for_sport("fifa") is SOCCER_PLUGIN, (
        "Underdog's real 'FIFA' sport label is real-life soccer, not the "
        "video game -- confirmed by real player names (Haaland, Mbappe, "
        "Bellingham) in the 2026-09-11 production pull -- see soccer.py "
        "module docstring"
    )
    assert plugin_for_sport("epl") is not SOCCER_PLUGIN, (
        "EPL must route to the FPL plug-in, not the ESPN plug-in"
    )


def test_soccer_plain_column_and_composite_stats():
    stats = build_soccer_stats_fixture()
    kind, value, _ = resolve_stat_spec(SOCCER_PLUGIN, "Shots")
    assert list(build_stat_series(SOCCER_PLUGIN, stats, "s1", kind, value)) == [3, 2, 5]

    kind, value, _ = resolve_stat_spec(SOCCER_PLUGIN, "SOT")
    assert list(build_stat_series(SOCCER_PLUGIN, stats, "s1", kind, value)) == [1, 0, 3]

    kind, value, _ = resolve_stat_spec(SOCCER_PLUGIN, "Goal + Assist")
    assert list(build_stat_series(SOCCER_PLUGIN, stats, "s1", kind, value)) == [1, 1, 3]

    kind, value, _ = resolve_stat_spec(SOCCER_PLUGIN, "Cards")  # real Underdog wording
    assert list(build_stat_series(SOCCER_PLUGIN, stats, "s1", kind, value)) == [1, 0, 2]


def test_soccer_computed_goalie_fantasy_score():
    """PrizePicks' real Goalie Fantasy Score formula (soccer.py docstring):
    Starting Score=5 (if started), Saves=2 each, Goals Conceded=-2 each,
    Clean Sheet=+5 (started AND 0 conceded).
    game1: started, 4 saves, 0 conceded -> 5 + 8 - 0 + 5 = 18
    game2: started, 2 saves, 2 conceded -> 5 + 4 - 4 + 0 = 5
    game3: NOT started, 0 saves, 0 conceded -> 0 + 0 - 0 + 0 = 0
    """
    stats = build_soccer_stats_fixture()
    kind, value, _ = resolve_stat_spec(SOCCER_PLUGIN, "Goalie Fantasy Score")
    series = build_stat_series(SOCCER_PLUGIN, stats, "s2", kind, value)
    assert list(series) == [18, 5, 0]


def test_soccer_tackles_and_outfield_fantasy_score_stay_unsupported():
    """Real, stated gaps (see soccer.py docstring) -- ESPN's real per-player
    soccer stats have no tackles field, and outfield Fantasy Score needs 6
    of PrizePicks' 11 real formula components that ESPN's data doesn't
    carry. Must resolve to None, not a guessed value."""
    for stat in ("Tackles", "Passes Attempted", "Fantasy Score", "Clearances",
                 "Attempted Dribbles", "Crosses", "1H Goals", "GA F30 Mins"):
        kind, _, reason = resolve_stat_spec(SOCCER_PLUGIN, stat)
        assert kind is None and reason == "unsupported_stat_type", stat


# ---------------------------------------------------------------------------
# Hotfix (2026-09-12) -- fault isolation for per-item HTTP fetches
# ---------------------------------------------------------------------------
# The real GitHub Actions pipeline failed 2026-09-12 when a single ESPN
# `summary?event=...` call (one match out of ~470 real ones walked per run)
# timed out and the unhandled exception propagated out of process_props(),
# silently blanking the estimation output for every sport, not just soccer.
# Each of these tests forces every retry attempt to fail and confirms the
# affected per-item fetch function returns an empty result instead of
# raising -- see pickem_sport_plugins/http_utils.py's module docstring.
def _always_times_out():
    return mock.patch(
        "pickem_sport_plugins.http_utils.requests.get",
        side_effect=requests.exceptions.ReadTimeout("boom"),
    )


def _no_sleep():
    return mock.patch("pickem_sport_plugins.http_utils.time.sleep")


def test_soccer_event_fetch_skips_instead_of_raising_on_repeated_failure():
    with _always_times_out(), _no_sleep():
        rows = _fetch_event_player_rows("esp.1", "999999", 1, "2026-09-01T12:00Z")
    assert rows == []


def test_epl_player_history_fetch_skips_instead_of_raising_on_repeated_failure():
    with _always_times_out(), _no_sleep():
        history = _fetch_player_history(999999)
    assert history == []


def test_mlb_roster_fetch_skips_instead_of_raising_on_repeated_failure():
    with _always_times_out(), _no_sleep():
        roster = _fetch_active_roster(999999)
    assert roster == []


def test_mlb_player_game_log_fetch_skips_instead_of_raising_on_repeated_failure():
    with _always_times_out(), _no_sleep():
        log_rows = _fetch_player_game_log(999999, 2026, "hitting")
    assert log_rows == []


# ---------------------------------------------------------------------------
# SESSION 2.32 -- MLB starter/lineup confirmation signal (Underdog gate).
# Fixture payload shapes below mirror the REAL MLB Stats API responses
# confirmed live 2026-09-15 (see ROADMAP.md Session 2.32 / SESSION_LOG.md
# for the real, live-captured output this mirrors): schedule?hydrate=
# probablePitcher's teams.{away,home}.{team,probablePitcher} shape, and
# v1.1/game/{pk}/feed/live's liveData.boxscore.teams.{away,home}.
# {battingOrder,pitchers} shape.
# ---------------------------------------------------------------------------
def _schedule_payload(games: list[dict]) -> dict:
    return {"dates": [{"games": games}]}


def _schedule_game(
    game_pk, away_id, away_name, away_pitcher, home_id, home_name, home_pitcher
) -> dict:
    return {
        "gamePk": game_pk,
        "teams": {
            "away": {
                "team": {"id": away_id, "name": away_name},
                "probablePitcher": away_pitcher,
            },
            "home": {
                "team": {"id": home_id, "name": home_name},
                "probablePitcher": home_pitcher,
            },
        },
    }


def test_mlb_schedule_fetch_skips_instead_of_raising_on_repeated_failure():
    with _always_times_out(), _no_sleep():
        games = fetch_schedule_games("2026-09-15")
    assert games == []


def test_mlb_confirmed_lineup_fetch_returns_none_on_repeated_failure():
    with _always_times_out(), _no_sleep():
        lineup = fetch_confirmed_lineup(999999)
    assert lineup is None


def test_mlb_fetch_schedule_games_reads_real_shape():
    payload = _schedule_payload([
        _schedule_game(
            824466, 119, "Los Angeles Dodgers",
            {"id": 808967, "fullName": "Yoshinobu Yamamoto"},
            113, "Cincinnati Reds",
            {"id": 695076, "fullName": "Rhett Lowder"},
        ),
    ])
    with mock.patch("pickem_sport_plugins.mlb.get_json_with_retries", return_value=payload):
        games = fetch_schedule_games("2026-09-15")
    assert len(games) == 1
    g = games[0]
    assert g["gamePk"] == 824466
    assert g["away_team_nickname"] == "Dodgers"
    assert g["home_team_nickname"] == "Reds"
    assert g["away_probable_pitcher_id"] == 808967
    assert g["home_probable_pitcher_id"] == 695076


def test_mlb_fetch_schedule_games_handles_missing_probable_pitcher():
    """A real, honest case: MLB hasn't announced one side's probable
    starter yet for a real scheduled game."""
    payload = _schedule_payload([
        _schedule_game(111, 119, "Los Angeles Dodgers", None, 113, "Cincinnati Reds", None),
    ])
    with mock.patch("pickem_sport_plugins.mlb.get_json_with_retries", return_value=payload):
        games = fetch_schedule_games("2026-09-15")
    assert games[0]["away_probable_pitcher_id"] is None
    assert games[0]["home_probable_pitcher_id"] is None


def test_mlb_fetch_probable_pitchers_builds_team_id_map():
    payload = _schedule_payload([
        _schedule_game(
            824466, 119, "Los Angeles Dodgers", {"id": 808967, "fullName": "X"},
            113, "Cincinnati Reds", {"id": 695076, "fullName": "Y"},
        ),
    ])
    with mock.patch("pickem_sport_plugins.mlb.get_json_with_retries", return_value=payload):
        pitchers = fetch_probable_pitchers("2026-09-15")
    assert pitchers == {119: 808967, 113: 695076}


def test_mlb_fetch_confirmed_lineup_returns_none_when_not_posted():
    """Confirmed live 2026-09-15: every game still hours from first pitch
    returns an empty battingOrder/pitchers on both sides."""
    payload = {"liveData": {"boxscore": {"teams": {
        "away": {"battingOrder": [], "pitchers": []},
        "home": {"battingOrder": [], "pitchers": []},
    }}}}
    with mock.patch("pickem_sport_plugins.mlb.get_json_with_retries", return_value=payload):
        lineup = fetch_confirmed_lineup(824466)
    assert lineup is None


def test_mlb_fetch_confirmed_lineup_returns_real_shape_when_posted():
    payload = {"liveData": {"boxscore": {"teams": {
        "away": {"battingOrder": [660271, 605141], "pitchers": [669373, 681911]},
        "home": {"battingOrder": [543760, 592663], "pitchers": [666157]},
    }}}}
    with mock.patch("pickem_sport_plugins.mlb.get_json_with_retries", return_value=payload):
        lineup = fetch_confirmed_lineup(824465)
    assert lineup == {
        "away": {"batting_order": [660271, 605141], "pitchers": [669373, 681911]},
        "home": {"batting_order": [543760, 592663], "pitchers": [666157]},
    }


def test_mlb_fetch_confirmed_lineup_returns_none_for_missing_game_pk():
    assert fetch_confirmed_lineup(None) is None


def test_find_scheduled_game_matches_nickname_with_punctuation_variants():
    """Real case: MLB Stats API's own teamName is "D-backs"; Underdog's
    real wording (confirmed live against data/pickem/clv_log.csv) is
    "D'Backs" -- different punctuation, same real team."""
    games = [{
        "gamePk": 825030,
        "away_team_nickname": "Marlins",
        "home_team_nickname": "D-backs",
    }]
    found = find_scheduled_game(games, "Marlins", "D'Backs")
    assert found is not None
    assert found["gamePk"] == 825030


def test_find_scheduled_game_returns_none_when_no_match():
    games = [{"gamePk": 1, "away_team_nickname": "Mets", "home_team_nickname": "Yankees"}]
    assert find_scheduled_game(games, "Reds", "Dodgers") is None


# --- compute_mlb_starter_status (pickem_model.py) ---------------------------

def _underdog_mlb_row(matchup="Marlins @ D'Backs", start="2026-09-15T22:40:00.000-04:00"):
    return {"game_matchup": matchup, "game_start_time": start, "platform": "underdog", "sport": "mlb"}


def test_compute_mlb_starter_status_returns_none_for_unparseable_matchup():
    row = _underdog_mlb_row(matchup=None)
    assert compute_mlb_starter_status(row, "660271", {}, {}) is None


def test_compute_mlb_starter_status_returns_none_when_no_schedule_match():
    row = _underdog_mlb_row()
    with mock.patch("pickem_model.mlb_plugin_module.fetch_schedule_games", return_value=[]):
        assert compute_mlb_starter_status(row, "660271", {}, {}) is None


def test_compute_mlb_starter_status_not_yet_confirmed_when_no_lineup_posted():
    row = _underdog_mlb_row()
    games = [{
        "gamePk": 825030, "away_team_nickname": "Marlins", "home_team_nickname": "D-backs",
        "away_probable_pitcher_id": 111, "home_probable_pitcher_id": 222,
    }]
    with (
        mock.patch("pickem_model.mlb_plugin_module.fetch_schedule_games", return_value=games),
        mock.patch("pickem_model.mlb_plugin_module.fetch_confirmed_lineup", return_value=None),
    ):
        status = compute_mlb_starter_status(row, "660271", {}, {})
    assert status == MLB_STARTER_STATUS_NOT_YET_CONFIRMED


def test_compute_mlb_starter_status_confirmed_for_batter_in_lineup():
    row = _underdog_mlb_row()
    games = [{
        "gamePk": 825030, "away_team_nickname": "Marlins", "home_team_nickname": "D-backs",
        "away_probable_pitcher_id": 111, "home_probable_pitcher_id": 222,
    }]
    lineup = {
        "away": {"batting_order": [660271, 605141], "pitchers": [111]},
        "home": {"batting_order": [543760], "pitchers": [222]},
    }
    with (
        mock.patch("pickem_model.mlb_plugin_module.fetch_schedule_games", return_value=games),
        mock.patch("pickem_model.mlb_plugin_module.fetch_confirmed_lineup", return_value=lineup),
    ):
        status = compute_mlb_starter_status(row, "660271", {}, {})
    assert status == MLB_STARTER_STATUS_CONFIRMED


def test_compute_mlb_starter_status_different_for_scratched_batter():
    """The real 'Underdog had news, here it is' case: a confirmed lineup
    exists for this game, but this prop's player is NOT in it."""
    row = _underdog_mlb_row()
    games = [{
        "gamePk": 825030, "away_team_nickname": "Marlins", "home_team_nickname": "D-backs",
        "away_probable_pitcher_id": 111, "home_probable_pitcher_id": 222,
    }]
    lineup = {
        "away": {"batting_order": [605141], "pitchers": [111]},  # 660271 scratched
        "home": {"batting_order": [543760], "pitchers": [222]},
    }
    with (
        mock.patch("pickem_model.mlb_plugin_module.fetch_schedule_games", return_value=games),
        mock.patch("pickem_model.mlb_plugin_module.fetch_confirmed_lineup", return_value=lineup),
    ):
        status = compute_mlb_starter_status(row, "660271", {}, {})
    assert status == MLB_STARTER_STATUS_DIFFERENT


def test_compute_mlb_starter_status_confirmed_pitcher_matches_probable():
    row = _underdog_mlb_row()
    games = [{
        "gamePk": 825030, "away_team_nickname": "Marlins", "home_team_nickname": "D-backs",
        "away_probable_pitcher_id": 111, "home_probable_pitcher_id": 222,
    }]
    lineup = {
        "away": {"batting_order": [], "pitchers": [111]},
        "home": {"batting_order": [], "pitchers": [222]},
    }
    with (
        mock.patch("pickem_model.mlb_plugin_module.fetch_schedule_games", return_value=games),
        mock.patch("pickem_model.mlb_plugin_module.fetch_confirmed_lineup", return_value=lineup),
    ):
        status = compute_mlb_starter_status(row, "111", {}, {})
    assert status == MLB_STARTER_STATUS_CONFIRMED


def test_compute_mlb_starter_status_different_when_confirmed_pitcher_differs_from_probable():
    row = _underdog_mlb_row()
    games = [{
        "gamePk": 825030, "away_team_nickname": "Marlins", "home_team_nickname": "D-backs",
        "away_probable_pitcher_id": 111, "home_probable_pitcher_id": 222,
    }]
    # MLB's real confirmed starter for the home side (999) differs from the
    # schedule's own probable pitcher (222) -- a real rotation change.
    lineup = {
        "away": {"batting_order": [], "pitchers": [111]},
        "home": {"batting_order": [], "pitchers": [999]},
    }
    with (
        mock.patch("pickem_model.mlb_plugin_module.fetch_schedule_games", return_value=games),
        mock.patch("pickem_model.mlb_plugin_module.fetch_confirmed_lineup", return_value=lineup),
    ):
        status = compute_mlb_starter_status(row, "222", {}, {})
    assert status == MLB_STARTER_STATUS_DIFFERENT


def test_process_props_leaves_mlb_starter_status_blank_for_non_underdog_rows():
    """Additive-only scope check: a non-MLB, non-Underdog row (this
    project's existing NFL fixture) must never get a non-None
    mlb_starter_status."""
    weekly_fixture = build_nfl_weekly_fixture()
    props_fixture = build_props_fixture()

    def fake_fetch(season):
        return weekly_fixture

    original_fetch = NFL_PLUGIN.fetch_stats
    NFL_PLUGIN.fetch_stats = fake_fetch
    try:
        result = process_props(props_fixture, season=2025)
    finally:
        NFL_PLUGIN.fetch_stats = original_fetch
    assert result["mlb_starter_status"].isna().all()


# ---------------------------------------------------------------------------
# Session 2.28 -- CFB grading-adapter plumbing (`game_date_utc`)
# ---------------------------------------------------------------------------
def _cfb_game(game_id: int, athlete_id: str, athlete_name: str, pass_yds: str) -> dict:
    """Minimal real-shape CFBD `/games/players` game dict -- trimmed to one
    stat (passing YDS) from the real payload structure confirmed live in
    Session 2.16 (see cfb.py's data/pickem/cache/cfbd/2025_regular_wk1.json
    for the full real shape this mirrors)."""
    return {
        "id": game_id,
        "teams": [{
            "team": "Test Team",
            "categories": [{
                "name": "passing",
                "types": [{
                    "name": "YDS",
                    "athletes": [{"id": athlete_id, "name": athlete_name, "stat": pass_yds}],
                }],
            }],
        }],
    }


def test_cfb_plugin_registered_sport_labels():
    assert plugin_for_sport("cfb") is CFB_PLUGIN, (
        "'cfb' is the real sport label both platforms use in "
        "data/pickem/clv_log.csv, confirmed live 2026-09-15"
    )


def test_cfb_plain_column_stat():
    games = [_cfb_game(1, "9001", "Test QB", "247")]
    rows = _flatten_game_players(games)
    kind, value, _ = resolve_stat_spec(CFB_PLUGIN, "Pass Yards")
    stats_df = pd.DataFrame(rows)
    series = build_stat_series(CFB_PLUGIN, stats_df, "9001", kind, value)
    assert list(series) == [247.0]


def test_cfb_flatten_attaches_game_date_utc():
    """Session 2.28: CFBD's `/games/players` payload itself never carries a
    date (real, confirmed gap -- see cfb.py's `_fetch_games_index`
    docstring); the real date has to come in from the separate `/games`
    endpoint's `game_dates` map, keyed by game id as a string. This is the
    one real per-row plumbing change auto_grade_outcomes.py's CFB adapter
    depends on (reusing find_soccer_or_epl_game_row, which reads
    `game_date_utc` directly)."""
    games = [_cfb_game(555, "9001", "Test QB", "300")]
    rows = _flatten_game_players(games, game_dates={"555": "2026-09-06T19:30:00.000Z"})
    assert len(rows) == 1
    assert rows[0]["game_date_utc"] == "2026-09-06T19:30:00.000Z"


def test_cfb_flatten_game_date_utc_none_when_missing():
    """Honest-empty shape (same pattern as every other 'no data yet' case
    in this plug-in) -- a game id with no entry in `game_dates` (e.g. the
    `/games` index call failed or no CFBD_API_KEY was set) must not crash
    the join, just leave the date unresolved for that row."""
    games = [_cfb_game(999, "9002", "Test RB", "88")]
    rows = _flatten_game_players(games, game_dates={})
    assert rows[0]["game_date_utc"] is None


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
