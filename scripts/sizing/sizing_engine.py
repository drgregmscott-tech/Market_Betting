"""
Session 2.6 -- Bankroll & Sizing Logic

WHAT THIS SCRIPT IS
--------------------
Turns two or more open, flagged legs from Session 2.4's
data/pickem/clv_log.csv into a concrete suggested stake for a real,
all-or-nothing pick'em entry (PrizePicks Power Play or Underdog Standard,
whichever platform the legs are from) at any leg count that platform has a
real, sourced payout number for -- see PICKEM_ENTRY_PAYOUT below. This is
the first place in the project where a probability estimate turns into an
actual dollar suggestion, so every number this script produces is either
sourced (the payout multiplier) or an explicitly named, documented
judgment call (the Kelly fraction, the platform dampener, the bankroll
cap) -- never a guessed one.

This script does NOT place any bet. Per ROADMAP.md's standing "flags and
sizes, does not place bets" principle, it prints a suggested stake; a human
decides whether to place it and reports the real outcome back through
Session 2.5's outcome_tracker.py.

WHY ONLY ALL-OR-NOTHING ENTRIES, AT SOURCED LEG COUNTS ONLY
----------------------------------------------------------------
PrizePicks and Underdog both require 2+ legs to be combined into one
all-or-nothing (Power Play / Standard) or Flex entry before a real payout
multiplier applies. Sizing real money against an entry requires knowing
that entry's real payout multiplier -- guessing at one would mean sizing
real money against an invented number, which this project does not do
(see e.g. Session 2.3's refusal to guess at PrizePicks' Fantasy Score
formula before confirming it against PrizePicks' own source). So v1
supports exactly the leg counts named in `PICKEM_ENTRY_PAYOUT` below, per
platform, and only the all-or-nothing entry type -- never Flex (see
"WHAT THIS ADDITION DOES NOT DO YET"). Every other combination (an
unsourced leg count, mixed platforms, or an unsupported platform) is
rejected with an explicit, named status -- never silently sized using a
number that was never confirmed.

SESSION 2.11 ADDENDUM -- BOTH PLATFORMS' REAL PAYOUT TABLES SOURCED AND WIRED IN
------------------------------------------------------------------------------
Through Session 2.10, only PrizePicks' 2-pick Power Play (3x, Session 2.5)
had a sourced payout, and Underdog was blocked from sizing entirely.
Session 2.11 closed both gaps in one pass, once it became clear the same
research effort needed to unblock Underdog's 2-pick entry (Underdog's own
help article) would also answer "what about 3 through 8 picks, and what
about PrizePicks' own larger entries" -- rather than doing that research
twice.

Underdog's real 2-pick Standard entry payout was sourced directly from
Underdog's own official help article
(help.underdogsports.com/en/articles/13780101-pick-em-standard-flex-entry-payouts,
"Standard Entries" table, confirmed live 2026-09-10): **3.5x**, not
PrizePicks' 3x -- confirming the two platforms' numbers are genuinely
different and must never be conflated. The same article's table was used
to source Underdog's 3- through 8-pick Standard payouts too. Separately,
PrizePicks' own published Power Play table (prizepicks.com/ways-to-pick,
confirmed live 2026-09-10, page states multipliers are "subject to
change") sourced PrizePicks' own 3- through 6-pick payouts, which PrizePicks
does not publish beyond.

`PICKEM_ENTRY_PAYOUT` is now a per-platform dict of {leg_count: multiplier}
(replacing the old flat `ENTRY_PAYOUT_MULTIPLIER` single-value-per-platform
constants), and `size_entry()` looks up the requested entry's own
(platform, leg_count) pair rather than assuming a single fixed leg count.
`entry_net_odds_b()` and `breakeven_win_rate_per_leg()` compute the Kelly
`b` and the per-leg breakeven from that same table generally (the per-leg
breakeven is the Nth root of 1/multiplier -- at N=2 this reduces to exactly
the 1/sqrt(M) figures already named in sample_size_methodology.md Section 2
and in this session's own 2-pick sourcing). `PLATFORM_RISK_MULTIPLIER
["underdog"] = 0.85` (already present in the code since Session 2.6, but
unreachable until this session removed the `SUPPORTED_PLATFORMS` gate) is
unchanged -- it was already a stated, sourced-to-research-not-to-a-number
judgment call, not something that needed re-deriving just because sizing
became reachable. An entry still cannot mix legs from two different
platforms -- the payout table applies to the whole entry, not per-leg, so
`size_entry()` rejects any request whose legs span more than one platform,
same as it always rejected a platform outside `SUPPORTED_PLATFORMS`.

THE SIZING METHOD -- FRACTIONAL KELLY, NAMED AND JUSTIFIED
---------------------------------------------------------------
Standard Kelly criterion for an all-or-nothing bet with combined win
probability p and net odds b (profit per $1 staked if the whole entry
hits):

    f* = (p * (b + 1) - 1) / b

For a 2-pick PrizePicks Power Play, b = 2 (a $1 stake returns $3 total on
a win -- $2 of that is profit); other (platform, leg_count) pairs use that
platform's own sourced b from PICKEM_ENTRY_PAYOUT. p is the entry's
combined win probability: this script multiplies every leg's own
model_prob value together (first_flagged_model_prob for each leg, from
Session 2.3's model), treating all legs as independent events -- a stated
simplification (different players/stats are a reasonable independence
assumption; see sizing_methodology.md for the case where this could fail,
e.g. two legs from the same game -- see SAME-GAME CAUTION below, which now
checks every pair of legs in an entry, not just a single pair).

Full Kelly is never staked directly. This script applies
KELLY_FRACTION = 0.25 (quarter-Kelly) -- a standard, named, conservative
practice used specifically when the win-probability input carries real
estimation uncertainty (this project's own model has no opponent/injury/
pace adjustments yet -- a stated v1 gap since Session 2.3 -- and
Session 2.4's own FLAG_EDGE_THRESHOLD is itself an unvalidated
placeholder). Quarter-Kelly is not a derived number any more than
FLAG_EDGE_THRESHOLD or Session 2.5's p1=0.60 were -- it is a reasoned
starting point, explicitly flagged here as a candidate for Session 8.3's
recalibration work once real graded outcomes exist to check it against.

PLATFORM-SPECIFIC RISK ADJUSTMENT
-------------------------------------
Per the Session 1.1 continuation research (account-limiting policy,
archived at docs/research/Pickem_Platform_Account_Limiting_Policy_Research.md):
PrizePicks has the most documented first-hand pattern of win-adjacent
account closures and withheld withdrawals; the specific "55% win rate over
200+ entries" threshold could not be corroborated and is NOT used here as
a hard number. What IS used: a named, conservative dampener applied on top
of quarter-Kelly for PrizePicks specifically, reflecting that a suspended
or limited account can turn a real, currently-winning edge into money that
is never actually collected -- a risk the raw Kelly formula does not know
about, since Kelly assumes every future bet is genuinely available to be
placed. PLATFORM_RISK_MULTIPLIER["prizepicks"] = 0.70 is this project's own
stated judgment call, not sourced to a specific number, since no source
gives one -- flagged explicitly, same as every other placeholder in this
project.

As of Session 2.11, Underdog IS sized (see "SESSION 2.11 ADDENDUM" above --
its own real, sourced payout table is now wired into PICKEM_ENTRY_PAYOUT).
PLATFORM_RISK_MULTIPLIER["underdog"] = 0.85 remains the same stated,
unsourced-to-a-specific-number judgment call it was when first added in
Session 2.6 -- only the payout-table gate that kept it unreachable has
changed, not the dampener figure itself.

SAME-GAME CAUTION DAMPENER -- FLAGGING, NOT MODELING, A REAL CORRELATION GAP
------------------------------------------------------------------------------
Kelly's formula (and the combined-probability multiplication above it)
assumes every leg is an independent event. When two (or more) legs in the
same entry come from the SAME real game (same game_id), that assumption is
weaker: a blowout, an overtime, or a key injury can move several players'
stats in the same direction at once. This project does not have real
correlation data to model that properly yet, and manufacturing a number to
"correct" for it would mean sizing real money off a guess -- exactly what
this project does not do (see Session 2.3's refusal to guess at an
unconfirmed scoring formula, or the PrizePicks dampener discussion above).

Rather than silently ignore this or invent a precise correction, this
script applies one more small, explicitly named dampener,
SAME_GAME_CAUTION_MULTIPLIER = 0.85, whenever ANY two legs in the entry
share a game_id (Session 2.11 generalized this check from "the two legs"
to "any pair of legs," since an entry can now have more than two) -- and
reports it plainly in the output (same_game_pair: True,
same_game_caution_applied: True) so it is visible whenever it happens,
never a hidden adjustment. This is a deliberate, direction-agnostic choice:
same-game correlation could in reality make the true combined probability
higher OR lower than the independence assumption suggests (it depends on
whether the two legs tend to move together or compete against each other),
and this project does not yet have the real data to know which, for which
stat pairs. Applying a mild, flagged caution factor nudges toward the
safer of the two possible errors (understaking a same-game pair) rather
than pretending independence is a safe default. This is a "flag it as
riskier, don't pretend to model it precisely" choice, not a corrected
number -- revisiting it with real same-game correlation data belongs to a
future session, once enough graded same-game entries exist to check
against (see Session 8.3).

BANKROLL CAP -- ENFORCED IN CODE, NOT JUST DESCRIBED
----------------------------------------------------------
MAX_SINGLE_POSITION_PCT = 0.05 -- no single suggested stake will ever
exceed 5% of the bankroll figure the user provides, regardless of what the
(already-dampened) Kelly fraction computes to. This is a hard ceiling,
applied after every other adjustment, so a large modeled edge cannot
produce an unreasonably large single-entry suggestion. Named and adjustable
here, not left as a documentation-only rule.

WHAT THIS SCRIPT DOES NOT DO YET (stated gap, not a silent one)
-----------------------------------------------------------------
- Does not size Flex-style entries on either platform (entries that still
  pay out, at a reduced multiplier, after one or more misses). Flex's
  payout is not a simple two-outcome win/lose bet -- it pays a different
  amount depending on exactly how many of N legs hit, so the win/lose
  Kelly formula used throughout this file does not apply to it without a
  genuinely different (multi-outcome expected-value) formulation. A named
  candidate for a future session, not guessed at here.
- Does not size any PrizePicks entry beyond 6 legs, since PrizePicks' own
  page (prizepicks.com/ways-to-pick) does not publish a Power Play number
  past 6 picks. Underdog's own table goes to 8 (its own page publishes
  that far), so PICKEM_ENTRY_PAYOUT's two platforms have genuinely
  different supported ranges -- not a bug, a reflection of what each
  platform actually publishes.
- Does not account for correlation between legs from the SAME real game
  (e.g. a QB's passing yards and his team's leading WR's receiving yards
  in the same game are not fully independent events) -- the combined
  probability is a straight product across all legs, a stated
  simplification, flagged (not corrected) by SAME_GAME_CAUTION_MULTIPLIER
  above.
- Does not track a running bankroll balance across multiple suggested
  entries placed over time -- each run is a single, independent
  suggestion against the bankroll figure supplied on that run. A real
  running-bankroll tracker (sized off the outcome_tracker.py log) is a
  named candidate for a future session, not built here.
- Does not re-derive KELLY_FRACTION or PLATFORM_RISK_MULTIPLIER from real
  graded results -- that is Session 8.3's job, same as
  FLAG_EDGE_THRESHOLD and Session 2.5's p1=0.60.

USAGE (pick'em sizing)
-----------------------
pip install pandas --break-system-packages
python sizing_engine.py pickem --flag-ids "prizepicks|12345678" "prizepicks|87654321" --bankroll 500

===============================================================================
SESSION 3.3 ADDENDUM -- ARBITRAGE SIZING (extends, does not replace, the above)
===============================================================================

WHAT WAS ADDED AND WHY IT IS NOT JUST "KELLY AGAIN"
-----------------------------------------------------
Everything above sizes a PROBABILISTIC bet: one entry either wins or loses,
and Kelly answers "how much of my bankroll should I risk on a estimated
edge." Session 3.2's arbitrage detector (`detector.py`) finds a genuinely
different shape of opportunity: two legs that, once both are actually
filled, are a LOCKED position with a guaranteed profit
(`net_profit_per_dollar`) regardless of which real-world outcome occurs --
there is no win/loss probability to plug into Kelly at all. Applying Kelly
here would be a category error, not a stricter or looser version of the
same math.

Arbitrage's real risk is not "did I pick the right side" -- it is:
1. CAPITAL LOCKUP ACROSS TWO VENUES AT ONCE. A pick'em entry stakes money
   at ONE platform. An arbitrage position requires buying one leg at
   Kalshi and the other leg at Polymarket SIMULTANEOUSLY -- the same
   dollar amount must be sitting, available, at BOTH venues at the same
   time, not split from one shared pool. `sizing_engine.py`'s pick'em
   code has always assumed a single bankroll figure because it only ever
   sizes a single-venue bet; that assumption is wrong for arbitrage and
   is not reused here.
2. EXECUTION ("LEGGING") RISK. `detector.py` prices a flagged opportunity
   at the ask price it read at pull time. Placing two real trades on two
   real venues is not instantaneous -- the price or available size on
   either leg can move in the seconds it takes to place both orders. A
   Kelly-style probability-of-winning adjustment does not describe this
   risk; a haircut on the sized position does.

WHY BANKROLL IS TWO NUMBERS, NOT ONE, FOR ARBITRAGE
------------------------------------------------------
`size_arbitrage_position()` below takes `kalshi_bankroll` and
`polymarket_bankroll` as two separate arguments -- real dollars actually
sitting, right now, in each venue's own account -- rather than one
combined bankroll figure. This mirrors the real mechanics: a $200
arbitrage position requires $200 already deposited at Kalshi AND $200
already deposited at Polymarket, a total of $400 tied up, not $200 drawn
from a shared $400 pool. Treating this as one pool would let the sizing
math suggest a position that cannot actually be placed because one
venue's account is thinner than the other's.

WHY AN OPEN-POSITIONS LEDGER WAS ADDED
------------------------------------------
A pick'em entry resolves in hours (the game ends). A real arbitrage
position may sit open for days or longer, since both legs settle only
when their real-world event resolves -- and this project has not
researched real settlement-time data for either venue, so no specific
number of days is assumed here (that would be exactly the kind of
guessed number this project's own standing rule forbids). What CAN be
tracked honestly, without guessing at settlement timing, is which
positions are currently open and how much capital each one has already
committed at each venue. `data/arbitrage/open_positions.csv` is a new,
small ledger (same pattern as Session 2.5's outcome_tracker.py): every
time a real arbitrage trade is placed, `record_open_arbitrage_position()`
appends a row; once it settles, `settle_arbitrage_position()` marks it
closed and frees that capital back up. `size_arbitrage_position()` always
subtracts currently-open commitments from the bankroll figures supplied,
so it never suggests a new position against capital that is already
tied up in an earlier, still-open one.

EXECUTION_RISK_BUFFER -- NAMED, NOT DERIVED, SAME POSTURE AS KELLY_FRACTION
------------------------------------------------------------------------------
EXECUTION_RISK_BUFFER = 0.85 is a flat haircut applied to the
liquidity/capital-bound raw position size, exactly the same "named
judgment call, not a sourced number" posture as KELLY_FRACTION and
SAME_GAME_CAUTION_MULTIPLIER above. It exists because `detector.py`'s
`fillable_size_dollars` describes size available at the INSTANT the
snapshot was pulled -- by the time a human actually places both real
orders, some of that size may already be gone or the price may have
ticked. Flagged explicitly as a candidate for Session 8.3 recalibration
once real placed-and-filled arbitrage trades exist to check it against.

RECALIBRATION ATTEMPT, 2026-09-11 (Open Decision #23) -- FIRST PASS LEFT
AT 0.85, NOT MOVED. Pulled all 21 real arbitrage snapshot files
accumulated since Session 3.4 (2026-09-06 through 2026-09-11) and
grouped by (market_a, market_b) pair to find real repeated
observations. Only 2 of 15 distinct pairs were ever seen more than
once: one (MI-07) showed 0% real fillable-size decay across three short
(10-68 minute) gaps; the other (TX-32) showed real +133%/-86% swings,
but only across multi-hour gaps. These two real findings conflict, and
the arbitrage pipeline's own ~4-6 hour snapshot cadence is structurally
too coarse to distinguish "real execution-time risk" from "the market
genuinely moved between runs" -- more accumulated days of this same
cadence would not resolve it.

REAL RECALIBRATION, SAME DAY, VIA execution_risk_poller.py -- BUFFER
NOW DEPTH-TIERED, NOT FLAT. Built a dedicated short-interval poller
(new: scripts/calibration/execution_risk_poller.py) and ran 4 real
30-minute sessions (2-minute intervals, 16 readings each) against live
markets: one down-ballot election contract (flat, uninformative -- near
zero real turnover) and three active weather contracts. Found a real,
clean pattern: fillable-size decay tracks how DEEP the order book is,
not which market it is. Two markets that stayed consistently at $200+
resting size showed 0% and -6.6% worst-case decay; two markets that sat
mostly below ~$80 showed -67% and -92% worst-case decay -- even
measured only from readings that had already crossed the OLD
MIN_SUFFICIENT_LIQUIDITY_DOLLARS=50 floor in liquidity_check.py, which
is therefore confirmed NOT protective against real execution-time risk
on its own. A single flat buffer cannot be correct for both regimes at
once. Replaced with EXECUTION_RISK_BUFFER_LIQUID (0.85, unchanged --
real evidence at depth supports the existing value with real margin)
and EXECUTION_RISK_BUFFER_THIN (0.15, new -- a deliberately conservative
round number between the two real thin-market findings of -67%/-92%,
not the literal worst case, given only 2 real thin-market sessions
exist so far), selected by EXECUTION_RISK_LIQUID_DEPTH_THRESHOLD_DOLLARS
(150.0 -- chosen to sit clearly above both thin markets' real sustained
range and clearly below both deep markets' real sustained range).

NAMED, HONEST LIMITATION -- NOT SOLVED HERE: one of the two real thin-
market sessions (KXHIGHTDAL) briefly showed a single $200.97 reading
(above the depth threshold) immediately before crashing 92% two minutes
later. This rule reads depth at ONE moment, not whether it's been
SUSTAINED -- a single deep reading is not proven to be a persistence
guarantee by this project's own real data. Flagged for a future
refinement (e.g. requiring two consecutive polls above threshold before
trusting "liquid" classification) rather than treated as solved.
See SESSION_LOG.md's 2026-09-11 entries for the full trail.

MAX_ARBITRAGE_POSITION_PCT -- SAME HARD-CAP PATTERN, APPLIED TO COMBINED CAPITAL
-----------------------------------------------------------------------------------
MAX_ARBITRAGE_POSITION_PCT = 0.05 caps a single arbitrage position at 5%
of the user's TOTAL combined bankroll (Kalshi + Polymarket balances
added together), the same hard-ceiling posture as pick'em's
MAX_SINGLE_POSITION_PCT, so one large flagged price gap cannot suggest an
outsized single commitment even before the per-venue capital check is
applied.

WHAT THIS ADDITION DOES NOT DO YET (stated gap, not a silent one)
-----------------------------------------------------------------------
- Does not model real settlement time / capital-lockup DURATION -- see
  "open-positions ledger" above. It tracks that capital IS locked, not
  for how long.
- Does not re-derive EXECUTION_RISK_BUFFER from real fill data -- a
  starting value, same as KELLY_FRACTION was in Session 2.6.
- Does not net opposing open positions against each other (e.g. an open
  Kalshi commitment from one arbitrage trade is not offset against a
  fresh flag that would sell back into the same market) -- each open
  position's committed capital is treated as fully locked until settled.

USAGE (arbitrage sizing)
--------------------------
python sizing_engine.py arbitrage size --market-a KXHOUSEMO5-26-R --market-b 0x1234abcd --kalshi-bankroll 1000 --polymarket-bankroll 1000
python sizing_engine.py arbitrage record-open --market-a KXHOUSEMO5-26-R --market-b 0x1234abcd --kalshi-bankroll 1000 --polymarket-bankroll 1000
python sizing_engine.py arbitrage settle --position-id <id> --note "both legs settled, profit collected"

===============================================================================
SESSION 5.4 ADDENDUM -- POLITICS (DOWN-BALLOT) SIZING
===============================================================================

WHY THIS IS A THIRD, DIFFERENT SIZING SHAPE -- NOT PICK'EM AGAIN, NOT ARBITRAGE
--------------------------------------------------------------------------------
Session 5.2's politics_model.py and Session 5.3's clv_logger.py --track
politics produce single-contract flags on Kalshi or Polymarket -- "buy YES
on this candidate at this price." That is closer to arbitrage's single-leg
mechanics than to pick'em's multi-leg parlay, but it is not a locked,
guaranteed-profit position like arbitrage -- it is a genuine probabilistic
bet, so Kelly applies here, unlike arbitrage. And unlike pick'em (resolves
in hours, one game at a time) or arbitrage (both legs typically settle once
the underlying event resolves, day-to-weeks per Session 3.3's own stated
gap), a down-ballot political contract can sit open for WEEKS OR MONTHS --
Session 5.1's real ingested race data runs up to the 2026 general election,
still roughly two months out as of this session (see politics_estimation_
model_spec.md's GENERAL_ELECTION_DATE). Session 5.3's own CLV log carries
`hours_to_resolution` on every row specifically because this gap was
already flagged as this session's concern (see that session's SESSION_LOG
entry: "a heads-up for Session 5.4").

Two real consequences follow directly from that long lockup, neither of
which pick'em's or arbitrage's sizing code accounts for:

1. OPPORTUNITY COST OF LONG-LOCKED CAPITAL. A dollar staked on a race that
   resolves in 2 days can be restaked on a new opportunity almost
   immediately if it loses (or is realized if it wins); a dollar staked on
   a race that resolves in 4 months cannot. The same modeled edge is worth
   less per year of capital tied up the longer it sits locked -- standard
   position-sizing logic, but nothing upstream of this session's code
   currently reflects it.
2. MANY SIMULTANEOUS LONG-DATED POSITIONS CAN OVERLAP. Because down-ballot
   positions resolve slowly, a real user placing several flagged politics
   bets over a few weeks will likely have MANY of them open AT THE SAME
   TIME (unlike pick'em, where an entry is settled same-day before the
   next is placed, or arbitrage, where Session 3.3's own open-positions
   ledger already tracks this per-venue). A single-position bankroll cap
   alone (this project's existing MAX_SINGLE_POSITION_PCT pattern) does
   not prevent ten simultaneously-open long-dated positions from
   collectively locking up far more of a bankroll than any one position
   looks risky on its own.

CAPITAL-LOCKUP DAMPENER -- NAMED, STEP-FUNCTION, NOT A DERIVED NUMBER
-----------------------------------------------------------------------
Same posture as SAME_GAME_CAUTION_MULTIPLIER (Session 2.6) and
EXECUTION_RISK_BUFFER (Session 3.3): this project has no real source or
graded data yet describing exactly how much a political-market edge should
be discounted for a given number of months of capital lockup. Rather than
invent a precise number, `POLITICS_LOCKUP_DAMPENER_TABLE` applies a
conservative, monotonically-decreasing step function keyed off
`hours_to_resolution` (already logged by Session 5.3) -- less than 30 days
gets no extra dampening beyond the shared quarter-Kelly step; each
additional resolution-time band applies a larger, explicitly stated
haircut. This is a real, stated judgment call, not sourced to a specific
figure -- flagged here exactly like every other placeholder in this
project, and a named candidate for Session 8.3's recalibration work once
enough real graded political positions exist (a track that, per Session
5.2, cannot be sanity-checked against resolved contracts until after the
2026 general election).

PORTFOLIO-LEVEL EXPOSURE LEDGER -- WHY THIS TRACK NEEDS A SECOND CAP
------------------------------------------------------------------------
`data/politics/open_positions.csv` is a new, small ledger, same append/
settle pattern as Session 3.3's arbitrage ledger. Every time a real
politics position is recorded, `record_open_politics_position()` appends a
row; `settle_politics_position()` marks it closed once the real race
resolves and frees that capital back up. Unlike arbitrage's ledger (which
exists to prevent double-committing capital already locked in one still-
open trade), this ledger's main job is enforcing
`POLITICS_MAX_TOTAL_EXPOSURE_PCT` -- a hard ceiling on the TOTAL capital
locked across every simultaneously-open politics position, on top of
(never instead of) the existing single-position cap
(`POLITICS_MAX_SINGLE_POSITION_PCT`). This directly addresses the "many
simultaneous long-dated positions" consequence named above -- a single
well-sized position and an already-overexposed portfolio look identical to
a per-position cap alone.

WHAT THIS ADDITION DOES NOT DO YET (stated gap, not a silent one)
-----------------------------------------------------------------------
- Does not model real opportunity-cost dollar figures (e.g. an actual
  annualized-return comparison against alternative uses of the same
  capital) -- POLITICS_LOCKUP_DAMPENER_TABLE is a stated, conservative
  step function, not a derived rate.
- Does not net or partially release capital for a position whose resolution
  date moves closer over time -- each open position's committed capital is
  treated as fully locked at its originally recorded amount until settled,
  same simplification Session 3.3's arbitrage ledger already makes.
- Does not re-derive KELLY_FRACTION, the lockup dampener table, or the two
  cap percentages from real graded results -- Session 8.3's job, once real
  resolved down-ballot contracts exist (post-2026-general-election, per
  Session 5.2's own stated constraint).

USAGE (politics sizing)
--------------------------
python sizing_engine.py politics size --flag-id "kalshi|MO-05|R" --venue-bankroll 500
python sizing_engine.py politics record-open --flag-id "kalshi|MO-05|R" --venue-bankroll 500
python sizing_engine.py politics settle --position-id <id> --note "race called, contract resolved"

===============================================================================
SESSION 6.4 ADDENDUM -- SPORTSBOOK PLAYER PROPS (DK/FD) SIZING
===============================================================================

WHY THIS IS ITS OWN SHAPE, NOT POLITICS SIZING REUSED BLINDLY
------------------------------------------------------------------
Session 6.3's clv_logger.py --track props flags carry the exact same shape
politics' single-contract Kelly math already handles: one flagged side,
one flag-time model probability, one flag-time market-implied price
(`first_flagged_model_prob` / `first_flagged_market_price` in the shared
CLV_CORE_COLUMNS -- see clv_logger.py). So the Kelly math itself
(`raw_kelly_fraction_binary_contract`) IS reused directly, not
reimplemented -- there is no new probability math to invent here. What
IS genuinely different, and is the actual point of this session per
ROADMAP.md's own card title ("Account-Limiting Risk Built In"): this is
the one track, of every track built so far, where the Track Reference
table (ROADMAP.md) names account-limiting risk as this project's OWN
highest-confidence concern for a venue type -- sportsbooks limiting or
banning consistently-winning bettors is the single most widely documented
account-restriction pattern in the entire sports-betting industry, more
so than either pick'em platform (Session 2.6's own PLATFORM_RISK_MULTIPLIER
research, `Pickem_Platform_Account_Limiting_Policy_Research.md`, found
PrizePicks/Underdog's evidence was ToS-power-only plus scattered first-hand
reports) or an exchange (Kalshi/Polymarket structurally cannot limit a
winner the way a bookmaker can -- Session 0.1's own founding vig
comparison). No project research doc specifically quantifies DK/FD's
real limiting rate or threshold (a stated, open gap -- see
`docs/research/sport_inventory.md`'s own "Account-limiting risk. Not yet
researched specifically for [sportsbooks]" note), so, exactly like
Session 2.6's PrizePicks dampener and Session 5.4's lockup table before
it, `PROPS_PLATFORM_RISK_MULTIPLIER` below is a NAMED, STATED JUDGMENT
CALL, not a sourced number -- set more conservative than pick'em's own
0.70 specifically because this venue type's limiting reputation is the
best-corroborated of the three, not because any specific DK/FD figure was
found.

PROPS_PLATFORM_RISK_MULTIPLIER -- NAMED, NOT DERIVED, SAME POSTURE AS
EVERY OTHER DAMPENER IN THIS FILE
------------------------------------------------------------------------
PROPS_PLATFORM_RISK_MULTIPLIER = {"draftkings": 0.50, "fanduel": 0.50} --
applied on top of quarter-Kelly, same mechanical position in the pipeline
as PLATFORM_RISK_MULTIPLIER["prizepicks"]. Both platforms get the same
figure because no source in this project distinguishes DK's limiting
practice from FD's -- inventing a difference between them would be
exactly the kind of guessed precision this project's own standing rule
forbids. Revisiting this against real graded results (were flagged props
actually followed by a real limiting/restriction event?) is Session 8.3's
job, same as every other dampener in this file.

FIELD-VIG-UNRESOLVED CAUTION -- A SECOND, DISTINCT DAMPENER FOR DK ROWS
STILL FLAGGED implied_prob_includes_field_vig=True
------------------------------------------------------------------------
Session 6.4 also fixed DK's TD-scorer field-vig problem in
`sportsbook_props_model.py` (see that file's own docstring) -- but the
fix only reaches rows this run's real data could actually group with
other real selections in the same market (`group_size >= 2`). A row this
run could only capture alone still reports the RAW, vig-included price
with the flag left True (an honest per-row boundary, not a claim the fix
covers every row). Sizing that row's edge as if it were already
field-normalized would risk staking real money against a number that
may still include real field vig. `PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER
= 0.60` -- another named, stated judgment call (not derived), applied
ONLY when `implied_prob_includes_field_vig` is True on the flag being
sized -- flags a real, distinct uncertainty this session's own fix could
not fully close, rather than silently sizing it the same as a row that
IS field-normalized.

WHAT THIS ADDITION DOES NOT DO YET (stated gap, not a silent one)
-----------------------------------------------------------------------
- Does not distinguish DK's limiting practice from FD's (see above) --
  both get the same PROPS_PLATFORM_RISK_MULTIPLIER.
- Does not track a portfolio-level exposure ledger the way Session 5.4's
  politics track does -- props resolve same-day/same-week (a live game),
  not weeks/months out, so the long-simultaneous-lockup problem that
  motivated politics' second cap does not apply the same way here. A
  single-position cap (PROPS_MAX_SINGLE_POSITION_PCT) is judged
  sufficient for v1.
- Does not re-derive PROPS_PLATFORM_RISK_MULTIPLIER or
  PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER from real graded results --
  Session 8.3's job, once real graded props positions exist.

USAGE (props sizing)
-----------------------
python sizing_engine.py props size --flag-id "draftkings|1234567890" --bankroll 500

===============================================================================
SESSION 4.4 ADDENDUM -- WEATHER (KALSHI) SIZING
===============================================================================

WHY THIS WAS BUILT NOW, OUT OF ROADMAP ORDER
-----------------------------------------------
ROADMAP.md's Session 4.4 card ("Sizing Adaptation" for the weather track)
was scoped right after Session 4.3 (CLV Logging Hook-In, weather), but sat
untouched at "Not started" while Sessions 5.4 (politics) and 6.4 (props)
were both built on top of the same shared clv_logger.py/sizing_engine.py
infrastructure -- the same kind of roadmap-order gap Session 4.3 itself
was found sitting in before it was finally built (see that session's own
SESSION_LOG.md entry). Found and closed now, following that same
established pattern: check what real infrastructure already exists
(Session 4.3's data/weather/clv_log.csv, live and producing real flags)
before writing anything new, rather than guessing at a schema.

WHY THIS IS CLOSER TO POLITICS/PROPS THAN TO PICK'EM, BUT NOT IDENTICAL
------------------------------------------------------------------------
Session 4.3's weather flags carry the exact same single-contract shape
politics and props already handle: one flagged side ("yes" or "no"), one
flag-time model probability (`first_flagged_model_prob`), one flag-time
market price (`first_flagged_market_price`) -- so `raw_kelly_fraction_
binary_contract()` is reused directly here too, not reimplemented a third
time. What is genuinely new, and is this session's actual roadmap
requirement ("Sizing correctly reflects Kalshi's fee structure and this
track's typical edge size"), is two things neither politics nor props
needed to model:

1. KALSHI'S REAL, PUBLISHED TRADING FEE. Unlike PrizePicks/Underdog
   (Session 2.6 -- no stated per-trade fee, only an account-limiting risk)
   or DK/FD (Session 6.4 -- same), Kalshi charges a real, published,
   round-trip trading fee on every contract: fee = round_up_to_the_cent
   (0.07 * contracts * price * (1 - price)) [Kalshi's own published
   general fee schedule, cross-checked against multiple independent 2026
   sources -- see docs/research/kalshi_fee_structure.md]. Unlike every
   other dampener in this file, this is NOT a named judgment call -- it
   is a real, sourced, formulaic cost that this project's own weather
   ingestion (Session 4.1) does not carry a fee-tier field for, so it
   must be computed here at sizing time, using the flag's own
   `first_flagged_market_price`. A single-contract sizing call cannot
   know the real total contract count in advance (that depends on the
   very stake this function is trying to compute), so this function
   uses the PER-CONTRACT fee rate (0.07 * price * (1-price), i.e. the
   formula's contract-count term set to 1) as the effective marginal
   cost per contract -- a stated, deliberate simplification of Kalshi's
   real order-level cent-rounding (which only matters at very small
   order sizes; see "WHAT THIS ADDITION DOES NOT DO YET" below), not a
   guessed number the way PLATFORM_RISK_MULTIPLIER or the lockup table
   are.
2. THIS TRACK'S OWN TYPICAL EDGE SIZE. Per Session 4.3's real live run
   (203 of 288 real contracts flagged, edges ranging 0.031-0.994) and
   Session 4.2's real backtest (81.58% directional accuracy, 228 real
   resolved contracts), weather edges are frequent but often small and
   short-dated (`lead_days` -- most contracts resolve within days, unlike
   politics' weeks/months). This is the opposite shape from politics'
   problem (few, large, long-locked positions needing a portfolio-level
   exposure cap) -- weather is closer to props' shape (frequent,
   same-day/short-dated, single-position cap judged sufficient, per
   Session 6.4's own reasoning) than to politics'. No portfolio-level
   exposure ledger is built for weather, for the same stated reason
   Session 6.4 gave for props: positions resolve in days, not weeks or
   months, so many-simultaneous-long-dated-positions is not this
   track's real risk shape.

WHY THE FEE IS FOLDED INTO THE EFFECTIVE COST, NOT A FLAT DAMPENER
---------------------------------------------------------------------
Every other per-track adjustment in this file (PLATFORM_RISK_MULTIPLIER,
SAME_GAME_CAUTION_MULTIPLIER, the lockup table, PROPS_FIELD_VIG_
UNRESOLVED_MULTIPLIER) is a flat multiplier applied AFTER Kelly, because
none of them describe a real, quantifiable dollar cost -- they are all
named judgment calls standing in for a risk this project has no real data
to price precisely. Kalshi's trading fee is different: it IS a real,
known dollar cost, so it belongs INSIDE the Kelly calculation itself, the
same way a sportsbook's vig is already baked into `price` everywhere else
in this file (the market price already reflects the book's edge; Kelly
is computed against that price directly). `kalshi_effective_cost_per_
contract(price)` returns `price + fee_per_contract(price)` -- the real,
all-in cost to acquire one contract -- and `raw_kelly_fraction_binary_
contract()` is called with THAT effective cost in place of the raw
market price, so the Kelly fraction this session produces already nets
out the real fee rather than overstating the edge by the fee amount and
then trying to claw it back with an unrelated flat multiplier.

WHAT THIS ADDITION DOES NOT DO YET (stated gap, not a silent one)
-----------------------------------------------------------------------
- Does not model Kalshi's real ORDER-LEVEL cent-rounding (the published
  formula rounds up once per whole order, not once per contract) -- this
  function's per-contract fee rate is the formula's own per-dollar rate
  applied at contract count = 1, a stated simplification that slightly
  OVER-states the real fee at large contract counts (rounding up on a
  100-contract order costs less per contract than rounding up 100 times)
  and slightly UNDER-states it at very small ones (a true 1-contract
  order rounds up to a full cent regardless of the formula's raw
  output) -- named here as a real, bounded imprecision, not treated as
  exact.
- Does not distinguish Kalshi's general 7% fee rate from any
  elevated-fee-tier market Kalshi may designate differently -- Session
  4.1's own weather ingestion carries no fee-tier field to check, so
  every weather contract is sized assuming the general rate. A stated
  gap, same posture as every other "our own data doesn't carry this
  field yet" gap already named elsewhere in this file.
- Does not track a portfolio-level exposure ledger (see "why this track
  is closer to props" above) -- a single-position cap
  (WEATHER_MAX_SINGLE_POSITION_PCT) is judged sufficient for v1, same
  reasoning Session 6.4 gave for props.
- Does not re-derive KALSHI_FEE_RATE from real data (it is sourced
  directly to Kalshi's own published fee schedule, not a placeholder),
  but does NOT re-derive KELLY_FRACTION for this track specifically --
  Session 8.3's job, once real graded weather outcomes exist.

USAGE (weather sizing)
--------------------------
python sizing_engine.py weather size --flag-id "KXHIGHNY-26SEP07-T77" --bankroll 500
"""

