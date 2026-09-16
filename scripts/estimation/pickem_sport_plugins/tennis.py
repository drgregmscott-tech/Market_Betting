"""
Session 2.17 -- Tennis plug-in (Pick'em), lag-based free archive.

WHY THIS ONE NEEDED A REAL DECISION FIRST
------------------------------------------
Per `docs/research/sport_inventory.md` (Session 2.10): real, substantial
tennis volume exists on both platforms (1,179 live PrizePicks projections;
one of only 3 sports Underdog's pick'em product offers at all), but no
free, real-time, per-match stats source was found -- only paid live
providers, or a free historical archive not built for fast post-match
grading. The user chose the free, lag-based path (2026-09-12): accept
delayed grading rather than pay for a live feed or skip tennis.

A SECOND, UNPLANNED GAP FOUND DURING THIS SESSION
---------------------------------------------------
The archive the roadmap actually named -- `JeffSackmann/tennis_atp` and
`tennis_wta` on GitHub -- no longer exists at that location (confirmed
live, 2026-09-12: both return a real 404; the JeffSackmann account is
still active but now has only one public repo,
`tennis_MatchChartingProject`). This is a second real, unplanned gap on
top of the one already known going into this session, not a naming detail
-- it meant the free path itself had quietly disappeared underneath the
decision the user had just made.

Checked several candidate replacements before picking one (stale clones
last updated 2018; unrelated personal projects of unknown data quality).
Settled on **`Aneeshers/tennis-sackmann-archive`**
(https://github.com/Aneeshers/tennis-sackmann-archive), which is
explicitly an archival mirror of Jeff Sackmann's original data (not a
derived/reinterpreted copy): same file layout and column schema as the
original (`atp_matches_{year}.csv` / `wta_matches_{year}.csv`), same CC
BY-NC-SA 4.0 license Sackmann released under, a `README.md` naming the
three original upstream repos directly, and per-folder
`UPSTREAM_README.md` files preserving Sackmann's own original
documentation for provenance. Its ATP/WTA match files run through 2026
(snapshot taken from an upstream commit in June 2026) -- confirmed live by
fetching `atp/atp_matches_2026.csv` directly and checking real rows (e.g.
a real "United Cup" Hurkacz/Wawrinka match, tourney_date 20260105).

License note: CC BY-NC-SA 4.0 is a non-commercial license. This project
uses the data only to grade its own props for internal
research/comparison, not to resell or redistribute the raw data itself --
consistent with that license -- but this is worth re-checking if this
project's use ever becomes commercial.

WHY "LAG-BASED" IS A REAL, NAMED TRADE-OFF, NOT A BUG
--------------------------------------------------------
The mirror above is a periodic snapshot of an already-periodic upstream
archive -- there is no guarantee either one updates same-day, or even
same-week, for a real completed match. A prop graded against this source
may resolve well after the platform itself would have settled it. This
plug-in re-downloads its cached file only every `REFRESH_HOURS` hours (see
below) precisely because there is no faster real signal available on this
path -- that gap is the whole reason a paid provider was the other real
option the user considered and explicitly declined.

FETCH SHAPE
-----------
One CSV per (tour, season) -- `fetch_tennis_season_stats(season)` pulls
both `atp_matches_{season}.csv` and `wta_matches_{season}.csv`, caches
each to `data/pickem/cache/tennis_archive/`, and flattens every match into
TWO rows (winner + loser), matching the fetch_stats() contract in
`pickem_sport_plugins/__init__.py`. Doubles matches are NOT in this
dataset (Sackmann's singles files only) -- a real Underdog/PrizePicks
doubles prop (player_name like "Krueger A / Montgomery R", confirmed
present in real ingested rows) will simply fail to match any player name
here and fall through to the existing "insufficient_history" path, the
same honest behavior an unmatched player already produces for every other
sport. Not a bug to fix in this plug-in -- singles-only coverage is the
real shape of the source.

STAT-TYPE COVERAGE -- REAL STRINGS, from a real ingested tennis snapshot
(`data/pickem/normalized/pickem_props_20260911T124346Z.csv`, 272 real
tennis rows, PrizePicks): Double Faults 60, Aces 55, Total Games Won 46,
Total Games 27, Fantasy Score 20, 1st Set Total Games Won 19, 1st Set
Total Games 14, Break Points Won 12, Total Tie Breaks 10, Total Sets 9.

Aces and Double Faults map directly to Sackmann's own `w_ace`/`l_ace` and
`w_df`/`l_df` columns. Every other real stat type here requires deriving a
value from the match `score` string (e.g. "6-3 3-6 6-3") and/or the
`bpSaved`/`bpFaced` columns -- done once per match in `_flatten_matches()`
below and stored as plain per-player columns, the same "precompute once,
map by column name" pattern CFB's `kick_fgm`/`kick_xpm` use for its own
combined "made/attempted" strings.

Left unsupported, real stated gap, same standard as every prior sport:
  - `Fantasy Score` (20 real rows) -- no official PrizePicks/Underdog
    tennis scoring formula could be sourced; guessing one here would be
    presenting an assumption as a real number, same reasoning as CFB's
    Fantasy Score/Fantasy Points gap.

A FINAL-SET MATCH TIE-BREAK ("[10-7]") IS A REAL SCORING-FORMAT WRINKLE
--------------------------------------------------------------------------
Some matches (mostly doubles historically, but also some ATP/WTA deciding
sets at certain events) end in a 10-point match tie-break written in
brackets, e.g. "6-4 3-6 [10-7]", played INSTEAD OF a full final set. That
bracket is real for `Total Sets` / `Total Tie Breaks` purposes (it is a
genuine deciding "set" of the match) but its two numbers are match-tiebreak
POINTS, not games -- counting them into `Total Games`/`Total Games Won`
would silently inflate those two stats with numbers that were never really
"games". `_parse_sets()` below tags this case explicitly
(`is_super_tiebreak=True`) and excludes it from the games sums while still
counting it toward sets/tiebreaks, rather than guessing either way
silently.
"""

