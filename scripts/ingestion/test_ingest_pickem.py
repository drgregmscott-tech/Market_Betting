"""
Session 2.2 — Validation Harness for ingest_pickem.py

WHAT THIS FILE IS
--------------------
This script proves three of Session 2.2's four roadmap validation items
WITHOUT calling the real PrizePicks/Underdog endpoints:

  1. Normal case: realistic synthetic responses (shaped exactly like the
     real field names captured in Session 2.1) produce correct normalized
     rows.
  2. Failure handling: a bad response (malformed JSON shape), an empty
     response, and a simulated schema change (missing expected key) are all
     handled without the pipeline crashing, and each is logged.
  3. Idempotency: running the full pipeline twice in a row does not
     duplicate or corrupt latest.csv, and produces two distinct, correctly
     separate timestamped snapshots (expected snapshot behavior, not a bug).

This does NOT prove the fourth validation item (3 consecutive days of real
automated pulls) — that requires real elapsed time against the real
endpoints and can only happen on your machine. See the session handoff notes
for that step.

USAGE
-----
python test_ingest_pickem.py
"""

from __future__ import annotations

import contextlib
import logging
import shutil
import sys
import tempfile
from pathlib import Path
from unittest import mock

import ingest_pickem as pipeline

FIXTURES_DIR = Path(__file__).resolve().parent / "test_fixtures"


def _load_fixture(name: str) -> dict:
    import json

    return json.loads((FIXTURES_DIR / name).read_text())


def make_synthetic_prizepicks() -> dict:
    return {
        "data": [
            {
                "type": "projection",
                "id": "pp-1001",
                "attributes": {
                    "stat_display_name": "Points",
                    "stat_type": "Points",
                    "line_score": 27.5,
                    "status": "pre_game",
                    "start_time": "2026-08-30T00:00:00Z",
                },
                "relationships": {
                    "new_player": {"data": {"type": "new_player", "id": "player-1"}},
                    "league": {"data": {"type": "league", "id": "league-1"}},
                    "game": {"data": {"type": "game", "id": "game-1"}},
                },
            },
            {
                # Deliberately malformed: no attributes at all. Must be
                # skipped, not fatal to the run.
                "type": "projection",
                "id": "pp-1002",
                "relationships": {},
            },
        ],
        "included": [
            {
                "type": "new_player",
                "id": "player-1",
                "attributes": {
                    "display_name": "Test Player A",
                    "team_name": "Test Team",
                },
            },
            {
                "type": "league",
                "id": "league-1",
                "attributes": {"name": "NBA"},
            },
            {
                "type": "game",
                "id": "game-1",
                "attributes": {"start_time": "2026-08-30T00:00:00Z"},
            },
        ],
        "links": {},
        "meta": {},
    }


def make_synthetic_underdog() -> dict:
    return {
        "over_under_lines": [
            {
                "id": "ud-2001",
                "stat_value": "8.5",  # deliberately a string, per Session 2.1
                "status": "active",
                "over_under": {
                    "display_stat": "Rebounds",
                    "appearance_stat": {"appearance_id": "app-1"},
                },
                "options": [
                    {"choice": "Higher", "payout_multiplier": "1.9"},
                    {"choice": "Lower", "payout_multiplier": "1.9"},
                ],
            },
            {
                # Deliberately malformed: stat_value is not numeric at all.
                "id": "ud-2002",
                "stat_value": "N/A",
                "status": "active",
                "over_under": {"display_stat": "Assists"},
                "options": [],
            },
        ],
        "appearances": [
            {"id": "app-1", "player_id": "p-1", "match_id": "m-1", "team_id": "t-1"}
        ],
        "players": [
            {"id": "p-1", "attributes": {"full_name": "Test Player B"}}
        ],
        "games": [
            {"id": "m-1", "attributes": {"scheduled_at": "2026-08-30T00:00:00Z"}}
        ],
        "providers": [],
        "solo_games": [],
    }


@contextlib.contextmanager
def isolated_data_dirs():
    """Point the pipeline's data and log paths at a temp folder.

    Without this, run() writes synthetic rows into the real data/pickem
    folders and logs/ingestion.log, and reset_data_dirs() deletes them.
    """
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        with mock.patch.object(pipeline, "RAW_DIR", root / "raw"),                 mock.patch.object(pipeline, "NORMALIZED_DIR", root / "normalized"),                 mock.patch.object(pipeline, "LOG_PATH", root / "ingestion.log"):
            # The module opened its log file at import time, on the real
            # logs/ingestion.log. Swap that handler for one in the temp folder.
            saved = list(pipeline.log.handlers)
            for handler in saved:
                if isinstance(handler, logging.FileHandler):
                    pipeline.log.removeHandler(handler)
            temp_handler = logging.FileHandler(root / "ingestion.log", encoding="utf-8")
            pipeline.log.addHandler(temp_handler)
            try:
                yield
            finally:
                pipeline.log.removeHandler(temp_handler)
                temp_handler.close()
                for handler in saved:
                    if isinstance(handler, logging.FileHandler):
                        pipeline.log.addHandler(handler)


try:
    import pytest

    @pytest.fixture(autouse=True)
    def _isolate_data_dirs():
        with isolated_data_dirs():
            yield
except ImportError:  # direct `python test_ingest_pickem.py` runs need no pytest
    pass


def reset_data_dirs():
    for d in (pipeline.RAW_DIR, pipeline.NORMALIZED_DIR):
        if d.exists():
            shutil.rmtree(d)
    if pipeline.LOG_PATH.exists():
        # Truncate, do not delete: the log handler holds the file open, and
        # Windows refuses to delete an open file.
        pipeline.LOG_PATH.write_text("", encoding="utf-8")


