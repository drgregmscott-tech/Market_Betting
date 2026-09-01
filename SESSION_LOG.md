# Session Log

Update this after completing every session — before closing that session, not
later. This is what makes the next session's handoff possible without
re-explaining the whole project.

This file records what was actually built, validated, and decided in each
session. It is the source of truth for handoff context. Every session entry
should be complete enough that a fresh session — given only this file and the
relevant ROADMAP.md card — can pick up exactly where the last one left off.

**Log standard: every entry includes:**
- Date completed
- What was built/decided (files created/modified, or — for explore sessions —
  conclusions reached)
- Validation results (pass/fail, with specifics)
- Decisions made (numbered, with reasoning)
- Open items / deferred items
- Any corrections or reversals along the way, and why

**Log entry template (copy this for each new session):**

```
## Session [X.X] — [Session Name]

**Date completed:** [date]
**Status:** ✅ Complete / ⚠️ Complete with caveats / ❌ Blocked

**What was actually done:**
(brief description — note any deviation from what the roadmap card said; drift is
normal and expected, just record it)

**Files created/modified:**
(exact paths — copy from the roadmap card, correct if it changed)

**Validation results:**
(pass/fail for every checkbox on the roadmap card, with the actual numbers/output,
not just "passed")

**Decisions made:**
(numbered list, with reasoning — future sessions need to know WHY, not just WHAT)

**Corrections/reversals during the session:**
(if any — what the original plan was, what changed it, why)

**Open items / deferred validations:**
(anything not fully closed — be explicit about what's deferred and to which future
session it's tied)
```

---

**Confirmed scope going into Session 0.1** (from an initial explore
conversation, dated 2026-08-28): user has three existing DFS optimizer repos
(NFL, NHL, PGA) and wanted to explore whether a related but distinct
betting/prediction-market analysis project was realistic. Kalshi/Polymarket
were raised as an initial example, explicitly not a hard boundary. No rush to a
build plan going in — this was declared an explore session from the start.

---

## Session 0.1 — Viability Assessment & Scope Definition

**Date completed:** 2026-08-28
**Status:** ✅ Complete

**What was actually done:**
An extended explore session covering feasibility, architecture, validation
methodology, and final scope. No code written, no repo created. Full flow:

1. Assessed general feasibility of a betting/prediction-market +EV system.
   Initial framing ("edge odds are the same as anyone else without
   institutional infrastructure") was corrected after the user pushed back —
   professional sharp bettors demonstrably exist, so the real question is
   *where* edge is findable, not whether it exists.
2. Reviewed the existing `DFS_Optimizer` and `DFS_Optimizer_NHL` repos directly
   via browser to identify the reusable architecture: data ingestion →
   projection/blend engine → ILP optimizer → ownership/chalk-score logic →
   GitHub Actions/Cloudflare automation → Cloudflare Pages frontend. Confirmed
   via the NHL sibling that this pattern was already proven portable once.
3. Decided explicitly to fork the architectural *pattern*, not the codebase —
   new repo, new code throughout, guided by the proven pattern.
4. Defined the calibration loop (predict → store → observe outcome → grade →
   recalibrate) as the system's core design principle, inspired directly by the
   DFS repos' own recalibration scripts (e.g. `fit_sigma_recalibration.py`).
5. Scoped candidate market categories directly from Kalshi's live category list
   (pulled via browser: Trending, Elections, Politics, Culture, Sports, Crypto,
   Commodities, Climate, Economics, Mentions, Finance, Tech & Science). Ranked
   by professional attention vs. available public ground truth. User approved:
   Sports, Climate/Commodities, and narrow/down-ballot Elections/Politics in;
   Culture/Mentions/Tech and Economics/Finance/Crypto out.
6. Ran a full Advanced Research task (task_id
   `wf-c7c4a5ee-76ef-5974-9f4c-6beb29ac8e8a`) synthesizing modeling techniques
   and market-efficiency evidence across the three in-scope domains plus
   Kalshi/Polymarket-specific arbitrage findings. Report title: *"Building a +EV
   Prediction-Market System: Edge-Detection Across Sports, Weather, and
   Down-Ballot Politics."*
7. Assessed the research findings directly against a "reasonable expectation of
   edge" bar, rather than treating the existence of a research report as
   sufficient on its own. This produced a real reordering of confidence by
   track (see Decisions below).
8. Tested the "target less-popular sports / more obscure prop bets" hypothesis
   directly against Kalshi's live market catalog (via browser). Found Kalshi's
   real props are coarse/banded and concentrated on high-volume games, not
   obscure ones — refined the hypothesis rather than confirming or discarding
   it outright.
9. Assessed whether sports scope should expand to traditional sportsbooks
   (DK/FD). Found a direct vig comparison (~0.85% Kalshi vs. ~4.62%
   sportsbooks, one study) and documented account-limiting risk for consistent
   winners on sportsbooks, neither of which apply to exchanges the same way.
10. User challenged the sportsbook conclusion with real-world counter-evidence
    (professional bettors profit on DK/FD/PrizePicks/Underdog daily).
    Researched this directly. Found PrizePicks/Underdog/DK Pick6 are legally
    daily-fantasy pick'em products with static, non-repricing lines — a
    structurally different, more favorable mechanism than either a sportsbook
    or an exchange — and elevated this to its own high-confidence track.
11. User corrected total scope framing: Kalshi/Polymarket were only ever an
    illustrative starting example, not a hard boundary. Re-ranked the full
    track list under genuinely open scope (any venue, evaluated on its own
    merits).
12. Final viability check, explicit: is this viable, and is scope defined?
    Concluded yes to both — "viable" defined precisely as a real mechanism plus
    a real, evidence-based way to grade the system's own performance, not a
    guarantee of profit.
13. Session moved into build-planning. Produced this SESSION_LOG.md and the
    accompanying ROADMAP.md.
14. **User flagged a language problem in the first draft of these documents**:
    the phrase "the goal is not guaranteed winning bets" read like a legal
    disclaimer and created risk that future sessions could use "nothing's
    guaranteed" to rationalize weaker decisions (skipped validation, a
    under-researched model, lower standards) rather than as a true statement
    about probability. Corrected: ROADMAP.md's Background & Approach section
    now states the goal as identifying bets more likely to be right than
    emotional or poorly-researched ones, and explicitly states that "no
    guarantees" must never be used to justify a lower bar — see that section
    for the exact standing rule.
15. **User requested the ROADMAP/SESSION_LOG format itself be rebuilt to match
    the actual DFS sibling repos' structure** (phase/session cards, status
    markers, validation checklists, numbered decisions) rather than the
    freeform sections used in the first draft. Both files rebuilt accordingly.
16. **User supplied the S&P 500 analogy** to sharpen the goal statement further:
    a 10-year S&P 500 chart has real drawdowns but an overall positive
    trendline — that is the exact shape of result this project should aim to
    produce, per track, over a real sample. Added to ROADMAP.md's Background &
    Approach section as the project's explicit north star, directly beneath
    the "no guarantees ≠ lower bar" rule from item 14.
17. **User resolved Open Decision #1 (v1 track) by asking for a structural
    assessment** rather than stating a preference — specifically, whether any
    track is more foundational to build first because it makes the others
    easier. Assessed: cross-venue arbitrage skips the estimation layer
    entirely (pure price comparison), so building it first wouldn't prove out
    the calibration/CLV loop the rest of the roadmap depends on. Weather and
    politics both need a new estimation engine built from scratch. Fixed-line
    pick'em platforms need an estimation engine too, but it's a near-direct
    reuse of the existing, proven DFS projection pattern — making it the
    track that exercises the full five-layer stack end-to-end at the lowest
    risk. **Decision: Fixed-Line Pick'em Platforms is the v1 track**, chosen
    on structural grounds, not confidence ranking (it was already tied for
    second-highest confidence, but that was not the deciding factor).
18. **User resolved Open Decision #2 (repo name): `Market_Betting`.** No
    strong preference stated beyond "simple and makes sense" — adopted as
    given.
19. **Open Decisions #3, #4, and #5 (data source access, account-limiting
    verification, concrete estimation model spec) deliberately left
    unresolved**, per explicit user direction, to be figured out in a future
    session once real investigation (not conversation) can settle them —
    matching the same pattern PGA's Data Golf decision followed.

**Files created:**
- `ROADMAP.md` (repo did not exist yet at time of writing — file was
  provisional, moved into the real repo at Session 1.1)
- `SESSION_LOG.md` (same — provisional until Session 1.1)
- Research artifact (project file, not yet in a repo at time of writing):
  *"Building a +EV Prediction-Market System: Edge-Detection Across Sports,
  Weather, and Down-Ballot Politics"*

**Validation results:**
- PASS: A real, evidence-backed mechanism was identified for every in-scope
  track — not merely asserted as plausible. See ROADMAP.md's Track Reference
  table and the research artifact for full sourcing.
- PASS: A defined, pre-outcome validation methodology (CLV-equivalent,
  adapted from professional sports-betting practice) was identified and is
  specified as mandatory from the first version of any track's estimation
  model — not deferred to "after it's built."
- PASS: Scope is explicitly ranked by confidence (six tiers), not left as an
  unordered wishlist.
- PASS: Out-of-scope categories are named with explicit reasoning (Culture/
  Mentions/Tech, Economics/Finance, Crypto), so a future session doesn't have
  to guess whether they were considered and rejected or simply overlooked.

**Decisions made:**
1. Fork the DFS_Optimizer architectural pattern, not the codebase — this is a
   new repo with new code, guided by a proven pattern.
2. The calibration loop (predict/store/grade/recalibrate) is the system's core
   design principle from v1 — not a feature added after the fact.
3. CLV-equivalent pre-outcome validation is the primary methodology; outcome
   backtesting is a downstream confirmation step, not the first validation
   tool used.
4. Scope is genuinely open across venues (exchanges, sportsbooks, pick'em
   platforms), evaluated per-venue on: repricing mechanism, fee/vig cost,
   account-limiting risk, liquidity, and legal footprint.
5. Final ranked track order (highest to lowest confidence): cross-venue
   arbitrage → fixed-line pick'em platforms → Kalshi/Polymarket weather/
   climate → Kalshi/Polymarket down-ballot politics (narrow only) →
   sportsbook props → sportsbook main lines/flagship exchange sports markets.
6. Explicitly out of scope: Culture/Mentions/Tech & Science, Economics/
   Finance, Crypto.
7. "No guarantees" language is a statement about probability only, never a
   justification for lower rigor — codified as a standing rule in ROADMAP.md,
   not left as an implicit understanding.

**Corrections/reversals during the session:**
1. **Backtesting-first → methodology-research-first.** Original plan was to
   validate via backtesting against historical data. Corrected: backtesting
   confirms an already-sound methodology, it doesn't establish one.
   Methodology research (leading to CLV-equivalent validation) had to come
   first.
2. **Infrastructure-readiness ranking → edge-confidence ranking.** Original
   assumption ranked Sports first because existing DFS tooling is most
   reusable there. Evidence-based research reordered this — arbitrage and
   weather rank above sports, because research showed sports edge exists only
   in narrow soft corners, not broadly.
3. **"Sports" as one track → split into several tracks with different
   confidence levels.** Initially treated as a single category. Splitting
   into flagship lines (lowest confidence), sportsbook props (moderate), and
   fixed-line pick'em platforms (high confidence) was the direct result of
   testing the user's real-world counter-example against research rather than
   dismissing it.
4. **Kalshi/Polymarket as scope boundary → Kalshi/Polymarket as starting
   example only.** User corrected this explicitly; scope was reframed as
   fully open, venue evaluated on its own merits.
5. **"Obscure props/less popular sports" hypothesis → "coarse banding on
   high-volume games" hypothesis.** Checked directly against Kalshi's live
   catalog rather than accepted or dismissed on reasoning alone; the real
   catalog data pointed somewhere more specific than the original idea.
6. **"Goal is not guaranteed winning bets" → goal is identifying bets more
   likely to be right than emotional/unresearched ones, with no-guarantees
   explicitly barred from being used to justify lower rigor.** User-flagged
   correction to the first draft of these very documents (see item 14 above).

**Open items / deferred validations:**
- ~~Which single track becomes the actual v1 build~~ — resolved: Fixed-Line
  Pick'em Platforms (see Decisions #17 and ROADMAP.md).
