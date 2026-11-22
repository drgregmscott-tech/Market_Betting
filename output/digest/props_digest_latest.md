# Props Pipeline Digest -- 2026-11-22T16:29:32Z

## Run summary
- DraftKings ingestion: 708 rows across 8 events (OK)
- FanDuel ingestion: 0 rows (OK)
- BetMGM ingestion (via Rotowire): 1044 rows (OK)
- Estimation: 1752 rows written (from 1752 ingested rows) -- status breakdown: {'estimated': 790, 'unsupported_market_first_scorer': 468, 'unsupported_stat_type': 344, 'no_player_match': 112, 'insufficient_history': 38}
- CLV logging: 1 newly flagged, 0 newly closed, 78 still open (1694 total ever logged)

## Currently open flags
Sizing is a manual step (`sizing_engine.py props size`, Session 6.4) -- this table is what to scan to pick a flag worth sizing. `implied_prob_includes_field_vig` matters here more than for the other tracks: a row still reporting True carries a real, separate uncertainty (Session 6.4's `PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER` dampener) that a bigger raw edge number does not describe.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_model_prob | first_flagged_market_price | first_flagged_edge | implied_prob_includes_field_vig | first_flagged_at |
|---|---|---|---|---|---|---|---|---|---|
| draftkings|389654195|0QA389654195#2367448007_13L88808Q1-438304181Q20 | draftkings | Teagan Quitoriano | Anytime TD Scorer | over | 0.6002 | 0.0278 | 0.5724 | False | 2026-11-18T07:45:59Z |
| betmgm|recs|19233 | betmgm | Jordyn Tyson | recs | over | 1.0 | 0.4797 | 0.5203 | False | 2026-11-19T01:58:02Z |
| betmgm|recs|16105 | betmgm | Bam Knight | recs | over | 1.0 | 0.5446 | 0.4554 | False | 2026-11-19T23:15:09Z |
| draftkings|389625756|0QA389625756#2367262286_13L88808Q11055160431Q20 | draftkings | Alvin Kamara | Anytime TD Scorer | over | 0.5145 | 0.2 | 0.3145 | False | 2026-11-17T23:36:43Z |
| draftkings|389757758|0QA389757758#2367965641_13L88808Q11402568200Q20 | draftkings | Pat Freiermuth | Anytime TD Scorer | over | 0.51 | 0.2273 | 0.2827 | False | 2026-11-18T17:25:01Z |
| betmgm|anytd|19281 | betmgm | Fernando Mendoza | anytd | over | 0.4182 | 0.1429 | 0.2754 | False | 2026-11-18T07:45:59Z |
| draftkings|389635554|0QA389635554#2367321467_13L88808Q1666446492Q20 | draftkings | Bucky Irving | Anytime TD Scorer | over | 0.6986 | 0.4444 | 0.2542 | False | 2026-11-18T07:45:59Z |
| draftkings|389625756|0QA389625756#2367262291_13L88808Q1214033643Q20 | draftkings | Audric Estime | Anytime TD Scorer | over | 0.4591 | 0.2083 | 0.2508 | False | 2026-11-17T23:36:43Z |
| draftkings|390324753|0QA390324753#2370426262_13L88808Q1-416383636Q20 | draftkings | Bucky Irving | 2+ TDs | over | 0.3372 | 0.1 | 0.2372 | False | 2026-11-18T07:45:59Z |
| draftkings|389627988|0QA389627988#2367276119_13L88808Q11222312202Q20 | draftkings | Jalen Tolbert | Anytime TD Scorer | over | 0.2704 | 0.0556 | 0.2148 | False | 2026-11-17T13:42:12Z |
| betmgm|anytd|18573 | betmgm | Gavin Bartholomew | anytd | over | 0.2704 | 0.0769 | 0.1934 | False | 2026-11-21T12:51:53Z |
| betmgm|anytd|18453 | betmgm | Andrew Armstrong | anytd | over | 0.2404 | 0.0476 | 0.1928 | False | 2026-11-18T17:25:01Z |
| draftkings|389654195|0QA389654195#2367447996_13L88808Q1-985183007Q20 | draftkings | Andrew Armstrong | Anytime TD Scorer | over | 0.2404 | 0.0526 | 0.1878 | False | 2026-11-18T07:45:59Z |
| draftkings|389635554|0QA389635554#2367321475_13L88808Q11141276074Q20 | draftkings | Sean Tucker | Anytime TD Scorer | over | 0.2882 | 0.1111 | 0.1771 | False | 2026-11-18T07:45:59Z |
| draftkings|389757758|0QA389757758#2371283317_13L88808Q11665380004Q20 | draftkings | Roman Wilson | Anytime TD Scorer | over | 0.3462 | 0.1739 | 0.1723 | False | 2026-11-19T01:58:02Z |
| draftkings|389757758|0QA389757758#2367965645_13L88808Q1292660006Q20 | draftkings | Ben Skowronek | Anytime TD Scorer | over | 0.2084 | 0.0435 | 0.1649 | False | 2026-11-18T17:25:01Z |
| draftkings|389757758|0QA389757758#2367965626_13L88808Q1-911882280Q20 | draftkings | DeVonta Smith | Anytime TD Scorer | over | 0.4224 | 0.2667 | 0.1558 | False | 2026-11-18T07:45:59Z |
| draftkings|389646238|0QA389646238#2367386934_13L88808Q1-1199795272Q20 | draftkings | Devontez Walker | Anytime TD Scorer | over | 0.2015 | 0.0476 | 0.1539 | False | 2026-11-18T07:45:59Z |
| draftkings|390259474|0QA390259474#2370023952_13L88808Q11612572832Q20 | draftkings | Tony Pollard | 2+ TDs | over | 0.3061 | 0.1667 | 0.1394 | False | 2026-11-18T07:45:59Z |
| draftkings|390277636|0QA390277636#2370133597_13L88808Q1839820985Q20 | draftkings | Alvin Kamara | 2+ TDs | over | 0.1637 | 0.0244 | 0.1393 | False | 2026-11-18T07:45:59Z |
| draftkings|390226233|0QA390226233#2369858152_13L88808Q1433051443Q20 | draftkings | Jeremy Ruckert | Anytime TD Scorer | over | 0.1813 | 0.0435 | 0.1378 | False | 2026-11-20T07:34:12Z |
| draftkings|389757758|0QA389757758#2367965630_13L88808Q11627968604Q20 | draftkings | Darius Cooper | Anytime TD Scorer | over | 0.2307 | 0.0952 | 0.1354 | False | 2026-11-18T17:25:01Z |
| draftkings|389635554|0QA389635554#2367321456_13L88808Q1480222870Q20 | draftkings | Jameson Williams | Anytime TD Scorer | over | 0.4389 | 0.3077 | 0.1312 | False | 2026-11-16T18:44:30Z |
| draftkings|389757758|0QA389757758#2374195385_13L88808Q197731504Q20 | draftkings | Will Shipley | Anytime TD Scorer | over | 0.2404 | 0.1111 | 0.1293 | False | 2026-11-22T07:09:56Z |
| draftkings|390474625|0QA390474625#2371008754_13L88808Q1-162258478Q20 | draftkings | Pat Freiermuth | 2+ TDs | over | 0.1605 | 0.0323 | 0.1282 | False | 2026-11-18T17:25:01Z |
| draftkings|389627988|0QA389627988#2367276104_13L88808Q11235745545Q20 | draftkings | Keleki Latu | Anytime TD Scorer | over | 0.171 | 0.0435 | 0.1275 | False | 2026-11-17T13:42:12Z |
| betmgm|anytd|18906 | betmgm | Keleki Latu | anytd | over | 0.171 | 0.0435 | 0.1275 | False | 2026-11-17T13:42:12Z |
| draftkings|389635554|0QA389635554#2367321468_13L88808Q1621783265Q20 | draftkings | Emeka Egbuka | Anytime TD Scorer | over | 0.3555 | 0.2439 | 0.1116 | False | 2026-11-18T07:45:59Z |
| draftkings|389625756|0QA389625756#2367262289_13L88808Q1873985604Q20 | draftkings | Juwan Johnson | Anytime TD Scorer | over | 0.2934 | 0.1818 | 0.1115 | False | 2026-11-17T23:36:43Z |
| draftkings|390277636|0QA390277636#2370133595_13L88808Q11659488704Q20 | draftkings | Audric Estime | 2+ TDs | over | 0.1267 | 0.0217 | 0.105 | False | 2026-11-18T07:45:59Z |
| draftkings|390277636|0QA390277636#2370133580_13L88808Q1-1008695778Q20 | draftkings | D'Andre Swift | 2+ TDs | over | 0.334 | 0.2326 | 0.1014 | False | 2026-11-18T07:45:59Z |
| betmgm|anytd|17802 | betmgm | Will Shipley | anytd | over | 0.2404 | 0.1429 | 0.0976 | False | 2026-11-21T12:51:53Z |
| draftkings|389646238|0QA389646238#2367386916_13L88808Q1294436062Q20 | draftkings | Darren Waller | Anytime TD Scorer | over | 0.3345 | 0.2381 | 0.0964 | False | 2026-11-18T07:45:59Z |
| draftkings|390259474|0QA390259474#2370023942_13L88808Q11452024780Q20 | draftkings | George Pickens | 2+ TDs | over | 0.2432 | 0.1538 | 0.0894 | False | 2026-11-18T07:45:59Z |
| draftkings|389646238|0QA389646238#2367386917_13L88808Q1-813345382Q20 | draftkings | Tommy Tremble | Anytime TD Scorer | over | 0.3104 | 0.2222 | 0.0882 | False | 2026-11-18T07:45:59Z |
| draftkings|389654195|0QA389654195#2367447998_13L88808Q12101047025Q20 | draftkings | Tyler Allgeier | Anytime TD Scorer | over | 0.2953 | 0.2083 | 0.087 | False | 2026-11-18T17:25:01Z |
| draftkings|389646238|0QA389646238#2367386924_13L88808Q11890020597Q20 | draftkings | Anthony Tyus III | Anytime TD Scorer | over | 0.1335 | 0.0476 | 0.0859 | False | 2026-11-18T07:45:59Z |
| draftkings|389625756|0QA389625756#2367262278_13L88808Q1655740791Q20 | draftkings | Kyle Monangai | Anytime TD Scorer | over | 0.5599 | 0.4762 | 0.0837 | False | 2026-11-17T23:36:43Z |
| draftkings|390324753|0QA390324753#2370426066_13L88808Q11455054237Q20 | draftkings | Jahmyr Gibbs | 2+ TDs | over | 0.4003 | 0.3175 | 0.0828 | False | 2026-11-18T07:45:59Z |
| draftkings|390226233|0QA390226233#2369858141_13L88808Q1-1123329864Q20 | draftkings | Derius Davis | Anytime TD Scorer | over | 0.1652 | 0.0833 | 0.0819 | False | 2026-11-20T07:34:12Z |
| draftkings|390277636|0QA390277636#2370133582_13L88808Q1902102257Q20 | draftkings | Kyle Monangai | 2+ TDs | over | 0.1986 | 0.1176 | 0.081 | False | 2026-11-18T07:45:59Z |
| draftkings|389627988|0QA389627988#2367276114_13L88808Q1-533028316Q20 | draftkings | Kevin Coleman Jr. | Anytime TD Scorer | over | 0.2328 | 0.1538 | 0.0789 | False | 2026-11-17T13:42:12Z |
| draftkings|390339745|0QA390339745#2370493839_13L88808Q11746484724Q20 | draftkings | Derrick Henry | 2+ TDs | over | 0.2642 | 0.1905 | 0.0738 | False | 2026-11-18T07:45:59Z |
| draftkings|390474625|0QA390474625#2371008736_13L88808Q1126691603Q20 | draftkings | DeVonta Smith | 2+ TDs | over | 0.1054 | 0.0323 | 0.0731 | False | 2026-11-18T17:25:01Z |
| betmgm|anytd|19095 | betmgm | Myles Price | anytd | over | 0.2059 | 0.1333 | 0.0726 | False | 2026-11-19T01:58:02Z |
| draftkings|389625756|0QA389625756#2367262294_13L88808Q11213714519Q20 | draftkings | Noah Fant | Anytime TD Scorer | over | 0.171 | 0.1 | 0.071 | False | 2026-11-17T23:36:43Z |
| betmgm|anytd|19607 | betmgm | Kaelon Black | anytd | over | 0.3203 | 0.25 | 0.0703 | False | 2026-11-17T13:42:12Z |
| draftkings|390339745|0QA390339745#2370493762_13L88808Q1-2084365438Q20 | draftkings | Chuba Hubbard | 2+ TDs | over | 0.2606 | 0.1905 | 0.0701 | False | 2026-11-18T07:45:59Z |
| draftkings|390324753|0QA390324753#2370426068_13L88808Q1-106544391Q20 | draftkings | Jameson Williams | 2+ TDs | over | 0.1146 | 0.05 | 0.0646 | False | 2026-11-18T07:45:59Z |
| draftkings|389654195|0QA389654195#2367447992_13L88808Q1-1195662886Q20 | draftkings | Cyrus Allen | Anytime TD Scorer | over | 0.2184 | 0.1538 | 0.0646 | False | 2026-11-18T07:45:59Z |
| draftkings|389648611|0QA389648611#2367417278_13L88808Q11550208160Q20 | draftkings | Daniel Bellinger | Anytime TD Scorer | over | 0.2059 | 0.1429 | 0.0631 | False | 2026-11-17T23:36:43Z |
| betmgm|anytd|16772 | betmgm | Roschon Johnson | anytd | over | 0.1232 | 0.0606 | 0.0626 | False | 2026-11-21T12:51:53Z |
| draftkings|389625756|0QA389625756#2367262287_13L88808Q1138922171Q20 | draftkings | Devaughn Vele | Anytime TD Scorer | over | 0.2341 | 0.1739 | 0.0602 | False | 2026-11-17T23:36:43Z |
| draftkings|389992033|0QA389992033#2368991842_13L88808Q11587218485Q20 | draftkings | Josh Allen | 2+ TDs | over | 0.3014 | 0.2439 | 0.0575 | False | 2026-11-17T13:42:12Z |
| draftkings|390474625|0QA390474625#2371283440_13L88808Q1-773934870Q20 | draftkings | Roman Wilson | 2+ TDs | over | 0.0684 | 0.0179 | 0.0505 | False | 2026-11-19T01:58:02Z |
| draftkings|389646238|0QA389646238#2367386935_13L88808Q1-700661814Q20 | draftkings | Matthew Hibner | Anytime TD Scorer | over | 0.116 | 0.0667 | 0.0494 | False | 2026-11-18T07:45:59Z |
| betmgm|anytd|19631 | betmgm | Cyrus Allen | anytd | over | 0.2184 | 0.1739 | 0.0445 | False | 2026-11-18T17:25:01Z |
| draftkings|389648611|0QA389648611#2367417260_13L88808Q1-24141105Q20 | draftkings | Ryan Flournoy | Anytime TD Scorer | over | 0.3719 | 0.3279 | 0.044 | False | 2026-11-22T16:29:49Z |
| draftkings|390324753|0QA390324753#2370426263_13L88808Q11465714566Q20 | draftkings | Emeka Egbuka | 2+ TDs | over | 0.0724 | 0.0323 | 0.0401 | False | 2026-11-18T07:45:59Z |
| draftkings|389625756|0QA389625756#2367262283_13L88808Q11750193742Q20 | draftkings | Roschon Johnson | Anytime TD Scorer | over | 0.1232 | 0.0833 | 0.0398 | False | 2026-11-17T23:36:43Z |
| draftkings|389654195|0QA389654195#2367447999_13L88808Q11587306986Q20 | draftkings | Trey McBride | Anytime TD Scorer | over | 0.3363 | 0.2985 | 0.0378 | False | 2026-11-16T18:44:30Z |
| draftkings|389625756|0QA389625756#2367262277_13L88808Q12086988331Q20 | draftkings | Luther Burden III | Anytime TD Scorer | over | 0.4632 | 0.4255 | 0.0377 | False | 2026-11-19T23:15:09Z |
| draftkings|389635554|0QA389635554#2367321457_13L88808Q11283746776Q20 | draftkings | Isaac TeSlaa | Anytime TD Scorer | over | 0.2114 | 0.1739 | 0.0375 | False | 2026-11-18T17:25:01Z |
| draftkings|390324753|0QA390324753#2370426270_13L88808Q1-1540780736Q20 | draftkings | Sean Tucker | 2+ TDs | over | 0.0462 | 0.009 | 0.0372 | False | 2026-11-18T07:45:59Z |
| draftkings|389627988|0QA389627988#2367276110_13L88808Q1-1601930688Q20 | draftkings | Caleb Douglas | Anytime TD Scorer | over | 0.2492 | 0.2128 | 0.0365 | False | 2026-11-19T23:15:09Z |
| draftkings|389992033|0QA389992033#2368991841_13L88808Q1503159412Q20 | draftkings | James Cook | 2+ TDs | over | 0.279 | 0.2439 | 0.0351 | False | 2026-11-17T13:42:12Z |
| draftkings|389757758|0QA389757758#2367965640_13L88808Q1-1532462247Q20 | draftkings | Darnell Washington | Anytime TD Scorer | over | 0.2787 | 0.2439 | 0.0348 | False | 2026-11-19T01:58:02Z |
| draftkings|389992033|0QA389992033#2368991930_13L88808Q11009072757Q20 | draftkings | Jalen Tolbert | 2+ TDs | over | 0.0404 | 0.0058 | 0.0345 | False | 2026-11-17T13:42:12Z |
| draftkings|390277636|0QA390277636#2370133584_13L88808Q1422541123Q20 | draftkings | Luther Burden III | 2+ TDs | over | 0.1293 | 0.0952 | 0.034 | False | 2026-11-18T07:45:59Z |
| draftkings|389757758|0QA389757758#2367961404_13L88808Q11750821948Q20 | draftkings | Saquon Barkley | Anytime TD Scorer | over | 0.459 | 0.4255 | 0.0334 | False | 2026-11-18T17:25:01Z |
| draftkings|390339745|0QA390339745#2370493766_13L88808Q1372601323Q20 | draftkings | Tommy Tremble | 2+ TDs | over | 0.0541 | 0.0217 | 0.0324 | False | 2026-11-18T17:25:01Z |
| draftkings|389625756|0QA389625756#2367262280_13L88808Q1-1770507643Q20 | draftkings | Jahdae Walker | Anytime TD Scorer | over | 0.08 | 0.0476 | 0.0323 | False | 2026-11-19T13:36:18Z |
| draftkings|389625756|0QA389625756#2367262290_13L88808Q11438391772Q20 | draftkings | Bryce Lance | Anytime TD Scorer | over | 0.1091 | 0.0769 | 0.0322 | False | 2026-11-17T23:36:43Z |
| draftkings|390207841|0QA390207841#2369787483_13L88808Q1-793431613Q20 | draftkings | Trey McBride | 2+ TDs | over | 0.0643 | 0.0323 | 0.032 | False | 2026-11-18T17:25:01Z |
| draftkings|390474625|0QA390474625#2371008735_13L88808Q113349962Q20 | draftkings | Saquon Barkley | 2+ TDs | over | 0.1266 | 0.0952 | 0.0314 | False | 2026-11-18T17:25:01Z |
| draftkings|390339745|0QA390339745#2370493765_13L88808Q1637812501Q20 | draftkings | Darren Waller | 2+ TDs | over | 0.0635 | 0.0323 | 0.0312 | False | 2026-11-18T07:45:59Z |
| draftkings|390226233|0QA390226233#2369858147_13L88808Q11061745166Q20 | draftkings | Mason Taylor | Anytime TD Scorer | over | 0.2311 | 0.2 | 0.0311 | False | 2026-11-20T07:34:12Z |
| draftkings|390277636|0QA390277636#2370133598_13L88808Q1-1463828113Q20 | draftkings | Juwan Johnson | 2+ TDs | over | 0.048 | 0.0179 | 0.0301 | False | 2026-11-18T07:45:59Z |
