# Props Pipeline Digest -- 2026-11-03T19:40:32Z

## Run summary
- DraftKings ingestion: 269 rows across 8 events (OK)
- FanDuel ingestion: 0 rows (OK)
- BetMGM ingestion (via Rotowire): 216 rows (OK)
- Estimation: 485 rows written (from 485 ingested rows) -- status breakdown: {'estimated': 323, 'unsupported_market_first_scorer': 96, 'no_player_match': 28, 'unsupported_stat_type': 27, 'insufficient_history': 11}
- CLV logging: 11 newly flagged, 0 newly closed, 46 still open (1401 total ever logged)

## Currently open flags
Sizing is a manual step (`sizing_engine.py props size`, Session 6.4) -- this table is what to scan to pick a flag worth sizing. `implied_prob_includes_field_vig` matters here more than for the other tracks: a row still reporting True carries a real, separate uncertainty (Session 6.4's `PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER` dampener) that a bigger raw edge number does not describe.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_model_prob | first_flagged_market_price | first_flagged_edge | implied_prob_includes_field_vig | first_flagged_at |
|---|---|---|---|---|---|---|---|---|---|
| betmgm|recs|18578 | betmgm | Travis Hunter | recs | over | 0.9998 | 0.3587 | 0.6411 | False | 2026-11-03T12:08:57Z |
| draftkings|385025617|0QA385025617#2346198696_13L88808Q1-1846552455Q20 | draftkings | Mike Gesicki | Anytime TD Scorer | over | 0.6321 | 0.2817 | 0.3504 | False | 2026-11-02T18:35:10Z |
| draftkings|385032605|0QA385032605#2346227941_13L88808Q1-577361648Q20 | draftkings | Nate Adkins | Anytime TD Scorer | over | 0.4701 | 0.1333 | 0.3367 | False | 2026-11-03T19:40:49Z |
| draftkings|385025617|0QA385025617#2346198681_13L88808Q1999478588Q20 | draftkings | Kyle Pitts Sr. | Anytime TD Scorer | over | 0.4701 | 0.2326 | 0.2375 | False | 2026-11-02T18:35:10Z |
| betmgm|anytd|13582 | betmgm | Josh Jacobs | anytd | over | 0.786 | 0.5556 | 0.2304 | False | 2026-11-03T12:08:57Z |
| draftkings|385070262|0QA385070262#2346502179_13L88808Q1480222870Q20 | draftkings | Jameson Williams | Anytime TD Scorer | over | 0.6255 | 0.4082 | 0.2173 | False | 2026-11-02T18:35:10Z |
| draftkings|385020238|0QA385020238#2346168574_13L88808Q11230695518Q20 | draftkings | Bhayshul Tuten | Anytime TD Scorer | over | 0.6565 | 0.4444 | 0.2121 | False | 2026-11-02T06:30:02Z |
| draftkings|385340515|0QA385340515#2347869309_13L88808Q1-1016060448Q20 | draftkings | Mike Gesicki | 2+ TDs | over | 0.2642 | 0.0556 | 0.2087 | False | 2026-11-03T12:08:57Z |
| draftkings|385020238|0QA385020238#2346168583_13L88808Q1-292926888Q20 | draftkings | Nate Boerkircher | Anytime TD Scorer | over | 0.3729 | 0.1667 | 0.2062 | False | 2026-11-02T06:30:02Z |
| draftkings|385047734|0QA385047734#2346301467_13L88808Q1622596392Q20 | draftkings | Stefon Diggs | Anytime TD Scorer | over | 0.5492 | 0.3448 | 0.2043 | False | 2026-11-02T18:35:10Z |
| draftkings|385032605|0QA385032605#2346227863_13L88808Q11890020597Q20 | draftkings | Anthony Tyus III | Anytime TD Scorer | over | 0.2296 | 0.0435 | 0.1861 | False | 2026-11-03T19:40:49Z |
| draftkings|385105249|0QA385105249#2346697217_13L88808Q1163343434Q20 | draftkings | Bhayshul Tuten | 2+ TDs | over | 0.2894 | 0.1053 | 0.1842 | False | 2026-11-02T06:30:02Z |
| draftkings|385028912|0QA385028912#2346210928_13L88808Q1-1809117535Q20 | draftkings | Isaiah Likely | Anytime TD Scorer | over | 0.4945 | 0.3125 | 0.182 | False | 2026-11-03T12:08:57Z |
| draftkings|385025617|0QA385025617#2346198700_13L88808Q1219777051Q20 | draftkings | Joe Burrow | Anytime TD Scorer | over | 0.3147 | 0.1538 | 0.1608 | False | 2026-11-03T12:08:57Z |
| draftkings|385020238|0QA385020238#2346168569_13L88808Q1-1199795272Q20 | draftkings | Devontez Walker | Anytime TD Scorer | over | 0.2015 | 0.0556 | 0.1459 | False | 2026-11-02T06:30:02Z |
| draftkings|385025617|0QA385025617#2346198702_13L88808Q1-409986828Q20 | draftkings | Drew Sample | Anytime TD Scorer | over | 0.2704 | 0.125 | 0.1454 | False | 2026-11-03T12:08:57Z |
| draftkings|385025617|0QA385025617#2346198691_13L88808Q11180641602Q20 | draftkings | Nick Muse | Anytime TD Scorer | over | 0.1881 | 0.0435 | 0.1446 | False | 2026-11-03T12:08:57Z |
| draftkings|385020238|0QA385020238#2346168578_13L88808Q1-271780635Q20 | draftkings | Brian Thomas Jr. | Anytime TD Scorer | over | 0.3147 | 0.1818 | 0.1329 | False | 2026-11-02T06:30:02Z |
| draftkings|385568967|0QA385568967#2348975280_13L88808Q1-1564766902Q20 | draftkings | Nate Adkins | 2+ TDs | over | 0.1336 | 0.0132 | 0.1204 | False | 2026-11-03T19:40:49Z |
| draftkings|385020238|0QA385020238#2346168579_13L88808Q11137102484Q20 | draftkings | Chris Rodriguez Jr. | Anytime TD Scorer | over | 0.3869 | 0.274 | 0.113 | False | 2026-11-02T06:30:02Z |
| draftkings|385020238|0QA385020238#2346168570_13L88808Q11714132096Q20 | draftkings | Josh Cuevas | Anytime TD Scorer | over | 0.1675 | 0.0556 | 0.112 | False | 2026-11-02T06:30:02Z |
| draftkings|385032605|0QA385032605#2346227926_13L88808Q1-813345382Q20 | draftkings | Tommy Tremble | Anytime TD Scorer | over | 0.2903 | 0.1905 | 0.0998 | False | 2026-11-03T19:40:49Z |
| draftkings|385070262|0QA385070262#2346502164_13L88808Q11579636272Q20 | draftkings | Malik Willis | Anytime TD Scorer | over | 0.3555 | 0.2597 | 0.0958 | False | 2026-11-02T18:35:10Z |
| draftkings|385340515|0QA385340515#2347869298_13L88808Q1-703917339Q20 | draftkings | Kyle Pitts Sr. | 2+ TDs | over | 0.1336 | 0.0385 | 0.0951 | False | 2026-11-03T12:08:57Z |
| draftkings|385020238|0QA385020238#2346168561_13L88808Q1-660534674Q20 | draftkings | Derrick Henry | Anytime TD Scorer | over | 0.5672 | 0.4762 | 0.091 | False | 2026-11-03T19:40:49Z |
| draftkings|385020238|0QA385020238#2346168568_13L88808Q1-700661814Q20 | draftkings | Matthew Hibner | Anytime TD Scorer | over | 0.1479 | 0.0625 | 0.0854 | False | 2026-11-02T06:30:02Z |
| draftkings|385032605|0QA385032605#2346227923_13L88808Q1294436062Q20 | draftkings | Darren Waller | Anytime TD Scorer | over | 0.2877 | 0.2041 | 0.0836 | False | 2026-11-03T19:40:49Z |
| draftkings|385032605|0QA385032605#2346227933_13L88808Q11696076099Q20 | draftkings | J.K. Dobbins | Anytime TD Scorer | over | 0.3766 | 0.2941 | 0.0824 | False | 2026-11-03T19:40:49Z |
| draftkings|385025617|0QA385025617#2346198695_13L88808Q1106346443Q20 | draftkings | Tee Higgins | Anytime TD Scorer | over | 0.551 | 0.4762 | 0.0748 | False | 2026-11-02T18:35:10Z |
| draftkings|385340515|0QA385340515#2347869308_13L88808Q1-1865349726Q20 | draftkings | Tee Higgins | 2+ TDs | over | 0.1915 | 0.125 | 0.0665 | False | 2026-11-03T12:08:57Z |
| draftkings|385020238|0QA385020238#2346168562_13L88808Q12018204784Q20 | draftkings | Zay Flowers | Anytime TD Scorer | over | 0.3156 | 0.25 | 0.0656 | False | 2026-11-02T06:30:02Z |
| draftkings|385340515|0QA385340515#2347869307_13L88808Q11526916627Q20 | draftkings | Ja'Marr Chase | 2+ TDs | over | 0.216 | 0.1538 | 0.0622 | False | 2026-11-03T12:08:57Z |
| draftkings|385105249|0QA385105249#2346697225_13L88808Q1-1058483772Q20 | draftkings | Nate Boerkircher | 2+ TDs | over | 0.0803 | 0.0196 | 0.0607 | False | 2026-11-02T06:30:02Z |
| draftkings|385568967|0QA385568967#2348975176_13L88808Q1-2084365438Q20 | draftkings | Chuba Hubbard | 2+ TDs | over | 0.2257 | 0.1667 | 0.059 | False | 2026-11-03T19:40:49Z |
| draftkings|385105249|0QA385105249#2346697203_13L88808Q11746484724Q20 | draftkings | Derrick Henry | 2+ TDs | over | 0.2047 | 0.1538 | 0.0509 | False | 2026-11-02T06:30:02Z |
| draftkings|385047734|0QA385047734#2346301464_13L88808Q1968442089Q20 | draftkings | Rachaad White | Anytime TD Scorer | over | 0.4566 | 0.4082 | 0.0485 | False | 2026-11-02T18:35:10Z |
| draftkings|385025617|0QA385025617#2346198697_13L88808Q11111630045Q20 | draftkings | Samaje Perine | Anytime TD Scorer | over | 0.3078 | 0.2597 | 0.048 | False | 2026-11-03T12:08:57Z |
| draftkings|385070262|0QA385070262#2346502163_13L88808Q1354446541Q20 | draftkings | Ollie Gordon II | Anytime TD Scorer | over | 0.4823 | 0.4348 | 0.0475 | False | 2026-11-02T18:35:10Z |
| draftkings|385105249|0QA385105249#2346697220_13L88808Q1-1327690156Q20 | draftkings | Chris Rodriguez Jr. | 2+ TDs | over | 0.087 | 0.0435 | 0.0435 | False | 2026-11-02T06:30:02Z |
| draftkings|385047734|0QA385047734#2346301465_13L88808Q1111756323Q20 | draftkings | Jayden Daniels | Anytime TD Scorer | over | 0.3297 | 0.2899 | 0.0398 | False | 2026-11-02T18:35:10Z |
| draftkings|385340515|0QA385340515#2347869312_13L88808Q1158576549Q20 | draftkings | Joe Burrow | 2+ TDs | over | 0.0557 | 0.0164 | 0.0393 | False | 2026-11-03T12:08:57Z |
| draftkings|385105249|0QA385105249#2346697224_13L88808Q11304672355Q20 | draftkings | Brian Thomas Jr. | 2+ TDs | over | 0.0557 | 0.0179 | 0.0379 | False | 2026-11-02T06:30:02Z |
| draftkings|385020238|0QA385020238#2346168580_13L88808Q1-458881524Q20 | draftkings | Travis Hunter | Anytime TD Scorer | over | 0.1783 | 0.1429 | 0.0355 | False | 2026-11-02T06:30:02Z |
| draftkings|385568967|0QA385568967#2348975272_13L88808Q1-1048311142Q20 | draftkings | J.K. Dobbins | 2+ TDs | over | 0.082 | 0.0476 | 0.0344 | False | 2026-11-03T19:40:49Z |
| draftkings|385020238|0QA385020238#2346168581_13L88808Q11380693923Q20 | draftkings | Josh Cameron | Anytime TD Scorer | over | 0.1671 | 0.1333 | 0.0338 | False | 2026-11-03T19:40:49Z |
| draftkings|385032605|0QA385032605#2346227921_13L88808Q1-537154100Q20 | draftkings | Jalen Coker | Anytime TD Scorer | over | 0.3462 | 0.3125 | 0.0337 | False | 2026-11-03T19:40:49Z |
