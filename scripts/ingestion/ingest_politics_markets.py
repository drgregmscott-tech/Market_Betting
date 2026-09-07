"""
Session 5.1 - Down-Ballot Politics Market Ingestion (Race Lists)

WHAT THIS SCRIPT IS
--------------------
Pulls the same narrow down-ballot universe Session 3.1b already defined
and validated (U.S. House district races + state-legislature district
races, marquee races like Governor/Senate explicitly excluded) - but
where ingest_kalshi.py writes those rows into schema_exchange.py's
generic per-venue-contract shape (for arbitrage matching), this script
writes ONE ROW PER REAL RACE into schema_politics.py's shape, with both
venues' pricing joined onto it by a shared, project-owned race_id. This
is the ingestion layer Session 5.2's estimation model and
ingest_polling_data.py's polling join both need.

REUSE, NOT RE-DERIVATION
--------------------------
The down-ballot scope filter (which Kalshi series count as "narrow
down-ballot") is Session 3.1b's classify_down_ballot() function,
imported directly from ingest_kalshi.py below - NOT reimplemented here.
Re-deriving that filter a second time would risk the two copies quietly
drifting apart the next time either one is corrected. Only the OUTPUT
SHAPE differs from ingest_kalshi.py: this script pulls fresh from
Kalshi's live markets endpoint per matched series (same reasoning
ingest_weather_markets.py used for its own richer, track-specific pull)
rather than re-reading ingest_kalshi.py's already-normalized
schema_exchange.py rows, which don't carry state/district as structured
fields.

PREREQUISITE - RUN ingest_polymarket.py FIRST
-----------------------------------------------
This script does NOT re-pull Polymarket. ingest_polymarket.py (Session
3.1) already pulls Polymarket's full active-event catalog, unfiltered by
category, into /data/exchange/normalized/polymarket_latest.csv - the
down-ballot races are already sitting in that file, same as every other
Polymarket category. This script reads that file and filters it down to
down-ballot rows structurally (see classify_polymarket_race() below),
the same "reuse the venue pull, don't re-fetch it" pattern
venue_matcher.py already established for its own Kalshi/Polymarket
comparison. If polymarket_latest.csv doesn't exist or is stale, run
ingest_polymarket.py first - this script logs a clear warning and
proceeds with Kalshi-only rows rather than failing outright.

STRUCTURAL RACE-ID MATCHING - NOT YET VALIDATED AGAINST A LIVE POLYMARKET
DOWN-BALLOT TITLE THIS SESSION
-----------------------------------------------------------------------------
Kalshi's own down-ballot structure is fully validated (Session 3.1b/3.2/
3.4). Polymarket's down-ballot title FORMAT is only confirmed for one
real historical example so far - venue_matcher.py's module docstring
records a real, live-matched pair: Kalshi's MO-05 U.S. House race against
Polymarket's "MO-05 House Election Winner" (Session 3.1b, 2026-09-05).
This script's classify_polymarket_race() therefore reuses
venue_matcher.py's own, already-validated (state, district) code
extraction (_extract_district_codes, imported directly - not
re-implemented) for the House tier, plus a requirement that the word
"house" appear in the title, matching the one real confirmed example.
State-legislature titles on Polymarket have NOT yet been confirmed live
this session (Session 3.1b only checked Kalshi's own title text for that
tier) - the same "State House/Senate/Assembly District N" structural
pattern is applied to Polymarket titles too, as a reasonable structural
guess pending a real match, and every match this path produces is logged
by ticker/title so a human can spot-check it, same conservative posture
venue_matcher.py already uses for every candidate pair it proposes.

LEGAL FOOTPRINT - REAL, DATED, SOURCED FINDINGS (closes Open Decision #22)
-----------------------------------------------------------------------------
Session 3.2 confirmed Kalshi's real state-level SPORTS-contract
restrictions were already modeled (via schema_exchange.py's downstream
consumers) but found no comparable Polymarket-specific list - logged as
Open Decision #22, not assumed either way. Checked live via web search
2026-09-07, specifically for POLITICS/ELECTIONS contracts (not sports,
which is a separate real fight at both venues and already out of this
track's scope):

KALSHI - a real, current, politics-specific restriction exists that is
NOT covered by the existing Sports-only restriction modeling:
  - Washington state: a King County Superior Court order (signed by
    Judge John F. McHale) took effect 2026-08-19/20 requiring Kalshi to
    geofence Washington users out of "Elections & Politics" contracts
    specifically, alongside Sports, Culture, Tech & Science, and
    Mentions. Commodities, Climate, Economics, and Finance are
    EXPRESSLY EXCLUDED from this order. Sources: Gambling Insider
    (gamblinginsider.com/news/193762), The Spokesman-Review
    (spokesman.com, 2026-08-13), Sports Betting Dime (2026-08-21).
  - Arizona: the state filed criminal election-wagering charges against
    Kalshi (including 2026 state races) in March 2026, but a federal
    court has since BLOCKED Arizona from enforcing its gambling law
    against Kalshi while litigation proceeds - i.e. not a current,
    enforced restriction on real access, unlike Washington's. Source:
    CBS Sports (cbssports.com/prediction/news/prediction-market-legal-states),
    checked 2026-09-07 (article dated as of "3 days ago").
  - Minnesota: a state law banning prediction markets (incl. political
    ones) took effect 2026-08-01, but a federal judge granted the CFTC
    preliminary relief blocking its enforcement - same "passed but not
    currently enforced" status as Arizona, not coded as a live
    restriction below.
  Named, honest gap: this is a live legal landscape (Washington's own
  order was under a week old as of this session's check) - the dict
  below should be re-verified, not assumed still accurate, before any
  future session leans on it for real sizing/suppression decisions.

POLYMARKET - checked the same way, same date: no politics-contract-
SPECIFIC state restriction was found, distinct from Polymarket's general
availability picture. The real, active state disputes found (Nevada,
Massachusetts, Michigan, Connecticut) are each specifically about SPORTS
event contracts, not political ones - confirmed explicitly by Gambling
Insider's own note that Massachusetts's Kalshi sports ruling "while
still not affecting Polymarket directly, sets an important precedent"
and The Lines' explicit statement that Nevada/New Jersey's Kalshi
disputes "involve sports, not elections." This is a real "not found,"
not an assumption of parity with Kalshi's Washington restriction -
logged as such, and this project's Open Decision #22 is considered
CLOSED as of this session on that basis (re-open if new evidence
surfaces).

WHERE OUTPUT GOES
------------------
/data/politics/raw/kalshi_politics_<timestamp>.json
/data/politics/normalized/politics_races_<timestamp>.csv
/data/politics/normalized/politics_races_latest.csv (overwritten each run)

USAGE
-----
pip install requests --break-system-packages
python ingest_politics_markets.py
(run ingest_polymarket.py first if polymarket_latest.csv is missing/stale)
"""

