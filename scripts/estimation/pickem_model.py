"""
Session 2.3 — Estimation Engine v1 (Fixed-Line Pick'em Platforms)

WHAT THIS SCRIPT IS
--------------------
Reads Session 2.2's normalized pick'em output (data/pickem/normalized/latest.csv:
one row per PrizePicks/Underdog prop, in the shared schema from schema.py) and,
for every row it can, produces:
  - a modeled probability that the real outcome lands OVER the platform's line
  - a modeled probability that it lands UNDER the line
  - the platform's own implied probability (see "IMPLIED PROBABILITY" below)
  - the edge (model probability minus implied probability) on each side

This is a v1 model. Its job is to prove the full pipeline shape end-to-end
(ingested prop -> real external performance data -> probability estimate ->
comparison against the platform's own price) using a small, fully-named set
of inputs -- not to be the final, most accurate version. Session 2.3's
roadmap card is explicit that the exact input list gets finalized "with real
data in hand, not guessed in advance," and that any excluded input must be a
STATED gap, not a silent one. See the "WHAT THIS MODEL DOES NOT DO YET"
section below and pickem_estimation_model_spec.md for that list.

WHY nflverse, AND WHY THE PATTERN LOOKS LIKE THE DFS REPO
-----------------------------------------------------------
This project reuses the DFS_Optimizer repo's proven architectural pattern,
not its code (see ROADMAP.md, Background & Approach). The season-average +
recency-weighted "recent form" blend below is the same shape of calculation
as DFS_Optimizer/scripts/projections_baseline.py, and the nflverse data pull
in fetch_nfl_weekly_stats() below is the same minimal, no-API-key parquet
read as DFS_Optimizer/scripts/nflverse_fetch.py -- copied deliberately
because that file's own docstring records that nfl_data_py (a more common
alternative) is dead upstream for any 2025+ season, and nflverse's own
release path changed once already. Reusing the already-debugged pull logic
here avoids re-discovering that same failure the hard way.

INPUTS USED IN v1 (named explicitly, per this project's "no unnamed
black-box factors" standard)
-----------------------------------------------------------------------
1. season_avg    -- mean of the relevant stat across the player's REG-season
                     games so far this season.
2. recent_form    -- recency-weighted average of the player's last 5 REG-
                     season games (weights: 0.35/0.25/0.20/0.12/0.08, most
                     recent game first -- identical weighting to
                     projections_baseline.py's RECENCY_WEIGHTS, renormalized
                     if the player has fewer than 5 games so far).
3. model_mean     -- blend of the two above: 50% season_avg / 50%
                     recent_form. A flat 50/50 blend is the simplest
                     defensible starting point for a v1 model; it is not
                     claimed to be optimal, and re-weighting this blend
                     against real graded outcomes is explicitly the kind of
                     work Session 8.3 (Ongoing Recalibration Cadence) exists
                     to do later, once real CLV/outcome data exists to tune
                     against (Sessions 2.4/2.5).
4. model_sigma    -- the player's own sample standard deviation of the stat
                     across their REG-season games so far. A player with
                     fewer than 2 qualifying games has no real sigma to
                     compute; see MIN_GAMES_FOR_ESTIMATE below.

WHAT THIS MODEL DOES NOT DO YET (stated gap, not a silent one)
-----------------------------------------------------------------
- Only NFL props are modeled in v1. PrizePicks and Underdog both carry
  props across many sports (Session 2.2's real ingested data included
  tennis and esports rows) -- v1 only has a real external stats source
  (nflverse) wired in for NFL. Every non-NFL row still gets a row in this
  script's output, explicitly marked model_status="unsupported_sport", not
  silently dropped.
- Only the NFL stat types listed in NFL_STAT_TYPE_MAP / COMPOSITE_STAT_TYPES
  / COMPUTED_STAT_TYPES are modeled. An NFL prop with a stat type not
  covered there is marked model_status="unsupported_stat_type" -- again, a
  visible row, not a dropped one. This list was built and expanded directly
  from real ingested-data stat_type strings (Session 2.3) -- see
  pickem_estimation_model_spec.md's "Stat-type coverage, checked against
  real data" section for the full record.
- No opponent/matchup adjustment, no injury/role status, no home/away
  split, no pace/usage adjustment. The roadmap card names these as
  candidate v1 inputs; they are deliberately deferred here so v1 proves the
  pipeline shape first, on the two inputs every later refinement will still
  need underneath it (a real performance baseline and a real recent-form
  signal).
- No weather input for outdoor games.
- The computed "Fantasy Score" stat (see COMPUTED_STAT_TYPES below)
  deliberately omits two components of PrizePicks' own official scoring
  table -- Offensive Fumble Recovery TDs and Kick/Punt/Field Goal Return
  TDs (6 points each) -- because nflverse's closest-named columns for these
  were checked directly against real data and do not reliably correspond
  (e.g. nflverse's `pt_return_tds` column fires for PUNTERS, not the
  players who actually returned a kick, on real 2025 data -- confirmed
  directly before this was written, not assumed). Both events are rare
  (well under 1% of player-games across a full season), so the omission's
  real-world impact is small, but it is a real, named gap, not a
  perfectly-complete implementation.
- The "implied probability" used for PrizePicks rows is a stated
  assumption (flat 50%), not a verified figure -- see "IMPLIED
  PROBABILITY" below. This should be revisited once Session 2.4's CLV
  logging is in place and a real benchmark is available to check it
  against.

IMPLIED PROBABILITY -- HOW IT IS COMPUTED, AND THE ASSUMPTION IT RESTS ON
-----------------------------------------------------------------------
Underdog's normalized rows carry over_payout_multiplier / under_payout_
multiplier (Session 2.2's schema). Treating those multipliers as fair-odds
(payout * true win probability = 1 at breakeven) gives:
    implied_prob_over  = (1 / over_multiplier)  / (1/over_multiplier + 1/under_multiplier)
    implied_prob_under = 1 - implied_prob_over
This is a normalized, no-vig-style conversion (mirrors how a sharp-book
benchmark is normalized in traditional sports betting), not a raw 1/odds
read, since 1/odds alone on both sides would not sum to 1 and would misstate
the platform's actual juice.

PrizePicks' normalized rows do NOT carry per-side multipliers (Session 2.2's
schema notes over_payout_multiplier/under_payout_multiplier as None for
PrizePicks -- standard PrizePicks lines pay a fixed multiplier on the whole
entry, not per individual pick). In the absence of a captured per-side
number, this script assumes a flat 50% implied probability on both sides
for PrizePicks rows. This is a STATED, UNVERIFIED assumption, not a
confirmed industry figure -- flagged here explicitly so it is not mistaken
for a researched fact, consistent with this project's standing rule (see
ROADMAP.md Open Decision #4) against building unverified claims into the
system as if they were confirmed.

USAGE
-----
pip install pandas numpy pyarrow --break-system-packages
python pickem_model.py --season 2025
"""

