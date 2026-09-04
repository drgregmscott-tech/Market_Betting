"""
Session 3.1 — Kalshi Ingestion (Multi-Venue Data Ingestion)

WHAT THIS SCRIPT IS
--------------------
Pulls live market data from Kalshi's real-money exchange and normalizes it
into the common exchange-venue schema defined in schema_exchange.py, the
same defensive pattern Session 2.2's ingest_pickem.py established for the
pick'em platforms:
1. Pulls live data from Kalshi's public market-data endpoint.
2. Normalizes Kalshi's raw shape into the one common exchange schema.
3. Survives a bad response, an empty response, or a schema change WITHOUT
   crashing — logs the failure and continues.
4. Writes output so running the pipeline twice does not duplicate or
   corrupt any stored data (same idempotency pattern as ingest_pickem.py).
5. Logs every run to /logs/ingestion.log.

ACCESS — RESOLVED THIS SESSION (Open Decision #3, Kalshi half)
------------------------------------------------------------------
Confirmed live 2026-09-04, via direct unauthenticated pull against
production: Kalshi's market-data read endpoints require NO API key and NO
account. This is different from Track 1's two platforms in one important
way: Kalshi's public-data access is an OFFICIAL, documented part of
Kalshi's own API (https://docs.kalshi.com), not an undocumented endpoint
found by inspection. Kalshi is a CFTC-regulated exchange, so this script
is reading the same public market data Kalshi's own site displays, through
the same interface Kalshi tells developers to use — not a workaround.
Authenticated endpoints (placing orders, viewing a personal portfolio)
DO require an RSA-PSS-signed request and real API credentials — this
script never touches those, since Session 3.1 is read-only ingestion.

Base URL used: https://api.elections.kalshi.com/trade-api/v2 (Kalshi's own
docs note this is the general-purpose base despite the "elections"
subdomain name — confirmed covers weather/climate and all other
categories, not just elections).

Rate limits: not yet load-tested by this project. Kalshi's own docs
describe a tiered token-bucket system for authenticated trading traffic;
public read-only traffic has not been separately quantified here. This
script paginates conservatively (LIMIT_PER_PAGE below) and should be
watched during Session 3.1's own validation pass rather than assumed safe
at higher volume.

WHERE OUTPUT GOES
------------------
/data/exchange/raw/kalshi_<timestamp>.json — the exact, unmodified response
    for each page pulled, saved every run.
/data/exchange/normalized/kalshi_markets_<timestamp>.csv — one normalized
    snapshot per run.
/data/exchange/normalized/kalshi_latest.csv — always overwritten each run.

USAGE
-----
pip install requests --break-system-packages
python ingest_kalshi.py
"""

from __future__ import annotations

import json
import logging
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import requests

from schema_exchange import NORMALIZED_EXCHANGE_COLUMNS, NormalizedContract

# --------------------------------------------------------------------------
# Paths — all relative to the repo root. Run this script from the repo root
# (or adjust BASE_DIR) so these resolve correctly.
# --------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parents[2]
RAW_DIR = BASE_DIR / "data" / "exchange" / "raw"
NORMALIZED_DIR = BASE_DIR / "data" / "exchange" / "normalized"
LOG_PATH = BASE_DIR / "logs" / "ingestion.log"

KALSHI_BASE_URL = "https://api.elections.kalshi.com/trade-api/v2"
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
LIMIT_PER_PAGE = 1000  # Kalshi's own docs confirm 1000 is the real per-page
# maximum for this endpoint (1-1000 allowed, 100 is only the default when
# no limit is given). The first real run of this script used 200 and hit
# its MAX_PAGES safety cap after only 5,000 of Kalshi's real "tens of
# thousands" of open markets (per Kalshi's own API vendor docs) — raising
# this to the documented real maximum cuts the number of pages needed by
# 5x for the same total market count.
MAX_PAGES = 60  # hard safety cap — ~60,000 markets at the new page size;
# prevents a runaway loop if Kalshi's cursor pagination ever returns a
# cursor that never terminates. Raised from Session 3.1's first real run,
# which showed the true open-market count is meaningfully above the old
# 5,000-market cap.


def setup_logging() -> logging.Logger:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("ingest_kalshi")
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