from __future__ import annotations

import csv
import json
import logging
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import requests

from schema_politics import NORMALIZED_POLITICS_COLUMNS, NormalizedRaceMarket

# ingest_kalshi.py and venue_matcher.py live in this same directory
# (scripts/ingestion) - imported directly rather than re-implemented, per
# this file's own "REUSE, NOT RE-DERIVATION" module-docstring section.
from ingest_kalshi import (
    classify_down_ballot,
    DOWN_BALLOT_CATEGORY,
    KALSHI_BASE_URL,
    HEADERS,
)
from venue_matcher import _extract_district_codes

BASE_DIR = Path(__file__).resolve().parents[2]
RAW_DIR = BASE_DIR / "data" / "politics" / "raw"
NORMALIZED_DIR = BASE_DIR / "data" / "politics" / "normalized"
LOG_PATH = BASE_DIR / "logs" / "ingestion.log"

POLYMARKET_LATEST = BASE_DIR / "data" / "exchange" / "normalized" / "polymarket_latest.csv"

KALSHI_SERIES_ENDPOINT = f"{KALSHI_BASE_URL}/series"
KALSHI_MARKETS_ENDPOINT = f"{KALSHI_BASE_URL}/markets"

MAX_RETRIES = 2
RETRY_BACKOFF_SECONDS = 3
REQUEST_TIMEOUT_SECONDS = 15