from __future__ import annotations

import argparse
import csv
import glob
import logging
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import pandas as pd

# ---------------------------------------------------------------------------
# Paths -- matching Session 2.2/2.4/2.5's existing repo-relative pattern.
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parents[2]
CLV_LOG_PATH = BASE_DIR / "data" / "pickem" / "clv_log.csv"
LOG_PATH = BASE_DIR / "logs" / "sizing.log"

# Session 3.3 additions -- arbitrage sizing reads Session 3.2's flag output
# and maintains its own small open-positions ledger (see docstring
# addendum above for why this ledger exists).
ARBITRAGE_FLAGS_DIR = BASE_DIR / "data" / "arbitrage" / "flags"
ARBITRAGE_OPEN_POSITIONS_PATH = BASE_DIR / "data" / "arbitrage" / "open_positions.csv"

# Session 5.4 additions -- politics sizing reads Session 5.3's clv_log.csv
# and maintains its own portfolio-level open-positions ledger (see
# "SESSION 5.4 ADDENDUM" in the docstring above for why this ledger exists).
POLITICS_CLV_LOG_PATH = BASE_DIR / "data" / "politics" / "clv_log.csv"
POLITICS_OPEN_POSITIONS_PATH = BASE_DIR / "data" / "politics" / "open_positions.csv"

