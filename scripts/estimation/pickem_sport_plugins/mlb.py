"""
Session 2.12 -- MLB plug-in: the "adding a second real sport plug-in"
proof case for the multi-sport architecture (see
pickem_sport_plugins/__init__.py and ROADMAP.md's Session 2.12 card).

SCOPE OF THIS FILE, STATED EXPLICITLY
---------------------------------------
This plug-in is real, working code against MLB Stats API
(statsapi.mlb.com -- official, free, no API key/account, confirmed live per
Session 2.10's sport_inventory.md), not a mock. It proves the plug-in
mechanism end-to-end: registering a second sport requires only this file,
not a change to pickem_model.py's process_props() loop.

What it deliberately does NOT do yet, per Session 2.13's own card ("confirm
the real ingested strings directly, don't guess the list in advance, same
rule Session 2.3 followed for NFL"): MLB_STAT_TYPE_MAP below covers only the
handful of hitting stats whose PrizePicks/Underdog wording is unambiguous
(hits, home runs, RBIs, runs, strikeouts, total bases, walks) as a proof-case
set -- it has NOT been checked against real, live ingested MLB stat_type
strings the way NFL's map was in Session 2.3. Session 2.13 is the session
that pulls the real ingested strings and confirms/expands this map for real,
plus builds the "at least one real live MLB prop scores end-to-end" proof
Session 2.12 itself does not claim.

FETCH_STATS -- ONE HTTP CALL PER PLAYER, NOT A BULK PULL
-----------------------------------------------------------
Unlike nflverse's single parquet file for an entire season, MLB Stats API
has no equivalent single bulk "every player's season game log" endpoint.
fetch_mlb_season_stats() below walks all 30 teams' active rosters, then
pulls each hitter's season game log individually
(/people/{id}/stats?stats=gameLog&group=hitting&season=...). This is real,
correct code, but doing this for real at production scale (Session 2.13)
means hundreds of HTTP calls per run -- a cost this session's test suite
avoids by monkeypatching fetch_stats with a small synthetic fixture rather
than exercising the live network path (see test_pickem_model.py). Team IDs
are MLB Stats API's own stable numeric team IDs.
"""

from __future__ import annotations

import requests
import pandas as pd

from . import SportPlugin

MLB_STATS_API_BASE = "https://statsapi.mlb.com/api/v1"

MLB_SPORT_LABELS = frozenset({"mlb", "baseball"})

# All 30 MLB Stats API team IDs (stable, official).
MLB_TEAM_IDS = [
    108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121,
    133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146,
    147, 158,
]

# Proof-case set only -- see module docstring. Not yet confirmed against
# real ingested stat_type strings (that is Session 2.13's job).
MLB_STAT_TYPE_MAP: dict[str, str] = {
    "hits": "hits",
    "home runs": "homeRuns",
    "runs": "runs",
    "rbis": "rbi",
    "strikeouts": "strikeOuts",
    "total bases": "totalBases",
    "walks": "baseOnBalls",
}

MLB_COMPOSITE_STAT_TYPES: dict[str, list[str]] = {
    "hits+runs+rbis": ["hits", "runs", "rbi"],
}

MLB_COMPUTED_STAT_TYPES: dict = {}
MLB_COMPUTED_REQUIRED_COLUMNS: dict = {}


def _fetch_active_roster(team_id: int) -> list[dict]:
    url = f"{MLB_STATS_API_BASE}/teams/{team_id}/roster?rosterType=active"
    resp = requests.get(url, timeout=15)
    resp.raise_for_status()
    return resp.json().get("roster", [])


def _fetch_player_hitting_game_log(person_id: int, season: int) -> list[dict]:
    url = (
        f"{MLB_STATS_API_BASE}/people/{person_id}/stats"
        f"?stats=gameLog&group=hitting&season={season}"
    )
    resp = requests.get(url, timeout=15)
    resp.raise_for_status()
    stats = resp.json().get("stats", [])
    if not stats:
        return []
    return stats[0].get("splits", [])


def fetch_mlb_season_stats(season: int) -> pd.DataFrame:
    """Real MLB Stats API pull: every active-roster hitter across all 30
    teams, one season game log each. See module docstring for why this is
    per-player rather than a single bulk file, and for why this session's
    own test suite does not exercise this function live."""
    rows: list[dict] = []
    for team_id in MLB_TEAM_IDS:
        for player in _fetch_active_roster(team_id):
            person = player.get("person", {})
            person_id = person.get("id")
            full_name = person.get("fullName")
            if person_id is None or not full_name:
                continue
            splits = _fetch_player_hitting_game_log(person_id, season)
            for game_index, split in enumerate(splits, start=1):
                stat = split.get("stat", {})
                rows.append({
                    "player_id": str(person_id),
                    "player_display_name": full_name,
                    "sort_key": game_index,
                    "hits": stat.get("hits", 0),
                    "homeRuns": stat.get("homeRuns", 0),
                    "runs": stat.get("runs", 0),
                    "rbi": stat.get("rbi", 0),
                    "strikeOuts": stat.get("strikeOuts", 0),
                    "totalBases": stat.get("totalBases", 0),
                    "baseOnBalls": stat.get("baseOnBalls", 0),
                })
    return pd.DataFrame(rows)


MLB_PLUGIN = SportPlugin(
    name="mlb",
    sport_labels=MLB_SPORT_LABELS,
    fetch_stats=fetch_mlb_season_stats,
    stat_type_map=MLB_STAT_TYPE_MAP,
    composite_stat_types=MLB_COMPOSITE_STAT_TYPES,
    computed_stat_types=MLB_COMPUTED_STAT_TYPES,
    computed_required_columns=MLB_COMPUTED_REQUIRED_COLUMNS,
)
