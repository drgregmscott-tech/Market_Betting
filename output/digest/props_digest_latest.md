# Props Pipeline Digest -- 2026-11-12T07:29:01Z

## Run summary
- DraftKings ingestion: 0 rows across 0 events (FAILED -- see logs/ingestion.log)
- FanDuel ingestion: 0 rows (FAILED -- see logs/ingestion.log)
- BetMGM ingestion (via Rotowire): 850 rows (OK)
- Estimation: 850 rows written (from 850 ingested rows) -- status breakdown: {'estimated': 366, 'unsupported_market_first_scorer': 248, 'unsupported_stat_type': 210, 'no_player_match': 16, 'insufficient_history': 10}
- CLV logging: 6 newly flagged, 0 newly closed, 8 still open (1534 total ever logged)

## Currently open flags
Sizing is a manual step (`sizing_engine.py props size`, Session 6.4) -- this table is what to scan to pick a flag worth sizing. `implied_prob_includes_field_vig` matters here more than for the other tracks: a row still reporting True carries a real, separate uncertainty (Session 6.4's `PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER` dampener) that a bigger raw edge number does not describe.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_model_prob | first_flagged_market_price | first_flagged_edge | implied_prob_includes_field_vig | first_flagged_at |
|---|---|---|---|---|---|---|---|---|---|
| betmgm|anytd|16034 | betmgm | Teagan Quitoriano | anytd | over | 0.6002 | 0.0476 | 0.5525 | False | 2026-11-12T07:29:25Z |
| betmgm|recs|16935 | betmgm | Tank Dell | recs | over | 1.0 | 0.5347 | 0.4653 | False | 2026-11-12T07:29:25Z |
| betmgm|anytd|19258 | betmgm | Jack Endries | anytd | over | 0.3677 | 0.0714 | 0.2962 | False | 2026-11-10T21:54:10Z |
| betmgm|anytd|14430 | betmgm | Van Jefferson | anytd | over | 0.4182 | 0.1538 | 0.2644 | False | 2026-11-10T12:50:30Z |
| betmgm|anytd|16935 | betmgm | Tank Dell | anytd | over | 0.4182 | 0.2381 | 0.1801 | False | 2026-11-12T07:29:25Z |
| betmgm|anytd|14608 | betmgm | Charlie Woerner | anytd | over | 0.2277 | 0.087 | 0.1407 | False | 2026-11-12T07:29:25Z |
| betmgm|anytd|18554 | betmgm | Savion Williams | anytd | over | 0.2704 | 0.1818 | 0.0886 | False | 2026-11-12T07:29:25Z |
| betmgm|anytd|13854 | betmgm | Ashton Dulin | anytd | over | 0.2404 | 0.2041 | 0.0363 | False | 2026-11-12T07:29:25Z |
