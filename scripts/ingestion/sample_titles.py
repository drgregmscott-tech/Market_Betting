"""
Session 3.1 — Sample Unclassified Titles (diagnostic, not part of the pipeline)

WHY THIS EXISTS
----------------
composition_check.py's real run found Kalshi's actual data is 98.4%
"unclassified" against a small hand-written keyword list — including 0%
"weather," even though every Kalshi title pulled live earlier this session
was a temperature contract. That mismatch means the keyword list is
missing whatever really makes up Kalshi's current catalog, not that
Kalshi's catalog stopped being weather-heavy. Rather than keep guessing
keywords, this script just prints real, random titles from the
"unclassified" bucket in each file, so the next step is based on what's
actually there.

USAGE
-----
python sample_titles.py
    (reads kalshi_latest.csv and polymarket_latest.csv from
    /data/exchange/normalized/ — run the ingestion scripts first)
"""

import csv
import random
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
NORMALIZED_DIR = BASE_DIR / "data" / "exchange" / "normalized"

# Same keyword list as composition_check.py, kept identical on purpose so
# "unclassified" means the same thing in both scripts.
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

SAMPLE_SIZE = 25


def is_unclassified(title: str) -> bool:
    if not title:
        return True
    lowered = title.lower()
    return not any(w in lowered for cat_words in KEYWORDS.values() for w in cat_words)


def sample_unclassified(path: Path, label: str) -> None:
    if not path.exists():
        print(f"{label}: file not found at {path} — run its ingestion script first.")
        return

    with path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    unclassified_titles = [
        row.get("title", "") for row in rows if is_unclassified(row.get("title", ""))
    ]

    print(f"\n=== {label}: {len(unclassified_titles)} unclassified of {len(rows)} total ===")
    if not unclassified_titles:
        print("  (none)")
        return

    sample = random.sample(
        unclassified_titles, min(SAMPLE_SIZE, len(unclassified_titles))
    )
    for i, title in enumerate(sample, 1):
        print(f"  {i:2d}. {title!r}")


if __name__ == "__main__":
    random.seed()  # real randomness each run, not a fixed sample every time
    sample_unclassified(NORMALIZED_DIR / "kalshi_latest.csv", "Kalshi")
    sample_unclassified(NORMALIZED_DIR / "polymarket_latest.csv", "Polymarket")
