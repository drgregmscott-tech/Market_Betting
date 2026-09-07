"""
Session 4.2 - Weather Threshold Estimation Model

WHAT THIS SCRIPT IS
--------------------
Computes this project's own real probability estimate for every real,
live Kalshi weather-threshold contract in Session 4.1's ingested data
(data/weather/normalized/kalshi_weather_latest.csv), by comparing that
contract's threshold against NWS's public forecast for the same
station/date (data/weather/normalized/nws_forecast_latest.csv), then
outputs that estimate next to Kalshi's own live price so a later session
(4.3, CLV logging) can flag and size real +EV opportunities.

This is new modeling work, not a reuse of pickem_model.py's blend logic
(season average + recency-weighted form) - that model exists because
player performance has a real, direct historical record to average.
Weather does not: this project has one forecast number per station per
day, not a player's last 10 games, so the estimation problem here is
fundamentally about turning ONE point forecast into a real probability
distribution, not about blending multiple historical inputs.

WHY THIS SCRIPT NEEDS AN UNCERTAINTY (SIGMA) VALUE, NOT JUST THE
FORECAST NUMBER ITSELF - A REAL, NAMED DECISION
-----------------------------------------------------------------------
Confirmed live during this session: NWS's public gridded forecast
(api.weather.gov's forecastGridData endpoint, pulled by
ingest_nws_weather_data.py) returns exactly ONE number per station per
day - a single deterministic forecast, not an ensemble of possible
outcomes and not a published confidence interval. A probability model
cannot honestly turn "the forecast is 84 F" into "there is a 62% chance
the real high is over 85 F" without SOME real, documented measure of how
far forecasts like this one have historically been from the truth.

Two real ways to get that uncertainty measure were considered:
1. This project's own measured forecast error, broken out by how many
   days ahead the forecast was made ("lead time"). This is the right
   long-term source - it is this project's own real data, for these
   exact stations. It does not exist yet: as of this session (2026-09-07)
   Session 4.1 has only pulled live data once, so there is no history to
   measure error against.
2. A literature-sourced, non-project starting estimate - published
   research on how accurate U.S. temperature forecasts typically are by
   lead time, clearly flagged as a placeholder, not this project's own
   measured number.

DECISION (this session): use BOTH, blended automatically, not one or the
other:
- Path 2 (the literature curve below, see LITERATURE_MAE_BY_LEAD_DAY) is
  used from day one so this model produces real, usable output
  immediately.
- Path 1 is being collected automatically in the background starting
  this session, via a new scheduled GitHub Action
  (.github/workflows/weather_calibration_pipeline.yml) that runs
  ingest_nws_weather_data.py once a day and keeps every day's snapshot
  (not just "latest"), plus a new script
  (scripts/calibration/weather_forecast_error.py) that turns those
  accumulating snapshots into this project's own real error-by-lead-day
  numbers once enough exist.
- This script (weather_model.py) checks, for EACH lead-day bucket
  separately, whether this project's own real measured data
  (data/weather/calibration/forecast_error_by_leadtime.csv) has reached
  MIN_REAL_SAMPLES_PER_LEAD_DAY real observations for that specific lead
  day. If yes, it uses the real measured MAE for that lead day. If not,
  it falls back to the literature curve for that lead day only. This
  means the model gets MORE accurate automatically over time, one lead-
  day bucket at a time, with no future session needing to remember to
  "swap it over" by hand - see get_sigma_for_lead_day() below for the
  exact logic.

LITERATURE SOURCE FOR THE STARTING CURVE (a real, cited, non-project
source - not an invented number)
-----------------------------------------------------------------------
Penn State University's public "Weather Revealed" course material
(courses.ems.psu.edu/meteo3/node/2285, accessed 2026-09-07), summarizing
published U.S. temperature forecast verification patterns, states three
real anchor points for daily high/low temperature forecast mean absolute
error (MAE):
- "a couple of days" out (roughly day 1-2): "reasonably accurate ...
  absolute errors of 3 degrees Fahrenheit or less"
- day 3-4 out: "within about 3 to 4 degrees Fahrenheit"
- day 7 out: "largest mean absolute errors, of about 5 to 6 degrees
  Fahrenheit"
This script uses the upper (more conservative/cautious) end of each
cited range as a named anchor point - 2.5 F (day 1), 4.0 F (day 4), 5.5 F
(day 7) - and LINEARLY INTERPOLATES between those three real anchors for
the lead days not directly named (2, 3, 5, 6). Choosing the upper/more-
cautious end of each cited range, and interpolating linearly rather than
guessing a curve shape, are this project's own documented modeling
choices, clearly separated above from the literature's own real, cited
numbers. Beyond day 7 (MAX_LITERATURE_LEAD_DAY), this project's own
NWS-pull horizon has not yet been confirmed live to extend that far
(Session 4.1 did not check the real maximum forecastGridData horizon) -
contracts beyond that are marked "lead_time_unsupported" rather than
silently extrapolating the curve past where it has any real citation.

THIS SESSION'S OWN NAMED CONSTANT: SETTLEMENT-GAP UNCERTAINTY
-----------------------------------------------------------------------
Session 4.1 (Open Decision #31) found, from real live data, that this
project's own NWS-based daily high/low reading differs from Kalshi's
actual settlement value by up to approximately 1 F, caused by Kalshi's
settlement feed rounding to the nearest whole degree per clock hour.
That is a REAL, separate source of uncertainty from forecast error (it
exists even for a same-day, already-observed temperature, not just a
multi-day-out forecast), so it is combined with the forecast-error sigma
in quadrature (combining two independent real error sources), not simply
added - see SETTLEMENT_GAP_SIGMA_F below.

HOW THE PROBABILITY IS COMPUTED
-----------------------------------------------------------------------
Every Kalshi weather contract asks a real, structured threshold
question (schema_weather.py's strike_type/floor_strike/cap_strike,
confirmed live in Session 4.1):
- "greater": real answer must be ABOVE floor_strike
- "less": real answer must be BELOW cap_strike
- "between": real answer must fall inside [floor_strike, cap_strike]
This model treats the true temperature as normally distributed around
the NWS forecast value (the mean) with the lead-day-specific sigma
described above, and computes the exact probability of each threshold
question using the normal distribution's CDF (implemented here with
Python's own math.erf - no third-party statistics dependency needed for
one distribution shape). This mirrors pickem_model.py's own use of a
normal-distribution approximation for prop lines (Session 2.3), applied
here to a genuinely different input (one point forecast + a lead-day
uncertainty band, instead of a player's own scoring history).

WHAT THIS SCRIPT DOES NOT DO (same ingestion/estimation boundary
schema_weather.py's docstring already draws)
-----------------------------------------------------------------------
No sizing, no Kelly-style bet sizing, no CLV logging, no flag/no-flag
decision threshold. This script's only job is to produce, for every real
contract it can, a documented probability estimate (or an explicit
model_status explaining why it couldn't) next to Kalshi's own live
yes_bid/yes_ask - the same "estimate now, size/flag/log later" boundary
Session 2.3's pickem_model.py and Session 2.4's clv_logger.py already
established for Track 1. Session 4.3 (CLV Logging Hook-In) is where this
output gets wired into that same downstream pipeline.

WHERE OUTPUT GOES
------------------
/data/weather/estimates/weather_estimates_<timestamp>.csv
/data/weather/estimates/weather_estimates_latest.csv

USAGE
-----
python weather_model.py
"""

