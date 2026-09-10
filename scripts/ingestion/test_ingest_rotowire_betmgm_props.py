"""
Session 6.9 — Synthetic-Fixture Validation Harness for Rotowire BetMGM Props

WHY THIS EXISTS
---------------
Unlike DK/FD's own test harnesses, this one is NOT a stand-in for an
untestable real endpoint — `ingest_rotowire_betmgm_props.py` was run live
against the real `rotowire.com` page this session and produced 377 real
normalized BetMGM rows. This harness instead locks in the exact real-data
bug this session found and fixed: a first version classified every
TD-scorer-shaped row (e.g. "anytd") as a two-sided market because
`mgm_anytdOver`/`mgm_anytdUnder` KEYS are present on those real rows even
though their VALUES are always null — that misrouted the real single price
into the `line` column instead of `over_american_odds`. This test fixture
is built directly from real captured field shapes (Jahmyr Gibbs' real
`anytd` row and a real `rushrec` row, both from this session's real pull)
so a future change to the classification logic can't silently reintroduce
that bug.

Run: python test_ingest_rotowire_betmgm_props.py
"""

from __future__ import annotations

from ingest_rotowire_betmgm_props import normalize_rotowire

FAKE_PULLED_AT = "2026-09-10T15:52:35+00:00"

# Real shape, real values, captured 2026-09-10 (Jahmyr Gibbs, "anytd"):
# Over/Under KEYS are present but null -- the real price is the bare field.
TD_SCORER_FIXTURE = [
    {
        "gameID": "2978635",
        "playerID": "16808",
        "firstName": "Jahmyr",
        "lastName": "Gibbs",
        "name": "Jahmyr Gibbs",
        "team": "DET",
        "opp": "NO",
        "mgm_anytd": "-325",
        "mgm_anytdUnder": None,
        "mgm_anytdOver": None,
    },
]

# Real shape, real values, captured 2026-09-10 (Samaje Perine, "rushrec"):
# a genuine two-sided-shaped market where BetMGM's real Under side happens
# to be blank in the source (a real, normal coverage gap -- confirmed
# against the raw page, not a parsing bug) while Over is real and priced.
TWO_SIDED_FIXTURE = [
    {
        "gameID": "2978621",
        "playerID": "11698",
        "firstName": "Samaje",
        "lastName": "Perine",
        "name": "Samaje Perine",
        "team": "CIN",
        "opp": "@PIT",
        "mgm_rushrec": "24.5",
        "mgm_rushrecOver": "-200",
        "mgm_rushrecUnder": "",
    },
]

# Real shape: BetMGM has no market at all for this player/stat (null base
# value, null Over, null Under) -- must be skipped, not stored as a fake
# zero-value row.
NO_COVERAGE_FIXTURE = [
    {
        "gameID": "2978638",
        "playerID": "11712",
        "firstName": "Deshaun",
        "lastName": "Watson",
        "name": "Deshaun Watson",
        "team": "CLE",
        "opp": "@JAX",
        "mgm_passyds": None,
        "mgm_passydsOver": None,
        "mgm_passydsUnder": None,
    },
]


def test_td_scorer_shape_goes_to_over_odds_not_line() -> None:
    rows = normalize_rotowire([TD_SCORER_FIXTURE], FAKE_PULLED_AT)
    assert len(rows) == 1
    row = rows[0]
    assert row.player_name == "Jahmyr Gibbs"
    assert row.prop_category == "player_touchdown"
    assert row.line is None
    assert row.over_american_odds == -325
    assert row.under_american_odds is None


def test_two_sided_shape_with_real_blank_under() -> None:
    rows = normalize_rotowire([TWO_SIDED_FIXTURE], FAKE_PULLED_AT)
    assert len(rows) == 1
    row = rows[0]
    assert row.player_name == "Samaje Perine"
    assert row.prop_category == "player_performance"
    assert row.line == 24.5
    assert row.over_american_odds == -200
    assert row.under_american_odds is None


def test_no_coverage_row_is_skipped() -> None:
    rows = normalize_rotowire([NO_COVERAGE_FIXTURE], FAKE_PULLED_AT)
    assert rows == []


def test_platform_is_betmgm_not_rotowire() -> None:
    rows = normalize_rotowire([TD_SCORER_FIXTURE], FAKE_PULLED_AT)
    assert rows[0].platform == "betmgm"


def run_all() -> None:
    tests = [
        test_td_scorer_shape_goes_to_over_odds_not_line,
        test_two_sided_shape_with_real_blank_under,
        test_no_coverage_row_is_skipped,
        test_platform_is_betmgm_not_rotowire,
    ]
    failures = 0
    for test in tests:
        try:
            test()
            print(f"PASS: {test.__name__}")
        except AssertionError as exc:
            failures += 1
            print(f"FAIL: {test.__name__}: {exc}")
    if failures:
        raise SystemExit(f"{failures} test(s) failed")
    print(f"All {len(tests)} tests passed.")


if __name__ == "__main__":
    run_all()
