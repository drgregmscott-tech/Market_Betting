"""
Session 2.37 -- Pick'em Model Validity Reassessment (Full Audit)

WHY THIS EXISTS
----------------
A 2026-09-17 morning-status conversation found and fixed two compounding
measurement bugs in auto_grade_outcomes.py (grading against
first_flagged_line instead of the real closing line; counting every
re-flag of the same real market as an independent sample instead of
deduping on player+stat+game+odds_type -- see that file's grading_line()/
market_key()/select_closing_flags()). Fixing those bugs and re-running the
full grader (2026-09-17, 07:42 local -- see logs/auto_grade_outcomes.log)
produced a clean data/pickem/outcome_log.csv: 51,846 auto-graded rows,
28,078 of them real win/loss/push grades on deduped, closing-line markets,
23,768 void (superseded re-flags of the same market, correctly excluded
from win-rate stats).

That fix answers "is the DATA clean" -- it does not answer the project's
founding question: does this track's model actually identify real +EV
opportunities? This script is a step back to answer that directly, per
ROADMAP.md's Session 2.37 card. It measures three more things the
existing calibration scripts (fit_sigma_recalibration.py,
pickem_calibration_by_stat.py) do not:

1. A flat 57.74% breakeven (outcome_tracker.py's BREAKEVEN_WIN_RATE) is
   wrong for any non-Standard PrizePicks line (Demon ~52.8%, Goblin
   ~69.5%) and for Underdog (its own per-leg multiplier-derived implied
   probability, already computed and stored per row at flag time as
   closing_implied_prob / first_flagged_implied_prob). This script uses
   each row's OWN real implied probability as its breakeven, not one flat
   constant, then rolls that up per sport x stat x odds_type cell.
2. Whether a stat's real outcome distribution (actual_value, already
   stored per graded leg) is zero-inflated / heavily right-skewed --
   confirmed live for MLB RBIs/Walks in the 2026-09-17 conversation -- a
   shape prob_over()'s plain Gaussian CDF cannot represent regardless of
   how well sigma is tuned.
3. A "clean slice" isolating MLB standard-odds-type, Gaussian-appropriate
   stats only (Hits, Total Bases), on this now-deduped, closing-line-graded
   data -- the cleanest available read on whether a real edge survives once
   every known measurement bug is stripped away.

Every cell below MIN_CELL_N (30 -- interim floor, matches
docs/sample_size_methodology.md Section 6 and weekly_review.py's own
MIN_GROUP_SIZE_FOR_CHECK convention) is labeled "not yet enough evidence,"
never silently included or excluded. Significance uses a Wilson score
interval around the real win rate vs. that cell's own mean real breakeven
-- not a point-estimate eyeball comparison -- so "beats breakeven" means
the interval's lower bound clears breakeven, not just that the point
estimate does.

SESSION 2.38 ADDITION -- CLUSTER-ROBUST SIGNIFICANCE, NOT JUST PER-LEG
------------------------------------------------------------------------
Session 2.38 (the NFL grading-path follow-up to this script's own Finding
#4) found a real methodology gap in the per-leg Wilson CI above: many
graded legs share the same real game (multiple players/stats from one
NFL Sunday, one MLB game, etc.), so they are not independent trials the
way the Wilson interval assumes. Checked live: NFL's entire graded sample
(1,972 legs) traces back to only 30 real games -- a per-leg test reported
a tight, "highly significant" interval on what is really ~30 correlated
data points, not ~2,000 independent ones. Every cell now also gets a
cluster-robust CI (clustered on the real `game_id` behind each leg, sandwich/
linearized variance estimator -- same method underlying `statsmodels`'
`cov_type="cluster"`, reimplemented directly here with numpy to avoid a
new dependency) alongside the naive per-leg Wilson interval. A cell's
FINAL verdict uses the cluster-robust interval, not the per-leg one --
the per-leg Wilson interval is kept in the output for comparison, so a
case where the two disagree (like NFL's did) is visible, not hidden.
Cells backed by fewer than MIN_CLUSTERS distinct games are labeled
"not_enough_evidence" regardless of leg count, for the same reason a
30-leg floor exists for uncorrelated data -- 30 correlated legs from 3
games is not real evidence either.

SESSION 2.62 CORRECTION -- WHAT "BREAKEVEN" MEANS FOR PRIZEPICKS ROWS
------------------------------------------------------------------------
The per-row breakeven above was the implied probability LOGGED at flag time.
For PrizePicks that logged number was never a real breakeven: Standard rows
carry the flat 0.5 constant (6,006 of 6,065 graded Standard rows), and
Demon/Goblin rows carry single-lineup constants (0.472/0.528 and 0.305/
0.695). Sessions 2.55/2.56 found PrizePicks prices each leg separately and
that the all-Standard payouts are 2/4.75/9/19/36.5x, so the real per-leg
breakeven is 0.7071 ... 0.5491 depending on entry size. Scoring Standard
against 0.5 made every PrizePicks Standard cell look about 5 points better
than it is. Now, in load_joined(): PrizePicks Standard rows use the reference
entry's breakeven (5-pick, 0.5549, same as the dashboards, Session 2.57);
PrizePicks Demon/Goblin rows get NO breakeven (verdict "no_valid_breakeven":
their per-leg price was never measured in general); Underdog rows keep their
logged implied probability (not re-examined here). The logged value stays in
the `breakeven_logged` column. Tables that mix rows (over/under, platform,
clean slice) use only rows that have a breakeven.

USAGE
-----
python scripts/calibration/pickem_model_validity_audit.py
    Loads data/pickem/clv_log.csv + data/pickem/outcome_log.csv, prints
    the full report to stdout, and writes the per-cell table to
    data/pickem/model_validity_audit_<date>.csv (durable record, matching
    this project's existing *_log.csv / *_report.csv convention).
"""

