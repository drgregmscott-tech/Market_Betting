"""
Session 6.1 — Shared Normalized Schema for Sportsbook Player Props (DK/FD)

WHAT THIS FILE IS
------------------
DraftKings and FanDuel each return their sportsbook odds data in a different
shape (both undocumented public feeds, same situation Session 2.1 found for
the pick'em platforms). This file defines the ONE common row shape that both
platforms' raw data gets converted into, following the exact same pattern as
schema.py (Session 2.2) for the pick'em track, so Session 6.2's estimation
model and Session 6.3's CLV hook-in can work against a single stable format.

KEY DIFFERENCE FROM schema.py (pick'em)
-----------------------------------------
Pick'em platforms post a fixed line with a fixed payout multiplier — no vig
to separate out. A sportsbook prop posts American odds on each side (e.g.
Over -115, Under -105), and those odds already have the book's built-in vig
(profit margin) baked in. This schema stores the RAW American odds for both
sides so Session 6.2 can compute the no-vig ("de-vigged") true probability —
storing only one side's odds, or a single blended number, would throw away
the exact information the vig computation needs.

FIELD NOTES
-----------
- platform: "draftkings" or "fanduel" — literal string, set by the
  normalizer, not present in either platform's raw data.
- source_event_id / source_market_id / source_selection_id: the platform's
  own IDs for the game, the specific prop market, and the specific
  over/under selection within it. Kept as three separate IDs (not
  collapsed into one) because a single game has many markets, and a single
  market has two selections (over/under) — later sessions need to be able
  to join back to the exact selection a price came from.
- over_american_odds / under_american_odds: the raw American-odds price
  for each side (e.g. -115, +105), stored as signed integers. Vig
  extraction (Session 6.2) needs BOTH sides' raw price, not a pre-computed
  probability, so no conversion happens in this file.
- line: the numeric prop value (e.g. 24.5 receiving yards).
- prop_category: the state-regulation-relevant grouping (e.g.
  "player_performance", "player_touchdown", "game_alt_lines") — kept
  separate from stat_type because Session 6.1's legal-footprint check
  operates at this category level, not the individual stat-type level
  (see docs/sportsbook_props_legal_footprint.md).
"""

from dataclasses import dataclass, asdict
from typing import Optional

NORMALIZED_COLUMNS = [
    "platform",
    "source_event_id",
    "source_market_id",
    "source_selection_id",
    "player_name",
    "team",
    "sport",
    "stat_type",
    "prop_category",
    "line",
    "over_american_odds",
    "under_american_odds",
    "game_id",
    "game_start_time",
    "status",
    "pulled_at",
]


@dataclass
class NormalizedSportsbookProp:
    """One row of the common schema. Every ingestion normalizer (one per
    platform) must produce a list of these before writing any output file."""

    platform: str
    source_event_id: str
    source_market_id: str
    source_selection_id: str
    player_name: Optional[str]
    team: Optional[str]
    sport: Optional[str]
    stat_type: Optional[str]
    prop_category: Optional[str]
    line: Optional[float]
    over_american_odds: Optional[int]
    under_american_odds: Optional[int]
    game_id: Optional[str]
    game_start_time: Optional[str]
    status: Optional[str]
    pulled_at: str

    def as_row(self) -> dict:
        d = asdict(self)
        return {col: d.get(col) for col in NORMALIZED_COLUMNS}


def american_odds_to_implied_probability(odds: Optional[int]) -> Optional[float]:
    """Converts one side's American odds into its raw (vig-included)
    implied probability. This is NOT the true probability — the two sides'
    raw implied probabilities always sum to > 1.0 (that gap IS the vig).
    Session 6.2 removes the vig by normalizing both sides so they sum to
    exactly 1.0. Kept here (not duplicated later) since it's a pure,
    reusable conversion both this file's own tests and Session 6.2 need."""
    if odds is None:
        return None
    if odds > 0:
        return 100.0 / (odds + 100.0)
    if odds < 0:
        return -odds / (-odds + 100.0)
    return None  # 0 is not a valid American odds value


def same_market_group_key(platform: str, source_event_id: str, source_market_id: str) -> str:
    """Session 6.4 — the key that groups every selection belonging to the
    SAME real one-sided market (e.g. every player priced in one real
    "Anytime TD Scorer" market for one real game) so their raw implied
    probabilities can be normalized against each other as a group, instead
    of against a nonexistent "under" side. `source_market_id` already
    identifies that exact real market on each normalized row (DraftKings'
    own `marketId`, confirmed in `ingest_dk_props.py`'s captured data) —
    this function does not add a new field, it just names the existing
    three fields' combination so the grouping logic in
    `sportsbook_props_model.py` (and its tests) has one shared, reusable
    definition rather than three separate ad-hoc groupbys."""
    return f"{platform}|{source_event_id}|{source_market_id}"


def normalize_field_vig(raw_implied_probs: list[float]) -> list[float]:
    """Session 6.4 — the N-way generalization of `american_odds_to_
    implied_probability`'s two-sided de-vig above, for a ONE-SIDED market
    with more than two priced selections (e.g. every player in a real
    "Anytime TD Scorer" market). Each selection's raw implied probability
    already includes the book's vig; summed across every selection in the
    same real market, that field's raw probabilities always add up to
    something above 1.0 (same vig gap, just spread across many prices
    instead of two). Dividing each one by the group's real total removes
    that field vig honestly, without inventing a number for any
    individual price. Returns an empty list unchanged; returns the input
    unchanged (never divides by zero) if the real group total is not
    strictly positive."""
    total = sum(raw_implied_probs)
    if total <= 0:
        return list(raw_implied_probs)
    return [p / total for p in raw_implied_probs]