from __future__ import annotations

import logging
import re
import time
from pathlib import Path

import pandas as pd
import requests

from . import SportPlugin

log = logging.getLogger("pickem_model")

ARCHIVE_BASE = "https://raw.githubusercontent.com/Aneeshers/tennis-sackmann-archive/main"
ATP_URL_TEMPLATE = f"{ARCHIVE_BASE}/atp/atp_matches_{{season}}.csv"
WTA_URL_TEMPLATE = f"{ARCHIVE_BASE}/wta/wta_matches_{{season}}.csv"

CACHE_DIR = Path("data/pickem/cache/tennis_archive")

# The archive itself only updates periodically (see module docstring's
# "lag-based" note) -- there is no point re-fetching more often than this.
# A prior season's file is effectively permanent (no games left to add) but
# is still refetched on this same schedule for simplicity; the extra call
# is cheap (one file, once per REFRESH_HOURS) compared to CFBD's metered
# call budget (Session 2.16), so no "_final" short-circuit is needed here.
REFRESH_HOURS = 12

TENNIS_SPORT_LABELS = frozenset({"tennis"})

TENNIS_STAT_TYPE_MAP: dict[str, str] = {
    "aces": "ace",
    "double faults": "df",
    "total games won": "games_won",
    "total games": "games_total",
    "1st set total games won": "set1_games_won",
    "1st set total games": "set1_games_total",
    "break points won": "break_points_won",
    "total tie breaks": "tiebreaks_total",
    "total sets": "sets_total",
    # "fantasy score" (20 real rows) has NO mapping -- see module
    # docstring's "Left unsupported" note.
}


# ---------------------------------------------------------------------------
# Score parsing
# ---------------------------------------------------------------------------
_SET_TOKEN_RE = re.compile(r"^(\d+)-(\d+)")


def _parse_sets(score: object) -> list[dict]:
    """Parses a real Sackmann `score` string (e.g. "6-3 3-6 6-3", "7-6(4)
    6-4", "6-4 3-6 [10-7]") into one dict per set:
    {"w_games", "l_games", "is_tiebreak", "is_super_tiebreak"}. Tokens that
    aren't a real set score at all (RET, W/O, DEF, Default, or a blank/NaN
    value for an abandoned/unplayed match) are skipped rather than guessed
    -- the same "don't guess" standard used everywhere else in this
    project. See module docstring for why a bracketed "[10-7]" match
    tie-break is tagged `is_super_tiebreak` and excluded from games sums."""
    if not isinstance(score, str) or not score.strip():
        return []
    sets: list[dict] = []
    for token in score.split():
        is_super_tiebreak = token.startswith("[")
        is_tiebreak = "(" in token or is_super_tiebreak
        cleaned = token.strip("[]")
        match = _SET_TOKEN_RE.match(cleaned)
        if not match:
            continue  # RET / W/O / DEF / etc. -- not a real set score
        sets.append({
            "w_games": int(match.group(1)),
            "l_games": int(match.group(2)),
            "is_tiebreak": is_tiebreak,
            "is_super_tiebreak": is_super_tiebreak,
        })
    return sets


