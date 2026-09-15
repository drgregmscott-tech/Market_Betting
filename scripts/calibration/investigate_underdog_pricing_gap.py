"""
Session 2.31 -- Underdog Cross-Sport Pricing Gap Investigation

WHY THIS SCRIPT EXISTS
-----------------------
Session 2.26's real MLB/NFL grading run found Underdog's real win rate is
below the 57.74% breakeven in BOTH sports tested (MLB 46.4%, NFL 49.5%,
n=9,499 / n=924), while PrizePicks is comfortably profitable in both
(66.9% / 69.4%). Worse, Underdog's real win rate FALLS as the model's own
stated edge RISES (edge~0%: 48.5%; edge~50%: 30.0%) -- an inverted
relationship a uniform sigma/overconfidence rescale cannot fix (that fixes
same-direction-wrong-magnitude, not a sign-flipped relationship). Two
cheap explanations were already ruled out in Session 2.26/before this
session started: a sign/side inversion in implied_prob_over_underdog()
(formula checked directly -- standard no-vig normalization, no flip), and
stale-pricing-at-flag-time (Underdog flags are caught with a SHORTER
median lead time, 7.3h, than PrizePicks', 13.7h -- the opposite of what a
staleness story predicts). A raw-field cross-check (payout_multiplier vs.
each option's own decimal_price/american_price on a real 14,273-line
Underdog pull) also confirmed payout_multiplier is a real, accurate
reflection of Underdog's own no-vig price (mean abs diff 0.49% across the
7,000 real two-sided lines in that file) -- not a broken/stale field.

This script is measurement only. It does not modify pickem_model.py,
sizing_engine.py, or any live scoring/badge logic (Session 2.26's
frontend "Below breakeven" badge is left untouched) -- same template as
Session 2.24's pickem_calibration_by_stat.py.

WHAT THIS SCRIPT DOES
----------------------
PART A -- source_line_id stability check (cheap, run first):
Loads several real, large Underdog raw snapshots from data/pickem/raw/
and checks whether the same over_under_lines[].id ever maps to a
DIFFERENT real (appearance_id, stat, stat_value) across snapshots taken
hours apart. If ids are stable, this rules out "flag_id/source_line_id
is silently picking up the wrong real prop" as a cause -- Underdog's
identifiers are trustworthy over the flag's real lifetime.

PART B -- real information-gap analysis, joining data/pickem/clv_log.csv
(flag_id, first_flagged_at, game_start_time, first_flagged_edge,
first_flagged_implied_prob, stat_type -- the real per-flag pricing/timing
record) against data/pickem/outcome_log.csv (flag_id, result -- the real
graded win/loss record) for Underdog rows only, across MLB and NFL:
  B1. Reproduce the edge-bucket win-rate inversion directly from this
      real joined data (not trusted from Session 2.26's report) --
      confirms this script is looking at the same signal before testing
      hypotheses against it.
  B2. Lead-time-crossed-with-edge test: does the inversion concentrate in
      LONG-lead-time flags (more real time for news to move Underdog's
      price after the model's own blend was computed), or does it persist
      even at short lead times (ruling out "the model was right when it
      looked, the world changed after" as a full explanation)?
  B3. Stat-type and implied-probability-skew breakdown: is the inversion
      concentrated on heavily-skewed ("chalk") Underdog lines, i.e. does
      the model's biggest stated edge appear exactly where Underdog's own
      price is most confident/skewed? That would be evidence the model is
      fighting a well-informed line, not finding a real edge.
Every cut reports its real n and is marked BELOW FLOOR (per this
project's MIN_GROUP_SIZE=20 convention, matching
pickem_calibration_by_stat.py / weekly_review.py) when too thin to trust.

USAGE
-----
python scripts/calibration/investigate_underdog_pricing_gap.py
    Reads data/pickem/clv_log.csv, data/pickem/outcome_log.csv, and (for
    Part A only) up to ID_STABILITY_SNAPSHOT_LIMIT real files from
    data/pickem/raw/underdog_*.json. Prints all tables. Writes no file.
"""

