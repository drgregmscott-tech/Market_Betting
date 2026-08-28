# +EV Market Analysis System — Build Roadmap

## Background & Approach

This project is a sibling to the **NFL DFS Optimizer** (`DFS_Optimizer`), **NHL DFS
Optimizer** (`DFS_Optimizer_NHL`), and **PGA DFS Optimizer** (`DFS_Optimizer_PGA`)
repos. The session methodology, validation discipline, and general engineering
approach carry over directly. What does NOT carry over is the codebase itself —
this project forks the *architectural pattern* proven across those three repos
(data ingestion → estimation/projection engine → optimizer/sizing → automation →
frontend), built clean, in a new repo. Confirmed explicitly with the user: this is
not a copy-and-adapt job the way PGA was built from the NFL/NHL pattern — the
domain is different enough (continuously repricing markets vs. a fixed weekly
slate) to warrant new code throughout, guided by the same proven pattern rather
than reusing it directly.

**Goal, stated precisely:** identify betting/market opportunities that are more
likely to be right than a bet made emotionally or without rigorous research —
understanding that no single bet is ever certain. "+EV" means genuinely better
odds of being right over many trials, not a guarantee on any individual outcome.

**The S&P 500 analogy (user's framing, adopted as the project's north star):**
a 10-year chart of the S&P 500 has real highs and real lows along the way — some
stretches lose money for months at a time — but the overall trendline moves up.
That is the exact shape of result this project is built to produce. Individual
bets will lose. Individual weeks or months, even entire slow stretches for a
given track, may show a flat or negative trendline. That is expected and normal,
not a sign of failure by itself. What the system must demonstrate, per track,
is the equivalent of that S&P 500 chart: real drawdowns, but a real positive
trendline over a large enough sample to mean something (see Phase 3's
sample-size thresholds). A track that cannot show that trendline, honestly,
over a real sample is not a working track — no matter how good any single
week looked.

**This distinction matters enough to state as a standing rule, not just a
definition:** "no guarantees" describes the nature of probability. It is not,
and must never become, a justification for a weaker system — skipping
validation, shipping an under-researched estimation model, or accepting a lower
bar because "nothing's certain anyway." Any future session that finds itself
using that language to excuse a shortcut should treat that as a signal
something is being rationalized, not explained. The standard this project holds
itself to is: **demonstrate, with real graded evidence (Phase 3 and onward),
that a given track performs meaningfully better than chance or unresearched
guessing before it is trusted with real capital or scaled up.**

**Scope decision (confirmed with user, Session 0.1):** genuinely open across
venues — exchanges (Kalshi, Polymarket), sportsbooks (DraftKings, FanDuel), and
fixed-line pick'em platforms (PrizePicks, Underdog, DK Pick6). Venue is a design
input evaluated on its own merits (repricing mechanism, fee/vig cost,
account-limiting risk, liquidity, legal footprint) — not a fixed boundary.
Category scope, by topic: Sports, Climate/Commodities, and narrow/down-ballot
Elections/Politics are in. Culture/Mentions/Tech & Science, Economics/Finance,
and Crypto are explicitly out (see Track Reference table below for why).

**Why validation methodology comes before backtesting, and both come before any
live capital:** the original plan treated backtesting (testing a finished model
against historical outcomes) as the validation step. That was corrected during
Session 0.1 — backtesting only confirms a model that already has a sound
methodology behind it. The real prerequisite is Closing Line Value (CLV), the
metric professional sports bettors actually use, adapted for prediction markets
(see Phase 3). This is a pre-outcome signal, gradeable far faster than waiting
for slow-resolving events (elections, seasonal weather thresholds) to fully
play out.

---

## Track Reference (confirmed scope, ranked by evidence-based confidence)

