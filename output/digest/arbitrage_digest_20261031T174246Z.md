# Arbitrage Pipeline Digest -- 2026-10-31T17:42:46Z

## Run summary
- Kalshi ingestion: 2575 rows kept (703 target series, 95 down-ballot)
- Polymarket ingestion: 19000 rows
- Venue matching: 482 candidate pairs (472 elections-wide)
- Detection: 6 flags (0 single-venue, 6 cross-venue) from 482 candidate pairs checked

## This run's flagged opportunities
Sizing is a manual step (`sizing_engine.py arbitrage size`, Session 3.3) -- this table is what to scan to pick a pair worth sizing.

| opportunity_type | platform_a | title_a | leg_a_ask | platform_b | title_b | leg_b_ask | net_profit_per_dollar | liquidity_sufficient | legal_footprint_status |
|---|---|---|---|---|---|---|---|---|---|
| cross_venue | polymarket | Will New York City FC win the 2026 MLS Cup? | 0.004 | kalshi | Snow in New York City in Dec 2026? | 0.6 | 0.3758 | False | both_venues_available |
| cross_venue | polymarket | Will New York City FC win the 2026 MLS Cup? | 0.004 | kalshi | Snow in New York City in Dec 2026? | 0.77 | 0.2058 | False | both_venues_available |
| cross_venue | polymarket | Will New York City FC win the 2026 MLS Cup? | 0.004 | kalshi | Snow in New York City in Dec 2026? | 0.87 | 0.1158 | False | both_venues_available |
| cross_venue | polymarket | Will New York City FC win the 2026 MLS Cup? | 0.004 | kalshi | Snow in New York City in Dec 2026? | 0.93 | 0.0558 | True | both_venues_available |
| cross_venue | polymarket | Will New York City FC win the 2026 MLS Cup? | 0.004 | kalshi | Snow in New York City in Dec 2026? | 0.93 | 0.0558 | False | both_venues_available |
| cross_venue | polymarket | Will New York City FC win the 2026 MLS Cup? | 0.004 | kalshi | Snow in New York City in Dec 2026? | 0.94 | 0.0458 | False | both_venues_available |
