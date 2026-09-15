"""
Session 2.12 -- MLB plug-in scaffold (proof case, small unverified stat map).
Session 2.13 -- real MLB coverage: this session's own job, per its roadmap
card ("confirm the real ingested strings directly, don't guess the list in
advance, same rule Session 2.3 followed for NFL"). Everything below the
"SESSION 2.13" marker is new or rewritten; the module-level shape (fetch
roster -> per-player game log -> SportPlugin) is unchanged from 2.12.

HOTFIX (2026-09-12): a real GitHub Actions pipeline failure (an unhandled
timeout from ONE HTTP call inside pickem_sport_plugins/soccer.py's
per-match loop aborted the entire pipeline run, every sport, not just
soccer) surfaced that this file's per-team/per-player HTTP calls had the
identical unprotected shape. Both now retry via http_utils.get_json_
with_retries() and, on repeated failure, skip just that one team/player
rather than raising -- see _fetch_active_roster()/_fetch_player_game_log()'s
own docstrings below.

SESSION 2.13 -- WHAT CHANGED AND WHY
-------------------------------------
Session 2.12 shipped real, working fetch code but a deliberately small,
UNVERIFIED stat map (hits, home runs, runs, RBIs, strikeouts, total bases,
walks) -- explicitly not checked against real ingested MLB `stat_type`
strings. This session did that check for real:

1. Ran a live production ingestion pull (scripts/ingestion/ingest_pickem.py,
   2026-09-11) -- 57,628 real rows, 11,142 of them real MLB props (plus a
   separate 1,428-row MLBLIVE category -- see "MLBLIVE" note below).
2. Counted every real MLB `stat_type` string from both platforms, with real
   counts, before mapping anything (same discipline as
   pickem_estimation_model_spec.md's NFL "Stat-type coverage" section).
3. Confirmed each one against a real, live MLB Stats API response --
   pulled Aaron Judge's (id 592450) real hitting game log and Gerrit Cole's
   (id 543037) real pitching game log directly, and checked every column
   name used below exists on those real payloads before writing it into
   either map.

HITTING VS. PITCHING -- WHY THIS PLUG-IN NOW FETCHES TWO GAME LOGS
---------------------------------------------------------------------
Real MLB props split cleanly into hitter stats (Hits, Home Runs, Total
Bases, ...) and pitcher stats (Hits Allowed, Earned Runs Allowed, Ks, ...).
MLB Stats API's hitting and pitching game logs are two separate endpoints
with two separate stat vocabularies that happen to share some names (both
have a `hits`/`strikeOuts` concept, but "hits" a hitter GOT and "hits" a
pitcher ALLOWED are different real-world things). Every pitching-group
column below is prefixed `p_` for exactly this reason -- so a pitcher's
"hits allowed" can never be silently summed with a hitter's own "hits".
fetch_mlb_season_stats() below reads each active-roster player's real MLB
Stats API `position.type` (confirmed live: "Pitcher", "Two-Way Player", or
a real position like "Outfielder"/"Catcher"/etc.) to decide which log(s) to
pull -- a two-way player (confirmed live: Shohei Ohtani, position.type
"Two-Way Player") gets both, appended as two separate row sets under the
same player_id, exactly like a normal player would only ever produce one.

STAT-TYPE COVERAGE -- CONFIRMED, MAPPED, AND STATED GAPS
-------------------------------------------------------------
See docs/research/pickem_estimation_model_spec.md's new "MLB stat-type
coverage" section (Session 2.13 addendum) for the full real-stat_type-string
table with counts and per-string outcome. Summary:
  - Mapped (single column): hits, home runs, runs, rbis, walks (batter walks
    included), doubles, triples, singles* (computed), stolen bases, plate
    appearances, total bases, hitter Ks / batter strikeouts, pitches seen*
    (hitting numberOfPitches, aliased to avoid the pitching-side name clash)
  - Mapped (composite, summed): Hits+Runs+RBIs (both platforms' real
    spellings)
  - Mapped (pitching, `p_`-prefixed): hits allowed, earned runs allowed,
    walks allowed, Ks/strikeouts (pitcher), pitching outs / PO, batters
    faced, pitches thrown, strikes thrown, balls thrown* (computed)
  - Mapped (computed formula, PrizePicks' own official scoring, confirmed
    live via prizepicks.com/playbook-article/how-to-play-prizepicks-mlb-
    fantasy-scoring-system): Hitter FS, Pitcher FS
  - LEFT UNSUPPORTED, real stated gaps (not guessed at):
    - `Strikes Counted` / `Balls Counted` (PrizePicks, hitter-side pitch
      count breakdown) -- MLB Stats API's hitting game log carries a total
      `numberOfPitches` (mapped as "pitches seen") but no ball/strike split
      of a batter's own plate appearances; that split does not exist in
      this endpoint.
    - Underdog `Fantasy Points` -- no official Underdog MLB scoring formula
      could be sourced (underdogfantasy.com/underdogsports.com's rules
      pages 301-redirect to a JS app that returns 403 to an unauthenticated
      fetch; unlike PrizePicks' formula, this one is not confirmable right
      now). Guessing a formula here would mean presenting an assumption as
      a real number -- left unsupported instead, same standard NFL's
      Fantasy Score gap already set.
    - Every `1st Inn. ___` / `1-3 Inn. ___` / `1-5 Inn. ___` stat (both
      platforms, real, mostly under the separate MLBLIVE sport label --
      see below) -- these need per-inning splits, which MLB Stats API's
      season game log does not carry (it is per-GAME totals only). This is
      a real architecture mismatch, not a missing mapping: the season_avg/
      recent_form model in pickem_model.py is built around one number per
      game, and an inning-level prop has no such per-game number to
      average.

MLBLIVE -- A SEPARATE, DELIBERATELY UNREGISTERED SPORT LABEL
-------------------------------------------------------------
Real ingested data (2026-09-11 pull) carries `MLB` (11,142 rows, pre-game
props -- what this plug-in supports) and `MLBLIVE` (1,428 rows) as two
DIFFERENT `sport` strings. Checked directly: every single real MLBLIVE
stat_type is inning-specific (`1st Inn. Pitches Seen`, `1-3 Inn. HRR`,
`3rd Inn. Balls Counted`, etc.) -- the exact same "no per-game number"
mismatch described above, for 100% of that category, not just some of it.
MLB_SPORT_LABELS below deliberately does NOT include "mlblive", so these
rows keep reporting model_status="unsupported_sport" -- an honest, correct
result (this plug-in genuinely does not support them), not a bug to fix
later.

FETCH_STATS -- ONE HTTP CALL PER PLAYER, NOT A BULK PULL (unchanged from
Session 2.12 -- see original note, carried forward)
-----------------------------------------------------------------------
Unlike nflverse's single parquet file for an entire season, MLB Stats API
has no equivalent single bulk "every player's season game log" endpoint.
fetch_mlb_season_stats() below walks all 30 teams' active rosters, then
pulls each player's own season game log (hitting, pitching, or both --
see above) individually. This means hundreds of real HTTP calls per
production run -- an accepted, real cost of this data source (there is no
bulk alternative), same as Session 2.12 already documented. Team IDs are
MLB Stats API's own stable numeric team IDs.
"""

