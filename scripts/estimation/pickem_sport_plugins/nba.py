"""
Session 2.15 -- NBA plug-in scaffold (proof-case, UNVERIFIED against a real
live game -- same split as Session 2.12's MLB scaffold before Session 2.13's
real verification pass).

WHY THIS SESSION IS SPLIT INTO ARCHITECTURE-NOW / VERIFICATION-LATER
----------------------------------------------------------------------
ROADMAP.md's Session 2.15 card is explicitly blocked, not on research: the
NBA regular season starts 2026-10-20 (confirmed directly below, not assumed
-- see "REAL DATA CONFIRMING THE SEASON-START DATE"), so there is no live
game yet to fetch a real box score from or grade a real prop against. The
user chose (this session, 2026-09-12) to build the offline half now --
fetch code, stat map, plug-in registration -- and leave live validation
explicitly open, rather than wait idle until October. Everything below is
real, working code against ESPN's real public endpoint shape, but the stat
map has NOT been confirmed against a real live NBA box score the way MLB's
map was confirmed against Aaron Judge's/Gerrit Cole's real payloads
(Session 2.13). Treat this file the same way Session 2.12's MLB scaffold
was treated: real architecture, unverified numbers, until a real game plays.

WHY ESPN's PUBLIC API, NOT `nba_api` (a deviation from sport_inventory.md's
stated recommendation, stated here so it isn't silently different from the
roadmap card)
----------------------------------------------------------------------
docs/research/sport_inventory.md named `nba_api` (a wrapper around
stats.nba.com/cdn.nba.com) as the strong candidate, but noted its own live
check was blocked by the off-season, not by a real problem with the source.
This plug-in uses ESPN's public sports API instead (`site.api.espn.com`),
the same source already proven live and working in this exact codebase for
soccer (pickem_sport_plugins/soccer.py, Session 2.14) -- no key, no
account, and (unlike stats.nba.com) no documented bot-detection headers
required to get a real response. This is a reasoned substitution, not a
silent swap: `nba_api`/stats.nba.com remains a fallback to reconsider if
ESPN's real NBA box score data (once checked live in October) turns out to
be missing a stat this plug-in needs.

REAL DATA CONFIRMING THE SEASON-START DATE (checked directly, 2026-09-12,
not assumed)
----------------------------------------------------------------------
A live production ingestion pull already carries 194 real PrizePicks NBA
rows for real season-opener games -- e.g. real matchup "BOS @ DET",
`game_start_time` 2026-10-20T15:10:00-04:00, `status` "pre_game" -- despite
today being 2026-09-12, well before any real games have been played. These
are real futures-style pre-season listings, not live in-game props; they
confirm the real season start date but cannot be used to verify a stat map
against an actual played game (there is no box score yet for a game that
hasn't happened).

STAT-TYPE COVERAGE -- REAL, CONFIRMED STRINGS; UNVERIFIED MAPPING TARGETS
----------------------------------------------------------------------
The stat_type strings themselves ARE real, pulled from that same live
2026-09-12 ingestion run (194 real PrizePicks NBA rows, real counts):
Pts+Rebs (30), PRA (29), Points (26), Pts+Asts (25), Rebounds (24), 3PTM
(22), Assists (20), Rebs+Asts (11), Double-Double (4), Blocked Shots (3).
What is NOT yet verified is the right-hand side of NBA_STAT_TYPE_MAP below
-- the ESPN box-score field names each one should read. Those are written
from ESPN's publicly documented basketball box-score label set (PTS, REB,
AST, BLK, 3PM, ...), the same label vocabulary broadcast box scores use,
but this plug-in has not yet pulled one real ESPN NBA summary payload to
confirm those exact label strings appear verbatim (no live game exists to
pull). Session 2.15's own re-opening (once the season starts, per its
roadmap card) must re-confirm every one of these against a real payload
before this plug-in is trusted, the same way Session 2.13 did for MLB.

Double-Double (4 real rows) is deliberately LEFT UNSUPPORTED here, not
guessed at: it depends on which two categories (of points/rebounds/
assists/steals/blocks) each cross 10 in a given game -- a real derived
condition, not a single column -- and this plug-in has no verified real
box score yet to confirm ESPN's per-player fields carry every category
needed to compute it correctly. Left unsupported rather than assumed,
same standard as every other sport plug-in's stated gaps.

FETCH SHAPE -- SAME "NO SEASON-AGGREGATE ENDPOINT" COST AS SOCCER
----------------------------------------------------------------------
Same real constraint as pickem_sport_plugins/soccer.py: ESPN's public API
has no single "every player's season stat line" endpoint for basketball
either. fetch_nba_espn_season_stats() below walks the season's scoreboard
month-by-month starting at the real 2026-10 season start, then each
completed game's own summary endpoint for real per-player box-score rows --
same month-chunking and per-item fault-isolation (http_utils.
get_json_with_retries, skip-and-log on repeated failure) as soccer's
plug-in, for the same reasons (hundreds of real per-game calls per run;
one transient timeout must not abort every sport's estimation output,
per the 2026-09-12 pipeline hotfix already applied to MLB/soccer/EPL).
"""

