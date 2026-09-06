"""
Session 3.1 / 3.1b / 3.2 - Kalshi Ingestion (Multi-Venue Data Ingestion +
Narrow Down-Ballot Politics/Elections + Arbitrage Detection Logic support)

WHAT THIS SCRIPT IS
--------------------
Pulls live market data from Kalshi's real-money exchange and normalizes it
into the common exchange-venue schema defined in schema_exchange.py, the
same defensive pattern Session 2.2's ingest_pickem.py established for the
pick'em platforms.

TARGETED PULL, NOT A FULL-CATALOG FIREHOSE - REAL REVERSAL FROM SESSION 3.1
-------------------------------------------------------------------------
Earlier versions of this script pulled Kalshi's ENTIRE open-market catalog
(GET /markets with no series filter) and paged as deep as practical hoping
the markets this project actually cares about would surface. A real run
showed why that doesn't work: Kalshi's catalog is dominated by combo/
multi-leg contracts (199,019 of 200,000 raw records in one real run), and
even paging 200,000 records deep turned up ZERO real weather markets -
they were apparently buried even further back by the sheer volume of
combo listings. Confirmed directly against Kalshi's own real,
unauthenticated `GET /series` endpoint (2026-09-04, 13,816 total series
returned, no API key required): Kalshi's series are organized into named
categories, and this project's actual in-scope categories per Session
0.1 - "Climate and Weather" (367 series) and "Commodities" (81 series) -
are a small, fully enumerable slice of the whole catalog. Rather than
searching for a needle in an ever-growing haystack, this script now:
1. Pulls the full series list once (GET /series, confirmed public).
2. Filters, client-side, to series whose category is "Climate and Weather"
   or "Commodities" - the two categories matching Session 0.1's actual
   edge thesis (see ROADMAP.md's Track 3 scoping).
3. For each matching series (~448), pulls its open markets directly via
   GET /markets?series_ticker=<ticker>&status=open - a small, targeted
   call per series, rather than paging through the unfiltered firehose.

This is a real, deliberate scope narrowing WITHIN Kalshi ingestion, logged
explicitly as such - not a silent one.

SESSION 3.1b - NARROW DOWN-BALLOT POLITICS/ELECTIONS
-------------------------------------------------------------------------
Session 3.1 deliberately left Kalshi's "Politics" (2,296 series, confirmed
live 2026-09-04) and "Elections" (1,704 series, confirmed live) categories
unpulled - Session 0.1's real scope decision was narrow, down-ballot races
specifically (individual U.S. House seats and individual state-legislature
seats), not politics or national elections broadly. Pulling either category
whole would have reintroduced the same scope drift this project has caught
and corrected before (see Open Decision #20 in ROADMAP.md).

This session designed and applied a real, checkable filter for "narrow
down-ballot," built directly from live data rather than assumed:

- The "Politics" category (2,296 series) was checked directly and found to
  contain ZERO individual-district race series - it is national political
  news, executive-branch actions, and officeholder-status questions (e.g.
  "Jared Polis out as Governor of Colorado?"), not races. It is NOT pulled
  by this filter.
- The "Elections" category (1,704 series) is where real race series live.
  Checked directly, three distinct tiers were found:
  1. Individual U.S. House district races (89 series) - Kalshi tags these
     "House" (excluding the separate "House Combos" tag, which covers
     multi-race combo contracts, not single races) and uses a structural
     ticker pattern: "HOUSE" or "KXHOUSE" followed by a two-letter state
     code and a district number (e.g. HOUSECA9, KXHOUSEMO5, KXHOUSEUT02,
     HOUSEAKAL for an at-large seat). This structural check - the same
     kind of approach already used by _is_combo_title() below - correctly
     excludes non-district House-tagged series like "Next DCCC Chair,"
     "Will Republicans lose control of the House?" and combo contracts
     (verified against all 116 "House"-tagged series: 89 real district
     races matched, all 27 non-matches confirmed by inspection to be
     leadership races, chamber-control aggregates, or state-level
     candidate-status news, not district races).
  2. Individual state-legislature district races (4 series found live:
     California State Senate District 26, Pennsylvania State House
     District 12, Maryland State Senate District 2, Missouri State Senate
     District 8) - identified by a structural title pattern ("State
     House/Senate/Assembly District <number>"), the same kind of title-
     text race identifier already observed live in Polymarket's own
     election-market titles per Open Decision #20's original note.
  3. City/county-level district races (14 series found live - 13 NYC City
     Council district seats, 1 Los Angeles City Council district seat) -
     a real, genuinely down-ballot tier, but one level below "House/State
     seats" as Session 0.1's scope was literally worded. Checked directly
     and DECIDED, together with the project owner, NOT to include this
     tier for now - see SESSION_LOG.md's Session 3.1b entry for the full
     evidence trail.
  Statewide races (Governor: 71 series; U.S. Senate: 121 series) were
  checked directly and confirmed to be exactly what Session 0.1 called
  "marquee" - one race per state, high media attention - and are
  deliberately EXCLUDED by this filter, matching the "not national or
  marquee races" half of Open Decision #20's definition.

Real per-seat public forecast data was also confirmed live for the two
included tiers, giving each a genuine basis for an independent edge
estimate (not just a structural naming pattern to pull the right rows):
ElectIndex (electindex.com) publishes a probabilistic forecast for every
2026 U.S. House race AND all 88 state-legislative chambers on the 2026
ballot; multistate.us separately publishes a baseline partisan-lean number
for all 7,388 state-legislative seats nationwide. No comparable per-seat
source was found for city/county races (see above).

Each matched series is tagged with a specific category string at write time
(e.g. "Elections - US House District") instead of Kalshi's generic
"Elections" category, so every row's down-ballot tier is visible directly
in the output CSV without needing to re-derive it from the ticker or title
later.

SESSION 3.2 - REAL YES_ASK_SIZE / YES_BID_SIZE NOW CAPTURED
-------------------------------------------------------------------------
Live validation of Session 3.2's arbitrage detector against real Kalshi
data (multiple KXHIGHPHIL weather strikes, the real KXHOUSEMO5 down-ballot
race - 2026-09-05) found that Kalshi's `liquidity_dollars` field reads
"0.0000" on every real market checked, even ones with substantial real
size resting on the book (one real KXHOUSEMO5 leg had 116.02 contracts at
its best ask). That field is therefore useless as a liquidity signal for
Kalshi specifically - see liquidity_check.py's Session 3.2 notes for the
full evidence trail and the fix. The real, populated fields Kalshi's
market payload DOES carry - `yes_ask_size_fp` and `yes_bid_size_fp` - are
now captured into the normalized schema (`schema_exchange.py`'s new
`yes_ask_size` / `yes_bid_size` columns) so the arbitrage detector's
liquidity check has real numbers to work with for Kalshi rows.

ACCESS - RESOLVED SESSION 3.1 (Open Decision #3, Kalshi half)
------------------------------------------------------------------
Confirmed live 2026-09-04: both GET /series and GET /markets require NO
API key and NO account. This is an OFFICIAL, documented part of Kalshi's
own API (https://docs.kalshi.com), not an undocumented endpoint found by
inspection. Authenticated endpoints (placing orders, viewing a personal
portfolio) DO require an RSA-PSS-signed request and real API credentials
- this script never touches those, since Session 3.1 is read-only
ingestion.

Base URL used: https://api.elections.kalshi.com/trade-api/v2 (Kalshi's own
docs note this is the general-purpose base despite the "elections"
subdomain name).

WHERE OUTPUT GOES
------------------
/data/exchange/raw/kalshi_<timestamp>.json - the exact, unmodified series
list and per-series market responses pulled, saved every run.
/data/exchange/normalized/kalshi_markets_<timestamp>.csv - one normalized
snapshot per run.
/data/exchange/normalized/kalshi_latest.csv - always overwritten each run.

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
# Paths - all relative to the repo root. Run this script from the repo root
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

# Session 3.4 (Automation Adaptation) - ROADMAP.md's Session 3.1 action
# item 18: this script makes one real HTTP request per target series
# (roughly 540 real requests per run - ~448 Climate/Commodities series
# plus 93 down-ballot Elections series, per Session 3.1/3.1b). Session
# 3.1's own real runs relied only on REACTIVE retries (MAX_RETRIES,
# RETRY_BACKOFF_SECONDS above) if a single request failed - there was no
# DELIBERATE pause between requests that succeed. That was an acceptable
# gap for a manually-triggered, watched run, but Session 3.4 turns this
# into an UNATTENDED job that a GitHub Actions runner fires on a
# schedule with no person watching it - a real difference in risk, not a
# cosmetic one. A fixed pause between every request (successful or not)
# is a deliberate, named choice to stay well clear of Kalshi's real
# rate limits, rather than only reacting after this project's own
# requests are already being throttled or blocked. 0.2 seconds adds
# roughly 108 real seconds total to a ~540-series run (540 x 0.2s) -
# small next to this workflow's 30-minute timeout, and worth it for an
# automation that runs unattended and unwatched. Not yet load-tested
# against Kalshi's actual real rate-limit ceiling (no such ceiling is
# published, per this file's own earlier ACCESS note) - if real 429/
# throttling responses are ever observed in the Actions logs, raise
# this value rather than lowering it, and log that as a real, named
# change, the same as any other constant in this project.
KALSHI_PER_SERIES_PAUSE_SECONDS = 0.2

# Real Kalshi category names, confirmed live 2026-09-04 against GET
# /series (13,816 total series). Matches Session 0.1's Track 3 scope
# ("Climate/Commodities") directly. Pulled in full - every series in these
# two categories is in scope, no further filtering needed.
TARGET_CATEGORIES = ["Climate and Weather", "Commodities"]

# Session 3.1b - the Kalshi category real down-ballot race series live in.
# Confirmed live 2026-09-04: "Politics" (2,296 series) contains no
# individual-district race series at all; "Elections" (1,704 series) does.
# Series in this category are NOT pulled in full - only the narrow subset
# matched by classify_down_ballot() below is kept. See module docstring for
# the full evidence trail.
DOWN_BALLOT_CATEGORY = "Elections"

# Structural ticker pattern for individual U.S. House district races,
# confirmed live 2026-09-04 against all 116 series Kalshi tags "House"
# (excluding "House Combos"). Matches e.g. HOUSECA9, KXHOUSEMO5,
# KXHOUSEUT02, HOUSEAKAL (at-large), KXHOUSENJ11SPECIAL (special election).
# Deliberately does NOT match leadership races ("Next DCCC Chair"), chamber-
# control aggregates ("Will Republicans lose control of the House?"), or
# combo contracts - verified directly, not assumed (see module docstring).
_HOUSE_DISTRICT_TICKER_PATTERN = re.compile(
    r"^K?X?HOUSE([A-Z]{2})(\d{1,3}[A-Z]{0,2}|AL)(SPECIAL)?$"
)

# Structural title pattern for individual state-legislature district races,
# confirmed live 2026-09-04 (e.g. "Pennsylvania State House District 12
# winner," "Missouri State Senate District 8 winner").
_STATE_LEG_DISTRICT_PATTERN = re.compile(
    r"state (house|senate|assembly) district \d+", re.IGNORECASE
)

# Structural title pattern for city/county-level district races (e.g. "NYC
# City Council District 4," "Los Angeles City Council District 13
# winner"). NOT currently pulled - kept here, dead but documented, so this
# can be switched back on quickly if the reason below changes.
#
# DECISION (2026-09-04, made directly with the project owner): city/county
# races are EXCLUDED from this filter for now. The test applied was
# whether a real, independent, per-seat probability estimate can be built
# to compare against Kalshi's price - the same test State Legislature
# passed (see below). For city/county races, live research found only
# journalism naming a handful of competitive seats each cycle (e.g. City &
# State NY's "races to watch"), not a systematic per-seat forecast model
# covering every district. Checked directly against Kalshi's own live
# order books too: 6 of 7 NYC City Council series sampled had NO open
# market at all; the one that did (LA City Council District 13) is itself
# one of the handful of seats that gets real news coverage, not
# representative of the rest. This is a "can't yet determine a real edge"
# result, not a "no edge exists" result - revisit if a comprehensive,
# per-seat local-election forecast source is found later.
_CITY_COUNTY_DISTRICT_PATTERN = re.compile(
    r"city council district \d+|county (commission|council) district \d+"
    r"|school board district \d+",
    re.IGNORECASE,
)


def classify_down_ballot(ticker: str, title: Optional[str], tags: Optional[list]) -> Optional[str]:
    """Returns a specific down-ballot tier label for a series confirmed to
    be a genuine, individual-district race with a real, checkable basis
    for an independent edge estimate, or None if the series is not in
    scope. This is the actual, checkable "narrow down-ballot" filter Open
    Decision #20 called for - built from live examples, not a subjective
    per-race judgment call.

    Two tiers are in scope:
    - US House district races: comprehensive, per-seat public forecast
      data exists (e.g. ElectIndex covers every 2026 U.S. House race).
    - State-legislature district races: comprehensive, per-seat public
      data also exists (ElectIndex covers all 88 state-legislative
      chambers on the 2026 ballot; multistate.us has baseline partisan-
      lean data for all 7,388 state-legislative seats nationwide).

    City/county-level district races (NYC/LA City Council, etc.) are
    checked for and deliberately NOT returned as a tier - see the
    DECISION note above _CITY_COUNTY_DISTRICT_PATTERN for why."""
    tags = tags or []
    title = title or ""

    if "House" in tags and "House Combos" not in tags:
        if _HOUSE_DISTRICT_TICKER_PATTERN.match(ticker or ""):
            return "Elections - US House District"

    if _STATE_LEG_DISTRICT_PATTERN.search(title):
        return "Elections - State Legislature District"

    # City/county district races are deliberately excluded - see DECISION
    # note above. Left as an explicit, named no-op (rather than simply
    # omitted) so a future session doesn't have to re-derive why this
    # pattern exists but isn't used.
    if _CITY_COUNTY_DISTRICT_PATTERN.search(title):
        return None

    return None


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
    this project's target categories, PLUS the narrow down-ballot subset
    of the Elections category (Session 3.1b). Confirmed live 2026-09-04:
    GET /series returns ALL series in one call (no pagination needed -
    13,816 returned directly), each with a real 'category' field and a
    'tags' field, so no category query-parameter guessing is needed.
    Returns (matching_tickers, all_series, down_ballot_tier_by_ticker) -
    all_series is kept so run() can build a ticker->category map without a
    second API call; down_ballot_tier_by_ticker lets run() tag each
    down-ballot row with its specific tier instead of the generic
    "Elections" category."""
    payload = _fetch_with_retries(KALSHI_SERIES_ENDPOINT)
    all_series = payload.get("series", payload if isinstance(payload, list) else [])
    if not isinstance(all_series, list):
        raise RuntimeError(
            "GET /series response was not in the expected shape - schema "
            "may have changed."
        )

    climate_commodity_tickers = [
        s.get("ticker")
        for s in all_series
        if s.get("category") in TARGET_CATEGORIES and s.get("ticker")
    ]

    down_ballot_tier_by_ticker: dict[str, str] = {}
    for s in all_series:
        if s.get("category") != DOWN_BALLOT_CATEGORY or not s.get("ticker"):
            continue
        tier = classify_down_ballot(s.get("ticker"), s.get("title"), s.get("tags"))
        if tier:
            down_ballot_tier_by_ticker[s.get("ticker")] = tier

    matching_tickers = climate_commodity_tickers + list(down_ballot_tier_by_ticker.keys())

    log.info(
        "Series discovery: %d total series pulled, %d match Climate/"
        "Commodities, %d match narrow down-ballot (House: %d, state "
        "legislature: %d) - %d target series total. City/county district "
        "races are deliberately excluded (see classify_down_ballot()).",
        len(all_series),
        len(climate_commodity_tickers),
        len(down_ballot_tier_by_ticker),
        sum(1 for t in down_ballot_tier_by_ticker.values() if t == "Elections - US House District"),
        sum(1 for t in down_ballot_tier_by_ticker.values() if t == "Elections - State Legislature District"),
        len(matching_tickers),
    )
    return matching_tickers, all_series, down_ballot_tier_by_ticker