# Same reasoning as ingest_kalshi.py's KALSHI_PER_SERIES_PAUSE_SECONDS -
# this script pulls a small, fixed number of series (93 confirmed live in
# Session 3.1b: 89 House + 4 state legislature), so this is a light run,
# but the pause is kept for consistency with every other unattended-safe
# ingestion script in this project.
KALSHI_PER_SERIES_PAUSE_SECONDS = 0.2

# --------------------------------------------------------------------------
# Liquidity thresholds - STARTING VALUES, named and flagged as such, not
# yet validated against a real down-ballot order book this session (no
# comparable evidence exists yet to Session 3.2's real MO-05 order-book
# check for arbitrage sizing). Same "no unnamed constants" pattern as
# sizing_engine.py's KELLY_FRACTION - recalibrate here, in one place, once
# this pipeline's first real run produces real numbers to check them
# against, and log that as a named change same as any other constant in
# this project.
# --------------------------------------------------------------------------
MIN_LIQUID_KALSHI_CONTRACTS = 10.0
MIN_LIQUID_POLYMARKET_DOLLARS = 100.0

# --------------------------------------------------------------------------
# Legal footprint - see module docstring's "LEGAL FOOTPRINT" section for
# the full, dated, sourced evidence trail behind these two dicts. Checked
# live via web search 2026-09-07 - re-verify before trusting as current.
# --------------------------------------------------------------------------
KALSHI_POLITICS_STATE_RESTRICTIONS: dict[str, str] = {
    "WA": (
        "Blocked: King County Superior Court order effective 2026-08-19/20 "
        "requires Kalshi to geofence Washington users out of Elections & "
        "Politics contracts specifically (Judge John F. McHale). Confirmed "
        "live via web search 2026-09-07 (Gambling Insider, Spokesman-Review, "
        "Sports Betting Dime). Re-verify before relying on this as current."
    ),
}

# Confirmed live 2026-09-07: no Polymarket-specific state restriction on
# POLITICAL contracts was found (distinct from Polymarket's general
# availability picture) - see module docstring. Left as an explicit,
# named empty dict (not simply omitted) so a future reader knows this
# was checked and came back empty, not never checked.
POLYMARKET_POLITICS_STATE_RESTRICTIONS: dict[str, str] = {}


def setup_logging() -> logging.Logger:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("ingest_politics_markets")
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

# --------------------------------------------------------------------------
# Race-ID construction - the shared join key this project owns (see
# schema_politics.py's module docstring for the exact format). One
# function per tier, reused by ingest_polling_data.py so both scripts
# build the identical string from equivalent inputs.
# --------------------------------------------------------------------------

_STATE_LEG_TITLE_PATTERN = re.compile(
    r"([A-Za-z ]+?)\s+State\s+(House|Senate|Assembly)\s+District\s+(\d+)",
    re.IGNORECASE,
)

# Standard USPS state name -> abbreviation map (50 states + DC). Needed
# because Kalshi/Polymarket state-legislature titles spell the state name
# out in full (e.g. "Pennsylvania"), while ElectIndex's leg_races.csv
# (ingest_polling_data.py) and this project's own race_id use the
# 2-letter code throughout.
_STATE_NAME_TO_ABBR = {
    "alabama": "AL", "alaska": "AK", "arizona": "AZ", "arkansas": "AR",
    "california": "CA", "colorado": "CO", "connecticut": "CT",
    "delaware": "DE", "florida": "FL", "georgia": "GA", "hawaii": "HI",
    "idaho": "ID", "illinois": "IL", "indiana": "IN", "iowa": "IA",
    "kansas": "KS", "kentucky": "KY", "louisiana": "LA", "maine": "ME",
    "maryland": "MD", "massachusetts": "MA", "michigan": "MI",
    "minnesota": "MN", "mississippi": "MS", "missouri": "MO",
    "montana": "MT", "nebraska": "NE", "nevada": "NV",
    "new hampshire": "NH", "new jersey": "NJ", "new mexico": "NM",
    "new york": "NY", "north carolina": "NC", "north dakota": "ND",
    "ohio": "OH", "oklahoma": "OK", "oregon": "OR", "pennsylvania": "PA",
    "rhode island": "RI", "south carolina": "SC", "south dakota": "SD",
    "tennessee": "TN", "texas": "TX", "utah": "UT", "vermont": "VT",
    "virginia": "VA", "washington": "WA", "west virginia": "WV",
    "wisconsin": "WI", "wyoming": "WY",
    "district of columbia": "DC",
}


