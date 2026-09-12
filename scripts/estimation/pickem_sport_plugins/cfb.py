"""
Session 2.16 -- CFB plug-in. Built offline-first (no key yet), then
LIVE-VERIFIED 2026-09-12 once the user obtained a real free CFBD key --
see ROADMAP.md's Session 2.16 card and SESSION_LOG.md for the full trail.
Real 2025 season pull: 22,583 player-game rows, 4,431 unique players, in 3
real HTTP calls once the season-completion index was cached (21.7s / a
handful of calls for the full first-time backfill). A real, live CFB slice
of ingested props (8,639 rows) was run through `process_props()` end-to-
end: 2,164 real props resolved to `model_status="estimated"`.

WHY CFBD, AND WHY THIS IS DIFFERENT FROM EVERY PRIOR SPORT
------------------------------------------------------------
Every prior plug-in (nflverse, MLB Stats API, ESPN for soccer/EPL/NBA) is
free with no account. College Football Data (collegefootballdata.com,
"CFBD") is the only real, current free source for CFB player game logs
(per docs/research/sport_inventory.md, Session 2.10) but requires a free
API key AND caps the free tier at 1,000 calls/month. That cap is a real
design constraint, not a detail to handle later -- see the caching strategy
below, named explicitly per this session's own roadmap card requirement
("batch/cache strategy named explicitly, not discovered after hitting the
limit").

CALL-BUDGET PLAN (stated up front, per the roadmap card's validation
requirement -- to be confirmed against CFBD's own usage dashboard after a
real week of running, not assumed from this doc alone)
------------------------------------------------------------------------
CFBD's `/games/players` endpoint returns EVERY game's player box score for
a given (year, week, seasonType) in ONE call -- not one call per game or
per player. A full FBS regular season is ~15 weeks; postseason adds a
handful more. That means a full season backfill costs on the order of
15-20 calls total, not one per game (~800+ FBS games/season) or per player
(thousands). This plug-in caches each week's response to disk
(`data/pickem/cache/cfbd/{season}_{seasonType}_wk{week}.json`) the first
time it is fetched:
  - A week whose games are ALL "final" gets cached with `_final: true` and
    is NEVER re-fetched again -- its real result cannot change.
  - A week with any in-progress/upcoming game is cached with `_final:
    false` and IS re-fetched on the next run (stats still developing).
This means steady-state cost is roughly one call per not-yet-final week
per hourly pipeline run (worst case ~24 calls/day while exactly one week is
live), not 15 calls repeated every hour for the whole season. Combined with
the one-time ~15-20 call full-season backfill, this stays well under the
1,000/month cap in normal operation.

LIVE-VERIFIED 2026-09-12: a real key confirmed a real, previously-unknown
gap in the original design -- `/games/players` rows carry NO `status`/
`completed` field of their own (only `id` and `teams`), so the original
"cache each week, mark final from that same payload" plan would have
silently never marked anything final. Fixed by adding one extra real call
per season per seasonType, to the DIFFERENT `/games` endpoint (which does
carry a real per-game `completed` boolean and returns an entire season —
888 real FBS games, weeks 1-16 — in one call with no `week` param), cached
the same way and skipped once every game in it is completed. A real
end-to-end timed run of the full 2025 season, cold cache: 21.7s. Re-run
with a warm cache: 3 real HTTP calls total (postseason weeks not yet
final), 1.6s, 22,583 rows, matching the cold-cache row count exactly. This
was the one required check CFBD's own dashboard would otherwise have had
to surface after the fact — confirmed directly with a real key instead.
Real CFBD usage-dashboard confirmation of steady-state monthly volume is
still owed (see Session 2.16's own re-opening checklist), since a full
season only just ran once, but the calls-per-run math above is now backed
by a real measurement, not just a plan.

STAT-TYPE COVERAGE -- REAL STRINGS, LIVE-VERIFIED 2026-09-12
---------------------------------------------------------------------
Real CFB `stat_type` strings pulled directly from the most recent real
ingested snapshot carrying CFB rows (`data/pickem/normalized/
pickem_props_20260912T100543Z.csv`, 8,639 real CFB rows, both platforms --
`latest.csv` itself has zero CFB rows right now, a real calendar gap
between game days, not a missing-support gap, same as ROADMAP.md's Session
2.10 note on CFB/Tennis volume). Full real counts:
Rec Yards 1012, Player TDs 966, Rush Yards 705, Recs 640, Rush + Rec TDs
450, Pass Yards 405, Rec TDs 280, Pass TDs 227, Receiving Yards 207, Pass
Attempts 202, Longest Rush 197, Longest Reception 194, Longest Rec 188,
Receptions 178, Rush Atts 155, Pass Comp 149, Rush TDs 134, Pass+Rush Yds
133, 1H Receiving TDs 121, 1Q Receptions 120, 1H Receptions 120, Fantasy
Score 118, 1H Receiving Yards 116, Longest Completion 95, 1H Rush TDs 95,
Fantasy Points 93, Kicking Points 76, FG Made 74, Rush+Rec Yds 71, Rush
Attempts 69, 1H Rush Yards 61, 1Q Receiving Yards 59, 1Q Rush TDs 56, 1Q
Receiving TDs 55, INT 48, INTs Thrown 48, 1Q Rush Yards 45, Pass + Rush
Yards 43, Completions 40, XP Made 35, 1H Pass Yards 34, 1H Pass TDs 34, 1Q
Pass Yards 32, 1Q Pass TDs 32, 1H Rush + Rec Yards 27, PAT Made 25, 1Q Rush
+ Rec Yards 25, Total TDs 18, Pass Yards (Combo) 12, Rush Yards (Combo) 6,
Receiving Yards (Combo) 6.

Mapped against CFBD's REAL `/games/players` payload (a real week-1 2025
game confirmed directly, 2026-09-12): categories "passing"/"rushing"/
"receiving"/"kicking"/"defensive"/"kickReturns"/"puntReturns"/"punting",
each with named `types`. Two real corrections to the original
documentation-only assumption:
  - Passing's `C/ATT` AND kicking's `FG`/`XP` are ALL real "made/attempted"
    combined strings (e.g. "20/29", "1/1", "4/4"), not plain numbers —
    `_made_count()`/the same split-logic path handles all three.
  - Passing has NO `LONG` type at all (only C/ATT, YDS, AVG, TD, INT,
    QBR) — unlike rushing/receiving, which both do. `longest completion`
    (95 real rows) is therefore a REAL, CONFIRMED gap, not guessed: CFBD
    simply doesn't carry this number for passing plays.

LEFT UNSUPPORTED, real stated gaps, same "don't guess" standard as every
prior sport:
  - `Longest Completion` (95 real rows) — see above; CFBD's real passing
    category has no LONG type.
  - Every `1Q ___` / `1H ___` stat (45 real rows across all listed
    variants above) -- CFBD's player-game endpoint is a full-GAME box
    score only, no quarter/half split (confirmed on the real payload — no
    per-quarter breakdown anywhere in it). Same "real architecture
    mismatch" as MLB's per-inning gap (Session 2.13).
  - `Fantasy Score` / `Fantasy Points` -- no official PrizePicks/Underdog
    CFB scoring formula could be sourced; guessing a formula here (as
    opposed to a documented platform rule, unlike NFL's real Kicking
    Points/Fantasy Score) would be presenting an assumption as a real
    number.
  - `Kicking Points` -- CFBD's real kicking category (confirmed on the
    live payload: FG, PCT, LONG, XP, PTS) has no distance-tiered FG
    breakdown (unlike NFL's nflverse `fg_made_40_49` etc.), so NFL's real
    tiered formula (Session 2.3) cannot be ported as-is.
  - `___ (Combo)` variants (Pass/Rush/Receiving Yards (Combo), 24 real
    rows) -- meaning not confirmed (NFL's own data has no equivalent
    "(Combo)" suffix to cross-check against); left unsupported rather than
    guessed.

Everything else below maps to a single, real, confirmed CFBD column or a
same-shape composite sum, same pattern as `nfl.py`/`mlb.py`. Real
end-to-end proof: running `process_props()` against the real 8,639-row CFB
slice above with live 2025 season stats produced 2,164 real rows with
`model_status="estimated"` (e.g. Arch Manning's real "Pass Yards" line
247.5, Jordan Marshall's real "Rush Atts" line 13.5).
"""

