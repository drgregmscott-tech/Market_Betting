"""
Session 3.1 — Composition Check (diagnostic, not part of the pipeline)

WHAT THIS SCRIPT IS FOR
------------------------
venue_matcher.py's real run found 0 candidate matches between 60,000 real
Kalshi rows and 20,713 real Polymarket rows. Before treating that as a real
finding ("these two venues don't currently overlap") rather than a bug,
this script answers a more basic question first: do the two files even
contain the same KIND of content right now? It counts how many rows in
each file look like weather markets, sports markets, crypto markets, and
politics markets, using simple keyword matching on each row's title. This
is a rough diagnostic, not a real classifier — it exists to tell us
whether to keep investigating the matcher, or accept the zero-match result
as a real reflection of what each venue currently lists.

USAGE
-----
python composition_check.py
    (reads kalshi_latest.csv and polymarket_latest.csv from
    /data/exchange/normalized/ — run the ingestion scripts first)
"""

import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
NORMALIZED_DIR = BASE_DIR / "data" / "exchange" / "normalized"

KEYWORDS = {
    "weather": ["temperature", "rain", "snow", "hurricane", "weather", "climate"],
    "sports": ["nfl", "nba", "mlb", "nhl", "soccer", "football", "basketball",
               "baseball", "hockey", "ufc", "golf", "tennis", "game", "match",
               "beat the", "matchup"],
    "crypto": ["bitcoin", "btc", "ethereum", "eth", "crypto", "solana"],
    "politics_elections": ["election", "president", "senate", "governor",
                            "congress", "vote", "poll", "fed ", "federal reserve",
                            "rate decision", "fomc"],
}


def classify(title: str) -> list[str]:
    if not title:
        return []
    lowered = title.lower()
    return [cat for cat, words in KEYWORDS.items() if any(w in lowered for w in words)]


def summarize(path: Path, label: str) -> None:
    if not path.exists():
        print(f"{label}: file not found at {path} — run its ingestion script first.")
        return

    with path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    counts = {cat: 0 for cat in KEYWORDS}
    uncategorized = 0
    for row in rows:
        cats = classify(row.get("title", ""))
        if not cats:
            uncategorized += 1
        for cat in cats:
            counts[cat] += 1

    print(f"\n=== {label}: {len(rows)} total rows ===")
    for cat, count in counts.items():
        pct = (count / len(rows) * 100) if rows else 0
        print(f"  {cat:20s}: {count:6d} rows ({pct:5.1f}%)")
    pct_unclassified = (uncategorized / len(rows) * 100) if rows else 0
    print(f"  {'(unclassified)':20s}: {uncategorized:6d} rows ({pct_unclassified:5.1f}%)")


if __name__ == "__main__":
    summarize(NORMALIZED_DIR / "kalshi_latest.csv", "Kalshi")
    summarize(NORMALIZED_DIR / "polymarket_latest.csv", "Polymarket")