def race_key_for_house_district(state: str, district: int) -> str:
    return f"US-HOUSE-{state.upper()}-{district:02d}"


def race_key_for_state_leg(state: str, chamber: str, district: str) -> str:
    return f"STATE-LEG-{state.upper()}-{chamber.upper()}-{district}"


def parse_state_leg_title(title: Optional[str]):
    """Returns (state_abbr, chamber, district_number_str) or None. Applied
    identically to Kalshi and Polymarket titles - see module docstring's
    note on this being unvalidated against a real Polymarket
    state-legislature title this session."""
    if not title:
        return None
    match = _STATE_LEG_TITLE_PATTERN.search(title)
    if not match:
        return None
    state_name, chamber, district = match.groups()
    abbr = _STATE_NAME_TO_ABBR.get(state_name.strip().lower())
    if not abbr:
        log.warning(
            "State-legislature title matched the structural pattern but "
            "'%s' isn't in the known state-name map - skipped, not "
            "guessed: %r", state_name.strip(), title,
        )
        return None
    return abbr, chamber.capitalize(), district


# --------------------------------------------------------------------------
# Kalshi fetch - down-ballot only (does NOT re-pull Climate/Weather or
# Commodities; ingest_kalshi.py already owns that pull for Track 2).
# --------------------------------------------------------------------------

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


def fetch_down_ballot_series() -> tuple[list[dict], dict[str, str]]:
    """Pulls Kalshi's full series list once and keeps only the Elections
    series classify_down_ballot() (Session 3.1b, imported above)
    confirms are real, individual down-ballot races."""
    payload = _fetch_with_retries(KALSHI_SERIES_ENDPOINT)
    all_series = payload.get("series", payload if isinstance(payload, list) else [])

    matched = []
    tier_by_ticker: dict[str, str] = {}
    for s in all_series:
        if s.get("category") != DOWN_BALLOT_CATEGORY or not s.get("ticker"):
            continue
        tier = classify_down_ballot(s.get("ticker"), s.get("title"), s.get("tags"))
        if tier:
            matched.append(s)
            tier_by_ticker[s["ticker"]] = tier

    log.info(
        "Series discovery: %d Elections-category series, %d confirmed "
        "narrow down-ballot (House: %d, state legislature: %d).",
        sum(1 for s in all_series if s.get("category") == DOWN_BALLOT_CATEGORY),
        len(matched),
        sum(1 for t in tier_by_ticker.values() if t == "Elections - US House District"),
        sum(1 for t in tier_by_ticker.values() if t == "Elections - State Legislature District"),
    )
    return matched, tier_by_ticker


_KALSHI_HOUSE_TICKER_STATE_DISTRICT = re.compile(
    r"^K?X?HOUSE([A-Z]{2})(\d{1,3}|AL)(SPECIAL)?$"
)


def kalshi_race_id_for_series(ticker: str, title: Optional[str], tier: str):
    """Derives this project's own race_id from a Kalshi series already
    confirmed down-ballot by classify_down_ballot(). Returns None (and
    logs a warning) if the structural parse fails - never guesses."""
    if tier == "Elections - US House District":
        match = _KALSHI_HOUSE_TICKER_STATE_DISTRICT.match(ticker)
        if not match:
            log.warning(
                "Series %s confirmed as US House District tier but ticker "
                "didn't match the expected state/district structure - "
                "skipped.", ticker,
            )
            return None
        state, district_raw, _special = match.groups()
        # REAL BUG FOUND AND FIXED (checked directly against ElectIndex's
        # real races_summary.csv before this script ever ran live, 2026-09-07):
        # at-large House seats (AK, ND, and other single-district states)
        # are numbered "01" in ElectIndex's real data, not "00" - confirmed
        # against the real AK-01 and ND-01 rows. Kalshi's own ticker uses
        # the literal string "AL" for at-large (e.g. HOUSEAKAL, per
        # ingest_kalshi.py's module docstring) - mapped to district 1 here,
        # not 0, so this project's race_id actually joins to ElectIndex's
        # real row instead of silently matching nothing.
        district = 1 if district_raw == "AL" else int(district_raw)
        return race_key_for_house_district(state, district), state, None, str(district)

    if tier == "Elections - State Legislature District":
        parsed = parse_state_leg_title(title)
        if not parsed:
            log.warning(
                "Series %s confirmed as State Legislature District tier "
                "but title didn't match the expected structure - "
                "skipped: %r", ticker, title,
            )
            return None
        state, chamber, district = parsed
        return race_key_for_state_leg(state, chamber, district), state, chamber, district

    return None


