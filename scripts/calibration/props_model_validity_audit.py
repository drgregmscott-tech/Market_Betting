"""
Session 6.12 -- Props Model Validity Audit

WHAT THIS IS
The props model flags player-prop bets (today: NFL anytime-touchdown and
2+ touchdown bets at DraftKings and BetMGM) when its probability is well above
the "market price". Session 6.11 started grading closed flags against real
results (data/sportsbook_props/outcome_log.csv). This audit asks the founding
question for this track: do the flagged bets win more often than the book's
odds require? It is the props twin of pickem_model_validity_audit.py.
Read-only: it changes no flag rule, no model and no log.

THE BREAKEVEN (the key fix over reusing one constant)
A bet at American odds pays a fixed amount. It breaks even when the win rate
equals the probability the odds quote (1 / decimal odds). That is each leg's
OWN breakeven. This audit reads it from the log's `over_american_odds`
(refreshed each run, so it is the last odds seen before close). Legs without
odds fall back to the newest CLV snapshot that has them; legs with none are
counted and left out of the profit measure.

The model instead scored edge against `first_flagged_market_price`. For a
touchdown market that price is field-normalized: the model divides each
player's price by the sum over the whole field, so the prices add to 1.0.
That is right for "who scores FIRST", where exactly one player wins. It is
wrong for "anytime" and "2+", where several players win. The audit reports
both breakevens side by side so the size of the gap is visible.

WHAT IT REPORTS
- Per book x market cell: legs, games, win rate with a game-clustered 95%
  interval (legs from one game are correlated), mean stated probability,
  mean quoted breakeven, mean logged price, profit per 1 unit staked (ROI at
  the real odds) with a game-clustered interval, and a verdict.
- Calibration by stated-probability band (does 30% mean 30%?).
- Sensitivity to the ungraded flags (players with no stat row: treated as
  losses, and excluded). Both are shown; a verdict must survive both.
- Field-vig flag counts and the game count behind each cell.

RULES FIXED BEFORE LOOKING AT ANY RESULT (as Session 2.65 did)
- A cell gets a verdict only with >= 30 graded legs AND >= 8 games. Else
  "insufficient".
- Verdict uses ROI: "beats" if the ROI interval low is above 0; "below" if
  the ROI interval high is below 0; else "inconclusive".
- "Worth building on" needs ALL of: verdict "beats", >= 100 legs, >= 30
  games, and still "beats" when ungraded flags count as losses. Nothing less
  is called worth building on.
- Clusters are per platform and game id. The same real NFL game has different
  ids at DraftKings and BetMGM, so a pooled interval is slightly too narrow;
  the per-book cells are the primary read.

Not covered (stated): the log has no player position, so no role split; all
flags are the OVER side, so no side split.

USAGE
    python props_model_validity_audit.py --report
"""

from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import numpy as np
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from pickem_model_validity_audit import clustered_ci  # noqa: E402  (mean CI, clustered)

PROPS_DIR = BASE_DIR / "data" / "sportsbook_props"
CLV_LOG_PATH = PROPS_DIR / "clv_log.csv"
OUTCOME_LOG_PATH = PROPS_DIR / "outcome_log.csv"
SNAPSHOT_DIR = PROPS_DIR / "clv_snapshots"

MIN_LEGS = 30
MIN_GAMES = 8
WORTH_MIN_LEGS = 100
WORTH_MIN_GAMES = 30
BANDS = [0.0, 0.15, 0.25, 0.35, 0.50, 1.01]
BAND_LABELS = ["<15%", "15-25%", "25-35%", "35-50%", ">=50%"]


def american_to_implied(odds: object) -> Optional[float]:
    if odds is None or pd.isna(odds):
        return None
    odds = float(odds)
    if odds == 0:
        return None
    return 100.0 / (odds + 100.0) if odds > 0 else -odds / (-odds + 100.0)


def market_name(stat_type: object) -> str:
    text = str(stat_type).strip().lower()
    return "2+ TDs" if text.startswith("2") else "Anytime TD"


