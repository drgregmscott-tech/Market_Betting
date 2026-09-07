"""
Session 4.2 - Resolved-Market Sanity Check

WHAT THIS SCRIPT IS
--------------------
A one-time (re-runnable) check of weather_model.py's real accuracy
against ALREADY-RESOLVED Kalshi weather contracts - the roadmap's own
required validation item for Session 4.2 ("sanity-checked against at
least a handful of already-resolved historical Kalshi weather markets"),
which the earlier hand-verification (Atlanta/NYC rows, confirmed live)
did NOT cover - that check confirmed the FORMULA was wired correctly,
not that the MODEL is actually right about the real world.

WHY THIS DOESN'T NEED A NEW MULTI-DAY WAIT
-----------------------------------------------------------------------
This project already has real, committed, timestamped snapshots from
Session 4.1's original run (2026-09-06) - a real Kalshi weather snapshot
(kalshi_weather_markets_<timestamp>.csv) and a real NWS forecast snapshot
(nws_forecast_<timestamp>.csv) for a target date that has, by now, fully
passed and settled. This script:
1. Finds the OLDEST committed Kalshi weather snapshot and the OLDEST
   committed NWS forecast snapshot (Session 4.1's real originals).
2. Reconstructs, using weather_model.py's own real functions (imported
   directly, not re-implemented, so this is checking the actual model,
   not a copy of it), what probability the model would have assigned to
   each of those real contracts at the time.
3. Calls Kalshi's real GET /markets/{ticker} endpoint (read-only) for
   each of those same real market tickers to get the REAL, now-known
   settlement result.
4. Compares the model's real probability estimate against the real
   outcome for every contract that has actually settled by now.

METRICS USED (both standard, named, not invented for this project)
-----------------------------------------------------------------------
- Directional accuracy: did the model's probability lean toward the
  side that actually happened (prob_yes > 0.5 when the real result was
  YES, or < 0.5 when the real result was NO)?
- Brier score: the standard scoring rule for probabilistic forecasts -
  mean((prob_yes - actual_outcome)^2), where actual_outcome is 1 for YES
  and 0 for NO. Lower is better; 0 is a perfect forecast, 0.25 is what a
  constant "always guess 50%" forecast scores, so a real score under
  0.25 is real evidence the model beats a coin flip on these contracts.

WHERE OUTPUT GOES
------------------
/data/weather/backtest/resolved_market_check_<timestamp>.csv
Printed summary (accuracy, Brier score, contract count) to the console.

USAGE
-----
python weather_backtest_check.py
"""

from __future__ import annotations

import csv
import logging
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
from weather_model import (  # noqa: E402
    _forecast_kind_for_series, _parse_date, compute_probability,
    get_sigma_for_lead_day, load_real_error_by_lead_day,
)

BASE_DIR = Path(__file__).resolve().parents[2]
NORMALIZED_DIR = BASE_DIR / "data" / "weather" / "normalized"
BACKTEST_DIR = BASE_DIR / "data" / "weather" / "backtest"
LOG_PATH = BASE_DIR / "logs" / "estimation.log"

KALSHI_BASE_URL = "https://api.elections.kalshi.com/trade-api/v2"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json",
}
REQUEST_TIMEOUT_SECONDS = 15
PER_MARKET_PAUSE_SECONDS = 0.2


def setup_logging() -> logging.Logger:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("weather_backtest_check")
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


def _oldest_snapshot(pattern: str) -> Optional[Path]:
    files = sorted(
        p for p in NORMALIZED_DIR.glob(pattern)
        if "latest" not in p.name
    )
    return files[0] if files else None


def _parse_pulled_at_date(value: str):
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).date()
    except (ValueError, TypeError, AttributeError):
        return None


