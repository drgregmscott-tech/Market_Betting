"""
Session 2.7 -- Automation Orchestrator

WHAT THIS SCRIPT IS
--------------------
Runs Track 1's three existing pipeline stages back-to-back, in the correct
order, in one process: ingestion (Session 2.2) -> estimation (Session 2.3)
-> CLV logging (Session 2.4). This is the single entry point GitHub Actions
(scripts/../.github/workflows/pickem_pipeline.yml, this same session) calls
on a schedule. It replaces run_full_pipeline.bat for the automated path;
run_full_pipeline.bat is untouched and still works for a manual local run.

This script does NOT call sizing_engine.py (Session 2.6). That script
requires a human to name two specific flag_ids and a real bankroll dollar
figure -- there is nothing for an unattended job to decide there. Automating
"ingest, estimate, log" and leaving "which pair do I size" to the person
matches this project's standing "flags and sizes, never places bets" rule
(ROADMAP.md) -- the automation's job ends at producing a clear, reviewable
list of open flags; a human still decides what to do with them.

WHY THIS STOPS EARLY ON EMPTY DATA, RATHER THAN "RUNNING ANYWAY"
------------------------------------------------------------------
clv_logger.py (Session 2.4) treats "this flag_id did not appear in the
latest ingestion run" as "the line closed" and freezes closing values for
it. That is the correct behavior when a game genuinely locks. It is the
WRONG behavior if ingestion returned zero rows because of a network problem,
a platform outage, or any other transient failure -- in that case every
currently open flag would be wrongly marked closed with meaningless closing
values, corrupting the CLV log's real history. So: if ingestion or
estimation comes back with zero usable rows, this script stops immediately,
BEFORE calling clv_logger.py, and reports exactly why. Nothing gets written
to clv_log.csv on a stage that failed -- a half-broken run must never look
like a normal one.

FILES TOUCHED
-------------
Reads/writes the same files the three underlying scripts already use
(data/pickem/raw, data/pickem/normalized, output/estimation,
data/pickem/clv_log.csv, data/pickem/clv_snapshots/). Additionally writes:
- output/digest/digest_latest.md -- always overwritten, the current snapshot
- output/digest/digest_<timestamp>.md -- one dated copy per run
- logs/pipeline.log -- orchestrator-level log, separate from each stage's
  own log file (ingestion.log, estimation.log, clv_logging.log), so a
  pipeline-level failure is findable without digging through three logs.

USAGE
-----
python scripts/run_pipeline.py
python scripts/run_pipeline.py --season 2025   # season is passed through to
                                                 # pickem_model.py; defaults
                                                 # to 2025, matching every
                                                 # prior session's usage
Exit code 0 = pipeline completed and clv_log.csv was updated.
Exit code 1 = pipeline stopped early; clv_log.csv was NOT touched this run.
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
INGEST_SCRIPT = BASE_DIR / "scripts" / "ingestion" / "ingest_pickem.py"
MODEL_SCRIPT = BASE_DIR / "scripts" / "estimation" / "pickem_model.py"
SEASON_UTILS_SCRIPT = BASE_DIR / "scripts" / "estimation" / "season_utils.py"
CLV_SCRIPT = BASE_DIR / "scripts" / "calibration" / "clv_logger.py"
CLV_LOG_PATH = BASE_DIR / "data" / "pickem" / "clv_log.csv"
DIGEST_DIR = BASE_DIR / "output" / "digest"
LOG_PATH = BASE_DIR / "logs" / "pipeline.log"


def setup_logging() -> logging.Logger:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("run_pipeline")
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
    """Loads one of the existing pipeline scripts as a Python module by
    file path, so this orchestrator can call its run() function directly
    and get real Python exceptions back -- no stdout-parsing, no
    subprocess exit-code guessing. Each script's own __main__ block never
    runs, since it's only triggered when a script is executed directly,
    not when it's imported like this.

    Each script (e.g. ingest_pickem.py) does a plain `from schema import
    ...`-style import of a helper file sitting in its own folder. When a
    script is run directly (`python ingest_pickem.py`), Python
    automatically adds that script's own folder to its module search
    list (sys.path), so the plain import just works. Loading a script
    this other way (importlib, by file path) does NOT do that step
    automatically -- so without the two lines below, that plain import
    fails with "No module named 'schema'", even though the file is
    sitting right there. Fix: temporarily add the script's own folder to
    sys.path for the moment it's loaded, then remove it again right
    after, so the three scripts' folders are never mixed together."""
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
    into clv_logger.py. Kept distinct from a real exception so the
    digest can report a clear, specific reason instead of a traceback."""


def run_ingestion() -> dict:
    log.info("--- Stage 1/3: ingestion ---")
    ingest_module = load_module(INGEST_SCRIPT, "ingest_pickem")
    summary = ingest_module.run()
    log.info("Ingestion summary: %s", summary)

    if summary.get("total_rows", 0) == 0:
        raise PipelineStageFailed(
            "Ingestion returned 0 total rows across both platforms "
            f"(prizepicks_ok={summary.get('prizepicks_ok')}, "
            f"underdog_ok={summary.get('underdog_ok')}). Stopping before "
            "estimation/CLV logging so a transient outage can never be "
            "mistaken for every prop closing."
        )
    return summary


def run_estimation(season: int) -> tuple[dict, Path]:
    log.info("--- Stage 2/3: estimation (season=%d) ---", season)
    model_module = load_module(MODEL_SCRIPT, "pickem_model")
    summary = model_module.run(season)
    log.info("Estimation summary: %s", summary)

    out_path = Path(summary["output_path"]) if "output_path" in summary else None
    if out_path is None or not out_path.exists():
        raise PipelineStageFailed(
            "Estimation did not produce a readable output file "
            f"(summary={summary}). Stopping before CLV logging."
        )

    if not summary.get("rows_out"):
        raise PipelineStageFailed(
            f"Estimation produced 0 output rows (summary={summary}). "
            "Stopping before CLV logging."
        )
    return summary, out_path


def run_clv_logging(estimates_path: Path) -> dict:
    log.info("--- Stage 3/3: CLV logging ---")
    clv_module = load_module(CLV_SCRIPT, "clv_logger")
    # Session 5.2 (2026-09-08) renamed clv_logger.py's flat run() to
    # run_pickem() when generalizing the module for weather/politics/props
    # (each track now gets its own run_<track>() entry point). This call
    # site was never updated to match, which broke the automated pick'em
    # GitHub Actions pipeline silently -- every scheduled run after the
    # rename crashed here with AttributeError, and none of them could
    # commit a fresh clv_log.csv as a result (see SESSION_LOG.md for the
    # full incident writeup).
    summary = clv_module.run_pickem(estimates_path)
    log.info("CLV logging summary: %s", summary)
    return summary


def build_digest(
    run_started_at: str,
    ingestion_summary: dict,
    estimation_summary: dict,
    clv_summary: dict,
) -> Path:
    """Writes a plain-language summary of this run plus a table of every
    currently OPEN flag, read straight from the just-updated clv_log.csv.
    This is the file a person actually looks at to decide which flag
    pairs, if any, are worth manually running through sizing_engine.py --
    the automation's output ends here; sizing stays a human decision."""
    DIGEST_DIR.mkdir(parents=True, exist_ok=True)
    timestamp_compact = run_started_at.replace(":", "").replace("-", "")

    lines: list[str] = []
    lines.append(f"# Pipeline Digest -- {run_started_at}")
    lines.append("")
    lines.append("## Run summary")
    lines.append(
        f"- Ingestion: {ingestion_summary.get('total_rows', 0)} rows "
        f"(PrizePicks {'OK' if ingestion_summary.get('prizepicks_ok') else 'FAILED'}, "
        f"Underdog {'OK' if ingestion_summary.get('underdog_ok') else 'FAILED'})"
    )
    lines.append(
        f"- Estimation: {estimation_summary.get('rows_out', 0)} rows estimated "
        f"(from {estimation_summary.get('rows_in', 0)} ingested props)"
    )
    lines.append(
        f"- CLV logging: {clv_summary.get('newly_flagged', 0)} newly flagged, "
        f"{clv_summary.get('newly_closed', 0)} newly closed, "
        f"{clv_summary.get('still_open', 0)} still open "
        f"({clv_summary.get('total_logged', 0)} total ever logged)"
    )
    lines.append("")

    lines.append("## Currently open flags")
    lines.append(
        "Sizing is a manual step (sizing_engine.py, Session 2.6) -- this "
        "table is what to scan to pick a pair worth sizing."
    )
    lines.append("")

    if CLV_LOG_PATH.exists():
        clv_df = pd.read_csv(CLV_LOG_PATH)
        open_df = clv_df.loc[clv_df["status"] == "open"].copy()
        if len(open_df) == 0:
            lines.append("_No open flags right now._")
        else:
            cols = [
                "flag_id", "platform", "player_name", "stat_type",
                "flagged_side", "first_flagged_edge", "first_flagged_at",
                "game_start_time",
            ]
            open_df = open_df[cols].sort_values("first_flagged_edge", ascending=False)
            lines.append("| " + " | ".join(cols) + " |")
            lines.append("|" + "---|" * len(cols))
            for _, row in open_df.iterrows():
                lines.append("| " + " | ".join(str(row[c]) for c in cols) + " |")
    else:
        lines.append("_clv_log.csv does not exist yet._")

    digest_text = "\n".join(lines) + "\n"

    latest_path = DIGEST_DIR / "digest_latest.md"
    dated_path = DIGEST_DIR / f"digest_{timestamp_compact}.md"
    latest_path.write_text(digest_text, encoding="utf-8")
    dated_path.write_text(digest_text, encoding="utf-8")
    log.info("Wrote digest to %s and %s", latest_path, dated_path)
    return latest_path


