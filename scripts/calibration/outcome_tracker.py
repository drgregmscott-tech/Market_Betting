"""
Session 2.5 -- Realized-Outcome Tracking

WHAT THIS SCRIPT IS
--------------------
Session 2.4's clv_logger.py logs a PRE-outcome proxy signal (cross-platform
consensus, own-line movement to close) for every flagged opportunity, before
anyone knows whether the pick actually wins. This script records the REAL
thing that proxy stands in for: what the user actually bet, and what
actually happened. Two logs, kept deliberately separate (per Session 2.4's
own Decision #3 -- proxy signal and real outcome should never be blended
into one number), joined only by a shared key: flag_id.

This project's own north star (ROADMAP.md, "the S&P 500 analogy") has no
real trendline to plot without this file existing. CLV is a fast, pre-outcome
substitute for waiting on real results -- this is the real results.

WHO USES THIS AND HOW
----------------------
The user places a bet manually (this project flags and sizes opportunities;
it does not place bets -- see ROADMAP.md, Background & Approach). Once that
bet resolves (the real game/stat is final), the user reports the result
back into this script by flag_id, which is looked up directly from
data/pickem/clv_log.csv -- the same flag_id Session 2.4 already assigned to
that flagged opportunity (platform + source_line_id). This script does not
invent a new identifier; it reuses the one that already exists so the two
logs join cleanly.

USAGE
-----
Record one graded leg:
    python outcome_tracker.py --record --flag-id "prizepicks|12345678" \
        --result win --actual-value 287.5 --entry-type "2-pick Power Play" \
        --stake 10 --payout 30 --notes "optional free-text note"

Record without a payout (e.g. an entry that hasn't fully resolved yet, or a
leg the user is grading independent of a specific real-money entry):
    python outcome_tracker.py --record --flag-id "underdog|98765" \
        --result loss --actual-value 4

List all flag_ids currently open for grading (present in the CLV log,
not yet reported in the outcome log) so the user knows what CAN be graded:
    python outcome_tracker.py --pending

Print a joined summary report (real win rate vs. Section 2's breakeven,
plus a CLV-vs-outcome agreement check):
    python outcome_tracker.py --report

WHY EVERY RECORD IS SELF-CONTAINED, NOT JUST A THIN LINK ROW
--------------------------------------------------------------
Each row in outcome_log.csv carries its own copy of the real context
(player, stat, flagged side, line, model probability, CLV-close edge) pulled
directly from the matching clv_log.csv row at record time, in addition to
flag_id. This is deliberate, not redundant: outcome_log.csv should remain
readable and queryable on its own, even if clv_log.csv is ever pruned,
rotated, or unavailable -- matching Session 2.2/2.4's own "durable/queryable
log" standard. flag_id remains the real join key for anyone who wants to
re-verify against the live CLV log directly.

WHAT THIS SCRIPT DOES NOT DO YET (stated gap, not a silent one)
-----------------------------------------------------------------
- Does not automatically grade a leg from public final stat results. Every
  outcome is manually reported by the user, by design (see ROADMAP.md
  Session 2.5 card, "Handoff notes" -- this system does not place bets, and
  by the same logic it does not assume it knows a real-money result without
  being told). Automating grading from public box scores is a real, named
  candidate for a future session (see sample_size_methodology.md, Section 6,
  option (c)) -- not built here.
- Does not enforce that a flag_id reported here actually exists in
  clv_log.csv as a hard failure -- it WARNS loudly and still records the
  outcome with blank context fields, rather than silently discarding a real
  user-reported result over a lookup miss (e.g. if clv_log.csv has since
  rotated past that flag). This mirrors clv_logger.py's own preference for
  a visible, logged gap over a silent drop.
- Does not compute the Session 2.5 sample-size threshold itself (that lives
  in sample_size_methodology.md as a fixed, documented number, not
  recomputed by this script) -- --report compares the real graded sample
  against that documented number, it does not re-derive it.

USAGE (setup)
-------------
pip install pandas --break-system-packages
"""

from __future__ import annotations

import argparse
import logging
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import pandas as pd

# ---------------------------------------------------------------------------
# Paths -- matching Session 2.2/2.4's existing repo-relative pattern exactly.
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parents[2]
CLV_LOG_PATH = BASE_DIR / "data" / "pickem" / "clv_log.csv"
OUTCOME_LOG_PATH = BASE_DIR / "data" / "pickem" / "outcome_log.csv"
LOG_PATH = BASE_DIR / "logs" / "outcome_tracking.log"

# Real breakeven per-leg win rate for a standard PrizePicks 2-pick Power Play
# (3x payout, both legs must hit: p^2 * 3 = 1 -> p = sqrt(1/3)). Sourced in
# sample_size_methodology.md Section 2. Used only for --report's summary
# comparison -- not enforced anywhere else in this script.
BREAKEVEN_WIN_RATE = 0.5774
SAMPLE_SIZE_THRESHOLD = 3725  # sample_size_methodology.md Section 3

