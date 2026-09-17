"""
Session 2.42 -- Shrinkage Estimation Fit (Pick'em, Thin-Sample Players)

WHAT THIS SCRIPT IS
--------------------
pickem_model.py's model_mean has never shrunk a thin-sample player's own
blended mean toward any kind of league prior -- MIN_GAMES_FOR_ESTIMATE = 2
means a player with exactly 2 games is trusted exactly as much as one with
15. ROADMAP.md's Session 2.42 card cites real, sourced evidence that
professional sports-projection systems instead shrink toward a league or
positional average, weighted by real sample size, specifically because raw
small-sample averages are known to be unreliable estimates of true talent.
pickem_model.py now has the machinery for this (compute_league_average(),
apply_shrinkage(), SHRINKAGE_PRIOR_STRENGTH_K -- see that file's "SHRINKAGE"
module docstring section), but SHRINKAGE_PRIOR_STRENGTH_K starts at 0.0 (a
clean no-op) until a real fit validates a specific k. This script is that
fit.

WHY THIS NEEDS THE SAME SNAPSHOT-JOIN APPROACH AS fit_blend_weight.py
-----------------------------------------------------------------------
Same reason fit_blend_weight.py needed it: outcome_log.csv/clv_log.csv only
ever stored the FINAL blended probability, never season_avg/recent_form/
games_used as separate numbers. Those are written per-row by
pickem_model.py's process_props() to output/estimation/pickem_estimates_*.csv
snapshots, so this script joins outcome_log.csv (via clv_log.csv, for
source_line_id/first_flagged_at) back to whichever RETAINED snapshot covers
that leg's flag date, at day granularity -- same join, same stated
"not every graded leg has a retained snapshot" limitation, as
fit_blend_weight.py's own docstring already documents in detail.

A REAL, STATED APPROXIMATION -- LEAGUE AVERAGE IS COMPUTED CURRENT, NOT
HISTORICAL
------------------------------------------------------------------------------
compute_league_average() needs a full-season player pool to average over.
No historical snapshot stored each stat's league average as of the leg's own
flag date -- only pickem_model.py's live process_props() run does. This
script instead computes each (sport, resolved_stat_key)'s league average
ONCE, live, against the CURRENT season's stats (via each plug-in's own
fetch_stats(current_pickem_season())), and applies that single current value
to every historical leg for that stat regardless of when it was flagged. For
most stats this is a reasonable approximation -- a league average is a
slow-moving population statistic, not something that swings week to week --
but it is stated here plainly, not hidden, as a real, second-order
approximation, matching this project's standard (see fit_blend_weight.py's
own "sigma is held fixed" section for the same kind of stated approximation
in a sibling fit). A genuinely more precise version would need pickem_model.py
to start writing league_avg into every snapshot going forward (it now does,
via the new `league_avg` output column -- so a FUTURE re-run of this fit,
once enough post-Session-2.42 snapshots exist, can join the real per-day
value instead of this live approximation).

METHOD
------
1. Load every graded (win/loss) leg joined to a retained snapshot (same
   join as fit_blend_weight.py), keeping games_used and sport this time too.
2. Exclude the same 12 isotonic-covered + (currently 21) per-stat-sigma-
   override stats fit_sigma_recalibration.py/fit_blend_weight.py already
   exclude, for the same reason: mixing populations whose downstream
   probability path differs would distort a single shared k.
3. Compute each (sport, resolved_stat_key)'s current league average once
   (see approximation note above), via pickem_model.compute_league_average(),
   reusing each row's own plug-in/kind/value resolution.
4. Grid-search k (SHRINKAGE_PRIOR_STRENGTH_K): for each k, recompute
   shrunk_mean = (n/(n+k)) * raw_mean + (k/(n+k)) * league_avg per leg
   (raw_mean = the leg's own stored season_avg/recent_form blend;
   model_sigma held fixed, same stated approximation fit_blend_weight.py's
   own docstring already uses for the identical reason -- re-deriving the
   MIN_GAMES_FOR_ESTIMATE-only sigma floor per counterfactual k would need
   the player's raw per-game series, not retained in any snapshot), score
   Brier against real win/loss on the probability of the side that was
   ACTUALLY flagged (flagged_side column, same convention as
   fit_blend_weight.py).
5. Real temporal held-out validation (Session 2.40's method, reused
   directly): sort by first_flagged_at, fit k on the earliest 70%, evaluate
   Brier on the most recent 30% (never seen during the fit) against the
   current production (k=0, i.e. no shrinkage) baseline on that SAME held-out
   set. Only a real held-out improvement is evidence this generalizes.
6. Explicit check of the Session 2.42 hypothesis: does the held-out
   improvement concentrate in thin-sample legs (games_used below the
   median) or is it flat/uniform across sample size? Reported separately,
   not asserted either way in advance.

USAGE
-----
python scripts/calibration/fit_shrinkage.py
    Loads outcome_log.csv + clv_log.csv + every retained
    output/estimation/pickem_estimates_*.csv, fits k, prints the held-out
    validation (overall and by sample-size bucket), and appends a dated row
    to data/pickem/shrinkage_recalibration_log.csv -- a durable, queryable
    record matching sigma_recalibration_log.csv / blend_weight_recalibration_
    log.csv's own pattern. Does NOT modify pickem_model.py --
    SHRINKAGE_PRIOR_STRENGTH_K is only updated there as a separate, deliberate
    step once this script's held-out result is reviewed, matching
    fit_sigma_recalibration.py / fit_isotonic_calibration.py's own
    "no silent recalibration" precedent.
"""

