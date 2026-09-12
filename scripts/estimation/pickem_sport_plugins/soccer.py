"""
Session 2.14 -- Soccer plug-in (everything outside EPL) for pickem_model.py's
multi-sport estimation architecture. EPL specifically is its own plug-in
(pickem_sport_plugins/epl.py, the official Fantasy Premier League API) -- see
that file's docstring for why EPL is split out rather than folded in here.

WHY ESPN's PUBLIC SPORTS API
------------------------------
Per docs/research/sport_inventory.md's "Soccer/EPL" section: ESPN runs a
public sports data API (site.api.espn.com) needing no key or account, and it
covers every major soccer league through the same URL pattern (just swapping
the league code). Confirmed live, this session (2026-09-11), for all five
league codes below -- La Liga and MLS had already been checked in the
research doc; Bundesliga and Ligue 1 are confirmed live for the FIRST time
by this session (real completed matches returned for both: 9 STATUS_FULL_TIME
events each in a 2026-09-01..11 scan window), closing this card's first
validation item.

THE REAL GOTCHA sport_inventory.md ALREADY FOUND: per-player stats live at
`rosters[].roster[].stats` on the event SUMMARY endpoint
(`.../soccer/{league}/summary?event={id}`), NOT the more obvious
`boxscore.players`, which only carries team-level totals for soccer
specifically. This plug-in reads `rosters[].roster[].stats`, per that
finding.

NO SEASON-AGGREGATE ENDPOINT -- WHY THIS PLUG-IN WALKS GAME BOXSCORES
-----------------------------------------------------------------------
Unlike nflverse's single parquet file or MLB Stats API's per-player season
game log, ESPN's public API has no single "every player's season stat line"
endpoint for soccer. Building a per-game series (the shape build_stat_series()
needs -- see pickem_sport_plugins/__init__.py's fetch_stats contract) means:
  1. Walking each league's SCOREBOARD across the season so far, month by
     month (a single wide date range was tried and silently returned FEWER
     events than two narrower calls covering the same span -- e.g. usa.1
     returned 25 events for a Feb-Sep range but 29 for just Sep 1-11 alone,
     an undocumented real quirk, not a coding mistake -- so this plug-in
     chunks by calendar month and dedupes by event id instead of trusting
     one wide-range call).
  2. Pulling each completed match's own SUMMARY endpoint for the real
     per-player stat rows.
This means hundreds of real HTTP calls per production run across five
leagues and a partial season -- an accepted, real cost of this data source,
same precedent as Session 2.13's MLB plug-in (no bulk alternative exists).

LEAGUE CODES AND SEASON-START MONTHS (real, checked)
-------------------------------------------------------
La Liga/Serie A/Bundesliga/Ligue 1 seasons start in August of the given
`season` year (matching the FPL API's own current-season confirmation:
Gameweek 2 as of 2026-09-11, i.e. the season that started August 2026).
MLS's season starts in February/March of the SAME calendar year (a real,
different convention -- soccer's "season" is not always Aug-May). Both are
handled by starting each league's month-chunk walk at its own real start
month for the same `season` int, rather than assuming one universal
convention.

STAT-TYPE COVERAGE -- REAL, CONFIRMED FIELDS, MAPPED PLATFORM-BY-PLATFORM
------------------------------------------------------------------------
ESPN's real per-player match stats (confirmed live across all five leagues
below, 2026-09-11, on real completed matches): appearances, foulsCommitted,
foulsSuffered, goalAssists, goalsConceded, offsides, ownGoals, redCards,
saves, shotsFaced, shotsOnTarget, subIns, totalGoals, totalShots,
yellowCards. Real ingested stat_type strings (2026-09-11 production pull,
10,113 real PrizePicks "SOCCER" rows + 2,581 real Underdog "FIFA" rows --
see docs/research/pickem_estimation_model_spec.md's Session 2.14 section for
the full table with real counts) were checked against this exact field list
before mapping anything:
  - Mapped (single column): Shots/Shots Attempted -> totalShots, SOT/Shots on
    Target -> shotsOnTarget, Goals -> totalGoals, Assists -> goalAssists,
    Fouls/Fouls Committed -> foulsCommitted, Fouls Drawn -> foulsSuffered,
    Goalie Saves/Saves -> saves, Goals Allowed -> goalsConceded
  - Mapped (composite, summed): Goal + Assist / Goals + Assists ->
    totalGoals+goalAssists, Cards (Underdog) -> yellowCards+redCards
  - Mapped (computed formula): Goalie Fantasy Score (PrizePicks' own official
    goalkeeper scoring, see _compute_goalie_fantasy_score below)
  - LEFT UNSUPPORTED, real stated gaps (not guessed at):
    - Tackles (PrizePicks, 1,109 real rows) -- ESPN's real per-player stat
      set for soccer has no tackles field at all, checked directly across
      all 5 leagues; there is no column to map to.
    - Passes Attempted (68), Clearances (13), Attempted Dribbles (12),
      Shots Assisted (9), Crosses (4) -- same reason: not present in ESPN's
      real per-player field set.
    - Fantasy Score, outfield (PrizePicks, 40 real rows) -- PrizePicks'
      real, sourced Outfield Fantasy Score formula (confirmed live via
      prizepicks.com/playbook-article/how-to-play-prizepicks-soccer-fantasy-
      scoring-system-for-world-cup, 2026-09-11: Goal=10, Assist=5, Shot=1,
      Shot on Target=1, Passes Attempted=0.05, Shots Assisted=0.5,
      Clearances=1, Tackles Attempted=1, Attempted Dribbles=1, Crosses=0.5,
      Yellow Card=-1, Red Card=-2, Fouls=-0.5) needs 6 of its 11 components
      (Passes Attempted, Shots Assisted, Clearances, Tackles Attempted,
      Attempted Dribbles, Crosses) that ESPN's real per-player data does not
      carry. Computing it from only the 5 available components would
      silently misrepresent it as the real formula while quietly dropping
      more than half its inputs -- this project's "no unnamed black-box
      factors" rule (Session 2.3, reaffirmed every sport session since)
      means this is left unsupported rather than approximated. Goalie
      Fantasy Score (below) is NOT the same gap -- its own real formula only
      needs components ESPN's data does carry (see below).
    - 1H Goals (Underdog, 131 real rows) / GA F30 Mins (PrizePicks, 1 real
      row) -- both need a within-game time split (first half / first 30
      minutes) that ESPN's per-match TOTAL stat line does not carry. Same
      real architecture mismatch as MLB's per-inning gap (Session 2.13):
      the season_avg/recent_form model is built around one number per game.

GOALIE FANTASY SCORE -- WHY THIS ONE COULD BE COMPUTED WHEN OUTFIELD
FANTASY SCORE COULD NOT
-----------------------------------------------------------------------
PrizePicks' real, sourced Goalie Fantasy Score formula (same source as
above): Starting Score=5 (if started), Saves=2 each, Goals Conceded=-2 each,
Clean Sheet=+5 (if started and conceded 0). Every one of these components
maps to a real ESPN field this plug-in already fetches (`starter` -- a real
boolean on each roster entry, confirmed live -- `saves`, `goalsConceded`);
Clean Sheet is derived (started AND goalsConceded==0), not guessed, the same
way MLB's Quality Start was derived from real outs/earnedRuns columns
(Session 2.13). This is why Goalie Fantasy Score is mapped while Outfield
Fantasy Score, needing components ESPN's real data does not expose, is not.
"""

