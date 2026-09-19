# Arbitrage Pipeline Digest -- 2026-09-19T16:25:42Z

## Run summary
- Kalshi ingestion: 2338 rows kept (572 target series, 94 down-ballot)
- Polymarket ingestion: 20203 rows
- Venue matching: 477 candidate pairs (477 elections-wide)
- Detection: 1 flags (0 single-venue, 1 cross-venue) from 477 candidate pairs checked

## This run's flagged opportunities
Sizing is a manual step (`sizing_engine.py arbitrage size`, Session 3.3) -- this table is what to scan to pick a pair worth sizing.

| opportunity_type | platform_a | title_a | leg_a_ask | platform_b | title_b | leg_b_ask | net_profit_per_dollar | liquidity_sufficient | legal_footprint_status |
|---|---|---|---|---|---|---|---|---|---|
| cross_venue | polymarket | Will the Republican Party win the NM-02 House seat? | 0.06 | kalshi | Will Republican win the House race for NM-2? | 0.91 | 0.0177 | True | both_venues_available |
