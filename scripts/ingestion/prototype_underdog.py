"""
Session 2.1 — Data Ingestion Prototype: Underdog Fantasy

WHAT THIS SCRIPT IS
--------------------
This is a throwaway proof-of-reach script, not a production pipeline. Its only
two jobs are:
  1. Confirm the endpoint below is reachable from your machine, with no login
     and no API key.
  2. Print out the real field names Underdog returns today, so Session 2.3
     (the estimation model) knows exactly what data it has to work with.

Session 2.2 will turn this into a real, scheduled, error-handled pipeline.
This script is deliberately simple.

ENDPOINT STATUS (confirmed 2026-08-28, via live browser test during this
session): api.underdogfantasy.com/beta/v3/over_under_lines returned live,
current player-prop data successfully, no login or API key required.

WHAT THE RESPONSE LOOKS LIKE
-----------------------------
The response is one JSON object with these top-level lists, cross-referenced
by ID (this is a "normalized" API shape — you look up details in a separate
list rather than getting them inline):

  - "over_under_lines": the actual prop lines. Each one has a "stat_value"
    (the line, e.g. "8.5") and an "over_under" object that names the stat
    (e.g. "Regular Season Games Started") and links to an "appearance_id".
  - "appearances": links a player to a specific game/match and team.
  - "players": player names and metadata, looked up by "player_id".
  - "games": the game/match schedule, looked up by "match_id".

This means: to build one clean row of "Player X, Stat Y, Line Z, Game W" you
must join across three lists using the IDs, not just read "over_under_lines"
on its own. Session 2.2's normalization step needs to do this join.

USAGE
-----
    pip install requests --break-system-packages
    python prototype_underdog.py
"""

import json
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

ENDPOINT = "https://api.underdogfantasy.com/beta/v3/over_under_lines"

# Underdog's endpoint has returned data successfully with no special headers
# during testing, but a normal browser User-Agent is included here as a
# defensive measure — some undocumented endpoints silently rate-limit or
# block requests that look like they're coming from a script.
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json",
}

OUTPUT_DIR = Path("snapshots")


def fetch_underdog_lines() -> dict:
    """Pull the current Underdog over/under lines. Raises on any HTTP error
    or network failure so the caller sees the real failure instead of a
    silent empty result."""
    response = requests.get(ENDPOINT, headers=HEADERS, timeout=15)
    response.raise_for_status()
    return response.json()


def summarize_schema(payload: dict) -> None:
    print("\n--- Underdog: top-level keys and counts ---")
    for key, value in payload.items():
        if isinstance(value, list):
            print(f"  {key}: {len(value)} items")
        else:
            print(f"  {key}: (not a list) {type(value).__name__}")

    if payload.get("over_under_lines"):
        sample = payload["over_under_lines"][0]
        print("\n--- Sample over_under_line record (field names only) ---")
        for key in sample.keys():
            print(f"  {key}")

    if payload.get("players"):
        sample_player = payload["players"][0]
        print("\n--- Sample player record (field names only) ---")
        for key in sample_player.keys():
            print(f"  {key}")


def save_snapshot(payload: dict) -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_path = OUTPUT_DIR / f"underdog_{timestamp}.json"
    out_path.write_text(json.dumps(payload, indent=2))
    return out_path


if __name__ == "__main__":
    start = time.time()
    try:
        data = fetch_underdog_lines()
    except requests.exceptions.RequestException as exc:
        print(f"FAILED to reach Underdog endpoint: {exc}")
        raise SystemExit(1)

    elapsed = time.time() - start
    print(f"Success — response received in {elapsed:.2f}s")

    summarize_schema(data)
    saved_path = save_snapshot(data)
    print(f"\nFull snapshot saved to: {saved_path.resolve()}")
