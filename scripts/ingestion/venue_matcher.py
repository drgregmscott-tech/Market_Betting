"""
Session 3.1 / 3.2 - Venue Matcher (Multi-Venue Data Ingestion +
Arbitrage Detection Logic)

WHAT THIS SCRIPT IS
--------------------
Reads the two normalized CSV snapshots ingest_kalshi.py and
ingest_polymarket.py just produced, and proposes pairs of contracts from
each venue that plausibly represent the SAME real-world outcome (e.g.
Kalshi's "Will the maximum temperature be >86F on Sep 5, 2026?" and a
similarly-worded Polymarket contract on the same city/date). Session 3.2
(Arbitrage Detection Logic) reads this script's output to decide which
matched pairs are actually mispriced against each other.

WHAT MATCHING METHOD THIS VERSION USES, AND WHY
----------------------------------------------------
Neither venue exposes a shared ID for "the same real-world question" -
Kalshi's ticker and Polymarket's conditionId are each internal to that one
venue. This first version matches on:
1. Title word-overlap: both titles are lowercased, stripped of common stop
   words, and compared using a simple Jaccard-similarity score (the size
   of the shared word set divided by the size of the combined word set).
2. Close-time proximity: the two contracts' close_time values must fall
   within a tolerance of each other, since two contracts on the same
   real-world event should resolve at close to the same time. Session 3.2
   made this tolerance CATEGORY-SPECIFIC - see "SESSION 3.2 FIX" below -
   because one real category (down-ballot Elections) breaks the
   assumption that "resolves at the same time" means "close_time is a
   few hours apart."

A pair is only proposed as a candidate match if BOTH conditions clear
their threshold - word overlap alone is not enough, since two unrelated
contracts can share generic words ("Will", "the", team names), and
close-time proximity alone is not enough, since many unrelated contracts
close at the same time (e.g. many weather contracts all close at midnight
local time on the same day).

SESSION 3.2 FIX - OPEN DECISION #21 (Elections close-time gap)
-----------------------------------------------------------------
Session 3.1b found a real, live, simultaneously-available matched pair for
the first time in this project's history (Kalshi's MO-05 U.S. House race
vs. Polymarket's "MO-05 House Election Winner") - but confirmed this
matcher, as it stood then, would NOT catch it. The reason is specific and
confirmed against real data, not assumed: Kalshi sets close_time on its
down-ballot political contracts to the seat's swearing-in/contract-
expiration date (2027-11-03 for MO-05), not the election date itself.
Polymarket's endDate for the same real race is the actual election date
(2026-11-04). That is roughly a 364-day gap - nowhere close to the
default 6-hour CLOSE_TIME_TOLERANCE_HOURS, which was tuned against
Session 3.1's real weather-market data, not political contracts. Session
3.1b confirmed this same 2027-11-03 pattern on two other real down-ballot
tickers (Pennsylvania House District 12, Missouri Senate District 8), so
this is systematic to how Kalshi structures these contracts - not a
one-off data issue that a single-pair special case would fix.

The fix applied here is the second option Session 3.1b's own
SESSION_LOG.md entry named: a PER-CATEGORY matching rule for the
Elections category, rather than trying to derive a second, election-day-
specific timestamp from Kalshi's data (Kalshi's public API does not
expose one - the only timestamp on a down-ballot political contract is
the swearing-in-date close_time, confirmed directly against the real
MO-05, PA-HD12, and MO-SD8 records pulled in Session 3.1b).

Concretely:
- Kalshi rows whose category starts with "Elections" (i.e. the specific
  tier labels ingest_kalshi.py's classify_down_ballot() writes -
  "Elections - US House District" and "Elections - State Legislature
  District") are matched against ALL Polymarket rows using a much wider
  tolerance, ELECTIONS_CLOSE_TIME_TOLERANCE_HOURS (400 days - long
  enough to comfortably cover a full one-year swearing-in gap with
  margin, short enough that it cannot span two different U.S. general
  election cycles, which are two years apart).
- Because a 400-day window is far less discriminating on its own than a
  6-hour one, the title-similarity bar for this category is raised to
  MIN_TITLE_SIMILARITY_ELECTIONS (0.5, vs. the default 0.35) - down-
  ballot race titles already contain a specific state and district
  number ("MO-05", "Pennsylvania State House District 12"), so a genuine
  match should score well above the default bar; requiring a higher
  score here is a deliberate, named trade-off for relaxing the time
  check, not a free relaxation.
- All non-Elections rows (Climate and Weather, Commodities) are entirely
  unaffected - they keep using the original 6-hour tolerance and the
  bucketed comparison, since that combination has already been
  validated against real Session 3.1 data and nothing about the
  Elections fix changes what was working there.
- This is a real, named trade-off, not a silent one: a genuinely
  different down-ballot race that happens to share a very similar title
  (e.g. two different "State Senate District 8" races in different
  states, if either title omits the state name) could now be proposed
  as a false-candidate match where it would not have been before. This
  matcher still only PROPOSES candidates for human/Session-3.2 review -
  see the module's original design note below - so this risk is caught
  at review time, not silently acted on.

WHY A SEPARATE, NON-BUCKETED PASS FOR ELECTIONS ROWS
-----------------------------------------------------------
The existing bucketed comparison (see find_candidate_matches's own
docstring for why bucketing exists at all) indexes Polymarket rows into
fixed-width time buckets sized to CLOSE_TIME_TOLERANCE_HOURS, then only
compares a Kalshi row against its own bucket and immediate neighbors.
Reusing that scheme for a 400-day tolerance would mean checking hundreds
of neighboring buckets per row - workable, but needlessly complex for a
dataset this small. Session 3.1b confirmed only 93 real down-ballot
Kalshi series exist (89 House + 4 state legislature) - small enough that
a direct, unbucketed comparison against every Polymarket row is cheap by
the same reasoning the original bucketing fix already established:
bucketing was needed for Kalshi's ~60,000-row Climate/Commodities pull,
not for a 93-row category.

THIS IS A DELIBERATELY CONSERVATIVE FIRST VERSION, NOT A FINISHED MATCHER
-------------------------------------------------------------------------
This word-overlap approach will miss real matches that are worded very
differently (e.g. Kalshi's ticker-driven, formal-question style vs.
Polymarket's often more colloquial phrasing). Every candidate pair this
script proposes is written out with its own similarity score and time
gap, not silently auto-confirmed - a human (or a future, better matcher)
should review the candidate list before Session 3.2's arbitrage logic is
allowed to treat a pair as definitely the same event.

WHERE OUTPUT GOES
------------------
/data/exchange/matched/candidate_matches_<timestamp>.csv - every candidate
pair found, with its similarity score, close-time gap, and which match
path found it (bucketed / elections_wide), for review.

USAGE
-----
python venue_matcher.py
(reads kalshi_latest.csv and polymarket_latest.csv from
/data/exchange/normalized/ - run both ingestion scripts first)
"""

