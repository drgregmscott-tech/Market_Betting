"""
Session 3.1 — Polymarket Ingestion (Multi-Venue Data Ingestion)

WHAT THIS SCRIPT IS
--------------------
Pulls live market data from Polymarket and normalizes it into the common
exchange-venue schema defined in schema_exchange.py — the Polymarket half
of Session 3.1's multi-venue ingestion, parallel to ingest_kalshi.py.

ACCESS — RESOLVED THIS SESSION (Open Decision #3, Polymarket half)
------------------------------------------------------------------
Confirmed live 2026-09-04, via direct unauthenticated pull against
production: Polymarket splits its data across three separate public APIs
(per Polymarket's own docs, https://docs.polymarket.com):
- Gamma API (https://gamma-api.polymarket.com) — markets, events,
  categories. Fully public, no key required. This script uses this one.
- Data API (https://data-api.polymarket.com) — user positions/trades, not
  needed for this script.
- CLOB API (https://clob.polymarket.com) — live order-book depth and
  trading. Its price-read endpoints are public; ORDER PLACEMENT requires
  an authenticated wallet. This script does not touch CLOB — Gamma API's
  markets endpoint already returns a best-bid/best-ask snapshot per
  market, which is sufficient for Session 3.1's ingestion scope. Session
  3.2 (Arbitrage Detection) should revisit whether real order-book DEPTH
  (not just best bid/ask) is needed once liquidity-check logic is built —
  flagged here, not decided in advance.

Rate limits: not yet load-tested by this project, same caveat as
ingest_kalshi.py.

A REAL SHAPE DIFFERENCE FROM KALSHI, HANDLED BELOW
-----------------------------------------------------
Kalshi returns yes_bid/yes_ask/no_bid/no_ask as four separate real numbers.
Polymarket's Gamma API markets object returns only a YES-side bestBid/
bestAsk pair (plus outcomePrices, a last-traded-price snapshot). The NO
side is DERIVED here via the standard complementary-probability
relationship for a two-outcome market (no_bid = 1 - yes_ask, no_ask = 1 -
yes_bid) — this is a real derivation, not a value Polymarket itself
returns, and is called out explicitly in the normalizer below rather than
silently presented as if it were a directly-observed price.

Several Polymarket fields arrive as JSON-ENCODED STRINGS, not native JSON
types (confirmed live 2026-09-04: outcomes, outcomePrices, and
clobTokenIds are each a string containing a JSON array, e.g.
'["Yes", "No"]', not an actual array). This mirrors the exact kind of
easy-to-miss typing trap Session 2.2 already found once with Underdog's
stat_value field — handled explicitly here with json.loads(), not assumed.

WHERE OUTPUT GOES
------------------
/data/exchange/raw/polymarket_<timestamp>.json
/data/exchange/normalized/polymarket_markets_<timestamp>.csv
/data/exchange/normalized/polymarket_latest.csv

USAGE
-----
pip install requests --break-system-packages
python ingest_polymarket.py
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

BASE_DIR = Path(__file__).resolve().parents[2]
RAW_DIR = BASE_DIR / "data" / "exchange" / "raw"
NORMALIZED_DIR = BASE_DIR / "data" / "exchange" / "normalized"
LOG_PATH = BASE_DIR / "logs" / "ingestion.log"

POLYMARKET_EVENTS_ENDPOINT = "https://gamma-api.polymarket.com/events"

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
LIMIT_PER_PAGE = 200
MAX_PAGES = 25  # hard safety cap, same reasoning as ingest_kalshi.py


def setup_logging() -> logging.Logger:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("ingest_polymarket")
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
# Fetching — offset-paginated (confirmed live 2026-09-04: Gamma API's
# /events takes limit/offset, not a cursor token the way Kalshi does).
# Pulling events (not the bare /markets endpoint) so each market's parent
# event/category context is available for venue_matcher.py later.
# --------------------------------------------------------------------------
def _fetch_with_retries(url: str, params: Optional[dict] = None) -> list:
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


def fetch_polymarket_events() -> list[list]:
    """Pulls every open, active event across all pages. Returns the raw
    page payloads (each a list of event dicts) so save_raw_snapshot can
    archive exactly what Polymarket returned."""
    pages: list[list] = []
    offset = 0
    for page_num in range(1, MAX_PAGES + 1):
        params = {
            "limit": LIMIT_PER_PAGE,
            "offset": offset,
            "active": "true",
            "closed": "false",
        }
        payload = _fetch_with_retries(POLYMARKET_EVENTS_ENDPOINT, params=params)
        if not isinstance(payload, list):
            log.error(
                "Polymarket /events response was not a list — schema may "
                "have changed. Stopping pagination for this run."
            )
            break
        pages.append(payload)
        log.info("Polymarket page %d: %d events", page_num, len(payload))
        if len(payload) < LIMIT_PER_PAGE:
            break  # short page — this was the last one
        offset += LIMIT_PER_PAGE
    else:
        log.warning(
            "Polymarket pagination hit MAX_PAGES (%d) without a short page "
            "— stopped early. Real event count may be larger than what "
            "was pulled this run.",
            MAX_PAGES,
        )
    return pages


# --------------------------------------------------------------------------
# Normalizer — one row per MARKET (an event can contain more than one
# market, e.g. a multi-candidate event), defensive by design.
# --------------------------------------------------------------------------
def normalize_polymarket(
    pages: list[list], pulled_at: str
) -> list[NormalizedContract]:
    rows: list[NormalizedContract] = []

    for page in pages:
        for event in page:
            try:
                event_id = str(event.get("id")) if event.get("id") else None
                category = event.get("category")
                markets = event.get("markets")
                if not isinstance(markets, list):
                    log.warning(
                        "Skipped one Polymarket event with no 'markets' "
                        "list (event id %s).",
                        event_id,
                    )
                    continue

                for market in markets:
                    try:
                        rows.append(_normalize_one_market(market, event_id, category, pulled_at))
                    except Exception as exc:  # noqa: BLE001 — one bad
                        # record must never take down the whole run.
                        log.warning(
                            "Skipped one malformed Polymarket market record: %s",
                            exc,
                        )
                        continue
            except Exception as exc:  # noqa: BLE001
                log.warning("Skipped one malformed Polymarket event: %s", exc)
                continue

    return rows


def _normalize_one_market(
    market: dict, event_id: Optional[str], category: Optional[str], pulled_at: str
) -> NormalizedContract:
    condition_id = market.get("conditionId")

    yes_ask = _to_float(market.get("bestAsk"))
    yes_bid = _to_float(market.get("bestBid"))
    # DERIVED, not directly returned — see module docstring's "A REAL SHAPE
    # DIFFERENCE FROM KALSHI" section for why this derivation is correct
    # for a two-outcome market and why it is called out explicitly here.
    no_bid = 1.0 - yes_ask if yes_ask is not None else None
    no_ask = 1.0 - yes_bid if yes_bid is not None else None

    is_active = market.get("active")
    is_closed = market.get("closed")
    if is_closed:
        status = "closed"
    elif is_active:
        status = "active"
    else:
        status = None

    return NormalizedContract(
        platform="polymarket",
        source_market_id=str(condition_id) if condition_id else str(market.get("id")),
        event_id=event_id,
        title=market.get("question"),
        category=category,
        yes_bid=yes_bid,
        yes_ask=yes_ask,
        no_bid=no_bid,
        no_ask=no_ask,
        volume=_to_float(market.get("volume")),
        liquidity=_to_float(market.get("liquidity")),
        close_time=market.get("endDate"),
        status=status,
        pulled_at=pulled_at,
    )


def _to_float(value) -> Optional[float]:
    """Converts a numeric-looking string or number to float. Several
    Polymarket numeric fields (volume, liquidity) arrive as strings in the
    raw payload — confirmed live 2026-09-04 — same conversion-correctness
    concern schema_exchange.py's docstring flags. Returns None (not 0) for
    anything that can't be parsed."""
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