def fetch_markets_for_series(ticker: str) -> list[dict]:
    try:
        payload = _fetch_with_retries(
            KALSHI_MARKETS_ENDPOINT, params={"series_ticker": ticker, "status": "open"}
        )
        return payload.get("markets", [])
    except RuntimeError as exc:
        log.warning("Failed to fetch markets for series %s: %s", ticker, exc)
        return []


def build_kalshi_rows(series_list: list[dict], tier_by_ticker: dict[str, str]) -> dict[str, dict]:
    """Returns race_id -> a dict of Kalshi-side fields ready to feed into
    NormalizedRaceMarket. One race is assumed to have at most one open
    Kalshi market at a time for this tier (confirmed live 2026-09-04/05,
    Session 3.1b) - if a series ever has more than one open market, the
    first is kept and a warning is logged, rather than silently
    overwriting with no record of it."""
    rows: dict[str, dict] = {}
    all_raw: dict[str, list[dict]] = {}

    for i, s in enumerate(series_list, 1):
        ticker = s["ticker"]
        tier = tier_by_ticker[ticker]
        parsed = kalshi_race_id_for_series(ticker, s.get("title"), tier)
        time.sleep(KALSHI_PER_SERIES_PAUSE_SECONDS)
        if parsed is None:
            continue
        race_id, state, chamber, district = parsed

        markets = fetch_markets_for_series(ticker)
        all_raw[ticker] = markets
        time.sleep(KALSHI_PER_SERIES_PAUSE_SECONDS)

        if not markets:
            continue
        if len(markets) > 1:
            log.warning(
                "Series %s has %d open markets - expected at most one "
                "for a single down-ballot race. Keeping the first, "
                "flagged here rather than silently dropped.",
                ticker, len(markets),
            )
        m = markets[0]

        state_restriction = KALSHI_POLITICS_STATE_RESTRICTIONS.get(state, "")

        rows[race_id] = {
            "race_id": race_id,
            "tier": tier,
            "state": state,
            "chamber": chamber,
            "district": district,
            "kalshi_ticker": m.get("ticker"),
            "kalshi_title": s.get("title"),
            "kalshi_yes_bid": _to_float(m.get("yes_bid_dollars")),
            "kalshi_yes_ask": _to_float(m.get("yes_ask_dollars")),
            "kalshi_no_bid": _to_float(m.get("no_bid_dollars")),
            "kalshi_no_ask": _to_float(m.get("no_ask_dollars")),
            "kalshi_yes_ask_size": _to_float(m.get("yes_ask_size_fp")),
            "kalshi_yes_bid_size": _to_float(m.get("yes_bid_size_fp")),
            "kalshi_close_time": m.get("close_time"),
            "kalshi_status": m.get("status"),
            "legal_footprint_kalshi": state_restriction,
        }

        if i % 20 == 0 or i == len(series_list):
            log.info("Kalshi: processed %d/%d down-ballot series so far.", i, len(series_list))

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    # Explicit encoding="utf-8" - see ingest_polling_data.py's real,
    # live-caught bug note (Session 5.1, first Windows run, 2026-09-07):
    # write_text() with no encoding argument defaults to the OS locale
    # encoding (cp1252 on Windows), which fails on real non-ASCII
    # characters in race/candidate titles. Fixed here proactively, same
    # fix applied there.
    (RAW_DIR / f"kalshi_politics_{ts}.json").write_text(
        json.dumps(all_raw, indent=2), encoding="utf-8"
    )

    return rows


# --------------------------------------------------------------------------
# Polymarket - reads the already-pulled polymarket_latest.csv (see module
# docstring's "PREREQUISITE" section) and filters structurally.
# --------------------------------------------------------------------------