from __future__ import annotations

import calendar
import logging
from datetime import date

import pandas as pd

from . import SportPlugin
from .http_utils import get_json_with_retries

log = logging.getLogger("pickem_model")

ESPN_BASE = "https://site.api.espn.com/apis/site/v2/sports/basketball/nba"

# Real ingested sport label (2026-09-12 production pull, 194 real PrizePicks
# rows). WNBA/NBASZN/BASKETBALL/FIBA are separate real sport labels seen in
# the same pull -- deliberately excluded, out of this session's stated scope
# (ROADMAP.md's Session 2.15 card covers NBA only).
NBA_SPORT_LABELS = frozenset({"nba"})

# NBA's regular season starts in October of the `season` year (confirmed
# directly above via real 2026-10-20 season-opener rows) -- same per-league
# "own real start month" handling soccer.py already uses, not a universal
# assumption.
SEASON_START_MONTH = 10

# UNVERIFIED against a real live payload -- see module docstring's
# "STAT-TYPE COVERAGE" section. Values are ESPN's publicly documented
# basketball box-score labels, not yet confirmed live against this exact
# endpoint.
NBA_STAT_TYPE_MAP: dict[str, str] = {
    "points": "PTS",
    "rebounds": "REB",
    "assists": "AST",
    "3ptm": "3PM",
    "blocked shots": "BLK",
}

NBA_COMPOSITE_STAT_TYPES: dict[str, list[str]] = {
    "pts+rebs": ["PTS", "REB"],
    "pts+asts": ["PTS", "AST"],
    "rebs+asts": ["REB", "AST"],
    "pra": ["PTS", "REB", "AST"],
}


# ---------------------------------------------------------------------------
# Fetch -- same month-chunked scoreboard + per-game summary shape as
# pickem_sport_plugins/soccer.py's fetch_soccer_espn_season_stats(), applied
# to basketball's box-score payload shape instead of soccer's rosters[].stats
# name/value shape (see module docstring -- unverified until a real game
# exists to check the parsing against).
# ---------------------------------------------------------------------------
def _month_ranges(season: int) -> list[tuple[str, str]]:
    """Same real calendar-month chunking as soccer.py's _month_ranges, using
    NBA's own October season-start month for the given `season` year."""
    today = date.today()
    ranges: list[tuple[str, str]] = []
    year, month = season, SEASON_START_MONTH
    while (year, month) <= (today.year, today.month):
        last_day = calendar.monthrange(year, month)[1]
        end_day = today.day if (year, month) == (today.year, today.month) else last_day
        ranges.append((f"{year}{month:02d}01", f"{year}{month:02d}{end_day:02d}"))
        month += 1
        if month > 12:
            month = 1
            year += 1
    return ranges


