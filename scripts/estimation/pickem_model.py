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
Session 2.41c addition: re-fit both SIGMA_CALIBRATION_FACTOR (1.61 -> 2.681)
and SEASON_AVG_BLEND_WEIGHT/RECENT_FORM_BLEND_WEIGHT (0.5/0.5 -> 0.9/0.1)
against the current, clean, post-2026-09-17-dedup-fix outcome_log.csv --
the first real fit either constant has received since Session 2.22/2.24's
original fits, which predate that fix. See the "SIGMA CALIBRATION" and
"BLEND WEIGHT" notes below for the full derivation and real caveats.

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

SESSION 2.41c ADDITION -- RE-FIT ON CLEAN, POST-DEDUP-FIX, POST-ISOTONIC DATA
--------------------------------------------------------------------------------
The 1.61 value above was fit 2026-09-15, BEFORE the 2026-09-17 dedup/closing-
line fix (Session 2.37) and before Session 2.40's isotonic calibration
existed. Both are real reasons the original fit could no longer be trusted
as current: the dedup fix changed which legs even exist in outcome_log.csv,
and isotonic calibration means 12 stat types' stored first_flagged_model_prob
is no longer a plain normal_cdf(z/factor) value at all for legs flagged after
Session 2.40 shipped (recovering a "z" from an isotonic-calibrated
probability is not meaningful). Session 2.41c
(scripts/calibration/fit_sigma_recalibration.py, re-run unchanged) refit
against the clean, current, post-fix outcome_log.csv, EXCLUDING both the 12
isotonic-covered stats and the 6 SIGMA_CALIBRATION_FACTOR_BY_STAT stats (each
already handled by its own independent path -- mixing them into a single
global fit would let 18% of the sample distort the other ~30+ stats' shared
factor) -- 18,766 usable legs. Result: fitted multiplier k=1.665 on top of
the existing 1.61 (i.e. the model was STILL meaningfully overconfident even
after the original fix), giving a new global factor of 1.61 * 1.665 = 2.681.
This closed the calibration gap from 0.0594 to 0.0151 on this clean sample --
a real, large improvement, though not as tight as Session 2.22's original
0.0008 (Brier-minimizing k does not always fully zero the mean gap; the
residual 0.0151 is itself evidence sigma alone cannot fully fix every
remaining stat -- see fit history in data/pickem/sigma_recalibration_log.csv).
This REPLACES 1.61 as the production global factor. The 6-stat
SIGMA_CALIBRATION_FACTOR_BY_STAT table below was fit independently and is
untouched by this session; re-checking it against the new global default is
scripts/calibration/pickem_calibration_by_stat.py's own job (see that
script's Session 2.41c exclusion note), not this fit.

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