from __future__ import annotations

import re
from typing import Callable, Optional

import logging

import pandas as pd

from . import SportPlugin
from .http_utils import get_json_with_retries

log = logging.getLogger("pickem_model")

MLB_STATS_API_BASE = "https://statsapi.mlb.com/api/v1"
MLB_STATS_API_BASE_V1_1 = "https://statsapi.mlb.com/api/v1.1"

# Deliberately excludes "mlblive" -- see module docstring's "MLBLIVE" note.
MLB_SPORT_LABELS = frozenset({"mlb", "baseball"})

# All 30 MLB Stats API team IDs (stable, official).
MLB_TEAM_IDS = [
    108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121,
    133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146,
    147, 158,
]

# SESSION 2.32 -- real team_id -> real "teamName" (MLB Stats API's own
# nickname field, e.g. "Yankees", NOT the abbreviation and NOT the full
# "New York Yankees" name), confirmed live 2026-09-15 via a real
# GET /v1/teams?sportId=1 pull. The schedule endpoint's own
# teams.{away,home}.team object does not carry this field directly (only
# id/name/link), so it is hardcoded here rather than re-fetched on every
# schedule call -- same "stable, official, hardcode it" standard MLB_TEAM_
# IDS above already uses. Used by find_scheduled_game() below to match
# Underdog's real "Away @ Home" nickname wording (e.g. "Mets @ Yankees",
# "Rangers @ D'Backs") against a real scheduled game.
MLB_TEAM_ID_TO_NICKNAME: dict[int, str] = {
    133: "Athletics", 134: "Pirates", 135: "Padres", 136: "Mariners",
    137: "Giants", 138: "Cardinals", 139: "Rays", 140: "Rangers",
    141: "Blue Jays", 142: "Twins", 143: "Phillies", 144: "Braves",
    145: "White Sox", 146: "Marlins", 147: "Yankees", 158: "Brewers",
    108: "Angels", 109: "D-backs", 110: "Orioles", 111: "Red Sox",
    112: "Cubs", 113: "Reds", 114: "Guardians", 115: "Rockies",
    116: "Tigers", 117: "Astros", 118: "Royals", 119: "Dodgers",
    120: "Nationals", 121: "Mets",
}