_HOUSE_KEYWORD_PATTERN = re.compile(r"\bhouse\b", re.IGNORECASE)


def classify_polymarket_race(title: Optional[str]):
    """Returns (race_id, state, chamber, district) for a Polymarket row
    structurally identified as a down-ballot race, or None. See module
    docstring's own section on why this is a reasonable-but-unvalidated
    structural guess for the state-legislature path specifically."""
    if not title:
        return None

    # US House path - reuses venue_matcher.py's own already-validated
    # (state, district) extraction (imported above), plus requiring the
    # word "house" appear, matching the one real confirmed Polymarket
    # down-ballot title found in Session 3.1b ("MO-05 House Election
    # Winner").
    codes = _extract_district_codes(title)
    if codes and _HOUSE_KEYWORD_PATTERN.search(title):
        state, district = next(iter(codes))
        return (
            race_key_for_house_district(state, district),
            state.upper(), None, str(district),
        )

    # State-legislature path - same structural title pattern used for
    # Kalshi, applied here too (see module docstring: not yet confirmed
    # live against a real Polymarket state-leg title this session).
    parsed = parse_state_leg_title(title)
    if parsed:
        state, chamber, district = parsed
        return race_key_for_state_leg(state, chamber, district), state, chamber, district

    return None


def build_polymarket_rows() -> dict[str, dict]:
    if not POLYMARKET_LATEST.exists():
        log.warning(
            "%s does not exist - run ingest_polymarket.py first. "
            "Proceeding with Kalshi-only rows for this run, not failing.",
            POLYMARKET_LATEST,
        )
        return {}

    with POLYMARKET_LATEST.open(newline="", encoding="utf-8") as f:
        all_rows = list(csv.DictReader(f))

    rows: dict[str, dict] = {}
    matched_count = 0
    for r in all_rows:
        parsed = classify_polymarket_race(r.get("title"))
        if not parsed:
            continue
        race_id, state, chamber, district = parsed
        matched_count += 1

        state_restriction = POLYMARKET_POLITICS_STATE_RESTRICTIONS.get(state, "")

        if race_id in rows:
            log.warning(
                "More than one Polymarket row matched race_id %s - "
                "keeping the first, flagged here rather than silently "
                "overwritten (source_market_id=%s).",
                race_id, r.get("source_market_id"),
            )
            continue

        rows[race_id] = {
            "race_id": race_id,
            "tier": (
                "Elections - US House District" if chamber is None
                else "Elections - State Legislature District"
            ),
            "state": state,
            "chamber": chamber,
            "district": district,
            "polymarket_market_id": r.get("source_market_id"),
            "polymarket_title": r.get("title"),
            "polymarket_yes_bid": _to_float(r.get("yes_bid")),
            "polymarket_yes_ask": _to_float(r.get("yes_ask")),
            "polymarket_no_bid": _to_float(r.get("no_bid")),
            "polymarket_no_ask": _to_float(r.get("no_ask")),
            "polymarket_liquidity": _to_float(r.get("liquidity")),
            "polymarket_close_time": r.get("close_time"),
            "polymarket_status": r.get("status"),
            "legal_footprint_polymarket": state_restriction,
        }

    log.info(
        "Polymarket: %d of %d rows in %s structurally matched a "
        "down-ballot race.",
        matched_count, len(all_rows), POLYMARKET_LATEST.name,
    )
    return rows


# --------------------------------------------------------------------------
# Liquidity labeling - against the named MIN_LIQUID_* constants above.
# --------------------------------------------------------------------------

def liquidity_note_kalshi(row: dict) -> Optional[str]:
    if row.get("kalshi_yes_ask_size") is None and row.get("kalshi_yes_bid_size") is None:
        return "no market" if row.get("kalshi_ticker") else None
    best_side = max(
        row.get("kalshi_yes_ask_size") or 0.0, row.get("kalshi_yes_bid_size") or 0.0
    )
    return "ok" if best_side >= MIN_LIQUID_KALSHI_CONTRACTS else "thin"


def liquidity_note_polymarket(row: dict) -> Optional[str]:
    if row.get("polymarket_liquidity") is None:
        return "no market" if row.get("polymarket_market_id") else None
    return (
        "ok" if row["polymarket_liquidity"] >= MIN_LIQUID_POLYMARKET_DOLLARS else "thin"
    )


