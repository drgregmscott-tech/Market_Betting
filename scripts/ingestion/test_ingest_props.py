"""
Session 6.1 — Synthetic-Fixture Validation Harness for DK/FD Props Ingestion

WHY THIS EXISTS
---------------
Same reason Session 2.2/2.4/2.5/2.6 each built their own synthetic-fixture
test harness: this sandbox cannot reach sportsbook.draftkings.com or
sportsbook.fanduel.com to test against real live data (both are blocked by
Claude's browser tool's safety category filter — see the "HONESTY NOTE" in
both ingest_dk_props.py and ingest_fd_props.py). This harness proves the
NORMALIZER logic is correct against a fixed, known-shape input — it does
NOT prove the real endpoints return that shape. That confirmation can only
happen when the user runs the real scripts locally.

Run: python test_ingest_props.py
"""

from __future__ import annotations

from ingest_dk_props import normalize_dk
from ingest_fd_props import normalize_fd
from schema_props import american_odds_to_implied_probability

FAKE_PULLED_AT = "2026-09-09T12:00:00+00:00"

DK_FIXTURE_OK = {
    "eventGroup": {
        "events": [
            {
                "eventId": "30001",
                "startDate": "2026-09-14T17:00:00Z",
                "status": "NotStarted",
            }
        ],
        "offerCategories": [
            {
                "offerSubcategoryDescriptors": [
                    {
                        "offerSubcategory": {
                            "offers": [
                                [
                                    {
                                        "eventId": "30001",
                                        "providerOfferId": "off-1",
                                        "label": "Patrick Mahomes Passing Yards",
                                        "outcomes": [
                                            {
                                                "label": "Over",
                                                "line": 275.5,
                                                "oddsAmerican": "-115",
                                                "participant": "Patrick Mahomes",
                                                "providerOutcomeId": "out-1",
                                            },
                                            {
                                                "label": "Under",
                                                "line": 275.5,
                                                "oddsAmerican": "-105",
                                                "participant": "Patrick Mahomes",
                                                "providerOutcomeId": "out-2",
                                            },
                                        ],
                                    }
                                ]
                            ]
                        }
                    }
                ]
            }
        ],
    }
}

DK_FIXTURE_MALFORMED_RECORD = {
    "eventGroup": {
        "events": [],
        "offerCategories": [
            {
                "offerSubcategoryDescriptors": [
                    {
                        "offerSubcategory": {
                            # "garbage" has no .get() method -> AttributeError
                            # inside the per-offer try/except, proving one bad
                            # record is skipped rather than crashing the run.
                            "offers": [["garbage"]]
                        }
                    }
                ]
            }
        ],
    }
}

DK_FIXTURE_MISSING_TOP_LEVEL = {"somethingElse": True}

FD_FIXTURE_OK = {
    # Shape confirmed against a real live pull, 2026-09-09 (275 raw markets,
    # 141 real player-prop rows after filtering — see SESSION_LOG.md).
    # handicap is 0 on real rows; the real line lives in runnerName text.
    "attachments": {
        "events": {
            "40001": {"openDate": "2026-09-14T17:00:00Z", "inPlayStatus": "PREPLAY"}
        },
        "markets": {
            "mkt-1": {
                "eventId": "40001",
                "marketName": "Patrick Mahomes Regular Season Passing Yards 2026-27",
                "marketType": "REGULAR_SEASON_PROPS_-_QUARTERBACKS",
                "runners": [
                    {
                        "runnerName": "Patrick Mahomes Over 275.5",
                        "handicap": 0,
                        "selectionId": "sel-1",
                        "result": {},
                        "winRunnerOdds": {
                            "americanDisplayOdds": {"americanOdds": "-115"}
                        },
                    },
                    {
                        "runnerName": "Patrick Mahomes Under 275.5",
                        "handicap": 0,
                        "selectionId": "sel-2",
                        "result": {},
                        "winRunnerOdds": {
                            "americanDisplayOdds": {"americanOdds": "-105"}
                        },
                    },
                ],
            },
            # Real, confirmed false-positive case (Worst Regular Season
            # Record) and a real non-player market (team season wins) —
            # both must be filtered out, not returned as a blank-player row.
            "mkt-2": {
                "eventId": "40001",
                "marketName": "Worst Regular Season Record 2026-27",
                "runners": [
                    {"runnerName": "AFC", "handicap": 0, "selectionId": "sel-3",
                     "result": {}, "winRunnerOdds": {"americanDisplayOdds": {"americanOdds": "+200"}}},
                ],
            },
            "mkt-3": {
                "eventId": "40001",
                "marketName": "Kansas City Chiefs - Regular Season Wins 2026-27",
                "runners": [
                    {"runnerName": "Over 10.5", "handicap": 0, "selectionId": "sel-4",
                     "result": {}, "winRunnerOdds": {"americanDisplayOdds": {"americanOdds": "-120"}}},
                ],
            },
        },
    }
}