from __future__ import annotations

import glob
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "estimation"))
from pickem_model import (  # noqa: E402
    compute_league_average,
    normal_cdf,
    resolve_stat_spec,
)
from pickem_sport_plugins import plugin_for_sport  # noqa: E402
from season_utils import current_pickem_season  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fit_sigma_recalibration import load_excluded_stats  # noqa: E402

BASE_DIR = Path(__file__).resolve().parents[2]
OUTCOME_LOG_PATH = BASE_DIR / "data" / "pickem" / "outcome_log.csv"
CLV_LOG_PATH = BASE_DIR / "data" / "pickem" / "clv_log.csv"
ESTIMATES_GLOB = str(BASE_DIR / "output" / "estimation" / "pickem_estimates_*.csv")
FIT_LOG_PATH = BASE_DIR / "data" / "pickem" / "shrinkage_recalibration_log.csv"

SNAPSHOT_COLUMNS = [
    "platform", "source_line_id", "pulled_at", "model_status", "sport",
    "season_avg", "recent_form", "model_mean", "model_sigma", "line",
    "resolved_stat_key", "games_used", "stat_type",
]
# NOTE: every retained snapshot predates Session 2.42 (SHRINKAGE_PRIOR_
# STRENGTH_K did not exist when these were written, and always defaults to
# 0.0 even now), so each snapshot's own `model_mean` column IS the raw,
# unshrunk blended mean (SEASON_AVG_BLEND_WEIGHT * season_avg +
# RECENT_FORM_BLEND_WEIGHT * recent_form, at whichever blend weight was
# production at that time) -- used directly below as raw_mean, rather than
# re-deriving it from season_avg/recent_form with today's blend weight,
# which would silently apply today's weight to a leg scored under a
# different historical one.

# Grid search range for k (SHRINKAGE_PRIOR_STRENGTH_K). 0 = no shrinkage.
# Expressed in "games" units, same units as games_used -- k=5 means the
# league prior carries the same weight as 5 real games of the player's own
# data. A player with games_used == k gets a 50/50 blend of their own mean
# and the league average.
K_GRID = np.concatenate([[0.0], np.arange(0.5, 20.001, 0.5)])

TRAIN_FRACTION = 0.70  # matches fit_isotonic_calibration.py's temporal split

FIT_LOG_COLUMNS = [
    "run_at", "n_legs_total", "n_snapshot_files_used",
    "n_train", "n_test",
    "held_out_baseline_brier", "held_out_fitted_brier", "fitted_k",
    "improvement_concentrates_in_thin_sample",
    "thin_sample_median_games_used",
]


