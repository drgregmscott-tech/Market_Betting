# Arbitrage Pipeline Digest -- 2026-09-18T05:55:18Z

## Run summary
- Kalshi ingestion: 2337 rows kept (571 target series, 94 down-ballot)
- Polymarket ingestion: 20430 rows
- Venue matching: 477 candidate pairs (477 elections-wide)
- Detection: 2 flags (0 single-venue, 2 cross-venue) from 477 candidate pairs checked

## This run's flagged opportunities
Sizing is a manual step (`sizing_engine.py arbitrage size`, Session 3.3) -- this table is what to scan to pick a pair worth sizing.

| opportunity_type | platform_a | title_a | leg_a_ask | platform_b | title_b | leg_b_ask | net_profit_per_dollar | liquidity_sufficient | legal_footprint_status |
|---|---|---|---|---|---|---|---|---|---|
| cross_venue | kalshi | Will Democratic win the House race for AK-AL? | 0.022 | polymarket | Will the Democratic Party win the AK-AL House seat? | 0.95 | 0.0161 | True | both_venues_available |
| cross_venue | kalshi | Will Republican win the House race for AK-AL? | 0.83 | polymarket | Will the Republican Party win the AK-AL House seat? | 0.14 | 0.0152 | True | both_venues_available |
