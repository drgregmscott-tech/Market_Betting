"""
Session 2.12 -- NFL plug-in for pickem_model.py's multi-sport estimation
architecture.

This is Session 2.3's original NFL logic (stats source, stat-type maps, the
two computed-formula stat types), moved here unchanged as the Session 2.12
refactor's reference implementation -- see pickem_sport_plugins/__init__.py
for the plug-in contract and ROADMAP.md's Session 2.12 card for why this
refactor happened. No scoring behavior changed; see
scripts/estimation/test_pickem_model.py for the byte-for-byte regression
proof against the pre-refactor output.

WHY nflverse (unchanged from the original docstring in pickem_model.py)
-------------------------------------------------------------------------
This project reuses the DFS_Optimizer repo's proven architectural pattern,
not its code. The nflverse data pull below is the same minimal, no-API-key
parquet read as DFS_Optimizer/scripts/nflverse_fetch.py -- copied
deliberately because that file's own docstring records that nfl_data_py (a
more common alternative) is dead upstream for any 2025+ season.
"""

from __future__ import annotations

from typing import Callable

import pandas as pd

from . import SportPlugin

NFLVERSE_BASE_URL = "https://github.com/nflverse/nflverse-data/releases/download"
WEEKLY_STATS_URL_TEMPLATE = (
    f"{NFLVERSE_BASE_URL}/stats_player/stats_player_week_{{season}}.parquet"
)

NFL_SPORT_LABELS = frozenset({"nfl", "football", "nfl football"})

# Maps a pick'em platform's stat_type string (lowercased, trimmed) to the
# single nflverse weekly-stats column measuring the same real-world
# quantity. Add new entries here as real ingested data surfaces stat-type
# strings not yet covered -- do not guess new ones in advance.
NFL_STAT_TYPE_MAP: dict[str, str] = {
    "pass yards": "passing_yards",
    "passing yards": "passing_yards",
    "pass yds": "passing_yards",
    "rush yards": "rushing_yards",
    "rushing yards": "rushing_yards",
    "rush yds": "rushing_yards",
    "receiving yards": "receiving_yards",
    "rec yards": "receiving_yards",
    "receptions": "receptions",
    "recs": "receptions",  # confirmed real variant, Session 2.3 real-data check
    "pass completions": "completions",
    "completions": "completions",
    "pass attempts": "attempts",
    "attempts": "attempts",
    "pass tds": "passing_tds",
    "passing tds": "passing_tds",  # real FanDuel wording, Session 6.2 continuation
    "passing touchdowns": "passing_tds",
    "rush tds": "rushing_tds",
    "rushing tds": "rushing_tds",  # real FanDuel wording, Session 6.2 continuation
    "rushing touchdowns": "rushing_tds",
    # --- Added Session 2.3, from real ingested-data stat_type strings,
    # each checked directly against nflverse's real column list before
    # being added (see pickem_estimation_model_spec.md, "Stat-type
    # coverage" section, for the verification record) ---
    "int": "passing_interceptions",
    "rec tds": "receiving_tds",
    "sacks": "def_sacks",  # a defensive player's own sacks recorded
    "rec targets": "targets",
    "fg made": "fg_made",
}

# Composite stat types are summed across more than one nflverse column.
# Kept separate from NFL_STAT_TYPE_MAP (which is a 1:1 lookup) so the
# single-column and multi-column cases can never be silently confused.
COMPOSITE_STAT_TYPES: dict[str, list[str]] = {
    "rush+rec yards": ["rushing_yards", "receiving_yards"],
    "rush + rec yards": ["rushing_yards", "receiving_yards"],
    "rushing + receiving yards": ["rushing_yards", "receiving_yards"],
    "rush+rec yds": ["rushing_yards", "receiving_yards"],  # real variant, Session 2.3
    "pass+rush+rec yards": ["passing_yards", "rushing_yards", "receiving_yards"],
    "pass + rush + rec yards": ["passing_yards", "rushing_yards", "receiving_yards"],
    # --- Added Session 2.3, from real ingested-data stat_type strings ---
    "player tds": ["passing_tds", "rushing_tds", "receiving_tds"],
    "pass+rush yds": ["passing_yards", "rushing_yards"],
    "pass+rush+rec tds": ["passing_tds", "rushing_tds", "receiving_tds"],
}


# ---------------------------------------------------------------------------
# Computed stat types -- unlike NFL_STAT_TYPE_MAP (one column) and
# COMPOSITE_STAT_TYPES (sum of columns), these apply a real, weighted
# scoring FORMULA across several columns. Both formulas below were taken
# directly from PrizePicks' own official scoring pages, not estimated or
# guessed -- and every nflverse column each formula reads was individually
# confirmed to exist before being used here.
# ---------------------------------------------------------------------------
def _compute_kicking_points(games: pd.DataFrame) -> pd.Series:
    """PrizePicks' official Kicking Points formula (confirmed directly via
    PrizePicks Support on X and prizepicks.com/playbook-article/how-to-play-
    prizepicks-nfl-fantasy-scoring-system, Sept 2025): field goals are
    tiered by distance, not flat -- 0-39 yds = 3 pts, 40-49 yds = 4 pts,
    50+ yds = 5 pts; PAT made = 1 pt; a missed FG or missed PAT is -1 pt
    each. This is explicitly NOT the same as Fantasy Score (PrizePicks'
    own distinction, stated on their scoring page)."""
    fg_0_39 = games[["fg_made_0_19", "fg_made_20_29", "fg_made_30_39"]].sum(axis=1)
    fg_40_49 = games["fg_made_40_49"]
    fg_50_plus = games[["fg_made_50_59", "fg_made_60_"]].sum(axis=1)
    fg_missed = games["fg_missed"]
    pat_made = games["pat_made"]
    pat_missed = games["pat_missed"]
    return (
        fg_0_39 * 3
        + fg_40_49 * 4
        + fg_50_plus * 5
        + pat_made * 1
        - fg_missed * 1
        - pat_missed * 1
    ).reset_index(drop=True)


