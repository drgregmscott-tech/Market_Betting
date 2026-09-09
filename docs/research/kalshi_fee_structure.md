# Kalshi Trading Fee Structure — Sourced for Session 4.4 (Sizing Adaptation)

**Why this doc exists:** every other per-track dampener in
`sizing_engine.py` (PLATFORM_RISK_MULTIPLIER, SAME_GAME_CAUTION_MULTIPLIER,
POLITICS_LOCKUP_DAMPENER_TABLE, PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER) is a
named judgment call this project could not source a specific number for.
Kalshi's trading fee is different — it is a real, published formula — so
it gets its own sourced record here rather than being treated as another
placeholder.

## The formula

```
fee = round_up_to_the_nearest_cent( 0.07 x contracts x price x (1 - price) )
```

Where `price` is the contract price in dollars (0 to 1) and `contracts` is
the number of contracts in the order. This is Kalshi's general trading fee
rate, charged on trade execution (both entry and any early exit before
settlement) — not on the settlement payout itself.

**Cross-checked against multiple independent 2026 sources** (search
performed 2026-09-09), all describing the same formula:
- [Kalshi Fees Explained: 2026 Trading Costs Overview](https://www.thelines.com/prediction-markets/kalshi/fees/)
- [Kalshi Fees Explained: The Real Cost of Trading (2026)](https://www.botforkalshi.com/blog/kalshi-fees-explained)
- [Kalshi Fees 2026: Trading, Deposit & Withdrawal Costs](https://www.predictionhunt.com/blog/kalshi-fees-complete-guide-2026)
- [Kalshi Fees: What The Coin Flip Really Costs](https://www.oddsshopper.com/articles/prediction-markets/kalshi-fees)

Example given directly in these sources: 100 contracts at 10 cents costs
63 cents in fees; 100 contracts at 50 cents (the maximum fee density,
since `price * (1-price)` peaks at price=0.50) costs $1.75.

## How `sizing_engine.py` uses this (Session 4.4)

A single sizing call for one contract cannot know its own final contract
count in advance — that depends on the Kelly fraction the call is trying
to compute. `kalshi_fee_per_contract(price)` applies the same formula at
`contracts = 1`, giving a per-contract marginal fee rate. This is folded
directly into `kalshi_effective_cost_per_contract(price) = price +
kalshi_fee_per_contract(price)`, which is passed into the existing
`raw_kelly_fraction_binary_contract()` helper in place of the raw market
price — so the fee is netted out of the edge before Kelly sizes the
position, rather than bolted on afterward as an unrelated flat multiplier.

**Stated simplification:** Kalshi's real fee rounds up once per whole
order, not once per contract — this project's per-contract rate is exact
at the formula level but does not reproduce that order-level rounding
(a real, bounded imprecision, not treated as exact — see
`sizing_engine.py`'s own Session 4.4 docstring addendum for the full
reasoning and stated boundaries).

**Not yet modeled:** any elevated/non-general fee tier Kalshi may apply to
specific market types. Session 4.1's weather ingestion carries no
fee-tier field, so every weather contract is sized assuming the general
7% rate. A stated gap, not a silent one.