OUTCOME_LOG_COLUMNS = [
    "outcome_id",
    "flag_id",
    "reported_at",
    "platform",
    "player_name",
    "team",
    "sport",
    "stat_type",
    "resolved_stat_key",
    "flagged_side",
    "first_flagged_line",
    "first_flagged_model_prob",
    "first_flagged_implied_prob",
    "first_flagged_edge",
    "clv_edge_at_close",
    "consensus_available",
    "result",
    "actual_value",
    "entry_type",
    "stake",
    "payout",
    "net_profit",
    "notes",
    "context_lookup_status",
]

VALID_RESULTS = {"win", "loss", "push", "void"}


def setup_logging() -> logging.Logger:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("outcome_tracker")
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
# Helpers
# ---------------------------------------------------------------------------
def load_clv_log() -> pd.DataFrame:
    if not CLV_LOG_PATH.exists():
        raise FileNotFoundError(
            f"{CLV_LOG_PATH} not found. Run clv_logger.py first (Session 2.4) "
            f"so there are flagged opportunities to grade."
        )
    return pd.read_csv(CLV_LOG_PATH)


def load_outcome_log() -> pd.DataFrame:
    if OUTCOME_LOG_PATH.exists():
        df = pd.read_csv(OUTCOME_LOG_PATH)
        for col in OUTCOME_LOG_COLUMNS:
            if col not in df.columns:
                df[col] = None
        return df[OUTCOME_LOG_COLUMNS]
    return pd.DataFrame(columns=OUTCOME_LOG_COLUMNS)


def lookup_flag_context(flag_id: str) -> tuple[Optional[pd.Series], str]:
    """Looks up flag_id in the live CLV log. Returns (row_or_None, status)
    where status is 'ok', 'not_found', or 'multiple_matches' -- a record is
    still created either way (see module docstring); this only determines
    whether context fields get populated or left blank with a logged
    warning."""
    clv_df = load_clv_log()
    matches = clv_df.loc[clv_df["flag_id"] == flag_id]
    if len(matches) == 0:
        log.warning(
            "flag_id '%s' not found in %s. Recording outcome with blank "
            "context fields -- verify this flag_id is correct.",
            flag_id, CLV_LOG_PATH,
        )
        return None, "not_found"
    if len(matches) > 1:
        log.warning(
            "flag_id '%s' matched %d rows in %s (should be unique). "
            "Using the first match.",
            flag_id, len(matches), CLV_LOG_PATH,
        )
        return matches.iloc[0], "multiple_matches"
    return matches.iloc[0], "ok"


def compute_net_profit(stake: Optional[float], payout: Optional[float], result: str) -> Optional[float]:
    if stake is None:
        return None
    if result in ("push", "void"):
        return 0.0
    if payout is None:
        return None
    return round(payout - stake, 2)


# ---------------------------------------------------------------------------
# Core actions
# ---------------------------------------------------------------------------
def record_outcome(
    flag_id: str,
    result: str,
    actual_value: Optional[float],
    entry_type: Optional[str],
    stake: Optional[float],
    payout: Optional[float],
    notes: Optional[str],
) -> dict:
    if result not in VALID_RESULTS:
        raise ValueError(f"--result must be one of {sorted(VALID_RESULTS)}, got '{result}'")

    context_row, status = lookup_flag_context(flag_id)
    reported_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    outcome_log = load_outcome_log()

    if flag_id in set(outcome_log["flag_id"]):
        log.warning(
            "flag_id '%s' already has a recorded outcome. Adding a new row "
            "rather than overwriting -- if this was a correction, remove "
            "the earlier row manually and note why (per this project's "
            "'corrections are documented, not silently absorbed' "
            "convention).",
            flag_id,
        )

    new_row = {
        "outcome_id": f"{flag_id}|{reported_at}",
        "flag_id": flag_id,
        "reported_at": reported_at,
        "platform": context_row.get("platform") if context_row is not None else None,
        "player_name": context_row.get("player_name") if context_row is not None else None,
        "team": context_row.get("team") if context_row is not None else None,
        "sport": context_row.get("sport") if context_row is not None else None,
        "stat_type": context_row.get("stat_type") if context_row is not None else None,
        "resolved_stat_key": context_row.get("resolved_stat_key") if context_row is not None else None,
        "flagged_side": context_row.get("flagged_side") if context_row is not None else None,
        "first_flagged_line": context_row.get("first_flagged_line") if context_row is not None else None,
        "first_flagged_model_prob": context_row.get("first_flagged_model_prob") if context_row is not None else None,
        "first_flagged_implied_prob": context_row.get("first_flagged_implied_prob") if context_row is not None else None,
        "first_flagged_edge": context_row.get("first_flagged_edge") if context_row is not None else None,
        "clv_edge_at_close": context_row.get("clv_edge_at_close") if context_row is not None else None,
        "consensus_available": context_row.get("consensus_available") if context_row is not None else None,
        "result": result,
        "actual_value": actual_value,
        "entry_type": entry_type,
        "stake": stake,
        "payout": payout,
        "net_profit": compute_net_profit(stake, payout, result),
        "notes": notes,
        "context_lookup_status": status,
    }

    outcome_log = pd.concat([outcome_log, pd.DataFrame([new_row])], ignore_index=True)
    OUTCOME_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    outcome_log.to_csv(OUTCOME_LOG_PATH, index=False)

    log.info(
        "Recorded outcome for flag_id='%s': result=%s, context_lookup=%s. "
        "Outcome log now has %d total rows.",
        flag_id, result, status, len(outcome_log),
    )
    return new_row


