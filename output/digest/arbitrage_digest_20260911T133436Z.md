# Arbitrage Pipeline Digest -- 2026-09-11T13:34:36Z

## Run summary
- Kalshi ingestion: 2429 rows kept (563 target series, 94 down-ballot)
- Polymarket ingestion: 20689 rows
- Venue matching: 477 candidate pairs (477 elections-wide)
- Detection: 2 flags (0 single-venue, 2 cross-venue) from 477 candidate pairs checked

## This run's flagged opportunities
Sizing is a manual step (`sizing_engine.py arbitrage size`, Session 3.3) -- this table is what to scan to pick a pair worth sizing.

| opportunity_type | platform_a | title_a | leg_a_ask | platform_b | title_b | leg_b_ask | net_profit_per_dollar | liquidity_sufficient | legal_footprint_status |
|---|---|---|---|---|---|---|---|---|---|
| cross_venue | polymarket | Will the Democratic Party win the NJ-09 House seat? | 0.916 | kalshi | Will Democratic win the House race for NJ-9? | 0.055 | 0.0159 | True | both_venues_available |
| cross_venue | kalshi | Will Republican win the House race for VA-7? | 0.042 | polymarket | Will the Republican Party win the VA-07 House seat? | 0.935 | 0.0106 | True | both_venues_available |
