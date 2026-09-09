"""
Session 6.2 -- synthetic-fixture test harness for sportsbook_props_model.py,
same precedent as Sessions 2.2/2.4/2.5/2.6's own test files: proves the
model's math is correct on known inputs, independent of live nflverse/DK/FD
network access.

Run: python test_sportsbook_props_model.py
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from sportsbook_props_model import (
    poisson_prob_at_least,
    project_season_total,
    prob_over,
    two_sided_devig,
)


def test_two_sided_devig_matches_known_example():
    # Same standard -115/-105 example already proven in Session 6.1's
    # test_vig_extraction_matches_known_example.
    implied_over, implied_under = two_sided_devig(-115, -105)
    assert implied_over is not None and implied_under is not None
    assert abs((implied_over + implied_under) - 1.0) < 1e-9
    # -105 (favorite-ish, slightly shorter) should carry the higher
    # no-vig probability than -115's side once normalized -- actually
    # -115 is the larger-magnitude (more favored) price, so its raw
    # implied probability, and therefore its no-vig share, should be
    # the larger of the two.
    assert implied_over > implied_under
    print("PASS: test_two_sided_devig_matches_known_example")


def test_two_sided_devig_missing_side_returns_none():
    implied_over, implied_under = two_sided_devig(-115, None)
    assert implied_over is None and implied_under is None
    print("PASS: test_two_sided_devig_missing_side_returns_none")


def test_poisson_prob_at_least_one_and_two():
    lam = 0.5
    p1 = poisson_prob_at_least(lam, 1)
    p2 = poisson_prob_at_least(lam, 2)
    expected_p1 = 1 - math.exp(-lam)
    expected_p2 = 1 - math.exp(-lam) - lam * math.exp(-lam)
    assert abs(p1 - expected_p1) < 1e-9
    assert abs(p2 - expected_p2) < 1e-9
    assert p1 > p2 > 0  # P(2+) must always be strictly less than P(1+)
    print("PASS: test_poisson_prob_at_least_one_and_two")


def test_poisson_prob_floors_zero_rate():
    # A real observed rate of exactly 0 must not produce P(anytime)=0.0
    # exactly (that would claim total certainty the player never scores,
    # which no finite sample of games can actually prove).
    p1 = poisson_prob_at_least(0.0, 1)
    assert 0.0 < p1 < 1e-3
    print("PASS: test_poisson_prob_floors_zero_rate")


def test_project_season_total_accrues_and_projects_remaining():
    # 3 games played, values 100/120/140 (rising) -- recent_form weights
    # recent games more, so the per-game rate used for the remaining 14
    # games should be pulled toward 140/120, not the flat mean of 120.
    series = pd.Series([100.0, 120.0, 140.0])
    full_mean, full_sigma, games_played, games_remaining = project_season_total(series)
    assert games_played == 3
    assert games_remaining == 14  # 17 - 3
    accrued = 100.0 + 120.0 + 140.0
    assert full_mean > accrued  # remaining games must add real projected value
    assert full_sigma is not None and full_sigma > 0
    print("PASS: test_project_season_total_accrues_and_projects_remaining")


def test_project_season_total_insufficient_history():
    series = pd.Series([100.0])  # only 1 game -- below MIN_GAMES_FOR_ESTIMATE
    full_mean, full_sigma, games_played, games_remaining = project_season_total(series)
    assert full_mean is None and full_sigma is None
    assert games_played == 1
    print("PASS: test_project_season_total_insufficient_history")


def test_project_season_total_season_complete():
    series = pd.Series([100.0] * 17)  # already played the full assumed season
    full_mean, full_sigma, games_played, games_remaining = project_season_total(series)
    assert games_remaining == 0
    assert full_sigma == 0.0
    assert full_mean == 1700.0
    print("PASS: test_project_season_total_season_complete")


def test_prob_over_matches_manual_normal_cdf():
    # line exactly at the mean must be ~0.5 regardless of sigma
    p = prob_over(line=100.0, mean=100.0, sigma=20.0)
    assert abs(p - 0.5) < 1e-9
    # a line far below the mean must be close to 1.0 (very likely to go over)
    p_high = prob_over(line=10.0, mean=100.0, sigma=20.0)
    assert p_high > 0.999
    print("PASS: test_prob_over_matches_manual_normal_cdf")


def test_prob_over_none_sigma_returns_none():
    assert prob_over(line=100.0, mean=100.0, sigma=0.0) is None
    assert prob_over(line=100.0, mean=100.0, sigma=float("nan")) is None
    print("PASS: test_prob_over_none_sigma_returns_none")


if __name__ == "__main__":
    test_two_sided_devig_matches_known_example()
    test_two_sided_devig_missing_side_returns_none()
    test_poisson_prob_at_least_one_and_two()
    test_poisson_prob_floors_zero_rate()
    test_project_season_total_accrues_and_projects_remaining()
    test_project_season_total_insufficient_history()
    test_project_season_total_season_complete()
    test_prob_over_matches_manual_normal_cdf()
    test_prob_over_none_sigma_returns_none()
    print("\nAll tests passed.")
