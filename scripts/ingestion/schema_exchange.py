"""
Session 3.1 / 3.2 - Shared Normalized Schema for Exchange-Style (YES/NO
Contract) Venues

WHAT THIS FILE IS
------------------
Session 2.2's schema.py defined one common row shape for the two pick'em
platforms (PrizePicks, Underdog), because both of those platforms price a
prop as ONE fixed line with an over/under choice. Kalshi and Polymarket are
built on a different mechanism entirely: a real order book with two live,
separately-priced sides (YES and NO), each with its own bid and its own ask.
This is the "exchange-style pricing" extension Session 3.1's ROADMAP.md card
calls for - a second, parallel schema, not a forced fit into schema.py's
single-line shape.

WHY A SEPARATE FILE, NOT A CHANGED schema.py
-----------------------------------------------
Forcing exchange pricing into schema.py's NormalizedProp (which has one
"line" field and one payout multiplier) would either lose real information
(the bid/ask spread - the actual tradable price, not just a last-trade
number) or require every existing Track 1 file to change shape for a
feature only Track 2 needs. This project's standing "no silent adjustments"
rule (see SESSION_LOG.md) is why the two schemas are kept explicitly
separate here instead: Track 1's data shape does not change, and Track 2
gets a shape that matches its own real mechanism.

FIELD NOTES (traced back to each platform's real, confirmed field names -
Session 3.1, live pull 2026-09-04; extended Session 3.2, live pull
2026-09-05)
-----------------------------------------------------------------------
- platform: "kalshi" or "polymarket" - literal string, set by the
  normalizer.
- source_market_id: the platform's own ID for this specific contract.
  Kalshi: markets[].ticker (e.g. "KXHIGHNY-26SEP05-T86"). Polymarket:
  markets[].conditionId (e.g. "0x064d33e3...").
- event_id: groups related contracts under one real-world question.
  Kalshi: markets[].event_ticker. Polymarket: the parent event's "id" field
  (a market's conditionId is per-contract; its event grouping is one level
  up in the events[] response).
- title: the human-readable question. Kalshi: markets[].title. Polymarket:
  markets[].question.
- category: Kalshi: not returned directly on the market object itself -
  carried on the parent series (not pulled by this file's markets-only
  call; filled in by ingest_kalshi.py's run() using a ticker->category map
  built from the separate /series pull - see that file). Polymarket:
  events[].category (e.g. "Sports", "Politics").
- yes_bid / yes_ask / no_bid / no_ask: the four real, separately quoted
  prices that make an order book an order book, not a single line. Kalshi:
  markets[].yes_bid_dollars / yes_ask_dollars / no_bid_dollars /
  no_ask_dollars - already returned as decimal-dollar strings (e.g.
  "0.3300"), confirmed live 2026-09-04. Polymarket: the Gamma API's
  markets[] object exposes bestBid/bestAsk as single-sided (YES-side)
  numbers, not four explicit yes/no prices the way Kalshi does - no_bid and
  no_ask are therefore DERIVED here as (1 - yes_ask) and (1 - yes_bid)
  respectively, per the standard complementary-probability relationship
  for a binary contract. This derivation is called out explicitly in
  ingest_polymarket.py's normalizer, not done silently. Confirmed this
  session (2026-09-05) against real Kalshi numbers too, even though Kalshi
  publishes no_bid/no_ask as separate fields: on the real KXHOUSEMO5-26-R
  market, yes_bid=0.19/yes_ask=0.20 and no_bid=0.80/no_ask=0.81, and
  0.80 = 1 - 0.20, 0.81 = 1 - 0.19 exactly - Kalshi's own published
  no-side fields are the same complementary math, not independent
  information, because there is only one real order book per market.
- yes_ask_size / yes_bid_size (ADDED Session 3.2): the real number of
  contracts resting at the best YES ask / best YES bid. Kalshi:
  markets[].yes_ask_size_fp / yes_bid_size_fp - confirmed live and
  POPULATED with real, non-zero numbers on every real market pulled this
  session (e.g. 116.02 contracts on a real KXHOUSEMO5 leg). Polymarket:
  the Gamma API's market summary does not expose an equivalent top-of-book
  size field, so these are left None for Polymarket rows - a named gap,
  not a silent omission. See liquidity_check.py's Session 3.2 notes for
  exactly why these fields were added: Kalshi's `liquidity_dollars` field
  (below) was found to read "0.0000" on every real market checked this
  session, making it useless as a liquidity signal for Kalshi specifically,
  while these size fields are real and populated.
- volume: Kalshi: markets[].volume_fp. Polymarket: markets[].volume (a
  string in the raw payload - must be converted to float, the same
  "don't silently mis-type a numeric string" lesson Session 2.2 already
  learned once for Underdog's stat_value field).
- liquidity: Kalshi: markets[].liquidity_dollars - confirmed LIVE and
  UNRELIABLE as of Session 3.2 (2026-09-05): this field read "0.0000" on
  every single real Kalshi market pulled this session (multiple weather
  strikes on KXHIGHPHIL, both legs of the real KXHOUSEMO5 down-ballot
  race), including markets with substantial real size resting on the book.
  Still captured here for completeness/future-proofing (if Kalshi ever
  starts populating it correctly, this field will pick that up
  automatically), but detector.py's liquidity_check.py does NOT rely on
  this field for Kalshi rows - it uses yes_ask_size/yes_bid_size instead.
  Polymarket: markets[].liquidity (also a string in the raw payload) -
  confirmed LIVE and REAL as of Session 3.2 (e.g. $9,746.02 on a real
  Polymarket down-ballot market), unlike Kalshi's dead field. This
  platform-specific difference in the same nominal field is real, not a
  parsing bug - it is why liquidity_check.py treats the two venues
  asymmetrically rather than applying one shared formula to both.
- close_time: Kalshi: markets[].close_time. Polymarket: markets[].endDate.
- status: Kalshi: markets[].status (e.g. "active"). Polymarket: derived
  from the market's own "active"/"closed" booleans, normalized to a single
  string ("active" / "closed") so both platforms' status field means the
  same thing in this common schema.
- pulled_at: UTC timestamp set by THIS pipeline at fetch time, same
  convention as schema.py.

WHAT IS DELIBERATELY NOT IN THIS SCHEMA YET
-----------------------------------------------
Fee/vig figures are NOT included as a per-row field here. Session 3.2
(Arbitrage Detection Logic) is the session that applies each venue's fee
schedule when evaluating a flagged opportunity - see ROADMAP.md and
detector.py. Baking a fee number into the ingestion row itself would mean
every future fee-schedule change requires re-running ingestion to matter,
rather than being picked up automatically by the detection layer. Keeping
the two concerns separate is intentional, not an oversight.

Full order-book DEPTH (size at the second-best price, third-best price,
etc.) is also not in this schema - only top-of-book (best bid/ask, plus
Session 3.2's added top-of-book size fields for Kalshi). See
liquidity_check.py's module docstring for what this limits and what a
future session pulling real depth-of-book data would unlock.
"""