from __future__ import annotations

import csv
import logging
import math
import time
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Optional

BASE_DIR = Path(__file__).resolve().parents[2]
KALSHI_WEATHER_LATEST = BASE_DIR / "data" / "weather" / "normalized" / "kalshi_weather_latest.csv"
NWS_FORECAST_LATEST = BASE_DIR / "data" / "weather" / "normalized" / "nws_forecast_latest.csv"
REAL_ERROR_BY_LEAD_DAY = BASE_DIR / "data" / "weather" / "calibration" / "forecast_error_by_leadtime.csv"
ESTIMATES_DIR = BASE_DIR / "data" / "weather" / "estimates"
LOG_PATH = BASE_DIR / "logs" / "estimation.log"

# --- Literature-sourced starting curve (see module docstring for the
# real, cited source and the "upper end of each range" / "linear
# interpolation" modeling choices this project made on top of it). ---
LITERATURE_MAE_ANCHORS_F: dict[int, float] = {
    1: 2.5,
    4: 4.0,
    7: 5.5,
}
MAX_LITERATURE_LEAD_DAY = 7

# --- This session's own named constant, from Session 4.1's Open
# Decision #31 (real, measured Kalshi-settlement-vs-NWS gap, bounded at
# approximately 1 F by a rounding-step root cause, not an open-ended or
# unexplained divergence). ---
SETTLEMENT_GAP_SIGMA_F = 1.0

