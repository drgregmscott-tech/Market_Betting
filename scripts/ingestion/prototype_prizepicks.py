"""
Session 2.1 — Data Ingestion Prototype: PrizePicks

WHAT THIS SCRIPT IS
--------------------
A throwaway proof-of-reach script (see prototype_underdog.py for the full
explanation of what this session is for). This one has a gap the Underdog
script does not: Claude's own browser tool is blocked by its safety filter
from visiting any prizepicks.com-family domain at all, so this endpoint could
not be tested live during this session. Running this script yourself is what
actually closes that gap.

ENDPOINT STATUS (as of 2026-08-28): NOT independently confirmed live by
Claude. The endpoint below (partner-api.prizepicks.com/projections) is
documented, consistently and recently, by multiple outside developers building
their own PrizePicks tools — this is the same endpoint referenced across
several independent public code repositories. That is good secondhand
evidence it is real and currently working, but "documented by others" is not
the same as "confirmed by us." Running this script is the confirmation step.

WHAT THE RESPONSE SHOULD LOOK LIKE (per outside documentation — verify against
the real printed output when you run this)
-----------------------------------------------------------------------------
PrizePicks' API follows a "JSON:API" pattern, which is a specific, named
convention: instead of one flat list of props, you get two lists that
reference each other by ID:

  - "data": the actual prop lines (the projections). Each entry has a "type"
    of "projection" and an "attributes" object that should contain the stat
    type, the line value, the start time of the game, and similar. It also
    has "relationships" — IDs pointing into the "included" list below, rather
    than the player's name directly inline.
  - "included": a mixed list of everything the "data" entries reference —
    player records (name, team, position), league records, and similar
    lookups. You match a projection to its player by following the
    relationship ID, the same join pattern as the Underdog script.

If the real output doesn't match this shape, that is exactly the kind of
finding this prototype session exists to catch — write down what you actually
got instead of what was expected.

USAGE
-----
    pip install requests --break-system-packages
    python prototype_prizepicks.py
"""

import json
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

ENDPOINT = "https://partner-api.prizepicks.com/projections"
PARAMS = {"per_page": 25}  # small page size for this proof-of-reach test only

# PrizePicks' endpoint is known, from outside reports, to sometimes reject
# requests that don't look like they're coming from a real browser. This
# header set is a reasonable starting point; if the request fails, the
# printed error will tell you whether this needs adjusting (see the
# troubleshooting note at the bottom of this file).
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json",
}

OUTPUT_DIR = Path("snapshots")


def fetch_prizepicks_projections() -> dict:
    response = requests.get(ENDPOINT, headers=HEADERS, params=PARAMS, timeout=15)
    response.raise_for_status()
    return response.json()


def summarize_schema(payload: dict) -> None:
    print("\n--- PrizePicks: top-level keys and counts ---")
    for key, value in payload.items():
        if isinstance(value, list):
            print(f"  {key}: {len(value)} items")
        else:
            print(f"  {key}: (not a list) {type(value).__name__}")

    if payload.get("data"):
        sample = payload["data"][0]
        print("\n--- Sample 'data' record (projection) ---")
        print(f"  type: {sample.get('type')}")
        if "attributes" in sample:
            print("  attributes fields:")
            for key in sample["attributes"].keys():
                print(f"    {key}")
        if "relationships" in sample:
            print("  relationships fields:")
            for key in sample["relationships"].keys():
                print(f"    {key}")

    if payload.get("included"):
        included_types = sorted({item.get("type") for item in payload["included"]})
        print(f"\n--- 'included' record types present: {included_types} ---")
        for item_type in included_types:
            example = next(i for i in payload["included"] if i.get("type") == item_type)
            print(f"\n  Sample '{item_type}' attributes fields:")
            for key in example.get("attributes", {}).keys():
                print(f"    {key}")


def save_snapshot(payload: dict) -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_path = OUTPUT_DIR / f"prizepicks_{timestamp}.json"
    out_path.write_text(json.dumps(payload, indent=2))
    return out_path


if __name__ == "__main__":
    start = time.time()
    try:
        data = fetch_prizepicks_projections()
    except requests.exceptions.RequestException as exc:
        print(f"FAILED to reach PrizePicks endpoint: {exc}")
        print(
            "\nTroubleshooting note: if this is a 403 (Forbidden) or 429 "
            "(Too Many Requests) error, the endpoint may be checking for "
            "additional headers (e.g. an Origin or Referer header matching "
            "app.prizepicks.com) or rate-limiting by IP. Report the exact "
            "status code and message back — that detail is exactly what "
            "Session 2.1's validation checklist asks for."
        )
        raise SystemExit(1)

    elapsed = time.time() - start
    print(f"Success — response received in {elapsed:.2f}s")

    summarize_schema(data)
    saved_path = save_snapshot(data)
    print(f"\nFull snapshot saved to: {saved_path.resolve()}")
