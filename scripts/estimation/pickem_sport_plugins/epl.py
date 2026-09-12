"""
Session 2.14 -- EPL plug-in for pickem_model.py's multi-sport estimation
architecture. Every other soccer league (La Liga, Serie A, Bundesliga,
Ligue 1, MLS) is handled by pickem_sport_plugins/soccer.py -- see that
file's docstring for why the split exists and ROADMAP.md's Session 2.14
card for the "why this sport" background.

WHY THE OFFICIAL FANTASY PREMIER LEAGUE API, NOT ESPN, FOR EPL SPECIFICALLY
-----------------------------------------------------------------------------
Per docs/research/sport_inventory.md: the Premier League runs its own
official Fantasy Premier League API (fantasy.premierleague.com/api) -- free,
no key, no login -- confirmed live with real per-player stats for 651
current players and a real, current gameweek (Gameweek 2 as of the 2026-09-11
research pull, matching the actual 2026-27 season calendar). This is the
same shape of source as nflverse/MLB Stats API/nba_api: official, free, no
gate -- the roadmap card explicitly calls for EPL to use this path rather
than ESPN's generic soccer API, even though ESPN's API also covers EPL,
because it is the more authoritative, EPL-specific source.

FETCH SHAPE -- ONE BOOTSTRAP CALL + ONE PER-PLAYER HISTORY CALL
-------------------------------------------------------------------
`bootstrap-static/` returns every current player's identity (real per-player
counts confirmed live: 656 as of this session's pull) but only SEASON-TO-DATE
totals, not a per-game series -- build_stat_series() needs one row per game
(see the fetch_stats contract in pickem_sport_plugins/__init__.py). The real
per-gameweek series lives at `element-summary/{player_id}/`'s `history` list
(confirmed live: one row per real gameweek played, with `round` as a real,
stable chronological ordinal -- aliased to `sort_key` below). This means one
HTTP call per player per production run (~650+ calls) -- the same accepted
real cost class as Session 2.13's MLB plug-in (no bulk per-player-history
endpoint exists here either).

STAT-TYPE COVERAGE -- REAL, CONFIRMED FIELDS, AND A REAL, SUBSTANTIAL STATED
GAP (NOT A SILENT ONE)
-----------------------------------------------------------------------------
Real per-gameweek FPL fields (confirmed live, 2026-09-11): minutes,
goals_scored, assists, clean_sheets, goals_conceded, own_goals,
penalties_saved, penalties_missed, yellow_cards, red_cards, saves, bonus,
bps, tackles, clearances_blocks_interceptions, recoveries, starts,
expected_goals, expected_assists. Real ingested EPL stat_type strings
(2026-09-11 production pull, 3,512 real PrizePicks "EPL" rows -- see
docs/research/pickem_estimation_model_spec.md's Session 2.14 section for the
full table) were checked against this exact field list:
  - Mapped (single column): Goals -> goals_scored, Assists -> assists,
    Tackles -> tackles, Goalie Saves -> saves, Goals Allowed -> goals_conceded
  - Mapped (composite, summed): Goal + Assist -> goals_scored+assists
  - LEFT UNSUPPORTED, a real and SUBSTANTIAL stated gap: Shots (937 real
    rows), SOT (639), Fouls (319), Fantasy Score (14), Goalie Fantasy Score
    (8), Clearances (3, and `clearances_blocks_interceptions` is a real,
    DIFFERENT combined stat -- clearances+blocks+interceptions, not pure
    clearances -- mapping it to a stat literally named "Clearances" would
    misrepresent what it measures, so it is left unmapped rather than
    treated as a close-enough substitute), Attempted Dribbles (3), Crosses
    (2), Passes Attempted (16), GA F30 Mins (1). FPL's real per-gameweek
    data simply does not carry shot counts, foul counts, or the six raw
    inputs PrizePicks' own outfield Fantasy Score formula needs (see
    pickem_sport_plugins/soccer.py's docstring for that formula's full,
    sourced point values) -- this is the same "no unnamed black-box
    factors" standard that already governs every other plug-in's stated
    gaps (Session 2.3's punt-return-TD gap, Session 2.13's MLB Underdog
    Fantasy Points gap), applied honestly here even though it leaves a
    real MAJORITY (about 55%) of real EPL row volume unsupported. Real,
    substantial non-EPL coverage from pickem_sport_plugins/soccer.py (ESPN)
    is NOT reduced by this -- ESPN's real field set genuinely does carry
    shots/SOT/fouls, which is why those ARE mapped there. This is a real,
    checked difference between the two data sources, not an inconsistency
    to "fix" by guessing at FPL data that does not exist.
"""

from __future__ import annotations

import requests
import pandas as pd

from . import SportPlugin

FPL_BASE = "https://fantasy.premierleague.com/api"

EPL_SPORT_LABELS = frozenset({"epl"})

EPL_STAT_TYPE_MAP: dict[str, str] = {
    "goals": "goals_scored",
    "assists": "assists",
    "tackles": "tackles",
    "goalie saves": "saves",
    "goals allowed": "goals_conceded",
}

EPL_COMPOSITE_STAT_TYPES: dict[str, list[str]] = {
    "goal + assist": ["goals_scored", "assists"],
}


def _fetch_current_players() -> list[dict]:
    resp = requests.get(f"{FPL_BASE}/bootstrap-static/", timeout=20)
    resp.raise_for_status()
    return resp.json().get("elements", [])


def _fetch_player_history(player_id: int) -> list[dict]:
    resp = requests.get(f"{FPL_BASE}/element-summary/{player_id}/", timeout=20)
    resp.raise_for_status()
    return resp.json().get("history", [])


def fetch_epl_season_stats(season: int) -> pd.DataFrame:
    """Real Fantasy Premier League API pull: every current player's real
    per-gameweek history this season so far. `season` is accepted for
    contract consistency with every other plug-in but unused -- the FPL API
    always serves the CURRENT season's own data, with no season parameter of
    its own (confirmed live: bootstrap-static's current gameweek always
    matches the real, ongoing season)."""
    rows: list[dict] = []
    for player in _fetch_current_players():
        player_id = player.get("id")
        full_name = f"{player.get('first_name', '')} {player.get('second_name', '')}".strip()
        if player_id is None or not full_name:
            continue
        for gw in _fetch_player_history(player_id):
            rows.append({
                "player_id": str(player_id),
                "player_display_name": full_name,
                "sort_key": gw.get("round"),
                "goals_scored": gw.get("goals_scored", 0) or 0,
                "assists": gw.get("assists", 0) or 0,
                "tackles": gw.get("tackles", 0) or 0,
                "saves": gw.get("saves", 0) or 0,
                "goals_conceded": gw.get("goals_conceded", 0) or 0,
            })
    return pd.DataFrame(rows)


EPL_PLUGIN = SportPlugin(
    name="epl",
    sport_labels=EPL_SPORT_LABELS,
    fetch_stats=fetch_epl_season_stats,
    stat_type_map=EPL_STAT_TYPE_MAP,
    composite_stat_types=EPL_COMPOSITE_STAT_TYPES,
)