# ---------------------------------------------------------------------------
# Stat-type map -- confirmed 2026-09-11 against real ingested PrizePicks/
# Underdog `stat_type` strings (see docs/research/pickem_estimation_model_
# spec.md's "MLB stat-type coverage" section for the full table with real
# counts) AND against real, live MLB Stats API columns (Aaron Judge's real
# hitting game log, Gerrit Cole's real pitching game log). Hitting columns
# use MLB Stats API's own names unprefixed; pitching columns are prefixed
# `p_` at fetch time (see module docstring) to keep the two vocabularies
# from ever colliding.
# ---------------------------------------------------------------------------
MLB_STAT_TYPE_MAP: dict[str, str] = {
    # --- Hitting ---
    "hits": "hits",
    "home runs": "homeRuns",
    "runs": "runs",
    "rbis": "rbi",
    "walks": "baseOnBalls",
    "batter walks": "baseOnBalls",  # real Underdog wording
    "doubles": "doubles",
    "triples": "triples",
    "sb": "stolenBases",
    "stolen bases": "stolenBases",  # real Underdog wording
    "plate appearances": "plateAppearances",
    "tb": "totalBases",
    "total bases": "totalBases",  # real Underdog wording
    "hitter ks": "strikeOuts",
    "batter strikeouts": "strikeOuts",  # real Underdog wording
    "pitches seen": "numberOfPitchesSeen",  # a BATTER'S pitches seen, aliased
    # from hitting's own "numberOfPitches" field at fetch time -- see fetch
    # function below -- to avoid colliding with the pitching side's own
    # "pitches thrown" (p_numberOfPitches).
    # --- Pitching (real Underdog "Strikeouts"/"Pitching Outs"/etc. are
    # pitcher-side stats -- confirmed by their real row counts all matching
    # each other, e.g. 28 each, within one real pitcher-props batch) ---
    "hits allowed": "p_hits",
    "earned runs allowed": "p_earnedRuns",
    "walks allowed": "p_baseOnBalls",
    "ks": "p_strikeOuts",
    "strikeouts": "p_strikeOuts",  # real Underdog wording (pitcher Ks)
    "po": "p_outs",
    "pitching outs": "p_outs",  # real Underdog wording
    "batters faced": "p_battersFaced",
    "pitches thrown": "p_numberOfPitches",
    "strikes thrown": "p_strikes",
}