# --------------------------------------------------------------------------
# Fetching — cursor-paginated, since Kalshi returns a bounded page per call
# with a "cursor" field for the next page (confirmed live 2026-09-04: an
# empty string cursor means no further pages).
# --------------------------------------------------------------------------
def _fetch_with_retries(url: str, params: Optional[dict] = None) -> dict:
    last_error = None
    for attempt in range(1, MAX_RETRIES + 2):
        try:
            response = requests.get(
                url, headers=HEADERS, params=params, timeout=REQUEST_TIMEOUT_SECONDS
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as exc:
            last_error = exc
            log.warning(
                "Attempt %d/%d failed for %s: %s",
                attempt,
                MAX_RETRIES + 1,
                url,
                exc,
            )
            if attempt <= MAX_RETRIES:
                time.sleep(RETRY_BACKOFF_SECONDS)
    raise RuntimeError(f"All attempts failed for {url}: {last_error}")


def fetch_kalshi_markets() -> list[dict]:
    """Pulls every open market across all pages. Returns the raw page
    payloads (not yet normalized) so save_raw_snapshot can archive exactly
    what Kalshi returned, same as ingest_pickem.py does for its platforms."""
    pages: list[dict] = []
    cursor = ""
    for page_num in range(1, MAX_PAGES + 1):
        params = {"status": "open", "limit": LIMIT_PER_PAGE}
        if cursor:
            params["cursor"] = cursor
        payload = _fetch_with_retries(KALSHI_MARKETS_ENDPOINT, params=params)
        pages.append(payload)
        cursor = payload.get("cursor") or ""
        log.info(
            "Kalshi page %d: %d markets, next cursor %s",
            page_num,
            len(payload.get("markets", [])),
            "present" if cursor else "empty (last page)",
        )
        if not cursor:
            break
    else:
        log.warning(
            "Kalshi pagination hit MAX_PAGES (%d) without an empty cursor — "
            "stopped early. Real market count may be larger than what was "
            "pulled this run.",
            MAX_PAGES,
        )
    return pages


# --------------------------------------------------------------------------
# Normalizer — defensive by design, same reasoning as ingest_pickem.py: a
# missing/renamed field on one row causes that row to be skipped (with a
# warning), not the whole run to fail.
# --------------------------------------------------------------------------
def normalize_kalshi(pages: list[dict], pulled_at: str) -> list[NormalizedContract]:
    rows: list[NormalizedContract] = []

    for page in pages:
        markets = page.get("markets")
        if not isinstance(markets, list):
            log.error(
                "Kalshi page missing expected 'markets' list — schema may "
                "have changed. Skipping this page for this run."
            )
            continue

        for record in markets:
            try:
                rows.append(
                    NormalizedContract(
                        platform="kalshi",
                        source_market_id=str(record.get("ticker")),
                        event_id=record.get("event_ticker"),
                        title=record.get("title"),
                        # Category is not present on the market object
                        # itself in this endpoint's response — a real,
                        # named gap, not a silent None. See
                        # schema_exchange.py's field notes.
                        category=None,
                        yes_bid=_to_float(record.get("yes_bid_dollars")),
                        yes_ask=_to_float(record.get("yes_ask_dollars")),
                        no_bid=_to_float(record.get("no_bid_dollars")),
                        no_ask=_to_float(record.get("no_ask_dollars")),
                        volume=_to_float(record.get("volume_fp")),
                        liquidity=_to_float(record.get("liquidity_dollars")),
                        close_time=record.get("close_time"),
                        status=record.get("status"),
                        pulled_at=pulled_at,
                    )
                )
            except Exception as exc:  # noqa: BLE001 — one bad record must
                # never take down the whole run.
                log.warning("Skipped one malformed Kalshi record: %s", exc)
                continue

    return rows


def _to_float(value) -> Optional[float]:
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


# --------------------------------------------------------------------------
# Output writers
# --------------------------------------------------------------------------
def save_raw_snapshot(pages: list[dict], pulled_at_compact: str) -> Path:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    out_path = RAW_DIR / f"kalshi_{pulled_at_compact}.json"
    out_path.write_text(json.dumps(pages, indent=2))
    return out_path


def write_normalized_csv(path: Path, rows: list[NormalizedContract]) -> None:
    import csv

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=NORMALIZED_EXCHANGE_COLUMNS)
        writer.writeheader()
        for row in rows:
            writer.writerow(row.as_row())


# --------------------------------------------------------------------------
# Main pipeline
# --------------------------------------------------------------------------
def run() -> dict:
    """Runs one full ingestion pass. Never raises — every failure mode is
    caught, logged, and reflected in the summary instead, same contract as
    ingest_pickem.py's run()."""
    pulled_at = datetime.now(timezone.utc).isoformat()
    pulled_at_compact = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    summary = {
        "pulled_at": pulled_at,
        "kalshi_rows": 0,
        "kalshi_ok": False,
    }

    log.info("=== Kalshi ingestion run starting ===")

    try:
        pages = fetch_kalshi_markets()
        save_raw_snapshot(pages, pulled_at_compact)
        rows = normalize_kalshi(pages, pulled_at)
        summary["kalshi_rows"] = len(rows)
        summary["kalshi_ok"] = True
        log.info("Kalshi: %d normalized rows across %d page(s)", len(rows), len(pages))
    except Exception as exc:  # noqa: BLE001 — an outage must not crash the
        # whole pipeline; write whatever we have (nothing, in this case).
        log.error("Kalshi ingestion failed for this run: %s", exc)
        rows = []

    snapshot_path = NORMALIZED_DIR / f"kalshi_markets_{pulled_at_compact}.csv"
    latest_path = NORMALIZED_DIR / "kalshi_latest.csv"
    write_normalized_csv(snapshot_path, rows)
    write_normalized_csv(latest_path, rows)  # overwrite, not append

    log.info(
        "=== Kalshi ingestion run complete: %d rows (%s) ===",
        len(rows),
        "OK" if summary["kalshi_ok"] else "FAILED",
    )

    summary["total_rows"] = len(rows)
    summary["snapshot_path"] = str(snapshot_path)
    return summary


if __name__ == "__main__":
    result = run()
    print(json.dumps(result, indent=2))
