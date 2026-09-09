"""
Session 6.5 -- Automation Adaptation (Sportsbook Props Track Orchestrator)

WHAT THIS SCRIPT IS
--------------------
Runs Track 6 (sportsbook player props)'s three existing stages back-to-back,
in the correct order, in one process: DraftKings + FanDuel props ingestion
(Session 6.1) -> estimation (Session 6.2/6.4, field-vig-normalized model) ->
CLV logging (Session 6.3, shared clv_logger.py --track props). This is the
single entry point .github/workflows/props_pipeline.yml (this same session)
calls on a schedule. It is this track's twin of scripts/run_pipeline.py
(Session 2.7, pick'em), scripts/run_arbitrage_pipeline.py (Session 3.4), and
scripts/run_politics_pipeline.py (Session 5.5) -- same importlib-by-path
module loading, same "never let a stage's failure silently flow into the
next stage" stance, same digest-file pattern.

WHY BOTH INGESTION STAGES ARE ALLOWED TO INDIVIDUALLY FAIL, UNLIKE
POLITICS' TWO INGESTION STAGES (WHICH BOTH MUST SUCCEED)
------------------------------------------------------------------
ingest_dk_props.run() and ingest_fd_props.run() each already catch their
own real exceptions internally and return a summary with an `_ok` flag and
a row count of 0 on failure -- they never raise. Session 6.1's real finding
was that DraftKings sits behind Akamai Bot Manager and requires a real,
visible (non-headless) Chromium browser (see ingest_dk_props.py's own
docstring) -- a single venue's bot-detection layer tightening on a given
run is a real, expected possibility this track must tolerate without
treating it as a whole-pipeline failure, the same way a single sportsbook
going down does not mean every prop in the world stopped existing. So this
orchestrator proceeds to estimation as long as AT LEAST ONE of the two
feeds returned real rows -- it only stops early if BOTH return 0 rows,
since sportsbook_props_model.py's load_props() itself already raises if
neither dk_latest.csv nor fd_latest.csv can be found/used, and running
estimation against a stale or partial single-venue file forward is exactly
the FanDuel-only degraded mode Session 6.1 already validated works
correctly.

WHY THIS STOPS EARLY IF ESTIMATION PRODUCES 0 ROWS
----------------------------------------------------
Same reasoning as every other orchestrator in this project: clv_logger.py's
generic_process_run() treats "this flag_id did not appear in the latest
estimates file" as "the market closed" and freezes closing values for it --
correct when a prop genuinely resolves or a venue genuinely pulls a market,
wrong if a transient upstream problem made estimation come back empty. A
half-broken run must never look like a normal one and silently mark every
currently-open props flag "closed" with meaningless closing values.

FILES TOUCHED
-------------
Reads/writes the same files the three underlying scripts already use
(data/sportsbook_props/raw, data/sportsbook_props/normalized,
output/estimation/sportsbook_props_latest.csv,
data/sportsbook_props/clv_log.csv). Additionally writes:
- output/digest/props_digest_latest.md -- always overwritten, the current
  snapshot. Kept as a SEPARATE file from every other track's digest so no
  two tracks' automated digests ever overwrite each other.
- output/digest/props_digest_<timestamp>.md -- one dated copy per run.
- logs/props_pipeline.log -- orchestrator-level log, separate from each
  stage's own log file (ingestion.log, estimation.log, clv_logging.log).

WHY THIS SCRIPT DOES NOT CALL sizing_engine.py's `props size` COMMAND
------------------------------------------------------------------------
Same reasoning as every other track's orchestrator: sizing needs a
human-supplied bankroll figure and a decision about which specific flagged
prop is worth acting on -- there is nothing for an unattended job to decide
there. This project's standing "flags and sizes, never places bets" rule
(ROADMAP.md) means the automation's job ends at producing a clear,
reviewable list of open flags; a human still runs
`sizing_engine.py props size` by hand against whichever flag_id they
choose.

USAGE
-----
python scripts/run_props_pipeline.py --season 2025
Exit code 0 = pipeline completed; clv_log.csv was updated (even if 0 flags
              are currently open -- a real empty result is not a failure).
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
INGEST_DK_SCRIPT = BASE_DIR / "scripts" / "ingestion" / "ingest_dk_props.py"
INGEST_FD_SCRIPT = BASE_DIR / "scripts" / "ingestion" / "ingest_fd_props.py"
MODEL_SCRIPT = BASE_DIR / "scripts" / "estimation" / "sportsbook_props_model.py"
CLV_SCRIPT = BASE_DIR / "scripts" / "calibration" / "clv_logger.py"
CLV_LOG_PATH = BASE_DIR / "data" / "sportsbook_props" / "clv_log.csv"
DIGEST_DIR = BASE_DIR / "output" / "digest"
LOG_PATH = BASE_DIR / "logs" / "props_pipeline.log"


def setup_logging() -> logging.Logger:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("run_props_pipeline")
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
    """Loads one of the existing props-track scripts as a Python module by
    file path, so this orchestrator can call its run() function directly
    and get real Python exceptions back -- no stdout-parsing, no subprocess
    exit-code guessing. Identical reasoning and mechanism to every other
    orchestrator's own load_module(), duplicated here (not imported from
    there) so all orchestrators stay fully independent -- a future change
    to one track's loading behavior should never silently affect another."""
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
    into clv_logger.py. Kept distinct from a real exception so the digest
    can report a clear, specific reason instead of a traceback. Identical
    role to the other orchestrators' own PipelineStageFailed."""


