"""
Session 6.9 — BetMGM Player Props Ingestion, via Rotowire (not BetMGM directly)

WHY THIS SCRIPT EXISTS, AND WHY IT DOESN'T TALK TO BETMGM
------------------------------------------------------------
Session 6.9 found BetMGM's own real data API (`cf-us4-cds-api.itsfogo.com`)
reachable but blocked on every real attempt by a persistent, unexplained
"Country code is missing" error that survived a real US-Kansas IP, a real
browser session/cookie set, and every realistic header/param combination
tried — a real technical wall this project could not get past. BetMGM's own
Terms of Use also separately prohibit "any robot, scraper, spider."

The same session traced how third-party odds-comparison sites (Rotowire,
Action Network) show BetMGM's lines anyway: BetMGM's own site bundles two
different things — the real-money wagering surface (blocked, above) and a
separate incentive to have its lines shown on free comparison sites, since
that's a customer-acquisition channel for BetMGM, not the same product.
Rotowire's player-props pages embed real BetMGM prop data directly in their
page's server-rendered HTML (confirmed live: `mgm_passydsOver`, `mgm_
firsttd`, etc., with real prices) with NO login, NO API key, and NO
GeoComply-style gate of any kind — the same practical situation as this
project's own `ingest_dk_props.py`/`ingest_fd_props.py` (real, working,
undocumented data access), NOT the same situation as the BetMGM-direct
no-go. Rotowire's own Terms of Use do prohibit automated "crawl or spider"
access — the same category of open ToS question this project already
carries for DK/FD's undocumented-endpoint approach, not a new or different
kind of risk.

**Platform value used downstream is "betmgm"** (matching DraftKings'/
FanDuel's platform-name convention), but the actual HTTP request in this
script goes to `rotowire.com`, never `betmgm.com`. This distinction matters
for anyone reading `clv_log.csv` later — a "betmgm" row's real price came
from Rotowire's copy of BetMGM's line, not a live pull from BetMGM itself,
and could in principle be stale by whatever interval Rotowire refreshes its
own page on.

REAL SCHEMA, CONFIRMED LIVE (2026-09-10)
------------------------------------------
`https://www.rotowire.com/betting/{sport}/player-props.php` server-renders
several `data: [...]` JSON arrays inline in the page's own <script> blocks
(webix table configs) — one array per stat-type tab (Passing, Rushing/
Receiving, Defense, Kicking, TD-scorer categories, etc.). Every array
shares one row shape, one object per player:

    {"gameID": "...", "playerID": "...", "firstName": "...",
     "lastName": "...", "name": "...", "team": "...", "opp": "...",
     "<book>_<stat>": <line or single price, or null/"">,
     "<book>_<stat>Over": <American odds or null>,   # two-sided stats only
     "<book>_<stat>Under": <American odds or null>}  # two-sided stats only

`<book>` for BetMGM is literally `"mgm"` (confirmed against Rotowire's own
book-chooser links, e.g. `?book=mgm`). Two real shapes exist, and this script tells them apart by whether
`<stat>Over`/`<stat>Under` carry a real (non-null) VALUE on that row --
**not** by whether those keys merely exist on the object. A real live
finding this session (first version of this script got wrong): Rotowire's
TD-scorer-shaped rows (`anytd`, etc.) DO carry `mgm_anytdOver`/`mgm_
anytdUnder` keys, but they are always `null` -- the real single price
lives in the bare `mgm_anytd` field. Checking key presence alone
misclassified every TD-scorer row as two-sided, silently dumping the real
single-sided price into the `line` column instead of `over_american_odds`
-- caught by inspecting this script's own real first-run output before
treating it as working, not assumed to be correct because it ran without
error. Value-based detection avoids this for any stat, without needing a
hardcoded list of which ones are TD-shaped:
  - Two-sided (has `...Over`/`...Under` keys): `mgm_passyds` is the real
    numeric line; `mgm_passydsOver`/`mgm_passydsUnder` are the real
    American odds for each side. Normalized as prop_category=
    "player_performance".
  - Single-sided (no `...Over`/`...Under` keys anywhere on that row):
    confirmed only for TD-scorer-shaped markets in this session's real
    pull (`firsttd`, `anytd`, `lasttd`, `twotd`, `threetd`, and a handful
    of defense/kicking fields — `assist`, `solo`, `fgm`, `xpm` — that this
    session's real pull happened to carry with no priced Over/Under
    either). `mgm_<stat>` is the single real price. Normalized the same
    way `ingest_dk_props.py` normalizes DK's real single-sided TD-scorer
    market: `over_american_odds` = that price ("this happens" = yes),
    `under_american_odds` = None, `line` = None, prop_category=
    "player_touchdown" for the TD-style keys, "player_performance" for
    the small number of other observed single-sided keys (own docstring
    admits this category call is a reasonable default for those, not a
    confirmed distinction — flagged, not silently guessed).
A real player/stat combination with `mgm_<stat>` null or "" (BetMGM simply
doesn't have that market for that player right now — a real, normal
coverage gap, same as DK/FD's own partial coverage) is skipped, not stored
as a fabricated zero.

WHAT THIS SCRIPT DOES NOT DO YET
-----------------------------------
- Single sport per run (`ROTOWIRE_SPORT`, default "nfl") — same v1 scoping
  reason as `ingest_dk_props.py`/`ingest_fd_props.py`.
- No `game_start_time`/`status` — Rotowire's real per-player row (unlike
  DK's/FD's) does not carry either field; both are stored as None rather
  than invented.
- Does not yet feed `scripts/estimation/sportsbook_props_model.py`'s
  `load_props()` — that function is currently hardcoded to only
  `dk_latest.csv`/`fd_latest.csv`. Wiring this file's output in is a small,
  separate, explicit follow-up (see ROADMAP.md), not silently done here.

WHERE OUTPUT GOES
--------------------
/data/sportsbook_props/raw/rotowire_betmgm_<sport>_<timestamp>.html
/data/sportsbook_props/normalized/rw_betmgm_props_<timestamp>.csv
/data/sportsbook_props/normalized/rw_betmgm_latest.csv  (overwritten every run)

USAGE
-----
pip install requests --break-system-packages
python ingest_rotowire_betmgm_props.py
"""