from __future__ import annotations

import csv
import logging
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

BASE_DIR = Path(__file__).resolve().parents[2]
NORMALIZED_DIR = BASE_DIR / "data" / "exchange" / "normalized"
MATCHED_DIR = BASE_DIR / "data" / "exchange" / "matched"
LOG_PATH = BASE_DIR / "logs" / "ingestion.log"

KALSHI_LATEST = NORMALIZED_DIR / "kalshi_latest.csv"
POLYMARKET_LATEST = NORMALIZED_DIR / "polymarket_latest.csv"

# Thresholds - starting values, not yet fully validated against a real
# matched pair for every category (see module docstring). Flagged here as
# named constants, the same "no silent adjustments" pattern as
# sizing_engine.py's KELLY_FRACTION, so a future session can find and
# recalibrate them in one place.
MIN_TITLE_SIMILARITY = 0.35
CLOSE_TIME_TOLERANCE_HOURS = 6.0

# Session 3.2 fix (Open Decision #21) - see module docstring's "SESSION
# 3.2 FIX" section for the full evidence trail on why Elections needs its
# own tolerance and its own, higher title-similarity bar.
DOWN_BALLOT_CATEGORY_PREFIX = "Elections"
ELECTIONS_CLOSE_TIME_TOLERANCE_HOURS = 400 * 24.0  # 400 days
MIN_TITLE_SIMILARITY_ELECTIONS = 0.5

