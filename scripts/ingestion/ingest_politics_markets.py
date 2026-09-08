"""
Session 5.1 - Down-Ballot Politics Market Ingestion (Race Lists)
Session 5.1c PATCH (this session) - now captures every open candidate
market per race and matches each to a party by real candidate name,
instead of keeping one arbitrary market per race with no party recorded.
See "SESSION 5.1c PATCH" section below for the real problem this fixes.

WHAT THIS SCRIPT IS
--------------------
Pulls the same narrow down-ballot universe Session 3.1b already defined
and validated (U.S. House district races + state-legislature district
races, marquee races like Governor/Senate explicitly excluded) - but
where ingest_kalshi.py writes those rows into schema_exchange.py's
generic per-venue-contract shape (for arbitrage matching), this script
writes ONE ROW PER REAL RACE into schema_politics.py's shape, with both
venues' Democratic- and Republican-candidate pricing joined onto it by a
shared, project-owned race_id. This is the ingestion layer Session 5.2's
estimation model and ingest_polling_data.py's polling join both need.

SESSION 5.1c PATCH - CANDIDATE IDENTITY WAS MISSING, NOW REQUIRED
-----------------------------------------------------------------------
Found live, this session (2026-09-08), while preparing Session 5.2's
estimation model: Kalshi does not run one YES/NO contract per race. Each
race is a SERIES with one open MARKET PER CANDIDATE. Confirmed directly
against the real KXCASEN26 series (California State Senate District 26):
8 open candidate markets - Wendy Carrillo, Sarah Rascon, Sang Masog, Sara
Hernandez, Paul A. Bowers, and 3 more. The real candidate name for each
market lives on that market's own `yes_sub_title` field (confirmed live
this session), NOT on the series-level title, which is generic ("Who
will win the 2026 California State Senate District 26 election?") and
names no candidate.

The original version of this script kept only the FIRST market Kalshi's
API returned per series, with no record of which candidate or party it
belonged to (the "13 series had more than one open market" note in
Session 5.1's own SESSION_LOG.md entry was this exact problem, observed
but not yet acted on). Since ElectIndex always reports a
Democrat-win-probability and a Republican-win-probability for the same
race (see ingest_polling_data.py), Session 5.2's model had no reliable
way to know which party the kept price actually belonged to.

THE FIX: this script now pulls EVERY open market for every matched
series (not just the first), and matches each one's candidate name
against ElectIndex's own real dem_name/rep_name for that race (read from
polling_estimates_latest.csv - ingest_polling_data.py's Session 5.1c
patch now carries those two fields through, reusing the existing
"reuse the pull, don't re-fetch" pattern this project already applies to
Polymarket). A market that matches neither name is a real, named
third-party or minor candidate - kept and logged in
schema_politics.py's `kalshi_unmatched_candidates` /
`polymarket_unmatched_candidates` fields, never silently dropped and
never guessed into a Dem/Rep slot on a name that didn't actually match.

PREREQUISITE - RUN ingest_polling_data.py BEFORE THIS SCRIPT (NEW,
THIS PATCH)
-----------------------------------------------------------------------
This script now reads polling_estimates_latest.csv for real dem_name/
rep_name candidate names, in addition to its existing Polymarket
prerequisite below. If that file is missing or stale, this script logs a
clear warning and proceeds with every open market marked unmatched
(never guessed) rather than failing outright - the same defensive
posture the existing Polymarket-missing case already uses.

PREREQUISITE - RUN ingest_polymarket.py FIRST (UNCHANGED FROM SESSION 5.1)
-----------------------------------------------------------------------
This script does NOT re-pull Polymarket. ingest_polymarket.py (Session
3.1) already pulls Polymarket's full active-event catalog, unfiltered by
category, into /data/exchange/normalized/polymarket_latest.csv - the
down-ballot races are already sitting in that file, same as every other
Polymarket category. This script reads that file and filters it down to
down-ballot rows structurally (see classify_polymarket_race() below).
SESSION 5.1c PATCH: previously, more than one Polymarket row matching
the same race_id had all but the first DISCARDED with a warning. Now
every structurally-matched row is kept and run through the same
candidate-name matching Kalshi's side uses, since a real race can
legitimately have more than one Polymarket market too (same underlying
multi-candidate reality this patch fixes on the Kalshi side).

STRUCTURAL RACE-ID MATCHING - NOT YET VALIDATED AGAINST A LIVE POLYMARKET
DOWN-BALLOT TITLE THIS SESSION (UNCHANGED FROM SESSION 5.1)
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
this session - the same "State House/Senate/Assembly District N"
structural pattern is applied to Polymarket titles too, as a reasonable
structural guess pending a real match, and every match this path
produces is logged by ticker/title so a human can spot-check it.
SESSION 5.1c PATCH: Polymarket candidate-name matching (title-substring
against dem_name/rep_name, see match_polymarket_candidate() below) is
similarly unvalidated against a real multi-candidate Polymarket title
this session - the real per-run unmatched-candidate count is the honest
signal of whether it's working, logged every run, not assumed correct.

LEGAL FOOTPRINT - REAL, DATED, SOURCED FINDINGS (closes Open Decision #22,
UNCHANGED FROM SESSION 5.1)
-----------------------------------------------------------------------------
KALSHI - a real, current, politics-specific restriction exists:
- Washington state: a King County Superior Court order (signed by
  Judge John F. McHale) took effect 2026-08-19/20 requiring Kalshi to
  geofence Washington users out of "Elections & Politics" contracts
  specifically. Sources: Gambling Insider (gamblinginsider.com/news/193762),
  The Spokesman-Review (spokesman.com, 2026-08-13), Sports Betting Dime
  (2026-08-21).
- Arizona / Minnesota: real restrictions exist on paper but are
  currently blocked from enforcement by federal court action - not
  coded as live restrictions below (see original Session 5.1 module
  docstring for the full evidence trail).
POLYMARKET - no politics-contract-specific state restriction was found,
distinct from Polymarket's general availability picture. Open Decision
#22 is considered CLOSED as of Session 5.1's live research (re-open if
new evidence surfaces). This is venue-level, unaffected by this patch.

WHERE OUTPUT GOES
------------------
/data/politics/raw/kalshi_politics_<timestamp>.json
/data/politics/normalized/politics_races_<timestamp>.csv
/data/politics/normalized/politics_races_latest.csv (overwritten each run)

USAGE
-----
pip install requests --break-system-packages
python ingest_polling_data.py   (run first - this script reads its output)
python ingest_polymarket.py     (run first if polymarket_latest.csv is missing/stale)
python ingest_politics_markets.py
"""