# Session 6.4 addition -- props sizing reads Session 6.3's clv_log.csv.
# No open-positions ledger (see "SESSION 6.4 ADDENDUM" docstring above for
# why this track doesn't need politics' portfolio-level exposure cap).
PROPS_CLV_LOG_PATH = BASE_DIR / "data" / "sportsbook_props" / "clv_log.csv"

# Session 4.4 addition -- weather sizing reads Session 4.3's clv_log.csv.
# No open-positions ledger, same reasoning as props (Session 6.4): this
# track's positions resolve in days, not weeks/months -- see "SESSION 4.4
# ADDENDUM" docstring above.
WEATHER_CLV_LOG_PATH = BASE_DIR / "data" / "weather" / "clv_log.csv"

# ---------------------------------------------------------------------------
# Constants -- named explicitly, per this project's "no unnamed black-box
# factors" documentation standard. See module docstring for full reasoning
# on each one.
# ---------------------------------------------------------------------------
ENTRY_TYPE_NAME = {"prizepicks": "Power Play", "underdog": "Standard"}

# Session 2.11 sourced the 2-pick number for each platform; Session 2.11's
# same-day follow-up extended this to every all-or-nothing leg count each
# platform has a REAL, PUBLISHED number for. These two tables are NOT
# interchangeable (see docstring "SESSION 2.11 ADDENDUM") -- each key is a
# leg count, each value is that platform's own published payout multiplier
# for an entry of exactly that many legs, ALL of which must hit (Power
# Play / Standard). Flex-style entries (which still pay out after one or
# more misses, at a lower multiplier) are a genuinely different payout
# shape -- not a simple two-outcome win/lose bet, so Kelly as implemented
# here does not apply to them without real rework -- and are explicitly
# NOT sized by this script (see "WHAT THIS ADDITION DOES NOT DO YET" in
# the docstring addendum below).
#
# PrizePicks Power Play -- sourced directly from prizepicks.com/ways-to-pick
# (PrizePicks' own page; the page itself states multipliers are "subject to
# change"), confirmed 2026-09-10. The 2-pick figure (3.0x) matches Session
# 2.5's own independently-sourced number (sample_size_methodology.md
# Section 2).
PICKEM_ENTRY_PAYOUT = {
    "prizepicks": {2: 3.0, 3: 6.0, 4: 10.0, 5: 20.0, 6: 37.5},
    # Underdog Standard entry -- sourced directly from Underdog's own help
    # article (help.underdogsports.com/en/articles/13780101-pick-em-standard-
    # flex-entry-payouts, "Standard Entries" table), confirmed live
    # 2026-09-10.
    "underdog": {2: 3.5, 3: 6.5, 4: 12.0, 5: 20.0, 6: 35.0, 7: 65.0, 8: 120.0},
}