from __future__ import annotations

import calendar
from datetime import date
from typing import Callable

import requests
import pandas as pd

from . import SportPlugin

ESPN_BASE = "https://site.api.espn.com/apis/site/v2/sports/soccer"

# Real ESPN league codes, confirmed live 2026-09-11 (La Liga/MLS previously
# confirmed in docs/research/sport_inventory.md; Bundesliga/Ligue 1 confirmed
# live for the first time this session -- see module docstring). Value is
# each league's real season-start month for the `season` int passed in.
LEAGUE_SEASON_START_MONTH: dict[str, int] = {
    "esp.1": 8,  # La Liga
    "ita.1": 8,  # Serie A
    "ger.1": 8,  # Bundesliga
    "fra.1": 8,  # Ligue 1
    "usa.1": 2,  # MLS -- real, different convention: season starts Feb/Mar
}

# Real ingested sport labels (2026-09-11 production pull): PrizePicks uses
# "SOCCER" for every non-EPL competition; Underdog uses "FIFA" for real-life
# soccer props (confirmed by real player names in that category -- Haaland,
# Mbappe, Bellingham, etc. -- NOT the video game). "EPL" is deliberately
# excluded here -- that sport label routes to the FPL-based plug-in instead
# (pickem_sport_plugins/epl.py).
SOCCER_SPORT_LABELS = frozenset({"soccer", "fifa"})