MLB_COMPOSITE_STAT_TYPES: dict[str, list[str]] = {
    "hits+runs+rbis": ["hits", "runs", "rbi"],  # real PrizePicks wording
    "hits + runs + rbis": ["hits", "runs", "rbi"],  # real Underdog wording
}


# ---------------------------------------------------------------------------
# Computed stat types -- a real formula/derivation across more than one raw
# column, same shape as NFL's Kicking Points / Fantasy Score
# (pickem_sport_plugins/nfl.py). Every column each one reads was confirmed
# to exist on a real MLB Stats API response before being used here.
# ---------------------------------------------------------------------------
def _compute_singles(games: pd.DataFrame) -> pd.Series:
    """A single is a hit that isn't a double, triple, or home run -- MLB
    Stats API has no direct "singles" column on either game log, so this is
    derived, not assumed. Real PrizePicks stat_type "Singles" (366 rows,
    2026-09-11 pull)."""
    return (
        games["hits"] - games["doubles"] - games["triples"] - games["homeRuns"]
    ).reset_index(drop=True)


def _compute_balls_thrown(games: pd.DataFrame) -> pd.Series:
    """A pitcher's total pitches minus the strikes among them -- MLB Stats
    API's pitching game log has no direct "balls thrown" column. Real
    PrizePicks stat_type "Balls Thrown" (18 rows, 2026-09-11 pull)."""
    return (games["p_numberOfPitches"] - games["p_strikes"]).reset_index(drop=True)


def _compute_hitter_fs(games: pd.DataFrame) -> pd.Series:
    """PrizePicks' official Hitter Fantasy Score formula (confirmed live,
    2026-09-11, via prizepicks.com/playbook-article/how-to-play-prizepicks-
    mlb-fantasy-scoring-system): Single=3, Double=5, Triple=8, Home Run=10,
    Run=2, RBI=2, Walk=2, Hit By Pitch=2, Stolen Base=5. Real PrizePicks
    stat_type "Hitter FS" (739 rows, 2026-09-11 pull)."""
    singles = _compute_singles(games)
    return (
        singles * 3
        + games["doubles"].reset_index(drop=True) * 5
        + games["triples"].reset_index(drop=True) * 8
        + games["homeRuns"].reset_index(drop=True) * 10
        + games["runs"].reset_index(drop=True) * 2
        + games["rbi"].reset_index(drop=True) * 2
        + games["baseOnBalls"].reset_index(drop=True) * 2
        + games["hitByPitch"].reset_index(drop=True) * 2
        + games["stolenBases"].reset_index(drop=True) * 5
    )


def _compute_pitcher_fs(games: pd.DataFrame) -> pd.Series:
    """PrizePicks' official Pitcher Fantasy Score formula (confirmed live,
    2026-09-11, same source as Hitter FS above): Win=6, Quality Start=4,
    Earned Run=-3, Strikeout=3, Out=1. "Win" is MLB Stats API's own real
    per-game `wins` field (0/1), not derived. "Quality Start" (a real MLB
    rule: at least 6 innings pitched AND 3 or fewer earned runs) is derived
    from `p_outs` (>=18, i.e. 6 full innings -- using the real outs count
    instead of parsing MLB's own "X.Y" innings-pitched STRING, where .1/.2
    mean partial-inning outs, not decimal tenths, per MLB Stats API's own
    documented format) and `p_earnedRuns` (<=3). Real PrizePicks stat_type
    "Pitcher FS" (66 rows, 2026-09-11 pull)."""
    quality_start = (
        (games["p_outs"] >= 18) & (games["p_earnedRuns"] <= 3)
    ).astype(int).reset_index(drop=True)
    return (
        games["p_wins"].reset_index(drop=True) * 6
        + quality_start * 4
        - games["p_earnedRuns"].reset_index(drop=True) * 3
        + games["p_strikeOuts"].reset_index(drop=True) * 3
        + games["p_outs"].reset_index(drop=True) * 1
    )