from __future__ import annotations

import math
from datetime import datetime, timezone
from pathlib import Path

import sys

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "sizing"))
from sizing_engine import breakeven_win_rate_per_leg  # noqa: E402

BASE_DIR = Path(__file__).resolve().parents[2]
CLV_LOG_PATH = BASE_DIR / "data" / "pickem" / "clv_log.csv"
OUTCOME_LOG_PATH = BASE_DIR / "data" / "pickem" / "outcome_log.csv"
OUT_DIR = BASE_DIR / "data" / "pickem"

MIN_CELL_N = 30  # interim floor, docs/sample_size_methodology.md Section 6
MIN_CLUSTERS = 8  # interim floor on distinct real games -- see Session 2.38 note above
ZERO_INFLATION_THRESHOLD = 0.20  # >=20% of real outcomes are exactly 0
SKEW_THRESHOLD = 1.0  # |skew| > 1.0 treated as materially non-Gaussian
Z_95 = 1.96
REFERENCE_ENTRY_LEGS = 5  # PrizePicks reference entry; docs/sample_size_methodology.md
PRIZEPICKS_STANDARD_BREAKEVEN = breakeven_win_rate_per_leg("prizepicks", REFERENCE_ENTRY_LEGS)


def wilson_ci(wins: int, n: int, z: float = Z_95) -> tuple[float, float]:
    if n == 0:
        return (float("nan"), float("nan"))
    phat = wins / n
    denom = 1 + z**2 / n
    center = phat + z**2 / (2 * n)
    margin = z * math.sqrt(phat * (1 - phat) / n + z**2 / (4 * n**2))
    return ((center - margin) / denom, (center + margin) / denom)


def clustered_ci(y: np.ndarray, clusters: np.ndarray, z: float = Z_95) -> tuple[float, float, int]:
    """Cluster-robust (sandwich/linearized) CI around a real win rate,
    clustered on the real game each leg belongs to -- same method
    underlying statsmodels' cov_type="cluster" for a single-regressor
    (intercept-only) OLS fit on a 0/1 outcome, reimplemented directly with
    numpy so this project adds no new dependency. See Session 2.38's
    module-docstring note for why this exists: many legs share the same
    real game, so they are not independent trials, and a naive per-leg
    Wilson interval overstates confidence whenever that correlation is
    real (confirmed live for NFL -- see SESSION_LOG.md).
    Returns (lo, hi, n_clusters); (nan, nan, 0) if there's nothing to compute."""
    n = len(y)
    if n == 0:
        return (float("nan"), float("nan"), 0)
    phat = float(np.mean(y))
    uniq = pd.unique(clusters)
    C = len(uniq)
    if C < 2:
        return (float("nan"), float("nan"), C)
    resid = y - phat
    cluster_sums = pd.Series(resid).groupby(clusters, observed=True).sum().to_numpy()
    var = (C / (C - 1)) * float(np.sum(cluster_sums**2)) / (n**2)
    se = math.sqrt(max(var, 0.0))
    return (phat - z * se, phat + z * se, C)