_STOPWORDS = {
    "will", "the", "a", "an", "in", "on", "at", "to", "of", "be", "is",
    "are", "or", "and", "than", "more", "less", "for", "by",
}

_NUMBER_PATTERN = re.compile(r"\d+\.?\d*")


def _extract_numbers(title: Optional[str]) -> set[float]:
    """Pulls every number out of a title EXCLUDING year-like numbers (e.g.
    '86', '9.0', '6.5' are kept; '2026', '2027' are dropped).

    BUG FOUND AND FIXED (same real earthquake pairs, immediately after
    adding this check): the first version of this function counted
    ANY shared number as a match - including the year. 'earthquake...
    before 2027' and '...earthquake before 2027' share the number 2027
    purely because they're both talking about the same TIME PERIOD, not
    because they agree on the actual threshold (8.0 vs 9.0 magnitude).
    Without excluding year-like numbers, the fix this function exists for
    doesn't work at all - confirmed directly: testing against the real
    earthquake titles still produced 2 candidates before this exclusion
    was added, for exactly this reason. A 4-digit integer in a plausible
    calendar-year range (2000-2099, comfortably covering this project's
    real operating window) is treated as a date, not a threshold, and
    excluded here.

    Note this also naturally excludes district numbers like "12" in
    "State House District 12" from being treated as a mismatch trigger
    against an unrelated numeric title - those pass through fine since a
    district number is not in the 2000-2099 range, and Elections-category
    pairs are additionally allowed to pass this check with no numbers
    present at all (see _numbers_are_compatible) if a title has none.
    """
    if not title:
        return set()
    numbers = {float(n) for n in _NUMBER_PATTERN.findall(title)}
    return {n for n in numbers if not (n == int(n) and 2000 <= n <= 2099)}


def _numbers_are_compatible(a: set[float], b: set[float]) -> bool:
    """REAL BUG FOUND AND FIXED (Session 3.1, first real matches found,
    2026-09-04): venue_matcher.py's first two genuine non-zero results
    both turned out to be FALSE MATCHES on inspection - 'at least 8
    magnitude earthquake in California' matched against both '9.0 or
    above earthquake' and 'Magnitude 6.5+ earthquake in LA', purely on
    shared generic wording ('earthquake', 'before', '2027') and a shared
    close time. Word similarity and close-time proximity alone cannot
    tell two DIFFERENT real-world thresholds apart - an 8.0+ earthquake
    and a 9.0+ earthquake are genuinely different bets with different
    real odds, not the same event worded two ways. This function adds a
    required check: if both titles contain at least one number, at least
    one of those numbers must actually match. If either title has no
    number at all, this check is skipped (not every real match involves a
    numeric threshold - e.g. two differently-worded yes/no questions
    about the same binary event, or a down-ballot race title with a
    district number that the other venue's title expresses differently).
    This is a necessary check, not a replacement for title similarity or
    close-time proximity - all three must still agree for a pair to be
    proposed.
    """
    if not a or not b:
        return True  # nothing to compare - don't block on this check
    return bool(a & b)


def setup_logging() -> logging.Logger:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("venue_matcher")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()

    file_handler = logging.FileHandler(LOG_PATH, mode="a", encoding="utf-8")
    console_handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s UTC | %(levelname)s | %(message)s")
    formatter.converter = time.gmtime
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger


log = setup_logging()