# --- Minimum real, measured samples this project's own calibration file
# must have for a SPECIFIC lead-day bucket before that bucket's real
# measured MAE is trusted over the literature placeholder for that same
# bucket. Chosen as a round, conservative starting number - small enough
# that real data can start overriding the placeholder within the first
# few weeks of the new daily calibration pipeline, large enough that a
# single unusual day's error doesn't swing the model. Revisit with real
# evidence once the calibration pipeline has run long enough to have an
# informed opinion - not claimed as statistically optimal here. ---
MIN_REAL_SAMPLES_PER_LEAD_DAY = 20

# MAE (mean absolute error) -> normal-distribution sigma. For a normal
# distribution, E[|X - mean|] = sigma * sqrt(2/pi), so sigma = MAE /
# sqrt(2/pi) (~= MAE / 0.7979). Standard, named conversion - not an
# arbitrary multiplier.
_MAE_TO_SIGMA_FACTOR = math.sqrt(2.0 / math.pi)


def setup_logging() -> logging.Logger:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("weather_model")
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


def _normal_cdf(x: float, mean: float, sigma: float) -> float:
    """Standard normal CDF via math.erf - no third-party stats package
    needed for a single distribution shape."""
    if sigma <= 0:
        # Degenerate case (should not occur with real sigma inputs, but
        # guarded rather than dividing by zero) - treat as certainty at
        # the mean.
        return 1.0 if x >= mean else 0.0
    z = (x - mean) / (sigma * math.sqrt(2.0))
    return 0.5 * (1.0 + math.erf(z))


def _literature_mae_for_lead_day(lead_days: int) -> Optional[float]:
    """Linearly interpolates between the three real, cited anchor points
    (day 1, 4, 7). Returns None for lead_days outside the range this
    project has any real citation for (see module docstring)."""
    anchors = sorted(LITERATURE_MAE_ANCHORS_F.items())
    if lead_days < anchors[0][0]:
        # Before day 1 (e.g. lead_days == 0, same-day forecast) - use
        # day 1's anchor rather than extrapolating below the cited range.
        return anchors[0][1]
    if lead_days > anchors[-1][0]:
        return None
    for (d1, mae1), (d2, mae2) in zip(anchors, anchors[1:]):
        if d1 <= lead_days <= d2:
            if d2 == d1:
                return mae1
            frac = (lead_days - d1) / (d2 - d1)
            return mae1 + frac * (mae2 - mae1)
    return None


def load_real_error_by_lead_day() -> dict[int, dict]:
    """Loads this project's own real, measured forecast-error-by-lead-day
    file if it exists yet (produced by
    scripts/calibration/weather_forecast_error.py, fed by the new daily
    calibration pipeline). Returns {} if the file does not exist yet -
    this is expected and normal for the first several weeks after this
    session, not an error."""
    if not REAL_ERROR_BY_LEAD_DAY.exists():
        log.info(
            "No real calibration file yet at %s - using the literature "
            "placeholder curve for every lead day until enough real data "
            "accumulates. This is expected, not an error, in the weeks "
            "right after Session 4.2.",
            REAL_ERROR_BY_LEAD_DAY,
        )
        return {}
    result: dict[int, dict] = {}
    with REAL_ERROR_BY_LEAD_DAY.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                lead_days = int(row["lead_days"])
                result[lead_days] = {
                    "sample_count": int(row["sample_count"]),
                    "mae_f": float(row["mae_f"]),
                }
            except (KeyError, ValueError):
                continue
    return result


