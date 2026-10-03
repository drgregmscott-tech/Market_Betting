# Arbitrage Pipeline Digest -- 2026-10-03T17:14:17Z

## Run summary
- Kalshi ingestion: 2500 rows kept (594 target series, 94 down-ballot)
- Polymarket ingestion: 19217 rows
- Venue matching: 478 candidate pairs (472 elections-wide)
- Detection: 6 flags (0 single-venue, 6 cross-venue) from 478 candidate pairs checked

## This run's flagged opportunities
Sizing is a manual step (`sizing_engine.py arbitrage size`, Session 3.3) -- this table is what to scan to pick a pair worth sizing.

| opportunity_type | platform_a | title_a | leg_a_ask | platform_b | title_b | leg_b_ask | net_profit_per_dollar | liquidity_sufficient | legal_footprint_status |
|---|---|---|---|---|---|---|---|---|---|
| cross_venue | polymarket | Will New York City FC win the 2026 MLS Cup? | 0.011 | kalshi | Snow in New York City in Dec 2026? | 0.68 | 0.2885 | True | both_venues_available |
| cross_venue | polymarket | Will New York City FC win the 2026 MLS Cup? | 0.011 | kalshi | Snow in New York City in Dec 2026? | 0.8 | 0.1685 | True | both_venues_available |
| cross_venue | polymarket | Will New York City FC win the 2026 MLS Cup? | 0.011 | kalshi | Snow in New York City in Dec 2026? | 0.86 | 0.1185 | True | both_venues_available |
| cross_venue | polymarket | Will New York City FC win the 2026 MLS Cup? | 0.011 | kalshi | Snow in New York City in Dec 2026? | 0.9 | 0.0785 | True | both_venues_available |
| cross_venue | polymarket | Will New York City FC win the 2026 MLS Cup? | 0.011 | kalshi | Snow in New York City in Dec 2026? | 0.93 | 0.0485 | True | both_venues_available |
| cross_venue | polymarket | Will New York City FC win the 2026 MLS Cup? | 0.011 | kalshi | Snow in New York City in Dec 2026? | 0.95 | 0.0285 | True | both_venues_available |
