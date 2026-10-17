# Arbitrage Pipeline Digest -- 2026-10-17T16:21:51Z

## Run summary
- Kalshi ingestion: 2539 rows kept (639 target series, 94 down-ballot)
- Polymarket ingestion: 19350 rows
- Venue matching: 480 candidate pairs (472 elections-wide)
- Detection: 2 flags (0 single-venue, 2 cross-venue) from 480 candidate pairs checked

## This run's flagged opportunities
Sizing is a manual step (`sizing_engine.py arbitrage size`, Session 3.3) -- this table is what to scan to pick a pair worth sizing.

| opportunity_type | platform_a | title_a | leg_a_ask | platform_b | title_b | leg_b_ask | net_profit_per_dollar | liquidity_sufficient | legal_footprint_status |
|---|---|---|---|---|---|---|---|---|---|
| cross_venue | polymarket | Will New York City FC win the 2026 MLS Cup? | 0.004 | kalshi | Snow in New York City in Dec 2026? | 0.9 | 0.0858 | False | both_venues_available |
| cross_venue | polymarket | Will New York City FC win the 2026 MLS Cup? | 0.004 | kalshi | Snow in New York City in Dec 2026? | 0.97 | 0.0158 | True | both_venues_available |
