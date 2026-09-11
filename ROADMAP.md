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
| Fixed-line pick'em platforms | PrizePicks, Underdog (DK Pick6 dropped, Session 2.1 — see below) | Static line set once by platform's own model; fixed-multiplier payout; no live repricing against money flow | **High** | Directly reuses the existing DFS projection-engine pattern — same problem shape (projection vs. fixed number), not a new kind of problem |
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

## Rule for sessions left open across other work (added Session 3.6)

**Real incident this rule exists to prevent:** Session 3.5's complete entry
was dropped from `SESSION_LOG.md`/`ROADMAP.md` because a separate session
closing out a leftover Session 3.4 item produced its own updated copy of
both files, without either session confirming the other's version had
already been committed to GitHub. Both files "looked done," but each was
missing the other's real work — caught and manually reconciled at the start
of Session 3.6 (see that session's entry for the full recovery).

**The actual failure was not a broken prerequisite** — Session 3.4 and 3.5
were sequential, not overlapping. The risk is broader than strict
prerequisites: **any time a session is left open (status other than ✅
Complete or ❌ Blocked) while later sessions proceed — including sessions in
a different phase whose only stated prerequisite is a phase, not the
specific open session** — a future close-out of the open session can start
from a stale copy of these files and silently overwrite real work done in
between.

**Standing rule:** before closing out ANY session (marking it ✅ Complete in
ROADMAP.md), first pull the actual current `SESSION_LOG.md` and
`ROADMAP.md` from GitHub directly — not a copy handed over earlier in a
different chat — and check for any session entries added after the one
being closed. If any exist, merge the closing session's update into that
current version (same reconciliation approach used to fix the 3.4/3.5 gap),
never simply append to a possibly-stale copy.

**Applies now, specifically:** Session 3.6 is being left open (real
sample size not yet reached — see that session's entry). If Phase 4, 5, or
any other session's work happens before 3.6 is revisited, whoever closes
3.6 must pull the live files from GitHub first and check for those sessions'
entries before writing anything, per the rule above.

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
/data <- raw + processed market/event data
/scripts <- all pipeline scripts (per-track subfolders likely, TBD)
/output <- flagged opportunities, sizing suggestions, digest content
/logs <- session log + automation run logs
/docs
/research <- Session 0.1 research artifact archived here
/config <- api_keys.env (gitignored), api_keys.env.example (template), venue configs
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

*Full original build of all five/six layers. PrizePicks and Underdog Fantasy —
reusing the DFS projection-engine pattern for the estimation layer, per
Session 0.1's structural decision. DK Pick6 was originally in scope for this
track but was dropped during Session 2.1 — see that session's card and
Decision #1 below for the full reasoning.*

### Session 2.1 — Data Ingestion Prototype
**Status:** ✅ Complete (2026-08-29) — see SESSION_LOG.md for full detail.

**Prerequisites:** Phase 1 complete.

**What gets built:** A working, non-production script that pulls live
projections from each platform's undocumented public endpoints (confirmed
reachable without login/API key per Session 1.1 continuation research):
- `partner-api.prizepicks.com/projections`
- `api.underdogfantasy.com/beta/v3/over_under_lines`

DK Pick6 was originally in scope for this session (a third prototype script
was built and run), but its endpoint could not be found — no credible public
documentation exists, and a best-guess URL returned a 404. **DK Pick6 was
dropped from Track 1's scope as a result — see Decision #1 below.**

Goal is proof-of-reach and schema discovery, not a production pipeline yet —
confirm each endpoint's real response shape, what fields are present (player,
stat type, line, sport, game time, odds/multiplier type), and how each platform's
schema differs from the others.

**Files touched:** `/scripts/ingestion/prototype_prizepicks.py`,
`/scripts/ingestion/prototype_underdog.py`,
`/scripts/ingestion/prototype_dkpick6.py` (built, ran, endpoint not found —
kept in repo per its own docstring instructions in case DK Pick6 is
reconsidered later),
`/scripts/ingestion/monitor_pickem_endpoints.py` (new — unattended
multi-check monitor built mid-session to gather the day's stability data
without requiring manual re-runs),
`/docs/research/endpoint_schemas.md` (new — documents the actual field-level
schema found per platform, plus the day's monitoring results)

**Validation (required to close session):**
- [x] Both remaining in-scope endpoints (PrizePicks, Underdog) return live
data successfully with no login/key — confirmed both individually and
across 21 unattended checks over ~10 hours with zero failures
- [x] Schema documented per platform (field names, types, what's missing/
inconsistent across platforms) — real field names captured from live
responses for both platforms in `endpoint_schemas.md`
- [x] At least one full day's snapshot captured and saved locally as a sanity
check on stability — ~10-hour unattended monitoring window (21 checks,
30-minute cadence), agreed with user as sufficient in place of a
literal 24-hour window
- [x] Explicit note on what breaks the pull — no failures observed in this
window for either platform; documented as a real finding, with the
caveat that Session 2.2's pipeline still needs real retry/error
handling since both are undocumented endpoints that can change without
notice at any time

**Decisions made:**
1. **DK Pick6 dropped from Track 1's scope.** No credible public documentation
of a Pick6-specific data endpoint exists (unlike PrizePicks and Underdog,
both independently corroborated before this session even started). A
best-guess endpoint, built by analogy to DraftKings' other documented
APIs, returned a 404. Manually reverse-engineering the real endpoint via
browser Developer Tools was possible in principle (documented as a
fallback procedure in `prototype_dkpick6.py`'s own docstring) but offered
no guarantee of success, and risked requiring a logged-in session — which
would break this project's "no login required" design principle for
pick'em ingestion (see Session 0.1 Decision #4 and the account-limiting
research). User explicitly chose to drop it rather than continue
investigating. Track 1 proceeds with two platforms (PrizePicks, Underdog)
instead of three.
2. **A ~10-hour unattended monitoring window, not a literal 24-hour window,
was treated as satisfying the "full day's snapshot" validation item.**
User asked whether a faster option existed; agreed approach was automating
the checks (removing manual re-run effort) rather than shrinking real
elapsed time, since the validation item's actual purpose — proving data
changes over time and surfacing any failure mode — depends on wall-clock
spread, not effort. ~10 hours with 21 checks and zero failures was judged
sufficient; noted as a deliberate, agreed scope decision, not a silent
shortcut.

**Handoff notes:** This session is allowed to be messy/exploratory — it exists to
de-risk Session 2.2, not to produce production code. Session 2.2 onward should
treat Track 1 as a two-platform track (PrizePicks, Underdog) per Decision #1
above.

---

### Session 2.2 — Production Data Ingestion Pipeline
**Status:** ✅ Complete (2026-08-31) — see SESSION_LOG.md for full detail.
**Prerequisites:** Session 2.1 complete.

**What gets built:** A real, scheduled-ready ingestion pipeline that normalizes
both platforms' data into one common schema (matching the "normalized across
books" pattern used by third-party odds aggregators, but built in-house), handles
errors/retries gracefully (since these are undocumented endpoints that can change
without notice — flagged explicitly in Session 2.1's research), and stores
snapshots to `/data`.

**Files touched:** `/scripts/ingestion/ingest_pickem.py` (production version),
`/scripts/ingestion/schema.py` (shared normalized schema),
`/scripts/ingestion/test_ingest_pickem.py` (new — validation harness using
synthetic fixtures, not in the original card; built so pipeline correctness
could be proven without live network access during development), `/data/pickem/`
(new data folder, `raw/` and `normalized/` subfolders), `/logs/ingestion.log`,
`run_ingest.bat` (new — repo-root wrapper script; not a project deliverable
itself, but required for correct scheduled-task execution on Windows, see
Decisions below).

**Validation (required to close session):**
- [x] Pipeline runs end-to-end and produces a normalized dataset across both
platforms — confirmed against real live data: first real run produced
19,891 combined rows (19,667 PrizePicks + 224 Underdog), correctly
joined (real player names, teams, stat types, and lines confirmed by
manual spot-check).
- [x] Handles a simulated failure (bad response, empty response, schema change)
without crashing — logs the failure instead. Confirmed via
`test_ingest_pickem.py` against synthetic fixtures: empty response,
missing top-level schema keys, and a full simulated network failure
(both platforms unreachable) were all handled without raising, each
logged and each producing a valid (if empty) output file.
- [x] Confirmed idempotent (running twice in a row doesn't duplicate/corrupt
data) — confirmed via `test_ingest_pickem.py`: `latest.csv` is fully
overwritten (never appended to) each run, and two runs in a row produce
two distinct, correctly separate timestamped snapshot files rather than
a duplicated or corrupted single file.
- [x] At least 3 consecutive days of real automated pulls captured, reviewed for
consistency — **the literal "3 days" framing was replaced, by explicit
agreement with the user, with an evidence-based standard matching
Session 2.1's own precedent** (see Decisions below): (1) 15+ clean
automated pulls with zero failures, (2) at least one observed material
swing in record counts proving live, non-cached data, and (3) at least
one pull captured near real game-lock times. All three were met: **26
consecutive successful hourly pulls** (2026-08-30 10:09 UTC through
2026-08-31 11:00 UTC) with zero failures; record counts swung from a
peak of 26,538 down to a low of 17,067 (~36% movement); and the
steepest, clearest drop (26,495 → 17,468 between 17:00–21:00 UTC on
8/30) lines up directly with NFL Sunday afternoon kickoff windows in
the user's local time, capturing real props expiring off the board as
games locked — direct evidence the pipeline holds up under genuine
load, not just quiet-hours traffic.

**Decisions made:**
1. **The roadmap's literal "3 consecutive days" validation language was
replaced with an explicit, evidence-based stopping condition** (15+ clean
pulls; a real observed count swing; at least one pull near a real
game-lock event), agreed with the user rather than followed as a default.
Reasoning, recorded plainly: this session's validation question is
pipeline *reliability* (does it break under real repeated use?), not a
statistical sample-size question — that distinct question belongs to
Session 2.5 (Sample-Size Thresholds), which will use real math once real
flag-frequency data exists. Importing that rigor into this session would
have been both unnecessary and dishonestly precise. This same
"elapsed-time-as-default vs. evidence-based stopping condition" pattern
was already set by Session 2.1 (which replaced a literal 24-hour window
with ~10 hours plus 21 zero-failure checks); this decision applies the
same principle a second time, now stated as a reusable standard rather
than re-derived from scratch.
2. **A Windows scheduled-task path bug was found and fixed during this
session** — worth recording as a real finding, not just a footnote. The
first scheduled-task attempt failed silently overnight (`Last Result:
-2147024894` — "the system cannot find the file specified") because the
task's non-interactive execution context could not resolve the bare
`python` command the way an interactive PowerShell session does.
Diagnosed by checking `(Get-Command python).Source`, which revealed the
interactive shell was resolving to the unreliable Microsoft Store stub
at `WindowsApps\python.exe` — not a real interpreter, and known to behave
inconsistently outside interactive use. Fixed by pointing the task at the
real interpreter (`C:\Users\gmsco\AppData\Local\Python\pythoncore-3.14-64\python.exe`)
via a new wrapper file, `run_ingest.bat`, placed at the repo root. The
wrapper also explicitly `cd`s into the repo root before running Python,
closing a second latent risk: `schtasks` has no dedicated
working-directory flag, and the pipeline's own file paths are relative to
the repo root, so a scheduled task launched from a different default
directory (commonly `C:\Windows\System32`) could otherwise have written
output to the wrong place or failed to find its own folders. This is the
kind of undocumented-environment failure mode Session 8.4 (Ingestion
Health Monitoring) exists to catch more generally later — noted here as a
real, concrete precedent for that future session, not just a one-off fix.
3. `%USERNAME%` does not reliably expand inside `schtasks /ru` — confirmed
directly (`ERROR: No mapping between account names and security IDs was
done`). Dropping `/ru` entirely and letting the task default to the
currently logged-in user resolved this. Worth remembering for any future
Windows Task Scheduler use in this project.

**Corrections/reversals during the session:**
1. **First scheduled task, created without a working-directory-safe wrapper
and pointed at the bare `python` command, silently failed overnight with
zero data collected.** Corrected per Decision #2 above. The original
overnight window (5:00 PM–5:00 AM) is not counted toward this session's
validation — the clock was explicitly restarted once the fix went in at
10:09 UTC on 8/30, and only pulls from that point forward are counted in
the 26-pull total above.

**Handoff notes:** Track 1's ingestion layer is now production-grade and
validated under real, repeated, automated use — including one real
operational failure mode found and fixed along the way, which is itself
useful signal for Session 8.4 later. Next session is Session 2.3 —
Estimation Engine v1, which can now be built and tested against real
accumulated ingested data rather than synthetic fixtures.

---

### Session 2.3 — Estimation Engine v1
**Status:** ✅ Complete (2026-08-31) — see SESSION_LOG.md for full detail.
**Prerequisites:** Session 2.2 complete (needs real ingested data to build/test
against).

**What gets built:** The actual projection model — a weighted blend of specific,
named inputs (matching the DFS projection-engine pattern), producing a probability
estimate for each prop's over/under outcome, then comparing that estimate against
the platform's fixed line. This is where **Open Decision #5** gets resolved for
real, with concrete inputs named (e.g., recent performance window, opponent
matchup factor, injury/role status, home/away, pace/usage where applicable) —
exact input list to be finalized with real data in hand, not guessed in advance.
**Scoped to NFL only for v1** (see Decisions below) — the other five sports
present in real ingested pick'em data are a stated gap, not a silent one.

**Files touched:** `/scripts/estimation/pickem_model.py`,
`/docs/research/pickem_estimation_model_spec.md` (new — documents exact inputs,
weights, and reasoning, same detail level as the existing DFS projection docs)

**Validation (required to close session):**
- [x] Model produces a probability estimate for every ingested prop, not just a
subset — **met with agreed v1 scope**: every one of 20,861 real ingested
props gets a row with an explicit status in the model's output (nothing
silently dropped); every NFL prop with a supported stat type gets a real
numeric probability estimate. Non-NFL sports (85% of real volume) and 3
stat types nflverse has no matching data for at all are the stated v1
boundary — confirmed acceptable by the user for v1.
- [x] Model's estimate is sanity-checked against a handful of manually-reasoned
examples (does the model agree with obvious cases?) — confirmed two ways:
(1) against real 2025 QB passing-yards props, modeled probability moved
in the correct direction as the platform's line increased, across every
tested case; (2) the two computed-formula stat types (Kicking Points,
Fantasy Score) were independently hand-recomputed from raw nflverse data
outside the model's own code and matched the model's real output exactly
for real players (Harrison Butker, Patrick Mahomes).
- [x] Model's inputs and weighting logic are documented at the same specificity
as the DFS repos' projection engines — no unnamed "black box" factors —
confirmed in `pickem_estimation_model_spec.md`, including exact source
citations for the two PrizePicks scoring formulas used.
- [x] Explicit note on what's NOT yet included (e.g. weather for outdoor sports,
Vegas team totals) and why, so it's a stated gap, not a silent one —
confirmed: non-NFL sports, unmapped stat types, no opponent/matchup/
injury/home-away/pace/weather adjustment, and the PrizePicks
implied-probability assumption are all named explicitly in the spec doc,
each with the reason it's excluded rather than guessed at.