def fetch_real_market_result(ticker: str) -> Optional[dict]:
    """Read-only call to Kalshi's real /markets/{ticker} endpoint - same
    HEADERS/timeout pattern as this project's other Kalshi ingestion
    scripts. Returns the real market payload (includes 'status' and,
    once settled, 'result') or None on failure."""
    try:
        r = requests.get(
            f"{KALSHI_BASE_URL}/markets/{ticker}", headers=HEADERS,
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        r.raise_for_status()
        return r.json().get("market")
    except requests.exceptions.RequestException as exc:
        log.warning("Could not fetch real result for %s: %s", ticker, exc)
        return None


def run() -> dict:
    log.info("=== Resolved-market sanity check starting ===")

    kalshi_path = _oldest_snapshot("kalshi_weather_markets_*.csv")
    forecast_path = _oldest_snapshot("nws_forecast_*.csv")
    if kalshi_path is None or forecast_path is None:
        raise FileNotFoundError(
            "No committed historical snapshots found yet - this check "
            "needs at least one real, older Kalshi and NWS forecast "
            "snapshot already sitting in data/weather/normalized/."
        )
    log.info("Using historical Kalshi snapshot: %s", kalshi_path.name)
    log.info("Using historical forecast snapshot: %s", forecast_path.name)

    with kalshi_path.open("r", newline="", encoding="utf-8") as f:
        kalshi_rows = list(csv.DictReader(f))
    with forecast_path.open("r", newline="", encoding="utf-8") as f:
        forecast_index: dict[tuple[str, str, str], dict] = {}
        for row in csv.DictReader(f):
            key = (row["station_id"], row["target_date"], row["forecast_kind"])
            if key not in forecast_index:
                forecast_index[key] = row

    real_error_by_lead_day = load_real_error_by_lead_day()
    today = datetime.now(timezone.utc).date()

    checked_rows: list[dict] = []
    for row in kalshi_rows:
        target_date = _parse_date(row["target_date"])
        if target_date is None or target_date >= today:
            continue  # only check contracts whose real date has actually passed

        forecast_kind = _forecast_kind_for_series(row["series_ticker"])
        if forecast_kind is None:
            continue

        forecast_row = forecast_index.get((row["station_id"], row["target_date"], forecast_kind))
        if forecast_row is None or not forecast_row.get("forecast_value_f"):
            continue

        pulled_at_date = _parse_pulled_at_date(forecast_row["pulled_at"])
        if pulled_at_date is None:
            continue
        lead_days = (target_date - pulled_at_date).days
        if lead_days < 0:
            continue

        sigma_f, sigma_source = get_sigma_for_lead_day(lead_days, real_error_by_lead_day)
        if sigma_f is None:
            continue

        floor_strike = float(row["floor_strike"]) if row.get("floor_strike") else None
        cap_strike = float(row["cap_strike"]) if row.get("cap_strike") else None
        mean_f = float(forecast_row["forecast_value_f"])
        prob_yes = compute_probability(row["strike_type"], floor_strike, cap_strike, mean_f, sigma_f)
        if prob_yes is None:
            continue

        real_market = fetch_real_market_result(row["market_ticker"])
        time.sleep(PER_MARKET_PAUSE_SECONDS)
        if real_market is None:
            continue
        status = real_market.get("status")
        result = real_market.get("result")  # expected: "yes" or "no" once settled
        if status not in ("finalized", "settled") or result not in ("yes", "no"):
            continue  # not actually resolved yet - skip, don't guess

        actual_outcome = 1.0 if result == "yes" else 0.0
        directionally_correct = (prob_yes > 0.5 and result == "yes") or (prob_yes < 0.5 and result == "no")
        brier_component = (prob_yes - actual_outcome) ** 2

        checked_rows.append({
            "market_ticker": row["market_ticker"],
            "city_label": row["city_label"],
            "target_date": row["target_date"],
            "strike_type": row["strike_type"],
            "floor_strike": floor_strike,
            "cap_strike": cap_strike,
            "forecast_value_f": mean_f,
            "lead_days": lead_days,
            "model_prob_yes": round(prob_yes, 4),
            "sigma_source": sigma_source,
            "real_result": result,
            "directionally_correct": directionally_correct,
            "brier_component": round(brier_component, 4),
        })

    BACKTEST_DIR.mkdir(parents=True, exist_ok=True)
    out_path = BACKTEST_DIR / f"resolved_market_check_{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}.csv"
    fields = [
        "market_ticker", "city_label", "target_date", "strike_type", "floor_strike",
        "cap_strike", "forecast_value_f", "lead_days", "model_prob_yes", "sigma_source",
        "real_result", "directionally_correct", "brier_component",
    ]
    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for r in checked_rows:
            writer.writerow(r)

    n = len(checked_rows)
    summary = {"resolved_contracts_checked": n, "output_path": str(out_path)}
    if n > 0:
        accuracy = sum(1 for r in checked_rows if r["directionally_correct"]) / n
        brier = sum(r["brier_component"] for r in checked_rows) / n
        summary["directional_accuracy"] = round(accuracy, 4)
        summary["brier_score"] = round(brier, 4)
        summary["brier_score_vs_coin_flip_baseline_0_25"] = round(0.25 - brier, 4)
    else:
        summary["note"] = (
            "No contracts from the historical snapshot have actually "
            "settled yet on Kalshi's side, or none survived the real "
            "matching/lead-day checks above - not necessarily an error, "
            "but nothing to report yet."
        )

    log.info("=== Resolved-market sanity check complete: %s ===", summary)
    return summary


if __name__ == "__main__":
    import json
    print(json.dumps(run(), indent=2))