from __future__ import annotations

import csv
import json
import logging
import re
import time
import unicodedata
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import requests

from schema_politics import NORMALIZED_POLITICS_COLUMNS, NormalizedRaceMarket

# ingest_kalshi.py and venue_matcher.py live in this same directory
# (scripts/ingestion) - imported directly rather than re-implemented, per
# this file's own "REUSE, NOT RE-DERIVATION" reasoning (Session 5.1).
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
# SESSION 5.1c PATCH - new prerequisite, see module docstring.
POLLING_ESTIMATES_LATEST = BASE_DIR / "data" / "politics" / "normalized" / "polling_estimates_latest.csv"

KALSHI_SERIES_ENDPOINT = f"{KALSHI_BASE_URL}/series"
KALSHI_MARKETS_ENDPOINT = f"{KALSHI_BASE_URL}/markets"

MAX_RETRIES = 2
RETRY_BACKOFF_SECONDS = 3
REQUEST_TIMEOUT_SECONDS = 15

# Same reasoning as ingest_kalshi.py's KALSHI_PER_SERIES_PAUSE_SECONDS -
# this script pulls a small, fixed number of series (93 confirmed live in
# Session 3.1b), so this is a light run, but the pause is kept for
# consistency with every other unattended-safe ingestion script.
KALSHI_PER_SERIES_PAUSE_SECONDS = 0.2

# --------------------------------------------------------------------------
# Liquidity thresholds - STARTING VALUES, named and flagged as such
# (Session 5.1). Unchanged by this patch.
# --------------------------------------------------------------------------
MIN_LIQUID_KALSHI_CONTRACTS = 10.0
MIN_LIQUID_POLYMARKET_DOLLARS = 100.0

# --------------------------------------------------------------------------
# Legal footprint - see module docstring's "LEGAL FOOTPRINT" section.
# Unchanged by this patch. Checked live via web search 2026-09-07 -
# re-verify before trusting as current.
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
# Race-ID construction - unchanged from Session 5.1 (the shared join key
# this project owns - see schema_politics.py's module docstring).
# --------------------------------------------------------------------------

