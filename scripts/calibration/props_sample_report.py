"""
Session 6.7 -- Props Sample-Size Progress Report (Live Validation Window)

WHAT THIS SCRIPT IS
--------------------
Reads data/sportsbook_props/clv_log.csv (Session 6.3's clv_logger.py
--track props output) and reports real progress against the two
thresholds derived in docs/props_sample_size_methodology.md:
  - Interim floor: 30 graded (resolved) flags
  - Full-confidence target: ~1,562 graded flags

A "graded" flag here means status == "closed" in clv_log.csv. clv_logger.py
marks a flag "closed" when it disappears from the latest estimates pull
(Session 2.4's existing "disappeared == closed" convention, reused for this
track) -- it does NOT yet know whether that closure was a real game
resolution (prop settled) or something else (e.g. a market pulled pregame,
or a transient DK/FD ingestion outage misread as closure -- the same
false-signal risk named for Track 4 in politics_sample_report.py). This
script reports the "closed" count honestly labeled as such -- NOT as
"graded win/loss outcomes" -- until a real props-specific outcome tracker
exists (see docs/props_sample_size_methodology.md Section 7).

USAGE
-----
python props_sample_report.py --report
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]
CLV_LOG_PATH = BASE_DIR / "data" / "sportsbook_props" / "clv_log.csv"

INTERIM_FLOOR = 30
FULL_CONFIDENCE_TARGET = 1562  # docs/props_sample_size_methodology.md Section 3


def build_report() -> dict:
    if not CLV_LOG_PATH.exists():
        return {
            "clv_log_exists": False,
            "message": (
                f"{CLV_LOG_PATH} does not exist yet. This means either "
                "props_pipeline.yml has not yet completed a successful "
                "run on GitHub, or its CLV-logging stage has not yet "
                "produced a committed log -- check the real run history on "
                "GitHub's Actions tab for props_pipeline.yml before "
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
            "confirmed as a real prop settlement. See this script's own "
            "docstring."
        ),
        "interim_floor": INTERIM_FLOOR,
        "interim_floor_met": n_closed >= INTERIM_FLOOR,
        "full_confidence_target": FULL_CONFIDENCE_TARGET,
        "pct_of_full_target": round(100 * n_closed / FULL_CONFIDENCE_TARGET, 2),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Session 6.7 -- props sample-size progress report.")
    parser.add_argument("--report", action="store_true", help="Print the progress report.")
    args = parser.parse_args()
    if not args.report:
        parser.error("Specify --report.")
    print(json.dumps(build_report(), indent=2, default=str))
