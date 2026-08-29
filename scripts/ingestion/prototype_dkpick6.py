"""
Session 2.1 — Data Ingestion Prototype: DraftKings Pick6

WHAT THIS SCRIPT IS
--------------------
A throwaway proof-of-reach script (see prototype_underdog.py for the full
explanation). This one is the most exploratory of the three. DraftKings'
main sportsbook and DFS-contest APIs are well documented by outside
developers, but Pick6 — DraftKings' fixed-line pick'em product, the one this
project actually needs — is a separate, newer product, and no credible public
documentation of its specific data endpoint could be found during this
session's research. Claude's browser tool is also blocked by its safety
filter from visiting pick6.draftkings.com directly, the same restriction
described in the PrizePicks script, so this could not be tested live either.

ENDPOINT STATUS (as of 2026-08-28): UNCONFIRMED AND UNDOCUMENTED. The URL
below is a best-guess pattern, built by analogy to DraftKings' other
documented APIs (which generally follow an "api.draftkings.com/<product>/v1/"
shape). It may be wrong. That is fine — finding out it's wrong, and what the
real one is, is what this script and this session are for.

HOW TO ACTUALLY FIND THE REAL ENDPOINT (if the guess below fails)
-------------------------------------------------------------------
This is the same reverse-engineering approach referenced in ROADMAP.md's
Session 8.4 (Ingestion Health Monitoring) as the repeatable pattern for any
undocumented endpoint that changes or was never found in the first place:

  1. Open pick6.draftkings.com in a normal browser (not this script).
  2. Open the browser's Developer Tools (F12 in Chrome/Edge), and click the
     "Network" tab.
  3. Filter the Network tab to "Fetch/XHR" only.
  4. Browse the Pick6 site normally — click into a sport, scroll the player
     prop list.
  5. Watch the Network tab for requests going to a domain other than
     pick6.draftkings.com itself (likely something like
     "api.draftkings.com/pick6/..." or a similarly-named subdomain) that
     return JSON.
  6. Click that request, open its "Response" tab to see the real JSON shape,
     and copy its exact URL.
  7. Replace the ENDPOINT constant below with that real URL, and re-run this
     script to confirm it works headlessly (i.e. without a logged-in browser
     session), the same way Underdog's endpoint does.

This is manual, one-time work — once found, Session 2.2 treats it the same
as the other two platforms.

USAGE
-----
    pip install requests --break-system-packages
    python prototype_dkpick6.py
"""

import json
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

# BEST-GUESS ENDPOINT — see the docstring above. Expect this to need
# correcting.
ENDPOINT = "https://api.draftkings.com/pick6/v1/leagues"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json",
}

OUTPUT_DIR = Path("snapshots")


def fetch_dkpick6_data() -> dict:
    response = requests.get(ENDPOINT, headers=HEADERS, timeout=15)
    response.raise_for_status()
    return response.json()


def summarize_schema(payload) -> None:
    print("\n--- DK Pick6: response shape ---")
    if isinstance(payload, dict):
        for key, value in payload.items():
            if isinstance(value, list):
                print(f"  {key}: {len(value)} items")
            else:
                print(f"  {key}: (not a list) {type(value).__name__}")
    elif isinstance(payload, list):
        print(f"  Response is a top-level list with {len(payload)} items")
        if payload:
            print("  Sample record field names:")
            for key in payload[0].keys():
                print(f"    {key}")
    else:
        print(f"  Unexpected response type: {type(payload).__name__}")


def save_snapshot(payload) -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_path = OUTPUT_DIR / f"dkpick6_{timestamp}.json"
    out_path.write_text(json.dumps(payload, indent=2))
    return out_path


if __name__ == "__main__":
    start = time.time()
    try:
        data = fetch_dkpick6_data()
    except requests.exceptions.RequestException as exc:
        print(f"FAILED to reach guessed DK Pick6 endpoint: {exc}")
        print(
            "\nThis guessed URL was expected to plausibly fail. Follow the "
            "'HOW TO ACTUALLY FIND THE REAL ENDPOINT' steps in this file's "
            "docstring to find the real one using your browser's Developer "
            "Tools, then update the ENDPOINT constant and re-run."
        )
        raise SystemExit(1)

    elapsed = time.time() - start
    print(f"Success — response received in {elapsed:.2f}s")
    print("(Unexpected but good news — the guessed endpoint worked. Treat")
    print("this schema as provisional until confirmed stable over repeat runs.)")

    summarize_schema(data)
    saved_path = save_snapshot(data)
    print(f"\nFull snapshot saved to: {saved_path.resolve()}")