from __future__ import annotations

import argparse
import logging
import math
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, Optional

import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parents[2]
NORMALIZED_LATEST = BASE_DIR / "data" / "pickem" / "normalized" / "latest.csv"
OUTPUT_DIR = BASE_DIR / "output" / "estimation"
LOG_PATH = BASE_DIR / "logs" / "estimation.log"

# ---------------------------------------------------------------------------
# nflverse data pull -- same minimal, no-API-key parquet read as
# DFS_Optimizer/scripts/nflverse_fetch.py (see module docstring for why).
# ---------------------------------------------------------------------------
NFLVERSE_BASE_URL = "https://github.com/nflverse/nflverse-data/releases/download"
WEEKLY_STATS_URL_TEMPLATE = (
    f"{NFLVERSE_BASE_URL}/stats_player/stats_player_week_{{season}}.parquet"
)

# ---------------------------------------------------------------------------
# Model constants -- named here, explicitly, per this project's "no
# unnamed black-box factors" documentation standard.
# ---------------------------------------------------------------------------
RECENCY_WEIGHTS = [0.35, 0.25, 0.20, 0.12, 0.08]
SEASON_AVG_BLEND_WEIGHT = 0.5
RECENT_FORM_BLEND_WEIGHT = 0.5
MIN_GAMES_FOR_ESTIMATE = 2  # below this, sigma is not meaningfully estimable
SIGMA_FLOOR_FRACTION = 0.15  # sigma floor, as a fraction of the mean, used
# only when a player has exactly MIN_GAMES_FOR_ESTIMATE games and their
# observed sample sigma is implausibly small (near-zero) -- prevents a
# probability estimate of ~100%/~0% off two coincidentally similar games.

