# Props Pipeline Digest -- 2026-11-11T06:50:17Z

## Run summary
- DraftKings ingestion: 496 rows across 8 events (OK)
- FanDuel ingestion: 0 rows (OK)
- BetMGM ingestion (via Rotowire): 179 rows (OK)
- Estimation: 675 rows written (from 675 ingested rows) -- status breakdown: {'estimated': 371, 'unsupported_market_first_scorer': 164, 'no_player_match': 77, 'unsupported_stat_type': 47, 'insufficient_history': 16}
- CLV logging: 33 newly flagged, 0 newly closed, 60 still open (1528 total ever logged)

## Currently open flags
Sizing is a manual step (`sizing_engine.py props size`, Session 6.4) -- this table is what to scan to pick a flag worth sizing. `implied_prob_includes_field_vig` matters here more than for the other tracks: a row still reporting True carries a real, separate uncertainty (Session 6.4's `PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER` dampener) that a bigger raw edge number does not describe.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_model_prob | first_flagged_market_price | first_flagged_edge | implied_prob_includes_field_vig | first_flagged_at |
|---|---|---|---|---|---|---|---|---|---|
| betmgm|anytd|19258 | betmgm | Jack Endries | anytd | over | 0.3677 | 0.0714 | 0.2962 | False | 2026-11-10T21:54:10Z |
| draftkings|387480437|0QA387480437#2357394470_13L88808Q1-115201972Q20 | draftkings | Van Jefferson | Anytime TD Scorer | over | 0.4182 | 0.1333 | 0.2849 | False | 2026-11-09T06:56:58Z |
| draftkings|387839216|0QA387839216#2359644663_13L88808Q1877705888Q20 | draftkings | Kirk Cousins | Anytime TD Scorer | over | 0.3371 | 0.0667 | 0.2704 | False | 2026-11-10T21:54:10Z |
| betmgm|anytd|14430 | betmgm | Van Jefferson | anytd | over | 0.4182 | 0.1538 | 0.2644 | False | 2026-11-10T12:50:30Z |
| draftkings|387480437|0QA387480437#2357394454_13L88808Q1-1809117535Q20 | draftkings | Isaiah Likely | Anytime TD Scorer | over | 0.537 | 0.3333 | 0.2037 | False | 2026-11-09T06:56:58Z |
| draftkings|387569245|0QA387569245#2357803430_13L88808Q11057552796Q20 | draftkings | Tank Dell | Anytime TD Scorer | over | 0.4182 | 0.2174 | 0.2008 | False | 2026-11-11T06:50:29Z |
| draftkings|388106515|0QA388106515#2360258724_13L88808Q11612572832Q20 | draftkings | Tony Pollard | 2+ TDs | over | 0.3156 | 0.1333 | 0.1823 | False | 2026-11-11T06:50:29Z |
| draftkings|387839216|0QA387839216#2359067390_13L88808Q1-1213243313Q20 | draftkings | Jordan Love | Anytime TD Scorer | over | 0.2926 | 0.1111 | 0.1815 | False | 2026-11-10T21:54:10Z |
| draftkings|387584920|0QA387584920#2357860056_13L88808Q1410823711Q20 | draftkings | Tony Pollard | Anytime TD Scorer | over | 0.6802 | 0.5 | 0.1802 | False | 2026-11-10T21:54:10Z |
| draftkings|387554294|0QA387554294#2357739847_13L88808Q1480222870Q20 | draftkings | Jameson Williams | Anytime TD Scorer | over | 0.5312 | 0.3571 | 0.174 | False | 2026-11-09T18:58:36Z |
| draftkings|387560840|0QA387560840#2357763167_13L88808Q1641834418Q20 | draftkings | Emmett Johnson | Anytime TD Scorer | over | 0.3462 | 0.1818 | 0.1644 | False | 2026-11-11T06:50:29Z |
| draftkings|387569245|0QA387569245#2357803427_13L88808Q1-1444150535Q20 | draftkings | Xavier Hutchinson | Anytime TD Scorer | over | 0.3462 | 0.1818 | 0.1644 | False | 2026-11-11T06:50:29Z |
| draftkings|387584920|0QA387584920#2357860077_13L88808Q1-292926888Q20 | draftkings | Nate Boerkircher | Anytime TD Scorer | over | 0.3078 | 0.1538 | 0.1539 | False | 2026-11-11T06:50:29Z |
| draftkings|387584920|0QA387584920#2357860072_13L88808Q1-271780635Q20 | draftkings | Brian Thomas Jr. | Anytime TD Scorer | over | 0.3147 | 0.1667 | 0.148 | False | 2026-11-11T06:50:29Z |
| draftkings|388114674|0QA388114674#2360300202_13L88808Q1917552914Q20 | draftkings | Kenneth Walker III | 2+ TDs | over | 0.4125 | 0.2667 | 0.1458 | False | 2026-11-11T06:50:29Z |
| draftkings|387584920|0QA387584920#2357860062_13L88808Q11807508626Q20 | draftkings | Chimere Dike | Anytime TD Scorer | over | 0.2114 | 0.0714 | 0.14 | False | 2026-11-11T06:50:29Z |
| draftkings|387480437|0QA387480437#2357394460_13L88808Q1-534343686Q20 | draftkings | Theo Johnson | Anytime TD Scorer | over | 0.2296 | 0.0909 | 0.1387 | False | 2026-11-09T06:56:58Z |
| draftkings|387560840|0QA387560840#2357763156_13L88808Q1-1356990742Q20 | draftkings | Charlie Woerner | Anytime TD Scorer | over | 0.2277 | 0.0909 | 0.1368 | False | 2026-11-11T06:50:29Z |
| draftkings|387560840|0QA387560840#2357763152_13L88808Q1999478588Q20 | draftkings | Kyle Pitts Sr. | Anytime TD Scorer | over | 0.3826 | 0.25 | 0.1326 | False | 2026-11-09T18:58:36Z |
| draftkings|387560840|0QA387560840#2357763160_13L88808Q11180641602Q20 | draftkings | Nick Muse | Anytime TD Scorer | over | 0.1575 | 0.0323 | 0.1253 | False | 2026-11-11T06:50:29Z |
| draftkings|387487626|0QA387487626#2357440084_13L88808Q1-861767826Q20 | draftkings | Isaiah Likely | 2+ TDs | over | 0.1805 | 0.0588 | 0.1216 | False | 2026-11-09T06:56:58Z |
| draftkings|387569930|0QA387569930#2357806207_13L88808Q1-106544391Q20 | draftkings | Jameson Williams | 2+ TDs | over | 0.176 | 0.0667 | 0.1094 | False | 2026-11-09T18:58:36Z |
| draftkings|387480437|0QA387480437#2357394468_13L88808Q1622596392Q20 | draftkings | Stefon Diggs | Anytime TD Scorer | over | 0.4413 | 0.3333 | 0.108 | False | 2026-11-09T06:56:58Z |
| draftkings|387839216|0QA387839216#2359067539_13L88808Q11154264979Q20 | draftkings | Savion Williams | Anytime TD Scorer | over | 0.2704 | 0.1667 | 0.1037 | False | 2026-11-11T06:50:29Z |
| draftkings|387554294|0QA387554294#2357739859_13L88808Q1-205213128Q20 | draftkings | Demario Douglas | Anytime TD Scorer | over | 0.3857 | 0.2899 | 0.0958 | False | 2026-11-09T18:58:36Z |
| draftkings|387584920|0QA387584920#2357860073_13L88808Q11137102484Q20 | draftkings | Chris Rodriguez Jr. | Anytime TD Scorer | over | 0.4457 | 0.3509 | 0.0948 | False | 2026-11-11T06:50:29Z |
| draftkings|387839216|0QA387839216#2359067536_13L88808Q11480921309Q20 | draftkings | Matthew Golden | Anytime TD Scorer | over | 0.4715 | 0.3774 | 0.0942 | False | 2026-11-11T06:50:29Z |
| draftkings|387839216|0QA387839216#2359067535_13L88808Q1-135035926Q20 | draftkings | MarShawn Lloyd | Anytime TD Scorer | over | 0.2647 | 0.1739 | 0.0908 | False | 2026-11-11T06:50:29Z |
| draftkings|387487626|0QA387487626#2357440099_13L88808Q11585686638Q20 | draftkings | Van Jefferson | 2+ TDs | over | 0.1031 | 0.0123 | 0.0907 | False | 2026-11-09T06:56:58Z |
| draftkings|387554294|0QA387554294#2357739821_13L88808Q1-725127430Q20 | draftkings | Drake Maye | Anytime TD Scorer | over | 0.3506 | 0.2632 | 0.0874 | False | 2026-11-09T18:58:36Z |
| draftkings|388124749|0QA388124749#2360343096_13L88808Q1183535264Q20 | draftkings | Tank Dell | 2+ TDs | over | 0.1031 | 0.0278 | 0.0753 | False | 2026-11-11T06:50:29Z |
| draftkings|387584920|0QA387584920#2357860057_13L88808Q117668529Q20 | draftkings | Wan'Dale Robinson | Anytime TD Scorer | over | 0.3314 | 0.2597 | 0.0716 | False | 2026-11-09T18:58:36Z |
| draftkings|387560840|0QA387560840#2357763163_13L88808Q1-1856213575Q20 | draftkings | Noah Gray | Anytime TD Scorer | over | 0.171 | 0.1 | 0.071 | False | 2026-11-11T06:50:29Z |
| draftkings|388106515|0QA388106515#2360258784_13L88808Q1163343434Q20 | draftkings | Bhayshul Tuten | 2+ TDs | over | 0.2872 | 0.2222 | 0.065 | False | 2026-11-11T06:50:29Z |
| draftkings|387839216|0QA387839216#2359067550_13L88808Q1122147185Q20 | draftkings | T.J. Hockenson | Anytime TD Scorer | over | 0.338 | 0.274 | 0.064 | False | 2026-11-11T06:50:29Z |
| draftkings|388074738|0QA388074738#2360070114_13L88808Q1905210328Q20 | draftkings | Matthew Golden | 2+ TDs | over | 0.1345 | 0.0714 | 0.0631 | False | 2026-11-11T06:50:29Z |
| draftkings|387569245|0QA387569245#2357803412_13L88808Q1466829631Q20 | draftkings | Harold Fannin Jr. | Anytime TD Scorer | over | 0.3278 | 0.2667 | 0.0611 | False | 2026-11-09T18:58:36Z |
| draftkings|387487626|0QA387487626#2357440096_13L88808Q1-60147958Q20 | draftkings | Stefon Diggs | 2+ TDs | over | 0.1161 | 0.0556 | 0.0605 | False | 2026-11-09T06:56:58Z |
| draftkings|387480437|0QA387480437#2357423649_13L88808Q1557870560Q20 | draftkings | Treylon Burks | Anytime TD Scorer | over | 0.2341 | 0.1739 | 0.0602 | False | 2026-11-09T06:56:58Z |
| draftkings|387554294|0QA387554294#2357739860_13L88808Q11958986630Q20 | draftkings | Kyle Williams | Anytime TD Scorer | over | 0.2413 | 0.1818 | 0.0595 | False | 2026-11-09T18:58:36Z |
| draftkings|388074738|0QA388074738#2360070135_13L88808Q1-1049669903Q20 | draftkings | Kirk Cousins | 2+ TDs | over | 0.0646 | 0.0055 | 0.059 | False | 2026-11-11T06:50:29Z |
| draftkings|387839216|0QA387839216#2359067534_13L88808Q1-1411527739Q20 | draftkings | Christian Watson | Anytime TD Scorer | over | 0.4748 | 0.4167 | 0.0581 | False | 2026-11-11T06:50:29Z |
| draftkings|387560840|0QA387560840#2357763157_13L88808Q1-189550648Q20 | draftkings | Austin Hooper | Anytime TD Scorer | over | 0.116 | 0.0625 | 0.0535 | False | 2026-11-11T06:50:29Z |
| draftkings|388106515|0QA388106515#2360258788_13L88808Q1-1327690156Q20 | draftkings | Chris Rodriguez Jr. | 2+ TDs | over | 0.1186 | 0.0667 | 0.052 | False | 2026-11-11T06:50:29Z |
| draftkings|388124749|0QA388124749#2360343094_13L88808Q11497747421Q20 | draftkings | Xavier Hutchinson | 2+ TDs | over | 0.0684 | 0.0179 | 0.0505 | False | 2026-11-11T06:50:29Z |
| draftkings|387554294|0QA387554294#2357739852_13L88808Q1-1939996255Q20 | draftkings | Jared Goff | Anytime TD Scorer | over | 0.1153 | 0.0667 | 0.0486 | False | 2026-11-09T18:58:36Z |
| draftkings|388114674|0QA388114674#2360300206_13L88808Q11061329834Q20 | draftkings | Emmett Johnson | 2+ TDs | over | 0.0684 | 0.0217 | 0.0466 | False | 2026-11-11T06:50:29Z |
| draftkings|387554294|0QA387554294#2357739862_13L88808Q1-2056923875Q20 | draftkings | Efton Chism III | Anytime TD Scorer | over | 0.2592 | 0.2128 | 0.0464 | False | 2026-11-09T18:58:36Z |
| draftkings|388074738|0QA388074738#2360070112_13L88808Q1-1356601652Q20 | draftkings | Christian Watson | 2+ TDs | over | 0.1366 | 0.0909 | 0.0456 | False | 2026-11-11T06:50:29Z |
| draftkings|387480437|0QA387480437#2357394400_13L88808Q11930260006Q20 | draftkings | Devin Singletary | Anytime TD Scorer | over | 0.3058 | 0.2632 | 0.0426 | False | 2026-11-09T06:56:58Z |
| draftkings|388114674|0QA388114674#2360300192_13L88808Q1-703917339Q20 | draftkings | Kyle Pitts Sr. | 2+ TDs | over | 0.0849 | 0.0435 | 0.0414 | False | 2026-11-11T06:50:29Z |
| draftkings|388124749|0QA388124749#2360343048_13L88808Q1-721675132Q20 | draftkings | Nico Collins | 2+ TDs | over | 0.1181 | 0.0769 | 0.0412 | False | 2026-11-11T06:50:29Z |
| draftkings|388106515|0QA388106515#2360258790_13L88808Q11304672355Q20 | draftkings | Brian Thomas Jr. | 2+ TDs | over | 0.0557 | 0.0164 | 0.0393 | False | 2026-11-11T06:50:29Z |
| draftkings|388074738|0QA388074738#2360070119_13L88808Q1-95410103Q20 | draftkings | Jordan Love | 2+ TDs | over | 0.0477 | 0.009 | 0.0387 | False | 2026-11-11T06:50:29Z |
| draftkings|387569930|0QA387569930#2357806218_13L88808Q1573901773Q20 | draftkings | Demario Douglas | 2+ TDs | over | 0.0864 | 0.0476 | 0.0387 | False | 2026-11-09T18:58:36Z |
| draftkings|388106515|0QA388106515#2360258726_13L88808Q1-1987217340Q20 | draftkings | Wan'Dale Robinson | 2+ TDs | over | 0.0622 | 0.0244 | 0.0378 | False | 2026-11-11T06:50:29Z |
| draftkings|387569245|0QA387569245#2357803424_13L88808Q11759839095Q20 | draftkings | Nico Collins | Anytime TD Scorer | over | 0.4447 | 0.4082 | 0.0366 | False | 2026-11-09T18:58:36Z |
| draftkings|388124602|0QA388124602#2360342526_13L88808Q1503159412Q20 | draftkings | James Cook | 2+ TDs | over | 0.2863 | 0.25 | 0.0363 | False | 2026-11-11T06:50:29Z |
| draftkings|387569930|0QA387569930#2357806219_13L88808Q11724982079Q20 | draftkings | Drake Maye | 2+ TDs | over | 0.0702 | 0.0345 | 0.0358 | False | 2026-11-09T18:58:36Z |
| draftkings|388106515|0QA388106515#2360258793_13L88808Q1-1058483772Q20 | draftkings | Nate Boerkircher | 2+ TDs | over | 0.0531 | 0.0179 | 0.0353 | False | 2026-11-11T06:50:29Z |