- ~~Repo name~~ — resolved: `Market_Betting`. Visibility (Private) and actual
  repo creation completed at Session 1.1.
- Data source/API access research per track, especially PrizePicks/Underdog,
  which has no established public API the way an exchange does — genuinely
  unresearched (Open Decision #3).
- Verifying account-limiting policy per pick'em platform directly rather than
  relying on secondhand characterization (Open Decision #4).
- Defining the first concrete estimation model for whichever track is chosen,
  at the same level of specificity as the existing DFS projection engines
  (Open Decision #5).

**Status at close of session:** Fully closed out on the viability/scope
decision. No repo exists yet. Next session should start from ROADMAP.md's Open
Decisions list, beginning with which track becomes v1.

---

## Session 1.1 — Environment & Repo Setup

**Date completed:** 2026-08-28
**Status:** ✅ Complete

**What was actually done:**
1. Confirmed via Claude in Chrome (browsing GitHub.com directly) that the
   `Market_Betting` repo did not yet exist under the user's account — only
   `DFS_Optimizer`, `DFS_Optimizer_NHL`, `DFS_Optimizer_PGA`,
   `family-budget-app`, `pharmentor-repo`, and `Scott-Family-Hub` were present.
2. Got explicit user confirmation before taking the account-changing action of
   creating a new repository (per this environment's permission rules for
   account-settings changes), then created `drgregmscott-tech/Market_Betting`
   directly on GitHub.com: private visibility, no README/gitignore/license
   auto-added (those were supplied as hand-built files instead, to match the
   DFS sibling repos' actual conventions rather than GitHub's generic
   defaults).
3. Built the full Session 1.1 file set locally (in Claude's own workspace,
   not directly on GitHub — per the user's standing workflow preference of
   receiving files to place and push manually via GitHub Desktop):
   - `requirements.txt` — `pandas`, `numpy`, `requests`, `python-dotenv`
   - `.gitignore` — standard Python/editor/OS ignores, plus
     `config/api_keys.env` and `*.env` (secrets), plus working contents of
     `/data`, `/output`, `/logs` (each kept alive via `.gitkeep`)
   - `README.md` — project summary, pointers to ROADMAP.md/SESSION_LOG.md/
     docs/research, repo structure diagram, setup instructions
   - `config/api_keys.env.example` — template for the real, gitignored
     `config/api_keys.env`, documenting the venue credential fields expected
     (Kalshi, Polymarket; pick'em platforms noted as unresearched, tied to
     Open Decision #3)
   - Folder structure: `/data`, `/scripts`, `/output`, `/logs`,
     `/docs/research`, `/config`, each populated with a `.gitkeep` placeholder
     so empty folders survive being pushed to Git (Git does not track empty
     directories on its own)
   - Session 0.1's research artifact copied into
     `/docs/research/Building_a_+EV_Prediction-Market_System_Edge-Detection_Across_Sports_Weather_and_Down-Ballot_Politics.md`
4. Verified locally (in Claude's own sandboxed environment, Python 3.12.3)
   that `pip install -r requirements.txt` resolved cleanly with no conflicts,
   as a first-pass sanity check before handoff.
5. Delivered all files to the user with an explicit destination path for each,
   per the project's standing file-handoff convention.
6. **GitHub Desktop first-time-publish issue, worked through live with the
   user:**
   - User placed the files locally and ran `pip install -r requirements.txt`
     successfully (see Validation results below for the real numbers).
   - User could not find the new local folder inside GitHub Desktop — expected,
     since GitHub Desktop only tracks folders it already knows about (either
     cloned by it, or explicitly added).
   - First attempted fix: **File → Add local repository** on the existing
     folder. This worked to make GitHub Desktop recognize the folder and
     create a local commit, but it initialized a **new, disconnected** local
     Git repository — it had no link to the `Market_Betting` repo already
     created on GitHub.com in step 2.
   - This surfaced when the user clicked **Publish repository**: GitHub
     Desktop tried to *create a new repository* on GitHub.com named
     `Market_Betting` and failed with `Repository creation failed. (name
     already exists on this account)` — because that repo already existed
     from step 2.
   - First correction attempt: pointed the user to **Repository → Repository
     settings → Remote** to manually set the origin URL to the existing
     GitHub.com repo. This menu path did not have the expected "Primary
     remote repository (origin)" field in the user's version of GitHub
     Desktop — noted as a version/UI difference rather than pursued further.
   - **Actual fix used:** abandoned trying to attach a remote to the
     already-initialized local repo. Instead: removed the repo from GitHub
     Desktop (Repository → Remove..., local files kept), renamed the local
     folder aside, used **File → Clone repository** to clone the real, empty
     `drgregmscott-tech/Market_Betting` from GitHub.com fresh (this correctly
     links local-to-remote automatically, which manually adding a folder does
     not), copied the project files into the freshly cloned folder, then
     committed and pushed normally. This resolved cleanly — push succeeded on
     the first attempt with no further errors.
7. Verified the final result directly on GitHub.com via Claude in Chrome:
   confirmed every expected file and folder is present at the correct path,
   one commit ("Repo Setup") on `main`, correct owner, private visibility
   intact.

**Files created/modified:**
- `/README.md`
- `/requirements.txt`
- `/.gitignore`
- `/config/api_keys.env.example`
- `/config/.gitkeep`, `/data/.gitkeep`, `/output/.gitkeep`, `/logs/.gitkeep`,
  `/scripts/.gitkeep`
- `/docs/research/Building_a_+EV_Prediction-Market_System_Edge-Detection_Across_Sports_Weather_and_Down-Ballot_Politics.md`
- `ROADMAP.md`, `SESSION_LOG.md` (moved from provisional/chat-only status into
  the actual repo as part of this session's push, alongside the rest — the
  versions the user pushed were the pre-Session-1.1-closure drafts; this
  session's closing update is what brings them current)

**Validation results:**
- PASS — Fresh clone + `pip install -r requirements.txt` runs without error.
  Confirmed on the user's actual machine (Windows, Python 3.14, via
  `pythoncore-3.14-64`): `pandas`, `numpy`, `requests` were already present
  and satisfied; `python-dotenv` installed cleanly (`python_dotenv-1.2.3`,
  22 KB wheel). One benign pip warning (`dotenv.exe` script installed outside
  PATH) — informational only, does not affect the install passing.
- PASS — Python version confirmed and logged: **Python 3.14**
  (`C:\Users\gmsco\AppData\Local\Python\pythoncore-3.14-64`).
- PASS — Research artifact from Session 0.1 is present in the repo, not
  orphaned in chat history. Confirmed live via direct browse of
  `github.com/drgregmscott-tech/Market_Betting/tree/main/docs/research` —
  file present at the correct path.
- Additional spot-check beyond the roadmap's original checklist (performed
  because the GitHub Desktop publish issue raised real doubt about what
  actually landed): every other folder (`/config`, `/data`, `/output`,
  `/logs`, `/scripts`) and file (`README.md`, `requirements.txt`,
  `.gitignore`) was individually confirmed present at its correct path via
  direct GitHub.com browsing, not assumed from the local push succeeding.

**Decisions made:**
1. Repo created directly on GitHub.com first (by Claude, with explicit user
   confirmation beforehand, since creating a repository is an account-level
   change), rather than letting GitHub Desktop create it via "Publish" — this
   was not the original plan, but became the deciding factor in resolving the
   GitHub Desktop issue (see Corrections below). Established as the preferred
   pattern for any future sibling repo: create on GitHub.com, then **Clone**
   in GitHub Desktop, never **Add local repository** for a brand-new project.
2. No README/gitignore/license auto-generated by GitHub at repo-creation time
   — all supplied as hand-authored files matching the DFS sibling repos'
   actual conventions, so the repo's baseline content is intentional rather
   than generic scaffolding.
3. `config/api_keys.env.example` added as a documented template even though
   no real credentials exist yet (Open Decision #3 still unresolved) — gives
   the next session a concrete shape to fill in rather than starting from
   nothing.
4. `.gitkeep` placeholder files used in every otherwise-empty folder — Git
   does not track empty directories, and the repo structure itself
   (data/scripts/output/logs/docs/config) is part of what Session 1.1 is
   meant to establish, so the folders needed to survive the first push.

**Corrections/reversals during the session:**
1. **GitHub Desktop "Add local repository" → "Clone repository."** Original
   guidance (based on the user already having files sitting in a local
   folder) was to use **Add local repository** to bring that existing folder
   under GitHub Desktop's tracking, then attach it to the GitHub.com remote
   manually via Repository Settings. This produced a disconnected local repo
   and a failed "Publish repository" attempt (duplicate name on GitHub.com).
   The Repository Settings → Remote menu path also did not match what the
   user's GitHub Desktop version actually showed. Corrected to the more
   reliable pattern: remove the disconnected local repo from GitHub Desktop,
   clone the real GitHub.com repo fresh, then copy files into the cloned
   folder before the first commit. This is now documented in ROADMAP.md's
   Workflow Preference section so future sibling-repo sessions don't repeat
   the same detour.

**Open items / deferred validations:**
- None for this session — all three roadmap validation checkboxes passed,
  plus the additional full file/folder spot-check.
- Carried forward, unchanged, from Session 0.1 (still open, tied to Sessions
  1.2+): Open Decisions #3 (data source access per track, especially
  PrizePicks/Underdog), #4 (account-limiting policy verification per pick'em
  platform), and #5 (concrete first estimation model spec).

**Status at close of session:** Fully closed out. Repo `Market_Betting` is
live on GitHub.com, private, correctly structured, with the Session 0.1
research artifact archived inside it and a clean local-development
environment confirmed on the user's actual machine. Next session should pick
up at Sessions 1.2+ in ROADMAP.md — real investigation of Open Decisions #3–#5
for the Fixed-Line Pick'em Platforms v1 track.

---

## Session 1.1 (continuation) — Open Decisions #3/#4 Research

**Date completed:** 2026-08-28
**Status:** ✅ Complete — logged here as a continuation of Session 1.1, not a
separately numbered session, per user direction (this was investigation
resolving Session 1.1's own still-open items, not new build work).

**What was actually done:**
1. General web research on PrizePicks/Underdog/DK Pick6 data access confirmed
   all three platforms lack an official developer API but each run
   undocumented public endpoints reachable without login or an API key (e.g.
   `partner-api.prizepicks.com/projections`).
2. General web research surfaced a widely-repeated but single-sourced claim
   that PrizePicks demotes winning accounts to Flex-only entries and cuts max
   entry size once win rate crosses ~55% over 200+ entries.
3. A full Advanced Research task (task_id `wf-2c042688-db7f-568c-b6a4-77a745d46367`)
   was run to verify account-limiting policy against primary sources (ToS
   language) and credible first-hand reports, rather than relying on the
   general search results. Report archived at
   `/docs/research/Pickem_Platform_Account_Limiting_Policy_Research.md`.

**Files created:**
- `/docs/research/Pickem_Platform_Account_Limiting_Policy_Research.md`

**Validation results:**
- PASS — All three platforms' Terms of Service quoted/paraphrased directly
  from primary sources, confirming broad sole-discretion authority to limit or
  close accounts.
- PASS — The ~55%/200-entry PrizePicks claim was checked against Reddit,
  forums, X, and journalism; found **no independent corroboration** beyond the
  single originating affiliate site. Explicitly flagged as unverified in the
  research artifact rather than treated as fact.
- PASS — First-hand evidence located (BBB, Trustpilot) showing a real pattern
  of PrizePicks account closures and withheld withdrawals perceived by users
  as win-triggered, distinct from (and better-documented than) the specific
  unverified threshold claim.
- PASS — State-by-state legal status of the "vs.-the-house" pick'em model
  documented, including confirmed peer-to-peer alternatives (PrizePicks
  "Arena," Underdog "Pick 'Em Champions," DK Pick6's native peer-to-peer
  design).

**Decisions made:**
1. The 55%/200-entry threshold will not be built into any sizing or risk logic
   as a hard number — treated as unconfirmed throughout the roadmap.
2. PrizePicks treated as higher account-closure risk (withdraw frequently);
   Underdog and DK Pick6 treated as more scalable — reflected in Session 2.6's
   sizing design once that session is built.
3. State-level legal footprint is now planned as an explicit check in every
   track's ingestion session (see Session 1.2 below), not just for pick'em.

**Open items / deferred validations:**
- None — Open Decisions #3 and #4 are resolved. Remaining research (Kalshi/
  Polymarket API access, sportsbook odds feeds) is deferred to Sessions 3.1
  and 6.1 respectively, where it's actually needed — not treated as a Phase 1
  blocker.

---

## Session 1.2 — Full Roadmap & Session Structure Definition

**Date completed:** 2026-08-28
**Status:** ✅ Complete

**What was actually done:**
1. User identified that Session 0.1 had defined project *scope* (six ranked
   tracks) but never broken it into the session-by-session build map used by
   the DFS sibling repos — the "Sessions 1.2+" card in ROADMAP.md was still a
   stub. This session closes that gap.
2. Built a complete phase/session map covering all six tracks (not just the
   v1 pick'em track), at the user's explicit direction, in the same card
   format as the DFS repos: prerequisites, what gets built, files touched,
   validation checklist, per session.
3. Structured the map as: Phase 2 (pick'em, v1) as a full original build of
   every stack layer; Phases 3–6 (arbitrage, weather, politics, sportsbook
   props) as scaffold-reuse builds, each swapping in only the track-specific
   estimation model and data source; Phase 7 (flagship/main lines) gated
   behind an explicit go/no-go checkpoint rather than an assumed build; Phase 8
   as cross-track portfolio management once 2+ tracks are live.
4. First review pass: user confirmed the structure was directionally right,
   then asked Claude to independently assess whether the roadmap, if fully
   executed, would actually produce a system capable of consistently
   identifying +EV bets daily across all in-scope tracks — not just whether it
   was well-organized. This assessment surfaced four real gaps: no defined
   sample-size threshold for go/no-go checkpoints, no recurring endpoint-health
   monitoring despite every non-exchange data source being an undocumented
   endpoint, no realized-outcome/P&L tracking distinct from the CLV proxy, and
   no explicit statement that the system flags/sizes but does not place bets.
   User approved all four; Claude added: Session 2.5 (sample-size thresholds +
   realized-outcome tracking), Session 8.4 (ingestion health monitoring), and
   an explicit "flags and sizes, does not place" statement in Background &
   Approach.
5. User raised a specific concern from Session 0.1 directly: had the roadmap
   actually captured the track-specific, evidence-based reasoning for why each
   edge is believed real (not just general validation discipline)? Claude
   audited the draft against Session 0.1's own five per-venue evaluation
   criteria (repricing mechanism, fee/vig cost, account-limiting risk,
   liquidity, legal footprint) by name, across all six tracks. Found liquidity
   and legal-footprint checks were narrative-only (not explicit session
   checklist items) for arbitrage, weather, politics, and sportsbook props —
   only the pick'em track (via the Session 1.1 continuation research) had them
   as concrete checks. Also found Phase 7's go/no-go was framed as a single
   up-or-down call on "flagship markets," missing the original research
   finding that market structure — not sport — determines efficiency at the
   sub-market level (e.g. Asian handicap soccer vs. that same game's 1X2
   market).
6. Fixed both gaps directly: added explicit liquidity and/or legal-footprint
   validation checkboxes to Sessions 3.2, 4.1, 5.1, and 6.1; rewrote Session
   7.0 to evaluate market structure at the sub-market-type level rather than
   as a blanket flagship judgment.
7. User raised a standing concern, also traceable to Session 0.1: that the
   project not be re-litigated, session after session, on the basic point that
   it is not designed to win every bet — it is designed to produce a real edge
   over the general betting market across a large sample, with real losing
   stretches expected along the way (the S&P 500 analogy, already established
   in Session 0.1). User asked this be captured once, permanently, rather than
   needing to be re-raised. Added directly to ROADMAP.md's Background &
   Approach section as a one-time, settled statement.
8. Merged the fully-reviewed roadmap into the real ROADMAP.md, replacing the
   "Sessions 1.2+" stub with 45 real, buildable session cards across Phases
   2–8. Updated the Open Decisions section: #3 and #4 marked resolved (with
   reference to the Session 1.1 continuation research above); #5 marked as
   deliberately deferred to Session 2.3, not abstract; two new items (#6, #7)
   added and marked resolved, documenting the liquidity/legal-footprint and
   Phase 7 sub-market gaps found and fixed during this session's own review.

**Files created/modified:**
- `ROADMAP.md` — full rewrite of the "Sessions 1.2+" stub into Phases 2–8 (45
  session cards), plus updates to Background & Approach and Open Decisions.
- `SESSION_LOG.md` — this entry, plus the Session 1.1 continuation entry above
  it.

**Validation results:**
- PASS — All six tracks have complete session breakdowns, not just the v1
  track (45 total session cards across Phases 2–8).
- PASS — Every session card includes a stated goal, prerequisites, files
  touched, and a validation checklist.
- PASS — User reviewed and approved the roadmap through two substantive
  revision passes, both of which surfaced and led to fixing real gaps rather
  than rubber-stamping the first draft.
- PASS — Sequencing logic (why this phase order) is stated explicitly in its
  own section, not just asserted.
- PASS — Cross-checked against Session 0.1's five per-venue evaluation
  criteria by name, across all six tracks — confirmed present as explicit
  checks after this session's fixes, not narrative-only.

**Decisions made:**
1. All six tracks planned in full session-level detail now, rather than
   scoping one phase at a time — user's explicit direction, departing from the
   DFS repos' incremental-scoping pattern. Reasoning: this project's edge
   sources are more heterogeneous across tracks than sport-to-sport variation
   in the DFS repos, so planning all six up front surfaced real cross-track
   gaps that phase-by-phase scoping likely would have missed until much later.
2. Confirmed scope is 6 build tracks — a user restatement as "3 or 4 areas"
   during this session was an imprecise recollection, not a scope change;
   re-verified against Session 0.1's own Track Reference table and recorded
   permanently in ROADMAP.md's Background & Approach.
3. Research resolving Open Decisions #3/#4 does not get its own session
   number — logged as a continuation of Session 1.1 (see entry above), since
   it was investigation closing out Session 1.1's own open items.
4. Sample-size thresholds and realized-outcome tracking (new Session 2.5) are
   treated as prerequisites for every later "go/no-go" checkpoint, not
   optional — every Live Validation Window session (2.9, 3.6, 4.7, 5.7, 6.7)
   and Phase 7.0 explicitly depend on Session 2.5's output.
5. Endpoint-health monitoring (new Session 8.4) is deliberately placed in
   Phase 8, not earlier, since a meaningful cross-track staleness/schema check
   needs at least 2 live tracks' real ingestion history to design against —
   each track's own automation session still carries its own basic retry/error
   handling in the meantime, so this isn't a coverage gap before Phase 8.
6. "This system flags and sizes, it does not place bets" is now a permanent,
   explicit statement in Background & Approach, tied directly to this
   environment's restriction against Claude executing financial trades on the
   user's behalf.

**Corrections/reversals during the session:**
1. **Initial draft treated Session 0.1's per-venue evaluation criteria as
   satisfied by narrative description → corrected to require explicit,
   checkable session-level validation items.** The first full draft mentioned
   liquidity, legal footprint, fee/vig cost, repricing mechanism, and
   account-limiting risk in prose within relevant sessions, but only pick'em
   (which had real research behind it) had them as concrete checklist items.
   User's direct question — "are we capturing what we said we'd capture in
   0.1?" — led to a full audit that found and fixed this for arbitrage,
   weather, politics, and sportsbook props.
2. **Phase 7's go/no-go was initially a single track-level judgment →
   corrected to evaluate market structure at the sub-market-type level.** The
   original research specifically found market *structure*, not sport,
   determines efficiency (e.g. Asian handicap soccer is efficient while that
   same game's 1X2 market is not) — a blanket "is flagship worth building"
   call would have missed exactly the kind of narrow, real edge this
   project's other tracks are built to find.

**Open items / deferred validations:**
- None blocking Phase 2 from starting. Kalshi/Polymarket API access and
  sportsbook odds feed research remain genuinely open but are deliberately
  deferred to Sessions 3.1 and 6.1, where they're actually needed — not
  treated as blockers to the pick'em v1 track.

**Status at close of session:** Fully closed out. ROADMAP.md now contains a
complete, reviewed, twice-audited session map for all six tracks (45 sessions,
Phases 2–8). All five of Phase 1's original Open Decisions are resolved or
deliberately deferred to their actual point of need. Next session is Session
2.1 — Data Ingestion Prototype, the first real build session of the project.

---

## Session 2.1 — Data Ingestion Prototype

**Date completed:** 2026-08-29
**Status:** ✅ Complete

**What was actually done:**
1. Built three throwaway proof-of-reach scripts, one per originally-planned
   platform: `prototype_underdog.py`, `prototype_prizepicks.py`, and
   `prototype_dkpick6.py`. Each script's only job was to confirm an endpoint
   is reachable with no login/API key and to print the real field names
   returned, per the roadmap's stated goal for this session (proof-of-reach
   and schema discovery, not a production pipeline).
2. Live-tested reachability directly (via Claude's own browser tool) before
   handing scripts to the user. Found Claude's browser tool is blocked by its
   own safety category filter from visiting prizepicks.com and
   pick6.draftkings.com at all, but not underdogfantasy.com — so Underdog's
   endpoint (`api.underdogfantasy.com/beta/v3/over_under_lines`) was
   confirmed live by Claude directly, with real schema captured from that
   response, before the user ran anything. PrizePicks and DK Pick6 could not
   be tested this way; the scripts for those two were built from outside
   documentation (PrizePicks) or best-guess analogy (DK Pick6) instead, with
   this limitation stated plainly to the user rather than presented as
   confirmed.
3. User ran all three scripts locally:
   - `prototype_underdog.py` succeeded — 268 lines, real field names matched
     what Claude had already captured directly.
   - `prototype_prizepicks.py` succeeded — 21,203 projections, confirming the
     endpoint documented by outside developers was in fact real and working.
     Real field names captured, including one naming quirk worth remembering
     for Session 2.3: the player record inside PrizePicks' `included` list is
     typed `new_player`, not `player`.
   - `prototype_dkpick6.py` failed — `404 Client Error: Not Found` on the
     guessed endpoint `https://api.draftkings.com/pick6/v1/leagues`, as
     anticipated (this URL was always labeled a guess, not a confirmed one).
4. User indicated openness to dropping DK Pick6 from scope rather than
   pursuing the manual browser-Developer-Tools reverse-engineering fallback
   documented in that script's own docstring.
5. Roadmap's third validation item (a full day's snapshot, to prove data is
   genuinely live and to observe stability) needed real elapsed time, not
   just repeat manual runs close together — this was explained to the user,
   along with the honest limit that wall-clock time can't be shortened, only
   the user's manual effort within that time can be. Built
   `monitor_pickem_endpoints.py`, a new unattended script (not in the
   original roadmap card) that checks both remaining platforms on a timer in
   the background, logging a compact summary per check, so the user did not
   need to manually re-trigger checks throughout the day. Default was set to
   every 30 minutes for 12 hours; user asked whether a shorter window would
   suffice, and 6 hours was agreed as sufficient before running.
6. User ran the monitor script for approximately 10 hours (05:06–15:13,
   beyond the agreed 6-hour minimum), producing 21 checks. All 21 succeeded
   for both platforms, with zero failures. Record counts for both platforms
   moved meaningfully across the window (PrizePicks: ~31,400 → ~22,200;
   Underdog: 261 → 212 lines), which was read as real evidence of genuinely
   live, non-cached data rather than treated as an unexplained anomaly.
7. Folded all of the above into `/docs/research/endpoint_schemas.md`,
   including the full monitoring results table, before presenting it as
   ready to close.
8. User confirmed Session 2.1 as fully closed and DK Pick6 as formally
   dropped from Track 1's scope.

**Files created/modified:**
- `/scripts/ingestion/prototype_underdog.py`
- `/scripts/ingestion/prototype_prizepicks.py`
- `/scripts/ingestion/prototype_dkpick6.py` (built and run; endpoint not
  found — kept in the repo per its own docstring's fallback instructions in
  case DK Pick6 is reconsidered in the future)
- `/scripts/ingestion/monitor_pickem_endpoints.py` (new — not in the original
  Session 2.1 roadmap card; built mid-session to solve the "full day's
  snapshot without requiring manual re-runs" problem)
- `/docs/research/endpoint_schemas.md`
- `ROADMAP.md` (Session 2.1 marked complete; DK Pick6 removed from Phase 2's
  description, the Track Reference table, and Sessions 2.2/2.4/2.6's active
  validation items; new Open Decision #8 added recording the drop)

**Validation results:**
- PASS — PrizePicks and Underdog (the two platforms remaining in scope) both
  return live data successfully with no login/API key. Confirmed via
  individual test runs and again across 21 unattended checks over ~10 hours
  with zero failures for either platform. DK Pick6 does not have a working
  endpoint and is out of scope as of this session — see Decisions below.
- PASS — Schema documented per platform, from real captured responses (not
  assumed field names) for both PrizePicks and Underdog. Full field lists
  recorded in `endpoint_schemas.md`.
- PASS (by agreement, not literal 24 hours) — Snapshot/stability window of
  ~10 hours, 21 checks at ~30-minute intervals, run unattended. User and
  Claude explicitly agreed in advance that this shorter, automated window
  satisfies the roadmap's intent (proving live data + surfacing failure
  modes) without requiring a literal calendar day.
- PASS — Explicit note on what breaks the pull is recorded: nothing did, in
  this window, for either platform. Documented as a genuine finding rather
  than an unaddressed checkbox, with the explicit caveat that Session 2.2's
  production pipeline still needs real retry/error handling regardless,
  since both remain undocumented endpoints that can change without notice at
  any time.

**Decisions made:**
1. **DK Pick6 dropped from Track 1's scope.** No credible public
   documentation of a Pick6-specific endpoint exists; a best-guess URL
   (built by analogy to DraftKings' other documented APIs) returned a 404.
   User chose to drop it rather than pursue manual reverse-engineering via
   browser Developer Tools, given no guarantee of success and the risk that
   any real endpoint found that way could require a logged-in session —
   which would break this project's "no login required" design principle for
   pick'em ingestion (see Session 0.1 Decision #4 and the account-limiting
   research). Track 1 proceeds as a two-platform track: PrizePicks and
   Underdog.
2. **An automated, unattended monitoring script was built in place of manual
   repeat runs**, once it became clear the roadmap's "full day's snapshot"
   validation item needed real elapsed time (to observe genuine data change
   and any failure mode) rather than effort that could be compressed. This
   removed the user's need to personally re-trigger checks throughout the
   day, without shortening the actual observation window.
3. **A ~10-hour unattended window was accepted as satisfying "a full day's
   snapshot,"** rather than a literal 24 hours — agreed with the user in
   advance, based on the validation item's real purpose (proving live data,
   catching failure modes) rather than the literal word "day." Recorded here
   explicitly as an agreed scope decision, not a silently lowered bar.

**Corrections/reversals during the session:**
1. **Original roadmap card assumed all three platforms would be tested with
   equal confidence → corrected to reflect that Claude's own tools could only
   confirm one of three live, in real time, before handoff.** Claude's
   browser tool is blocked by its own safety category filter from visiting
   prizepicks.com- and pick6.draftkings.com-family domains at all, but not
   underdogfantasy.com. This was stated to the user plainly before any script
   was handed over, rather than presenting untested endpoints as confirmed.
2. **DK Pick6 in scope → DK Pick6 dropped.** See Decision #1. This reverses
   the original three-platform framing carried in ROADMAP.md's Phase 2
   description and Track Reference table since Session 0.1/1.2; both were
   updated as part of closing this session, per the project's standing
   convention that corrections are logged explicitly, not silently
   incorporated.

**Open items / deferred validations:**
- None blocking Session 2.2 from starting. Track 1 proceeds with two
  platforms (PrizePicks, Underdog) instead of three.
- If DK Pick6 is ever reconsidered, `prototype_dkpick6.py`'s docstring
  contains the manual browser-Developer-Tools procedure for finding its real
  endpoint — this was deliberately left in place rather than deleted.

**Status at close of session:** Fully closed out, by explicit agreement with
the user. Two of the three originally-planned pick'em platforms are
confirmed live with documented real schemas; the third (DK Pick6) is
formally dropped from Track 1's scope, with the reasoning and the option to
revisit it later both recorded rather than silently dropped. Next session is
Session 2.2 — Production Data Ingestion Pipeline, now scoped for two
platforms.

---

## Session 2.2 — Production Data Ingestion Pipeline

**Date completed:** 2026-08-31
**Status:** ✅ Complete

**What was actually done:**
1. Built the production ingestion pipeline, replacing Session 2.1's two
   throwaway prototype scripts: `schema.py` (shared normalized row format
   both platforms convert into, with field-by-field notes tracing each
   column back to Session 2.1's real captured field names — including the
   `new_player` vs. `player` PrizePicks quirk and Underdog's `stat_value`
   being returned as a string, not a number) and `ingest_pickem.py` (fetches
   both platforms with retry logic, saves raw snapshots, normalizes into the
   shared schema, writes both a uniquely-timestamped snapshot and an
   always-overwritten `latest.csv`, and logs every run to
   `/logs/ingestion.log`).
2. Built `test_ingest_pickem.py`, a validation harness using synthetic
   fixtures shaped like Session 2.1's real captured schemas — not requested
   explicitly by the roadmap card, but built because this sandbox's network
   access does not reach prizepicks.com or underdogfantasy.com, so the
   pipeline's error-handling and idempotency logic needed to be provable
   without live network access before handoff. Five scenarios tested: normal
   case, empty response, simulated schema change, simulated total network
   failure, and idempotency (two runs in a row). All five passed.
3. User ran the pipeline live on their own machine for the first time:
   19,891 combined normalized rows (19,667 PrizePicks + 224 Underdog).
   Manually spot-checked sample rows together — confirmed real player names,
   teams, sports, stat types, and lines across a real mix of categories
   (NFL passing yards, tennis, esports), not placeholder or malformed data.
4. Set up a Windows Task Scheduler task to run the pipeline hourly, to
   satisfy the roadmap's "3 consecutive days of real automated pulls"
   validation item. Before committing to a literal multi-day window, the
   user directly challenged whether that literal duration was actually
   necessary or just an inherited default. On review, agreed: this
   session's validation question is pipeline reliability, not statistical
   sample size (that question is Session 2.5's, to be answered later with
   real math against real flag-frequency data) — so a literal calendar
   duration wasn't the right unit of measure. Replaced with an explicit,
   evidence-based stopping condition instead: 15+ clean automated pulls with
   zero failures, at least one observed material swing in record counts
   (proof of live, non-cached data), and at least one pull captured near a
   real game-lock event. This mirrors the same pattern Session 2.1 already
   established (replacing a literal 24-hour window with ~10 hours of real
   evidence).
5. First scheduled-task attempt, using the bare `python` command with
   `/ru "%USERNAME%"`, failed immediately at creation
   (`ERROR: No mapping between account names and security IDs was done`) —
   `%USERNAME%` does not expand inside `schtasks`. Corrected by dropping
   `/ru` entirely.
6. Task was then created successfully and left running overnight
   (5:00 PM–5:00 AM local). In the morning, the log showed only the
   original manual run from the day before — the overnight task had not
   produced any new entries. `schtasks /query ... /v /fo list` showed
   `Last Result: -2147024894` ("the system cannot find the file
   specified") — the task had fired on schedule but failed to launch
   Python. Diagnosed via `(Get-Command python).Source`, which revealed the
   user's interactive shell resolves `python` to
   `C:\Users\gmsco\AppData\Local\Microsoft\WindowsApps\python.exe` — a
   Microsoft Store redirect stub, not a real interpreter, known to behave
   unreliably outside an interactive session (which a scheduled task is).
7. Located the user's real Python 3.14 install
   (`C:\Users\gmsco\AppData\Local\Python\pythoncore-3.14-64\python.exe`,
   already on record from Session 1.1) via a direct filesystem search.
   Built `run_ingest.bat`, a small wrapper placed at the repo root that
   explicitly changes into the repo's root directory before invoking the
   real Python interpreter directly by full path — closing both the
   interpreter-resolution problem and a second latent risk (the pipeline's
   file paths are relative to the repo root, and `schtasks` has no
   dedicated working-directory flag, so a task launched from a different
   default directory could otherwise misplace its own output).
8. Deleted and recreated the scheduled task pointed at `run_ingest.bat`,
   then force-triggered it immediately (`schtasks /run`) rather than
   waiting an hour to find out if the fix worked. Confirmed via
   `Last Result: 0` and a real, correctly-joined new data pull (24,303
   total rows) that the fix worked.
9. Per the evidence-based stopping condition agreed in step 4, the overnight
   window that failed silently was explicitly NOT counted — the clock was
   restarted from the first successful fixed run (2026-08-30 10:09 UTC).
   User asked directly whether continuing to run this was actually necessary
   for the next sessions (2.3 onward) to proceed properly, given reasonable
   confidence the pipeline already worked. Clarified explicitly: this
   overnight/full-day run is a reliability check on the pipeline itself for
   this session's own validation, not a data-gathering step Session 2.3
   depends on — Session 2.3 can use whatever data exists by the time it
   starts, live-pulled or historical, and does not require this specific
   batch. The run continued anyway, specifically to prove the just-fixed
   pipeline (not just the underlying endpoints, already proven stable in
   Session 2.1) holds up under real repeated automated use, since a fix
   that "looks like it worked once" is exactly the kind of unproven claim
   this project's own validation discipline exists to catch.
10. Given the user's Central time zone, set a concrete target stop time
    (~9:00 PM Central) calculated to comfortably clear 15+ hourly pulls and
    to land inside typical NFL Sunday evening game-lock windows.
11. User let the task run through 26 consecutive hourly pulls
    (2026-08-30 10:09 UTC through 2026-08-31 11:00 UTC). Reviewed the full
    log and per-snapshot row counts together. All three evidence-based
    conditions were met, with a stronger result than anticipated: record
    counts swung from a peak of 26,538 down to a low of 17,067 (~36%
    movement — a larger, clearer swing than Session 2.1's own), and the
    steepest single stretch of that drop (26,495 → 17,468 between
    17:00–21:00 UTC on 8/30) lines up directly with NFL Sunday afternoon
    kickoff windows in the user's local time — direct evidence of the
    pipeline correctly capturing real props expiring off the board as games
    locked, not just a quiet-hours pass.
12. Task Scheduler task deleted (`schtasks /delete`) once validation was
    confirmed complete, since it was temporary scaffolding for this
    session's own validation step, not part of the project's real
    automation (that is Session 2.7's job, deliberately not built early so
    as not to blur the two sessions together).

**Files created/modified:**
- `/scripts/ingestion/schema.py`
- `/scripts/ingestion/ingest_pickem.py`
- `/scripts/ingestion/test_ingest_pickem.py` (new, not in original card)
- `/data/pickem/raw/` (new folder, `.gitkeep` placeholder)
- `/data/pickem/normalized/` (new folder, `.gitkeep` placeholder)
- `/logs/ingestion.log` (created automatically on first run)
- `run_ingest.bat` (new, repo root — local Windows Task Scheduler helper,
  not intended to be committed; recommended addition to `.gitignore` since
  it hardcodes the user's local Windows username in file paths)
- `ROADMAP.md` (Session 2.2 marked complete, validation results and
  decisions recorded)

**Validation results:**
- PASS — Pipeline runs end-to-end and produces a normalized dataset across
  both platforms. Confirmed on real live data (19,891 rows on first real
  run), with a manual spot-check confirming correct joins (real player
  names/teams/stat types/lines, not placeholder data).
- PASS — Handles a simulated failure (bad response, empty response, schema
  change) without crashing. Confirmed via `test_ingest_pickem.py` against
  synthetic fixtures — empty response, missing top-level keys (simulated
  schema change), and total simulated network failure all handled cleanly,
  each logged, none fatal to the run.
- PASS — Confirmed idempotent. Proven via `test_ingest_pickem.py`:
  `latest.csv` is overwritten (never appended to) each run; two consecutive
  runs produce two correctly distinct timestamped snapshots, never a
  duplicated or corrupted single file.
- PASS (via an explicitly agreed evidence-based standard, replacing the
  literal "3 consecutive days" language) — 26 consecutive successful hourly
  pulls with zero failures (well past the 15-pull bar); a genuine ~36%
  record-count swing (26,538 → 17,067); and direct evidence of a real
  game-lock event captured live (steep, clean count drop lining up with NFL
  Sunday afternoon kickoffs in the user's local time).

**Decisions made:**
1. The roadmap's literal "3 consecutive days" validation language was
   replaced with an explicit, evidence-based stopping condition (15+ clean
   pulls; a real observed count swing; at least one pull near a real
   game-lock event) — agreed directly with the user rather than followed by
   default. Reasoning: this session's validation question is pipeline
   *reliability*, not the *statistical sample size* question that belongs
   to Session 2.5 later, once real flag-frequency data exists to calculate
   a real threshold from. This is the same "elapsed-time default →
   evidence-based standard" correction pattern Session 2.1 already set;
   this decision restates it as a reusable principle rather than
   re-deriving it from scratch each time a "how long do we run this" moment
   comes up in the project.
2. `run_ingest.bat` was built as a working-directory-safe wrapper around the
   real Python interpreter, rather than pointing the scheduled task at
   `python` directly, after that direct approach failed silently overnight.
   This is now the established pattern for any future Windows-scheduled
   script in this project, and a concrete, real precedent for the kind of
   failure mode Session 8.4 (Ingestion Health Monitoring) is designed to
   catch more systematically later.
3. Data collected during the overnight window before the scheduled-task fix
   was explicitly discarded from this session's validation count (the "26
   pulls" total starts only from the first successful fixed run), rather
   than being quietly folded in — consistent with the project's standing
   convention that corrections are documented as corrections, not silently
   absorbed.
4. Confirmed and recorded explicitly, at the user's direct request: the
   data collected during this session's validation run is not itself an
   input Session 2.3 depends on. Session 2.3 can build and test against
   whatever ingested data exists by the time it starts. This session's
   validation run exists solely to prove the pipeline's own reliability
   under real repeated use — not to produce a specific dataset for later
   sessions to consume.

**Corrections/reversals during the session:**
1. **First scheduled-task attempt (`/ru "%USERNAME%"`) → dropped `/ru`
   entirely.** `%USERNAME%` does not expand inside `schtasks`; the task
   defaults correctly to the current user without it.
2. **Bare `python` command in the scheduled task → full-path wrapper
   (`run_ingest.bat`).** The task's non-interactive execution context could
   not resolve `python` the way the user's interactive shell does (which
   itself was resolving to an unreliable Microsoft Store stub, not a real
   interpreter). The overnight window lost to this failure was not counted
   toward this session's validation total — the clock restarted from the
   first successful fixed run.
3. **Literal "3 consecutive days" validation target → explicit
   evidence-based stopping condition**, agreed directly with the user after
   they questioned whether the literal duration was actually necessary.
   Recorded here as a real correction, not a silent scope reduction — the
   replacement standard is arguably stricter in what it actually proves
   (a real game-lock event, a specific count-swing magnitude) than a
   duration-only requirement would have been.

**Open items / deferred validations:**
- None blocking Session 2.3 from starting.
- `run_ingest.bat` should be added to `.gitignore` before or during the next
  commit, since it hardcodes the user's local Windows username — flagged
  here so it isn't missed, not treated as a blocker to closing this session.

**Status at close of session:** Fully closed out. The production ingestion
pipeline is built, tested against synthetic failure scenarios, and proven
reliable under 26 consecutive hours of real automated use — including one
real operational failure (a Windows scheduled-task path issue) found and
fixed along the way, which is now a documented precedent for Session 8.4.
Next session is Session 2.3 — Estimation Engine v1.

---

## Session 2.3 — Estimation Engine v1

**Date completed:** 2026-08-31
**Status:** ✅ Complete

**What was actually done:**
1. Read the current, real contents of `schema.py` and `ingest_pickem.py`
   (Session 2.2) directly from GitHub before building anything, per this
   project's standing convention. Also reviewed DFS_Optimizer's
   `projections_baseline.py` and `nflverse_fetch.py` directly, since Session
   2.3's estimation model reuses the DFS repo's proven pattern (season
   average + recency-weighted recent form) and its proven, no-API-key
   nflverse data-pull method, not its code.
2. Built `pickem_model.py` v1, scoped to NFL only: for every prop in
   Session 2.2's real ingested data (`data/pickem/normalized/latest.csv`),
   attempts to match the player to nflverse's public weekly stats, compute a
   season average and recency-weighted recent form for the relevant stat,
   blend them 50/50 into a model mean, estimate a sigma from the player's
   own game-to-game variance, and compute a probability the real outcome
   lands over the platform's line via a normal-distribution approximation.
   Every prop that can't be modeled (wrong sport, unmapped stat type, no
   player match, too little history) still gets a row in the output with an
   explicit `model_status` — nothing silently dropped.
3. **Before handing the first version to the user, tested it directly
   against live nflverse data** (this sandbox's network allowlist reaches
   `github.com`/`raw.githubusercontent.com`, which nflverse's public parquet
   releases are hosted on) and found a real bug: nflverse's weekly-stats
   release has two name columns, `player_name` (abbreviated, e.g.
   "P.Mahomes") and `player_display_name` (full form, e.g. "Patrick
   Mahomes"). The model was initially built against `player_name`, which
   would have silently produced a `no_player_match` result for nearly every
   real row — a pipeline that runs cleanly while modeling almost nothing.
   Caught and fixed before handoff, and documented as a real, named finding
   in the spec doc rather than a silently-corrected mistake.
4. User ran the model against real, live ingested data for the first time:
   20,861 real props, first run breakdown
   `{'unsupported_sport': 17740, 'unsupported_stat_type': 1650, 'estimated':
   1420, 'no_player_match': 50, 'no_line_value': 1}`. Real player-match rate
   on NFL props with a mapped stat type: 1420/(1420+50) = 96.6%.
5. Inspected the real `unsupported_stat_type` breakdown directly (15 real
   stat-type strings, with counts) rather than guessing what to add next.
   Checked each one against nflverse's real column list before any mapping
   decision:
   - 10 stat types mapped from existing simple/composite nflverse columns
     (`Recs`, `Player TDs`, `Pass+Rush Yds`, `Rush+Rec Yds`, `INT`,
     `Rec TDs`, `Sacks`, `Rec Targets`, `FG Made`, `Pass+Rush+Rec TDs` —
     1,096 rows total).
   - 3 stat types (`Longest Rec`, `Longest Completion`, `Longest Rush` —
     416 rows) confirmed to have NO matching nflverse column of any kind
     (nflverse only has `fg_long`/`pt_long`, for kicking/punting) — left
     deliberately unsupported.
   - 2 stat types (`Kicking Points`, `Fantasy Score` — 138 rows) initially
     left unsupported pending confirmation of PrizePicks' real scoring
     formula, since nflverse has the raw ingredients but guessing the exact
     formula would present an assumption as a real number.
6. User asked to resolve the Kicking Points/Fantasy Score gap in the same
   session rather than deferring it. Researched both directly via web
   search and a direct fetch of PrizePicks' own official scoring page
   (`prizepicks.com/playbook-article/how-to-play-prizepicks-nfl-fantasy-
   scoring-system`, published September 17, 2025), corroborated for Kicking
   Points by PrizePicks Support's own reply on X. Confirmed real formulas:
   Kicking Points is tiered by field-goal distance (0–39 yds = 3 pts,
   40–49 yds = 4 pts, 50+ yds = 5 pts; PAT made = 1 pt; missed FG/PAT = −1
   pt each) and is explicitly stated by PrizePicks to be a different stat
   from Fantasy Score; Fantasy Score is full-PPR-style scoring across the
   standard offensive stat categories.
7. Before coding either formula, checked that every nflverse column each
   one needs actually exists (confirmed: `fg_made_0_19` through
   `fg_made_60_`, `fg_missed`, `pat_made`, `pat_missed` for Kicking Points;
   the full offensive stat line plus per-category lost-fumble and
   2-point-conversion columns for Fantasy Score). While doing this, found
   that nflverse's closest-named column for return touchdowns
   (`pt_return_tds`) does not measure what its name suggests — checked
   directly against real 2025 data and found it fires on punters (Bryce
   Baringer, AJ Cole, Thomas Morstead — all with zero recorded returns),
   not the players who actually returned a kick. Rather than guess at an
   alternative, the two rare 6-point components that would have needed that
   column (Offensive Fumble Recovery TDs, Kick/Punt/FG Return TDs) were
   left out of the implemented Fantasy Score formula and documented as a
   real, named, small gap.
8. Implemented both formulas as real weighted-scoring functions (not
   column sums, since these are genuine multi-term formulas), extending
   the model's stat-resolution logic to support a "computed" stat kind
   alongside the existing simple-column and summed-column kinds.
9. **Verified both formulas independently before sending the update to the
   user**: recomputed Kicking Points and Fantasy Score by hand, directly
   from raw nflverse data, completely outside the model's own code, for two
   real players (Harrison Butker, Patrick Mahomes). The model's own output
   matched the hand calculation exactly — for Butker, the model's blended
   `model_mean` of 9.72 was confirmed to equal precisely the documented
   50/50 blend of his hand-computed season average (8.29) and hand-computed
   recency-weighted recent form (11.15), proving the formula is correctly
   wired into the rest of the pipeline, not just producing a
   plausible-looking number.
10. User re-ran the updated model against the same real 20,861 props:
    `{'unsupported_sport': 17740, 'estimated': 2525, 'unsupported_stat_type':
    416, 'no_player_match': 138, 'no_line_value': 41, 'insufficient_history':
    1}`. Confirmed by direct arithmetic that exactly 138 rows moved out of
    `unsupported_stat_type` (matching Kicking Points' 85 + Fantasy Score's
    53 real counts precisely), with 128 landing in `estimated` and the
    remaining 10 falling to `no_player_match`/other — expected variance,
    not an error.
11. User confirmed a 96%+ real player-match rate is sufficient for v1 and
    signed off on closing the session with the current NFL-only,
    stated-gap scope.

**Files created/modified:**
- `/scripts/estimation/pickem_model.py` (new)
- `/docs/research/pickem_estimation_model_spec.md` (new — documents every
  input, weight, formula, and stated gap, including exact source citations
  for both PrizePicks scoring formulas and the real verification record for
  stat-type coverage)
- `ROADMAP.md` (Session 2.3 marked complete; Open Decision #5 marked
  resolved; new Open Decision #9 added, recording the deferred 2025→2026
  data-transition decision)

**Validation results:**
- PASS (met with agreed v1 scope) — Model produces a probability estimate
  for every ingested prop it can, and an explicit status for every prop it
  can't, across all 20,861 real rows tested. Non-NFL sports (85% of real
  volume) and 3 stat types with no matching data source are the stated v1
  boundary, confirmed acceptable by the user.
- PASS — Model's estimates sanity-checked two ways: real QB passing-yards
  props showed the correct monotonic relationship between line and modeled
  probability; both computed-formula stat types were independently
  hand-verified against real players and matched exactly.
- PASS — Inputs and weighting logic documented at DFS-repo specificity in
  `pickem_estimation_model_spec.md`, including exact formula source
  citations.
- PASS — Explicit, itemized list of what's not yet included (sport
  coverage, stat-type coverage, opponent/injury/home-away/pace/weather
  inputs, the PrizePicks implied-probability assumption, and the one real
  Fantasy Score formula gap) is documented in the spec doc, each with the
  specific reason for exclusion.
- Real player-match rate on supported NFL props: **96.6%** (2,525 estimated
  / 2,663 attempted), confirmed against live data and judged sufficient for
  v1 by the user.

**Decisions made:**
1. v1 scoped to NFL only, using nflverse's public weekly player stats (no
   API key required) as the external performance source — see ROADMAP.md's
   Session 2.3 card, Decision #1, for full reasoning.
2. Two inputs only (season average, recency-weighted recent form, blended
   50/50), matching DFS_Optimizer's own first-pass projection pattern —
   re-weighting this blend against real graded results is explicitly
   deferred to Session 8.3, once Sessions 2.4/2.5 produce real data to tune
   against.
3. Player-name matching uses nflverse's `player_display_name` column, not
   `player_name` — a real bug (see "What was actually done," item 3) found
   and fixed before handoff, not discovered later.
4. Stat-type coverage (10 simple/composite mappings, 2 computed-formula
   mappings, 3 confirmed-unsupported types) was built entirely from real
   ingested `stat_type` strings and checked against nflverse's real column
   list before each mapping decision — none guessed in advance.
5. Kicking Points and Fantasy Score formulas were sourced directly from
   PrizePicks' own official scoring page and PrizePicks Support's own
   statement, not assumed or approximated — see ROADMAP.md's Session 2.3
   card, Decision #5, for the exact source URLs and formula values.
6. The implemented Fantasy Score formula deliberately omits Offensive
   Fumble Recovery TDs and Kick/Punt/FG Return TDs (6 points each per
   PrizePicks' official table) because nflverse's closest-named column for
   return TDs does not measure the same real-world event (verified
   directly against real data, not assumed) — a real, small, named
   limitation, not a silent one.
7. Run against `--season 2025` for now; switching to real 2026 data is
   explicitly deferred to a future session (new Open Decision #9 in
   ROADMAP.md), since nflverse's 2026 release does not exist yet and no
   evidence yet exists to decide between a clean switch-over vs. a blended
   2025/2026 transition period.

**Corrections/reversals during the session:**
1. **Player-name column (`player_name` → `player_display_name`).** See
   "What was actually done," item 3. Corrected before the first handoff to
   the user, based on a direct live-data check, not discovered as a bug
   after the fact.
2. **Kicking Points / Fantasy Score: initially left unsupported → mapped
   with real, sourced formulas.** The first version of the spec doc
   documented these as a deliberate, stated gap (formula unverified). The
   user asked to resolve this within the same session rather than defer
   it; both formulas were then researched and confirmed against PrizePicks'
   own official sources and implemented. Recorded as a real correction to
   the session's original scope, not a silent reversal — the original
   "left unsupported" reasoning is preserved in the spec doc's history
   alongside the resolution, so the reasoning trail is visible.

**Open items / deferred validations:**
- Switching the model from `--season 2025` to real 2026 data (cleanly, or
  blended during the early-2026 transition) is deliberately deferred — see
  new Open Decision #9 in ROADMAP.md. No action needed until real 2026
  games start being played (first games 2026-09-07).
- No further stat-type expansion planned before Session 2.4 — the 3
  remaining unsupported stat types (`Longest Rec`, `Longest Completion`,
  `Longest Rush`) have no matching nflverse data source at all, not an
  unresearched gap.
- Opponent/matchup, injury/role, home/away, and pace/usage inputs remain
  out of v1 by design — real, named candidates for a future model
  iteration once Session 2.4/2.5's CLV and outcome data shows where v1's
  blind spots actually cost accuracy (see `pickem_estimation_model_spec.md`,
  "What v1 does NOT do").

**Status at close of session:** Fully closed out. The estimation engine is
built, tested against live nflverse data, and validated with a 96.6% real
player-match rate on its supported scope — including two real formulas
(Kicking Points, Fantasy Score) sourced directly from PrizePicks' own
official documentation rather than approximated, and one real bug
(player-name column mismatch) and one real data-quality trap
(`pt_return_tds` not measuring what its name suggests) both caught via
direct verification against live data before being shipped, not discovered
later. Next session is Session 2.4 — CLV-Equivalent Calibration Logging.

---


## Session 2.4 — CLV-Equivalent Calibration Logging

**Date completed:** 2026-09-01
**Status:** ⚠️ Complete with caveats

**What was actually done:**
1. Read Session 2.3's real `pickem_model.py` and Session 2.2's `schema.py`
   directly from GitHub before building anything, per this project's
   standing convention.
2. Built `clv_logger.py` — the pre-outcome validation layer. For every prop
   Session 2.3's model marks `model_status="estimated"` where the model's
   probability clears a stated edge threshold (`FLAG_EDGE_THRESHOLD = 0.03`,
   an explicit placeholder, not derived from graded data — see Decisions
   below), the script logs the flag to `data/pickem/clv_log.csv` and tracks
   it against two benchmarks until the prop disappears from the feed
   (treated as game-lock): (a) a same-moment cross-platform consensus match
   against the other platform, when the same real prop is priced there too,
   and (b) the prop's own last-seen price before it drops out of a run,
   frozen as a "closing" value. Explicitly did NOT treat this as literal
   sportsbook CLV, since Session 0.1's own research established PrizePicks/
   Underdog run "static, non-repricing lines" — a platform's own price not
   moving is not itself evidence of anything, unlike a sportsbook's real
   closing line.
3. **Made one small, additive change to `pickem_model.py`** to support (a)
   above: added a new output column, `resolved_stat_key`, carrying the
   canonical stat the model resolved a prop's raw `stat_type` string down to
   (e.g. `"passing_yards"`, or `"rushing_yards+receiving_yards"` for a
   composite). Needed because PrizePicks and Underdog word the same real
   stat differently, and matching on raw text alone would be unreliable. No
   existing column, calculation, or behavior in the file changed.
4. Built `test_clv_logger.py`, a synthetic-fixture validation harness
   (same reasoning as Session 2.2's `test_ingest_pickem.py`: this sandbox's
   network doesn't reach the real endpoints, so matching/open/close/
   idempotency logic needed to be provable without live data before
   handoff). Six scenarios: new flag with a real consensus match, new flag
   with none available, a sub-threshold row correctly NOT flagged, an open
   flag correctly refreshed (not duplicated) across a second run including
   its own line moving, a flag correctly transitioning to `closed` with
   frozen values and a correct `clv_edge_at_close` calculation once its
   prop disappears, and running the identical file through the logger twice
   producing no duplication. All six passed, plus a full integration check
   (real file discovery, real CSV write, real snapshot write).
5. Wrote `docs/clv_methodology.md` documenting both benchmarks, the stated
   threshold, the log schema, and named gaps — matching the specificity
   level of Session 2.3's own model spec doc.
6. **Threshold decision, confirmed with user directly:** kept
   `FLAG_EDGE_THRESHOLD` at 0.03 for this session's real-data validation
   run rather than tuning it blind before any real flags existed.
7. **Validation-window duration, decided directly with user, before any
   live run:** the original roadmap card's implicit expectation of "one
   real week" of logged data was challenged by the user as an inherited
   default, not a derived number — same pattern as Session 2.1 and Session
   2.2's own corrections. Replaced with four explicit, evidence-based
   conditions (15+ new flags; 3+ closed; 1+ closed flag with a real
   consensus match; zero pipeline failures) and a target checkpoint of ~17
   hours, matching Session 2.2's own real validation window (~15–26 hours)
   rather than a full calendar week.
8. User set up the same kind of temporary scheduled-task validation
   scaffolding Session 2.2 used: a new local-only wrapper,
   `run_full_pipeline.bat` (repo root, not committed — same reasoning as
   `run_ingest.bat`), chaining `ingest_pickem.py` →
   `pickem_model.py --season 2025` → `clv_logger.py`, run hourly via
   Windows Task Scheduler.
9. **First log review surfaced an apparent gap** (ingestion fired hourly at
   13:00–16:00, then jumped to 17:39 with no 17:00 entry) that looked like
   a missed scheduled run. User clarified directly: the 13:00–16:00 entries
   predated the new scheduled task (leftover from earlier same-day manual
   testing) — 17:39 was the task's real first run. No actual failure;
   corrected the misread before it wasted investigation time on a
   non-issue.
10. **Second review (after ~17 hours, 3,205 total flags logged, 272
    closed) found a real anomaly:** every single closed flag showed
    `consensus_available = False` — not just mostly false, all 3,205 rows
    in the log, with zero Underdog rows present at all. Investigated
    directly against live data rather than guessing:
    - First hypothesis (platform-string casing mismatch in
      `pickem_model.py`'s `row.get("platform") == "underdog"` check) —
      checked directly against `normalized/latest.csv` and ruled out;
      `platform` values were correctly lowercase.
    - Real cause found: the `sport` column was blank for 234 of 244
      Underdog rows in the live data (10 showed `CFB`; zero showed `NFL`).
      Traced into `ingest_pickem.py`'s `normalize_underdog()`: `sport` is
      read from `game_attrs`, joined via
      `games_by_id.get(appearance["match_id"])`. Pulled a real raw
      Underdog snapshot (`underdog_20260901T093802Z.json`) directly and
      confirmed a real game's own `id` (182897) and a real appearance's
      `match_id` (438) do not correspond — the join was failing.
    - Checked the payload's real top-level keys directly
      (`appearances`, `games`, `over_under_lines`, `players`, `providers`,
      `solo_games`) — no separate `matches` collection exists that the
      code was missing.
    - Checked whether game `438` existed anywhere in `games` or
      `solo_games` by direct ID search — it did not, in either list.
    - Checked the REAL, decisive question directly: whether Underdog's
      live `games`/`solo_games` lists contain any `NFL` sport_id at all
      right now. They do not — only `CFB` and `TENNIS`. **Root cause
      confirmed: Underdog has not posted real NFL lines yet as of
      2026-09-01 (real NFL season starts 2026-09-07); this is a real,
      external, calendar-driven fact, not a pipeline defect.** Since
      `pickem_model.py` is NFL-only in v1 scope, zero Underdog rows could
      ever have reached `model_status="estimated"` this week regardless of
      any code correctness.
    - While investigating, found a real, separate, smaller issue: only 89
      of 217 real Underdog `appearances` (41%) successfully joined to a
      real `games`/`solo_games` record, even for the sports Underdog does
      carry live right now (CFB, tennis). Cause not yet determined
      (plausible explanation: appearances referencing games not yet
      published into the feed that far ahead; not confirmed). This was
      NOT fixed this session — see Open items below — because it does not
      change this session's core finding (Underdog genuinely has zero NFL
      data right now) and fixing it blind, without real NFL data to test
      the fix against, risks a false sense of confidence.
11. **User decided directly, given the finding:** close Session 2.4 now
    rather than wait several more days for Underdog to post real NFL
    lines. The cross-platform consensus-matching mechanism is confirmed
    correct on synthetic data (`test_clv_logger.py` scenario 1) but is
    explicitly NOT yet confirmed on live NFL data, since none exists yet
    to test against — recorded here as a stated, not silent, gap, tied to
    a specific future trigger (Underdog posting real NFL lines, expected
    on or shortly before 2026-09-07).

**Files created/modified:**
- `/scripts/calibration/clv_logger.py` (new)
- `/scripts/calibration/test_clv_logger.py` (new)
- `/docs/clv_methodology.md` (new)
- `/scripts/estimation/pickem_model.py` (modified — added
  `resolved_stat_key` output column only; no other logic changed)
- `run_full_pipeline.bat` (new, repo root — local-only Windows Task
  Scheduler wrapper, not committed, same convention as `run_ingest.bat`)
- `data/pickem/clv_log.csv`, `data/pickem/clv_snapshots/` (created
  automatically on first real run)

**Validation results:**
- PASS — All 6 synthetic test scenarios in `test_clv_logger.py` passed
  before live handoff, plus a full integration check (real file discovery,
  real CSV write, real snapshot write).
- PASS (via explicit, agreed evidence-based conditions, replacing the
  roadmap's original "one real week" framing — same correction pattern as
  Sessions 2.1/2.2) — real live validation run, ~17 hours
  (2026-08-31 17:39 UTC through 2026-09-01 09:42 UTC): 3,205 total flags
  logged (well past the 15-flag bar), 272 closed (well past the 3-flag
  bar), zero pipeline failures across every logged run.
- DEFERRED, not failed — "1+ closed flag with a real cross-platform
  consensus match" was not achievable this week. Root cause confirmed
  directly against live data: Underdog has zero real NFL lines posted as
  of 2026-09-01 (season starts 2026-09-07), and Track 1's model is
  NFL-only in v1 scope. This is an external, calendar-driven fact, not a
  code defect — the consensus-matching code itself is confirmed correct
  against synthetic data. Re-verification against live NFL data is
  explicitly deferred, not silently dropped — see Open items below.

**Decisions made:**
1. `FLAG_EDGE_THRESHOLD = 0.03` kept as-is for this session's real-data
   validation run, confirmed directly with the user rather than tuned
   blind before any real flags existed. Still an explicit placeholder, not
   a researched figure — revisiting it against real graded results
   remains Session 8.3's job.
2. The roadmap's original "one real week" validation expectation was
   replaced with four explicit, evidence-based conditions and a ~17-hour
   target checkpoint, matching Session 2.2's own real validation window —
   same "elapsed-time-as-default → evidence-based standard" correction
   this project has now applied a third time (Sessions 2.1, 2.2, 2.4).
3. Two independent, distinct benchmarks (cross-platform consensus;
   own-line movement to close) are logged side by side, unblended, rather
   than combined into one number — deliberately, so a future session can
   judge which one (if either) actually correlates with real graded
   outcomes once Session 2.5 exists to check that.
4. `resolved_stat_key` was added to `pickem_model.py`'s output rather than
   attempting fuzzy text matching on each platform's raw `stat_type`
   string in `clv_logger.py` — an exact-match-only approach, accepted to
   risk missing some real matches (if a stat resolves on only one platform)
   rather than risk a wrong match (comparing two different real stats
   as if they were the same one).
5. **Given the confirmed root cause (Underdog has no real NFL data yet,
   not a bug), the session was closed now rather than delayed several more
   days waiting for Underdog to post NFL lines.** Live confirmation of
   cross-platform consensus matching is explicitly deferred to a future
   check once Underdog posts real NFL lines — tracked as a new Open
   Decision (#10) below, not silently dropped.
6. The real, separate 41% Underdog appearances-to-games join gap found
   during this session's investigation was deliberately NOT fixed this
   session. Reasoning: fixing it blind, with no real NFL data to test the
   fix against, risks false confidence that the real problem (which
   affects `sport`, `game_start_time`, and therefore cross-platform
   matching) is solved when it may not be. Tracked as a new Open Decision
   (#11) below, tied to the same future trigger as Decision #5.

**Corrections/reversals during the session:**
1. **First hypothesis (platform-string casing bug in `pickem_model.py`) →
   ruled out by direct data check, replaced with the real cause (a broken
   `sport` field, traced to a `games`/`appearances` ID join that doesn't
   resolve — itself ultimately explained by Underdog having no real NFL
   games live yet, not a code defect at all).** Recorded as a real
   investigation trail, not silently corrected — each hypothesis was
   checked directly against live data before being accepted or discarded,
   per this project's standing convention.
2. **An apparent missed scheduled run (13:00–16:00 ingestion entries, then
   a gap to 17:39) was initially treated as a possible reliability
   failure.** User clarified directly: those entries predated the
   scheduled task's creation (same-day manual testing). No real failure
   occurred; corrected before further time was spent investigating a
   non-issue.

**Open items / deferred validations:**
- **New Open Decision #10 (opened this session):** Live confirmation that
  cross-platform consensus matching works correctly on real NFL data is
  deferred until Underdog posts real NFL lines — expected on or shortly
  before 2026-09-07 (real season start). Once that happens, re-run the
  same kind of short validation window used in this session and confirm
  at least one real closed flag shows `consensus_available = True` with a
  sane `consensus_edge` value.
- **New Open Decision #11 (opened this session):** The Underdog
  `appearances` → `games`/`solo_games` join in `ingest_pickem.py`'s
  `normalize_underdog()` only resolved for 41% of real appearances checked
  (89 of 217) in a live 2026-09-01 snapshot. Cause not yet confirmed —
  plausibly appearances referencing games not yet published that far
  ahead into the feed, but not verified. This directly affects whether
  `sport` and `game_start_time` populate correctly for Underdog rows once
  real NFL games do appear, and therefore whether Open Decision #10 above
  can actually be resolved when the time comes. Should be investigated
  before or alongside Decision #10's re-check, not assumed fine.
- PrizePicks' `NFL1H` (first-half props, 552 rows) and `NFLSZN`
  (season-long props, 1,324 rows) are excluded from v1 by the same exact
  `"nfl"` string match that correctly excludes non-NFL sports — noted
  during this session's investigation as a real, defensible scope boundary
  (arguably different market types from a full-game prop), but was not
  explicitly named as excluded before this session. Not fixed or resolved
  here; flagged for a future session to decide whether either should be
  brought into scope.

**Status at close of session:** Closed by explicit agreement with the
user, with two real, named, tied-to-a-specific-future-trigger deferrals
(Open Decisions #10 and #11) rather than unresolved loose ends. The CLV
logger itself is fully built, tested on synthetic data, and proven
reliable on ~17 hours of real live PrizePicks data with zero pipeline
failures — the piece not yet provable is cross-platform matching on real
NFL data, which cannot exist until Underdog itself posts real NFL lines.
Next session is Session 2.5 — Sample-Size Thresholds & Realized-Outcome
Tracking, though Open Decisions #10/#11 should be revisited once real NFL
data exists, independent of Session 2.5's own start.

---

## Session 2.5 — Sample-Size Thresholds & Realized-Outcome Tracking

**Date completed:** 2026-09-01
**Status:** ✅ Complete

**What was actually done:**
1. Calculated the real sample-size threshold for Track 1: derived PrizePicks'
   real per-leg breakeven win rate for a 2-pick Power Play (√(1/3) ≈ 57.7%,
   from PrizePicks' own published 3x payout — not assumed), then used a
   standard one-sample proportion power calculation (α=0.05, power=0.80,
   target true win rate 60%) to arrive at ≈3,725 graded legs needed for
   standard statistical confidence. Documented in full, including the
   reasoning behind each chosen parameter, in `sample_size_methodology.md`.
2. Built `outcome_tracker.py`, a second log (separate from Session 2.4's
   `clv_log.csv`) recording real, manually-reported bet outcomes, linked by
   `flag_id`. Tested against six synthetic scenarios (win with payout, loss,
   unknown flag_id handled without crashing, pending list, report, duplicate
   re-report treated as a correction not an overwrite) before being sent to
   the user — all six passed.
3. User pointed out ≈3,725 graded legs was a large number to treat as a
   single gate, and redirected the session's design: build to a reasonable
   working point now, then run an indefinite recurring review (weekly, by
   the user's explicit choice) that recalibrates over time as real data
   accumulates, rather than blocking on one large threshold. This was
   discussed as three named options (A: wait for the full threshold; B: a
   smaller interim checkpoint; C: auto-grade a broader pool of
   flagged-but-not-bet legs against public final stats) — user chose a
   fourth, better-fitting option not originally on the list: a genuinely
   recurring cadence, not a bigger or smaller one-time checkpoint.
4. Built `weekly_review.py` to implement this: a 30-leg interim floor below
   which no recalibration recommendation is given (mirroring Session 2.4's
   own "15+ flags" reporting minimum); above it, every run reports real
   numbers (this period and cumulative) next to the fixed 57.7%
   breakeven and 3,725-leg full threshold; every run also checks (a) a
   calibration gap (does the model's stated confidence match real win
   rate) and (b) whether higher-edge flags actually outperform lower-edge
   flags, producing a recommendation only — no automatic changes to
   `pickem_model.py` or `clv_logger.py`. Tested against a 50-leg synthetic
   dataset (below-floor case, full run, second same-day run, history) —
   all scenarios passed.
5. `sample_size_methodology.md`'s Section 6 was rewritten to record this as
   a real, explicit decision (recurring review, not a single gate), including
   the point that this pulls part of Session 8.3's job forward for this one
   track, ahead of the cross-track version Session 8.3 will eventually build.
6. Real-data test of both scripts, requested by the user: pulled the actual
   live `clv_log.csv` from GitHub via Claude in Chrome (3,207 real flag
   rows, 273 closed). Recorded two real flag_ids (`prizepicks|13961517`,
   `prizepicks|14252061`) through `outcome_tracker.py` — both correctly
   pulled real context by `flag_id` lookup; `--pending` correctly reported
   3,205 remaining. Ran `weekly_review.py --run` against this real (2-leg)
   outcome log — correctly identified the sample as below the 30-leg floor
   and withheld a recalibration recommendation, exactly as designed.
   **Both graded outcomes used were placeholders for pipeline-testing
   purposes only** — the underlying games have not been played yet
   (2026-09-09 kickoff) — and were recorded only in Claude's own sandbox
   copy of the repo, not pushed to the user's real `outcome_log.csv`
   (which does not yet exist in the real repo).
7. While reviewing the real `clv_log.csv` pulled in step 6, noticed every
   PrizePicks row uses a flat 50% implied probability, producing some very
   large edge values. User raised this, noting uncertainty about whether a
   different approach had been decided previously. Checked directly against
   the full real record (`pickem_model.py`'s own docstring, all of Session
   2.3's Decisions in ROADMAP.md and SESSION_LOG.md) — confirmed no
   different decision exists on record; the flat 50% has been a stated,
   unverified Session 2.3 assumption throughout.
8. Discussed with the user whether to change the 50% to the real 57.7%
   breakeven derived earlier this session. Recommended against a direct
   substitution: 50% and 57.7% answer different questions (50% is a
   flagging-sensitivity threshold used before any entry type is chosen;
   57.7% is one specific entry type's real breakeven, only meaningful once
   an entry type is actually being sized) — swapping one flat number for
   another flat number would still be wrong for every entry type other than
   a 2-pick Power Play. User agreed. Added a clarifying section to both
   `pickem_model.py`'s docstring and `clv_methodology.md`, stating the
   distinction explicitly. No code logic changed — confirmed the edited
   `pickem_model.py` still parses cleanly before handoff.

**Files created/modified:**
- `/docs/sample_size_methodology.md` (new)
- `/scripts/calibration/outcome_tracker.py` (new)
- `/scripts/calibration/weekly_review.py` (new — not in the original card)
- `/data/pickem/outcome_log.csv` (new — starts empty in the real repo)
- `/data/pickem/review_log.csv` (new — not in the original card, starts empty)
- `/scripts/estimation/pickem_model.py` (docstring-only correction)
- `/docs/clv_methodology.md` (new section added)

**Validation results:**
- PASS — Sample-size threshold calculated and documented with full reasoning
  shown (real breakeven, chosen power-analysis parameters each explained,
  not just asserted).
- PASS — Outcome tracker records real, manually-reported results and links
  them to the CLV log — confirmed on real live data (two real flag_ids from
  the actual `clv_log.csv`, both correctly pulled real context; `--pending`
  correctly reported 3,205 of 3,207 real flags remaining).
- PASS — The two logs can be joined/compared — confirmed on real data via
  `weekly_review.py --report`'s join logic.

**Decisions made:**
1. Sample size treated as a recurring weekly review, not a one-time gate —
   user's explicit direction, departing from the original card's framing.
   See ROADMAP.md's Session 2.5 card, Decision #1, for full reasoning.
2. This pulls part of Session 8.3's job (Ongoing Recalibration Cadence)
   forward to a single-track cadence starting now, rather than waiting for
   Phase 8's 2+-track cross-track version.
3. The flat 50% PrizePicks "implied probability" (Session 2.3) and the real
   57.7% entry-type-specific breakeven (derived this session) are
   deliberately kept as two separate, differently-scoped numbers, not
   merged — real breakeven economics are Session 2.6's job, not this
   session's or Session 2.3's. No code changed; both relevant files'
   documentation was corrected instead.
4. The two placeholder outcome records used for real-data pipeline testing
   are explicitly not real graded results and were not pushed to the real
   repo — noted here so no future session mistakes them for real data if
   they're ever encountered.

**Corrections/reversals during the session:**
1. **Original three-option framing (A: wait for full threshold, B: smaller
   interim checkpoint, C: auto-grade a broader pool) → user chose a fourth,
   better-fitting option (recurring weekly cadence) not on the original
   list.** Recorded as a real redirection, not a refinement of one of the
   three offered options.
2. **A flat 50%-to-57.7% substitution in `pickem_model.py` was proposed,
   then reconsidered and not made**, once it became clear 57.7% is only
   correct for one specific entry type. Corrected to a documentation-only
   fix instead of a code change, per Decision #3 above.

**Open items / deferred validations:**
- **New Open Decision #12 (opened this session):** No real bets have been
  placed or graded as of this session's close — `weekly_review.py`'s first
  real run has not happened. Not a blocker to closing this session (the
  weekly review is designed as an ongoing practice, not a one-time
  deliverable), but flagged so a future session knows `review_log.csv`
  genuinely starts empty. Action needed: once the user places and reports
  a first real bet, run `weekly_review.py --run` for real.
- Open Decisions #10 and #11 (from Session 2.4) remain open, tied to
  Underdog posting real NFL lines (expected on or shortly before
  2026-09-07) — untouched by this session, carried forward unchanged.

**Status at close of session:** Fully closed out. All three original
roadmap validation items are met, confirmed against real live data where
possible. The recurring-review redesign and the implied-probability
clarification are both real, user-directed changes from the original card,
recorded here rather than silently absorbed. Next session is Session 2.6 —
Bankroll & Sizing Logic, which is also where the real, entry-type-specific
breakeven math from this session first gets applied to an actual sizing
decision.

---

## Session 2.6 — Bankroll & Sizing Logic

**Date completed:** 2026-09-01
**Status:** ✅ Complete

**What was actually done:**
1. Before building anything, checked the real repo directly (via Claude in
   Chrome) and found Session 2.5's files (`outcome_tracker.py`,
   `weekly_review.py`, `sample_size_methodology.md`) were missing from
   GitHub, even though Session 2.5 had closed in chat — a real gap between
   "session closed in conversation" and "session actually pushed," not
   previously an issue in this project. User confirmed the push had
   simply been forgotten and completed it; re-checking GitHub directly
   confirmed all three files were then present, and the session proceeded
   from there.
2. Read the real, live contents of `pickem_model.py`, `clv_logger.py`,
   `outcome_tracker.py`, and `sample_size_methodology.md` directly from
   GitHub before designing anything, per this project's standing
   convention.
3. Made a real, stated scope decision before writing any code: pick'em
   entries require 2+ legs combined together, and only one entry type has
   a real, sourced payout multiplier anywhere in this project's research
   — PrizePicks' 2-pick Power Play (3x payout, sourced in Session 2.5).
   Rather than guess at a multiplier for any other entry size or for
   Underdog (no real Underdog payout table has been researched), v1 was
   scoped to size exactly that one entry type, rejecting every other
   combination with an explicit reason. This mirrors Session 2.3's own
   NFL-only scoping decision.
4. Built `sizing_engine.py`: reads two `flag_id`s from the real
   `clv_log.csv`, multiplies their model probabilities together for a
   combined entry probability, runs that through the Kelly criterion,
   applies quarter-Kelly (`KELLY_FRACTION = 0.25`) for estimation-
   uncertainty safety, applies a named PrizePicks account-risk dampener
   (`PLATFORM_RISK_MULTIPLIER["prizepicks"] = 0.70`, reflecting the
   Session 1.1 continuation research on account closures), and enforces a
   hard bankroll cap (`MAX_SINGLE_POSITION_PCT = 0.05`) after every other
   adjustment. Every constant is named and documented as either sourced
   (the 3x payout) or an explicit, stated judgment call (everything else)
   — no unnamed factors, matching this project's standing documentation
   standard.
5. Built `test_sizing_engine.py` (not in the original card — same
   reasoning as Session 2.2/2.4/2.5's own test harnesses: this sandbox
   cannot reach the real repo's live data). Six initial synthetic
   scenarios — bigger edge produces a bigger stake, a sub-breakeven
   combined probability produces `no_bet_negative_edge` and $0 (never
   negative), an extreme edge is correctly capped, a mixed/Underdog leg
   is rejected with a stated reason, wrong leg counts are rejected, and
   closed-status legs are filtered before reaching the sizing math — plus
   an independent hand-check of the Kelly formula itself. All passed, and
   were also run through a simulated copy of the real repo's folder
   structure with a fake `clv_log.csv`, to prove the file-lookup and CLI
   path worked end-to-end, not just the isolated math.
6. Wrote `sizing_methodology.md`, documenting the Kelly formula with a
   worked example, and explicitly separating which numbers are sourced
   (the 3x payout) from which are this project's own stated judgment
   calls (quarter-Kelly, the platform dampener, the bankroll cap).
7. User asked directly for an objective assessment of the two judgment-
   call constants (`KELLY_FRACTION`, `PLATFORM_RISK_MULTIPLIER`) before
   accepting them. Assessed each separately: quarter-Kelly recommended
   as-is, since it's standard practice specifically for the kind of
   estimation uncertainty this model has, and there was no real basis to
   recommend a different fraction. The 0.70 platform dampener was
   assessed more critically — flagged plainly that it collapses two
   different real risks (account-closure risk and general safety margin)
   into one unsourced number, but that no amount of additional reasoning
   turns it into a sourced figure without real data on actual account
   limiting outcomes, which doesn't exist yet. Recommended keeping both
   as explicitly-labeled placeholders for v1, consistent with this
   project's existing pattern (Session 2.4's edge threshold, Session
   2.5's target win rate). User accepted this recommendation as given.
8. User raised the same-game correlation gap directly and asked to
   discuss it further rather than deciding immediately. Talked through
   the real mechanism (two legs from the same game are not fully
   independent — a blowout, overtime, or injury can move several
   players' stats together), and the fact that the direction of the bias
   depends on whether legs are positively or negatively correlated, which
   isn't known without real data. User's stated instinct: the model
   should flag same-game pairs as potentially riskier rather than pretend
   to precisely model the correlation. This exactly matches the dampener
   approach already used elsewhere in the script.
9. Built `SAME_GAME_CAUTION_MULTIPLIER = 0.85`, applied whenever both
   requested legs share the same real `game_id`, and added two new output
   fields (`same_game_pair`, `same_game_caution_multiplier_applied`) so
   the flag is always visible when it fires, never a silent adjustment.
   Added a new synthetic test (`test_7`) proving a same-game pair gets a
   smaller stake than an otherwise-identical cross-game pair. Updated
   `sizing_methodology.md` with a new section (4.5) explaining the
   reasoning and showing real worked numbers.
10. User ran the full sizing engine against real, live flag pairs pulled
    directly from the actual `clv_log.csv` (found and provided by Claude
    via Claude in Chrome), covering three distinct real paths:
    - A very high-edge same-game pair (Drake Maye Pass+Rush Yards under
      374.5, model probability 0.9765; Sam Darnold Pass Yards under
      358.5, model probability 0.9825): correctly produced
      `status: sized_capped_at_max_position`, $25.00 on a $500 bankroll
      (5%), with every intermediate value (combined probability 0.9594,
      raw Kelly 0.9391, quarter-Kelly 0.2348, platform-dampened 0.1643,
      same-game-dampened 0.1397, uncapped $69.85) hand-verified against
      the code's own output.
    - A smaller-edge same-game pair (two different Drake Maye Pass+Rush
      Yards lines, one over/one under): initially mis-predicted by Claude
      as a below-breakeven no-bet case — a real error, conflating the
      57.7% *per-leg* breakeven (Session 2.5) with the true *combined*
      two-leg breakeven of 1/3 ≈ 33.3% for a 3x-payout entry. The real
      combined probability (0.365) was actually above 1/3, and the
      script correctly returned a small positive stake ($3.48, later
      re-confirmed at that same value with the same-game flag applied).
      Corrected openly in the same turn once the real output didn't
      match the prediction, with the corrected math shown directly
      against the real numbers.
    - A genuine below-breakeven pair (Jaxon Smith-Njigba Rec Yards under
      99.5, model probability 0.535; Hunter Henry Rec Yards under 49.5,
      model probability 0.547): combined probability 0.293, correctly
      produced `status: no_bet_negative_edge`, raw Kelly −0.0606 (floored
      to 0, never a negative stake).
11. User re-ran `test_sizing_engine.py` after updating to the version
    with the same-game dampener; all 8 checks (including the new
    `test_7`) passed, matching the predicted same-game vs. cross-game
    stake split exactly ($25.76 vs. $30.31 on the synthetic fixture).

**Files created/modified:**
- `/scripts/sizing/sizing_engine.py` (new)
- `/scripts/sizing/test_sizing_engine.py` (new — not in the original card)
- `/docs/sizing_methodology.md` (new)

**Validation results:**
- PASS — Sizing logic produces a concrete stake suggestion for every
  CLV-positive flagged opportunity. Confirmed on four distinct real flag
  pairs pulled from the live `clv_log.csv`: two capped at $25.00, one
  uncapped at $3.48, and one correctly returning $0 with
  `no_bet_negative_edge` — never a negative number in any case.
- PASS — Platform-specific risk adjustment present and documented. The
  0.70 PrizePicks dampener is visible in every real output; Underdog is
  fully gated off (rejected with a stated reason) rather than sized off
  an unsourced number.
- PASS — Sanity-checked against real manual examples: stake rose
  monotonically with combined probability across every real pair tested
  ($0 → $3.48 → $25.00-capped), and every intermediate Kelly-formula
  value was independently hand-verified against the real code output.
- PASS — Bankroll cap enforced in code, hit twice on real data (both
  exactly 5% of a $500 bankroll), never exceeded.
- PASS (added mid-session) — Same-game caution dampener confirmed on both
  synthetic data (`test_7`, 8/8 checks passing) and real data (the same
  real flag pair's uncapped stake moved from $15.15 to $12.88 once the
  flag applied; both real capped-example pairs also correctly showed
  `same_game_pair: True`).

**Decisions made:**
1. v1 scoped to exactly one entry type (PrizePicks 2-pick Power Play),
   reusing Session 2.5's sourced 3x payout — every other combination
   rejected with a stated reason rather than guessed. See ROADMAP.md's
   Session 2.6 card, Decision #1.
2. Fractional Kelly (`KELLY_FRACTION = 0.25`) used, not full Kelly —
   standard practice given this project's own model has real, named
   estimation uncertainty (no opponent/injury/pace adjustment yet).
3. `PLATFORM_RISK_MULTIPLIER["prizepicks"] = 0.70` is a stated, unsourced
   judgment call, assessed directly with the user and accepted as a v1
   placeholder rather than delayed pending a number this project's
   research cannot currently produce.
4. `SAME_GAME_CAUTION_MULTIPLIER = 0.85` added mid-session, at the user's
   explicit direction following a discussion of same-game correlation
   risk — a deliberate "flag as riskier, don't pretend to precisely
   model" choice, reported explicitly in the output rather than applied
   silently.
5. `MAX_SINGLE_POSITION_PCT = 0.05` enforced as a hard ceiling in code,
   confirmed binding on real data twice this session.
6. All three judgment-call constants (`KELLY_FRACTION`,
   `PLATFORM_RISK_MULTIPLIER`, `SAME_GAME_CAUTION_MULTIPLIER`) are
   explicitly named as placeholders, not derived figures — re-deriving
   them against real graded outcomes is Session 8.3's job, matching this
   project's existing pattern (Session 2.4's edge threshold, Session
   2.5's target win rate).

**Corrections/reversals during the session:**
1. **Session 2.5's files were missing from the real repo at the start of
   this session** — closed in chat, but never actually pushed. Found by
   checking GitHub directly before starting any Session 2.6 work, rather
   than assuming the prior session's handoff had landed. User confirmed
   and completed the push; re-verified directly before proceeding.
2. **A predicted no-bet test case was actually a real, small positive-
   edge case** — Claude's own error, conflating the 57.7% per-leg
   breakeven with the true 1/3 combined-probability breakeven for a
   2-leg entry. Caught and corrected openly against the real script
   output in the same turn, rather than the prediction being quietly
   dropped.

**Open items / deferred validations:**
- None blocking Session 2.7 from starting.
- Sizing coverage remains limited to the PrizePicks 2-pick Power Play —
  extending to other entry sizes or to Underdog requires first sourcing
  those platforms'/entry types' real payout multipliers, not built or
  guessed at this session.
- `KELLY_FRACTION`, `PLATFORM_RISK_MULTIPLIER`, and
  `SAME_GAME_CAUTION_MULTIPLIER` remain unvalidated placeholders by
  design — re-deriving them against real graded outcomes is Session
  8.3's job, once Session 2.5's outcome tracking has real data to check
  against.
- Open Decisions #10 and #11 (from Session 2.4, re-verifying cross-
  platform CLV consensus matching and the Underdog appearances-to-games
  join once Underdog posts real NFL lines) remain open, untouched by
  this session.

**Status at close of session:** Fully closed out. The sizing engine is
built, tested against 8 synthetic scenarios, and validated against
multiple real flag pairs pulled directly from the live `clv_log.csv` —
covering the capped-stake path, the small-uncapped-stake path, the
no-bet path, and the same-game caution flag, all on real data. Two
constants were assessed and accepted as v1 placeholders at the user's
direct request; a third (the same-game dampener) was added mid-session
following a real discussion of correlation risk, at the user's explicit
direction. Next session is Session 2.7 — Automation (GitHub Actions).