def entry_net_odds_b(platform: str, leg_count: int) -> float:
    """b in the Kelly formula (profit per $1 staked on a win) for a given
    platform's own sourced payout at this leg count."""
    return PICKEM_ENTRY_PAYOUT[platform][leg_count] - 1.0


def breakeven_win_rate_per_leg(platform: str, leg_count: int) -> float:
    """Per-leg breakeven win rate for an equal-probability N-leg
    all-or-nothing entry: the Nth root of 1/payout_multiplier. For N=2 this
    reduces to the same 1/sqrt(M) figure named explicitly in Session 2.5's
    sample_size_methodology.md (PrizePicks: sqrt(1/3) = 0.5774; Underdog:
    sqrt(1/3.5) = 0.5345) -- computed generally here so it stays correct at
    every other sourced leg count too, rather than hand-deriving one figure
    per (platform, leg_count) pair."""
    multiplier = PICKEM_ENTRY_PAYOUT[platform][leg_count]
    return multiplier ** (-1.0 / leg_count)

KELLY_FRACTION = 0.25  # quarter-Kelly -- stated placeholder, see docstring

PLATFORM_RISK_MULTIPLIER = {
    "prizepicks": 0.70,  # stated judgment call, see docstring -- account-closure risk dampener
    "underdog": 0.85,    # stated judgment call, see docstring -- same posture, less-documented risk
}
SUPPORTED_PLATFORMS = {"prizepicks", "underdog"}  # v1 gate -- both platforms now have a sourced payout multiplier

MAX_SINGLE_POSITION_PCT = 0.05  # hard bankroll cap, enforced below -- see docstring
MIN_BANKROLL = 1.0  # guards against a zero/negative bankroll producing a nonsense stake

SAME_GAME_CAUTION_MULTIPLIER = 0.85  # stated, direction-agnostic placeholder -- see docstring

# ---------------------------------------------------------------------------
# Session 3.3 additions -- arbitrage-specific constants. Same "named, not
# guessed" standard as the pick'em constants above -- see docstring
# addendum for the reasoning behind each one.
# ---------------------------------------------------------------------------
ARBITRAGE_SUPPORTED_PLATFORMS = {"kalshi", "polymarket"}

# Depth-tiered execution-risk haircut (recalibrated 2026-09-11, see
# docstring's "REAL RECALIBRATION" section for the full real-data trail
# via execution_risk_poller.py). Real evidence: deep order books ($200+
# sustained) showed 0% to -6.6% real decay over 30 real minutes; thin
# ones (mostly under ~$80) showed -67% to -92% -- a single flat number
# cannot fit both regimes.
EXECUTION_RISK_LIQUID_DEPTH_THRESHOLD_DOLLARS = 150.0
EXECUTION_RISK_BUFFER_LIQUID = 0.85  # unchanged -- real margin above the -6.6% worst case observed at depth
EXECUTION_RISK_BUFFER_THIN = 0.15  # new -- conservative round number between the real -67%/-92% thin-market findings


def execution_risk_buffer_for_depth(fillable_contracts: float) -> float:
    """Real, evidence-based depth-tiered lookup -- see the module
    docstring's 2026-09-11 recalibration section for where these two
    numbers and the threshold between them come from."""
    if fillable_contracts >= EXECUTION_RISK_LIQUID_DEPTH_THRESHOLD_DOLLARS:
        return EXECUTION_RISK_BUFFER_LIQUID
    return EXECUTION_RISK_BUFFER_THIN
MAX_ARBITRAGE_POSITION_PCT = 0.05  # hard cap vs. TOTAL combined bankroll -- see docstring
MIN_ARBITRAGE_BANKROLL = 1.0  # guards against a zero/negative bankroll figure

# ---------------------------------------------------------------------------
# Session 5.4 additions -- politics-specific constants. Same "named, not
# guessed" standard as every other constant in this file -- see the
# "SESSION 5.4 ADDENDUM" docstring section above for the reasoning behind
# each one.
# ---------------------------------------------------------------------------
POLITICS_SUPPORTED_VENUES = {"kalshi", "polymarket"}
POLITICS_MAX_SINGLE_POSITION_PCT = 0.05  # same single-position ceiling posture as pick'em/arbitrage
POLITICS_MAX_TOTAL_EXPOSURE_PCT = 0.25  # NEW: portfolio-level cap -- see docstring "why a second cap"
MIN_POLITICS_BANKROLL = 1.0  # guards against a zero/negative bankroll figure

# Stated, conservative step function -- NOT a derived/sourced number (see
# docstring). Keyed on hours_to_resolution; each tuple is
# (max_hours_for_this_band, dampener_multiplier). The last band (no upper
# bound) is represented with float("inf").
POLITICS_LOCKUP_DAMPENER_TABLE = [
    (24 * 30, 1.00),    # < 30 days -- no extra lockup dampening
    (24 * 90, 0.85),    # 30-90 days
    (24 * 180, 0.70),   # 90-180 days
    (float("inf"), 0.55),  # 180+ days
]

# ---------------------------------------------------------------------------
# Session 6.4 additions -- sportsbook player props (DK/FD)-specific
# constants. Same "named, not guessed" standard as every other constant in
# this file -- see the "SESSION 6.4 ADDENDUM" docstring section above for
# the reasoning behind each one.
# ---------------------------------------------------------------------------
PROPS_SUPPORTED_PLATFORMS = {"draftkings", "fanduel", "betmgm"}
PROPS_PLATFORM_RISK_MULTIPLIER = {
    "draftkings": 0.50,  # stated judgment call, see docstring -- account-limiting-risk dampener
    "fanduel": 0.50,      # same figure -- no source distinguishes DK from FD (see docstring)
    # Session 6.9 -- BetMGM is one of the largest, most established
    # regulated US sportsbooks, subject to the same well-documented
    # industry-wide account-limiting pattern this whole dampener exists
    # for (see docstring above) -- no project research distinguishes it
    # from DK/FD specifically, so it gets the same figure rather than a
    # guessed difference, same standing rule as DK vs. FD above.
    # NAMED, DISTINCT, UNRESOLVED CONSIDERATION (not folded into this
    # number -- inventing a value for it with no real evidence would be
    # exactly the "guessed precision" this file's own standing rule
    # forbids): BetMGM's real price here is sourced via Rotowire's own
    # copy of BetMGM's line (see ingest_rotowire_betmgm_props.py), not a
    # live pull from BetMGM directly -- how fresh Rotowire's copy is at
    # the moment a flag is sized has not been measured this session. A
    # real bettor should treat `first_flagged_market_price` as "BetMGM's
    # line as of Rotowire's last refresh," and re-check BetMGM's own real
    # line before actually placing a bet, not assume second-for-second
    # freshness the way a direct DK/FD pull would imply. Left as a stated
    # open item for Session 8.3 (same real-graded-results revisit point
    # as every other dampener here) rather than a guessed multiplier.
    "betmgm": 0.50,
}
PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER = 0.60  # stated placeholder -- see docstring
PROPS_MAX_SINGLE_POSITION_PCT = 0.05  # same single-position ceiling posture as every other track
MIN_PROPS_BANKROLL = 1.0  # guards against a zero/negative bankroll figure

# ---------------------------------------------------------------------------
# Session 4.4 additions -- weather (Kalshi)-specific constants. Unlike every
# other per-track constant above, KALSHI_FEE_RATE is a real, sourced
# published figure, not a named judgment call -- see "SESSION 4.4 ADDENDUM"
# docstring above and docs/research/kalshi_fee_structure.md.
# ---------------------------------------------------------------------------
KALSHI_FEE_RATE = 0.07  # Kalshi's published general trading fee rate (sourced, see docstring)
WEATHER_SUPPORTED_SIDES = {"yes", "no"}
WEATHER_MAX_SINGLE_POSITION_PCT = 0.05  # same single-position ceiling posture as every other track
MIN_WEATHER_BANKROLL = 1.0  # guards against a zero/negative bankroll figure

POLITICS_LEDGER_FIELDS = [
    "position_id",
    "opened_at",
    "venue",
    "race_id",
    "party",
    "flag_id",
    "candidate_name",
    "hours_to_resolution_at_open",
    "capital_committed",
    "status",
    "settled_at",
    "settlement_note",
]

ARBITRAGE_LEDGER_FIELDS = [
    "position_id",
    "opened_at",
    "platform_a",
    "market_a",
    "leg_a_side",
    "leg_a_ask",
    "capital_committed_a",
    "platform_b",
    "market_b",
    "leg_b_side",
    "leg_b_ask",
    "capital_committed_b",
    "net_profit_per_dollar",
    "expected_profit_dollars",
    "status",
    "settled_at",
    "settlement_note",
]


def setup_logging() -> logging.Logger:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("sizing_engine")
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


# ---------------------------------------------------------------------------
# CLV log lookup
# ---------------------------------------------------------------------------
def load_clv_log() -> pd.DataFrame:
    if not CLV_LOG_PATH.exists():
        raise FileNotFoundError(
            f"{CLV_LOG_PATH} not found. Run clv_logger.py first (Session 2.4) "
            f"so there are flagged opportunities to size."
        )
    return pd.read_csv(CLV_LOG_PATH)


def fetch_legs(flag_ids: list[str]) -> tuple[list[dict], list[str]]:
    """Looks up each flag_id in the live CLV log. Returns (legs_found,
    problems) -- problems is a list of human-readable reasons any
    requested flag_id could not be used, so a rejected sizing request
    always says exactly why, not just that it failed."""
    clv_df = load_clv_log()
    legs: list[dict] = []
    problems: list[str] = []

    for flag_id in flag_ids:
        matches = clv_df.loc[clv_df["flag_id"] == flag_id]
        if len(matches) == 0:
            problems.append(f"flag_id '{flag_id}' not found in {CLV_LOG_PATH}")
            continue
        row = matches.iloc[0].to_dict()

        if row.get("status") != "open":
            problems.append(
                f"flag_id '{flag_id}' has status='{row.get('status')}', not 'open' "
                f"-- this leg is no longer available to bet (game likely locked)."
            )
            continue

        model_prob = row.get("first_flagged_model_prob")
        if model_prob is None or pd.isna(model_prob):
            problems.append(f"flag_id '{flag_id}' has no first_flagged_model_prob logged.")
            continue

        if row.get("game_id") is None or pd.isna(row.get("game_id")):
            problems.append(
                f"flag_id '{flag_id}' has no game_id logged -- required to check for a "
                f"same-game pair (see SAME_GAME_CAUTION_MULTIPLIER in the docstring)."
            )
            continue

        legs.append(row)

    return legs, problems