NFL_SPORT_LABELS = {"nfl", "football", "nfl football"}

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
    "passing touchdowns": "passing_tds",
    "rush tds": "rushing_tds",
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
# directly from PrizePicks' own official scoring pages (see
# pickem_estimation_model_spec.md for the exact source URLs and dates),
# not estimated or guessed -- and every nflverse column each formula reads
# was individually confirmed to exist before being used here.
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
    this is a small, real, and explicitly named gap, not a hidden one --
    see the module docstring's 'WHAT THIS MODEL DOES NOT DO YET' section."""
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
_COMPUTED_STAT_REQUIRED_COLUMNS: dict[str, list[str]] = {
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

NAME_SUFFIXES = {"jr", "sr", "ii", "iii", "iv", "v"}


# ---------------------------------------------------------------------------
# Logging -- same append-plus-console pattern as ingest_pickem.py, so a
# human or a future automated run sees the same kind of record.
# ---------------------------------------------------------------------------
def setup_logging() -> logging.Logger:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("pickem_model")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()

    file_handler = logging.FileHandler(LOG_PATH, mode="a", encoding="utf-8")
    console_handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s UTC | %(levelname)s | %(message)s")
    formatter.converter = time.gmtime
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger


log = setup_logging()


# ---------------------------------------------------------------------------
# nflverse fetch
# ---------------------------------------------------------------------------
def fetch_nfl_weekly_stats(season: int) -> pd.DataFrame:
    """Pulls one season of nflverse weekly player stats directly from the
    published parquet release. No API key required. If this 404s, nflverse
    has likely renamed the release again -- see
    https://github.com/nflverse/nflverse-data/releases and update
    WEEKLY_STATS_URL_TEMPLATE above (same fix pattern documented in
    DFS_Optimizer/scripts/nflverse_fetch.py)."""
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
    return df


# ---------------------------------------------------------------------------
# Name normalization / matching
# ---------------------------------------------------------------------------
def normalize_name(name: Optional[str]) -> str:
    """Lowercases, strips punctuation and common suffixes (Jr/Sr/II/III/IV),
    and collapses whitespace, so the same real player matches across two
    platforms' different name formatting (e.g. 'Patrick Mahomes II' vs
    'Patrick Mahomes'). Returns '' for a missing name so it never
    accidentally matches another missing name."""
    if not name or not isinstance(name, str):
        return ""
    cleaned = re.sub(r"[.\-']", " ", name.lower())
    cleaned = re.sub(r"[^a-z0-9\s]", "", cleaned)
    tokens = [t for t in cleaned.split() if t not in NAME_SUFFIXES]
    return " ".join(tokens).strip()


def build_name_lookup(weekly_df: pd.DataFrame) -> dict[str, str]:
    """Builds normalized_name -> player_id, using each player's MOST RECENT
    name on record (same 'most recent identity wins' pattern used in
    DFS_Optimizer/scripts/projections_baseline.py's season_baseline(), for
    the same reason: the same player_id can show slightly different name
    strings across weeks).

    Uses nflverse's `player_display_name` column, NOT `player_name`.
    Verified directly against a live pull of the 2025 weekly-stats release
    before this script was handed off: `player_name` is an abbreviated form
    ("P.Mahomes"), while `player_display_name` is the full name
    ("Patrick Mahomes") that actually matches how PrizePicks/Underdog print
    player names in Session 2.2's ingested data. Using `player_name` here
    would have silently produced a `no_player_match` result for nearly
    every row -- this was caught and fixed before Session 2.3 was handed
    off, not left as a discovered-later bug."""
    most_recent = (
        weekly_df.sort_values("week")
        .groupby("player_id")[["player_display_name"]]
        .last()
        .reset_index()
    )
    lookup: dict[str, str] = {}
    for _, row in most_recent.iterrows():
        norm = normalize_name(row["player_display_name"])
        if norm:
            lookup[norm] = row["player_id"]
    return lookup


# ---------------------------------------------------------------------------
# Stat resolution + per-player stat series
# ---------------------------------------------------------------------------
def resolve_stat_spec(stat_type: Optional[str]) -> tuple[Optional[str], object, str]:
    """Returns (kind, value, reason). kind is 'computed', 'columns', or
    None. For 'computed', value is the stat_type key (used to look up both
    the function and its required-column list). For 'columns', value is
    the list of nflverse columns to sum. reason is only meaningful when
    kind is None."""
    if not stat_type:
        return None, None, "unsupported_stat_type"
    key = stat_type.strip().lower()
    if key in COMPUTED_STAT_TYPES:
        return "computed", key, ""
    if key in COMPOSITE_STAT_TYPES:
        return "columns", COMPOSITE_STAT_TYPES[key], ""
    if key in NFL_STAT_TYPE_MAP:
        return "columns", [NFL_STAT_TYPE_MAP[key]], ""
    return None, None, "unsupported_stat_type"


def build_stat_series(
    weekly_df: pd.DataFrame, player_id: str, kind: str, value: object
) -> pd.Series:
    """Returns the player's per-game value for the target stat, across
    their REG-season games so far this season, sorted oldest to newest.
    Dispatches to either a straight column-sum (kind='columns') or a real
    scoring-formula function (kind='computed')."""
    games = weekly_df[weekly_df["player_id"] == player_id].sort_values("week")
    if games.empty:
        return pd.Series(dtype=float)

    if kind == "computed":
        stat_key = value
        required = _COMPUTED_STAT_REQUIRED_COLUMNS[stat_key]
        missing = [c for c in required if c not in games.columns]
        if missing:
            log.warning(
                "nflverse weekly data is missing columns required for computed "
                "stat '%s': %s", stat_key, missing,
            )
            return pd.Series(dtype=float)
        return COMPUTED_STAT_TYPES[stat_key](games)

    # kind == "columns"
    stat_cols = value
    for col in stat_cols:
        if col not in games.columns:
            log.warning("nflverse weekly data is missing expected column '%s'", col)
            return pd.Series(dtype=float)
    return games[stat_cols].sum(axis=1).reset_index(drop=True)


def season_average(series: pd.Series) -> Optional[float]:
    if series.empty:
        return None
    return float(series.mean())


def recent_form(series: pd.Series) -> Optional[float]:
    if series.empty:
        return None
    last_n = series.tail(len(RECENCY_WEIGHTS))
    weights = np.array(RECENCY_WEIGHTS[: len(last_n)])
    weights = weights / weights.sum()  # renormalize if fewer than 5 games
    # tail() preserves chronological order (oldest..newest); recency weights
    # are defined most-recent-first, so reverse before dotting.
    values = last_n.values[::-1]
    return float(np.dot(values, weights))


def sample_sigma(series: pd.Series, model_mean: float) -> float:
    """Sample standard deviation of the player's own game log for this
    stat. A sigma of (near) zero from only MIN_GAMES_FOR_ESTIMATE games is
    not trustworthy on its own (two similar games is not evidence of true
    zero variance), so a floor proportional to the mean is applied only in
    that narrow case."""
    if len(series) < 2:
        return float("nan")
    sigma = float(series.std(ddof=1))
    if len(series) == MIN_GAMES_FOR_ESTIMATE:
        floor = abs(model_mean) * SIGMA_FLOOR_FRACTION
        sigma = max(sigma, floor)
    return sigma


def normal_cdf(x: float) -> float:
    """Standard normal CDF via math.erf -- avoids adding scipy as a new
    project dependency for a single function."""
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def prob_over(line: float, mean: float, sigma: float) -> Optional[float]:
    if sigma is None or sigma != sigma or sigma <= 0:  # NaN-safe check
        return None
    z = (line - mean) / sigma
    return 1.0 - normal_cdf(z)


def implied_prob_over_underdog(over_mult: Optional[float], under_mult: Optional[float]) -> Optional[float]:
    """No-vig-style normalization of Underdog's per-side payout multipliers
    -- see module docstring's 'IMPLIED PROBABILITY' section."""
    if not over_mult or not under_mult or over_mult <= 0 or under_mult <= 0:
        return None
    raw_over = 1.0 / over_mult
    raw_under = 1.0 / under_mult
    total = raw_over + raw_under
    if total <= 0:
        return None
    return raw_over / total


PRIZEPICKS_ASSUMED_IMPLIED_PROB = 0.5  # stated, unverified assumption -- see docstring


# ---------------------------------------------------------------------------
# Main per-row processing
# ---------------------------------------------------------------------------
def process_props(props_df: pd.DataFrame, weekly_df: pd.DataFrame) -> pd.DataFrame:
    name_lookup = build_name_lookup(weekly_df)

    out_rows = []
    for _, prop in props_df.iterrows():
        row = prop.to_dict()
        sport = str(row.get("sport") or "").strip().lower()

        if sport not in NFL_SPORT_LABELS:
            row["model_status"] = "unsupported_sport"
            row.update(_blank_model_fields())
            out_rows.append(row)
            continue

        kind, value, reason = resolve_stat_spec(row.get("stat_type"))
        if kind is None:
            row["model_status"] = reason
            row.update(_blank_model_fields())
            out_rows.append(row)
            continue

        norm_name = normalize_name(row.get("player_name"))
        player_id = name_lookup.get(norm_name)
        if player_id is None:
            row["model_status"] = "no_player_match"
            row.update(_blank_model_fields())
            out_rows.append(row)
            continue

        series = build_stat_series(weekly_df, player_id, kind, value)
        if len(series) < MIN_GAMES_FOR_ESTIMATE:
            row["model_status"] = "insufficient_history"
            row.update(_blank_model_fields())
            row["games_used"] = len(series)
            out_rows.append(row)
            continue

        s_avg = season_average(series)
        r_form = recent_form(series)
        model_mean = SEASON_AVG_BLEND_WEIGHT * s_avg + RECENT_FORM_BLEND_WEIGHT * r_form
        sigma = sample_sigma(series, model_mean)

        line = row.get("line")
        p_over = prob_over(line, model_mean, sigma) if line is not None else None

        if row.get("platform") == "underdog":
            implied_over = implied_prob_over_underdog(
                row.get("over_payout_multiplier"), row.get("under_payout_multiplier")
            )
        elif row.get("platform") == "prizepicks":
            implied_over = PRIZEPICKS_ASSUMED_IMPLIED_PROB
        else:
            implied_over = None

        row["model_status"] = "estimated" if p_over is not None else "no_line_value"
        row["season_avg"] = s_avg
        row["recent_form"] = r_form
        row["model_mean"] = model_mean
        row["model_sigma"] = sigma
        row["games_used"] = len(series)
        row["prob_over"] = p_over
        row["prob_under"] = (1.0 - p_over) if p_over is not None else None
        row["implied_prob_over"] = implied_over
        row["implied_prob_under"] = (1.0 - implied_over) if implied_over is not None else None
        row["edge_over"] = (p_over - implied_over) if (p_over is not None and implied_over is not None) else None
        row["edge_under"] = (
            (row["prob_under"] - row["implied_prob_under"])
            if (row["prob_under"] is not None and row["implied_prob_under"] is not None)
            else None
        )
        out_rows.append(row)

    return pd.DataFrame(out_rows)


def _blank_model_fields() -> dict:
    return {
        "season_avg": None,
        "recent_form": None,
        "model_mean": None,
        "model_sigma": None,
        "games_used": None,
        "prob_over": None,
        "prob_under": None,
        "implied_prob_over": None,
        "implied_prob_under": None,
        "edge_over": None,
        "edge_under": None,
    }


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
def run(season: int) -> dict:
    log.info("=== Estimation run starting (season=%d) ===", season)

    if not NORMALIZED_LATEST.exists():
        raise FileNotFoundError(
            f"{NORMALIZED_LATEST} not found. Run scripts/ingestion/ingest_pickem.py "
            f"first (Session 2.2)."
        )
    props_df = pd.read_csv(NORMALIZED_LATEST)
    log.info("Loaded %d ingested props from %s", len(props_df), NORMALIZED_LATEST)

    weekly_df = fetch_nfl_weekly_stats(season)
    log.info("Loaded %d nflverse weekly-stat rows for season %d", len(weekly_df), season)

    result_df = process_props(props_df, weekly_df)

    status_counts = result_df["model_status"].value_counts(dropna=False).to_dict()
    log.info("Model status breakdown: %s", status_counts)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_path = OUTPUT_DIR / f"pickem_estimates_{timestamp}.csv"
    result_df.to_csv(out_path, index=False)
    log.info("Wrote %d rows to %s", len(result_df), out_path)

    return {
        "rows_in": len(props_df),
        "rows_out": len(result_df),
        "status_counts": status_counts,
        "output_path": str(out_path),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--season",
        type=int,
        required=True,
        help="NFL season year to pull nflverse weekly stats for (e.g. 2025).",
    )
    args = parser.parse_args()
    summary = run(args.season)
    print(summary)
