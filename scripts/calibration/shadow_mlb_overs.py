"""
Session 2.65 -- Shadow Measure for PrizePicks MLB Overs

WHAT THIS IS
Since Session 2.64 the model no longer flags PrizePicks MLB overs. Once a
side is not flagged it is never graded, so its record stops growing and we
could never learn whether it recovers. This keeps a SHADOW record: every
PrizePicks MLB Standard over that WOULD have been flagged (model edge of 3
points or more, the normal flag threshold) is logged and graded exactly like
a real flag, in its own files. Nothing here touches the real flags, the
real outcome log, sizing, the dashboard or any audit.

FILES
  data/pickem/shadow_clv_log.csv       same columns and lifecycle as clv_log.csv
  data/pickem/shadow_outcome_log.csv   same columns as outcome_log.csv

HOW
  --track   read output/estimation/latest.csv, keep PrizePicks MLB Standard
            rows, compute the over edge the model no longer computes
            (prob_over - implied_prob_over), and run them through the SAME
            clv_logger.process_run_pickem() with the unflagged-sides rule
            switched off. Over side only.
  --grade   grade closed shadow flags with the SAME auto_grade_outcomes.run()
            (MLB adapter only, closing line, deduped by market).
  --report  read-only: win rate, game-clustered 95% interval, and a
            verdict against the 5- and 6-pick per-leg breakevens.
  --run     --track then --grade (what the pipeline runs).

DECISION RULE (fixed before any shadow leg exists)
  Re-check only when there are at least MIN_LEGS_FOR_RECHECK graded shadow
  legs across at least MIN_GAMES_FOR_RECHECK games. Then:
    interval low above the 5-pick breakeven  -> "recovered": consider
        removing ("mlb", "over") from PRIZEPICKS_UNFLAGGED_SIDES;
    interval high below the 6-pick breakeven -> "still below": keep the rule;
    otherwise -> "inconclusive": keep the rule, keep collecting.
  Baseline before the rule: 50.1% on 2,969 legs, 108 games.
"""

from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
BASE_DIR = HERE.parents[1]
for _sub in (HERE, BASE_DIR / "scripts" / "sizing", BASE_DIR / "scripts" / "estimation"):
    sys.path.insert(0, str(_sub))

import auto_grade_outcomes as grader  # noqa: E402
import clv_logger  # noqa: E402
import pickem_model_validity_audit as audit  # noqa: E402
from outcome_tracker import OUTCOME_LOG_COLUMNS  # noqa: E402
from sizing_engine import breakeven_win_rate_per_leg  # noqa: E402

SHADOW_CLV_LOG_PATH = BASE_DIR / "data" / "pickem" / "shadow_clv_log.csv"
SHADOW_OUTCOME_LOG_PATH = BASE_DIR / "data" / "pickem" / "shadow_outcome_log.csv"
ESTIMATES_PATH = BASE_DIR / "output" / "estimation" / "latest.csv"

MIN_LEGS_FOR_RECHECK = 200
MIN_GAMES_FOR_RECHECK = 30
HURDLE_5 = breakeven_win_rate_per_leg("prizepicks", 5)
HURDLE_6 = breakeven_win_rate_per_leg("prizepicks", 6)


def build_shadow_estimates(estimates_df: pd.DataFrame) -> pd.DataFrame:
    """PrizePicks MLB Standard rows with the OVER edge the model no longer
    computes; the under edge is blanked so only the over side can be flagged."""
    df = estimates_df.copy()
    odds = df["odds_type"].fillna("standard").astype(str).str.strip().str.lower()
    keep = (
        (df["platform"] == "prizepicks")
        & (df["sport"].fillna("").astype(str).str.strip().str.lower() == "mlb")
        & (odds == "standard")
        & (df["model_status"] == "estimated")
        & df["prob_over"].notna()
        & df["implied_prob_over"].notna()
    )
    df = df.loc[keep].copy()
    df["edge_over"] = df["prob_over"] - df["implied_prob_over"]
    df["edge_under"] = None
    return df


def _load_shadow_clv() -> pd.DataFrame:
    return clv_logger.load_clv_log_generic(SHADOW_CLV_LOG_PATH, clv_logger.CLV_LOG_COLUMNS_PICKEM)


