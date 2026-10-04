# Arbitrage Pipeline Digest -- 2026-10-04T17:33:45Z

## Run summary
- Kalshi ingestion: 2506 rows kept (595 target series, 94 down-ballot)
- Polymarket ingestion: 19238 rows
- Venue matching: 478 candidate pairs (472 elections-wide)
- Detection: 6 flags (0 single-venue, 6 cross-venue) from 478 candidate pairs checked

## This run's flagged opportunities
Sizing is a manual step (`sizing_engine.py arbitrage size`, Session 3.3) -- this table is what to scan to pick a pair worth sizing.

| opportunity_type | platform_a | title_a | leg_a_ask | platform_b | title_b | leg_b_ask | net_profit_per_dollar | liquidity_sufficient | legal_footprint_status |
|---|---|---|---|---|---|---|---|---|---|
| cross_venue | polymarket | Will New York City FC win the 2026 MLS Cup? | 0.006 | kalshi | Snow in New York City in Dec 2026? | 0.65 | 0.3237 | False | both_venues_available |
| cross_venue | polymarket | Will New York City FC win the 2026 MLS Cup? | 0.006 | kalshi | Snow in New York City in Dec 2026? | 0.79 | 0.1837 | False | both_venues_available |
| cross_venue | polymarket | Will New York City FC win the 2026 MLS Cup? | 0.006 | kalshi | Snow in New York City in Dec 2026? | 0.85 | 0.1337 | True | both_venues_available |
| cross_venue | polymarket | Will New York City FC win the 2026 MLS Cup? | 0.006 | kalshi | Snow in New York City in Dec 2026? | 0.9 | 0.0837 | True | both_venues_available |
| cross_venue | polymarket | Will New York City FC win the 2026 MLS Cup? | 0.006 | kalshi | Snow in New York City in Dec 2026? | 0.91 | 0.0737 | False | both_venues_available |
| cross_venue | polymarket | Will New York City FC win the 2026 MLS Cup? | 0.006 | kalshi | Snow in New York City in Dec 2026? | 0.95 | 0.0337 | True | both_venues_available |
