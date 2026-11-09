# Props Pipeline Digest -- 2026-11-09T06:56:44Z

## Run summary
- DraftKings ingestion: 170 rows across 8 events (OK)
- FanDuel ingestion: 0 rows (OK)
- BetMGM ingestion (via Rotowire): 84 rows (OK)
- Estimation: 254 rows written (from 254 ingested rows) -- status breakdown: {'estimated': 122, 'unsupported_market_first_scorer': 72, 'unsupported_stat_type': 27, 'no_player_match': 20, 'insufficient_history': 13}
- CLV logging: 15 newly flagged, 0 newly closed, 16 still open (1477 total ever logged)

## Currently open flags
Sizing is a manual step (`sizing_engine.py props size`, Session 6.4) -- this table is what to scan to pick a flag worth sizing. `implied_prob_includes_field_vig` matters here more than for the other tracks: a row still reporting True carries a real, separate uncertainty (Session 6.4's `PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER` dampener) that a bigger raw edge number does not describe.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_model_prob | first_flagged_market_price | first_flagged_edge | implied_prob_includes_field_vig | first_flagged_at |
|---|---|---|---|---|---|---|---|---|---|
| betmgm|recs|18536 | betmgm | Ben Yurosek | recs | over | 1.0 | 0.5575 | 0.4425 | False | 2026-11-07T23:45:48Z |
| draftkings|387480437|0QA387480437#2357394470_13L88808Q1-115201972Q20 | draftkings | Van Jefferson | Anytime TD Scorer | over | 0.4182 | 0.1333 | 0.2849 | False | 2026-11-09T06:56:58Z |
| draftkings|387480437|0QA387480437#2357394454_13L88808Q1-1809117535Q20 | draftkings | Isaiah Likely | Anytime TD Scorer | over | 0.537 | 0.3333 | 0.2037 | False | 2026-11-09T06:56:58Z |
| draftkings|385044057|0QA385044057#2346285987_13L88808Q1-2072232579Q20 | draftkings | Keon Coleman | Anytime TD Scorer | over | 0.393 | 0.1905 | 0.2026 | False | 2026-11-09T06:56:58Z |
| draftkings|387480437|0QA387480437#2357394460_13L88808Q1-534343686Q20 | draftkings | Theo Johnson | Anytime TD Scorer | over | 0.2296 | 0.0909 | 0.1387 | False | 2026-11-09T06:56:58Z |
| draftkings|385785493|0QA385785493#2349815207_13L88808Q1503159412Q20 | draftkings | James Cook | 2+ TDs | over | 0.301 | 0.1667 | 0.1343 | False | 2026-11-09T06:56:58Z |
| draftkings|387487626|0QA387487626#2357440084_13L88808Q1-861767826Q20 | draftkings | Isaiah Likely | 2+ TDs | over | 0.1805 | 0.0588 | 0.1216 | False | 2026-11-09T06:56:58Z |
| draftkings|385785493|0QA385785493#2349815208_13L88808Q11587218485Q20 | draftkings | Josh Allen | 2+ TDs | over | 0.2855 | 0.1667 | 0.1188 | False | 2026-11-09T06:56:58Z |
| draftkings|387480437|0QA387480437#2357394468_13L88808Q1622596392Q20 | draftkings | Stefon Diggs | Anytime TD Scorer | over | 0.4413 | 0.3333 | 0.108 | False | 2026-11-09T06:56:58Z |
| draftkings|387487626|0QA387487626#2357440099_13L88808Q11585686638Q20 | draftkings | Van Jefferson | 2+ TDs | over | 0.1031 | 0.0123 | 0.0907 | False | 2026-11-09T06:56:58Z |
| draftkings|385044057|0QA385044057#2346285975_13L88808Q1122147185Q20 | draftkings | T.J. Hockenson | Anytime TD Scorer | over | 0.4021 | 0.3226 | 0.0795 | False | 2026-11-09T06:56:58Z |
| draftkings|385785493|0QA385785493#2349815212_13L88808Q1-2143181684Q20 | draftkings | Keon Coleman | 2+ TDs | over | 0.09 | 0.0217 | 0.0682 | False | 2026-11-09T06:56:58Z |
| draftkings|387487626|0QA387487626#2357440096_13L88808Q1-60147958Q20 | draftkings | Stefon Diggs | 2+ TDs | over | 0.1161 | 0.0556 | 0.0605 | False | 2026-11-09T06:56:58Z |
| draftkings|387480437|0QA387480437#2357423649_13L88808Q1557870560Q20 | draftkings | Treylon Burks | Anytime TD Scorer | over | 0.2341 | 0.1739 | 0.0602 | False | 2026-11-09T06:56:58Z |
| draftkings|387480437|0QA387480437#2357394400_13L88808Q11930260006Q20 | draftkings | Devin Singletary | Anytime TD Scorer | over | 0.3058 | 0.2632 | 0.0426 | False | 2026-11-09T06:56:58Z |
| draftkings|385785493|0QA385785493#2349815405_13L88808Q11811847572Q20 | draftkings | T.J. Hockenson | 2+ TDs | over | 0.0946 | 0.0526 | 0.0419 | False | 2026-11-09T06:56:58Z |