def sample_skew(x: np.ndarray) -> float:
    x = x[~np.isnan(x)]
    if len(x) < 3:
        return float("nan")
    mean = x.mean()
    sd = x.std(ddof=0)
    if sd == 0:
        return 0.0
    return float(np.mean(((x - mean) / sd) ** 3))


def load_joined() -> pd.DataFrame:
    clv = pd.read_csv(CLV_LOG_PATH, low_memory=False)
    oc = pd.read_csv(OUTCOME_LOG_PATH, low_memory=False)

    clv_cols = [
        "flag_id", "odds_type", "allowed_wager_types", "game_id",
        "closing_implied_prob", "first_flagged_implied_prob",
    ]
    df = oc.merge(clv[clv_cols], on="flag_id", how="left", suffixes=("", "_clv"))

    # Real per-row breakeven: prefer the real closing implied prob (what
    # was actually live right before the market locked); fall back to
    # first_flagged_implied_prob only when a closing re-check never ran.
    df["breakeven"] = df["closing_implied_prob"]
    missing = df["breakeven"].isna()
    df.loc[missing, "breakeven"] = df.loc[missing, "first_flagged_implied_prob"]

    def odds_bucket(row) -> str:
        if row["platform"] == "underdog":
            return "underdog"
        ot = row["odds_type"]
        if isinstance(ot, str) and ot.strip():
            return ot.strip().lower()
        return "standard"  # PrizePicks missing odds_type -- matches
        # pickem_model.py's is_scorable_prizepicks_odds_type() default.

    df["odds_bucket"] = df.apply(odds_bucket, axis=1)
    return apply_breakeven_reference(df)


def apply_breakeven_reference(df: pd.DataFrame) -> pd.DataFrame:
    """Session 2.62: replace the logged (never-real) PrizePicks breakevens.
    Keeps the logged number in `breakeven_logged`. See module note."""
    df = df.copy()
    df["breakeven_logged"] = df["breakeven"]
    is_pp = df["platform"] == "prizepicks"
    df.loc[is_pp & (df["odds_bucket"] == "standard"), "breakeven"] = PRIZEPICKS_STANDARD_BREAKEVEN
    df.loc[is_pp & (df["odds_bucket"] != "standard"), "breakeven"] = float("nan")
    return df


def graded_only(df: pd.DataFrame) -> pd.DataFrame:
    """win/loss only -- push and void excluded from win-rate stats,
    matching outcome_tracker.build_report()'s own convention."""
    return df.loc[df["result"].isin(["win", "loss"])].copy()


def cell_stats(group: pd.DataFrame) -> dict:
    n = len(group)
    wins = int((group["result"] == "win").sum())
    win_rate = wins / n if n else float("nan")
    breakeven = group["breakeven"].dropna()
    p0 = float(breakeven.mean()) if len(breakeven) else float("nan")
    lo, hi = wilson_ci(wins, n)

    y = (group["result"] == "win").to_numpy(dtype=float)
    # Missing game_id (older/legacy rows) must each be their own singleton
    # cluster, not silently dropped (pandas groupby drops NaN keys) or
    # silently pooled together as one giant fake cluster -- same
    # conservative "no stable id -> treat as its own market" convention
    # auto_grade_outcomes.py's market_key() already uses.
    game_id = group["game_id"]
    cluster_key = game_id.astype(str).where(
        game_id.notna(), "__no_game_id__|" + pd.Series(group.index, index=group.index).astype(str)
    ).to_numpy()
    c_lo, c_hi, n_clusters = clustered_ci(y, cluster_key)

    if n < MIN_CELL_N or n_clusters < MIN_CLUSTERS:
        verdict = "not_enough_evidence"
    elif math.isnan(p0):
        verdict = "no_valid_breakeven"  # Session 2.62: e.g. PrizePicks Demon/Goblin
    elif c_lo > p0:
        verdict = "beats_breakeven"
    elif c_hi < p0:
        verdict = "below_breakeven"
    else:
        verdict = "inconclusive"
    return {
        "n": n, "wins": wins, "win_rate": win_rate, "n_clusters": n_clusters,
        "breakeven": p0, "edge": (win_rate - p0) if not math.isnan(p0) else float("nan"),
        "ci_lo": lo, "ci_hi": hi,
        "cluster_ci_lo": c_lo, "cluster_ci_hi": c_hi,
        "verdict": verdict,
    }


