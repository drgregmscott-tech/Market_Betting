"""
Session 5.1 - Shared Normalized Schema for Down-Ballot Political Race Markets
Session 5.1c PATCH (this session) - candidate identity, not just race
identity, is now captured. See module docstring's "SESSION 5.1c PATCH"
section below for why this changed and what broke without it.

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

SESSION 5.1c PATCH - CANDIDATE IDENTITY IS NOW REQUIRED, NOT OPTIONAL
-----------------------------------------------------------------------
Found live, this session, while preparing Session 5.2's estimation model:
Kalshi's down-ballot race markets are NOT one YES/NO contract per race.
Each race is a SERIES with one open market PER CANDIDATE (confirmed live
against the real KXCASEN26 series, 2026-09-08: 8 open candidate markets
for one race - Wendy Carrillo, Sarah Rascon, Sang Masog, Sara Hernandez,
Paul A. Bowers, and 3 others). The real candidate name lives on each
individual MARKET object's `yes_sub_title` field (confirmed live,
2026-09-08), NOT on the series-level title, which is generic ("Who will
win the 2026 California State Senate District 26 election?") and does not
name a candidate at all.

The original version of this file (and of ingest_politics_markets.py)
stored exactly one Kalshi price and one Polymarket price per race, kept
by taking whichever market Kalshi's API happened to return first for that
series. That price had no recorded link to a specific candidate or party.
Because ElectIndex (this project's polling source, see
ingest_polling_data.py) always reports a Democrat-win-probability and a
Republican-win-probability for the same race, Session 5.2's model would
have had no reliable way to know which party the kept market's price
actually belonged to - it could just as easily have been a losing minor
candidate's contract as the Democrat's or the Republican's, with no way
to tell after the fact. This would have let mismatched numbers feed
straight into the model with no error raised - caught before any model
code was written, not after.

THE FIX: match each open candidate market to a party by NAME, using
ElectIndex's own published candidate names (`dem_name`/`rep_name` -
confirmed live in both of ElectIndex's real source tables,
races_summary.csv and leg_races.csv, 2026-09-08) as the source of truth
for who is running as which party. ingest_polling_data.py (patched this
session) now carries those two name fields through into
polling_estimates_latest.csv; ingest_politics_markets.py (patched this
session) reads that file and matches every open candidate market's
`yes_sub_title` against it by last name. A market that matches neither
name is a real, named third-party/minor candidate - kept and logged in
this file's own `*_unmatched_candidates` field, never silently dropped,
but also never guessed into a Dem/Rep slot it wasn't matched to.

FIELD NOTES
------------------
- race_id / tier / state / chamber / district: unchanged from the
original version of this file - see git history for that reasoning if
needed.
- electindex_dem_name / electindex_rep_name: the real candidate names
this race's row was matched against, carried through from
polling_estimates_latest.csv so a human (or a future session) can
spot-check a match without re-joining files. Empty string if
ElectIndex's own row had no candidate listed for that party (a real,
observed case - see ingest_polling_data.py's Session 5.1c patch notes
for the real AK-HD-1 example, an uncontested race with no real
Democratic candidate).
- kalshi_dem_* / kalshi_rep_*: the specific open Kalshi market matched to
that party's candidate name, or all-None if no open Kalshi market
matched (no Kalshi market for this race, or this party's candidate
isn't running/has no market open).
- kalshi_unmatched_candidates: candidate names (semicolon-separated) of
every OTHER open Kalshi market for this race that did not match either
party's name - real minor/third-party candidates or a name-matching
miss, logged so a human can review, never dropped with no record.
- kalshi_total_open_candidates: total count of open Kalshi candidate
markets found for this race (dem + rep + unmatched), so a reader can
see at a glance how contested/multi-candidate a real race is (the real
KXCASEN26 example above has 8).
- polymarket_dem_* / polymarket_rep_* / polymarket_unmatched_candidates /
polymarket_total_open_candidates: same structure, Polymarket side.
Polymarket's own candidate-naming convention on down-ballot markets was
NOT confirmed live this session (same open gap ingest_politics_markets.py's
original module docstring already named for state-legislature titles) -
ingest_politics_markets.py's Session 5.1c patch applies the same
name-matching logic defensively, and logs unmatched at the same rate
Kalshi's does, as a real, honest signal of whether it's working, not an
assumption that it does.
- liquidity_note_kalshi_dem / _rep, liquidity_note_polymarket_dem / _rep:
same "thin"/"ok"/"no market" convention as the original file, now
computed once per matched candidate market rather than once per race.
- legal_footprint_kalshi / legal_footprint_polymarket: unchanged - this
is a venue-level restriction, not a candidate-level one.
- pulled_at: ISO-8601 UTC timestamp of this specific run.

WHAT IS DELIBERATELY NOT IN THIS SCHEMA YET
-----------------------------------------------
No fair-value comparison or CLV field - Session 5.2 (Estimation Engine)
computes this project's own probability estimate downstream of this file,
matching the same ingestion/estimation boundary schema_weather.py's
docstring already draws for Track 3.
No support for races with more than two ElectIndex-tracked parties
(independents, third parties with their own real chance) - ElectIndex
itself only forecasts dem_prob/rep_prob for these tiers (see
ingest_polling_data.py), so this project has no independent probability
to compare a minor candidate's market price against yet. Their markets
are captured (kalshi_unmatched_candidates / polymarket_unmatched_candidates)
so they are visible, not lost, but Session 5.2 does not estimate them.
"""

