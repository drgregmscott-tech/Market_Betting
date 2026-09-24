# Arbitrage Pipeline Digest -- 2026-09-24T17:51:43Z

## Run summary
- Kalshi ingestion: 2859 rows kept (586 target series, 94 down-ballot)
- Polymarket ingestion: 20051 rows
- Venue matching: 477 candidate pairs (477 elections-wide)
- Detection: 1 flags (0 single-venue, 1 cross-venue) from 477 candidate pairs checked

## This run's flagged opportunities
Sizing is a manual step (`sizing_engine.py arbitrage size`, Session 3.3) -- this table is what to scan to pick a pair worth sizing.

| opportunity_type | platform_a | title_a | leg_a_ask | platform_b | title_b | leg_b_ask | net_profit_per_dollar | liquidity_sufficient | legal_footprint_status |
|---|---|---|---|---|---|---|---|---|---|
| cross_venue | polymarket | Will the Republican Party win the OH-01 House seat? | 0.105 | kalshi | Will a Republican win the House race for OH-1? | 0.87 | 0.0112 | True | both_venues_available |