def load_snapshots() -> tuple[pd.DataFrame, int]:
    files = sorted(glob.glob(ESTIMATES_GLOB))
    frames = []
    used = 0
    for f in files:
        try:
            df = pd.read_csv(f, usecols=lambda c: c in SNAPSHOT_COLUMNS, low_memory=False)
        except ValueError:
            continue
        required = {"platform", "source_line_id", "pulled_at", "model_status", "sport",
                    "season_avg", "recent_form", "model_mean", "model_sigma", "line",
                    "games_used", "stat_type"}
        if not required.issubset(df.columns):
            continue
        df = df.loc[df["model_status"] == "estimated"].copy()
        if df.empty:
            continue
        df["source_line_id"] = df["source_line_id"].astype(str)
        df["snapshot_date"] = pd.to_datetime(df["pulled_at"], utc=True).dt.date
        frames.append(df)
        used += 1
    if not frames:
        raise SystemExit("No usable pickem_estimates_*.csv snapshots found under output/estimation/.")
    snap = pd.concat(frames, ignore_index=True)
    # Same confirmed-stable-per-day property fit_blend_weight.py's docstring
    # already relies on for season_avg/recent_form/model_sigma; games_used
    # is derived from the exact same per-game series, so it is equally
    # stable within a calendar day.
    snap = snap.drop_duplicates(subset=["platform", "source_line_id", "snapshot_date"], keep="first")
    return snap, used


def load_joined_legs(snap: pd.DataFrame) -> pd.DataFrame:
    outcome = pd.read_csv(OUTCOME_LOG_PATH, low_memory=False)
    graded = outcome.loc[outcome["result"].isin(["win", "loss"])].copy()
    graded = graded.dropna(subset=["first_flagged_model_prob", "flag_id", "flagged_side"])
    graded["win"] = (graded["result"] == "win").astype(int)

    clv = pd.read_csv(CLV_LOG_PATH, usecols=["flag_id", "platform", "source_line_id", "first_flagged_at"])
    clv["source_line_id"] = clv["source_line_id"].astype(str)
    merged = graded.merge(clv, on="flag_id", how="left", suffixes=("", "_clv"))
    merged = merged.dropna(subset=["source_line_id", "first_flagged_at"])
    merged["flag_date"] = pd.to_datetime(merged["first_flagged_at"], utc=True).dt.date

    joined = merged.merge(
        snap.drop(columns=["resolved_stat_key", "stat_type", "sport"]),
        left_on=["platform", "source_line_id", "flag_date"],
        right_on=["platform", "source_line_id", "snapshot_date"],
        how="inner",
    )
    joined = joined.dropna(subset=["season_avg", "recent_form", "model_mean", "model_sigma", "line", "games_used"])
    joined = joined.loc[joined["model_sigma"] > 0].copy()
    joined["games_used"] = joined["games_used"].astype(int)

    excluded = load_excluded_stats()
    if excluded:
        joined = joined.loc[~joined["resolved_stat_key"].isin(excluded)]
    return joined


def compute_league_averages_for_sample(joined: pd.DataFrame) -> dict[str, float]:
    """Live, current-season league average per resolved_stat_key present in
    the joined sample (see module docstring's "LEAGUE AVERAGE IS COMPUTED
    CURRENT, NOT HISTORICAL" note for why this is an approximation, not a
    historical reconstruction). Fetches each needed plug-in's stats once."""
    season = current_pickem_season()
    league_avgs: dict[str, float] = {}
    stats_cache: dict[str, pd.DataFrame] = {}

    combos = joined[["sport", "resolved_stat_key", "stat_type"]].drop_duplicates()
    for _, combo in combos.iterrows():
        stat_key = combo["resolved_stat_key"]
        if stat_key in league_avgs:
            continue
        sport = str(combo["sport"] or "").strip().lower()
        plugin = plugin_for_sport(sport)
        if plugin is None:
            continue
        if plugin.name not in stats_cache:
            stats_cache[plugin.name] = plugin.fetch_stats(season)
        stats_df = stats_cache[plugin.name]
        kind, value, _reason = resolve_stat_spec(plugin, combo["stat_type"])
        if kind is None:
            continue
        avg = compute_league_average(plugin, stats_df, kind, value)
        if avg is not None:
            league_avgs[stat_key] = avg
    return league_avgs


def brier_score(probs: np.ndarray, outcomes: np.ndarray) -> float:
    return float(np.mean((probs - outcomes) ** 2))