def _compute_fantasy_score(games: pd.DataFrame) -> pd.Series:
    """PrizePicks' official NFL offensive Fantasy Score formula (confirmed
    directly via prizepicks.com/playbook-article/how-to-play-prizepicks-nfl-
    fantasy-scoring-system, Sept 2025): full PPR. Deliberately OMITS two
    real components of PrizePicks' own table -- Offensive Fumble Recovery
    TDs and Kick/Punt/FG Return TDs (6 pts each) -- because nflverse's
    closest-named columns for these do not reliably correspond to the same
    real-world event (checked directly against real 2025 data: nflverse's
    `pt_return_tds` column fires for PUNTERS on real rows, not the players
    who returned a kick). Both events are rare across a full season, so
    this is a small, real, and explicitly named gap, not a hidden one."""
    fumbles_lost = games[
        ["rushing_fumbles_lost", "receiving_fumbles_lost", "sack_fumbles_lost"]
    ].sum(axis=1)
    two_pt = games[
        ["passing_2pt_conversions", "rushing_2pt_conversions", "receiving_2pt_conversions"]
    ].sum(axis=1)
    return (
        games["passing_yards"] * 0.04
        + games["passing_tds"] * 4
        - games["passing_interceptions"] * 1
        + games["rushing_yards"] * 0.1
        + games["rushing_tds"] * 6
        + games["receptions"] * 1
        + games["receiving_yards"] * 0.1
        + games["receiving_tds"] * 6
        - fumbles_lost * 1
        + two_pt * 2
    ).reset_index(drop=True)


COMPUTED_STAT_TYPES: dict[str, Callable[[pd.DataFrame], pd.Series]] = {
    "kicking points": _compute_kicking_points,
    "fantasy score": _compute_fantasy_score,
}

# Every nflverse column each computed formula reads, so a missing/renamed
# column is caught with a clear message instead of a raw KeyError.
COMPUTED_REQUIRED_COLUMNS: dict[str, list[str]] = {
    "kicking points": [
        "fg_made_0_19", "fg_made_20_29", "fg_made_30_39", "fg_made_40_49",
        "fg_made_50_59", "fg_made_60_", "fg_missed", "pat_made", "pat_missed",
    ],
    "fantasy score": [
        "passing_yards", "passing_tds", "passing_interceptions",
        "rushing_yards", "rushing_tds", "receptions", "receiving_yards",
        "receiving_tds", "rushing_fumbles_lost", "receiving_fumbles_lost",
        "sack_fumbles_lost", "passing_2pt_conversions",
        "rushing_2pt_conversions", "receiving_2pt_conversions",
    ],
}


def fetch_nfl_weekly_stats(season: int) -> pd.DataFrame:
    """Pulls one season of nflverse weekly player stats directly from the
    published parquet release. No API key required. If this 404s, nflverse
    has likely renamed the release again -- see
    https://github.com/nflverse/nflverse-data/releases and update
    WEEKLY_STATS_URL_TEMPLATE above."""
    url = WEEKLY_STATS_URL_TEMPLATE.format(season=season)
    try:
        df = pd.read_parquet(url, engine="pyarrow")
    except Exception as exc:  # noqa: BLE001
        raise RuntimeError(
            f"Failed to fetch nflverse weekly stats for season {season} from "
            f"{url}. If this is a 404, nflverse may have renamed the release "
            f"-- check https://github.com/nflverse/nflverse-data/releases. "
            f"Original error: {exc}"
        ) from exc
    df = df[df["season_type"] == "REG"].copy()
    # Plug-in contract (see pickem_sport_plugins/__init__.py): every plug-in's
    # fetch_stats() must supply a chronological "sort_key" column. nflverse's
    # own "week" column already is one -- aliased, not replaced, since
    # NAME/format details elsewhere in this file still reference "week"
    # nowhere outside this function.
    df["sort_key"] = df["week"]
    return df


NFL_PLUGIN = SportPlugin(
    name="nfl",
    sport_labels=NFL_SPORT_LABELS,
    fetch_stats=fetch_nfl_weekly_stats,
    stat_type_map=NFL_STAT_TYPE_MAP,
    composite_stat_types=COMPOSITE_STAT_TYPES,
    computed_stat_types=COMPUTED_STAT_TYPES,
    computed_required_columns=COMPUTED_REQUIRED_COLUMNS,
)
