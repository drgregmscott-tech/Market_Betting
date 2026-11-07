# Props Pipeline Digest -- 2026-11-07T23:45:33Z

## Run summary
- DraftKings ingestion: 720 rows across 8 events (OK)
- FanDuel ingestion: 0 rows (OK)
- BetMGM ingestion (via Rotowire): 1132 rows (OK)
- Estimation: 1852 rows written (from 1852 ingested rows) -- status breakdown: {'estimated': 812, 'unsupported_market_first_scorer': 496, 'unsupported_stat_type': 353, 'no_player_match': 154, 'insufficient_history': 37}
- CLV logging: 2 newly flagged, 0 newly closed, 72 still open (1451 total ever logged)

## Currently open flags
Sizing is a manual step (`sizing_engine.py props size`, Session 6.4) -- this table is what to scan to pick a flag worth sizing. `implied_prob_includes_field_vig` matters here more than for the other tracks: a row still reporting True carries a real, separate uncertainty (Session 6.4's `PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER` dampener) that a bigger raw edge number does not describe.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_model_prob | first_flagged_market_price | first_flagged_edge | implied_prob_includes_field_vig | first_flagged_at |
|---|---|---|---|---|---|---|---|---|---|
| betmgm|recs|12061 | betmgm | Tim Patrick | recs | over | 1.0 | 0.4165 | 0.5835 | False | 2026-11-07T23:45:48Z |
| betmgm|recs|19445 | betmgm | Reggie Virgil | recs | over | 0.9912 | 0.4425 | 0.5487 | False | 2026-11-07T06:17:27Z |
| betmgm|recs|13582 | betmgm | Josh Jacobs | recs | over | 1.0 | 0.5071 | 0.4929 | False | 2026-11-04T19:58:29Z |
| betmgm|recs|18536 | betmgm | Ben Yurosek | recs | over | 1.0 | 0.5575 | 0.4425 | False | 2026-11-07T23:45:48Z |
| draftkings|385025617|0QA385025617#2346198696_13L88808Q1-1846552455Q20 | draftkings | Mike Gesicki | Anytime TD Scorer | over | 0.6321 | 0.2817 | 0.3504 | False | 2026-11-02T18:35:10Z |
| draftkings|385032605|0QA385032605#2346227941_13L88808Q1-577361648Q20 | draftkings | Nate Adkins | Anytime TD Scorer | over | 0.4701 | 0.1333 | 0.3367 | False | 2026-11-03T19:40:49Z |
| draftkings|385070262|0QA385070262#2346502170_13L88808Q1-533028316Q20 | draftkings | Kevin Coleman Jr. | Anytime TD Scorer | over | 0.357 | 0.1 | 0.257 | False | 2026-11-04T12:22:18Z |
| draftkings|385025617|0QA385025617#2346198681_13L88808Q1999478588Q20 | draftkings | Kyle Pitts Sr. | Anytime TD Scorer | over | 0.4701 | 0.2326 | 0.2375 | False | 2026-11-02T18:35:10Z |
| betmgm|anytd|13582 | betmgm | Josh Jacobs | anytd | over | 0.786 | 0.5556 | 0.2304 | False | 2026-11-03T12:08:57Z |
| draftkings|385038485|0QA385038485#2346261888_13L88808Q1938922925Q20 | draftkings | Omar Cooper Jr. | Anytime TD Scorer | over | 0.5075 | 0.2778 | 0.2298 | False | 2026-11-05T00:59:13Z |
| draftkings|385038485|0QA385038485#2346261894_13L88808Q12123082164Q20 | draftkings | Isaiah Williams | Anytime TD Scorer | over | 0.2882 | 0.0667 | 0.2216 | False | 2026-11-05T00:59:13Z |
| draftkings|385070262|0QA385070262#2346502179_13L88808Q1480222870Q20 | draftkings | Jameson Williams | Anytime TD Scorer | over | 0.6255 | 0.4082 | 0.2173 | False | 2026-11-02T18:35:10Z |
| draftkings|385340515|0QA385340515#2347869309_13L88808Q1-1016060448Q20 | draftkings | Mike Gesicki | 2+ TDs | over | 0.2642 | 0.0556 | 0.2087 | False | 2026-11-03T12:08:57Z |
| draftkings|385047734|0QA385047734#2346301467_13L88808Q1622596392Q20 | draftkings | Stefon Diggs | Anytime TD Scorer | over | 0.5492 | 0.3448 | 0.2043 | False | 2026-11-02T18:35:10Z |
| draftkings|385032605|0QA385032605#2346227863_13L88808Q11890020597Q20 | draftkings | Anthony Tyus III | Anytime TD Scorer | over | 0.2296 | 0.0435 | 0.1861 | False | 2026-11-03T19:40:49Z |
| draftkings|385028912|0QA385028912#2346210928_13L88808Q1-1809117535Q20 | draftkings | Isaiah Likely | Anytime TD Scorer | over | 0.4945 | 0.3125 | 0.182 | False | 2026-11-03T12:08:57Z |
| draftkings|385828865|0QA385828865#2350013825_13L88808Q1-106544391Q20 | draftkings | Jameson Williams | 2+ TDs | over | 0.2577 | 0.0833 | 0.1743 | False | 2026-11-04T12:22:18Z |
| draftkings|385028912|0QA385028912#2346210918_13L88808Q11627968604Q20 | draftkings | Darius Cooper | Anytime TD Scorer | over | 0.3229 | 0.1538 | 0.1691 | False | 2026-11-04T19:58:29Z |
| draftkings|385038485|0QA385038485#2346261896_13L88808Q1433051443Q20 | draftkings | Jeremy Ruckert | Anytime TD Scorer | over | 0.2296 | 0.0625 | 0.1671 | False | 2026-11-05T00:59:13Z |
| draftkings|385025186|0QA385025186#2346191571_13L88808Q11213714519Q20 | draftkings | Noah Fant | Anytime TD Scorer | over | 0.3093 | 0.1429 | 0.1664 | False | 2026-11-06T07:04:01Z |
| draftkings|385025617|0QA385025617#2346198700_13L88808Q1219777051Q20 | draftkings | Joe Burrow | Anytime TD Scorer | over | 0.3147 | 0.1538 | 0.1608 | False | 2026-11-03T12:08:57Z |
| draftkings|385163667|0QA385163667#2347045615_13L88808Q1-1885662408Q20 | draftkings | Mo Alie-Cox | Anytime TD Scorer | over | 0.2296 | 0.0833 | 0.1463 | False | 2026-11-04T19:58:29Z |
| draftkings|385025617|0QA385025617#2346198702_13L88808Q1-409986828Q20 | draftkings | Drew Sample | Anytime TD Scorer | over | 0.2704 | 0.125 | 0.1454 | False | 2026-11-03T12:08:57Z |
| draftkings|385025617|0QA385025617#2346198691_13L88808Q11180641602Q20 | draftkings | Nick Muse | Anytime TD Scorer | over | 0.1881 | 0.0435 | 0.1446 | False | 2026-11-03T12:08:57Z |
| draftkings|385025186|0QA385025186#2346191563_13L88808Q11055160431Q20 | draftkings | Alvin Kamara | Anytime TD Scorer | over | 0.3904 | 0.25 | 0.1404 | False | 2026-11-06T07:04:01Z |
| draftkings|385038485|0QA385038485#2346261890_13L88808Q11061745166Q20 | draftkings | Mason Taylor | Anytime TD Scorer | over | 0.3624 | 0.2222 | 0.1401 | False | 2026-11-05T00:59:13Z |
| draftkings|386127772|0QA386127772#2351099773_13L88808Q1-60147958Q20 | draftkings | Stefon Diggs | 2+ TDs | over | 0.19 | 0.0556 | 0.1345 | False | 2026-11-05T00:59:13Z |
| draftkings|385568967|0QA385568967#2348975280_13L88808Q1-1564766902Q20 | draftkings | Nate Adkins | 2+ TDs | over | 0.1336 | 0.0132 | 0.1204 | False | 2026-11-03T19:40:49Z |
| draftkings|385025186|0QA385025186#2346191587_13L88808Q1-914474805Q20 | draftkings | Jaleel McLaughlin | Anytime TD Scorer | over | 0.1479 | 0.0278 | 0.1201 | False | 2026-11-06T07:04:01Z |
| draftkings|385740709|0QA385740709#2349618433_13L88808Q11556693862Q20 | draftkings | Omar Cooper Jr. | 2+ TDs | over | 0.1587 | 0.0476 | 0.1111 | False | 2026-11-05T00:59:13Z |
| draftkings|385070262|0QA385070262#2346502166_13L88808Q1-1601930688Q20 | draftkings | Caleb Douglas | Anytime TD Scorer | over | 0.4065 | 0.2985 | 0.108 | False | 2026-11-04T12:22:18Z |
| draftkings|385028912|0QA385028912#2346210933_13L88808Q1-534343686Q20 | draftkings | Theo Johnson | Anytime TD Scorer | over | 0.2296 | 0.125 | 0.1046 | False | 2026-11-04T19:58:29Z |
| draftkings|385981278|0QA385981278#2350530032_13L88808Q1-861767826Q20 | draftkings | Isaiah Likely | 2+ TDs | over | 0.1496 | 0.0476 | 0.102 | False | 2026-11-04T19:58:29Z |
| draftkings|385032605|0QA385032605#2346227926_13L88808Q1-813345382Q20 | draftkings | Tommy Tremble | Anytime TD Scorer | over | 0.2903 | 0.1905 | 0.0998 | False | 2026-11-03T19:40:49Z |
| draftkings|385070262|0QA385070262#2346502164_13L88808Q11579636272Q20 | draftkings | Malik Willis | Anytime TD Scorer | over | 0.3555 | 0.2597 | 0.0958 | False | 2026-11-02T18:35:10Z |
| draftkings|385047734|0QA385047734#2346301482_13L88808Q1-822030320Q20 | draftkings | Davis Allen | Anytime TD Scorer | over | 0.3127 | 0.2174 | 0.0953 | False | 2026-11-04T19:58:29Z |
| draftkings|385340515|0QA385340515#2347869298_13L88808Q1-703917339Q20 | draftkings | Kyle Pitts Sr. | 2+ TDs | over | 0.1336 | 0.0385 | 0.0951 | False | 2026-11-03T12:08:57Z |
| draftkings|385025186|0QA385025186#2346191570_13L88808Q11438391772Q20 | draftkings | Bryce Lance | Anytime TD Scorer | over | 0.1783 | 0.0909 | 0.0874 | False | 2026-11-07T20:22:01Z |
| draftkings|385032605|0QA385032605#2346227923_13L88808Q1294436062Q20 | draftkings | Darren Waller | Anytime TD Scorer | over | 0.2877 | 0.2041 | 0.0836 | False | 2026-11-03T19:40:49Z |
| draftkings|385032605|0QA385032605#2346227933_13L88808Q11696076099Q20 | draftkings | J.K. Dobbins | Anytime TD Scorer | over | 0.3766 | 0.2941 | 0.0824 | False | 2026-11-03T19:40:49Z |
| betmgm|anytd|11008 | betmgm | Dak Prescott | anytd | over | 0.2114 | 0.1333 | 0.0781 | False | 2026-11-04T19:58:29Z |
| draftkings|385025617|0QA385025617#2346198695_13L88808Q1106346443Q20 | draftkings | Tee Higgins | Anytime TD Scorer | over | 0.551 | 0.4762 | 0.0748 | False | 2026-11-02T18:35:10Z |
| draftkings|385163667|0QA385163667#2347045625_13L88808Q1795642865Q20 | draftkings | Dak Prescott | Anytime TD Scorer | over | 0.2114 | 0.1429 | 0.0685 | False | 2026-11-04T19:58:29Z |
| draftkings|385070262|0QA385070262#2346502184_13L88808Q1-1939996255Q20 | draftkings | Jared Goff | Anytime TD Scorer | over | 0.1575 | 0.0909 | 0.0666 | False | 2026-11-04T12:22:18Z |
| draftkings|385340515|0QA385340515#2347869308_13L88808Q1-1865349726Q20 | draftkings | Tee Higgins | 2+ TDs | over | 0.1915 | 0.125 | 0.0665 | False | 2026-11-03T12:08:57Z |
| draftkings|385828865|0QA385828865#2350013752_13L88808Q11465906394Q20 | draftkings | Kevin Coleman Jr. | 2+ TDs | over | 0.0731 | 0.0083 | 0.0648 | False | 2026-11-04T12:22:18Z |
| draftkings|385032605|0QA385032605#2352345661_13L88808Q164075827Q20 | draftkings | Pat Bryant | Anytime TD Scorer | over | 0.2296 | 0.1667 | 0.063 | False | 2026-11-06T07:04:01Z |
| draftkings|385340515|0QA385340515#2347869307_13L88808Q11526916627Q20 | draftkings | Ja'Marr Chase | 2+ TDs | over | 0.216 | 0.1538 | 0.0622 | False | 2026-11-03T12:08:57Z |
| draftkings|385568967|0QA385568967#2348975176_13L88808Q1-2084365438Q20 | draftkings | Chuba Hubbard | 2+ TDs | over | 0.2257 | 0.1667 | 0.059 | False | 2026-11-03T19:40:49Z |
| draftkings|385038485|0QA385038485#2346261875_13L88808Q1-1856213575Q20 | draftkings | Noah Gray | Anytime TD Scorer | over | 0.2184 | 0.1667 | 0.0517 | False | 2026-11-05T00:59:13Z |
| draftkings|385038485|0QA385038485#2346261885_13L88808Q1-1853948704Q20 | draftkings | Braelon Allen | Anytime TD Scorer | over | 0.3446 | 0.2941 | 0.0505 | False | 2026-11-06T07:04:01Z |
| draftkings|386072423|0QA386072423#2350885036_13L88808Q1839820985Q20 | draftkings | Alvin Kamara | 2+ TDs | over | 0.0887 | 0.0385 | 0.0502 | False | 2026-11-06T07:04:01Z |
| draftkings|385025186|0QA385025186#2346191567_13L88808Q1138922171Q20 | draftkings | Devaughn Vele | Anytime TD Scorer | over | 0.3619 | 0.3125 | 0.0494 | False | 2026-11-06T07:04:01Z |
| draftkings|385828865|0QA385828865#2350013748_13L88808Q1-1586162533Q20 | draftkings | Caleb Douglas | 2+ TDs | over | 0.0969 | 0.0476 | 0.0492 | False | 2026-11-04T12:22:18Z |
| draftkings|385047734|0QA385047734#2346301464_13L88808Q1968442089Q20 | draftkings | Rachaad White | Anytime TD Scorer | over | 0.4566 | 0.4082 | 0.0485 | False | 2026-11-02T18:35:10Z |
| draftkings|385025617|0QA385025617#2346198697_13L88808Q11111630045Q20 | draftkings | Samaje Perine | Anytime TD Scorer | over | 0.3078 | 0.2597 | 0.048 | False | 2026-11-03T12:08:57Z |
| draftkings|385740709|0QA385740709#2349618436_13L88808Q1806541095Q20 | draftkings | Mason Taylor | 2+ TDs | over | 0.0754 | 0.0278 | 0.0477 | False | 2026-11-05T00:59:13Z |
| draftkings|385070262|0QA385070262#2346502163_13L88808Q1354446541Q20 | draftkings | Ollie Gordon II | Anytime TD Scorer | over | 0.4823 | 0.4348 | 0.0475 | False | 2026-11-02T18:35:10Z |
| betmgm|anytd|15459 | betmgm | Noah Gray | anytd | over | 0.2184 | 0.1739 | 0.0445 | False | 2026-11-05T00:59:13Z |
| draftkings|385047734|0QA385047734#2346301479_13L88808Q11373713880Q20 | draftkings | Blake Corum | Anytime TD Scorer | over | 0.5084 | 0.4651 | 0.0432 | False | 2026-11-05T00:59:13Z |
| draftkings|385025186|0QA385025186#2346191586_13L88808Q1-262322861Q20 | draftkings | Blake Whiteheart | Anytime TD Scorer | over | 0.1479 | 0.1053 | 0.0426 | False | 2026-11-07T06:17:27Z |
| draftkings|386127772|0QA386127772#2351099786_13L88808Q11181433178Q20 | draftkings | Blake Corum | 2+ TDs | over | 0.1593 | 0.1176 | 0.0416 | False | 2026-11-05T00:59:13Z |
| draftkings|385981278|0QA385981278#2350530203_13L88808Q1-477962024Q20 | draftkings | Darius Cooper | 2+ TDs | over | 0.0589 | 0.0179 | 0.041 | False | 2026-11-04T19:58:29Z |
| draftkings|385047734|0QA385047734#2346301465_13L88808Q1111756323Q20 | draftkings | Jayden Daniels | Anytime TD Scorer | over | 0.3297 | 0.2899 | 0.0398 | False | 2026-11-02T18:35:10Z |
| draftkings|385740709|0QA385740709#2349618440_13L88808Q12070196828Q20 | draftkings | Isaiah Williams | 2+ TDs | over | 0.0462 | 0.0066 | 0.0396 | False | 2026-11-05T00:59:13Z |
| draftkings|385032605|0QA385032605#2346227936_13L88808Q1-1003727875Q20 | draftkings | Bo Nix | Anytime TD Scorer | over | 0.2212 | 0.1818 | 0.0394 | False | 2026-11-04T12:22:18Z |
| draftkings|385340515|0QA385340515#2347869312_13L88808Q1158576549Q20 | draftkings | Joe Burrow | 2+ TDs | over | 0.0557 | 0.0164 | 0.0393 | False | 2026-11-03T12:08:57Z |
| draftkings|386072423|0QA386072423#2350885040_13L88808Q1669299964Q20 | draftkings | Noah Fant | 2+ TDs | over | 0.0537 | 0.0179 | 0.0358 | False | 2026-11-06T07:04:01Z |
| draftkings|386127772|0QA386127772#2351099789_13L88808Q1-1802470485Q20 | draftkings | Davis Allen | 2+ TDs | over | 0.055 | 0.0196 | 0.0354 | False | 2026-11-06T21:41:28Z |
| draftkings|385568967|0QA385568967#2348975272_13L88808Q1-1048311142Q20 | draftkings | J.K. Dobbins | 2+ TDs | over | 0.082 | 0.0476 | 0.0344 | False | 2026-11-03T19:40:49Z |
| draftkings|385032605|0QA385032605#2346227921_13L88808Q1-537154100Q20 | draftkings | Jalen Coker | Anytime TD Scorer | over | 0.3462 | 0.3125 | 0.0337 | False | 2026-11-03T19:40:49Z |
| draftkings|386072423|0QA386072423#2350885035_13L88808Q1-1344177905Q20 | draftkings | Devaughn Vele | 2+ TDs | over | 0.0752 | 0.0435 | 0.0318 | False | 2026-11-06T21:41:28Z |
