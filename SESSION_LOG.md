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
   session. Reasoning: fixing it blind, with no real NFL data to test
   the fix against, risks false confidence that the real problem (which
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

---

## Session 2.7 — Automation (GitHub Actions)

**Date completed:** 2026-09-02
**Status:** ✅ Complete

**What was actually done:**
1. Read the live `ingest_pickem.py`, `pickem_model.py`, `clv_logger.py`, and
   `sizing_engine.py` directly from GitHub before writing anything, per this
   project's standing pattern.
2. Identified a real architecture problem before writing code: GitHub
   Actions runners are stateless between runs — nothing written to disk
   during a run survives to the next one unless explicitly committed back.
   `clv_logger.py` depends on reading the *previous* run's `clv_log.csv` to
   correctly tell "still open" from "closed" (a flag not seen in the
   current pull is treated as closed). Without persistence, every run
   would start from an empty log and misclassify every prior flag as
   closed with meaningless closing values — silently corrupting the CLV
   history this project's whole validation methodology depends on. Raised
   this with the user before writing any code; user approved having the
   workflow auto-commit `clv_log.csv` and its snapshot back to the repo
   using GitHub's built-in `GITHUB_TOKEN`.
3. Read `sizing_engine.py` directly and found it requires a human to name
   two specific flag IDs and a real bankroll figure — there's nothing for
   an unattended job to decide there. Scoped automation to ingestion →
   estimation → CLV logging → digest only, leaving sizing as a manual step
   the user runs himself — consistent with this project's standing "flags
   and sizes, never places bets" rule.
4. Built `scripts/run_pipeline.py`: imports the three existing scripts as
   modules (not subprocess) so real Python exceptions propagate; aborts
   *before* calling `clv_logger.py` if ingestion or estimation returns
   suspiciously empty data, specifically to prevent the corruption
   scenario in (2); writes `output/digest/digest_latest.md` (a plain
   table of currently open flags, sorted by edge — sizing stays manual, so
   this is what a person scans to pick a pair worth sizing) and a dated
   copy per run; logs to `logs/pipeline.log`.
5. Built `.github/workflows/pickem_pipeline.yml`: scheduled trigger plus
   manual `workflow_dispatch`, installs dependencies, runs the
   orchestrator, then commits `clv_log.csv`/snapshot/digest back to the
   repo only if the pipeline succeeded.
6. **Run #1 (first real GitHub Actions execution) failed:**
   `ModuleNotFoundError: No module named 'schema'`. Root cause:
   `ingest_pickem.py` does a plain `from schema import ...` of a sibling
   file in its own folder — this only resolves automatically when Python
   runs the script directly (`python ingest_pickem.py`), which adds that
   folder to `sys.path`. Loading the script via `importlib` (what
   `run_pipeline.py` does) doesn't do that automatically. Fixed by
   temporarily inserting each script's own folder onto `sys.path` for the
   duration of its load, then removing it — verified the pipeline never
   touched `clv_log.csv` before this failure, confirming the safety design
   in (4) worked as intended on a real failure, not just in theory.
7. **Run #2 failed differently:** `ModuleNotFoundError: No module named
   'pyarrow'`. Root cause: `pickem_model.py` reads nflverse's parquet
   files, which requires `pyarrow` — present on the user's local machine
   (apparently a side effect of installing something else) but never
   listed in `requirements.txt`. Ingestion had already succeeded in this
   run (31,076 real rows); confirmed the orchestrator correctly stopped
   before CLV logging rather than running it on a broken estimation step.
   Fixed by adding `pyarrow` to `requirements.txt`.
8. **Run #3 succeeded end-to-end** — first fully clean run: real commit
   from `pickem-pipeline-bot`, `clv_log.csv` updated (2,979 rows changed),
   new dated snapshot, both digest files written.
9. User ran `pip freeze` on the local machine and asked about three
   packages present locally but not in `requirements.txt`
   (`beautifulsoup4`, `fastparquet`, `PuLP`). Answered directly: none were
   needed, proven by run #3's own success with only the five packages
   actually listed. `PuLP` is most likely staged ahead of a future
   ILP-optimizer session (matching the DFS repos' pattern); the other two
   are most likely artifacts of prototype/troubleshooting scripts, not the
   production path. No `requirements.txt` change made on this basis.
10. **Extended, real troubleshooting of GitHub's scheduled ("cron")
    trigger not firing at all**, spanning roughly 5 hours of the session:
    - Initial schedule set to `0 * * * *` (top of hour), then proactively
      moved to `7 * * * *` before any evidence of a problem, based on
      GitHub's own documented guidance that top-of-hour is their busiest,
      most delay-prone scheduling slot.
    - After ~3 hours with zero scheduled firings (only manual runs
      showing), user asked for the schedule to be temporarily set to
      every 5 minutes (`*/5 * * * *`) to shorten the feedback loop rather
      than waiting up to an hour per test.
    - Systematically ruled out, one at a time, checked directly against
      the live repo/account rather than assumed: file syntax/content
      (confirmed correct via direct GitHub view each time), Actions
      billing/quota (7 of 2,000 included minutes used), workflow-disabled
      state (no warning banner present), repo Actions permissions (set to
      allow-all, read/write confirmed working via successful auto-commits),
      and a GitHub-wide platform incident (status page showed none).
    - At user's request, manually triggered the *current* file directly
      (run #4) specifically to isolate "is it the file or the schedule" —
      succeeded cleanly in 1m 12s, proving the file itself was correct and
      the problem was specific to the scheduled trigger.
    - Tried a documented community workaround: a trivial re-push of the
      workflow file (comment-only change, no functional difference) to
      "kick" GitHub into re-registering the schedule.
    - **Run #5 fired as a genuine `"Triggered via schedule"` run
      approximately 1h39m after that re-push** — confirming the schedule
      was not permanently broken, just very slow (about 1h40m) to register
      after a schedule change. This matches community-reported behavior,
      not officially documented by GitHub.
    - User initially asked to park this as a deferred item for a future
      session; before that could be finalized, user observed run #5 live
      and the plan changed to reverting to the intended hourly cadence and
      continuing to watch rather than deferring.
    - Reverted schedule to `7 * * * *` (final, intended value) immediately
      after run #5 confirmed the trigger worked, to stop the 5-minute
      testing cadence from continuing to hit PrizePicks/Underdog
      overnight. User pushed this before ending the session for the day.
    - **Runs #6, #7, and #8 all fired overnight as genuine scheduled runs**
      (all `"Scheduled"` trigger, all succeeded, all produced real
      auto-commits) — confirmed the next morning by reading run timestamps
      and the commit history directly, cross-checking that every
      successful run had a matching `pickem-pipeline-bot` commit.
11. Spot-checked the real overnight digest (`output/digest/digest_latest.md`,
    run #8, 2026-09-02T09:32:05Z): 30,373 rows ingested, 126 newly flagged,
    0 newly closed, 3,452 still open, 3,856 total ever logged, real
    September NFL game dates in the open-flags table — confirmed the
    digest reflects real data correctly, not just a plausible-looking
    placeholder.

**Files created/modified:**
- `/scripts/run_pipeline.py` (new)
- `.github/workflows/pickem_pipeline.yml` (new)
- `/requirements.txt` (modified — added `pyarrow`)

**Validation results:**
- PASS — Workflow runs successfully on GitHub Actions' own infrastructure
  at least 3 times on schedule. 4 confirmed real scheduled runs (#5–#8),
  all green, all with matching real auto-commits.
- PASS — Failure in one step doesn't silently corrupt downstream steps.
  Proven twice on real failures (runs #1 and #2), not just by design:
  `clv_log.csv` was correctly untouched both times the pipeline stopped
  early.
- PASS — Digest output complete and matches what a manual run would
  produce. Confirmed against real overnight data (see item 11 above).
- PASS — Secrets, if any needed, handled via GitHub Actions secrets, not
  committed anywhere. No secrets needed at all; none committed. Trivially
  satisfied.

**Decisions made:**
1. Sizing (`sizing_engine.py`) explicitly excluded from the automated
   pipeline's scope. Automation covers ingestion → estimation → CLV
   logging → digest only; sizing stays a manual step run by the user,
   since it requires naming specific flag IDs and a real bankroll figure
   that an unattended job has no basis to choose. A real, deliberate
   deviation from the original roadmap card's description — see
   ROADMAP.md.
2. `clv_log.csv` persistence handled via the workflow auto-committing back
   to the repo using GitHub's built-in `GITHUB_TOKEN` — necessary because
   GitHub Actions runners are stateless between runs and `clv_logger.py`
   depends on reading the prior run's output.
3. Schedule set to hourly (`7 * * * *`, off the exact top of the hour),
   matching the existing Windows Task Scheduler cadence as a known-safe
   baseline. Actual observed cadence in practice is slower and irregular
   (see Open items below) — worth revisiting, not blocking.
4. `run_pipeline.py` loads the three underlying scripts via `importlib`
   rather than `subprocess`, so real Python exceptions (not just exit
   codes) propagate to the orchestrator and can be caught, logged, and
   used to decide whether it's safe to proceed to the next stage.

**Corrections/reversals during the session:**
1. **`run_pipeline.py`'s first real run failed with `ModuleNotFoundError:
   No module named 'schema'`** — `importlib`-based loading doesn't
   replicate Python's automatic `sys.path` behavior when a script is run
   directly. Fixed by temporarily adding each script's own folder to
   `sys.path` for the duration of its load.
2. **Second real run failed with `ModuleNotFoundError: No module named
   'pyarrow'`** — present locally, missing from `requirements.txt`. Fixed
   by adding it.
3. **Initial plan to "park" GitHub Actions scheduling as a deferred item
   was reversed mid-conversation** once a genuine scheduled run (#5) was
   observed live — the underlying problem turned out to be a one-time,
   slow (~1h40m) schedule-registration delay rather than a persistently
   broken feature, so the session continued to a real close instead of
   deferring.

**Open items / deferred validations:**
- **Scheduled-run cadence is irregular in practice.** Observed gaps
  between real scheduled runs were 2h16m, 4h19m, and 5h9m — not the
  intended hourly cadence, despite the schedule being correctly set to
  `7 * * * *`. This looks like GitHub's documented behavior of
  delaying/coalescing scheduled triggers under load on their end, not a
  bug in this workflow, but hasn't been observed over a long enough
  window to characterize with confidence. Revisit once NFL season data
  volume ramps up (season starts ~Sept 7) and freshness starts to matter
  more; local Windows Task Scheduler remains the reliable hourly path in
  the meantime, untouched by any of this.
- `data/pickem/clv_snapshots/` grows by one file per successful run
  forever (roughly 24/day if hourly cadence is eventually achieved). Not
  a problem yet; worth a pruning step in a future session once it's
  actually a nuisance.
- Open Decisions #10 and #11 (from Session 2.4) remain open, untouched by
  this session.

**Status at close of session:** Fully closed out. All four roadmap
validation items pass on real evidence, not just design: 4 genuine
GitHub-triggered scheduled runs, two real (not simulated) failure cases
proving the pipeline fails safely, and a real overnight digest confirmed
against real data. The GitHub-side scheduling delay that dominated this
session's troubleshooting time resolved itself once properly diagnosed as
a registration-delay issue rather than a broken feature — no external
support ticket was ultimately needed. One open item (irregular scheduled
cadence) is noted for future attention but does not block moving forward.
Next session is Session 2.8 — Frontend (Cloudflare Pages).


---

## Session 2.8 — Frontend (Cloudflare Pages)

**Date completed:** 2026-09-02
**Status:** ✅ Complete

**What was actually done:**
1. Read the DFS sibling repos' existing frontend (`dfs_optimizer_frontend/`)
   directly on GitHub before building anything. Found it to be a single
   static HTML file with no framework and no build step, but one that
   requires the user to manually drag-and-drop a CSV to view it — not a
   fit here, since this session's whole point is showing *live automated*
   data with no manual step. Built a new static `/frontend/` from scratch
   instead, following the same "single static file, no framework" spirit
   but wired to read real pipeline output automatically.
2. Read `output/digest/digest_latest.md` and `data/pickem/clv_log.csv`
   directly before choosing a data source. Found the digest is a 500+ KB
   growing text file, a poor fit for a webpage to parse. `clv_log.csv` is
   a single, continuously-updated structured file with a `status` column
   (open/closed) and a `clv_edge_at_close` column — the right single
   source for both the flagged-opportunities table and the performance
   trendline. `output/estimation/` was also checked and ruled out — it
   writes a new timestamped file every hourly run with no single "latest"
   file to point a static page at.
3. Built `/frontend/index.html`, `/frontend/style.css`, `/frontend/app.js`
   — plain HTML/CSS/JS, no framework, matching the DFS repos' static-file
   pattern. `app.js` fetches `data/clv_log.csv` client-side, parses it,
   and renders a summary stat row, an SVG trendline chart (hand-drawn, no
   charting library), and two tables (open flags, recently closed flags).
4. Attempted first Cloudflare Pages setup via the dashboard's newer unified
   "Create application" flow. This silently created a **Worker**
   (`market-betting`, under `/workers/services/...`) rather than a
   **Pages** project — confirmed by the presence of a "Deploy command"
   field (`npx wrangler deploy`), which only exists on Workers. Cloudflare
   then tried to prepare the whole repo to run as a program and began
   installing `requirements.txt`'s Python packages (`pandas`, `numpy`,
   etc. — needed by the pipeline scripts, not the frontend), and the build
   never completed. Diagnosed by reading the build log directly rather
   than assuming; root cause confirmed before attempting any fix.
5. User deleted the failed Worker project. Rebuilt it correctly via the
   dashboard's legacy "Continue to Pages" → "Import an existing Git
   repository" flow, which is the genuine Pages product. Settings used:
   framework preset **None**; build command
   `mkdir -p frontend/data && cp data/pickem/clv_log.csv frontend/data/clv_log.csv`;
   build output directory `frontend`; root directory `/`; production
   branch `main`. First deploy succeeded (1m 25s) once `/frontend/` was
   actually pushed to GitHub (an initial deploy attempt ran before the
   three frontend files had been committed locally — caught immediately
   by checking the build's "Assets uploaded" list, which showed only the
   copied `clv_log.csv` and none of the frontend files).
6. Checked the live site's actual numbers against the real data rather
   than assuming a successful deploy meant a correct page. Found the
   "cumulative CLV edge" stat read **+11,262.6%** — not plausible. Traced
   the cause: the chart summed the raw `clv_edge_at_close` percentage
   across all 404 closed flags, and summing a percentage across hundreds
   of independent flags grows without bound and stops meaning anything,
   even though every individual flag's edge was a normal, believable size
   (confirmed real values like 8%, 28%, 48% directly in the CSV). Fixed by
   changing the stat and the trendline to a **running average** per closed
   flag instead of a running sum — this is also the more correct match to
   the roadmap's "is the system right more often than chance, over a large
   sample" goal. Re-verified live after the fix: **+27.9% average edge**,
   a plausible number.
7. Checked mobile responsiveness on the live site. The connected browser's
   window would not resize in this environment, so verified instead by
   loading the live page inside a 390px-wide iframe injected into the
   page, and separately confirmed programmatically that both tables'
   scroll containers report `scrollWidth > clientWidth` (888px of content
   in a 399px box) and that `scrollLeft` actually moves — the tables
   scroll independently of the page rather than breaking the layout.
   Confirmed visually as well: stat grid switches to 2 columns, chart and
   footer render cleanly, nothing overflows the viewport.
8. Read `scripts/sizing/sizing_engine.py` directly before deciding how to
   handle the roadmap card's "sizing suggestions" language. Found it is a
   manual, per-entry calculator, not a batch job: it requires a human to
   name exactly two specific flag IDs (PrizePicks only — no sourced payout
   multiplier exists for any other platform/leg-count combination) and a
   real bankroll figure typed in fresh each run; it has no memory of
   bankroll across runs. Confirmed with the user this reflects a genuine
   design constraint, not just a missing config value — nothing in the
   project decides which two of 3,452+ open flags should be paired into
   an entry, so full automation would require inventing a new leg-pairing
   strategy from nothing, which was explicitly out of scope for this
   session.
9. User decided sizing should stay part of Session 2.8 rather than being
   deferred, and confirmed it should remain exactly as manual as the
   script already is (no in-page bankroll tracking across entries either
   — the user carries that themselves, same as running the CLI twice).
10. Added a sizing calculator to the frontend: a checkbox on every open-flag
    table row, a "Selected legs" panel, and a bankroll input field. When
    exactly two PrizePicks legs are checked and a bankroll is entered, the
    page runs the same math as `sizing_engine.py` — quarter-Kelly, the
    0.70× PrizePicks account-risk dampener, the 0.85× same-game caution
    multiplier, and the 5%-of-bankroll cap — ported by hand into
    JavaScript (`sizeEntry()` in `app.js`), since the site is static and
    cannot call the Python script directly. The bankroll figure is never
    saved anywhere; it lives only in the browser tab for that session.
    Clear rejection messages are shown (not exactly two legs selected,
    mixed platforms, missing bankroll) rather than a blank or silently
    wrong result.
11. Verified the ported JavaScript math against the real Python formula
    before handing it over: ran the same three test cases (a normal
    entry, a same-game entry, a negative-edge entry) through both a
    Python reimplementation and the new JavaScript side by side — every
    intermediate number matched exactly. Also built a headless DOM test
    harness (Node + jsdom) to run the actual shipped `app.js` and
    `index.html` end to end — simulated checking two PrizePicks boxes and
    typing a bankroll, confirmed the page rendered the correct dollar
    figure, and confirmed all three rejection paths produce clear,
    specific messages rather than failing silently.
12. Selected two real open PrizePicks flags on the live deployed site and
    entered a real bankroll, confirming the calculator works correctly
    against genuine live data end to end (not just the local test
    harness): returned `$25.00, Sized — capped at 5% of bankroll`, with a
    full, internally consistent breakdown.
13. While testing the sizing calculator against live data, noticed nearly
    every open flag's `first_flagged_model_prob` reads extremely close to
    100% (and `first_flagged_edge` correspondingly reads +50.0% for
    effectively every open row checked). This may be legitimate for
    certain stat/line combinations, or may indicate the estimation step
    is saturating for some inputs — not investigated further this
    session, since it's a data-quality question upstream of both the
    dashboard and the sizing calculator, not a bug in either. Flagged to
    the user directly rather than silently building on top of it. See
    Decisions and Open items below, and new Open Decision #13 in
    ROADMAP.md.

**Files created/modified:**
- `/frontend/index.html` (new)
- `/frontend/style.css` (new)
- `/frontend/app.js` (new)
- Cloudflare Pages project `market-betting` (new — dashboard configuration,
  not a repo file; connected to `drgregmscott-tech/Market_Betting`, branch
  `main`, auto-deploying on every push)
- `ROADMAP.md` (Session 2.8 card marked complete; new Open Decision #13
  added)
- `SESSION_LOG.md` (this entry)

**Validation results:**
- [x] Frontend deploys successfully and is reachable at a live URL —
  `https://market-betting.pages.dev`, confirmed live, auto-redeploying on
  every push to `main` including the hourly pipeline's own automated
  commits (verified directly: a real pipeline-triggered push produced a
  new successful deploy with no manual action taken).
- [x] Displays current flagged opportunities pulled from real automated
  output, not mock data — confirmed the page's row counts (3,452 open,
  404 closed) exactly match the real `clv_log.csv`'s real row count
  (3,856 total rows, confirmed directly via GitHub's own line count).
- [x] Displays a CLV-performance trendline view — present, and corrected
  mid-session from a meaningless raw-sum metric (+11,262.6%) to a
  believable running-average metric (+27.9%), verified live after the
  fix.
- [x] Confirmed working on both desktop and mobile view — see item 7
  above for the specific checks performed.

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

**Corrections/reversals during the session:**
1. **Unified Cloudflare "Create application" flow → legacy "Continue to
   Pages" flow.** The first deploy attempt used the newer dashboard flow
   and produced a Worker, not a Pages project, causing a build failure
   (see item 4 above). Corrected by deleting the Worker and recreating
   the project via the legacy Pages-specific import flow.
2. **First live deploy included no frontend files.** The first successful
   Cloudflare build only uploaded `data/clv_log.csv` (the build
   command's own output) — `/frontend/index.html`, `style.css`, and
   `app.js` had not actually been committed and pushed yet at that point.
   Caught by checking the deploy's "Assets uploaded" list directly rather
   than assuming a green build meant a correct one. Corrected once the
   three files were actually pushed.
3. **"Cumulative CLV edge" (running sum) → "Average CLV edge" (running
   average).** See item 6 and Decision #3 above. Caught by checking the
   live page's actual numbers against a plausibility check, not by
   assuming a successful, error-free deploy meant a correct result.

**Open items / deferred validations:**
- **New Open Decision #13** (see ROADMAP.md): nearly every open flag's
  `first_flagged_model_prob` observed live is extremely close to 100%,
  which may be legitimate or may indicate an estimation-step issue for
  some stat types. Not yet investigated. Action needed: spot-check
  `first_flagged_model_prob` for a handful of these open flags (e.g. a
  low-line "Sacks Under 1.5" PrizePicks flag) against
  `pickem_estimation_model_spec.md`'s actual formula to confirm the value
  is a genuine model output, not a bug or placeholder. This affects the
  sizing calculator's real-world reliability directly, since the
  probability feeds straight into the Kelly calculation — the calculator
  itself is verified correct given whatever probability it's handed, but
  a bad input still produces a misleading suggested stake.

**Status at close of session:** Fully closed out, including sizing, per the
user's explicit request to fold sizing into this session rather than defer
it. Live dashboard, corrected trendline, sizing calculator, and mobile
responsiveness are all built and verified against real live data. One new
open item (#13) is carried forward, not blocking, and not silently
absorbed. Next session is Session 2.9 — Live Paper-Trading Validation
Window, per ROADMAP.md.

---

## Session 2.9 (continuation) — Pipeline Correctness Fixes & Sport-Coverage Discovery

**Date completed:** 2026-09-02
**Status:** ✅ Complete (as prerequisite/discovery work — see Status note below;
this is distinct from Session 2.9's own defined validation-window scope, which
has not started)

**Context:** Session 2.9 proper (ROADMAP.md) is a soak-test/go-no-go review —
no new code, just watching real data accumulate. That window can't meaningfully
start until real games exist to bet on (NFL season starts 2026-09-07). Opening
this session by reading the live repo state (per this project's standing
session-open convention) surfaced three real, live bugs standing between the
pipeline and that window even being possible — this entry documents fixing
those, plus a scope correction on what "done" means for this track.

**What was actually done:**
1. Spot-checked **Open Decision #13** (near-100% `first_flagged_model_prob`
   observed on the live frontend) against the real `clv_log.csv`, not just the
   dashboard view. Found the real distribution is mostly normal — only 4.9% of
   3,461 open flags sat at 99–100% probability, another 6.6% at 95–99%; 74.3%
   sat in the ordinary 50–85% range. The near-100% impression came from
   `app.js` sorting the open-flags table by `first_flagged_edge` descending,
   which surfaces exactly the highest-probability rows first — a display
   artifact, not an estimation bug. **Resolved, no code change needed.**
2. Investigated **Open Decision #11** (Underdog join only resolving 41% of
   appearances) by reading `normalize_underdog()` in `ingest_pickem.py`
   directly and comparing it against a live Underdog snapshot. Found the real
   cause: Underdog's feed splits scheduled events across `games` (team
   sports), `solo_games` (individual sports — tennis), and a third,
   undocumented category tagged `match_type: "Series"` whose match ID exists
   in neither list. The code only ever read `games`. Live check confirmed 129
   of 190 real appearances in that moment were real NFL props tagged
   `"Series"` — meaning Open Decision #10's "Underdog has zero NFL lines"
   finding was already stale.