from __future__ import annotations

import json
import logging
import os
from pathlib import Path
from typing import Callable

import pandas as pd

from . import SportPlugin
from .http_utils import get_json_with_retries

log = logging.getLogger("pickem_model")

CFBD_API_BASE = "https://api.collegefootballdata.com"
CFBD_API_KEY_ENV_VAR = "CFBD_API_KEY"

CACHE_DIR = Path("data/pickem/cache/cfbd")

CFB_SPORT_LABELS = frozenset({"cfb", "college football", "ncaaf"})

# Regular season is 15 weeks in a normal CFBD year; postseason is fetched
# separately as its own seasonType. Kept as a constant, not hardcoded
# inline, so a future season-length change (rare, but has happened) is a
# one-line fix.
REGULAR_SEASON_WEEKS = 15

# ---------------------------------------------------------------------------
# Stat-type map -- see module docstring's "STAT-TYPE COVERAGE" section for
# the real string counts and CFBD source. Column names below are this
# plug-in's own flat per-player-per-game schema (assigned when parsing
# CFBD's nested category/type payload in _flatten_game_players() below),
# not CFBD's raw field names directly.
# ---------------------------------------------------------------------------
CFB_STAT_TYPE_MAP: dict[str, str] = {
    "pass yards": "pass_yds",
    "passing yards": "pass_yds",
    "pass tds": "pass_td",
    "pass attempts": "pass_att",
    "pass comp": "pass_comp",
    "completions": "pass_comp",
    "int": "pass_int",
    "ints thrown": "pass_int",
    # "longest completion" (95 real rows) has NO mapping -- LIVE-VERIFIED
    # 2026-09-12: CFBD's real passing category only carries C/ATT, YDS,
    # AVG, TD, INT, QBR types -- no LONG, unlike rushing/receiving which
    # both have one. A real, confirmed CFBD data gap, not an oversight.
    "rush yards": "rush_yds",
    "rush tds": "rush_td",
    "rush atts": "rush_att",
    "rush attempts": "rush_att",
    "longest rush": "rush_long",
    "rec yards": "rec_yds",
    "receiving yards": "rec_yds",
    "rec tds": "rec_td",
    "recs": "rec",
    "receptions": "rec",
    "longest rec": "rec_long",
    "longest reception": "rec_long",
    "fg made": "kick_fgm",
    "xp made": "kick_xpm",
    "pat made": "kick_xpm",  # real Underdog wording, same real-world event as an XP
}

