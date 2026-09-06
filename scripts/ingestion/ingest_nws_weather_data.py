"""
Session 4.1 - Public Ground-Truth Weather Data Ingestion (NWS)

WHAT THIS SCRIPT IS
--------------------
Pulls the free, public, no-key data this project needs to independently
estimate the real answer to each Kalshi weather-threshold question:
1. NWS's own gridded FORECAST data (daily max/min temperature, several
   days out) - the input to Session 4.2's estimation model.
2. NWS's own OBSERVED data (METAR-sourced, near-real-time) for the same
   station - used both to check forecast accuracy over time and, once a
   market's target_date has passed, as this project's own independent
   read on what the real answer was.

WHY "NWS" COVERS THIS PROJECT'S ORIGINAL "NWS/GFS/METAR" SCOPE WITH ONE
API, NOT THREE SEPARATE FEEDS - A REAL, NAMED DECISION
-----------------------------------------------------------------------
ROADMAP.md's Session 4.1 card named three public sources: NWS, GFS, and
METAR. Checked live, 2026-09-06: NWS's own public API (api.weather.gov,
no key required) already IS the union of these for this project's actual
need - its gridded forecast endpoint is NWS's own official forecast
(itself built from blended model guidance, GFS included, not a separate
raw GFS feed this project would otherwise have to decode on its own), and
its station-observation endpoint returns the same METAR reports directly,
already parsed into structured fields (temperature, timestamp, quality
flag) instead of raw METAR text this project would have to parse itself.
Pulling raw GFS grib2 files or raw METAR text and re-deriving what NWS's
own API already computes would add real complexity (grib2 decoding, METAR
text parsing) for no additional real information - a deliberate scope
decision, not a shortcut, and reversible later if a real reason to go
lower-level ever appears.

WHY THIS MATTERS FOR THE KALSHI/SETTLEMENT-SOURCE QUESTION RAISED THIS
SESSION
-----------------------------------------------------------------------
Kalshi's own settlement page (weather.com/kalshi, confirmed live
2026-09-06) states its data is "METAR airport observations relayed via
The Weather Company" for a fixed, named list of station codes - the SAME
station codes (e.g. KPHL, KATL) this script queries directly against
NWS's own public API. Both this project's ground truth and Kalshi's own
settlement value trace back to the same real-world METAR reports for the
same station. This does not guarantee an exact number-for-number match
(NWS and The Weather Company could round, time-window, or QC the same raw
reports slightly differently - not yet measured), but it means there is
no separate, private, unreplicable data source underneath Kalshi's
settlement, which was the real risk this session set out to check.

WHERE OUTPUT GOES
------------------
/data/weather/raw/nws_<station_id>_<timestamp>.json (one per station,
  forecast + observations together)
/data/weather/normalized/nws_forecast_<timestamp>.csv
/data/weather/normalized/nws_forecast_latest.csv
/data/weather/normalized/nws_observed_daily_<timestamp>.csv
/data/weather/normalized/nws_observed_daily_latest.csv

USAGE
-----
pip install requests --break-system-packages
python ingest_nws_weather_data.py
"""

from __future__ import annotations

import csv
import json
import logging
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional
from zoneinfo import ZoneInfo

import requests

from station_map import SERIES_TICKER_TO_STATION, UNMATCHED_REFERENCE_STATIONS

BASE_DIR = Path(__file__).resolve().parents[2]
RAW_DIR = BASE_DIR / "data" / "weather" / "raw"
NORMALIZED_DIR = BASE_DIR / "data" / "weather" / "normalized"
LOG_PATH = BASE_DIR / "logs" / "ingestion.log"

NWS_BASE_URL = "https://api.weather.gov"

# NWS's public API asks callers to identify themselves via User-Agent
# (documented, no key/registration required) rather than an API key -
# confirmed live 2026-09-06, requests succeeded without one, but this is
# NWS's own documented best practice so it is set here anyway.
HEADERS = {
    "User-Agent": "MarketBetting-Session4.1 (drgregmscott-tech/Market_Betting)",
    "Accept": "application/geo+json",
}

MAX_RETRIES = 2
RETRY_BACKOFF_SECONDS = 3
REQUEST_TIMEOUT_SECONDS = 15
NWS_PER_STATION_PAUSE_SECONDS = 0.5