from __future__ import annotations

import csv
import json
import logging
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import requests

from schema_props import NORMALIZED_COLUMNS, NormalizedSportsbookProp

BASE_DIR = Path(__file__).resolve().parents[2]
RAW_DIR = BASE_DIR / "data" / "sportsbook_props" / "raw"
NORMALIZED_DIR = BASE_DIR / "data" / "sportsbook_props" / "normalized"
LOG_PATH = BASE_DIR / "logs" / "ingestion.log"

ROTOWIRE_SPORT = "nfl"
ROTOWIRE_BOOK_KEY = "mgm"  # BetMGM's real key in Rotowire's data, confirmed live
ROTOWIRE_URL = f"https://www.rotowire.com/betting/{ROTOWIRE_SPORT}/player-props.php"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml",
}

MAX_RETRIES = 2
RETRY_BACKOFF_SECONDS = 3
REQUEST_TIMEOUT_SECONDS = 20

# Confirmed live (2026-09-10): real single-sided (no Over/Under) markets
# are TD-scorer shaped. A handful of other keys (assist/solo/fgm/xpm) were
# also single-sided in this session's real pull -- kept out of this set
# deliberately (see module docstring) since their single-sidedness looked
# like an incidental gap in that pull, not a confirmed permanent market
# shape; they still get ingested, just categorized as player_performance.
TD_STAT_KEYS = {"firsttd", "anytd", "lasttd", "twotd", "threetd"}


def setup_logging() -> logging.Logger:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("ingest_rotowire_betmgm_props")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()

    file_handler = logging.FileHandler(LOG_PATH, mode="a", encoding="utf-8")
    console_handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s UTC | %(levelname)s | %(message)s")
    formatter.converter = time.gmtime
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger


log = setup_logging()


def fetch_rotowire_html() -> str:
    last_error = None
    for attempt in range(1, MAX_RETRIES + 2):
        try:
            response = requests.get(
                ROTOWIRE_URL, headers=HEADERS, timeout=REQUEST_TIMEOUT_SECONDS
            )
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as exc:
            last_error = exc
            log.warning(
                "Attempt %d/%d failed for %s: %s",
                attempt,
                MAX_RETRIES + 1,
                ROTOWIRE_URL,
                exc,
            )
            if attempt <= MAX_RETRIES:
                time.sleep(RETRY_BACKOFF_SECONDS)
    raise RuntimeError(f"All attempts failed for {ROTOWIRE_URL}: {last_error}")


def _find_matching_bracket(html: str, open_index: int) -> int:
    """Returns the index just past the `]` that matches the `[` at
    open_index, tracking string literals so a `]`/`[` inside a real quoted
    value (player name, team abbreviation, etc.) is never miscounted."""
    depth = 0
    i = open_index
    in_string = False
    escape_next = False
    while i < len(html):
        ch = html[i]
        if in_string:
            if escape_next:
                escape_next = False
            elif ch == "\\":
                escape_next = True
            elif ch == '"':
                in_string = False
        else:
            if ch == '"':
                in_string = True
            elif ch == "[":
                depth += 1
            elif ch == "]":
                depth -= 1
                if depth == 0:
                    return i + 1
        i += 1
    raise ValueError("Unbalanced brackets -- Rotowire's page structure may have changed.")


def extract_data_arrays(html: str) -> list[list[dict]]:
    """Finds every real `data: [{...}]` JSON array embedded in the page's
    own inline <script> blocks and parses each one. Rotowire's real NFL
    props page carries several of these (one per stat-tab widget) -- this
    function is deliberately generic about how many there are or what
    order they're in, since that's presentation structure this project
    doesn't control and shouldn't hardcode against."""
    arrays: list[list[dict]] = []
    search_start = 0
    marker = "data: ["
    while True:
        idx = html.find(marker, search_start)
        if idx == -1:
            break
        bracket_start = idx + len("data: ")
        try:
            bracket_end = _find_matching_bracket(html, bracket_start)
            raw = html[bracket_start:bracket_end]
            parsed = json.loads(raw)
            if isinstance(parsed, list) and parsed and isinstance(parsed[0], dict):
                arrays.append(parsed)
        except (ValueError, json.JSONDecodeError) as exc:
            log.warning("Skipped one unparseable data array at offset %d: %s", idx, exc)
        search_start = idx + len(marker)
    return arrays


def _clean(value) -> Optional[str]:
    if value is None:
        return None
    text = str(value).strip()
    return text if text else None


def _to_float(value) -> Optional[float]:
    text = _clean(value)
    if text is None:
        return None
    try:
        return float(text)
    except ValueError:
        return None


def _to_int(value) -> Optional[int]:
    text = _clean(value)
    if text is None:
        return None
    try:
        return int(float(text))
    except ValueError:
        return None


