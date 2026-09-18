"""
Session 2.56 -- adjusted_odds is carried from the PrizePicks feed into the
normalized rows (see schema.py's adjusted_odds note). Pure functions only: no
files are read or written.

Run: python -m pytest scripts/ingestion/test_adjusted_odds.py -v
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import ingest_pickem as pipeline  # noqa: E402
import schema  # noqa: E402


def _payload(adjusted):
    attrs = {
        "stat_display_name": "Points", "stat_type": "Points", "line_score": 27.5,
        "status": "pre_game", "start_time": "2026-08-30T00:00:00Z", "odds_type": "standard",
    }
    if adjusted != "omit":
        attrs["adjusted_odds"] = adjusted
    return {"data": [{"type": "projection", "id": "pp-1", "attributes": attrs, "relationships": {}}], "included": []}


def test_column_exists_in_the_normalized_schema():
    assert "adjusted_odds" in schema.NORMALIZED_COLUMNS
    assert schema.NORMALIZED_COLUMNS.index("adjusted_odds") == schema.NORMALIZED_COLUMNS.index("allowed_wager_types") + 1


def test_prizepicks_adjusted_odds_true_false_and_missing_are_kept_as_is():
    for value, expected in [(True, True), (False, False), ("omit", None)]:
        rows = pipeline.normalize_prizepicks(_payload(value), "2026-09-18T00:00:00Z")
        assert len(rows) == 1
        assert rows[0].adjusted_odds is expected, (value, rows[0].adjusted_odds)
        assert rows[0].as_row()["adjusted_odds"] is expected


def test_underdog_rows_have_no_adjusted_odds():
    payload = {
        "over_under_lines": [{
            "id": "ud-1", "stat_value": "8.5", "status": "active",
            "over_under": {"display_stat": "Rebounds", "appearance_stat": {"appearance_id": "a"}},
            "options": [{"choice": "Higher", "payout_multiplier": "1.9"}, {"choice": "Lower", "payout_multiplier": "1.9"}],
        }],
        "appearances": [{"id": "a", "player_id": "p", "match_id": "m", "team_id": "t"}],
        "players": [{"id": "p", "attributes": {"full_name": "Test Player"}}],
        "games": [{"id": "m", "attributes": {"scheduled_at": "2026-08-30T00:00:00Z"}}],
        "providers": [], "solo_games": [],
    }
    rows = pipeline.normalize_underdog(payload, "2026-09-18T00:00:00Z")
    assert len(rows) == 1 and rows[0].adjusted_odds is None