MLB_COMPUTED_STAT_TYPES: dict[str, Callable[[pd.DataFrame], pd.Series]] = {
    "singles": _compute_singles,
    "balls thrown": _compute_balls_thrown,
    "hitter fs": _compute_hitter_fs,
    "pitcher fs": _compute_pitcher_fs,
}

MLB_COMPUTED_REQUIRED_COLUMNS: dict[str, list[str]] = {
    "singles": ["hits", "doubles", "triples", "homeRuns"],
    "balls thrown": ["p_numberOfPitches", "p_strikes"],
    "hitter fs": [
        "hits", "doubles", "triples", "homeRuns", "runs", "rbi",
        "baseOnBalls", "hitByPitch", "stolenBases",
    ],
    "pitcher fs": ["p_wins", "p_outs", "p_earnedRuns", "p_strikeOuts"],
}


# ---------------------------------------------------------------------------
# Fetch
# ---------------------------------------------------------------------------
def _fetch_active_roster(team_id: int) -> list[dict]:
    """HOTFIX (2026-09-12): a per-team call inside fetch_mlb_season_stats()'s
    30-team loop -- same real fault-isolation standard as
    pickem_sport_plugins/soccer.py's per-match calls, applied here after
    that file's own real production incident (an unhandled timeout from
    one HTTP call aborting the ENTIRE pipeline, every sport) surfaced this
    file had the identical unprotected shape. If every retry fails, logs a
    warning and returns no roster for this one team rather than raising."""
    url = f"{MLB_STATS_API_BASE}/teams/{team_id}/roster?rosterType=active"
    try:
        payload = get_json_with_retries(url, timeout=15)
    except Exception as exc:  # noqa: BLE001
        log.warning("Skipping MLB team %s roster after repeated failures: %s", team_id, exc)
        return []
    return payload.get("roster", [])


def _fetch_player_game_log(person_id: int, season: int, group: str) -> list[dict]:
    """Same fault-isolation standard as _fetch_active_roster above -- one
    player's game log failing after retries returns no rows for this one
    player/group rather than aborting the whole plug-in."""
    url = (
        f"{MLB_STATS_API_BASE}/people/{person_id}/stats"
        f"?stats=gameLog&group={group}&season={season}"
    )
    try:
        payload = get_json_with_retries(url, timeout=15)
    except Exception as exc:  # noqa: BLE001
        log.warning(
            "Skipping MLB player %s (%s) game log after repeated failures: %s",
            person_id, group, exc,
        )
        return []
    stats = payload.get("stats", [])
    if not stats:
        return []
    return stats[0].get("splits", [])


def _hitting_rows(person_id: int, full_name: str, season: int) -> list[dict]:
    rows: list[dict] = []
    for game_index, split in enumerate(
        _fetch_player_game_log(person_id, season, "hitting"), start=1
    ):
        stat = split.get("stat", {})
        rows.append({
            "player_id": str(person_id),
            "player_display_name": full_name,
            "sort_key": game_index,
            # Session 2.26: MLB Stats API's own gameLog split already reports
            # this game's real calendar date directly (unlike NFL, which has
            # no such field and needs a separate schedule-file join to find
            # it -- see auto_grade_outcomes.py's GradingAdapter for MLB vs
            # NFL). Carried through here so grading can match a flag to its
            # real game by date alone, with no extra fetch.
            "game_date": split.get("date"),
            "hits": stat.get("hits", 0),
            "homeRuns": stat.get("homeRuns", 0),
            "runs": stat.get("runs", 0),
            "rbi": stat.get("rbi", 0),
            "baseOnBalls": stat.get("baseOnBalls", 0),
            "doubles": stat.get("doubles", 0),
            "triples": stat.get("triples", 0),
            "stolenBases": stat.get("stolenBases", 0),
            "plateAppearances": stat.get("plateAppearances", 0),
            "totalBases": stat.get("totalBases", 0),
            "strikeOuts": stat.get("strikeOuts", 0),
            "hitByPitch": stat.get("hitByPitch", 0),
            "numberOfPitchesSeen": stat.get("numberOfPitches", 0),
        })
    return rows


