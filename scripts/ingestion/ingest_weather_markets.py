"""
Session 4.1 - Weather Market Ingestion (Kalshi structured threshold data)

WHAT THIS SCRIPT IS
--------------------
Pulls Kalshi's real weather-threshold markets - the specific subset of
Session 3.1's "Climate and Weather" category series that ask a genuine
numeric temperature question with a structural, computable answer (e.g.
"Will the maximum temperature be >85 on Sep 7, 2026?") - and normalizes
them into schema_weather.py's shape, joinable to this project's NWS data
(ingest_nws_weather_data.py) on (station_id, target_date).

WHY THIS IS A SEPARATE SCRIPT FROM ingest_kalshi.py, NOT A SHARED PULL
-----------------------------------------------------------------------
ingest_kalshi.py (Session 3.1) already pulls every Climate and Weather +
Commodities series for arbitrage's needs (Track 2 only needs the tradable
price, so its schema doesn't carry floor_strike/cap_strike/target_date).
Re-deriving those fields from ingest_kalshi.py's already-normalized
output would mean re-parsing a ticker string a second time after the
information was already discarded once - fragile and duplicative. This
script instead pulls fresh from Kalshi's live market endpoint, capturing
the structured strike fields directly at the source, the one time they
are available in their original, structured form.

STRUCTURAL FILTER - NOT EVERY "Climate and Weather" SERIES QUALIFIES
-----------------------------------------------------------------------
Confirmed live 2026-09-06: Kalshi's "Climate and Weather" category (369
series) includes things with no computable numeric threshold at all (e.g.
"Keystone Resort Opening," "Number of tropical storms"). This script
targets only series whose ticker matches Kalshi's real KXHIGH*/KXLOW*
structural naming pattern for daily temperature threshold questions (104
series found live), the same "check the structure, don't guess from a
category label alone" approach ingest_kalshi.py already uses for combo
contracts and down-ballot races.

Of those 104, only series mapped to a real NWS station in station_map.py
are kept - see that file's own docstring for the full international-
exclusion reasoning (20 series excluded, confirmed live) and the two
named, unresolved station gaps (Houston, Chicago).

WHERE OUTPUT GOES
------------------
/data/weather/raw/kalshi_weather_<timestamp>.json
/data/weather/normalized/kalshi_weather_markets_<timestamp>.csv
/data/weather/normalized/kalshi_weather_latest.csv (overwritten each run)

USAGE
-----
pip install requests --break-system-packages
python ingest_weather_markets.py
"""

from __future__ import annotations

import json
import logging
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import requests

from schema_weather import NORMALIZED_WEATHER_COLUMNS, NormalizedWeatherMarket
from station_map import station_for_series, INTERNATIONAL_SERIES_OUT_OF_SCOPE

BASE_DIR = Path(__file__).resolve().parents[2]
RAW_DIR = BASE_DIR / "data" / "weather" / "raw"
NORMALIZED_DIR = BASE_DIR / "data" / "weather" / "normalized"
LOG_PATH = BASE_DIR / "logs" / "ingestion.log"

KALSHI_BASE_URL = "https://api.elections.kalshi.com/trade-api/v2"
KALSHI_SERIES_LIST_ENDPOINT = f"{KALSHI_BASE_URL}/series"
KALSHI_SERIES_DETAIL_ENDPOINT = f"{KALSHI_BASE_URL}/series"  # + /{ticker}
KALSHI_MARKETS_ENDPOINT = f"{KALSHI_BASE_URL}/markets"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json",
}

MAX_RETRIES = 2
RETRY_BACKOFF_SECONDS = 3
REQUEST_TIMEOUT_SECONDS = 15

# Same reasoning as ingest_kalshi.py's KALSHI_PER_SERIES_PAUSE_SECONDS -
# this script makes one series-detail + one markets call per target
# series (roughly 2x ~84 real requests for the confirmed-mapped series
# below). A fixed pause keeps this well clear of Kalshi's real (unpublished)
# rate limits on an unattended scheduled run.
KALSHI_PER_SERIES_PAUSE_SECONDS = 0.2

TARGET_CATEGORY = "Climate and Weather"