CFB_COMPOSITE_STAT_TYPES: dict[str, list[str]] = {
    "player tds": ["pass_td", "rush_td", "rec_td"],
    "total tds": ["pass_td", "rush_td", "rec_td"],  # same real-world event as "Player TDs"
    "rush + rec tds": ["rush_td", "rec_td"],
    "pass+rush yds": ["pass_yds", "rush_yds"],
    "rush+rec yds": ["rush_yds", "rec_yds"],
    "rush + rec yards": ["rush_yds", "rec_yds"],
    "pass + rush yards": ["pass_yds", "rush_yds"],
}


# ---------------------------------------------------------------------------
# Fetch -- CFBD's /games/players endpoint returns every game's player box
# score for one (year, week, seasonType) in a single call. Parsing shape
# below follows CFBD's own published API docs (collegefootballdata.com/
# api/docs) -- NOT YET CHECKED against a real payload, since no key exists
# yet (see module docstring). If the real response nests differently once
# a key is obtained, this is the function to fix.
# ---------------------------------------------------------------------------
def _cfbd_headers() -> dict[str, str] | None:
    key = os.environ.get(CFBD_API_KEY_ENV_VAR)
    if not key:
        return None
    return {"Authorization": f"Bearer {key}"}


def _week_cache_path(season: int, season_type: str, week: int) -> Path:
    return CACHE_DIR / f"{season}_{season_type}_wk{week}.json"


def _games_index_cache_path(season: int, season_type: str) -> Path:
    return CACHE_DIR / f"{season}_{season_type}_games_index.json"


def _fetch_completed_weeks(season: int, season_type: str) -> set[int]:
    """LIVE-VERIFIED 2026-09-12 (real key): `/games/players` rows carry NO
    `status`/`completed` field of their own -- the original design here
    assumed one, which would have silently disabled the whole caching
    scheme (every week would look "not final" forever, defeating the
    call-budget plan). `/games` (a DIFFERENT, plain-games endpoint) DOES
    carry a real `completed: true/false` per game, and returns an ENTIRE
    season in one call when no `week` param is given (confirmed live:
    year=2025, seasonType=regular -> 888 games, weeks 1-16, one call).
    This function is that one extra call, cached the same way as a
    player-stats week: skipped entirely once every game in the cached
    index is already completed, so a full season costs exactly one of
    these calls total once finished, not one per week."""
    path = _games_index_cache_path(season, season_type)
    if path.exists():
        try:
            cached = json.loads(path.read_text())
            if cached.get("_all_completed"):
                return set(cached["completed_weeks"])
        except (json.JSONDecodeError, OSError) as exc:
            log.warning("Discarding unreadable CFBD games-index cache %s: %s", path, exc)

    headers = _cfbd_headers()
    if headers is None:
        return set()

    url = f"{CFBD_API_BASE}/games?year={season}&seasonType={season_type}&classification=fbs"
    try:
        games = get_json_with_retries(url, headers=headers, timeout=20)
    except Exception as exc:  # noqa: BLE001
        log.warning("Could not fetch CFBD games index for %s %s: %s", season, season_type, exc)
        return set()

    weeks_seen = sorted({g["week"] for g in games})
    completed_weeks = {
        w for w in weeks_seen
        if all(g["completed"] for g in games if g["week"] == w)
    }
    all_completed = bool(games) and all(g["completed"] for g in games)
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({
        "_all_completed": all_completed,
        "completed_weeks": sorted(completed_weeks),
    }))
    return completed_weeks