def _load_shadow_outcomes() -> pd.DataFrame:
    if SHADOW_OUTCOME_LOG_PATH.exists():
        df = pd.read_csv(SHADOW_OUTCOME_LOG_PATH)
        for col in OUTCOME_LOG_COLUMNS:
            if col not in df.columns:
                df[col] = None
        return df[OUTCOME_LOG_COLUMNS]
    return pd.DataFrame(columns=OUTCOME_LOG_COLUMNS)


def track(estimates_path: Path = ESTIMATES_PATH) -> dict:
    estimates = pd.read_csv(estimates_path, low_memory=False)
    shadow = build_shadow_estimates(estimates)
    run_pulled_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    updated = clv_logger.process_run_pickem(
        shadow, _load_shadow_clv(), run_pulled_at, unflagged_sides=frozenset()
    )
    SHADOW_CLV_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    updated.to_csv(SHADOW_CLV_LOG_PATH, index=False)
    return {
        "shadow_rows_in": len(shadow),
        "shadow_flags_total": len(updated),
        "shadow_flags_open": int((updated["status"] == "open").sum()),
    }


def grade(dry_run: bool = False) -> dict:
    return grader.run(
        dry_run=dry_run,
        clv_df=_load_shadow_clv(),
        outcome_df=_load_shadow_outcomes(),
        outcome_path=SHADOW_OUTCOME_LOG_PATH,
        adapters=[grader.MLB_ADAPTER],
    )


def summarize(outcomes: pd.DataFrame, shadow_clv: pd.DataFrame) -> dict:
    """Pure function over the two shadow frames (unit-tested)."""
    graded = outcomes.loc[outcomes["result"].isin(["win", "loss"])].copy()
    graded = graded.merge(
        shadow_clv[["flag_id", "game_id"]].drop_duplicates("flag_id"), on="flag_id", how="left"
    )
    n = len(graded)
    out = {"legs": n, "games": 0, "win_rate": float("nan"), "ci_lo": float("nan"),
           "ci_hi": float("nan"), "stated": float("nan"), "verdict": "insufficient_data"}
    if n == 0:
        return out
    y = (graded["result"] == "win").to_numpy(dtype=float)
    cluster = graded["game_id"].astype(str).where(
        graded["game_id"].notna(), "na_" + graded.index.astype(str)
    )
    lo, hi, games = audit.clustered_ci(y, cluster.to_numpy())
    out.update(
        games=games, win_rate=float(y.mean()), ci_lo=lo, ci_hi=hi,
        stated=float(pd.to_numeric(graded["first_flagged_model_prob"], errors="coerce").mean()),
    )
    if n < MIN_LEGS_FOR_RECHECK or games < MIN_GAMES_FOR_RECHECK:
        out["verdict"] = "insufficient_data"
    elif lo > HURDLE_5:
        out["verdict"] = "recovered"
    elif hi < HURDLE_6:
        out["verdict"] = "still_below"
    else:
        out["verdict"] = "inconclusive"
    return out


def report() -> dict:
    s = summarize(_load_shadow_outcomes(), _load_shadow_clv())
    print("Shadow record: PrizePicks MLB Standard overs the model no longer flags (Session 2.65)")
    print(f"  Graded legs {s['legs']}, games {s['games']} "
          f"(re-check needs {MIN_LEGS_FOR_RECHECK}+ legs and {MIN_GAMES_FOR_RECHECK}+ games)")
    if s["legs"]:
        print(f"  Win rate {s['win_rate']*100:.1f}%  95% interval "
              f"[{s['ci_lo']*100:.1f}, {s['ci_hi']*100:.1f}]  stated by the model {s['stated']*100:.1f}%")
    print(f"  Breakevens: 5-pick {HURDLE_5*100:.1f}%, 6-pick {HURDLE_6*100:.1f}%.  "
          f"Before the rule: 50.1% on 2,969 legs.")
    print(f"  Verdict: {s['verdict']}")
    return s


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--track", action="store_true")
    parser.add_argument("--grade", action="store_true")
    parser.add_argument("--run", action="store_true", help="--track then --grade")
    parser.add_argument("--report", action="store_true")
    args = parser.parse_args()
    if not (args.track or args.grade or args.run or args.report):
        parser.error("Specify --track, --grade, --run or --report.")
    if args.track or args.run:
        print(track())
    if args.grade or args.run:
        print(grade())
    if args.report:
        report()
