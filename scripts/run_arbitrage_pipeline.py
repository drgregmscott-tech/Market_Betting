"""
Session 3.4 -- Automation Adaptation (Arbitrage Track Orchestrator)

WHAT THIS SCRIPT IS
--------------------
Runs Track 1 (arbitrage)'s four existing stages back-to-back, in the
correct order, in one process: Kalshi ingestion (Session 3.1) ->
Polymarket ingestion (Session 3.1) -> venue matching (Session 3.1) ->
arbitrage detection (Session 3.2, fee-aware, liquidity- and legal-
footprint-enriched per Session 3.3's sizing work). This is the single
entry point GitHub Actions (.github/workflows/arbitrage_pipeline.yml,
this same session) calls on a schedule. It is the arbitrage-track twin
of scripts/run_pipeline.py (Session 2.7, pick'em track) and copies that
script's structure deliberately -- same importlib-by-path module
loading, same "never write a corrupted/partial result silently" stance,
same digest-file pattern -- rather than inventing a new orchestration
style for this second track.

This script does NOT call sizing_engine.py's `arbitrage size` command.
Same reasoning as run_pipeline.py's pick'em equivalent: sizing needs a
human-supplied bankroll figure for each of the two real venues (Session
3.3) and a decision about which specific flagged pair is worth acting
on -- there is nothing for an unattended job to decide there. This
project's standing "flags and sizes, never places bets" rule
(ROADMAP.md) means the automation's job ends at producing a clear,
reviewable list of flagged arbitrage opportunities; a human still runs
`sizing_engine.py arbitrage size` by hand against whichever flag_id they
choose.

WHY THIS STOPS EARLY IF EITHER VENUE'S INGESTION RETURNS ZERO ROWS
------------------------------------------------------------------
detector.py treats "this market did not appear in the latest
normalized snapshot" the same way clv_logger.py treats a pick'em prop
disappearing: as the real world (the market closed), not as "the
ingestion step that was supposed to fetch it failed." If either
Kalshi's or Polymarket's ingestion came back with zero rows because of
a network problem or a platform outage, running venue_matcher.py and
detector.py on top of that would silently produce a candidate/flag list
built from one venue's real data and the other venue's empty data --
which could either wrongly suppress the single-venue YES+NO detection
for that venue (Shape 1 in detector.py) or wrongly report zero
cross-venue candidates as if the two venues had genuinely diverged
(Shape 2), rather than reporting the real cause (an ingestion failure).
So: if EITHER venue's ingestion returns zero rows, this script stops
immediately, before calling venue_matcher.py or detector.py, and
reports exactly why. Nothing gets written to data/exchange/matched/ or
data/arbitrage/flags/ on a run where an upstream stage failed.

FILES TOUCHED
-------------
Reads/writes the same files the four underlying scripts already use
(data/exchange/raw, data/exchange/normalized, data/exchange/matched,
data/arbitrage/flags). Additionally writes:
- output/digest/arbitrage_digest_latest.md -- always overwritten, the
  current snapshot. Kept as a SEPARATE file from run_pipeline.py's
  output/digest/digest_latest.md (pick'em track) so the two tracks'
  digests never overwrite each other now that both are automated.
- output/digest/arbitrage_digest_<timestamp>.md -- one dated copy per
  run.
- logs/arbitrage_pipeline.log -- orchestrator-level log, separate from
  each stage's own log file (ingestion.log, arbitrage.log), so a
  pipeline-level failure is findable without digging through both.

USAGE
-----
python scripts/run_arbitrage_pipeline.py
Exit code 0 = pipeline completed; a new arbitrage_flags_*.csv exists
              (even if it has zero rows -- an empty, real result is not
              a failure).
Exit code 1 = pipeline stopped early; no new candidate-match or flags
              file was written this run.
"""

from __future__ import annotations

import argparse
import importlib.util
import logging
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from types import ModuleType

import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
INGEST_KALSHI_SCRIPT = BASE_DIR / "scripts" / "ingestion" / "ingest_kalshi.py"
INGEST_POLYMARKET_SCRIPT = BASE_DIR / "scripts" / "ingestion" / "ingest_polymarket.py"
VENUE_MATCHER_SCRIPT = BASE_DIR / "scripts" / "ingestion" / "venue_matcher.py"
DETECTOR_SCRIPT = BASE_DIR / "scripts" / "arbitrage" / "detector.py"
DIGEST_DIR = BASE_DIR / "output" / "digest"
LOG_PATH = BASE_DIR / "logs" / "arbitrage_pipeline.log"


def setup_logging() -> logging.Logger:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("run_arbitrage_pipeline")
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