BLEND WEIGHT (Session 2.41c)
-----------------------------
SEASON_AVG_BLEND_WEIGHT/RECENT_FORM_BLEND_WEIGHT had been a flat, never-
empirically-tested 50/50 since this model's first version -- a real,
separate gap from sigma (the blend weight controls WHICH mean feeds
prob_over(), not how extreme the resulting probability is; see "SIGMA
CALIBRATION" above for why that's a different problem). Session 2.41c
(scripts/calibration/fit_blend_weight.py, new) fit it for the first time
against real graded outcomes. This needed a different data source than the
sigma fit: outcome_log.csv/clv_log.csv never stored season_avg/recent_form
as two separate numbers, only the final blended probability -- so this
script joins each graded leg back to whichever RETAINED
output/estimation/pickem_estimates_*.csv snapshot covers its flag date (35
files survived locally, 2026-08-31 through 2026-09-16 -- a real, smaller,
non-uniform sample than the sigma fit's, stated plainly, not glossed over)
to recover the two real component means, matched at day granularity (the
underlying player game log only changes once real games finish, not
intra-day -- confirmed directly before relying on this, see that script's
own docstring). Same exclusion as the sigma fit above (12 isotonic-covered +
6 per-stat-override stats) applied for consistency. Result, on 9,170 joined
clean legs: Brier score fell steadily from w=0.0 (0.2454) to an interior
minimum at w=0.95 (0.2244) -- recent_form contributes only a small residual
amount of value on this real sample, a genuinely surprising result for a
component that had been trusted at equal weight since v1. Checked by sport
before trusting the pooled number: MLB (n=8,057, 88% of the sample) alone
prefers w=1.0 (recent_form contributes nothing), NFL (n=731) prefers w=0.8,
FIFA (n=222) w=0.65 -- all meaningfully above 0.5, consistent in direction
even though the exact optimum varies by sport; only SOCCER (n=143, the
smallest usable group) disagreed (w=0.0). SEASON_AVG_BLEND_WEIGHT = 0.95 is
the literal pooled-fit optimum, not a hand-softened compromise -- it is an
interior grid point, not a boundary result, so no extra shrinkage was
applied on top of it.
Real, honest caveat, same as the sigma fit's: this recomputes probabilities
directly from season_avg/recent_form/model_sigma (not via inverse_normal_cdf
of a stored probability), so it is NOT distorted by isotonic calibration the
way a naive re-run of the sigma-fit method would be -- but a real ~0.029
mean absolute gap between this script's recomputed w=0.5 probability and the
actual stored first_flagged_model_prob for the same rows (its own built-in
sanity check) means the reconstruction is close but not exact, most likely
from the SIGMA_FLOOR_FRACTION mean-dependence not being re-derived per
counterfactual w (see that script's own docstring) -- a real, second-order
approximation, not hidden. This is in-sample fit only, not held-out
validated (Session 2.40/2.42's stricter standard) -- worth a held-out check
in a future session, same as the sigma factor's own open item. Re-run
periodically as more snapshots survive and more legs grade in, same cadence
as the sigma fit.

SHRINKAGE (Session 2.42)
-------------------------
MIN_GAMES_FOR_ESTIMATE = 2 means a player with exactly 2 games has their raw
sample mean/sigma trusted exactly as much as a player with 15 -- real,
professional sports-projection systems instead shrink a thin-sample player's
mean toward a league average, weighted by real sample size, because a raw
small-sample average is known to be an unreliable estimate of true talent
(2026-09-17 research finding -- see ROADMAP.md Session 2.42). This is a
mean-side correction, independent of SIGMA_CALIBRATION_FACTOR (which
controls how extreme the resulting probability is, not which mean feeds it
-- same distinction the "BLEND WEIGHT" section above draws for
SEASON_AVG_BLEND_WEIGHT) and independent of isotonic calibration (which
recalibrates a probability's SHAPE downstream of whatever mean produced it).

compute_league_average() computes, per resolved_stat_key, the mean of every
qualifying player's own season_average() for that stat (equal weight per
player), using data every sport plug-in already fetches -- no new data
source. apply_shrinkage() blends the model's existing blended mean
(season_avg/recent_form) toward that league average, weighted by the
player's own games_used via shrunk_mean = (n/(n+k)) * raw_mean + (k/(n+k)) *
league_avg -- k = SHRINKAGE_PRIOR_STRENGTH_K, fit against real graded
outcomes by scripts/calibration/fit_shrinkage.py (same Brier-minimizing
grid-search method as SIGMA_CALIBRATION_FACTOR's own fit), with a real
temporal held-out validation (Session 2.40's method) before being wired in.
Every scored row carries model_mean_pre_shrinkage, league_avg, and
shrinkage_weight -- visible, so it is always possible to see whether/how
much shrinkage was applied to a given row, never a hidden adjustment. See
SHRINKAGE_PRIOR_STRENGTH_K's own inline comment and SESSION_LOG.md Session
2.42 for the fit result and whether it validated.

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
from pickem_sport_plugins import nfl as nfl_plugin_module
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
SEASON_AVG_BLEND_WEIGHT = 0.95  # Session 2.41c: re-fit from the original,
RECENT_FORM_BLEND_WEIGHT = 0.05  # never-tested 0.5/0.5 -- see the "BLEND
# WEIGHT" module docstring section below for the full derivation. Must
# continue to sum to 1.0.
MIN_GAMES_FOR_ESTIMATE = 2  # below this, sigma is not meaningfully estimable
SIGMA_FLOOR_FRACTION = 0.15  # sigma floor, as a fraction of the mean, used
# only when a player has exactly MIN_GAMES_FOR_ESTIMATE games and their
# observed sample sigma is implausibly small (near-zero) -- prevents a
# probability estimate of ~100%/~0% off two coincidentally similar games.
SIGMA_CALIBRATION_FACTOR = 2.681  # Session 2.41c: re-fit against 18,766 real
# graded legs on clean, post-2026-09-17-dedup-fix data (data/pickem/
# outcome_log.csv), excluding the 12 isotonic-covered and 6 per-stat-override
# stats, via scripts/calibration/fit_sigma_recalibration.py -- see the
# "SIGMA CALIBRATION" module docstring section above for the full
# derivation, and the "SESSION 2.41c ADDITION" note there for why the
# original Session 2.22 value (1.61, fit 2026-09-15) could no longer be
# trusted as current.

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
    # Excluded from this table on purpose (Session 2.24, still holds under
    # the Session 2.41c global factor -- re-checked, not re-derived, since
    # "no real edge" is a property of the stat's real win rate, not of
    # which global factor happens to be current):
    # - "targets": flagged, but its real win rate is ~50% -- the model has
    #   no real edge on this stat, so no sigma multiplier fixes it (pushing
    #   k toward infinity trivially shrinks the gap without improving Brier
    #   score). A sigma fix does not apply here.
    "rushing_tds": 0.610,  # n=27 -- smallest sample here; watch for drift
    "passing_interceptions": 0.825,  # n=63
    "completions": 1.595,  # n=43 -- best-Brier k still leaves ~+0.09 gap
    "kicking points": 2.100,  # n=186 -- best-Brier k still leaves ~+0.05 gap
    "passing_tds+rushing_tds+receiving_tds": 1.155,  # n=325
    "fg_made": 1.495,  # n=146

    # SESSION 2.41d -- expanded under the new 2.681 global factor.
    # scripts/calibration/pickem_calibration_by_stat.py, re-run after
    # Session 2.41c's global refit, flagged 20 more stats past the 0.03 gap
    # threshold (up from the 6 above) -- the new global factor closes the
    # AGGREGATE gap but leaves individual stats over/under-corrected. Same
    # method as the 6 above (independent per-stat grid search, Brier-
    # minimizing, against that stat's own graded legs only); same caveat
    # (a same-sample fit, not held-out validated -- see SESSION_LOG.md
    # Session 2.41d for exact numbers and the full 20-stat breakdown).
    "hits": 1.280,  # n=2798
    "singles": 1.385,  # n=1219
    "receiving_yards": 1.530,  # n=317
    "plateAppearances": 1.575,  # n=309
    "p_numberOfPitches": 1.200,  # n=160
    "foulsCommitted": 0.600,  # n=149 -- best-Brier k still leaves ~+0.03 gap;
    # real win rate 87.9% is unusually high for this stat, a real, large
    # improvement (Brier 0.1357->0.0957) but watch for drift, not "fully
    # recalibrated"
    "triples": 1.065,  # n=93 -- rare/zero-inflated discrete stat (like the
    # Session 2.40 isotonic-covered stats); a per-stat sigma fit is "best
    # normal fit available," not a true count-data model -- same caveat this
    # script's own docstring already states for stats like this
    "p_strikes": 0.925,  # n=90
    "totalGoals+goalAssists": 0.805,  # n=81 -- best-Brier k still leaves
    # ~-0.06 gap; real, large improvement (Brier 0.2060->0.1810), not fully
    # recalibrated
    "passing_yards": 1.210,  # n=55
    "goalie fantasy score": 2.285,  # n=51
    "totalGoals": 0.795,  # n=50
    "passing_tds": 1.920,  # n=47
    "goalAssists": 0.755,  # n=39
    "passing_yards+rushing_yards": 1.970,  # n=31 -- smallest sample in this
    # table; best-Brier k barely improves Brier (0.2317->0.2306) and still
    # leaves a ~-0.10 gap -- a real but low-confidence fit, included per this
    # table's existing precedent (rushing_tds, n=27) of watching small
    # groups for drift rather than excluding them outright, but weaker
    # evidence than every other entry here

    # SESSION 2.51 -- the first overrides validated held-out before wiring.
    # p_baseOnBalls and p_earnedRuns had been moved off isotonic (Session
    # 2.47) onto the untuned global factor. Rolling-origin (4 folds, train
    # only fit, 251 test legs, 39 games): a per-stat factor beat the global
    # 2.681 by -0.019 Brier (p_baseOnBalls) and -0.018 (p_earnedRuns), and
    # the train-fit factor stayed in 0.85-1.15 across folds. Final values are
    # fit on all snapshot-joined legs (137 and 147). "pitcher fs" was
    # tested the same way and NOT given an override: its fitted factor swung
    # 2.65-3.85 and it did not beat global (-0.0004). See SESSION_LOG.md
    # Session 2.51. Rule for any new override: at least 100 legs at fit time
    # plus a held-out check (older entries below with fewer legs pre-date it).
    "p_baseOnBalls": 0.850,  # n=137 joined legs
    "p_earnedRuns": 1.000,  # n=147 joined legs

    # Excluded from the Session 2.41d expansion on purpose, same "no real
    # edge" or "degenerate fit" reasoning as "targets" above:
    # - "numberOfPitchesSeen" (n=396): real win rate 50.3% -- no real edge;
    #   best-Brier k hit the widened 8.0 grid ceiling (k pushed toward
    #   infinity chasing noise, not a real fix).
    # - "saves" (n=108): real win rate 55.6%, not clearly distinguishable
    #   from 50% at this sample size, AND best-Brier k hit the widened 8.0
    #   ceiling -- a degenerate fit, not a trustworthy per-stat multiplier.
    # - "p_battersFaced" (n=63): real win rate 47.6% -- no real edge (below
    #   50%); also hit the widened 8.0 ceiling.
    # - "rushing_yards+receiving_yards" (n=95, re-checked under the new
    #   global factor): real win rate 51.6% -- no real edge, same
    #   reasoning as "targets".
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


def compute_league_average(
    plugin: SportPlugin, stats_df: pd.DataFrame, kind: str, value: object
) -> Optional[float]:
    """Session 2.42 -- the shrinkage target for one resolved_stat_key: the
    mean of every qualifying player's OWN season_average() for this stat,
    equal weight per player (not per game -- weighting by game would let a
    handful of high-volume players dominate "what a typical player
    averages," which is the wrong target for shrinking one specific
    player's mean toward). Only players with at least MIN_GAMES_FOR_ESTIMATE
    games count, matching this model's own sigma-estimability floor.
    Returns None if stats_df is empty or no player qualifies -- an honest
    gap (falls back to the unshrunk mean at the call site), never a
    guessed 0."""
    if stats_df.empty:
        return None
    means = []
    for pid in stats_df["player_id"].unique():
        series = build_stat_series(plugin, stats_df, pid, kind, value)
        if len(series) >= MIN_GAMES_FOR_ESTIMATE:
            m = season_average(series)
            if m is not None:
                means.append(m)
    if not means:
        return None
    return float(np.mean(means))


SHRINKAGE_PRIOR_STRENGTH_K = 5.0  # Session 2.42: fit and held-out-validated
# by scripts/calibration/fit_shrinkage.py -- Brier-minimizing grid search on
# the earliest 70% (4,606 legs) of 6,581 real graded legs joined to a
# retained pickem_estimates_*.csv snapshot (13 resolved_stat_keys had a
# computable league average; see that script's "LEAGUE AVERAGE IS COMPUTED
# CURRENT, NOT HISTORICAL" docstring note for the one stated approximation
# in this fit), evaluated on the most recent 30% (1,975 legs), never seen
# during the fit. Held-out Brier improved from 0.226323 (k=0, no shrinkage)
# to 0.225768 at k=5.0 -- a real but modest improvement, not a dramatic one.
# The Session 2.42 hypothesis (thin-sample legs benefit more) held on this
# split: the below-median-games_used half of the held-out set improved more
# (delta +0.000783) than the above-median half (delta +0.000318) -- but see
# the fit run's own log (data/pickem/shrinkage_recalibration_log.csv) for a
# real, stated caveat: this sample is 88% MLB (same composition as the
# blend-weight fit), so the held-out set's OWN median games_used was 113 --
# "thin-sample" here means "fewer games than a typical MLB regular," not
# literally a 2-game rookie sample; a stat/sport mix with more real
# thin-sample (NFL early-season, first-year player) legs graded in would be
# a stronger test of the Week-1-link hypothesis specifically. Re-fit
# periodically as more legs grade in and more snapshots retain a real
# per-row league_avg (this fit's own live-current-season approximation
# becomes unnecessary once enough post-Session-2.42 snapshots exist to join
# a real historical value instead), same cadence as the sigma/blend fits.


def apply_shrinkage(
    raw_mean: float, n_games: int, league_avg: Optional[float]
) -> tuple[float, float]:
    """Session 2.42 -- sample-size-weighted shrinkage of one player's own
    blended mean toward the league average for this stat:
    shrunk_mean = (n/(n+k)) * raw_mean + (k/(n+k)) * league_avg, k =
    SHRINKAGE_PRIOR_STRENGTH_K. As n grows, weight on league_avg shrinks
    toward 0 automatically -- no separate "n already large" gate is needed,
    the formula does this by construction. Returns (shrunk_mean,
    shrinkage_weight); shrinkage_weight is the fraction of the final mean
    drawn from league_avg, always 0.0 (shrunk_mean == raw_mean exactly)
    when league_avg is None or SHRINKAGE_PRIOR_STRENGTH_K <= 0 -- clean,
    visible fallback to the raw mean, never a silent partial application."""
    if league_avg is None or SHRINKAGE_PRIOR_STRENGTH_K <= 0:
        return raw_mean, 0.0
    weight = SHRINKAGE_PRIOR_STRENGTH_K / (n_games + SHRINKAGE_PRIOR_STRENGTH_K)
    shrunk = (1.0 - weight) * raw_mean + weight * league_avg
    return shrunk, weight


PRIOR_SEASON_STRENGTH_K = 0.0  # Session 2.44 follow-up v3: OFF (clean no-op).
# Backtest (scripts/calibration/research_prior_blend_backtest.py) fit k=4 on
# 2023->2024 and cut held-out 2024->2025 RMSE for receiving_yards 33.8->25.3
# and receptions 2.39->1.80 (weeks 2-4, continuity-reliable players). It is
# NOT switched on because it needs a real leg-level Brier fit on graded 2026
# legs first (none exist past Week 1). Set to 4.0 only after that fit.
PRIOR_SEASON_STAT_KEYS = frozenset({"receiving_yards", "receptions"})  # NFL only


def apply_prior_season_blend(
    mean: float, n_games: int, prior_mean: Optional[float]
) -> tuple[float, float]:
    """Session 2.44 follow-up v3 -- blends the player's current mean toward
    their own PRIOR-season per-game average of the same stat:
    (n/(n+k))*mean + (k/(n+k))*prior_mean, k = PRIOR_SEASON_STRENGTH_K.
    Returns (blended_mean, prior_weight); (mean, 0.0) exactly when the prior
    is missing or k <= 0."""
    if prior_mean is None or PRIOR_SEASON_STRENGTH_K <= 0:
        return mean, 0.0
    weight = PRIOR_SEASON_STRENGTH_K / (n_games + PRIOR_SEASON_STRENGTH_K)
    return (1.0 - weight) * mean + weight * prior_mean, weight


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


# ---------------------------------------------------------------------------
# SESSION 2.40 -- ISOTONIC (NONPARAMETRIC) CALIBRATION FOR CONFIRMED
# NON-GAUSSIAN STATS
# ---------------------------------------------------------------------------
# Session 2.37's full audit confirmed, directly against real graded
# actual_value data, that many stats this model scores are zero-inflated or
# heavily right-skewed (MLB home runs: 89.3% real zero-rate; RBI 70.7%; NFL
# def_sacks 77.2%; 30 of 49 checked sport/stat cells flagged non-Gaussian).
# prob_over()'s plain normal CDF above cannot represent that shape no matter
# how SIGMA_CALIBRATION_FACTOR is tuned -- sigma only changes the curve's
# WIDTH, not its shape.
#
# scripts/calibration/fit_isotonic_calibration.py fits a nonparametric,
# monotonic (isotonic regression, via PAVA) recalibration curve per
# resolved_stat_key directly against real win/loss outcomes, and validates
# it on a real, TEMPORAL held-out split (fit on the earliest 70% of a stat's
# real flags, scored against the most recent 30%, never seen during the fit)
# -- not just in-sample Brier score, which isotonic regression trivially
# improves for any stat by construction. Only stats that (a) have >=200 real
# graded legs and (b) beat the current global-sigma-corrected model on that
# held-out split are written to ISOTONIC_CALIBRATION_PATH with
# ready_to_apply=True; this loader only ever reads those rows -- a stat
# with a thin sample, or one where the isotonic fit did not actually
# generalize, silently keeps using the plain Gaussian path above, never a
# half-validated override. Re-run that script periodically as more real
# outcomes accumulate; this loader picks up whatever is currently marked
# ready in the CSV, no code change needed here to update the set.
#
# WHAT THE TABLE IS ACTUALLY FIT AGAINST -- IMPORTANT, NOT A RAW prob_over
# Z-SCORE: clv_logger.py's determine_flagged_side_pickem()/model_prob
# logic (see that file, ~line 602) logs first_flagged_model_prob as
# prob_over when the OVER side was flagged, or prob_under when the UNDER
# side was flagged -- i.e., always the probability of whichever side the
# model actually favored, not always prob_over. fit_isotonic_calibration.py
# recovers z from THAT value, so the table is keyed on a side-normalized
# "confidence z" (call it z_eff: inverse_normal_cdf of whichever side's own
# probability is being asked about), not literally (line - mean) / sigma.
# isotonic_calibrate() below reproduces that exact convention -- callers
# pass the raw probability of the SPECIFIC side they want calibrated
# (prob_over or prob_under), never a raw z.
ISOTONIC_CALIBRATION_PATH = (
    Path(__file__).resolve().parents[2] / "data" / "pickem" / "isotonic_calibration_by_stat.csv"
)

_isotonic_table_cache: Optional[dict[str, tuple[np.ndarray, np.ndarray]]] = None
_isotonic_domain_min_cache: Optional[dict[str, float]] = None


def _load_isotonic_table() -> dict[str, tuple[np.ndarray, np.ndarray]]:
    """Lazy-loaded, cached: resolved_stat_key -> (block_hi, block_val),
    both sorted ascending, for stats with a validated (ready_to_apply=True)
    isotonic calibration on file. Missing file or no ready rows -> empty
    dict, so every row falls back to the plain Gaussian path with no
    special-casing needed at call sites."""
    global _isotonic_table_cache, _isotonic_domain_min_cache
    if _isotonic_table_cache is not None:
        return _isotonic_table_cache

    table: dict[str, tuple[np.ndarray, np.ndarray]] = {}
    domain_min: dict[str, float] = {}
    if ISOTONIC_CALIBRATION_PATH.exists():
        df = pd.read_csv(ISOTONIC_CALIBRATION_PATH)
        ready = df.loc[df["ready_to_apply"] == True]  # noqa: E712 (real bool column, not a Series compare pitfall here)
        for stat_key, group in ready.groupby("resolved_stat_key"):
            group = group.sort_values("z_hi")
            domain_min[stat_key] = float(group["z_lo"].min())
            table[stat_key] = (
                group["z_hi"].to_numpy(dtype=float),
                group["calibrated_prob"].to_numpy(dtype=float),
            )
    _isotonic_table_cache = table
    _isotonic_domain_min_cache = domain_min
    return table


def _isotonic_domain_min(resolved_stat_key: str) -> float:
    """Lowest z the stat's isotonic table was fit on (-inf if unknown, e.g.
    a test that mocks _load_isotonic_table). See isotonic_calibrate()."""
    _load_isotonic_table()
    return (_isotonic_domain_min_cache or {}).get(resolved_stat_key, float("-inf"))


def _inverse_normal_cdf(p: float, lo: float = -8.0, hi: float = 8.0, tol: float = 1e-10) -> float:
    """Bisection inverse of normal_cdf() above -- exact match (same
    erf-based CDF), so it exactly reverses the z that produced a given
    probability. Deliberately duplicated from
    scripts/calibration/fit_sigma_recalibration.py's identical function
    rather than imported -- scripts/calibration already depends on this
    file (pickem_model.py); the reverse dependency would be a real
    architectural smell for ~10 lines of pure math with zero state."""
    if p <= 0.0:
        return lo
    if p >= 1.0:
        return hi
    while hi - lo > tol:
        mid = (lo + hi) / 2.0
        if normal_cdf(mid) < p:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


# SESSION 2.60 -- CEILING ON A STATED PROBABILITY. Some isotonic tables end in
# blocks at exactly 1.000 (every leg in that range won, in the fit sample),
# and the plain Gaussian also reaches 0.99+ far out in the tail. Neither is
# real: on 1,081 graded legs stated at 0.95 or higher, 89.6% won (stated 0.98).
# Stated 0.99-0.9999: 90.0% won (n=349); exactly 1.0: 90.4% won (n=104,
# game-clustered 95% interval 84.1-96.7%). Time split (fit on the earlier half,
# scored on the later half): capping improves the Brier score in BOTH halves;
# the best cap was 0.88 early and 0.93 late, 0.90 is the pooled win rate.
# A stated 1.0 implies an infinite edge and a full-size Kelly stake, so the
# ceiling is applied to both sides after calibration. It does not change which
# legs are flagged (the edge over a 0.55-0.60 breakeven stays above 0.30); it
# fixes the stated probability, the edge shown, and the stake.
MAX_MODEL_PROB = 0.90


def cap_model_prob(prob: Optional[float]) -> Optional[float]:
    """Apply MAX_MODEL_PROB. None (and NaN) pass through unchanged."""
    if prob is None or prob != prob:
        return prob
    return min(prob, MAX_MODEL_PROB)


def isotonic_calibrate(resolved_stat_key: str, raw_prob: Optional[float]) -> Optional[float]:
    """The validated isotonic recalibration of a raw Gaussian-model
    probability for ONE side (pass prob_over to calibrate prob_over, or
    prob_under to calibrate prob_under -- see module note above for why
    this is side-specific, not a shared z). Returns None if this stat has
    no validated (ready_to_apply=True) table on file, or raw_prob itself
    is None/NaN -- callers must keep the original Gaussian value in that
    case, never silently drop the row."""
    if raw_prob is None or raw_prob != raw_prob:
        return None
    table = _load_isotonic_table()
    block_hi, block_val = table.get(resolved_stat_key, (None, None))
    if block_hi is None:
        return None
    z_eff = _inverse_normal_cdf(raw_prob)
    # SESSION 2.54 FIX: the tables are fit on FLAGGED-side legs only, so
    # they start at whatever the lowest flagged confidence was (homeRuns:
    # z=0.13, a raw probability of 55%). A raw probability below that range
    # (for example a 10% chance a hitter homers) used to fall into the first
    # block and take its value -- 0.5 for homeRuns and doubles, 0.654 for
    # stolenBases, 0.0 for several others -- which invented a large edge on
    # the unflagged side (homeRuns: every over at exactly 0.8333, 77 graded
    # losses at 6.5% wins). Below the fitted range there is no evidence, so
    # return None and let the caller keep the plain Gaussian value.
    if z_eff < _isotonic_domain_min(resolved_stat_key):
        return None
    idx = int(np.clip(np.searchsorted(block_hi[:-1], z_eff, side="right"), 0, len(block_val) - 1))
    return float(block_val[idx])


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


# SESSION 2.55/2.56: was a flat 0.5, which is below every real Power Play
# breakeven. Read by the user off their own PrizePicks app, 2026-09-18, for
# all-Standard entries: 2/3/4/5/6-pick pay 2/4.75/9/19/36.5x. With equal,
# independent legs each leg must win M ** (-1/N) for the entry to break even:
# 0.7071 / 0.5949 / 0.5774 / 0.5549 / 0.5491. This constant is the LOWEST of
# those (the 6-pick), so a flag means "this leg can be +EV in the most
# favorable entry"; sizing_engine.py chooses the entry size and applies the
# higher breakeven of any smaller entry. A 3-pick would need 0.5949. Applies
# to BOTH sides of a Standard line (an under leg has the same entry payout,
# so its breakeven is this same number, not 1 minus it). These multipliers
# are one lineup and can vary by leg; legs PrizePicks marks adjusted_odds
# are not scored at all (see is_scorable_prizepicks_odds_type).
PRIZEPICKS_ASSUMED_IMPLIED_PROB = 36.5 ** (-1 / 6)

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

# SESSION 2.55: Demon and Goblin are NOT scorable. Measured 2026-09-18 on the
# user's own PrizePicks app (3-pick, 2 Standard + 1 special leg): on a
# hits+runs+rbi leg Demon paid 5.25x and Goblin 4.25x (Standard 4.75x); on a
# home-run leg Demon paid 13.5x and Goblin 2.9x. The multiplier is set per leg
# (PrizePicks builds its own probability for that line into it), so no single
# constant per odds_type can price them, and the feed carries no per-leg
# multiplier. Scoring them against a constant produced edges of 30+ points
# that were artifacts of the constant. PRIZEPICKS_ODDS_TYPE_IMPLIED_PROB above
# is kept only for history and for fit_odds_type_implied_prob.py; nothing in
# scoring reads it. To score them again, the ingestion must capture a real
# per-leg price.
PRIZEPICKS_SCORABLE_ODDS_TYPES = {"standard"}


def prizepicks_odds_are_adjusted(row: dict) -> bool:
    """True when PrizePicks' own adjusted_odds flag is set on this leg
    (Session 2.56): the leg's payout is off the default table, so its real
    price is unknown. Missing/None/False all mean default. Accepts a real
    bool or the strings "True"/"true" (CSV round trip)."""
    v = row.get("adjusted_odds")
    if isinstance(v, str):
        return v.strip().lower() == "true"
    return isinstance(v, (bool, np.bool_)) and bool(v)


def is_scorable_prizepicks_odds_type(row: dict) -> bool:
    if row.get("platform") != "prizepicks":
        return True
    if prizepicks_odds_are_adjusted(row):
        return False
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


# SESSION 2.64 -- SIDES THE MODEL DOES NOT FLAG. PrizePicks MLB overs won
# 50.1% on 2,969 graded Standard legs over 108 games (game-clustered 95%
# interval 47.4-52.8%), below even the lowest per-leg breakeven of any entry
# size (6-pick, 54.9%), while the model stated them at 58%+. The shortfall is
# spread over the big stats (hitter fantasy score 50.2%, total bases 46.3%).
# Unders (56.2%, inconclusive) stay flagged. The row is kept visible with its
# probability, but no edge is computed for that side, so it is never flagged.
# Underdog is not affected (44.6% vs 44.2% breakeven, inconclusive). Re-check
# once 200 new clean-flag legs exist on this side; remove the entry to undo.
# clv_logger.py mirrors this set (test_clv_logger / test_pickem_model compare
# the two).
PRIZEPICKS_UNFLAGGED_SIDES = frozenset({("mlb", "over")})


def prizepicks_side_is_flaggable(row: dict, side: str) -> bool:
    """False for a (sport, side) the model has decided not to flag (see
    PRIZEPICKS_UNFLAGGED_SIDES). Always True for non-PrizePicks rows."""
    if row.get("platform") != "prizepicks":
        return True
    sport = str(row.get("sport") or "").strip().lower()
    return (sport, side) not in PRIZEPICKS_UNFLAGGED_SIDES


def prizepicks_side_is_scorable(row: dict, side: str) -> bool:
    """Buyable AND not a side the model has decided not to flag."""
    return prizepicks_side_is_buyable(row, side) and prizepicks_side_is_flaggable(row, side)


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
# SESSION 2.45 -- NFL injury-report confirmation status (informational only,
# same shape and names as MLB's mlb_starter_status). Does NOT change any
# edge or probability. A live validation window is open: read win rate by
# status from the CLV/outcome logs before anyone gates on it (Session 2.33's
# "measure first, gate second" rule).
#   confirmed              final game-status report is out, player not
#                          listed as Out/Doubtful/Questionable
#   different_than_expected player is listed Out or Doubtful
#   not_yet_confirmed      no final game statuses filed yet for that team's
#                          week, or the player is Questionable
#   None                   could not resolve the prop to a real game/report
# ---------------------------------------------------------------------------
NFL_INJURY_STATUS_CONFIRMED = "confirmed"
NFL_INJURY_STATUS_DIFFERENT = "different_than_expected"
NFL_INJURY_STATUS_NOT_YET_CONFIRMED = "not_yet_confirmed"


def compute_nfl_injury_status(
    row: dict,
    player_id: str,
    injury_df: Optional[pd.DataFrame],
    schedule_df: Optional[pd.DataFrame],
) -> Optional[str]:
    """See the SESSION 2.45 block comment above. `player_id` is the nflverse
    gsis id, which is also the injury report's `gsis_id`."""
    if injury_df is None or schedule_df is None:
        return None
    matchup = row.get("game_matchup")
    if not isinstance(matchup, str) or "@" not in matchup:
        return None
    away_label, _, home_label = matchup.partition("@")
    week = nfl_plugin_module.find_nfl_game_week(schedule_df, away_label.strip(), home_label.strip())
    if week is None:
        return None
    teams = {
        nfl_plugin_module.normalize_nfl_team(away_label),
        nfl_plugin_module.normalize_nfl_team(home_label),
    }
    week_rows = injury_df[(injury_df["week"] == week) & (injury_df["team"].isin(teams))]
    if week_rows.empty or week_rows["report_status"].notna().sum() == 0:
        return NFL_INJURY_STATUS_NOT_YET_CONFIRMED
    mine = week_rows[week_rows["gsis_id"] == player_id]["report_status"].dropna()
    if mine.empty:
        return NFL_INJURY_STATUS_CONFIRMED
    if set(mine) & {"Out", "Doubtful"}:
        return NFL_INJURY_STATUS_DIFFERENT
    return NFL_INJURY_STATUS_NOT_YET_CONFIRMED


# ---------------------------------------------------------------------------
# SESSION 2.46 -- NFL game-time wind. See pickem_sport_plugins/nfl.py for the
# research and the factor table. Returns (roof, wind_mph, temp_f); wind and
# temp are None for dome/closed/unknown roofs, unknown stadiums, past the
# forecast window, or any fetch failure -- which means no adjustment.
# ---------------------------------------------------------------------------
def compute_nfl_weather(
    row: dict,
    venue_df: Optional[pd.DataFrame],
    forecast_cache: dict[tuple[str, str], Optional[tuple[float, float]]],
) -> tuple[Optional[str], Optional[float], Optional[float]]:
    matchup = row.get("game_matchup")
    kickoff = row.get("game_start_time")
    if venue_df is None or not isinstance(matchup, str) or "@" not in matchup:
        return None, None, None
    away_label, _, home_label = matchup.partition("@")
    venue = nfl_plugin_module.find_nfl_game_venue(venue_df, away_label.strip(), home_label.strip())
    if venue is None or not isinstance(venue["roof"], str):
        return None, None, None
    coords = nfl_plugin_module.STADIUM_COORDS.get(str(venue["stadium_id"]))
    if venue["roof"] != "outdoors" or coords is None or not isinstance(kickoff, str):
        return venue["roof"], None, None
    key = (str(venue["stadium_id"]), kickoff)
    if key not in forecast_cache:
        forecast_cache[key] = nfl_plugin_module.fetch_kickoff_weather(coords[0], coords[1], kickoff)
    forecast = forecast_cache[key]
    if forecast is None:
        return venue["roof"], None, None
    return venue["roof"], forecast[0], forecast[1]


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
    # SESSION 2.42 -- per-run cache for compute_league_average(), keyed by
    # (plugin.name, resolved_stat_key) so a run with many props on the same
    # stat only computes the league average for it once, not once per row.
    league_avg_cache: dict[tuple[str, str], Optional[float]] = {}
    prior_stats_cache: dict[str, pd.DataFrame] = {}  # Session 2.44 follow-up v3
    nfl_injury_cache: dict[str, Optional[pd.DataFrame]] = {}  # Session 2.45, loaded once per run
    nfl_venue_cache: dict[str, Optional[pd.DataFrame]] = {}  # Session 2.46
    nfl_forecast_cache: dict[tuple[str, str], Optional[tuple[float, float]]] = {}  # Session 2.46

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
        row["nfl_injury_status"] = None  # Session 2.45
        row["weather_roof"] = None  # Session 2.46
        row["weather_wind_mph"] = None
        row["weather_temp_f"] = None
        row["weather_factor"] = None
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

        if plugin.name == "nfl":  # Session 2.45
            if not nfl_injury_cache:
                nfl_injury_cache["injuries"] = nfl_plugin_module.fetch_injury_report(season)
                nfl_injury_cache["schedule"] = nfl_plugin_module.fetch_nfl_schedule(season)
            row["nfl_injury_status"] = compute_nfl_injury_status(
                row, player_id, nfl_injury_cache["injuries"], nfl_injury_cache["schedule"]
            )

        weather_factor = 1.0
        if plugin.name == "nfl":  # Session 2.46
            if "venues" not in nfl_venue_cache:
                nfl_venue_cache["venues"] = nfl_plugin_module.fetch_nfl_schedule_with_venues(season)
            roof, wind_mph, temp_f = compute_nfl_weather(
                row, nfl_venue_cache["venues"], nfl_forecast_cache
            )
            row["weather_roof"], row["weather_wind_mph"], row["weather_temp_f"] = roof, wind_mph, temp_f
            weather_factor = nfl_plugin_module.wind_factor(row.get("resolved_stat_key"), wind_mph)
            row["weather_factor"] = weather_factor

        series = build_stat_series(plugin, stats_df, player_id, kind, value)
        if len(series) < MIN_GAMES_FOR_ESTIMATE:
            row["model_status"] = "insufficient_history"
            row.update(_blank_model_fields())
            row["games_used"] = len(series)
            out_rows.append(row)
            continue

        s_avg = season_average(series)
        r_form = recent_form(series)
        raw_model_mean = SEASON_AVG_BLEND_WEIGHT * s_avg + RECENT_FORM_BLEND_WEIGHT * r_form

        # SESSION 2.42 -- shrink the player's own blended mean toward this
        # stat's league average, weighted by real sample size (games_used).
        # See the "SHRINKAGE" module docstring section above. A clean
        # no-op (shrinkage_weight == 0.0, model_mean == raw_model_mean
        # exactly) whenever SHRINKAGE_PRIOR_STRENGTH_K is 0 (unvalidated,
        # the current default) or no league average is available for this
        # stat.
        cache_key = (plugin.name, row["resolved_stat_key"])
        if cache_key not in league_avg_cache:
            league_avg_cache[cache_key] = compute_league_average(plugin, stats_df, kind, value)
        league_avg = league_avg_cache[cache_key]
        model_mean, shrinkage_weight = apply_shrinkage(raw_model_mean, len(series), league_avg)

        prior_season_mean: Optional[float] = None
        if (
            PRIOR_SEASON_STRENGTH_K > 0
            and plugin.name == "nfl"
            and row["resolved_stat_key"] in PRIOR_SEASON_STAT_KEYS
        ):
            if plugin.name not in prior_stats_cache:
                try:
                    prior_stats_cache[plugin.name] = plugin.fetch_stats(season - 1)
                except RuntimeError:
                    prior_stats_cache[plugin.name] = pd.DataFrame()
            prior_df = prior_stats_cache[plugin.name]
            if not prior_df.empty:
                prior_series = build_stat_series(plugin, prior_df, player_id, kind, value)
                if len(prior_series) > 0:
                    prior_season_mean = season_average(prior_series)
        model_mean, prior_weight = apply_prior_season_blend(
            model_mean, len(series), prior_season_mean
        )

        model_mean *= weather_factor  # Session 2.46: 1.0 unless windy outdoor NFL game

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
        row["model_mean_pre_shrinkage"] = raw_model_mean
        row["league_avg"] = league_avg
        row["shrinkage_weight"] = shrinkage_weight
        row["prior_season_mean"] = prior_season_mean
        row["prior_season_weight"] = prior_weight
        row["model_mean"] = model_mean
        row["model_sigma"] = sigma
        row["games_used"] = len(series)

        prob_under_raw = (1.0 - p_over) if p_over is not None else None
        # Session 2.47: keep the pre-isotonic Gaussian probabilities on the row so a
        # refit of the isotonic tables never has to calibrate an already-calibrated value.
        row["prob_over_raw"] = p_over
        row["prob_under_raw"] = prob_under_raw
        # SESSION 2.40 -- for stats with a real, held-out-validated isotonic
        # calibration on file (see module note above prob_over()), override
        # the plain Gaussian probability with the empirical one. Each side
        # is calibrated independently against its OWN raw probability, and
        # either side falls straight back to the Gaussian value if no
        # validated table exists for this resolved_stat_key -- never a
        # partial or guessed override.
        calibrated_over = isotonic_calibrate(row["resolved_stat_key"], p_over)
        calibrated_under = isotonic_calibrate(row["resolved_stat_key"], prob_under_raw)
        p_over = calibrated_over if calibrated_over is not None else p_over
        prob_under = calibrated_under if calibrated_under is not None else prob_under_raw
        row["prob_calibration_method"] = (
            "isotonic" if (calibrated_over is not None or calibrated_under is not None) else "gaussian"
        )

        p_over = cap_model_prob(p_over)
        prob_under = cap_model_prob(prob_under)
        row["prob_over"] = p_over
        row["prob_under"] = prob_under
        row["implied_prob_over"] = implied_over
        if row.get("platform") == "prizepicks":
            # Session 2.55: a Standard under leg has the same entry payout as an
            # over leg, so its breakeven is the same number, not 1 - implied_over.
            row["implied_prob_under"] = implied_over
        else:
            row["implied_prob_under"] = (1.0 - implied_over) if implied_over is not None else None
        row["edge_over"] = (
            (p_over - implied_over)
            if (p_over is not None and implied_over is not None and prizepicks_side_is_scorable(row, "over"))
            else None
        )
        row["edge_under"] = (
            (row["prob_under"] - row["implied_prob_under"])
            if (
                row["prob_under"] is not None
                and row["implied_prob_under"] is not None
                and prizepicks_side_is_scorable(row, "under")
            )
            else None
        )
        out_rows.append(row)

    return pd.DataFrame(out_rows)


def _blank_model_fields() -> dict:
    return {
        "season_avg": None,
        "recent_form": None,
        "model_mean_pre_shrinkage": None,
        "league_avg": None,
        "shrinkage_weight": None,
        "prior_season_mean": None,
        "prior_season_weight": None,
        "model_mean": None,
        "model_sigma": None,
        "games_used": None,
        "prob_over": None,
        "prob_under": None,
        "prob_calibration_method": None,
        "prob_over_raw": None,
        "prob_under_raw": None,
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
