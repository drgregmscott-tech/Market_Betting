"""
Session 2.4 -- CLV-Equivalent Calibration Logging

WHAT THIS SCRIPT IS
--------------------
Reads Session 2.3's estimation output (output/estimation/pickem_estimates_*.csv
-- one file per run of pickem_model.py) and, for every prop where the model's
estimate disagrees enough with the platform's own implied probability to
count as "flagged" (see FLAG_EDGE_THRESHOLD below), writes or updates one row
in a durable log (data/pickem/clv_log.csv) tracking that flag against two
pre-outcome benchmarks. This is the project's core design principle from
Session 0.1: a model is not "validated" until it is logging a real
price-vs-benchmark comparison on every flagged opportunity, before any bet
resolves (see ROADMAP.md, "Rule for every session").

This script is meant to be run AFTER each pickem_model.py run, against that
run's freshly written estimates file. It is not yet wired into any scheduled
automation -- that is Session 2.7's job. For now it is invoked manually,
matching the current state of the rest of Track 1's pipeline.

WHY THIS DOESN'T LOOK LIKE TRADITIONAL SPORTSBOOK CLV
-------------------------------------------------------
Classic Closing Line Value compares the price a bettor got at bet time
against that SAME market's price right before it closes -- a market moving
toward your side after you bet it is evidence you were early and right.
Session 0.1 confirmed PrizePicks and Underdog are structurally different:
"static, non-repricing lines" (ROADMAP.md Track Reference table) -- a
platform sets a line once and does not continuously reprice it against
betting volume the way a sportsbook does. That means the pure "did this
platform's own price move toward my side" signal cannot be assumed to behave
like real sportsbook CLV, and this script does not treat it as if it does.

Two distinct, explicitly labeled benchmarks are logged instead, per the
Session 2.4 roadmap card's own suggestion ("consensus across both platforms,
or a sharp-book proxy where available"):

1. CROSS-PLATFORM CONSENSUS (primary benchmark) -- at the moment a prop is
   flagged, this script checks whether the SAME real-world prop (same
   player, same resolved stat -- see pickem_model.py's Session 2.4 addition
   of `resolved_stat_key` -- and same game) is also priced on the OTHER
   platform at that same moment. If it is, that platform's own implied
   probability is logged as a second, independent read on the same
   real-world question. Two platforms independently setting their own lines
   is the closest available proxy this project has to a second opinion, in
   the absence of any real sharp-book feed for pick'em platforms.
2. OWN-LINE MOVEMENT TO CLOSE (secondary benchmark) -- because Session 2.2's
   ingestion pipeline is designed to run hourly, this script also re-checks,
   on every later run, whether a previously-flagged prop is still present
   under its original platform + source_line_id. Once it stops appearing in
   a fresh run (the platform took it off the board -- game locked, or the
   line was pulled), the last line/implied-probability values seen before it
   disappeared are frozen as this prop's "closing" values -- the direct
   pick'em analog of a real closing line, even though Session 0.1's own
   research says this platform type reprices rarely, not never.

Both benchmarks are logged side by side, explicitly labeled, so a future
session (2.5 onward, once real graded outcomes exist) can judge which one --
if either -- actually correlates with the model being right. Neither is
presented here as a proven proxy, only as a real, named, pre-outcome signal.

WHAT COUNTS AS "FLAGGED" -- A STATED, UNVALIDATED THRESHOLD
-----------------------------------------------------------
FLAG_EDGE_THRESHOLD is set at 0.03 -- the model's probability must be at
least 3 percentage points away from the platform's own implied probability,
on whichever side (over/under) has the edge, before this script logs it as a
flagged opportunity. This number is NOT derived from any real graded data --
no such data exists yet; producing it is what this whole calibration loop is
for. It is a placeholder, chosen loosely enough to generate a meaningful
number of real flags to validate this session's own logging mechanics
against, without flagging nearly every row the model can estimate at all
(which a threshold of 0 would do, and would not test anything). Revisiting
this threshold against real graded results belongs to Session 8.3 (Ongoing
Recalibration Cadence), not this session.

MATCHING KEYS -- HOW A "FLAG" IS TRACKED ACROSS MULTIPLE RUNS
-----------------------------------------------------------------
- flag_id = platform + "|" + source_line_id. This is the platform's own,
  stable ID for a specific line -- used to recognize "is this the same
  prop I already logged" across runs of THIS script.
- consensus_match_key = normalized player name + "|" + resolved_stat_key +
  "|" + game_id. Used ONLY at flag time, to look for the same real-world
  prop on the OTHER platform within the same estimates file. Deliberately
  not used as the durable flag_id, since a platform's own source_line_id
  is the more stable identity for tracking one specific line over its own
  lifetime.

WHAT THIS SCRIPT DOES NOT DO YET (stated gap, not a silent one)
-----------------------------------------------------------------
- Does not yet know the real outcome of any prop -- that is realized-outcome
  tracking, explicitly Session 2.5's job, using a separate log
  (outcome_log.csv) the user reports into manually. This script's job ends
  at logging pre-outcome signal.
- Consensus matching requires an exact resolved_stat_key match. A prop whose
  stat only resolved on one platform (e.g. a stat_type string not yet in
  pickem_model.py's maps on one platform but present on the other) will not
  find a consensus partner even if the same real prop exists on both
  platforms under a differently-worded, unmapped stat_type. This is a real,
  named limitation of relying on resolved_stat_key rather than fuzzy text
  matching, accepted here because a wrong consensus match (silently
  comparing two different real stats) would be worse than a missed one.
- Game-lock detection is inferred (a source_line_id simply stops appearing
  in the latest run), not confirmed against the platform's own `status`
  field, since Session 2.1/2.2's research did not enumerate every real
  status value either platform can return. A prop that disappears for a
  reason OTHER than game lock (e.g. the platform pulled it for an unrelated
  reason) would be treated the same way -- stated here as a real, not
  silent, limitation.

USAGE
-----
pip install pandas numpy --break-system-packages
python clv_logger.py --estimates path/to/pickem_estimates_TIMESTAMP.csv
If --estimates is omitted, the most recently written file in
output/estimation/ is used automatically.
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
# Paths
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parents[2]
ESTIMATION_DIR = BASE_DIR / "output" / "estimation"
CLV_LOG_PATH = BASE_DIR / "data" / "pickem" / "clv_log.csv"
CLV_SNAPSHOT_DIR = BASE_DIR / "data" / "pickem" / "clv_snapshots"
LOG_PATH = BASE_DIR / "logs" / "clv_logging.log"

# ---------------------------------------------------------------------------
# Constants -- named explicitly, per this project's "no unnamed black-box
# factors" documentation standard. See module docstring for full reasoning.
# ---------------------------------------------------------------------------
FLAG_EDGE_THRESHOLD = 0.03  # stated, unvalidated placeholder -- see docstring

CLV_LOG_COLUMNS = [
    "flag_id",
    "platform",
    "source_line_id",
    "player_name",
    "team",
    "sport",
    "stat_type",
    "resolved_stat_key",
    "game_id",
    "game_start_time",
    "flagged_side",
    "first_flagged_at",
    "first_flagged_line",
    "first_flagged_model_prob",
    "first_flagged_implied_prob",
    "first_flagged_edge",
    "consensus_available",
    "consensus_platform",
    "consensus_source_line_id",
    "consensus_line",
    "consensus_implied_prob_same_side",
    "consensus_edge",
    "last_seen_at",
    "last_seen_line",
    "last_seen_implied_prob",
    "status",
    "closing_line",
    "closing_implied_prob",
    "closing_pulled_at",
    "line_moved",
    "clv_edge_at_close",
]


def setup_logging() -> logging.Logger:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("clv_logger")
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
def find_latest_estimates_file() -> Path:
    files = sorted(ESTIMATION_DIR.glob("pickem_estimates_*.csv"))
    if not files:
        raise FileNotFoundError(
            f"No pickem_estimates_*.csv files found in {ESTIMATION_DIR}. "
            f"Run scripts/estimation/pickem_model.py first (Session 2.3)."
        )
    return files[-1]


def load_clv_log() -> pd.DataFrame:
    if CLV_LOG_PATH.exists():
        df = pd.read_csv(CLV_LOG_PATH)
        # Ensure every expected column exists even if an older log version
        # is being read (durable/queryable format should tolerate additive
        # schema growth, not break on it).
        for col in CLV_LOG_COLUMNS:
            if col not in df.columns:
                df[col] = None
        return df[CLV_LOG_COLUMNS]
    return pd.DataFrame(columns=CLV_LOG_COLUMNS)


def determine_flagged_side(row: pd.Series) -> Optional[str]:
    """Returns 'over', 'under', or None. A row can only be flagged on the
    side where the model's edge (model probability minus implied
    probability) meets FLAG_EDGE_THRESHOLD. Since implied_prob_over +
    implied_prob_under == 1 by construction (see pickem_model.py), a
    genuine edge on one side is the mirror-negative edge on the other, so
    at most one side is ever flagged per row -- this function never returns
    both."""
    if row.get("model_status") != "estimated":
        return None
    edge_over = row.get("edge_over")
    edge_under = row.get("edge_under")
    if pd.notna(edge_over) and edge_over >= FLAG_EDGE_THRESHOLD:
        return "over"
    if pd.notna(edge_under) and edge_under >= FLAG_EDGE_THRESHOLD:
        return "under"
    return None


def consensus_match_key(row: pd.Series) -> Optional[str]:
    """Builds the lookup key used to find the SAME real-world prop on the
    other platform within the same estimates file. Returns None if any
    required piece is missing (in which case no consensus lookup is
    attempted for this row -- consensus_available will be recorded False,
    not guessed)."""
    name = row.get("player_name")
    stat_key = row.get("resolved_stat_key")
    game_id = row.get("game_id")
    if not name or not isinstance(name, str):
        return None
    if not stat_key or not isinstance(stat_key, str):
        return None
    if not game_id or (isinstance(game_id, float) and pd.isna(game_id)):
        return None
    norm_name = " ".join(name.strip().lower().split())
    return f"{norm_name}|{stat_key}|{game_id}"


def implied_prob_same_side(row: pd.Series, side: str) -> Optional[float]:
    if side == "over":
        return row.get("implied_prob_over")
    return row.get("implied_prob_under")


def line_value_same_side_source(row: pd.Series) -> Optional[float]:
    return row.get("line")


def build_consensus_index(estimates_df: pd.DataFrame) -> dict[tuple[str, str], list[int]]:
    """Maps (platform, consensus_match_key) -> list of row indices, so a
    flagged row on one platform can look up whether the SAME real-world
    prop exists on the platform's counterpart within this same file."""
    index: dict[tuple[str, str], list[int]] = {}
    for idx, row in estimates_df.iterrows():
        key = consensus_match_key(row)
        if key is None:
            continue
        platform = row.get("platform")
        if not platform:
            continue
        index.setdefault((platform, key), []).append(idx)
    return index