def load_module(path: Path, name: str) -> ModuleType:
    """Loads one of the existing arbitrage-track scripts as a Python
    module by file path, so this orchestrator can call its run()
    function directly and get real Python exceptions back -- no
    stdout-parsing, no subprocess exit-code guessing. Identical
    reasoning and mechanism to run_pipeline.py's own load_module(),
    duplicated here (not imported from there) so the two orchestrators
    stay fully independent -- a future change to one track's loading
    behavior should never silently affect the other.

    Each script (e.g. ingest_kalshi.py) does a plain `from
    schema_exchange import ...`-style import of a helper file sitting
    in its own folder, and detector.py does a plain `from
    liquidity_check import ...` of a sibling file in ITS folder. When a
    script is run directly, Python automatically adds that script's own
    folder to its module search list (sys.path). Loading a script this
    other way (importlib, by file path) does not do that automatically
    -- so without the two lines below, those plain imports fail with
    "No module named ...", even though the file is sitting right there.
    Fix: temporarily add the script's own folder to sys.path for the
    moment it's loaded, then remove it again right after, so the four
    scripts' folders are never mixed together."""
    script_dir = str(path.parent)
    sys.path.insert(0, script_dir)
    try:
        spec = importlib.util.spec_from_file_location(name, path)
        if spec is None or spec.loader is None:
            raise ImportError(f"Could not load {path} as a module.")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    finally:
        sys.path.remove(script_dir)


class PipelineStageFailed(Exception):
    """Raised when a stage completes without a Python exception but its
    output is empty/unusable in a way that must not be allowed to flow
    into venue_matcher.py or detector.py. Kept distinct from a real
    exception so the digest can report a clear, specific reason instead
    of a traceback. Identical role to run_pipeline.py's own
    PipelineStageFailed."""


def run_kalshi_ingestion() -> dict:
    log.info("--- Stage 1/4: Kalshi ingestion ---")
    module = load_module(INGEST_KALSHI_SCRIPT, "ingest_kalshi")
    summary = module.run()
    log.info("Kalshi ingestion summary: %s", summary)

    if not summary.get("kalshi_ok") or not summary.get("kalshi_rows_kept"):
        raise PipelineStageFailed(
            "Kalshi ingestion returned 0 usable rows "
            f"(kalshi_ok={summary.get('kalshi_ok')}, "
            f"kalshi_rows_kept={summary.get('kalshi_rows_kept')}). Stopping "
            "before venue matching/detection so a transient Kalshi outage "
            "can never be mistaken for every Kalshi market closing."
        )
    return summary


def run_polymarket_ingestion() -> dict:
    log.info("--- Stage 2/4: Polymarket ingestion ---")
    module = load_module(INGEST_POLYMARKET_SCRIPT, "ingest_polymarket")
    summary = module.run()
    log.info("Polymarket ingestion summary: %s", summary)

    if not summary.get("polymarket_ok") or not summary.get("total_rows"):
        raise PipelineStageFailed(
            "Polymarket ingestion returned 0 usable rows "
            f"(polymarket_ok={summary.get('polymarket_ok')}, "
            f"total_rows={summary.get('total_rows')}). Stopping before "
            "venue matching/detection so a transient Polymarket outage "
            "can never be mistaken for every Polymarket market closing."
        )
    return summary


def run_venue_matcher() -> dict:
    log.info("--- Stage 3/4: venue matching ---")
    module = load_module(VENUE_MATCHER_SCRIPT, "venue_matcher")
    summary = module.run()
    log.info("Venue matcher summary: %s", summary)
    # Deliberately NOT treated as a PipelineStageFailed if this comes
    # back with 0 candidate pairs -- unlike the two ingestion stages
    # above, "0 matches this run" is a real, valid outcome (the two
    # venues' currently-open markets simply may not overlap on a given
    # run), not evidence of a broken stage. detector.py's own run()
    # already handles a missing/empty candidate-matches file by logging
    # a warning and skipping cross-venue detection for that run, rather
    # than failing outright -- see detector.py's run().
    return summary


def run_detector() -> tuple[dict, Path]:
    log.info("--- Stage 4/4: arbitrage detection ---")
    module = load_module(DETECTOR_SCRIPT, "detector")
    summary = module.run()
    log.info("Detector summary: %s", summary)

    out_path = Path(summary["output_path"]) if "output_path" in summary else None
    if out_path is None or not out_path.exists():
        raise PipelineStageFailed(
            f"Detector did not produce a readable output file (summary={summary})."
        )
    return summary, out_path