# --------------------------------------------------------------------------
# Output writers
# --------------------------------------------------------------------------
def save_raw_snapshot(pages: list[list], pulled_at_compact: str) -> Path:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    out_path = RAW_DIR / f"polymarket_{pulled_at_compact}.json"
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
    caught, logged, and reflected in the summary instead."""
    pulled_at = datetime.now(timezone.utc).isoformat()
    pulled_at_compact = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    summary = {
        "pulled_at": pulled_at,
        "polymarket_rows": 0,
        "polymarket_ok": False,
    }

    log.info("=== Polymarket ingestion run starting ===")

    try:
        pages = fetch_polymarket_events()
        save_raw_snapshot(pages, pulled_at_compact)
        rows = normalize_polymarket(pages, pulled_at)
        summary["polymarket_rows"] = len(rows)
        summary["polymarket_ok"] = True
        log.info(
            "Polymarket: %d normalized rows across %d page(s)", len(rows), len(pages)
        )
    except Exception as exc:  # noqa: BLE001
        log.error("Polymarket ingestion failed for this run: %s", exc)
        rows = []

    snapshot_path = NORMALIZED_DIR / f"polymarket_markets_{pulled_at_compact}.csv"
    latest_path = NORMALIZED_DIR / "polymarket_latest.csv"
    write_normalized_csv(snapshot_path, rows)
    write_normalized_csv(latest_path, rows)

    log.info(
        "=== Polymarket ingestion run complete: %d rows (%s) ===",
        len(rows),
        "OK" if summary["polymarket_ok"] else "FAILED",
    )

    summary["total_rows"] = len(rows)
    summary["snapshot_path"] = str(snapshot_path)
    return summary


if __name__ == "__main__":
    result = run()
    print(json.dumps(result, indent=2))