# ---------------------------------------------------------------------------
# Sizing math
# ---------------------------------------------------------------------------
def combined_entry_probability(legs: list[dict]) -> float:
    """Product of each leg's own flagged-side model probability. Treats
    legs as independent -- a stated simplification, see docstring."""
    p = 1.0
    for leg in legs:
        p *= float(leg["first_flagged_model_prob"])
    return p


def raw_kelly_fraction(p: float, b: float) -> float:
    """f* = (p*(b+1) - 1) / b. Can be negative (no real edge) -- callers
    must floor at 0, never bet a negative fraction."""
    return (p * (b + 1.0) - 1.0) / b


def size_entry(legs: list[dict], bankroll: float) -> dict:
    """Runs the full sizing pipeline for one all-or-nothing pick'em entry
    (PrizePicks Power Play or Underdog Standard, whichever platform the
    legs are from, at whatever leg count that platform has a real, sourced
    payout for -- see PICKEM_ENTRY_PAYOUT) and returns a fully-explained
    result dict -- every intermediate number is included, not just the
    final stake, so a manual sanity check never requires re-deriving the
    math by hand."""
    platforms = {leg.get("platform") for leg in legs}

    if len(platforms) != 1 or not platforms.issubset(SUPPORTED_PLATFORMS):
        return _rejected(
            f"sizing_engine v1 only supports platform(s) {sorted(SUPPORTED_PLATFORMS)}, "
            f"one platform per entry (an entry's payout table applies to the "
            f"whole entry, not per leg, so it cannot mix legs from two "
            f"different platforms) -- received leg(s) from {sorted(platforms)}."
        )

    platform = legs[0]["platform"]
    payout_table = PICKEM_ENTRY_PAYOUT[platform]
    leg_count = len(legs)

    if leg_count not in payout_table:
        return _rejected(
            f"sizing_engine v1 only supports {sorted(payout_table)}-leg all-or-nothing "
            f"({ENTRY_TYPE_NAME[platform]}) entries on {platform} -- received {leg_count} "
            f"legs. Flex-style entries (which pay out after a miss) are not sized -- "
            f"see docstring."
        )

    if bankroll < MIN_BANKROLL:
        return _rejected(f"--bankroll must be at least {MIN_BANKROLL}, got {bankroll}.")

    payout_multiplier = payout_table[leg_count]
    net_odds_b = entry_net_odds_b(platform, leg_count)
    breakeven_win_rate = breakeven_win_rate_per_leg(platform, leg_count)

    p_combined = combined_entry_probability(legs)
    f_raw = raw_kelly_fraction(p_combined, net_odds_b)
    f_quarter = max(f_raw, 0.0) * KELLY_FRACTION

    dampener = PLATFORM_RISK_MULTIPLIER[platform]

    game_ids = [leg.get("game_id") for leg in legs]
    same_game_pair = len(set(game_ids)) < len(game_ids)  # True if ANY two legs share a game_id
    same_game_multiplier = SAME_GAME_CAUTION_MULTIPLIER if same_game_pair else 1.0

    f_dampened = f_quarter * dampener * same_game_multiplier

    uncapped_stake = bankroll * f_dampened
    cap_amount = bankroll * MAX_SINGLE_POSITION_PCT
    capped = uncapped_stake > cap_amount
    final_stake = min(uncapped_stake, cap_amount)

    if f_raw <= 0:
        status = "no_bet_negative_edge"
        final_stake = 0.0
    elif capped:
        status = "sized_capped_at_max_position"
    else:
        status = "sized"

    return {
        "status": status,
        "entry_type": f"{leg_count}-pick {ENTRY_TYPE_NAME[platform]}",
        "leg_count": leg_count,
        "platform": platform,
        "leg_flag_ids": [leg["flag_id"] for leg in legs],
        "leg_model_probs": [float(leg["first_flagged_model_prob"]) for leg in legs],
        "combined_entry_probability": round(p_combined, 4),
        "entry_payout_multiplier": payout_multiplier,
        "breakeven_win_rate_reference": breakeven_win_rate,
        "entry_net_odds_b": net_odds_b,
        "raw_kelly_fraction": round(f_raw, 4),
        "quarter_kelly_fraction": round(f_quarter, 4),
        "platform_risk_multiplier_applied": dampener,
        "same_game_pair": same_game_pair,
        "same_game_caution_multiplier_applied": same_game_multiplier,
        "dampened_kelly_fraction": round(f_dampened, 4),
        "bankroll": bankroll,
        "uncapped_suggested_stake": round(uncapped_stake, 2),
        "max_single_position_cap": round(cap_amount, 2),
        "suggested_stake": round(final_stake, 2),
        "suggested_stake_pct_of_bankroll": round(100 * final_stake / bankroll, 2) if bankroll else None,
    }


def _rejected(reason: str) -> dict:
    return {"status": "rejected", "reason": reason}


# ===========================================================================
# SESSION 3.3 -- ARBITRAGE SIZING
# See the "SESSION 3.3 ADDENDUM" section of the module docstring above for
# why this is a genuinely different sizing problem from the pick'em code
# above it, not a variant of the same Kelly math.
# ===========================================================================

# ---------------------------------------------------------------------------
# Reading Session 3.2's flag output
# ---------------------------------------------------------------------------
def _latest_arbitrage_flags_path() -> Optional[Path]:
    pattern = str(ARBITRAGE_FLAGS_DIR / "arbitrage_flags_*.csv")
    matches = sorted(glob.glob(pattern))
    if not matches:
        return None
    return Path(matches[-1])


def load_latest_arbitrage_flags() -> list[dict]:
    """Reads the most recent arbitrage_flags_<timestamp>.csv written by
    detector.py. Raises FileNotFoundError with a clear, actionable message
    if detector.py has never been run -- same "fail loud, not silent"
    posture as load_clv_log() above."""
    path = _latest_arbitrage_flags_path()
    if path is None:
        raise FileNotFoundError(
            f"No arbitrage_flags_*.csv found in {ARBITRAGE_FLAGS_DIR}. "
            f"Run detector.py first (Session 3.2) so there are flagged "
            f"opportunities to size."
        )
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def fetch_arbitrage_flag(market_a: str, market_b: str) -> tuple[Optional[dict], list[str]]:
    """Looks up a specific flagged pair by its two market ids in the
    latest arbitrage_flags_*.csv. market_a/market_b are matched in either
    position, since which venue detector.py labeled 'a' vs. 'b' for a
    given direction is not something the caller should have to know in
    advance. Returns (flag_row_or_None, problems)."""
    try:
        flags = load_latest_arbitrage_flags()
    except FileNotFoundError as exc:
        return None, [str(exc)]

    for row in flags:
        ids = {row.get("market_a"), row.get("market_b")}
        if ids == {market_a, market_b}:
            return row, []

    return None, [
        f"No open flag matching market_a='{market_a}' and market_b='{market_b}' "
        f"found in the latest arbitrage_flags_*.csv. The opportunity may have "
        f"closed, or detector.py needs to be re-run against current data."
    ]


# ---------------------------------------------------------------------------
# Open-positions ledger -- tracks capital already committed at each venue
# ---------------------------------------------------------------------------
def load_open_arbitrage_positions() -> list[dict]:
    """Reads the open-positions ledger. Returns an empty list, not an
    error, if the ledger doesn't exist yet -- a brand-new project has no
    open positions, which is a valid real state, not a missing-file
    problem."""
    if not ARBITRAGE_OPEN_POSITIONS_PATH.exists():
        return []
    with ARBITRAGE_OPEN_POSITIONS_PATH.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def committed_capital_by_venue(open_positions: list[dict]) -> dict[str, float]:
    """Sums capital currently tied up at each venue across every
    still-open position. A single arbitrage position commits capital at
    BOTH its platform_a and platform_b -- see docstring on why this is
    two separate commitments, not one shared amount."""
    committed: dict[str, float] = {"kalshi": 0.0, "polymarket": 0.0}
    for pos in open_positions:
        if pos.get("status") != "open":
            continue
        plat_a = pos.get("platform_a")
        plat_b = pos.get("platform_b")
        if plat_a in committed:
            committed[plat_a] += float(pos.get("capital_committed_a") or 0.0)
        if plat_b in committed:
            committed[plat_b] += float(pos.get("capital_committed_b") or 0.0)
    return committed


def _append_ledger_row(row: dict) -> None:
    ARBITRAGE_OPEN_POSITIONS_PATH.parent.mkdir(parents=True, exist_ok=True)
    file_exists = ARBITRAGE_OPEN_POSITIONS_PATH.exists()
    with ARBITRAGE_OPEN_POSITIONS_PATH.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=ARBITRAGE_LEDGER_FIELDS, extrasaction="ignore")
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)


def record_open_arbitrage_position(sized_result: dict) -> dict:
    """Appends a real, placed arbitrage position to the open-positions
    ledger, using the output of size_arbitrage_position() below. Call
    this only after the human has actually placed both real legs -- this
    project sizes and flags, it does not place bets (see ROADMAP.md's
    standing principle), so this function records a decision the human
    already made, it does not make one."""
    if sized_result.get("status") not in ("sized", "sized_capped"):
        return _rejected(
            f"Refusing to record an open position from a sizing result "
            f"with status='{sized_result.get('status')}' -- only a "
            f"successfully sized result should be recorded as a real, "
            f"placed trade."
        )

    position_id = datetime.now(timezone.utc).strftime("arb_%Y%m%dT%H%M%SZ")
    row = {
        "position_id": position_id,
        "opened_at": datetime.now(timezone.utc).isoformat(),
        "platform_a": sized_result["platform_a"],
        "market_a": sized_result["market_a"],
        "leg_a_side": sized_result.get("leg_a_side"),
        "leg_a_ask": sized_result.get("leg_a_ask"),
        "capital_committed_a": sized_result["capital_required_at_platform_a"],
        "platform_b": sized_result["platform_b"],
        "market_b": sized_result["market_b"],
        "leg_b_side": sized_result.get("leg_b_side"),
        "leg_b_ask": sized_result.get("leg_b_ask"),
        "capital_committed_b": sized_result["capital_required_at_platform_b"],
        "net_profit_per_dollar": sized_result["net_profit_per_dollar"],
        "expected_profit_dollars": sized_result["expected_profit_dollars_if_both_legs_fill"],
        "status": "open",
        "settled_at": "",
        "settlement_note": "",
    }
    _append_ledger_row(row)
    log.info("Recorded open arbitrage position %s: %s", position_id, row)
    return {"status": "recorded", "position_id": position_id, "ledger_row": row}


def settle_arbitrage_position(position_id: str, note: str = "") -> dict:
    """Marks a ledger row as settled, freeing its committed capital back
    up for future sizing. Rewrites the whole ledger file (small file,
    same acceptable pattern as other CSV logs in this project) rather
    than appending, since this is an update to an existing row, not a
    new one."""
    positions = load_open_arbitrage_positions()
    found = False
    for pos in positions:
        if pos.get("position_id") == position_id and pos.get("status") == "open":
            pos["status"] = "settled"
            pos["settled_at"] = datetime.now(timezone.utc).isoformat()
            pos["settlement_note"] = note
            found = True
            break

    if not found:
        return _rejected(
            f"No OPEN position with position_id='{position_id}' found in "
            f"{ARBITRAGE_OPEN_POSITIONS_PATH} -- check the id, or it may "
            f"already be settled."
        )

    with ARBITRAGE_OPEN_POSITIONS_PATH.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=ARBITRAGE_LEDGER_FIELDS, extrasaction="ignore")
        writer.writeheader()
        for pos in positions:
            writer.writerow(pos)

    log.info("Settled arbitrage position %s (note=%r)", position_id, note)
    return {"status": "settled", "position_id": position_id}


