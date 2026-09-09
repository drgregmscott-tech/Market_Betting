"""
Session 5.7 -- Politics Sample-Size Progress Report (Live Validation Window)

WHAT THIS SCRIPT IS
--------------------
Reads data/politics/clv_log.csv (Session 5.3's clv_logger.py --track politics
output) and reports real progress against the two thresholds derived in
docs/politics_sample_size_methodology.md:
  - Interim floor: 30 graded (resolved) flags
  - Full-confidence target: ~892 graded flags

A "graded" flag here means status == "closed" in clv_log.csv AND a real
resolution outcome is known. clv_logger.py currently marks a flag "closed"
when it disappears from the latest estimates pull (Session 2.4's existing
"disappeared == closed" convention, reused for this track) -- it does NOT
yet know whether that closure was a real race resolution (won/lost) or
something else (e.g. a market getting delisted, or a transient Kalshi/
Polymarket/ElectIndex outage misread as closure, the same false-signal risk
run_politics_pipeline.py's own docstring already names for a bad ingestion
run). This script reports the "closed" count honestly labeled as such --
NOT as "graded win/loss outcomes" -- until a real politics-specific outcome
tracker exists (see docs/politics_sample_size_methodology.md Section 7).

USAGE
-----
python politics_sample_report.py --report
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]
CLV_LOG_PATH = BASE_DIR / "data" / "politics" / "clv_log.csv"

INTERIM_FLOOR = 30
FULL_CONFIDENCE_TARGET = 892  # docs/politics_sample_size_methodology.md Section 3


def build_report() -> dict:
    if not CLV_LOG_PATH.exists():
        return {
            "clv_log_exists": False,
            "message": (
                f"{CLV_LOG_PATH} does not exist yet. This means either "
                "politics_pipeline.yml has not yet completed a successful "
                "run on GitHub, or its CLV-logging stage has not yet "
                "produced a committed log -- check the real run history on "
                "GitHub's Actions tab for politics_pipeline.yml before "
                "assuming this is simply 'no data yet.'"
            ),
            "interim_floor": INTERIM_FLOOR,
            "full_confidence_target": FULL_CONFIDENCE_TARGET,
            "closed_flags_observed": 0,
            "interim_floor_met": False,
        }

    df = pd.read_csv(CLV_LOG_PATH)
    total = len(df)
    closed = df.loc[df["status"] == "closed"] if "status" in df.columns else df.iloc[0:0]
    n_closed = len(closed)

    return {
        "clv_log_exists": True,
        "total_flags_ever_logged": total,
        "closed_flags_observed": n_closed,
        "note": (
            "'closed' means the flag disappeared from the latest estimates "
            "pull, per clv_logger.py's existing convention -- not yet "
            "confirmed as a real race resolution. See this script's own "
            "docstring."
        ),
        "interim_floor": INTERIM_FLOOR,
        "interim_floor_met": n_closed >= INTERIM_FLOOR,
        "full_confidence_target": FULL_CONFIDENCE_TARGET,
        "pct_of_full_target": round(100 * n_closed / FULL_CONFIDENCE_TARGET, 2),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Session 5.7 -- politics sample-size progress report.")
    parser.add_argument("--report", action="store_true", help="Print the progress report.")
    args = parser.parse_args()
    if not args.report:
        parser.error("Specify --report.")
    print(json.dumps(build_report(), indent=2, default=str))
