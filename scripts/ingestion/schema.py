"""
Session 2.2 — Shared Normalized Schema for Pick'em Platform Data

WHAT THIS FILE IS
------------------
PrizePicks and Underdog Fantasy each return their prop data in a different
shape (confirmed in Session 2.1 — see /docs/research/endpoint_schemas.md).
This file defines the ONE common row shape that both platforms' raw data
gets converted into, so every later session (2.3's estimation model, 2.4's
CLV logger, and beyond) can work against a single, stable format instead of
two different ones.

Every field below is either present directly in both platforms' raw data, or
can be built from it. If a future platform is added and is missing a field,
that field should be left as None (not skipped) so every row always has the
same columns.

FIELD NOTES (traced back to Session 2.1's real captured field names)
-----------------------------------------------------------------------
- platform: "prizepicks" or "underdog" — literal string, set by the
  normalizer, not present in either platform's raw data.
- source_line_id: the platform's own ID for this specific prop line.
  PrizePicks: data[].id. Underdog: over_under_lines[].id.
- player_name: PrizePicks: included[type=new_player].attributes.display_name
  (note the field is named "new_player", not "player" — a real naming quirk
  found in Session 2.1). Underdog: players[].attributes name field, joined
  via appearances[].player_id.
- stat_type: PrizePicks: attributes.stat_display_name or stat_type.
  Underdog: over_under[].appearance_stat / display_stat.
- line: the numeric prop value. PrizePicks: attributes.line_score (already
  numeric). Underdog: over_under_lines[].stat_value — Session 2.1 found this
  is returned as a STRING (e.g. "8.5"), so the normalizer must convert it to
  a float. This conversion is the single most important correctness step in
  this file, since a silently-unconverted string would break any later
  numeric comparison against the estimation model's own probability output.
- game_start_time: PrizePicks: included[type=game].attributes.start_time.
  Underdog: games[].attributes start time, joined via appearances.match_id.
- status: PrizePicks: attributes.status. Underdog: over_under_lines[].status.
  Kept as a raw string (not enumerated) since Session 2.1 did not capture
  every possible value either platform can return.
- pulled_at: UTC timestamp set by THIS pipeline at fetch time, not by the
  platform. This is what lets later sessions ask "how fresh was this row
  when it was flagged."
- game_matchup: FIX (2026-09-11, replaces the old per-player `team` field):
  a compact "Away @ Home" string for the specific game this prop belongs to
  (e.g. "CLE @ JAC"), not the player's own team name. Chosen over `team`
  because it needs no per-player team_id resolution at all -- both
  platforms already carry a ready-made matchup string directly on the GAME
  record itself. PrizePicks: built from included[type=game]'s
  away_team_data/home_team_data relationships, joined to
  included[type=team].attributes.abbreviation. Underdog: games[]/
  solo_games[].short_title (falls back to abbreviated_title, then title,
  then full_team_names_title if short_title is missing). None for a prop
  whose game has no real two-side matchup at all (a season-long futures
  market, or an individual event like a race) -- a real, stated gap, not a
  guess.
- odds_type: PrizePicks-only (attributes.odds_type). PrizePicks offers more
  than one line per player/stat: "standard" (the default line most people
  mean when they say "the line"), plus "demon" and "goblin" alt-lines
  priced at different, real payout multipliers PrizePicks does not publish
  in this response. Found real and necessary 2026-09-11: a player's Demon
  and Goblin projections were being ingested as ordinary rows with no way
  to tell them apart from the Standard one, and pickem_model.py's flat 50%
  implied-probability assumption (which is only defensible for a Standard
  line) was being applied to them too -- producing a fabricated edge and
  surfacing the wrong line as "the" flagged opportunity. None otherwise
  (including for every Underdog row -- Underdog has no equivalent
  concept in this project's ingested data).
"""

from dataclasses import dataclass, asdict
from typing import Optional

# Column order used for every CSV/output file. Keeping this as one explicit
# list (rather than relying on dict insertion order) means the column order
# can never silently drift between platforms or between runs.
NORMALIZED_COLUMNS = [
    "platform",
    "source_line_id",
    "player_name",
    "game_matchup",
    "sport",
    "stat_type",
    "line",
    "over_payout_multiplier",
    "under_payout_multiplier",
    "game_id",
    "game_start_time",
    "status",
    "odds_type",
    "pulled_at",
]


@dataclass
class NormalizedProp:
    """One row of the common schema. Every ingestion normalizer (one per
    platform) must produce a list of these before writing any output file."""

    platform: str
    source_line_id: str
    player_name: Optional[str]
    game_matchup: Optional[str]
    sport: Optional[str]
    stat_type: Optional[str]
    line: Optional[float]
    over_payout_multiplier: Optional[float]
    under_payout_multiplier: Optional[float]
    game_id: Optional[str]
    game_start_time: Optional[str]
    status: Optional[str]
    odds_type: Optional[str]
    pulled_at: str

    def as_row(self) -> dict:
        """Returns a plain dict with keys in NORMALIZED_COLUMNS order —
        what gets written to CSV."""
        d = asdict(self)
        return {col: d.get(col) for col in NORMALIZED_COLUMNS}
