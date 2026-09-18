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


# ---------------------------------------------------------------------------
# SESSION 2.45 -- NFL injury-report confirmation signal (informational only).
#
# WHAT: nflverse republishes the NFL's official weekly injury report (the
# list each team must file for every game: practice level Wed-Fri, plus a
# final game status of Questionable / Doubtful / Out) as a free CSV. No API
# key. Checked live 2026-09-18: 2026 file had weeks 1-2, 2025 had full season.
# WHO/WHY: pickem_model.py uses it to tag each NFL prop with a status, the
# same idea as MLB's `mlb_starter_status` (Session 2.32): the model only
# knows season averages, but the platform's own line may already price in
# that a player is hurt.
# Runs automatically inside every estimation run. Fail-safe: any fetch
# error returns None and the status stays blank -- never a guess.
# ---------------------------------------------------------------------------
INJURY_REPORT_URL_TEMPLATE = NFLVERSE_BASE_URL + "/injuries/injuries_{season}.csv"
SCHEDULE_URL = "https://raw.githubusercontent.com/nflverse/nfldata/master/data/games.csv"

# Team-code spellings differ between platforms, the schedule, and injuries.
NFL_TEAM_ALIASES: dict[str, str] = {
    "LAR": "LA", "JAC": "JAX", "WSH": "WAS", "OAK": "LV", "LVR": "LV",
    "SD": "LAC", "STL": "LA", "ARZ": "ARI", "BLT": "BAL", "CLV": "CLE",
    "HST": "HOU", "SL": "LA", "NWE": "NE", "GNB": "GB", "KAN": "KC",
    "NOR": "NO", "SFO": "SF", "TAM": "TB",
}


# Session 2.46 follow-up: Underdog labels teams by nickname ("Packers @ Jets"),
# not by code. Maps each nickname (upper-case) to the nflverse team code.
NFL_TEAM_NICKNAMES: dict[str, str] = {
    "CARDINALS": "ARI", "FALCONS": "ATL", "RAVENS": "BAL", "BILLS": "BUF",
    "PANTHERS": "CAR", "BEARS": "CHI", "BENGALS": "CIN", "BROWNS": "CLE",
    "COWBOYS": "DAL", "BRONCOS": "DEN", "LIONS": "DET", "PACKERS": "GB",
    "TEXANS": "HOU", "COLTS": "IND", "JAGUARS": "JAX", "CHIEFS": "KC",
    "RAIDERS": "LV", "CHARGERS": "LAC", "RAMS": "LA", "DOLPHINS": "MIA",
    "VIKINGS": "MIN", "PATRIOTS": "NE", "SAINTS": "NO", "GIANTS": "NYG",
    "JETS": "NYJ", "EAGLES": "PHI", "STEELERS": "PIT", "49ERS": "SF",
    "SEAHAWKS": "SEA", "BUCCANEERS": "TB", "TITANS": "TEN", "COMMANDERS": "WAS",
}


def normalize_nfl_team(code: object) -> str:
    """Upper-cases a team label and maps it to the nflverse team code.
    Handles codes with alternate spellings ("JAC"), nicknames ("Packers")
    and full names ("Green Bay Packers", via the last word). Returns "" for
    non-strings."""
    if not isinstance(code, str):
        return ""
    cleaned = code.strip().upper()
    if cleaned in NFL_TEAM_NICKNAMES:
        return NFL_TEAM_NICKNAMES[cleaned]
    if " " in cleaned and cleaned.split()[-1] in NFL_TEAM_NICKNAMES:
        return NFL_TEAM_NICKNAMES[cleaned.split()[-1]]
    return NFL_TEAM_ALIASES.get(cleaned, cleaned)


def fetch_injury_report(season: int) -> "pd.DataFrame | None":
    """One season of the NFL weekly injury report, or None on any failure."""
    try:
        df = pd.read_csv(INJURY_REPORT_URL_TEMPLATE.format(season=season))
    except Exception:  # noqa: BLE001 -- fault-isolated, status stays blank
        return None
    required = {"team", "week", "gsis_id", "report_status", "game_type"}
    if not required.issubset(df.columns):
        return None
    df = df[df["game_type"] == "REG"].copy()
    df["team"] = df["team"].map(normalize_nfl_team)
    return df


def fetch_nfl_schedule(season: int) -> "pd.DataFrame | None":
    """One season of the NFL schedule (week + teams), or None on failure."""
    try:
        df = pd.read_csv(SCHEDULE_URL, usecols=["season", "week", "game_type", "away_team", "home_team"])
    except Exception:  # noqa: BLE001
        return None
    df = df[(df["season"] == season) & (df["game_type"] == "REG")].copy()
    df["away_team"] = df["away_team"].map(normalize_nfl_team)
    df["home_team"] = df["home_team"].map(normalize_nfl_team)
    return df


def find_nfl_game_week(schedule: pd.DataFrame, away_label: str, home_label: str) -> "int | None":
    """Week number of the scheduled game between these two teams, or None.
    Two teams meet at most once per regular season in nearly all cases."""
    away, home = normalize_nfl_team(away_label), normalize_nfl_team(home_label)
    hit = schedule[(schedule["away_team"] == away) & (schedule["home_team"] == home)]
    if hit.empty:
        return None
    return int(hit.iloc[0]["week"])