def _pitching_rows(person_id: int, full_name: str, season: int) -> list[dict]:
    rows: list[dict] = []
    for game_index, split in enumerate(
        _fetch_player_game_log(person_id, season, "pitching"), start=1
    ):
        stat = split.get("stat", {})
        rows.append({
            "player_id": str(person_id),
            "player_display_name": full_name,
            "sort_key": game_index,
            "game_date": split.get("date"),
            "p_hits": stat.get("hits", 0),
            "p_earnedRuns": stat.get("earnedRuns", 0),
            "p_baseOnBalls": stat.get("baseOnBalls", 0),
            "p_strikeOuts": stat.get("strikeOuts", 0),
            "p_outs": stat.get("outs", 0),
            "p_battersFaced": stat.get("battersFaced", 0),
            "p_numberOfPitches": stat.get("numberOfPitches", 0),
            "p_strikes": stat.get("strikes", 0),
            "p_wins": stat.get("wins", 0),
        })
    return rows


def fetch_mlb_season_stats(season: int) -> pd.DataFrame:
    """Real MLB Stats API pull: every active-roster player across all 30
    teams, one season game log each -- hitting, pitching, or both,
    depending on that player's real `position.type` (see module docstring).
    Returns one combined DataFrame; hitting-only and pitching-only rows
    simply carry NaN in the columns the other group uses, which
    pickem_model.py's build_stat_series() already handles (it filters to
    one player_id's own rows before reading any column)."""
    rows: list[dict] = []
    for team_id in MLB_TEAM_IDS:
        for player in _fetch_active_roster(team_id):
            person = player.get("person", {})
            person_id = person.get("id")
            full_name = person.get("fullName")
            if person_id is None or not full_name:
                continue
            position_type = (player.get("position") or {}).get("type")

            if position_type == "Pitcher":
                rows.extend(_pitching_rows(person_id, full_name, season))
            elif position_type == "Two-Way Player":
                rows.extend(_pitching_rows(person_id, full_name, season))
                rows.extend(_hitting_rows(person_id, full_name, season))
            else:
                rows.extend(_hitting_rows(person_id, full_name, season))
    return pd.DataFrame(rows)


