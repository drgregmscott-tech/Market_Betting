# Props Pipeline Digest -- 2026-11-12T16:57:03Z

## Run summary
- DraftKings ingestion: 681 rows across 8 events (OK)
- FanDuel ingestion: 0 rows (OK)
- BetMGM ingestion (via Rotowire): 949 rows (OK)
- Estimation: 1630 rows written (from 1630 ingested rows) -- status breakdown: {'estimated': 764, 'unsupported_market_first_scorer': 466, 'unsupported_stat_type': 260, 'no_player_match': 112, 'insufficient_history': 28}
- CLV logging: 23 newly flagged, 0 newly closed, 31 still open (1557 total ever logged)

## Currently open flags
Sizing is a manual step (`sizing_engine.py props size`, Session 6.4) -- this table is what to scan to pick a flag worth sizing. `implied_prob_includes_field_vig` matters here more than for the other tracks: a row still reporting True carries a real, separate uncertainty (Session 6.4's `PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER` dampener) that a bigger raw edge number does not describe.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_model_prob | first_flagged_market_price | first_flagged_edge | implied_prob_includes_field_vig | first_flagged_at |
|---|---|---|---|---|---|---|---|---|---|
| betmgm|recs|14430 | betmgm | Van Jefferson | recs | over | 0.9997 | 0.3333 | 0.6664 | False | 2026-11-12T16:57:22Z |
| betmgm|anytd|16034 | betmgm | Teagan Quitoriano | anytd | over | 0.6002 | 0.0476 | 0.5525 | False | 2026-11-12T07:29:25Z |
| betmgm|recs|16935 | betmgm | Tank Dell | recs | over | 1.0 | 0.5347 | 0.4653 | False | 2026-11-12T07:29:25Z |
| betmgm|recs|16163 | betmgm | Jordan Mason | recs | over | 0.9992 | 0.5941 | 0.4051 | False | 2026-11-12T16:57:22Z |
| draftkings|387569245|0QA387569245#2357803433_13L88808Q1-1461677560Q20 | draftkings | Foster Moreau | Anytime TD Scorer | over | 0.4831 | 0.1667 | 0.3165 | False | 2026-11-12T16:57:22Z |
| betmgm|anytd|19258 | betmgm | Jack Endries | anytd | over | 0.3677 | 0.0714 | 0.2962 | False | 2026-11-10T21:54:10Z |
| betmgm|anytd|14430 | betmgm | Van Jefferson | anytd | over | 0.4182 | 0.1538 | 0.2644 | False | 2026-11-10T12:50:30Z |
| draftkings|387569245|0QA387569245#2357803431_13L88808Q1401138925Q20 | draftkings | Kayshon Boutte | Anytime TD Scorer | over | 0.3781 | 0.125 | 0.2531 | False | 2026-11-12T16:57:22Z |
| draftkings|387842881|0QA387842881#2359090181_13L88808Q1938922925Q20 | draftkings | Omar Cooper Jr. | Anytime TD Scorer | over | 0.3902 | 0.1667 | 0.2235 | False | 2026-11-12T16:57:22Z |
| draftkings|387596455|0QA387596455#2357910968_13L88808Q1-813345382Q20 | draftkings | Tommy Tremble | Anytime TD Scorer | over | 0.3828 | 0.1739 | 0.2088 | False | 2026-11-12T16:57:22Z |
| betmgm|anytd|16935 | betmgm | Tank Dell | anytd | over | 0.4182 | 0.2381 | 0.1801 | False | 2026-11-12T07:29:25Z |
| draftkings|387596455|0QA387596455#2357910967_13L88808Q1294436062Q20 | draftkings | Darren Waller | Anytime TD Scorer | over | 0.4084 | 0.2326 | 0.1759 | False | 2026-11-12T16:57:22Z |
| draftkings|387842881|0QA387842881#2359090185_13L88808Q1433051443Q20 | draftkings | Jeremy Ruckert | Anytime TD Scorer | over | 0.2296 | 0.0556 | 0.1741 | False | 2026-11-12T16:57:22Z |
| draftkings|387842881|0QA387842881#2359090201_13L88808Q11235745545Q20 | draftkings | Keleki Latu | Anytime TD Scorer | over | 0.2184 | 0.0625 | 0.1559 | False | 2026-11-12T16:57:22Z |
| draftkings|387596455|0QA387596455#2357923818_13L88808Q11890020597Q20 | draftkings | Anthony Tyus III | Anytime TD Scorer | over | 0.1813 | 0.0385 | 0.1428 | False | 2026-11-12T16:57:22Z |
| betmgm|anytd|14608 | betmgm | Charlie Woerner | anytd | over | 0.2277 | 0.087 | 0.1407 | False | 2026-11-12T07:29:25Z |
| draftkings|387842881|0QA387842881#2359090179_13L88808Q11061745166Q20 | draftkings | Mason Taylor | Anytime TD Scorer | over | 0.307 | 0.1667 | 0.1403 | False | 2026-11-12T16:57:22Z |
| draftkings|388124749|0QA388124749#2360343099_13L88808Q1257323792Q20 | draftkings | Foster Moreau | 2+ TDs | over | 0.142 | 0.0179 | 0.1242 | False | 2026-11-12T16:57:22Z |
| draftkings|387596455|0QA387596455#2357910959_13L88808Q11213714519Q20 | draftkings | Noah Fant | Anytime TD Scorer | over | 0.2549 | 0.1333 | 0.1216 | False | 2026-11-12T16:57:22Z |
| draftkings|387569245|0QA387569245#2357803429_13L88808Q12058064406Q20 | draftkings | Marvin Harrison Jr. | Anytime TD Scorer | over | 0.2795 | 0.1667 | 0.1129 | False | 2026-11-12T16:57:22Z |
| draftkings|387842881|0QA387842881#2359090183_13L88808Q12123082164Q20 | draftkings | Isaiah Williams | Anytime TD Scorer | over | 0.2103 | 0.1111 | 0.0992 | False | 2026-11-12T16:57:22Z |
| betmgm|anytd|18554 | betmgm | Savion Williams | anytd | over | 0.2704 | 0.1818 | 0.0886 | False | 2026-11-12T07:29:25Z |
| draftkings|387596455|0QA387596455#2357910955_13L88808Q1873985604Q20 | draftkings | Juwan Johnson | Anytime TD Scorer | over | 0.3462 | 0.2632 | 0.0831 | False | 2026-11-12T16:57:22Z |
| draftkings|388124602|0QA388124602#2360342594_13L88808Q11556693862Q20 | draftkings | Omar Cooper Jr. | 2+ TDs | over | 0.0886 | 0.0164 | 0.0722 | False | 2026-11-12T16:57:22Z |
| draftkings|388124749|0QA388124749#2360343097_13L88808Q1-1010510811Q20 | draftkings | Kayshon Boutte | 2+ TDs | over | 0.0827 | 0.0123 | 0.0704 | False | 2026-11-12T16:57:22Z |
| draftkings|388124901|0QA388124901#2360343637_13L88808Q1637812501Q20 | draftkings | Darren Waller | 2+ TDs | over | 0.0979 | 0.0278 | 0.0701 | False | 2026-11-12T16:57:22Z |
| draftkings|388124901|0QA388124901#2360343638_13L88808Q1372601323Q20 | draftkings | Tommy Tremble | 2+ TDs | over | 0.0849 | 0.0179 | 0.0671 | False | 2026-11-12T16:57:22Z |
| draftkings|387842881|0QA387842881#2359090195_13L88808Q1-2072232579Q20 | draftkings | Keon Coleman | Anytime TD Scorer | over | 0.3212 | 0.2632 | 0.0581 | False | 2026-11-12T16:57:22Z |
| draftkings|387569245|0QA387569245#2357803418_13L88808Q1-262322861Q20 | draftkings | Blake Whiteheart | Anytime TD Scorer | over | 0.116 | 0.0769 | 0.0391 | False | 2026-11-12T16:57:22Z |
| draftkings|388124602|0QA388124602#2360342595_13L88808Q1806541095Q20 | draftkings | Mason Taylor | 2+ TDs | over | 0.0528 | 0.0152 | 0.0377 | False | 2026-11-12T16:57:22Z |
| betmgm|anytd|13854 | betmgm | Ashton Dulin | anytd | over | 0.2404 | 0.2041 | 0.0363 | False | 2026-11-12T07:29:25Z |