def build_failure_digest(run_started_at: str, reason: str) -> Path:
    """A stopped run still gets a digest -- so a failure is visible by
    opening a file, not just by reading Actions logs (see ROADMAP.md
    validation requirement: 'pipeline fails loudly and logs why')."""
    DIGEST_DIR.mkdir(parents=True, exist_ok=True)
    timestamp_compact = run_started_at.replace(":", "").replace("-", "")
    text = (
        f"# Pipeline Digest -- {run_started_at}\n\n"
        f"## RUN FAILED\n\n"
        f"{reason}\n\n"
        f"clv_log.csv was NOT modified this run.\n"
    )
    latest_path = DIGEST_DIR / "digest_latest.md"
    dated_path = DIGEST_DIR / f"digest_{timestamp_compact}_FAILED.md"
    latest_path.write_text(text, encoding="utf-8")
    dated_path.write_text(text, encoding="utf-8")
    return latest_path


def main(season: int) -> int:
    run_started_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    log.info("=== Pipeline run starting at %s (season=%d) ===", run_started_at, season)

    try:
        ingestion_summary = run_ingestion()
        estimation_summary, estimates_path = run_estimation(season)
        clv_summary = run_clv_logging(estimates_path)
    except PipelineStageFailed as exc:
        log.error("Pipeline stopped: %s", exc)
        build_failure_digest(run_started_at, str(exc))
        return 1
    except Exception as exc:  # noqa: BLE001 -- deliberately broad: any
        # unexpected exception from any stage must still stop the run and
        # be logged, not crash the orchestrator with a bare traceback that
        # skips the failure digest.
        log.exception("Pipeline stopped on an unexpected error: %s", exc)
        build_failure_digest(run_started_at, f"Unexpected error: {exc}")
        return 1

    build_digest(run_started_at, ingestion_summary, estimation_summary, clv_summary)
    log.info("=== Pipeline run complete ===")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--season",
        type=int,
        default=None,
        help="Passed through to pickem_model.py. Defaults to the real "
        "current season (see scripts/estimation/season_utils.py) rather "
        "than a hardcoded year, so this never silently goes stale -- see "
        "ROADMAP.md Open Decision #9 for the separate, still-open question "
        "of when a brand-new season has enough real data to trust.",
    )
    args = parser.parse_args()
    season = args.season
    if season is None:
        season_utils = load_module(SEASON_UTILS_SCRIPT, "season_utils")
        season = season_utils.current_pickem_season()
    sys.exit(main(season))