3. Fixed `normalize_underdog()`: added a `solo_games` lookup, a fallback join
   (`games` → `solo_games`), and a fallback to the player's own `sport_id`
   field when neither game container exists yet. Verified against the live
   feed before and after: sport resolution went from 89/217 (41%) to 191/191
   (100%) real appearances.
4. Manually triggered the fixed pipeline (`run_ingest.bat` locally, then the
   GitHub Actions workflow via its `workflow_dispatch` trigger) to validate
   for real rather than waiting on the next scheduled hour. First manual
   workflow run (**#10**) failed with a new, different crash:
   `AttributeError: 'float' object has no attribute 'strip'` in
   `pickem_model.py`'s `resolve_stat_spec()`. Root cause: pandas represents a
   genuinely blank `stat_type` cell as `NaN` (a float), and the existing guard
   `if not stat_type` doesn't catch `NaN` because `not float('nan')` is
   `False` in Python. This bug pre-existed but was never exercised before,
   since rows with no resolved sport were discarded upstream before reaching
   this function — fixing item 3 above is what surfaced it.
5. Fixed `resolve_stat_spec()`: replaced the guard with
   `isinstance(stat_type, str)`, which correctly catches `None`, `NaN`, and
   any other non-string value the same way. Reproduced the exact real crash
   locally with a `NaN` input, confirmed the fix resolves it, confirmed
   normal string inputs are unaffected. Re-ran the workflow (**#12**) — green,
   26,464/26,464 rows estimated, no crash.
6. User asked, correctly, why Underdog still showed zero flagged rows even
   after both fixes. Investigated using inference only (no direct visibility
   into the estimation stage's real per-row output, since it was never
   committed to GitHub) and gave a wrong answer — guessed the 3% flagging
   threshold wasn't being cleared. **This was a real miss, corrected below.**
7. Fixed the visibility gap that caused item 6's wrong guess: added a
   `output/estimation/latest.csv` write to `pickem_model.py` (mirroring
   `ingest_pickem.py`'s own existing `latest.csv` pattern) and added that path
   to `pickem_pipeline.yml`'s commit step. Deliberately did NOT commit the
   hourly timestamped files, to avoid unbounded repo growth — same boundary
   ingestion's own timestamped snapshots already respect.
8. With real per-row visibility now available (workflow run **#13**), found
   the real, correct answer: zero Underdog rows had ever reached a computed
   edge at all. 92 rows were CFB/Tennis (`unsupported_sport` — correct, known
   v1 scope boundary). The other 178 were real NFL rows correctly tagged
   `sport = NFL` by item 3's fix, but ALL of them came back
   `unsupported_stat_type` with a **blank** stat name — not a wording
   mismatch as first assumed.
9. User pushed back a second time: the investigation kept narrowing to NFL
   specifically, when the project's actual scope is +EV bets across all
   markets, and other sports (tennis, CFB, baseball) are live right now while
   the NFL season hasn't started. This was a fair, repeated correction — see
   Corrections/reversals below.
10. Traced the blank-stat-name rows to their real cause: Underdog never
    populates the clean `display_stat` field for any of these three
    categories — NFL "Series" props, CFB, or Tennis. Pulled a real live
    example directly (Carlos Alcaraz, "Higher 33.5 Games Played", real match
    starting 2026-09-03) and confirmed the real stat name exists only as free
    text on the price option itself (`selection_subheader`), never in a
    clean field.
11. Fixed `ingest_pickem.py` a second time: added
    `_stat_type_from_subheader()`, a regex-based fallback
    (`"Higher/Lower {number} {stat name}"`) used only when the clean field is
    empty. Verified against the full live feed: 245 of 263 live lines (93%)
    now resolve a real stat name, including genuine per-match tennis props
    (Aces, Double Faults, Games Won, Points Won, Breakpoints Won) that were
    previously completely invisible. 18 lines still return no stat name and
    are left as a stated, unexplained gap rather than forced.
12. Re-ran the workflow after this final fix — green, confirmed via
    `output/estimation/latest.csv` that the real breakdown matches
    prediction: 178 named `unsupported_stat_type` rows (real stat names now
    attached), 86 `unsupported_sport` rows (correctly named, correctly out of
    the NFL-only model's current scope), only 18 residual blanks.

**Decisions made:**
1. `solo_games` is treated as **optional** in `normalize_underdog()`'s schema
   check (the pipeline won't abort if Underdog ever drops it), consistent
   with this file's existing "keep running on a partial schema, log and skip"
   design rather than the stricter all-or-nothing check used for the other
   four top-level lists.
2. Only `output/estimation/latest.csv` is committed to GitHub, not the hourly
   timestamped snapshot files — matches the existing boundary already applied
   to ingestion's own timestamped output, to avoid unbounded repo growth.
3. The three ingestion/estimation fixes made in this session are scoped to
   **visibility and correctness** (making real stats and sports show up
   correctly, by name, without crashing) — not to building real estimation
   support for Tennis, CFB, or NFL season-long props. That remains real,
   separate, undecided work.

**Corrections/reversals during the session:**
1. **Wrong guess on why Underdog showed zero flags → real answer found via
   direct evidence.** First explanation (edge threshold not cleared) was
   inference without the data to back it up. Corrected once
   `output/estimation/latest.csv` existed and could be checked directly — the
   real cause was structural (blank stat names), not a threshold question.
   Recorded as a real miss, not silently revised.
2. **NFL-only investigation frame → corrected to all-sports frame, twice.**
   First correction: user pointed out CFB/Tennis were being treated as
   "known scope, nothing to fix" without actually checking what was in that
   bucket — which turned out to share the exact same root cause as the NFL
   issue and included real, live, currently-tradeable tennis props. Second
   correction: user pointed out the investigation was still narrowing back to
   "which two extra sports" instead of the project's actual stated scope —
   +EV bets across all betting markets, not one or two additional sports
   layered onto NFL. This reframed the next session's real open item (see
   Open Decisions below) from a narrow "add Tennis/CFB" ask into a proper
   full-market inventory.

**Open items / deferred validations:**
- **New Open Decision #14** (see ROADMAP.md): a full inventory of every sport
  currently live on both pick'em platforms, checked against what's actually
  gradeable, is needed before this track's real scope can be called
  complete — not just whichever sport happened to be in front of the model
  that week. Not started this session; scoped as its own session below.
- Session 2.9's own defined validation window (sample-size threshold, real
  graded outcomes, go/no-go decision) has **not** started — nothing in this
  session's work substitutes for it. It remains blocked on the 2026-09-07
  NFL season start, same as before this session began.
- The 18 Underdog lines that still return no stat name even after item 11's
  fix are a real, unexplained residual gap. Not investigated further this
  session — worth a look once broader sport coverage is being scoped, not
  urgent on its own.

**Status at close of session:** Complete as prerequisite/discovery work, not
as Session 2.9's own defined scope. Three real, live bugs found and fixed,
each verified against real live data (not synthetic) before and after: the
Underdog join gap, a hidden estimation crash the join fix exposed, and a
stat-name visibility gap affecting NFL, CFB, and Tennis alike. One process gap
also fixed (estimation output is now visible on GitHub going forward, not just
during the run that produced it). The real Session 2.9 soak-test window still
has not begun — that remains blocked on the 2026-09-07 NFL season start, as it
was before this session. Next session, **Session 2.10 — Cross-Sport +EV
Inventory (Track 1)**, addresses new Open Decision #14 before Session 2.9's
validation window is revisited, per ROADMAP.md.

---

## Session 2.10 — Cross-Sport +EV Inventory (Track 1)

**Date completed:** 2026-09-03
**Status:** ✅ Complete, with one validation item deferred to a bounded,
automated follow-up (not left open-ended, not a new numbered session).

**Context:** Addresses Open Decision #14 (opened Session 2.9 continuation).
Track 1's estimation model has been NFL-only since Session 2.3, and every
prior attempt to broaden it kept narrowing back to "which one or two extra
sports" rather than asking the real question once, deliberately. This
session exists to do that properly.

**What was actually done:**

1. **PrizePicks and Underdog checked live**, not from memory. PrizePicks:
   29 distinct leagues confirmed in one live pull (22,657–26,215
   projections across runs), a much broader platform than any prior
   session had assumed. Underdog: 3 sports confirmed live across four
   separate same-day pulls (NFL season-long futures, CFB, Tennis) — MLB
   notably absent from every pull despite being mid-season, flagged as a
   real finding pending further confirmation (see deferred item below).

2. **Real, named data-source answers found for every sport**, not just
   the largest. Strong candidates with official, free, no-key sources
   confirmed live: **NFL** (`nflverse`, already in production), **MLB**
   (MLB Stats API), **NBA** (`nba_api`, official NBA.com data — out of
   season so a live spot-check has to wait for October, but the source
   itself is confirmed), **EPL** (the official Fantasy Premier League
   API, confirmed live with real per-player stats), **soccer outside
   EPL** — La Liga, Bundesliga, Ligue 1, MLS (ESPN's public sports API,
   confirmed live for La Liga/EPL/MLS directly; real per-player stats
   found under `rosters[].roster[].stats`, not the more obvious
   `boxscore.players` path), **UFC** and **golf** (same ESPN API family,
   confirmed live), **F1** (Jolpica, the maintained successor to the
   now-retired Ergast API). Real, honest gaps found and named rather than
   skipped: **Tennis** (no adequate free real-time source), **KBO, NPB,
   handball, badminton** (nothing found), most **esports** (the
   professional provider is paid-only; free alternatives are
   community-run, not official). **Cricket** is a real, useful structural
   exception worth remembering: the same ESPN URL pattern that worked for
   every other sport checked returns 404 for cricket specifically — it
   lives on a separate ESPN API family entirely. **CFB** has a working
   source (CFBD API) but needs a free key and has a 1,000-call/month cap,
   unlike NFL/MLB/NBA's uncapped sources.

3. **Sport prioritization corrected mid-session** after conflating two
   different questions. The first pass ranked sports by today's live
   snapshot volume, which ranked NBA as "structurally smaller" than
   soccer/MLB — wrong, since NBA being small in one September snapshot is
   a season-calendar artifact (NBA starts in October), not a real fact
   about its size. Corrected using real, sourced US betting-popularity
   data instead: NFL, college football, NBA, MLB, soccer, NHL, MMA/UFC,
   tennis, golf, boxing (top 10, in that order). NASCAR was raised as a
   hypothesis and explicitly not confirmed — it did not appear in any
   popularity source checked, and was named as unconfirmed rather than
   added on assumption.

4. **A real bug found and fixed in the research tooling itself**: the
   first version of `sport_inventory_scan.py` used `api.prizepicks.com`,
   which 403s. The confirmed, working production endpoint (already used
   by `ingest_pickem.py` since Session 2.2) is `partner-api.prizepicks.com`
   — fixed, and the league-matching logic was rewritten to mirror
   `ingest_pickem.py`'s real, confirmed join logic rather than guessed
   again.

5. **A second, related research thread opened and substantially
   resolved**: both PrizePicks and Underdog were found to offer products
   beyond fixed-line pick'em. PrizePicks Predict is a direct Kalshi
   partnership (Team Picks: moneylines/spreads/totals, live in 30
   states; Culture Picks: Yes/No event contracts, live in 47–48 states),
   run through a named regulated entity (Performance Predictions II,
   LLC). Underdog Exchange (UDX) is a separate CFTC-regulated exchange
   via Aristotle Exchange DCM/DCO — not confirmed to be a Kalshi wrapper
   the same way. Checking Kalshi's own public API directly (no login, no
   key — confirmed live) mostly answered the resulting question of
   whether to route through these wrappers: there's no reason to, since
   Kalshi's real markets are already fully open on their own.

6. **Track 3's scope and ranking re-tested against real evidence, using
   the same five criteria Session 0.1 used** (repricing mechanism,
   fee/vig, account-limiting risk, liquidity, legal footprint) — not
   re-litigated on opinion, per direction received mid-session. Findings:
   Kalshi's sports-contract repricing mechanism matches Track 6 (already
   correctly ranked lowest-confidence), not Track 3. Fee schedule
   confirmed low (peaks at 1.75% at a 50¢ price) but this was already
   priced into Kalshi's existing ranking, not new evidence specific to
   sports. Liquidity checked directly on real MLB moneyline markets
   several days out: mostly zero or near-zero volume, 9–12¢ wide
   spreads. Legal footprint checked directly: Kalshi's sports contracts
   specifically are in active, unresolved conflict with over a dozen
   states, including a Nevada court-extended ban and criminal charges
   filed by Arizona (20 counts) — none of this touches Kalshi's weather/
   climate contracts. **Recommendation: Track 3's original scope and
   ranking should stand as originally set** — logged as a recommendation
   for review, not an applied decision.

7. **Deferred item, with a real, verified mechanism, not a vague TODO**:
   confirming Underdog's complete sport list needs real time spread
   across multiple days — checked directly that no shortcut exists (no
   sports-catalog endpoint on Underdog's API; the `games`/`solo_games`
   data already includes near-term scheduled events, not just this-
   instant lines, so this wasn't even a narrower window than assumed).
   Built `scripts/ingestion/sport_inventory_scan_automated.py` (writes
   dated JSON snapshots instead of printing to a screen) and
   `.github/workflows/sport_inventory_scan.yml` (runs it 3x/day for 4
   days — 12 runs — and commits results back to the repo automatically).
   **Verified working end-to-end before being left unattended**: found
   and fixed a real repo misconfiguration first (Actions workflow
   permissions were set to read-only, which would have silently failed
   every commit-back step) via GitHub Settings → Actions → General →
   Workflow permissions → switched to "Read and write permissions."
   Manually triggered one real run via `workflow_dispatch`, watched it
   succeed (48s), and read the actual committed output file directly
   from GitHub to confirm real data (26,215 PrizePicks projections
   across 30 leagues, including two new ones — Darts, Lacrosse — not
   seen in any manual pull) rather than trusting a green checkmark alone.

**Corrections/reversals during the session:**
1. **Plan to keep re-running snapshots indefinitely → replaced with
   calendar logic, at the user's direction.** The original plan assumed
   a sport's absence from a snapshot was mostly random noise requiring
   more sampling. Corrected: it's mostly explained by the public sports
   calendar, which doesn't need repeated sampling to check.
2. **NBA ranked "structurally smaller" than soccer/MLB → corrected.**
   Based on today's live-snapshot volume, which conflated "current
   season timing" with "real size." Fixed using real popularity data
   (see item 3 above).
3. **PrizePicks endpoint bug** — see item 4 above.
4. **"Soccer has no equivalent to `nflverse`" → substantially reversed**
   after the user directly pushed back on a too-shallow first pass. The
   first check only compared generic third-party football-API listings
   without checking whether the leagues themselves ran open data
   infrastructure the way NFL/MLB/NBA's sources do. The official Fantasy
   Premier League API and ESPN's public sports API both resolved most of
   what was initially reported as a real gap.
5. **"No free source for golf" → reversed** once ESPN's API (already
   confirmed for soccer/UFC) was checked for golf specifically rather
   than assuming the earlier golf-specific-provider search was
   sufficient.

**Files touched:**
- `/docs/research/sport_inventory.md` (new) — full inventory, data-source
  findings, priority list, Part 2 product-scope findings and Track 3
  reassessment, and the deferred item's exact closing plan.
- `scripts/ingestion/sport_inventory_scan.py` (new) — manual scan script
  (fixed PrizePicks endpoint).
- `scripts/ingestion/sport_inventory_scan_automated.py` (new) — same
  scan, built for unattended scheduled runs.
- `.github/workflows/sport_inventory_scan.yml` (new) — bounded, temporary
  4-day/12-run schedule; should be disabled once the deferred item closes.
- `docs/research/scans/` (new directory) — one real file already present
  from the verification run (`scan_2026-09-03T12-41-06Z.json`); more
  will accumulate automatically.
- `ROADMAP.md` — Session 2.10 card closed with the deferral noted; Open
  Decision #14 resolved; two new Open Decisions (#15 deferred-item
  closing plan, #16 Track 3 reassessment recommendation) added.

**Next session:** No new session number needed yet. The immediate next
action is calendar-driven, not a build session: once the 4-day scan
window ends (see Open Decision #15), read the accumulated files and
close out Underdog's sport-list confirmation in
`/docs/research/sport_inventory.md`, then disable the workflow. Session
2.9's real soak-test window remains blocked on the 2026-09-07 NFL season
start, unchanged from before this session.
## Session 3.1 — Multi-Venue Data Ingestion

**Date completed:** 2026-09-04
**Status:** ⚠️ Complete with caveats — Climate and Weather + Commodities half
fully built and validated; Politics/Elections deliberately deferred (see Open
Decision #20); a real, live matched pair between venues has not yet been
observed (see Open Decision #17).

**What was actually done:**

Built the four files the roadmap card called for, then found and fixed a real
chain of bugs while trying to validate them against live data — each one
only surfaced because the fix before it worked well enough to expose the next
layer underneath.

1. **`schema_exchange.py`** (new) — a second, parallel normalized schema for
   exchange-style YES/NO contract pricing (four separate prices: yes_bid,
   yes_ask, no_bid, no_ask), kept deliberately separate from Session 2.2's
   `schema.py` rather than forcing Kalshi/Polymarket's order-book pricing
   into a schema built for fixed-line pick'em odds.

2. **Kalshi and Polymarket API access confirmed and documented** (closes the
   first validation checkbox): both platforms' market-data read endpoints
   require no API key and no account. Confirmed live: Kalshi's base URL
   (`api.elections.kalshi.com`, despite the "elections" subdomain, covers all
   categories), Polymarket's three-API split (Gamma for markets/events, Data
   API for positions, CLOB for order-book depth — this project only needs
   Gamma). Rate limits not formally published by either vendor; both were
   hit and handled empirically during this session (see below).

3. **`ingest_kalshi.py` rebuilt twice**, not once. The first version pulled
   Kalshi's entire open-market catalog with no filter and paged as deep as
   practical. This failed in several real, sequential ways (see
   Corrections/reversals). The final version instead: (a) pulls Kalshi's
   full series list once via `GET /series` (13,816 series, confirmed public,
   no pagination needed), (b) filters client-side to series whose category
   is `"Climate and Weather"` (367) or `"Commodities"` (81) — 448 series
   total, matching Session 0.1's original Track 3 edge thesis exactly, (c)
   pulls each matching series's open markets individually via
   `GET /markets?series_ticker=<ticker>&status=open`. A real run: 448 target
   series, 1,629 genuine single-question markets kept, 0 filtered as combo
   listings (confirming combo-style contracts are a Sports-category
   phenomenon, not something Climate/Commodities needs defending against —
   though the structural filter is left in place regardless, at negligible
   cost, rather than assumed unnecessary).

4. **`ingest_polymarket.py` fixed three times** against real, live bugs (see
   Corrections/reversals): a pagination-termination bug that silently capped
   real data at ~100 events forever, a page-level failure that discarded an
   entire run's already-collected data, and a real, still-unexplained 422
   error from Polymarket's Gamma API at a consistent offset (2,100) every
   run. The final version keeps whatever it collected before that wall
   rather than losing it — real runs consistently yield ~20,700 normalized
   rows across ~2,100 events (multiple markets per event, e.g. multi-
   candidate races, expanding the row count).

5. **`venue_matcher.py` built, then fixed twice more** after real testing
   surfaced two different problems: a real performance bug (naive n×m
   comparison became ~126 million comparisons at Kalshi's true scale,
   looking hung rather than just slow — fixed with time-bucketing, verified
   at 2.55 seconds for the same real-scale data) and a real correctness bug
   found on the FIRST non-zero real result this session produced — two
   "matches" that turned out to be false positives on inspection (an 8.0+
   magnitude earthquake market matched against 9.0+ and 6.5+ magnitude
   markets, purely on shared generic wording and a shared close time). Fixed
   by requiring that, when both titles contain numbers, at least one number
   actually matches — with a further fix on top of that fix, since the first
   attempt let both titles' shared *year* ("before 2027") count as a
   spurious numeric match. Verified against three real cases: the false-
   positive earthquake pairs (now correctly rejected), the genuine NYC
   temperature match from earlier in the session (still correctly accepted,
   since both sides genuinely share the number 86), and a same-topic pair
   with no numbers at all (still matches on words/time alone, confirming the
   new check doesn't block genuine matches that never had a number to
   compare).

6. **Real diagnostic scripts built along the way, kept in the repo for reuse
   rather than thrown away**: `composition_check.py` (keyword-based category
   breakdown of each venue's real data), `sample_titles.py` (prints real,
   random titles from an "unclassified" bucket — this is what surfaced the
   combo-listing discovery), `discover_kalshi_series.py` (confirmed
   `GET /series` works without auth and produced the real 13,816-series,
   18-category breakdown that made the targeted-pull redesign possible).

7. **A real, live matched pair was NOT found** by the end of this session.
   The final, fully-fixed pipeline (1,629 real Kalshi Climate/Weather +
   Commodities markets vs. ~20,700 real Polymarket markets) returned 0
   candidates on its last real run. The matcher's correctness has been
   validated thoroughly against real title text assembled into test cases
   (see item 5), but not against a live pair that arrived together from a
   real simultaneous pull. **Decision, made explicitly with the user:** this
   is deferred rather than chased further this session — validated as
   thoroughly as current conditions allow, with the expectation that a live
   match becomes checkable once real conditions produce genuine overlap
   (e.g. an active storm or extreme-heat event both venues list). See Open
   Decision #17.

**Files created/modified:**
- `/scripts/ingestion/schema_exchange.py` (new)
- `/scripts/ingestion/ingest_kalshi.py` (new, rebuilt twice — see above)
- `/scripts/ingestion/ingest_polymarket.py` (new, fixed three times — see
  above)
- `/scripts/ingestion/venue_matcher.py` (new, fixed twice after initial
  build — see above)
- `/scripts/ingestion/composition_check.py` (new, diagnostic — kept)
- `/scripts/ingestion/sample_titles.py` (new, diagnostic — kept)
- `/scripts/ingestion/discover_kalshi_series.py` (new, diagnostic — kept)
- `/.gitignore` (new — repo had none before this session; added specifically
  to exclude `data/exchange/raw/` after a real 338.50 MB file exceeded
  GitHub's 100 MB push limit; raw snapshots are still written locally every
  run for debugging, just no longer committed)

**Validation results (against the roadmap card's original checklist):**
- [x] **Kalshi and Polymarket API access confirmed and documented** — pass,
  see item 2 above.
- [ ] **Venue-matching logic correctly identifies the same real-world
  event/outcome across at least 2 venues in a real test** — **partial
  pass.** The logic has been validated correctness-wise against real title
  text (genuine matches accepted, real false positives rejected, edge cases
  handled), but a live, real, simultaneously-pulled matched pair has not yet
  occurred. Deferred per item 7 above and Open Decision #17 — not treated as
  a session blocker, but explicitly not a full pass either.
- [x] **Normalized schema extended to cover exchange-style pricing
  (YES/NO contracts)** — pass, `schema_exchange.py`.

**Decisions made:**
1. **Target Kalshi's Climate and Weather + Commodities series specifically,
   not its full catalog.** Confirmed via real evidence (a 200,000-record
   pull that was 99.5% combo/multi-leg listings and still found zero
   weather markets) that a blind full-catalog pull is unworkable at Kalshi's
   real scale. Confirmed via `GET /series` that these two categories map
   directly onto Session 0.1's original Track 3 edge thesis, so this is a
   real scope match, not a convenient narrowing.
2. **Defer Politics/Elections ingestion to a future session.** Kalshi has
   3,949 series across Politics + Elections combined, but Session 0.1's real
   decision was narrow, down-ballot races specifically — a filter for that
   distinction doesn't exist yet, and pulling all of Politics/Elections
   as-is would reintroduce the same kind of scope drift this project has
   caught and corrected before (see SESSION_LOG.md history on NFL-only
   narrowing). See Open Decision #20.
3. **Defer chasing a live matched pair further this session** (item 7,
   above) rather than continuing to search — agreed directly with the user.

**Corrections/reversals during the session:**
1. **Kalshi page-size/cap tuning, three rounds.** Started at limit=200/
   cap=25 pages (~5,000 markets, hit cap). Raised to Kalshi's documented
   real max (limit=1000) and cap=60 (60,000 markets, still hit cap).
   Discovered via `composition_check.py`/`sample_titles.py` that the vast
   majority of that pull was multi-leg combo listings, not single-question
   markets. Attempted a `market_type == "binary"` filter — **tested against
   a real run and had ZERO effect** (every combo listing also carries
   `market_type: "binary"`) — reversed and replaced with a structural title
   check instead (two or more comma-separated "yes "/"no "-prefixed
   segments). Raised the cap to 200 pages to compensate — still found only
   30 real single-question markets, suspiciously few. Root-caused to combo
   listings likely being created continuously and crowding out single-
   question markets further back in Kalshi's result order. **Final fix
   (real reversal, not more page-cap tuning): switched to the targeted,
   category-based series pull described above**, which made the page-cap
   problem moot entirely.
2. **Polymarket pagination-termination bug.** Original logic treated "this
   page came back shorter than the limit I requested" as "no more data" —
   confirmed live that Polymarket's Gamma API silently caps real page size
   below whatever is requested, so this stopped real pagination after page
   1 every run, forever. Fixed to only stop on a genuinely empty page.
3. **Polymarket page-level failure discarding an entire run's data.** A
   real run hit an HTTP 422 error on page 22 (after 21 real, successful
   pages) and the original code let that exception propagate all the way up,
   losing all 2,100 already-collected events and reporting 0 rows for the
   whole run. Fixed to keep already-collected pages when a later page fails,
   only treating a first-page failure as fully fatal.
4. **A file-size problem, found from a real screenshot, not a log message.**
   A 338.50 MB raw Kalshi snapshot exceeded GitHub's 100 MB push limit. No
   `.gitignore` existed in the repo before this session — added one,
   excluding `data/exchange/raw/` specifically, while keeping local raw
   snapshots for debugging.
5. **`venue_matcher.py` performance.** Naive n×m comparison became ~126
   million real comparisons once Kalshi's real scale was known, looking
   hung rather than slow. Fixed with time-bucketing (verified 2.55 seconds
   at real 60,000×2,100 scale) without changing which pairs can match.
6. **`venue_matcher.py` correctness — false positives.** The first two real,
   non-zero matches this session produced were both false positives on
   inspection (different earthquake magnitude thresholds, matched on shared
   generic wording and close time alone). Added a numeric-compatibility
   check — which itself had a bug on first attempt (a shared *year* number
   counted as a spurious match) — fixed by excluding year-like numbers from
   the comparison.

**Open items / deferred validations:**
- **Open Decision #17 (new):** no live, real matched pair has been observed
  between Kalshi (Climate/Weather + Commodities) and Polymarket as of
  2026-09-04. Matcher correctness is validated against real title text in
  constructed test cases, not a live simultaneous find. Action needed: watch
  for genuine overlap in future runs (e.g. active storm/extreme-heat events
  both venues list) and confirm a real match when one appears — not treated
  as a session blocker, but a real, standing gap worth closing when
  conditions allow.
- **Open Decision #18 (new):** Kalshi's 448-series targeted pull hit
  repeated `429 Too Many Requests` responses during a real run; existing
  retry logic recovered every time and no data was lost, but this was not
  load-tested deliberately. Before Session 3.4 (Automation), add a
  deliberate pause between per-series requests rather than relying on
  reactive retries alone.
- **Open Decision #19 (new):** Polymarket's Gamma API `/events` endpoint
  fails with a consistent HTTP 422 error at offset=2100 on every real run
  this session. The current fix keeps data collected before the failure
  (see Corrections/reversals #3), but the root cause — a real API limit vs.
  the query running past the true count of currently active events — is not
  confirmed.
- **Open Decision #20 (new):** Kalshi's Politics/Elections categories
  (3,949 series combined) are deliberately not ingested yet. Needs a real,
  defined filter for "narrow down-ballot races" (matching Session 0.1's
  actual scope) before that half of this session's original card can be
  built — not simply "pull all of Politics/Elections."

**Next session:** Session 3.2 (Arbitrage Detection Logic) can proceed on
the Climate/Weather + Commodities ingestion built this session, with Open
Decision #17 (no live match yet) carried forward as a known, named gap
rather than a blocker — Session 3.2's own validation checklist should
account for this when it's reached.

---

## Session 3.1b — Kalshi Politics/Elections Ingestion (Narrow Down-Ballot)

**Date completed:** 2026-09-04
**Status:** ✅ Complete, with one specific matching-logic gap carried
forward to Session 3.2 (not a blocker for closing this session).

**What was actually done:**

1. **Checked Kalshi's "Politics" and "Elections" categories directly, live,
   before designing any filter.** "Politics" (2,296 series) was confirmed
   to contain ZERO individual-district race series — it is national
   political news and officeholder-status questions (e.g. "Jared Polis
   out as Governor of Colorado?"), not races, and is correctly excluded
   entirely. "Elections" (1,704 series) is where real race series live.

2. **Designed and validated a real, checkable "narrow down-ballot" filter**
   against live data, resolving Open Decision #20. Three distinct tiers
   were found and checked individually:
   - **U.S. House district races (89 series, confirmed live):** Kalshi
     tags these "House" (excluding the separate "House Combos" tag) and
     uses a structural ticker pattern (state code + district number, e.g.
     `HOUSECA9`, `KXHOUSEMO5`, `HOUSEAKAL` for an at-large seat). Verified
     against all 116 "House"-tagged series: the structural check correctly
     kept all 89 real district races and correctly excluded all 27
     non-matches (leadership races, chamber-control aggregates, combo
     contracts) on inspection.
   - **State-legislature district races (4 series found live):** California
     State Senate District 26, Pennsylvania State House District 12,
     Maryland State Senate District 2, Missouri State Senate District 8 —
     identified by a structural title pattern ("State House/Senate/Assembly
     District <number>").
   - **City/county district races (14 series found live — 13 NYC City
     Council, 1 Los Angeles City Council):** checked and found NOT to pass
     the same bar as the other two tiers — see Decision 1 below.
   - Statewide races (Governor: 71 series; U.S. Senate: 121 series) were
     confirmed to be exactly the "marquee" races Open Decision #20 said to
     exclude, and are not pulled.

3. **Extended `ingest_kalshi.py`** with a new `classify_down_ballot()`
   function implementing the filter above, plus a `DOWN_BALLOT_CATEGORY`
   constant and structural regex patterns for each tier. Down-ballot rows
   are tagged with a specific category string at write time (e.g.
   "Elections - US House District") instead of Kalshi's generic
   "Elections" category, so a row's tier is visible directly in the output
   CSV. Unit-tested the classification function against the real examples
   gathered live (House, state-legislature, city/county, Governor, Senate)
   before delivery — every case classified correctly.

4. **Ran the real filtering logic live** against Kalshi's full, current
   series list (13,817 series pulled) to confirm the numbers designed
   against didn't drift: 448 Climate/Commodities series (unchanged from
   Session 3.1), 93 narrow down-ballot series (89 House + 4 state
   legislature), 541 target series total. This was run directly against
   the live API rather than through the full GitHub Actions pipeline,
   since no such pipeline exists yet for this script (see Decision 3
   below).

5. **Checked Polymarket for real overlap**, addressing the third
   validation checkbox. Searched Polymarket's public search API for each
   of Kalshi's real down-ballot races:
   - **U.S. House tier: real, live matches confirmed.** All 5 House races
     checked (MO-05, WA-08, UT-02, NY-17, CA-09) have a corresponding
     Polymarket market, using a consistent "XX-## House Election Winner"
     naming pattern. This is the first genuine live, simultaneously-
     available cross-venue matched pair this project has found (Session
     3.1 found none for Climate/Weather — see Open Decision #17).
   - **State-legislature tier: no overlap found.** None of the 4 real
     Kalshi state-legislature races (Missouri, Maryland, California,
     Pennsylvania) have a matching Polymarket market. Polymarket does list
     some state-legislature races (a Wyoming one was found), just not
     these four.

6. **Found a real, specific reason `venue_matcher.py` would still miss the
   MO-05 match even though it exists**, by running the actual real data
   for both venues through the matcher's real logic (not just checking
   that a matching market exists on each venue). Title similarity and the
   numeric-compatibility check both pass easily for the MO-05 pair. The
   close-time-proximity check (6-hour tolerance) does NOT pass: Kalshi's
   `close_time` for this contract is `2027-11-03` (the swearing-in/
   contract-expiration date), while Polymarket's `endDate` is
   `2026-11-04` (the actual election date) — a gap of roughly a year, far
   outside tolerance. Checked two other Kalshi down-ballot tickers
   (Pennsylvania House District 12, Missouri Senate District 8) and found
   the identical `2027-11-03` pattern, confirming this is systematic to
   how Kalshi structures these political contracts, not a one-off data
   issue. See Open Decision #21.

**Files created/modified:**
- `/scripts/ingestion/ingest_kalshi.py` (extended — added
  `DOWN_BALLOT_CATEGORY`, `classify_down_ballot()`, structural regex
  patterns for each tier, updated `fetch_target_series_tickers()` and
  `run()` to pull and tag the narrow down-ballot subset alongside the
  existing Climate/Commodities pull)

**Validation results (against the roadmap card's original checklist):**
- [x] **A real, checkable definition of "narrow down-ballot" is documented
  and applied as an actual filter** — pass. See items 2–3 above;
  `classify_down_ballot()` is the filter, tested against real examples.
- [x] **Real narrow down-ballot series pulled and confirmed against
  Session 0.1's original scope** — pass. 93 real series (89 House + 4
  state legislature) confirmed live against the filter logic, matching
  Session 0.1's "individual House/State seats" scope; city/county and
  statewide races correctly excluded (see Decision 1).
- [ ] **Venue-matching re-run against the expanded Kalshi data to check for
  real overlap with Polymarket's own down-ballot election markets** —
  **partial pass.** Real overlap WAS found for the U.S. House tier (5/5
  races checked have a live Polymarket match) — a first for this project.
  However, `venue_matcher.py`'s existing close-time-proximity logic would
  not actually catch this match as currently configured, for the specific,
  confirmed reason in item 6 above. Deferred to Session 3.2 rather than
  fixed here — see Decision 3 and Open Decision #21.

**Decisions made:**
1. **City/county district races (NYC/LA City Council) are excluded from
   the narrow down-ballot filter, for now — decided directly with the
   user against an explicit test.** The user's standing rule: include a
   tier only if a real +EV edge can be determined; if that can't easily be
   determined, leave it out. The test applied was whether a real,
   independent, per-seat probability estimate can be built to compare
   against Kalshi's price. State legislature passed this test (see
   Decision 2). City/county did not: live research found only ad hoc
   journalism naming a handful of competitive seats per cycle (e.g. City &
   State NY's "races to watch"), not a systematic per-seat forecast model
   covering every district. Kalshi's own live order books confirmed this
   isn't just a research gap: 6 of 7 NYC City Council series sampled had
   NO open market running at all; the one that did (LA City Council
   District 13) is itself one of the handful of seats that gets real news
   coverage, not representative of the rest. This is logged as a "can't
   yet determine a real edge" result, not a "no edge exists" result — the
   detection pattern is left in `ingest_kalshi.py`, dead but documented,
   so this can be switched back on if a comprehensive per-seat local-
   election forecast source is found later.
2. **State-legislature district races are included, on the same test.**
   Real, comprehensive, per-seat public forecast data was confirmed live:
   ElectIndex publishes a probabilistic forecast for all 88 state-
   legislative chambers on the 2026 ballot; multistate.us separately
   publishes a baseline partisan-lean number for all 7,388 state-
   legislative seats nationwide. This gives a genuine, independent basis
   for an edge estimate, the same test the House tier already passes via
   well-known federal election forecasting sources.
3. **The real end-to-end pipeline run (fetching markets for all 541 target
   series, writing `kalshi_latest.csv`, committing it back) was not
   performed this session.** Checked directly: no GitHub Actions workflow
   exists yet for `ingest_kalshi.py`/`ingest_polymarket.py` (only
   `pickem_pipeline.yml` and `sport_inventory_scan.yml` exist in
   `.github/workflows/`) — wiring this pipeline into an automated,
   schedulable workflow is Session 3.4 (Automation Adaptation), not yet
   started. In its place, the real filtering logic was run directly
   against Kalshi's live API (item 4 above) to confirm correctness without
   waiting on automation that isn't built yet.
4. **The `venue_matcher.py` close-time bug found in item 6 is NOT fixed in
   this session**, even though a fix is now well-understood. Changing
   venue-matching logic is Session 3.2's (Arbitrage Detection Logic)
   domain, not this ingestion session's — decided directly with the user
   rather than editing another session's file unilaterally.

**Corrections/reversals during the session:** None — the filter design
held up against live validation without needing revision, and the one
real surprise (Kalshi's close_time representing the swearing-in date, not
the election date, for down-ballot political contracts) was a new finding
rather than a correction of something built this session.

**Open items / deferred validations:**
- **Open Decision #20 is now RESOLVED** — see Decisions 1–2 above for the
  real, evidence-based narrow down-ballot definition.
- **New Open Decision #21:** `venue_matcher.py`'s close-time-proximity
  check (6-hour tolerance, tuned against Session 3.1's weather-market
  data) does not account for Kalshi's down-ballot political contracts
  setting `close_time` to the post-election swearing-in/expiration date
  rather than the election date itself — confirmed across 3 real tickers
  (MO-05, PA House District 12, MO Senate District 8), all showing the
  same `2027-11-03` pattern regardless of race type. Polymarket's
  `endDate` for the same real races is the actual election date
  (`2026-11-04`), so a real, live matched pair (MO-05, confirmed present
  on both venues) would currently be missed by the matcher as configured.
  **Action needed, before Session 3.2's matching logic is considered
  final for down-ballot politics:** either derive a second, election-date-
  specific timestamp for Kalshi's political contracts to match against
  (rather than relying on `close_time` alone), or add a per-category
  matching rule that relaxes/replaces the close-time check for the
  Elections category specifically. Not a blocker for closing this
  session, per direct agreement with the user.
- City/county down-ballot races remain a named, revisitable exclusion (see
  Decision 1) — no further action needed unless a comprehensive per-seat
  local-election forecast source is found.

**Next session:** No specific ingestion work is required next for Track 4
— the narrow down-ballot filter is built and validated. Session 3.2
(Arbitrage Detection Logic) should account for Open Decision #21 when it
reaches down-ballot politics specifically, in addition to the existing
Open Decision #17 (Climate/Weather, no live match yet). Session 3.4
(Automation Adaptation) is still where the actual GitHub Actions workflow
for this pipeline gets built — nothing changed about that timing this
session.

---

## Session 3.2 — Arbitrage Detection Logic

**Date completed:** 2026-09-05
**Status:** ✅ Complete

**What was actually done:**
Built the core price-comparison logic for cross-venue and single-venue
arbitrage detection, fee-adjusted against each venue's real, current fee
schedule rather than the raw price gap. Two real bugs were found and
fixed against live Kalshi/Polymarket data pulled directly via Claude in
Chrome mid-session, not deferred to a later session:

1. **Built `detector.py`**, checking two distinct arbitrage shapes: (a)
   single-venue YES+NO mispricing (a venue's own YES and NO contract on
   the same market summing to under $1.00), and (b) cross-venue
   matched-pair mispricing (buying YES on one venue and NO on the other,
   per a `venue_matcher.py` candidate pair, for under $1.00 combined).
   Both shapes price every leg at each venue's real TAKER fee rate —
   Kalshi: `round_up(0.07 × C × P × (1-P))` per the venue's own published
   fee schedule; Polymarket: `FeeRate_by_category × C × P × (1-P)`, with
   real category-specific rates (0.04 Politics, 0.05 Weather, etc.) pulled
   directly from Polymarket's current docs. This is a real, current pull
   — Session 0.1's original research predates Polymarket's 2026 fee
   rollout (Polymarket was previously near fee-free) and would have been
   silently stale if reused here.
2. **Manually cross-checked both fee formulas against 2+ real examples**
   and found exact agreement with each venue's own published fee table
   (Polymarket Politics at 30¢: $0.84/100 shares in both places; Kalshi at
   30¢: $1.47/100 contracts in both places) — the formulas are not
   approximations, they reproduce the venues' own numbers exactly.
3. **Built `liquidity_check.py`** to attach a real fillable size to every
   flag, and **`/docs/venue_legal_footprint.md`** to document what is and
   isn't known about state-level legal availability across the two
   venues, per Session 0.1's five per-venue evaluation criteria.
4. **Fixed Open Decision #21 in `venue_matcher.py`** — added a
   category-specific matching path for down-ballot Elections rows,
   using a 400-day close-time tolerance (vs. the default 6 hours) and a
   raised title-similarity bar (0.5 vs. 0.35) to compensate. Validated
   first against a constructed test case, then against real live data
   (see Validation results below) — this is the first Open Decision in
   this project closed out with live evidence rather than a synthetic
   case alone.
5. **Pulled real, live Kalshi and Polymarket data directly** (via Claude
   in Chrome, hitting both venues' real public API endpoints — Kalshi's
   `GET /series`/`GET /markets`, Polymarket's Gamma API) specifically to
   validate the detector and matcher against real numbers rather than
   only constructed test cases. This surfaced a real, previously-unknown
   defect (see item 6) that no amount of synthetic testing would have
   caught, since the defect was in what real data actually looks like,
   not in the detection logic itself.
6. **Found and fixed a real Kalshi data defect discovered only by pulling
   live data:** Kalshi's `liquidity_dollars` field reads `"0.0000"` on
   every single real market checked this session (multiple KXHIGHPHIL
   weather strikes, both real legs of the real KXHOUSEMO5 down-ballot
   race), including markets with substantial real size resting on the
   book (one real leg had 116.02 contracts at its best ask, tens of
   thousands of contracts in real volume). This is systematic, not a
   stale-market fluke. Fixed by extending `schema_exchange.py` with two
   new fields (`yes_ask_size`, `yes_bid_size`), updating
   `ingest_kalshi.py`'s normalizer to populate them from Kalshi's real,
   populated `yes_ask_size_fp`/`yes_bid_size_fp` fields, and rewriting
   `liquidity_check.py` to use those fields for Kalshi legs specifically
   while keeping Polymarket's own `liquidity` field (confirmed real and
   populated, e.g. $9,746.02 on the real MO-05 Republican market) for
   Polymarket legs. This required reopening two Session 3.1 files
   (`schema_exchange.py`, `ingest_kalshi.py`) after Session 3.1 had
   already closed — done with the user's explicit go-ahead, on the
   stated principle that these are working documents that should be
   revisited when new evidence requires it, not treated as frozen once a
   session closes.
7. **Found and fixed a real floating-point rounding bug** in the
   false-positive threshold check: an intentionally constructed
   exact-breakeven test case (gross cost $0.95, fees $0.04, leaving
   exactly $0.01 of real profit) was being silently dropped, because
   `1.0 - 0.95 - 0.04` evaluates to `0.009999999999999933` in binary
   floating point, a hair under the `MIN_NET_PROFIT_FRACTION = 0.01`
   threshold despite there being no real cent of shortfall. Fixed by
   rounding the net-profit calculation to 6 decimal places before the
   threshold comparison, in both the single-venue and cross-venue
   detection functions.

**Files created/modified:**
- `/scripts/arbitrage/detector.py` (new)
- `/scripts/arbitrage/liquidity_check.py` (new)
- `/docs/venue_legal_footprint.md` (new)
- `/scripts/ingestion/venue_matcher.py` (modified — Open Decision #21 fix)
- `/scripts/ingestion/schema_exchange.py` (modified — added
  `yes_ask_size`/`yes_bid_size` fields, both defaulted to `None` so
  `ingest_polymarket.py` needed no changes)
- `/scripts/ingestion/ingest_kalshi.py` (modified — populates the two new
  fields from real Kalshi data)

**Validation results:**
- [x] **Detection logic correctly flags a known historical or simulated
  arbitrage case** — pass. Confirmed on constructed test cases for both
  shapes, then re-run against real current Kalshi/Polymarket MO-05 prices
  and correctly found zero arbitrage (real markets are efficient right
  now — the correct real-world answer, not a bug).
- [x] **Fee-adjusted profit calculation confirmed accurate (manually
  cross-checked on at least 2 real examples)** — pass. Hand-computed
  values matched both venues' own published fee tables exactly (see item
  2 above).
- [x] **False-positive check: confirms it does NOT flag price differences
  that don't actually clear fees** — pass. Confirmed on a constructed
  razor-thin case and on real MO-05 prices (real gross costs of
  $1.00–$1.05 across both legs and both directions, correctly producing
  zero flags). The float-precision bug (item 7) was caught and fixed
  during this same validation pass, not after.
- [x] **Liquidity check confirmed: a flagged opportunity includes the
  real available size at that price, not just the headline price** —
  pass, after a real fix. Initial version relied on Kalshi's dead
  `liquidity_dollars` field and would have reported every Kalshi-involving
  flag as illiquid; fixed per item 6 above and re-validated against real
  MO-05 data, correctly reporting a real, non-zero fillable size ($15.28,
  bound by the real, thinner Kalshi leg) instead of a false $0.00.
- [x] **Legal footprint check confirmed: a flagged opportunity is
  suppressed or clearly labeled if either venue isn't legally available
  to the user** — pass, with an honest documented gap. The mechanism
  works (Kalshi's confirmed Sports-contract state restrictions are
  modeled correctly); no comparably detailed Polymarket-specific
  restriction list was found this session, so the check currently reports
  `both_available_nationally = True` more often than a fully-verified
  check would — logged as Open Decision #22, not silently cleared.

**Decisions made:**
1. **Every leg is priced at each venue's TAKER fee rate, always** — a
   deliberate worst-case assumption, not an average or a best case. Both
   venues charge less (Kalshi: a reduced maker rate, sometimes zero;
   Polymarket: literally zero) to a resting order, but this project's
   normalized schema only captures top-of-book price at pull time, with
   no way to know whether a specific flagged opportunity could actually
   be filled patiently as a maker order. A flagged opportunity's real
   profit, if filled as a maker, can only be higher than what's reported
   here — never lower.
2. **`MIN_NET_PROFIT_FRACTION = 0.01`** (at least 1 cent of real profit
   per $1 risked) is a named floor below which a technically-positive gap
   is not flagged at all, given real execution risk (both legs must
   actually fill) and the fact that every input is itself an estimate.
   Not yet validated against a real filled trade — a starting value,
   flagged for recalibration the same way `sizing_engine.py`'s
   `KELLY_FRACTION` was.
3. **Kalshi and Polymarket are treated asymmetrically in
   `liquidity_check.py`, on purpose** — Kalshi legs use real per-contract
   order-book size fields; Polymarket legs use the venue's own `liquidity`
   dollar figure divided by price. This is not a stylistic inconsistency;
   it reflects a real, confirmed difference in what each venue's real API
   actually exposes (see item 6 above).
4. **Reopening Session 3.1 files was approved directly by the user** when
   the live liquidity-field defect was found, on the explicit standing
   principle that ROADMAP/SESSION_LOG sessions are working documents, not
   frozen artifacts — a real session boundary should not block fixing a
   real, newly-discovered problem in an earlier file.
5. **Open Decision #22 (Polymarket legal-footprint gap) is logged, not
   silently cleared or worked around with an assumption.** `detector.py`
   currently reports every flagged pair as available in every state,
   which is accurate for what's been checked (Kalshi Sports doesn't
   currently apply to this project's tracks) but not a verified guarantee
   for Polymarket specifically.

**Corrections/reversals during the session:**
- The original `liquidity_check.py` (written before live data was pulled)
  used Kalshi's `liquidity_dollars` field directly, following the venue's
  own schema field name at face value. This was corrected once live data
  showed the field itself doesn't carry real information for Kalshi —
  see item 6 above. This is a real reversal of a design choice made
  earlier the same session, not a pre-existing bug carried in from
  Session 3.1.
- The floating-point rounding fix (item 7) corrected a bug introduced
  and caught within this same session's own validation pass.

**Open items / deferred validations:**
- **New Open Decision #22:** Polymarket-specific state-by-state legal
  availability has not been researched to the same depth as Kalshi's
  confirmed Sports-contract restriction list. Not a blocker for closing
  this session; most relevant once Track 6 (flagship sports/exchange
  markets) is built. See ROADMAP.md's Open Decisions list and
  `/docs/venue_legal_footprint.md` for the full evidence trail.
- Order-book DEPTH (beyond top-of-book) remains unpulled for both
  venues. `liquidity_check.py`'s Polymarket-leg estimate
  (`liquidity ÷ price`) is a named approximation, not a literal
  per-price-level read, since Polymarket's Gamma API doesn't expose one
  the way Kalshi's real `yes_ask_size_fp`/`yes_bid_size_fp` fields do.
- Wiring `detector.py`/`liquidity_check.py` into an automated,
  schedulable GitHub Actions workflow is Session 3.4's job (Automation
  Adaptation) — not built here, consistent with how Session 3.1's own
  ingestion scripts were left unwired until their automation session.

**Next session:** Session 3.3 (Sizing Logic Adaptation) is next per
ROADMAP.md — its prerequisite (Session 3.2 complete) is now met. Session
3.3 should be aware of Open Decision #22 (Polymarket legal-footprint gap)
if sizing logic ever needs to reason about legal availability directly,
though that is not expected to be its main concern.


## Session 3.3 — Sizing Logic Adaptation

**Date completed:** 2026-09-05
**Status:** ✅ Complete

**What was actually done:**
Extended `sizing_engine.py` (Session 2.6's pick'em sizing script) to also
size arbitrage positions from Session 3.2's `detector.py` output, without
rebuilding or altering the existing pick'em code. Full flow:

1. Established up front that arbitrage sizing is a genuinely different
   problem from pick'em's Kelly-based sizing, not a variant of it — an
   arbitrage position is a locked, guaranteed-profit trade once both legs
   fill, so there is no win/loss probability to size against. Its real
   risks are (a) capital needing to sit at two venues simultaneously, not
   drawn from one shared pool, and (b) execution ("legging") risk between
   detecting a price gap and actually placing both real orders.
2. Added two new sizing inputs, `--kalshi-bankroll` and
   `--polymarket-bankroll`, kept as separate real dollar figures rather
   than one combined bankroll, matching the real mechanics: a position
   requires the same dollar amount sitting in both accounts at once.
3. Added a small new open-positions ledger,
   `data/arbitrage/open_positions.csv`, with `record_open_arbitrage_position()`
   and `settle_arbitrage_position()` functions (same pattern as Session
   2.5's `outcome_tracker.py`), so sizing a new position correctly
   subtracts capital already committed to earlier, still-open positions
   at each venue.
4. Added `EXECUTION_RISK_BUFFER = 0.85`, a named haircut on sized
   contract count, same "named judgment call, not a sourced number"
   posture as `KELLY_FRACTION`.
5. Added `MAX_ARBITRAGE_POSITION_PCT = 0.05`, capping a single position
   at 5% of the user's total combined bankroll, mirroring pick'em's
   `MAX_SINGLE_POSITION_PCT` pattern.
6. Validated against constructed test cases first (thin per-venue
   balances correctly binding position size, the ledger correctly
   reducing available capital on a second sizing call, settlement
   correctly freeing that capital back up, and a same-venue YES+NO flag
   being explicitly rejected rather than mis-sized) — same
   constructed-then-real validation order as Session 3.2.
7. **Ran the corrected script against real, live Kalshi order-book data
   this session** (`KXHOUSEMO5`, `KXHIGHPHIL`, `KXHIGHNY` — this
   project's actual down-ballot-politics and weather tracks) and found a
   real, second bug in the process (see below), which was fixed and
   re-validated before this session closed, not deferred.
8. **Real bug found and fixed against live data:** `detector.py`'s
   `fillable_size_dollars` field is actually a CONTRACT COUNT, not real
   dollars — `liquidity_check.py`'s own docstring says this explicitly
   ("a contract count IS a dollar notional amount," referring to each
   contract's $1 PAYOUT, not its purchase cost). The first version of
   `size_arbitrage_position()` treated that count as if it were already
   real dollars of capital. Confirmed the real-world impact directly:
   Kalshi's real MO-05 Republican leg has `yes_ask=$0.20` and
   `yes_ask_size=15.28` real contracts — the real cost to buy all 15.28
   is $3.06, not $15.28. Fixed by reworking the sizing math to operate in
   contracts throughout, converting to real per-leg dollar cost
   (`contracts × that leg's own ask price`) only at the point a dollar
   figure is actually needed. Re-validated against both the full
   constructed test suite and the real MO-05 numbers after the fix:
   correctly reports ~$2.60/$9.74 real per-leg cost (asymmetric, matching
   each leg's real price) instead of the old, wrong $12.99/$12.99
   (identical, treating contract count as dollars on both legs).
9. **Checked for a genuine live arbitrage opportunity to size against, as
   a real positive case — none currently exists.** Checked 14 real
   markets live across MO-05, `KXHIGHPHIL`, and `KXHIGHNY`: every single
   one showed real `yes_ask + no_ask` between $1.01 and $1.04 (a few
   cents ABOVE the $1.00 arbitrage threshold, never below it). This is
   systematic across all 14 real markets checked, not an isolated stale
   quote, and matches Session 3.2's own finding that real markets are
   currently efficient. `arbitrage size` was validated against real
   numbers plugged into a labeled test flag (see below) rather than a
   genuine live positive case, since none existed to test against.
10. **Objective sanity-check performed on both named constants, using
    real numbers rather than judgment alone:**
    - `EXECUTION_RISK_BUFFER = 0.85`: pulled the same real MO-05 and
      Philadelphia weather markets twice, roughly 13–30 real minutes
      apart. Real quoted PRICE was completely unchanged across every
      market checked both times. Real order-book SIZE at the best price
      was not stable — one real Philadelphia strike's bid size dropped
      67% (1.56 → 0.52 contracts) in 13 real minutes. This confirms the
      buffer is aimed at the right kind of risk (size risk, which moved;
      not price risk, which didn't, in this real sample) but the single
      real data point showing a 67% swing is larger than the 15% haircut
      currently applied — a real, if thin-sample, signal that 0.85 may
      be too lenient. Not changed this session (sample size of one
      real before/after pair does not support a confident recalibration
      — flagged as a candidate for Session 8.3 once a proper repeated-
      pull sample exists).
    - `MAX_ARBITRAGE_POSITION_PCT = 0.05`: computed real per-leg dollar
      liquidity (real ask price × real order-book size) across the same
      14 real markets — ranging $0.56 to $95.14. Cross-referenced against
      the 5% cap at several bankroll sizes: at a $200 bankroll the cap
      ($10) binds before real liquidity almost every time; at $1,000 the
      two are roughly evenly mixed; at $5,000 the cap ($250) almost never
      binds, since observed real liquidity in this project's actual
      tracks rarely exceeds it. Conclusion: the constant itself is
      reasonable, but whether it ever actually matters depends heavily on
      bankroll size — logged as context for whoever tunes this later,
      not changed.

**Files created/modified:**
- `/scripts/sizing/sizing_engine.py` (extended — added arbitrage sizing
  functions, the open-positions ledger, and new `arbitrage`/`pickem` CLI
  subcommands; existing pick'em code and behavior unchanged, confirmed via
  regression test)

**Validation results:**
- [x] **Sizing correctly accounts for capital needing to sit in two
  venues simultaneously** — pass. Confirmed the thinner venue's balance
  (not a shared pool) correctly becomes the binding constraint, confirmed
  the open-positions ledger correctly reduces available capital at each
  venue independently on a subsequent sizing call, and confirmed
  settling a position correctly frees that venue's capital back up.
- [x] **Execution-risk buffer included** — pass. Confirmed the 0.85
  haircut is applied to the sized contract count and reported explicitly
  on every result, both before and after the unit-mismatch fix.
- [x] **Real bug found during validation was fixed within this session,
  not deferred** — pass. The contracts-vs-dollars mismatch was caught
  by deliberately testing against real Kalshi order-book numbers (not
  just constructed cases), fixed, and re-validated against both the full
  constructed suite and the real numbers that exposed it.
- [x] **Same-venue (single-venue YES+NO) flag explicitly rejected, not
  mis-sized** — pass. `size_arbitrage_position()` refuses a flag where
  `platform_a == platform_b` with a clear reason, since that shape has no
  real two-venue capital-lockup risk to size.
- [x] **Pick'em sizing regression check** — pass. Existing pick'em
  behavior reproduced exactly under the new `pickem` CLI subcommand.

**Decisions made:**
1. **Bankroll is two separate numbers for arbitrage sizing, never one
   combined figure** — reflects the real mechanics of needing the same
   dollar amount sitting at both venues simultaneously, not drawn from a
   shared pool.
2. **A new open-positions ledger (`data/arbitrage/open_positions.csv`)
   tracks real committed capital per venue, not real settlement
   duration** — this project has no real settlement-timing data for
   either venue yet, and inventing a number would repeat exactly the
   kind of guess this project's standing rules forbid. The ledger tracks
   what CAN be known honestly (capital is locked) without guessing at
   what can't (for how long).
3. **`EXECUTION_RISK_BUFFER = 0.85` is a haircut on position SIZE, not on
   required profit margin** — a deliberate choice once real data showed
   quoted size moves faster than quoted price in this project's actual
   markets (see item 10 above), though the specific magnitude is only
   weakly validated by a single real data point.
4. **The contracts-vs-dollars unit fix (item 8) was treated as a real bug
   to fix immediately upon discovery, not a design choice to defer** —
   consistent with Session 3.2's own standing practice of fixing real
   defects found during validation within the same session, not carrying
   them forward.

**Corrections/reversals during the session:**
- The first version of `size_arbitrage_position()` treated
  `detector.py`'s `fillable_size_dollars` field as real dollars of
  capital. This was corrected after real live Kalshi data (MO-05's
  15.28-contract, $0.20-ask real order book) showed the field is
  actually a contract count, and the bug would have materially misstated
  real per-leg capital requirements on any real, low-priced leg (the
  normal case). See item 8 above for the full before/after.
- `record_open_arbitrage_position()` initially referenced a result field
  (`expected_profit_dollars`) that didn't exist under that name in
  `size_arbitrage_position()`'s return value, caught by running
  `arbitrage record-open` end-to-end during validation rather than
  trusting the code path unexercised. Fixed to reference the correct
  field name before this session closed.

**Open items / deferred validations:**
- **Sizing has not yet been run against a genuine LIVE positive
  arbitrage flag** — real markets checked this session (MO-05,
  `KXHIGHPHIL`, `KXHIGHNY`, 14 markets total) are all currently
  efficient, consistent with Session 3.2's own finding. Validated
  instead against real market numbers plugged into a labeled test flag.
  Not a blocker for closing this session, since the sizing math itself
  has been validated both ways (constructed cases, and real numbers) —
  but a true end-to-end real-flag run is still owed once one exists.
- **`EXECUTION_RISK_BUFFER = 0.85` recalibration** — the real 67%
  size swing observed in 13 minutes on one real market suggests 0.85
  may be too lenient, but a sample of one real before/after pair is too
  thin to act on. Candidate for Session 8.3, once repeated automated
  snapshots (Session 3.4) provide a real distribution to check against.
- **`MAX_ARBITRAGE_POSITION_PCT = 0.05`** — not changed; its practical
  effect depends heavily on the bankroll size actually used (see item 10
  above). No action needed unless Greg's real trading bankroll changes
  materially.
- Wiring the sizing engine into an automated workflow remains Session
  3.4's job (Automation Adaptation) — not built here, same as
  Session 3.2's detection scripts were left unwired until their own
  automation session.

**Next session:** Session 3.4 (Automation Adaptation) is next per
ROADMAP.md — its prerequisite (Session 3.3 complete) is now met.

---

## Session 3.4 — Automation Adaptation

**Date completed:** 2026-09-06
**Status:** ✅ Complete

**What was actually done:**
Wired the arbitrage track's four existing scripts (Kalshi ingestion,
Polymarket ingestion, venue matching, detection — Sessions 3.1–3.3) into
an automated GitHub Actions workflow, the arbitrage-track equivalent of
Session 2.7's pick'em automation. Full flow:

1. Added `KALSHI_PER_SERIES_PAUSE_SECONDS = 0.2` and a deliberate pause
   after every one of `ingest_kalshi.py`'s ~540 real per-series
   requests (success or failure) — the action item flagged in Session
   3.1 ("add a deliberate pause... before Session 3.4"). Reasoning:
   Session 3.1 relied only on reactive retries, acceptable for a
   watched manual run but not for a scheduled, unattended one.
2. Built `scripts/run_arbitrage_pipeline.py`, a new orchestrator
   modeled directly on `run_pipeline.py` (Session 2.7): same
   importlib-by-path module loading, same "stop before later stages if
   an ingestion stage returns zero rows" guard, same per-run digest
   file. One real design difference from the pick'em orchestrator:
   zero candidate pairs from venue matching does NOT stop the
   pipeline — a real, valid outcome (Session 3.2/3.3 already
   established venues can genuinely not overlap on a given run),
   unlike zero rows from an ingestion stage, which means something
   broke.
3. Built `.github/workflows/arbitrage_pipeline.yml`, committing only
   the real historical record (candidate matches, flags, digest) —
   deliberately NOT the raw/normalized snapshots, which would grow the
   repo fast for no real benefit beyond single-run debugging.
4. **Real bug found and fixed via the pipeline's own first live
   automated run, not caught in isolated testing beforehand:**
   `venue_matcher.py`'s Elections wide-tolerance path (Session 3.2)
   proposed 10 flagged "arbitrage" pairs, several reporting an
   absurd 50–90 cent-per-dollar edge. Inspection of the real output
   showed every one of the 9 highest-edge flags was a false match
   across DIFFERENT states sharing the same district NUMBER — e.g.
   Kalshi's "WA-08" matched against Polymarket's "IN-08" (Washington's
   8th District vs. Indiana's 8th District). Root cause: `_title_words()`
   tokenizes "WA-08" into separate "wa" and "08" tokens (the hyphen
   splits them), so the shared "08" token satisfied both the Jaccard
   title-similarity bar and `_numbers_are_compatible()`'s "at least
   one number must match" check — neither check knew a district
   number only means the same race when paired with the same state.
   Fixed within this session (per this project's own standing
   practice, established in Session 3.3, of fixing real validation
   bugs immediately rather than deferring them): added
   `_extract_district_codes()` and `_district_codes_compatible()` to
   `venue_matcher.py`, extracting a (state, district) pair from each
   title and requiring an exact match when both titles have one,
   applied only to the Elections wide-tolerance path (not the
   bucketed path, which never had this failure mode). Re-ran the real
   pipeline after the fix: candidate pairs dropped from 497 to 477 (the
   20 false-state-pair candidates gone), and the flag list dropped from
   10 false flags to exactly 1 — Kalshi's "MI-7" vs. Polymarket's
   "MI-07," now reporting a realistic 1-cent-per-dollar edge instead of
   90 cents.
5. **Confirmed the one surviving flag is a genuine same-race match, not
   another formatting coincidence** — checked directly (web search):
   Michigan's 7th Congressional District, incumbent Republican Tom
   Barrett vs. Democrat William Lawrence, general election 2026-11-03.
   Both venues are pricing the same real contest, just formatted
   differently ("MI-7" vs. "MI-07"). Not yet run through
   `sizing_engine.py arbitrage size` — that remains a manual, human
   decision per this project's "flags and sizes, never places bets"
   rule.
6. **Polling cadence — set with real cost math, not a guess, after a
   real back-and-forth with Greg about what the cadence actually
   controls.** Corrected a real misunderstanding Greg raised: this
   detector does NOT compare against past data the way pick'em's CLV
   logging does — every run is a self-contained, point-in-time check
   of whether both sides of a locked position can be bought under
   $1.00 right now. Cadence therefore only affects the odds of a
   snapshot landing inside a real mispricing's (currently unknown)
   lifetime, not trend detection. Checked the account's real GitHub
   billing page directly rather than assuming: GitHub Free plan, 2,000
   included Actions minutes/month, shared across Greg's entire account
   (Market_Betting AND all three DFS optimizer repos — confirmed via
   the billing page's real per-repo breakdown, not assumed). Also
   confirmed directly: the account's Actions budget is configured at
   $0 with "Stop usage: Yes" — going over the allowance does NOT
   silently charge Greg's card, it silently STOPS every Actions
   workflow on the account (pick'em included) until the next month's
   reset. An initial 15-minute-cadence placeholder was rejected once
   this was checked — it would have used ~11,500 runner-minutes/month
   by itself, ~5.8x the entire account's allowance. Settled on 6
   runs/day (~every 4 hours, cron offset to avoid the exact hour) —
   real cost ≈720 runner-minutes/month, combined with pick'em's own
   real ~960 min/month (confirmed from its actual run history: hourly,
   ~1m20s/run) keeps the account under its 2,000-minute ceiling with
   room left for the DFS repos. Also widened the workflow's job
   timeout from 12 to 30 minutes, since the tight 12-minute cap existed
   specifically to prevent overlap at the old, much faster 15-minute
   cadence and is no longer needed at 6 runs/day.
7. **Real, live-tested confirmation, not just a syntax check:** both
   the pre-fix and post-fix versions of the pipeline were run for real
   via `workflow_dispatch` (not just planned) — run #1 (pre-fix, green,
   3m 53s, exposed the false-match bug via its own real digest output)
   and run #2 (post-fix, green, 4m 15s, confirmed the fix against the
   same real Kalshi/Polymarket data). No scheduled (cron-triggered) run
   had fired yet as of this session's close — same real registration
   delay Session 2.7 already documented for pick'em's own schedule.

**Files created/modified:**
- `scripts/ingestion/ingest_kalshi.py` (added
  `KALSHI_PER_SERIES_PAUSE_SECONDS` and the per-series pause)
- `scripts/ingestion/venue_matcher.py` (added `_extract_district_codes()`
  and `_district_codes_compatible()`; wired into `_find_elections_matches()`
  only)
- `scripts/run_arbitrage_pipeline.py` (new)
- `.github/workflows/arbitrage_pipeline.yml` (new)

**Validation results:**
- [x] **Workflow runs on schedule reliably** — ⚠️ partially validated.
  Two real `workflow_dispatch` runs both succeeded end-to-end
  (ingestion → matching → detection → commit), confirmed via the
  Actions tab and the real committed digest/flags files. A genuine
  CRON-triggered run had not yet fired as of this session's close —
  Greg will check back once GitHub has had time to register the new
  schedule (same real delay Session 2.7 hit for pick'em). Not treated
  as a blocker for closing this session, since Session 2.7 already
  established this delay is a one-time, expected registration lag, not
  a sign of a broken schedule — but flagged here as the one piece
  still owed a real look.
- [x] **Polling frequency justified against real evidence, not an
  arbitrary guess** — pass, with an explicit caveat. The evidence used
  is NOT "how fast a real arbitrage window closes" (that data still
  does not exist — no genuine window has ever been observed to close,
  per Session 3.2/3.3's own findings) but real GitHub Actions cost data
  checked directly against the account's actual billing page and
  budget settings. This is a deliberate, named substitution: real cost
  evidence in place of real timing evidence, because the timing
  evidence doesn't exist yet and won't until Session 3.6 collects it.
  6 runs/day is explicitly logged as a placeholder to revisit once
  Session 3.6's real timing data exists — not a final, confident answer
  to the original question.

**Decisions made:**
1. **The per-series Kalshi pause (0.2s) is a named constant, not a
   magic number** — same "no silent adjustments" pattern as every
   other tunable constant in this project (`KELLY_FRACTION`,
   `MIN_TITLE_SIMILARITY`, etc.).
2. **District-code matching (state + district number as a pair) is
   required only on the Elections wide-tolerance path, not the
   bucketed path** — the bucketed path (Climate/Commodities) never
   exhibited this failure mode, and this project's standing practice
   is to fix the actual bug found, not to defensively rewrite adjacent
   working code.
3. **Zero candidate pairs from venue matching does not stop the
   arbitrage orchestrator; zero rows from either venue's ingestion
   does** — these are genuinely different situations (a real, valid
   "no overlap this run" outcome vs. a broken ingestion stage), and
   collapsing them into one check would either wrongly stop a healthy
   run or wrongly let a broken one continue.
4. **Cadence set from real account-wide GitHub Actions cost data,
   explicitly acknowledging the timing question it was meant to answer
   is still open** — a deliberate trade-off between "the checkbox as
   literally worded" and "the honest state of the evidence," logged
   as such rather than either skipped or answered with invented
   confidence.
5. **GitHub Actions minute budgeting is a real, ongoing, account-wide
   concern, not a one-time calculation for this session** — the
   account's three DFS optimizer repos draw from the same 2,000-minute
   pool and their own usage will grow once NHL/PGA seasons are active.
   Rather than modeling their exact future cost today (would require
   auditing three more repos' own multi-job workflow files — itself a
   real, separate undertaking, confirmed after actually reading
   DFS_Optimizer's `refresh_data.yml` and finding it non-trivial: four
   jobs, two schedule cadences, a slate matrix, not a simple single
   script), the standing practice going forward is: check the
   account's real billing-overview page periodically (especially once
   NHL season starts), and treat the arbitrage pipeline's cadence as
   the easiest, lowest-cost lever to pull back first if the account
   ever trends toward its ceiling.

**Corrections/reversals during the session:**
- The workflow's polling cadence was originally set to every 15
  minutes, justified at the time only by request-count/timeout
  reasoning (no rate-limit or budget check). Corrected after checking
  the account's real GitHub billing page: 15 minutes would have used
  ~11,500 runner-minutes/month against a 2,000-minute account-wide
  allowance. Replaced with 6 runs/day (~720 min/month) after this real
  check, and the job timeout widened from 12 to 30 minutes to match
  (the short timeout was only needed to prevent overlap at the faster,
  since-abandoned cadence).
- `venue_matcher.py`'s Elections wide-tolerance matching was believed
  complete and validated as of Session 3.2/3.3. This session's own
  first live automated run disproved that — 9 of 10 real flags were
  false cross-state matches. Fixed within this session per item 4
  above, not deferred, consistent with this project's standing
  "real bugs found in validation get fixed now" practice.
- Greg corrected a real misunderstanding about how this detector
  works: it does not compare current data against past data the way
  pick'em's CLV logging does. Every run is a self-contained,
  point-in-time check. This correction changed what "justifying the
  cadence" actually means for this track (see Decision 4 above) and is
  recorded here so a future session doesn't re-introduce the CLV-style
  framing by assumption.

**Open items / deferred validations:**
- **A genuine scheduled (cron-triggered) run has not yet been
  confirmed** — both real runs on record were manually dispatched.
  Greg will check the Actions tab after GitHub has had time to
  register the new schedule; if a scheduled run has NOT appeared after
  a reasonable wait (Session 2.7's pick'em schedule took roughly 1h40m
  to register after a push), that is itself worth a real look, not an
  assumption that it will eventually work.
- **The one surviving flag (Kalshi MI-7 / Polymarket MI-07) has not
  been run through `sizing_engine.py arbitrage size`** — confirmed as
  a genuine same-race match via web search, but sizing it is a
  deliberate manual step per this project's "flags and sizes, never
  places bets" rule, not something this session does automatically.
- **6 runs/day is a placeholder, not a final answer** — Session 3.6
  (Live Validation Window) is where real flagged-opportunity timing
  data should replace this cost-driven placeholder with genuine
  evidence about how long a real mispricing stays open.
- **Account-wide GitHub Actions budget monitoring is now a standing
  practice, not a solved problem** — no dedicated tracking doc was
  built this session (see Decision 5's reasoning). Revisit if/when NHL
  or PGA seasons ramp up their own repos' automation, or if the
  account's billing page ever shows a trend toward the 2,000-minute
  ceiling.
- **`_extract_district_codes()` was validated against this session's
  real false-positive pairs and the one real surviving true-positive
  pair, not against every possible district-naming format** — e.g. a
  title that spells out a state name in full instead of a two-letter
  abbreviation would not be caught by the current regex and would fall
  back to the pre-existing (weaker) checks. Not a known live gap today
  (both venues' real titles observed this session use abbreviated
  state-dash-number formatting), but worth re-checking if a future
  session finds a district title formatted differently.

**Next session:** Session 3.5 (Frontend Integration) is next per
ROADMAP.md — its prerequisite (Session 3.4 complete) is now met.