def _fetch_completed_events(season: int) -> list[tuple[str, str]]:
    """Returns [(event_id, iso_date), ...] for every completed NBA game so
    far this season. Same per-month fault isolation as soccer.py's
    _fetch_completed_events -- one month's scoreboard call failing after
    retries is logged and skipped, not fatal to the whole plug-in."""
    seen: dict[str, str] = {}
    for start, end in _month_ranges(season):
        url = f"{ESPN_BASE}/scoreboard?dates={start}-{end}&limit=1000"
        try:
            payload = get_json_with_retries(url, timeout=20)
        except Exception as exc:  # noqa: BLE001
            log.warning(
                "Skipping NBA scoreboard for %s-%s after repeated failures: %s",
                start, end, exc,
            )
            continue
        for event in payload.get("events", []):
            event_id = event.get("id")
            status = (event.get("status") or {}).get("type", {}).get("name")
            if event_id and status == "STATUS_FINAL" and event_id not in seen:
                seen[event_id] = event.get("date", "")
    return sorted(seen.items(), key=lambda pair: pair[1])


def _parse_athlete_stats(names: list[str], athlete_entry: dict) -> dict[str, str]:
    """ESPN's basketball box score reports one `stats` array per athlete,
    positionally aligned with a shared `names` header array (e.g.
    ["MIN","FG","3PT","FT","OREB","DREB","REB","AST","STL","BLK","TO","PF",
    "+/-","PTS"]) rather than soccer's name/value pairs -- UNVERIFIED here
    (no real live payload pulled yet, see module docstring), written from
    ESPN's publicly documented label set. Returns a dict of label -> raw
    string value; some values (e.g. "5-10" for FG makes-attempts) are not
    plain integers, so this plug-in only reads columns it needs from
    NBA_STAT_TYPE_MAP as-is (PTS/REB/AST/BLK are plain integer strings; 3PM
    is read from the "3PT" makes-attempts split, first number)."""
    values = athlete_entry.get("stats", [])
    return dict(zip(names, values))


def _fetch_event_player_rows(event_id: str, sort_key: int) -> list[dict]:
    """Same fault-isolation standard as soccer.py's _fetch_event_player_rows
    -- one game's summary call failing after retries returns no rows for
    this one game rather than raising."""
    url = f"{ESPN_BASE}/summary?event={event_id}"
    try:
        payload = get_json_with_retries(url, timeout=20)
    except Exception as exc:  # noqa: BLE001
        log.warning("Skipping NBA event %s after repeated failures: %s", event_id, exc)
        return []

    rows: list[dict] = []
    for team_block in (payload.get("boxscore") or {}).get("players", []):
        for stat_group in team_block.get("statistics", []):
            names = stat_group.get("names", [])
            for athlete_entry in stat_group.get("athletes", []):
                athlete = athlete_entry.get("athlete", {})
                player_id = athlete.get("id")
                full_name = athlete.get("fullName") or athlete.get("displayName")
                if not player_id or not full_name:
                    continue
                if athlete_entry.get("didNotPlay"):
                    continue
                stat_values = _parse_athlete_stats(names, athlete_entry)
                three_pt_made = 0
                if "3PT" in stat_values and "-" in str(stat_values["3PT"]):
                    three_pt_made = int(str(stat_values["3PT"]).split("-")[0] or 0)
                rows.append({
                    "player_id": str(player_id),
                    "player_display_name": full_name,
                    "sort_key": sort_key,
                    "PTS": int(stat_values.get("PTS", 0) or 0),
                    "REB": int(stat_values.get("REB", 0) or 0),
                    "AST": int(stat_values.get("AST", 0) or 0),
                    "BLK": int(stat_values.get("BLK", 0) or 0),
                    "3PM": three_pt_made,
                })
    return rows


def fetch_nba_espn_season_stats(season: int) -> pd.DataFrame:
    """UNVERIFIED against a real live payload -- see module docstring. Same
    real cost/shape as soccer.py's fetch_soccer_espn_season_stats(): walks
    the season's completed-game scoreboard month by month, then each game's
    own summary endpoint for real per-player box-score rows."""
    events = _fetch_completed_events(season)
    rows: list[dict] = []
    for game_index, (event_id, _iso_date) in enumerate(events, start=1):
        rows.extend(_fetch_event_player_rows(event_id, game_index))
    return pd.DataFrame(rows)


NBA_PLUGIN = SportPlugin(
    name="nba",
    sport_labels=NBA_SPORT_LABELS,
    fetch_stats=fetch_nba_espn_season_stats,
    stat_type_map=NBA_STAT_TYPE_MAP,
    composite_stat_types=NBA_COMPOSITE_STAT_TYPES,
)