_STATE_LEG_TITLE_PATTERN = re.compile(
    r"([A-Za-z ]+?)\s+State\s+(House|Senate|Assembly)\s+District\s+(\d+)",
    re.IGNORECASE,
)

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
# SESSION 5.1c PATCH - candidate name -> party matching.
# --------------------------------------------------------------------------

def _normalize_name(name: Optional[str]) -> str:
    """Lowercases and strips accents (e.g. 'Rascón' -> 'rascon') so a
    real accented name from one source matches a plain-ASCII rendering
    from another - a real, observed risk given ElectIndex's and Kalshi's
    data come from independent pipelines. Not a guess: this is the
    standard NFKD-decompose-and-drop-combining-marks technique, applied
    identically to both sides of every comparison below."""
    if not name:
        return ""
    decomposed = unicodedata.normalize("NFKD", name)
    stripped = "".join(c for c in decomposed if not unicodedata.combining(c))
    return stripped.strip().lower()


def _last_name(full_name: Optional[str]) -> str:
    norm = _normalize_name(full_name)
    parts = norm.split()
    return parts[-1] if parts else ""


def match_kalshi_candidate(candidate_name: Optional[str], dem_name: str, rep_name: str) -> Optional[str]:
    """Returns 'dem', 'rep', or None (unmatched - real minor/third-party
    candidate, or a genuine name-matching miss to be spot-checked from
    the logged unmatched-candidates field). Matches on last name only,
    case- and accent-insensitive - first names/middle initials on down-
    ballot candidate lists are inconsistent enough across sources (e.g.
    'Paul A. Bowers' on Kalshi vs however ElectIndex renders the same
    candidate) that requiring a full-name match would produce more false
    non-matches than a last-name match produces false positives, given
    real down-ballot races rarely have two candidates sharing a surname."""
    cand_last = _last_name(candidate_name)
    if not cand_last:
        return None
    dem_last = _last_name(dem_name)
    rep_last = _last_name(rep_name)
    if dem_last and cand_last == dem_last:
        return "dem"
    if rep_last and cand_last == rep_last:
        return "rep"
    return None


def match_polymarket_candidate(title: Optional[str], dem_name: str, rep_name: str) -> Optional[str]:
    """Polymarket's real market objects do not carry a structured
    per-candidate name field the way Kalshi's yes_sub_title does (not
    confirmed live this session - see module docstring). This matches by
    checking whether the candidate's last name appears as a substring of
    the market title instead. If both parties' last names appear (or
    neither does), the match is genuinely ambiguous and returns None -
    logged as unmatched rather than guessed either way."""
    t = _normalize_name(title)
    if not t:
        return None
    dem_last = _last_name(dem_name)
    rep_last = _last_name(rep_name)
    dem_hit = bool(dem_last) and dem_last in t
    rep_hit = bool(rep_last) and rep_last in t
    if dem_hit and not rep_hit:
        return "dem"
    if rep_hit and not dem_hit:
        return "rep"
    return None


def load_electindex_names() -> dict[str, tuple[str, str]]:
    """Returns race_id -> (dem_name, rep_name), read from
    polling_estimates_latest.csv (ingest_polling_data.py's Session 5.1c
    patch output). Missing/stale file is a real, logged gap - every
    candidate in this run is then marked unmatched rather than guessed,
    same defensive posture as the existing missing-Polymarket-file case
    below."""
    if not POLLING_ESTIMATES_LATEST.exists():
        log.warning(
            "%s does not exist - run ingest_polling_data.py first. "
            "Proceeding with NO candidate-name matching this run (every "
            "open market will be logged as unmatched, not guessed).",
            POLLING_ESTIMATES_LATEST,
        )
        return {}
    out: dict[str, tuple[str, str]] = {}
    with POLLING_ESTIMATES_LATEST.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            race_id = row.get("race_id")
            if not race_id:
                continue
            out[race_id] = (
                (row.get("dem_name") or "").strip(),
                (row.get("rep_name") or "").strip(),
            )
    log.info("Loaded ElectIndex candidate names for %d races from %s.", len(out), POLLING_ESTIMATES_LATEST.name)
    return out


# --------------------------------------------------------------------------
# Kalshi fetch - down-ballot only.
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
    """SESSION 5.1c PATCH: returns EVERY open market for this series, not
    just the first. status='open' already excludes closed/settled
    markets - no further filtering applied here."""
    try:
        payload = _fetch_with_retries(
            KALSHI_MARKETS_ENDPOINT, params={"series_ticker": ticker, "status": "open"}
        )
        return payload.get("markets", [])
    except RuntimeError as exc:
        log.warning("Failed to fetch markets for series %s: %s", ticker, exc)
        return []


