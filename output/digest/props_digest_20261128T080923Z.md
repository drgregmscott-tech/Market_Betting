# Props Pipeline Digest -- 2026-11-28T08:09:23Z

## Run summary
- DraftKings ingestion: 671 rows across 8 events (OK)
- FanDuel ingestion: 0 rows (OK)
- BetMGM ingestion (via Rotowire): 854 rows (OK)
- Estimation: 1525 rows written (from 1525 ingested rows) -- status breakdown: {'estimated': 716, 'unsupported_market_first_scorer': 426, 'unsupported_stat_type': 275, 'no_player_match': 83, 'insufficient_history': 25}
- CLV logging: 6 newly flagged, 0 newly closed, 85 still open (1850 total ever logged)

## Currently open flags
Sizing is a manual step (`sizing_engine.py props size`, Session 6.4) -- this table is what to scan to pick a flag worth sizing. `implied_prob_includes_field_vig` matters here more than for the other tracks: a row still reporting True carries a real, separate uncertainty (Session 6.4's `PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER` dampener) that a bigger raw edge number does not describe.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_model_prob | first_flagged_market_price | first_flagged_edge | implied_prob_includes_field_vig | first_flagged_at |
|---|---|---|---|---|---|---|---|---|---|
| betmgm|recs|11751 | betmgm | Zay Jones | recs | over | 0.9987 | 0.4554 | 0.5433 | False | 2026-11-28T08:09:38Z |
| betmgm|recs|19331 | betmgm | Harrison Wallace | recs | over | 1.0 | 0.4899 | 0.5101 | False | 2026-11-28T08:09:38Z |
| draftkings|392005423|0QA392005423#2378349026_13L88808Q11707072676Q20 | draftkings | Emanuel Wilson | Anytime TD Scorer | over | 0.4937 | 0.05 | 0.4437 | False | 2026-11-28T00:10:07Z |
| draftkings|391964719|0QA391964719#2381884702_13L88808Q1-1040068565Q20 | draftkings | Sterling Shepard | Anytime TD Scorer | over | 0.5374 | 0.1333 | 0.404 | False | 2026-11-28T00:10:07Z |
| draftkings|392529707|0QA392529707#2380907520_13L88808Q11055160431Q20 | draftkings | Alvin Kamara | Anytime TD Scorer | over | 0.5499 | 0.1818 | 0.3681 | False | 2026-11-28T00:10:07Z |
| draftkings|391937589|0QA391937589#2378060839_13L88808Q1-1683593135Q20 | draftkings | Marlin Klein | Anytime TD Scorer | over | 0.4182 | 0.0588 | 0.3594 | False | 2026-11-25T14:41:23Z |
| betmgm|anytd|19352 | betmgm | Marlin Klein | anytd | over | 0.4182 | 0.087 | 0.3313 | False | 2026-11-25T14:41:23Z |
| draftkings|392005423|0QA392005423#2378349016_13L88808Q1-1863661381Q20 | draftkings | Deebo Samuel | Anytime TD Scorer | over | 0.5069 | 0.2 | 0.3069 | False | 2026-11-28T00:10:07Z |
| draftkings|391964719|0QA391964719#2378159304_13L88808Q1-782741055Q20 | draftkings | Kyle McCord | Anytime TD Scorer | over | 0.3677 | 0.0833 | 0.2843 | False | 2026-11-28T00:10:07Z |
| draftkings|392174894|0QA392174894#2379264425_13L88808Q1-1442390665Q20 | draftkings | Christian McCaffrey | 2+ TDs | over | 0.4718 | 0.1905 | 0.2814 | False | 2026-11-28T00:10:07Z |
| betmgm|anytd|18498 | betmgm | Kyle McCord | anytd | over | 0.3677 | 0.1053 | 0.2624 | False | 2026-11-25T14:41:23Z |
| draftkings|392210422|0QA392210422#2379414671_13L88808Q11240135444Q20 | draftkings | Ladd McConkey | Anytime TD Scorer | over | 0.4312 | 0.1739 | 0.2573 | False | 2026-11-28T00:10:07Z |
| draftkings|392529707|0QA392529707#2380907509_13L88808Q11974991558Q20 | draftkings | Colbie Young | Anytime TD Scorer | over | 0.3198 | 0.0952 | 0.2246 | False | 2026-11-28T00:10:07Z |
| draftkings|391937589|0QA391937589#2378060835_13L88808Q1-1461677560Q20 | draftkings | Foster Moreau | Anytime TD Scorer | over | 0.3961 | 0.1739 | 0.2222 | False | 2026-11-25T14:41:23Z |
| draftkings|392529707|0QA392529707#2380907511_13L88808Q1-409986828Q20 | draftkings | Drew Sample | Anytime TD Scorer | over | 0.3241 | 0.1111 | 0.213 | False | 2026-11-28T00:10:07Z |
| betmgm|anytd|19447 | betmgm | Colbie Young | anytd | over | 0.3198 | 0.1081 | 0.2117 | False | 2026-11-25T14:41:23Z |
| draftkings|392005423|0QA392005423#2378349014_13L88808Q1-2099105975Q20 | draftkings | George Kittle | Anytime TD Scorer | over | 0.5229 | 0.3175 | 0.2054 | False | 2026-11-28T00:10:07Z |
| draftkings|392210422|0QA392210422#2379414693_13L88808Q1-1380862881Q20 | draftkings | Lan Larison | Anytime TD Scorer | over | 0.2704 | 0.0714 | 0.1989 | False | 2026-11-28T00:10:07Z |
| draftkings|392566736|0QA392566736#2381065061_13L88808Q1839820985Q20 | draftkings | Alvin Kamara | 2+ TDs | over | 0.1906 | 0.0196 | 0.171 | False | 2026-11-28T00:10:07Z |
| betmgm|anytd|18886 | betmgm | Lan Larison | anytd | over | 0.2704 | 0.1 | 0.1704 | False | 2026-11-28T00:10:07Z |
| draftkings|392401530|0QA392401530#2381884686_13L88808Q1-1194127990Q20 | draftkings | Sterling Shepard | 2+ TDs | over | 0.1808 | 0.0123 | 0.1684 | False | 2026-11-28T00:10:07Z |
| draftkings|391946714|0QA391946714#2378107906_13L88808Q1-1746358002Q20 | draftkings | Jameis Winston | Anytime TD Scorer | over | 0.2926 | 0.125 | 0.1676 | False | 2026-11-28T00:10:07Z |
| draftkings|391973083|0QA391973083#2378204469_13L88808Q1877705888Q20 | draftkings | Kirk Cousins | Anytime TD Scorer | over | 0.2219 | 0.0556 | 0.1664 | False | 2026-11-25T14:41:23Z |
| draftkings|391964719|0QA391964719#2378159308_13L88808Q11222312202Q20 | draftkings | Jalen Tolbert | Anytime TD Scorer | over | 0.2015 | 0.0435 | 0.158 | False | 2026-11-28T00:10:07Z |
| draftkings|392005423|0QA392005423#2384735172_13L88808Q1785301666Q20 | draftkings | Demarcus Robinson | Anytime TD Scorer | over | 0.253 | 0.0952 | 0.1577 | False | 2026-11-28T08:09:38Z |
| draftkings|392005423|0QA392005423#2378349030_13L88808Q1-1216598181Q20 | draftkings | Cooper Kupp | Anytime TD Scorer | over | 0.3462 | 0.1905 | 0.1558 | False | 2026-11-28T00:10:07Z |
| draftkings|392005423|0QA392005423#2378349012_13L88808Q11665839176Q20 | draftkings | Mike Evans | Anytime TD Scorer | over | 0.4516 | 0.2985 | 0.1531 | False | 2026-11-28T00:10:07Z |
| draftkings|391959446|0QA391959446#2378143040_13L88808Q1-271780635Q20 | draftkings | Brian Thomas Jr. | Anytime TD Scorer | over | 0.357 | 0.2128 | 0.1443 | False | 2026-11-25T14:41:23Z |
| draftkings|392174894|0QA392174894#2379264446_13L88808Q1-1357951342Q20 | draftkings | Emanuel Wilson | 2+ TDs | over | 0.1491 | 0.005 | 0.1442 | False | 2026-11-28T00:10:07Z |
| draftkings|392174894|0QA392174894#2379264430_13L88808Q1-1288734733Q20 | draftkings | Deebo Samuel | 2+ TDs | over | 0.1583 | 0.0217 | 0.1366 | False | 2026-11-28T00:10:07Z |
| draftkings|391973083|0QA391973083#2378204485_13L88808Q11180641602Q20 | draftkings | Nick Muse | Anytime TD Scorer | over | 0.1575 | 0.0217 | 0.1358 | False | 2026-11-25T14:41:23Z |
| draftkings|392005423|0QA392005423#2378349018_13L88808Q11061966518Q20 | draftkings | Kyle Juszczyk | Anytime TD Scorer | over | 0.2156 | 0.0833 | 0.1323 | False | 2026-11-28T00:10:07Z |
| draftkings|391946714|0QA391946714#2378096187_13L88808Q1-1809117535Q20 | draftkings | Isaiah Likely | Anytime TD Scorer | over | 0.4594 | 0.3279 | 0.1315 | False | 2026-11-28T00:10:07Z |
| draftkings|391973083|0QA391973083#2378204471_13L88808Q1-1841072915Q20 | draftkings | Gavin Bartholomew | Anytime TD Scorer | over | 0.2015 | 0.0714 | 0.1301 | False | 2026-11-25T14:41:23Z |
| betmgm|anytd|12616 | betmgm | Calvin Ridley | anytd | over | 0.2184 | 0.0909 | 0.1275 | False | 2026-11-26T00:35:17Z |
| draftkings|392174894|0QA392174894#2379264427_13L88808Q11108077714Q20 | draftkings | George Kittle | 2+ TDs | over | 0.1698 | 0.0476 | 0.1222 | False | 2026-11-28T00:10:07Z |
| draftkings|391937589|0QA391937589#2378060845_13L88808Q11994625172Q20 | draftkings | Justice Hill | Anytime TD Scorer | over | 0.3064 | 0.1905 | 0.116 | False | 2026-11-25T14:41:23Z |
| draftkings|392210422|0QA392210422#2379414687_13L88808Q1-205213128Q20 | draftkings | Demario Douglas | Anytime TD Scorer | over | 0.2882 | 0.1739 | 0.1143 | False | 2026-11-28T00:10:07Z |
| draftkings|391937589|0QA391937589#2378060851_13L88808Q1-1199795272Q20 | draftkings | Devontez Walker | Anytime TD Scorer | over | 0.1675 | 0.0556 | 0.112 | False | 2026-11-25T14:41:23Z |
| draftkings|391973083|0QA391973083#2378204480_13L88808Q1-1356990742Q20 | draftkings | Charlie Woerner | Anytime TD Scorer | over | 0.1783 | 0.0667 | 0.1117 | False | 2026-11-25T14:41:23Z |
| draftkings|392005423|0QA392005423#2378349024_13L88808Q11896367839Q20 | draftkings | Jaxon Smith-Njigba | Anytime TD Scorer | over | 0.5661 | 0.4545 | 0.1116 | False | 2026-11-28T00:10:07Z |
| draftkings|392529707|0QA392529707#2380907505_13L88808Q1106346443Q20 | draftkings | Tee Higgins | Anytime TD Scorer | over | 0.5873 | 0.4762 | 0.1111 | False | 2026-11-28T00:10:07Z |
| draftkings|391964719|0QA391964719#2378159318_13L88808Q1433051443Q20 | draftkings | Jeremy Ruckert | Anytime TD Scorer | over | 0.1813 | 0.0714 | 0.1098 | False | 2026-11-28T00:10:07Z |
| draftkings|392500152|0QA392500152#2380763534_13L88808Q11746484724Q20 | draftkings | Derrick Henry | 2+ TDs | over | 0.2754 | 0.1667 | 0.1088 | False | 2026-11-25T14:41:23Z |
| draftkings|392210422|0QA392210422#2379414690_13L88808Q1-2056923875Q20 | draftkings | Efton Chism III | Anytime TD Scorer | over | 0.2103 | 0.1053 | 0.105 | False | 2026-11-28T00:10:07Z |
| draftkings|392174894|0QA392174894#2379264438_13L88808Q1491696445Q20 | draftkings | Jaxon Smith-Njigba | 2+ TDs | over | 0.2038 | 0.1 | 0.1038 | False | 2026-11-28T00:10:07Z |
| draftkings|391959446|0QA391959446#2378143055_13L88808Q1546774868Q20 | draftkings | Calvin Ridley | Anytime TD Scorer | over | 0.2184 | 0.1176 | 0.1008 | False | 2026-11-25T14:41:23Z |
| draftkings|391959446|0QA391959446#2378143047_13L88808Q1410823711Q20 | draftkings | Tony Pollard | Anytime TD Scorer | over | 0.5747 | 0.4762 | 0.0985 | False | 2026-11-25T14:41:23Z |
| draftkings|392566736|0QA392566736#2381065037_13L88808Q1-1865349726Q20 | draftkings | Tee Higgins | 2+ TDs | over | 0.222 | 0.125 | 0.097 | False | 2026-11-28T00:10:07Z |
| draftkings|392500152|0QA392500152#2380763481_13L88808Q11568418663Q20 | draftkings | Marlin Klein | 2+ TDs | over | 0.1031 | 0.0062 | 0.0969 | False | 2026-11-25T14:41:23Z |
| draftkings|392761541|0QA392761541#2381964023_13L88808Q1304906002Q20 | draftkings | Ladd McConkey | 2+ TDs | over | 0.1103 | 0.0179 | 0.0924 | False | 2026-11-28T00:10:07Z |
| draftkings|392210422|0QA392210422#2379414689_13L88808Q11958986630Q20 | draftkings | Kyle Williams | Anytime TD Scorer | over | 0.1813 | 0.0909 | 0.0904 | False | 2026-11-28T00:10:07Z |
| draftkings|392601119|0QA392601119#2381201036_13L88808Q11612572832Q20 | draftkings | Tony Pollard | 2+ TDs | over | 0.2111 | 0.125 | 0.0861 | False | 2026-11-25T14:41:23Z |
| draftkings|392005423|0QA392005423#2378349013_13L88808Q11981396460Q20 | draftkings | Kaelon Black | Anytime TD Scorer | over | 0.248 | 0.1667 | 0.0813 | False | 2026-11-28T00:10:07Z |
| draftkings|391964719|0QA391964719#2378159306_13L88808Q1-533028316Q20 | draftkings | Kevin Coleman Jr. | Anytime TD Scorer | over | 0.1573 | 0.0769 | 0.0803 | False | 2026-11-28T00:10:07Z |
| draftkings|391973083|0QA391973083#2378204475_13L88808Q1999478588Q20 | draftkings | Kyle Pitts Sr. | Anytime TD Scorer | over | 0.2882 | 0.2083 | 0.0799 | False | 2026-11-25T14:41:23Z |
| draftkings|392529707|0QA392529707#2380907406_13L88808Q1219777051Q20 | draftkings | Joe Burrow | Anytime TD Scorer | over | 0.2666 | 0.1905 | 0.0761 | False | 2026-11-28T00:10:07Z |
| draftkings|392174894|0QA392174894#2379264426_13L88808Q1-1809939904Q20 | draftkings | Mike Evans | 2+ TDs | over | 0.1221 | 0.0476 | 0.0745 | False | 2026-11-28T00:10:07Z |
| draftkings|392580035|0QA392580035#2381110416_13L88808Q1-861767826Q20 | draftkings | Isaiah Likely | 2+ TDs | over | 0.1269 | 0.0526 | 0.0742 | False | 2026-11-28T00:10:07Z |
| draftkings|391937589|0QA391937589#2378060831_13L88808Q11759839095Q20 | draftkings | Nico Collins | Anytime TD Scorer | over | 0.5393 | 0.4651 | 0.0742 | False | 2026-11-25T14:41:23Z |
| draftkings|392500152|0QA392500152#2380763479_13L88808Q1257323792Q20 | draftkings | Foster Moreau | 2+ TDs | over | 0.0915 | 0.0196 | 0.0719 | False | 2026-11-25T14:41:23Z |
| draftkings|392401530|0QA392401530#2380158482_13L88808Q1-1908399554Q20 | draftkings | Kyle McCord | 2+ TDs | over | 0.0778 | 0.0066 | 0.0712 | False | 2026-11-28T00:10:07Z |
| draftkings|391937589|0QA391937589#2378060834_13L88808Q1-1444150535Q20 | draftkings | Xavier Hutchinson | Anytime TD Scorer | over | 0.3527 | 0.2817 | 0.071 | False | 2026-11-25T14:41:23Z |
| draftkings|392500152|0QA392500152#2380763474_13L88808Q1-721675132Q20 | draftkings | Nico Collins | 2+ TDs | over | 0.1823 | 0.1176 | 0.0646 | False | 2026-11-25T14:41:23Z |
| draftkings|392210422|0QA392210422#2379414679_13L88808Q1-1123329864Q20 | draftkings | Derius Davis | Anytime TD Scorer | over | 0.1393 | 0.0769 | 0.0624 | False | 2026-11-28T00:10:07Z |
| betmgm|anytd|15559 | betmgm | Simi Fehoko | anytd | over | 0.2059 | 0.1481 | 0.0578 | False | 2026-11-28T08:09:38Z |
| draftkings|391959446|0QA391959446#2378143056_13L88808Q11550208160Q20 | draftkings | Daniel Bellinger | Anytime TD Scorer | over | 0.1605 | 0.1053 | 0.0553 | False | 2026-11-25T14:41:23Z |
| draftkings|391959446|0QA391959446#2378143039_13L88808Q11380693923Q20 | draftkings | Josh Cameron | Anytime TD Scorer | over | 0.2404 | 0.1905 | 0.05 | False | 2026-11-25T14:41:23Z |
| draftkings|391973083|0QA391973083#2378204470_13L88808Q1313197721Q20 | draftkings | Myles Price | Anytime TD Scorer | over | 0.1605 | 0.1111 | 0.0494 | False | 2026-11-25T14:41:23Z |
| draftkings|392174894|0QA392174894#2379264441_13L88808Q1-1758481335Q20 | draftkings | Cooper Kupp | 2+ TDs | over | 0.0684 | 0.0196 | 0.0488 | False | 2026-11-28T00:10:07Z |
| draftkings|392566736|0QA392566736#2381065051_13L88808Q1-2014301802Q20 | draftkings | Colbie Young | 2+ TDs | over | 0.0577 | 0.009 | 0.0487 | False | 2026-11-28T00:10:07Z |
| draftkings|391959446|0QA391959446#2378143042_13L88808Q1-292926888Q20 | draftkings | Nate Boerkircher | Anytime TD Scorer | over | 0.248 | 0.2 | 0.048 | False | 2026-11-25T14:41:23Z |
| draftkings|391964719|0QA391964719#2378196974_13L88808Q12123082164Q20 | draftkings | Isaiah Williams | Anytime TD Scorer | over | 0.1813 | 0.1333 | 0.0479 | False | 2026-11-28T00:10:07Z |
| draftkings|392566736|0QA392566736#2381065049_13L88808Q1992963390Q20 | draftkings | Drew Sample | 2+ TDs | over | 0.0593 | 0.0123 | 0.047 | False | 2026-11-28T00:10:07Z |
| draftkings|391937589|0QA391937589#2378065858_13L88808Q12058064406Q20 | draftkings | Marvin Harrison Jr. | Anytime TD Scorer | over | 0.2795 | 0.2326 | 0.047 | False | 2026-11-26T00:35:17Z |
| draftkings|391946714|0QA391946714#2378096181_13L88808Q1942374795Q20 | draftkings | Ashton Dulin | Anytime TD Scorer | over | 0.1575 | 0.1111 | 0.0464 | False | 2026-11-28T00:10:07Z |
| draftkings|392601119|0QA392601119#2381200976_13L88808Q11304672355Q20 | draftkings | Brian Thomas Jr. | 2+ TDs | over | 0.0731 | 0.0278 | 0.0453 | False | 2026-11-25T14:41:23Z |
| draftkings|391946714|0QA391946714#2378096188_13L88808Q11930260006Q20 | draftkings | Devin Singletary | Anytime TD Scorer | over | 0.1836 | 0.1429 | 0.0407 | False | 2026-11-28T08:09:38Z |
| draftkings|392529707|0QA392529707#2380907510_13L88808Q11452425719Q20 | draftkings | Jack Endries | Anytime TD Scorer | over | 0.1732 | 0.1333 | 0.0399 | False | 2026-11-28T00:10:07Z |
| draftkings|392210422|0QA392210422#2379414672_13L88808Q1-1799172597Q20 | draftkings | Quentin Johnston | Anytime TD Scorer | over | 0.1441 | 0.1053 | 0.0388 | False | 2026-11-28T08:09:38Z |
| draftkings|392580035|0QA392580035#2381110469_13L88808Q1564357304Q20 | draftkings | Jameis Winston | 2+ TDs | over | 0.0477 | 0.011 | 0.0367 | False | 2026-11-28T00:10:07Z |
| draftkings|391959446|0QA391959446#2378143048_13L88808Q11703123874Q20 | draftkings | Carnell Tate | Anytime TD Scorer | over | 0.3297 | 0.2941 | 0.0356 | False | 2026-11-25T14:41:23Z |
| draftkings|392761541|0QA392761541#2381963992_13L88808Q1-1206993808Q20 | draftkings | Lan Larison | 2+ TDs | over | 0.0404 | 0.0066 | 0.0338 | False | 2026-11-28T00:10:07Z |
| draftkings|391937589|0QA391937589#2378060847_13L88808Q1-511742258Q20 | draftkings | Rashod Bateman | Anytime TD Scorer | over | 0.2335 | 0.2 | 0.0335 | False | 2026-11-25T14:41:23Z |
| draftkings|392500152|0QA392500152#2380763536_13L88808Q11902362131Q20 | draftkings | Justice Hill | 2+ TDs | over | 0.0527 | 0.0217 | 0.0309 | False | 2026-11-25T14:41:23Z |