# Structural ticker pattern for Kalshi's daily temperature threshold
# series, confirmed live 2026-09-06 against the real 369-series Climate
# and Weather category (104 series matched).
_TEMP_SERIES_TICKER_PATTERN = re.compile(r"^KX(HIGH|LOW)T?[A-Z]+$")

# Structural pattern for the market-ticker's embedded target date, e.g.
# "KXHIGHPHIL-26SEP07-T85" -> "26SEP07". Confirmed live 2026-09-06.
_MARKET_DATE_PATTERN = re.compile(r"-(\d{2}[A-Z]{3}\d{2})-")

_MONTH_ABBR = {
    "JAN": "01", "FEB": "02", "MAR": "03", "APR": "04", "MAY": "05",
    "JUN": "06", "JUL": "07", "AUG": "08", "SEP": "09", "OCT": "10",
    "NOV": "11", "DEC": "12",
}


def setup_logging() -> logging.Logger:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("ingest_weather_markets")
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


def _to_float(value) -> Optional[float]:
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def parse_target_date(market_ticker: str) -> Optional[str]:
    """'KXHIGHPHIL-26SEP07-T85' -> '2026-09-07'. Returns None (and logs a
    warning) if the ticker doesn't match the expected structure, rather
    than silently guessing a date."""
    match = _MARKET_DATE_PATTERN.search(market_ticker)
    if not match:
        return None
    raw = match.group(1)  # e.g. "26SEP07"
    year, month_abbr, day = raw[:2], raw[2:5], raw[5:7]
    month = _MONTH_ABBR.get(month_abbr)
    if not month:
        return None
    return f"20{year}-{month}-{day}"


def fetch_target_series() -> list[dict]:
    """Pulls Kalshi's full series list and filters, client-side, to the
    real structural temperature-threshold pattern - same approach as
    ingest_kalshi.py's classify_down_ballot(), applied here to weather."""
    payload = _fetch_with_retries(KALSHI_SERIES_LIST_ENDPOINT)
    all_series = payload.get("series", payload if isinstance(payload, list) else [])
    matched = [
        s for s in all_series
        if s.get("category") == TARGET_CATEGORY
        and s.get("ticker")
        and _TEMP_SERIES_TICKER_PATTERN.match(s["ticker"])
    ]
    log.info(
        "Series discovery: %d total series, %d match the temperature-"
        "threshold structural pattern within Climate and Weather.",
        len(all_series), len(matched),
    )
    return matched


def fetch_series_settlement_source(ticker: str) -> tuple[Optional[str], Optional[str]]:
    """One extra call per series to GET /series/{ticker} for its real
    settlement_sources field - not returned by the bulk /series list
    call. Returns (name, url), (None, None) if missing/malformed."""
    try:
        payload = _fetch_with_retries(f"{KALSHI_SERIES_DETAIL_ENDPOINT}/{ticker}")
        sources = payload.get("series", {}).get("settlement_sources") or []
        if sources:
            return sources[0].get("name"), sources[0].get("url")
    except RuntimeError as exc:
        log.warning("Could not fetch settlement source for series %s: %s", ticker, exc)
    return None, None


def fetch_markets_for_series(ticker: str) -> list[dict]:
    try:
        payload = _fetch_with_retries(
            KALSHI_MARKETS_ENDPOINT, params={"series_ticker": ticker, "status": "open"}
        )
        return payload.get("markets", [])
    except RuntimeError as exc:
        log.warning("Failed to fetch markets for series %s: %s", ticker, exc)
        return []


