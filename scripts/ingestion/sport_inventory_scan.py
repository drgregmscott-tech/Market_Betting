"""
sport_inventory_scan.py

Purpose (Session 2.10 — Cross-Sport +EV Inventory, Track 1):
List every sport/league that is CURRENTLY LIVE on PrizePicks and Underdog,
right now, at the moment this script is run. This is not a production
ingestion script — it does not write to clv_log.csv or touch any other
project file. It only prints a summary so the findings can be copied into
/docs/research/sport_inventory.md.

Why this has to run on your machine, not Claude's:
Claude's browser tool is blocked by its own safety filter from reaching
prizepicks.com and pick6.draftkings.com (confirmed back in Session 2.1),
so PrizePicks cannot be checked from Claude's side at all. Underdog is
reachable from Claude's side and was already checked directly as part of
this session — but re-running it here too means both platforms are
checked from the same real snapshot in time, which matters because these
endpoints are live and change hour to hour (e.g. whether MLB games happen
to be in progress right now).

How to run:
    python sport_inventory_scan.py

Output:
    Prints a per-platform breakdown of sport/league codes and counts to
    the screen. Copy the printed output back to Claude to fold into
    sport_inventory.md — no file is written automatically, so nothing to
    place or push for this step.
"""

import requests
from collections import Counter

PRIZEPICKS_URL = "https://api.prizepicks.com/projections?per_page=10000"
UNDERDOG_URL = "https://api.underdogfantasy.com/beta/v3/over_under_lines"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
    )
}


def scan_prizepicks():
    print("\n=== PrizePicks ===")
    try:
        resp = requests.get(PRIZEPICKS_URL, headers=HEADERS, timeout=30)
        resp.raise_for_status()
    except Exception as exc:
        print(f"FAILED to reach PrizePicks: {exc}")
        return

    data = resp.json()
    included = data.get("included", [])

    # League/sport info lives on "league" objects; projections reference
    # them via relationships. We count how many live projections exist
    # per league name, which is what "currently listed" means here.
    leagues_by_id = {}
    for item in included:
        if item.get("type") == "league":
            leagues_by_id[item["id"]] = item.get("attributes", {}).get("name", "UNKNOWN")

    league_counts = Counter()
    projections = [d for d in data.get("data", []) if d.get("type") == "projection"]
    for proj in projections:
        rel = proj.get("relationships", {}).get("league", {}).get("data")
        league_id = rel.get("id") if rel else None
        league_name = leagues_by_id.get(league_id, f"unknown_league_id_{league_id}")
        league_counts[league_name] += 1

    print(f"Total live projections: {len(projections)}")
    print(f"Total distinct leagues found: {len(league_counts)}")
    for league, count in league_counts.most_common():
        print(f"  {league:30s} {count}")


def scan_underdog():
    print("\n=== Underdog ===")
    try:
        resp = requests.get(UNDERDOG_URL, headers=HEADERS, timeout=30)
        resp.raise_for_status()
    except Exception as exc:
        print(f"FAILED to reach Underdog: {exc}")
        return

    data = resp.json()

    games = data.get("games", [])
    solo_games = data.get("solo_games", [])
    players = data.get("players", [])
    appearances = data.get("appearances", [])
    lines = data.get("over_under_lines", [])

    game_sports = Counter(g.get("sport_id", "UNKNOWN") for g in games)
    solo_sports = Counter(g.get("sport_id", "UNKNOWN") for g in solo_games)
    player_sports = Counter(p.get("sport_id", "UNKNOWN") for p in players)
    match_types = Counter(a.get("match_type", "UNKNOWN") for a in appearances)

    print(f"Total live lines: {len(lines)}")
    print(f"Total appearances: {len(appearances)}")
    print(f"\n  games[] sport_id counts:      {dict(game_sports)}")
    print(f"  solo_games[] sport_id counts: {dict(solo_sports)}")
    print(f"  players[] sport_id counts:    {dict(player_sports)}")
    print(f"  appearances[] match_type:     {dict(match_types)}")


if __name__ == "__main__":
    scan_prizepicks()
    scan_underdog()
    print(
        "\nDone. Copy everything above back to Claude so it can be folded "
        "into /docs/research/sport_inventory.md. Consider running this "
        "again at a different time of day (e.g. evening, when more MLB "
        "games are live) since these are live snapshots, not fixed lists."
    )
