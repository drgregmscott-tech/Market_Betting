# Arbitrage Pipeline Digest -- 2026-10-05T21:16:21Z

## Run summary
- Kalshi ingestion: 2593 rows kept (601 target series, 94 down-ballot)
- Polymarket ingestion: 19000 rows
- Venue matching: 478 candidate pairs (472 elections-wide)
- Detection: 7 flags (0 single-venue, 7 cross-venue) from 478 candidate pairs checked

## This run's flagged opportunities
Sizing is a manual step (`sizing_engine.py arbitrage size`, Session 3.3) -- this table is what to scan to pick a pair worth sizing.

| opportunity_type | platform_a | title_a | leg_a_ask | platform_b | title_b | leg_b_ask | net_profit_per_dollar | liquidity_sufficient | legal_footprint_status |
|---|---|---|---|---|---|---|---|---|---|
| cross_venue | polymarket | Will New York City FC win the 2026 MLS Cup? | 0.005 | kalshi | Snow in New York City in Dec 2026? | 0.59 | 0.3848 | False | both_venues_available |
| cross_venue | polymarket | Will New York City FC win the 2026 MLS Cup? | 0.005 | kalshi | Snow in New York City in Dec 2026? | 0.79 | 0.1848 | True | both_venues_available |
| cross_venue | polymarket | Will New York City FC win the 2026 MLS Cup? | 0.005 | kalshi | Snow in New York City in Dec 2026? | 0.84 | 0.1448 | False | both_venues_available |
| cross_venue | polymarket | Will New York City FC win the 2026 MLS Cup? | 0.005 | kalshi | Snow in New York City in Dec 2026? | 0.89 | 0.0948 | True | both_venues_available |
| cross_venue | polymarket | Will New York City FC win the 2026 MLS Cup? | 0.005 | kalshi | Snow in New York City in Dec 2026? | 0.91 | 0.0748 | False | both_venues_available |
| cross_venue | polymarket | Will New York City FC win the 2026 MLS Cup? | 0.005 | kalshi | Snow in New York City in Dec 2026? | 0.94 | 0.0448 | True | both_venues_available |
| cross_venue | polymarket | Will the Republican Party win the NM-02 House seat? | 0.028 | kalshi | Will Republican win the House race for NM-2? | 0.948 | 0.0129 | True | both_venues_available |