# This project's actual target station list - every real, confirmed
# station this session's station_map.py resolves a live Kalshi series to,
# deduplicated. Deliberately does NOT include
# UNMATCHED_REFERENCE_STATIONS (no live series points to those yet - see
# station_map.py).
TARGET_STATIONS = sorted(set(SERIES_TICKER_TO_STATION.values()))


def setup_logging() -> logging.Logger:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("ingest_nws_weather_data")
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


def _fetch_with_retries(url: str, params: Optional[dict] = None) -> dict:
    last_error = None
    for attempt in range(1, MAX_RETRIES + 2):
        try:
            r = requests.get(url, headers=HEADERS, params=params, timeout=REQUEST_TIMEOUT_SECONDS)
            r.raise_for_status()
            return r.json()
        except requests.exceptions.RequestException as exc:
            last_error = exc
            log.warning("Attempt %d/%d failed for %s: %s", attempt, MAX_RETRIES + 1, url, exc)
            if attempt <= MAX_RETRIES:
                time.sleep(RETRY_BACKOFF_SECONDS)
    raise RuntimeError(f"All attempts failed for {url}: {last_error}")


def _c_to_f(celsius: Optional[float]) -> Optional[float]:
    """Kalshi's weather thresholds are in Fahrenheit (confirmed live -
    'Will the maximum temperature be >85 on Sep 7, 2026?'). NWS's API
    returns Celsius (confirmed live). Converted here, once, at ingestion,
    so every downstream file already speaks Kalshi's unit - not left for
    a future script to get wrong."""
    if celsius is None:
        return None
    return celsius * 9.0 / 5.0 + 32.0


def fetch_station_metadata(station_id: str) -> Optional[dict]:
    """Station lat/lon/timezone via NWS's /stations/{id} endpoint - needed
    to resolve which grid office+cell to query for forecast data, and
    which local calendar day an hourly observation actually belongs to."""
    try:
        payload = _fetch_with_retries(f"{NWS_BASE_URL}/stations/{station_id}")
        props = payload.get("properties", {})
        coords = payload.get("geometry", {}).get("coordinates")  # [lon, lat]
        if not coords:
            return None
        return {
            "lon": coords[0],
            "lat": coords[1],
            "timezone": props.get("timeZone"),
        }
    except RuntimeError as exc:
        log.warning("Could not fetch station metadata for %s: %s", station_id, exc)
        return None


def fetch_grid_forecast(lat: float, lon: float) -> Optional[dict]:
    """NWS's /points lookup, then its gridded forecast data (daily max/min
    temperature, several days out, confirmed live). This is NWS's own
    official forecast, not a raw single-model pull - see module docstring
    for why that's the right level for this project."""
    try:
        point = _fetch_with_retries(f"{NWS_BASE_URL}/points/{lat},{lon}")
        grid_url = point.get("properties", {}).get("forecastGridData")
        if not grid_url:
            return None
        return _fetch_with_retries(grid_url)
    except RuntimeError as exc:
        log.warning("Could not fetch grid forecast for %s,%s: %s", lat, lon, exc)
        return None


def fetch_recent_observations(station_id: str) -> list[dict]:
    """Recent METAR-sourced observations for this station (confirmed live
    - 5-minute-ish cadence). NWS's default page covers roughly the last
    several hours; that is enough to confirm freshness this session and
    to build same-day running max/min once this pipeline runs on a
    schedule (Session 4.5)."""
    try:
        payload = _fetch_with_retries(f"{NWS_BASE_URL}/stations/{station_id}/observations")
        return payload.get("features", [])
    except RuntimeError as exc:
        log.warning("Could not fetch observations for %s: %s", station_id, exc)
        return []


def daily_max_min_from_observations(
    observations: list[dict], timezone_name: Optional[str]
) -> dict[str, dict]:
    """Groups raw hourly-ish observations into real local calendar days
    and computes the running max/min for each - the same aggregation
    Kalshi's own settlement (a DAILY high/low) requires. Uses the
    station's own local timezone (from fetch_station_metadata), not UTC,
    since a UTC calendar day and a station's local calendar day disagree
    for several hours every day - confirmed this matters live: KPHL's
    timezone is America/New_York, five hours behind UTC most of the year.
    """
    tz = ZoneInfo(timezone_name) if timezone_name else ZoneInfo("UTC")
    by_day: dict[str, list[float]] = defaultdict(list)

    for feature in observations:
        props = feature.get("properties", {})
        temp_c = (props.get("temperature") or {}).get("value")
        ts = props.get("timestamp")
        if temp_c is None or not ts:
            continue
        local_dt = datetime.fromisoformat(ts).astimezone(tz)
        local_date = local_dt.date().isoformat()
        by_day[local_date].append(_c_to_f(temp_c))

    return {
        day: {
            "observed_max_f": round(max(temps), 1),
            "observed_min_f": round(min(temps), 1),
            "sample_count": len(temps),
        }
        for day, temps in by_day.items()
    }


