"""
Session 5.1 - Shared Normalized Schema for Down-Ballot Political Race Markets

WHAT THIS FILE IS
------------------
schema_exchange.py (Session 3.1/3.1b) already captures Kalshi's and
Polymarket's down-ballot Elections markets as generic YES/NO order-book
contracts - correct for arbitrage (Track 2), which only needs the tradable
price and a loose text title to match venues against each other.

Track 4 needs something schema_exchange.py deliberately does not carry:
one row PER REAL RACE (not per venue-contract), with the race's state,
chamber, and district pulled out as real structured fields - because
Session 5.2's estimation model and this session's polling join both need
to key off "which race is this," not off a venue-specific ticker string.
Same reasoning Session 4.1 used when it added schema_weather.py alongside
schema_exchange.py rather than widening the shared schema a second time.

FIELD NOTES
------------------
- race_id: this project's own normalized join key, NOT any venue's native
  ID. Built by ingest_politics_markets.py from structural parsing of each
  venue's ticker/title (see that file's race_key_for_house_district() and
  race_key_for_state_leg()), and reused unchanged by
  ingest_polling_data.py so a market row and its polling estimate join on
  this single field. Format:
    US House:          "US-HOUSE-<STATE>-<DD>"       e.g. "US-HOUSE-MI-07"
    State Legislature:  "STATE-LEG-<STATE>-<CHAMBER>-<N>"
                                                       e.g. "STATE-LEG-PA-HOUSE-12"
  <STATE> is always the 2-letter USPS abbreviation, <DD> is always
  zero-padded to 2 digits (US House only), <CHAMBER> is one of
  HOUSE/SENATE/ASSEMBLY, and <N> is NOT zero-padded (matches ElectIndex's
  leg_races.csv district numbering, confirmed live 2026-09-07 - see
  ingest_polling_data.py's module docstring).
- tier: "US House District" or "State Legislature District" - the exact
  two tier labels ingest_kalshi.py's classify_down_ballot() already uses,
  kept identical here on purpose so a row's tier never needs re-deriving.
- One row = one real race. Either venue's columns may be entirely empty
  (None) if that race does not currently trade there - this is expected,
  not an error, since Session 3.1b confirmed neither venue lists every
  real down-ballot race.
- kalshi_yes_ask_size / kalshi_yes_bid_size: same real, populated Kalshi
  fields ingest_kalshi.py and ingest_weather_markets.py already rely on
  for liquidity - Kalshi's own liquidity_dollars field is not trusted
  here either (reads "0.0000" on every real market checked so far).
- polymarket_liquidity: Polymarket's own `liquidity` field, confirmed
  real and populated (per ingest_polymarket.py's docstring) - used
  directly for Polymarket-side liquidity, unlike the Kalshi side.
- liquidity_note_kalshi / liquidity_note_polymarket: a plain-language
  flag ("thin"/"ok"/"no market") written by ingest_politics_markets.py
  against the named MIN_LIQUID_* constants in that file, so a downstream
  reader never has to re-derive whether a race is actionable from the
  raw size numbers alone.
- legal_footprint_kalshi / legal_footprint_polymarket: a short, sourced
  note on any CONFIRMED, CURRENT state-level restriction specifically on
  political/election contracts at that venue (not general availability -
  see ingest_politics_markets.py's LEGAL_FOOTPRINT section for the full,
  dated, sourced findings this closes Open Decision #22 with). Empty
  string means no politics-specific restriction was found for that venue
  as of this session's check, not that none exists anywhere.
- pulled_at: ISO-8601 UTC timestamp of this specific run, same convention
  as every other ingestion script in this project.

WHAT IS DELIBERATELY NOT IN THIS SCHEMA YET
-----------------------------------------------
No polling/forecast probability field - that lives in
ingest_polling_data.py's own output CSV, joined by race_id, not merged
into this file. No fair-value comparison or CLV field - Session 5.2
(Estimation Engine) is where this project's own probability estimate
gets computed, matching the same ingestion/estimation boundary
schema_weather.py's docstring already draws for Track 3.
"""

from dataclasses import dataclass, asdict
from typing import Optional

NORMALIZED_POLITICS_COLUMNS = [
    "race_id",
    "tier",
    "state",
    "chamber",
    "district",
    "kalshi_ticker",
    "kalshi_title",
    "kalshi_yes_bid",
    "kalshi_yes_ask",
    "kalshi_no_bid",
    "kalshi_no_ask",
    "kalshi_yes_ask_size",
    "kalshi_yes_bid_size",
    "kalshi_close_time",
    "kalshi_status",
    "liquidity_note_kalshi",
    "legal_footprint_kalshi",
    "polymarket_market_id",
    "polymarket_title",
    "polymarket_yes_bid",
    "polymarket_yes_ask",
    "polymarket_no_bid",
    "polymarket_no_ask",
    "polymarket_liquidity",
    "polymarket_close_time",
    "polymarket_status",
    "liquidity_note_polymarket",
    "legal_footprint_polymarket",
    "pulled_at",
]


@dataclass
class NormalizedRaceMarket:
    """One row = one real down-ballot race, with each venue's real market
    data attached where that race currently trades there (either venue's
    columns may be None)."""

    race_id: str
    tier: str
    state: str
    chamber: Optional[str]
    district: str

    kalshi_ticker: Optional[str] = None
    kalshi_title: Optional[str] = None
    kalshi_yes_bid: Optional[float] = None
    kalshi_yes_ask: Optional[float] = None
    kalshi_no_bid: Optional[float] = None
    kalshi_no_ask: Optional[float] = None
    kalshi_yes_ask_size: Optional[float] = None
    kalshi_yes_bid_size: Optional[float] = None
    kalshi_close_time: Optional[str] = None
    kalshi_status: Optional[str] = None
    liquidity_note_kalshi: Optional[str] = None
    legal_footprint_kalshi: str = ""

    polymarket_market_id: Optional[str] = None
    polymarket_title: Optional[str] = None
    polymarket_yes_bid: Optional[float] = None
    polymarket_yes_ask: Optional[float] = None
    polymarket_no_bid: Optional[float] = None
    polymarket_no_ask: Optional[float] = None
    polymarket_liquidity: Optional[float] = None
    polymarket_close_time: Optional[str] = None
    polymarket_status: Optional[str] = None
    liquidity_note_polymarket: Optional[str] = None
    legal_footprint_polymarket: str = ""

    pulled_at: str = ""

    def as_row(self) -> dict:
        d = asdict(self)
        return {col: d.get(col) for col in NORMALIZED_POLITICS_COLUMNS}