def prob_for_flagged_side(df: pd.DataFrame, k: float) -> np.ndarray:
    """Recomputes the probability of the ACTUALLY-flagged side after
    shrinking each leg's own stored (production-blend) model_mean toward
    its resolved_stat_key's league_avg column by k, holding model_sigma
    fixed (see module docstring's stated approximation). k=0 reproduces the
    unshrunk production probability exactly (shrinkage_weight is 0 by
    construction), which is this fit's own baseline."""
    n = df["games_used"].to_numpy(dtype=float)
    raw_mean = df["model_mean"].to_numpy(dtype=float)
    league_avg = df["league_avg"].to_numpy(dtype=float)
    sigma = df["model_sigma"].to_numpy(dtype=float)
    line = df["line"].to_numpy(dtype=float)

    has_prior = ~np.isnan(league_avg)
    if k <= 0:
        shrunk_mean = raw_mean.copy()
    else:
        weight = np.where(has_prior, k / (n + k), 0.0)
        shrunk_mean = np.where(has_prior, (1.0 - weight) * raw_mean + weight * league_avg, raw_mean)

    z = (line - shrunk_mean) / sigma
    p_over = np.array([1.0 - normal_cdf(zi) for zi in z])
    return np.where(df["flagged_side"].to_numpy() == "over", p_over, 1.0 - p_over)


def fit_k(df: pd.DataFrame) -> dict:
    """Real temporal held-out split (Session 2.40's method): fit k on the
    earliest TRAIN_FRACTION of legs by first_flagged_at, evaluate Brier on
    the most recent split, never seen during the fit, against the k=0
    (current production, no shrinkage) baseline on that SAME held-out set."""
    df = df.sort_values("first_flagged_at").reset_index(drop=True)
    n = len(df)
    split = int(n * TRAIN_FRACTION)

    train, test = df.iloc[:split], df.iloc[split:]
    test_outcomes = test["win"].to_numpy()

    baseline_test_probs = prob_for_flagged_side(test, k=0.0)
    baseline_brier = brier_score(baseline_test_probs, test_outcomes)

    best_k = 0.0
    best_train_brier = brier_score(prob_for_flagged_side(train, k=0.0), train["win"].to_numpy())
    for k in K_GRID:
        train_probs = prob_for_flagged_side(train, k=float(k))
        b = brier_score(train_probs, train["win"].to_numpy())
        if b < best_train_brier:
            best_train_brier = b
            best_k = float(k)

    fitted_test_probs = prob_for_flagged_side(test, k=best_k)
    fitted_brier = brier_score(fitted_test_probs, test_outcomes)

    # Session 2.42 hypothesis check: does the held-out improvement
    # concentrate in thin-sample (below-median games_used) legs, or is it
    # flat/uniform? Reported honestly either way, not asserted in advance.
    median_games = float(test["games_used"].median())
    thin = test.loc[test["games_used"] <= median_games]
    thick = test.loc[test["games_used"] > median_games]
    thin_result = None
    thick_result = None
    if len(thin) >= 10:
        thin_result = {
            "n": len(thin),
            "baseline_brier": brier_score(prob_for_flagged_side(thin, k=0.0), thin["win"].to_numpy()),
            "fitted_brier": brier_score(prob_for_flagged_side(thin, k=best_k), thin["win"].to_numpy()),
        }
    if len(thick) >= 10:
        thick_result = {
            "n": len(thick),
            "baseline_brier": brier_score(prob_for_flagged_side(thick, k=0.0), thick["win"].to_numpy()),
            "fitted_brier": brier_score(prob_for_flagged_side(thick, k=best_k), thick["win"].to_numpy()),
        }

    concentrates_in_thin = None
    if thin_result is not None and thick_result is not None:
        thin_delta = thin_result["baseline_brier"] - thin_result["fitted_brier"]
        thick_delta = thick_result["baseline_brier"] - thick_result["fitted_brier"]
        concentrates_in_thin = bool(thin_delta > thick_delta)

    return {
        "n_train": len(train),
        "n_test": len(test),
        "held_out_baseline_brier": baseline_brier,
        "held_out_fitted_brier": fitted_brier,
        "fitted_k": best_k,
        "beats_baseline_held_out": fitted_brier < baseline_brier,
        "thin_sample_median_games_used": median_games,
        "thin_result": thin_result,
        "thick_result": thick_result,
        "improvement_concentrates_in_thin_sample": concentrates_in_thin,
    }


