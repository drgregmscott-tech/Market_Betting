# Arbitrage Pipeline Digest -- 2026-10-23T17:53:14Z

## Run summary
- Kalshi ingestion: 3145 rows kept (654 target series, 94 down-ballot)
- Polymarket ingestion: 19163 rows
- Venue matching: 480 candidate pairs (472 elections-wide)
- Detection: 3 flags (0 single-venue, 3 cross-venue) from 480 candidate pairs checked

## This run's flagged opportunities
Sizing is a manual step (`sizing_engine.py arbitrage size`, Session 3.3) -- this table is what to scan to pick a pair worth sizing.

| opportunity_type | platform_a | title_a | leg_a_ask | platform_b | title_b | leg_b_ask | net_profit_per_dollar | liquidity_sufficient | legal_footprint_status |
|---|---|---|---|---|---|---|---|---|---|
| cross_venue | polymarket | Will New York City FC win the 2026 MLS Cup? | 0.004 | kalshi | Snow in New York City in Dec 2026? | 0.68 | 0.2958 | False | both_venues_available |
| cross_venue | polymarket | Will New York City FC win the 2026 MLS Cup? | 0.004 | kalshi | Snow in New York City in Dec 2026? | 0.96 | 0.0258 | False | both_venues_available |
| cross_venue | polymarket | Will New York City FC win the 2026 MLS Cup? | 0.004 | kalshi | Snow in New York City in Dec 2026? | 0.96 | 0.0258 | False | both_venues_available |