def build_kalshi_rows(
    series_list: list[dict], tier_by_ticker: dict[str, str], electindex_names: dict[str, tuple[str, str]]
) -> dict[str, dict]:
    """Returns race_id -> a dict of Kalshi-side fields ready to feed into
    NormalizedRaceMarket. SESSION 5.1c PATCH: every open market for a
    series is now fetched and matched to dem/rep by real candidate name
    (see match_kalshi_candidate() above) via each market's own
    `yes_sub_title` field (confirmed live 2026-09-08 as the real field
    carrying the candidate name - the series-level title does not name
    one). A market that matches neither party's name is kept in
    kalshi_unmatched_candidates, never dropped and never guessed."""
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

        dem_name, rep_name = electindex_names.get(race_id, ("", ""))

        dem_market = None
        rep_market = None
        unmatched_names: list[str] = []

        for m in markets:
            # yes_sub_title is the real, live-confirmed field carrying
            # the candidate's name (see module docstring). Falls back to
            # the market's own title (not the series title) if
            # yes_sub_title is ever absent, rather than leaving the
            # candidate name blank outright.
            candidate_name = m.get("yes_sub_title") or m.get("title") or ""
            party = match_kalshi_candidate(candidate_name, dem_name, rep_name)
            if party == "dem" and dem_market is None:
                dem_market = (candidate_name, m)
            elif party == "rep" and rep_market is None:
                rep_market = (candidate_name, m)
            elif party is None:
                unmatched_names.append(candidate_name)
            else:
                # A second market matched the same party as one already
                # kept (e.g. a data anomaly) - logged, not silently
                # overwritten.
                log.warning(
                    "Series %s: candidate %r matched '%s' but that party "
                    "already has a matched market for race %s - kept as "
                    "unmatched instead of overwriting.",
                    ticker, candidate_name, party, race_id,
                )
                unmatched_names.append(candidate_name)

        state_restriction = KALSHI_POLITICS_STATE_RESTRICTIONS.get(state, "")

        row = {
            "race_id": race_id,
            "tier": tier,
            "state": state,
            "chamber": chamber,
            "district": district,
            "kalshi_unmatched_candidates": "; ".join(unmatched_names),
            "kalshi_total_open_candidates": len(markets),
            "legal_footprint_kalshi": state_restriction,
        }

        if dem_market:
            name, m = dem_market
            row.update({
                "kalshi_dem_candidate_name": name,
                "kalshi_dem_ticker": m.get("ticker"),
                "kalshi_dem_yes_bid": _to_float(m.get("yes_bid_dollars")),
                "kalshi_dem_yes_ask": _to_float(m.get("yes_ask_dollars")),
                "kalshi_dem_yes_ask_size": _to_float(m.get("yes_ask_size_fp")),
                "kalshi_dem_yes_bid_size": _to_float(m.get("yes_bid_size_fp")),
                "kalshi_dem_close_time": m.get("close_time"),
                "kalshi_dem_status": m.get("status"),
            })
        if rep_market:
            name, m = rep_market
            row.update({
                "kalshi_rep_candidate_name": name,
                "kalshi_rep_ticker": m.get("ticker"),
                "kalshi_rep_yes_bid": _to_float(m.get("yes_bid_dollars")),
                "kalshi_rep_yes_ask": _to_float(m.get("yes_ask_dollars")),
                "kalshi_rep_yes_ask_size": _to_float(m.get("yes_ask_size_fp")),
                "kalshi_rep_yes_bid_size": _to_float(m.get("yes_bid_size_fp")),
                "kalshi_rep_close_time": m.get("close_time"),
                "kalshi_rep_status": m.get("status"),
            })

        rows[race_id] = row

        if i % 20 == 0 or i == len(series_list):
            log.info("Kalshi: processed %d/%d down-ballot series so far.", i, len(series_list))

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    (RAW_DIR / f"kalshi_politics_{ts}.json").write_text(
        json.dumps(all_raw, indent=2), encoding="utf-8"
    )

    return rows


# --------------------------------------------------------------------------
# Polymarket - reads the already-pulled polymarket_latest.csv.
# --------------------------------------------------------------------------

_HOUSE_KEYWORD_PATTERN = re.compile(r"\bhouse\b", re.IGNORECASE)


