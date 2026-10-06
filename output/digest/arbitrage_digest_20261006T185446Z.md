# Arbitrage Pipeline Digest -- 2026-10-06T18:54:46Z

## Run summary
- Kalshi ingestion: 3190 rows kept (610 target series, 94 down-ballot)
- Polymarket ingestion: 18853 rows
- Venue matching: 478 candidate pairs (472 elections-wide)
- Detection: 6 flags (0 single-venue, 6 cross-venue) from 478 candidate pairs checked

## This run's flagged opportunities
Sizing is a manual step (`sizing_engine.py arbitrage size`, Session 3.3) -- this table is what to scan to pick a pair worth sizing.

| opportunity_type | platform_a | title_a | leg_a_ask | platform_b | title_b | leg_b_ask | net_profit_per_dollar | liquidity_sufficient | legal_footprint_status |
|---|---|---|---|---|---|---|---|---|---|
| cross_venue | polymarket | Will New York City FC win the 2026 MLS Cup? | 0.005 | kalshi | Snow in New York City in Dec 2026? | 0.59 | 0.3848 | False | both_venues_available |
| cross_venue | polymarket | Will New York City FC win the 2026 MLS Cup? | 0.005 | kalshi | Snow in New York City in Dec 2026? | 0.79 | 0.1848 | False | both_venues_available |
| cross_venue | polymarket | Will New York City FC win the 2026 MLS Cup? | 0.005 | kalshi | Snow in New York City in Dec 2026? | 0.85 | 0.1348 | False | both_venues_available |
| cross_venue | polymarket | Will New York City FC win the 2026 MLS Cup? | 0.005 | kalshi | Snow in New York City in Dec 2026? | 0.89 | 0.0948 | True | both_venues_available |
| cross_venue | polymarket | Will New York City FC win the 2026 MLS Cup? | 0.005 | kalshi | Snow in New York City in Dec 2026? | 0.92 | 0.0648 | False | both_venues_available |
| cross_venue | polymarket | Will New York City FC win the 2026 MLS Cup? | 0.005 | kalshi | Snow in New York City in Dec 2026? | 0.94 | 0.0448 | True | both_venues_available |
