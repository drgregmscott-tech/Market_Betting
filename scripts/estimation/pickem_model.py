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
Session 2.22 addition: applies SIGMA_CALIBRATION_FACTOR (see the "SIGMA
CALIBRATION" note below) to every computed sigma, closing a real, measured
overconfidence gap found by Session 2.20's weekly_review.py against real
graded outcomes. No other model logic changed.
Session 2.25 addition: applies SIGMA_CALIBRATION_FACTOR_BY_STAT (see the
"SIGMA CALIBRATION" note below) as a per-stat override for 6 stat types
Session 2.24 found still miscalibrated past a 0.03 gap after the global
factor -- every other stat still falls back to the single global
SIGMA_CALIBRATION_FACTOR. No other model logic changed.

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
   across their REG-season games so far, scaled by
   SIGMA_CALIBRATION_FACTOR, or by a stat-specific override in
   SIGMA_CALIBRATION_FACTOR_BY_STAT when one exists for that
   row's resolved_stat_key (Session 2.22/2.25 -- see the "SIGMA
   CALIBRATION" section below). A player with fewer than 2
   qualifying games has no real sigma to compute; see
   MIN_GAMES_FOR_ESTIMATE below.

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

SIGMA CALIBRATION (Session 2.22)
---------------------------------
Session 2.20's weekly_review.py, run against real graded outcomes
(data/pickem/outcome_log.csv), found a persistent calibration gap: the
model's stated confidence averaged ~74% while real legs won ~67% of the
time -- a real, moderate overconfidence signal, not noise (see
SESSION_LOG.md Session 2.20 and 2.22 for the full evidence trail). This is
a sigma problem, not a blend-weight problem: sigma controls how extreme a
probability the normal CDF produces from a given z-score, independent of
which mean (season_avg vs recent_form) fed it. Session 2.22 fit a single
scalar multiplier, SIGMA_CALIBRATION_FACTOR, against the full real graded
sample (8,196 usable win/loss legs, 2026-09-15) by minimizing Brier score
between recalibrated probabilities and real outcomes -- see
scripts/calibration/fit_sigma_recalibration.py for the exact method and
data/pickem/sigma_recalibration_log.csv for the fit's own logged
result. The fitted value (1.61) closed the calibration gap from 0.0674 to
0.0008 on the same sample it was fit against. Every computed sample_sigma()
is multiplied by this factor before being used in prob_over(), UNLESS a
per-stat override applies (see below).

SESSION 2.24/2.25 ADDITION -- SIGMA_CALIBRATION_FACTOR_BY_STAT
------------------------------------------------------------------
The global fit above averages across every stat type combined -- Session
2.24 (scripts/calibration/pickem_calibration_by_stat.py) checked whether
that average was masking real per-stat-type miscalibration by re-running
the same z-recovery/Brier-score method grouped by resolved_stat_key. Of
18 stat types with enough graded volume (n>=20), 6 remained past a 0.03
gap even after the global 1.61 correction: rushing_tds, passing_
interceptions, completions, kicking points, passing_tds+rushing_tds+
receiving_tds, and fg_made. SIGMA_CALIBRATION_FACTOR_BY_STAT holds an
independently-fit k for each of those 6 (same Brier-minimizing grid
search, restricted to that stat's own graded legs), which REPLACES
SIGMA_CALIBRATION_FACTOR for that stat only -- every other stat, including
two that were flagged in the first pass but resolved on inspection
(targets: no real model edge on this stat, so no sigma multiplier applies;
rushing_yards+receiving_yards: its true best fit turned out to already sit
inside the global factor's own grid range, so the original flag was a
grid-search-ceiling artifact, not real miscalibration), keeps using the
single global factor. See SIGMA_CALIBRATION_FACTOR_BY_STAT's own inline
comments for the excluded-stats reasoning and per-stat n. These 6 values
have NOT been validated on held-out data -- they are a same-sample
Brier-minimizing fit, same caveat as the global factor's own fit, and the
smallest (rushing_tds, n=27) should be watched for drift as more legs
grade in, same as the global factor already is via weekly_review.py.
Also stated plainly: the grid search minimizes BRIER SCORE, not the mean
calibration gap directly, and those are not always minimized by the same
k. Two of the 6 -- completions (residual gap ~+0.09) and kicking points
(residual gap ~+0.05) -- still sit above the 0.03 threshold even at their
own individually-fit best k. Their per-stat override is still a real
improvement over the single global factor (which left them at +0.09/+0.08
respectively) and a genuinely better Brier score, but it should not be
read as "fully recalibrated" for those two specifically -- see
SESSION_LOG.md Session 2.25 for the exact numbers.
Re-fitting either the global or per-stat factors periodically as more real
outcomes accumulate (and, eventually, per-sport once other sports have
enough real graded volume of their own) is real future work -- see
data/pickem/sigma_recalibration_log.csv's own notes.

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
from pickem_sport_plugins import mlb as mlb_plugin_module
from season_utils import current_pickem_season

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
SIGMA_CALIBRATION_FACTOR = 1.61  # Session 2.22: fit against 8,196 real graded
# legs (data/pickem/outcome_log.csv, 2026-09-15) via
# scripts/calibration/fit_sigma_recalibration.py -- see the "SIGMA
# CALIBRATION" module docstring section above for the full derivation.

SIGMA_CALIBRATION_FACTOR_BY_STAT = {
    # Session 2.24: scripts/calibration/pickem_calibration_by_stat.py found
    # that SIGMA_CALIBRATION_FACTOR (1.61), fit globally, still leaves these
    # 6 resolved_stat_key groups miscalibrated past a 0.03 gap even after
    # the global correction is applied. Each value below REPLACES (does not
    # stack on top of) SIGMA_CALIBRATION_FACTOR for that stat -- it is an
    # independent per-stat fit against the same method (grid-search k
    # minimizing Brier score against real graded outcomes for that stat
    # only), not the global k further adjusted. See SESSION_LOG.md Session
    # 2.24/2.25 for the fit run and n per stat; data/pickem/outcome_log.csv
    # is the source. Any resolved_stat_key not listed here falls back to
    # SIGMA_CALIBRATION_FACTOR.
    #
    # Excluded from this table on purpose:
    # - "targets" (n=127): flagged, but its real win rate is ~50% -- the
    #   model has no real edge on this stat, so no sigma multiplier fixes
    #   it (pushing k toward infinity trivially shrinks the gap without
    #   improving Brier score). A sigma fix does not apply here.
    # - "rushing_yards+receiving_yards" (n=445): the widened-grid re-fit
    #   found its true optimum (k=3.095) already brings the gap under the
    #   0.03 threshold using the GLOBAL factor's own grid range -- it was a
    #   grid-search-ceiling artifact in the first pass, not real
    #   miscalibration, so it stays on the global 1.61.
    "rushing_tds": 0.610,  # n=27 -- smallest sample here; watch for drift
    "passing_interceptions": 0.825,  # n=63
    "completions": 1.595,  # n=43 -- best-Brier k still leaves ~+0.09 gap
    "kicking points": 2.100,  # n=186 -- best-Brier k still leaves ~+0.05 gap
    "passing_tds+rushing_tds+receiving_tds": 1.155,  # n=325
    "fg_made": 1.495,  # n=146
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
    every match).

    Session 2.15 fix: an entirely empty `stats_df` (a plug-in's fetch_stats
    returning zero rows -- a real, normal case pre-season, e.g. NBA's real
    plug-in before 2026-10, not an error) has no columns at all
    (`pd.DataFrame([])`), so `.sort_values("sort_key")` raised a KeyError
    before this guard. Returns an empty lookup instead -- every prop for
    that sport correctly falls through to model_status="insufficient_history"
    downstream, the same real, honest result a lookup miss already produces
    for one unmatched player, just for all of them."""
    if stats_df.empty:
        return {}
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
# These rows got an explicit, named gap (model_status="unsupported_odds_type")
# instead -- consistent with this project's "no unnamed black-box factors"
# rule -- rather than a fabricated edge that outranks real Standard-line
# flags.
#
# SESSION 2.21 FIX (2026-09-14, real finding): PrizePicks does not publish a
# static Demon/Goblin payout table anywhere (checked prizepicks.com's own
# payout page, its help center, and the raw ingestion API response itself --
# none carry a per-leg multiplier or implied probability for Demon/Goblin;
# PrizePicks' own help center confirms the multiplier is computed live,
# per-lineup, inside the app's entry builder, not published in advance). The
# only real number available is a live observation from the user's own
# PrizePicks account (2026-09-14): a real 3-pick Power Play entry made of 2
# Standard legs + 1 special leg paid 4.75x with that leg as Goblin, and 6.25x
# with the SAME leg as Demon (the all-Standard 3-pick baseline is the
# existing, separately-sourced 6.0x in sizing_engine.py's
# PICKEM_ENTRY_PAYOUT).
#
# Treating each leg's contribution to the entry multiplier as independent
# (the same equal-leg assumption sizing_engine.py's breakeven_win_rate_per_leg
# already uses for all-Standard entries), the two Standard legs' own per-leg
# breakeven is 6.0 ** (-1/3) = 0.550321. Solving M = 1 / (p_std**2 * p_special)
# for p_special at each observed M gives:
#   p_goblin = 1 / (4.75 * 0.550321**2) = 0.695143
#   p_demon  = 1 / (6.25 * 0.550321**2) = 0.528308
# (p_demon < p_std < p_goblin, matching the real-world direction: a Demon
# line needs to hit LESS often to break even, since it pays more; a Goblin
# line needs to hit MORE often, since it pays less -- see
# docs/sizing_methodology.md for the full derivation.)
#
# This rests on exactly ONE observed combination pattern (3-pick, 2 Standard
# + 1 special leg) -- it has not been confirmed to hold at other leg counts
# or other Standard/special mixes, so sizing_engine.py's entry-level payout
# table is extended ONLY for that exact pattern (see
# PRIZEPICKS_MIXED_ENTRY_PAYOUT there), not generalized further. The per-leg
# implied probabilities below are used here for individual-row scoring
# (edge/ranking), which is a coarser question than exact entry sizing and is
# reasonable to unblock on this evidence.
PRIZEPICKS_ODDS_TYPE_IMPLIED_PROB = {
    "demon": 0.5283083598231403,
    "goblin": 0.6951425787146582,
}

PRIZEPICKS_SCORABLE_ODDS_TYPES = {"standard", "demon", "goblin"}


def is_scorable_prizepicks_odds_type(row: dict) -> bool:
    if row.get("platform") != "prizepicks":
        return True
    odds_type = row.get("odds_type")
    if not isinstance(odds_type, str) or not odds_type.strip():
        return True  # missing odds_type -- treat as Standard, matching pre-fix behavior
    return odds_type.strip().lower() in PRIZEPICKS_SCORABLE_ODDS_TYPES


def prizepicks_implied_prob_over(row: dict) -> float:
    """PrizePicks implied probability for the Over/More side, by odds_type.
    Standard keeps the existing flat 50% assumption; Demon/Goblin use the
    real, sourced-from-live-account numbers in
    PRIZEPICKS_ODDS_TYPE_IMPLIED_PROB (see SESSION 2.21 FIX above)."""
    odds_type = row.get("odds_type")
    key = odds_type.strip().lower() if isinstance(odds_type, str) else ""
    return PRIZEPICKS_ODDS_TYPE_IMPLIED_PROB.get(key, PRIZEPICKS_ASSUMED_IMPLIED_PROB)


# SESSION 2.33 FIX (2026-09-16, real finding): PrizePicks' own
# attributes.allowed_wager_types on a projection states which side is
# actually buyable in the app -- observed real values "over" (Over/More
# only), "under_or_over" (both sides), or missing (no restriction stated).
# This is independent of odds_type: real Standard rows carry "over" too,
# not only Demon/Goblin. Before this, edge_over/edge_under were computed
# and flaggable on BOTH sides of every row regardless of this field, so
# the model could (and, confirmed live, did) surface "under" as the
# flagged side on a real over-only row -- a recommendation for a side
# that cannot be purchased on PrizePicks. Missing/None is treated as
# unrestricted (matches pre-fix behavior) since the API not stating a
# restriction is not evidence one exists.
PRIZEPICKS_OVER_ONLY_WAGER_TYPE = "over"
PRIZEPICKS_UNDER_ONLY_WAGER_TYPE = "under"


def prizepicks_side_is_buyable(row: dict, side: str) -> bool:
    """True unless PrizePicks' own allowed_wager_types explicitly rules
    `side` ("over" or "under") out for this row. Always True for
    non-PrizePicks rows and for rows with no stated restriction."""
    if row.get("platform") != "prizepicks":
        return True
    raw = row.get("allowed_wager_types")
    if not isinstance(raw, str) or not raw.strip():
        return True
    restriction = raw.strip().lower()
    if restriction == PRIZEPICKS_OVER_ONLY_WAGER_TYPE:
        return side == "over"
    if restriction == PRIZEPICKS_UNDER_ONLY_WAGER_TYPE:
        return side == "under"
    return True  # "under_or_over" or any other stated value -- both sides buyable


# ---------------------------------------------------------------------------
# SESSION 2.32 -- real-time MLB starter/lineup confirmation signal
# (Underdog gate, MLB only). See docs/research/underdog_pricing_gap_
# investigation.md (Session 2.31): Underdog's own per-side price on
# skewed ("chalk") lines reflects real, current lineup/starting-pitcher/
# injury information this model's season-average + recent-form blend does
# not have. This does NOT change edge_over/edge_under/prob_over for any
# row -- it attaches a new, purely informational column
# (`mlb_starter_status`) to MLB Underdog rows so a human (or a later,
# separate session, once real graded evidence exists) can see whether
# MLB's own confirmed lineup agrees with what the model assumed. No
# filtering or down-weighting happens here, per the roadmap card's
# explicit scope.
# ---------------------------------------------------------------------------
MLB_STARTER_STATUS_CONFIRMED = "confirmed"
MLB_STARTER_STATUS_DIFFERENT = "different_than_expected"
MLB_STARTER_STATUS_NOT_YET_CONFIRMED = "not_yet_confirmed"


def compute_mlb_starter_status(
    row: dict,
    player_id: str,
    schedule_cache: dict[str, list[dict]],
    lineup_cache: dict[object, Optional[dict]],
) -> Optional[str]:
    """Session 2.32. Compares one MLB Underdog prop's player against MLB
    Stats API's real, current probable-pitcher + confirmed-lineup data for
    their real scheduled game. Returns one of:
      - MLB_STARTER_STATUS_CONFIRMED: the player IS in the real confirmed
        batting order (a hitter prop), or IS the real confirmed starting
        pitcher matching MLB's own probable-pitcher signal (a pitcher
        prop, first entry of that side's real `pitchers` usage list).
      - MLB_STARTER_STATUS_DIFFERENT: a real confirmed lineup exists for
        this game, but this player is NOT in it (a real scratch) or the
        real confirmed starter differs from the schedule's probable
        pitcher -- the real "Underdog had news, here it is" case this
        session exists to surface.
      - MLB_STARTER_STATUS_NOT_YET_CONFIRMED: MLB has not posted a real
        lineup for this game yet at estimation time -- an honest "we
        don't know yet" state, never conflated with "confirmed clean".
      - None: this prop could not be resolved to a real scheduled MLB
        game at all (unparseable game_start_time/game_matchup, or no
        schedule match found) -- a real, separate gap, not a verdict.
    `schedule_cache`/`lineup_cache` are the caller's per-run caches (see
    process_props()) so a run with many props on the same date/game only
    fetches each real schedule/lineup once.
    """
    matchup = row.get("game_matchup")
    start_time = row.get("game_start_time")
    if not isinstance(matchup, str) or "@" not in matchup:
        return None
    if not isinstance(start_time, str) or len(start_time) < 10:
        return None
    game_date = start_time[:10]  # ISO date prefix, e.g. "2026-09-15"
    away_label, _, home_label = matchup.partition("@")
    away_label, home_label = away_label.strip(), home_label.strip()
    if not away_label or not home_label:
        return None

    try:
        pid = int(player_id)
    except (TypeError, ValueError):
        return None

    if game_date not in schedule_cache:
        schedule_cache[game_date] = mlb_plugin_module.fetch_schedule_games(game_date)
    games = schedule_cache[game_date]

    game = mlb_plugin_module.find_scheduled_game(games, away_label, home_label)
    if game is None:
        return None

    game_pk = game.get("gamePk")
    if game_pk not in lineup_cache:
        lineup_cache[game_pk] = mlb_plugin_module.fetch_confirmed_lineup(game_pk)
    lineup = lineup_cache[game_pk]

    if lineup is None:
        return MLB_STARTER_STATUS_NOT_YET_CONFIRMED

    for side_key in ("away", "home"):
        if pid in lineup[side_key]["batting_order"]:
            return MLB_STARTER_STATUS_CONFIRMED

    for side_key, probable_key in (
        ("away", "away_probable_pitcher_id"),
        ("home", "home_probable_pitcher_id"),
    ):
        if game.get(probable_key) == pid:
            confirmed_pitchers = lineup[side_key]["pitchers"]
            if not confirmed_pitchers:
                return MLB_STARTER_STATUS_NOT_YET_CONFIRMED
            return (
                MLB_STARTER_STATUS_CONFIRMED
                if confirmed_pitchers[0] == pid
                else MLB_STARTER_STATUS_DIFFERENT
            )

    # A confirmed lineup exists for this game, but this specific player is
    # in neither side's real confirmed batting order nor is either side's
    # real probable pitcher -- a real scratch/bench/unconfirmed-role case.
    return MLB_STARTER_STATUS_DIFFERENT


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
    # SESSION 2.32 -- per-run caches for the MLB starter/lineup confirmation
    # signal (see compute_mlb_starter_status() above), keyed by real
    # calendar date / real gamePk so a run with many MLB Underdog props on
    # the same date/game only fetches each real schedule/lineup once.
    mlb_schedule_cache: dict[str, list[dict]] = {}
    mlb_lineup_cache: dict[object, Optional[dict]] = {}

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
        # SESSION 2.32 -- default for every row; only ever overwritten below
        # for an MLB Underdog row with a resolved player_id (see "no
        # unnamed black-box factors" / "leave blank, not fabricated" rule
        # applied the same way _blank_model_fields() already does for the
        # existing model columns).
        row["mlb_starter_status"] = None
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

        # SESSION 2.32 -- computed here, independent of downstream model
        # math, so it's present regardless of whether this row ends up
        # "estimated", "insufficient_history", or "no_line_value" below.
        # Scoped to MLB Underdog rows only, per the roadmap card -- every
        # other row keeps the row["mlb_starter_status"] = None default set
        # above.
        if plugin.name == "mlb" and row.get("platform") == "underdog":
            row["mlb_starter_status"] = compute_mlb_starter_status(
                row, player_id, mlb_schedule_cache, mlb_lineup_cache
            )

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
        if sigma == sigma:  # NaN-safe: NaN sigma stays NaN, prob_over() handles it
            calibration_factor = SIGMA_CALIBRATION_FACTOR_BY_STAT.get(
                row["resolved_stat_key"], SIGMA_CALIBRATION_FACTOR
            )
            sigma *= calibration_factor

        line = row.get("line")
        p_over = prob_over(line, model_mean, sigma) if line is not None else None

        if row.get("platform") == "underdog":
            implied_over = implied_prob_over_underdog(
                row.get("over_payout_multiplier"), row.get("under_payout_multiplier")
            )
        elif row.get("platform") == "prizepicks":
            implied_over = prizepicks_implied_prob_over(row)
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
        row["edge_over"] = (
            (p_over - implied_over)
            if (p_over is not None and implied_over is not None and prizepicks_side_is_buyable(row, "over"))
            else None
        )
        row["edge_under"] = (
            (row["prob_under"] - row["implied_prob_under"])
            if (
                row["prob_under"] is not None
                and row["implied_prob_under"] is not None
                and prizepicks_side_is_buyable(row, "under")
            )
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
        default=None,
        help="Season year to pull each sport plug-in's stats for (e.g. 2025). "
        "Defaults to the real current season (see season_utils.py) rather "
        "than a hardcoded year, so this never silently goes stale.",
    )
    args = parser.parse_args()
    season = args.season if args.season is not None else current_pickem_season()
    summary = run(season)
    print(summary)
