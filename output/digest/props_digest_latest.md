# Props Pipeline Digest -- 2026-11-17T13:41:57Z

## Run summary
- DraftKings ingestion: 198 rows across 8 events (OK)
- FanDuel ingestion: 0 rows (OK)
- BetMGM ingestion (via Rotowire): 147 rows (OK)
- Estimation: 345 rows written (from 345 ingested rows) -- status breakdown: {'estimated': 231, 'unsupported_market_first_scorer': 53, 'no_player_match': 25, 'unsupported_stat_type': 22, 'insufficient_history': 14}
- CLV logging: 11 newly flagged, 0 newly closed, 23 still open (1621 total ever logged)

## Currently open flags
Sizing is a manual step (`sizing_engine.py props size`, Session 6.4) -- this table is what to scan to pick a flag worth sizing. `implied_prob_includes_field_vig` matters here more than for the other tracks: a row still reporting True carries a real, separate uncertainty (Session 6.4's `PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER` dampener) that a bigger raw edge number does not describe.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_model_prob | first_flagged_market_price | first_flagged_edge | implied_prob_includes_field_vig | first_flagged_at |
|---|---|---|---|---|---|---|---|---|---|
| draftkings|389630297|0QA389630297#2367290735_13L88808Q1-1461677560Q20 | draftkings | Foster Moreau | Anytime TD Scorer | over | 0.4831 | 0.1667 | 0.3165 | False | 2026-11-16T06:53:00Z |
| draftkings|389627988|0QA389627988#2367276119_13L88808Q11222312202Q20 | draftkings | Jalen Tolbert | Anytime TD Scorer | over | 0.2704 | 0.0556 | 0.2148 | False | 2026-11-17T13:42:12Z |
| draftkings|389630297|0QA389630297#2367290733_13L88808Q1-1444150535Q20 | draftkings | Xavier Hutchinson | Anytime TD Scorer | over | 0.4326 | 0.2703 | 0.1623 | False | 2026-11-16T06:53:00Z |
| draftkings|389635554|0QA389635554#2367321456_13L88808Q1480222870Q20 | draftkings | Jameson Williams | Anytime TD Scorer | over | 0.4389 | 0.3077 | 0.1312 | False | 2026-11-16T18:44:30Z |
| betmgm|anytd|18906 | betmgm | Keleki Latu | anytd | over | 0.171 | 0.0435 | 0.1275 | False | 2026-11-17T13:42:12Z |
| draftkings|389627988|0QA389627988#2367276104_13L88808Q11235745545Q20 | draftkings | Keleki Latu | Anytime TD Scorer | over | 0.171 | 0.0435 | 0.1275 | False | 2026-11-17T13:42:12Z |
| draftkings|389672552|0QA389672552#2367557392_13L88808Q1257323792Q20 | draftkings | Foster Moreau | 2+ TDs | over | 0.142 | 0.0164 | 0.1256 | False | 2026-11-16T06:53:00Z |
| betmgm|anytd|19303 | betmgm | Seth McGowan | anytd | over | 0.3297 | 0.2174 | 0.1123 | False | 2026-11-17T13:42:12Z |
| draftkings|389630297|0QA389630297#2367290748_13L88808Q1942374795Q20 | draftkings | Ashton Dulin | Anytime TD Scorer | over | 0.1881 | 0.0833 | 0.1047 | False | 2026-11-16T06:53:00Z |
| draftkings|389630297|0QA389630297#2367290744_13L88808Q1-348566577Q20 | draftkings | Seth McGowan | Anytime TD Scorer | over | 0.3297 | 0.25 | 0.0797 | False | 2026-11-16T06:53:00Z |
| draftkings|389627988|0QA389627988#2367276114_13L88808Q1-533028316Q20 | draftkings | Kevin Coleman Jr. | Anytime TD Scorer | over | 0.2328 | 0.1538 | 0.0789 | False | 2026-11-17T13:42:12Z |
| draftkings|389672552|0QA389672552#2367557390_13L88808Q11497747421Q20 | draftkings | Xavier Hutchinson | 2+ TDs | over | 0.1111 | 0.0345 | 0.0766 | False | 2026-11-16T06:53:00Z |
| betmgm|anytd|19607 | betmgm | Kaelon Black | anytd | over | 0.3203 | 0.25 | 0.0703 | False | 2026-11-17T13:42:12Z |
| draftkings|389992033|0QA389992033#2368991842_13L88808Q11587218485Q20 | draftkings | Josh Allen | 2+ TDs | over | 0.3014 | 0.2439 | 0.0575 | False | 2026-11-17T13:42:12Z |
| draftkings|389630297|0QA389630297#2367290732_13L88808Q11057552796Q20 | draftkings | Tank Dell | Anytime TD Scorer | over | 0.276 | 0.2273 | 0.0487 | False | 2026-11-16T18:44:30Z |
| draftkings|389630297|0QA389630297#2367290734_13L88808Q1401138925Q20 | draftkings | Kayshon Boutte | Anytime TD Scorer | over | 0.3031 | 0.2564 | 0.0467 | False | 2026-11-16T06:53:00Z |
| draftkings|389654195|0QA389654195#2367447999_13L88808Q11587306986Q20 | draftkings | Trey McBride | Anytime TD Scorer | over | 0.3363 | 0.2985 | 0.0378 | False | 2026-11-16T18:44:30Z |
| draftkings|389630297|0QA389630297#2367290736_13L88808Q12058064406Q20 | draftkings | Marvin Harrison Jr. | Anytime TD Scorer | over | 0.2795 | 0.2439 | 0.0356 | False | 2026-11-16T18:44:30Z |
| draftkings|389992033|0QA389992033#2368991841_13L88808Q1503159412Q20 | draftkings | James Cook | 2+ TDs | over | 0.279 | 0.2439 | 0.0351 | False | 2026-11-17T13:42:12Z |
| draftkings|389630297|0QA389630297#2367290743_13L88808Q11289716993Q20 | draftkings | Laquon Treadwell | Anytime TD Scorer | over | 0.2015 | 0.1667 | 0.0348 | False | 2026-11-16T06:53:00Z |
| betmgm|anytd|10739 | betmgm | Laquon Treadwell | anytd | over | 0.2015 | 0.1667 | 0.0348 | False | 2026-11-17T13:42:12Z |
| draftkings|389992033|0QA389992033#2368991930_13L88808Q11009072757Q20 | draftkings | Jalen Tolbert | 2+ TDs | over | 0.0404 | 0.0058 | 0.0345 | False | 2026-11-17T13:42:12Z |
| draftkings|389672552|0QA389672552#2367557396_13L88808Q1-472168960Q20 | draftkings | Seth McGowan | 2+ TDs | over | 0.0616 | 0.0278 | 0.0338 | False | 2026-11-17T13:42:12Z |