def odds_from_snapshots(snapshot_dir: Path = SNAPSHOT_DIR) -> dict[str, float]:
    """Newest non-blank over_american_odds per flag_id across CLV snapshots."""
    found: dict[str, float] = {}
    if not snapshot_dir.exists():
        return found
    for path in sorted(snapshot_dir.glob("clv_log_*.csv")):
        snap = pd.read_csv(path, usecols=lambda c: c in ("flag_id", "over_american_odds"))
        if "over_american_odds" not in snap.columns:
            continue
        for fid, odds in snap.dropna(subset=["over_american_odds"]).itertuples(index=False):
            found[fid] = float(odds)
    return found


def load_joined(
    clv: Optional[pd.DataFrame] = None,
    outcomes: Optional[pd.DataFrame] = None,
    snapshot_odds: Optional[dict[str, float]] = None,
) -> pd.DataFrame:
    """One row per closed flag with a result column: win, loss or NaN (ungraded)."""
    clv = pd.read_csv(CLV_LOG_PATH) if clv is None else clv
    outcomes = pd.read_csv(OUTCOME_LOG_PATH) if outcomes is None else outcomes
    snapshot_odds = odds_from_snapshots() if snapshot_odds is None else snapshot_odds
    df = clv.loc[clv["status"] == "closed"].copy()
    res = outcomes.loc[outcomes["result"].isin(["win", "loss"]), ["flag_id", "result"]].drop_duplicates("flag_id")
    df = df.merge(res, on="flag_id", how="left")
    odds = df["over_american_odds"].where(df["over_american_odds"].notna(), df["flag_id"].map(snapshot_odds))
    df["quoted_breakeven"] = odds.map(american_to_implied)
    df["market"] = df["stat_type"].map(market_name)
    df["cluster"] = df["platform"].astype(str) + "|" + df["game_id"].astype(str)
    df["won"] = (df["result"] == "win").astype(float)
    # Profit per 1 unit staked at the quoted odds: a win pays (1/p - 1), a loss costs 1.
    payout = (1.0 / df["quoted_breakeven"]) - 1.0
    df["profit"] = np.where(df["result"] == "win", payout, np.where(df["result"] == "loss", -1.0, np.nan))
    df.loc[df["quoted_breakeven"].isna(), "profit"] = np.nan
    return df


def verdict(roi_lo: float, roi_hi: float, legs: int, games: int) -> str:
    if legs < MIN_LEGS or games < MIN_GAMES or np.isnan(roi_lo):
        return "insufficient"
    if roi_lo > 0:
        return "beats"
    if roi_hi < 0:
        return "below"
    return "inconclusive"


def cell_stats(group: pd.DataFrame) -> dict:
    graded = group.loc[group["result"].notna()]
    n = len(graded)
    games = int(graded["cluster"].nunique())
    out = {
        "flags_closed": len(group), "legs": n, "games": games, "ungraded": len(group) - n,
        "win_rate": float("nan"), "win_lo": float("nan"), "win_hi": float("nan"),
        "stated_prob": float("nan"), "quoted_breakeven": float("nan"), "logged_price": float("nan"),
        "legs_with_odds": 0, "roi": float("nan"), "roi_lo": float("nan"), "roi_hi": float("nan"),
        "verdict": "insufficient", "verdict_ungraded_as_losses": "insufficient",
    }
    if n == 0:
        return out
    y = graded["won"].to_numpy()
    out["win_rate"] = float(y.mean())
    out["win_lo"], out["win_hi"], _ = clustered_ci(y, graded["cluster"].to_numpy())
    out["stated_prob"] = float(graded["first_flagged_model_prob"].mean())
    out["quoted_breakeven"] = float(graded["quoted_breakeven"].mean())
    out["logged_price"] = float(graded["first_flagged_market_price"].mean())
    with_odds = graded.dropna(subset=["profit"])
    out["legs_with_odds"] = len(with_odds)
    if len(with_odds):
        p = with_odds["profit"].to_numpy()
        out["roi"] = float(p.mean())
        out["roi_lo"], out["roi_hi"], _ = clustered_ci(p, with_odds["cluster"].to_numpy())
        out["verdict"] = verdict(out["roi_lo"], out["roi_hi"], len(with_odds), int(with_odds["cluster"].nunique()))
    # Sensitivity: every ungraded flag counted as a loss (worst case for the model).
    worst = group.copy()
    lost = worst["result"].isna() & worst["quoted_breakeven"].notna()
    worst.loc[lost, "profit"] = -1.0
    worst = worst.dropna(subset=["profit"])
    if len(worst):
        wp = worst["profit"].to_numpy()
        lo, hi, _ = clustered_ci(wp, worst["cluster"].to_numpy())
        out["verdict_ungraded_as_losses"] = verdict(lo, hi, len(worst), int(worst["cluster"].nunique()))
    out["worth_building_on"] = bool(
        out["verdict"] == "beats" and out["verdict_ungraded_as_losses"] == "beats"
        and out["legs"] >= WORTH_MIN_LEGS and out["games"] >= WORTH_MIN_GAMES
    )
    return out