# ---------------------------------------------------------------------------
# SESSION 2.32 -- real-time starter/lineup confirmation signal (Underdog
# gate, MLB only). See docs/research/underdog_pricing_gap_investigation.md
# (Session 2.31): Underdog's own per-side price on skewed ("chalk") lines
# reflects real, current lineup/starting-pitcher/injury information this
# project's season-average + recent-form blend does not have. The two
# functions below give this project access to the SAME real-time signal --
# MLB Stats API's own probable-pitcher and confirmed-lineup data -- so a
# later stage can compare what the model assumed against what MLB has
# actually confirmed. This module does NOT decide what to do with that
# comparison (no filtering/gating here) -- pickem_model.py's
# compute_mlb_starter_status() (Session 2.32) reads these and attaches a
# new, purely informational column, per the roadmap card's explicit "no
# hard-coded filtering yet" scope.
#
# Confirmed live, 2026-09-15, against real MLB Stats API responses (see
# ROADMAP.md Session 2.32 / SESSION_LOG.md for the real output):
#   1. GET /v1/schedule?sportId=1&date=YYYY-MM-DD&hydrate=probablePitcher
#      -- each game's teams.{away,home}.probablePitcher (id + fullName),
#      MLB's own real, current probable-starter signal.
#   2. GET /v1.1/game/{gamePk}/feed/live -- once MLB posts a real lineup,
#      liveData.boxscore.teams.{away,home}.battingOrder (real player ids)
#      and .pitchers (real player ids, in real usage order). Confirmed
#      live: EMPTY for a game still hours from first pitch, POPULATED once
#      MLB posts the real lineup (typically ~1-2h before first pitch,
#      sometimes later) -- a real, honest data gap when unavailable, not a
#      bug to fake around.
# ---------------------------------------------------------------------------
def fetch_schedule_games(date: str) -> list[dict]:
    """Real per-game MLB schedule for `date` (YYYY-MM-DD), hydrated with
    each team's real probable starting pitcher. Returns one dict per real
    scheduled game: gamePk, away_team_id, away_team_name, home_team_id,
    home_team_name, away_probable_pitcher_id, away_probable_pitcher_name,
    home_probable_pitcher_id, home_probable_pitcher_name -- the pitcher
    fields are None when MLB has not posted a probable starter for that
    team/game yet (a real, honest gap, never fabricated). Returns [] (not
    an exception) if the whole schedule call fails after retries -- same
    fault-isolation standard as _fetch_active_roster/_fetch_player_game_log
    above."""
    url = f"{MLB_STATS_API_BASE}/schedule?sportId=1&date={date}&hydrate=probablePitcher"
    try:
        payload = get_json_with_retries(url, timeout=15)
    except Exception as exc:  # noqa: BLE001
        log.warning("Could not fetch MLB schedule for %s: %s", date, exc)
        return []
    games: list[dict] = []
    for date_entry in payload.get("dates", []):
        for g in date_entry.get("games", []):
            teams = g.get("teams", {}) or {}
            away = teams.get("away", {}) or {}
            home = teams.get("home", {}) or {}
            away_team = away.get("team", {}) or {}
            home_team = home.get("team", {}) or {}
            away_pp = away.get("probablePitcher") or {}
            home_pp = home.get("probablePitcher") or {}
            away_team_id = away_team.get("id")
            home_team_id = home_team.get("id")
            games.append({
                "gamePk": g.get("gamePk"),
                "away_team_id": away_team_id,
                "away_team_name": away_team.get("name"),
                "away_team_nickname": MLB_TEAM_ID_TO_NICKNAME.get(away_team_id),
                "home_team_id": home_team_id,
                "home_team_name": home_team.get("name"),
                "home_team_nickname": MLB_TEAM_ID_TO_NICKNAME.get(home_team_id),
                "away_probable_pitcher_id": away_pp.get("id"),
                "away_probable_pitcher_name": away_pp.get("fullName"),
                "home_probable_pitcher_id": home_pp.get("id"),
                "home_probable_pitcher_name": home_pp.get("fullName"),
            })
    return games


def fetch_probable_pitchers(date: str) -> dict:
    """Real per-game map of {team_id: probable_pitcher_id} for every team
    scheduled to play on `date` (YYYY-MM-DD), built from
    fetch_schedule_games() above. A team with no real probable pitcher
    posted yet for that date is simply absent from the returned dict --
    callers must treat a missing key as "not yet known", not as any other
    value. Returns {} if the schedule call itself failed (see
    fetch_schedule_games's own fault-isolation)."""
    pitchers: dict[int, int] = {}
    for g in fetch_schedule_games(date):
        away_id, away_pitcher = g["away_team_id"], g["away_probable_pitcher_id"]
        if away_id is not None and away_pitcher is not None:
            pitchers[away_id] = away_pitcher
        home_id, home_pitcher = g["home_team_id"], g["home_probable_pitcher_id"]
        if home_id is not None and home_pitcher is not None:
            pitchers[home_id] = home_pitcher
    return pitchers


