# Arbitrage Pipeline Digest -- 2026-09-21T18:39:11Z

## Run summary
- Kalshi ingestion: 2861 rows kept (573 target series, 94 down-ballot)
- Polymarket ingestion: 20102 rows
- Venue matching: 477 candidate pairs (477 elections-wide)
- Detection: 2 flags (0 single-venue, 2 cross-venue) from 477 candidate pairs checked

## This run's flagged opportunities
Sizing is a manual step (`sizing_engine.py arbitrage size`, Session 3.3) -- this table is what to scan to pick a pair worth sizing.

| opportunity_type | platform_a | title_a | leg_a_ask | platform_b | title_b | leg_b_ask | net_profit_per_dollar | liquidity_sufficient | legal_footprint_status |
|---|---|---|---|---|---|---|---|---|---|
| cross_venue | kalshi | Will Republican win the House race for TX-32? | 0.88 | polymarket | Will the Republican Party win the TX-32 House seat? | 0.0799999999999999 | 0.0271 | False | both_venues_available |
| cross_venue | kalshi | Will Democratic win the House race for AK-AL? | 0.021 | polymarket | Will the Democratic Party win the AK-AL House seat? | 0.946 | 0.021 | True | both_venues_available |