def build_cell_table(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for (platform, market), grp in df.groupby(["platform", "market"]):
        rows.append({"platform": platform, "market": market, **cell_stats(grp)})
    for platform, grp in df.groupby("platform"):
        rows.append({"platform": platform, "market": "ALL", **cell_stats(grp)})
    rows.append({"platform": "ALL", "market": "ALL", **cell_stats(df)})
    table = pd.DataFrame(rows)
    table["worth_building_on"] = table["worth_building_on"].fillna(False)
    return table


def calibration_bands(df: pd.DataFrame) -> pd.DataFrame:
    graded = df.loc[df["result"].notna()].copy()
    graded["band"] = pd.cut(graded["first_flagged_model_prob"], BANDS, labels=BAND_LABELS, right=False)
    rows = []
    for band, grp in graded.groupby("band", observed=True):
        lo, hi, _ = clustered_ci(grp["won"].to_numpy(), grp["cluster"].to_numpy())
        rows.append({
            "band": band, "legs": len(grp), "games": int(grp["cluster"].nunique()),
            "stated": grp["first_flagged_model_prob"].mean(), "win_rate": grp["won"].mean(),
            "win_lo": lo, "win_hi": hi, "quoted_breakeven": grp["quoted_breakeven"].mean(),
        })
    return pd.DataFrame(rows)


def field_vig_counts(df: pd.DataFrame) -> pd.DataFrame:
    col = df["implied_prob_includes_field_vig"].fillna("blank").astype(str)
    return df.groupby(["platform", col]).size().rename("flags").reset_index()


def pct(x: float) -> str:
    return "n/a" if x != x else f"{100 * x:.1f}%"


def main() -> None:
    df = load_joined()
    table = build_cell_table(df)
    bands = calibration_bands(df)
    print(f"Props model validity audit -- {len(df)} closed flags, {int(df['result'].notna().sum())} graded\n")
    for _, r in table.iterrows():
        print(
            f"{r['platform']:<11}{r['market']:<11} legs {r['legs']:>3} games {r['games']:>2}  "
            f"win {pct(r['win_rate'])} [{pct(r['win_lo'])}, {pct(r['win_hi'])}]  stated {pct(r['stated_prob'])}  "
            f"quoted BE {pct(r['quoted_breakeven'])}  logged price {pct(r['logged_price'])}  "
            f"ROI {pct(r['roi'])} [{pct(r['roi_lo'])}, {pct(r['roi_hi'])}]  "
            f"verdict {r['verdict']} / ungraded-as-loss {r['verdict_ungraded_as_losses']}  "
            f"worth building on: {bool(r['worth_building_on'])}"
        )
    print("\nCalibration by stated-probability band")
    for _, r in bands.iterrows():
        print(
            f"  {r['band']:<7} legs {r['legs']:>3} games {r['games']:>2}  stated {pct(r['stated'])}  "
            f"win {pct(r['win_rate'])} [{pct(r['win_lo'])}, {pct(r['win_hi'])}]  quoted BE {pct(r['quoted_breakeven'])}"
        )
    print("\nField-vig flag counts (flag time)")
    print(field_vig_counts(df).to_string(index=False))
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d")
    out_path = PROPS_DIR / f"model_validity_audit_{stamp}.csv"
    table.to_csv(out_path, index=False)
    print(f"\nCell table written to {out_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", action="store_true")
    parser.parse_args()
    main()
