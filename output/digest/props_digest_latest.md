# Props Pipeline Digest -- 2026-10-30T06:04:45Z

## Run summary
- DraftKings ingestion: 706 rows across 8 events (OK)
- FanDuel ingestion: 0 rows (OK)
- BetMGM ingestion (via Rotowire): 912 rows (OK)
- Estimation: 1618 rows written (from 1618 ingested rows) -- status breakdown: {'estimated': 730, 'unsupported_market_first_scorer': 464, 'unsupported_stat_type': 264, 'no_player_match': 123, 'insufficient_history': 37}
- CLV logging: 11 newly flagged, 0 newly closed, 71 still open (1333 total ever logged)

## Currently open flags
Sizing is a manual step (`sizing_engine.py props size`, Session 6.4) -- this table is what to scan to pick a flag worth sizing. `implied_prob_includes_field_vig` matters here more than for the other tracks: a row still reporting True carries a real, separate uncertainty (Session 6.4's `PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER` dampener) that a bigger raw edge number does not describe.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_model_prob | first_flagged_market_price | first_flagged_edge | implied_prob_includes_field_vig | first_flagged_at |
|---|---|---|---|---|---|---|---|---|---|
| betmgm|recs|16036 | betmgm | Daniel Bellinger | recs | over | 1.0 | 0.4425 | 0.5575 | False | 2026-10-29T15:21:11Z |
| betmgm|recs|15924 | betmgm | Charlie Kolar | recs | over | 1.0 | 0.4653 | 0.5347 | False | 2026-10-29T21:16:56Z |
| betmgm|recs|18467 | betmgm | Dylan Sampson | recs | over | 0.9994 | 0.4797 | 0.5197 | False | 2026-10-30T06:04:59Z |
| draftkings|382709590|0QA382709590#2336304202_13L88808Q1-1846552455Q20 | draftkings | Mike Gesicki | Anytime TD Scorer | over | 0.6321 | 0.2326 | 0.3996 | False | 2026-10-28T21:14:02Z |
| betmgm|anytd|19343 | betmgm | Caleb Douglas | anytd | over | 0.5374 | 0.2041 | 0.3333 | False | 2026-10-28T15:16:18Z |
| draftkings|382665132|0QA382665132#2336049735_13L88808Q11141276074Q20 | draftkings | Sean Tucker | Anytime TD Scorer | over | 0.4919 | 0.1667 | 0.3252 | False | 2026-10-28T05:58:28Z |
| draftkings|382689796|0QA382689796#2336199132_13L88808Q1-2072232579Q20 | draftkings | Keon Coleman | Anytime TD Scorer | over | 0.478 | 0.2 | 0.278 | False | 2026-10-28T05:58:28Z |
| draftkings|382796087|0QA382796087#2336703201_13L88808Q11061745166Q20 | draftkings | Mason Taylor | Anytime TD Scorer | over | 0.4676 | 0.1905 | 0.2772 | False | 2026-10-30T06:04:59Z |
| betmgm|anytd|18535 | betmgm | Mason Taylor | anytd | over | 0.4676 | 0.2 | 0.2676 | False | 2026-10-29T06:04:22Z |
| draftkings|383652722|0QA383652722#2340252357_13L88808Q1-1016060448Q20 | draftkings | Mike Gesicki | 2+ TDs | over | 0.2642 | 0.0323 | 0.232 | False | 2026-10-28T21:14:02Z |
| draftkings|382796087|0QA382796087#2336703213_13L88808Q12025358379Q20 | draftkings | Tre Tucker | Anytime TD Scorer | over | 0.5087 | 0.2778 | 0.2309 | False | 2026-10-30T06:04:59Z |
| draftkings|382665132|0QA382665132#2336049742_13L88808Q1999478588Q20 | draftkings | Kyle Pitts Sr. | Anytime TD Scorer | over | 0.5555 | 0.3279 | 0.2276 | False | 2026-10-26T15:30:26Z |
| draftkings|382641891|0QA382641891#2335870681_13L88808Q1480222870Q20 | draftkings | Jameson Williams | Anytime TD Scorer | over | 0.6068 | 0.3922 | 0.2146 | False | 2026-10-26T15:30:26Z |
| draftkings|382665132|0QA382665132#2336049750_13L88808Q11180641602Q20 | draftkings | Nick Muse | Anytime TD Scorer | over | 0.2404 | 0.0345 | 0.2059 | False | 2026-10-28T05:58:28Z |
| draftkings|382656185|0QA382656185#2336136653_13L88808Q1292660006Q20 | draftkings | Ben Skowronek | Anytime TD Scorer | over | 0.276 | 0.0714 | 0.2045 | False | 2026-10-29T06:04:22Z |
| draftkings|383051429|0QA383051429#2337756863_13L88808Q1-106544391Q20 | draftkings | Jameson Williams | 2+ TDs | over | 0.2397 | 0.0588 | 0.1809 | False | 2026-10-27T14:44:03Z |
| draftkings|382656185|0QA382656185#2336007907_13L88808Q1-1532462247Q20 | draftkings | Darnell Washington | Anytime TD Scorer | over | 0.4369 | 0.2564 | 0.1805 | False | 2026-10-28T21:14:02Z |
| draftkings|382791058|0QA382791058#2336695885_13L88808Q1-297522584Q20 | draftkings | Tyler Warren | Anytime TD Scorer | over | 0.4373 | 0.2632 | 0.1741 | False | 2026-10-28T21:14:02Z |
| draftkings|382796087|0QA382796087#2336703209_13L88808Q1433051443Q20 | draftkings | Jeremy Ruckert | Anytime TD Scorer | over | 0.2296 | 0.0588 | 0.1708 | False | 2026-10-30T06:04:59Z |
| draftkings|382791058|0QA382791058#2336678355_13L88808Q1-1885662408Q20 | draftkings | Mo Alie-Cox | Anytime TD Scorer | over | 0.2296 | 0.0714 | 0.1582 | False | 2026-10-29T15:21:11Z |
| draftkings|382796087|0QA382796087#2336703220_13L88808Q1925853180Q20 | draftkings | Ian Thomas | Anytime TD Scorer | over | 0.2084 | 0.0526 | 0.1558 | False | 2026-10-30T06:04:59Z |
| draftkings|382656185|0QA382656185#2336007923_13L88808Q1-262322861Q20 | draftkings | Blake Whiteheart | Anytime TD Scorer | over | 0.2084 | 0.0556 | 0.1528 | False | 2026-10-29T06:04:22Z |
| draftkings|383396208|0QA383396208#2339229760_13L88808Q1-703917339Q20 | draftkings | Kyle Pitts Sr. | 2+ TDs | over | 0.1951 | 0.0435 | 0.1516 | False | 2026-10-28T05:58:28Z |
| draftkings|382709590|0QA382709590#2336304207_13L88808Q1-409986828Q20 | draftkings | Drew Sample | Anytime TD Scorer | over | 0.2704 | 0.125 | 0.1454 | False | 2026-10-28T21:14:02Z |
| betmgm|anytd|13809 | betmgm | Drew Sample | anytd | over | 0.2704 | 0.1333 | 0.137 | False | 2026-10-29T06:04:22Z |
| draftkings|383396208|0QA383396208#2339229669_13L88808Q1-1540780736Q20 | draftkings | Sean Tucker | 2+ TDs | over | 0.1479 | 0.0196 | 0.1283 | False | 2026-10-28T05:58:28Z |
| draftkings|382665132|0QA382665132#2336049732_13L88808Q1621783265Q20 | draftkings | Emeka Egbuka | Anytime TD Scorer | over | 0.4457 | 0.3175 | 0.1282 | False | 2026-10-28T05:58:28Z |
| draftkings|382709590|0QA382709590#2336304212_13L88808Q1410823711Q20 | draftkings | Tony Pollard | Anytime TD Scorer | over | 0.5813 | 0.4545 | 0.1268 | False | 2026-10-26T15:30:26Z |
| draftkings|383765102|0QA383765102#2340705157_13L88808Q11556693862Q20 | draftkings | Omar Cooper Jr. | 2+ TDs | over | 0.1587 | 0.0323 | 0.1264 | False | 2026-10-30T06:04:59Z |
| draftkings|383765102|0QA383765102#2340705247_13L88808Q1-591605316Q20 | draftkings | Tre Tucker | 2+ TDs | over | 0.1595 | 0.0385 | 0.1211 | False | 2026-10-30T06:04:59Z |
| draftkings|382689796|0QA382689796#2336199147_13L88808Q1-700661814Q20 | draftkings | Matthew Hibner | Anytime TD Scorer | over | 0.2084 | 0.0909 | 0.1175 | False | 2026-10-28T05:58:28Z |
| draftkings|383436920|0QA383436920#2339401460_13L88808Q1-2143181684Q20 | draftkings | Keon Coleman | 2+ TDs | over | 0.1386 | 0.0217 | 0.1169 | False | 2026-10-28T05:58:28Z |
| draftkings|382641891|0QA382641891#2335870687_13L88808Q1-1939996255Q20 | draftkings | Jared Goff | Anytime TD Scorer | over | 0.1881 | 0.0714 | 0.1166 | False | 2026-10-27T14:44:03Z |
| draftkings|382796087|0QA382796087#2336703218_13L88808Q11805711602Q20 | draftkings | Cody White | Anytime TD Scorer | over | 0.2245 | 0.1111 | 0.1134 | False | 2026-10-30T06:04:59Z |
| draftkings|383765102|0QA383765102#2340705236_13L88808Q1806541095Q20 | draftkings | Mason Taylor | 2+ TDs | over | 0.132 | 0.0196 | 0.1124 | False | 2026-10-30T06:04:59Z |
| draftkings|382689796|0QA382689796#2336199148_13L88808Q1-1199795272Q20 | draftkings | Devontez Walker | Anytime TD Scorer | over | 0.2015 | 0.0909 | 0.1106 | False | 2026-10-28T05:58:28Z |
| draftkings|383436920|0QA383436920#2339401456_13L88808Q1503159412Q20 | draftkings | James Cook | 2+ TDs | over | 0.3101 | 0.2128 | 0.0973 | False | 2026-10-28T05:58:28Z |
| draftkings|382689796|0QA382689796#2336199145_13L88808Q11714132096Q20 | draftkings | Josh Cuevas | Anytime TD Scorer | over | 0.2015 | 0.1053 | 0.0962 | False | 2026-10-28T05:58:28Z |
| draftkings|382791058|0QA382791058#2336678345_13L88808Q1-458881524Q20 | draftkings | Travis Hunter | Anytime TD Scorer | over | 0.2277 | 0.1333 | 0.0943 | False | 2026-10-28T21:14:02Z |
| betmgm|anytd|19448 | betmgm | Nate Boerkircher | anytd | over | 0.2404 | 0.1481 | 0.0923 | False | 2026-10-28T21:14:02Z |
| draftkings|382656185|0QA382656185#2336007924_13L88808Q1-914474805Q20 | draftkings | Jaleel McLaughlin | Anytime TD Scorer | over | 0.1479 | 0.0556 | 0.0923 | False | 2026-10-29T06:04:22Z |
| draftkings|382796087|0QA382796087#2336703217_13L88808Q1791336936Q20 | draftkings | Dylan Laube | Anytime TD Scorer | over | 0.1575 | 0.0667 | 0.0909 | False | 2026-10-30T06:04:59Z |
| draftkings|382641891|0QA382641891#2335870682_13L88808Q1472584472Q20 | draftkings | Sam LaPorta | Anytime TD Scorer | over | 0.4025 | 0.3125 | 0.09 | False | 2026-10-26T15:30:26Z |
| draftkings|382665132|0QA382665132#2336049743_13L88808Q1-419764349Q20 | draftkings | Jahan Dotson | Anytime TD Scorer | over | 0.2795 | 0.1905 | 0.0891 | False | 2026-10-28T05:58:28Z |
| draftkings|382656185|0QA382656185#2336007914_13L88808Q1-1895349765Q20 | draftkings | Quinshon Judkins | Anytime TD Scorer | over | 0.5034 | 0.4167 | 0.0867 | False | 2026-10-26T15:30:26Z |
| draftkings|383652722|0QA383652722#2340252482_13L88808Q11612572832Q20 | draftkings | Tony Pollard | 2+ TDs | over | 0.2168 | 0.1333 | 0.0835 | False | 2026-10-28T21:14:02Z |
| draftkings|383670616|0QA383670616#2340311466_13L88808Q1282689831Q20 | draftkings | Jonathan Taylor | 2+ TDs | over | 0.2611 | 0.1818 | 0.0793 | False | 2026-10-28T21:14:02Z |
| draftkings|383704032|0QA383704032#2340424347_13L88808Q1854391200Q20 | draftkings | Darnell Washington | 2+ TDs | over | 0.1135 | 0.0345 | 0.079 | False | 2026-10-28T21:14:02Z |
| draftkings|382709590|0QA382709590#2336304201_13L88808Q11111630045Q20 | draftkings | Samaje Perine | Anytime TD Scorer | over | 0.3729 | 0.2941 | 0.0788 | False | 2026-10-28T21:14:02Z |
| draftkings|382709590|0QA382709590#2336304199_13L88808Q11365449708Q20 | draftkings | Ja'Marr Chase | Anytime TD Scorer | over | 0.5754 | 0.5 | 0.0754 | False | 2026-10-28T05:58:28Z |
| draftkings|383670616|0QA383670616#2340311470_13L88808Q11041398384Q20 | draftkings | Tyler Warren | 2+ TDs | over | 0.1137 | 0.0385 | 0.0753 | False | 2026-10-28T21:14:02Z |
| draftkings|382791058|0QA382791058#2336678343_13L88808Q1-292926888Q20 | draftkings | Nate Boerkircher | Anytime TD Scorer | over | 0.2404 | 0.1667 | 0.0738 | False | 2026-10-28T21:14:02Z |
| draftkings|383436920|0QA383436920#2339401455_13L88808Q11587218485Q20 | draftkings | Josh Allen | 2+ TDs | over | 0.2979 | 0.2273 | 0.0706 | False | 2026-10-28T05:58:28Z |
| draftkings|383074636|0QA383074636#2337864278_13L88808Q1759561049Q20 | draftkings | CeeDee Lamb | Anytime TD Scorer | over | 0.5677 | 0.5 | 0.0677 | False | 2026-10-28T21:14:02Z |
| draftkings|382796087|0QA382796087#2336703206_13L88808Q12123082164Q20 | draftkings | Isaiah Williams | Anytime TD Scorer | over | 0.1232 | 0.0556 | 0.0676 | False | 2026-10-30T06:04:59Z |
| draftkings|383396208|0QA383396208#2339229664_13L88808Q11465714566Q20 | draftkings | Emeka Egbuka | 2+ TDs | over | 0.1186 | 0.0526 | 0.066 | False | 2026-10-28T05:58:28Z |
| draftkings|383754217|0QA383754217#2340615683_13L88808Q12056061885Q20 | draftkings | Javonte Williams | 2+ TDs | over | 0.36 | 0.2941 | 0.0658 | False | 2026-10-29T06:04:22Z |
| draftkings|382656185|0QA382656185#2336007920_13L88808Q1184390672Q20 | draftkings | Deshaun Watson | Anytime TD Scorer | over | 0.2184 | 0.1538 | 0.0646 | False | 2026-10-28T21:14:02Z |
| draftkings|382665132|0QA382665132#2336049745_13L88808Q1-189550648Q20 | draftkings | Austin Hooper | Anytime TD Scorer | over | 0.1479 | 0.0833 | 0.0645 | False | 2026-10-28T05:58:28Z |
| draftkings|383704032|0QA383704032#2340424346_13L88808Q1-162258478Q20 | draftkings | Pat Freiermuth | 2+ TDs | over | 0.1044 | 0.0435 | 0.0609 | False | 2026-10-28T21:14:02Z |
| draftkings|382656185|0QA382656185#2336007915_13L88808Q1466829631Q20 | draftkings | Harold Fannin Jr. | Anytime TD Scorer | over | 0.2983 | 0.2381 | 0.0602 | False | 2026-10-29T15:21:11Z |
| draftkings|383652722|0QA383652722#2340252354_13L88808Q11526916627Q20 | draftkings | Ja'Marr Chase | 2+ TDs | over | 0.2117 | 0.1538 | 0.0579 | False | 2026-10-28T21:14:02Z |
| draftkings|382791058|0QA382791058#2336678338_13L88808Q11137102484Q20 | draftkings | Chris Rodriguez Jr. | Anytime TD Scorer | over | 0.2787 | 0.2273 | 0.0514 | False | 2026-10-28T21:14:02Z |
| draftkings|383704032|0QA383704032#2340424349_13L88808Q1-681441441Q20 | draftkings | Quinshon Judkins | 2+ TDs | over | 0.1558 | 0.1053 | 0.0505 | False | 2026-10-28T21:14:02Z |
| draftkings|383396208|0QA383396208#2339229662_13L88808Q1-416383636Q20 | draftkings | Bucky Irving | 2+ TDs | over | 0.2301 | 0.1818 | 0.0483 | False | 2026-10-28T05:58:28Z |
| draftkings|383051429|0QA383051429#2337756864_13L88808Q1-558374750Q20 | draftkings | Sam LaPorta | 2+ TDs | over | 0.0948 | 0.0476 | 0.0472 | False | 2026-10-27T20:50:12Z |
| draftkings|382709590|0QA382709590#2336304206_13L88808Q1219777051Q20 | draftkings | Joe Burrow | Anytime TD Scorer | over | 0.1675 | 0.125 | 0.0425 | False | 2026-10-28T05:58:28Z |
| draftkings|382665132|0QA382665132#2336049734_13L88808Q1-1654530021Q20 | draftkings | Tez Johnson | Anytime TD Scorer | over | 0.2184 | 0.1818 | 0.0366 | False | 2026-10-28T05:58:28Z |
| draftkings|382791058|0QA382791058#2336678341_13L88808Q1-271780635Q20 | draftkings | Brian Thomas Jr. | Anytime TD Scorer | over | 0.1675 | 0.1333 | 0.0342 | False | 2026-10-29T15:21:11Z |
| draftkings|383704032|0QA383704032#2340424504_13L88808Q11611408856Q20 | draftkings | Ben Skowronek | 2+ TDs | over | 0.0422 | 0.009 | 0.0332 | False | 2026-10-29T06:04:22Z |
| draftkings|383652722|0QA383652722#2340252356_13L88808Q1-1895789824Q20 | draftkings | Samaje Perine | 2+ TDs | over | 0.0803 | 0.0476 | 0.0327 | False | 2026-10-28T21:14:02Z |
