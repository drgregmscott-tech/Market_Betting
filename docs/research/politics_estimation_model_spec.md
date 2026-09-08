# Down-Ballot Politics Estimation Model — Spec (Session 5.2)

Documented at the same specificity level as `weather_estimation_model_spec.md`
(Session 4.2) and `pickem_estimation_model_spec.md` (Session 2.3): every
input, every formula, every named constant and its evidence basis, and
every stated gap.

## What this model answers

For every real, live Kalshi/Polymarket down-ballot candidate market
Session 5.1c ingests (one row per race, matched to a specific named
Democratic or Republican candidate — see `schema_politics.py`'s module
docstring for how that matching works and why it was added this
session), this model computes this project's own corrected probability
estimate that the candidate wins, so it can be compared against the
venue's own raw price.

## Required re-verification step (ROADMAP.md gate) — result

ROADMAP.md required the underconfidence finding be re-checked against
current, independent sources before being built into a model, given the
original Session 0.1 research flagged the key paper as an unreviewed
preprint with a data-count discrepancy, and a related study's methodology
as publicly disputed by Kalshi.

**Checked live, 2026-09-08.** The paper (Le, 2026, "Decomposing Crowd
Wisdom: Domain-Specific Calibration Dynamics in Prediction Markets,"
arXiv:2602.19520) is now at v2 (August 2026), and its own text shows it
has been through a formal review round ("As one reviewer noted...", a
new Bayesian measurement-error section added specifically in response).
The revision adds a hierarchical model that treats every first-stage
calibration slope as uncertain rather than exact, and propagates that
uncertainty into the headline finding. Result: political-market
underconfidence survives this stricter check — the model's 95% credible
interval for the Politics domain effect is entirely above zero
([0.062, 0.152]), and the same pattern replicates independently on
Polymarket (mean slope 1.45 across reliable horizons). The finding's
*magnitude* shrinks under the stricter check (posterior mean effect
0.107 vs. the raw descriptive estimate 0.156 — roughly a 31% reduction),
which this model treats as a real, sourced correction to lean into, not
a reason to discard the finding (see "Dampening factor" below).

**Decision:** the underconfidence finding is confirmed as real and
statistically robust, and is built into this model at a deliberately
damped strength given the paper's own downward revision — not at the
raw table's full strength.

## Why a correction model, not a from-scratch forecast

Weather (4.2) and pick'em (2.3) both built an independent forecast from
scratch because no independent forecast source existed. Down-ballot
politics is different: ElectIndex already publishes a real, independent,
per-race probability model (`dem_prob`/`rep_prob`, ingested by
`ingest_polling_data.py`). Building a second election-forecasting model
on top of it would duplicate real expert work this project has no
comparative advantage at.

What ElectIndex's number does not answer is a market-calibration
question: is Kalshi's or Polymarket's *live price* wrong, and by how
much, in a way this project can act on? That has a real, published,
statistically-validated answer — see above — so this model corrects the
venue's own raw price directly, using ElectIndex's independent number as
a logged sanity check on the result, not as the estimate itself.

## A real ingestion problem found and fixed first (Session 5.1c)

Before this model could be written, a real problem was found in Session
5.1's own output: Kalshi's down-ballot races are not one Democrat-vs-
Republican contract each — they are a **separate open market per
candidate** (confirmed live against the real `KXCASEN26` series,
California State Senate District 26: 8 open candidate markets). The
original ingestion code kept only the first market Kalshi returned per
race, with no record of which candidate or party it belonged to.

This was fixed as a Session 5.1c patch, ahead of this model:
`ingest_politics_markets.py` now pulls every open market per series and
matches each one's real candidate name (Kalshi's `yes_sub_title` field,
confirmed live) against ElectIndex's own real `dem_name`/`rep_name`
columns (now carried through by `ingest_polling_data.py`) by last name,
accent- and case-insensitive. A market that matches neither name is a
real minor/third-party candidate — logged in
`kalshi_unmatched_candidates` / `polymarket_unmatched_candidates`, never
dropped and never guessed into a Dem/Rep slot. See
`schema_politics.py`'s and `ingest_politics_markets.py`'s own module
docstrings for the full evidence trail.

## Inputs

| Input | Source | Real field(s) used |
|---|---|---|
| Matched candidate market price | `politics_races_latest.csv` (Session 5.1c) | `kalshi_dem_yes_bid/ask`, `kalshi_rep_yes_bid/ask`, `polymarket_dem_yes_bid/ask`, `polymarket_rep_yes_bid/ask` |
| Independent probability (sanity check only) | `polling_estimates_latest.csv` (Session 5.1c) | `dem_win_prob`, `rep_win_prob` |
| Time-to-resolution | Fixed constant, not either venue's own `close_time` — see below | `GENERAL_ELECTION_DATE` |