**Decisions made:**
1. **v1 scoped to NFL only**, using nflverse's public weekly player-stats
data (no API key required — same source DFS_Optimizer already uses) as
the external performance source. Against a real live run of 20,861
ingested props, 85% were non-NFL sports; those get a real, visible
`model_status="unsupported_sport"` row rather than being silently
skipped or force-fit to a sport with no real data source wired in yet.
Confirmed acceptable to the user for v1.
2. **Two inputs only: season average and recency-weighted recent form,
blended 50/50.** Mirrors DFS_Optimizer's own first-pass projection
pattern (`projections_baseline.py`). The 50/50 blend weight is a
deliberate, simple starting point, not a tuned number — re-weighting it
against real graded results is explicitly deferred to Session 8.3
(Ongoing Recalibration Cadence), once Sessions 2.4/2.5 produce real CLV
and outcome data to tune against.
3. **Player-name matching bug found and fixed before handoff.** nflverse's
weekly-stats release has two name columns — `player_name` (abbreviated,
e.g. "P.Mahomes") and `player_display_name` (full form, e.g. "Patrick
Mahomes"). The model was initially built against the wrong one, which
would have silently produced a `no_player_match` result for nearly every
real row. Checked directly against a live pull before this was handed
off, not assumed — caught and fixed, not discovered later as a bug.
4. **Stat-type coverage was built entirely from real ingested data, not
guessed in advance.** A first real run against 20,861 live props
surfaced 1,650 NFL props with an unrecognized `stat_type` string. Each
real string was checked individually against nflverse's actual column
list before any mapping decision: 10 stat types were mapped from
existing simple/composite nflverse columns (1,096 rows); 2 more
(`Kicking Points`, `Fantasy Score` — 138 rows) required real scoring
*formulas*, confirmed against PrizePicks' own official sources (see
Decision #5); 3 (`Longest Rec`, `Longest Completion`, `Longest Rush` —
416 rows) were left deliberately unsupported because nflverse has no
per-game "longest play" data of any kind to map them to.
5. **Kicking Points and Fantasy Score formulas confirmed against
PrizePicks' own official sources, not assumed.** Kicking Points:
confirmed via PrizePicks Support's own reply on X
(`x.com/PrizeSupport/status/1963792635933434257`) and PrizePicks' own
scoring page — field goals are tiered by distance (0–39 yds = 3 pts,
40–49 yds = 4 pts, 50+ yds = 5 pts), PAT made = 1 pt, a missed FG or PAT
= −1 pt each, and PrizePicks' own page states this is explicitly not the
same stat as Fantasy Score. Fantasy Score: confirmed via the same
official page — full-PPR-style scoring across passing/rushing/receiving
yards, TDs, interceptions, receptions, fumbles lost, and 2-point
conversions. The Fantasy Score formula deliberately omits two rare
6-point components (Offensive Fumble Recovery TDs, Kick/Punt/FG Return
TDs) because nflverse's closest-named column for return TDs
(`pt_return_tds`) was checked directly against real 2025 data and found
to fire on punters, not the players who actually returned a kick — using
it would have produced a wrong number with false confidence. Left out
and documented rather than guessed around; both omitted events are rare
(well under 1% of player-games per season).
6. **Real player-match rate of 96.6%** (2,525 estimated out of 2,663 NFL
props with a supported stat type) was confirmed against live data and
judged sufficient for v1 by the user — no further name-matching work
planned before Session 2.4.
7. **Model run against `--season 2025` for now, with switching to 2026 data
explicitly deferred** (see new Open Decision #9) — nflverse's 2026
season release does not exist yet (confirmed directly, returns 404 as of
2026-08-31: the 2026 NFL season's first games are 2026-09-07, and
nflverse only publishes a season's file once real games from it have
been played).

---

### Session 2.4 — CLV-Equivalent Calibration Logging

**Status:** ⚠️ Complete with caveats (2026-09-01) — see SESSION_LOG.md for full detail.
**Prerequisites:** Session 2.3 complete.

**What gets built:** The pre-outcome validation layer — for every flagged
opportunity, log the model's estimate alongside a benchmark at flag time, then
track how that comparison moves before the event resolves. Built as
`clv_logger.py`, logging TWO distinct benchmarks side by side rather than one
blended number: (1) cross-platform consensus (the same real prop's price on the
other platform, at flag time, when available) and (2) own-line movement to
close (the prop's own last-seen price before it drops off the board). Neither
is literal sportsbook CLV — Session 0.1 already established PrizePicks/
Underdog run static, non-repricing lines, so a platform's own price not moving
is not itself evidence of anything.

**Files touched:** `/scripts/calibration/clv_logger.py`,
`/scripts/calibration/test_clv_logger.py` (new — synthetic-fixture validation
harness, not in the original card, built for the same reason Session 2.2's
test harness was), `/docs/clv_methodology.md`,
`/scripts/estimation/pickem_model.py` (small additive change — see Decision #4
below), `/data/pickem/clv_log.csv`, `/data/pickem/clv_snapshots/`.

**Validation (required to close session):**
- [x] Every flagged opportunity from Session 2.3's model gets a CLV-equivalent
entry logged automatically — confirmed on real live data: 3,205 total
flags logged across a ~17-hour real validation window
(2026-08-31 17:39 UTC – 2026-09-01 09:42 UTC), zero pipeline failures.
- [x] Logging captures both the flag-time estimate and a real benchmark
comparison — confirmed: both cross-platform consensus and own-line
movement-to-close are logged on every row, explicitly labeled and never
blended.
- [x] At least one real window of logged data collected and reviewed for
completeness — the roadmap's original "one real week" framing was
replaced with four explicit, evidence-based conditions, agreed directly
with the user (same correction pattern as Sessions 2.1/2.2): 15+ new
flags (met — 3,205), 3+ closed (met — 272), zero pipeline failures
(met), and 1+ closed flag with a real consensus match.
- [ ] 1+ closed flag with a real cross-platform consensus match — **NOT MET,
explicitly deferred, not failed.** Root cause confirmed directly against
live data: Underdog has posted zero real NFL lines as of 2026-09-01
(real NFL season starts 2026-09-07); Track 1's model is NFL-only in v1
scope. This is an external, calendar-driven fact, not a code defect —
the consensus-matching logic itself is confirmed correct against
synthetic data (`test_clv_logger.py`). See Open Decision #10 below for
the re-verification trigger.
- [x] Log format is durable/queryable — confirmed: `clv_log.csv` is a single,
fully-overwritten CSV per run (never appended-and-duplicated), plus a
timestamped snapshot per run in `clv_snapshots/`, matching Session 2.2's
own snapshot pattern. A future session can query "all flags from the
last N days" directly against the snapshot folder or filter the main
log's timestamp columns, with no custom one-off code needed.

**Decisions made:**
1. `FLAG_EDGE_THRESHOLD = 0.03` (a model probability at least 3 percentage
points from the platform's own implied probability) — a stated,
unvalidated placeholder, confirmed with the user before the live
validation run rather than tuned blind. Re-deriving this against real
graded results remains Session 8.3's job (Ongoing Recalibration Cadence).
2. Two distinct benchmarks logged side by side (cross-platform consensus;
own-line movement to close), never blended into one number —
deliberately, so Session 2.5 onward can determine which one, if either,
actually correlates with real graded outcomes.
3. The roadmap's original "one real week" validation duration was replaced
with four explicit, evidence-based conditions and a ~17-hour target
checkpoint (matching Session 2.2's own real validation window), agreed
directly with the user — the third time this project has applied the
"elapsed-time-as-default → evidence-based standard" correction (after
Sessions 2.1 and 2.2).
4. `pickem_model.py` (Session 2.3's file) received one small, additive
change: a new `resolved_stat_key` output column, giving `clv_logger.py`
a reliable, exact-match way to recognize the same real prop across both
platforms (raw `stat_type` wording differs by platform; the canonical
resolved stat does not). No existing column, calculation, or behavior
changed.
5. Given the confirmed external root cause, Session 2.4 was closed now
rather than delayed several more days for Underdog to post real NFL
lines. Live confirmation of cross-platform consensus matching on real
NFL data is explicitly deferred — see Open Decision #10.
6. A real, separate data-quality gap found during this session's
investigation (Underdog's appearances→games join only resolved for 41%
of real records checked) was deliberately NOT fixed this session, since
there is no real NFL data yet to test a fix against, and fixing it blind
risks false confidence. See Open Decision #11.

**Handoff notes:** The CLV logger itself is fully built and proven reliable on
real live PrizePicks data. The one piece not yet provable — cross-platform
matching against real NFL data — cannot be proven until Underdog itself posts
real NFL lines, which is outside this project's control. Session 2.5 does not
need to wait on this, but Open Decisions #10 and #11 should be revisited as
soon as real NFL data appears on Underdog (expected on or shortly before
2026-09-07), independent of whichever session is active at that time.

---

### Session 2.5 — Sample-Size Thresholds & Realized-Outcome Tracking
**Status:** ✅ Complete (2026-09-01) — see SESSION_LOG.md for full detail.
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
`/scripts/calibration/weekly_review.py` (new — not in the original card;
added mid-session once the user redesigned this session's approach from a
one-time gate to a recurring cadence, see Decision #2 below),
`/data/pickem/outcome_log.csv` (new — separate from `clv_log.csv`),
`/data/pickem/review_log.csv` (new — not in the original card, holds
`weekly_review.py`'s permanent review history),
`/scripts/estimation/pickem_model.py` (docstring-only correction, see
Decision #3 below — no logic changed),
`/docs/clv_methodology.md` (new section added, same correction)

**Validation (required to close session):**
- [x] Sample-size threshold calculated and documented with the reasoning
shown — real breakeven (≈57.7%, sourced from PrizePicks' own
published 2-pick Power Play payout) and real target sample (≈3,725
graded legs), full derivation in `sample_size_methodology.md`.
- [x] Outcome tracker can accept a manually-reported bet result and store
it durably, linked to the CLV log — confirmed on real data: recorded
real graded outcomes against two actual `flag_id`s from the live
`clv_log.csv` (`prizepicks|13961517`, `prizepicks|14252061`), both
correctly pulled real context by `flag_id` lookup. `--pending`
correctly reported 3,205 of 3,207 real flags still ungraded.
- [x] Confirmed the two logs (CLV and outcome) can be joined/compared
later — confirmed on real data via `weekly_review.py --report`,
which joins `outcome_log.csv` against `clv_log.csv` on `flag_id` and
reports win rate alongside the breakeven and full-sample references.

**Decisions made:**
1. **Sample size treated as a recurring weekly review, not a one-time gate.**
The original card implied validating once the full ≈3,725-leg threshold
is reached. User redirected this mid-session: build to "a reasonable
working point," then run an indefinite recurring review (weekly, by
user's explicit choice) that gets more accurate over time as more real
data accumulates, rather than blocking all progress on one large number.
`weekly_review.py` implements this: a 30-leg interim floor (mirroring
Session 2.4's own "15+ flags" reporting minimum) below which no
recalibration recommendation is given; above it, every review reports
real numbers next to both fixed reference points (57.7% breakeven,
3,725-leg full threshold) so a provisional read is never visually
confused with a statistically solid one.
2. **This pulls part of Session 8.3's job forward.** Session 8.3 ("Ongoing
Recalibration Cadence") was scoped to wait for Phase 8 (2+ live tracks)
because a *cross-track* cadence needs multiple tracks to be meaningful.
A *single-track* weekly review has no such dependency and starts now.
Session 8.3's own card should build on this single-track review, not
start from a blank design, once Phase 8 begins.
3. **Real correction found and resolved: the flat 50% "implied probability"
used for PrizePicks rows (Session 2.3) was being confused with — and
should never be confused with — the real, entry-type-specific breakeven
win rate (57.7% for a 2-pick Power Play) this session derived.** These
answer two different questions: 50% is a flagging-sensitivity
threshold, chosen before any entry type is known; 57.7% is the real
breakeven for one specific, named entry type, only meaningful once an
entry type is actually chosen (Session 2.6's job). No code changed —
`pickem_model.py`'s docstring and `clv_methodology.md` were both
updated to state this distinction explicitly, closing a real point of
confusion rather than leaving it to cause the same question again in a
future session.
4. **Two placeholder outcome records used during real-data testing must
not be treated as real results.** The two `flag_id`s recorded during
this session's validation (`prizepicks|13961517`,
`prizepicks|14252061`) belong to props whose games have not been played
yet (2026-09-09 kickoff) — the win/loss values used were arbitrary,
solely to prove the pipeline works end-to-end. These were recorded only
in Claude's own sandbox test copy, not pushed to the real repo — the
user's real `outcome_log.csv` does not yet exist and starts clean.

**Handoff notes:** This session also formalizes something implicit until
now: **this system flags and sizes opportunities for the user to act on
manually — it does not place bets itself.** That's a deliberate design
decision, not a gap: consistent with this environment's restriction
against Claude executing financial trades or transfers on a user's behalf,
and because the whole point of the outcome tracker depends on the user
reporting what they actually did, which may reasonably differ from what
the system suggested. Real bet placement and the first live weekly review
did not happen this session (no real bets exist yet to grade) — this is
expected, ongoing usage rather than a deferred validation item, since the
weekly review is designed to run indefinitely, not to gate this session's
close. Next session is 2.6 — Bankroll & Sizing Logic, which is also where
the real, entry-type-specific breakeven math (Decision #3 above) actually
gets applied for the first time.

---

### Session 2.6 — Bankroll & Sizing Logic
**Status:** ✅ Complete (2026-09-01)
**Prerequisites:** Session 2.5 complete (sizing should only apply to
CLV-validated opportunities, not raw model output).

**What gets built:** Position-sizing logic (a fractional-Kelly-criterion
approach, consistent with what professional sports bettors use) that turns
a flagged, CLV-validated opportunity into a concrete suggested stake,
factoring in account-limiting risk per platform (from the Session 1.1
continuation research — PrizePicks treated as "cash out frequently, assume
elevated closure risk," Underdog treated as more scalable).

**What actually gets built (v1 scope, resolved this session):** v1 sizes
exactly one real, sourced entry shape — a PrizePicks 2-pick Power Play
(3x payout, per Session 2.5's own sourced number) — combining two open
flags from `data/pickem/clv_log.csv`. No other entry size (3-pick, 4-pick,
Flex) or Underdog entry type has a confirmed real payout multiplier
anywhere in this project's research yet, so `sizing_engine.py` explicitly
rejects any other combination rather than guess at an unsourced number —
a stated v1 boundary, matching Session 2.3's own NFL-only scoping pattern,
not a silent one.

**Files touched:** `/scripts/sizing/sizing_engine.py`,
`/scripts/sizing/test_sizing_engine.py` (new — not in the original card;
built for the same reason Session 2.2/2.4/2.5's own test harnesses were,
since this sandbox cannot reach the real repo's live `clv_log.csv`),
`/docs/sizing_methodology.md`

**Validation (required to close session):**
- [x] Sizing logic produces a concrete stake suggestion for every
CLV-positive flagged opportunity — confirmed against real, live
`clv_log.csv` data pulled directly from GitHub: three real flag
pairs produced a $25.00 capped stake, a $69.85-uncapped-then-capped
stake, and a $3.48 uncapped stake respectively, plus a fourth real
pair (below the true combined-probability breakeven) correctly
produced `status: no_bet_negative_edge` and a $0 stake — never a
negative number.
- [x] Platform-specific risk adjustment is present and documented — a
named `PLATFORM_RISK_MULTIPLIER["prizepicks"] = 0.70` dampener is
applied and visible in every real output; Underdog's own multiplier
is present in the code for future use but is gated off entirely
(rejected with an explicit reason) since no real Underdog payout
number has been sourced yet.
- [x] Sanity-checked against a few manual examples (does a bigger edge
produce a bigger suggested stake, within sane bounds?) — confirmed
on real live data: suggested stake rose from $0 (combined
probability 0.293, below the true 1/3 breakeven for a 2-pick entry)
to $3.48 (combined probability 0.365) to $25.00-capped (combined
probability 0.959–0.988), monotonic across every real pair tested.
Every Kelly-formula intermediate value was independently hand-
verified against the code's own output before being accepted (see
Decisions below).
- [x] Explicit bankroll cap / max-single-position rule stated and enforced
in code, not just described in docs — `MAX_SINGLE_POSITION_PCT =
0.05` is enforced directly in `size_entry()`, not left as a
documentation-only rule; hit twice on real live data (both
correctly capped at exactly $25.00 on a $500 bankroll, 5%), never
exceeded.

**Decisions made:**
1. **v1 scoped to exactly one entry type — a PrizePicks 2-pick Power
Play** — reusing Session 2.5's own sourced 3x payout number, rather
than guessing at a multiplier for any other entry size or for
Underdog. Every other leg-count/platform combination is rejected with
an explicit, stated reason. Extending coverage is a named candidate
for a future session, not built here.
2. **Sizing uses fractional Kelly, not full Kelly.**
`KELLY_FRACTION = 0.25` (quarter-Kelly) is applied to the raw Kelly
fraction before any other adjustment — standard, conservative practice
given this project's own model has no opponent/injury/pace adjustment
yet (a stated v1 gap since Session 2.3) and Session 2.4's edge
threshold is itself an unvalidated placeholder. Discussed directly
with the user and confirmed as the right v1 starting point — full
Kelly assumes the probability input is exactly correct, which this
model does not claim to be.
3. **`PLATFORM_RISK_MULTIPLIER["prizepicks"] = 0.70` is a stated,
unsourced judgment call, not a derived number**, applied on top of
quarter-Kelly to reflect the Session 1.1 continuation research finding
that PrizePicks has the most documented first-hand pattern of
win-adjacent account closures and withheld withdrawals. No source
gives a specific dampening figure, so 0.70 is named explicitly as a
placeholder — discussed directly with the user, who agreed to accept
it as-is for v1 rather than delay the session chasing a number this
project's research cannot currently justify. Revisiting it against
real graded results remains Session 8.3's job, same as
`FLAG_EDGE_THRESHOLD` and Session 2.5's `p1 = 0.60`.
4. **A same-game caution dampener was added mid-session, at the user's
direction, after a discussion of same-game correlation risk.**
`SAME_GAME_CAUTION_MULTIPLIER = 0.85` applies whenever both requested
legs share the same real `game_id`, and is reported explicitly in the
output (`same_game_pair`, `same_game_caution_multiplier_applied`) —
never a silent adjustment. This was a deliberate "flag it as riskier,
don't pretend to model it precisely" choice: this project has no real
data on how strongly, or in which direction, same-game legs actually
correlate, and manufacturing a precise correction would mean sizing
real money off a guess. Confirmed on real live data — the same real
flag pair's uncapped stake moved from $15.15 to $12.88 once the flag
applied, and both real capped-example pairs also correctly showed
`same_game_pair: True`. Re-deriving this multiplier (or replacing it
with real correlation modeling) is a named future candidate, not
built here.
5. **The bankroll cap (`MAX_SINGLE_POSITION_PCT = 0.05`) is a hard
ceiling applied after every other adjustment**, so a large modeled
edge — even a combined probability above 95%, as seen twice on real
data this session — cannot produce an unreasonably large single-entry
suggestion.

**Corrections/reversals during the session:**
1. **A predicted "no-bet" test case turned out to be a real, small
positive-edge case instead.** While walking through a manual
prediction for a real flag pair (Drake Maye's two different Pass+Rush
Yards lines), Claude initially predicted the combined probability
would fall below the 57.7% per-leg breakeven and produce a $0 stake —
an error, since 57.7% is the *per-leg* breakeven, not the *combined*
two-leg breakeven (which is 1/3 ≈ 33.3% for a 3x-payout 2-pick entry).
The real combined probability (0.365) was actually above 1/3, and the
script correctly returned a small positive stake ($3.48), not a $0
result. Caught and corrected in the same turn, with the corrected math
shown against the real output rather than silently moved past — a
genuinely useful real-data test of the small-positive-edge path that
the original (mistaken) prediction would not have produced.

**Handoff notes:** The sizing engine is built, tested against 8 synthetic
scenarios (including the same-game dampener added mid-session), and
proven against multiple real flag pairs pulled directly from the live
`clv_log.csv` — covering the capped path, the uncapped small-edge path,
and the no-bet path, plus the same-game caution flag on real same-game
data. `KELLY_FRACTION`, `PLATFORM_RISK_MULTIPLIER`, and
`SAME_GAME_CAUTION_MULTIPLIER` are all explicitly stated placeholders,
confirmed acceptable to the user for v1, and named as candidates for
Session 8.3's recalibration work once real graded outcomes exist to check
them against. Next session is Session 2.7 — Automation (GitHub Actions).

---

### Session 2.7 — Automation (GitHub Actions)
**Status:** ✅ Complete
**Prerequisites:** Session 2.6 complete.

**What actually got built:** Scheduled automation that runs ingestion →
estimation → CLV logging on an hourly schedule, then writes a digest of
currently open flagged opportunities. Sizing (`sizing_engine.py`) is
deliberately **not** part of the automated run — see Decision #1 below;
this is a real, deliberate deviation from the card's original "ingestion
→ estimation → CLV logging → sizing" description.

**Files touched:** `.github/workflows/pickem_pipeline.yml` (new),
`/scripts/run_pipeline.py` (new, orchestrator), `/output/digest/` (new),
`/requirements.txt` (modified — added `pyarrow`)

**Validation (required to close session):**
- [x] Workflow runs successfully on GitHub Actions' own infrastructure (not just
locally) at least 3 times on schedule — 4 confirmed real "Scheduled"-
trigger runs (#5–#8), all green, all producing real auto-commits.
- [x] Failure in one step (e.g. ingestion) doesn't silently corrupt downstream
steps — pipeline fails loudly and logs why — proven twice for real, not
just by design: a `ModuleNotFoundError` (run #1) and a missing-dependency
error (run #2) each stopped the pipeline before CLV logging ran, and
`clv_log.csv` was correctly left untouched both times.
- [x] Digest output is complete and matches what a manual run would produce —
confirmed against real overnight data: 30,373 real props ingested, 126
newly flagged, real September NFL game dates.
- [x] Secrets (if any needed) are handled via GitHub Actions secrets, not
committed anywhere — no secrets needed at all (PrizePicks/Underdog
endpoints are unauthenticated); trivially satisfied.

**Handoff notes:** GitHub's scheduled ("cron") trigger took real, extended
troubleshooting to get firing at all — see SESSION_LOG.md for the full
trail. Once firing, observed gaps between scheduled runs were **2h16m,
4h19m, and 5h9m — not the intended hourly cadence.** This looks like
GitHub's documented behavior of delaying/coalescing scheduled triggers
under load, not a bug in this workflow; the validation checkbox above is
satisfied on its literal terms (3+ real scheduled runs), but **actual
cadence should not be assumed to be hourly** until observed over a longer
window. Worth revisiting once NFL season data volume ramps up (season
starts ~Sept 7) and freshness starts to matter more.

---

### Session 2.8 — Frontend (Cloudflare Pages)
**Status:** ✅ Complete
**Prerequisites:** Session 2.7 complete (needs real automated output to display).

**What actually got built:** A Cloudflare Pages frontend, no framework, matching
the DFS repos' static-file pattern, displaying current flagged opportunities, a
corrected running-average CLV-performance trendline (the "S&P 500 chart" north
star from ROADMAP.md), and an interactive sizing calculator. The calculator is
a real, deliberate deviation from this card's original "sizing suggestions"
description — see Decision #1 below and SESSION_LOG.md's Session 2.8 entry for
full reasoning: it mirrors `sizing_engine.py`'s actual manual, per-entry design
(exact math ported to JavaScript and verified against the Python original)
rather than inventing automated per-flag sizing output that nothing else in the
project's design supports.

**Files touched:** `/frontend/index.html`, `/frontend/style.css`,
`/frontend/app.js` (all new), Cloudflare Pages project `market-betting`
(dashboard configuration, connected to `main`, auto-deploys on every push)

**Validation (required to close session):**
- [x] Frontend deploys successfully and is reachable at a live URL —
`https://market-betting.pages.dev`
- [x] Displays current flagged opportunities pulled from real automated output,
not mock data — row counts confirmed to exactly match the real
`clv_log.csv` (3,856 total rows)
- [x] Displays a CLV-performance trendline view — corrected mid-session from a
meaningless raw-sum metric to a running-average metric; see
SESSION_LOG.md
- [x] Confirmed working on both desktop and mobile view

**Decisions made:**
1. Sizing is shown via an **interactive client-side calculator**, not
automated per-flag output — this mirrors `sizing_engine.py`'s real,
deliberate design (manual, per-entry, no persisted bankroll) rather
than inventing new automation (a leg-pairing strategy) that doesn't
exist anywhere else in the project. Bankroll is never persisted
anywhere; it resets when the browser tab closes.
2. Cloudflare Pages projects for this repo must be created via the
dashboard's **"Continue to Pages" → "Import an existing Git
repository"** path, not the newer unified "Create application" flow —
the unified flow silently produces a Worker instead of a Pages
project for a plain static site. Recorded here as a standing gotcha
for any future sibling-project Cloudflare Pages setup.
3. The trendline and its headline stat use a **running average** of
per-flag CLV edge, not a running sum — a sum grows without bound as
more flags close and stops representing anything real; the average is
what actually answers "is this system right more often than chance,"
which is the roadmap's stated north star.

**Handoff notes:** See SESSION_LOG.md's Session 2.8 entry for the full build
trail, including the Cloudflare Worker-vs-Pages mixup and the trendline-metric
bug both found and fixed mid-session, and the sizing calculator's math-parity
verification. Next session is Session 2.9 — Live Paper-Trading Validation
Window.

---

### Session 2.9 — Live Paper-Trading Validation Window
**Status:** ⚠️ Complete with caveats (2026-09-09) — explicit **NO-GO** decision
recorded. See SESSION_LOG.md for full detail.
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
- [x] Sample-size threshold from Session 2.5 reached, for both CLV entries and
real reported outcomes — **partial:** the CLV-close threshold (≈3,725)
is cleared (3,845 real closed flags as of 2026-09-09); the real-outcome
threshold is **not** cleared — `outcome_log.csv` does not exist, zero
real bets have been reported.
- [x] Real graded CLV performance reviewed — does it show the "positive
trendline with real drawdowns" pattern the project's north star describes,
or not? — reviewed; see SESSION_LOG.md. Own-line-movement signal only
(cross-platform consensus has never fired); this proxy cannot answer
the win-rate question the north star is about.
- [ ] Real reported outcomes (not just CLV) reviewed against the same standard,
and checked for directional agreement with the CLV signal — **not met**,
no real outcomes exist yet. User has deliberately chosen not to place
real bets until confidence is established — see SESSION_LOG.md.
- [x] Explicit go/no-go decision recorded: is Track 1 (pick'em) validated enough
to consider real capital, or does it need another iteration on the
estimation model first? — **NO-GO for real capital**, explicitly because
there is no real graded outcome data yet, not because of any negative
signal found in the CLV data. See SESSION_LOG.md for full reasoning.
- [x] If no-go: specific, named reasons documented (not just "didn't work") so
the next session knows what to fix — see SESSION_LOG.md.

**Handoff notes:** This is the checkpoint the whole "no guarantees ≠ lower bar"
rule exists for. A session that fails this validation is not a failed project —
it's the system doing exactly what it's supposed to do before capital is at risk.
**This session closed on a NO-GO, for a specific, narrow reason: no real bet has
ever been placed and reported, so there is no real outcome data to grade against
the CLV proxy.** This is not a finding that the model is bad — it is a finding
that the one piece of evidence this checkpoint actually needs (real graded
results) does not exist yet. Re-opening this checkpoint is straightforward once
that changes: the user places a small number of real test bets, reports each
result via `outcome_tracker.py --record`, and once enough real graded legs
accumulate, `weekly_review.py --run` becomes runnable and this checkpoint can be
re-evaluated for real. See Open Decision #22 (new) for the exact re-trigger.

---

### Session 2.10 — Cross-Sport +EV Inventory (Track 1)
**Status:** ✅ Complete, with one validation item deferred to a bounded,
automated follow-up — not a new numbered session. See SESSION_LOG.md for
the full write-up and `/docs/research/sport_inventory.md` for the
complete findings. Closing the deferred item (Underdog's full sport
list) is expected in early-to-mid September 2026, once
`.github/workflows/sport_inventory_scan.yml`'s 4-day scheduled run
window ends — see that section of SESSION_LOG.md for the exact plan.
**Prerequisites:** Session 2.9 (continuation) complete — real per-row
visibility (`output/estimation/latest.csv`) and correct sport/stat-name
resolution for both platforms are in place.

**Why this exists:** Addresses Open Decision #14. This project's stated scope
is +EV bets across all betting markets, not one or two sports. Track 1's
model has been NFL-only since Session 2.3's scoping decision, and repeated
investigation this session kept narrowing back to individual sports (first
NFL, then "add Tennis and CFB") rather than asking the actual right
question — this session exists to ask it properly, once, deliberately.

**What gets built:** No estimation code yet — this is an inventory and
scoping session, the same spirit as Session 2.3's original model-scoping
work. For every sport currently live on PrizePicks and Underdog (checked
live, not from memory or assumption):
- What real sports are actually listed right now (both platforms, pulled
live)
- For each: does a real, current public data source exist to grade it
against? (`nflverse` only covers NFL — MLB, Tennis, and CFB each need
their own answer, not yet researched)
- Which are structurally close to workable now (a per-game stat, a public
stats API or scrapeable source) vs. genuine build-outs (no public data
source, or a fundamentally different market structure)

**Files touched:** `/docs/research/sport_inventory.md` (new — the actual
inventory and per-sport findings), possibly `ROADMAP.md` if new sessions need
to be added for whichever sports turn out workable.

**Validation (required to close session):**
- [x] Every sport currently listed on PrizePicks confirmed live (not assumed
from a past session) — 29 leagues confirmed via a live pull
- [ ] Every sport currently listed on Underdog confirmed live (not assumed)
— **deferred, with a real automated mechanism now running** (see
"Handoff notes" below), not left open-ended
- [x] For each sport found: a real, named answer on data-source availability
(found and confirmed, or confirmed not to exist — not left unchecked)
— includes the long tail, not just the largest sports
- [x] At least MLB explicitly checked, since it's mid-season right now and
was missed entirely this session despite being a live, obvious
candidate
- [x] Clear, named list of which sports are candidates for near-term
estimation-model support vs. which require real build-out vs. which
are ruled out, with reasoning for each

**Handoff notes:** The point of this session is to stop this track's scope
from silently narrowing to whichever sport is easiest to see at the moment.
A sport being ruled out here (no viable data source, market structure
doesn't fit) is a legitimate, useful outcome — the failure mode this session
guards against is a sport never being checked at all.

**Deferred item — real mechanism, not a vague TODO:** confirming Underdog's
full sport list turned out to require genuine time-of-day/day-of-week
spread that can't be produced in one sitting (checked directly — no
sports-catalog endpoint exists on Underdog's API as a shortcut). A
GitHub Actions workflow (`.github/workflows/sport_inventory_scan.yml`)
now runs the scan 3x/day for 4 days (12 runs) automatically, writing
dated results to `docs/research/scans/`, verified working end-to-end via
one real manual run before being left unattended (see SESSION_LOG.md for
that verification). When the window ends: read the accumulated files,
build the real union list, update `/docs/research/sport_inventory.md`,
and disable the workflow — it's explicitly temporary.

**Also produced this session, beyond the original scope (see
SESSION_LOG.md for full detail):** a product-scope finding that both
PrizePicks and Underdog now offer products beyond fixed-line pick'em
(PrizePicks Predict is a direct Kalshi partnership; Underdog Exchange is
a separate CFTC-regulated exchange). This was investigated and a
recommendation reached (Track 3's existing scope and ranking should
stand as-is — see SESSION_LOG.md's reasoning, which re-applied Session
0.1's own five ranking criteria against real, newly-gathered evidence
rather than treating the new data as automatic grounds for rescoping).

---

### Session 2.11 — Underdog Payout Multiplier & Sizing Support (Pick'em)
**Status:** ⚠️ Complete with caveats (2026-09-10) — see SESSION_LOG.md for
full detail. Underdog's real 2-pick payout is sourced and wired into both
`sizing_engine.py` and the frontend; regression-tested against real
PrizePicks data and a synthetic Underdog fixture. **Same-day scope
extension, at the user's request:** both platforms' full published
all-or-nothing payout tables were sourced and wired in too (PrizePicks:
2-6 picks; Underdog: 2-8 picks) — not just the 2-pick number — since the
same research effort needed to unblock Underdog's 2-pick entry also
answered "what about more picks" for both platforms at once. Not verified
against a real, currently-open Underdog 2-leg entry (see caveat below) —
a real data gap, not a code gap.

**Prerequisites:** None new — Underdog's data has been fully ingested and
flowing into `data/pickem/clv_log.csv` since Session 2.1/2.2 (confirmed
live, 2026-09-10: real `underdog` rows exist in the CLV log alongside
`prizepicks`). This is a sizing/frontend-only gap, not a data-ingestion gap.

**Why Underdog picks don't show up as bettable today:** `sizing_engine.py`'s
`SUPPORTED_PLATFORMS = {"prizepicks"}` gate (and the frontend's matching
`SUPPORTED_PLATFORMS` set in `app.js`) block Underdog specifically because
`ENTRY_PAYOUT_MULTIPLIER = 3.0` is PrizePicks' own published 2-pick Power
Play payout table (sourced in `sample_size_methodology.md`) — it is not a
generic pick'em constant, and applying it to an Underdog entry would size
against the wrong payout. A `PLATFORM_RISK_MULTIPLIER["underdog"] = 0.85`
entry already exists in the code specifically for this day, with a comment
noting it is "NOT currently reachable" until this session happens.

**What gets built:**
1. Source Underdog's real, current published payout multiplier table
   (their "Higher/Lower" entries pay out differently by pick count than
   PrizePicks' Power Play/Flex structure — this needs the same kind of
   direct verification Session 1.1's account-limiting research did, not an
   assumption).
2. Extend `sizing_engine.py`'s Kelly-sizing path to branch by platform
   instead of assuming one payout table — Underdog entries get sized
   against Underdog's real payout, PrizePicks entries unchanged.
3. Extend `frontend/app.js`'s `SUPPORTED_PLATFORMS` gate and the sizing-tool
   UI on the Pick'em tab the same way, so a real Underdog row can be sized
   in the browser, not just flagged.
4. Re-validate: run the sizing tool against a real, currently open Underdog
   row and confirm the output payout/edge numbers match Underdog's own app.
5. **(Added same-day, at the user's request):** source and wire in each
   platform's FULL published all-or-nothing table, not just 2-pick —
   PrizePicks' Power Play (3-6 picks; PrizePicks does not publish past 6)
   and Underdog's Standard entry (3-8 picks) — generalizing
   `sizing_engine.py`/`app.js` from a fixed 2-leg assumption to a
   per-(platform, leg-count) payout lookup. Explicitly does NOT include
   Flex-style entries on either platform (a genuinely different,
   multi-outcome payout shape — not sizeable with the same win/lose Kelly
   formula without real additional work — see `sizing_methodology.md`
   Section 2).

**Validation (required to close session):**
- [x] Underdog's real payout table sourced and cited (not guessed) —
confirmed live 2026-09-10 directly against Underdog's own help article
(help.underdogsports.com/en/articles/13780101-pick-em-standard-flex-entry-payouts):
2-pick Standard entry pays 3.5x (vs. PrizePicks' 3x for its own 2-pick
Power Play — confirmed genuinely different numbers, not assumed).
- [ ] `sizing_engine.py` sizes a real Underdog entry correctly, verified
against Underdog's own app for the same real entry — **NOT MET, explicitly
deferred, not failed.** Root cause confirmed directly against live data:
`data/pickem/clv_log.csv` contains exactly one real Underdog row total
(a closed Cam Ward NFL Pass Yards prop), not two real currently-open
Underdog legs to size and cross-check against Underdog's own app. This is
the same external, calendar/volume-driven gap Session 2.10 already
documented for Underdog (its real ingested volume is far lower than
PrizePicks'). The sizing math itself IS verified: a synthetic
all-Underdog fixture (`test_4b_underdog_sized_with_own_payout`,
`test_sizing_engine.py`) confirms the code correctly looks up Underdog's
3.5x payout and 0.85 dampener rather than PrizePicks' numbers. Re-running
this specific check against a real live 2-leg Underdog entry, once one
exists, is the re-verification trigger — see Open Decision #45's
resolution below.
- [x] Frontend Pick'em tab's sizing tool accepts Underdog legs — confirmed:
`SUPPORTED_PLATFORMS` now includes `underdog`, `ENTRY_PAYOUT_MULTIPLIER`/
`ENTRY_NET_ODDS_B` are per-platform, and the sizing result panel now
displays which platform/payout was used.
- [x] PrizePicks sizing behavior unchanged (regression check) — confirmed:
running `sizing_engine.py pickem` against two real, currently-open
PrizePicks legs pulled live from `clv_log.csv`
(`prizepicks|13957672` + `prizepicks|13961549`) reproduces the exact same
shape of result Session 2.6's own validation reported for a same-game,
high-combined-probability pair — `$69.85` uncapped, capped to `$25.00`
(5% of a $500 bankroll) — confirming the PrizePicks math path (payout
3.0x, dampener 0.70) is byte-for-byte unchanged by the platform-branching
refactor.
- [x] **(Extension)** Both platforms' full leg-count tables sourced and
cited from each platform's own page (PrizePicks: `prizepicks.com/ways-to-pick`;
Underdog: same help article as above), confirmed live 2026-09-10.
- [x] **(Extension)** `sizing_engine.py` sizes a real, live 3-leg PrizePicks
entry correctly — confirmed against three real, currently-open PrizePicks
legs pulled live from `clv_log.csv` (`prizepicks|13957672`,
`prizepicks|13957680`, `prizepicks|13957679`): correctly used the 3-pick
6.0x payout (not 2-pick's 3.0x), produced `entry_type: "3-pick Power Play"`
and a real, positive suggested stake ($25.00, capped).
- [x] **(Extension)** Synthetic coverage added for every other newly-supported
leg count (PrizePicks 4/5/6; Underdog 3/7/8) confirming each uses its own
platform-and-leg-count-specific payout, not a neighboring one
(`test_5b_prizepicks_3_through_6_pick_sized`,
`test_5c_underdog_7_and_8_pick_sized`, `test_sizing_engine.py`) — real,
live multi-leg Underdog data is not available yet, same gap named above.
- [x] **(Extension)** Same-game caution check generalized correctly —
confirmed via `test_7` (still 2-leg) plus manual reasoning: the dampener
now fires whenever ANY two legs in an N-leg entry share a game_id, not
only when a 2-leg entry's single pair does.
- [x] **(Extension)** All 27 tests in `test_sizing_engine.py` pass;
`node --check frontend/app.js` reports no syntax errors.

---

# PHASE 3 — Track 2: Cross-Venue Arbitrage

*Highest-confidence track. Unlike Phase 2, this track skips the estimation layer
entirely — it's pure price comparison across venues, so several Phase 2 sessions
collapse or don't apply.*

### Session 3.1 — Multi-Venue Data Ingestion
**Status:** ⚠️ Complete with caveats (2026-09-04) — see SESSION_LOG.md for full
detail. Climate and Weather + Commodities half fully built and validated;
Politics/Elections deliberately deferred to Session 3.1b (below); no live
matched pair observed yet (Open Decision #17).
**Prerequisites:** Phase 2 fully complete (reuses its ingestion pattern).

**What was built:** Generalizes the Phase 2 ingestion pattern to pull the same
real-world outcome's pricing from Kalshi and Polymarket. Kalshi ingestion
targets its "Climate and Weather" and "Commodities" series categories
specifically (448 series, confirmed via `GET /series`) rather than its full
catalog — a full-catalog pull was tried first and found unworkable at Kalshi's
real scale (99.5%+ combo/multi-leg contracts even 200,000 records deep). See
SESSION_LOG.md for the full bug-fixing story.

**Files touched:** `/scripts/ingestion/schema_exchange.py` (new),
`/scripts/ingestion/ingest_kalshi.py` (new), `/scripts/ingestion/ingest_polymarket.py`
(new), `/scripts/ingestion/venue_matcher.py` (new — matches the same real-world
event across venues), plus three diagnostic scripts kept in the repo
(`composition_check.py`, `sample_titles.py`, `discover_kalshi_series.py`) and a
new repo-root `.gitignore`.

**Validation (required to close session):**
- [x] Kalshi and Polymarket API access confirmed and documented (auth method,
rate limits, what's free vs. requires an account)
- [ ] Venue-matching logic correctly identifies the same real-world event/outcome
across at least 2 venues in a real test — **partial:** validated
against real title text in constructed test cases (including catching
and fixing two real false-positive matches); no live simultaneous match
observed yet. See Open Decision #17.
- [x] Normalized schema extended to cover exchange-style pricing (YES/NO
contracts), not just sportsbook-style odds

---

### Session 3.1b — Kalshi Politics/Elections Ingestion (Narrow Down-Ballot)
**Status:** ✅ Complete (2026-09-04) — see SESSION_LOG.md for full detail.
Narrow down-ballot filter designed, built, and validated against live data.
One specific matching-logic gap (Open Decision #21) carried forward to
Session 3.2 rather than fixed here, by direct agreement with the user.
**Prerequisites:** Session 3.1 complete. Does not block Sessions 3.2–3.4 —
arbitrage detection, sizing, and automation are all built to work on whatever
venues are already ingested, so this can be built whenever convenient rather
than gating the rest of Phase 3.

**What was built:** Extended `ingest_kalshi.py`'s targeted-series pattern to
Kalshi's Elections category (1,704 series, confirmed via `GET /series`) —
filtered down to two real, checkable tiers: individual U.S. House district
races (89 series) and individual state-legislature district races (4
series), 93 total, matching Session 0.1's actual "individual House/State
seats" scope. Kalshi's "Politics" category (2,296 series) was checked
directly and confirmed to contain no individual-race series at all, so it is
not pulled. City/county district races (14 series found live — NYC/LA City
Council) were checked against a real +EV-edge test and deliberately excluded
for now — see SESSION_LOG.md's Decision 1 for the full evidence trail. A new
`classify_down_ballot()` function implements the filter; down-ballot rows are
tagged with their specific tier (e.g. "Elections - US House District")
instead of Kalshi's generic "Elections" category.

**Files touched:** `/scripts/ingestion/ingest_kalshi.py` (extended, not
rebuilt — adds a second target-category set alongside Climate/Commodities)

**Validation (against this card's original checklist):**
- [x] A real, checkable definition of "narrow down-ballot" is documented and
applied as an actual filter (race type, geographic level, or similar —
not a subjective judgment call per race)
- [x] Real narrow down-ballot series pulled and confirmed against Session
0.1's original scope (not simply all of Politics/Elections) — 93 real
series confirmed live (89 House + 4 state legislature)
- [ ] Venue-matching re-run against the expanded Kalshi data to check for
real overlap with Polymarket's own down-ballot election markets —
**partial pass.** A real, live matched pair WAS found (U.S. House tier:
5/5 races checked have a matching Polymarket market — the first live
cross-venue match this project has found). However, `venue_matcher.py`
as currently configured would not catch it: Kalshi's `close_time` for
these contracts is the post-election swearing-in date, not the
election date, breaking the matcher's close-time-proximity check. See
Open Decision #21 — carried forward to Session 3.2, not fixed here.

---

### Session 3.2 — Arbitrage Detection Logic
**Status:** ✅ Complete (2026-09-05) — see SESSION_LOG.md for full detail,
including two real bugs found and fixed against live Kalshi/Polymarket data
mid-session (Open Decision #21's fix, and a previously-unknown Kalshi
liquidity-field defect).
**Prerequisites:** Session 3.1 complete (with Open Decision #17 — no live
matched pair yet for Climate/Weather — carried forward as a known gap, not
a blocker) and Session 3.1b complete (with Open Decision #21 — now resolved
this session, see below).

**What gets built:** Pure price-comparison logic — flags cases where the same
outcome is priced inconsistently across venues (including single-market YES+NO ≠
$1.00 mispricing), accounting for each venue's fee structure so a flagged
"arbitrage" is real profit, not an illusion created by ignoring fees. Per Session
0.1's five per-venue evaluation criteria, this session also explicitly checks
**liquidity** (a price gap that can't actually be filled at meaningful size isn't
a real arbitrage) and **legal footprint** (confirms both venues in a flagged pair
are legally available in the user's jurisdiction before the opportunity is
surfaced, not just priced).

**Files touched:** `/scripts/arbitrage/detector.py` (new),
`/scripts/arbitrage/liquidity_check.py` (new),
`/docs/venue_legal_footprint.md` (new — per-venue, per-state availability
reference, checked at flag time), `/scripts/ingestion/venue_matcher.py`
(modified — Open Decision #21 fix), `/scripts/ingestion/schema_exchange.py`
(modified — two new fields added mid-session after a real Kalshi data
defect was found), `/scripts/ingestion/ingest_kalshi.py` (modified — same
reason)

**Validation (required to close session):**
- [x] Detection logic correctly flags a known historical or simulated arbitrage
case — confirmed both single-venue (same-market YES+NO) and
cross-venue (matched-pair) shapes against constructed test cases, then
re-run against real live Kalshi/Polymarket prices for the real MO-05
down-ballot race (see below) with the correct real-world result: no
arbitrage, since real markets are efficient right now.
- [x] Fee-adjusted profit calculation confirmed accurate (manually cross-checked
on at least 2 real examples) — hand-computed Kalshi's and Polymarket's
own published fee formulas and confirmed exact agreement with each
venue's own published fee table (e.g. Polymarket Politics at 30¢ =
$0.84/100 shares; Kalshi at 30¢ = $1.47/100 contracts).
- [x] False-positive check: confirms it does NOT flag price differences that
don't actually clear fees — confirmed on a razor-thin constructed case
and, more importantly, on real current MO-05 prices (real gross costs
of $1.00–$1.05, correctly producing zero flags). Caught and fixed a
real floating-point rounding bug along the way where an exact-
breakeven case was silently dropped.
- [x] Liquidity check confirmed: a flagged opportunity includes the real
available size at that price, not just the headline price — **a real
bug was found here against live data and fixed within this session,
not deferred.** Kalshi's `liquidity_dollars` field was found to read
`"0.0000"` on every real Kalshi market pulled (multiple KXHIGHPHIL
weather strikes, both real legs of KXHOUSEMO5), despite real,
substantial size resting on the book. Fixed by capturing Kalshi's
real `yes_ask_size_fp`/`yes_bid_size_fp` fields (new
`schema_exchange.py`/`ingest_kalshi.py` columns) and using those for
Kalshi legs specifically, while keeping Polymarket's own `liquidity`
field (confirmed real and populated) for Polymarket legs. Re-validated
against the real MO-05 data after the fix: correctly reports a real,
non-zero fillable size instead of a false $0.00.
- [x] Legal footprint check confirmed: a flagged opportunity is suppressed or
clearly labeled if either venue isn't legally available to the user —
mechanism confirmed working (Kalshi's real, confirmed Sports-contract
state restrictions are modeled and would suppress/label a flag if this
project's tracks ever included Kalshi Sports). Honest, named gap: no
comparably detailed Polymarket-specific state-restriction list was
found this session — see Open Decision #22 below.

---

### Session 3.3 — Sizing Logic Adaptation
**Status:** ✅ Complete (2026-09-05)
**Prerequisites:** Session 3.2 complete.

**What gets built:** Adapts Phase 2's sizing engine for arbitrage's different
risk profile (execution risk and capital-lockup time across two simultaneous
positions, rather than single-position edge sizing).

**Files touched:** `/scripts/sizing/sizing_engine.py` (extended, not rebuilt)

**Validation (required to close session):**
- [x] Sizing correctly accounts for capital needing to sit in two venues
simultaneously — confirmed via two separate bankroll inputs
(`--kalshi-bankroll`, `--polymarket-bankroll`) and a new
open-positions ledger (`data/arbitrage/open_positions.csv`) that
tracks real committed capital per venue and correctly reduces
available capital on subsequent sizing calls; settlement correctly
frees it back up.
- [x] Execution-risk buffer included (price can move between detecting and
executing both legs) — `EXECUTION_RISK_BUFFER = 0.85` applied to
sized contract count. Sanity-checked against real live Kalshi data
(see SESSION_LOG.md): real quoted PRICE was stable across the real
windows checked, but real order-book SIZE moved up to 67% in 13
real minutes on one market — confirming the buffer targets the
right kind of risk, though its specific magnitude is only weakly
validated by one real data point (see Open Decision #23).

**Real bug found and fixed within this session, against live data:**
`detector.py`'s `fillable_size_dollars` field is a real CONTRACT COUNT,
not real dollars (per `liquidity_check.py`'s own docstring). The first
version of this session's sizing math treated it as dollars directly,
which would have materially misstated real per-leg capital on any
low-priced leg — confirmed directly against Kalshi's real MO-05
Republican leg ($0.20 ask, 15.28 real contracts: real cost is $3.06, not
$15.28). Fixed by sizing in contracts throughout and converting to real
per-leg dollar cost only at the end, using each leg's own ask price. See
SESSION_LOG.md for the full before/after and re-validation record.

---

### Session 3.4 — Automation Adaptation
**Status:** ✅ Complete (2026-09-06)
**Prerequisites:** Session 3.3 complete.

**What was built:** Extended automation to the arbitrage pipeline via a new
orchestrator (`scripts/run_arbitrage_pipeline.py`) and a new workflow
(`.github/workflows/arbitrage_pipeline.yml`), modeled on Session 2.7's
pick'em automation. Also added a deliberate per-series pause to
`ingest_kalshi.py` (an action item carried from Session 3.1), and fixed a
real false-positive matching bug in `venue_matcher.py`'s Elections path,
found via this session's own first live automated run — see
SESSION_LOG.md's Session 3.4 entry for the full evidence trail
(9 of 10 real flags were false cross-state matches; e.g. Kalshi's "WA-08"
vs. Polymarket's "IN-08").

**Files touched:** `.github/workflows/arbitrage_pipeline.yml` (new),
`scripts/run_arbitrage_pipeline.py` (new), `scripts/ingestion/ingest_kalshi.py`
(pause added), `scripts/ingestion/venue_matcher.py` (district-code matching
fix)

**Validation (required to close session):**
- [x] Workflow runs on schedule reliably — ✅ confirmed 2026-09-06: run
#4 was triggered via schedule (cron, not manual), succeeded in
4m 36s, and reproduced the same one genuine flag as the two prior
manual runs.
- [x] Polling frequency justified against real evidence — ⚠️ justified
against real GitHub Actions cost/budget data (checked directly:
2,000 min/month account-wide allowance, $0 budget with
"Stop usage: Yes"), NOT against real arbitrage-window-closing
timing, which still does not exist. 6 runs/day (~every 4 hours) is
an explicit, named placeholder pending Session 3.6's real timing
data — see SESSION_LOG.md for the full reasoning and the real cost
math for the cadences considered.

---

### Session 3.5 — Frontend Integration
**Status:** ✅ Complete (2026-09-06)
**Prerequisites:** Session 3.4 complete.

**What was built:** Added arbitrage opportunities to the existing frontend as
a new, clearly-labeled section on the same page (Track 2, blue accent),
rather than a separate site. This required three real, load-bearing changes
beyond the frontend files themselves, none of which were anticipated at
session open:

1. `detector.py` now writes a second, stable-named file
(`arbitrage_flags_latest.csv`) on every run, alongside its existing
timestamped output — the frontend needs one predictable filename to
fetch, and the pipeline previously only ever produced timestamped ones.
2. The Cloudflare Pages build command was extended to copy that new file
into `frontend/data/` alongside pick'em's existing `clv_log.csv` copy
step.
3. A real bug in `app.js`'s CSV reader (present since Session 2.8, never
triggered until now) was found and fixed — see Corrections below.

**Files touched:** `frontend/index.html`, `frontend/app.js`,
`frontend/style.css` (all extended, not replaced), `scripts/arbitrage/detector.py`
(two-line addition), Cloudflare Pages build command (dashboard setting, not
a repo file).

**Validation (required to close session):**
- [x] Arbitrage opportunities display correctly alongside pick'em, clearly
distinguished as a different track — confirmed on the live production
URL (`market-betting.pages.dev`), not just locally: a real screenshot
and a direct DOM check both show the one real flagged opportunity
(Kalshi MI-7 / Polymarket MI-07, carried over from Session 3.4)
rendering under a blue "Track 2" badge, below Track 1's own section,
with real stat-row and table values matching the underlying CSV.

---

### Session 3.6 — Live Validation Window
**Status:** ⚠️ In progress, left open intentionally — see SESSION_LOG.md for
full detail. **Before closing this session, read "Rule for sessions left
open across other work" above and pull the live files from GitHub first.**
**Prerequisites:** Session 3.5 complete.

**What gets built:** Same soak-test pattern as Session 2.9, adapted — since
arbitrage has no estimation model, "validation" here means confirming flagged
opportunities were real and executable, not a CLV comparison. Realized-outcome
reporting reuses Session 3.3's existing `sizing_engine.py` arbitrage ledger
(`record-open`/`settle`) directly — confirmed this session that it already
covers this need; nothing new was built for that half.

Sample size for arbitrage cannot use Session 2.5's breakeven-based method
(no win probability exists to size against — see
`docs/arbitrage_sample_size_methodology.md`, new this session). Real target,
derived from a standard zero-failure statistical convention applied to
Session 3.4's own measured 90% pre-fix defect rate: **30 confirmed-clean
distinct opportunities per detection mechanism (90 total across the
detector's three mechanisms)**. This session closes on a smaller, explicitly
named interim floor instead (≥1 per mechanism, or a documented zero-found
finding) — see SESSION_LOG.md Decision #3 for the full reasoning.

**Files touched:** `scripts/calibration/arbitrage_flag_tracker.py` (new),
`docs/arbitrage_sample_size_methodology.md` (new).

**Validation (required to close session):**
- [ ] Minimum sample size of flagged opportunities reached — interim floor
status as of 2026-09-06: `elections_wide` met (1 distinct real
opportunity); `single_venue` and `bucketed` not met (0 each). Re-check
via `arbitrage_flag_tracker.py --scan --report` after more real runs
accumulate.
- [ ] Spot-checked sample confirms flagged opportunities were genuinely
executable at the prices logged (not stale/unavailable by execution time)
- [ ] Go/no-go decision recorded

---

# PHASE 4 — Track 3: Weather/Climate Markets (Kalshi)

### Session 4.1 — Data Ingestion (Kalshi + Public Weather Data)
**Status:** ✅ Complete
**Prerequisites:** Phase 2 complete (reuses ingestion pattern); Kalshi API access
already resolved in Session 3.1 if Phase 3 is done first — otherwise resolve here.

**What gets built:** Ingests Kalshi's weather/climate markets alongside free
public ground-truth data (NWS, GFS, METAR) needed to independently estimate the
same outcomes Kalshi is pricing. Per Session 0.1's per-venue evaluation
criteria, this session also captures each market's real order-book depth
(**liquidity** — Kalshi weather markets are known to be thin, so this can't be
assumed adequate) and confirms Kalshi's current legal availability to the user
(**legal footprint**), rather than deferring either check to a later session.

**What actually got built (real drift from the card above, logged per this
project's standing practice):** "NWS, GFS, METAR" turned out to be one real,
free API, not three — see SESSION_LOG.md's Session 4.1 entry for the live
evidence. `ingest_nws_gfs_metar.py` was built as `ingest_nws_weather_data.py`
instead, and a second new file, `schema_weather.py`, plus a third,
`station_map.py` (a hand-built, real-data-confirmed city-to-station reference
table), were added beyond the original card — needed once it became clear
Kalshi runs several different ticker spellings per city and settles some
cities against a private-labeled but METAR-sourced feed, not NWS directly.

**Files touched:** `/scripts/ingestion/ingest_weather_markets.py` (new),
`/scripts/ingestion/ingest_nws_weather_data.py` (new, replaces the
originally-planned `ingest_nws_gfs_metar.py` — see above),
`/scripts/ingestion/schema_weather.py` (new),
`/scripts/ingestion/station_map.py` (new),
`/docs/weather_data_freshness_check.md` (new),
`/docs/nws_settlement_gap_resolution.md` (new),
`/docs/venue_legal_footprint.md` (extended with a Track 3 addendum, not
rewritten)

**Validation (required to close session):**
- [x] Kalshi weather market data and public weather data both ingest
successfully and can be joined on the same real-world event — pass,
confirmed against real committed data (576 rows, 62 series, 24 US
stations); Philadelphia spot-checked directly: same `KPHL` station code
in both files, real plausible temperatures, sane market pricing.
- [x] Data freshness confirmed adequate for the market's resolution timing (data
arrives before markets need to be evaluated) — pass, real evidence in
`docs/weather_data_freshness_check.md`: forecast data available
31–34 real hours before the earliest market close for that date;
observed data for grading arrives within minutes of a local day ending.
- [x] Order-book depth/liquidity captured per market, not just the top price —
pass, came through automatically via `yes_ask_size`/`yes_bid_size` on
every real row (same fields Session 3.2 already added for arbitrage).
- [x] Legal footprint confirmed and documented for Kalshi in the user's
jurisdiction — pass, by reference: `docs/venue_legal_footprint.md`'s
existing Session 3.2 finding (Kalshi's only confirmed restriction is
Sports-specific) extended with a one-paragraph addendum naming Track 3
explicitly, plus a live, direct check this session confirming Kansas
specifically (the user's own state) is fully available.

---

### Session 4.2 — Estimation Engine (Weather Threshold Model)
**Status:** ✅ Complete (closed 2026-09-07, ~20:04 UTC / 3:04 PM CDT) —
all three validation items pass on real evidence, including the
resolved-market sanity check, completed once Kalshi's real settlement
window passed. See SESSION_LOG.md's Session 4.2 (continuation) entry for
the real accuracy numbers.
**Prerequisites:** Session 4.1 complete.

**What gets built:** A model that computes the true probability of a weather
threshold being met directly from public forecast data (e.g. GFS ensemble spread
around a specific temperature/precipitation threshold), then compares that
against Kalshi's round-number-anchored market price. This is new modeling work
(not a reuse of the pick'em model), per Session 0.1.

**REAL FINDING (2026-09-07): no GFS ensemble was ever actually used.**
NWS's own public API (already the confirmed data source per Session
4.1/Open Decision #28) returns one deterministic forecast number, not an
ensemble — confirmed live before any model code was written. Built a
real, automated substitute instead: a literature-sourced starting
uncertainty curve, blended with this project's own real, measured
forecast-error data as it accumulates via a new daily pipeline. See Open
Decisions #32-#34 below and the full reasoning in
`weather_estimation_model_spec.md`.

**Files touched:** `/scripts/estimation/weather_model.py`,
`/docs/research/weather_estimation_model_spec.md`,
`/scripts/calibration/weather_forecast_error.py` (new),
`/scripts/estimation/weather_backtest_check.py` (new),
`/.github/workflows/weather_calibration_pipeline.yml` (new)

**Validation (required to close session):**
- [x] Model correctly handles ensemble/uncertainty data, not just a
single point forecast — pass, via the real automated blend
described above (no true ensemble exists to draw from; see Open
Decision #32).
- [x] Documented at the same specificity level as Session 2.3's spec —
pass, `weather_estimation_model_spec.md`.
- [x] Model's probability estimates are sanity-checked against at least a
handful of already-resolved historical Kalshi weather markets —
**pass, real evidence: 228 real resolved contracts checked, 81.58%
directional accuracy, Brier score 0.1342 (vs. a 0.25 coin-flip
baseline).** See SESSION_LOG.md's Session 4.2 (continuation) entry.

---

### Session 4.3 — CLV Logging Hook-In
**Status:** ⚠️ Complete with caveats (2026-09-08) — see SESSION_LOG.md for
full detail. Real work finally done this session (started 2026-09-07,
left as a placeholder, then closed alongside Session 5.3).
**Prerequisites:** Session 4.2 complete.

**What gets built:** Connects the weather model's output to the same CLV
logging infrastructure built in Session 2.4 (reused, not rebuilt).

**Files touched:** `/scripts/calibration/clv_logger.py` (extended to accept a
new track parameter, not duplicated — pick'em's own Session 2.4 code path
left fully unchanged)

**Validation (required to close session):**
- [x] Weather track flags log correctly into the same CLV structure — pass,
confirmed against real live data (288 real contracts, 203 flagged, 0
errors). See SESSION_LOG.md.
- [ ] At least one real week of logged weather flags reviewed for
completeness — **NOT MET, explicitly deferred by user direction**, not
silently dropped. See Open Decision #42.

---

### Session 4.4 — Sizing Adaptation
**Status:** ✅ Complete (2026-09-09) — see SESSION_LOG.md for full detail.
**Prerequisites:** Session 4.3 complete.

**What was actually done:** This card sat at "Not started" while Sessions
5.4 (politics) and 6.4 (props) were both built on top of the same shared
`sizing_engine.py` infrastructure — the same kind of roadmap-order gap
Session 4.3 itself was found sitting in before being built. Found and
closed now. Extended `sizing_engine.py` with a fourth sizing shape:
single-contract Kelly (reusing `raw_kelly_fraction_binary_contract()`
directly, same as politics/props) with Kalshi's real, sourced trading fee
folded into the effective cost per contract, rather than a named flat
dampener like every other track's adjustment.

**Files touched:** `/scripts/sizing/sizing_engine.py` (extended),
`/scripts/sizing/test_sizing_engine.py` (extended — 4 new synthetic
tests), `/docs/research/kalshi_fee_structure.md` (new — sources Kalshi's
published fee formula against 4 independent 2026 sources).

**Validation (required to close session):**
- [x] Sizing correctly reflects Kalshi's fee structure and this track's typical
edge size (likely smaller, more frequent edges than pick'em) — confirmed:
`KALSHI_FEE_RATE = 0.07` (Kalshi's own published general fee formula,
sourced not guessed — see `kalshi_fee_structure.md`) is folded directly
into the Kelly calculation via `kalshi_effective_cost_per_contract()`,
not applied as a post-hoc multiplier. Confirmed against real, live
`data/weather/clv_log.csv` (203 real open flags from Session 4.3): an
extreme-edge real flag (`KXHIGHTATL-26SEP07-B85.5`, model_prob=1.0 vs.
market_price=0.535) correctly capped at $25.00 (5% of a $500 bankroll);
a real thin-edge flag (`KXHIGHPHIL-26SEP07-T85`, edge≈0.0315) correctly
produced a small, proportional $2.73 stake — no portfolio-level exposure
ledger built (this track's positions resolve in days per `lead_days`,
not weeks/months, matching Session 6.4's own reasoning for props).

**Decisions made:**
1. **Kalshi's trading fee is sourced, not a named judgment call** —
unlike every other per-track dampener in this file (PLATFORM_RISK_
MULTIPLIER, the lockup table, PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER),
this is a real published formula (`fee = round_up_to_cent(0.07 *
contracts * price * (1-price))`), cross-checked against 4 independent
2026 sources. It is folded into the Kelly calculation itself (via an
effective per-contract cost), not bolted on afterward.
2. **No portfolio-level exposure ledger for weather** — same reasoning
Session 6.4 gave for props: real Session 4.3 data shows most weather
contracts resolve within days (`lead_days`), not the weeks/months that
motivated politics' second cap. A single-position cap
(`WEATHER_MAX_SINGLE_POSITION_PCT = 0.05`) is judged sufficient for v1.
3. **The per-contract fee rate is a stated simplification of Kalshi's
real order-level cent-rounding** (the published formula rounds up once
per whole order, not once per contract) — named explicitly as a real,
bounded imprecision in the code's own docstring, not treated as exact.

**Handoff notes:** Session 4.5 (Automation Adaptation) is next.

---

### Session 4.5 — Automation Adaptation
**Status:** ✅ Complete (2026-09-09) — see SESSION_LOG.md for full detail.
**Prerequisites:** Session 4.4 complete.

**What gets built:** The scheduled, unattended version of this track's
pipeline — Kalshi weather-market ingestion → NWS forecast/observed data
ingestion → threshold-probability estimation → CLV logging, run
back-to-back on a GitHub Actions schedule, matching the orchestrator
pattern already built for pick'em (Session 2.7), arbitrage (Session 3.4),
and politics (Session 5.5). This is distinct from
`weather_calibration_pipeline.yml` (Session 4.2), which only builds this
project's own forecast-error history — this pipeline is the one that
actually produces and logs real flagged opportunities.

**Files touched:** `scripts/run_weather_pipeline.py` (new — orchestrator,
not in the original card; needed because no prior session had built one
for this track, matching the other three tracks' own orchestrator
scripts), `.github/workflows/weather_pipeline.yml` (new)

**Validation (required to close session):**
- [x] Workflow scheduled appropriately against weather forecast update
cadence (e.g. aligned to GFS run times) — 4x/day (05:15, 11:15, 17:15,
23:15 UTC), each timed ~4-5 hours after a real GFS model cycle
(00Z/06Z/12Z/18Z) so NWS's own blended forecast has had time to ingest
that cycle before this pipeline pulls it; full reasoning recorded in the
workflow file's own header comment. Confirmed end-to-end against real
live data before scheduling: `run_weather_pipeline.py` run manually
produced 576 real market rows (62 series), 405 real NWS forecast rows
(24/24 stations OK), 576 real probability estimates, and 399 real newly
flagged CLV entries with zero pipeline failures across all four stages.

**Decisions made:**
1. **A dedicated orchestrator script (`run_weather_pipeline.py`) had to be
built this session** — unlike Sessions 4.1-4.4, which each extended an
existing shared file, no prior weather session had written a single
script that runs all four stages in order. Built to the same pattern as
`run_politics_pipeline.py` (Session 5.5): importlib-by-path module
loading, a `PipelineStageFailed` exception so an empty/broken stage never
silently flows into CLV logging as a false "market closed" signal, and a
per-run digest file (`output/digest/weather_digest_latest.md`) listing
every currently open flag.
2. **This pipeline re-runs NWS ingestion independently of
`weather_calibration_pipeline.yml`**, rather than trying to share a
single pull between the two workflows. Both scripts already treat
`_latest.csv` as fully overwritten and idempotent per run (same pattern
every ingestion script in this project uses), so a second real pull
during the same day is harmless — and keeping the two pipelines fully
independent means a future change to either one's schedule or logic
can't silently break the other.

---

### Session 4.6 — Frontend Integration
**Status:** ✅ Complete (2026-09-08) — see SESSION_LOG.md for full detail.
**Prerequisites:** Session 4.5 complete.

**What was actually done:** Added a third, independently-loading track
section (Track 3 — weather/climate markets) to the existing static
Cloudflare Pages frontend (`frontend/index.html`, `app.js`,
`style.css`), same pattern Session 3.5 (arbitrage) and Session 5.6
(politics) already established. This session was picked up out of
roadmap order — Session 5.6 (politics frontend) had already been built
and closed first, leaving weather as the one remaining track with no
frontend section — done now at the user's explicit request rather than
left open indefinitely.

**Files touched:** `frontend/app.js`, `frontend/index.html`,
`frontend/style.css`.

**Validation (required to close session):**
- [x] Weather track displays correctly in the existing frontend —
confirmed against a synthetic local fixture (real
`data/weather/clv_log.csv` schema, per `clv_logger.py`'s
`CLV_LOG_COLUMNS_WEATHER`), served over a local static HTTP server:
stats row, open-flags table (city, target date, forecast value, strike
threshold, side, market price, model edge, lead time), and closed-flags
table all rendered correctly with no console errors. This track's real
schema difference from the other three — `consensus_available` is
always `false` here, since Kalshi is the only venue this track ingests
— required no special-casing in the frontend beyond reusing the same
null-safe rendering already used elsewhere; it just never shows a
consensus figure, which is correct.

**Decisions made:**
1. **A fourth distinct accent hue (amber, `--accent-weather`) was
added**, continuing the "different hue per track" pattern from Sessions
3.5 and 5.6 — green (pick'em), blue (arbitrage), amber (weather),
purple (politics).
2. **No sizing calculator was added for this track**, matching Session
5.6's own reasoning for politics: this track's roadmap card required
correct display only, not an in-browser sizing flow.
3. **Weather-specific fields (city, target date, forecast, strike) are
shown directly in the table** rather than reusing pick'em's
player/team columns or politics' candidate/race columns — each
track's table matches what a flagged row actually represents, per
this project's existing per-track pattern rather than forcing one
generic table shape across tracks with genuinely different data
shapes.

**Handoff notes:** The Cloudflare Pages build command (dashboard
setting, not a repo file) needs one more copy step added, alongside the
politics one still pending from Session 5.6:

```
mkdir -p frontend/data && cp data/pickem/clv_log.csv frontend/data/clv_log.csv && (cp data/arbitrage/flags/arbitrage_flags_latest.csv frontend/data/arbitrage_flags_latest.csv || true) && (cp data/weather/clv_log.csv frontend/data/weather_clv_log.csv || true) && (cp data/politics/clv_log.csv frontend/data/politics_clv_log.csv || true)
```

All four tracks now have a frontend section. Phase 4/5's remaining open
sessions (4.7, 5.7 — Live Validation Windows) are unaffected by this
work and remain separately scoped.

---

### Session 4.7 — Live Validation Window
**Status:** ⚠️ Complete with caveats (2026-09-09) — see SESSION_LOG.md for full detail.
**Prerequisites:** Session 4.6 complete.

**What was actually done:** Derived Track 3's real sample-size thresholds
(same one-sample proportion-test method as Sessions 2.5/3.6/5.7/6.7, applied
to this track's own real flagged data rather than reused from another
track), built a recurring progress-report script matching Session 6.7's own
pattern, and ran the resulting go/no-go review against real, live
`data/weather/clv_log.csv` data.

**Files touched:** `docs/weather_sample_size_methodology.md` (new),
`scripts/calibration/weather_sample_report.py` (new — recurring progress
report, same pattern as `props_sample_report.py`).

**Validation (required to close session):**
- [x] Minimum sample size reached — **interim floor met**: 203 real closed
flags ≥ the 30-flag interim floor (same floor used by every prior track).
Full-confidence target (≈2,069 graded flags, derived in
`docs/weather_sample_size_methodology.md` Section 3) is not yet reached
(203/2,069 ≈ 9.8%) — expected and not a blocker, per every prior track's
own recurring-review precedent (Sessions 2.5, 3.6, 5.7, 6.7).
- [x] Real graded CLV performance reviewed against the north-star trendline
standard — confirmed via `weather_sample_report.py --report` against real
live data: mean `clv_edge_at_close` across all 203 real closed flags is
**+0.2592**, and **100% of closed flags (203/203) show a positive
`clv_edge_at_close`**. This is a real, honest positive signal at the
CLV-proxy stage (price-movement-to-close, not yet a confirmed win/loss
outcome — see caveat below and `docs/weather_sample_size_methodology.md`
Section 7), consistent with the S&P-500-trendline standard this project
holds itself to (ROADMAP.md Background & Approach).
- [x] Go/no-go decision recorded — **Go, continue running.** No red flags
found: zero pipeline failures since Session 4.5's automation landed, the
interim floor is already met, and the real CLV-proxy signal is uniformly
positive across every closed flag observed so far. This is not yet a
declaration of a *proven* edge — that requires the full ≈2,069-flag
target and, per the caveat below, a real graded win/loss outcome tracker
this track does not have yet — but there is no real evidence to stop or
pause the track either.

**Decisions made:**
1. **p₀ = 0.3804** (real mean `first_flagged_market_price` across 399 real
open flags) used as this track's breakeven, same reasoning Track 4/5 used
for their own p₀ — Kalshi weather contracts are binary $0/$1 payouts with
no fixed multiplier, so the flagged side's own market price at flag time
is the real breakeven, not a value borrowed from another track.
2. **Full-confidence target of ≈2,069 graded flags**, landing between Track
4's ≈892 and Track 5's ≈1,562 — a real, explained property of the
variance formula (Section 4 of the new methodology doc), not an
inconsistency between tracks.
3. **"Closed" is explicitly not claimed as "graded win/loss."** Same
honest limitation Sessions 3.6/5.7/6.7 already named for their own
tracks: `clv_logger.py`'s "disappeared == closed" convention confirms a
contract left the board, not which side it actually resolved. Unlike
those tracks, this one has a real structural path to a fully automated
grader — the same public NWS observed-value data already ingested for
forecasting (Session 4.1) can, in principle, also confirm the real
settlement value with no dependency on the user manually reporting a
placed bet. Named as a real candidate for a future session
(`docs/weather_sample_size_methodology.md` Section 7), not built here —
Session 4.7's own scope is the sample-size derivation and go/no-go
review, not a new tracker.

**Handoff notes:** Track 3 is validated to continue running under its
existing Session 4.5 automation. The recurring-review pattern (same as
`weekly_review.py`/`props_sample_report.py`) is now in place —
`weather_sample_report.py --report` can be re-run at any future point to
check real progress toward the ≈2,069-flag full-confidence target without
needing a new session. The one real open item is the weather-specific
automated outcome tracker named in Decision #3 above — a genuine
opportunity (objective public ground truth, no manual reporting required)
worth a future session once this track's real flag volume justifies
building it.

---

# PHASE 5 — Track 4: Down-Ballot Politics (Kalshi/Polymarket)

### Session 5.1 — Data Ingestion (Race Lists + Polling Data)
**Status:** ✅ Complete (2026-09-07) — see SESSION_LOG.md for full detail.
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

**Files touched:** `/scripts/ingestion/schema_politics.py` (new),
`/scripts/ingestion/ingest_politics_markets.py`,
`/scripts/ingestion/ingest_polling_data.py`

**Validation (required to close session):**
- [x] Race markets and polling data both ingest successfully and join correctly
on the same race — confirmed against real live data pulled back down from
GitHub after the user's live runs: 433 real races (93 Kalshi down-ballot
series matched, 80 kept as race rows; 427 Polymarket rows structurally
matched), 74 present on both venues; all 6 previously-known real races
(MO-05, MI-07, PA-HD12, CA-SD26, MD-SD2, MO-SD8) present with correct
data, and MI-07 exactly reproduces Session 3.4's own real arbitrage-check
finding (Kalshi 0.47 = Polymarket 0.47, correctly no edge).
- [x] Explicit filter confirmed working: marquee/high-profile races excluded per
scope — confirmed programmatically against the real 433-race output: zero
Governor, U.S. Senate, mayoral, or city-council rows found.
- [x] Liquidity captured per race market, and thin/illiquid races flagged as
such rather than treated the same as deep markets — confirmed via
`liquidity_note_kalshi`/`liquidity_note_polymarket` ("ok"/"thin"/"no
market") on every real output row, against named starting thresholds
(see Open Decision #38).
- [x] Legal footprint confirmed specifically for political-market participation,
not assumed from the venue's general availability — real, dated, sourced
finding via live web search: Kalshi has an active Washington-state
restriction on Elections & Politics contracts specifically (separate from
its existing Sports restriction); no equivalent Polymarket restriction was
found. Confirmed correctly applied row-by-row in the real output: exactly
the 2 of 10 WA races with a real Kalshi market are flagged, the other 8
(Polymarket-only) correctly are not.

---

### Session 5.1c — Candidate Identity Patch (found and fixed during Session 5.2 prep)
**Status:** ✅ Complete (2026-09-08) — see SESSION_LOG.md for full detail.
**Prerequisites:** Session 5.1 complete.

**What gets built:** Not originally a planned session — a real, load-bearing
problem was found in Session 5.1's own output while preparing Session 5.2's
estimation model: Kalshi runs one open market PER CANDIDATE per race, not one
Democrat-vs-Republican market per race (confirmed live: 8 open candidate
markets for one real race, KXCASEN26). The original ingestion kept only the
first market returned, with no record of which candidate or party it
belonged to — leaving no reliable way to align a venue's price with
ElectIndex's own per-party probability. Fixed at the root: every open
candidate market is now captured and matched to a party by real candidate
name (Kalshi's `yes_sub_title` field) or, on Polymarket, by the party word
stated directly in the market title ("Will the Republican Party win the
AL-01 House seat?") — a real, live-confirmed pattern found only after the
first live run of the fix exposed a 0-match Polymarket bug.

**Files touched:** `/scripts/ingestion/schema_politics.py`,
`/scripts/ingestion/ingest_politics_markets.py`,
`/scripts/ingestion/ingest_polling_data.py`

**Validation (required to close session):**
- [x] Every open candidate market per race captured (not just the first) —
confirmed live: 167 Kalshi + 3,416 Polymarket candidate markets captured
across 433 races, up from one arbitrary market per race previously.
- [x] Each market matched to Dem/Rep by real candidate name/party, unmatched
candidates logged not dropped — confirmed live, final run: Kalshi 76/80
races matched a Dem candidate, 75/80 matched a Rep candidate (16 of 167
open markets correctly unmatched — real minor candidates); Polymarket
427/427 races matched both Dem and Rep (2,562 of 3,416 correctly
unmatched — lettered placeholder/write-in markets, not a matching miss).
- [x] Real bug found and fixed mid-session, not assumed correct from code
review: first live run matched 0 of 3,416 Polymarket candidates because
Polymarket's real titles state the party directly rather than naming a
candidate — found by inspecting the real unmatched-candidate output,
fixed, and re-verified against the full real dataset before the second
live run.

---

### Session 5.2 — Estimation Engine (Underconfidence-Correction Model)
**Status:** ✅ Complete (2026-09-08) — see SESSION_LOG.md for full detail.
**Prerequisites:** Session 5.1 complete; Session 5.1c complete.

**What gets built:** A model targeting the documented "underconfidence" pattern
(prices compressed toward 50%, most pronounced in down-ballot races) — new
modeling work. Given the Track Reference table's noted caveat (key paper is an
unreviewed preprint with a data-count discrepancy; a related study's methodology
was publicly disputed by Kalshi), this session should include a re-verification
step against current, independent sources before the model is built around that
finding.

**Files touched:** `/scripts/estimation/politics_model.py`,
`/docs/politics_estimation_model_spec.md` (see Open Decision #39 — landed
outside `/docs/research/`, a real path inconsistency, not yet corrected)

**Validation (required to close session):**
- [x] Underconfidence finding re-checked against current sources before being
built into the model, given the noted contested magnitude — checked live:
the source paper is now a v2 preprint with a formal peer-review response,
adding a Bayesian measurement-error model. The finding survives (95%
credible interval entirely above zero, replicates independently on
Polymarket) but its magnitude shrinks under the stricter check (posterior
mean 0.107 vs. raw descriptive 0.156, ~31% reduction) — built into the
model as a named, sourced dampening factor
(`POSTERIOR_SHRINKAGE_FACTOR = 0.107/0.156`) rather than applied at full
raw strength.
- [ ] **Deferred, evidence-based, not a gap:** model sanity-checked against
historical resolved down-ballot markets where available. No real resolved
down-ballot contracts exist for this check yet — the 2026 general election
(`GENERAL_ELECTION_DATE`, used for this model's own time-to-resolution
calculation) is still roughly two months out. Same real constraint Track 4
(weather) hit and deferred for the same reason. Revisit once real
resolved contracts exist post-election.
- [x] Documented at the same specificity level as prior estimation specs —
`politics_estimation_model_spec.md` covers every input, the correction
formula, the sourced dampening factor, and named stated gaps, matching
`weather_estimation_model_spec.md`'s format.

Model math independently spot-checked by hand against three real output
rows (MD Senate 2 Dem and Rep, CA Senate 26 Dem) — recomputing
`sigmoid(slope × logit(raw_price))` by hand reproduced the file's own
`kalshi_corrected_prob` values exactly in all three cases.

---

### Session 5.3 — CLV Logging Hook-In
**Status:** ✅ Complete (2026-09-08) — see SESSION_LOG.md for full detail.
Built and closed together with Session 4.3 above (both share the same
generalized `clv_logger.py`).
**Prerequisites:** Session 5.2 complete.

**Files touched:** `/scripts/calibration/clv_logger.py` (same file as
Session 4.3 — shared engineering work)

**Validation (required to close session):**
- [x] Politics track flags log correctly into shared CLV structure — pass,
confirmed against real live data (866 real rows, 415 flagged, 0
errors). See SESSION_LOG.md.
- [x] Noted explicitly: this track's markets resolve slowly (election dates),
so CLV-equivalent (pre-outcome) signal matters even more here than
elsewhere — confirm the logged benchmark is meaningful pre-resolution,
not just a placeholder — pass: the cross-venue consensus benchmark is
real and time-independent (already firing on 129 of 415 real flags);
the closing benchmark's expected long-open shape for this track is
named explicitly and feeds directly into Session 5.4's sizing design.

---

### Session 5.4 — Sizing Adaptation
**Status:** ✅ Complete (2026-09-08) — see SESSION_LOG.md for full detail.
**Prerequisites:** Session 5.3 complete.

**What gets built:** Extends `sizing_engine.py` with a third, distinct
sizing shape — `size_politics_position()` — for single-contract Kalshi/
Polymarket flags out of `data/politics/clv_log.csv`. Unlike pick'em's
multi-leg parlay or arbitrage's locked two-venue pair, this is a single
genuinely probabilistic bet (standard binary-contract Kelly applies), with
two new adjustments neither other track needs: a stated, conservative
`POLITICS_LOCKUP_DAMPENER_TABLE` step function (keyed on Session 5.3's own
`hours_to_resolution` field) that shrinks the suggested stake as time to
resolution grows, and a new portfolio-level `POLITICS_MAX_TOTAL_EXPOSURE_PCT`
cap (backed by a new `data/politics/open_positions.csv` ledger) that limits
total capital locked across every simultaneously-open politics position,
not just any single one — since down-ballot positions can sit open for
weeks or months and realistically overlap, unlike pick'em or arbitrage.

**Files touched:** `/scripts/sizing/sizing_engine.py` (extended — new
politics section, constants, CLI subcommands),
`/scripts/sizing/test_sizing_engine.py` (6 new synthetic tests, 13 total),
`/docs/sizing_methodology.md` (new addendum, Sections 8–12)

**Validation (required to close session):**
- [x] Sizing reflects the long capital-lockup time for slow-resolving political
markets (money tied up for weeks/months, not hours/days) — confirmed via
`POLITICS_LOCKUP_DAMPENER_TABLE` (identical edge, identical bankroll:
10 days out → $35.00 suggested stake; 200 days out → $19.25, a real,
strictly smaller stake for the same edge) and the new portfolio-level
exposure ledger, both proven against synthetic fixtures in
`test_sizing_engine.py` (13/13 tests pass; no real
`data/politics/clv_log.csv` exists in this sandbox — same constraint
Sessions 2.6/3.3 already worked under).

**Decisions made:**
1. **Single-contract binary Kelly, not a parlay or an arbitrage-style
locked position.** A politics flag is one contract on one venue with a
real win/loss outcome — closer to arbitrage's single-leg mechanics than
to pick'em's multi-leg combination, but a genuine probabilistic bet
(Kelly applies), unlike arbitrage (no win/loss probability exists for a
locked position). The same project-wide `KELLY_FRACTION = 0.25` is
reused, not re-invented, for consistency with every other track.
2. **`POLITICS_LOCKUP_DAMPENER_TABLE` is a stated, conservative step
function, not a derived rate** — same posture as `SAME_GAME_CAUTION_
MULTIPLIER` (Session 2.6) and `EXECUTION_RISK_BUFFER` (Session 3.3). No
source gives a precise opportunity-cost figure for a specific number of
months of capital lockup, so a monotonically-decreasing 4-band step
function (< 30 days: 1.00; 30–90: 0.85; 90–180: 0.70; 180+: 0.55) is
used instead of inventing one. Re-deriving it is named as Session 8.3's
job, explicitly blocked on real resolved down-ballot contracts, which
per Session 5.2's own stated constraint cannot exist before the 2026
general election.
3. **A second, portfolio-level cap (`POLITICS_MAX_TOTAL_EXPOSURE_PCT =
25%`) was added on top of the existing single-position cap
(`POLITICS_MAX_SINGLE_POSITION_PCT = 5%`), backed by a new
`data/politics/open_positions.csv` ledger** — the real, structural
reason this track needs sizing adaptation at all. A single-position cap
alone cannot see that several long-dated positions, each individually
well-sized, can collectively lock up far more of a bankroll once they
realistically overlap for weeks or months at once (unlike pick'em,
which settles same-day, or arbitrage, whose existing per-venue ledger
already guards this from Session 3.3). Both cap percentages are stated
placeholders, same posture as every other cap in this project.
4. **No real `data/politics/clv_log.csv` exists in this sandbox** (the
user's live copy has real flagged rows, per Session 5.3's 866-row real
validation run, but is not reachable here) — validated entirely against
synthetic fixtures in `test_sizing_engine.py`, same constraint and same
resolution Sessions 2.6 and 3.3 already worked under for their own
sizing code.

**Open items / deferred validations:**
- None blocking. Re-deriving `POLITICS_LOCKUP_DAMPENER_TABLE` and both
cap percentages against real graded political positions remains
Session 8.3's job, tied to real resolved down-ballot contracts existing
after the 2026 general election (same constraint already logged against
Session 5.2's own model).

---

### Session 5.5 — Automation Adaptation
**Status:** ✅ Complete (2026-09-08) — see SESSION_LOG.md for full detail.
**Prerequisites:** Session 5.4 complete.

**What was built:** A fourth track orchestrator, `scripts/run_politics_pipeline.py`
— modeled directly on `run_pipeline.py` (Session 2.7) and
`run_arbitrage_pipeline.py` (Session 3.4) — running Track 4's four existing
stages back-to-back: race-market ingestion (Session 5.1) → polling/forecast
ingestion (Session 5.1) → estimation (Session 5.2) → CLV logging (Session
5.3). Same "stop before the next stage on 0 usable rows, never let a
transient outage look like every race closing" stance as the other two
orchestrators. A new workflow, `.github/workflows/politics_pipeline.yml`,
calls it on a daily schedule. Sizing (Session 5.4) is deliberately **not**
part of the automated run, same standing reason as the other two tracks —
this project flags and sizes, it does not place bets, and sizing needs a
human-supplied bankroll and a chosen flag_id.

**Files touched:** `.github/workflows/politics_pipeline.yml` (new),
`scripts/run_politics_pipeline.py` (new)

**Validation (required to close session):**
- [x] Workflow scheduled appropriately (likely daily/weekly, not high-frequency,
given slow-moving polling data) — daily (13:40 UTC), staggered from the
other three workflows' own run times, with the reasoning (down-ballot
race odds and ElectIndex's polling forecast move on a day/week
timescale, not hourly, per Session 5.1's own real `hours_to_resolution`
data; shared GitHub Actions minutes budget) recorded directly in the
workflow file's own docstring, matching this project's established
pattern for every prior polling-frequency decision (Sessions 2.7, 3.4,
4.x weather calibration).
- [x] Pipeline runs end-to-end against real, live data — confirmed directly
in this sandbox: a real run against live Kalshi, Polymarket, and
ElectIndex endpoints produced 434 real races, 5,655 real polling rows,
868 real (race, party) estimate rows, and 414 real newly-flagged CLV
rows, exit code 0, with a correctly populated
`output/digest/politics_digest_latest.md`. This sandbox's own
pre-existing tracked politics data files were restored afterward
(`git checkout --`) and all other real-network test artifacts deleted,
so this validation run does not overwrite or corrupt the user's real
committed history — same discipline Sessions 2.6/3.4/5.4 already
applied when validating against real or synthetic data outside the
user's own live environment.
- [x] Stage-failure handling confirmed by code inspection against the same
pattern already proven live in `run_pipeline.py` and
`run_arbitrage_pipeline.py`: any of the two ingestion stages or the
estimation stage returning 0 usable rows stops the run before CLV
logging and writes a `_FAILED` digest, so a transient Kalshi/
Polymarket/ElectIndex outage can never be mistaken for every
down-ballot race closing.

**Decisions made:**
1. **Daily cadence, not hourly or every-few-hours** — the real, explicit
scope call this session's validation checkbox required. Reasoning
recorded in the workflow file itself: down-ballot race prices and
ElectIndex's own forecast do not move on the hourly timescale a pick'em
line or an arbitrage window does (Session 5.1's real ingested data
already showed races sitting open for weeks/months), so hourly polling
would mostly re-log unchanged numbers while drawing down the same
shared, account-wide GitHub Actions minutes budget three other
workflows already draw from.
2. **Normalized race/polling snapshots and the estimates file ARE
committed every run** (unlike arbitrage's raw/normalized folders, which
are deliberately not committed) — same reasoning as
`weather_calibration_pipeline.yml`: Session 5.2's model and Session
5.4's lockup dampener are both named, sourced placeholders Session 8.3
must re-derive against real accumulated history once real resolved
down-ballot contracts exist, so this workflow builds that history on
purpose rather than only keeping the latest snapshot.
3. **No sandbox live `data/politics/clv_log.csv` history was preserved
from this session's validation run** — the run was real and against
live endpoints, but its output was reverted/deleted immediately after
confirming success, to avoid this sandbox's copy of the user's real
committed politics data diverging from what the user's own GitHub
history actually contains. The user's first real automated run happens
once this session's files are pushed and the workflow's schedule (or a
manual "Run workflow" click) fires for real.

---

### Session 5.6 — Frontend Integration
**Status:** ✅ Complete (2026-09-08) — see SESSION_LOG.md for full detail.
**Prerequisites:** Session 5.5 complete.

**What was actually done:** Added a fourth, independently-loading track
section (Track 4 — down-ballot politics) to the existing static
Cloudflare Pages frontend (`frontend/index.html`, `app.js`,
`style.css`), following the same pattern Session 3.5 established for
Track 2 (arbitrage): its own data file, its own accent color, its own
`init*()` function, loaded via `Promise.allSettled` alongside the other
tracks so a load failure in one track never hides another's real data.
Track 3 (weather) still has no frontend section — its own Session 4.6
remains "Not started," a pre-existing, separately-tracked gap this
session did not silently fold in or close.

**Files touched:** `frontend/app.js`, `frontend/index.html`,
`frontend/style.css`.

**Validation (required to close session):**
- [x] Politics track displays correctly, with resolution-date context
shown (since these are long-dated positions) — confirmed against a
synthetic local fixture (real `data/politics/clv_log.csv` schema,
served over a local static HTTP server, not the `file://` protocol,
since fetch() against `file://` is blocked): stats row, open-flags
table, and closed-flags table all rendered correctly. The open table's
dedicated "Time to resolution" column (converts `hours_to_resolution`
into a human h/d/mo string) correctly showed "2.1mo" for a
1560.5-hour-out test race, with rows past 60 days visually highlighted
in the track's accent color — the specific requirement this session's
roadmap card called out by name.

**Decisions made:**
1. **A third distinct accent hue (purple, `--accent-politics`) was added**,
matching Track 2's own "different hue per track" precedent from Session
3.5, rather than reusing pick'em's green or arbitrage's blue.
2. **No sizing calculator was added for this track.** Unlike pick'em
(Session 2.8), politics sizing is single-contract Kelly with a
portfolio-level exposure ledger (Session 5.4), not a
select-two-legs-and-combine flow — porting Session 2.8's
in-browser sizing calculator would mean re-implementing
`committed_capital_politics()`'s live ledger state in the browser,
which the static frontend has no way to read. This session's roadmap
card did not require a sizing calculator, only correct display with
resolution-date context — deferring the sizing UI is a stated
boundary, not a silent gap.
3. **Tested against a synthetic fixture, not the sandbox's real
`data/politics/clv_log.csv`**, because Session 5.5 already established
this sandbox has no real politics CLV log to test against (deleted
after that session's live validation run). Matches this project's own
established precedent (Sessions 2.6/3.3/5.4) of validating against
synthetic data first when the sandbox cannot reach the user's real
file, with real validation deferred to the user's live deploy.

**Handoff notes:** The Cloudflare Pages build command (a dashboard
setting, not a repo file — see Session 2.8/3.5's precedent) needs one
more copy step added, the same one-time dashboard edit Session 3.5
required when arbitrage was added:

```
mkdir -p frontend/data && cp data/pickem/clv_log.csv frontend/data/clv_log.csv && (cp data/arbitrage/flags/arbitrage_flags_latest.csv frontend/data/arbitrage_flags_latest.csv || true) && (cp data/politics/clv_log.csv frontend/data/politics_clv_log.csv || true)
```

The `|| true` fallback matches Session 3.5's own reasoning: politics'
first-ever CLV log write already happened for real in Session 5.3's
validation run, but a fresh deploy shouldn't hard-fail if this file is
ever briefly absent between pipeline runs. Next session is 5.7 — Live
Validation Window.

---

### Session 5.7 — Live Validation Window
**Status:** ⚠️ In progress — NOT complete, left open intentionally (see
SESSION_LOG.md for full detail and open items). Do not skip ahead to a
future close-out without first pulling the live SESSION_LOG.md/ROADMAP.md
from GitHub — see "Rule for sessions left open across other work" above.
**Prerequisites:** Session 5.6 complete.

**What was actually done:** Derived a real, evidence-based sample-size
threshold for this track (this track flags on a model-probability edge, like
Track 1, not a defect rate like Track 3 — so Session 2.5's method applies,
with a breakeven pulled from this track's own real data rather than reused
from Track 1's fixed-payout math). See
`docs/politics_sample_size_methodology.md` for the full derivation and
`scripts/calibration/politics_sample_report.py` for the recurring progress
check. Checking real data surfaced a genuine, unresolved gap — see Open
items below — that blocks this session's close independent of the sample-
size question itself.

**Validation (required to close session):**
- [ ] Minimum sample size reached — explicitly acknowledged this may take
longer to accumulate than faster-resolving tracks. **NOT MET.**
`data/politics/clv_log.csv` now exists and holds 415 real flags (real
run confirmed 2026-09-09, see "Root cause found" below), but 0 are
closed/graded yet — races take ~55+ days to resolve, per real
`hours_to_resolution` data. Interim floor: 30 closed flags; full
target: ≈892 (see methodology doc, Section 6).
- [ ] Go/no-go decision recorded — not yet possible; blocked on the item
above.

**Root cause found (2026-09-09):** GitHub's Actions tab showed **zero run
history at all** for `politics_pipeline.yml` — the scheduled daily trigger
had never fired, not "ran and failed silently" as originally suspected. The
user manually dispatched the workflow directly on GitHub.com; it completed
with a green checkmark and committed a real `clv_log.csv` (415 flags) to the
repo. This confirms the pipeline code itself is fine — the gap was the
schedule never triggering, cause still not confirmed (common causes: a
scheduled workflow's first cron firing can be delayed after being added to
the default branch, or GitHub silently disables scheduled workflows on
repos with 60+ days of no activity — unlikely here given how new the repo
is, but not ruled out). **Not yet confirmed: whether the daily 13:40 UTC
schedule now fires on its own**, since only a manual dispatch has been
proven so far. See Open items.

**Update (2026-09-10):** Checked via GitHub's own Actions tab (user
screenshot). Confirmed: 2 real runs exist, both from 2026-09-09 — run #1
was the manual dispatch (7:05 AM CDT / 12:06 UTC); **run #2 was a genuine
`Scheduled` trigger** (12:15 PM CDT / 17:15 UTC), ~3.5 hours late versus
the configured 13:40 UTC. As of 2026-09-10 15:10 UTC (over an hour past
that day's 13:40 UTC slot), no third run had appeared — the schedule
missed its second real opportunity entirely. **Applied a known fix:**
`.github/workflows/politics_pipeline.yml`'s cron was nudged from `40 13`
to `43 13` UTC and a dated comment added explaining why — committing any
change to a workflow file is a documented way to force GitHub to
re-register a stuck schedule trigger. The minute was deliberately changed
(not left at :40) so the next real run is independently verifiable as
this fix working, rather than indistinguishable from a lucky on-time
firing of the old registration.

**Update (2026-09-11):** The re-registration fix did **not** work. The
cron-minute-change commit (`4616f47`, "5.7 scheduled cron revisit") landed
on `main` 2026-09-10 15:12 UTC — over 22 hours before the next real
opportunity (2026-09-11 13:43 UTC). Checked at 2026-09-11 13:55 UTC (12
minutes past that slot): `git log --all | grep "politics pipeline"` still
shows only the same 2 runs from 2026-09-09. This is worse than the prior
state (which had at least one late-but-real fire) — the schedule has now
missed two consecutive real opportunities in a row since the fix. **A
minor re-commit is confirmed NOT to be the fix.**

**Update (2026-09-11, later same day) — delete/re-create fix applied:**
`.github/workflows/politics_pipeline.yml` was deleted in one commit
(`1113c0f`) and re-added as a brand-new file with identical content in a
separate commit (`269026e`), both pushed to `main`. This is the stronger
of the two escalation options named above — a full re-registration, not
another minor edit. Schedule unchanged (`cron: "43 13 * * *"` UTC).

**Open items / deferred validations:**
- **Confirm the delete/re-create fix worked.** After the next 13:43 UTC
slot passes (first real opportunity: 2026-09-12), check for a new
`Automated politics pipeline run` commit landing close to :43 UTC without
anyone triggering it manually. On time → fix confirmed, close this item.
Still late or missing → this is no longer explainable as a registration
quirk; a direct look at GitHub's status/known-issues page, or GitHub
Support, is the next real step (two independent fixes will have failed by
then).
- In the meantime, **`workflow_dispatch` (the manual "Run workflow"
button) is confirmed reliable** — both real successful runs to date used
it. Until the schedule is confirmed fixed, manually triggering the
workflow every day or two is a reasonable stopgap to keep real data
accumulating toward the sample-size thresholds below, rather than leaving
this fully idle while the schedule issue is worked.
- Re-run `python scripts/calibration/politics_sample_report.py --report`
periodically to track real progress against the interim floor (30) and
full target (≈892) from `docs/politics_sample_size_methodology.md`.
- Given real races take ~55+ days to resolve (real `hours_to_resolution`
data, Section 5 of the methodology doc), this session should be expected
to stay open across multiple future sessions/phases — same posture as
Session 3.6. Before ever closing it, re-read "Rule for sessions left open
across other work" and pull the live files from GitHub first.

---

# PHASE 6 — Track 5: Sportsbook Player Props (DraftKings, FanDuel)

### Session 6.1 — Odds Feed Ingestion
**Status:** ✅ Complete (2026-09-09) — see SESSION_LOG.md for full detail.
Both platforms confirmed working against real live data: FanDuel (141 real
player-prop rows) and DraftKings (672 real rows across 8 NFL events, via a
Playwright-driven real browser — DK sits behind Akamai Bot Manager, which
plain HTTP requests cannot pass). DK's real fix took four rounds of
real diagnosis (wrong fetch mechanism → CORS → headless detection → a
plain wait-condition timeout) — each a genuine bug, not a guess.
**Prerequisites:** Phase 2 complete.

**What gets built:** Ingests DK/FD player prop odds. Since DK/FD don't offer
public APIs (same undocumented-endpoint situation as the pick'em platforms, per
Session 1.1 continuation research pattern), this reuses the defensive-ingestion
approach from Session 2.2 rather than starting from scratch. Per Session 0.1's
per-venue criteria, this session also confirms **legal footprint** specifically
for player-prop markets, since prop-bet legality varies by state independently
of a sportsbook's general legal status (some states permit sportsbook wagering
but restrict or ban certain prop categories).

**Files touched:** `/scripts/ingestion/schema_props.py` (new — common
normalized schema, mirrors `schema.py`'s pattern),
`/scripts/ingestion/ingest_dk_props.py`,
`/scripts/ingestion/ingest_fd_props.py`,
`/scripts/ingestion/test_ingest_props.py` (new — synthetic-fixture harness,
same precedent as Sessions 2.2/2.4/2.5/2.6's own test files),
`/docs/venue_legal_footprint.md` (Session 6.1 addendum section added)

**Validation (required to close session):**
- [x] FanDuel ingests successfully — **CONFIRMED against real data,
2026-09-09**: 141 real player-prop rows, zero missing player names, zero
missing lines, after two real bugs (wrong player-name field; line
embedded in free text, not the `handicap` field) were found from the
actual live response and fixed. Non-player markets (Moneyline, Spread,
team win totals, etc.) correctly filtered out and logged, not stored as
misleading rows.
- [x] DraftKings ingests successfully — **CONFIRMED against real data,
2026-09-09**: 672 real rows across 8 real NFL events, spot-checked
against real player names, real matchup, and real odds moving in the
correct direction. Required a real API rediscovery (the original
`/api/v5/eventgroups` guess was wrong — DK's real current API lives on
`sportsbook-nash.draftkings.com/api/sportscontent/...`) plus a
Playwright-driven real browser instead of `requests`, since DraftKings
runs Akamai Bot Manager (TLS/JS fingerprinting, not header-based). Full
diagnostic chain in SESSION_LOG.md.
- [x] Vig/juice correctly extracted and stored — `schema_props.py` stores
both sides' raw American odds (not a pre-blended number), and
`american_odds_to_implied_probability()` plus its no-vig-normalization
test (`test_vig_extraction_matches_known_example`) confirm the
math is correct against a standard -115/-105 two-sided example.
- [x] Legal footprint confirmed specifically at the prop-category level —
`docs/venue_legal_footprint.md`'s Session 6.1 addendum documents
college-props and injury-props as the real, narrower-than-general-
sportsbook-legality restrictions found (college props out of v1 scope
regardless, since v1 is NFL-only); NFL player-performance props
specifically have no confirmed state-by-state restriction found, an
explicitly named open gap rather than an assumed clean bill of health.
Both ingestion scripts tag every row with `prop_category` so a future
session's flagging logic has the hook to gate on, per this document's
own stated next step.

---

### Session 6.2 — Estimation Engine Adaptation
**Status:** ✅ Complete (2026-09-09) — see SESSION_LOG.md for full detail.
FanDuel's real player-match gap (flagged in this session's first close) was
resolved same-day: the user re-ran `ingest_fd_props.py` locally, producing
141 real player-prop rows, and a real stat-type coverage gap found from
that data ("Passing TDs"/"Rushing TDs" wording) was fixed in
`pickem_model.py`'s `NFL_STAT_TYPE_MAP`. The one remaining caveat (DK
TD-scorer field vig not yet de-vigged) is a stated, scoped v1 boundary, not
an open blocker — see SESSION_LOG.md continuation entry.
**Prerequisites:** Session 6.1 complete.

**What gets built:** Adapts the Phase 2 pick'em projection model (same
underlying problem shape — projection vs. a number) rather than building new,
with adjustments for sportsbook-specific vig and market depth. Real Session
6.1 data turned out to contain two market shapes neither of which matches
pick'em's "one line, two-sided, single game" shape (season-long futures on
FanDuel; one-sided TD-scorer props on DraftKings) — both handled explicitly,
see SESSION_LOG.md.

**Files touched:** `/scripts/estimation/sportsbook_props_model.py` (imports
shared logic from `pickem_model.py` directly rather than duplicating it),
`/scripts/estimation/test_sportsbook_props_model.py` (new — synthetic-fixture
harness, same precedent as this project's other test files),
`/docs/sportsbook_props_estimation_model_spec.md` (new)

**Validation (required to close session):**
- [x] Model correctly separates "true edge" from "vig cost" so sizing later
isn't fooled by a line that only looks soft after vig is ignored — **met
for the two-sided case** (FanDuel `player_performance` rows: real
no-vig de-vig, proven against the -115/-105 example); **explicitly
NOT met for the one-sided case** (DraftKings TD-scorer rows: no
"under" side exists to de-vig against — raw implied probability is
used, flagged `implied_prob_includes_field_vig=True`), a stated v1
gap rather than a silently wrong number. See spec doc for full
reasoning.

---

### Session 6.3 — CLV Logging Hook-In
**Status:** ✅ Complete (2026-09-09) — see SESSION_LOG.md for full detail.
Extended `clv_logger.py` with a fourth `--track props` path, reusing the
generic (weather/politics) engine. 172 real flags logged against real
live data, zero pipeline failures, refresh path confirmed idempotent.
Real finding: cross-book consensus never matched on real data, because
DK and FD's real v1 markets are two different shapes (TD-scorer props vs.
season-long futures) with no real overlap yet — a stated, investigated
external-data gap, not a code defect (see SESSION_LOG.md Decision #2/
Finding #4).
**Prerequisites:** Session 6.2 complete.

**Files touched:** `/scripts/calibration/clv_logger.py` (extended — new
`--track props` path), `/scripts/calibration/test_clv_logger.py`
(extended — 5 new props scenarios; 6 stale pick'em scenario call sites
fixed), `/data/sportsbook_props/clv_log.csv` (new),
`/data/sportsbook_props/clv_snapshots/` (new)

**Validation (required to close session):**
- [x] Props track flags log correctly into shared CLV structure, with a real
sharp-book benchmark (e.g. Pinnacle-style no-vig line) where available —
this is the actual CLV metric in its most literal form for this track
— **met on an honest, explicitly-named basis**: neither DK nor FD is a
sharp book and no sharp-book feed exists anywhere in this project, so
the benchmark actually logged is the other book's own no-vig price on
the same real prop when both books carry it (same substitution
pick'em's own Session 2.4 made for its cross-platform benchmark). All
172 real flags from this session's live run wrote correctly into the
shared core-column CLV structure; the cross-book match itself did not
fire on any of them (real, investigated external-data gap — see
SESSION_LOG.md), but is proven correct against synthetic fixtures where
a real match exists.

---

### Session 6.4 — Sizing Adaptation (Account-Limiting Risk Built In)
**Status:** ✅ Complete (2026-09-09) — see SESSION_LOG.md for full detail.
The DK field-vig fix turned out not to need a schema change:
`source_market_id` already carried DK's own real per-market id per row
since Session 6.1, so grouping was purely an estimation-layer fix
(`schema_props.py` gained two small, reusable helper functions instead).
315 of 326 real DK rows now report a real field-normalized probability;
11 stayed honestly flagged (their real market only had that one
selection captured this run). Sizing then added two independent,
explicitly named account-limiting/uncertainty dampeners — see that
session's entry for full reasoning and real-data validation numbers.
**Prerequisites:** Session 6.3 complete.

**Prerequisite work carried forward from Session 6.2/6.3 — must be done
BEFORE any DK sizing is built:** DraftKings' TD-scorer rows still report
`implied_prob_includes_field_vig=True` (Session 6.2), and Session 6.3
confirmed this flag now also flows through into every DK flag logged in
the real CLV log — a real, investigated gap, not a placeholder that was
quietly resolved along the way. The fix requires a schema change (grouping
same-market selections together — e.g. all players priced in one real
"Anytime TD Scorer" market — so the field vig spread across the whole
group can actually be normalized out), which is real scoped work, not a
quick patch. **This session must close that gap before building DK's
sizing logic**, since sizing off an edge number that still includes field
vig would produce an inflated, untrustworthy DK stake — the exact
mismatch a limiting-risk dampener cannot fix if the edge underneath it is
already wrong. FanDuel's two-sided rows are unaffected (already correctly
de-vigged as of Session 6.2) and do not need this fix.

**What gets built:** (1) The DK field-vig fix — likely a change to
`schema_props.py` (to preserve/expose same-market selection grouping)
plus `sportsbook_props_model.py` (to actually normalize the group and
replace `implied_prob_includes_field_vig=True` with a real de-vigged
number) — followed by (2) sizing logic that must explicitly account for
account-limiting risk — this is the track where that risk is highest and
best-documented (per Track Reference table: consistent winners get
limited on DK/FD sportsbooks in a way that doesn't apply the same way to
exchanges or, per the pick'em research, even to PrizePicks/Underdog).

**Files touched:** `/scripts/ingestion/schema_props.py` (extended — same-
market selection grouping), `/scripts/estimation/sportsbook_props_model.py`
(extended — real DK field-vig normalization, replacing the
`implied_prob_includes_field_vig=True` placeholder), `/scripts/sizing/
sizing_engine.py` (extended)

**Validation (required to close session):**
- [x] DK TD-scorer rows report a real, field-normalized no-vig probability —
`implied_prob_includes_field_vig` is False (or the flag is retired
entirely) for every DK row this session can actually group, with any
row it still can't group left explicitly flagged, not silently assumed
fixed — confirmed on real live data: of 326 real DraftKings `estimated`
rows, 315 got a real field-normalized probability (group_size >= 2 real
selections, sum verified to exactly 1.0 on a spot-checked 30-selection
real market); 11 stayed honestly flagged True (their real group had only
that one selection captured this run).
- [x] Sizing logic includes an explicit limiting-risk dampener/cap distinct from
the other tracks, not reused blindly from pick'em or arbitrage --
`PROPS_PLATFORM_RISK_MULTIPLIER` (0.50 for both DK/FD, a stated judgment
call, more conservative than pick'em's 0.70 per this track's own
best-corroborated industry limiting reputation) plus a second,
independent `PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER` (0.60) that fires
only on a still-unresolved DK row -- confirmed against real live CLV
flags: a resolved DK flag (Jaxon Smith-Njigba, Anytime TD) sized to
$20.20 on a $500 bankroll; an otherwise-similar still-unresolved DK flag
(Rhamondre Stevenson, 2+ TDs) sized to $9.05, correctly smaller from the
extra dampener.

---

### Session 6.5 — Automation Adaptation
**Status:** ✅ Complete (2026-09-09) — see SESSION_LOG.md for full detail.
**Prerequisites:** Session 6.4 complete.

**What was built:** A sixth track orchestrator, `scripts/run_props_pipeline.py`
— modeled directly on `run_pipeline.py` (Session 2.7), `run_arbitrage_pipeline.py`
(Session 3.4), and `run_politics_pipeline.py` (Session 5.5) — running Track 6's
three existing stages back-to-back: DraftKings + FanDuel props ingestion
(Session 6.1) → estimation (Session 6.2/6.4, field-vig-normalized model) → CLV
logging (Session 6.3). One real difference from the other three orchestrators:
this one tolerates either single ingestion feed failing on its own (proceeding
in degraded single-venue mode, exactly the fallback Session 6.1 already
validated) and only stops before estimation/CLV logging if BOTH DK and FD
return 0 rows — reflecting that DraftKings' Akamai-bot-detection fight
(Session 6.1) makes a single-venue hiccup a real, expected possibility here in
a way it isn't for politics' two ingestion sources. A new workflow,
`.github/workflows/props_pipeline.yml`, calls it on a schedule. Sizing (Session
6.4) is deliberately **not** part of the automated run, same standing reason as
every other track.

**The one genuinely new piece of infrastructure this session required:**
DraftKings' ingestion (Session 6.1) needs a REAL, visible (non-headless)
Chromium browser — Akamai Bot Manager fingerprints headless Chromium
specifically and 403s it. A standard GitHub Actions Linux runner has no
display at all, so `props_pipeline.yml` installs Playwright's Chromium
(`playwright install --with-deps chromium`) and runs the whole pipeline under
`xvfb-run`, a virtual-display utility pre-installed on `ubuntu-latest` runners
— confirmed as the correct fix directly in `ingest_dk_props.py`'s own docstring
(Session 6.1's real finding), not guessed at fresh this session.

**Files touched:** `.github/workflows/props_pipeline.yml` (new),
`scripts/run_props_pipeline.py` (new)

**Validation (required to close session):**
- [x] Workflow scheduled against DK/FD line-movement cadence — every 3 hours
(8x/day), a deliberate, stated judgment call recorded directly in the
workflow file's own docstring: faster than politics' daily cadence (player
props move faster than down-ballot polling — injury news, lineup changes,
approaching kickoff can move a line within the same day) but deliberately
slower than pick'em's hourly cadence, because this track's own
best-corroborated risk (Session 6.4's `PROPS_PLATFORM_RISK_MULTIPLIER`,
per the Track Reference table) is account-limiting/bot-detection risk, and
DraftKings' ingestion in particular only works at all because of real,
hard-won Session 6.1 fixes against Akamai Bot Manager — hammering that
same fragile path every hour was judged an unnecessary escalation of a
real, unrecoverable-if-triggered risk (an IP-level block on GitHub's
shared runner ranges). Named explicitly as a placeholder cadence to
revisit once real run-history exists, same posture as every other
scheduling decision in this project.
- [x] Pipeline runs end-to-end against real, live data — confirmed directly
in this real run (not a disposable sandbox): DraftKings returned 674 real
rows across 8 events, FanDuel returned 141 real rows, estimation produced
815 real output rows (397 `estimated`, matching Session 6.4's
field-vig-fixed status breakdown), CLV logging added 1 real newly-flagged
row on top of the 228 already open from Session 6.4's own validation run
(229 total open), and `output/digest/props_digest_latest.md` was written
with a correctly populated, edge-sorted open-flags table. Exit code 0.

**Decisions made:**
1. **Either ingestion feed is allowed to independently fail without
stopping the pipeline** — a deliberate departure from politics'
orchestrator (Session 5.5), where both race and polling ingestion must
each succeed. Reasoning: `ingest_dk_props.py` and `ingest_fd_props.py`
already catch their own real exceptions internally and return a 0-row
summary rather than raising; DraftKings' Akamai bot-detection layer
tightening on a given run (or a runner-level Chromium/display problem)
is a real, expected single-venue risk this track must tolerate, and
`sportsbook_props_model.py`'s `load_props()` already runs correctly
against a single venue's file (confirmed Session 6.1). The pipeline only
stops early if BOTH feeds return 0 rows.
2. **3-hour cadence, not hourly** — see validation item above for the
full, named reasoning (account-limiting/bot-detection risk on the
DraftKings side specifically, weighed against player-props' faster real
movement than politics/weather).
3. **Automation does not call `sizing_engine.py props size`** — same
standing reason as every other track's orchestrator (Sessions 2.7, 3.4,
5.5): sizing needs a human-supplied bankroll and a chosen flag_id; this
project flags and sizes, it does not place bets.

---

### Session 6.6 — Frontend Integration
**Status:** ✅ Complete (2026-09-09) — see SESSION_LOG.md for full detail.
**Prerequisites:** Session 6.5 complete.

**What was actually done:** Added a fifth, independently-loading track
section (Track 5 — sportsbook player props, DraftKings + FanDuel) to the
existing static Cloudflare Pages frontend (`frontend/index.html`,
`app.js`, `style.css`), following the same established pattern as every
prior track's frontend session (3.5, 4.6, 5.6): its own data file
(`data/props_clv_log.csv`, a copy of `data/sportsbook_props/clv_log.csv`
per Session 6.3's `CLV_LOG_COLUMNS_PROPS`), its own accent color, its own
`initProps()` function, loaded via `Promise.allSettled` alongside the
other four tracks so a load failure in one track never hides another's
real data.

**Files touched:** `frontend/app.js`, `frontend/index.html`,
`frontend/style.css`.

**Validation (required to close session):**
- [x] Props track displays correctly, with a visible limiting-risk indicator
per flagged opportunity — confirmed against a synthetic local fixture
(real `CLV_LOG_COLUMNS_PROPS` schema, served over a local static HTTP
server, not `file://`): stats row, open-flags table, and closed-flags
table all rendered correctly with no console errors. Every open row
shows an "Acct. limit risk" badge — this track's real, best-corroborated
risk (`PROPS_PLATFORM_RISK_MULTIPLIER = 0.50`, applied equally to
DraftKings and FanDuel, per `sizing_engine.py`'s Session 6.4 addendum) —
plus a second "Field vig" badge on the one synthetic DraftKings row
flagged `implied_prob_includes_field_vig=True`, correctly absent from the
FanDuel row where that column was `False`.

**Decisions made:**
1. **A fifth distinct accent hue (teal, `--accent-props`) was added**,
continuing the "different hue per track" pattern from Sessions 3.5, 4.6,
and 5.6 — green (pick'em), blue (arbitrage), amber (weather), purple
(politics), teal (props).
2. **The limiting-risk indicator is shown as two separate badges, not one
blended label** — a static, always-present "Acct. limit risk" badge
(since `PROPS_PLATFORM_RISK_MULTIPLIER` is identical for DraftKings and
FanDuel, per Session 6.4's own stated reasoning that no source in this
project distinguishes the two) and a conditional "Field vig" badge that
only appears when `implied_prob_includes_field_vig` is true — the one
piece of real per-row risk variation this track's own data actually
carries. Blending these into one badge would have hidden the real,
row-level signal behind a label that's identical on every row.
3. **No sizing calculator was added for this track**, matching Session
5.6/4.6's own reasoning: this session's roadmap card required correct
display with the limiting-risk indicator only, not an in-browser sizing
flow — porting `sizing_engine.py`'s props-specific dampener chain
(`PROPS_PLATFORM_RISK_MULTIPLIER` and
`PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER` stacked with quarter-Kelly) into
the browser is a named future candidate, not built here.
4. **Tested against a synthetic fixture, not the sandbox's real
`data/sportsbook_props/clv_log.csv`**, matching this project's own
established precedent (Sessions 2.6/3.3/5.4/5.6/4.6) of validating
against synthetic data first when the sandbox cannot reach the user's
real file, with real validation deferred to the user's live deploy.

**Handoff notes:** The Cloudflare Pages build command (a dashboard
setting, not a repo file) needs one more copy step added, alongside the
weather/politics ones from Sessions 4.6/5.6:

```
mkdir -p frontend/data && cp data/pickem/clv_log.csv frontend/data/clv_log.csv && (cp data/arbitrage/flags/arbitrage_flags_latest.csv frontend/data/arbitrage_flags_latest.csv || true) && (cp data/weather/clv_log.csv frontend/data/weather_clv_log.csv || true) && (cp data/politics/clv_log.csv frontend/data/politics_clv_log.csv || true) && (cp data/sportsbook_props/clv_log.csv frontend/data/props_clv_log.csv || true)
```

The `|| true` fallback matches Sessions 3.5/4.6/5.6's own reasoning: a
fresh deploy shouldn't hard-fail if this file is ever briefly absent
between pipeline runs. All five tracks now have a frontend section. Next
session is 6.7 — Live Validation Window.

---

### Session 6.7 — Live Validation Window
**Status:** ⚠️ In progress — NOT complete, left open intentionally (see
SESSION_LOG.md for full detail and open items). Do not skip ahead to a
future close-out without first pulling the live SESSION_LOG.md/ROADMAP.md
from GitHub — see "Rule for sessions left open across other work" above.
**Prerequisites:** Session 6.6 complete.

**What was actually done:** Derived a real, evidence-based sample-size
threshold for this track (probability-based flagging, like Tracks 1 and 4 —
not a defect rate like Track 3), with a breakeven pulled from this track's
own real DK/FD American-odds-implied data rather than reused from either
prior track's math. See `docs/props_sample_size_methodology.md` for the full
derivation and `scripts/calibration/props_sample_report.py` for the
recurring progress check.

**Validation (required to close session):**
- [ ] Minimum sample size reached — **NOT MET.** `data/sportsbook_props/
clv_log.csv` holds 230 real open flags (confirmed against the real,
currently-committed file), but 0 are closed/graded yet — these are real
NFL props tied to the 2026-09-10 game slate, which had not yet kicked off
as of this session. Interim floor: 30 closed flags; full target: ≈1,562
(see methodology doc, Section 6).
- [ ] Go/no-go decision recorded, explicitly factoring in whether real-world
account limiting was observed during the window, not just modeled edge —
not yet possible; blocked on the item above.

**Decisions made:**
1. **p₀ = 0.2255 (real mean `first_flagged_market_price` across all 230
currently-flagged rows), not a reused or guessed number** — full reasoning
in `docs/props_sample_size_methodology.md` Section 2. Unlike Track 1
(fixed PrizePicks payout multiplier) or Track 4 (Kalshi/Polymarket
per-contract pricing), this track's breakeven comes from DK/FD American
odds converted to no-vig implied probability (Session 6.1/6.2).
2. **A props-specific realized-outcome tracker is deliberately NOT built
this session** — same reasoning as Sessions 3.6 and 5.7: building one
before any real prop has resolved would mean testing it against nothing
real. Deferred until at least one real flag in `clv_log.csv` closes.
3. **This session is being left open**, per the same standing rule
Sessions 3.6 and 5.7 established. Unlike Track 4's ~55-day race timescale,
this track's real resolution timescale is short (days, not months) — see
methodology doc Section 5 — so this session is expected to close sooner
than 5.7, not to stay open indefinitely.

**Open items / deferred validations:**
- Re-run `python scripts/calibration/props_sample_report.py --report`
after the 2026-09-10 NFL slate locks/resolves, to check for the first real
closed flags.
- Once the interim floor (30 closed) is reached, review real hit rate
against the 22.55% breakeven and record whether real-world account
limiting (this track's own best-corroborated risk, per the Track
Reference table) was observed during the window — not just modeled edge.
- Per ROADMAP.md's standing rule, before this session is ever closed, pull
the live SESSION_LOG.md/ROADMAP.md from GitHub again and check for any
session entries added in the meantime.

---

### Session 6.8 — FanDuel Independent Flagging Assessment (Props)
**Status:** ⚠️ Complete with caveats (2026-09-10) — see SESSION_LOG.md for
full detail.

**Prerequisites:** None new — FanDuel ingestion has been live and working
since Session 6.1 (confirmed live, 2026-09-09 run: 141 real normalized
rows) and `sizing_engine.py`'s `PROPS_SUPPORTED_PLATFORMS` already includes
`"fanduel"` alongside `"draftkings"` — props sizing is not the blocker here,
unlike Session 2.11's Underdog gap.

**Why the frontend/CLV log only ever shows `draftkings` rows today:**
`clv_logger.py`'s own props docstring uses `consensus_label` to name "which
book" a flagged row's cross-book price check came from — the real design
this session needs to confirm (not yet confirmed) is whether the props
estimation pipeline (`sportsbook_props_model.py`) only ever flags
DraftKings rows and uses FanDuel purely as the consensus benchmark price,
or whether FanDuel rows can also be flagged in their own right and simply
haven't cleared the edge threshold yet on real recent runs. This is a real
open question, not an assumed bug.

**What gets built:**
1. Trace `sportsbook_props_model.py` and `run_props_pipeline.py` to confirm,
   directly against the code (not memory), whether FanDuel rows are ever
   eligible to be flagged as the primary side, or structurally excluded.
2. If structurally excluded: assess what's needed to make FanDuel
   independently flaggable given its real data shape is season-long
   futures, not per-game props (see `sportsbook_props_model.py`'s own
   Session 6.2 docstring) — this may need its own probability model path,
   not just removing a filter.
3. If not excluded, just untested: confirm with a real run and document why
   no FanDuel row has cleared the edge threshold yet.
4. Extend the frontend's Props tab to show a platform column/filter either
   way, so DraftKings vs. FanDuel rows are visually distinguishable once
   both can appear (same pattern as the venue-link work done 2026-09-10).

**Validation (required to close session):**
- [x] Real, cited answer (from the code, not assumption) to "can FanDuel be
flagged on its own, today?" — **yes, structurally** (`build_props_
candidates()` in `clv_logger.py` and `process_props()` in
`sportsbook_props_model.py` apply identical logic to both platforms, no
`platform == "draftkings"` filter anywhere), **but no, in practice on
real data right now** — every real FanDuel row hits either the Session
6.6 stale-season-stats guard (correctly, against the pipeline's real
`--season 2025` default) or `no_player_match` (nflverse's 2026 file is
real but still too sparse — 67 rows, ~66 matchable players).
- [x] Not structurally excluded, so no follow-up build is needed — the gap
is real 2026 nflverse data maturity plus the `--season` default switch
already tracked as Open Decision #9, not missing code. Named as a
re-verification trigger for whichever session next touches Track 5.
- [ ] A real FanDuel-flagged row observed end-to-end — **not met, stated
gap, not silent.** An earlier real run (2026-09-09, before Session 6.6's
fix) did flag 70 FanDuel rows, but with false near-100% edges from
comparing a fresh 2026 line against a fully-completed 2025 season — the
exact bug Session 6.6 correctly closed. No real, non-bogus FanDuel flag
exists yet.
- [x] Frontend Props tab shows platform per row — already true, built as
part of the same 2026-09-10 venue-link work; confirmed directly in
`frontend/app.js` and `frontend/index.html`, no change needed.

---

### Session 6.9 — BetMGM Props Ingestion Feasibility & Build
**Status:** ✅ Complete — 2026-09-10. Direct, unauthenticated BetMGM
scraping (BetMGM's own site) is a confirmed no-go (real technical wall
plus an explicit ToS anti-scraping clause). **Real go found the same
day via a different, real venue: Rotowire.** Rotowire's own player-props
pages server-render real BetMGM prop data (no login, no key, no
geolocation gate of any kind) for the same reason sportsbooks let their
lines show on free comparison sites — it's a customer-acquisition channel
for BetMGM, not the same product surface this session's direct attempt
hit. Built and ran `scripts/ingestion/ingest_rotowire_betmgm_props.py`
against the real live page; wired its output into `sportsbook_props_
model.py`'s `load_props()` alongside DK/FD. Real caveat, stated plainly,
not hidden: Rotowire's own Terms of Use also prohibit automated "crawl or
spider" access — the same open-ToS-question category this project already
carries for DK's/FD's own undocumented-endpoint ingestion, not a new or
different kind of risk. Full build details in SESSION_LOG.md.

**Prerequisites:** Session 6.1's precedent (DraftKings/FanDuel ingestion)
and this project's standing due-diligence pattern for a brand-new venue —
same shape as Session 1.1's PrizePicks/Underdog endpoint research and
account-limiting review, and Session 3.1's Kalshi/Polymarket access
research. BetMGM has never been touched by this project before; treat this
as onboarding a genuinely new venue, not extending an existing one.

**What gets built (feasibility phase, same standard as prior venues'
Session 1-equivalent work):**
1. Confirm whether BetMGM exposes a reachable public or undocumented props
   endpoint without a login/API key (the same hard requirement this
   project has held every other pick'em/props venue to) — likely requires
   live browser Developer Tools reverse-engineering, the same fallback
   procedure documented in `prototype_dkpick6.py` for the one venue where
   this project already tried and failed.
2. If reachable: prototype-pull real data, document the real schema (field
   names, market shape — single-game props vs. season-long futures vs.
   TD-scorer-style field props, per Session 6.2's finding that DK and FD
   already differ from each other in this exact way).
3. Verify account-limiting/ToS posture specifically for props/sportsbook
   betting (distinct from BetMGM's other product lines), following the
   same archived-research pattern as
   `/docs/research/Pickem_Platform_Account_Limiting_Policy_Research.md`.
4. **Explicit go/no-go at the end of this session** — if no reachable
   endpoint exists (the real DK Pick6 outcome), BetMGM is dropped from
   scope here rather than carried forward as an open item, per this
   project's own established practice (see Session 2.1 Decision #1).

**If a "go":** a second, separate build session (numbered once this
session's findings are known) does ingestion + estimation-model adaptation
+ CLV logging + sizing + automation + frontend, the same seven-stage
pattern every other track has followed — not attempted in this
feasibility session.

**Validation (required to close this feasibility session):**
- [x] Explicit go/no-go, backed by a real, reproducible endpoint check
(not a guess) — **NO-GO.** See Session 6.9 entry in SESSION_LOG.md.
- [ ] If go: real schema documented, real account-limiting research cited —
N/A, no-go.
- [x] If no-go: reason stated plainly, same as DK Pick6's Session 2.1
Decision #1 — a real, reachable, unauthenticated data endpoint exists
(`cf-us4-cds-api.itsfogo.com`, BetMGM's real "CDS" sports-odds API, found
via the real `clientconfig` boot call, same discovery method Session 6.1
used for DraftKings), but it hard-gates every real request behind a
`"Country code is missing"` 400 error that persisted even with a real
US-Kansas IP and a real browser session/cookie set — confirmed as
BetMGM's GeoComply device-geolocation layer (GPS/Wi-Fi/plugin-based,
not simple IP geolocation), which a scripted HTTP client structurally
cannot satisfy. Separately and independently, BetMGM's Terms of Use
explicitly prohibit "using any robot, scraper, spider, or any other
automatic device ... to monitor or copy any content" — a second, named,
independent bar. **BetMGM is dropped from scope, no follow-up build
session planned**, per this card's own stated go/no-go rule.

---

### Session 6.10 — Caesars Props Ingestion Feasibility & Build
**Status:** ✅ Complete (no-go) — 2026-09-10. See full SESSION_LOG.md
entry for the real, reproducible evidence trail.

**Prerequisites/what gets built/validation:** Identical structure to
Session 6.9 above, substituting Caesars Sportsbook throughout. Sequenced
after Session 6.9 so the two feasibility checks don't get conflated, not
because one technically blocks the other.

**Outcome:** NO-GO — Caesars' public SPA host (`sportsbook.caesars.com`)
is static-only (S3/CloudFront); its real dynamic backend
(`americanwagering.com`) is confirmed live but gated by a real AWS WAF
CAPTCHA challenge, a different mechanism from BetMGM's GeoComply block but
the same practical outcome. Unlike BetMGM, neither established fallback
(Rotowire, Action Network) currently carries any Caesars data — checked
live, zero `czr_*` fields on Rotowire's props page, zero Caesars mentions
in Action Network's scoreboard payload. Caesars is dropped from scope
until one of two named re-check triggers fires (see SESSION_LOG.md).

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
Underdog, DK/FD sportsbook props) is an undocumented public endpoint —
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
5. ~~Scope the first estimation model concretely.~~ **Resolved 2026-08-31
(Session 2.3)**, using real ingested data rather than guessed in advance.
The model was scoped to NFL only for v1, using nflverse's public weekly
player stats as the external data source, with two inputs (season average
and recency-weighted recent form, blended 50/50) and a normal-distribution
probability estimate against each platform's fixed line. Stat-type
coverage — including two real scoring-formula stats (Kicking Points,
Fantasy Score) — was built directly from real ingested `stat_type`
strings, each checked against nflverse's real column list before being
mapped, with the two PrizePicks scoring formulas confirmed against
PrizePicks' own official sources rather than assumed. See Session 2.3 in
SESSION_LOG.md and `/docs/research/pickem_estimation_model_spec.md` for
the full input list, formulas, and verification record.
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

8. **New, opened Session 2.1:** Which pick'em platforms actually belong in
Track 1's scope, once real endpoint research (not secondhand
characterization) was performed. **Resolved 2026-08-29: DK Pick6 dropped.**
No credible public documentation of a Pick6-specific data endpoint was
found, and a best-guess URL (built by analogy to DraftKings' other
documented APIs) returned a 404. PrizePicks and Underdog were both
independently confirmed live, no login/key required, with real schemas
documented — see Session 2.1 in SESSION_LOG.md and
`/docs/research/endpoint_schemas.md` for full detail. Track 1 proceeds as
a two-platform track.
9. **New, opened Session 2.3:** Once 2026 NFL season data becomes available
from nflverse (first 2026 games are 2026-09-07; nflverse's
`stats_player_week_2026.parquet` release does not exist until real 2026
games have been played — confirmed directly, returns 404 as of
2026-08-31), the estimation model should begin folding in real 2026 data
instead of running entirely on 2025 season data. **Deliberately left
open, not decided in advance:** whether to switch cleanly to
`--season 2026` once enough 2026 games exist to be meaningful, or blend
2025 and early-2026 data during the transition period to avoid the model
swinging on a tiny early-2026 sample. No evidence yet exists to make that
call correctly — to be resolved in a future session once real 2026 data
starts accumulating.
10. ~~New, opened Session 2.4: Cross-platform CLV consensus matching...~~
**Superseded 2026-09-02 (Session 2.9 continuation):** the "Underdog has
zero real NFL lines" finding this decision was based on is now stale.
Live confirmation: Underdog does post real NFL props ahead of kickoff,
tagged `match_type: "Series"` — but these are all season-long totals
(Season Rush Yards, Season Pass TDs, etc.), not the weekly per-game props
this model estimates, and the `games`/`solo_games` join gap that was
suppressing them is fixed (see Open Decision #11 below). Real per-game
Underdog NFL lines still do not exist as of this update, since the
season hasn't started (2026-09-07). Action still needed once real
per-game lines exist: same re-check this decision originally called for.
11. ~~New, opened Session 2.4: `ingest_pickem.py`'s `normalize_underdog()`
joins each appearances record...~~ **Resolved 2026-09-02 (Session 2.9
continuation):** real cause found and fixed. Underdog's feed splits
scheduled events across `games` (team sports), `solo_games` (individual
sports), and a third, undocumented category tagged `match_type:
"Series"` whose match ID exists in neither list. `normalize_underdog()`
only ever read `games`. Fixed by adding a `solo_games` lookup, a
`games`→`solo_games` fallback join, and a fallback to the player's own
`sport_id` field when neither game container exists yet. Verified live,
before/after: sport resolution went from 89/217 (41%) to 191/191 (100%)
real appearances. A second, related gap was found and fixed the same
session: Underdog also never populates a clean stat-name field for these
same categories (NFL "Series", CFB, Tennis) — the real stat name only
exists as free text on the price option itself (e.g. "Higher 33.5 Games
Played"). Fixed via a regex fallback parser; verified against the live
feed at 245/263 lines (93%) resolving a real stat name, including real,
currently-tradeable Tennis props (Aces, Double Faults, Games Won). 18
lines still return no stat name — a real, small, unexplained residual
gap, not investigated further.
12. New, opened Session 2.5: `weekly_review.py`'s real first run has not
happened yet — no real bets have been placed or graded as of this
session's close. Not treated as a blocker (see Session 2.5's Handoff
notes: the weekly review is designed as an indefinite, ongoing
practice, not a one-time deferred validation item), but flagged here
so a future session picking up this thread knows the review history
in `review_log.csv` genuinely starts empty, not just under-sampled.
Action needed: once the user places and reports a first real bet,
run `weekly_review.py --run` for real and confirm the interim-floor
behavior (Section 6 of `sample_size_methodology.md`) holds on a real,
small sample the same way it did on synthetic and placeholder data.
13. ~~New, opened Session 2.8: nearly every open flag's `first_flagged_model_prob`
observed on the live frontend is extremely close to 100%~~ **Resolved
2026-09-02 (Session 2.9 continuation):** checked the real distribution in
`clv_log.csv` directly rather than the dashboard view — only 4.9% of
3,461 open flags sat at 99–100%, another 6.6% at 95–99%; 74.3% sat in the
ordinary 50–85% range. The near-100% impression came from `app.js`
sorting the open-flags table by `first_flagged_edge` descending, which
surfaces exactly the highest-probability rows first — a display sort
artifact, not an estimation-model bug. No code change needed.
14. ~~New, opened Session 2.9 (continuation): this project's stated scope is
+EV bets across all betting markets...~~ **Resolved 2026-09-03
(Session 2.10).** Full inventory completed: 29 PrizePicks leagues
confirmed live, real data-source answers found for every sport
including the long tail (strong candidates: NFL, MLB, NBA, EPL,
ESPN-API-covered non-EPL soccer, UFC, F1, golf; genuine gaps: KBO,
NPB, handball, badminton, most esports; Tennis has real volume but no
adequate free data source). Underdog's full list is the one piece not
fully closed — deferred to a bounded, already-running automated
follow-up rather than left open (see Session 2.10's card above and
SESSION_LOG.md for the verification record).
15. **New, opened Session 2.10:** confirming Underdog's complete current
sport list required real time-of-day/day-of-week spread that a single
session can't produce (checked directly — no shortcut endpoint exists
on Underdog's API). A GitHub Actions workflow now gathers this
automatically over a defined 4-day, 12-run window
(`.github/workflows/sport_inventory_scan.yml`) rather than leaving it
as an indefinite TODO. **Action needed:** once the window ends (early-
to-mid September 2026), read the accumulated files in
`docs/research/scans/`, finish `/docs/research/sport_inventory.md`'s
Underdog tables, and disable the workflow.
16. **New, opened Session 2.10:** both PrizePicks and Underdog were found
to now offer products beyond fixed-line pick'em — PrizePicks Predict
(a direct Kalshi partnership, live in most states) and Underdog
Exchange (a separate CFTC-regulated exchange via Aristotle Exchange,
not confirmed to be a Kalshi wrapper the same way). Re-applying
Session 0.1's own five ranking criteria (repricing mechanism, fee/vig,
account-limiting risk, liquidity, legal footprint) against real,
newly-gathered evidence (Kalshi's own public API confirmed live and
fully open with no key; real sports-market liquidity checked directly
and found thin; Kalshi's sports contracts specifically found to be in
active, unresolved multi-state legal conflict, including criminal
charges filed by Arizona) **did not support expanding Track 3's scope
to Kalshi's direct sports markets.** Recommendation: Track 3's
original scope (weather/climate, narrow down-ballot politics) and
ranking stand as originally set — see SESSION_LOG.md for the full
evidence-by-evidence writeup. This is logged as a recommendation for
review, not an applied decision, consistent with how every other
ranking call in this project has been made.
17. **New, opened Session 3.1:** no live, real matched pair has been
observed between Kalshi (Climate/Weather + Commodities) and Polymarket
as of 2026-09-04. `venue_matcher.py`'s correctness has been validated
against real title text assembled into constructed test cases —
including catching and fixing two real false-positive matches
(mismatched earthquake magnitude thresholds) — but not against a pair
that arrived together from a real, live, simultaneous pull. **Action
needed:** watch for genuine overlap in future runs (e.g. an active
storm or extreme-heat event both venues list) and confirm a real match
when one appears. Not treated as a blocker for Session 3.2, but a real,
named gap — decided explicitly with the user rather than chased
further in Session 3.1.
18. **Opened Session 3.1, RESOLVED Session 3.4 (2026-09-06):** Kalshi's
targeted 448-series pull hit repeated `429 Too Many Requests`
responses on a real run. Existing retry logic recovered every time
with no data lost, but this was not a deliberate load test.
Fixed: added `KALSHI_PER_SERIES_PAUSE_SECONDS = 0.2` and a
deliberate pause after every one of `ingest_kalshi.py`'s ~540
real per-series requests (success or failure), specifically
because Session 3.4 turns this into an unattended, scheduled job
rather than a watched manual run. See SESSION_LOG.md's Session 3.4
entry.
19. **New, opened Session 3.1:** Polymarket's Gamma API `/events` endpoint
fails with a consistent HTTP 422 error at offset=2100 on every real run
this session (reproduced multiple times, same exact offset). The
current fix in `ingest_polymarket.py` keeps data collected before the
failure rather than losing it, but the root cause — a real, undocumented
API limit vs. the query running past the true count of currently active
events for this filter — is not confirmed. Not a blocker; a real,
named gap for whoever next has reason to look at Polymarket ingestion
depth.
20. **Opened Session 3.1, RESOLVED Session 3.1b (2026-09-04):** Kalshi's
Politics and Elections categories (2,287 + 1,662 = 3,949 series
combined, confirmed via `GET /series`) were deliberately not ingested
in Session 3.1. Session 3.1b checked both categories directly and
found the real, checkable distinction: "Politics" (2,296 series)
contains no individual-race series at all (national news and
officeholder-status questions); "Elections" (1,704 series) is where
real races live, and within it, individual U.S. House district races
(89 series, structural ticker pattern) and individual state-
legislature district races (4 series, structural title pattern) pass
a real per-seat forecast-data-availability test, while city/county
races (14 series) do not — see SESSION_LOG.md's Session 3.1b entry for
the full evidence trail. 93 real down-ballot series are now ingested.
21. ~~New, opened Session 3.1b: `venue_matcher.py`'s close-time-proximity
check does not account for Kalshi's down-ballot political contracts
setting `close_time` to the post-election swearing-in date...~~
**Resolved 2026-09-05 (Session 3.2), confirmed against real live data.**
Kalshi rows tagged with an Elections category now match against
Polymarket using a separate, 400-day close-time tolerance (vs. the
default 6 hours) plus a raised title-similarity bar (0.5 vs. 0.35) to
compensate for the looser time check — see `venue_matcher.py`'s own
"SESSION 3.2 FIX" docstring section for the full rationale. Verified
live: pulled the real `KXHOUSEMO5-26-R`/`-D` markets (real close_time
`2027-11-03T15:00:00Z`) and the real Polymarket "MO-05 House Election
Winner" markets (real endDate `2026-11-04T00:00:00Z`, an 8,751-hour
gap) and confirmed the matcher now correctly proposes both legs as
candidate matches (title similarity 0.625, well above the 0.5 bar).
22. ~~New, opened Session 3.2: no comparably detailed Polymarket-specific
state-by-state legal-restriction list was found this session...~~
**Resolved 2026-09-07 (Session 5.1), checked live specifically for
political/election contracts (not sports, which remains the separate,
already-tracked restriction).** Kalshi: a real, current, dated
restriction found — a King County Superior Court order (effective
2026-08-19/20) requires Kalshi to geofence Washington users out of
Elections & Politics contracts specifically, separate from its existing
Sports restriction. Polymarket: no politics-specific state restriction
was found, distinct from its general availability picture. Named,
honest caveat carried forward: this is a fast-moving legal landscape
(Washington's own order was under a week old at the time of this
check) and should be re-verified, not assumed still accurate, before a
future session leans on it for real sizing/suppression logic. See
`ingest_politics_markets.py`'s module docstring and SESSION_LOG.md's
Session 5.1 entry for the full evidence trail.
23. **New, opened Session 3.3; revisited 2026-09-11, still NOT
RESOLVED.** `EXECUTION_RISK_BUFFER = 0.85` in `sizing_engine.py` is a
named placeholder, sanity-checked but not fully validated against real
data. Real live Kalshi quotes (MO-05, `KXHIGHPHIL`) were pulled twice,
roughly 13–30 real minutes apart: quoted PRICE was completely unchanged
both times, but real order-book SIZE at the best price moved as much as
67% in 13 real minutes on one market. **Revisited 2026-09-11** once
Session 3.4's automation had produced 5 real days / 21 snapshot files:
pulled all of them and found only 2 of 15 distinct flagged pairs were
ever observed more than once. One (MI-07) showed 0% real size decay
across three short (10–68 min) gaps; the other (TX-32) showed real
±86–133% swings, but only across multi-hour gaps too coarse to say
anything about execution-time risk specifically. These two real
findings directly conflict, and the arbitrage detector's own ~4–6 hour
polling cadence (Open Decision #26) is structurally too coarse to
resolve which one reflects real execution risk — more days of the same
cadence will not fix this. Built `execution_risk_poller.py` (new) to
poll a single live pair's real order book at short, fixed intervals.
**First real run (2026-09-11, 30 real minutes, 16 readings every 2
min, Kalshi `HOUSEVA7-26-R` vs. Polymarket's VA-07 market): 0% movement
across every single reading.** This is a fourth real, single-market
data point, and it still conflicts with the original 67%-in-13-minutes
finding rather than resolving anything — most likely because a
down-ballot election contract months from resolution has near-zero
real turnover, unlike the actively-traded weather market the original
finding came from. **Action needed, updated again:** run
`execution_risk_poller.py` against an ACTIVELY traded, near-resolution
market (a weather threshold contract close to its settlement window is
the best real candidate this project has) rather than another
low-turnover election contract — the instrument matters as much as the
polling interval. See SESSION_LOG.md's 2026-09-11 entries for the full
evidence trail.
24. **Opened Session 3.3, UPDATED Session 3.4 (2026-09-06):**
`sizing_engine.py`'s arbitrage sizing has been validated against
constructed test cases and against real Kalshi order-book numbers
plugged into a labeled test flag, but not yet against a genuine LIVE
positive arbitrage opportunity end-to-end. Session 3.4's real
automated run produced exactly one: Kalshi's "MI-7" vs. Polymarket's
"MI-07" (Michigan's 7th Congressional District, confirmed via web
search to be the same real race, not a formatting coincidence).
**Action needed:** run `sizing_engine.py arbitrage size` against
this real flag as the first genuine end-to-end check — still a
manual step per this project's "flags and sizes, never places bets"
rule, not something automation does on its own.
25. **New, opened and RESOLVED same session, Session 3.4 (2026-09-06):**
`venue_matcher.py`'s Elections wide-tolerance path proposed 10
flagged pairs on its first real automated run; 9 were false matches
across DIFFERENT states sharing only a coincidental district
NUMBER (e.g. Kalshi's "WA-08" vs. Polymarket's "IN-08" — Washington's
8th District vs. Indiana's 8th District), several reporting a
50–90 cent-per-dollar "edge." Root cause: title tokenization splits
"WA-08" into separate "wa"/"08" tokens, so a shared district number
alone could satisfy both the title-similarity and number-compatibility
checks with no state comparison at all. Fixed within the same
session (per this project's standing "fix real validation bugs now"
practice): added `_extract_district_codes()`/
`_district_codes_compatible()`, requiring an exact (state, district)
match when both titles have one. Re-validated against real data:
candidate pairs dropped 497→477, flags dropped 10→1 (the one
genuine MI-7/MI-07 match, now reporting a realistic 1-cent edge).
See SESSION_LOG.md's Session 3.4 entry for the full evidence trail.
26. **New, opened Session 3.4:** the arbitrage pipeline's polling cadence
(6 runs/day, ~every 4 hours) is justified against real GitHub
Actions cost/budget data, NOT against real arbitrage-window-closing
timing — that evidence still does not exist (no genuine window has
ever been observed to close, per Session 3.2/3.3). This is a
deliberate, named substitution of one kind of real evidence for
another that doesn't exist yet, not a resolved question. **Action
needed:** once Session 3.6 (Live Validation Window) produces real
timing data on how long a genuine flagged opportunity stays open,
revisit this cadence against that evidence rather than the cost
constraint alone.
27. **New, opened Session 3.4:** GitHub Actions minute usage is shared
account-wide across Market_Betting AND all three DFS optimizer
repos (confirmed directly via the account's real billing page,
2026-09-06) — a single 2,000-minute/month pool, with the account's
Actions budget configured to STOP all workflows account-wide (not
silently charge) if exceeded. DFS_Optimizer's real workflow
(`refresh_data.yml`) was found to be a genuinely complex multi-job,
multi-cadence matrix, not a simple single script — modeling its
(and DFS_Optimizer_NHL's/DFS_Optimizer_PGA's) exact future cost
would require a real audit of three more repos' workflow files, not
attempted this session. **Standing practice going forward, not a
one-time fix:** periodically check the account's real billing
overview page (especially once NHL/PGA seasons ramp up their own
repos' automation), and treat the arbitrage pipeline's cadence as
the first, lowest-cost lever to pull back if the account ever
trends toward its ceiling.
28. **New, opened and RESOLVED same session, Session 4.1 (2026-09-06):**
the roadmap card's "NWS, GFS, METAR" wording implied three separate
public data feeds. Checked live: NWS's own public API
(`api.weather.gov`) already returns both an official gridded
forecast (built from blended model guidance, GFS included) and
METAR-sourced station observations, in structured JSON, for free,
with no key. Pulling raw GFS grib2 files or raw METAR text
separately would re-derive what this one API already computes, for
no additional real information. Session 4.1 built on this one API
rather than three feeds — see `ingest_nws_weather_data.py`'s module
docstring for the full reasoning, and SESSION_LOG.md's Session 4.1
entry for the live evidence.
29. **New, opened and RESOLVED same session, Session 4.1 (2026-09-06):**
Kalshi's weather series settlement sources are NOT uniform. A live
check of six real series found five settle against "The Weather
Company" (a 2026-09-02 contract migration, confirmed via Kalshi's
own contract-terms metadata) and one legacy series (Houston) still
settles directly against an NWS Climatological Report. Checked
further and RESOLVED: `weather.com/kalshi`'s own reference page
states its data is "METAR airport observations relayed via The
Weather Company" for a fixed, named list of 37 government-station
codes — the same underlying government data this project's own NWS
pipeline already pulls for those same station codes. This is a real,
confirmed naming difference in Kalshi's settlement-source field, not
a private/proprietary data source this project can't independently
replicate. See SESSION_LOG.md's Session 4.1 entry for the full
evidence trail.
30. **New, opened and RESOLVED same session, Session 4.1 (2026-09-06):**
two of Kalshi's weather cities (Houston, Chicago) each have two real
candidate airports, and this project's ticker alone could not say
which one Kalshi settles against. RESOLVED via two independent real
sources: a Houston Chronicle article about an actual executed Kalshi
weather trade naming "William P. Hobby Airport" explicitly, and a
third-party Kalshi weather-data vendor's own published station
mapping, which separately confirmed Houston=Hobby (KHOU) AND
Chicago=Midway (KMDW) — the latter corrected this project's own
original placeholder guess (O'Hare), caught before it reached any
real sizing decision. See `station_map.py`'s module docstring.
31. **New, opened and RESOLVED same session, Session 4.1 (2026-09-06):**
a real, live comparison of this project's own NWS-based daily
high/low against Kalshi's actual settlement record (Philadelphia,
2026-09-05) found a small gap (0.2–0.9°F). Investigated directly
against real 5-minute-resolution station data: the gap is explained
by Kalshi's settlement feed storing one rounded, whole-degree value
per clock hour, while this project's pipeline keeps exact-decimal,
5-minute-resolution readings. This bounds the real gap at
approximately ≤1°F (one rounding step), not an open-ended or
unexplained divergence. **Action for Session 4.2:** treat this
project's own forecast/observation numbers as accurate to
approximately ±1°F relative to Kalshi's actual settlement value by
design, and treat any contract whose threshold sits within that
band of this project's estimate as a named, lower-confidence edge
case rather than a silent risk. See
`docs/nws_settlement_gap_resolution.md` for the full evidence trail,
including a second, separate finding (a manual verification script's
own timezone-conversion bug, unrelated to and now ruled out as a
cause of this gap) resolved in the same investigation.

32. **New, opened and RESOLVED same session, Session 4.2 (2026-09-07):**
the roadmap card's "GFS ensemble spread" wording assumed ensemble
data would be available. Checked live before writing any model code:
NWS's public API (this project's confirmed data source since
Session 4.1) returns exactly one deterministic forecast value per
station per day — no ensemble, no published confidence interval.
RESOLVED via a real, automated blend rather than either extreme
(blocking on a real backtest history that didn't exist yet, or
silently guessing a placeholder forever): a literature-sourced
starting curve (Penn State's public course material, cited with the
exact real anchor points used, see
`weather_estimation_model_spec.md`) is used immediately, while a new
daily pipeline (`weather_calibration_pipeline.yml`) builds this
project's own real, measured forecast-error history in the
background; the model automatically swaps to real numbers per
lead-day bucket once each one crosses a named minimum real sample
size (20) — no future session needs to remember a manual cutover.
33. **New, opened and RESOLVED same session, Session 4.2 (2026-09-07):**
the first real run of the new calibration pipeline
(`weather_forecast_error.py`) produced an implausible same-day
forecast error (4.3°F MAE, already over the model's own real-data
trust threshold) — root-caused to comparing full-day forecasts
against still-in-progress "observed so far" readings for the current
day, not a real, finished answer. RESOLVED: an observed reading is
only trusted once pulled at least 32 hours after its own date's UTC
midnight (covers every real target station's local day-end,
including the latest-closing West Coast ones). Corrected same-day
MAE after the fix: a real, plausible 1.7°F with near-zero bias. See
SESSION_LOG.md's Session 4.2 entry for the full real evidence.
34. **New, opened and RESOLVED same session, Session 4.2 (2026-09-07):**
`weather_backtest_check.py`'s first version gated on guessed Kalshi
market-status values (`"finalized"`/`"settled"`) that had never been
confirmed against a real API response. A real, direct check of one
live market (`KXLOWTMIN-26SEP06-T69`) showed Kalshi's real status
reads `"closed"` well before the real `result` field is populated
(which can sit as an empty string for hours after trading closes) —
neither guessed value was real. RESOLVED: gate solely on a real,
non-empty `result` field instead of a guessed status string.
35. **New, opened, NOT YET RESOLVED — carried forward from Session
4.2:** the roadmap's resolved-market sanity-check validation item was
genuinely blocked on Kalshi's own real settlement clock (~19:00 UTC /
2:00 PM CDT, 2026-09-07). **RESOLVED same day, ~20:04 UTC / 3:04 PM
CDT:** re-ran `weather_backtest_check.py` after real settlement — 228
real resolved contracts checked, 81.58% directional accuracy, Brier
score 0.1342 (vs. a 0.25 coin-flip baseline). Session 4.2 is fully
closed; see SESSION_LOG.md's Session 4.2 (continuation) entry.
36. ~~New, opened, NOT YET RESOLVED — Session 5.1 (2026-09-07): Polymarket's
title format for state-legislature races is unconfirmed...~~ **Resolved
2026-09-09.** Checked live, directly against Polymarket's public-search
API, for three real Kalshi state-legislature races (Missouri State
Senate District 8 — Keri Ingle vs. Jon Patterson; Maryland State Senate
District 2; Pennsylvania State House District 12), queried by district
name, both real candidate names, and generic terms. Every query returned
only unrelated fuzzy matches (e.g. "Missouri State" college sports,
"Paul" name collisions) — zero real Polymarket markets for any of these
races. Confirms this is not a matcher bug: **Polymarket simply does not
list individual state-legislature races.** `ingest_politics_markets.py`'s
absence of matches for this tier is correct behavior, not a gap to fix.
37. ~~When more than one Polymarket market matches the same down-ballot
race_id, `ingest_politics_markets.py` kept whichever row appeared first,
arbitrary.~~ **Resolved 2026-09-08 (Session 5.1c):** the "keep first" logic
was the direct symptom of the deeper candidate-identity problem found this
session — every open market per race is now captured and matched to a
specific party by real candidate name (Kalshi) or by the party word stated
directly in the market title (Polymarket), so there is no longer an
arbitrary tie-break: each party gets its own matched market, not one
arbitrary pick per race. Confirmed live: 427/427 races matched both a
Dem and a Rep Polymarket market on the second live run, after a real bug
in the first live run (0/3,416 matched — Polymarket's titles name the
party directly, not a candidate) was found and fixed.
38. **New, opened, NOT YET RESOLVED — Session 5.1 (2026-09-07):**
`MIN_LIQUID_KALSHI_CONTRACTS` (10.0) and `MIN_LIQUID_POLYMARKET_DOLLARS`
(100.0) in `ingest_politics_markets.py` are named starting values, not
yet calibrated against real down-ballot order-book behavior. **Action:**
revisit once enough real down-ballot order-book history exists to check
them against, same pattern as Session 3.2's sizing-constant validation.
39. ~~New, opened, NOT YET RESOLVED — Session 5.2 (2026-09-08): the politics
estimation spec doc landed at `/docs/politics_estimation_model_spec.md`
instead of `/docs/research/politics_estimation_model_spec.md`...~~
**Resolved 2026-09-09.** Checked live: the file is already at
`/docs/research/politics_estimation_model_spec.md`, alongside the
weather and pick'em specs — no move needed. This entry was already stale
by the time it was checked.
40. **New, opened, NOT YET RESOLVED — Session 5.2 (2026-09-08):** the
politics estimation model's own "sanity-check against historical
resolved down-ballot markets" validation item could not be completed —
no real down-ballot contracts have resolved yet this cycle
(`GENERAL_ELECTION_DATE` is roughly two months out from this session).
**Action:** revisit once real resolved down-ballot contracts exist
post-election, same deferral pattern Track 4 (weather) used for its own
settlement-dependent check.
41. **New, opened, NOT YET RESOLVED — Session 5.2 (2026-09-08):**
`STATE-LEG-CA-SENATE-26` surfaced a real, structural gap: California's
top-two/nonpartisan-blanket-primary system can put two candidates from
the same party on the general-election ballot, but ElectIndex's own
per-race data only tracks one name as "the Democrat" and one as "the
Republican." A real second Democrat in that race (Wendy Carrillo)
correctly could not be matched to either ElectIndex slot and is
logged in `kalshi_unmatched_candidates` rather than guessed — not a
matching bug, a real limit of ElectIndex's two-party framing in
nonpartisan-primary states. **Action:** no fix planned; revisit only if
this project's scope ever needs correct handling of same-party general
elections specifically.
42. **New, opened, NOT YET RESOLVED — Session 4.3 (2026-09-08):** the
roadmap's "at least one real week of logged weather flags reviewed for
completeness" validation item could not be met — weather's CLV log did
not exist before this session, so no real elapsed time across repeated
runs exists yet to review. Following this project's own established
pattern (Sessions 2.1/2.2/2.4), a real-week-equivalent evidence-based
condition was considered but not substituted, since no repeated runs
exist yet to derive one from. **Action:** revisit once weather's
`clv_logger.py` has run automatically over real elapsed time — tied
practically to Session 4.5 (Automation Adaptation), or several manual
runs spread over real days in the meantime.
43. ~~New, opened, NOT YET RESOLVED — Session 4.3 (2026-09-08): a real
dtype-coercion bug was found and fixed in the new weather/politics CLV
code (`load_clv_log_generic()`)...~~ **Resolved 2026-09-09.** Checked
`data/pickem/clv_log.csv` directly: confirmed the risk was real, not
theoretical — `consensus_platform`, `consensus_source_line_id`,
`consensus_line`, `consensus_implied_prob_same_side`, and
`consensus_edge` were all still `float64` after 6,850 real rows (no
cross-platform match has landed yet). Patched `load_clv_log_pickem()`
with the same object-dtype-on-load fix already applied to
`load_clv_log_generic()`. Verified: writing a real string into a
previously-blank column now succeeds where it previously raised
`TypeError`. Note: `test_clv_logger.py` fails on a run, but this was
confirmed via `git stash` to be a pre-existing, unrelated bug — the test
writes against the real production `clv_log.csv` path instead of a tmp
fixture — not caused by this fix.
44. **New, opened Session 2.9 (2026-09-09):** Track 1's live paper-trading
checkpoint closed on an explicit **NO-GO for real capital**, for one
specific, narrow reason — no real bet has ever been placed and reported,
so `outcome_log.csv` does not exist and there is no real graded win/loss
data to evaluate against the CLV proxy. This is not a finding that the
model or CLV signal is bad; it is a finding that the evidence this
checkpoint needs doesn't exist yet. The CLV-close sample-size threshold
(≈3,725, per Session 2.5) IS cleared (3,845 real closed flags as of
2026-09-09), but cross-platform consensus has still never fired even
once across all 6,850 real logged flags — own-line-movement is the only
real signal available, and per Session 2.4's own documented limitation,
a static line not moving (or moving) is not itself proof of directional
accuracy. User explicitly confirmed (Session 2.9) they are deliberately
holding off on placing real bets until confidence is established — a
reasonable, deliberate choice, not an oversight. **Action needed to
re-trigger this checkpoint:** once the user places a small number of
real test bets and reports each result via
`outcome_tracker.py --record`, run `weekly_review.py --run` for the
first time ever on real data, and once enough real graded legs
accumulate, re-run this go/no-go review against real outcome evidence
instead of CLV alone.
45. **Resolved, Session 2.11 (2026-09-10).** Underdog's real 2-pick
Standard-entry payout (3.5x, sourced directly from Underdog's own help
article — see Session 2.11's card and SESSION_LOG.md for the full trail)
is now wired into `sizing_engine.py` (per-platform `ENTRY_PAYOUT_MULTIPLIER`/
`ENTRY_NET_ODDS_B`/`BREAKEVEN_WIN_RATE`) and `frontend/app.js`. One piece
remains open, not closed silently: no real, currently-open 2-leg Underdog
entry exists in live data to verify the sizing output against Underdog's
own app directly (only one real Underdog row total exists in
`clv_log.csv`, and it is closed) — re-verify this specific check once
Underdog's real ingested volume produces two real simultaneous open legs
(tracked as the same kind of volume gap Session 2.10 already documented
for Underdog).
46. **Resolved, Session 6.8 (2026-09-10).** FanDuel is not structurally
excluded from flagging — `clv_logger.py`/`sportsbook_props_model.py`
apply identical logic to both platforms. Every real row is `draftkings`
today for two real, temporary reasons instead: the pipeline's
`--season 2025` default plus Session 6.6's (correct) stale-season-stats
guard shut out every FanDuel row, and nflverse's real 2026 weekly file is
still too sparse (67 rows) to name-match most current players even when
tested directly against `--season 2026`. No code changes needed — the
gap closes on its own as the season's real data accumulates. One item
remains open, not closed silently: no real, non-bogus FanDuel-flagged row
has been observed end-to-end yet — re-verify per Session 6.8's own
Decision #2 once nflverse's 2026 file has meaningfully more rows.
47. **New, opened 2026-09-10, same request:** BetMGM and Caesars have zero
ingestion code today — the user asked to reassess adding them. Per this
project's own standing practice (no venue gets built out without a real,
reproducible endpoint check first — see Session 2.1's DK Pick6 outcome),
this is scoped as two separate feasibility sessions before any real build
work. **Action needed:** Sessions 6.9 (BetMGM) and 6.10 (Caesars), both new,
added this session.
48. **Resolved (BetMGM half), Session 6.9 (2026-09-10). Real, unexplained
technical wall found on BetMGM's own site**, plus an explicit ToS anti-
scraping clause — see full session entry for the honest account of what
was and wasn't confirmed about the exact mechanism (later corrected away
from an unverified "it's GeoComply" claim to "confirmed blocked, exact
cause not proven from the code"). Direct BetMGM access is a no-go.
49. **New finding, same day, same session: Rotowire has real, complete
BetMGM prop data, reachable for free.** Traced how third-party sites
(Rotowire, Action Network) show BetMGM's lines despite the direct no-go —
they're not calling BetMGM's own gated surface; BetMGM (and other books)
choose to distribute their lines to free comparison/media sites as a
customer-acquisition channel, a structurally different distribution path.
Confirmed both Rotowire and Action Network work this way and are free;
Rotowire has fuller BetMGM props coverage (every player row, every stat,
via `mgm_<stat>`/`mgm_<stat>Over`/`mgm_<stat>Under` fields) vs. Action
Network's props tool (shows only one "best" book per prop, not
selectable — BetMGM appeared in 0 of 970 sampled real rows). Both carry
the same explicit "no bots/scrapers/spiders" ToS language BetMGM's own
site does. User chose Rotowire, accepting that ToS situation as
consistent with how this project already treats DK/FD's own undocumented-
endpoint ingestion. Built `scripts/ingestion/ingest_rotowire_betmgm_props.
py`, ran it live (377 real BetMGM prop rows, a real classification bug
found and fixed mid-build — see SESSION_LOG.md), and wired its output into
`sportsbook_props_model.py`'s `load_props()` and `clv_logger.py`'s
consensus-matching (which was itself hardcoded to a draftkings<->fanduel
binary and needed generalizing for a real third platform). Caesars
(Session 6.10) is unaffected and must still be checked independently —
this same Rotowire/Action-Network path may or may not apply to it and
should not be assumed.
50. **CLV logging hook-in for BetMGM, same day (2026-09-10).**
`clv_logger.py`'s props pipeline was already fully platform-generic
(Session 6.3, plus decision #49's own N-platform consensus fix) — no new
CLV-logging code needed structurally. But BetMGM had nothing real to log:
its raw Rotowire stat keys (`anytd`, etc.) weren't registered in the
estimation model's TD-market lookup, so every BetMGM row fell into
`unsupported_stat_type` — fixed in `sportsbook_props_model.py`. Running
the real pipeline end-to-end then surfaced two more real, pre-existing
consensus-matching bugs, neither caused by BetMGM but both first exposed
by it: (1) the match key included each platform's own internal `game_id`,
which structurally can never coincide across platforms — confirmed 0 of
154 real pre-existing DraftKings flags ever had a real consensus match
before this fix; fixed by dropping `game_id` (safe for NFL: one real open
game per player at a time). (2) every TD-scorer-shaped market (Anytime/
2+/First/Last) shares one `resolved_stat_key`, so matching on that alone
produced real "consensus_available=True" flags with a blank
`consensus_price` (matched to the wrong TD-market type); fixed with a
narrow TD-market-kind disambiguator, scoped only to TD-composite stats.
Real result: 291 BetMGM rows now reach `estimated` (up from 0), 210
newly flagged into `clv_log.csv`, 104 with a real cross-platform
consensus check, 94 with a real non-blank consensus price. Full trail
in SESSION_LOG.md.
51. **Sizing adaptation for BetMGM, same day (2026-09-10).**
`sizing_engine.py`'s props Kelly-sizing math was already generic; BetMGM
was blocked by one explicit allowlist (`PROPS_SUPPORTED_PLATFORMS`).
Added `betmgm` to that set and to `PROPS_PLATFORM_RISK_MULTIPLIER` at the
same 0.50 account-limiting dampener DK/FD already carry (no project
source distinguishes the three). Named, but deliberately did NOT invent
a number for, a real distinct consideration: BetMGM's price here comes
via Rotowire's copy of BetMGM's line, not a live BetMGM pull — freshness
unmeasured, flagged for Session 8.3. Verified against the real, live CLV
log end-to-end (`betmgm|16808`, Jahmyr Gibbs, real $25 suggested stake
on $500 bankroll, capped at the standard 5% ceiling) and with a new test
(`test_18b`) proving BetMGM sizes identically to DK on identical inputs.
Full trail in SESSION_LOG.md.
52. **Automation adaptation for BetMGM, same day (2026-09-10).** Extended
`scripts/run_props_pipeline.py` (the orchestrator `props_pipeline.yml`
runs on a schedule) from two ingestion feeds to three: added `run_rw_
ingestion()` calling `ingest_rotowire_betmgm_props.run()`, and widened
the early-stop guard so it only stops if DK, FD, AND BetMGM all return 0
rows (was: DK and FD only). No new GitHub Actions step needed — BetMGM's
ingestion uses plain `requests`, not a browser, so it rides inside the
existing `xvfb-run`-wrapped call. Ran the full real pipeline end-to-end:
DK 680 rows/FD 129 rows/BetMGM 377 rows, all three feeding one combined
estimation+CLV run, real BetMGM flags (e.g. Chase Brown `anytd`, edge
0.5729) correctly ranked alongside real DraftKings flags in the digest.
Also restated Rotowire's ToS caveat directly in the workflow file itself
(not just the ingestion script), since running it on a recurring schedule
is a real, ongoing instance of that same open question, not a smaller
one. Full trail in SESSION_LOG.md.
53. **Frontend integration for BetMGM, same day (2026-09-10) — closes
the seven-stage build for this venue.** The Props tab's table logic
(Session 6.6) was already platform-generic; the only real gap was
hardcoded "DraftKings + FanDuel"-only copy in `frontend/index.html`/
`frontend/app.js`, fixed to name all three platforms. Tested live in a
real browser (new `.claude/launch.json`, none existed before): real
BetMGM rows correctly interleave with DraftKings rows sorted by edge,
carry the same risk badge, and honestly show "—" for `Game time` — a
real, named, un-fixed gap (Rotowire's player-props page carries no
kickoff-time field; the Blocked-badge convenience doesn't fire for
BetMGM rows, though the underlying CLV close-on-disappearance safety
mechanism is unaffected). Full trail in SESSION_LOG.md.
54. **Resolved, 2026-09-11 — real production incident found and fixed:
the automated Pick'em Pipeline (GitHub Actions) had been failing on
EVERY scheduled run for ~3 days straight (2026-09-08 14:29 UTC through
2026-09-11), with zero new flags logged for either platform in that
entire window.** Root cause: Session 5.2 (2026-09-08) renamed
`clv_logger.py`'s flat `run()` to `run_pickem()` when generalizing the
module for weather/politics/props (each track got its own `run_<track>()`
entry point), but `scripts/run_pipeline.py`'s call site
(`clv_module.run(estimates_path)`) was never updated to match — every
run after the rename crashed with `AttributeError: module 'clv_logger'
has no attribute 'run'` at the CLV-logging stage, after ingestion and
estimation had already completed successfully, so nothing looked wrong
until the final commit step silently never happened. Found by reading
the actual GitHub Actions failure log the user pulled directly (this
environment has no Actions/API access of its own) — the crash traceback
named the exact bad call site. Fixed with a one-line change
(`clv_module.run(...)` → `clv_module.run_pickem(...)`) plus a docstring
note at the call site explaining why, so a future rename doesn't
reintroduce the same gap silently. Verified by running the real pipeline
end-to-end locally: it completed all 3 stages and wrote 702 real new
flags to the live `clv_log.csv` (open count rose from 3,005 to 4,518) —
the first successful pick'em pipeline run since the outage began. This
is why PrizePicks flags looked normal on the frontend throughout the
outage (thousands of pre-existing open rows masked the staleness) while
Underdog showed zero (it has never had more than one flag total — see
#55).
55. **Resolved, 2026-09-11, same day — Underdog's real endpoint found and
fixed; the block in the first half of this entry is now historical, not
current.** After eight guessed headers and a version sweep (v3-v8, all
gated or 404) failed, the user asked to keep pursuing it rather than drop
it. Found the real answer by inspecting Underdog's own live webapp
directly (app.underdogsports.com, via browser) rather than guessing
further: its bundled JS names the current real path outright —
`sW={regular:"/v1/over_under_lines", live:"/beta/v2/live_over_under_lines"}`
— Underdog dropped the `beta` prefix entirely for its main feed, a full
endpoint restructure, not a version bump or a header gate. Confirmed
directly via `curl`:
`https://api.underdogfantasy.com/v1/over_under_lines` returns HTTP 200
with 14,076 real `over_under_lines` rows (vs. ~250 on the dead `beta/v3`
path — roughly 50x more real inventory), in the exact same JSON shape
`normalize_underdog()` already expected (confirmed field-by-field:
`over_under.appearance_stat`, `options[].choice`/`payout_multiplier`,
`players[].first_name`/`last_name`/`sport_id`, `games[].scheduled_at`/
`sport_id` all present and unchanged) — so the fix was a one-line URL
change in `ingest_pickem.py` (`UNDERDOG_ENDPOINT`), no normalizer
changes needed. **Verified end-to-end on real, live data**: ingestion
pulled 14,077 real Underdog rows; the full pipeline
(`run_pipeline.py --season 2025`) ran clean and flagged **547 real, open
Underdog opportunities** (real players — James Cook, Josh Allen — real
NFL stat types, real edges) into the live `clv_log.csv`. This also
closes Session 2.11's own deferred validation item: sized a real,
live 2-leg Underdog entry
(`underdog|a5fbbed4-...` + `underdog|883a47f2-...`) — correctly resolved
`entry_type: "2-pick Standard"`, real 3.5x payout, 0.85 platform
dampener, `$2.42` suggested stake on a $500 bankroll. Underdog is fully
live again, not dropped.
56. **Resolved, 2026-09-11 — the "no automated redeploy follows a
`[skip ci]` pipeline commit" gap (first flagged as an open item back in
Session 3.5's SESSION_LOG entry, never previously promoted to a numbered
decision here) is now closed for real, project-wide.** This gap is what
caused the very confusion #54/#55 above surfaced from the user's side:
after fixing Underdog's ingestion, the live frontend still showed stale
data because the pipeline's own data commit is tagged `[skip ci]` (by
design, to avoid an hourly bot commit re-triggering the same GitHub
Actions workflow) — and Cloudflare Pages, it turns out, honors that same
tag and silently skips auto-deploying that commit too. Confirmed
directly: the live site's served `data/clv_log.csv` matched an EARLIER
commit's exact byte count, not the latest one, proving the real fix's
data had never actually reached production. Fixed by adding a Cloudflare
Pages **Deploy Hook** (a URL that starts a deploy regardless of git
metadata) — the user created one in the Cloudflare dashboard and stored
it as the GitHub Actions repository secret `CF_PAGES_DEPLOY_HOOK_URL`.
All five data-producing pipeline workflows (pick'em, weather, props,
arbitrage, politics — the two non-frontend workflows, weather
calibration and the sport-inventory scan, don't need it) now `curl -X
POST` that secret as their final step, gated on the commit step actually
having pushed something (`steps.commit.outputs.committed == 'true'`,
newly added to each commit step) so a genuinely no-op run doesn't trigger
a pointless rebuild. Every future pipeline run now redeploys the live
frontend automatically, `[skip ci]` or not — this was previously named
as "Greg's call, not applied unilaterally" (Session 3.5); the user's
explicit direction this session ("set up the deploy hook now") is that
call being made.

---
*Update this file at the close of each future session, per the project's
standing convention: ROADMAP.md and SESSION_LOG.md are only updated once both
sides agree a session is fully closed out, or remaining pieces are being
deliberately deferred to a later session (and that deferral is stated
explicitly, not silently dropped).*
