"""
Session 2.3 -- Estimation Engine v1 (Fixed-Line Pick'em Platforms)
Session 2.4 addition: added `resolved_stat_key` to the output row (see the
"SESSION 2.4 ADDITION" note below the module docstring) -- no other logic
in this file changed.
Session 2.12 addition: refactored the previously NFL-hardcoded stats-source
and stat-type-map logic into a per-sport plug-in shape (see
pickem_sport_plugins/__init__.py). NFL scoring behavior is unchanged --
proven byte-for-byte via test_pickem_model.py's regression fixture, not just
re-derived. See the "SESSION 2.12 REFACTOR" note below for what moved where.

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

SESSION 2.4 ADDITION -- resolved_stat_key
------------------------------------------
PrizePicks and Underdog use different raw stat_type strings for the same
real-world stat (e.g. PrizePicks "Pass Yards" vs. an Underdog variant of the
same wording). This script already resolves that raw string down to one
canonical nflverse column (or computed-formula name) internally via
resolve_stat_spec(), but v1 never wrote that canonical value out -- only the
original per-platform stat_type string survived to the output row. Session
2.4's CLV logger needs to match the SAME real-world prop across both
platforms (e.g. "is this PrizePicks Patrick Mahomes passing-yards prop the
same real prop as this Underdog Patrick Mahomes passing-yards prop"), and
matching on the raw stat_type text alone is unreliable, since the two
platforms don't always word it the same way. `resolved_stat_key` is a new
output column carrying that canonical value (e.g. "passing_yards", or
"rushing_yards+receiving_yards" for a composite, or "kicking points" for a
computed formula) whenever the stat was resolvable -- None otherwise. This
is a purely additive change: no existing column was removed, renamed, or
recalculated differently.

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
1. season_avg -- mean of the relevant stat across the player's REG-season
   games so far this season.
2. recent_form -- recency-weighted average of the player's last 5 REG-
   season games (weights: 0.35/0.25/0.20/0.12/0.08, most
   recent game first -- identical weighting to
   projections_baseline.py's RECENCY_WEIGHTS, renormalized
   if the player has fewer than 5 games so far).
3. model_mean -- blend of the two above: 50% season_avg / 50%
   recent_form. A flat 50/50 blend is the simplest
   defensible starting point for a v1 model; it is not
   claimed to be optimal, and re-weighting this blend
   against real graded outcomes is explicitly the kind of
   work Session 8.3 (Ongoing Recalibration Cadence) exists
   to do later, once real CLV/outcome data exists to tune
   against (Sessions 2.4/2.5).
4. model_sigma -- the player's own sample standard deviation of the stat
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
  visible row, not a dropped one.
- No opponent/matchup adjustment, no injury/role status, no home/away
  split, no pace/usage adjustment.
- No weather input for outdoor games.
- The computed "Fantasy Score" stat deliberately omits two components of
  PrizePicks' own official scoring table -- Offensive Fumble Recovery TDs
  and Kick/Punt/Field Goal Return TDs (6 points each) -- because nflverse's
  closest-named columns for these were checked directly against real data
  and do not reliably correspond.
- The "implied probability" used for PrizePicks rows is a stated
  assumption (flat 50%), not a verified figure.

IMPLIED PROBABILITY -- HOW IT IS COMPUTED, AND THE ASSUMPTION IT RESTS ON
-----------------------------------------------------------------------
Underdog's normalized rows carry over_payout_multiplier / under_payout_
multiplier. Treating those multipliers as fair-odds (payout * true win
probability = 1 at breakeven) gives:
  implied_prob_over = (1 / over_multiplier) / (1/over_multiplier + 1/under_multiplier)
  implied_prob_under = 1 - implied_prob_over

PrizePicks' normalized rows do NOT carry per-side multipliers. In the
absence of a captured per-side number, this script assumes a flat 50%
implied probability on both sides for PrizePicks rows. This is a STATED,
UNVERIFIED assumption, not a confirmed industry figure.

SESSION 2.5 CLARIFICATION -- 50% here is NOT a claimed real breakeven
------------------------------------------------------------------------
This 50% answers a narrow, specific question: "is this prop interesting
enough to flag at all?" It is a flagging-sensitivity threshold, chosen for
maximum sensitivity at the point a prop is evaluated -- BEFORE any real
entry type (2-pick, 3-pick, 4-pick, Flex) has been chosen for it, since
that choice happens downstream, when entries are actually assembled.

This is a DIFFERENT question from "what real win rate does a specific
PrizePicks entry type need to break even?" -- that real breakeven is
entry-type-specific (e.g. a 2-pick Power Play's real breakeven, derived
from PrizePicks' own published 3x payout, is sqrt(1/3) ~= 57.7%, not 50% --
see docs/sample_size_methodology.md, Section 2). Applying an entry-type
breakeven like 57.7% HERE, upstream of entry selection, would be just as
wrong as 50% is for describing real breakeven -- a different flagged leg
could end up in a different entry type with a different real breakeven.
Real breakeven economics belong in Session 2.6 (Bankroll & Sizing Logic),
once a specific entry type is actually being sized -- not in this file.

See docs/clv_methodology.md's own "Session 2.5" section for the full
explanation of why these are two different numbers, not one figure with an
error in it. No code in this file changed as a result of this
clarification -- it exists solely to prevent this same confusion from
recurring in a future session.

SESSION 2.12 REFACTOR -- what moved where
------------------------------------------
Everything that was NFL-specific (the nflverse fetch, NFL_STAT_TYPE_MAP,
COMPOSITE_STAT_TYPES, COMPUTED_STAT_TYPES, and the two PrizePicks scoring
formulas) moved to pickem_sport_plugins/nfl.py, unchanged, as this project's
first SportPlugin. What stays in THIS file is the sport-agnostic part: the
season-avg / recent-form / sigma / normal-CDF scoring math (untouched), and
a generic process_props() loop that looks up the right plug-in per row via
pickem_sport_plugins.plugin_for_sport() instead of hardcoding NFL. Adding a
new sport (Sessions 2.13+) means adding a new plug-in file under
pickem_sport_plugins/, not touching this file's core loop. See
pickem_sport_plugins/__init__.py for the plug-in contract and
test_pickem_model.py for the regression proof that NFL output is unchanged.

USAGE
-----
pip install pandas numpy pyarrow requests --break-system-packages
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
from typing import Optional

import numpy as np
import pandas as pd

from pickem_sport_plugins import SportPlugin, plugin_for_sport

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parents[2]
NORMALIZED_LATEST = BASE_DIR / "data" / "pickem" / "normalized" / "latest.csv"
OUTPUT_DIR = BASE_DIR / "output" / "estimation"
LOG_PATH = BASE_DIR / "logs" / "estimation.log"

# ---------------------------------------------------------------------------
# Model constants -- named here, explicitly, per this project's "no
# unnamed black-box factors" documentation standard. Sport-agnostic: these
# apply identically regardless of which plug-in produced the per-game
# stat series (see SESSION 2.12 REFACTOR note above).
# ---------------------------------------------------------------------------
RECENCY_WEIGHTS = [0.35, 0.25, 0.20, 0.12, 0.08]
SEASON_AVG_BLEND_WEIGHT = 0.5
RECENT_FORM_BLEND_WEIGHT = 0.5
MIN_GAMES_FOR_ESTIMATE = 2  # below this, sigma is not meaningfully estimable
SIGMA_FLOOR_FRACTION = 0.15  # sigma floor, as a fraction of the mean, used
# only when a player has exactly MIN_GAMES_FOR_ESTIMATE games and their
# observed sample sigma is implausibly small (near-zero) -- prevents a
# probability estimate of ~100%/~0% off two coincidentally similar games.

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
# Name normalization / matching
# ---------------------------------------------------------------------------
def normalize_name(name: Optional[str]) -> str:
    """Lowercases, strips punctuation and common suffixes (Jr/Sr/II/III/IV),
    and collapses whitespace, so the same real player matches across two
    platforms' different name formatting."""
    if not name or not isinstance(name, str):
        return ""
    cleaned = re.sub(r"[.\-']", " ", name.lower())
    cleaned = re.sub(r"[^a-z0-9\s]", "", cleaned)
    tokens = [t for t in cleaned.split() if t not in NAME_SUFFIXES]
    return " ".join(tokens).strip()


