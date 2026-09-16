# Arbitrage Pipeline Digest -- 2026-09-16T23:39:45Z

## Run summary
- Kalshi ingestion: 2664 rows kept (571 target series, 94 down-ballot)
- Polymarket ingestion: 20515 rows
- Venue matching: 477 candidate pairs (477 elections-wide)
- Detection: 2 flags (0 single-venue, 2 cross-venue) from 477 candidate pairs checked

## This run's flagged opportunities
Sizing is a manual step (`sizing_engine.py arbitrage size`, Session 3.3) -- this table is what to scan to pick a pair worth sizing.

| opportunity_type | platform_a | title_a | leg_a_ask | platform_b | title_b | leg_b_ask | net_profit_per_dollar | liquidity_sufficient | legal_footprint_status |
|---|---|---|---|---|---|---|---|---|---|
| cross_venue | polymarket | Will the Democratic Party win the TX-09 House seat? | 0.1 | kalshi | Will Democratic win the House race for TX-09? | 0.87 | 0.0164 | False | both_venues_available |
| cross_venue | kalshi | Will Republican win the House race for AK-AL? | 0.85 | polymarket | Will the Republican Party win the AK-AL House seat? | 0.12 | 0.0158 | True | both_venues_available |