from __future__ import annotations

import glob
import json
from datetime import datetime
from pathlib import Path

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[2]
CLV_LOG_PATH = REPO_ROOT / "data" / "pickem" / "clv_log.csv"
OUTCOME_LOG_PATH = REPO_ROOT / "data" / "pickem" / "outcome_log.csv"
RAW_DIR = REPO_ROOT / "data" / "pickem" / "raw"

MIN_GROUP_SIZE = 20  # matches pickem_calibration_by_stat.py / weekly_review.py
BREAKEVEN = 0.5774  # PrizePicks-style 3x/2-pick breakeven, this project's standard reference point

# Part A: real large Underdog snapshots spanning ~17 hours on 2026-09-11/12,
# picked because they are full production pulls (~57MB / ~14,300 lines each),
# not the truncated/placeholder pulls also present in data/pickem/raw/.
ID_STABILITY_SNAPSHOTS = [
    "underdog_20260911T172815Z.json",
    "underdog_20260911T185609Z.json",
    "underdog_20260911T194533Z.json",
    "underdog_20260912T100543Z.json",
]


# ---------------------------------------------------------------------------
# PART A -- source_line_id stability check
# ---------------------------------------------------------------------------


def check_id_stability() -> None:
    print("=" * 78)
    print("PART A -- source_line_id (over_under_lines[].id) stability check")
    print("=" * 78)

    files = [RAW_DIR / name for name in ID_STABILITY_SNAPSHOTS]
    missing = [f for f in files if not f.exists()]
    if missing:
        print(f"SKIPPED -- missing real snapshot file(s): {[str(m) for m in missing]}")
        return

    snapshots: dict[str, dict[str, tuple]] = {}
    for f in files:
        with open(f, encoding="utf-8") as fh:
            payload = json.load(fh)
        lines = payload.get("over_under_lines") or []
        m: dict[str, tuple] = {}
        for line in lines:
            lid = line.get("id")
            over_under = line.get("over_under", {}) or {}
            appearance_stat = over_under.get("appearance_stat", {}) or {}
            key = (
                appearance_stat.get("appearance_id"),
                appearance_stat.get("stat"),
                line.get("stat_value"),
            )
            m[lid] = key
        snapshots[f.name] = m
        print(f"  {f.name}: {len(m)} real over_under_lines rows")

    names = list(snapshots.keys())
    common_ids = set(snapshots[names[0]].keys())
    for name in names[1:]:
        common_ids &= set(snapshots[name].keys())

    mismatches = []
    for lid in common_ids:
        values = {snapshots[name][lid] for name in names}
        if len(values) > 1:
            mismatches.append((lid, [snapshots[name][lid] for name in names]))

    print()
    print(f"Real source_line_ids present in ALL {len(names)} snapshots: {len(common_ids)}")
    print(f"Of those, ids whose (appearance_id, stat, stat_value) CHANGED across snapshots: {len(mismatches)}")
    for lid, vals in mismatches[:10]:
        print(f"  MISMATCH id={lid}: {vals}")

    if not mismatches:
        print(
            "RESULT: id-stability check is CLEAN -- no source_line_id in this "
            "real sample was ever reused for a different real (player, stat, "
            "line) across snapshots spanning ~17 real hours. Rules out a "
            "flag_id/source_line_id mismatch as a cause of the win-rate "
            "inversion."
        )
    else:
        print(
            "RESULT: id reuse FOUND -- this is a real data-integrity finding, "
            "not the clean result expected. Needs follow-up before trusting "
            "any Underdog-keyed join."
        )
    print()


# ---------------------------------------------------------------------------
# PART B -- real information-gap analysis
# ---------------------------------------------------------------------------