# --------------------------------------------------------------------------
# Join + output
# --------------------------------------------------------------------------

def join_rows(kalshi_rows: dict[str, dict], polymarket_rows: dict[str, dict], pulled_at: str) -> list[NormalizedRaceMarket]:
    all_race_ids = set(kalshi_rows) | set(polymarket_rows)
    out: list[NormalizedRaceMarket] = []

    for race_id in sorted(all_race_ids):
        k = kalshi_rows.get(race_id, {})
        p = polymarket_rows.get(race_id, {})

        tier = k.get("tier") or p.get("tier")
        state = k.get("state") or p.get("state")
        chamber = k.get("chamber") if k.get("chamber") is not None else p.get("chamber")
        district = k.get("district") or p.get("district")

        merged = {**k, **{key: val for key, val in p.items() if key not in k or k.get(key) is None}}
        merged["race_id"] = race_id
        merged["tier"] = tier
        merged["state"] = state
        merged["chamber"] = chamber
        merged["district"] = district

        merged["liquidity_note_kalshi"] = liquidity_note_kalshi(merged)
        merged["liquidity_note_polymarket"] = liquidity_note_polymarket(merged)
        merged["legal_footprint_kalshi"] = merged.get("legal_footprint_kalshi", "")
        merged["legal_footprint_polymarket"] = merged.get("legal_footprint_polymarket", "")
        merged["pulled_at"] = pulled_at

        fields = {f: merged.get(f) for f in NormalizedRaceMarket.__dataclass_fields__}
        out.append(NormalizedRaceMarket(**fields))

    return out


def write_normalized_csv(path: Path, rows: list[NormalizedRaceMarket]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=NORMALIZED_POLITICS_COLUMNS)
        writer.writeheader()
        for row in rows:
            writer.writerow(row.as_row())


def run() -> dict:
    pulled_at = datetime.now(timezone.utc).isoformat()
    pulled_at_compact = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    summary = {
        "pulled_at": pulled_at,
        "kalshi_series_matched": 0,
        "kalshi_race_rows": 0,
        "polymarket_race_rows": 0,
        "races_total": 0,
        "races_both_venues": 0,
        "ok": False,
    }

    log.info("=== Down-ballot politics market ingestion run starting ===")

    try:
        series_list, tier_by_ticker = fetch_down_ballot_series()
        summary["kalshi_series_matched"] = len(series_list)

        kalshi_rows = build_kalshi_rows(series_list, tier_by_ticker)
        polymarket_rows = build_polymarket_rows()

        summary["kalshi_race_rows"] = len(kalshi_rows)
        summary["polymarket_race_rows"] = len(polymarket_rows)
        summary["races_both_venues"] = len(set(kalshi_rows) & set(polymarket_rows))

        rows = join_rows(kalshi_rows, polymarket_rows, pulled_at)
        summary["races_total"] = len(rows)
        summary["ok"] = True

        log.info(
            "Down-ballot politics: %d Kalshi series matched, %d Kalshi "
            "race rows, %d Polymarket race rows, %d races total (%d on "
            "both venues).",
            summary["kalshi_series_matched"], summary["kalshi_race_rows"],
            summary["polymarket_race_rows"], summary["races_total"],
            summary["races_both_venues"],
        )
    except Exception as exc:  # noqa: BLE001 - an outage must not crash
        # the whole pipeline; write whatever we have.
        log.error("Down-ballot politics ingestion failed for this run: %s", exc)
        rows = []

    snapshot_path = NORMALIZED_DIR / f"politics_races_{pulled_at_compact}.csv"
    latest_path = NORMALIZED_DIR / "politics_races_latest.csv"
    write_normalized_csv(snapshot_path, rows)
    write_normalized_csv(latest_path, rows)

    log.info(
        "=== Down-ballot politics ingestion run complete: %d race rows (%s) ===",
        len(rows), "OK" if summary["ok"] else "FAILED",
    )
    summary["snapshot_path"] = str(snapshot_path)
    return summary


if __name__ == "__main__":
    result = run()
    print(json.dumps(result, indent=2))
