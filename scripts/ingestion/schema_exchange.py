"""
Session 3.1 — Shared Normalized Schema for Exchange-Style (YES/NO Contract) Venues

WHAT THIS FILE IS
------------------
Session 2.2's schema.py defined one common row shape for the two pick'em
platforms (PrizePicks, Underdog), because both of those platforms price a
prop as ONE fixed line with an over/under choice. Kalshi and Polymarket are
built on a different mechanism entirely: a real order book with two live,
separately-priced sides (YES and NO), each with its own bid and its own ask.
This is the "exchange-style pricing" extension Session 3.1's ROADMAP.md card
calls for — a second, parallel schema, not a forced fit into schema.py's
single-line shape.

WHY A SEPARATE FILE, NOT A CHANGED schema.py
-----------------------------------------------
Forcing exchange pricing into schema.py's NormalizedProp (which has one
"line" field and one payout multiplier) would either lose real information
(the bid/ask spread — the actual tradable price, not just a last-trade
number) or require every existing Track 1 file to change shape for a
feature only Track 2 needs. This project's standing "no silent adjustments"
rule (see SESSION_LOG.md) is why the two schemas are kept explicitly
separate here instead: Track 1's data shape does not change, and Track 2
gets a shape that matches its own real mechanism.

FIELD NOTES (traced back to each platform's real, confirmed field names —
Session 3.1, live pull 2026-09-04)
-----------------------------------------------------------------------
- platform: "kalshi" or "polymarket" — literal string, set by the
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
- category: Kalshi: not returned directly on the market object itself —
  carried on the parent series (not pulled by this file's markets-only
  call; left None here, a known, named gap, not a silent omission).
  Polymarket: events[].category (e.g. "Sports", "Politics").
- yes_bid / yes_ask / no_bid / no_ask: the four real, separately quoted
  prices that make an order book an order book, not a single line. Kalshi:
  markets[].yes_bid_dollars / yes_ask_dollars / no_bid_dollars /
  no_ask_dollars — already returned as decimal-dollar strings (e.g.
  "0.3300"), confirmed live 2026-09-04. Polymarket: the Gamma API's
  markets[] object exposes bestBid/bestAsk as single-sided (YES-side)
  numbers, not four explicit yes/no prices the way Kalshi does — no_bid and
  no_ask are therefore DERIVED here as (1 - yes_ask) and (1 - yes_bid)
  respectively, per the standard complementary-probability relationship
  for a binary contract. This derivation is called out explicitly in
  ingest_polymarket.py's normalizer, not done silently.
- volume: Kalshi: markets[].volume_fp. Polymarket: markets[].volume (a
  string in the raw payload — must be converted to float, the same
  "don't silently mis-type a numeric string" lesson Session 2.2 already
  learned once for Underdog's stat_value field).
- liquidity: Kalshi: markets[].liquidity_dollars. Polymarket:
  markets[].liquidity (also a string in the raw payload).
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
schedule when evaluating a flagged opportunity — see ROADMAP.md. Baking a
fee number into the ingestion row itself would mean every future fee-
schedule change requires re-running ingestion to matter, rather than being
picked up automatically by the detection layer. Keeping the two concerns
separate is intentional, not an oversight.
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
    writing any output file — parallel in spirit to schema.py's
    NormalizedProp, but shaped for order-book pricing instead of a single
    fixed line."""

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

    def as_row(self) -> dict:
        """Returns a plain dict with keys in NORMALIZED_EXCHANGE_COLUMNS
        order — what gets written to CSV."""
        d = asdict(self)
        return {col: d.get(col) for col in NORMALIZED_EXCHANGE_COLUMNS}