def _parse_iso(ts: str) -> datetime | None:
    if not isinstance(ts, str) or not ts.strip():
        return None
    try:
        return pd.Timestamp(ts).to_pydatetime()
    except (ValueError, TypeError):
        return None


def load_joined_underdog() -> pd.DataFrame:
    """Join clv_log.csv (real per-flag price/timing) to outcome_log.csv (real
    graded result) on flag_id, restricted to real Underdog win/loss rows."""
    clv = pd.read_csv(CLV_LOG_PATH, low_memory=False)
    outcome = pd.read_csv(OUTCOME_LOG_PATH, low_memory=False)

    outcome_graded = outcome.loc[outcome["result"].isin(["win", "loss"])].copy()
    outcome_graded["win"] = (outcome_graded["result"] == "win").astype(int)

    joined = outcome_graded.merge(
        clv[["flag_id", "first_flagged_at", "game_start_time"]],
        on="flag_id",
        how="left",
        suffixes=("", "_clv"),
    )

    underdog = joined.loc[joined["platform"] == "underdog"].copy()
    underdog = underdog.dropna(subset=["first_flagged_edge", "first_flagged_at", "game_start_time"])

    underdog["first_flagged_at_dt"] = underdog["first_flagged_at"].apply(_parse_iso)
    underdog["game_start_time_dt"] = underdog["game_start_time"].apply(_parse_iso)
    underdog = underdog.dropna(subset=["first_flagged_at_dt", "game_start_time_dt"])

    underdog["lead_time_hours"] = underdog.apply(
        lambda r: (r["game_start_time_dt"] - r["first_flagged_at_dt"]).total_seconds() / 3600.0,
        axis=1,
    )
    # Drop nonsensical negative lead times (flag logged after game start --
    # a real but separate data-quality question, not in scope for this
    # investigation; excluding keeps the lead-time analysis honest rather
    # than silently averaging in rows that can't mean what they'd suggest).
    before = len(underdog)
    underdog = underdog.loc[underdog["lead_time_hours"] >= 0]
    dropped = before - len(underdog)
    if dropped:
        print(f"(Dropped {dropped} real row(s) with negative lead_time_hours before Part B analysis.)")

    return underdog


def _report_bucket(label: str, df: pd.DataFrame, group_col: str) -> None:
    print(f"\n{label}")
    print(f"{'bucket':<28} {'n':>6} {'win%':>7} {'avg_edge':>9} {'avg_implied':>12}")
    print("-" * 66)
    for bucket, g in df.groupby(group_col, observed=True):
        n = len(g)
        flag = "  (BELOW FLOOR n<20)" if n < MIN_GROUP_SIZE else ""
        print(
            f"{str(bucket):<28} {n:>6} {g['win'].mean()*100:>6.1f}% "
            f"{g['first_flagged_edge'].mean():>+9.4f} "
            f"{g['first_flagged_implied_prob'].mean():>12.4f}{flag}"
        )


def edge_bucket(edge: float) -> str:
    if edge < 0.10:
        return "0.00-0.10"
    if edge < 0.20:
        return "0.10-0.20"
    if edge < 0.30:
        return "0.20-0.30"
    if edge < 0.40:
        return "0.30-0.40"
    return "0.40+"


def lead_time_bucket(hours: float) -> str:
    if hours < 3:
        return "0-3h (short)"
    if hours < 8:
        return "3-8h (medium)"
    if hours < 16:
        return "8-16h (long)"
    return "16h+ (very long)"


def implied_prob_skew_bucket(implied_prob: float) -> str:
    skew = abs(implied_prob - 0.5)
    if skew < 0.05:
        return "near-coinflip (|p-0.5|<0.05)"
    if skew < 0.15:
        return "mild skew (0.05-0.15)"
    return "chalk / heavy skew (>=0.15)"