def list_pending() -> pd.DataFrame:
    """Flags present in the CLV log (any status) that have no recorded
    outcome yet -- i.e. real candidates the user could grade if they placed
    (or want to paper-track) that pick."""
    clv_df = load_clv_log()
    outcome_df = load_outcome_log()
    graded_ids = set(outcome_df["flag_id"])
    pending = clv_df.loc[~clv_df["flag_id"].isin(graded_ids)]
    cols = [
        "flag_id", "platform", "player_name", "stat_type", "flagged_side",
        "first_flagged_line", "first_flagged_model_prob", "status",
        "clv_edge_at_close",
    ]
    return pending[[c for c in cols if c in pending.columns]]


def build_report() -> dict:
    """Joins outcome_log.csv against clv_log.csv on flag_id and prints a
    summary: real graded win rate vs. the documented breakeven rate
    (sample_size_methodology.md Section 2), progress against the documented
    sample-size threshold (Section 3), and a directional CLV-agreement
    check (did closed flags with a positive clv_edge_at_close win more
    often than ones with a negative or zero clv_edge_at_close?)."""
    outcome_df = load_outcome_log()
    graded = outcome_df.loc[outcome_df["result"].isin(["win", "loss"])].copy()

    n_graded = len(graded)
    n_wins = int((graded["result"] == "win").sum())
    real_win_rate = (n_wins / n_graded) if n_graded > 0 else None

    clv_agreement = None
    if n_graded > 0 and graded["clv_edge_at_close"].notna().any():
        positive_clv = graded.loc[graded["clv_edge_at_close"] > 0]
        nonpositive_clv = graded.loc[graded["clv_edge_at_close"] <= 0]
        pos_win_rate = (
            (positive_clv["result"] == "win").mean() if len(positive_clv) > 0 else None
        )
        nonpos_win_rate = (
            (nonpositive_clv["result"] == "win").mean() if len(nonpositive_clv) > 0 else None
        )
        clv_agreement = {
            "n_positive_clv_edge": len(positive_clv),
            "win_rate_when_clv_edge_positive": pos_win_rate,
            "n_nonpositive_clv_edge": len(nonpositive_clv),
            "win_rate_when_clv_edge_nonpositive": nonpos_win_rate,
        }

    report = {
        "n_graded_legs": n_graded,
        "n_wins": n_wins,
        "real_win_rate": real_win_rate,
        "breakeven_win_rate": BREAKEVEN_WIN_RATE,
        "sample_size_threshold": SAMPLE_SIZE_THRESHOLD,
        "pct_of_threshold_reached": round(100 * n_graded / SAMPLE_SIZE_THRESHOLD, 2),
        "clv_agreement_check": clv_agreement,
    }
    return report


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--record", action="store_true", help="Record a new graded outcome.")
    parser.add_argument("--pending", action="store_true", help="List flags with no recorded outcome yet.")
    parser.add_argument("--report", action="store_true", help="Print a joined CLV-vs-outcome summary report.")

    parser.add_argument("--flag-id", type=str, default=None)
    parser.add_argument("--result", type=str, default=None, choices=sorted(VALID_RESULTS))
    parser.add_argument("--actual-value", type=float, default=None)
    parser.add_argument("--entry-type", type=str, default=None)
    parser.add_argument("--stake", type=float, default=None)
    parser.add_argument("--payout", type=float, default=None)
    parser.add_argument("--notes", type=str, default=None)

    args = parser.parse_args()

    if args.record:
        if not args.flag_id or not args.result:
            parser.error("--record requires --flag-id and --result")
        result = record_outcome(
            flag_id=args.flag_id,
            result=args.result,
            actual_value=args.actual_value,
            entry_type=args.entry_type,
            stake=args.stake,
            payout=args.payout,
            notes=args.notes,
        )
        print(result)
    elif args.pending:
        pending_df = list_pending()
        print(f"{len(pending_df)} flag(s) with no recorded outcome yet:")
        print(pending_df.to_string(index=False))
    elif args.report:
        print(build_report())
    else:
        parser.error("Specify one of --record, --pending, or --report")
