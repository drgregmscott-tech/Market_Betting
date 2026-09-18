"""
Session 2.47 -- Isotonic Calibration Refit Under the CURRENT Model Configuration

WHY THIS EXISTS
----------------
Session 2.40's isotonic tables (data/pickem/isotonic_calibration_by_stat.csv)
are a step function keyed on an absolute z-score, "z_eff" = the normal-CDF
inverse of the raw Gaussian probability of the flagged side. They were fit
2026-09-17, when the model used sigma factor 1.61, a 50/50 season/recent
blend and no shrinkage. Later the same day Session 2.41c changed the sigma
factor to 2.681 and the blend to 0.95/0.05, and Session 2.42 added shrinkage
(k=5). Every one of those changes moves the z_eff a given leg produces, but
the table was never refit. Session 2.40's claim that isotonic calibration is
"robust to the sigma factor" is true only for FITTING (rank order does not
depend on a uniform rescale); it is false for APPLYING a table fit under one
configuration to probabilities produced under another, because the lookup
keys on absolute z, not rank. Checked 2026-09-18 by replaying the sigma change
alone on the pre-2.40 graded legs: Brier got worse for all 12 covered stats,
and for passing_tds+rushing_tds+receiving_tds the misaligned table scored
worse than plain Gaussian.

A second, separate flaw: for legs flagged after Session 2.40 shipped,
clv_log.csv's first_flagged_model_prob is ALREADY an isotonic-calibrated
value, so refitting on it would calibrate a calibration. This script never
reads first_flagged_model_prob.

METHOD
------
1. Take every graded win/loss leg that joins to a retained
   output/estimation/pickem_estimates_*.csv snapshot (same join as
   fit_shrinkage.py / fit_blend_weight.py), and rebuild the raw Gaussian
   probability of the flagged side as the CURRENT code would produce it:
     raw_mean  = SEASON_AVG_BLEND_WEIGHT*season_avg
                 + RECENT_FORM_BLEND_WEIGHT*recent_form
     mean      = apply_shrinkage(raw_mean, games_used, league_avg)
     sigma     = (snapshot model_sigma / sigma factor in force when the
                 snapshot was written) * current factor for that stat
   The factor in force at snapshot time is reconstructed from the three
   known configurations (see FACTOR_* below). Snapshots written inside the
   deployment windows of Sessions 2.41c/2.41d/2.42 are dropped, because
   which factor applied to them cannot be told from the file alone.
2. z_eff = inverse_normal_cdf(raw flagged-side probability).
3. Per resolved_stat_key, fit isotonic regression on the earliest 70% of legs
   by first_flagged_at, score the latest 30% against (a) the current plain
   Gaussian and (b) the table currently live (misaligned), and only mark a
   stat ready_to_apply when it clears MIN_GROUP_SIZE_FOR_PRODUCTION legs AND
   beats the plain Gaussian on the held-out split.
4. Writes the full-sample fit for every stat to the same CSV pickem_model.py
   already loads, so nothing in production code has to change to pick it up.

STATED APPROXIMATIONS (not hidden)
- league_avg is computed live for the current season, not per historical
  flag date (same approximation fit_shrinkage.py documents).
- Wind (Session 2.46) and prior-season blend (2.44, switched off) mean
  adjustments are not reconstructed. Wind touches outdoor NFL games only.
- sigma's MIN_GAMES floor (a fraction of the mean, only for players with
  exactly 2 games) is not re-derived; sigma is rescaled by the factor ratio.
- Only legs with a retained snapshot are used. output/estimation/ does not
  keep every historical snapshot.

USAGE
-----
python scripts/calibration/refit_isotonic_current_config.py [--write]
    Prints the held-out comparison. --write replaces
    data/pickem/isotonic_calibration_by_stat.csv with the refit.
"""

from __future__ import annotations

