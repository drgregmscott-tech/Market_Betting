"""
Session 4.7 -- Weather Sample-Size Progress Report (Live Validation Window)

WHAT THIS SCRIPT IS
--------------------
Reads data/weather/clv_log.csv (Session 4.3's clv_logger.py --track weather
output) and reports real progress against the two thresholds derived in
docs/weather_sample_size_methodology.md:
  - Interim floor: 30 graded (resolved) flags
  - Full-confidence target: ~2,069 graded flags

A "graded" flag here means status == "closed" in clv_log.csv. clv_logger.py
marks a flag "closed" when it disappears from the latest Kalshi weather
markets pull (Session 2.4's existing "disappeared == closed" convention,
reused for this track) -- it does NOT yet confirm whether the underlying
contract resolved YES or NO. This script reports the "closed" count honestly
labeled as a CLV-equivalent signal -- NOT a graded win/loss outcome -- until
a real weather-specific outcome tracker exists (see
docs/weather_sample_size_methodology.md Section 7).

Also reports mean clv_edge_at_close across closed flags -- the same
north-star trendline signal (real edge holding up at close, on average
positive) this session's go/no-go review depends on.

USAGE
-----
python weather_sample_report.py --report
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]
CLV_LOG_PATH = BASE_DIR / "data" / "weather" / "clv_log.csv"

INTERIM_FLOOR = 30
FULL_CONFIDENCE_TARGET = 2069  # docs/weather_sample_size_methodology.md Section 3


def build_report() -> dict:
    if not CLV_LOG_PATH.exists():
        return {
            "clv_log_exists": False,
            "message": (
                f"{CLV_LOG_PATH} does not exist yet. This means either "
                "weather_pipeline.yml has not yet completed a successful "
                "run on GitHub, or its CLV-logging stage has not yet "
                "produced a committed log -- check the real run history on "
                "GitHub's Actions tab for weather_pipeline.yml before "
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

    mean_clv_edge_at_close = None
    pct_positive_clv_edge = None
    if n_closed > 0 and "clv_edge_at_close" in closed.columns:
        valid = closed["clv_edge_at_close"].dropna()
        if len(valid) > 0:
            mean_clv_edge_at_close = round(float(valid.mean()), 4)
            pct_positive_clv_edge = round(100 * float((valid > 0).mean()), 2)

    return {
        "clv_log_exists": True,
        "total_flags_ever_logged": total,
        "closed_flags_observed": n_closed,
        "mean_clv_edge_at_close": mean_clv_edge_at_close,
        "pct_closed_flags_with_positive_clv_edge": pct_positive_clv_edge,
        "note": (
            "'closed' means the flag disappeared from the latest Kalshi "
            "weather markets pull, per clv_logger.py's existing convention "
            "-- not yet a confirmed real win/loss outcome. See this "
            "script's own docstring and docs/weather_sample_size_methodology.md "
            "Section 7."
        ),
        "interim_floor": INTERIM_FLOOR,
        "interim_floor_met": n_closed >= INTERIM_FLOOR,
        "full_confidence_target": FULL_CONFIDENCE_TARGET,
        "pct_of_full_target": round(100 * n_closed / FULL_CONFIDENCE_TARGET, 2),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Session 4.7 -- weather sample-size progress report.")
    parser.add_argument("--report", action="store_true", help="Print the progress report.")
    args = parser.parse_args()
    if not args.report:
        parser.error("Specify --report.")
    print(json.dumps(build_report(), indent=2, default=str))