def build_cell_table(graded: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for (sport, stat, bucket), group in graded.groupby(
        ["sport", "resolved_stat_key", "odds_bucket"], dropna=False
    ):
        stats = cell_stats(group)
        rows.append({"sport": sport, "resolved_stat_key": stat, "odds_bucket": bucket, **stats})
    table = pd.DataFrame(rows)
    return table.sort_values(["n"], ascending=False).reset_index(drop=True)


def shape_check(graded: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for (sport, stat), group in graded.groupby(["sport", "resolved_stat_key"]):
        n = len(group)
        if n < MIN_CELL_N:
            continue
        vals = group["actual_value"].to_numpy(dtype=float)
        zero_rate = float(np.mean(vals == 0))
        skew = sample_skew(vals)
        non_gaussian = (zero_rate >= ZERO_INFLATION_THRESHOLD) or (
            not math.isnan(skew) and abs(skew) > SKEW_THRESHOLD
        )
        rows.append({
            "sport": sport, "resolved_stat_key": stat, "n": n,
            "zero_rate": zero_rate, "skew": skew,
            "flagged_non_gaussian": non_gaussian,
        })
    return pd.DataFrame(rows).sort_values("n", ascending=False).reset_index(drop=True)


def directional_check(graded: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for (sport, side), group in graded.groupby(["sport", "flagged_side"]):
        stats = cell_stats(group)
        rows.append({"sport": sport, "flagged_side": side, **stats})
    return pd.DataFrame(rows).sort_values(["sport", "flagged_side"]).reset_index(drop=True)


def platform_check(graded: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for (sport, platform), group in graded.groupby(["sport", "platform"]):
        stats = cell_stats(group)
        rows.append({"sport": sport, "platform": platform, **stats})
    return pd.DataFrame(rows).sort_values(["sport", "platform"]).reset_index(drop=True)


def clean_slice(graded: pd.DataFrame) -> dict:
    mask = (
        (graded["sport"].str.upper() == "MLB")
        & (graded["platform"] == "prizepicks")
        & (graded["odds_bucket"] == "standard")
        & (graded["resolved_stat_key"].isin(["hits", "totalBases"]))
    )
    return cell_stats(graded.loc[mask])


def fmt_pct(x: float) -> str:
    return "n/a" if x is None or (isinstance(x, float) and math.isnan(x)) else f"{x*100:.2f}%"


def main() -> None:
    df = load_joined()
    graded = graded_only(df)
    print(f"Total outcome_log.csv rows: {len(df)}")
    print(f"Real win/loss graded rows (push/void excluded): {len(graded)}")
    print()

    # --- 1. Per-sport x per-stat x per-odds_type calibration table -----
    table = build_cell_table(graded)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d")
    out_path = OUT_DIR / f"model_validity_audit_{stamp}.csv"
    table.to_csv(out_path, index=False)
    print(f"Full {len(table)}-cell sport x stat x odds_type table written to {out_path}")
    print()

    qualified = table.loc[~table["verdict"].isin(["not_enough_evidence", "no_valid_breakeven"])].copy()
    unpriced = table.loc[table["verdict"] == "no_valid_breakeven"]
    print(f"Cells with no valid breakeven (PrizePicks Demon/Goblin): {len(unpriced)} cells, "
          f"{int(unpriced['n'].sum())} legs, listed in the CSV but not scored.")
    print(f"Cells clearing the {MIN_CELL_N}-leg floor: {len(qualified)} of {len(table)}")
    print()
    print("Top 25 qualified cells by |edge| (real win rate - real per-row breakeven).")
    print("cluster_ci is the authoritative interval (clustered on real game_id -- see Session")
    print("2.38 module note); leg_ci is the naive per-leg Wilson interval, kept for comparison.")
    top = qualified.reindex(qualified["edge"].abs().sort_values(ascending=False).index).head(25)
    for _, r in top.iterrows():
        print(
            f"  {r['sport']:<8} {r['resolved_stat_key']:<28} {r['odds_bucket']:<10} "
            f"n={r['n']:>5} games={r['n_clusters']:>3} win={fmt_pct(r['win_rate'])} "
            f"breakeven={fmt_pct(r['breakeven'])} edge={r['edge']*100:+.2f}pp "
            f"leg_ci=[{fmt_pct(r['ci_lo'])},{fmt_pct(r['ci_hi'])}] "
            f"cluster_ci=[{fmt_pct(r['cluster_ci_lo'])},{fmt_pct(r['cluster_ci_hi'])}] {r['verdict']}"
        )
    print()

    # --- 2. Gaussian-shape check ----------------------------------------
    shape = shape_check(graded)
    flagged_shape = shape.loc[shape["flagged_non_gaussian"]]
    print(f"Stat/sport cells checked for distribution shape (n>={MIN_CELL_N}): {len(shape)}")
    print(f"Flagged non-Gaussian (zero-rate>={ZERO_INFLATION_THRESHOLD:.0%} or |skew|>{SKEW_THRESHOLD}): "
          f"{len(flagged_shape)}")
    for _, r in flagged_shape.sort_values("n", ascending=False).iterrows():
        print(
            f"  {r['sport']:<8} {r['resolved_stat_key']:<28} n={r['n']:>5} "
            f"zero_rate={r['zero_rate']*100:.1f}% skew={r['skew']:+.2f}"
        )
    print()

    # --- 3. Directional bias (over vs under), per sport -----------------
    priced = graded.loc[graded["breakeven"].notna()]
    print(f"(Sections 3-5 use the {len(priced)} of {len(graded)} graded legs that have a valid breakeven.)")
    print("Directional check (flagged_side over vs under), per sport:")
    direc = directional_check(priced)
    for _, r in direc.iterrows():
        print(
            f"  {r['sport']:<8} {str(r['flagged_side']):<6} n={r['n']:>5} games={r['n_clusters']:>3} "
            f"win={fmt_pct(r['win_rate'])} breakeven={fmt_pct(r['breakeven'])} "
            f"edge={r['edge']*100:+.2f}pp cluster_ci=[{fmt_pct(r['cluster_ci_lo'])},"
            f"{fmt_pct(r['cluster_ci_hi'])}] {r['verdict']}"
        )
    print()

    # --- 4. Platform check (prizepicks vs underdog), per sport -----------
    print("Platform check (prizepicks vs underdog), per sport:")
    plat = platform_check(priced)
    for _, r in plat.iterrows():
        print(
            f"  {r['sport']:<8} {r['platform']:<11} n={r['n']:>5} games={r['n_clusters']:>3} "
            f"win={fmt_pct(r['win_rate'])} breakeven={fmt_pct(r['breakeven'])} "
            f"edge={r['edge']*100:+.2f}pp cluster_ci=[{fmt_pct(r['cluster_ci_lo'])},"
            f"{fmt_pct(r['cluster_ci_hi'])}] {r['verdict']}"
        )
    print()

    # --- 5. Clean slice ---------------------------------------------------
    cs = clean_slice(priced)
    print("Clean slice -- MLB, PrizePicks, Standard odds_type, Hits/Total Bases only "
          "(deduped, closing-line graded):")
    print(
        f"  n={cs['n']} games={cs['n_clusters']} win={fmt_pct(cs['win_rate'])} "
        f"breakeven={fmt_pct(cs['breakeven'])} "
        f"edge={cs['edge']*100 if not math.isnan(cs['edge']) else float('nan'):+.2f}pp "
        f"cluster_ci=[{fmt_pct(cs['cluster_ci_lo'])},{fmt_pct(cs['cluster_ci_hi'])}] "
        f"verdict={cs['verdict']}"
    )


if __name__ == "__main__":
    main()