def find_consensus_row(
    estimates_df: pd.DataFrame,
    index: dict[tuple[str, str], list[int]],
    own_platform: str,
    match_key: str,
) -> Optional[pd.Series]:
    other_platform = "underdog" if own_platform == "prizepicks" else "prizepicks"
    candidates = index.get((other_platform, match_key))
    if not candidates:
        return None
    # If more than one candidate matches (shouldn't normally happen -- a
    # given player/stat/game should have one active line per platform --
    # but real undocumented-endpoint data can surprise), take the first and
    # log a warning rather than silently averaging or guessing.
    if len(candidates) > 1:
        log.warning(
            "Multiple consensus candidates found for platform=%s key=%s "
            "(%d matches) -- using the first.",
            other_platform, match_key, len(candidates),
        )
    return estimates_df.loc[candidates[0]]


# ---------------------------------------------------------------------------
# Core logic
# ---------------------------------------------------------------------------
def process_run(estimates_df: pd.DataFrame, existing_log: pd.DataFrame, run_pulled_at: str) -> pd.DataFrame:
    """Given one run's estimates and the current CLV log, returns the
    updated CLV log: new flags appended, still-open flags refreshed, and
    flags that dropped out of this run's data transitioned to closed with
    their closing values frozen."""
    log_df = existing_log.copy()
    log_df = log_df.set_index("flag_id", drop=False) if not log_df.empty else log_df

    consensus_index = build_consensus_index(estimates_df)

    # Build a lookup of every (platform, source_line_id) present in THIS run,
    # used both to detect newly flagged rows and to refresh/close existing ones.
    estimates_df = estimates_df.copy()
    estimates_df["_flag_id"] = estimates_df["platform"].astype(str) + "|" + estimates_df["source_line_id"].astype(str)
    present_flag_ids = set(estimates_df["_flag_id"])

    new_rows = []
    existing_flag_ids = set(log_df["flag_id"]) if not log_df.empty else set()

    for _, row in estimates_df.iterrows():
        side = determine_flagged_side(row)
        flag_id = row["_flag_id"]

        if flag_id in existing_flag_ids:
            # Already logged from a prior run -- refresh last_seen fields
            # only (first_flagged_* values never change once set).
            log_df.loc[flag_id, "last_seen_at"] = run_pulled_at
            log_df.loc[flag_id, "last_seen_line"] = row.get("line")
            side_for_update = log_df.loc[flag_id, "flagged_side"]
            log_df.loc[flag_id, "last_seen_implied_prob"] = implied_prob_same_side(row, side_for_update)
            log_df.loc[flag_id, "status"] = "open"
            continue

        if side is None:
            continue  # not flagged this run, and not previously logged -- nothing to do

        # New flag.
        match_key = consensus_match_key(row)
        consensus_row = None
        if match_key is not None:
            consensus_row = find_consensus_row(estimates_df, consensus_index, row.get("platform"), match_key)

        consensus_available = consensus_row is not None
        consensus_platform = consensus_row.get("platform") if consensus_available else None
        consensus_source_line_id = consensus_row.get("source_line_id") if consensus_available else None
        consensus_line = consensus_row.get("line") if consensus_available else None
        consensus_implied = implied_prob_same_side(consensus_row, side) if consensus_available else None
        model_prob = row.get("prob_over") if side == "over" else row.get("prob_under")
        consensus_edge = (
            (model_prob - consensus_implied)
            if (consensus_available and model_prob is not None and consensus_implied is not None)
            else None
        )

        own_implied = implied_prob_same_side(row, side)
        own_edge = row.get("edge_over") if side == "over" else row.get("edge_under")

        new_rows.append({
            "flag_id": flag_id,
            "platform": row.get("platform"),
            "source_line_id": row.get("source_line_id"),
            "player_name": row.get("player_name"),
            "team": row.get("team"),
            "sport": row.get("sport"),
            "stat_type": row.get("stat_type"),
            "resolved_stat_key": row.get("resolved_stat_key"),
            "game_id": row.get("game_id"),
            "game_start_time": row.get("game_start_time"),
            "flagged_side": side,
            "first_flagged_at": run_pulled_at,
            "first_flagged_line": row.get("line"),
            "first_flagged_model_prob": model_prob,
            "first_flagged_implied_prob": own_implied,
            "first_flagged_edge": own_edge,
            "consensus_available": consensus_available,
            "consensus_platform": consensus_platform,
            "consensus_source_line_id": consensus_source_line_id,
            "consensus_line": consensus_line,
            "consensus_implied_prob_same_side": consensus_implied,
            "consensus_edge": consensus_edge,
            "last_seen_at": run_pulled_at,
            "last_seen_line": row.get("line"),
            "last_seen_implied_prob": own_implied,
            "status": "open",
            "closing_line": None,
            "closing_implied_prob": None,
            "closing_pulled_at": None,
            "line_moved": None,
            "clv_edge_at_close": None,
        })

    if new_rows:
        new_df = pd.DataFrame(new_rows).set_index("flag_id", drop=False)
        log_df = pd.concat([log_df, new_df]) if not log_df.empty else new_df

    # Close out any previously-open flag that no longer appears in this run.
    if not log_df.empty:
        open_mask = log_df["status"] == "open"
        dropped_mask = open_mask & (~log_df["flag_id"].isin(present_flag_ids))
        for flag_id in log_df.loc[dropped_mask, "flag_id"]:
            closing_line = log_df.loc[flag_id, "last_seen_line"]
            closing_implied = log_df.loc[flag_id, "last_seen_implied_prob"]
            first_line = log_df.loc[flag_id, "first_flagged_line"]
            first_model_prob = log_df.loc[flag_id, "first_flagged_model_prob"]
            log_df.loc[flag_id, "status"] = "closed"
            log_df.loc[flag_id, "closing_line"] = closing_line
            log_df.loc[flag_id, "closing_implied_prob"] = closing_implied
            log_df.loc[flag_id, "closing_pulled_at"] = log_df.loc[flag_id, "last_seen_at"]
            log_df.loc[flag_id, "line_moved"] = (
                bool(pd.notna(closing_line) and pd.notna(first_line) and closing_line != first_line)
            )
            log_df.loc[flag_id, "clv_edge_at_close"] = (
                (first_model_prob - closing_implied)
                if (pd.notna(first_model_prob) and pd.notna(closing_implied))
                else None
            )

    return log_df.reset_index(drop=True)[CLV_LOG_COLUMNS]


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
def run(estimates_path: Optional[Path]) -> dict:
    log.info("=== CLV logging run starting ===")

    path = estimates_path or find_latest_estimates_file()
    estimates_df = pd.read_csv(path)
    log.info("Loaded %d estimate rows from %s", len(estimates_df), path)

    run_pulled_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    existing_log = load_clv_log()
    log.info("Existing CLV log has %d rows before this run", len(existing_log))

    updated_log = process_run(estimates_df, existing_log, run_pulled_at)

    newly_opened = int((updated_log["first_flagged_at"] == run_pulled_at).sum())
    newly_closed = int(
        ((updated_log["status"] == "closed") & (updated_log["closing_pulled_at"] == run_pulled_at)).sum()
    )
    still_open = int((updated_log["status"] == "open").sum())

    CLV_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    updated_log.to_csv(CLV_LOG_PATH, index=False)
    log.info("Wrote %d total rows to %s", len(updated_log), CLV_LOG_PATH)

    CLV_SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)
    snapshot_path = CLV_SNAPSHOT_DIR / f"clv_log_{run_pulled_at.replace(':', '').replace('-', '')}.csv"
    updated_log.to_csv(snapshot_path, index=False)

    summary = {
        "estimates_file": str(path),
        "rows_in_estimates": len(estimates_df),
        "newly_flagged": newly_opened,
        "newly_closed": newly_closed,
        "still_open": still_open,
        "total_logged": len(updated_log),
        "log_path": str(CLV_LOG_PATH),
    }
    log.info("Run summary: %s", summary)
    return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--estimates",
        type=str,
        default=None,
        help="Path to a specific pickem_estimates_*.csv file. Defaults to "
             "the most recently written file in output/estimation/.",
    )
    args = parser.parse_args()
    estimates_arg = Path(args.estimates) if args.estimates else None
    result = run(estimates_arg)
    print(result)