def run_dk_ingestion() -> dict:
    log.info("--- Stage 1a/3: DraftKings props ingestion ---")
    try:
        module = load_module(INGEST_DK_SCRIPT, "ingest_dk_props")
        summary = module.run()
        log.info("DraftKings ingestion summary: %s", summary)
        return summary
    except Exception as exc:  # noqa: BLE001 -- a real unhandled exception
        # here (e.g. Playwright/Chromium itself missing on this runner)
        # must not crash the whole pipeline before FanDuel gets a chance to
        # run -- treated the same as DK's own internal 0-rows failure mode.
        log.error("DraftKings ingestion raised an unexpected error: %s", exc)
        return {"draftkings_rows": 0, "draftkings_ok": False, "events_pulled": 0, "error": str(exc)}


def run_fd_ingestion() -> dict:
    log.info("--- Stage 1b/3: FanDuel props ingestion ---")
    try:
        module = load_module(INGEST_FD_SCRIPT, "ingest_fd_props")
        summary = module.run()
        log.info("FanDuel ingestion summary: %s", summary)
        return summary
    except Exception as exc:  # noqa: BLE001 -- see run_dk_ingestion()
        log.error("FanDuel ingestion raised an unexpected error: %s", exc)
        return {"fanduel_rows": 0, "fanduel_ok": False, "error": str(exc)}


