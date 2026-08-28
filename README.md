# Market_Betting

A +EV (positive expected value) prediction-market analysis system. It looks
for betting/market opportunities that are more likely to be right than a bet
made emotionally or without rigorous research — across sports, weather/
climate, and narrow down-ballot political markets, plus fixed-line pick'em
platforms and cross-venue arbitrage.

This is a sibling project to `DFS_Optimizer`, `DFS_Optimizer_NHL`, and
`DFS_Optimizer_PGA`. It reuses their proven architectural pattern (data
ingestion → estimation/projection engine → sizing → automation → frontend)
but is built with new code throughout, since continuously repricing markets
are a different problem shape than a fixed weekly DFS slate.

## Where to start

- **`ROADMAP.md`** — full project scope, the ranked track-confidence table,
  validation methodology, and the phase/session build plan.
- **`SESSION_LOG.md`** — a complete record of what was built, validated, and
  decided in every session. Read this before starting any new session.
- **`docs/research/`** — the sourced research artifact behind the project's
  scope decisions.

## Status

Phase 0 (viability and scope) is complete. Phase 1 (foundation and repo
setup) is in progress. See `SESSION_LOG.md` for the current session.

## Repo structure

```
/data          <- raw + processed market/event data (gitignored contents)
/scripts       <- all pipeline scripts (per-track subfolders likely, TBD)
/output        <- flagged opportunities, sizing suggestions, digest content
/logs          <- session log + automation run logs
/docs
  /research    <- sourced research artifacts
/config        <- api_keys.env (gitignored — copy from api_keys.env.example), venue configs
```

## Setup

```
pip install -r requirements.txt
```

Copy `config/api_keys.env.example` to `config/api_keys.env` and fill in real
credentials once venue access is confirmed (see ROADMAP.md Open Decisions).