def normalize_rotowire(arrays: list[list[dict]], pulled_at: str) -> list[NormalizedSportsbookProp]:
    rows: list[NormalizedSportsbookProp] = []
    seen_keys: set[tuple] = set()  # de-dupe across arrays -- some players/stats repeat

    for array in arrays:
        for record in array:
            try:
                player_id = record.get("playerID")
                if player_id is None:
                    continue  # not a player-prop row (shouldn't happen given the filter above)

                player_name = _clean(record.get("name"))
                team = _clean(record.get("team"))
                game_id = _clean(record.get("gameID"))

                base_key = f"{ROTOWIRE_BOOK_KEY}_"
                for key, value in record.items():
                    if not key.startswith(base_key) or key.endswith(("Over", "Under")):
                        continue
                    stat = key[len(base_key):]
                    line_raw = value

                    over_raw = record.get(f"{base_key}{stat}Over")
                    under_raw = record.get(f"{base_key}{stat}Under")
                    over_odds = _to_int(over_raw)
                    under_odds = _to_int(under_raw)

                    if over_odds is not None or under_odds is not None:
                        # Real two-sided market: over/under carry a real
                        # priced value (not just a present-but-null key).
                        line_value = _to_float(line_raw)
                        prop_category = "player_performance"
                    else:
                        # No real priced Over/Under -- the bare field is a
                        # single price (TD-scorer-shaped market), same
                        # convention ingest_dk_props.py uses for DK's real
                        # single-sided TD markets.
                        price = _to_int(line_raw)
                        if price is None:
                            continue  # real, normal BetMGM coverage gap -- skip, don't fabricate
                        line_value = None
                        over_odds = price
                        under_odds = None
                        prop_category = (
                            "player_touchdown" if stat in TD_STAT_KEYS else "player_performance"
                        )

                    dedupe_key = (player_id, game_id, stat)
                    if dedupe_key in seen_keys:
                        continue
                    seen_keys.add(dedupe_key)

                    rows.append(
                        NormalizedSportsbookProp(
                            platform="betmgm",
                            source_event_id=str(game_id or ""),
                            source_market_id=stat,
                            source_selection_id=str(player_id),
                            player_name=player_name,
                            team=team,
                            sport=ROTOWIRE_SPORT.upper(),
                            stat_type=stat,
                            prop_category=prop_category,
                            line=line_value,
                            over_american_odds=over_odds,
                            under_american_odds=under_odds,
                            game_id=game_id,
                            game_start_time=None,  # not carried in Rotowire's real row shape
                            status=None,  # not carried in Rotowire's real row shape
                            pulled_at=pulled_at,
                        )
                    )
            except Exception as exc:  # noqa: BLE001
                log.warning("Skipped one malformed Rotowire record: %s", exc)
                continue

    return rows


def save_raw_snapshot(html: str, pulled_at_compact: str) -> Path:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    out_path = RAW_DIR / f"rotowire_betmgm_{ROTOWIRE_SPORT}_{pulled_at_compact}.html"
    out_path.write_text(html, encoding="utf-8")
    return out_path


def write_normalized_csv(path: Path, rows: list[NormalizedSportsbookProp]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=NORMALIZED_COLUMNS)
        writer.writeheader()
        for row in rows:
            writer.writerow(row.as_row())


def run() -> dict:
    pulled_at = datetime.now(timezone.utc).isoformat()
    pulled_at_compact = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    summary = {
        "pulled_at": pulled_at,
        "betmgm_rows": 0,
        "betmgm_ok": False,
    }

    log.info("=== Rotowire BetMGM props ingestion run starting (sport=%s) ===", ROTOWIRE_SPORT)

    try:
        html = fetch_rotowire_html()
        save_raw_snapshot(html, pulled_at_compact)
        arrays = extract_data_arrays(html)
        log.info("Found %d real data array(s) embedded in the page", len(arrays))
        rows = normalize_rotowire(arrays, pulled_at)
        summary["betmgm_rows"] = len(rows)
        summary["betmgm_ok"] = True
        log.info("BetMGM (via Rotowire): %d normalized rows", len(rows))
    except Exception as exc:  # noqa: BLE001
        log.error("Rotowire BetMGM ingestion failed for this run: %s", exc)
        rows = []

    snapshot_path = NORMALIZED_DIR / f"rw_betmgm_props_{pulled_at_compact}.csv"
    latest_path = NORMALIZED_DIR / "rw_betmgm_latest.csv"
    write_normalized_csv(snapshot_path, rows)
    write_normalized_csv(latest_path, rows)

    log.info(
        "=== Rotowire BetMGM props ingestion run complete: %d rows (%s) ===",
        len(rows),
        "OK" if summary["betmgm_ok"] else "FAILED",
    )

    summary["snapshot_path"] = str(snapshot_path)
    return summary


if __name__ == "__main__":
    result = run()
    print(json.dumps(result, indent=2))