SOCCER_STAT_TYPE_MAP: dict[str, str] = {
    "shots": "totalShots",
    "shots attempted": "totalShots",  # real Underdog wording
    "sot": "shotsOnTarget",
    "shots on target": "shotsOnTarget",  # real Underdog wording
    "goals": "totalGoals",
    "assists": "goalAssists",
    "fouls": "foulsCommitted",  # real PrizePicks wording
    "fouls committed": "foulsCommitted",  # real Underdog wording
    "fouls drawn": "foulsSuffered",  # real Underdog wording
    "goalie saves": "saves",  # real PrizePicks wording
    "saves": "saves",  # real Underdog wording
    "goals allowed": "goalsConceded",  # real PrizePicks wording
}

SOCCER_COMPOSITE_STAT_TYPES: dict[str, list[str]] = {
    "goal + assist": ["totalGoals", "goalAssists"],  # real PrizePicks wording
    "goals + assists": ["totalGoals", "goalAssists"],  # real Underdog wording
    "cards": ["yellowCards", "redCards"],  # real Underdog wording
}


# ---------------------------------------------------------------------------
# Computed stat types
# ---------------------------------------------------------------------------
def _compute_goalie_fantasy_score(games: pd.DataFrame) -> pd.Series:
    """PrizePicks' official Goalie Fantasy Score formula (confirmed live,
    2026-09-11, via prizepicks.com/playbook-article/how-to-play-prizepicks-
    soccer-fantasy-scoring-system-for-world-cup): Starting Score=5 (if
    started), Saves=2 each, Goals Conceded=-2 each, Clean Sheet=+5 (started
    AND 0 goals conceded). Real PrizePicks stat_type "Goalie Fantasy Score"
    (17 rows, 2026-09-11 pull)."""
    started = games["starter"].astype(int).reset_index(drop=True)
    conceded = games["goalsConceded"].reset_index(drop=True)
    clean_sheet = ((games["starter"]) & (games["goalsConceded"] == 0)).astype(int).reset_index(drop=True)
    return (
        started * 5
        + games["saves"].reset_index(drop=True) * 2
        - conceded * 2
        + clean_sheet * 5
    )


SOCCER_COMPUTED_STAT_TYPES: dict[str, Callable[[pd.DataFrame], pd.Series]] = {
    "goalie fantasy score": _compute_goalie_fantasy_score,
}

SOCCER_COMPUTED_REQUIRED_COLUMNS: dict[str, list[str]] = {
    "goalie fantasy score": ["starter", "saves", "goalsConceded"],
}


# ---------------------------------------------------------------------------
# Fetch
# ---------------------------------------------------------------------------
def _month_ranges(season: int, start_month: int) -> list[tuple[str, str]]:
    """Yields (YYYYMMDD, YYYYMMDD) covering each real calendar month from
    the league's own season-start month through today -- see module
    docstring's "NO SEASON-AGGREGATE ENDPOINT" note for why this chunks by
    month instead of trusting one wide date range."""
    today = date.today()
    ranges: list[tuple[str, str]] = []
    year, month = season, start_month
    while (year, month) <= (today.year, today.month):
        last_day = calendar.monthrange(year, month)[1]
        end_day = today.day if (year, month) == (today.year, today.month) else last_day
        ranges.append((f"{year}{month:02d}01", f"{year}{month:02d}{end_day:02d}"))
        month += 1
        if month > 12:
            month = 1
            year += 1
    return ranges