# ---------------------------------------------------------------------------
# Arbitrage sizing math
# ---------------------------------------------------------------------------
def size_arbitrage_position(
    flag_row: dict, kalshi_bankroll: float, polymarket_bankroll: float
) -> dict:
    """Runs the full arbitrage sizing pipeline for one flagged pair from
    detector.py and returns a fully-explained result dict, same
    "every intermediate number included" standard as size_entry() above.

    kalshi_bankroll / polymarket_bankroll are real dollars currently
    sitting in each venue's own account -- see docstring for why these
    are two separate numbers, not one combined bankroll.

    UNIT FIX (found via real-data validation, not a design choice made
    up front): detector.py's `fillable_size_dollars` field name is
    misleading. liquidity_check.py's own docstring says plainly that it
    is a CONTRACT COUNT ("a contract count IS a dollar notional amount"
    -- referring to the $1 PAYOUT each contract settles for, not its
    purchase cost). Buying N contracts at an ask price of $0.20 costs
    N * $0.20 in real dollars, not N dollars. Confirmed directly against
    real live Kalshi order-book data this session, e.g. MO-05
    Republican: yes_ask=$0.20, yes_ask_size=15.28 contracts -- the real
    cost to buy all 15.28 is $3.06, not $15.28. The first version of
    this function treated the contract count as if it were already a
    dollar amount, which would have UNDER-committed the sizing math's
    own bankroll caps relative to what a position of that many contracts
    actually costs to buy at low-priced legs, and OVER-stated real
    capital tied up at each venue. This version sizes in CONTRACTS
    throughout and converts to real per-leg dollar cost using each leg's
    own ask price only at the end, where a dollar figure is actually
    needed."""
    platform_a = flag_row.get("platform_a")
    platform_b = flag_row.get("platform_b")

    if platform_a not in ARBITRAGE_SUPPORTED_PLATFORMS or platform_b not in ARBITRAGE_SUPPORTED_PLATFORMS:
        return _rejected(
            f"Unrecognized platform(s) in flag row: platform_a='{platform_a}', "
            f"platform_b='{platform_b}'. Supported: {sorted(ARBITRAGE_SUPPORTED_PLATFORMS)}."
        )

    if platform_a == platform_b:
        return _rejected(
            f"size_arbitrage_position() expects two DIFFERENT venues for capital-"
            f"lockup purposes; got platform_a == platform_b == '{platform_a}' "
            f"(a single-venue YES+NO flag -- both legs are filled at the same "
            f"venue, so this is not a two-venue capital-lockup case; size it as "
            f"a single-venue bankroll check instead, not via this function)."
        )

    if kalshi_bankroll < MIN_ARBITRAGE_BANKROLL or polymarket_bankroll < MIN_ARBITRAGE_BANKROLL:
        return _rejected(
            f"Both --kalshi-bankroll and --polymarket-bankroll must be at least "
            f"{MIN_ARBITRAGE_BANKROLL}, got kalshi={kalshi_bankroll}, "
            f"polymarket={polymarket_bankroll}."
        )

    try:
        ask_a = float(flag_row.get("leg_a_ask"))
        ask_b = float(flag_row.get("leg_b_ask"))
    except (TypeError, ValueError):
        return _rejected(
            f"Flag row is missing a usable leg_a_ask/leg_b_ask -- cannot convert "
            f"contract count to a real dollar cost without both ask prices."
        )
    if ask_a <= 0 or ask_b <= 0:
        return _rejected(f"Flag row has a non-positive ask price (ask_a={ask_a}, ask_b={ask_b}).")

    fillable_contracts = float(flag_row.get("fillable_size_dollars") or 0.0)  # see docstring: really a contract count
    net_profit_per_dollar = float(flag_row.get("net_profit_per_dollar") or 0.0)  # profit per contract

    bankroll_by_venue = {"kalshi": kalshi_bankroll, "polymarket": polymarket_bankroll}
    committed = committed_capital_by_venue(load_open_arbitrage_positions())

    available_a = bankroll_by_venue[platform_a] - committed.get(platform_a, 0.0)
    available_b = bankroll_by_venue[platform_b] - committed.get(platform_b, 0.0)

    total_bankroll = kalshi_bankroll + polymarket_bankroll
    max_capital_by_pct = total_bankroll * MAX_ARBITRAGE_POSITION_PCT
    gross_cost_per_contract = ask_a + ask_b  # real total $ cost to buy one contract on each leg

    # Every candidate below is expressed in CONTRACTS, so they compare on
    # the same footing as fillable_contracts -- real dollar limits are
    # divided by the relevant real price first.
    contract_candidates = {
        "fillable_contracts": fillable_contracts,
        f"available_capital_{platform_a}": available_a / ask_a,
        f"available_capital_{platform_b}": available_b / ask_b,
        "max_position_pct_cap": max_capital_by_pct / gross_cost_per_contract,
    }
    binding_constraint = min(contract_candidates, key=contract_candidates.get)
    raw_contracts = max(contract_candidates[binding_constraint], 0.0)

    if raw_contracts <= 0:
        return _rejected(
            f"Sized position is 0 contracts -- binding constraint was "
            f"'{binding_constraint}' ({contract_candidates[binding_constraint]:.4f}). "
            f"Committed capital so far: {committed}."
        )

    # Tier selection uses the market's own real fillable_contracts (order-
    # book depth), not raw_contracts -- a position capped small by our
    # OWN bankroll isn't the same real-world condition as a market that's
    # actually thin, and the buffer is meant to reflect the latter. See
    # execution_risk_buffer_for_depth()'s docstring for the real evidence.
    execution_risk_buffer = execution_risk_buffer_for_depth(fillable_contracts)
    buffered_contracts = round(raw_contracts * execution_risk_buffer, 4)
    was_capped = binding_constraint != "fillable_contracts"

    capital_a = round(buffered_contracts * ask_a, 2)
    capital_b = round(buffered_contracts * ask_b, 2)
    expected_profit_dollars = round(buffered_contracts * net_profit_per_dollar, 2)

    return {
        "status": "sized_capped" if was_capped else "sized",
        "opportunity_type": flag_row.get("opportunity_type"),
        "platform_a": platform_a,
        "market_a": flag_row.get("market_a"),
        "leg_a_side": flag_row.get("leg_a_side"),
        "leg_a_ask": ask_a,
        "platform_b": platform_b,
        "market_b": flag_row.get("market_b"),
        "leg_b_side": flag_row.get("leg_b_side"),
        "leg_b_ask": ask_b,
        "net_profit_per_dollar": net_profit_per_dollar,
        "fillable_contracts": fillable_contracts,
        "kalshi_bankroll": kalshi_bankroll,
        "polymarket_bankroll": polymarket_bankroll,
        "committed_capital_kalshi": round(committed.get("kalshi", 0.0), 2),
        "committed_capital_polymarket": round(committed.get("polymarket", 0.0), 2),
        "available_capital_platform_a": round(available_a, 2),
        "available_capital_platform_b": round(available_b, 2),
        "max_position_pct_cap_dollars": round(max_capital_by_pct, 2),
        "binding_constraint": binding_constraint,
        "raw_contracts_before_execution_buffer": round(raw_contracts, 4),
        "execution_risk_buffer_applied": execution_risk_buffer,
        "suggested_contracts": buffered_contracts,
        "capital_required_at_platform_a": capital_a,
        "capital_required_at_platform_b": capital_b,
        "capital_required_total_across_both_venues": round(capital_a + capital_b, 2),
        "expected_profit_dollars_if_both_legs_fill": expected_profit_dollars,
        "liquidity_sufficient": flag_row.get("liquidity_sufficient"),
        "legal_footprint_status": flag_row.get("legal_footprint_status"),
    }


def run_arbitrage_sizing(
    market_a: str, market_b: str, kalshi_bankroll: float, polymarket_bankroll: float
) -> dict:
    log.info(
        "=== Arbitrage sizing run starting: market_a=%s, market_b=%s, "
        "kalshi_bankroll=%s, polymarket_bankroll=%s ===",
        market_a, market_b, kalshi_bankroll, polymarket_bankroll,
    )
    flag_row, problems = fetch_arbitrage_flag(market_a, market_b)
    if problems:
        result = _rejected("; ".join(problems))
        log.warning("Arbitrage sizing request rejected: %s", result["reason"])
        return result

    result = size_arbitrage_position(flag_row, kalshi_bankroll, polymarket_bankroll)
    log.info("Arbitrage sizing result: %s", result)
    return result


# ===========================================================================
# SESSION 5.4 -- POLITICS (DOWN-BALLOT) SIZING
# See the "SESSION 5.4 ADDENDUM" section of the module docstring above for
# why this is a third, distinct sizing shape (single-leg Kelly, like
# arbitrage's per-leg mechanics, but a genuine probabilistic bet, like
# pick'em -- combined with a long-capital-lockup adjustment neither of
# those tracks needs).
# ===========================================================================

def load_politics_clv_log() -> pd.DataFrame:
    if not POLITICS_CLV_LOG_PATH.exists():
        raise FileNotFoundError(
            f"{POLITICS_CLV_LOG_PATH} not found. Run clv_logger.py --track politics "
            f"first (Session 5.3) so there are flagged opportunities to size."
        )
    return pd.read_csv(POLITICS_CLV_LOG_PATH)


def fetch_politics_flag(flag_id: str) -> tuple[Optional[dict], list[str]]:
    """Looks up one flag_id (venue|race_id|party, per Session 5.3's own
    scheme) in the live politics CLV log. Returns (flag_row_or_None,
    problems), same "always say exactly why" posture as fetch_legs()
    above."""
    try:
        clv_df = load_politics_clv_log()
    except FileNotFoundError as exc:
        return None, [str(exc)]

    matches = clv_df.loc[clv_df["flag_id"] == flag_id]
    if len(matches) == 0:
        return None, [f"flag_id '{flag_id}' not found in {POLITICS_CLV_LOG_PATH}"]

    row = matches.iloc[0].to_dict()
    if row.get("status") != "open":
        return None, [
            f"flag_id '{flag_id}' has status='{row.get('status')}', not 'open' "
            f"-- this position is no longer available (race likely settled/delisted)."
        ]

    for required in ("first_flagged_model_prob", "first_flagged_market_price", "hours_to_resolution"):
        if row.get(required) is None or pd.isna(row.get(required)):
            return None, [f"flag_id '{flag_id}' has no {required} logged."]

    return row, []


def politics_lockup_dampener(hours_to_resolution: float) -> float:
    """Looks up the stated, conservative step-function dampener for a
    given hours_to_resolution -- see POLITICS_LOCKUP_DAMPENER_TABLE and
    the docstring's "CAPITAL-LOCKUP DAMPENER" section for why this is a
    named judgment call, not a derived rate."""
    for max_hours, multiplier in POLITICS_LOCKUP_DAMPENER_TABLE:
        if hours_to_resolution <= max_hours:
            return multiplier
    return POLITICS_LOCKUP_DAMPENER_TABLE[-1][1]  # unreachable given the inf band, kept defensive


def raw_kelly_fraction_binary_contract(p: float, price: float) -> float:
    """Kelly for a single binary contract bought at `price` (0 < price < 1),
    paying $1 if the flagged side resolves YES. Net odds
    b = (1 - price) / price (profit per $1 staked on a win); this is
    algebraically the same f* = (p*(b+1) - 1) / b formula used elsewhere in
    this file, just expressed directly in terms of price so callers never
    need to separately compute b themselves. Can be negative (no real
    edge) -- callers must floor at 0, never bet a negative fraction."""
    if not (0.0 < price < 1.0):
        raise ValueError(f"price must be strictly between 0 and 1, got {price}")
    b = (1.0 - price) / price
    return raw_kelly_fraction(p, b)


def load_open_politics_positions() -> list[dict]:
    """Reads the portfolio-level open-positions ledger. Returns an empty
    list, not an error, if the ledger doesn't exist yet -- same posture as
    load_open_arbitrage_positions()."""
    if not POLITICS_OPEN_POSITIONS_PATH.exists():
        return []
    with POLITICS_OPEN_POSITIONS_PATH.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def committed_capital_politics(open_positions: list[dict], venue: Optional[str] = None) -> float:
    """Sums capital currently locked across every still-open politics
    position. If `venue` is given, sums only that venue's positions
    (matching the single-venue bankroll figure a user actually has sitting
    at that venue); with venue=None, sums ALL open positions across every
    venue -- this is the number POLITICS_MAX_TOTAL_EXPOSURE_PCT is checked
    against, since that cap is deliberately venue-agnostic (see docstring:
    it exists to catch many simultaneous long-dated positions overlapping,
    regardless of which venue each one sits at)."""
    total = 0.0
    for pos in open_positions:
        if pos.get("status") != "open":
            continue
        if venue is not None and pos.get("venue") != venue:
            continue
        total += float(pos.get("capital_committed") or 0.0)
    return total