def get_sigma_for_lead_day(lead_days: int, real_error_by_lead_day: dict[int, dict]) -> tuple[Optional[float], str]:
    """Returns (sigma_f, source_label). source_label is one of
    'real_measured' or 'literature_placeholder', logged per-row in the
    output so every estimate's uncertainty source is auditable, not
    hidden. Returns (None, ...) if neither a real measurement nor a
    literature anchor covers this lead day."""
    real = real_error_by_lead_day.get(lead_days)
    if real is not None and real["sample_count"] >= MIN_REAL_SAMPLES_PER_LEAD_DAY:
        forecast_sigma = real["mae_f"] * _MAE_TO_SIGMA_FACTOR
        source = "real_measured"
    else:
        mae = _literature_mae_for_lead_day(lead_days)
        if mae is None:
            return None, "unsupported_lead_day"
        forecast_sigma = mae * _MAE_TO_SIGMA_FACTOR
        source = "literature_placeholder"
    total_sigma = math.sqrt(forecast_sigma**2 + SETTLEMENT_GAP_SIGMA_F**2)
    return total_sigma, source


def load_kalshi_weather_rows() -> list[dict]:
    if not KALSHI_WEATHER_LATEST.exists():
        raise FileNotFoundError(
            f"Missing {KALSHI_WEATHER_LATEST} - run "
            f"scripts/ingestion/ingest_weather_markets.py first."
        )
    with KALSHI_WEATHER_LATEST.open("r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_forecast_index() -> dict[tuple[str, str, str], dict]:
    """Keys on (station_id, target_date, forecast_kind) -> forecast row,
    matching schema_weather.py's own stated join fields."""
    if not NWS_FORECAST_LATEST.exists():
        raise FileNotFoundError(
            f"Missing {NWS_FORECAST_LATEST} - run "
            f"scripts/ingestion/ingest_nws_weather_data.py first."
        )
    index: dict[tuple[str, str, str], dict] = {}
    with NWS_FORECAST_LATEST.open("r", newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            key = (row["station_id"], row["target_date"], row["forecast_kind"])
            # Kalshi's forecastGridData can return more than one entry
            # per day for the same station (rare, but Session 4.1 did
            # not rule it out) - keep the first real one seen rather
            # than silently overwrite, and log if a real duplicate
            # shows up.
            if key not in index:
                index[key] = row
    return index


def _forecast_kind_for_series(series_ticker: str) -> Optional[str]:
    """Kalshi's own real ticker convention (confirmed live, Session 4.1):
    KXHIGH* series ask about the daily HIGH, KXLOW* series ask about the
    daily LOW. Returns None (not guessed) for anything else."""
    if series_ticker.startswith("KXHIGH"):
        return "max"
    if series_ticker.startswith("KXLOW"):
        return "min"
    return None


def _parse_date(value: str) -> Optional[date]:
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return None


def _parse_pulled_at_date(value: str) -> Optional[date]:
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).date()
    except (ValueError, TypeError, AttributeError):
        return None


def compute_probability(
    strike_type: str, floor_strike: Optional[float], cap_strike: Optional[float],
    mean_f: float, sigma_f: float,
) -> Optional[float]:
    if strike_type == "greater":
        if floor_strike is None:
            return None
        return 1.0 - _normal_cdf(floor_strike, mean_f, sigma_f)
    if strike_type == "less":
        if cap_strike is None:
            return None
        return _normal_cdf(cap_strike, mean_f, sigma_f)
    if strike_type == "between":
        if floor_strike is None or cap_strike is None:
            return None
        return _normal_cdf(cap_strike, mean_f, sigma_f) - _normal_cdf(floor_strike, mean_f, sigma_f)
    return None


OUTPUT_FIELDS = [
    "series_ticker", "market_ticker", "city_label", "station_id", "target_date",
    "strike_type", "floor_strike", "cap_strike",
    "yes_bid", "yes_ask", "no_bid", "no_ask",
    "forecast_kind", "forecast_value_f", "lead_days",
    "model_sigma_f", "sigma_source", "model_prob_yes",
    "model_status", "pulled_at",
]


def run() -> dict:
    pulled_at = datetime.now(timezone.utc).isoformat()
    pulled_at_compact = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    today = datetime.now(timezone.utc).date()

    summary = {
        "pulled_at": pulled_at,
        "input_rows": 0,
        "estimated": 0,
        "no_forecast_kind": 0,
        "no_forecast_data": 0,
        "target_date_passed": 0,
        "unsupported_lead_day": 0,
        "missing_strike_fields": 0,
    }

    log.info("=== Weather estimation run starting ===")

    kalshi_rows = load_kalshi_weather_rows()
    forecast_index = load_forecast_index()
    real_error_by_lead_day = load_real_error_by_lead_day()

    summary["input_rows"] = len(kalshi_rows)
    output_rows: list[dict] = []

    for row in kalshi_rows:
        base = {col: row.get(col) for col in [
            "series_ticker", "market_ticker", "city_label", "station_id", "target_date",
            "strike_type", "floor_strike", "cap_strike",
            "yes_bid", "yes_ask", "no_bid", "no_ask",
        ]}
        base["pulled_at"] = pulled_at

        forecast_kind = _forecast_kind_for_series(row["series_ticker"])
        if forecast_kind is None:
            summary["no_forecast_kind"] += 1
            output_rows.append({**base, "model_status": "no_forecast_kind"})
            continue

        target_date = _parse_date(row["target_date"])
        if target_date is None:
            output_rows.append({**base, "model_status": "bad_target_date"})
            continue

        lead_days = (target_date - today).days
        if lead_days < 0:
            summary["target_date_passed"] += 1
            output_rows.append({**base, "forecast_kind": forecast_kind, "lead_days": lead_days,
                                 "model_status": "target_date_passed"})
            continue

        key = (row["station_id"], row["target_date"], forecast_kind)
        forecast_row = forecast_index.get(key)
        if forecast_row is None or not forecast_row.get("forecast_value_f"):
            summary["no_forecast_data"] += 1
            output_rows.append({**base, "forecast_kind": forecast_kind, "lead_days": lead_days,
                                 "model_status": "no_forecast_data"})
            continue

        try:
            mean_f = float(forecast_row["forecast_value_f"])
        except (TypeError, ValueError):
            summary["no_forecast_data"] += 1
            output_rows.append({**base, "forecast_kind": forecast_kind, "lead_days": lead_days,
                                 "model_status": "no_forecast_data"})
            continue

        sigma_f, sigma_source = get_sigma_for_lead_day(lead_days, real_error_by_lead_day)
        if sigma_f is None:
            summary["unsupported_lead_day"] += 1
            output_rows.append({**base, "forecast_kind": forecast_kind, "lead_days": lead_days,
                                 "forecast_value_f": mean_f, "model_status": "unsupported_lead_day"})
            continue

        floor_strike = float(row["floor_strike"]) if row.get("floor_strike") else None
        cap_strike = float(row["cap_strike"]) if row.get("cap_strike") else None
        prob_yes = compute_probability(row["strike_type"], floor_strike, cap_strike, mean_f, sigma_f)
        if prob_yes is None:
            summary["missing_strike_fields"] += 1
            output_rows.append({**base, "forecast_kind": forecast_kind, "lead_days": lead_days,
                                 "forecast_value_f": mean_f, "model_sigma_f": round(sigma_f, 2),
                                 "sigma_source": sigma_source, "model_status": "missing_strike_fields"})
            continue

        summary["estimated"] += 1
        output_rows.append({
            **base,
            "forecast_kind": forecast_kind,
            "forecast_value_f": mean_f,
            "lead_days": lead_days,
            "model_sigma_f": round(sigma_f, 2),
            "sigma_source": sigma_source,
            "model_prob_yes": round(prob_yes, 4),
            "model_status": "estimated",
        })

    ESTIMATES_DIR.mkdir(parents=True, exist_ok=True)
    snapshot_path = ESTIMATES_DIR / f"weather_estimates_{pulled_at_compact}.csv"
    latest_path = ESTIMATES_DIR / "weather_estimates_latest.csv"
    for path in (snapshot_path, latest_path):
        with path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=OUTPUT_FIELDS)
            writer.writeheader()
            for r in output_rows:
                writer.writerow({col: r.get(col) for col in OUTPUT_FIELDS})

    log.info(
        "=== Weather estimation run complete: %d input rows, %d estimated, "
        "%d no_forecast_kind, %d no_forecast_data, %d target_date_passed, "
        "%d unsupported_lead_day, %d missing_strike_fields ===",
        summary["input_rows"], summary["estimated"], summary["no_forecast_kind"],
        summary["no_forecast_data"], summary["target_date_passed"],
        summary["unsupported_lead_day"], summary["missing_strike_fields"],
    )
    summary["snapshot_path"] = str(snapshot_path)
    return summary


if __name__ == "__main__":
    import json
    result = run()
    print(json.dumps(result, indent=2))