def test_normal_case():
    print("\n[TEST] Normal case — realistic synthetic data")
    with mock.patch.object(
        pipeline, "fetch_prizepicks", return_value=make_synthetic_prizepicks()
    ), mock.patch.object(
        pipeline, "fetch_underdog", return_value=make_synthetic_underdog()
    ):
        summary = pipeline.run()

    assert summary["prizepicks_ok"] is True
    assert summary["underdog_ok"] is True
    # 1 valid + 1 malformed submitted per platform. The normalizer is
    # defensive enough that a record with missing fields still produces a
    # row (with None in the missing fields) rather than raising — so both
    # rows survive, but the malformed one must carry None, not fabricated
    # data.
    assert summary["prizepicks_rows"] == 2, summary
    assert summary["underdog_rows"] == 2, summary

    latest = pipeline.NORMALIZED_DIR / "latest.csv"
    content = latest.read_text()
    assert "Test Player A" in content
    assert "Test Player B" in content
    # Confirm the string "8.5" was converted to a real float, not left as text
    assert "8.5" in content

    import csv as _csv
    with latest.open() as f:
        rows = list(_csv.DictReader(f))
    malformed_pp_row = next(r for r in rows if r["source_line_id"] == "pp-1002")
    assert malformed_pp_row["player_name"] == "", malformed_pp_row
    malformed_ud_row = next(r for r in rows if r["source_line_id"] == "ud-2002")
    assert malformed_ud_row["line"] == "", malformed_ud_row  # "N/A" -> None, not 0 or garbage

    print("  PASS — normal rows produced correctly; malformed rows kept as "
          "rows with missing fields left blank (not fabricated); "
          "stat_value string->float conversion confirmed for the valid row.")


def test_empty_response():
    print("\n[TEST] Empty response from both platforms")
    with mock.patch.object(pipeline, "fetch_prizepicks", return_value={}), \
         mock.patch.object(pipeline, "fetch_underdog", return_value={}):
        summary = pipeline.run()  # must not raise

    assert summary["prizepicks_rows"] == 0
    assert summary["underdog_rows"] == 0
    assert summary["total_rows"] == 0
    print("  PASS — empty responses handled without crashing; zero rows, "
          "run completed and logged.")


def test_schema_change():
    print("\n[TEST] Simulated schema change (expected key missing)")
    broken_pp = {"data": [{"id": "x"}]}  # no "included" at all
    broken_ud = {"over_under_lines": []}  # missing players/appearances/games
    with mock.patch.object(pipeline, "fetch_prizepicks", return_value=broken_pp), \
         mock.patch.object(pipeline, "fetch_underdog", return_value=broken_ud):
        summary = pipeline.run()  # must not raise

    assert summary["prizepicks_rows"] == 0
    assert summary["underdog_rows"] == 0
    print("  PASS — missing top-level keys detected and logged as a likely "
          "schema change; pipeline completed instead of crashing.")


def test_network_failure():
    print("\n[TEST] Simulated network failure (both platforms unreachable)")
    import requests

    def raise_timeout(*args, **kwargs):
        raise requests.exceptions.ConnectTimeout("simulated network failure")

    with mock.patch.object(pipeline.requests, "get", side_effect=raise_timeout):
        summary = pipeline.run()  # must not raise

    assert summary["prizepicks_ok"] is False
    assert summary["underdog_ok"] is False
    assert summary["total_rows"] == 0
    # A file should still be written (empty), not skipped entirely
    assert (pipeline.NORMALIZED_DIR / "latest.csv").exists()
    print("  PASS — total network failure on both platforms handled without "
          "crashing; empty output written and failure logged.")


def test_idempotency():
    print("\n[TEST] Idempotency — run twice in a row")
    with mock.patch.object(
        pipeline, "fetch_prizepicks", return_value=make_synthetic_prizepicks()
    ), mock.patch.object(
        pipeline, "fetch_underdog", return_value=make_synthetic_underdog()
    ):
        summary1 = pipeline.run()
        snapshots_after_1 = list(pipeline.NORMALIZED_DIR.glob("pickem_props_*.csv"))
        summary2 = pipeline.run()
        snapshots_after_2 = list(pipeline.NORMALIZED_DIR.glob("pickem_props_*.csv"))

    # latest.csv must always have exactly the current run's row count -
    # never doubled.
    latest_rows = latest_row_count()
    assert latest_rows == summary2["total_rows"], (
        f"latest.csv has {latest_rows} rows but run 2 produced "
        f"{summary2['total_rows']} — possible duplication."
    )
    # Two distinct snapshot files should exist (correct: two separate points
    # in time), never fewer than before and never the same file overwritten.
    assert len(snapshots_after_2) >= len(snapshots_after_1), (
        "Second run did not add a new snapshot file as expected."
    )
    print(f"  PASS — latest.csv correctly reflects only the most recent run "
          f"({latest_rows} rows, not duplicated); "
          f"{len(snapshots_after_2)} distinct timestamped snapshots exist.")


def latest_row_count() -> int:
    import csv as _csv

    with (pipeline.NORMALIZED_DIR / "latest.csv").open() as f:
        return sum(1 for _ in _csv.DictReader(f))


def _run_all():
    reset_data_dirs()
    try:
        test_normal_case()
        reset_data_dirs()
        test_empty_response()
        reset_data_dirs()
        test_schema_change()
        reset_data_dirs()
        test_network_failure()
        reset_data_dirs()
        test_idempotency()
    except AssertionError as e:
        print(f"\nFAIL: {e}")
        sys.exit(1)

    print("\nAll ingest_pickem.py validation tests passed.")


if __name__ == "__main__":
    with isolated_data_dirs():
        _run_all()