def size_politics_position(flag_row: dict, venue_bankroll: float, total_bankroll: float) -> dict:
    """Runs the full single-contract Kelly sizing pipeline for one flagged
    politics position and returns a fully-explained result dict, same
    "every intermediate number included" standard as size_entry() and
    size_arbitrage_position() above.

    venue_bankroll: real dollars currently sitting at the flag's own venue
    (Kalshi or Polymarket) -- checked against the single-position cap.
    total_bankroll: the user's combined bankroll across all venues/tracks
    -- checked against POLITICS_MAX_TOTAL_EXPOSURE_PCT together with every
    other currently-open politics position (see docstring)."""
    venue = flag_row.get("venue")
    if venue not in POLITICS_SUPPORTED_VENUES:
        return _rejected(
            f"Unrecognized venue '{venue}' in flag row -- supported: "
            f"{sorted(POLITICS_SUPPORTED_VENUES)}."
        )

    if venue_bankroll < MIN_POLITICS_BANKROLL or total_bankroll < MIN_POLITICS_BANKROLL:
        return _rejected(
            f"--venue-bankroll and --total-bankroll must both be at least "
            f"{MIN_POLITICS_BANKROLL}, got venue_bankroll={venue_bankroll}, "
            f"total_bankroll={total_bankroll}."
        )

    p = float(flag_row["first_flagged_model_prob"])
    price = float(flag_row["first_flagged_market_price"])
    hours_to_resolution = float(flag_row["hours_to_resolution"])

    try:
        f_raw = raw_kelly_fraction_binary_contract(p, price)
    except ValueError as exc:
        return _rejected(str(exc))

    f_quarter = max(f_raw, 0.0) * KELLY_FRACTION  # reuses the project-wide quarter-Kelly constant

    dampener = politics_lockup_dampener(hours_to_resolution)
    f_dampened = f_quarter * dampener

    open_positions = load_open_politics_positions()
    committed_at_venue = committed_capital_politics(open_positions, venue=venue)
    committed_total = committed_capital_politics(open_positions, venue=None)

    available_at_venue = venue_bankroll - committed_at_venue
    single_position_cap = venue_bankroll * POLITICS_MAX_SINGLE_POSITION_PCT
    total_exposure_cap = total_bankroll * POLITICS_MAX_TOTAL_EXPOSURE_PCT
    remaining_exposure_room = total_exposure_cap - committed_total

    uncapped_stake = venue_bankroll * f_dampened
    binding_candidates = {
        "uncapped_kelly_stake": uncapped_stake,
        "single_position_cap": single_position_cap,
        "available_capital_at_venue": max(available_at_venue, 0.0),
        "remaining_total_exposure_room": max(remaining_exposure_room, 0.0),
    }
    binding_constraint = min(binding_candidates, key=binding_candidates.get)
    final_stake = round(max(binding_candidates[binding_constraint], 0.0), 2)

    if f_raw <= 0:
        status = "no_bet_negative_edge"
        final_stake = 0.0
        binding_constraint = "negative_edge"
    elif binding_constraint != "uncapped_kelly_stake":
        status = "sized_capped"
    else:
        status = "sized"

    return {
        "status": status,
        "flag_id": flag_row.get("flag_id"),
        "venue": venue,
        "race_id": flag_row.get("race_id"),
        "party": flag_row.get("party"),
        "candidate_name": flag_row.get("candidate_name"),
        "model_prob": round(p, 4),
        "market_price": round(price, 4),
        "hours_to_resolution": hours_to_resolution,
        "raw_kelly_fraction": round(f_raw, 4),
        "quarter_kelly_fraction": round(f_quarter, 4),
        "lockup_dampener_applied": dampener,
        "dampened_kelly_fraction": round(f_dampened, 4),
        "venue_bankroll": venue_bankroll,
        "total_bankroll": total_bankroll,
        "committed_capital_at_venue": round(committed_at_venue, 2),
        "committed_capital_total_all_venues": round(committed_total, 2),
        "single_position_cap": round(single_position_cap, 2),
        "total_exposure_cap": round(total_exposure_cap, 2),
        "binding_constraint": binding_constraint,
        "uncapped_suggested_stake": round(uncapped_stake, 2),
        "suggested_stake": final_stake,
        "suggested_stake_pct_of_venue_bankroll": round(100 * final_stake / venue_bankroll, 2) if venue_bankroll else None,
    }


def _append_politics_ledger_row(row: dict) -> None:
    POLITICS_OPEN_POSITIONS_PATH.parent.mkdir(parents=True, exist_ok=True)
    file_exists = POLITICS_OPEN_POSITIONS_PATH.exists()
    with POLITICS_OPEN_POSITIONS_PATH.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=POLITICS_LEDGER_FIELDS, extrasaction="ignore")
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)


def record_open_politics_position(sized_result: dict) -> dict:
    """Appends a real, placed politics position to the portfolio-level
    open-positions ledger. Call this only after the human has actually
    placed the real trade -- this project sizes and flags, it does not
    place bets (ROADMAP.md's standing principle), so this function records
    a decision the human already made, it does not make one."""
    if sized_result.get("status") not in ("sized", "sized_capped"):
        return _rejected(
            f"Refusing to record an open position from a sizing result "
            f"with status='{sized_result.get('status')}' -- only a "
            f"successfully sized result should be recorded as a real, "
            f"placed trade."
        )

    position_id = datetime.now(timezone.utc).strftime("pol_%Y%m%dT%H%M%SZ")
    row = {
        "position_id": position_id,
        "opened_at": datetime.now(timezone.utc).isoformat(),
        "venue": sized_result["venue"],
        "race_id": sized_result["race_id"],
        "party": sized_result["party"],
        "flag_id": sized_result["flag_id"],
        "candidate_name": sized_result.get("candidate_name"),
        "hours_to_resolution_at_open": sized_result["hours_to_resolution"],
        "capital_committed": sized_result["suggested_stake"],
        "status": "open",
        "settled_at": "",
        "settlement_note": "",
    }
    _append_politics_ledger_row(row)
    log.info("Recorded open politics position %s: %s", position_id, row)
    return {"status": "recorded", "position_id": position_id, "ledger_row": row}


def settle_politics_position(position_id: str, note: str = "") -> dict:
    """Marks a ledger row as settled, freeing its committed capital back
    up -- same rewrite-whole-file pattern as settle_arbitrage_position()."""
    positions = load_open_politics_positions()
    found = False
    for pos in positions:
        if pos.get("position_id") == position_id and pos.get("status") == "open":
            pos["status"] = "settled"
            pos["settled_at"] = datetime.now(timezone.utc).isoformat()
            pos["settlement_note"] = note
            found = True
            break

    if not found:
        return _rejected(
            f"No OPEN position with position_id='{position_id}' found in "
            f"{POLITICS_OPEN_POSITIONS_PATH} -- check the id, or it may "
            f"already be settled."
        )

    with POLITICS_OPEN_POSITIONS_PATH.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=POLITICS_LEDGER_FIELDS, extrasaction="ignore")
        writer.writeheader()
        for pos in positions:
            writer.writerow(pos)

    log.info("Settled politics position %s (note=%r)", position_id, note)
    return {"status": "settled", "position_id": position_id}


def run_politics_sizing(flag_id: str, venue_bankroll: float, total_bankroll: float) -> dict:
    log.info(
        "=== Politics sizing run starting: flag_id=%s, venue_bankroll=%s, total_bankroll=%s ===",
        flag_id, venue_bankroll, total_bankroll,
    )
    flag_row, problems = fetch_politics_flag(flag_id)
    if problems:
        result = _rejected("; ".join(problems))
        log.warning("Politics sizing request rejected: %s", result["reason"])
        return result

    result = size_politics_position(flag_row, venue_bankroll, total_bankroll)
    log.info("Politics sizing result: %s", result)
    return result


# ===========================================================================
# SESSION 6.4 -- SPORTSBOOK PLAYER PROPS (DK/FD) SIZING
# See the "SESSION 6.4 ADDENDUM" section of the module docstring above for
# why this reuses politics' single-contract Kelly math directly but adds
# its own, distinct account-limiting-risk dampener (the actual point of
# this session, per ROADMAP.md's own card title).
# ===========================================================================

def load_props_clv_log() -> pd.DataFrame:
    if not PROPS_CLV_LOG_PATH.exists():
        raise FileNotFoundError(
            f"{PROPS_CLV_LOG_PATH} not found. Run clv_logger.py --track props "
            f"first (Session 6.3) so there are flagged opportunities to size."
        )
    return pd.read_csv(PROPS_CLV_LOG_PATH)


def fetch_props_flag(flag_id: str) -> tuple[Optional[dict], list[str]]:
    """Looks up one flag_id (platform|source_selection_id, per Session
    6.3's own scheme) in the live props CLV log. Returns
    (flag_row_or_None, problems), same "always say exactly why" posture
    as fetch_legs()/fetch_politics_flag() above."""
    try:
        clv_df = load_props_clv_log()
    except FileNotFoundError as exc:
        return None, [str(exc)]

    matches = clv_df.loc[clv_df["flag_id"] == flag_id]
    if len(matches) == 0:
        return None, [f"flag_id '{flag_id}' not found in {PROPS_CLV_LOG_PATH}"]

    row = matches.iloc[0].to_dict()
    if row.get("status") != "open":
        return None, [
            f"flag_id '{flag_id}' has status='{row.get('status')}', not 'open' "
            f"-- this position is no longer available (game likely locked/prop delisted)."
        ]

    for required in ("first_flagged_model_prob", "first_flagged_market_price", "platform"):
        if row.get(required) is None or pd.isna(row.get(required)):
            return None, [f"flag_id '{flag_id}' has no {required} logged."]

    return row, []


def size_props_position(flag_row: dict, bankroll: float) -> dict:
    """Runs the full single-contract Kelly sizing pipeline for one flagged
    sportsbook prop and returns a fully-explained result dict, same
    "every intermediate number included" standard as every other sizing
    function in this file. Reuses `raw_kelly_fraction_binary_contract`
    directly (same probabilistic-single-contract shape as politics'
    sizing) -- see docstring for why the actual new work here is the
    account-limiting-risk dampener, not the Kelly math."""
    platform = flag_row.get("platform")
    if platform not in PROPS_SUPPORTED_PLATFORMS:
        return _rejected(
            f"Unrecognized platform '{platform}' in flag row -- supported: "
            f"{sorted(PROPS_SUPPORTED_PLATFORMS)}."
        )

    if bankroll < MIN_PROPS_BANKROLL:
        return _rejected(f"--bankroll must be at least {MIN_PROPS_BANKROLL}, got {bankroll}.")

    p = float(flag_row["first_flagged_model_prob"])
    price = float(flag_row["first_flagged_market_price"])

    try:
        f_raw = raw_kelly_fraction_binary_contract(p, price)
    except ValueError as exc:
        return _rejected(str(exc))

    f_quarter = max(f_raw, 0.0) * KELLY_FRACTION  # reuses the project-wide quarter-Kelly constant

    limiting_dampener = PROPS_PLATFORM_RISK_MULTIPLIER[platform]

    field_vig_unresolved = bool(flag_row.get("implied_prob_includes_field_vig"))
    field_vig_multiplier = PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER if field_vig_unresolved else 1.0

    f_dampened = f_quarter * limiting_dampener * field_vig_multiplier

    uncapped_stake = bankroll * f_dampened
    cap_amount = bankroll * PROPS_MAX_SINGLE_POSITION_PCT
    capped = uncapped_stake > cap_amount
    final_stake = min(uncapped_stake, cap_amount)

    if f_raw <= 0:
        status = "no_bet_negative_edge"
        final_stake = 0.0
    elif capped:
        status = "sized_capped_at_max_position"
    else:
        status = "sized"

    return {
        "status": status,
        "flag_id": flag_row.get("flag_id"),
        "platform": platform,
        "player_name": flag_row.get("player_name"),
        "sport": flag_row.get("sport"),
        "stat_type": flag_row.get("stat_type"),
        "prop_category": flag_row.get("prop_category"),
        "flagged_side": flag_row.get("flagged_side"),
        "model_prob": round(p, 4),
        "market_price": round(price, 4),
        "raw_kelly_fraction": round(f_raw, 4),
        "quarter_kelly_fraction": round(f_quarter, 4),
        "platform_limiting_risk_multiplier_applied": limiting_dampener,
        "field_vig_unresolved": field_vig_unresolved,
        "field_vig_unresolved_multiplier_applied": field_vig_multiplier,
        "dampened_kelly_fraction": round(f_dampened, 4),
        "bankroll": bankroll,
        "uncapped_suggested_stake": round(uncapped_stake, 2),
        "max_single_position_cap": round(cap_amount, 2),
        "suggested_stake": round(final_stake, 2),
        "suggested_stake_pct_of_bankroll": round(100 * final_stake / bankroll, 2) if bankroll else None,
    }


def run_props_sizing(flag_id: str, bankroll: float) -> dict:
    log.info("=== Props sizing run starting: flag_id=%s, bankroll=%s ===", flag_id, bankroll)
    flag_row, problems = fetch_props_flag(flag_id)
    if problems:
        result = _rejected("; ".join(problems))
        log.warning("Props sizing request rejected: %s", result["reason"])
        return result

    result = size_props_position(flag_row, bankroll)
    log.info("Props sizing result: %s", result)
    return result


# ===========================================================================
# SESSION 4.4 -- WEATHER (KALSHI) SIZING
# See the "SESSION 4.4 ADDENDUM" section of the module docstring above for
# why this reuses politics/props' single-contract Kelly math directly but
# adds Kalshi's real, sourced trading fee into the effective cost per
# contract, rather than a named flat dampener.
# ===========================================================================

def kalshi_fee_per_contract(price: float) -> float:
    """Kalshi's published general fee formula, applied at contract
    count = 1 -- see docstring for why a single-contract sizing call uses
    the per-contract rate rather than the real order-level rounded fee
    (which depends on a total contract count this function is trying to
    determine). fee = round_up_to_cent(0.07 * price * (1 - price)) for
    one contract."""
    import math
    raw_fee = KALSHI_FEE_RATE * price * (1.0 - price)
    return math.ceil(raw_fee * 100.0) / 100.0