# ---------------------------------------------------------------------------
# SESSION 2.46 -- NFL game-time weather (wind) adjustment.
#
# WHAT: strong wind makes passing harder. Research
# (scripts/calibration/research_nfl_weather_effect.py, 2020-2025 outdoor
# games, fit 2020-23, checked on 2024-25) found that when game-time wind is
# 15 mph or more, passing yards, completions, receiving yards and receptions
# fall about 10-18% below the calm-wind level, in BOTH the fit and the
# held-out seasons. Temperature effects were weaker and mixed; kicking was
# NOT wind-sensitive in the data; rushing showed no reliable effect. So only
# the four wind-sensitive stats below are adjusted, only at wind >= 15 mph.
# WHO/WHY: pickem_model.py multiplies its estimated mean by the factor, so a
# windy-game prop is not scored as if the game were calm.
# SOURCE: free Open-Meteo forecast API (no key). Stadium roof type and
# stadium id come from the nflverse schedule file. Only roof == "outdoors"
# games are adjusted; dome, closed and open-retractable games get NO
# adjustment (weather cannot be trusted to act there).
# Runs automatically inside every estimation run. Fail-safe: any failure
# leaves the factor at 1.0 (no adjustment) -- never a guess.
# ---------------------------------------------------------------------------
OPEN_METEO_FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
WEATHER_WIND_THRESHOLD_MPH = 15.0
# Multiplier on the model mean when forecast wind >= threshold. Measured
# effect vs calm (<10 mph), fit / held-out: passing_yards -14%/-18%,
# completions -10%/-14%, receiving_yards -11%/-18%, receptions -7%/-12%.
# Set slightly milder than measured because forecast wind is noisier than
# the observed wind the research used.
WIND_FACTOR_BY_STAT: dict[str, float] = {
    "passing_yards": 0.88,
    "completions": 0.90,
    "receiving_yards": 0.90,
    "receptions": 0.93,
}

# (latitude, longitude) by nflverse stadium_id, for OUTDOOR venues only.
# Domes/retractables are omitted on purpose: no coordinates, no adjustment.
STADIUM_COORDS: dict[str, tuple[float, float]] = {
    "BAL00": (39.278, -76.623), "BOS00": (42.091, -71.264), "BUF00": (42.774, -78.787),
    "CAR00": (35.226, -80.853), "CHI98": (41.862, -87.617), "CIN00": (39.095, -84.516),
    "CLE00": (41.506, -81.700), "DEN00": (39.744, -105.020), "GNB00": (44.501, -88.062),
    "JAX00": (30.324, -81.637), "KAN00": (39.049, -94.484), "MIA00": (25.958, -80.239),
    "NAS00": (36.166, -86.771), "NYC01": (40.814, -74.074), "PHI00": (39.901, -75.168),
    "PIT00": (40.447, -80.016), "SEA00": (47.595, -122.332), "SFO01": (37.403, -121.970),
    "TAM00": (27.976, -82.503), "WAS00": (38.908, -76.864),
}

_VENUE_FIELDS = ["gameday", "gametime", "roof", "stadium_id"]


def fetch_nfl_schedule_with_venues(season: int) -> "pd.DataFrame | None":
    """Schedule with venue fields (roof, stadium id, date, time), or None."""
    try:
        df = pd.read_csv(
            SCHEDULE_URL,
            usecols=["season", "week", "game_type", "away_team", "home_team"] + _VENUE_FIELDS,
        )
    except Exception:  # noqa: BLE001
        return None
    df = df[(df["season"] == season) & (df["game_type"] == "REG")].copy()
    df["away_team"] = df["away_team"].map(normalize_nfl_team)
    df["home_team"] = df["home_team"].map(normalize_nfl_team)
    return df


def find_nfl_game_venue(
    schedule: pd.DataFrame, away_label: str, home_label: str
) -> "dict | None":
    """Roof and stadium id of the scheduled game, or None if not found."""
    away, home = normalize_nfl_team(away_label), normalize_nfl_team(home_label)
    hit = schedule[(schedule["away_team"] == away) & (schedule["home_team"] == home)]
    if hit.empty:
        return None
    first = hit.iloc[0]
    return {"roof": first.get("roof"), "stadium_id": first.get("stadium_id")}


def fetch_kickoff_weather(
    lat: float, lon: float, kickoff_iso: str
) -> "tuple[float, float] | None":
    """(wind_mph, temp_f) forecast for kickoff plus two hours (mid-game), or
    None on any failure or if the game is past the forecast window.
    `kickoff_iso` carries its own UTC offset."""
    try:
        import requests

        kickoff = pd.Timestamp(kickoff_iso)
        if kickoff.tzinfo is None:
            return None
        target = (kickoff + pd.Timedelta(hours=2)).tz_convert("UTC").floor("h")
        resp = requests.get(
            OPEN_METEO_FORECAST_URL,
            params={
                "latitude": lat, "longitude": lon,
                "hourly": "wind_speed_10m,temperature_2m",
                "wind_speed_unit": "mph", "temperature_unit": "fahrenheit",
                "timezone": "UTC", "forecast_days": 16,
            },
            timeout=15,
        )
        resp.raise_for_status()
        hourly = resp.json()["hourly"]
        idx = hourly["time"].index(target.strftime("%Y-%m-%dT%H:00"))
        wind, temp = hourly["wind_speed_10m"][idx], hourly["temperature_2m"][idx]
        if wind is None or temp is None:
            return None
        return float(wind), float(temp)
    except Exception:  # noqa: BLE001 -- fault-isolated, factor stays 1.0
        return None


def wind_factor(resolved_stat_key: object, wind_mph: "float | None") -> float:
    """Multiplier for the model mean. 1.0 unless wind >= threshold and the
    stat is one of the wind-sensitive ones."""
    if wind_mph is None or wind_mph < WEATHER_WIND_THRESHOLD_MPH:
        return 1.0
    return WIND_FACTOR_BY_STAT.get(str(resolved_stat_key), 1.0)