| Track | Venue(s) | Mechanism | Confidence | Why |
|---|---|---|---|---|
| Cross-venue arbitrage | Kalshi, Polymarket, sportsbooks, pick'em — any pair pricing the same real-world outcome differently | Price disagreement between venues, or a single market's YES+NO ≠ $1.00 | **Highest** | Doesn't depend on forecasting skill at all — real, already-realized profits documented (~$40M on Polymarket alone in one measured year) |
| Fixed-line pick'em platforms | PrizePicks, Underdog, DK Pick6 | Static line set once by platform's own model; fixed-multiplier payout; no live repricing against money flow | **High** | Directly reuses the existing DFS projection-engine pattern — same problem shape (projection vs. fixed number), not a new kind of problem |
| Weather/climate markets | Kalshi | Ground truth is objectively computable from free public data (NWS/GFS/METAR); retail anchors on round-number thresholds | **High** | Edge is in correctly applying available public data faster/better than a thin, low-attention market — no need to out-think anyone |
| Down-ballot politics (governor, mayoral, primary — marquee races excluded) | Kalshi, Polymarket | Documented "underconfidence" — prices compressed toward 50%, most extreme in down-ballot subcategories | **Moderate** | Real, qualitatively corroborated across sources, but magnitude is contested (key paper is an unreviewed preprint with an internal data-count discrepancy; a related study's methodology was publicly disputed by Kalshi) |
| Sportsbook player props (not main lines) | DraftKings, FanDuel | Documented as softer than main lines — less-covered by sharp risk management, slower to react to news | **Moderate** | Real vig-based cost to overcome (~4.6% avg. vs. ~0.85% on Kalshi, one direct comparison) plus account-limiting risk for consistent winners |
| Sportsbook main lines / flagship exchange sports markets | All | None identified beyond what's already priced in | **Lowest** | Market structure, not sport, determines efficiency — e.g. Asian handicap soccer is efficient while the plain 1X2 market on the same sport is biased; flagship markets sit on the efficient side |

**Explicitly out of scope**, confirmed Session 0.1: Culture/Mentions/Tech &
Science (thinnest available public data to build a real estimate from — arbitrage-only
territory at best); Economics/Finance (Fed decisions, inflation prints — among the
most professionally saturated categories researched); Crypto (dominated by traders
already pricing the underlying asset on crypto-native exchanges in real time).

Full sourced research backing this table is preserved in the Session 0.1 research
artifact — see Phase 0 below for its location.

---

## Rule for every session

A session is not "done" until its validation step passes. If validation fails,
that session is not complete — do not move to the next one. Same rule as the DFS
projects, carried over directly, with one addition specific to this project: **a
track's estimation model is not "validated" until it is logging CLV-equivalent
data on every flagged opportunity** (see Phase 3) — a model that produces
plausible-looking output but isn't logging its own price-vs-benchmark comparison
does not count as complete, even if it runs without error.

## Workflow preference — GitHub Desktop

Same as the DFS projects: the user commits and pushes through GitHub Desktop, not
raw `git` commands in PowerShell — it also handles pulls cleanly when needed. When
a session's files are ready, Claude provides the finished files and explains
exactly where each belongs in the repo; the user stages, commits, and pushes (and
pulls first, if needed) through GitHub Desktop.

## How to use this for session handoff

At the start of each new session, provide:
1. This session's card below (once Phase 1+ cards are scoped)
2. The relevant SESSION_LOG.md entries for prerequisite sessions
3. The actual current contents of any files listed under "Files touched"

That is the full context a fresh session needs — no need to re-explain the whole
project.

## Repo Structure (proposed — confirm at Session 1.1)

```
/Market_Betting
  /data          <- raw + processed market/event data
  /scripts       <- all pipeline scripts (per-track subfolders likely, TBD)
  /output        <- flagged opportunities, sizing suggestions, digest content
  /logs          <- session log + automation run logs
  /docs
    /research    <- Session 0.1 research artifact archived here
  /config        <- api_keys.env (gitignored), venue configs
  SESSION_LOG.md
  ROADMAP.md
  README.md
  requirements.txt
```

---

# PHASE 0 — Viability & Scope (Explore Session)

*No code. Establishes whether this project is worth building and, if so, what it
should focus on first.*

### Session 0.1 — Viability Assessment & Scope Definition

**Status:** ✅ Complete (2026-08-28) — see SESSION_LOG.md for full detail.

**Prerequisites:** None — first session.

**What was actually done:** An extended explore/discussion session, not a build
session. Reviewed the existing DFS_Optimizer repos directly (via browser) to
identify what architecture pattern was portable. Ran a full Advanced Research
task synthesizing academic and practitioner evidence on probability modeling and
market efficiency across sports, weather/climate, and down-ballot political
markets, plus Kalshi/Polymarket-specific arbitrage findings. Tested several
assumptions directly against real data (Kalshi's live market catalog, a direct
Kalshi-vs-sportsbook vig comparison, PrizePicks/Underdog's actual platform
structure) rather than relying on priors, which changed the plan's shape more
than once (see SESSION_LOG.md Session 0.1 entry for the full decision trail).

**Outputs:**
- This ROADMAP.md — the confirmed scope, ranked Track Reference table, and
  validation methodology.
- Research artifact: *"Building a +EV Prediction-Market System: Edge-Detection
  Across Sports, Weather, and Down-Ballot Politics"* — full sourced findings
  behind the Track Reference table. **Not yet archived in a repo** (no repo
  exists yet) — move to `/docs/research/` at Session 1.1.

**Validation (required to close session):**
- [x] A real, evidence-backed mechanism identified for each in-scope track (not
      just "this seems plausible")
- [x] A defined, pre-outcome validation methodology identified (CLV-equivalent)
      that doesn't require waiting for slow-resolving events to fully play out
- [x] Scope explicitly ranked by confidence, not left as an unordered list
- [x] Out-of-scope categories explicitly named with reasoning, not just omitted

**Handoff notes:** See "Open Decisions" at the end of this document — none of
them block Phase 0 from being closed, but all of them need answers before Phase
1 can start for real.

---

# PHASE 1 — Foundation & Repo Setup

*Not started. Cannot be fully scoped until the v1 track (Open Decision #1) is
chosen — the data source and estimation-engine sessions differ meaningfully by
track. Session 1.1 (repo/environment setup) is track-agnostic and can be scoped
now; later sessions in this phase should get their own detailed cards once a
track is picked, mirroring how each DFS sibling repo got its own Session 1.2+
once its data-source situation was actually investigated.*

### Session 1.1 — Environment & Repo Setup

**Status:** Not started.

**Prerequisites:** Phase 0 complete (done). Repo name decided (Open Decision #2).

**NFL/NHL/PGA analog:** Session 1.1 — direct copy pattern, contents genuinely new
(different dependencies expected: likely `pandas`, `numpy`, `requests`, plus
venue-specific API clients rather than `pulp`/`ortools` from day one — the sizing
optimizer isn't needed until a track has real flagged opportunities to allocate
across).

**Files touched (planned):**
- `/requirements.txt`, `/README.md`, `/.gitignore`
- Folder structure per Repo Structure above
- `/docs/research/` — Session 0.1's research artifact moved in here

**Validation (required to close session):**
- [ ] Fresh clone + `pip install -r requirements.txt` runs without error
- [ ] Python version confirmed and logged
- [ ] Research artifact from Session 0.1 is present in the repo, not orphaned in
      chat history

### Sessions 1.2+ — Track-Specific Data Ingestion, Estimation Engine, CLV Logging

**Status:** Not scoped yet. Track chosen (see below) — actual session cards
(what data source, what estimation model, what the validation checklist checks)
still need real investigation, the same way PGA's Session 1.2 couldn't be
written for real until Data Golf was actually evaluated and rejected.

**v1 track, decided Session 0.1 continuation (2026-08-28): Fixed-Line Pick'em
Platforms (PrizePicks, Underdog, DK Pick6).**

**Why this track, specifically, over the other two highest-confidence
candidates (cross-venue arbitrage, weather/climate):** this was a structural
decision, not a confidence-ranking decision — the user had no venue preference
and asked which track would make the others easier to build. Assessment:

- Cross-venue arbitrage needs the data-ingestion layer but skips the
  estimation layer entirely (pure price comparison, no probability model).
  Building it first would not exercise or prove out the calibration loop that
  every other track depends on.
- Weather/climate and down-ballot politics both need a real estimation engine
  built from scratch — new modeling work, not a reuse of anything that already
  exists.
- Fixed-line pick'em platforms also need a real estimation engine, but it's
  the one case where that engine is a near-direct reuse of code that already
  works: the existing DFS projection pattern (weighted blend of inputs →
  per-player projection) maps onto "projection vs. a platform's fixed line"
  almost without translation.

Building this track first forces the full five-layer stack (ingestion →
estimation → calibration/CLV logging → sizing → automation) to get built
end-to-end, using the lowest-risk, most-proven component for the hardest
layer. Every other estimation-based track then becomes "swap in a new
estimation model, reuse the proven scaffold" rather than building the scaffold
from nothing. Arbitrage is a reasonable candidate to bolt on relatively soon
after, since the scaffold it needs (multi-venue data ingestion, generalized)
will already partly exist.

Data source access, account-limiting-policy verification, and the concrete
estimation model spec (Open Decisions #3–#5 below) still need real
investigation before this becomes an actual Session 1.2 card — deliberately
deferred to a future session, not skipped.

---

## Open Decisions (block Phase 1 from being fully scoped)

1. ~~Which track becomes the actual v1 build?~~ **Resolved 2026-08-28: Fixed-Line
   Pick'em Platforms**, chosen on structural grounds (see Sessions 1.2+ card
   above for full reasoning) rather than confidence ranking. User had no venue
   preference and asked for a structural assessment; the DFS projection-engine
   reuse and full-stack scaffold benefit were the deciding factors.
2. ~~Repo name and visibility.~~ **Resolved 2026-08-28: `Market_Betting`.**
   Visibility to be set Private at Session 1.1, matching the DFS sibling repos,
   unless told otherwise.
3. **Data source access per track**, not yet researched:
   - Kalshi/Polymarket API access (public, need to confirm what's actually
     available without an account vs. with one)
   - Sportsbook odds feed options (if Track 5/6 pursued)
   - **PrizePicks/Underdog/DK Pick6 data access — genuinely unresearched.**
     Unlike Kalshi, these platforms don't have an established public API the way
     an exchange does. This needs real investigation before Track 2 can be
     scoped as a real Session 1.2+, the same way Data Golf's actual subscription
     terms had to be investigated (and ultimately rejected) before PGA's Session
     1.2 could be built for real.
4. **Verify account-limiting policy per pick'em platform directly** before
   relying on any platform's secondhand reputation for being more or less
   permissive toward consistent winners (Underdog was described by one source
   as more permissive than DraftKings/FanDuel — unverified, treat as a claim to
   check, not a fact to build around).
5. **Scope the first estimation model concretely** for whichever track is
   picked — at the same level of detail the DFS projection engines already have
   (weighted blend of specific, named inputs), not left abstract.

---
*Update this file at the close of each future session, per the project's
standing convention: ROADMAP.md and SESSION_LOG.md are only updated once both
sides agree a session is fully closed out, or remaining pieces are being
deliberately deferred to a later session (and that deferral is stated
explicitly, not silently dropped).*