import glob
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "estimation"))
import pickem_model as pm  # noqa: E402
from pickem_model import normal_cdf  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fit_isotonic_calibration import (  # noqa: E402
    MIN_GROUP_SIZE_FOR_DIAGNOSTIC,
    MIN_GROUP_SIZE_FOR_PRODUCTION,
    TRAIN_FRACTION,
    isotonic_regression,
    predict_isotonic,
)
from fit_shrinkage import compute_league_averages_for_sample  # noqa: E402
from fit_sigma_recalibration import brier_score, inverse_normal_cdf  # noqa: E402

BASE_DIR = Path(__file__).resolve().parents[2]
OUTCOME_LOG_PATH = BASE_DIR / "data" / "pickem" / "outcome_log.csv"
CLV_LOG_PATH = BASE_DIR / "data" / "pickem" / "clv_log.csv"
ESTIMATES_GLOB = str(BASE_DIR / "output" / "estimation" / "pickem_estimates_*.csv")
OUT_PATH = BASE_DIR / "data" / "pickem" / "isotonic_calibration_by_stat.csv"

# Configuration history for the sigma factor (commit times, UTC).
T_2_41C = pd.Timestamp("2026-09-17T16:23:49Z")  # global 1.61 -> 2.681
T_2_41D = pd.Timestamp("2026-09-17T17:06:56Z")  # per-stat table expanded
T_2_42 = pd.Timestamp("2026-09-17T17:48:51Z")  # shrinkage added
# Snapshots written from just before the first change to a few hours after
# the last are dropped (pipeline lag between a commit and the first run that
# uses it is unknown).
AMBIGUOUS_START = T_2_41C - pd.Timedelta(hours=2)
AMBIGUOUS_END = T_2_42 + pd.Timedelta(hours=3)

FACTOR_GLOBAL_OLD = 1.61
# The per-stat table as it stood before Session 2.41d (Sessions 2.24/2.25).
FACTOR_BY_STAT_OLD = {
    "rushing_tds": 0.610,
    "passing_interceptions": 0.825,
    "completions": 1.595,
    "kicking points": 2.100,
    "passing_tds+rushing_tds+receiving_tds": 1.155,
    "fg_made": 1.495,
}

SNAPSHOT_COLUMNS = [
    "platform", "source_line_id", "pulled_at", "model_status", "sport",
    "season_avg", "recent_form", "model_sigma", "line",
    "resolved_stat_key", "games_used", "stat_type",
]


def factor_in_force(stat_key: str, pulled_at: pd.Timestamp) -> float:
    if pulled_at < T_2_41C:
        return FACTOR_BY_STAT_OLD.get(stat_key, FACTOR_GLOBAL_OLD)
    if pulled_at < T_2_41D:
        return FACTOR_BY_STAT_OLD.get(stat_key, pm.SIGMA_CALIBRATION_FACTOR)
    return pm.SIGMA_CALIBRATION_FACTOR_BY_STAT.get(stat_key, pm.SIGMA_CALIBRATION_FACTOR)


def current_factor(stat_key: str) -> float:
    return pm.SIGMA_CALIBRATION_FACTOR_BY_STAT.get(stat_key, pm.SIGMA_CALIBRATION_FACTOR)


def load_snapshots() -> tuple[pd.DataFrame, int]:
    frames, used = [], 0
    for f in sorted(glob.glob(ESTIMATES_GLOB)):
        try:
            df = pd.read_csv(f, usecols=lambda c: c in SNAPSHOT_COLUMNS, low_memory=False)
        except ValueError:
            continue
        need = {"platform", "source_line_id", "pulled_at", "model_status", "season_avg",
                "recent_form", "model_sigma", "line", "games_used"}
        if not need.issubset(df.columns):
            continue
        df = df.loc[df["model_status"] == "estimated"].copy()
        if df.empty:
            continue
        df["source_line_id"] = df["source_line_id"].astype(str)
        df["pulled_ts"] = pd.to_datetime(df["pulled_at"], utc=True)
        frames.append(df)
        used += 1
    snap = pd.concat(frames, ignore_index=True)
    snap = snap.loc[(snap["pulled_ts"] < AMBIGUOUS_START) | (snap["pulled_ts"] > AMBIGUOUS_END)]
    snap["snapshot_date"] = snap["pulled_ts"].dt.date
    snap = snap.drop_duplicates(subset=["platform", "source_line_id", "snapshot_date"], keep="first")
    return snap, used


