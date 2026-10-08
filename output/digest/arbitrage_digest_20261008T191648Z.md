# Arbitrage Pipeline Digest -- 2026-10-08T19:16:48Z

## Run summary
- Kalshi ingestion: 2965 rows kept (611 target series, 94 down-ballot)
- Polymarket ingestion: 18869 rows
- Venue matching: 478 candidate pairs (472 elections-wide)
- Detection: 1 flags (0 single-venue, 1 cross-venue) from 478 candidate pairs checked

## This run's flagged opportunities
Sizing is a manual step (`sizing_engine.py arbitrage size`, Session 3.3) -- this table is what to scan to pick a pair worth sizing.

| opportunity_type | platform_a | title_a | leg_a_ask | platform_b | title_b | leg_b_ask | net_profit_per_dollar | liquidity_sufficient | legal_footprint_status |
|---|---|---|---|---|---|---|---|---|---|
| cross_venue | polymarket | Will New York City FC win the 2026 MLS Cup? | 0.005 | kalshi | Snow in New York City in Dec 2026? | 0.91 | 0.0748 | False | both_venues_available |