def _fetch_completed_events(league_code: str, season: int) -> list[tuple[str, str]]:
    """Returns [(event_id, iso_date), ...] for every real completed match
    this league has played so far this season, deduped across the
    month-chunked scoreboard calls."""
    start_month = LEAGUE_SEASON_START_MONTH[league_code]
    seen: dict[str, str] = {}
    for start, end in _month_ranges(season, start_month):
        url = f"{ESPN_BASE}/{league_code}/scoreboard?dates={start}-{end}&limit=1000"
        resp = requests.get(url, timeout=20)
        resp.raise_for_status()
        for event in resp.json().get("events", []):
            event_id = event.get("id")
            status = (event.get("status") or {}).get("type", {}).get("name")
            if event_id and status == "STATUS_FULL_TIME" and event_id not in seen:
                seen[event_id] = event.get("date", "")
    return sorted(seen.items(), key=lambda pair: pair[1])


def _fetch_event_player_rows(league_code: str, event_id: str, sort_key: int) -> list[dict]:
    url = f"{ESPN_BASE}/{league_code}/summary?event={event_id}"
    resp = requests.get(url, timeout=20)
    resp.raise_for_status()
    rows: list[dict] = []
    for roster in resp.json().get("rosters", []):
        for player in roster.get("roster", []):
            athlete = player.get("athlete", {})
            player_id = athlete.get("id")
            full_name = athlete.get("fullName") or athlete.get("displayName")
            if not player_id or not full_name:
                continue
            stat_values = {s["name"]: s.get("value") for s in player.get("stats", []) if "name" in s}
            rows.append({
                "player_id": str(player_id),
                "player_display_name": full_name,
                "sort_key": sort_key,
                "starter": bool(player.get("starter")),
                "totalGoals": stat_values.get("totalGoals", 0) or 0,
                "goalAssists": stat_values.get("goalAssists", 0) or 0,
                "totalShots": stat_values.get("totalShots", 0) or 0,
                "shotsOnTarget": stat_values.get("shotsOnTarget", 0) or 0,
                "foulsCommitted": stat_values.get("foulsCommitted", 0) or 0,
                "foulsSuffered": stat_values.get("foulsSuffered", 0) or 0,
                "yellowCards": stat_values.get("yellowCards", 0) or 0,
                "redCards": stat_values.get("redCards", 0) or 0,
                "saves": stat_values.get("saves", 0) or 0,
                "goalsConceded": stat_values.get("goalsConceded", 0) or 0,
            })
    return rows


def fetch_soccer_espn_season_stats(season: int) -> pd.DataFrame:
    """Real ESPN pull across five confirmed-live leagues (see module
    docstring): walks each league's completed-match scoreboard for the
    season so far, then each match's own summary endpoint for real
    per-player stat rows. `sort_key` is each league's own chronological
    match order (by real event date), matching the fetch_stats contract in
    pickem_sport_plugins/__init__.py."""
    rows: list[dict] = []
    for league_code in LEAGUE_SEASON_START_MONTH:
        events = _fetch_completed_events(league_code, season)
        for game_index, (event_id, _iso_date) in enumerate(events, start=1):
            rows.extend(_fetch_event_player_rows(league_code, event_id, game_index))
    return pd.DataFrame(rows)


SOCCER_PLUGIN = SportPlugin(
    name="soccer",
    sport_labels=SOCCER_SPORT_LABELS,
    fetch_stats=fetch_soccer_espn_season_stats,
    stat_type_map=SOCCER_STAT_TYPE_MAP,
    composite_stat_types=SOCCER_COMPOSITE_STAT_TYPES,
    computed_stat_types=SOCCER_COMPUTED_STAT_TYPES,
    computed_required_columns=SOCCER_COMPUTED_REQUIRED_COLUMNS,
)
