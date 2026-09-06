"""
Session 3.6 -- Arbitrage Flag Tracking (Live Validation Window)

WHAT THIS SCRIPT IS
--------------------
Session 3.2's detector.py writes one arbitrage_flags_<timestamp>.csv per
pipeline run. The same real-world opportunity (e.g. the MI-07/MI-7 House
race) can appear in MANY consecutive runs simply because it hasn't closed
yet -- 4 real runs so far have produced 4 files, but only 1 genuinely
distinct opportunity. Counting "rows seen" would silently overstate the
real sample. This script builds the deduplicated view: how many DISTINCT
real opportunities have actually been observed, split out by which of the
detector's three distinct mechanisms produced each one -- so Session 3.6's
"minimum sample size" checklist item can be checked honestly.

THE THREE MECHANISMS (confirmed directly from detector.py / venue_matcher.py,
not assumed -- see docs/arbitrage_sample_size_methodology.md for the full
derivation):
  1. single_venue   -- detect_single_venue_mispricing(): one venue's own
                        YES + NO prices don't sum to $1. No cross-venue
                        matching involved.
  2. cross_venue / elections_wide -- _find_elections_matches(): down-ballot
                        Elections markets, matched Kalshi<->Polymarket via
                        Session 3.4's district-code fix.
  3. cross_venue / bucketed -- _find_bucketed_matches(): everything else
                        (currently Climate/Commodities), matched via a
                        coarser time-bucket comparison.

WHY A KNOWN-BAD RUN IS EXCLUDED, NOT SILENTLY COUNTED
----------------------------------------------------------
The very first real arbitrage_flags_*.csv ever produced
(arbitrage_flags_20260906T101214Z.csv) predates Session 3.4's district-code
fix and contains the exact false cross-state matches that session found and
fixed (e.g. Kalshi's WA-08 vs. Polymarket's IN-08) -- 9 of its 10 rows were
confirmed false positives. Counting those rows here would launder a known
bug into "real sample size." EXCLUDE_RUNS_BEFORE is set to the timestamp of
the first POST-fix run (2026-09-06T10:22:36Z) -- an objective cutoff derived
directly from the real data (the first run with zero cross-state
mismatches), not a guessed date.

WHAT "DISTINCT OPPORTUNITY" MEANS HERE
-------------------------------------------
Two flag rows are the SAME real opportunity if they reference the same pair
of real markets, regardless of which venue detector.py happened to label
"a" vs "b" on a given run (direction can flip run to run). Identity key:
frozenset({(platform_a, market_a), (platform_b, market_b)}) for cross-venue
rows, or (platform_a, market_a) alone for single-venue rows (no "b" leg).

USAGE
-----
pip install pandas --break-system-packages
python arbitrage_flag_tracker.py --scan       # rebuild the ledger from every
                                                 real arbitrage_flags_*.csv on
                                                 disk, print a summary
python arbitrage_flag_tracker.py --report      # print progress vs. the
                                                 interim floor and the real
                                                 30-per-mechanism target,
                                                 from the last --scan
"""

from __future__ import annotations

import argparse
import csv
import glob
import json
import logging
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

# ---------------------------------------------------------------------------
# Paths -- matching this project's existing repo-relative pattern
# (Session 2.2/2.4/2.5/3.3).
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parents[2]
ARBITRAGE_FLAGS_DIR = BASE_DIR / "data" / "arbitrage" / "flags"
LEDGER_PATH = BASE_DIR / "data" / "arbitrage" / "distinct_opportunities.csv"
LOG_PATH = BASE_DIR / "logs" / "arbitrage_flag_tracking.log"

# ---------------------------------------------------------------------------
# Constants -- named and sourced, per this project's "no unnamed black-box
# factors" standard. See docs/arbitrage_sample_size_methodology.md for the
# full derivation of every number below.
# ---------------------------------------------------------------------------
EXCLUDE_RUNS_BEFORE = datetime(2026, 9, 6, 10, 22, 0, tzinfo=timezone.utc)
# ^ Objectively derived: first post-Session-3.4-fix run. Runs at or after
# this timestamp are the ones confirmed clean of the WA-08/IN-08-style
# cross-state false-match bug.

MECHANISMS = ["single_venue", "cross_venue_elections_wide", "cross_venue_bucketed"]

# Rule-of-three sample size (n = 3/p) for 95% confidence the true residual
# false-positive rate of a given mechanism is below the stated threshold.
# 10% chosen as the real target: Session 3.4's own found defect rate on the
# elections_wide path was 90% pre-fix, so "confident it's now much better
# than that" is the honest bar, not an arbitrarily small one.
FULL_CONFIDENCE_TARGET_PER_MECHANISM = 30 # n = 3 / 0.10