def fetch_markets_for_series(tickers: list[str]) -> list[dict]:
    """Pulls open markets for each target series individually. Each
    series's failure is isolated - one bad/unreachable series must not
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
        finally:
            # Session 3.4 fix (ROADMAP.md action item 18) - a deliberate
            # pause after EVERY request, whether it succeeded or failed,
            # so an unattended scheduled run never fires the next of
            # ~540 real requests back-to-back with no gap at all. See
            # KALSHI_PER_SERIES_PAUSE_SECONDS above for the full
            # reasoning and the real request-count/timeout math.
            time.sleep(KALSHI_PER_SERIES_PAUSE_SECONDS)

    if failed_tickers:
        log.warning(
            "%d of %d target series could not be fetched this run: %s",
            len(failed_tickers),
            len(tickers),
            failed_tickers[:20],  # cap the printed list - could be long
        )

    return pages


# --------------------------------------------------------------------------
# Normalizer - defensive by design, same reasoning as ingest_pickem.py: a
# missing/renamed field on one row causes that row to be skipped (with a
# warning), not the whole run to fail.
# --------------------------------------------------------------------------
_COMBO_LEG_PATTERN = re.compile(r"^\s*(yes|no)\s", re.IGNORECASE)


def _is_combo_title(title: Optional[str]) -> bool:
    """Detects Kalshi's multi-leg combo-contract titles by STRUCTURE
    (see this project's SESSION_LOG.md for the full discovery story of
    why market_type alone can't be used for this). Kept as a defensive
    check even with the new targeted series pull - Climate and Weather/
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
                "Kalshi page missing expected 'markets' list - schema may "
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
                        # guessed here - the raw market object itself
                        # still doesn't carry a category field.
                        category=None,
                        yes_bid=_to_float(record.get("yes_bid_dollars")),
                        yes_ask=_to_float(record.get("yes_ask_dollars")),
                        no_bid=_to_float(record.get("no_bid_dollars")),
                        no_ask=_to_float(record.get("no_ask_dollars")),
                        # Session 3.2 addition - see this file's own
                        # "SESSION 3.2" module-docstring section and
                        # liquidity_check.py for why these two fields
                        # exist and why liquidity_dollars (below) is not
                        # trusted for Kalshi rows despite being pulled.
                        yes_ask_size=_to_float(record.get("yes_ask_size_fp")),
                        yes_bid_size=_to_float(record.get("yes_bid_size_fp")),
                        volume=_to_float(record.get("volume_fp")),
                        liquidity=_to_float(record.get("liquidity_dollars")),
                        close_time=record.get("close_time"),
                        status=record.get("status"),
                        pulled_at=pulled_at,
                    )
                )
            except Exception as exc:  # noqa: BLE001 - one bad record must
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
    """Runs one full ingestion pass. Never raises - every failure mode is
    caught, logged, and reflected in the summary instead, same contract as
    ingest_pickem.py's run()."""
    pulled_at = datetime.now(timezone.utc).isoformat()
    pulled_at_compact = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    summary = {
        "pulled_at": pulled_at,
        "kalshi_target_series_count": 0,
        "kalshi_down_ballot_series_count": 0,
        "kalshi_down_ballot_house_count": 0,
        "kalshi_down_ballot_state_leg_count": 0,
        "kalshi_raw_records_pulled": 0,
        "kalshi_combo_records_filtered_out": 0,
        "kalshi_rows_kept": 0,
        "kalshi_ok": False,
    }

    log.info(
        "=== Kalshi ingestion run starting (Climate and Weather + "
        "Commodities + narrow down-ballot Elections) ==="
    )

    try:
        target_tickers, all_series, down_ballot_tier_by_ticker = (
            fetch_target_series_tickers()
        )
        summary["kalshi_target_series_count"] = len(target_tickers)
        summary["kalshi_down_ballot_series_count"] = len(down_ballot_tier_by_ticker)
        summary["kalshi_down_ballot_house_count"] = sum(
            1 for t in down_ballot_tier_by_ticker.values()
            if t == "Elections - US House District"
        )
        summary["kalshi_down_ballot_state_leg_count"] = sum(
            1 for t in down_ballot_tier_by_ticker.values()
            if t == "Elections - State Legislature District"
        )

        # Map ticker -> category, so each row can be tagged with its real
        # category even though the /markets response itself doesn't
        # include one - filled in below, not guessed. Down-ballot tickers
        # get their specific tier label instead of the generic Kalshi
        # category, so a row's tier is visible directly in the output CSV.
        category_by_ticker = {
            s.get("ticker"): down_ballot_tier_by_ticker.get(
                s.get("ticker"), s.get("category")
            )
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
            "Kalshi: %d target series (%d down-ballot: %d House, %d state "
            "legislature), %d raw records pulled, %d filtered out as "
            "combo listings, %d single-question rows kept",
            len(target_tickers),
            summary["kalshi_down_ballot_series_count"],
            summary["kalshi_down_ballot_house_count"],
            summary["kalshi_down_ballot_state_leg_count"],
            raw_count,
            raw_count - len(rows),
            len(rows),
        )
    except Exception as exc:  # noqa: BLE001 - an outage must not crash the
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