FD_FIXTURE_MISSING_TOP_LEVEL = {"somethingElse": True}


def test_dk_normalizer_happy_path():
    rows = normalize_dk(DK_FIXTURE_OK, FAKE_PULLED_AT)
    assert len(rows) == 1, f"expected 1 row, got {len(rows)}"
    row = rows[0]
    assert row.platform == "draftkings"
    assert row.player_name == "Patrick Mahomes"
    assert row.line == 275.5
    assert row.over_american_odds == -115
    assert row.under_american_odds == -105
    assert row.game_start_time == "2026-09-14T17:00:00Z"
    print("PASS: test_dk_normalizer_happy_path")


def test_dk_normalizer_skips_malformed_record_without_crashing():
    rows = normalize_dk(DK_FIXTURE_MALFORMED_RECORD, FAKE_PULLED_AT)
    assert rows == [], "malformed record should be skipped, not raise"
    print("PASS: test_dk_normalizer_skips_malformed_record_without_crashing")


def test_dk_normalizer_handles_missing_top_level_key():
    rows = normalize_dk(DK_FIXTURE_MISSING_TOP_LEVEL, FAKE_PULLED_AT)
    assert rows == [], "missing eventGroup key should return empty list, not raise"
    print("PASS: test_dk_normalizer_handles_missing_top_level_key")


def test_fd_normalizer_happy_path():
    rows = normalize_fd(FD_FIXTURE_OK, FAKE_PULLED_AT)
    # mkt-2 (league-wide, no real player) and mkt-3 (team-level, not a
    # player prop) must both be filtered out — only mkt-1 survives.
    assert len(rows) == 1, f"expected 1 row, got {len(rows)}"
    row = rows[0]
    assert row.platform == "fanduel"
    assert row.player_name == "Patrick Mahomes"
    assert row.stat_type == "Passing Yards"
    assert row.line == 275.5
    assert row.over_american_odds == -115
    assert row.under_american_odds == -105
    assert row.game_start_time == "2026-09-14T17:00:00Z"
    print("PASS: test_fd_normalizer_happy_path")


def test_fd_normalizer_handles_missing_top_level_key():
    rows = normalize_fd(FD_FIXTURE_MISSING_TOP_LEVEL, FAKE_PULLED_AT)
    assert rows == [], "missing attachments key should return empty list, not raise"
    print("PASS: test_fd_normalizer_handles_missing_top_level_key")


def test_vig_extraction_matches_known_example():
    # -115 / -105 is a standard, commonly-cited two-sided prop price.
    # Raw (vig-included) implied probabilities:
    over_raw = american_odds_to_implied_probability(-115)
    under_raw = american_odds_to_implied_probability(-105)
    assert over_raw is not None and under_raw is not None
    total = over_raw + under_raw
    assert total > 1.0, "both sides' raw implied probability must sum to > 1.0 (the vig)"
    # No-vig probability: each side normalized by the total.
    over_no_vig = over_raw / total
    under_no_vig = under_raw / total
    assert abs((over_no_vig + under_no_vig) - 1.0) < 1e-9
    print(
        f"PASS: test_vig_extraction_matches_known_example "
        f"(raw sum={total:.4f}, no-vig over={over_no_vig:.4f})"
    )


def test_american_odds_positive_and_negative():
    assert abs(american_odds_to_implied_probability(100) - 0.5) < 1e-9
    assert abs(american_odds_to_implied_probability(-100) - 0.5) < 1e-9
    assert american_odds_to_implied_probability(None) is None
    print("PASS: test_american_odds_positive_and_negative")


if __name__ == "__main__":
    test_dk_normalizer_happy_path()
    test_dk_normalizer_skips_malformed_record_without_crashing()
    test_dk_normalizer_handles_missing_top_level_key()
    test_fd_normalizer_happy_path()
    test_fd_normalizer_handles_missing_top_level_key()
    test_vig_extraction_matches_known_example()
    test_american_odds_positive_and_negative()
    print("\nAll tests passed.")