## Why this model does not use either venue's own `close_time`

This project's own `tools-and-api-patterns.md` already records a
confirmed gotcha: Kalshi's `close_time` for political contracts reflects
the swearing-in date (~2027), not the election date. This model
sidesteps that entirely by using a single named constant,
`GENERAL_ELECTION_DATE = 2026-11-03` (the real, fixed date of the 2026
U.S. general election), applied identically to every race on both
venues, so the horizon bucket lookup below is computed the same way
regardless of which venue's own `close_time` field happens to be
trustworthy.

## The correction formula

Logistic recalibration, per Le (2026) Section 4.1 and 9.3:

```
p* = sigmoid(a + b · logit(p))
```

- `p` — the venue's raw price (bid/ask midpoint; falls back to whichever
  single side is quoted if only one exists, a real, observed case on
  thin down-ballot markets).
- `a` — the intercept. Le (2026) Table 10 reports a Politics domain mean
  intercept of −0.006 — close enough to zero that this model uses
  `a = 0` for every race. Named and sourced, not an omission.
- `b` — the calibration slope, domain- and horizon-specific. This model
  uses Le (2026) Table 4's Politics row, bucketed by real
  time-to-resolution (nine buckets, 0–1h through 1mo+, matching the
  paper's own bucket boundaries exactly).

## Dampening factor — the re-verification finding applied

Per the re-verification result above, this model does not apply Table
4's raw slopes at full strength. Each slope's deviation from 1.0 is
scaled by a named, sourced dampening factor:

```
POSTERIOR_SHRINKAGE_FACTOR = 0.107 / 0.156 ≈ 0.686
damped_b = 1.0 + (raw_b − 1.0) × POSTERIOR_SHRINKAGE_FACTOR
```

0.107 and 0.156 are Le (2026) Section 8.2's own posterior-mean-vs-raw-
descriptive comparison for the Politics domain intercept effect — the
paper's own measure of how much of the raw signal is real structure
versus estimation noise. This is this project's own modeling choice (a
conservative one, consistent with the weather model's own precedent of
choosing the more cautious end of its literature range), not a
multiplier the paper itself states.

## What every output row contains

One row per `(race_id, party)`, matching ElectIndex's own two-number-
per-race structure. Every row carries an explicit
`kalshi_model_status_<party>` / `polymarket_model_status_<party>`
explaining why a venue could not be estimated when that's the case —
nothing silently skipped:

`estimated` · `no_market_price` (no open market at this venue matched
this candidate) · `no_electindex_prob` (ElectIndex published no
probability for this party in this race — a real, observed case, e.g.
an uncontested race)

Each estimated cell also carries `*_edge_vs_raw_<party>` (corrected
estimate minus raw price — the model's own signal) and, where
ElectIndex has a number for that race, `*_edge_vs_electindex_<party>`
(corrected estimate minus ElectIndex's independent number — the sanity
check, logged but not fed back into the estimate).

## Stated gaps (v1, this session)

1. **Domain-by-horizon only, not the full domain-by-horizon-by-trade-size
   cube.** Le (2026)'s strongest political effect is actually the
   trade-size interaction (large Kalshi political trades show
   additional compression beyond the horizon effect alone — Table 5).
   This project's own ingestion does not currently capture per-contract
   trade-size data for down-ballot markets, so this model applies the
   horizon-only slope, which is real and sourced but understates the
   correction for races where the visible price is dominated by a few
   large trades. Revisit once trade-size data is captured, if ever
   needed.
2. **Candidate-name matching is real but not yet spot-checked against a
   large, live sample.** Session 5.1c's last-name matching (Kalshi) and
   title-substring matching (Polymarket) are new this session — the
   `kalshi_unmatched_candidates` / `polymarket_unmatched_candidates`
   fields on every race row are the honest, per-run signal of how well
   it's working. Spot-check against the first real live run before
   trusting this model's output for sizing.
3. **Polymarket's candidate-matching approach is unvalidated.**
   Polymarket's down-ballot title format for multi-candidate races was
   not confirmed live this session (same open gap the original Session
   5.1 module docstring already named for state-legislature titles more
   generally) — the title-substring matching here is a reasonable,
   defensive guess pending a real multi-candidate Polymarket example to
   check it against.
4. **No sizing, flagging, or CLV logging.** Same ingestion/estimation
   boundary this project's other tracks already established — a future
   session wires this into that downstream pipeline.
5. **Third-party and independent candidates are not estimated.**
   ElectIndex itself only forecasts `dem_prob`/`rep_prob` for these
   tiers — a minor candidate's own market is captured (in
   `*_unmatched_candidates`) so it's visible, but this model has no
   independent probability to correct it against yet.
