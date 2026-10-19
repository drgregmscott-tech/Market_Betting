# Arbitrage Pipeline Digest -- 2026-10-19T19:17:09Z

## Run summary
- Kalshi ingestion: 3091 rows kept (640 target series, 94 down-ballot)
- Polymarket ingestion: 19218 rows
- Venue matching: 480 candidate pairs (472 elections-wide)
- Detection: 2 flags (0 single-venue, 2 cross-venue) from 480 candidate pairs checked

## This run's flagged opportunities
Sizing is a manual step (`sizing_engine.py arbitrage size`, Session 3.3) -- this table is what to scan to pick a pair worth sizing.

| opportunity_type | platform_a | title_a | leg_a_ask | platform_b | title_b | leg_b_ask | net_profit_per_dollar | liquidity_sufficient | legal_footprint_status |
|---|---|---|---|---|---|---|---|---|---|
| cross_venue | polymarket | Will New York City FC win the 2026 MLS Cup? | 0.005 | kalshi | Snow in New York City in Dec 2026? | 0.74 | 0.2348 | False | both_venues_available |
| cross_venue | polymarket | Will New York City FC win the 2026 MLS Cup? | 0.005 | kalshi | Snow in New York City in Dec 2026? | 0.96 | 0.0248 | False | both_venues_available |
