"""
Session 3.1 — Kalshi Ingestion (Multi-Venue Data Ingestion)

WHAT THIS SCRIPT IS
--------------------
Pulls live market data from Kalshi's real-money exchange and normalizes it
into the common exchange-venue schema defined in schema_exchange.py, the
same defensive pattern Session 2.2's ingest_pickem.py established for the
pick'em platforms.

TARGETED PULL, NOT A FULL-CATALOG FIREHOSE — REAL REVERSAL THIS SESSION
-------------------------------------------------------------------------
Earlier versions of this script pulled Kalshi's ENTIRE open-market catalog
(GET /markets with no series filter) and paged as deep as practical hoping
the markets this project actually cares about would surface. A real run
showed why that doesn't work: Kalshi's catalog is dominated by combo/
multi-leg contracts (199,019 of 200,000 raw records in one real run), and
even paging 200,000 records deep turned up ZERO real weather markets —
they were apparently buried even further back by the sheer volume of
combo listings. Confirmed directly against Kalshi's own real,
unauthenticated `GET /series` endpoint (2026-09-04, 13,816 total series
returned, no API key required): Kalshi's series are organized into named
categories, and this project's actual in-scope categories per Session
0.1 — "Climate and Weather" (367 series) and "Commodities" (81 series) —
are a small, fully enumerable slice of the whole catalog. Rather than
searching for a needle in an ever-growing haystack, this script now:
1. Pulls the full series list once (GET /series, confirmed public).
2. Filters, client-side, to series whose category is "Climate and Weather"
   or "Commodities" — the two categories matching Session 0.1's actual
   edge thesis (see ROADMAP.md's Track 3 scoping). "Politics"/"Elections"
   (3,949 combined series) are DELIBERATELY deferred, not pulled here —
   Session 0.1's real decision was narrow, down-ballot races specifically,
   not politics broadly, and that narrower filter hasn't been built yet.
   Pulling all of Politics/Elections now would reintroduce the same kind
   of scope drift this project has caught and corrected before.
3. For each matching series (~448), pulls its open markets directly via
   GET /markets?series_ticker=<ticker>&status=open — a small, targeted
   call per series, rather than paging through the unfiltered firehose.

This is a real, deliberate scope narrowing WITHIN Kalshi ingestion, logged
explicitly as such — not a silent one. It does not narrow the PROJECT's
scope (Politics/Elections remains on the roadmap, just not built yet).

ACCESS — RESOLVED THIS SESSION (Open Decision #3, Kalshi half)
------------------------------------------------------------------
Confirmed live 2026-09-04: both GET /series and GET /markets require NO
API key and NO account. This is an OFFICIAL, documented part of Kalshi's
own API (https://docs.kalshi.com), not an undocumented endpoint found by
inspection. Authenticated endpoints (placing orders, viewing a personal
portfolio) DO require an RSA-PSS-signed request and real API credentials
— this script never touches those, since Session 3.1 is read-only
ingestion.

Base URL used: https://api.elections.kalshi.com/trade-api/v2 (Kalshi's own
docs note this is the general-purpose base despite the "elections"
subdomain name).

WHERE OUTPUT GOES
------------------
/data/exchange/raw/kalshi_<timestamp>.json — the exact, unmodified series
    list and per-series market responses pulled, saved every run.
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
import re
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
KALSHI_SERIES_ENDPOINT = f"{KALSHI_BASE_URL}/series"
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

# Real Kalshi category names, confirmed live 2026-09-04 against GET
# /series (13,816 total series). Matches Session 0.1's Track 3 scope
# ("Climate/Commodities") directly — see this file's module docstring for
# why Politics/Elections is deliberately not included yet.
TARGET_CATEGORIES = ["Climate and Weather", "Commodities"]


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
# Fetching
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


def fetch_target_series_tickers():
    """Pulls Kalshi's full series list once and filters, client-side, to
    this project's target categories. Confirmed live 2026-09-04: GET
    /series returns ALL series in one call (no pagination needed — 13,816
    returned directly), each with a real 'category' field, so no category
    query-parameter guessing is needed. Returns (matching_tickers,
    all_series) — all_series is kept so run() can build a ticker->category
    map without a second API call."""
    payload = _fetch_with_retries(KALSHI_SERIES_ENDPOINT)
    all_series = payload.get("series", payload if isinstance(payload, list) else [])
    if not isinstance(all_series, list):
        raise RuntimeError(
            "GET /series response was not in the expected shape — schema "
            "may have changed."
        )

    matching_tickers = [
        s.get("ticker")
        for s in all_series
        if s.get("category") in TARGET_CATEGORIES and s.get("ticker")
    ]
    log.info(
        "Series discovery: %d total series pulled, %d match target "
        "categories %s",
        len(all_series),
        len(matching_tickers),
        TARGET_CATEGORIES,
    )
    return matching_tickers, all_series


def fetch_markets_for_series(tickers: list[str]) -> list[dict]:
    """Pulls open markets for each target series individually. Each
    series's failure is isolated — one bad/unreachable series must not
    lose markets already pulled for the others, same 'don't discard real
    partial progress' principle applied to ingest_polymarket.py's page-
    level failures earlier this session."""
    pages: list[dict] = []
    failed_tickers: list[str] = []

    for i, ticker in enumerate(tickers, 1):
        try:
            payload = _fetch_with_retries(
                KALSHI_MARKETS_ENDPOINT,
                params={"series_ticker": ticker, "status": "open"},
            )
            market_count = len(payload.get("markets", []))
            pages.append(payload)
            if i % 50 == 0 or i == len(tickers):
                log.info(
                    "Fetched markets for %d/%d target series so far "
                    "(most recent: %s, %d markets)",
                    i,
                    len(tickers),
                    ticker,
                    market_count,
                )
        except RuntimeError as exc:
            failed_tickers.append(ticker)
            log.warning("Failed to fetch markets for series %s: %s", ticker, exc)
            continue

    if failed_tickers:
        log.warning(
            "%d of %d target series could not be fetched this run: %s",
            len(failed_tickers),
            len(tickers),
            failed_tickers[:20],  # cap the printed list — could be long
        )

    return pages


# --------------------------------------------------------------------------
# Normalizer — defensive by design, same reasoning as ingest_pickem.py: a
# missing/renamed field on one row causes that row to be skipped (with a
# warning), not the whole run to fail.
# --------------------------------------------------------------------------
_COMBO_LEG_PATTERN = re.compile(r"^\s*(yes|no)\s", re.IGNORECASE)


def _is_combo_title(title: Optional[str]) -> bool:
    """Detects Kalshi's multi-leg combo-contract titles by STRUCTURE
    (see this project's SESSION_LOG.md for the full discovery story of
    why market_type alone can't be used for this). Kept as a defensive
    check even with the new targeted series pull — Climate and Weather/
    Commodities are not known to carry combo-style contracts, but this
    costs nothing to leave in place in case that assumption is ever
    wrong, and it's cheaper to filter defensively than to assume a
    category is combo-free without having checked every series in it."""
    if not title:
        return False
    segments = title.split(",")
    leg_like_segments = sum(1 for seg in segments if _COMBO_LEG_PATTERN.match(seg))
    return leg_like_segments >= 2


def normalize_kalshi(pages: list[dict], pulled_at: str) -> list[NormalizedContract]:
    rows: list[NormalizedContract] = []
    skipped_combo_titles = 0

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
                title = record.get("title")
                if _is_combo_title(title):
                    skipped_combo_titles += 1
                    continue

                rows.append(
                    NormalizedContract(
                        platform="kalshi",
                        source_market_id=str(record.get("ticker")),
                        event_id=record.get("event_ticker"),
                        title=title,
                        # Category IS now known (this run only pulled
                        # target-category series), filled in by the
                        # caller in run() via a ticker->category map, not
                        # guessed here — the raw market object itself
                        # still doesn't carry a category field.
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

    if skipped_combo_titles:
        log.warning(
            "Filtered out %d Kalshi record(s) whose title looks like a "
            "multi-leg combo listing, not a single real-world question.",
            skipped_combo_titles,
        )

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
def save_raw_snapshot(
    series_list: list[dict], market_pages: list[dict], pulled_at_compact: str
) -> Path:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    out_path = RAW_DIR / f"kalshi_{pulled_at_compact}.json"
    out_path.write_text(
        json.dumps(
            {"all_series": series_list, "market_pages": market_pages}, indent=2
        )
    )
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
        "kalshi_target_series_count": 0,
        "kalshi_raw_records_pulled": 0,
        "kalshi_combo_records_filtered_out": 0,
        "kalshi_rows_kept": 0,
        "kalshi_ok": False,
    }

    log.info(
        "=== Kalshi ingestion run starting (Climate and Weather + Commodities) ==="
    )

    try:
        target_tickers, all_series = fetch_target_series_tickers()
        summary["kalshi_target_series_count"] = len(target_tickers)

        # Map ticker -> category, so each row can be tagged with its real
        # category even though the /markets response itself doesn't
        # include one — filled in below, not guessed.
        category_by_ticker = {
            s.get("ticker"): s.get("category")
            for s in all_series
            if s.get("ticker") in target_tickers
        }

        market_pages = fetch_markets_for_series(target_tickers)
        save_raw_snapshot(all_series, market_pages, pulled_at_compact)

        raw_count = sum(len(page.get("markets", [])) for page in market_pages)
        rows = normalize_kalshi(market_pages, pulled_at)

        # Fill in the real category per row using the series->category
        # map built above (matched via event_ticker's series prefix,
        # since the market object itself has no category field).
        for row in rows:
            for ticker, category in category_by_ticker.items():
                if row.event_id and row.event_id.startswith(ticker):
                    row.category = category
                    break

        summary["kalshi_raw_records_pulled"] = raw_count
        summary["kalshi_combo_records_filtered_out"] = raw_count - len(rows)
        summary["kalshi_rows_kept"] = len(rows)
        summary["kalshi_ok"] = True
        log.info(
            "Kalshi: %d target series, %d raw records pulled, %d filtered "
            "out as combo listings, %d single-question rows kept",
            len(target_tickers),
            raw_count,
            raw_count - len(rows),
            len(rows),
        )
    except Exception as exc:  # noqa: BLE001 — an outage must not crash the
        # whole pipeline; write whatever we have (nothing, in this case).
        log.error("Kalshi ingestion failed for this run: %s", exc)
        rows = []

    snapshot_path = NORMALIZED_DIR / f"kalshi_markets_{pulled_at_compact}.csv"
    latest_path = NORMALIZED_DIR / "kalshi_latest.csv"
    write_normalized_csv(snapshot_path, rows)
    write_normalized_csv(latest_path, rows)  # overwrite, not append

    log.info(
        "=== Kalshi ingestion run complete: %d single-question rows kept (%s) ===",
        len(rows),
        "OK" if summary["kalshi_ok"] else "FAILED",
    )

    summary["snapshot_path"] = str(snapshot_path)
    return summary


if __name__ == "__main__":
    result = run()
    print(json.dumps(result, indent=2))
