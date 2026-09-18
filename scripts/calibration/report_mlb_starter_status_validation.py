"""
Session 2.33 -- MLB Starter/Lineup Confirmation Signal: Live Validation Report

Question (ROADMAP.md Session 2.33): among graded Underdog MLB legs that carry
a non-null `mlb_starter_status` (Session 2.32), does the real win rate differ
by bucket (confirmed / different_than_expected / not_yet_confirmed) enough to
justify gating flags on it?

Method: join clv_log.csv to outcome_log.csv (via the audit script's loader, so
breakeven is each row's own real implied probability, legs are deduped per
market and graded against the closing line, and significance uses a
game-clustered interval, never a per-leg one). Reports per bucket, per side,
a same-window baseline of Underdog MLB legs with no status, and a confound
check the first pass of this session found to matter:

`mlb_starter_status` is the value logged when a flag was LAST seen on the
board (clv_logger refreshes it each run). A flag that left the board hours
before first pitch can only ever show `not_yet_confirmed`, because MLB posts
lineups roughly 1-3 hours out. So the bucket is largely a proxy for "how long
before first pitch this flag left the board" (hrs_last below). The report
therefore also splits by that staleness, and compares buckets WITHIN a
staleness band, which is the only comparison that isolates lineup status.

Reporting only. Does not gate or change any flag.

USAGE
-----
python scripts/calibration/report_mlb_starter_status_validation.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pickem_model_validity_audit import cell_stats, graded_only, load_joined  # noqa: E402

BASE_DIR = Path(__file__).resolve().parents[2]
CLV_LOG_PATH = BASE_DIR / "data" / "pickem" / "clv_log.csv"

BUCKETS = ["confirmed", "not_yet_confirmed", "different_than_expected"]
STALE_BINS = [-99, 0.5, 1.5, 3, 6, 99]
STALE_LABELS = ["<=0.5h", "0.5-1.5h", "1.5-3h", "3-6h", ">6h"]


def fmt(label: str, g: pd.DataFrame) -> str:
    if g.empty:
        return f"  {label:<34} n=0"
    s = cell_stats(g)
    return (
        f"  {label:<34} n={s['n']:>5} games={s['n_clusters']:>3} win={s['win_rate']*100:5.1f}% "
        f"be={s['breakeven']*100:5.1f}% edge={s['edge']*100:+5.1f}pp "
        f"ci=[{s['cluster_ci_lo']*100:.1f},{s['cluster_ci_hi']*100:.1f}] {s['verdict']}"
    )


def load() -> pd.DataFrame:
    df = graded_only(load_joined())
    clv = pd.read_csv(
        CLV_LOG_PATH, low_memory=False,
        usecols=["flag_id", "mlb_starter_status", "first_flagged_at", "game_start_time", "last_seen_at"],
    )
    df = df.merge(clv, on="flag_id", how="left")
    df = df[(df["sport"] == "MLB") & (df["platform"] == "underdog")].copy()
    for c in ["first_flagged_at", "game_start_time", "last_seen_at"]:
        df[c] = pd.to_datetime(df[c], utc=True, errors="coerce")
    df["hrs_last"] = (df["game_start_time"] - df["last_seen_at"]).dt.total_seconds() / 3600
    df["stale"] = pd.cut(df["hrs_last"], STALE_BINS, labels=STALE_LABELS)
    return df


def main() -> None:
    u = load()
    s = u[u["mlb_starter_status"].notna()]
    print(f"Underdog MLB graded legs with a status: {len(s)}; game dates "
          f"{s['game_start_time'].dt.date.min()} to {s['game_start_time'].dt.date.max()}; "
          f"distinct games {s['game_id'].nunique()}")
    print()
    print("Per bucket (and by side):")
    for b in BUCKETS:
        g = s[s["mlb_starter_status"] == b]
        print(fmt(b, g))
        for side in ["over", "under"]:
            print(fmt(f"   {side}", g[g["flagged_side"] == side]))
    print()
    base = u[u["mlb_starter_status"].isna() & (u["game_start_time"] >= s["game_start_time"].min())]
    print(fmt("no status, same window (baseline)", base))
    print()
    print("Hours between last seen on board and first pitch, by bucket:")
    print(s.groupby("mlb_starter_status")["hrs_last"].describe().round(2).to_string())
    print()
    print("By staleness band (all buckets), per side:")
    for side in ["over", "under"]:
        print(f" {side}")
        for band, g in s[s["flagged_side"] == side].groupby("stale", observed=True):
            print(fmt(str(band), g))
    print()
    print("Bucket comparison WITHIN a staleness band (the only comparison that isolates lineup status), overs:")
    for band in STALE_LABELS:
        for b in ["confirmed", "not_yet_confirmed"]:
            g = s[(s["stale"] == band) & (s["flagged_side"] == "over") & (s["mlb_starter_status"] == b)]
            if len(g) >= 30:
                print(fmt(f"{band} {b}", g))


if __name__ == "__main__":
    main()