def run_part_b() -> None:
    print("=" * 78)
    print("PART B -- real information-gap analysis (Underdog, MLB + NFL)")
    print("=" * 78)

    underdog = load_joined_underdog()
    print(f"\nReal joined Underdog win/loss legs with usable edge+timing data: {len(underdog)}")
    print(underdog["sport"].value_counts().to_string())
    print(f"\nOverall real Underdog win rate: {underdog['win'].mean()*100:.1f}% "
          f"(breakeven reference: {BREAKEVEN*100:.2f}%)")

    underdog["edge_bucket"] = underdog["first_flagged_edge"].apply(edge_bucket)
    underdog["lead_bucket"] = underdog["lead_time_hours"].apply(lead_time_bucket)
    underdog["skew_bucket"] = underdog["first_flagged_implied_prob"].apply(implied_prob_skew_bucket)

    # B1 -- reproduce the edge-bucket inversion directly from real data.
    _report_bucket("B1. Win rate by edge bucket (reproduction of Session 2.26's finding)",
                    underdog, "edge_bucket")

    # B1b -- same split by sport, since MLB dominates the pooled n.
    for sport in sorted(underdog["sport"].unique()):
        sub = underdog.loc[underdog["sport"] == sport]
        _report_bucket(f"B1b. Win rate by edge bucket -- {sport} only", sub, "edge_bucket")

    # B2 -- lead time crossed with edge level (the key test the roadmap card asks for).
    print("\n" + "=" * 78)
    print("B2. Lead-time x edge-level cross tab (key test)")
    print("=" * 78)
    for lead in ["0-3h (short)", "3-8h (medium)", "8-16h (long)", "16h+ (very long)"]:
        sub = underdog.loc[underdog["lead_bucket"] == lead]
        if len(sub) == 0:
            continue
        _report_bucket(f"Lead time = {lead} (n={len(sub)} total)", sub, "edge_bucket")

    # B3 -- implied-probability skew ("chalk") breakdown.
    _report_bucket("\nB3. Win rate by Underdog implied-probability skew bucket", underdog, "skew_bucket")

    # B3b -- does model edge correlate with how skewed Underdog's own price already is?
    corr = underdog["first_flagged_edge"].corr(
        (underdog["first_flagged_implied_prob"] - 0.5).abs()
    )
    print(f"\nCorrelation(model's stated edge, |Underdog implied_prob - 0.5|): {corr:+.4f}")
    print(
        "(Positive => the model's biggest claimed edges cluster on Underdog's "
        "most price-skewed/confident lines -- evidence the model disagrees "
        "hardest exactly where Underdog's own price is most informed, not "
        "where it is softest.)"
    )

    # B3d -- isolate skew as a confound: within near-coinflip lines only,
    # does the edge-bucket inversion still appear? If not, the inversion is
    # a property of skewed/chalk lines, not of "high edge" in general.
    print("\nB3d. Win rate by edge bucket, RESTRICTED to near-coinflip Underdog lines only (|implied_prob-0.5|<0.05)")
    near_coinflip = underdog.loc[underdog["skew_bucket"] == "near-coinflip (|p-0.5|<0.05)"]
    _report_bucket(f"(n={len(near_coinflip)} total near-coinflip legs)", near_coinflip, "edge_bucket")

    # B3c -- stat-type breakdown, floor-gated.
    print("\nB3c. Win rate by stat_type (Underdog, real n per group; floor = 20)")
    counts = underdog["stat_type"].value_counts()
    header = f"{'stat_type':<30} {'n':>6} {'win%':>7} {'avg_edge':>9}"
    print(header)
    print("-" * len(header))
    for stat, n in counts.items():
        g = underdog.loc[underdog["stat_type"] == stat]
        flag = "  (BELOW FLOOR n<20)" if n < MIN_GROUP_SIZE else ""
        print(f"{str(stat):<30} {n:>6} {g['win'].mean()*100:>6.1f}% {g['first_flagged_edge'].mean():>+9.4f}{flag}")


def main() -> None:
    check_id_stability()
    run_part_b()


if __name__ == "__main__":
    main()
