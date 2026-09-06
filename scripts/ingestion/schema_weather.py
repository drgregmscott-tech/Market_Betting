"""
Session 4.1 - Shared Normalized Schema for Kalshi Weather-Threshold Contracts

WHAT THIS FILE IS
------------------
schema_exchange.py (Session 3.1) already captures Kalshi's Climate and
Weather + Commodities markets as generic YES/NO order-book contracts. That
schema is correct for arbitrage (Track 2), which only needs the tradable
price. It does NOT capture the fields a weather ESTIMATION model (Track 3,
Session 4.2) actually needs: the specific numeric temperature threshold
each contract is asking about, which city, and which calendar day.

Rather than widen schema_exchange.py (used live by the arbitrage pipeline
since Session 3.4 - changing its shape risks a silent break there), this
is a second, parallel schema, same pattern Session 3.1 used when it added
schema_exchange.py alongside schema.py rather than forcing pick'em and
exchange pricing into one shape.

FIELD NOTES (confirmed live against Kalshi's real API, 2026-09-06)
-----------------------------------------------------------------------
- series_ticker / market_ticker: e.g. series "KXHIGHPHIL", market
  "KXHIGHPHIL-26SEP07-T85". The market ticker embeds the target date
  (26SEP07 = 2026-09-07) and the threshold (T85 = "greater than 85",
  B84.5 = "between 84 and 85") - confirmed live, not assumed from docs.
- city_label: the human city name as this project's station_map.py names
  it (e.g. "Philadelphia"), NOT Kalshi's own series title text, which is
  inconsistent in format across series (see station_map.py's own notes).
- station_id: the official station code (e.g. "KPHL") this project has
  mapped the series to - see station_map.py. This is the SAME station
  code used to query NWS's public API for both forecast and actual
  observed data (Session 4.2 onward), so a market row and its NWS data
  join on this single field.
- strike_type / floor_strike / cap_strike: Kalshi's own structured strike
  fields (markets[].strike_type, .floor_strike, .cap_strike), confirmed
  live. "greater" contracts carry only floor_strike, "less" only
  cap_strike, "between" carry both. This is real structured data Kalshi
  itself computes - far more reliable than parsing the human-readable
  title text for a number.
- target_date: the calendar date (YYYY-MM-DD) this contract's temperature
  question is actually about, parsed from the market ticker's embedded
  date segment. This is the date this project's NWS observation pull
  must be compared against - NOT close_time or expiration_time, both of
  which are administrative timestamps that fall on or after this date,
  not the event date itself (confirmed live: a market with target_date
  2026-09-07 had close_time 2026-09-08T05:00:00Z and expiration_time
  2026-09-14T14:00:00Z).
- settlement_source_name / settlement_source_url: pulled once per series
  from GET /series/{ticker} (not per-market - Kalshi returns this at the
  series level). Kept on every row anyway (denormalized) so a later
  script reading only the markets CSV never has to make a second lookup
  to know where a given row's real answer will come from.
- yes_bid / yes_ask / no_bid / no_ask / yes_ask_size / yes_bid_size /
  volume / liquidity: same fields and same real caveats as
  schema_exchange.py (Kalshi's liquidity_dollars reads 0.0000 on every
  real market checked so far - not trusted here either, same as Track 2).
- close_time / status / pulled_at: same meaning as schema_exchange.py.

WHAT IS DELIBERATELY NOT IN THIS SCHEMA YET
-----------------------------------------------
No probability estimate, no fair-value comparison, no CLV field - this is
an ingestion-layer schema only. Session 4.2 (Estimation Engine) is where
this project's own probability estimate gets computed and compared
against yes_ask/yes_bid; baking that in here would blur the same
ingestion/estimation boundary schema_exchange.py's docstring already
draws for Track 2.
"""

from dataclasses import dataclass, asdict
from typing import Optional

NORMALIZED_WEATHER_COLUMNS = [
    "series_ticker",
    "market_ticker",
    "city_label",
    "station_id",
    "target_date",
    "strike_type",
    "floor_strike",
    "cap_strike",
    "settlement_source_name",
    "settlement_source_url",
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
class NormalizedWeatherMarket:
    """One row = one real Kalshi weather-threshold contract, joinable to
    this project's NWS ingestion output on (station_id, target_date)."""

    series_ticker: str
    market_ticker: str
    city_label: str
    station_id: Optional[str]
    target_date: Optional[str]
    strike_type: Optional[str]
    floor_strike: Optional[float]
    cap_strike: Optional[float]
    settlement_source_name: Optional[str]
    settlement_source_url: Optional[str]
    yes_bid: Optional[float]
    yes_ask: Optional[float]
    no_bid: Optional[float]
    no_ask: Optional[float]
    yes_ask_size: Optional[float]
    yes_bid_size: Optional[float]
    volume: Optional[float]
    liquidity: Optional[float]
    close_time: Optional[str]
    status: Optional[str]
    pulled_at: str

    def as_row(self) -> dict:
        d = asdict(self)
        return {col: d.get(col) for col in NORMALIZED_WEATHER_COLUMNS}