def build_name_lookup(stats_df: pd.DataFrame) -> dict[str, str]:
    """Builds normalized_name -> player_id, using each player's MOST RECENT
    name on record (sorted by the plug-in's `sort_key` column -- see the
    fetch_stats contract in pickem_sport_plugins/__init__.py). Uses
    `player_display_name`, NOT any abbreviated name column a source might
    also carry (see Session 2.3 notes on nflverse's own `player_name` vs.
    `player_display_name` -- the abbreviated form silently broke almost
    every match)."""
    most_recent = (
        stats_df.sort_values("sort_key")
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
def resolve_stat_spec(
    plugin: SportPlugin, stat_type: Optional[str]
) -> tuple[Optional[str], object, str]:
    """Returns (kind, value, reason). kind is 'computed', 'columns', or
    None. For 'computed', value is the stat_type key. For 'columns', value
    is the list of that plug-in's stats-source columns to sum. reason is
    only meaningful when kind is None. Looks the stat_type up against the
    given plug-in's own stat_type_map / composite_stat_types /
    computed_stat_types -- generic across sports (see SESSION 2.12
    REFACTOR note in this module's docstring)."""
    # FIX (2026-09-02, surfaced by Open Decision #11's fix): the old check
    # `if not stat_type` correctly catches a real Python None, but pandas
    # represents a genuinely blank/missing cell as NaN -- a float -- and
    # `not float('nan')` is False in Python, so a NaN slipped past this
    # check and crashed on `.strip()` below with
    # "AttributeError: 'float' object has no attribute 'strip'". This did
    # not happen before Open Decision #11's ingestion fix because rows
    # with no resolved sport were discarded upstream before ever reaching
    # this function; now that real NFL/tennis rows resolve a sport
    # correctly, some of them carry a genuinely missing stat_type and
    # reach here for the first time. Checking `isinstance(stat_type, str)`
    # catches None, NaN, and any other non-string value the same way,
    # and reports it through the same "unsupported_stat_type" reason this
    # function already uses for a plain missing value -- consistent with
    # this project's "every unsupported stat type is named, not dropped"
    # rule, and critically: a bad stat_type on one row must never crash
    # the whole batch again.
    if not isinstance(stat_type, str) or not stat_type.strip():
        return None, None, "unsupported_stat_type"
    key = stat_type.strip().lower()
    if key in plugin.computed_stat_types:
        return "computed", key, ""
    if key in plugin.composite_stat_types:
        return "columns", plugin.composite_stat_types[key], ""
    if key in plugin.stat_type_map:
        return "columns", [plugin.stat_type_map[key]], ""
    return None, None, "unsupported_stat_type"


def resolved_stat_key_for(kind: Optional[str], value: object) -> Optional[str]:
    """SESSION 2.4 ADDITION. Turns the (kind, value) pair from
    resolve_stat_spec() into one canonical, human-readable string that means
    the same real-world stat regardless of which platform's wording produced
    it -- e.g. ("columns", ["rushing_yards", "receiving_yards"]) becomes
    "rushing_yards+receiving_yards"; ("computed", "kicking points") becomes
    "kicking points". Returns None if the stat wasn't resolvable at all.
    This is the join key Session 2.4's CLV logger uses to recognize the same
    real prop posted independently on PrizePicks and Underdog."""
    if kind == "computed":
        return str(value)
    if kind == "columns":
        return "+".join(value)
    return None


def build_stat_series(
    plugin: SportPlugin, stats_df: pd.DataFrame, player_id: str, kind: str, value: object
) -> pd.Series:
    """Returns the player's per-game value for the target stat, across
    their season so far, sorted oldest to newest by the plug-in's
    `sort_key` column. Generic across sports -- reads the computed-formula
    function and its required columns from the given plug-in rather than a
    hardcoded NFL dict (see SESSION 2.12 REFACTOR note in this module's
    docstring).

    SESSION 2.13 FIX -- a multi-game-log player (real example: Shohei
    Ohtani, whose MLB plug-in row set includes both his real hitting AND
    real pitching game logs under the same player_id, each with its own
    `sort_key` starting at 1 -- see pickem_sport_plugins/mlb.py) previously
    had EVERY one of his rows summed together for any stat request, not
    just the rows from the relevant game log. A hitting-stat query (e.g.
    Home Runs) silently included his pitching rows too -- pandas'
    .sum(axis=1) treats a NaN cell (his pitching rows have no `homeRuns`
    value at all) as 0 rather than excluding the row, so the SUM came out
    right but the row COUNT did not (his real 130 hitting games plus 14
    unrelated pitching games = 144, diluting season_average), and
    recent_form's "last 5 by sort_key" could mix real batting games with
    real pitching games that happen to share a sort_key, since the two
    logs each restart their own sort_key at 1. Confirmed live against
    Ohtani's real 2026 data before this fix (Home Runs season_average came
    out 30/144 = 0.208 instead of the real 30/130 = 0.231). Dropping rows
    where the requested stat's own columns are entirely absent -- i.e. rows
    from a DIFFERENT game log than the one this stat actually belongs to --
    before summing/computing fixes this for every current and future
    plug-in that might fetch more than one game-log type per player, not
    just MLB."""
    games = stats_df[stats_df["player_id"] == player_id].sort_values("sort_key")
    if games.empty:
        return pd.Series(dtype=float)

    if kind == "computed":
        stat_key = value
        required = plugin.computed_required_columns[stat_key]
        missing = [c for c in required if c not in games.columns]
        if missing:
            log.warning(
                "%s stats data is missing columns required for computed "
                "stat '%s': %s", plugin.name, stat_key, missing,
            )
            return pd.Series(dtype=float)
        games = games.dropna(subset=required, how="all")
        if games.empty:
            return pd.Series(dtype=float)
        return plugin.computed_stat_types[stat_key](games)

    # kind == "columns"
    stat_cols = value
    for col in stat_cols:
        if col not in games.columns:
            log.warning("%s stats data is missing expected column '%s'", plugin.name, col)
            return pd.Series(dtype=float)
    games = games.dropna(subset=stat_cols, how="all")
    if games.empty:
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
    values = last_n.values[::-1]
    return float(np.dot(values, weights))


def sample_sigma(series: pd.Series, model_mean: float) -> float:
    """Sample standard deviation of the player's own game log for this
    stat. A floor proportional to the mean is applied only when exactly
    MIN_GAMES_FOR_ESTIMATE games are available and the observed sigma is
    implausibly small."""
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
    """No-vig-style normalization of Underdog's per-side payout multipliers."""
    if not over_mult or not under_mult or over_mult <= 0 or under_mult <= 0:
        return None
    raw_over = 1.0 / over_mult
    raw_under = 1.0 / under_mult
    total = raw_over + raw_under
    if total <= 0:
        return None
    return raw_over / total


PRIZEPICKS_ASSUMED_IMPLIED_PROB = 0.5  # stated, unverified assumption -- see docstring

# FIX (2026-09-11, real finding): PRIZEPICKS_ASSUMED_IMPLIED_PROB is only
# defensible for a Standard-odds line. PrizePicks also offers "demon" (harder)
# and "goblin" (easier) alt-lines on the same player/stat at real, different
# payout multipliers this project's ingestion does not capture -- confirmed
# live, e.g. Edgerrin Cooper's real Sacks props included a 0.5 AND a 1.5 line,
# both tagged odds_type="demon", simultaneously. Scoring a Demon/Goblin line
# against a flat 50% "implied" breakeven is not a rounding error: a Demon line
# is deliberately set at an easy bar, so the model's own true-probability
# estimate on it is naturally close to 100%, which manufactures an edge that
# caps out just under 50% regardless of whether the line is really mispriced.
# These rows get an explicit, named gap (model_status="unsupported_odds_type")
# instead -- consistent with this project's "no unnamed black-box factors"
# rule -- rather than a fabricated edge that outranks real Standard-line
# flags. Re-enabling scoring for these requires PrizePicks' real per-type
# payout multipliers, which are not in this response.
PRIZEPICKS_SCORABLE_ODDS_TYPES = {"standard"}


def is_scorable_prizepicks_odds_type(row: dict) -> bool:
    if row.get("platform") != "prizepicks":
        return True
    odds_type = row.get("odds_type")
    if not isinstance(odds_type, str) or not odds_type.strip():
        return True  # missing odds_type -- treat as Standard, matching pre-fix behavior
    return odds_type.strip().lower() in PRIZEPICKS_SCORABLE_ODDS_TYPES


# ---------------------------------------------------------------------------
# Main per-row processing
# ---------------------------------------------------------------------------
def process_props(props_df: pd.DataFrame, season: int) -> pd.DataFrame:
    """Generic across every registered sport plug-in (see SESSION 2.12
    REFACTOR note in this module's docstring). A plug-in's fetch_stats() and
    the resulting name lookup are pulled lazily and cached per plug-in, so a
    run only fetches stats for sports actually present in props_df."""
    stats_cache: dict[str, pd.DataFrame] = {}
    lookup_cache: dict[str, dict[str, str]] = {}

    def get_stats_and_lookup(plugin: SportPlugin) -> tuple[pd.DataFrame, dict[str, str]]:
        if plugin.name not in stats_cache:
            stats_df = plugin.fetch_stats(season)
            log.info(
                "Loaded %d %s stat rows for season %d", len(stats_df), plugin.name, season
            )
            stats_cache[plugin.name] = stats_df
            lookup_cache[plugin.name] = build_name_lookup(stats_df)
        return stats_cache[plugin.name], lookup_cache[plugin.name]

    out_rows = []
    for _, prop in props_df.iterrows():
        row = prop.to_dict()
        sport = str(row.get("sport") or "").strip().lower()
        plugin = plugin_for_sport(sport)

        if plugin is None:
            row["model_status"] = "unsupported_sport"
            row["resolved_stat_key"] = None
            row.update(_blank_model_fields())
            out_rows.append(row)
            continue

        if not is_scorable_prizepicks_odds_type(row):
            row["model_status"] = "unsupported_odds_type"
            row["resolved_stat_key"] = None
            row.update(_blank_model_fields())
            out_rows.append(row)
            continue

        kind, value, reason = resolve_stat_spec(plugin, row.get("stat_type"))
        if kind is None:
            row["model_status"] = reason
            row["resolved_stat_key"] = None
            row.update(_blank_model_fields())
            out_rows.append(row)
            continue

        # SESSION 2.4 ADDITION: record the canonical stat key as soon as it
        # resolves, regardless of what happens later in this row (player
        # match failure, insufficient history, etc.) -- the fact that the
        # stat itself was resolvable is real information Session 2.4's CLV
        # matcher can still use.
        row["resolved_stat_key"] = resolved_stat_key_for(kind, value)

        stats_df, name_lookup = get_stats_and_lookup(plugin)

        norm_name = normalize_name(row.get("player_name"))
        player_id = name_lookup.get(norm_name)
        if player_id is None:
            row["model_status"] = "no_player_match"
            row.update(_blank_model_fields())
            out_rows.append(row)
            continue

        series = build_stat_series(plugin, stats_df, player_id, kind, value)
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

    # Per-plug-in stats fetching happens lazily inside process_props() now
    # (see SESSION 2.12 REFACTOR note in this module's docstring) -- only
    # sports actually present in props_df get fetched.
    result_df = process_props(props_df, season)

    status_counts = result_df["model_status"].value_counts(dropna=False).to_dict()
    log.info("Model status breakdown: %s", status_counts)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_path = OUTPUT_DIR / f"pickem_estimates_{timestamp}.csv"
    result_df.to_csv(out_path, index=False)
    log.info("Wrote %d rows to %s", len(result_df), out_path)

    # ADDITION (2026-09-02, visibility-gap fix): also write a fixed-name
    # latest.csv, overwritten every run -- same pattern ingest_pickem.py
    # already uses for data/pickem/normalized/latest.csv. The timestamped
    # file above is kept for local history but is NOT committed to GitHub
    # (same as ingestion's own timestamped snapshots); committing a new
    # ~26,000-row file every hour would grow the repo without bound.
    # latest.csv is the one path the pipeline workflow commits, so this
    # stage's real, row-by-row output (including per-row model_status and
    # computed edge -- e.g. for Underdog rows) becomes something that can
    # actually be checked after the fact, instead of only being visible on
    # a GitHub Actions runner that's already gone by the next run.
    latest_path = OUTPUT_DIR / "latest.csv"
    result_df.to_csv(latest_path, index=False)
    log.info("Wrote %d rows to %s", len(result_df), latest_path)

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
        help="Season year to pull each sport plug-in's stats for (e.g. 2025).",
    )
    args = parser.parse_args()
    summary = run(args.season)
    print(summary)