def _read_rows(path: Path) -> list[dict]:
    if not path.exists():
        log.error(
            "%s does not exist - run its ingestion script first. "
            "Treating as zero rows for this run, not crashing.",
            path,
        )
        return []
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _title_words(title: Optional[str]) -> set[str]:
    if not title:
        return set()
    words = re.findall(r"[a-z0-9]+", title.lower())
    return {w for w in words if w not in _STOPWORDS and len(w) > 1}


def _jaccard_similarity(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    intersection = len(a & b)
    union = len(a | b)
    return intersection / union if union else 0.0


def _parse_close_time(value: Optional[str]) -> Optional[datetime]:
    """Both venues return ISO-8601 timestamps (confirmed live 2026-09-04),
    but Python's fromisoformat needs the trailing 'Z' converted to an
    explicit UTC offset on the Python version this project runs
    (confirmed: Python 3.14 per ROADMAP.md's environment record)."""
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


_DISTRICT_CODE_PATTERN = re.compile(r"\b([a-z]{2})-0*(\d{1,2})\b")


def _extract_district_codes(title: Optional[str]) -> set[tuple[str, int]]:
    """Pulls a (state abbreviation, district number) code out of a title,
    e.g. "WA-08" -> ("wa", 8), "MI-7" -> ("mi", 7). Returns a set since a
    title could in principle mention more than one; in practice every
    real title checked has exactly one or zero.

    REAL BUG FOUND AND FIXED (Session 3.4, first live automated
    arbitrage_pipeline.yml run, 2026-09-06): _find_elections_matches()
    was proposing candidate pairs like Kalshi's "Will a Republican win
    the House race for WA-08?" against Polymarket's "Will the
    Republican Party win the IN-08 House seat?" - Washington's 8th
    District and Indiana's 8th District, two different real-world
    races, reported with a 90-cent-per-dollar "arbitrage." The cause:
    _title_words() tokenizes "WA-08" into "wa" and "08" as SEPARATE
    words (the hyphen splits them), so the shared token "08" satisfied
    both the Jaccard title-similarity bar (title_similarity does not
    know "08" is a district number, not a generic word) AND
    _numbers_are_compatible()'s "at least one number must match" check
    (which only compares raw numbers, with no idea that "8" needs to be
    paired with the SAME state to mean the same district). Confirmed
    live: 10 flags from this run's real output, several with a 400-day
    close-time gap and a 0.5+ title-similarity score, none of them the
    same real race. This function - and the check built on it in
    _find_elections_matches() below - fixes this at the source: for a
    down-ballot title, "same district number" is only meaningful
    together with "same state," so both must be extracted and compared
    as a pair, not as two independent, order-blind checks."""
    if not title:
        return set()
    return {
        (state.lower(), int(district))
        for state, district in _DISTRICT_CODE_PATTERN.findall(title.lower())
    }


def _district_codes_compatible(a: set[tuple[str, int]], b: set[tuple[str, int]]) -> bool:
    """Elections-specific version of _numbers_are_compatible(): if BOTH
    titles have an extractable (state, district) code, at least one
    pair must match exactly - a shared district number with a
    different state is a genuine mismatch, not merely an unconfirmed
    one. If either title has no extractable code (e.g. a state-
    legislature title without a two-letter/number pattern), this check
    is skipped rather than blocking a real match on a formatting
    difference this function cannot see past - the existing title-
    similarity and number checks still apply in that case."""
    if not a or not b:
        return True
    return bool(a & b)


def _is_down_ballot_category(category: Optional[str]) -> bool:
    """True for either down-ballot Elections tier ingest_kalshi.py tags
    ("Elections - US House District", "Elections - State Legislature
    District") - checked by prefix so both tiers share one code path,
    and so a future third tier (see the city/county note in
    ingest_kalshi.py) picks up this fix automatically if it's ever
    turned on."""
    return bool(category) and category.startswith(DOWN_BALLOT_CATEGORY_PREFIX)


def _build_candidate_row(k_row, p_row, similarity, gap_hours, match_path) -> dict:
    return {
        "kalshi_source_market_id": k_row.get("source_market_id"),
        "kalshi_title": k_row.get("title"),
        "kalshi_category": k_row.get("category"),
        "kalshi_yes_ask": k_row.get("yes_ask"),
        "kalshi_no_ask": k_row.get("no_ask"),
        "polymarket_source_market_id": p_row.get("source_market_id"),
        "polymarket_title": p_row.get("title"),
        "polymarket_yes_ask": p_row.get("yes_ask"),
        "polymarket_no_ask": p_row.get("no_ask"),
        "title_similarity": round(similarity, 3),
        "close_time_gap_hours": round(gap_hours, 2),
        "match_path": match_path,
    }


def _find_bucketed_matches(kalshi_parsed: list, polymarket_parsed: list) -> list[dict]:
    """Original Session 3.1 bucketed comparison, unchanged - used for
    every Kalshi row that is NOT in a down-ballot Elections tier. See
    this function's Session 3.1 history in SESSION_LOG.md for why
    bucketing exists (naive n*m comparison was ~126 million pairs at
    real Kalshi scale and looked hung rather than slow)."""
    candidates: list[dict] = []
    bucket_seconds = CLOSE_TIME_TOLERANCE_HOURS * 3600.0

    def _bucket_key(dt: Optional[datetime]) -> Optional[int]:
        if dt is None:
            return None
        return int(dt.timestamp() // bucket_seconds)

    polymarket_by_bucket: dict[int, list] = {}
    for p_row, p_words, p_close, p_numbers in polymarket_parsed:
        bucket = _bucket_key(p_close)
        if bucket is None:
            continue
        polymarket_by_bucket.setdefault(bucket, []).append(
            (p_row, p_words, p_close, p_numbers)
        )

    for k_row, k_words, k_close, k_numbers in kalshi_parsed:
        if _is_down_ballot_category(k_row.get("category")):
            continue  # handled by _find_elections_matches instead
        k_bucket = _bucket_key(k_close)
        if k_bucket is None:
            continue

        nearby_polymarket_rows = []
        for offset in (-1, 0, 1):
            nearby_polymarket_rows.extend(
                polymarket_by_bucket.get(k_bucket + offset, [])
            )

        for p_row, p_words, p_close, p_numbers in nearby_polymarket_rows:
            similarity = _jaccard_similarity(k_words, p_words)
            if similarity < MIN_TITLE_SIMILARITY:
                continue

            gap_hours = abs((k_close - p_close).total_seconds()) / 3600.0
            if gap_hours > CLOSE_TIME_TOLERANCE_HOURS:
                continue

            if not _numbers_are_compatible(k_numbers, p_numbers):
                continue

            candidates.append(
                _build_candidate_row(k_row, p_row, similarity, gap_hours, "bucketed")
            )

    return candidates


def _find_elections_matches(kalshi_parsed: list, polymarket_parsed: list) -> list[dict]:
    """Session 3.2 fix (Open Decision #21) - direct, unbucketed
    comparison for down-ballot Elections rows only, using a much wider
    close-time tolerance and a raised title-similarity bar. See module
    docstring's "SESSION 3.2 FIX" section for the full rationale. Cheap
    by design: Session 3.1b confirmed only 93 real down-ballot series
    exist, so this is at most 93 x (Polymarket row count) comparisons,
    not the ~60,000-row scale bucketing was built for."""
    candidates: list[dict] = []

    election_kalshi_rows = [
        row for row in kalshi_parsed if _is_down_ballot_category(row[0].get("category"))
    ]
    if not election_kalshi_rows:
        return candidates

    for k_row, k_words, k_close, k_numbers in election_kalshi_rows:
        if k_close is None:
            continue
        k_district_codes = _extract_district_codes(k_row.get("title"))
        for p_row, p_words, p_close, p_numbers in polymarket_parsed:
            if p_close is None:
                continue

            similarity = _jaccard_similarity(k_words, p_words)
            if similarity < MIN_TITLE_SIMILARITY_ELECTIONS:
                continue

            gap_hours = abs((k_close - p_close).total_seconds()) / 3600.0
            if gap_hours > ELECTIONS_CLOSE_TIME_TOLERANCE_HOURS:
                continue

            if not _numbers_are_compatible(k_numbers, p_numbers):
                continue

            # Session 3.4 fix - see _extract_district_codes()'s
            # docstring for the real false-positive pairs (e.g.
            # WA-08 vs IN-08) this check exists to stop. Applied only
            # here, not in _find_bucketed_matches(), since this is
            # specifically where the wide 400-day tolerance and raised
            # similarity bar made a shared district NUMBER look like
            # enough evidence on its own.
            p_district_codes = _extract_district_codes(p_row.get("title"))
            if not _district_codes_compatible(k_district_codes, p_district_codes):
                continue

            candidates.append(
                _build_candidate_row(
                    k_row, p_row, similarity, gap_hours, "elections_wide"
                )
            )

    return candidates


def find_candidate_matches(
    kalshi_rows: list[dict], polymarket_rows: list[dict]
) -> list[dict]:
    """Compares Kalshi rows against Polymarket rows using TWO paths:
    1. A time-bucketed approach for all non-Elections rows (Climate and
       Weather, Commodities) - the original Session 3.1 logic, unchanged.
    2. A direct, wide-tolerance approach for down-ballot Elections rows -
       the Session 3.2 fix for Open Decision #21 (see module docstring).

    Every Kalshi row is routed to exactly one path based on its category
    field, so nothing is compared twice and nothing falls through
    uncompared."""
    kalshi_parsed = [
        (
            row,
            _title_words(row.get("title")),
            _parse_close_time(row.get("close_time")),
            _extract_numbers(row.get("title")),
        )
        for row in kalshi_rows
    ]
    polymarket_parsed = [
        (
            row,
            _title_words(row.get("title")),
            _parse_close_time(row.get("close_time")),
            _extract_numbers(row.get("title")),
        )
        for row in polymarket_rows
    ]

    bucketed = _find_bucketed_matches(kalshi_parsed, polymarket_parsed)
    elections = _find_elections_matches(kalshi_parsed, polymarket_parsed)

    return bucketed + elections


def write_candidates_csv(path: Path, candidates: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "kalshi_source_market_id",
        "kalshi_title",
        "kalshi_category",
        "kalshi_yes_ask",
        "kalshi_no_ask",
        "polymarket_source_market_id",
        "polymarket_title",
        "polymarket_yes_ask",
        "polymarket_no_ask",
        "title_similarity",
        "close_time_gap_hours",
        "match_path",
    ]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in candidates:
            writer.writerow(row)


def run() -> dict:
    pulled_at_compact = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    log.info("=== Venue matcher run starting ===")

    kalshi_rows = _read_rows(KALSHI_LATEST)
    polymarket_rows = _read_rows(POLYMARKET_LATEST)

    candidates = find_candidate_matches(kalshi_rows, polymarket_rows)
    elections_count = sum(1 for c in candidates if c["match_path"] == "elections_wide")

    out_path = MATCHED_DIR / f"candidate_matches_{pulled_at_compact}.csv"
    write_candidates_csv(out_path, candidates)

    log.info(
        "=== Venue matcher run complete: %d candidate pairs (%d bucketed, "
        "%d elections-wide) from %d Kalshi rows x %d Polymarket rows ===",
        len(candidates),
        len(candidates) - elections_count,
        elections_count,
        len(kalshi_rows),
        len(polymarket_rows),
    )

    return {
        "kalshi_rows_checked": len(kalshi_rows),
        "polymarket_rows_checked": len(polymarket_rows),
        "candidate_matches_found": len(candidates),
        "candidate_matches_elections_wide": elections_count,
        "output_path": str(out_path),
    }


if __name__ == "__main__":
    import json

    result = run()
    print(json.dumps(result, indent=2))