def normalize_forecast_rows(
    station_id: str, grid_data: dict, pulled_at: str
) -> list[dict]:
    props = grid_data.get("properties", {})
    max_values = (props.get("maxTemperature") or {}).get("values", [])
    min_values = (props.get("minTemperature") or {}).get("values", [])
    rows = []
    for kind, values in (("max", max_values), ("min", min_values)):
        for entry in values:
            valid_time = entry.get("validTime", "")
            target_date = valid_time.split("T")[0] if valid_time else None
            rows.append({
                "station_id": station_id,
                "target_date": target_date,
                "forecast_kind": kind,
                "forecast_value_f": _c_to_f(entry.get("value")),
                "pulled_at": pulled_at,
            })
    return rows


def write_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def run() -> dict:
    pulled_at = datetime.now(timezone.utc).isoformat()
    pulled_at_compact = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    summary = {
        "pulled_at": pulled_at,
        "target_station_count": len(TARGET_STATIONS),
        "stations_ok": 0,
        "stations_failed": [],
        "forecast_rows": 0,
        "observed_day_rows": 0,
    }

    log.info("=== NWS weather data ingestion run starting (%d target stations) ===",
              len(TARGET_STATIONS))

    forecast_rows: list[dict] = []
    observed_rows: list[dict] = []

    for i, station_id in enumerate(TARGET_STATIONS, 1):
        meta = fetch_station_metadata(station_id)
        if meta is None:
            summary["stations_failed"].append(station_id)
            continue

        grid_data = fetch_grid_forecast(meta["lat"], meta["lon"])
        if grid_data:
            new_rows = normalize_forecast_rows(station_id, grid_data, pulled_at)
            forecast_rows.extend(new_rows)

        observations = fetch_recent_observations(station_id)
        daily = daily_max_min_from_observations(observations, meta.get("timezone"))
        for day, stats in daily.items():
            observed_rows.append({
                "station_id": station_id,
                "observed_date": day,
                "observed_max_f": stats["observed_max_f"],
                "observed_min_f": stats["observed_min_f"],
                "sample_count": stats["sample_count"],
                "pulled_at": pulled_at,
            })

        raw_path = RAW_DIR / f"nws_{station_id}_{pulled_at_compact}.json"
        raw_path.parent.mkdir(parents=True, exist_ok=True)
        raw_path.write_text(json.dumps(
            {"station_meta": meta, "grid_data": grid_data, "observations": observations},
            indent=2,
        ))

        summary["stations_ok"] += 1
        if i % 5 == 0 or i == len(TARGET_STATIONS):
            log.info("Processed %d/%d target stations so far.", i, len(TARGET_STATIONS))

        time.sleep(NWS_PER_STATION_PAUSE_SECONDS)

    summary["forecast_rows"] = len(forecast_rows)
    summary["observed_day_rows"] = len(observed_rows)

    forecast_fields = ["station_id", "target_date", "forecast_kind", "forecast_value_f", "pulled_at"]
    observed_fields = ["station_id", "observed_date", "observed_max_f", "observed_min_f", "sample_count", "pulled_at"]

    write_csv(NORMALIZED_DIR / f"nws_forecast_{pulled_at_compact}.csv", forecast_rows, forecast_fields)
    write_csv(NORMALIZED_DIR / "nws_forecast_latest.csv", forecast_rows, forecast_fields)
    write_csv(NORMALIZED_DIR / f"nws_observed_daily_{pulled_at_compact}.csv", observed_rows, observed_fields)
    write_csv(NORMALIZED_DIR / "nws_observed_daily_latest.csv", observed_rows, observed_fields)

    log.info(
        "=== NWS ingestion run complete: %d/%d stations OK, %d forecast rows, "
        "%d observed-day rows (failed stations: %s) ===",
        summary["stations_ok"], len(TARGET_STATIONS), len(forecast_rows),
        len(observed_rows), summary["stations_failed"] or "none",
    )
    return summary


if __name__ == "__main__":
    result = run()
    print(json.dumps(result, indent=2))
