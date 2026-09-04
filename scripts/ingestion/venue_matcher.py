"""
Session 3.1 — Venue Matcher (Multi-Venue Data Ingestion)

WHAT THIS SCRIPT IS
--------------------
Reads the two normalized CSV snapshots ingest_kalshi.py and
ingest_polymarket.py just produced, and proposes pairs of contracts from
each venue that plausibly represent the SAME real-world outcome (e.g.
Kalshi's "Will the maximum temperature be >86° on Sep 5, 2026?" and a
similarly-worded Polymarket contract on the same city/date). Session 3.2
(Arbitrage Detection Logic) reads this script's output to decide which
matched pairs are actually mispriced against each other.

WHAT MATCHING METHOD THIS VERSION USES, AND WHY
----------------------------------------------------
Neither venue exposes a shared ID for "the same real-world question" —
Kalshi's ticker and Polymarket's conditionId are each internal to that one
venue. This first version matches on:
1. Title word-overlap: both titles are lowercased, stripped of common stop
   words, and compared using a simple Jaccard-similarity score (the size
   of the shared word set divided by the size of the combined word set).
2. Close-time proximity: the two contracts' close_time values must fall
   within CLOSE_TIME_TOLERANCE_HOURS of each other, since two contracts on
   the same real-world event should resolve at close to the same time.

A pair is only proposed as a candidate match if BOTH conditions clear
their threshold — word overlap alone is not enough, since two unrelated
contracts can share generic words ("Will", "the", team names), and
close-time proximity alone is not enough, since many unrelated contracts
close at the same time (e.g. many weather contracts all close at midnight
local time on the same day).

THIS IS A DELIBERATELY CONSERVATIVE FIRST VERSION, NOT A FINISHED MATCHER
-------------------------------------------------------------------------
This word-overlap approach will miss real matches that are worded very
differently (e.g. Kalshi's ticker-driven, formal-question style vs.
Polymarket's often more colloquial phrasing) and will need real, live
Kalshi/Polymarket data on the SAME real-world event to validate against —
which requires both venues actually listing an overlapping market at the
same time this project checks (weather markets, confirmed both venues
carry temperature contracts, are the most likely near-term candidate for
this — see the "next validation step" note in Session 3.1's own SESSION_LOG
entry). Every candidate pair this script proposes is written out with its
own similarity score and time gap, not silently auto-confirmed — a human
(or a future, better matcher) should review the candidate list before
Session 3.2's arbitrage logic is allowed to treat a pair as definitely the
same event.

WHERE OUTPUT GOES
------------------
/data/exchange/matched/candidate_matches_<timestamp>.csv — every candidate
    pair found, with its similarity score and close-time gap, for review.

USAGE
-----
python venue_matcher.py
    (reads kalshi_latest.csv and polymarket_latest.csv from
    /data/exchange/normalized/ — run both ingestion scripts first)
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

# Thresholds — starting values, not yet validated against a real matched
# pair (see module docstring). Flagged here as named constants, the same
# "no silent adjustments" pattern as sizing_engine.py's KELLY_FRACTION, so
# a future session can find and recalibrate them in one place.
MIN_TITLE_SIMILARITY = 0.35
CLOSE_TIME_TOLERANCE_HOURS = 6.0

_STOPWORDS = {
    "will", "the", "a", "an", "in", "on", "at", "to", "of", "be", "is",
    "are", "or", "and", "than", "more", "less", "for", "by",
}


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
            "%s does not exist — run its ingestion script first. "
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


def find_candidate_matches(
    kalshi_rows: list[dict], polymarket_rows: list[dict]
) -> list[dict]:
    """Compares Kalshi rows against Polymarket rows using a TIME-BUCKETED
    approach, not a full n*m scan of every pair.

    BUG FOUND AND FIXED (Session 3.1, third real run, 2026-09-04): the
    original version of this function compared every Kalshi row against
    every Polymarket row unconditionally — with Kalshi's real confirmed
    count at 60,000 rows and Polymarket's at roughly 2,100, that is about
    126 million comparisons, which ran long enough on a real run that it
    looked hung rather than just slow. This function's own docstring
    originally called the naive approach "acceptable... in the thousands,
    not millions" and flagged revisiting it "if either venue's live count
    grows an order of magnitude" — that threshold was already crossed by
    Kalshi's real, confirmed count, and this was not re-checked against
    the real numbers once they came in. This is a real correction, not a
    silent optimization: the fix does not change WHICH pairs can match
    (close-time proximity is already a hard requirement for any real
    match — see the module docstring), it only skips pairs that could
    never have passed that requirement in the first place.

    HOW THE BUCKETING WORKS: every row's close_time is rounded down into a
    fixed-width time bucket (width = CLOSE_TIME_TOLERANCE_HOURS, the same
    tolerance already used for real matching). A Kalshi row can only match
    a Polymarket row in its OWN bucket or an immediately ADJACENT bucket —
    covering the case where two close times are within tolerance of each
    other but fall just either side of a bucket boundary. This turns the
    comparison count from (Kalshi rows x Polymarket rows) into roughly
    (Kalshi rows x average Polymarket rows per bucket), which is small in
    practice since real close times cluster around a limited number of
    real-world moments (e.g. many contracts closing at midnight, or at a
    game's real start time), not spread evenly across all of history.
    """
    candidates: list[dict] = []

    kalshi_parsed = [
        (row, _title_words(row.get("title")), _parse_close_time(row.get("close_time")))
        for row in kalshi_rows
    ]
    polymarket_parsed = [
        (row, _title_words(row.get("title")), _parse_close_time(row.get("close_time")))
        for row in polymarket_rows
    ]

    bucket_seconds = CLOSE_TIME_TOLERANCE_HOURS * 3600.0

    def _bucket_key(dt: Optional[datetime]) -> Optional[int]:
        if dt is None:
            return None
        return int(dt.timestamp() // bucket_seconds)

    # Index Polymarket rows by bucket so a Kalshi row only has to check the
    # small number of Polymarket rows near it in time, not all of them.
    polymarket_by_bucket: dict[int, list] = {}
    for p_row, p_words, p_close in polymarket_parsed:
        bucket = _bucket_key(p_close)
        if bucket is None:
            continue  # no close_time to bucket on — same real, named skip
            # as the original version (can't confirm close-time proximity).
        polymarket_by_bucket.setdefault(bucket, []).append((p_row, p_words, p_close))

    for k_row, k_words, k_close in kalshi_parsed:
        k_bucket = _bucket_key(k_close)
        if k_bucket is None:
            continue

        # Check the row's own bucket plus both neighbors, to catch real
        # matches that fall just either side of a bucket boundary.
        nearby_polymarket_rows = []
        for offset in (-1, 0, 1):
            nearby_polymarket_rows.extend(polymarket_by_bucket.get(k_bucket + offset, []))

        for p_row, p_words, p_close in nearby_polymarket_rows:
            similarity = _jaccard_similarity(k_words, p_words)
            if similarity < MIN_TITLE_SIMILARITY:
                continue

            gap_hours = abs((k_close - p_close).total_seconds()) / 3600.0
            if gap_hours > CLOSE_TIME_TOLERANCE_HOURS:
                continue

            candidates.append(
                {
                    "kalshi_source_market_id": k_row.get("source_market_id"),
                    "kalshi_title": k_row.get("title"),
                    "kalshi_yes_ask": k_row.get("yes_ask"),
                    "kalshi_no_ask": k_row.get("no_ask"),
                    "polymarket_source_market_id": p_row.get("source_market_id"),
                    "polymarket_title": p_row.get("title"),
                    "polymarket_yes_ask": p_row.get("yes_ask"),
                    "polymarket_no_ask": p_row.get("no_ask"),
                    "title_similarity": round(similarity, 3),
                    "close_time_gap_hours": round(gap_hours, 2),
                }
            )

    return candidates


def write_candidates_csv(path: Path, candidates: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "kalshi_source_market_id",
        "kalshi_title",
        "kalshi_yes_ask",
        "kalshi_no_ask",
        "polymarket_source_market_id",
        "polymarket_title",
        "polymarket_yes_ask",
        "polymarket_no_ask",
        "title_similarity",
        "close_time_gap_hours",
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

    out_path = MATCHED_DIR / f"candidate_matches_{pulled_at_compact}.csv"
    write_candidates_csv(out_path, candidates)

    log.info(
        "=== Venue matcher run complete: %d candidate pairs from %d Kalshi "
        "rows x %d Polymarket rows ===",
        len(candidates),
        len(kalshi_rows),
        len(polymarket_rows),
    )

    return {
        "kalshi_rows_checked": len(kalshi_rows),
        "polymarket_rows_checked": len(polymarket_rows),
        "candidate_matches_found": len(candidates),
        "output_path": str(out_path),
    }


if __name__ == "__main__":
    import json

    result = run()
    print(json.dumps(result, indent=2))
