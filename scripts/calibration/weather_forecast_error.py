"""
Session 4.2 - Real Forecast-Error-by-Lead-Day Calculator

WHAT THIS SCRIPT IS
--------------------
Turns this project's own accumulating, real, daily NWS forecast/observed
snapshots into this project's own real, measured forecast error, broken
out by lead time (how many days ahead each forecast was made). This is
the "real data" side of weather_model.py's documented blend (see that
script's own module docstring): a literature-sourced placeholder is used
where this file does not yet have enough real samples for a given lead
day, and this file's own real numbers take over automatically, one lead-
day bucket at a time, once they do.

WHY THIS SCRIPT DOES NOTHING USEFUL THE FIRST TIME IT RUNS - EXPECTED,
NOT A BUG
-----------------------------------------------------------------------
This script needs REAL PAIRS: a forecast made N days before a target
date, and a real observed value for that same target date, for the same
station. Before this session, only one live snapshot of each existed
(2026-09-06). The new scheduled pipeline
(.github/workflows/weather_calibration_pipeline.yml) is what actually
builds up real pairs over time, one day at a time - this script just
reads whatever has accumulated so far and computes real statistics from
it. Running this the day after Session 4.2 closes will find few or no
real pairs yet (a forecast made today for a target date 3 days out
cannot be checked against a real observation until 3 real days have
passed) - that is correct behavior, not a broken script.

HOW A "REAL PAIR" IS FOUND
-----------------------------------------------------------------------
1. Every committed forecast snapshot file
   (data/weather/normalized/nws_forecast_<timestamp>.csv) contributes
   its own real forecast rows: (station_id, target_date, forecast_kind,
   forecast_value_f, pulled_at).
2. lead_days = (target_date - date(pulled_at)).days - the real number of
   days between when the forecast was made and the date it was about.
3. Every committed observed snapshot file
   (data/weather/normalized/nws_observed_daily_<timestamp>.csv)
   contributes real observed rows: (station_id, observed_date,
   observed_max_f, observed_min_f, sample_count, pulled_at).
4. For a given (station_id, target_date, forecast_kind), the real
   observed value used is taken from the observed snapshot with the
   HIGHEST sample_count for that (station_id, observed_date==target_date)
   pair - more real samples in a day means a more complete real read on
   that day's true max/min, not a partial day still in progress.
5. error = forecast_value_f - observed_value (signed; positive =
   forecast too high). abs_error = abs(error).

WHAT THIS SCRIPT WRITES
-----------------------------------------------------------------------
- data/weather/calibration/forecast_error_detail.csv - every real
  matched (forecast, observation) pair found, for audit - so a future
  session can see exactly which real days fed into a given lead-day's
  MAE, not just the aggregated number.
- data/weather/calibration/forecast_error_by_leadtime.csv - aggregated
  by lead_days: sample_count, mae_f (mean absolute error), mean_bias_f
  (signed mean error - useful later for spotting a real systematic
  over/under-forecast pattern, not used by weather_model.py yet),
  last_updated. This is the file weather_model.py's
  get_sigma_for_lead_day() reads.

USAGE
-----
python weather_forecast_error.py
"""

from __future__ import annotations

import csv
import logging
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

BASE_DIR = Path(__file__).resolve().parents[2]
NORMALIZED_DIR = BASE_DIR / "data" / "weather" / "normalized"
CALIBRATION_DIR = BASE_DIR / "data" / "weather" / "calibration"
LOG_PATH = BASE_DIR / "logs" / "estimation.log"


def setup_logging() -> logging.Logger:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("weather_forecast_error")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()
    fh = logging.FileHandler(LOG_PATH, mode="a", encoding="utf-8")
    ch = logging.StreamHandler()
    fmt = logging.Formatter("%(asctime)s UTC | %(levelname)s | %(message)s")
    fmt.converter = time.gmtime
    fh.setFormatter(fmt)
    ch.setFormatter(fmt)
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger


log = setup_logging()


def _parse_date(value: str):
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return None


def _parse_pulled_at_date(value: str):
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).date()
    except (ValueError, TypeError, AttributeError):
        return None


def load_all_forecast_rows() -> list[dict]:
    """Reads every real, timestamped forecast snapshot file (not just
    'latest') - this is this project's own real accumulated history,
    building up one real GitHub Actions run at a time."""
    rows: list[dict] = []
    for path in sorted(NORMALIZED_DIR.glob("nws_forecast_*.csv")):
        if path.name == "nws_forecast_latest.csv":
            continue
        with path.open("r", newline="", encoding="utf-8") as f:
            rows.extend(csv.DictReader(f))
    return rows