def load_legs(snap: pd.DataFrame) -> pd.DataFrame:
    outcome = pd.read_csv(OUTCOME_LOG_PATH, low_memory=False)
    g = outcome.loc[outcome["result"].isin(["win", "loss"])].dropna(subset=["flag_id", "flagged_side"]).copy()
    g["win"] = (g["result"] == "win").astype(int)
    clv = pd.read_csv(CLV_LOG_PATH, usecols=["flag_id", "platform", "source_line_id", "first_flagged_at"])
    clv["source_line_id"] = clv["source_line_id"].astype(str)
    m = g.merge(clv, on="flag_id", how="left", suffixes=("", "_clv")).dropna(
        subset=["source_line_id", "first_flagged_at"])
    m["flag_date"] = pd.to_datetime(m["first_flagged_at"], utc=True).dt.date
    j = m.merge(
        snap.drop(columns=["resolved_stat_key", "stat_type", "sport"], errors="ignore"),
        left_on=["platform", "source_line_id", "flag_date"],
        right_on=["platform", "source_line_id", "snapshot_date"],
        how="inner",
    )
    j = j.dropna(subset=["season_avg", "recent_form", "model_sigma", "line", "games_used"])
    j = j.loc[j["model_sigma"] > 0].copy()
    j["games_used"] = j["games_used"].astype(int)
    return j


def current_config_z(j: pd.DataFrame) -> pd.DataFrame:
    """Adds raw_prob (current-config Gaussian probability of the flagged
    side) and z_eff, and the plain-Gaussian baseline used for scoring."""
    league = compute_league_averages_for_sample(j)
    j["league_avg"] = j["resolved_stat_key"].map(league)

    raw_mean = (pm.SEASON_AVG_BLEND_WEIGHT * j["season_avg"]
                + pm.RECENT_FORM_BLEND_WEIGHT * j["recent_form"]).to_numpy(dtype=float)
    n = j["games_used"].to_numpy(dtype=float)
    la = j["league_avg"].to_numpy(dtype=float)
    k = pm.SHRINKAGE_PRIOR_STRENGTH_K
    w = np.where(np.isnan(la) | (k <= 0), 0.0, k / (n + k))
    mean = np.where(np.isnan(la), raw_mean, (1 - w) * raw_mean + w * la)

    old_f = np.array([factor_in_force(s, t) for s, t in zip(j["resolved_stat_key"], j["pulled_ts"])])
    new_f = np.array([current_factor(s) for s in j["resolved_stat_key"]])
    sigma = j["model_sigma"].to_numpy(dtype=float) / old_f * new_f

    z = (j["line"].to_numpy(dtype=float) - mean) / sigma
    p_over = np.array([1.0 - normal_cdf(v) for v in z])
    over = j["flagged_side"].to_numpy() == "over"
    j["raw_prob"] = np.where(over, p_over, 1.0 - p_over)
    j["z_eff"] = [inverse_normal_cdf(p) for p in j["raw_prob"]]
    return j


def live_table_lookup(stat_key: str, z: np.ndarray, table: dict) -> np.ndarray | None:
    if stat_key not in table:
        return None
    hi, val = table[stat_key]
    idx = np.clip(np.searchsorted(hi[:-1], z, side="right"), 0, len(val) - 1)
    return val[idx]


