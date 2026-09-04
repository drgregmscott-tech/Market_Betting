"""
Session 3.1 — Kalshi Series Discovery (diagnostic, not part of the pipeline)

WHY THIS EXISTS
----------------
The project needs a real answer to two questions before switching Kalshi
ingestion from a blind full-catalog pull to a targeted one:
1. Does Kalshi's series-list endpoint work without an API key, the same
   way /markets and /events do? (Kalshi's own SDK docs show it under
   bearerAuth, which would mean it does NOT — but a separate getting-
   started guide calls a single-series lookup with no auth at all, so
   this needs a real, direct answer, not another guess.)
2. If it does work, how many real series exist in this project's actual
   in-scope categories (Climate, and narrow down-ballot Politics/
   Elections — NOT general Economics, Finance, Crypto, Culture, Mentions,
   or Tech & Science, which Session 0.1 explicitly ruled out)?

USAGE
-----
pip install requests --break-system-packages
python discover_kalshi_series.py
"""

import json

import requests

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json",
}

BASE_URL = "https://api.elections.kalshi.com/trade-api/v2"

# Candidate category strings to try. Kalshi's terminology page confirms a
# category filter exists but doesn't give the exact string values it
# accepts — these are reasonable guesses based on names seen in this
# project's own Session 0.1 research (Trending, Elections, Politics,
# Culture, Sports, Crypto, Commodities, Climate, Economics, Mentions,
# Finance, Tech & Science) plus the "Climate and Weather" label style seen
# in one search result. Printing the RAW response for each lets us see
# real category strings back, rather than assuming these guesses are
# exactly right.
CANDIDATE_CATEGORIES = ["Climate", "Weather", "Climate and Weather", "Politics", "Elections"]


def try_list_all_series():
    print("=== Step 1: does GET /series work without an API key? ===")
    url = f"{BASE_URL}/series"
    try:
        response = requests.get(url, headers=HEADERS, timeout=15)
        print(f"Status code: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            series_list = data.get("series", data if isinstance(data, list) else [])
            print(f"SUCCESS — {len(series_list)} total series returned, no API key needed.")
            categories_seen = {}
            for s in series_list:
                cat = s.get("category", "(none)")
                categories_seen[cat] = categories_seen.get(cat, 0) + 1
            print("Real category breakdown across all series:")
            for cat, count in sorted(categories_seen.items(), key=lambda x: -x[1]):
                print(f"  {cat}: {count}")
            return series_list
        else:
            print(f"Did NOT succeed. Response body: {response.text[:500]}")
            return None
    except requests.exceptions.RequestException as exc:
        print(f"Request failed entirely: {exc}")
        return None


def try_category_filters():
    print("\n=== Step 2: trying category filter values directly ===")
    for cat in CANDIDATE_CATEGORIES:
        url = f"{BASE_URL}/series"
        try:
            response = requests.get(
                url, headers=HEADERS, params={"category": cat}, timeout=15
            )
            if response.status_code == 200:
                data = response.json()
                series_list = data.get("series", data if isinstance(data, list) else [])
                print(f"category={cat!r}: {response.status_code}, {len(series_list)} series")
                for s in series_list[:10]:
                    print(f"    {s.get('ticker')}: {s.get('title')}")
            else:
                print(f"category={cat!r}: {response.status_code} — {response.text[:200]}")
        except requests.exceptions.RequestException as exc:
            print(f"category={cat!r}: request failed — {exc}")


def try_single_known_series():
    print("\n=== Step 3: confirming single-series lookup (known to work) ===")
    url = f"{BASE_URL}/series/KXHIGHNY"
    try:
        response = requests.get(url, headers=HEADERS, timeout=15)
        print(f"GET /series/KXHIGHNY: {response.status_code}")
        if response.status_code == 200:
            print(json.dumps(response.json(), indent=2)[:500])
    except requests.exceptions.RequestException as exc:
        print(f"Request failed: {exc}")


if __name__ == "__main__":
    all_series = try_list_all_series()
    if all_series is None:
        try_category_filters()
    try_single_known_series()