def load_best_observed_by_station_date() -> dict[tuple[str, str], dict]:
    """Reads every real, timestamped observed-daily snapshot file and
    keeps, per (station_id, observed_date), the row with the highest
    real sample_count seen across all snapshots - the most complete real
    read on that day."""
    best: dict[tuple[str, str], dict] = {}
    for path in sorted(NORMALIZED_DIR.glob("nws_observed_daily_*.csv")):
        if path.name == "nws_observed_daily_latest.csv":
            continue
        with path.open("r", newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                key = (row["station_id"], row["observed_date"])
                try:
                    sample_count = int(row["sample_count"])
                except (TypeError, ValueError):
                    continue
                existing = best.get(key)
                if existing is None or sample_count > int(existing["sample_count"]):
                    best[key] = row
    return best


def run() -> dict:
    log.info("=== Forecast-error calibration run starting ===")

    forecast_rows = load_all_forecast_rows()
    observed_by_station_date = load_best_observed_by_station_date()

    detail_rows: list[dict] = []
    seen_pairs: set[tuple] = set()  # de-dupe identical (station, target_date, kind, pulled_at) across overlapping snapshot files

    for frow in forecast_rows:
        target_date = _parse_date(frow.get("target_date", ""))
        pulled_at_date = _parse_pulled_at_date(frow.get("pulled_at", ""))
        if target_date is None or pulled_at_date is None:
            continue
        forecast_value = frow.get("forecast_value_f")
        if not forecast_value:
            continue

        dedupe_key = (frow["station_id"], frow["target_date"], frow["forecast_kind"], frow["pulled_at"])
        if dedupe_key in seen_pairs:
            continue
        seen_pairs.add(dedupe_key)

        lead_days = (target_date - pulled_at_date).days
        if lead_days < 0:
            # A forecast pulled after its own target date already
            # passed - not a real forward-looking forecast, skip.
            continue

        obs_key = (frow["station_id"], frow["target_date"])
        observed_row = observed_by_station_date.get(obs_key)
        if observed_row is None:
            continue  # target date hasn't happened yet, or no real observation was ever captured for it

        obs_field = "observed_max_f" if frow["forecast_kind"] == "max" else "observed_min_f"
        observed_value = observed_row.get(obs_field)
        if not observed_value:
            continue

        try:
            forecast_f = float(forecast_value)
            observed_f = float(observed_value)
        except (TypeError, ValueError):
            continue

        error = forecast_f - observed_f
        detail_rows.append({
            "station_id": frow["station_id"],
            "target_date": frow["target_date"],
            "forecast_kind": frow["forecast_kind"],
            "lead_days": lead_days,
            "forecast_value_f": forecast_f,
            "observed_value_f": observed_f,
            "error_f": round(error, 2),
            "abs_error_f": round(abs(error), 2),
            "forecast_pulled_at": frow["pulled_at"],
            "observed_sample_count": observed_row.get("sample_count"),
        })

    CALIBRATION_DIR.mkdir(parents=True, exist_ok=True)

    detail_path = CALIBRATION_DIR / "forecast_error_detail.csv"
    detail_fields = [
        "station_id", "target_date", "forecast_kind", "lead_days",
        "forecast_value_f", "observed_value_f", "error_f", "abs_error_f",
        "forecast_pulled_at", "observed_sample_count",
    ]
    with detail_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=detail_fields)
        writer.writeheader()
        for row in detail_rows:
            writer.writerow(row)

    by_lead: dict[int, list[dict]] = defaultdict(list)
    for row in detail_rows:
        by_lead[row["lead_days"]].append(row)

    last_updated = datetime.now(timezone.utc).isoformat()
    summary_rows = []
    for lead_days, rows in sorted(by_lead.items()):
        sample_count = len(rows)
        mae = sum(r["abs_error_f"] for r in rows) / sample_count
        mean_bias = sum(r["error_f"] for r in rows) / sample_count
        summary_rows.append({
            "lead_days": lead_days,
            "sample_count": sample_count,
            "mae_f": round(mae, 3),
            "mean_bias_f": round(mean_bias, 3),
            "last_updated": last_updated,
        })

    summary_path = CALIBRATION_DIR / "forecast_error_by_leadtime.csv"
    summary_fields = ["lead_days", "sample_count", "mae_f", "mean_bias_f", "last_updated"]
    with summary_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=summary_fields)
        writer.writeheader()
        for row in summary_rows:
            writer.writerow(row)

    result = {
        "last_updated": last_updated,
        "real_pairs_found": len(detail_rows),
        "lead_day_buckets": len(summary_rows),
        "by_lead_day": {r["lead_days"]: r["sample_count"] for r in summary_rows},
    }
    log.info(
        "=== Forecast-error calibration run complete: %d real forecast/"
        "observation pairs found across %d lead-day buckets: %s ===",
        result["real_pairs_found"], result["lead_day_buckets"], result["by_lead_day"],
    )
    return result


if __name__ == "__main__":
    import json
    print(json.dumps(run(), indent=2))