def fit_stat(stat_key: str, g: pd.DataFrame, live_table: dict) -> dict:
    g = g.sort_values("first_flagged_at")
    z, y = g["z_eff"].to_numpy(), g["win"].to_numpy()
    gauss = g["raw_prob"].to_numpy()
    n = len(g)
    split = int(n * TRAIN_FRACTION)

    held = None
    if split >= MIN_GROUP_SIZE_FOR_DIAGNOSTIC and (n - split) >= 10:
        tr = np.argsort(z[:split])
        lo, hi, val = isotonic_regression(z[:split][tr], y[:split][tr])
        pred = predict_isotonic(z[split:], lo, hi, val)
        live = live_table_lookup(stat_key, z[split:], live_table)
        held = {
            "n_test": n - split,
            "gauss": brier_score(gauss[split:], y[split:]),
            "iso": brier_score(pred, y[split:]),
            "live_table": None if live is None else brier_score(live, y[split:]),
        }
        held["beats"] = held["iso"] < held["gauss"]

    order = np.argsort(z)
    lo, hi, val = isotonic_regression(z[order], y[order])
    return {
        "stat": stat_key, "n": n, "win_rate": float(y.mean()),
        "blocks": (lo, hi, val), "held": held,
        "ready": bool(n >= MIN_GROUP_SIZE_FOR_PRODUCTION and held is not None and held["beats"]),
    }


def main(write: bool) -> None:
    snap, n_files = load_snapshots()
    j = current_config_z(load_legs(snap))
    print(f"Snapshot files used: {n_files}; graded legs joined to a usable snapshot: {len(j)}")
    print(f"Legs flagged before Session 2.40 shipped are the bulk; earliest {j['first_flagged_at'].min()}, "
          f"latest {j['first_flagged_at'].max()}")
    live_table = pm._load_isotonic_table()

    results = []
    for stat_key, g in j.groupby("resolved_stat_key"):
        if len(g) >= MIN_GROUP_SIZE_FOR_DIAGNOSTIC:
            results.append(fit_stat(stat_key, g, live_table))

    print()
    print(f"{'stat':<38}{'n':>6}{'n_test':>7}{'gauss':>9}{'refit':>9}{'live_tbl':>9}  refit_beats  ready  was_live")
    rows = []
    for r in sorted(results, key=lambda r: -r["n"]):
        h = r["held"]
        was_live = r["stat"] in live_table
        if h:
            lt = "" if h["live_table"] is None else f"{h['live_table']:.4f}"
            print(f"{r['stat']:<38}{r['n']:>6}{h['n_test']:>7}{h['gauss']:>9.4f}{h['iso']:>9.4f}{lt:>9}"
                  f"  {'YES' if h['beats'] else 'no':<11} {'YES' if r['ready'] else 'no':<6} {'YES' if was_live else ''}")
        else:
            print(f"{r['stat']:<38}{r['n']:>6}   (too small for a held-out check)")
        lo, hi, val = r["blocks"]
        for a, b, v in zip(lo, hi, val):
            rows.append({"resolved_stat_key": r["stat"], "n_total": r["n"], "z_lo": a, "z_hi": b,
                         "calibrated_prob": v, "ready_to_apply": r["ready"],
                         "fit_date": datetime.now(timezone.utc).strftime("%Y-%m-%d")})

    ready = sorted(r["stat"] for r in results if r["ready"])
    dropped = sorted(set(live_table) - set(ready))
    added = sorted(set(ready) - set(live_table))
    print()
    print(f"Ready under the current configuration ({len(ready)}): {ready}")
    print(f"Currently live but NOT ready after refit -> would fall back to Gaussian: {dropped}")
    print(f"Newly ready: {added}")
    if write:
        pd.DataFrame(rows).to_csv(OUT_PATH, index=False)
        print(f"Wrote {len(rows)} blocks to {OUT_PATH}")
    else:
        print("(dry run -- pass --write to replace the live table)")


if __name__ == "__main__":
    main("--write" in sys.argv)
