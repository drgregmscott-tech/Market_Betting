"""
sport_inventory_scan_automated.py

Purpose (Session 2.10 continuation — deferred Underdog sport-inventory
check):
Same job as sport_inventory_scan.py, but built to run unattended on a
schedule (via GitHub Actions) instead of by hand in PowerShell. Instead of
printing results to a screen someone has to be watching, this writes each
run's results to a dated JSON file in the repo, so the results are there
to read later regardless of who's around when the run happens.

This does not touch clv_log.csv, the estimation pipeline, or any other
production file. It only writes new files under docs/research/scans/.

Output: one JSON file per run, named
    docs/research/scans/{platform}_{UTC timestamp}.json
containing the same sport/league breakdown the manual script prints,
plus the timestamp itself so the union list can be built up correctly
across runs without guessing when each one happened.
"""

import json
import os
from collections import Counter
from datetime import datetime, timezone

import requests

PRIZEPICKS_URL = "https://partner-api.prizepicks.com/projections?per_page=10000"
UNDERDOG_URL = "https://api.underdogfantasy.com/beta/v3/over_under_lines"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
    )
}

OUTPUT_DIR = "docs/research/scans"


def scan_prizepicks():
    try:
        resp = requests.get(PRIZEPICKS_URL, headers=HEADERS, timeout=30)
        resp.raise_for_status()
    except Exception as exc:
        return {"error": str(exc)}

    data = resp.json()
    included = data.get("included", [])

    leagues_by_id = {}
    for item in included:
        if item.get("type") == "league":
            leagues_by_id[str(item["id"])] = item.get("attributes", {}).get("name", "UNKNOWN")

    league_counts = Counter()
    projections = [d for d in data.get("data", []) if d.get("type") == "projection"]
    for proj in projections:
        rel = proj.get("relationships", {}).get("league", {}).get("data")
        league_id = str(rel.get("id")) if rel else None
        league_name = leagues_by_id.get(league_id, f"unknown_league_id_{league_id}")
        league_counts[league_name] += 1

    return {
        "total_projections": len(projections),
        "league_counts": dict(league_counts),
    }


def scan_underdog():
    try:
        resp = requests.get(UNDERDOG_URL, headers=HEADERS, timeout=30)
        resp.raise_for_status()
    except Exception as exc:
        return {"error": str(exc)}

    data = resp.json()

    games = data.get("games", [])
    solo_games = data.get("solo_games", [])
    players = data.get("players", [])
    appearances = data.get("appearances", [])
    lines = data.get("over_under_lines", [])

    return {
        "total_lines": len(lines),
        "total_appearances": len(appearances),
        "games_sport_id_counts": dict(Counter(g.get("sport_id", "UNKNOWN") for g in games)),
        "solo_games_sport_id_counts": dict(Counter(g.get("sport_id", "UNKNOWN") for g in solo_games)),
        "players_sport_id_counts": dict(Counter(p.get("sport_id", "UNKNOWN") for p in players)),
        "appearances_match_type_counts": dict(Counter(a.get("match_type", "UNKNOWN") for a in appearances)),
    }


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%SZ")

    result = {
        "run_timestamp_utc": timestamp,
        "prizepicks": scan_prizepicks(),
        "underdog": scan_underdog(),
    }

    out_path = os.path.join(OUTPUT_DIR, f"scan_{timestamp}.json")
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)

    print(f"Wrote {out_path}")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