from dataclasses import dataclass, asdict
from typing import Optional

NORMALIZED_POLITICS_COLUMNS = [
    "race_id",
    "tier",
    "state",
    "chamber",
    "district",

    "electindex_dem_name",
    "electindex_rep_name",

    "kalshi_dem_candidate_name",
    "kalshi_dem_ticker",
    "kalshi_dem_yes_bid",
    "kalshi_dem_yes_ask",
    "kalshi_dem_yes_ask_size",
    "kalshi_dem_yes_bid_size",
    "kalshi_dem_close_time",
    "kalshi_dem_status",
    "liquidity_note_kalshi_dem",

    "kalshi_rep_candidate_name",
    "kalshi_rep_ticker",
    "kalshi_rep_yes_bid",
    "kalshi_rep_yes_ask",
    "kalshi_rep_yes_ask_size",
    "kalshi_rep_yes_bid_size",
    "kalshi_rep_close_time",
    "kalshi_rep_status",
    "liquidity_note_kalshi_rep",

    "kalshi_unmatched_candidates",
    "kalshi_total_open_candidates",
    "legal_footprint_kalshi",

    "polymarket_dem_candidate_name",
    "polymarket_dem_market_id",
    "polymarket_dem_yes_bid",
    "polymarket_dem_yes_ask",
    "polymarket_dem_liquidity",
    "polymarket_dem_close_time",
    "polymarket_dem_status",
    "liquidity_note_polymarket_dem",

    "polymarket_rep_candidate_name",
    "polymarket_rep_market_id",
    "polymarket_rep_yes_bid",
    "polymarket_rep_yes_ask",
    "polymarket_rep_liquidity",
    "polymarket_rep_close_time",
    "polymarket_rep_status",
    "liquidity_note_polymarket_rep",

    "polymarket_unmatched_candidates",
    "polymarket_total_open_candidates",
    "legal_footprint_polymarket",

    "pulled_at",
]


@dataclass
class NormalizedRaceMarket:
    """One row = one real down-ballot race, with each venue's Democratic-
    and Republican-candidate markets attached separately (matched by real
    candidate name against ElectIndex - see module docstring's "SESSION
    5.1c PATCH" section). Either party's columns, or an entire venue's
    columns, may be None/empty if that candidate or venue has no open
    market for this race - expected, not an error."""

    race_id: str
    tier: str
    state: str
    chamber: Optional[str]
    district: str

    electindex_dem_name: str = ""
    electindex_rep_name: str = ""

    kalshi_dem_candidate_name: Optional[str] = None
    kalshi_dem_ticker: Optional[str] = None
    kalshi_dem_yes_bid: Optional[float] = None
    kalshi_dem_yes_ask: Optional[float] = None
    kalshi_dem_yes_ask_size: Optional[float] = None
    kalshi_dem_yes_bid_size: Optional[float] = None
    kalshi_dem_close_time: Optional[str] = None
    kalshi_dem_status: Optional[str] = None
    liquidity_note_kalshi_dem: Optional[str] = None

    kalshi_rep_candidate_name: Optional[str] = None
    kalshi_rep_ticker: Optional[str] = None
    kalshi_rep_yes_bid: Optional[float] = None
    kalshi_rep_yes_ask: Optional[float] = None
    kalshi_rep_yes_ask_size: Optional[float] = None
    kalshi_rep_yes_bid_size: Optional[float] = None
    kalshi_rep_close_time: Optional[str] = None
    kalshi_rep_status: Optional[str] = None
    liquidity_note_kalshi_rep: Optional[str] = None

    kalshi_unmatched_candidates: str = ""
    kalshi_total_open_candidates: int = 0
    legal_footprint_kalshi: str = ""

    polymarket_dem_candidate_name: Optional[str] = None
    polymarket_dem_market_id: Optional[str] = None
    polymarket_dem_yes_bid: Optional[float] = None
    polymarket_dem_yes_ask: Optional[float] = None
    polymarket_dem_liquidity: Optional[float] = None
    polymarket_dem_close_time: Optional[str] = None
    polymarket_dem_status: Optional[str] = None
    liquidity_note_polymarket_dem: Optional[str] = None

    polymarket_rep_candidate_name: Optional[str] = None
    polymarket_rep_market_id: Optional[str] = None
    polymarket_rep_yes_bid: Optional[float] = None
    polymarket_rep_yes_ask: Optional[float] = None
    polymarket_rep_liquidity: Optional[float] = None
    polymarket_rep_close_time: Optional[str] = None
    polymarket_rep_status: Optional[str] = None
    liquidity_note_polymarket_rep: Optional[str] = None

    polymarket_unmatched_candidates: str = ""
    polymarket_total_open_candidates: int = 0
    legal_footprint_polymarket: str = ""

    pulled_at: str = ""

    def as_row(self) -> dict:
        d = asdict(self)
        return {col: d.get(col) for col in NORMALIZED_POLITICS_COLUMNS}