def _load_cached_week(season: int, season_type: str, week: int) -> list[dict] | None:
    path = _week_cache_path(season, season_type, week)
    if not path.exists():
        return None
    try:
        payload = json.loads(path.read_text())
    except (json.JSONDecodeError, OSError) as exc:
        log.warning("Discarding unreadable CFBD cache file %s: %s", path, exc)
        return None
    if payload.get("_final"):
        return payload["games"]
    return None  # not final -- caller re-fetches


def _save_cached_week(season: int, season_type: str, week: int, games: list[dict], is_final: bool) -> None:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    path = _week_cache_path(season, season_type, week)
    path.write_text(json.dumps({"_final": is_final, "games": games}))


def _fetch_week_player_stats(season: int, season_type: str, week: int, completed_weeks: set[int]) -> list[dict]:
    """One real CFBD call per not-yet-final (season, seasonType, week) --
    see module docstring's call-budget plan. Fault-isolated the same way as
    every other plug-in's per-item HTTP calls (Hotfix, 2026-09-12): a
    failure after retries logs a warning and returns no games for this one
    week rather than aborting the whole plug-in."""
    cached = _load_cached_week(season, season_type, week)
    if cached is not None:
        return cached

    headers = _cfbd_headers()
    if headers is None:
        log.warning(
            "%s not set -- CFB plug-in has no real key yet, returning no "
            "data (see ROADMAP.md Session 2.16).",
            CFBD_API_KEY_ENV_VAR,
        )
        return []

    url = (
        f"{CFBD_API_BASE}/games/players"
        f"?year={season}&week={week}&seasonType={season_type}&classification=fbs"
    )
    try:
        games = get_json_with_retries(url, headers=headers, timeout=20)
    except Exception as exc:  # noqa: BLE001
        log.warning(
            "Skipping CFB %s %s week %s after repeated failures: %s",
            season, season_type, week, exc,
        )
        return []

    _save_cached_week(season, season_type, week, games, is_final=week in completed_weeks)
    return games


def _stat_value(athlete_stat: str) -> float:
    """A plain numeric stat -- never expected to contain a "/" (the "C/ATT"
    combined completions/attempts string, and kicking's "M/ATT"-style "FG"/
    "XP" strings, are each split by dedicated handling elsewhere before
    reaching this function). Falls back to 0.0 for an unparseable value
    rather than raising, consistent with every other plug-in's use of
    `.get(..., 0)` for a missing stat."""
    try:
        return float(athlete_stat)
    except (TypeError, ValueError):
        return 0.0


def _made_count(made_over_attempted: str) -> float:
    """LIVE-VERIFIED 2026-09-12 (real key, real week-1 2025 payload):
    kicking's "FG" and "XP" types both carry a "made/attempted" string
    (e.g. "1/1", "4/4"), the same combined shape as passing's "C/ATT" --
    NOT a plain number, contrary to this plug-in's original (pre-key)
    assumption. Only the made count (the first number) is a real per-game
    quantity a pick'em prop ever asks about (FG Made / XP Made / PAT
    Made -- see stat-type map above); attempts are discarded here."""
    made_str = str(made_over_attempted).split("/", 1)[0]
    return _stat_value(made_str)