def classify_polymarket_race(title: Optional[str]):
    if not title:
        return None

    codes = _extract_district_codes(title)
    if codes and _HOUSE_KEYWORD_PATTERN.search(title):
        state, district = next(iter(codes))
        return (
            race_key_for_house_district(state, district),
            state.upper(), None, str(district),
        )

    parsed = parse_state_leg_title(title)
    if parsed:
        state, chamber, district = parsed
        return race_key_for_state_leg(state, chamber, district), state, chamber, district

    return None


def build_polymarket_rows(electindex_names: dict[str, tuple[str, str]]) -> dict[str, dict]:
    """SESSION 5.1c PATCH: every structurally-matched Polymarket row for
    a race_id is now collected (not just the first), then matched to
    dem/rep by candidate-name substring (see match_polymarket_candidate()
    above)."""
    if not POLYMARKET_LATEST.exists():
        log.warning(
            "%s does not exist - run ingest_polymarket.py first. "
            "Proceeding with Kalshi-only rows for this run, not failing.",
            POLYMARKET_LATEST,
        )
        return {}

    with POLYMARKET_LATEST.open(newline="", encoding="utf-8") as f:
        all_rows = list(csv.DictReader(f))

    by_race: dict[str, list[dict]] = defaultdict(list)
    matched_count = 0
    for r in all_rows:
        parsed = classify_polymarket_race(r.get("title"))
        if not parsed:
            continue
        race_id, state, chamber, district = parsed
        matched_count += 1
        by_race[race_id].append({**r, "_state": state, "_chamber": chamber, "_district": district})

    rows: dict[str, dict] = {}
    for race_id, candidates in by_race.items():
        dem_name, rep_name = electindex_names.get(race_id, ("", ""))
        first = candidates[0]

        dem_row = None
        rep_row = None
        unmatched_titles: list[str] = []

        for r in candidates:
            party = match_polymarket_candidate(r.get("title"), dem_name, rep_name)
            if party == "dem" and dem_row is None:
                dem_row = r
            elif party == "rep" and rep_row is None:
                rep_row = r
            elif party is None:
                unmatched_titles.append(r.get("title") or "")
            else:
                unmatched_titles.append(r.get("title") or "")

        state_restriction = POLYMARKET_POLITICS_STATE_RESTRICTIONS.get(first["_state"], "")

        row = {
            "race_id": race_id,
            "tier": (
                "Elections - US House District" if first["_chamber"] is None
                else "Elections - State Legislature District"
            ),
            "state": first["_state"],
            "chamber": first["_chamber"],
            "district": first["_district"],
            "polymarket_unmatched_candidates": "; ".join(t for t in unmatched_titles if t),
            "polymarket_total_open_candidates": len(candidates),
            "legal_footprint_polymarket": state_restriction,
        }

        if dem_row:
            row.update({
                "polymarket_dem_candidate_name": dem_row.get("title"),
                "polymarket_dem_market_id": dem_row.get("source_market_id"),
                "polymarket_dem_yes_bid": _to_float(dem_row.get("yes_bid")),
                "polymarket_dem_yes_ask": _to_float(dem_row.get("yes_ask")),
                "polymarket_dem_liquidity": _to_float(dem_row.get("liquidity")),
                "polymarket_dem_close_time": dem_row.get("close_time"),
                "polymarket_dem_status": dem_row.get("status"),
            })
        if rep_row:
            row.update({
                "polymarket_rep_candidate_name": rep_row.get("title"),
                "polymarket_rep_market_id": rep_row.get("source_market_id"),
                "polymarket_rep_yes_bid": _to_float(rep_row.get("yes_bid")),
                "polymarket_rep_yes_ask": _to_float(rep_row.get("yes_ask")),
                "polymarket_rep_liquidity": _to_float(rep_row.get("liquidity")),
                "polymarket_rep_close_time": rep_row.get("close_time"),
                "polymarket_rep_status": rep_row.get("status"),
            })

        rows[race_id] = row

    log.info(
        "Polymarket: %d of %d rows in %s structurally matched a "
        "down-ballot race, across %d distinct races.",
        matched_count, len(all_rows), POLYMARKET_LATEST.name, len(rows),
    )
    return rows


# --------------------------------------------------------------------------
# Liquidity labeling - now per matched candidate market, not per race.
# --------------------------------------------------------------------------