from dataclasses import dataclass, asdict
from typing import Optional

NORMALIZED_EXCHANGE_COLUMNS = [
    "platform",
    "source_market_id",
    "event_id",
    "title",
    "category",
    "yes_bid",
    "yes_ask",
    "no_bid",
    "no_ask",
    "yes_ask_size",
    "yes_bid_size",
    "volume",
    "liquidity",
    "close_time",
    "status",
    "pulled_at",
]


@dataclass
class NormalizedContract:
    """One row of the common exchange-venue schema. Every ingestion
    normalizer (one per exchange venue) must produce a list of these before
    writing any output file - parallel in spirit to schema.py's
    NormalizedProp, but shaped for order-book pricing instead of a single
    fixed line.

    yes_ask_size and yes_bid_size default to None (added Session 3.2, after
    schema_exchange.py already existed) so that any existing normalizer
    call built before this session - which won't pass these two keyword
    arguments - still works without modification. ingest_kalshi.py was
    updated this session to actually populate them from real data;
    ingest_polymarket.py was not (no equivalent field exists in Polymarket's
    Gamma API market summary), so Polymarket rows carry None here by
    design, not by oversight."""

    platform: str
    source_market_id: str
    event_id: Optional[str]
    title: Optional[str]
    category: Optional[str]
    yes_bid: Optional[float]
    yes_ask: Optional[float]
    no_bid: Optional[float]
    no_ask: Optional[float]
    volume: Optional[float]
    liquidity: Optional[float]
    close_time: Optional[str]
    status: Optional[str]
    pulled_at: str
    yes_ask_size: Optional[float] = None
    yes_bid_size: Optional[float] = None

    def as_row(self) -> dict:
        """Returns a plain dict with keys in NORMALIZED_EXCHANGE_COLUMNS
        order - what gets written to CSV."""
        d = asdict(self)
        return {col: d.get(col) for col in NORMALIZED_EXCHANGE_COLUMNS}