def normalize_rows(
    series_ticker: str,
    city_label: str,
    station_id: str,
    settlement_name: Optional[str],
    settlement_url: Optional[str],
    markets: list[dict],
    pulled_at: str,
) -> list[NormalizedWeatherMarket]:
    rows: list[NormalizedWeatherMarket] = []
    for m in markets:
        market_ticker = m.get("ticker")
        if not market_ticker:
            continue
        target_date = parse_target_date(market_ticker)
        if target_date is None:
            log.warning(
                "Skipped market %s - ticker did not match the expected "
                "date structure.", market_ticker,
            )
            continue
        rows.append(
            NormalizedWeatherMarket(
                series_ticker=series_ticker,
                market_ticker=market_ticker,
                city_label=city_label,
                station_id=station_id,
                target_date=target_date,
                strike_type=m.get("strike_type"),
                floor_strike=_to_float(m.get("floor_strike")),
                cap_strike=_to_float(m.get("cap_strike")),
                settlement_source_name=settlement_name,
                settlement_source_url=settlement_url,
                yes_bid=_to_float(m.get("yes_bid_dollars")),
                yes_ask=_to_float(m.get("yes_ask_dollars")),
                no_bid=_to_float(m.get("no_bid_dollars")),
                no_ask=_to_float(m.get("no_ask_dollars")),
                yes_ask_size=_to_float(m.get("yes_ask_size_fp")),
                yes_bid_size=_to_float(m.get("yes_bid_size_fp")),
                volume=_to_float(m.get("volume_fp")),
                liquidity=_to_float(m.get("liquidity_dollars")),
                close_time=m.get("close_time"),
                status=m.get("status"),
                pulled_at=pulled_at,
            )
        )
    return rows


def write_normalized_csv(path: Path, rows: list[NormalizedWeatherMarket]) -> None:
    import csv
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=NORMALIZED_WEATHER_COLUMNS)
        writer.writeheader()
        for row in rows:
            writer.writerow(row.as_row())


def run() -> dict:
    pulled_at = datetime.now(timezone.utc).isoformat()
    pulled_at_compact = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    summary = {
        "pulled_at": pulled_at,
        "temp_series_found": 0,
        "international_series_skipped": 0,
        "unmapped_series_skipped": 0,
        "series_ingested": 0,
        "rows_kept": 0,
        "ok": False,
    }

    log.info("=== Weather market ingestion run starting ===")
    all_raw: dict[str, list[dict]] = {}
    rows: list[NormalizedWeatherMarket] = []

    try:
        target_series = fetch_target_series()
        summary["temp_series_found"] = len(target_series)

        for i, s in enumerate(target_series, 1):
            ticker = s["ticker"]
            title = s.get("title") or ticker

            if ticker in INTERNATIONAL_SERIES_OUT_OF_SCOPE:
                summary["international_series_skipped"] += 1
                continue

            station_id = station_for_series(ticker)
            if station_id is None:
                summary["unmapped_series_skipped"] += 1
                log.warning(
                    "Series %s ('%s') is a real temperature-threshold "
                    "series but has no confirmed station mapping in "
                    "station_map.py - skipped, not guessed.", ticker, title,
                )
                continue

            settlement_name, settlement_url = fetch_series_settlement_source(ticker)
            time.sleep(KALSHI_PER_SERIES_PAUSE_SECONDS)
            markets = fetch_markets_for_series(ticker)
            time.sleep(KALSHI_PER_SERIES_PAUSE_SECONDS)

            all_raw[ticker] = markets
            series_rows = normalize_rows(
                ticker, title, station_id, settlement_name, settlement_url,
                markets, pulled_at,
            )
            rows.extend(series_rows)
            summary["series_ingested"] += 1

            if i % 20 == 0 or i == len(target_series):
                log.info("Processed %d/%d target series so far.", i, len(target_series))

        summary["rows_kept"] = len(rows)
        summary["ok"] = True
        log.info(
            "Weather markets: %d temperature series found, %d international "
            "(skipped, out of scope), %d unmapped (skipped, named gap), "
            "%d series ingested, %d market rows kept.",
            summary["temp_series_found"], summary["international_series_skipped"],
            summary["unmapped_series_skipped"], summary["series_ingested"], len(rows),
        )
    except Exception as exc:  # noqa: BLE001
        log.error("Weather market ingestion failed for this run: %s", exc)

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    raw_path = RAW_DIR / f"kalshi_weather_{pulled_at_compact}.json"
    raw_path.write_text(json.dumps(all_raw, indent=2))

    snapshot_path = NORMALIZED_DIR / f"kalshi_weather_markets_{pulled_at_compact}.csv"
    latest_path = NORMALIZED_DIR / "kalshi_weather_latest.csv"
    write_normalized_csv(snapshot_path, rows)
    write_normalized_csv(latest_path, rows)

    log.info("=== Weather market ingestion run complete (%s) ===", "OK" if summary["ok"] else "FAILED")
    summary["snapshot_path"] = str(snapshot_path)
    return summary


if __name__ == "__main__":
    result = run()
    print(json.dumps(result, indent=2))