# Interim floor for closing THIS session, agreed directly with the user
# (2026-09-06): at least one genuine, confirmed-clean flag per mechanism, or
# an explicit documented finding that a mechanism produced zero real
# candidates over a stated real observation window. This is NOT a
# statistically rigorous number -- seesession log for why the full target
# above is deliberately not required to close this session.
INTERIM_FLOOR_PER_MECHANISM = 1

LEDGER_FIELDS = [
"opportunity_key",
"mechanism",
"platform_a",
"market_a",
"title_a",
"platform_b",
"market_b",
"title_b",
"first_seen",
"last_seen",
"times_seen",
"still_appearing_in_latest_scan",
"category",
"match_path",
]


def setup_logging() -> logging.Logger:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("arbitrage_flag_tracker")
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
# Reading real pipeline run files
# ---------------------------------------------------------------------------
def _parse_run_timestamp(path: Path) -> Optional[datetime]:
    """Extracts the UTC timestamp embedded in a real run's filename, e.g.
    arbitrage_flags_20260906T101214Z.csv -> 2026-09-06T10:12:14Z. Returns
    None (and logs a warning) for a filename that doesn't match the
    expected pattern, rather than crashing or silently skipping."""
    stem = path.stem # arbitrage_flags_20260906T101214Z
    marker = "arbitrage_flags_"
    if not stem.startswith(marker):
        return None
    raw = stem[len(marker):]
    try:
        return datetime.strptime(raw, "%Y%m%dT%H%M%SZ").replace(tzinfo=timezone.utc)
    except ValueError:
        log.warning("Could not parse a run timestamp from filename: %s", path.name)
        return None


def _mechanism_for_row(row: dict) -> str:
    opp_type = (row.get("opportunity_type") or "").strip()
    match_path = (row.get("match_path") or "").strip()
    if opp_type == "single_venue":
        return "single_venue"
    if opp_type == "cross_venue" and match_path == "elections_wide":
        return "cross_venue_elections_wide"
    if opp_type == "cross_venue" and match_path == "bucketed":
        return "cross_venue_bucketed"
    return f"unrecognized:{opp_type}/{match_path}"


def _opportunity_key(row: dict) -> str:
    """Direction-agnostic, order-agnostic identity for a real-world
    opportunity. Two rows are the same opportunity if they name the same
    real market pair, regardless of which venue got labeled 'a' vs 'b' on
    a given run (Session 3.2's detector can flip direction run to run)."""
    plat_a, mkt_a = row.get("platform_a"), row.get("market_a")
    plat_b, mkt_b = row.get("platform_b"), row.get("market_b")
    if not plat_b or not mkt_b:
        # single_venue row -- no second leg
        return f"single|{plat_a}:{mkt_a}"
    pair = frozenset({(plat_a, mkt_a), (plat_b, mkt_b)})
    return "cross|" + "|".join(sorted(f"{p}:{m}" for p, m in pair))


def scan_all_runs() -> tuple[dict[str, dict], list[str]]:
    """Reads every real arbitrage_flags_*.csv on disk (excluding the
    always-overwritten 'latest' file, to avoid double-counting the most
    recent run), applies the EXCLUDE_RUNS_BEFORE cutoff, and builds a
    deduplicated ledger of distinct real opportunities. Returns
    (ledger_by_key, warnings)."""
    pattern = str(ARBITRAGE_FLAGS_DIR / "arbitrage_flags_*.csv")
    all_paths = sorted(Path(p) for p in glob.glob(pattern))
    run_paths = [p for p in all_paths if p.name != "arbitrage_flags_latest.csv"]

    warnings: list[str] = []
    ledger: dict[str, dict] = {}
    latest_run_timestamp: Optional[datetime] = None
    seen_in_latest: set[str] = set()

    for path in run_paths:
        run_ts = _parse_run_timestamp(path)
        if run_ts is None:
            warnings.append(f"Skipped unparseable file: {path.name}")
            continue
        if run_ts < EXCLUDE_RUNS_BEFORE:
            warnings.append(
                f"Excluded {path.name} (run at {run_ts.isoformat()}, before "
                f"EXCLUDE_RUNS_BEFORE={EXCLUDE_RUNS_BEFORE.isoformat()} -- "
                f"this is the known pre-Session-3.4-fix run containing "
                f"confirmed cross-state false matches)."
            )
            continue

        if latest_run_timestamp is None or run_ts > latest_run_timestamp:
            latest_run_timestamp = run_ts
            seen_in_latest = set()

        with path.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                key = _opportunity_key(row)
                mechanism = _mechanism_for_row(row)
                if mechanism.startswith("unrecognized:"):
                    warnings.append(
                        f"{path.name}: row with key={key} has an "
                        f"unrecognized mechanism ({mechanism}) -- check "
                        f"detector.py/venue_matcher.py for a new "
                        f"opportunity_type/match_path not accounted for "
                        f"in _mechanism_for_row()."
                    )

                if run_ts == latest_run_timestamp:
                    seen_in_latest.add(key)

                if key not in ledger:
                    ledger[key] = {
                        "opportunity_key": key,
                        "mechanism": mechanism,
                        "platform_a": row.get("platform_a"),
                        "market_a": row.get("market_a"),
                        "title_a": row.get("title_a"),
                        "platform_b": row.get("platform_b"),
                        "market_b": row.get("market_b"),
                        "title_b": row.get("title_b"),
                        "first_seen": run_ts.isoformat(),
                        "last_seen": run_ts.isoformat(),
                        "times_seen": 0,
                        "category": row.get("category"),
                        "match_path": row.get("match_path"),
                    }
                entry = ledger[key]
                entry["times_seen"] += 1
                if run_ts.isoformat() > entry["last_seen"]:
                    entry["last_seen"] = run_ts.isoformat()
                if run_ts.isoformat() < entry["first_seen"]:
                    entry["first_seen"] = run_ts.isoformat()

    for entry in ledger.values():
        entry["still_appearing_in_latest_scan"] = entry["opportunity_key"] in seen_in_latest

    return ledger, warnings


