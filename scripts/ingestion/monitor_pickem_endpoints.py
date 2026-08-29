"""
Session 2.1 — Unattended Endpoint Monitor (Underdog + PrizePicks)

WHAT THIS SCRIPT IS
--------------------
An alternative to manually re-running prototype_underdog.py and
prototype_prizepicks.py several times throughout the day. This script does
that automatically: it calls both endpoints on a timer, in the background,
and writes one short line to a log file per check. Start it once in the
morning (or whenever), leave the window open (or minimized), and read the
log at the end of the day.

This does NOT replace the two prototype scripts — it reuses their same
endpoints, just on a loop, and only logs a compact summary each time (not a
full snapshot) so the log file stays small and easy to read in one pass.

WHY A TIMER, NOT JUST "RUN IT MORE"
------------------------------------
The goal of a full day's check is to see two things a single run cannot show:
  1. Does the data actually change over the day (a sign it's genuinely live,
     not cached/static)?
  2. Does either endpoint ever fail partway through the day (rate limiting,
     an outage, a schema change)?
Neither question can be answered faster by running the check five times in
the next ten minutes — only by spreading checks across real elapsed time.
This script just removes the need for a person to be the one triggering each
check.

DEFAULT BEHAVIOR
-----------------
Checks both endpoints every 30 minutes, for 12 hours (25 checks total), then
stops on its own. Adjust CHECK_INTERVAL_MINUTES and TOTAL_DURATION_HOURS
below if you want a different cadence or window.

USAGE
-----
    python monitor_pickem_endpoints.py

Leave the terminal window open. To stop early, press Ctrl+C — everything
logged so far is still saved.

OUTPUT
------
Writes to monitor_log.jsonl (one JSON object per line, in the same folder).
Each line records: timestamp, platform, success/failure, record counts, and
a small sample of stat_value/line_score numbers so you can eyeball whether
lines are actually moving between checks, without opening every snapshot.
"""

import json
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

CHECK_INTERVAL_MINUTES = 30
TOTAL_DURATION_HOURS = 12

LOG_PATH = Path("monitor_log.jsonl")

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json",
}

UNDERDOG_ENDPOINT = "https://api.underdogfantasy.com/beta/v3/over_under_lines"
PRIZEPICKS_ENDPOINT = "https://partner-api.prizepicks.com/projections"
PRIZEPICKS_PARAMS = {"per_page": 25}


def check_underdog() -> dict:
    result = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "platform": "underdog",
    }
    try:
        resp = requests.get(UNDERDOG_ENDPOINT, headers=HEADERS, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        lines = data.get("over_under_lines", [])
        result["success"] = True
        result["record_count"] = len(lines)
        result["sample_stat_values"] = [line.get("stat_value") for line in lines[:5]]
    except requests.exceptions.RequestException as exc:
        result["success"] = False
        result["error"] = str(exc)
    return result


def check_prizepicks() -> dict:
    result = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "platform": "prizepicks",
    }
    try:
        resp = requests.get(
            PRIZEPICKS_ENDPOINT, headers=HEADERS, params=PRIZEPICKS_PARAMS, timeout=15
        )
        resp.raise_for_status()
        data = resp.json()
        entries = data.get("data", [])
        result["success"] = True
        result["record_count"] = len(entries)
        result["sample_line_scores"] = [
            e.get("attributes", {}).get("line_score") for e in entries[:5]
        ]
    except requests.exceptions.RequestException as exc:
        result["success"] = False
        result["error"] = str(exc)
    return result


def append_log(entry: dict) -> None:
    with LOG_PATH.open("a") as f:
        f.write(json.dumps(entry) + "\n")


def run_one_check_round(round_number: int, total_rounds: int) -> None:
    print(f"\n[Check {round_number}/{total_rounds}] {datetime.now().strftime('%H:%M:%S')}")

    ud_result = check_underdog()
    append_log(ud_result)
    if ud_result["success"]:
        print(f"  Underdog: OK — {ud_result['record_count']} lines")
    else:
        print(f"  Underdog: FAILED — {ud_result['error']}")

    pp_result = check_prizepicks()
    append_log(pp_result)
    if pp_result["success"]:
        print(f"  PrizePicks: OK — {pp_result['record_count']} projections")
    else:
        print(f"  PrizePicks: FAILED — {pp_result['error']}")


if __name__ == "__main__":
    total_checks = int((TOTAL_DURATION_HOURS * 60) / CHECK_INTERVAL_MINUTES) + 1
    print(
        f"Starting monitor: checking every {CHECK_INTERVAL_MINUTES} minutes "
        f"for {TOTAL_DURATION_HOURS} hours ({total_checks} checks total)."
    )
    print(f"Logging to: {LOG_PATH.resolve()}")
    print("Press Ctrl+C to stop early — everything logged so far is kept.\n")

    try:
        for i in range(1, total_checks + 1):
            run_one_check_round(i, total_checks)
            if i < total_checks:
                time.sleep(CHECK_INTERVAL_MINUTES * 60)
    except KeyboardInterrupt:
        print("\nStopped early by user. Log file has everything captured so far.")

    print(f"\nDone. Review {LOG_PATH.resolve()} — or just tell Claude you're")
    print("ready to look at it together.")