def _safe_num(value: object) -> float:
    try:
        f = float(value)
    except (TypeError, ValueError):
        return 0.0
    return 0.0 if pd.isna(f) else f


def _sort_key(row: pd.Series) -> int:
    """Chronological ordering within one player's rows, per the fetch_stats
    contract in pickem_sport_plugins/__init__.py. Sackmann's `tourney_date`
    (e.g. 20260105, an int YYYYMMDD) orders matches by day; `match_num` is
    appended to keep same-day matches in a stable, deterministic order
    (its own real ordering isn't strictly chronological within a day, but
    consistency here matters more than exactness, same as CFBD's
    non-sequential game id noted in cfb.py)."""
    try:
        date_part = int(row.get("tourney_date"))
    except (TypeError, ValueError):
        date_part = 0
    try:
        match_part = int(row.get("match_num"))
    except (TypeError, ValueError):
        match_part = 0
    return date_part * 10000 + match_part


# ---------------------------------------------------------------------------
# Fetch + cache
# ---------------------------------------------------------------------------
def _cache_path(tour: str, season: int) -> Path:
    return CACHE_DIR / f"{tour}_matches_{season}.csv"


def _download_matches(tour: str, season: int, url_template: str) -> pd.DataFrame:
    """Downloads one tour's season CSV, caching to disk and only
    re-fetching every REFRESH_HOURS (see module docstring). A network
    failure with a cached file present logs a warning and falls back to
    the stale cache rather than losing the whole tour's data for one
    transient error, same fault-isolation standard as
    `http_utils.get_json_with_retries()`; a failure with NO cache at all
    returns an empty DataFrame, the same honest "no data yet" shape every
    other plug-in uses."""
    path = _cache_path(tour, season)
    needs_fetch = True
    if path.exists():
        age_hours = (time.time() - path.stat().st_mtime) / 3600
        needs_fetch = age_hours >= REFRESH_HOURS

    if needs_fetch:
        url = url_template.format(season=season)
        try:
            resp = requests.get(url, timeout=30)
            resp.raise_for_status()
            CACHE_DIR.mkdir(parents=True, exist_ok=True)
            path.write_bytes(resp.content)
        except requests.exceptions.RequestException as exc:
            if path.exists():
                log.warning(
                    "Could not refresh %s tennis archive for %s (%s) -- "
                    "using stale cache.", tour, season, exc,
                )
            else:
                log.warning(
                    "Could not fetch %s tennis archive for %s: %s -- no "
                    "tennis data for this tour/season.", tour, season, exc,
                )
                return pd.DataFrame([])

    try:
        return pd.read_csv(path, low_memory=False)
    except (OSError, pd.errors.ParserError) as exc:
        log.warning("Could not parse cached %s tennis archive file %s: %s", tour, season, exc)
        return pd.DataFrame([])