def liquidity_note_kalshi(row: dict, side: str) -> Optional[str]:
    ask_size = row.get(f"kalshi_{side}_yes_ask_size")
    bid_size = row.get(f"kalshi_{side}_yes_bid_size")
    ticker = row.get(f"kalshi_{side}_ticker")
    if ask_size is None and bid_size is None:
        return "no market" if ticker else None
    best_side = max(ask_size or 0.0, bid_size or 0.0)
    return "ok" if best_side >= MIN_LIQUID_KALSHI_CONTRACTS else "thin"


def liquidity_note_polymarket(row: dict, side: str) -> Optional[str]:
    liquidity = row.get(f"polymarket_{side}_liquidity")
    market_id = row.get(f"polymarket_{side}_market_id")
    if liquidity is None:
        return "no market" if market_id else None
    return "ok" if liquidity >= MIN_LIQUID_POLYMARKET_DOLLARS else "thin"


# --------------------------------------------------------------------------
# Join + output
# --------------------------------------------------------------------------

def join_rows(
    kalshi_rows: dict[str, dict], polymarket_rows: dict[str, dict],
    electindex_names: dict[str, tuple[str, str]], pulled_at: str,
) -> list[NormalizedRaceMarket]:
    all_race_ids = set(kalshi_rows) | set(polymarket_rows)
    out: list[NormalizedRaceMarket] = []

    for race_id in sorted(all_race_ids):
        k = kalshi_rows.get(race_id, {})
        p = polymarket_rows.get(race_id, {})
        dem_name, rep_name = electindex_names.get(race_id, ("", ""))

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
        merged["electindex_dem_name"] = dem_name
        merged["electindex_rep_name"] = rep_name

        merged["liquidity_note_kalshi_dem"] = liquidity_note_kalshi(merged, "dem")
        merged["liquidity_note_kalshi_rep"] = liquidity_note_kalshi(merged, "rep")
        merged["liquidity_note_polymarket_dem"] = liquidity_note_polymarket(merged, "dem")
        merged["liquidity_note_polymarket_rep"] = liquidity_note_polymarket(merged, "rep")
        merged["legal_footprint_kalshi"] = merged.get("legal_footprint_kalshi", "")
        merged["legal_footprint_polymarket"] = merged.get("legal_footprint_polymarket", "")
        merged["kalshi_unmatched_candidates"] = merged.get("kalshi_unmatched_candidates", "")
        merged["kalshi_total_open_candidates"] = merged.get("kalshi_total_open_candidates", 0)
        merged["polymarket_unmatched_candidates"] = merged.get("polymarket_unmatched_candidates", "")
        merged["polymarket_total_open_candidates"] = merged.get("polymarket_total_open_candidates", 0)
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
        "races_dem_matched": 0,
        "races_rep_matched": 0,
        "total_unmatched_candidates": 0,
        "ok": False,
    }

    log.info("=== Down-ballot politics market ingestion run starting (Session 5.1c: per-candidate matching) ===")

    try:
        electindex_names = load_electindex_names()

        series_list, tier_by_ticker = fetch_down_ballot_series()
        summary["kalshi_series_matched"] = len(series_list)

        kalshi_rows = build_kalshi_rows(series_list, tier_by_ticker, electindex_names)
        polymarket_rows = build_polymarket_rows(electindex_names)

        summary["kalshi_race_rows"] = len(kalshi_rows)
        summary["polymarket_race_rows"] = len(polymarket_rows)
        summary["races_both_venues"] = len(set(kalshi_rows) & set(polymarket_rows))

        rows = join_rows(kalshi_rows, polymarket_rows, electindex_names, pulled_at)
        summary["races_total"] = len(rows)
        summary["races_dem_matched"] = sum(
            1 for r in rows if r.kalshi_dem_candidate_name or r.polymarket_dem_candidate_name
        )
        summary["races_rep_matched"] = sum(
            1 for r in rows if r.kalshi_rep_candidate_name or r.polymarket_rep_candidate_name
        )
        summary["total_unmatched_candidates"] = sum(
            len([x for x in r.kalshi_unmatched_candidates.split("; ") if x])
            + len([x for x in r.polymarket_unmatched_candidates.split("; ") if x])
            for r in rows
        )
        summary["ok"] = True

        log.info(
            "Down-ballot politics: %d races total (%d on both venues), "
            "%d with a matched Dem candidate, %d with a matched Rep "
            "candidate, %d total unmatched candidate markets logged for "
            "review.",
            summary["races_total"], summary["races_both_venues"],
            summary["races_dem_matched"], summary["races_rep_matched"],
            summary["total_unmatched_candidates"],
        )
    except Exception as exc:  # noqa: BLE001
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
