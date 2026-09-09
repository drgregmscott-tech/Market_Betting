# Arbitrage Pipeline Digest -- 2026-09-09T13:43:13Z

## Run summary
- Kalshi ingestion: 2383 rows kept (553 target series, 94 down-ballot)
- Polymarket ingestion: 20636 rows
- Venue matching: 477 candidate pairs (477 elections-wide)
- Detection: 1 flags (0 single-venue, 1 cross-venue) from 477 candidate pairs checked

## This run's flagged opportunities
Sizing is a manual step (`sizing_engine.py arbitrage size`, Session 3.3) -- this table is what to scan to pick a pair worth sizing.

| opportunity_type | platform_a | title_a | leg_a_ask | platform_b | title_b | leg_b_ask | net_profit_per_dollar | liquidity_sufficient | legal_footprint_status |
|---|---|---|---|---|---|---|---|---|---|
| cross_venue | polymarket | Will the Republican Party win the TX-32 House seat? | 0.81 | kalshi | Will Republican win the House race for TX-32? | 0.15 | 0.0238 | False | both_venues_available |