def write_ledger(ledger: dict[str, dict]) -> None:
    LEDGER_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LEDGER_PATH.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=LEDGER_FIELDS, extrasaction="ignore")
        writer.writeheader()
        for entry in sorted(ledger.values(), key=lambda e: e["first_seen"]):
            writer.writerow(entry)


def load_ledger() -> list[dict]:
    if not LEDGER_PATH.exists():
        raise FileNotFoundError(
            f"{LEDGER_PATH} not found. Run --scan first to build it."
        )
    with LEDGER_PATH.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------
def build_report(ledger_rows: list[dict]) -> dict:
    by_mechanism: dict[str, list[dict]] = {m: [] for m in MECHANISMS}
    unrecognized: list[dict] = []
    for row in ledger_rows:
        mech = row.get("mechanism", "")
        if mech in by_mechanism:
            by_mechanism[mech].append(row)
        else:
            unrecognized.append(row)

    mechanism_summary = {}
    interim_floor_met = True
    for mech in MECHANISMS:
        rows = by_mechanism[mech]
        n_distinct = len(rows)
        meets_interim = n_distinct >= INTERIM_FLOOR_PER_MECHANISM
        interim_floor_met = interim_floor_met and meets_interim
        mechanism_summary[mech] = {
            "distinct_opportunities_observed": n_distinct,
            "interim_floor": INTERIM_FLOOR_PER_MECHANISM,
            "interim_floor_met": meets_interim,
            "full_confidence_target": FULL_CONFIDENCE_TARGET_PER_MECHANISM,
            "pct_of_full_target": round(
                100 * n_distinct / FULL_CONFIDENCE_TARGET_PER_MECHANISM, 1
            ),
            "opportunities": [
                {
                    "opportunity_key": r["opportunity_key"],
                    "title_a": r.get("title_a"),
                    "title_b": r.get("title_b"),
                    "first_seen": r.get("first_seen"),
                    "last_seen": r.get("last_seen"),
                    "times_seen": r.get("times_seen"),
                    "still_appearing": r.get("still_appearing_in_latest_scan"),
                }
                for r in rows
            ],
        }

    return {
        "interim_floor_per_mechanism": INTERIM_FLOOR_PER_MECHANISM,
        "full_confidence_target_per_mechanism": FULL_CONFIDENCE_TARGET_PER_MECHANISM,
        "session_3_6_sample_size_checklist_met": interim_floor_met,
        "mechanisms": mechanism_summary,
        "unrecognized_mechanism_rows": len(unrecognized),
    }


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Session 3.6 -- deduplicated arbitrage flag tracking."
    )
    parser.add_argument("--scan", action="store_true", help="Rebuild the ledger from real run files on disk.")
    parser.add_argument("--report", action="store_true", help="Print a progress report from the last --scan.")
    args = parser.parse_args()

    if not args.scan and not args.report:
        parser.error("Specify --scan, --report, or both.")

    if args.scan:
        ledger, warnings = scan_all_runs()
        write_ledger(ledger)
        log.info(
            "Scan complete: %d distinct real opportunities found across "
            "all post-fix runs. %d warnings.",
            len(ledger), len(warnings),
        )
        for w in warnings:
            log.warning(w)
        print(f"Scanned. {len(ledger)} distinct real opportunities written to {LEDGER_PATH}")
        if warnings:
            print(f"{len(warnings)} warning(s) -- see {LOG_PATH} for detail.")

    if args.report:
        rows = load_ledger()
        report = build_report(rows)
        print(json.dumps(report, indent=2, default=str))