def _flatten_game_players(games: list[dict]) -> list[dict]:
    """Reshapes CFBD's nested game -> team -> category -> type -> athletes
    payload into one flat row per (player, game). LIVE-VERIFIED 2026-09-12
    against a real week-1 2025 `/games/players` payload (real key) -- see
    module docstring's "Mapped, UNVERIFIED" note, now resolved. Each real
    `game` dict is expected to carry an injected `_sort_key` (the calling
    week number, see fetch_cfb_season_stats() below) so a player's rows
    sort chronologically by week, not by CFBD's non-sequential internal
    game id."""
    # player_id -> row dict, keyed per game via a composite key so the same
    # player's rows across different games never collide.
    rows_by_key: dict[tuple, dict] = {}

    category_type_column = {
        ("passing", "YDS"): "pass_yds",
        ("passing", "TD"): "pass_td",
        ("passing", "INT"): "pass_int",
        ("rushing", "CAR"): "rush_att",
        ("rushing", "YDS"): "rush_yds",
        ("rushing", "TD"): "rush_td",
        ("rushing", "LONG"): "rush_long",
        ("receiving", "REC"): "rec",
        ("receiving", "YDS"): "rec_yds",
        ("receiving", "TD"): "rec_td",
        ("receiving", "LONG"): "rec_long",
        # ("kicking", "FG") / ("kicking", "XP") are handled separately below
        # -- both are real "made/attempted" strings, not plain numbers.
    }

    for game in games:
        game_id = game.get("id")
        sort_key = game.get("_sort_key", game_id)
        for team in game.get("teams", []):
            for category in team.get("categories", []):
                cat_name = category.get("name")
                for stat_type in category.get("types", []):
                    type_name = stat_type.get("name")

                    # "C/ATT" (passing) and "FG"/"XP" (kicking) are all
                    # real "made/attempted"-style combined strings (e.g.
                    # "20/29", "1/1", "4/4") -- LIVE-VERIFIED 2026-09-12,
                    # NOT plain numbers as originally assumed for FG/XP.
                    # Handled here, split out, before the plain-numeric
                    # path below (which would otherwise coerce them to 0.0
                    # via _stat_value's "/"-triggered fallback).
                    made_attempted_column = {
                        ("passing", "C/ATT"): ("pass_comp", "pass_att"),
                        ("kicking", "FG"): ("kick_fgm", None),
                        ("kicking", "XP"): ("kick_xpm", None),
                    }.get((cat_name, type_name))
                    if made_attempted_column is not None:
                        made_col, att_col = made_attempted_column
                        for athlete in stat_type.get("athletes", []):
                            player_id = athlete.get("id")
                            full_name = athlete.get("name")
                            raw = athlete.get("stat") or ""
                            if player_id is None or not full_name or "/" not in raw:
                                continue
                            made_str, att_str = raw.split("/", 1)
                            key = (game_id, player_id)
                            row = rows_by_key.setdefault(key, {
                                "player_id": str(player_id),
                                "player_display_name": full_name,
                                "sort_key": sort_key,
                            })
                            row[made_col] = _stat_value(made_str)
                            if att_col is not None:
                                row[att_col] = _stat_value(att_str)
                        continue

                    column = category_type_column.get((cat_name, type_name))
                    if column is None:
                        continue
                    for athlete in stat_type.get("athletes", []):
                        player_id = athlete.get("id")
                        full_name = athlete.get("name")
                        if player_id is None or not full_name:
                            continue
                        key = (game_id, player_id)
                        row = rows_by_key.setdefault(key, {
                            "player_id": str(player_id),
                            "player_display_name": full_name,
                            "sort_key": sort_key,
                        })
                        row[column] = _stat_value(athlete.get("stat"))

    return list(rows_by_key.values())


def fetch_cfb_season_stats(season: int) -> pd.DataFrame:
    """Full real season pull: every regular-season week plus postseason,
    each via one cached/real CFBD `/games/players` call (see module
    docstring's call-budget plan). Returns an empty DataFrame -- the same
    honest "no data yet" shape Session 2.15 established for NBA's
    pre-season case -- if no CFBD_API_KEY is set."""
    if _cfbd_headers() is None:
        return pd.DataFrame([])

    completed_weeks = _fetch_completed_weeks(season, "regular")
    all_games: list[dict] = []
    for week in range(1, REGULAR_SEASON_WEEKS + 1):
        for game in _fetch_week_player_stats(season, "regular", week, completed_weeks):
            game["_sort_key"] = week
            all_games.append(game)
    # Postseason (bowls + CFP) spans a handful of weeks -- finality tracked
    # separately since it is a distinct CFBD seasonType from "regular".
    postseason_completed = _fetch_completed_weeks(season, "postseason")
    for week in range(1, 5):
        for game in _fetch_week_player_stats(season, "postseason", week, postseason_completed):
            game["_sort_key"] = REGULAR_SEASON_WEEKS + week
            all_games.append(game)

    rows = _flatten_game_players(all_games)
    return pd.DataFrame(rows)


CFB_PLUGIN = SportPlugin(
    name="cfb",
    sport_labels=CFB_SPORT_LABELS,
    fetch_stats=fetch_cfb_season_stats,
    stat_type_map=CFB_STAT_TYPE_MAP,
    composite_stat_types=CFB_COMPOSITE_STAT_TYPES,
)