def load_fit_log() -> pd.DataFrame:
    if FIT_LOG_PATH.exists():
        df = pd.read_csv(FIT_LOG_PATH)
        for col in FIT_LOG_COLUMNS:
            if col not in df.columns:
                df[col] = None
        return df[FIT_LOG_COLUMNS]
    return pd.DataFrame(columns=FIT_LOG_COLUMNS)


def append_fit_log(result: dict, n_legs_total: int, n_snapshot_files_used: int) -> None:
    fit_log = load_fit_log()
    new_row = {
        "run_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "n_legs_total": n_legs_total,
        "n_snapshot_files_used": n_snapshot_files_used,
        "n_train": result["n_train"],
        "n_test": result["n_test"],
        "held_out_baseline_brier": result["held_out_baseline_brier"],
        "held_out_fitted_brier": result["held_out_fitted_brier"],
        "fitted_k": result["fitted_k"],
        "improvement_concentrates_in_thin_sample": result["improvement_concentrates_in_thin_sample"],
        "thin_sample_median_games_used": result["thin_sample_median_games_used"],
    }
    fit_log = pd.concat([fit_log, pd.DataFrame([new_row])], ignore_index=True)
    FIT_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    fit_log.to_csv(FIT_LOG_PATH, index=False)


if __name__ == "__main__":
    snap, n_files = load_snapshots()
    joined = load_joined_legs(snap)
    if len(joined) < 30:
        raise SystemExit(
            f"Only {len(joined)} graded legs joined to a retained snapshot -- below "
            f"the 30-leg interim floor this project uses elsewhere. Not fitting on a "
            f"sample this small. ({n_files} snapshot files were usable.)"
        )

    league_avgs = compute_league_averages_for_sample(joined)
    joined["league_avg"] = joined["resolved_stat_key"].map(league_avgs)
    n_with_prior = int(joined["league_avg"].notna().sum())
    print(f"Snapshot files used: {n_files}")
    print(f"Joined graded legs: {len(joined)} (of which {n_with_prior} have a computed league_avg)")
    print(f"Resolved_stat_keys with a league average: {len(league_avgs)}")

    if n_with_prior < 30:
        raise SystemExit(
            f"Only {n_with_prior} joined legs have a computable league_avg -- below "
            f"the 30-leg interim floor. Cannot fit a real k on a sample this small."
        )

    result = fit_k(joined)
    append_fit_log(result, len(joined), n_files)

    print()
    print(f"Held-out split: {result['n_train']} train / {result['n_test']} test (temporal, "
          f"earliest {int(TRAIN_FRACTION*100)}% train)")
    print(f"Held-out baseline Brier (k=0, no shrinkage): {result['held_out_baseline_brier']:.6f}")
    print(f"Fitted k (SHRINKAGE_PRIOR_STRENGTH_K): {result['fitted_k']}")
    print(f"Held-out fitted Brier: {result['held_out_fitted_brier']:.6f}")
    print(f"Shrinkage beats no-shrinkage baseline on HELD-OUT data: "
          f"{'YES' if result['beats_baseline_held_out'] else 'no'}")
    print()
    print(f"Thin-sample median games_used in test split: {result['thin_sample_median_games_used']}")
    if result["thin_result"] is not None:
        t = result["thin_result"]
        print(f"  Thin-sample (<= median, n={t['n']}): baseline={t['baseline_brier']:.6f} "
              f"fitted={t['fitted_brier']:.6f} delta={t['baseline_brier']-t['fitted_brier']:+.6f}")
    if result["thick_result"] is not None:
        t = result["thick_result"]
        print(f"  Thick-sample (>  median, n={t['n']}): baseline={t['baseline_brier']:.6f} "
              f"fitted={t['fitted_brier']:.6f} delta={t['baseline_brier']-t['fitted_brier']:+.6f}")
    print(f"Improvement concentrates in thin-sample legs: "
          f"{result['improvement_concentrates_in_thin_sample']}")
