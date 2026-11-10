# Props Pipeline Digest -- 2026-11-10T21:53:58Z

## Run summary
- DraftKings ingestion: 186 rows across 8 events (OK)
- FanDuel ingestion: 0 rows (OK)
- BetMGM ingestion (via Rotowire): 120 rows (OK)
- Estimation: 306 rows written (from 306 ingested rows) -- status breakdown: {'estimated': 191, 'unsupported_market_first_scorer': 46, 'unsupported_stat_type': 35, 'no_player_match': 26, 'insufficient_history': 8}
- CLV logging: 4 newly flagged, 0 newly closed, 27 still open (1495 total ever logged)

## Currently open flags
Sizing is a manual step (`sizing_engine.py props size`, Session 6.4) -- this table is what to scan to pick a flag worth sizing. `implied_prob_includes_field_vig` matters here more than for the other tracks: a row still reporting True carries a real, separate uncertainty (Session 6.4's `PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER` dampener) that a bigger raw edge number does not describe.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_model_prob | first_flagged_market_price | first_flagged_edge | implied_prob_includes_field_vig | first_flagged_at |
|---|---|---|---|---|---|---|---|---|---|
| betmgm|anytd|19258 | betmgm | Jack Endries | anytd | over | 0.3677 | 0.0714 | 0.2962 | False | 2026-11-10T21:54:10Z |
| draftkings|387480437|0QA387480437#2357394470_13L88808Q1-115201972Q20 | draftkings | Van Jefferson | Anytime TD Scorer | over | 0.4182 | 0.1333 | 0.2849 | False | 2026-11-09T06:56:58Z |
| draftkings|387839216|0QA387839216#2359644663_13L88808Q1877705888Q20 | draftkings | Kirk Cousins | Anytime TD Scorer | over | 0.3371 | 0.0667 | 0.2704 | False | 2026-11-10T21:54:10Z |
| betmgm|anytd|14430 | betmgm | Van Jefferson | anytd | over | 0.4182 | 0.1538 | 0.2644 | False | 2026-11-10T12:50:30Z |
| draftkings|387480437|0QA387480437#2357394454_13L88808Q1-1809117535Q20 | draftkings | Isaiah Likely | Anytime TD Scorer | over | 0.537 | 0.3333 | 0.2037 | False | 2026-11-09T06:56:58Z |
| draftkings|387839216|0QA387839216#2359067390_13L88808Q1-1213243313Q20 | draftkings | Jordan Love | Anytime TD Scorer | over | 0.2926 | 0.1111 | 0.1815 | False | 2026-11-10T21:54:10Z |
| draftkings|387584920|0QA387584920#2357860056_13L88808Q1410823711Q20 | draftkings | Tony Pollard | Anytime TD Scorer | over | 0.6802 | 0.5 | 0.1802 | False | 2026-11-10T21:54:10Z |
| draftkings|387554294|0QA387554294#2357739847_13L88808Q1480222870Q20 | draftkings | Jameson Williams | Anytime TD Scorer | over | 0.5312 | 0.3571 | 0.174 | False | 2026-11-09T18:58:36Z |
| draftkings|387480437|0QA387480437#2357394460_13L88808Q1-534343686Q20 | draftkings | Theo Johnson | Anytime TD Scorer | over | 0.2296 | 0.0909 | 0.1387 | False | 2026-11-09T06:56:58Z |
| draftkings|387560840|0QA387560840#2357763152_13L88808Q1999478588Q20 | draftkings | Kyle Pitts Sr. | Anytime TD Scorer | over | 0.3826 | 0.25 | 0.1326 | False | 2026-11-09T18:58:36Z |
| draftkings|387487626|0QA387487626#2357440084_13L88808Q1-861767826Q20 | draftkings | Isaiah Likely | 2+ TDs | over | 0.1805 | 0.0588 | 0.1216 | False | 2026-11-09T06:56:58Z |
| draftkings|387569930|0QA387569930#2357806207_13L88808Q1-106544391Q20 | draftkings | Jameson Williams | 2+ TDs | over | 0.176 | 0.0667 | 0.1094 | False | 2026-11-09T18:58:36Z |
| draftkings|387480437|0QA387480437#2357394468_13L88808Q1622596392Q20 | draftkings | Stefon Diggs | Anytime TD Scorer | over | 0.4413 | 0.3333 | 0.108 | False | 2026-11-09T06:56:58Z |
| draftkings|387554294|0QA387554294#2357739859_13L88808Q1-205213128Q20 | draftkings | Demario Douglas | Anytime TD Scorer | over | 0.3857 | 0.2899 | 0.0958 | False | 2026-11-09T18:58:36Z |
| draftkings|387487626|0QA387487626#2357440099_13L88808Q11585686638Q20 | draftkings | Van Jefferson | 2+ TDs | over | 0.1031 | 0.0123 | 0.0907 | False | 2026-11-09T06:56:58Z |
| draftkings|387554294|0QA387554294#2357739821_13L88808Q1-725127430Q20 | draftkings | Drake Maye | Anytime TD Scorer | over | 0.3506 | 0.2632 | 0.0874 | False | 2026-11-09T18:58:36Z |
| draftkings|387584920|0QA387584920#2357860057_13L88808Q117668529Q20 | draftkings | Wan'Dale Robinson | Anytime TD Scorer | over | 0.3314 | 0.2597 | 0.0716 | False | 2026-11-09T18:58:36Z |
| draftkings|387569245|0QA387569245#2357803412_13L88808Q1466829631Q20 | draftkings | Harold Fannin Jr. | Anytime TD Scorer | over | 0.3278 | 0.2667 | 0.0611 | False | 2026-11-09T18:58:36Z |
| draftkings|387487626|0QA387487626#2357440096_13L88808Q1-60147958Q20 | draftkings | Stefon Diggs | 2+ TDs | over | 0.1161 | 0.0556 | 0.0605 | False | 2026-11-09T06:56:58Z |
| draftkings|387480437|0QA387480437#2357423649_13L88808Q1557870560Q20 | draftkings | Treylon Burks | Anytime TD Scorer | over | 0.2341 | 0.1739 | 0.0602 | False | 2026-11-09T06:56:58Z |
| draftkings|387554294|0QA387554294#2357739860_13L88808Q11958986630Q20 | draftkings | Kyle Williams | Anytime TD Scorer | over | 0.2413 | 0.1818 | 0.0595 | False | 2026-11-09T18:58:36Z |
| draftkings|387554294|0QA387554294#2357739852_13L88808Q1-1939996255Q20 | draftkings | Jared Goff | Anytime TD Scorer | over | 0.1153 | 0.0667 | 0.0486 | False | 2026-11-09T18:58:36Z |
| draftkings|387554294|0QA387554294#2357739862_13L88808Q1-2056923875Q20 | draftkings | Efton Chism III | Anytime TD Scorer | over | 0.2592 | 0.2128 | 0.0464 | False | 2026-11-09T18:58:36Z |
| draftkings|387480437|0QA387480437#2357394400_13L88808Q11930260006Q20 | draftkings | Devin Singletary | Anytime TD Scorer | over | 0.3058 | 0.2632 | 0.0426 | False | 2026-11-09T06:56:58Z |
| draftkings|387569930|0QA387569930#2357806218_13L88808Q1573901773Q20 | draftkings | Demario Douglas | 2+ TDs | over | 0.0864 | 0.0476 | 0.0387 | False | 2026-11-09T18:58:36Z |
| draftkings|387569245|0QA387569245#2357803424_13L88808Q11759839095Q20 | draftkings | Nico Collins | Anytime TD Scorer | over | 0.4447 | 0.4082 | 0.0366 | False | 2026-11-09T18:58:36Z |
| draftkings|387569930|0QA387569930#2357806219_13L88808Q11724982079Q20 | draftkings | Drake Maye | 2+ TDs | over | 0.0702 | 0.0345 | 0.0358 | False | 2026-11-09T18:58:36Z |
