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

import numpy as np
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]
CLV_LOG_PATH = BASE_DIR / "data" / "pickem" / "clv_log.csv"
OUTCOME_LOG_PATH = BASE_DIR / "data" / "pickem" / "outcome_log.csv"
OUT_DIR = BASE_DIR / "data" / "pickem"

MIN_CELL_N = 30  # interim floor, docs/sample_size_methodology.md Section 6
ZERO_INFLATION_THRESHOLD = 0.20  # >=20% of real outcomes are exactly 0
SKEW_THRESHOLD = 1.0  # |skew| > 1.0 treated as materially non-Gaussian
Z_95 = 1.96


def wilson_ci(wins: int, n: int, z: float = Z_95) -> tuple[float, float]:
    if n == 0:
        return (float("nan"), float("nan"))
    phat = wins / n
    denom = 1 + z**2 / n
    center = phat + z**2 / (2 * n)
    margin = z * math.sqrt(phat * (1 - phat) / n + z**2 / (4 * n**2))
    return ((center - margin) / denom, (center + margin) / denom)


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
        "flag_id", "odds_type", "allowed_wager_types",
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
    if n < MIN_CELL_N or math.isnan(p0):
        verdict = "not_enough_evidence"
    elif lo > p0:
        verdict = "beats_breakeven"
    elif hi < p0:
        verdict = "below_breakeven"
    else:
        verdict = "inconclusive"
    return {
        "n": n, "wins": wins, "win_rate": win_rate,
        "breakeven": p0, "edge": (win_rate - p0) if not math.isnan(p0) else float("nan"),
        "ci_lo": lo, "ci_hi": hi, "verdict": verdict,
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

    qualified = table.loc[table["verdict"] != "not_enough_evidence"].copy()
    print(f"Cells clearing the {MIN_CELL_N}-leg floor: {len(qualified)} of {len(table)}")
    print()
    print("Top 25 qualified cells by |edge| (real win rate - real per-row breakeven):")
    top = qualified.reindex(qualified["edge"].abs().sort_values(ascending=False).index).head(25)
    for _, r in top.iterrows():
        print(
            f"  {r['sport']:<8} {r['resolved_stat_key']:<28} {r['odds_bucket']:<10} "
            f"n={r['n']:>5} win={fmt_pct(r['win_rate'])} breakeven={fmt_pct(r['breakeven'])} "
            f"edge={r['edge']*100:+.2f}pp ci=[{fmt_pct(r['ci_lo'])},{fmt_pct(r['ci_hi'])}] {r['verdict']}"
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
    print("Directional check (flagged_side over vs under), per sport:")
    direc = directional_check(graded)
    for _, r in direc.iterrows():
        print(
            f"  {r['sport']:<8} {str(r['flagged_side']):<6} n={r['n']:>5} "
            f"win={fmt_pct(r['win_rate'])} breakeven={fmt_pct(r['breakeven'])} "
            f"edge={r['edge']*100:+.2f}pp {r['verdict']}"
        )
    print()

    # --- 4. Platform check (prizepicks vs underdog), per sport -----------
    print("Platform check (prizepicks vs underdog), per sport:")
    plat = platform_check(graded)
    for _, r in plat.iterrows():
        print(
            f"  {r['sport']:<8} {r['platform']:<11} n={r['n']:>5} "
            f"win={fmt_pct(r['win_rate'])} breakeven={fmt_pct(r['breakeven'])} "
            f"edge={r['edge']*100:+.2f}pp {r['verdict']}"
        )
    print()

    # --- 5. Clean slice ---------------------------------------------------
    cs = clean_slice(graded)
    print("Clean slice -- MLB, PrizePicks, Standard odds_type, Hits/Total Bases only "
          "(deduped, closing-line graded):")
    print(
        f"  n={cs['n']} win={fmt_pct(cs['win_rate'])} breakeven={fmt_pct(cs['breakeven'])} "
        f"edge={cs['edge']*100 if not math.isnan(cs['edge']) else float('nan'):+.2f}pp "
        f"ci=[{fmt_pct(cs['ci_lo'])},{fmt_pct(cs['ci_hi'])}] verdict={cs['verdict']}"
    )


if __name__ == "__main__":
    main()