def _flatten_matches(matches: pd.DataFrame, tour_prefix: str) -> list[dict]:
    """One real match -> two rows (winner, loser), each carrying that
    player's own view of every stat in TENNIS_STAT_TYPE_MAP. player_id is
    prefixed by tour ("atp_"/"wta_") since ATP and WTA player ids are
    separate namespaces in Sackmann's data and could otherwise collide."""
    rows: list[dict] = []
    for _, m in matches.iterrows():
        winner_id = m.get("winner_id")
        loser_id = m.get("loser_id")
        winner_name = m.get("winner_name")
        loser_name = m.get("loser_name")
        if pd.isna(winner_id) or pd.isna(loser_id) or not winner_name or not loser_name:
            continue

        sets = _parse_sets(m.get("score"))
        scored_sets = [s for s in sets if not s["is_super_tiebreak"]]
        games_total = sum(s["w_games"] + s["l_games"] for s in scored_sets)
        winner_games_won = sum(s["w_games"] for s in scored_sets)
        loser_games_won = sum(s["l_games"] for s in scored_sets)
        sets_total = len(sets)
        tiebreaks_total = sum(1 for s in sets if s["is_tiebreak"])
        set1 = sets[0] if sets else None
        set1_games_total = (set1["w_games"] + set1["l_games"]) if set1 else 0
        set1_winner_games = set1["w_games"] if set1 else 0
        set1_loser_games = set1["l_games"] if set1 else 0

        # Break points WON by a player is not a column Sackmann carries
        # directly -- it's the break points the OPPONENT faced and did not
        # save (bpFaced - bpSaved), the same real-world event viewed from
        # the other side of the net.
        winner_bp_won = _safe_num(m.get("l_bpFaced")) - _safe_num(m.get("l_bpSaved"))
        loser_bp_won = _safe_num(m.get("w_bpFaced")) - _safe_num(m.get("w_bpSaved"))

        sort_key = _sort_key(m)
        # Session 2.29: `tourney_date` is the TOURNAMENT's own start date,
        # shared by every match in a (possibly multi-week) event -- not
        # this individual match's real calendar date. Confirmed live
        # against the real 2026 archive (e.g. the "United Cup" tourney_id
        # 2026-9900 carries the identical tourney_date 20260105 across 20
        # different real matches). That rules out date-based grading the
        # way every other sport's adapter uses it (auto_grade_outcomes.py
        # docstring) -- this plug-in instead carries `opponent_name` on
        # every row so the grader can match a flag to its real match by
        # (player, real opponent) from the flag's own `game_matchup`
        # field, not by date. `tourney_date` is kept too, only as an
        # approximate tie-breaker if a player faces the same real opponent
        # more than once in a season (rare, e.g. a tour-then-rematch).
        try:
            tourney_date = int(m.get("tourney_date"))
        except (TypeError, ValueError):
            tourney_date = None

        rows.append({
            "player_id": f"{tour_prefix}_{int(winner_id)}",
            "player_display_name": winner_name,
            "opponent_name": loser_name,
            "tourney_date": tourney_date,
            "sort_key": sort_key,
            "ace": _safe_num(m.get("w_ace")),
            "df": _safe_num(m.get("w_df")),
            "games_won": winner_games_won,
            "games_total": games_total,
            "set1_games_won": set1_winner_games,
            "set1_games_total": set1_games_total,
            "break_points_won": winner_bp_won,
            "tiebreaks_total": tiebreaks_total,
            "sets_total": sets_total,
        })
        rows.append({
            "player_id": f"{tour_prefix}_{int(loser_id)}",
            "player_display_name": loser_name,
            "opponent_name": winner_name,
            "tourney_date": tourney_date,
            "sort_key": sort_key,
            "ace": _safe_num(m.get("l_ace")),
            "df": _safe_num(m.get("l_df")),
            "games_won": loser_games_won,
            "games_total": games_total,
            "set1_games_won": set1_loser_games,
            "set1_games_total": set1_games_total,
            "break_points_won": loser_bp_won,
            "tiebreaks_total": tiebreaks_total,
            "sets_total": sets_total,
        })
    return rows


def fetch_tennis_season_stats(season: int) -> pd.DataFrame:
    """Both tours' real match data for one calendar year (Sackmann's
    archive is filed by calendar year, not a Sept-to-Jan "season" the way
    NFL/CFB are -- `season` here is simply the year to fetch). Returns an
    empty DataFrame, the same honest "no data yet" shape every other
    plug-in uses, if both tours fail to fetch."""
    atp_df = _download_matches("atp", season, ATP_URL_TEMPLATE)
    wta_df = _download_matches("wta", season, WTA_URL_TEMPLATE)

    rows: list[dict] = []
    if not atp_df.empty:
        rows.extend(_flatten_matches(atp_df, "atp"))
    if not wta_df.empty:
        rows.extend(_flatten_matches(wta_df, "wta"))

    return pd.DataFrame(rows)


TENNIS_PLUGIN = SportPlugin(
    name="tennis",
    sport_labels=TENNIS_SPORT_LABELS,
    fetch_stats=fetch_tennis_season_stats,
    stat_type_map=TENNIS_STAT_TYPE_MAP,
)
