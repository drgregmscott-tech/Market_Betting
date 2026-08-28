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
trendline over a large enough sample to mean something (see Session 2.5's
sample-size thresholds). A track that cannot show that trendline, honestly,
over a real sample is not a working track — no matter how good any single
week looked.

**This point was raised again during Session 1.2 and is recorded here once, so
it doesn't need to be re-established every session going forward:** this system
is not being built to win every bet, or even most individual weeks. It is being
built to produce a real, positive edge over the general betting market across a
large enough sample — with real losing stretches along the way, same as any
legitimate trading edge. Any future session, or any person reading this roadmap
cold, should treat that as settled, not open for debate.

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

**Scope decision (confirmed with user, Session 0.1; re-confirmed Session 1.2):**
genuinely open across venues — exchanges (Kalshi, Polymarket), sportsbooks
(DraftKings, FanDuel), and fixed-line pick'em platforms (PrizePicks, Underdog,
DK Pick6). Venue is a design input evaluated on its own merits — repricing
mechanism, fee/vig cost, account-limiting risk, liquidity, and legal footprint —
not a fixed boundary. This is **6 build tracks**, not a rougher "3-4 areas"
count: the 3 original category areas (Sports, Climate/Commodities, narrow
Politics) split into 6 tracks because Sports alone spans three different venue
mechanisms (arbitrage, pick'em, sportsbook props), each with a distinct edge
source and risk profile. All 6 are planned at full session-level detail in this
roadmap as of Session 1.2.

**This system flags and sizes opportunities — it does not place bets.** Every
track's build ends at a frontend showing flagged opportunities and suggested
stakes; a human places the actual bet and reports the outcome back into the
system (see Session 2.5's outcome tracker). This is a deliberate design
decision, not a gap: consistent with this environment's restriction against
executing financial trades on the user's behalf, and because the system's own
outcome-tracking depends on knowing what was actually placed, which may
reasonably differ from what was suggested.
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
artifact — archived in `/docs/research/` as of Session 1.1.

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

**Session 1.1 note on this workflow:** the first-time setup of a brand-new repo
through GitHub Desktop has one sharp edge worth remembering for future sibling
projects — see the Session 1.1 entry in SESSION_LOG.md for the specific failure
mode (GitHub Desktop's "Add local repository" on a folder with no prior Git
history creates a *new*, disconnected local repository; "Publish repository"
then tries to create a second, duplicate repo on GitHub.com instead of linking
to one that already exists there). The reliable pattern is: create the repo on
GitHub.com first, then use GitHub Desktop's **Clone repository** flow (not
**Add local repository**) to pull that empty repo down, then copy project files
into the cloned folder before the first commit.

## How to use this for session handoff

At the start of each new session, provide:
1. This session's card below (once Phase 1+ cards are scoped)
2. The relevant SESSION_LOG.md entries for prerequisite sessions
3. The actual current contents of any files listed under "Files touched"

That is the full context a fresh session needs — no need to re-explain the whole
project.

## Repo Structure (confirmed, built Session 1.1)

```
/Market_Betting
  /data          <- raw + processed market/event data
  /scripts       <- all pipeline scripts (per-track subfolders likely, TBD)
  /output        <- flagged opportunities, sizing suggestions, digest content
  /logs          <- session log + automation run logs
  /docs
    /research    <- Session 0.1 research artifact archived here
  /config        <- api_keys.env (gitignored), api_keys.env.example (template), venue configs
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
- ROADMAP.md — the confirmed scope, ranked Track Reference table, and
  validation methodology.
- Research artifact: *"Building a +EV Prediction-Market System: Edge-Detection
  Across Sports, Weather, and Down-Ballot Politics"* — full sourced findings
  behind the Track Reference table. Archived in `/docs/research/` as of
  Session 1.1.

**Validation (required to close session):**
- [x] A real, evidence-backed mechanism identified for each in-scope track (not
      just "this seems plausible")
- [x] A defined, pre-outcome validation methodology identified (CLV-equivalent)
      that doesn't require waiting for slow-resolving events to fully play out
- [x] Scope explicitly ranked by confidence, not left as an unordered list
- [x] Out-of-scope categories explicitly named with reasoning, not just omitted

**Handoff notes:** See "Open Decisions" at the end of this document.

---

# PHASE 1 — Foundation & Repo Setup

### Session 1.1 — Environment & Repo Setup

**Status:** ✅ Complete (2026-08-28) — see SESSION_LOG.md for full detail.

**Prerequisites:** Phase 0 complete. Repo name decided (`Market_Betting`,
resolved Session 0.1 continuation).

**NFL/NHL/PGA analog:** Session 1.1 — direct copy pattern, contents genuinely new
(dependencies: `pandas`, `numpy`, `requests`, `python-dotenv` — venue-specific
API clients and the sizing optimizer are deferred until a track has real
flagged opportunities to allocate across).

**Files touched:**
- `/requirements.txt`, `/README.md`, `/.gitignore`
- `/config/api_keys.env.example` (template; real `config/api_keys.env` is
  gitignored and not yet created — no venue credentials exist yet)
- Folder structure per Repo Structure above, each empty folder held in place
  with a `.gitkeep` placeholder file
- `/docs/research/Building_a_+EV_Prediction-Market_System_Edge-Detection_Across_Sports_Weather_and_Down-Ballot_Politics.md`
  — Session 0.1's research artifact, moved in

**Validation (required to close session):**
- [x] Fresh clone + `pip install -r requirements.txt` runs without error —
      confirmed on the user's machine (Windows, Python 3.14): all four
      packages installed/resolved with no errors or conflicts.
- [x] Python version confirmed and logged — **Python 3.14**
      (`pythoncore-3.14-64`).
- [x] Research artifact from Session 0.1 is present in the repo, not orphaned
      in chat history — confirmed live at
      `github.com/drgregmscott-tech/Market_Betting/docs/research/`.

**Handoff notes:** Repo is live, private, on `main` branch, single commit
("Repo Setup"). GitHub Desktop's first-time publish workflow had a wrinkle —
see SESSION_LOG.md Session 1.1 entry for the specific failure and fix; the
Repo Structure section above and the Workflow Preference section earlier in
this document both now carry the corrected pattern for next time.

### Session 1.2 — Full Roadmap & Session Structure Definition
**Status:** ✅ Complete (2026-08-28)

**Prerequisites:** Phase 0 complete; Session 1.1 complete.

**What this session does:** Defines the complete phase/session map for the entire
project (this document), across all six tracks, so every future session has a
scoped card to start from — closing the gap Session 0.1 left (scope was defined,
but not broken into buildable sessions).

**Files touched:** `ROADMAP.md` (full rewrite/expansion), `SESSION_LOG.md` (new
entry once this closes).

**Validation (required to close session):**
- [x] Every one of the six tracks has a complete session breakdown (not just the
      v1 track) — Phases 2–8, 45 sessions total
- [x] Every session card has a stated goal, prerequisites, files touched, and a
      validation checklist — not left abstract
- [x] User has reviewed and approved the full map, through two full revision
      passes: (1) confirmed 6-track scope and requested 4 gap-closing additions
      (sample-size thresholds, manual-execution clarity, endpoint-health
      monitoring, realized-outcome tracking); (2) requested and received a full
      audit against Session 0.1's five per-venue evaluation criteria
      (repricing mechanism, fee/vig cost, account-limiting risk, liquidity,
      legal footprint), which surfaced and closed real gaps — liquidity and
      legal-footprint checks were narrative-only for arbitrage/weather/politics/
      props and are now explicit session-level checks; Phase 7's go/no-go was
      sharpened to evaluate market structure at the sub-market level rather than
      as a blanket flagship judgment
- [x] Sequencing logic (why this order) is explicit, not just asserted

**Decisions made:**
1. Full session-level roadmap built for all 6 tracks now, not just the v1 track
   — user's explicit direction, departing from the DFS repos' pattern of only
   scoping the next phase in detail. Rationale: this project's edge sources are
   more heterogeneous across tracks than the DFS repos' sport-to-sport variation,
   so planning all 6 up front surfaces cross-track gaps (as the two audit passes
   below demonstrated) that wouldn't be visible scoping one phase at a time.
2. Research from Open Decisions #3/#4 (endpoint access, account-limiting policy)
   does not get its own session number — folded into Session 1.1's continuation
   notes instead, since it was investigation supporting Session 1.1's still-open
   items, not a new build session. This roadmap-structuring work is Session 1.2.
3. Confirmed scope is 6 build tracks (not "3-4 areas," which was an imprecise
   restatement, not a scope change) — see Background & Approach above for the
   permanent record of this.
4. Explicit "flags and sizes, does not place bets" statement added to Background
   & Approach as a permanent, one-time record — not to be re-derived per session.
5. The project's "wins over time, not every bet" north star (already established
   in Session 0.1) was re-raised during this session's review and is now recorded
   as explicitly settled in Background & Approach, per user direction that this
   should not need to be re-argued in future sessions.

**Handoff notes:** This roadmap replaces the "Sessions 1.2+" stub that previously
stood in for all future work. Sessions 2.1 onward are now real, buildable cards —
Phase 2 (Fixed-Line Pick'em Platforms, the v1 track) is next.

---

# PHASE 2 — Track 1 (v1): Fixed-Line Pick'em Platforms

*Full original build of all five/six layers. PrizePicks, Underdog Fantasy, DK
Pick6 — reusing the DFS projection-engine pattern for the estimation layer, per
Session 0.1's structural decision.*

### Session 2.1 — Data Ingestion Prototype
**Status:** Not started
**Prerequisites:** Phase 1 complete.

**What gets built:** A working, non-production script that pulls live
projections from all three platforms' undocumented public endpoints (confirmed
reachable without login/API key per Session 1.1 continuation research):
- `partner-api.prizepicks.com/projections`
- Underdog's equivalent public projections endpoint
- DraftKings Pick6's equivalent public endpoint

Goal is proof-of-reach and schema discovery, not a production pipeline yet —
confirm each endpoint's real response shape, what fields are present (player,
stat type, line, sport, game time, odds/multiplier type), and how each platform's
schema differs from the others.

**Files touched:** `/scripts/ingestion/prototype_prizepicks.py`,
`/scripts/ingestion/prototype_underdog.py`,
`/scripts/ingestion/prototype_dkpick6.py`, `/docs/research/endpoint_schemas.md`
(new — documents the actual field-level schema found per platform)

**Validation (required to close session):**
- [ ] All three endpoints return live data successfully with no login/key
- [ ] Schema documented per platform (field names, types, what's missing/
      inconsistent across platforms)
- [ ] At least one full day's snapshot captured and saved locally as a sanity
      check on stability
- [ ] Explicit note on what breaks the pull (rate limiting? headers required?
      geographic restriction?) so Session 2.2 knows what defenses are needed

**Handoff notes:** This session is allowed to be messy/exploratory — it exists to
de-risk Session 2.2, not to produce production code.

---

### Session 2.2 — Production Data Ingestion Pipeline
**Status:** Not started
**Prerequisites:** Session 2.1 complete.

**What gets built:** A real, scheduled-ready ingestion pipeline that normalizes
all three platforms' data into one common schema (matching the "normalized across
books" pattern used by third-party odds aggregators, but built in-house), handles
errors/retries gracefully (since these are undocumented endpoints that can change
without notice — flagged explicitly in Session 2.1's research), and stores
snapshots to `/data`.

**Files touched:** `/scripts/ingestion/ingest_pickem.py` (production version),
`/scripts/ingestion/schema.py` (shared normalized schema), `/data/pickem/` (new
data folder), `/logs/ingestion.log`

**Validation (required to close session):**
- [ ] Pipeline runs end-to-end and produces a normalized dataset across all three
      platforms
- [ ] Handles a simulated failure (bad response, empty response, schema change)
      without crashing — logs the failure instead
- [ ] Confirmed idempotent (running twice in a row doesn't duplicate/corrupt data)
- [ ] At least 3 consecutive days of real automated pulls captured, reviewed for
      consistency

---

### Session 2.3 — Estimation Engine v1
**Status:** Not started
**Prerequisites:** Session 2.2 complete (needs real ingested data to build/test
against).

**What gets built:** The actual projection model — a weighted blend of specific,
named inputs (matching the DFS projection-engine pattern), producing a probability
estimate for each prop's over/under outcome, then comparing that estimate against
the platform's fixed line. This is where **Open Decision #5** gets resolved for
real, with concrete inputs named (e.g., recent performance window, opponent
matchup factor, injury/role status, home/away, pace/usage where applicable) —
exact input list to be finalized with real data in hand, not guessed in advance.

**Files touched:** `/scripts/estimation/pickem_model.py`,
`/docs/research/pickem_estimation_model_spec.md` (new — documents exact inputs,
weights, and reasoning, same detail level as the existing DFS projection docs)

**Validation (required to close session):**
- [ ] Model produces a probability estimate for every ingested prop, not just a
      subset
- [ ] Model's estimate is sanity-checked against a handful of manually-reasoned
      examples (does the model agree with obvious cases?)
- [ ] Model's inputs and weighting logic are documented at the same specificity
      as the DFS repos' projection engines — no unnamed "black box" factors
- [ ] Explicit note on what's NOT yet included (e.g. weather for outdoor sports,
      Vegas team totals) and why, so it's a stated gap, not a silent one

---

### Session 2.4 — CLV-Equivalent Calibration Logging
**Status:** Not started
**Prerequisites:** Session 2.3 complete.

**What gets built:** The pre-outcome validation layer — for every flagged
opportunity, log the model's estimate alongside a benchmark (e.g. the consensus
across all three platforms, or a sharp-book proxy where available) at flag time,
then track how that comparison moves before the event resolves. This is the
project's core design principle (per Session 0.1, Decision #2) and is what makes
a model "validated," not just "running."

**Files touched:** `/scripts/calibration/clv_logger.py`,
`/data/pickem/clv_log.csv` (or equivalent structured store), `/docs/clv_methodology.md`

**Validation (required to close session):**
- [ ] Every flagged opportunity from Session 2.3's model gets a CLV-equivalent
      entry logged automatically, not manually
- [ ] Logging captures both the flag-time estimate and a real benchmark
      comparison (not just the model's own confidence)
- [ ] At least one real week of logged data collected and reviewed for
      completeness (no silently-dropped entries)
- [ ] Log format is durable/queryable — a future session can pull "all flags from
      the last N days" without custom one-off code

---

### Session 2.5 — Sample-Size Thresholds & Realized-Outcome Tracking
**Status:** Not started
**Prerequisites:** Session 2.4 complete.

**What gets built:** Two related pieces, both foundational for every later
"go/no-go" checkpoint in this roadmap (Sessions 2.9, 3.6, 4.7, 5.7, 6.7, 7.0):

- **Sample-size thresholds:** a concrete, calculated minimum number of graded
  flags needed before this track's performance is treated as meaningful, based
  on this track's real observed flag frequency (now knowable from Sessions
  2.1–2.4's real data) and standard statistical practice for evaluating a
  binary-outcome edge (not an arbitrarily chosen calendar length). This becomes
  the actual number "Phase 3's sample-size thresholds" was pointing to in
  earlier drafts of this roadmap — defined here, for real, using real data.
- **Realized-outcome tracking:** a distinct log, separate from the CLV log built
  in Session 2.4, that records the actual resolved result (won/lost, actual
  payout) of every bet the user reports having placed. CLV is a deliberate
  pre-outcome proxy signal — this is the real thing it's a proxy for. Without
  this, the project's own "S&P 500 chart" north star (ROADMAP.md, Background &
  Approach) has no real trendline to plot, only a proxy for one.

**Files touched:** `/docs/sample_size_methodology.md` (new),
`/scripts/calibration/outcome_tracker.py` (new),
`/data/pickem/outcome_log.csv` (new — separate from `clv_log.csv`)

**Validation (required to close session):**
- [ ] Sample-size threshold calculated and documented with the reasoning shown,
      not just a final number asserted
- [ ] Outcome tracker can accept a manually-reported bet result (placed bet →
      outcome) and store it durably, linked back to the original CLV log entry
      for that flagged opportunity
- [ ] Confirmed the two logs (CLV and outcome) can be joined/compared later —
      e.g. "did high-CLV flags actually win more" is a queryable question, not
      just a hoped-for correlation

**Handoff notes:** This session also formalizes something implicit until now:
**this system flags and sizes opportunities for the user to act on manually — it
does not place bets itself.** That's a deliberate design decision, not a gap:
consistent with this environment's restriction against Claude executing
financial trades or transfers on a user's behalf, and because the whole point of
the outcome tracker above depends on the user reporting what they actually did,
which may reasonably differ from what the system suggested. This should be
stated plainly in the real ROADMAP.md's Background & Approach section once this
draft is merged, so no future session mistakes "flagged" for "placed."

---

### Session 2.6 — Bankroll & Sizing Logic
**Status:** Not started
**Prerequisites:** Session 2.5 complete (sizing should only apply to
CLV-validated opportunities, not raw model output).

**What gets built:** Position-sizing logic (e.g. a Kelly-criterion-based or
fractional-Kelly approach, consistent with what professional sports bettors use)
that turns a flagged, CLV-positive opportunity into a concrete suggested stake,
factoring in account-limiting risk per platform (from the Session 1.1
continuation research — PrizePicks treated as "cash out frequently, assume
elevated closure risk," Underdog/DK Pick6 as more scalable).

**Files touched:** `/scripts/sizing/sizing_engine.py`,
`/docs/sizing_methodology.md`

**Validation (required to close session):**
- [ ] Sizing logic produces a concrete stake suggestion for every CLV-positive
      flagged opportunity
- [ ] Platform-specific risk adjustment is present and documented (not applying
      identical sizing logic to all three platforms blindly)
- [ ] Sanity-checked against a few manual examples (does a bigger edge produce a
      bigger suggested stake, within sane bounds?)
- [ ] Explicit bankroll cap / max-single-position rule stated and enforced in
      code, not just described in docs

---

### Session 2.7 — Automation (GitHub Actions)
**Status:** Not started
**Prerequisites:** Session 2.6 complete.

**What gets built:** Scheduled automation (matching the DFS repos' GitHub
Actions pattern) that runs ingestion → estimation → CLV logging → sizing on a
recurring schedule appropriate to the pick'em platforms' update cadence, and
produces a digest of flagged opportunities.

**Files touched:** `.github/workflows/pickem_pipeline.yml`,
`/scripts/run_pipeline.py` (orchestrator), `/output/digest/`

**Validation (required to close session):**
- [ ] Workflow runs successfully on GitHub Actions' own infrastructure (not just
      locally) at least 3 times on schedule
- [ ] Failure in one step (e.g. ingestion) doesn't silently corrupt downstream
      steps — pipeline fails loudly and logs why
- [ ] Digest output is complete and matches what a manual run would produce
- [ ] Secrets (if any needed) are handled via GitHub Actions secrets, not
      committed anywhere

---

### Session 2.8 — Frontend (Cloudflare Pages)
**Status:** Not started
**Prerequisites:** Session 2.7 complete (needs real automated output to display).

**What gets built:** A Cloudflare Pages frontend (matching the DFS repos'
pattern) displaying current flagged opportunities, sizing suggestions, and a
running CLV-performance view (the "S&P 500 chart" north star from ROADMAP.md —
this is the actual visualization of that trendline).

**Files touched:** `/frontend/` (new), Cloudflare Pages deployment config

**Validation (required to close session):**
- [ ] Frontend deploys successfully and is reachable at a live URL
- [ ] Displays current flagged opportunities pulled from real automated output,
      not mock data
- [ ] Displays a CLV-performance trendline view, even if the sample is still
      small at this point
- [ ] Confirmed working on both desktop and mobile view

---

### Session 2.9 — Live Paper-Trading Validation Window
**Status:** Not started
**Prerequisites:** Session 2.8 complete. Full stack live and running
automatically.

**What gets built:** No new code — this is a **soak-test session**. The full
pipeline runs live, unattended, for a window sized against the sample-size
threshold defined in Session 2.5 (not an arbitrary calendar length). During this
window, the user is expected to report real placed-bet outcomes into the
outcome tracker built in Session 2.5, so this checkpoint can weigh actual
results, not just the CLV proxy for them.

**Files touched:** None new — this session reviews `/data/pickem/clv_log.csv`
and `/data/pickem/outcome_log.csv` together and produces a written assessment.

**Validation (required to close session):**
- [ ] Sample-size threshold from Session 2.5 reached, for both CLV entries and
      real reported outcomes
- [ ] Real graded CLV performance reviewed — does it show the "positive
      trendline with real drawdowns" pattern the project's north star describes,
      or not?
- [ ] Real reported outcomes (not just CLV) reviewed against the same standard,
      and checked for directional agreement with the CLV signal
- [ ] Explicit go/no-go decision recorded: is Track 1 (pick'em) validated enough
      to consider real capital, or does it need another iteration on the
      estimation model first?
- [ ] If no-go: specific, named reasons documented (not just "didn't work") so
      the next session knows what to fix

**Handoff notes:** This is the checkpoint the whole "no guarantees ≠ lower bar"
rule exists for. A session that fails this validation is not a failed project —
it's the system doing exactly what it's supposed to do before capital is at risk.

---

# PHASE 3 — Track 2: Cross-Venue Arbitrage

*Highest-confidence track. Unlike Phase 2, this track skips the estimation layer
entirely — it's pure price comparison across venues, so several Phase 2 sessions
collapse or don't apply.*

### Session 3.1 — Multi-Venue Data Ingestion
**Status:** Not started
**Prerequisites:** Phase 2 fully complete (reuses its ingestion pattern).

**What gets built:** Generalizes the Phase 2 ingestion pattern to pull the same
real-world outcome's pricing from multiple venues simultaneously — Kalshi,
Polymarket, sportsbooks, and the pick'em platforms already integrated in Phase 2.
Kalshi/Polymarket API access needs to be investigated here specifically (flagged
as unresearched in Open Decision #3 — the pick'em research covered platforms 1-3,
not the exchanges).

**Files touched:** `/scripts/ingestion/ingest_kalshi.py`,
`/scripts/ingestion/ingest_polymarket.py`, `/scripts/ingestion/venue_matcher.py`
(matches the same real-world event across venues)

**Validation (required to close session):**
- [ ] Kalshi and Polymarket API access confirmed and documented (auth method,
      rate limits, what's free vs. requires an account)
- [ ] Venue-matching logic correctly identifies the same real-world event/outcome
      across at least 2 venues in a real test
- [ ] Normalized schema extended to cover exchange-style pricing (YES/NO
      contracts), not just sportsbook-style odds

---

### Session 3.2 — Arbitrage Detection Logic
**Status:** Not started
**Prerequisites:** Session 3.1 complete.

**What gets built:** Pure price-comparison logic — flags cases where the same
outcome is priced inconsistently across venues (including single-market YES+NO ≠
$1.00 mispricing), accounting for each venue's fee structure so a flagged
"arbitrage" is real profit, not an illusion created by ignoring fees. Per Session
0.1's five per-venue evaluation criteria, this session also explicitly checks
**liquidity** (a price gap that can't actually be filled at meaningful size isn't
a real arbitrage) and **legal footprint** (confirms both venues in a flagged pair
are legally available in the user's jurisdiction before the opportunity is
surfaced, not just priced).

**Files touched:** `/scripts/arbitrage/detector.py`,
`/scripts/arbitrage/liquidity_check.py` (new),
`/docs/venue_legal_footprint.md` (new — per-venue, per-state availability
reference, checked at flag time)

**Validation (required to close session):**
- [ ] Detection logic correctly flags a known historical or simulated arbitrage
      case
- [ ] Fee-adjusted profit calculation confirmed accurate (manually cross-checked
      on at least 2 real examples)
- [ ] False-positive check: confirms it does NOT flag price differences that
      don't actually clear fees
- [ ] Liquidity check confirmed: a flagged opportunity includes the real
      available size at that price, not just the headline price
- [ ] Legal footprint check confirmed: a flagged opportunity is suppressed or
      clearly labeled if either venue isn't legally available to the user

---

### Session 3.3 — Sizing Logic Adaptation
**Status:** Not started
**Prerequisites:** Session 3.2 complete.

**What gets built:** Adapts Phase 2's sizing engine for arbitrage's different
risk profile (execution risk and capital-lockup time across two simultaneous
positions, rather than single-position edge sizing).

**Files touched:** `/scripts/sizing/sizing_engine.py` (extended, not rebuilt)

**Validation (required to close session):**
- [ ] Sizing correctly accounts for capital needing to sit in two venues
      simultaneously
- [ ] Execution-risk buffer included (price can move between detecting and
      executing both legs)

---

### Session 3.4 — Automation Adaptation
**Status:** Not started
**Prerequisites:** Session 3.3 complete.

**What gets built:** Extends the Phase 2 GitHub Actions workflow to include the
arbitrage pipeline, likely on a faster polling cadence than pick'em given how
quickly arbitrage windows close.

**Files touched:** `.github/workflows/arbitrage_pipeline.yml`

**Validation (required to close session):**
- [ ] Workflow runs on schedule reliably
- [ ] Polling frequency justified against how quickly real arbitrage windows are
      observed to close (not an arbitrary guess)

---

### Session 3.5 — Frontend Integration
**Status:** Not started
**Prerequisites:** Session 3.4 complete.

**What gets built:** Adds arbitrage opportunities to the existing Phase 2
frontend as a new section/view, rather than a separate site.

**Files touched:** `/frontend/` (extended)

**Validation (required to close session):**
- [ ] Arbitrage opportunities display correctly alongside pick'em, clearly
      distinguished as a different track

---

### Session 3.6 — Live Validation Window
**Status:** Not started
**Prerequisites:** Session 3.5 complete.

**What gets built:** Same soak-test pattern as Session 2.9, adapted — since
arbitrage has no estimation model, "validation" here means confirming flagged
opportunities were real and executable, not a CLV comparison. Realized-outcome
reporting (per Session 2.5's tracker) still applies here too, since arbitrage
positions do get placed and resolve.

**Validation (required to close session):**
- [ ] Minimum sample size of flagged opportunities reached
- [ ] Spot-checked sample confirms flagged opportunities were genuinely
      executable at the prices logged (not stale/unavailable by execution time)
- [ ] Go/no-go decision recorded

---

# PHASE 4 — Track 3: Weather/Climate Markets (Kalshi)

### Session 4.1 — Data Ingestion (Kalshi + Public Weather Data)
**Status:** Not started
**Prerequisites:** Phase 2 complete (reuses ingestion pattern); Kalshi API access
already resolved in Session 3.1 if Phase 3 is done first — otherwise resolve here.

**What gets built:** Ingests Kalshi's weather/climate markets alongside free
public ground-truth data (NWS, GFS, METAR) needed to independently estimate the
same outcomes Kalshi is pricing. Per Session 0.1's per-venue evaluation
criteria, this session also captures each market's real order-book depth
(**liquidity** — Kalshi weather markets are known to be thin, so this can't be
assumed adequate) and confirms Kalshi's current legal availability to the user
(**legal footprint**), rather than deferring either check to a later session.

**Files touched:** `/scripts/ingestion/ingest_weather_markets.py`,
`/scripts/ingestion/ingest_nws_gfs_metar.py`

**Validation (required to close session):**
- [ ] Kalshi weather market data and public weather data both ingest
      successfully and can be joined on the same real-world event
- [ ] Data freshness confirmed adequate for the market's resolution timing (data
      arrives before markets need to be evaluated)
- [ ] Order-book depth/liquidity captured per market, not just the top price
- [ ] Legal footprint confirmed and documented for Kalshi in the user's
      jurisdiction

---

### Session 4.2 — Estimation Engine (Weather Threshold Model)
**Status:** Not started
**Prerequisites:** Session 4.1 complete.

**What gets built:** A model that computes the true probability of a weather
threshold being met directly from public forecast data (e.g. GFS ensemble spread
around a specific temperature/precipitation threshold), then compares that
against Kalshi's round-number-anchored market price. This is new modeling work
(not a reuse of the pick'em model), per Session 0.1.

**Files touched:** `/scripts/estimation/weather_model.py`,
`/docs/research/weather_estimation_model_spec.md`

**Validation (required to close session):**
- [ ] Model's probability estimates are sanity-checked against at least a
      handful of already-resolved historical Kalshi weather markets
- [ ] Model correctly handles ensemble/uncertainty data, not just a single
      point forecast
- [ ] Documented at the same specificity level as Session 2.3's spec

---

### Session 4.3 — CLV Logging Hook-In
**Status:** Not started
**Prerequisites:** Session 4.2 complete.

**What gets built:** Connects the weather model's output to the same CLV
logging infrastructure built in Session 2.4 (reused, not rebuilt).

**Files touched:** `/scripts/calibration/clv_logger.py` (extended to accept a
new track parameter, not duplicated)

**Validation (required to close session):**
- [ ] Weather track flags log correctly into the same CLV structure
- [ ] At least one real week of logged weather flags reviewed for completeness

---

### Session 4.4 — Sizing Adaptation
**Status:** Not started
**Prerequisites:** Session 4.3 complete.

**Files touched:** `/scripts/sizing/sizing_engine.py` (extended)

**Validation (required to close session):**
- [ ] Sizing correctly reflects Kalshi's fee structure and this track's typical
      edge size (likely smaller, more frequent edges than pick'em)

---

### Session 4.5 — Automation Adaptation
**Status:** Not started
**Prerequisites:** Session 4.4 complete.

**Files touched:** `.github/workflows/weather_pipeline.yml`

**Validation (required to close session):**
- [ ] Workflow scheduled appropriately against weather forecast update cadence
      (e.g. aligned to GFS run times)

---

### Session 4.6 — Frontend Integration
**Status:** Not started
**Prerequisites:** Session 4.5 complete.

**Validation (required to close session):**
- [ ] Weather track displays correctly in the existing frontend

---

### Session 4.7 — Live Validation Window
**Status:** Not started
**Prerequisites:** Session 4.6 complete.

**Validation (required to close session):**
- [ ] Minimum sample size reached
- [ ] Real graded CLV performance reviewed against the north-star trendline
      standard
- [ ] Go/no-go decision recorded

---

# PHASE 5 — Track 4: Down-Ballot Politics (Kalshi/Polymarket)

### Session 5.1 — Data Ingestion (Race Lists + Polling Data)
**Status:** Not started
**Prerequisites:** Phase 2 complete; Kalshi/Polymarket access already resolved
by this point (Phase 3).

**What gets built:** Ingests down-ballot race markets (governor, mayoral,
primary — marquee races explicitly excluded per Track Reference table) plus
available public polling data for the same races. Per Session 0.1's per-venue
criteria, this session also captures market **liquidity** (down-ballot markets
are lower-volume by nature, and a flagged mispricing with no real size behind it
isn't actionable) and confirms each venue's **legal footprint** for down-ballot
political markets specifically, since political-market legality can differ from
a venue's general legal status.

**Files touched:** `/scripts/ingestion/ingest_politics_markets.py`,
`/scripts/ingestion/ingest_polling_data.py`

**Validation (required to close session):**
- [ ] Race markets and polling data both ingest successfully and join correctly
      on the same race
- [ ] Explicit filter confirmed working: marquee/high-profile races excluded per
      scope
- [ ] Liquidity captured per race market, and thin/illiquid races flagged as
      such rather than treated the same as deep markets
- [ ] Legal footprint confirmed specifically for political-market participation,
      not assumed from the venue's general availability

---

### Session 5.2 — Estimation Engine (Underconfidence-Correction Model)
**Status:** Not started
**Prerequisites:** Session 5.1 complete.

**What gets built:** A model targeting the documented "underconfidence" pattern
(prices compressed toward 50%, most pronounced in down-ballot races) — new
modeling work. Given the Track Reference table's noted caveat (key paper is an
unreviewed preprint with a data-count discrepancy; a related study's methodology
was publicly disputed by Kalshi), this session should include a re-verification
step against current, independent sources before the model is built around that
finding.

**Files touched:** `/scripts/estimation/politics_model.py`,
`/docs/research/politics_estimation_model_spec.md`

**Validation (required to close session):**
- [ ] Underconfidence finding re-checked against current sources before being
      built into the model, given the noted contested magnitude
- [ ] Model sanity-checked against historical resolved down-ballot markets where
      available
- [ ] Documented at the same specificity level as prior estimation specs

---

### Session 5.3 — CLV Logging Hook-In
**Status:** Not started
**Prerequisites:** Session 5.2 complete.

**Validation (required to close session):**
- [ ] Politics track flags log correctly into shared CLV structure
- [ ] Noted explicitly: this track's markets resolve slowly (election dates),
      so CLV-equivalent (pre-outcome) signal matters even more here than
      elsewhere — confirm the logged benchmark is meaningful pre-resolution,
      not just a placeholder

---

### Session 5.4 — Sizing Adaptation
**Status:** Not started
**Prerequisites:** Session 5.3 complete.

**Validation (required to close session):**
- [ ] Sizing reflects the long capital-lockup time for slow-resolving political
      markets (money tied up for weeks/months, not hours/days)

---

### Session 5.5 — Automation Adaptation
**Status:** Not started
**Prerequisites:** Session 5.4 complete.

**Validation (required to close session):**
- [ ] Workflow scheduled appropriately (likely daily/weekly, not high-frequency,
      given slow-moving polling data)

---

### Session 5.6 — Frontend Integration
**Status:** Not started
**Prerequisites:** Session 5.5 complete.

**Validation (required to close session):**
- [ ] Politics track displays correctly, with resolution-date context shown
      (since these are long-dated positions)

---

### Session 5.7 — Live Validation Window
**Status:** Not started
**Prerequisites:** Session 5.6 complete.

**Validation (required to close session):**
- [ ] Minimum sample size reached — explicitly acknowledged this may take
      longer to accumulate than faster-resolving tracks
- [ ] Go/no-go decision recorded

---

# PHASE 6 — Track 5: Sportsbook Player Props (DraftKings, FanDuel)

### Session 6.1 — Odds Feed Ingestion
**Status:** Not started
**Prerequisites:** Phase 2 complete.

**What gets built:** Ingests DK/FD player prop odds. Since DK/FD don't offer
public APIs (same undocumented-endpoint situation as the pick'em platforms, per
Session 1.1 continuation research pattern), this reuses the defensive-ingestion
approach from Session 2.2 rather than starting from scratch. Per Session 0.1's
per-venue criteria, this session also confirms **legal footprint** specifically
for player-prop markets, since prop-bet legality varies by state independently
of a sportsbook's general legal status (some states permit sportsbook wagering
but restrict or ban certain prop categories).

**Files touched:** `/scripts/ingestion/ingest_dk_props.py`,
`/scripts/ingestion/ingest_fd_props.py`

**Validation (required to close session):**
- [ ] Both feeds ingest successfully
- [ ] Vig/juice correctly extracted and stored (needed to compute true no-vig
      probability, not just the raw line)
- [ ] Legal footprint confirmed specifically at the prop-category level, not
      just "is this sportsbook legal here"

---

### Session 6.2 — Estimation Engine Adaptation
**Status:** Not started
**Prerequisites:** Session 6.1 complete.

**What gets built:** Adapts the Phase 2 pick'em projection model (same
underlying problem shape — projection vs. a number) rather than building new,
with adjustments for sportsbook-specific vig and market depth.

**Files touched:** `/scripts/estimation/sportsbook_props_model.py` (adapted from
`pickem_model.py`, not duplicated logic where avoidable)

**Validation (required to close session):**
- [ ] Model correctly separates "true edge" from "vig cost" so sizing later
      isn't fooled by a line that only looks soft after vig is ignored

---

### Session 6.3 — CLV Logging Hook-In
**Status:** Not started
**Prerequisites:** Session 6.2 complete.

**Validation (required to close session):**
- [ ] Props track flags log correctly into shared CLV structure, with a real
      sharp-book benchmark (e.g. Pinnacle-style no-vig line) where available —
      this is the actual CLV metric in its most literal form for this track

---

### Session 6.4 — Sizing Adaptation (Account-Limiting Risk Built In)
**Status:** Not started
**Prerequisites:** Session 6.3 complete.

**What gets built:** Sizing here must explicitly account for account-limiting
risk — this is the track where that risk is highest and best-documented (per
Track Reference table: consistent winners get limited on DK/FD sportsbooks in a
way that doesn't apply the same way to exchanges or, per the pick'em research,
even to PrizePicks/Underdog/DK Pick6).

**Files touched:** `/scripts/sizing/sizing_engine.py` (extended)

**Validation (required to close session):**
- [ ] Sizing logic includes an explicit limiting-risk dampener/cap distinct from
      the other tracks, not reused blindly from pick'em or arbitrage

---

### Session 6.5 — Automation Adaptation
**Status:** Not started
**Prerequisites:** Session 6.4 complete.

**Validation (required to close session):**
- [ ] Workflow scheduled against DK/FD line-movement cadence

---

### Session 6.6 — Frontend Integration
**Status:** Not started
**Prerequisites:** Session 6.5 complete.

**Validation (required to close session):**
- [ ] Props track displays correctly, with a visible limiting-risk indicator per
      flagged opportunity

---

### Session 6.7 — Live Validation Window
**Status:** Not started
**Prerequisites:** Session 6.6 complete.

**Validation (required to close session):**
- [ ] Minimum sample size reached
- [ ] Go/no-go decision recorded, explicitly factoring in whether real-world
      account limiting was observed during the window, not just modeled edge

---

# PHASE 7 — Track 6: Sportsbook Main Lines / Flagship Exchange Sports Markets

**⚠️ Go/No-Go Checkpoint required before this phase starts building anything.**
This is the lowest-confidence track in the Track Reference table ("None
identified beyond what's already priced in"). Per the project's standing rule
(no track gets built out on hope alone), this phase opens with an explicit
checkpoint session, not a build session.

### Session 7.0 — Go/No-Go Checkpoint
**Status:** Not started
**Prerequisites:** Phases 2–6 complete, so there's a real track record to weigh
this decision against (does the project actually need a 6th track, or are 5
enough?).

**What this session does:** Revisits the Track Reference table's reasoning
("market structure, not sport, determines efficiency... flagship markets sit on
the efficient side") against whatever's been learned building Phases 2–6, and
makes an explicit build/skip decision. Critically, this session evaluates
**market structure at the sub-market level, not the track as a whole** — the
original research specifically found that within the same sport, some market
*types* are efficient (e.g. Asian handicap soccer) while others on the same
event are not (e.g. that same game's plain 1X2 market). A blanket "is flagship
worth building" judgment would miss this; the real question is whether any
specific sub-market type shows the same softness pattern found in the
higher-confidence tracks, even inside an overall-efficient flagship market.

**Files touched:** `/docs/research/flagship_submarket_efficiency_review.md`
(new)

**Validation (required to close session):**
- [ ] Explicit decision recorded: build Phase 7 or formally retire this track
- [ ] Decision is made at the sub-market-type level (which specific bet types,
      if any, look soft), not as a single up-or-down call on "flagship sports"
      as an undifferentiated category
- [ ] If building: reasoning stated for why flagship markets are now believed
      worth pursuing despite the original low-confidence rating
- [ ] If retiring: ROADMAP.md updated to move this from "planned" to "explicitly
      out of scope," matching how Culture/Mentions/Tech was documented in
      Session 0.1

### Sessions 7.1–7.7 — Full Build (only if Session 7.0 is a "go")
**Status:** Not scoped in detail — deliberately deferred until Session 7.0's
decision is made, since detailing a track that may be retired wastes effort.
Would follow the same seven-session pattern as Phase 6 if greenlit.

---

# PHASE 8 — Cross-Track Portfolio Management

*Only relevant once 2+ tracks are live and validated. Not a single track's
concern — this is about managing the system as a whole.*

### Session 8.1 — Unified Dashboard
**Status:** Not started
**Prerequisites:** At least 2 tracks through their own Live Validation Window
(e.g. Phases 2 and 3 both complete).

**What gets built:** Consolidates the per-track frontend views (built
incrementally in each phase) into one true unified view — all currently flagged
opportunities across every live track, ranked and comparable.

**Validation (required to close session):**
- [ ] Displays real data from at least 2 live tracks simultaneously
- [ ] Correctly ranks/compares opportunities across tracks with different edge
      sizes and units (a 3% weather edge vs. a 10% pick'em edge needs a common
      comparison basis)

---

### Session 8.2 — Portfolio-Level Bankroll Allocation
**Status:** Not started
**Prerequisites:** Session 8.1 complete.

**What gets built:** Extends per-track sizing into a portfolio-level allocator —
total bankroll gets split across tracks based on each track's demonstrated edge
and volatility, not just summed naively from independent per-track sizing.

**Validation (required to close session):**
- [ ] Allocator respects a total-bankroll cap across all tracks combined, not
      just per-track caps that could sum to over-exposure
- [ ] Sanity-checked against a manual example spanning 2+ tracks

---

### Session 8.3 — Ongoing Recalibration Cadence
**Status:** Not started
**Prerequisites:** Session 8.2 complete.

**What gets built:** A defined, recurring process (inspired directly by the DFS
repos' own recalibration scripts, e.g. `fit_sigma_recalibration.py`) for
periodically re-fitting every track's estimation model against newly graded
outcomes — making the calibration loop an ongoing practice, not a one-time
Phase 2–7 build step.

**Validation (required to close session):**
- [ ] Recalibration process runs successfully against real accumulated outcome
      data from at least one track
- [ ] Cadence (how often this runs) is explicitly stated and justified, not left
      implicit

---

### Session 8.4 — Ingestion Health Monitoring & Endpoint Repair Cadence
**Status:** Not started
**Prerequisites:** Session 8.1 complete (at least 2 tracks live, so there's
real multi-source ingestion running to monitor).

**What gets built:** Every non-exchange data source in this project (PrizePicks,
Underdog, DK Pick6, DK/FD sportsbook props) is an undocumented public endpoint —
flagged repeatedly throughout this roadmap as something that "can change without
notice." Up to this point, every automation session (2.7, 3.4, 4.5, 5.5, 6.5)
built retry/error-logging into its own pipeline individually, but nothing checks
*across* tracks whether a source has silently gone stale (still returning
200-OK responses, but with wrong/empty/malformed data that passes basic error
handling). This session builds that cross-track check plus a defined response
process: a lightweight schema-validation and freshness check that runs
alongside the existing automation, alerts (at minimum, a visible flag in the
frontend; a real notification channel — e.g. email — can be considered here
too) when a source looks broken, and a documented, repeatable process for
re-diagnosing an endpoint that's changed (matching the reverse-engineering
approach used in Session 2.1, applied again on demand rather than only once).

**Files touched:** `/scripts/monitoring/endpoint_health_check.py` (new),
`.github/workflows/health_check.yml` (new — runs independently of the per-track
pipelines so a broken track can't hide its own monitoring failure),
`/docs/endpoint_repair_runbook.md` (new — the repeatable re-diagnosis process)

**Validation (required to close session):**
- [ ] Health check correctly distinguishes "source is down" (no response) from
      "source responded but data looks wrong" (schema/freshness failure) —
      these need different handling
- [ ] Simulated staleness/schema-change test confirms the check actually catches
      it, not just a clean-failure test
- [ ] Alert is visible somewhere the user will actually see it in time to matter
      for daily use, not buried in a log file
- [ ] Runbook is concrete enough that repairing a broken endpoint doesn't
      require re-deriving Session 2.1's original investigation from scratch

**Handoff notes:** This session directly protects the project's ability to
"consistently identify +EV bets on a daily basis" — a silently broken pick'em
endpoint that keeps returning stale data would otherwise flag confidently wrong
opportunities with no visible sign anything was off.

---

## Sequencing logic — why this order

1. **Phase 2 before everything else, in full detail**, because it's the only
   phase that builds each layer of the stack for the first time. Every later
   phase's session count is smaller specifically *because* Phase 2 pays that cost
   once.
2. **Phase 3 (arbitrage) second**, even though it doesn't need Phase 2's
   estimation layer, because it needs the ingestion pattern and because it's the
   highest-confidence track — validating it early gives the project a second data
   point on whether the "S&P 500 trendline" standard is achievable in practice,
   fast (arbitrage resolves quickly), before committing more sessions to slower
   tracks.
3. **Phases 4–5 (weather, politics) in Track Reference order**, since both need
   genuinely new estimation models and neither depends on the other.
4. **Phase 6 (sportsbook props) after weather/politics**, since it's rated
   "Moderate" and specifically requires the account-limiting-risk handling that's
   easier to design well once the project has real operating experience with
   risk-adjusted sizing from earlier tracks.
5. **Phase 7 (flagship/main lines) gated behind an explicit go/no-go**, since
   it's the lowest-confidence track and the project's own standing rule says
   tracks don't get built on hope — by the time Phase 7 would start, there's
   real evidence to make that call with instead of guessing now.
6. **Phase 8 last**, since portfolio-level management is meaningless with only
   one live track. **Session 8.4 (endpoint health) is deliberately placed here**,
   not earlier — it needs at least 2 live tracks' real ingestion history to
   design a meaningful cross-track check against, even though the risk it
   protects against (silent endpoint breakage) exists from Session 2.1 onward.
   Each track's own automation session still includes its own basic retry/error
   handling in the meantime — 8.4 adds the cross-track staleness/schema check on
   top of that, not a replacement for it.

---

## Open Decisions

1. ~~Which track becomes the actual v1 build?~~ **Resolved 2026-08-28: Fixed-Line
   Pick'em Platforms**, chosen on structural grounds (see Phase 2 above for full
   reasoning) rather than confidence ranking. User had no venue preference and
   asked for a structural assessment; the DFS projection-engine reuse and
   full-stack scaffold benefit were the deciding factors.
2. ~~Repo name and visibility.~~ **Resolved 2026-08-28: `Market_Betting`.**
   Created Session 1.1, private, under `drgregmscott-tech`.
3. ~~Data source access per pick'em platform.~~ **Resolved 2026-08-28** (Session
   1.1 continuation, ahead of Session 1.2): PrizePicks, Underdog, and DK Pick6
   each have no official developer API, but all three run undocumented public
   endpoints reachable without login or an API key (e.g.
   `partner-api.prizepicks.com/projections`). No public API is stable by design
   — Session 2.1 (Data Ingestion Prototype) and Session 8.4 (Ingestion Health
   Monitoring) exist specifically because these endpoints can change without
   notice. **Kalshi/Polymarket API access and sportsbook odds feed options
   remain open** — deferred to Session 3.1 (Multi-Venue Data Ingestion) and
   Session 6.1 (Odds Feed Ingestion) respectively, where they're actually
   needed.
4. ~~Verify account-limiting policy per pick'em platform.~~ **Resolved
   2026-08-28** via a full Advanced Research task (Session 1.1 continuation),
   archived at `/docs/research/Pickem_Platform_Account_Limiting_Policy_Research.md`.
   Key findings folded into the roadmap: all three platforms' Terms of Service
   grant broad discretion to limit or close accounts; the widely-cited "~55%
   win rate over 200+ entries triggers Flex-only demotion" claim could **not**
   be corroborated beyond a single affiliate source and should be treated as
   unconfirmed; PrizePicks has the most documented first-hand pattern of
   win-adjacent account closures and withheld withdrawals (BBB/Trustpilot);
   Underdog and DK Pick6 are reputationally more winner-tolerant but this is
   not independently verified. This is reflected in Session 2.6's
   platform-specific sizing risk adjustment (PrizePicks treated as
   cash-out-frequently; Underdog/DK Pick6 as more scalable) and in
   Session 2.1/3.x/4.x/5.x/6.x's legal-footprint checks (state-by-state
   vs.-the-house bans and peer-to-peer alternatives, also documented in the
   same research artifact).
5. ~~Scope the first estimation model concretely.~~ **Deferred to Session 2.3
   by design**, not left abstract — the DFS projection engines were built the
   same way, with the exact input list finalized once real ingested data is in
   hand (Session 2.2), not guessed in advance. Session 2.3's card specifies the
   deliverable at the same detail level as the DFS repos' projection docs.
6. **New, opened Session 1.2:** Liquidity and legal-footprint checks were
   present for the pick'em track (via Decision #4's research) but had only been
   handled narratively, not as explicit session-level checks, for arbitrage,
   weather, politics, and sportsbook props. **Resolved during Session 1.2's own
   review pass** — Sessions 3.2, 4.1, 5.1, and 6.1 now each carry explicit
   liquidity and/or legal-footprint validation checkboxes.
7. **New, opened Session 1.2:** Phase 7's original go/no-go framing treated
   "flagship markets" as a single up-or-down call. **Resolved** — Session 7.0
   now evaluates market structure at the sub-market-type level (per the
   original research finding that market structure, not sport, determines
   efficiency — e.g. Asian handicap soccer vs. that same game's 1X2 market),
   so a genuinely soft sub-market inside an overall-efficient flagship track
   won't be missed by a blanket judgment.

All five of Phase 1's open decisions are now resolved or deliberately deferred
to the specific session where they're actually needed — Phase 1 is fully
scoped. Sessions 2.1 onward are real, buildable session cards; there are no
remaining blockers to starting Phase 2.

---
*Update this file at the close of each future session, per the project's
standing convention: ROADMAP.md and SESSION_LOG.md are only updated once both
sides agree a session is fully closed out, or remaining pieces are being
deliberately deferred to a later session (and that deferral is stated
explicitly, not silently dropped).*