def build_digest(
    run_started_at: str,
    kalshi_summary: dict,
    polymarket_summary: dict,
    matcher_summary: dict,
    detector_summary: dict,
    flags_path: Path,
) -> Path:
    """Writes a plain-language summary of this run plus a table of every
    flag this run's detector.py pass produced, read straight from the
    just-written arbitrage_flags_<timestamp>.csv. This is the file a
    person actually looks at to decide whether any flagged pair is
    worth manually running through `sizing_engine.py arbitrage size` --
    the automation's output ends here, same "human decides what to do
    with a clean, reviewable list" boundary as run_pipeline.py's own
    digest."""
    DIGEST_DIR.mkdir(parents=True, exist_ok=True)
    timestamp_compact = run_started_at.replace(":", "").replace("-", "")

    lines: list[str] = []
    lines.append(f"# Arbitrage Pipeline Digest -- {run_started_at}")
    lines.append("")
    lines.append("## Run summary")
    lines.append(
        f"- Kalshi ingestion: {kalshi_summary.get('kalshi_rows_kept', 0)} rows kept "
        f"({kalshi_summary.get('kalshi_target_series_count', 0)} target series, "
        f"{kalshi_summary.get('kalshi_down_ballot_series_count', 0)} down-ballot)"
    )
    lines.append(
        f"- Polymarket ingestion: {polymarket_summary.get('total_rows', 0)} rows"
    )
    lines.append(
        f"- Venue matching: {matcher_summary.get('candidate_matches_found', 0)} "
        f"candidate pairs ({matcher_summary.get('candidate_matches_elections_wide', 0)} "
        "elections-wide)"
    )
    lines.append(
        f"- Detection: {detector_summary.get('total_flags', 0)} flags "
        f"({detector_summary.get('single_venue_flags', 0)} single-venue, "
        f"{detector_summary.get('cross_venue_flags', 0)} cross-venue) from "
        f"{detector_summary.get('candidate_pairs_checked', 0)} candidate pairs checked"
    )
    lines.append("")

    lines.append("## This run's flagged opportunities")
    lines.append(
        "Sizing is a manual step (`sizing_engine.py arbitrage size`, Session "
        "3.3) -- this table is what to scan to pick a pair worth sizing."
    )
    lines.append("")

    if flags_path.exists():
        flags_df = pd.read_csv(flags_path)
        if len(flags_df) == 0:
            lines.append("_No opportunities flagged this run._")
        else:
            cols = [
                "opportunity_type", "platform_a", "title_a", "leg_a_ask",
                "platform_b", "title_b", "leg_b_ask", "net_profit_per_dollar",
                "liquidity_sufficient", "legal_footprint_status",
            ]
            display_df = flags_df[cols].sort_values(
                "net_profit_per_dollar", ascending=False
            )
            lines.append("| " + " | ".join(cols) + " |")
            lines.append("|" + "---|" * len(cols))
            for _, row in display_df.iterrows():
                lines.append("| " + " | ".join(str(row[c]) for c in cols) + " |")
    else:
        lines.append("_Flags file does not exist this run._")

    digest_text = "\n".join(lines) + "\n"

    latest_path = DIGEST_DIR / "arbitrage_digest_latest.md"
    dated_path = DIGEST_DIR / f"arbitrage_digest_{timestamp_compact}.md"
    latest_path.write_text(digest_text, encoding="utf-8")
    dated_path.write_text(digest_text, encoding="utf-8")
    log.info("Wrote digest to %s and %s", latest_path, dated_path)
    return latest_path


def build_failure_digest(run_started_at: str, reason: str) -> Path:
    """A stopped run still gets a digest -- so a failure is visible by
    opening a file, not just by reading Actions logs. Same reasoning as
    run_pipeline.py's build_failure_digest()."""
    DIGEST_DIR.mkdir(parents=True, exist_ok=True)
    timestamp_compact = run_started_at.replace(":", "").replace("-", "")
    text = (
        f"# Arbitrage Pipeline Digest -- {run_started_at}\n\n"
        f"## RUN FAILED\n\n"
        f"{reason}\n\n"
        f"No new candidate-match or flags file was written this run.\n"
    )
    latest_path = DIGEST_DIR / "arbitrage_digest_latest.md"
    dated_path = DIGEST_DIR / f"arbitrage_digest_{timestamp_compact}_FAILED.md"
    latest_path.write_text(text, encoding="utf-8")
    dated_path.write_text(text, encoding="utf-8")
    return latest_path


def main() -> int:
    run_started_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    log.info("=== Arbitrage pipeline run starting at %s ===", run_started_at)

    try:
        kalshi_summary = run_kalshi_ingestion()
        polymarket_summary = run_polymarket_ingestion()
        matcher_summary = run_venue_matcher()
        detector_summary, flags_path = run_detector()
    except PipelineStageFailed as exc:
        log.error("Pipeline stopped: %s", exc)
        build_failure_digest(run_started_at, str(exc))
        return 1
    except Exception as exc:  # noqa: BLE001 -- deliberately broad: any
        # unexpected exception from any stage must still stop the run
        # and be logged, not crash the orchestrator with a bare
        # traceback that skips the failure digest.
        log.exception("Pipeline stopped on an unexpected error: %s", exc)
        build_failure_digest(run_started_at, f"Unexpected error: {exc}")
        return 1

    build_digest(
        run_started_at,
        kalshi_summary,
        polymarket_summary,
        matcher_summary,
        detector_summary,
        flags_path,
    )
    log.info("=== Arbitrage pipeline run complete ===")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.parse_args()  # no arguments today; kept for symmetry with
    # run_pipeline.py and so a future flag (e.g. --track) has a place
    # to go without changing the calling convention in the workflow file.
    sys.exit(main())