def kalshi_effective_cost_per_contract(price: float) -> float:
    """Real, all-in cost to acquire one contract at `price`, including
    Kalshi's own trading fee -- see docstring's "WHY THE FEE IS FOLDED
    INTO THE EFFECTIVE COST" section for why this is passed into Kelly
    directly rather than applied as a post-hoc multiplier."""
    return price + kalshi_fee_per_contract(price)


def load_weather_clv_log() -> pd.DataFrame:
    if not WEATHER_CLV_LOG_PATH.exists():
        raise FileNotFoundError(
            f"{WEATHER_CLV_LOG_PATH} not found. Run clv_logger.py --track weather "
            f"first (Session 4.3) so there are flagged opportunities to size."
        )
    return pd.read_csv(WEATHER_CLV_LOG_PATH)


def fetch_weather_flag(flag_id: str) -> tuple[Optional[dict], list[str]]:
    """Looks up one flag_id (the contract's own market_ticker, per
    Session 4.3's own scheme) in the live weather CLV log. Returns
    (flag_row_or_None, problems), same "always say exactly why" posture
    as every other fetch_*_flag() in this file."""
    try:
        clv_df = load_weather_clv_log()
    except FileNotFoundError as exc:
        return None, [str(exc)]

    matches = clv_df.loc[clv_df["flag_id"] == flag_id]
    if len(matches) == 0:
        return None, [f"flag_id '{flag_id}' not found in {WEATHER_CLV_LOG_PATH}"]

    row = matches.iloc[0].to_dict()
    if row.get("status") != "open":
        return None, [
            f"flag_id '{flag_id}' has status='{row.get('status')}', not 'open' "
            f"-- this contract is no longer available (likely settled/delisted)."
        ]

    for required in ("first_flagged_model_prob", "first_flagged_market_price", "flagged_side"):
        if row.get(required) is None or pd.isna(row.get(required)):
            return None, [f"flag_id '{flag_id}' has no {required} logged."]

    if row.get("flagged_side") not in WEATHER_SUPPORTED_SIDES:
        return None, [
            f"flag_id '{flag_id}' has flagged_side='{row.get('flagged_side')}' -- "
            f"expected one of {sorted(WEATHER_SUPPORTED_SIDES)}."
        ]

    return row, []


def size_weather_position(flag_row: dict, bankroll: float) -> dict:
    """Runs the full single-contract Kelly sizing pipeline for one
    flagged Kalshi weather contract, with Kalshi's real trading fee
    folded into the effective per-contract cost (see docstring) rather
    than applied as a flat post-hoc dampener. Same "every intermediate
    number included" standard as every other sizing function in this
    file."""
    if bankroll < MIN_WEATHER_BANKROLL:
        return _rejected(f"--bankroll must be at least {MIN_WEATHER_BANKROLL}, got {bankroll}.")

    p = float(flag_row["first_flagged_model_prob"])
    price = float(flag_row["first_flagged_market_price"])

    if not (0.0 < price < 1.0):
        return _rejected(f"first_flagged_market_price must be strictly between 0 and 1, got {price}.")

    fee_per_contract = kalshi_fee_per_contract(price)
    effective_cost = kalshi_effective_cost_per_contract(price)

    try:
        f_raw = raw_kelly_fraction_binary_contract(p, effective_cost)
    except ValueError as exc:
        return _rejected(str(exc))

    f_quarter = max(f_raw, 0.0) * KELLY_FRACTION  # reuses the project-wide quarter-Kelly constant

    uncapped_stake = bankroll * f_quarter
    cap_amount = bankroll * WEATHER_MAX_SINGLE_POSITION_PCT
    capped = uncapped_stake > cap_amount
    final_stake = min(uncapped_stake, cap_amount)

    if f_raw <= 0:
        status = "no_bet_negative_edge"
        final_stake = 0.0
    elif capped:
        status = "sized_capped_at_max_position"
    else:
        status = "sized"

    return {
        "status": status,
        "flag_id": flag_row.get("flag_id"),
        "flagged_side": flag_row.get("flagged_side"),
        "city_label": flag_row.get("city_label"),
        "target_date": flag_row.get("target_date"),
        "lead_days": flag_row.get("lead_days"),
        "model_prob": round(p, 4),
        "market_price": round(price, 4),
        "kalshi_fee_rate": KALSHI_FEE_RATE,
        "fee_per_contract": round(fee_per_contract, 4),
        "effective_cost_per_contract": round(effective_cost, 4),
        "raw_kelly_fraction": round(f_raw, 4),
        "quarter_kelly_fraction": round(f_quarter, 4),
        "bankroll": bankroll,
        "uncapped_suggested_stake": round(uncapped_stake, 2),
        "max_single_position_cap": round(cap_amount, 2),
        "suggested_stake": round(final_stake, 2),
        "suggested_stake_pct_of_bankroll": round(100 * final_stake / bankroll, 2) if bankroll else None,
    }


def run_weather_sizing(flag_id: str, bankroll: float) -> dict:
    log.info("=== Weather sizing run starting: flag_id=%s, bankroll=%s ===", flag_id, bankroll)
    flag_row, problems = fetch_weather_flag(flag_id)
    if problems:
        result = _rejected("; ".join(problems))
        log.warning("Weather sizing request rejected: %s", result["reason"])
        return result

    result = size_weather_position(flag_row, bankroll)
    log.info("Weather sizing result: %s", result)
    return result


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
def run(flag_ids: list[str], bankroll: float) -> dict:
    log.info("=== Sizing run starting: flag_ids=%s, bankroll=%s ===", flag_ids, bankroll)
    legs, problems = fetch_legs(flag_ids)

    if problems:
        result = _rejected("; ".join(problems))
        log.warning("Sizing request rejected: %s", result["reason"])
        return result

    result = size_entry(legs, bankroll)
    log.info("Sizing result: %s", result)
    return result


if __name__ == "__main__":
    import json

    parser = argparse.ArgumentParser(
        description="Session 2.6 pick'em sizing and Session 3.3 arbitrage sizing."
    )
    subparsers = parser.add_subparsers(dest="mode", required=True)

    # -- pickem (Session 2.6, unchanged behavior, now under a subcommand) --
    pickem_parser = subparsers.add_parser(
        "pickem",
        help="Size an all-or-nothing pick'em entry (PrizePicks Power Play or "
        "Underdog Standard) from data/pickem/clv_log.csv.",
    )
    pickem_parser.add_argument(
        "--flag-ids",
        type=str,
        nargs="+",
        required=True,
        help="2 or more flag_id values from data/pickem/clv_log.csv, all from the "
        "SAME platform, at a leg count that platform has a sourced payout for "
        f"(PrizePicks: {sorted(PICKEM_ENTRY_PAYOUT['prizepicks'])}; Underdog: "
        f"{sorted(PICKEM_ENTRY_PAYOUT['underdog'])}) (e.g. --flag-ids "
        f'"prizepicks|123" "prizepicks|456").',
    )
    pickem_parser.add_argument(
        "--bankroll", type=float, required=True, help="Total real bankroll available, in dollars."
    )

    # -- arbitrage (Session 3.3, new) --
    arb_parser = subparsers.add_parser(
        "arbitrage", help="Size, record, or settle an arbitrage position from detector.py's flags."
    )
    arb_subparsers = arb_parser.add_subparsers(dest="action", required=True)

    arb_size = arb_subparsers.add_parser(
        "size", help="Compute a suggested position size for one flagged pair."
    )
    arb_size.add_argument("--market-a", type=str, required=True, help="market_a or market_b id from the flag.")
    arb_size.add_argument("--market-b", type=str, required=True, help="The other market id from the flag.")
    arb_size.add_argument(
        "--kalshi-bankroll", type=float, required=True, help="Real dollars currently in the Kalshi account."
    )
    arb_size.add_argument(
        "--polymarket-bankroll", type=float, required=True, help="Real dollars currently in the Polymarket account."
    )

    arb_record = arb_subparsers.add_parser(
        "record-open",
        help="Size a flagged pair AND record it as a real, placed open position in the ledger.",
    )
    arb_record.add_argument("--market-a", type=str, required=True)
    arb_record.add_argument("--market-b", type=str, required=True)
    arb_record.add_argument("--kalshi-bankroll", type=float, required=True)
    arb_record.add_argument("--polymarket-bankroll", type=float, required=True)

    arb_settle = arb_subparsers.add_parser(
        "settle", help="Mark an open position as settled, freeing its committed capital."
    )
    arb_settle.add_argument("--position-id", type=str, required=True)
    arb_settle.add_argument("--note", type=str, default="", help="Optional free-text settlement note.")

    # -- politics (Session 5.4, new) --
    politics_parser = subparsers.add_parser(
        "politics", help="Size, record, or settle a down-ballot politics position from clv_logger.py's flags."
    )
    politics_subparsers = politics_parser.add_subparsers(dest="action", required=True)

    politics_size = politics_subparsers.add_parser(
        "size", help="Compute a suggested position size for one flagged politics position."
    )
    politics_size.add_argument(
        "--flag-id", type=str, required=True,
        help='flag_id from data/politics/clv_log.csv (venue|race_id|party, e.g. "kalshi|MO-05|R").',
    )
    politics_size.add_argument(
        "--venue-bankroll", type=float, required=True, help="Real dollars currently in that flag's own venue account."
    )
    politics_size.add_argument(
        "--total-bankroll", type=float, required=True,
        help="Real combined bankroll across all venues/tracks -- checked against the portfolio-level exposure cap.",
    )

    politics_record = politics_subparsers.add_parser(
        "record-open",
        help="Size a flagged position AND record it as a real, placed open position in the ledger.",
    )
    politics_record.add_argument("--flag-id", type=str, required=True)
    politics_record.add_argument("--venue-bankroll", type=float, required=True)
    politics_record.add_argument("--total-bankroll", type=float, required=True)

    politics_settle = politics_subparsers.add_parser(
        "settle", help="Mark an open politics position as settled, freeing its committed capital."
    )
    politics_settle.add_argument("--position-id", type=str, required=True)
    politics_settle.add_argument("--note", type=str, default="", help="Optional free-text settlement note.")

    # -- props (Session 6.4, new) --
    props_parser = subparsers.add_parser(
        "props", help="Size a flagged DK/FD sportsbook player prop from clv_logger.py's --track props flags."
    )
    props_subparsers = props_parser.add_subparsers(dest="action", required=True)

    props_size = props_subparsers.add_parser(
        "size", help="Compute a suggested position size for one flagged prop, with an account-limiting-risk dampener applied."
    )
    props_size.add_argument(
        "--flag-id", type=str, required=True,
        help='flag_id from data/sportsbook_props/clv_log.csv (platform|source_selection_id, e.g. "draftkings|1234567890").',
    )
    props_size.add_argument(
        "--bankroll", type=float, required=True, help="Real dollars currently in that flag's own sportsbook account."
    )

    # -- weather (Session 4.4, new) --
    weather_parser = subparsers.add_parser(
        "weather", help="Size a flagged Kalshi weather contract from clv_logger.py's --track weather flags."
    )
    weather_subparsers = weather_parser.add_subparsers(dest="action", required=True)

    weather_size = weather_subparsers.add_parser(
        "size", help="Compute a suggested position size for one flagged weather contract, with Kalshi's real trading fee folded in."
    )
    weather_size.add_argument(
        "--flag-id", type=str, required=True,
        help='flag_id from data/weather/clv_log.csv (the contract\'s own market_ticker, e.g. "KXHIGHNY-26SEP07-T77").',
    )
    weather_size.add_argument(
        "--bankroll", type=float, required=True, help="Real dollars currently in the Kalshi account."
    )

    args = parser.parse_args()

    if args.mode == "pickem":
        summary = run(args.flag_ids, args.bankroll)
        print(summary)

    elif args.mode == "arbitrage":
        if args.action in ("size", "record-open"):
            result = run_arbitrage_sizing(
                args.market_a, args.market_b, args.kalshi_bankroll, args.polymarket_bankroll
            )
            if args.action == "record-open" and result.get("status") in ("sized", "sized_capped"):
                record_result = record_open_arbitrage_position(result)
                result["ledger_record"] = record_result
            print(json.dumps(result, indent=2, default=str))

        elif args.action == "settle":
            result = settle_arbitrage_position(args.position_id, args.note)
            print(json.dumps(result, indent=2, default=str))

    elif args.mode == "politics":
        if args.action in ("size", "record-open"):
            result = run_politics_sizing(args.flag_id, args.venue_bankroll, args.total_bankroll)
            if args.action == "record-open" and result.get("status") in ("sized", "sized_capped"):
                record_result = record_open_politics_position(result)
                result["ledger_record"] = record_result
            print(json.dumps(result, indent=2, default=str))

        elif args.action == "settle":
            result = settle_politics_position(args.position_id, args.note)
            print(json.dumps(result, indent=2, default=str))

    elif args.mode == "props":
        if args.action == "size":
            result = run_props_sizing(args.flag_id, args.bankroll)
            print(json.dumps(result, indent=2, default=str))

    elif args.mode == "weather":
        if args.action == "size":
            result = run_weather_sizing(args.flag_id, args.bankroll)
            print(json.dumps(result, indent=2, default=str))