def run_estimation(season: int) -> tuple[dict, Path]:
    log.info("--- Stage 2/3: estimation (field-vig-normalized model, season=%d) ---", season)
    module = load_module(MODEL_SCRIPT, "sportsbook_props_model")
    summary = module.run(season)
    log.info("Estimation summary: %s", summary)

    out_path = Path(summary["output_path"]) if "output_path" in summary else None
    if out_path is None or not out_path.exists():
        raise PipelineStageFailed(
            f"Estimation did not produce a readable output file (summary={summary})."
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
    summary = clv_module.run_props(estimates_path)
    log.info("CLV logging summary: %s", summary)
    return summary


def build_digest(
    run_started_at: str,
    dk_summary: dict,
    fd_summary: dict,
    estimation_summary: dict,
    clv_summary: dict,
) -> Path:
    """Writes a plain-language summary of this run plus a table of every
    currently OPEN props flag, read straight from the just-updated
    clv_log.csv. This is the file a person actually looks at to decide
    which specific flag is worth manually running through
    `sizing_engine.py props size` -- the automation's output ends here;
    sizing stays a human decision, per this project's standing rule."""
    DIGEST_DIR.mkdir(parents=True, exist_ok=True)
    timestamp_compact = run_started_at.replace(":", "").replace("-", "")

    lines: list[str] = []
    lines.append(f"# Props Pipeline Digest -- {run_started_at}")
    lines.append("")
    lines.append("## Run summary")
    lines.append(
        f"- DraftKings ingestion: {dk_summary.get('draftkings_rows', 0)} rows "
        f"across {dk_summary.get('events_pulled', 0)} events "
        f"({'OK' if dk_summary.get('draftkings_ok') else 'FAILED -- see logs/ingestion.log'})"
    )
    lines.append(
        f"- FanDuel ingestion: {fd_summary.get('fanduel_rows', 0)} rows "
        f"({'OK' if fd_summary.get('fanduel_ok') else 'FAILED -- see logs/ingestion.log'})"
    )
    lines.append(
        f"- Estimation: {estimation_summary.get('rows_out', 0)} rows written "
        f"(from {estimation_summary.get('rows_in', 0)} ingested rows) -- "
        f"status breakdown: {estimation_summary.get('status_counts', {})}"
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
        "Sizing is a manual step (`sizing_engine.py props size`, Session "
        "6.4) -- this table is what to scan to pick a flag worth sizing. "
        "`implied_prob_includes_field_vig` matters here more than for the "
        "other tracks: a row still reporting True carries a real, "
        "separate uncertainty (Session 6.4's "
        "`PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER` dampener) that a bigger "
        "raw edge number does not describe."
    )
    lines.append("")

    if CLV_LOG_PATH.exists():
        clv_df = pd.read_csv(CLV_LOG_PATH)
        open_df = clv_df.loc[clv_df["status"] == "open"].copy()
        if len(open_df) == 0:
            lines.append("_No open flags right now._")
        else:
            cols = [
                "flag_id", "platform", "player_name", "stat_type", "flagged_side",
                "first_flagged_model_prob", "first_flagged_market_price",
                "first_flagged_edge", "implied_prob_includes_field_vig",
                "first_flagged_at",
            ]
            cols = [c for c in cols if c in open_df.columns]
            open_df = open_df[cols].sort_values("first_flagged_edge", ascending=False)
            lines.append("| " + " | ".join(cols) + " |")
            lines.append("|" + "---|" * len(cols))
            for _, row in open_df.iterrows():
                lines.append("| " + " | ".join(str(row[c]) for c in cols) + " |")
    else:
        lines.append("_clv_log.csv does not exist yet._")

    digest_text = "\n".join(lines) + "\n"

    latest_path = DIGEST_DIR / "props_digest_latest.md"
    dated_path = DIGEST_DIR / f"props_digest_{timestamp_compact}.md"
    latest_path.write_text(digest_text, encoding="utf-8")
    dated_path.write_text(digest_text, encoding="utf-8")
    log.info("Wrote digest to %s and %s", latest_path, dated_path)
    return latest_path


def build_failure_digest(run_started_at: str, reason: str) -> Path:
    """A stopped run still gets a digest -- so a failure is visible by
    opening a file, not just by reading Actions logs. Same reasoning as
    every other orchestrator's own build_failure_digest()."""
    DIGEST_DIR.mkdir(parents=True, exist_ok=True)
    timestamp_compact = run_started_at.replace(":", "").replace("-", "")
    text = (
        f"# Props Pipeline Digest -- {run_started_at}\n\n"
        f"## RUN FAILED\n\n"
        f"{reason}\n\n"
        f"data/sportsbook_props/clv_log.csv was NOT modified this run.\n"
    )
    latest_path = DIGEST_DIR / "props_digest_latest.md"
    dated_path = DIGEST_DIR / f"props_digest_{timestamp_compact}_FAILED.md"
    latest_path.write_text(text, encoding="utf-8")
    dated_path.write_text(text, encoding="utf-8")
    return latest_path


def main(season: int) -> int:
    run_started_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    log.info("=== Props pipeline run starting at %s (season=%d) ===", run_started_at, season)

    dk_summary = run_dk_ingestion()
    fd_summary = run_fd_ingestion()

    dk_rows = dk_summary.get("draftkings_rows", 0)
    fd_rows = fd_summary.get("fanduel_rows", 0)
    if not dk_rows and not fd_rows:
        reason = (
            "Both DraftKings and FanDuel ingestion returned 0 usable rows "
            f"(dk_summary={dk_summary}, fd_summary={fd_summary}). Stopping "
            "before estimation/CLV logging so a total upstream outage (or "
            "this runner's Chromium/display setup breaking) can never be "
            "mistaken for every props market closing."
        )
        log.error("Pipeline stopped: %s", reason)
        build_failure_digest(run_started_at, reason)
        return 1
    if not dk_rows:
        log.warning(
            "DraftKings returned 0 rows this run -- proceeding in "
            "FanDuel-only degraded mode (Session 6.1's already-validated "
            "fallback path)."
        )
    if not fd_rows:
        log.warning(
            "FanDuel returned 0 rows this run -- proceeding in "
            "DraftKings-only degraded mode."
        )

    try:
        estimation_summary, estimates_path = run_estimation(season)
        clv_summary = run_clv_logging(estimates_path)
    except PipelineStageFailed as exc:
        log.error("Pipeline stopped: %s", exc)
        build_failure_digest(run_started_at, str(exc))
        return 1
    except Exception as exc:  # noqa: BLE001 -- deliberately broad: any
        # unexpected exception from either remaining stage must still stop
        # the run and be logged, not crash the orchestrator with a bare
        # traceback that skips the failure digest.
        log.exception("Pipeline stopped on an unexpected error: %s", exc)
        build_failure_digest(run_started_at, f"Unexpected error: {exc}")
        return 1

    build_digest(run_started_at, dk_summary, fd_summary, estimation_summary, clv_summary)
    log.info("=== Props pipeline run complete ===")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--season",
        type=int,
        default=2025,
        help="Passed through to sportsbook_props_model.py. Defaults to "
        "2025, matching run_pipeline.py's own placeholder default -- see "
        "ROADMAP.md Open Decision #9 for when this should switch to 2026.",
    )
    args = parser.parse_args()
    sys.exit(main(args.season))