def fetch_confirmed_lineup(game_pk) -> Optional[dict]:
    """Real confirmed starting lineup + pitcher-usage for one real MLB
    game, from MLB Stats API's live game feed (v1.1). Returns None (never
    an exception, never a fabricated value) when MLB has not posted a real
    lineup for this game yet -- confirmed live, 2026-09-15:
    liveData.boxscore.teams.{away,home}.battingOrder is an empty list for
    a game still hours from first pitch, and populates with real MLB
    player ids once MLB posts the real lineup. When a lineup IS posted,
    returns:
        {"away": {"batting_order": [player_id, ...], "pitchers": [player_id, ...]},
         "home": {"batting_order": [...], "pitchers": [...]}}
    `pitchers` is MLB's own real, ordered list of pitcher ids who have
    actually appeared/been announced for that side -- the first entry is
    that side's real starter once available."""
    if game_pk is None:
        return None
    url = f"{MLB_STATS_API_BASE_V1_1}/game/{game_pk}/feed/live"
    try:
        payload = get_json_with_retries(url, timeout=15)
    except Exception as exc:  # noqa: BLE001
        log.warning("Could not fetch MLB confirmed lineup for game %s: %s", game_pk, exc)
        return None
    boxscore_teams = ((payload.get("liveData") or {}).get("boxscore") or {}).get("teams", {}) or {}
    away = boxscore_teams.get("away", {}) or {}
    home = boxscore_teams.get("home", {}) or {}
    away_order = away.get("battingOrder") or []
    home_order = home.get("battingOrder") or []
    away_pitchers = away.get("pitchers") or []
    home_pitchers = home.get("pitchers") or []
    if not away_order and not home_order and not away_pitchers and not home_pitchers:
        # Real, honest "not posted yet" case -- see docstring above.
        return None
    return {
        "away": {"batting_order": away_order, "pitchers": away_pitchers},
        "home": {"batting_order": home_order, "pitchers": home_pitchers},
    }


def _normalize_team_token(name: Optional[str]) -> str:
    """Strips everything but lowercase letters/digits, so real team-name
    spellings that differ only in punctuation match -- e.g. MLB Stats
    API's own "D-backs" (Diamondbacks' real teamName) and Underdog's real
    "D'Backs" wording both normalize to "dbacks"."""
    return re.sub(r"[^a-z0-9]", "", (name or "").lower())


def find_scheduled_game(games: list[dict], away_label: str, home_label: str) -> Optional[dict]:
    """Matches a platform's own real 'Away @ Home' matchup labels (this is
    written for Underdog's real wording -- full team nicknames, e.g.
    "Mets @ Yankees", confirmed live 2026-09-15 against a real
    data/pickem/clv_log.csv sample) against fetch_schedule_games()'s real
    away_team_name/home_team_name (MLB Stats API's own `teamName` field),
    using the normalized-token match above. Returns None if no real
    scheduled game matches both labels -- an honest "couldn't resolve this
    prop to a real game" result, never a guess."""
    away_norm = _normalize_team_token(away_label)
    home_norm = _normalize_team_token(home_label)
    if not away_norm or not home_norm:
        return None
    for g in games:
        if (
            _normalize_team_token(g.get("away_team_nickname")) == away_norm
            and _normalize_team_token(g.get("home_team_nickname")) == home_norm
        ):
            return g
    return None


MLB_PLUGIN = SportPlugin(
    name="mlb",
    sport_labels=MLB_SPORT_LABELS,
    fetch_stats=fetch_mlb_season_stats,
    stat_type_map=MLB_STAT_TYPE_MAP,
    composite_stat_types=MLB_COMPOSITE_STAT_TYPES,
    computed_stat_types=MLB_COMPUTED_STAT_TYPES,
    computed_required_columns=MLB_COMPUTED_REQUIRED_COLUMNS,
)
