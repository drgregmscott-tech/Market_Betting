# Props Pipeline Digest -- 2026-10-25T04:58:55Z

## Run summary
- DraftKings ingestion: 720 rows across 8 events (OK)
- FanDuel ingestion: 0 rows (OK)
- BetMGM ingestion (via Rotowire): 1073 rows (OK)
- Estimation: 1793 rows written (from 1793 ingested rows) -- status breakdown: {'estimated': 772, 'unsupported_market_first_scorer': 479, 'unsupported_stat_type': 339, 'no_player_match': 143, 'insufficient_history': 58, 'no_line_value': 2}
- CLV logging: 1 newly flagged, 0 newly closed, 92 still open (1227 total ever logged)

## Currently open flags
Sizing is a manual step (`sizing_engine.py props size`, Session 6.4) -- this table is what to scan to pick a flag worth sizing. `implied_prob_includes_field_vig` matters here more than for the other tracks: a row still reporting True carries a real, separate uncertainty (Session 6.4's `PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER` dampener) that a bigger raw edge number does not describe.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_model_prob | first_flagged_market_price | first_flagged_edge | implied_prob_includes_field_vig | first_flagged_at |
|---|---|---|---|---|---|---|---|---|---|
| betmgm|recs|14418 | betmgm | J.K. Dobbins | recs | over | 1.0 | 0.3666 | 0.6334 | False | 2026-10-23T20:01:31Z |
| betmgm|recs|16069 | betmgm | John Metchie | recs | over | 1.0 | 0.3887 | 0.6113 | False | 2026-10-23T20:01:31Z |
| betmgm|recs|9260 | betmgm | Brandin Cooks | recs | over | 1.0 | 0.4335 | 0.5665 | False | 2026-10-24T22:37:09Z |
| betmgm|recs|13449 | betmgm | Devin Singletary | recs | over | 0.9988 | 0.4754 | 0.5234 | False | 2026-10-23T05:15:13Z |
| betmgm|recs|17967 | betmgm | Tyrone Tracy | recs | over | 1.0 | 0.4797 | 0.5203 | False | 2026-10-23T05:15:13Z |
| betmgm|recs|19314 | betmgm | Omar Cooper | recs | over | 1.0 | 0.5 | 0.5 | False | 2026-10-23T20:01:31Z |
| betmgm|recs|18647 | betmgm | Jordan Watkins | recs | over | 1.0 | 0.5246 | 0.4754 | False | 2026-10-24T22:37:09Z |
| betmgm|recs|19343 | betmgm | Caleb Douglas | recs | over | 1.0 | 0.5482 | 0.4518 | False | 2026-10-24T12:49:27Z |
| betmgm|recs|18535 | betmgm | Mason Taylor | recs | over | 1.0 | 0.5665 | 0.4335 | False | 2026-10-22T13:57:22Z |
| draftkings|380428471|0QA380428471#2326683930_13L88808Q1-1846552455Q20 | draftkings | Mike Gesicki | Anytime TD Scorer | over | 0.6321 | 0.2083 | 0.4238 | False | 2026-10-20T23:16:14Z |
| betmgm|recs|19230 | betmgm | Ja'Kobi Lane | recs | over | 1.0 | 0.6113 | 0.3887 | False | 2026-10-24T22:37:09Z |
| betmgm|recs|19631 | betmgm | Cyrus Allen | recs | over | 0.9993 | 0.625 | 0.3743 | False | 2026-10-25T04:59:12Z |
| draftkings|380429075|0QA380429075#2326686724_13L88808Q1-1461677560Q20 | draftkings | Foster Moreau | Anytime TD Scorer | over | 0.4831 | 0.1667 | 0.3165 | False | 2026-10-21T20:17:03Z |
| draftkings|380413767|0QA380413767#2326613364_13L88808Q11213714519Q20 | draftkings | Noah Fant | Anytime TD Scorer | over | 0.4173 | 0.1333 | 0.2839 | False | 2026-10-20T05:03:27Z |
| draftkings|380407190|0QA380407190#2326583670_13L88808Q1433051443Q20 | draftkings | Jeremy Ruckert | Anytime TD Scorer | over | 0.3198 | 0.05 | 0.2698 | False | 2026-10-23T05:15:13Z |
| draftkings|380421806|0QA380421806#2326655286_13L88808Q1999478588Q20 | draftkings | Kyle Pitts Sr. | Anytime TD Scorer | over | 0.5157 | 0.25 | 0.2657 | False | 2026-10-21T05:03:46Z |
| draftkings|381031860|0QA381031860#2329023414_13L88808Q1-1016060448Q20 | draftkings | Mike Gesicki | 2+ TDs | over | 0.2642 | 0.0244 | 0.2399 | False | 2026-10-20T23:16:14Z |
| draftkings|380413767|0QA380413767#2326613373_13L88808Q11402568200Q20 | draftkings | Pat Freiermuth | Anytime TD Scorer | over | 0.4951 | 0.274 | 0.2211 | False | 2026-10-20T05:03:27Z |
| draftkings|380407190|0QA380407190#2326583663_13L88808Q1938922925Q20 | draftkings | Omar Cooper Jr. | Anytime TD Scorer | over | 0.4182 | 0.2041 | 0.2141 | False | 2026-10-23T05:15:13Z |
| draftkings|380408418|0QA380408418#2326589002_13L88808Q1-1885662408Q20 | draftkings | Mo Alie-Cox | Anytime TD Scorer | over | 0.3198 | 0.1111 | 0.2087 | False | 2026-10-21T05:03:46Z |
| draftkings|380429075|0QA380429075#2326686729_13L88808Q1-1809117535Q20 | draftkings | Isaiah Likely | Anytime TD Scorer | over | 0.569 | 0.3636 | 0.2054 | False | 2026-10-19T15:46:16Z |
| betmgm|anytd|19241 | betmgm | Jonah Coleman | anytd | over | 0.4182 | 0.2174 | 0.2008 | False | 2026-10-24T12:49:27Z |
| draftkings|380428471|0QA380428471#2329037509_13L88808Q1-700661814Q20 | draftkings | Matthew Hibner | Anytime TD Scorer | over | 0.276 | 0.0769 | 0.199 | False | 2026-10-20T23:16:14Z |
| draftkings|380413767|0QA380413767#2326613357_13L88808Q11055160431Q20 | draftkings | Alvin Kamara | Anytime TD Scorer | over | 0.4908 | 0.2941 | 0.1967 | False | 2026-10-19T15:46:16Z |
| draftkings|380412485|0QA380412485#2326628065_13L88808Q11141276074Q20 | draftkings | Sean Tucker | Anytime TD Scorer | over | 0.3677 | 0.1818 | 0.1858 | False | 2026-10-21T13:58:59Z |
| betmgm|anytd|19426 | betmgm | Josh Cuevas | anytd | over | 0.2704 | 0.0909 | 0.1795 | False | 2026-10-22T05:06:55Z |
| draftkings|380407190|0QA380407190#2326583686_13L88808Q1-533028316Q20 | draftkings | Kevin Coleman Jr. | Anytime TD Scorer | over | 0.2704 | 0.0909 | 0.1795 | False | 2026-10-23T05:15:13Z |
| betmgm|anytd|10729 | betmgm | Jared Goff | anytd | over | 0.2404 | 0.0645 | 0.1759 | False | 2026-10-20T13:42:44Z |
| draftkings|380429075|0QA380429075#2326686734_13L88808Q1-98347530Q20 | draftkings | Tyrone Tracy Jr. | Anytime TD Scorer | over | 0.4035 | 0.2326 | 0.1709 | False | 2026-10-21T20:17:03Z |
| draftkings|380412485|0QA380412485#2326607832_13L88808Q1-813345382Q20 | draftkings | Tommy Tremble | Anytime TD Scorer | over | 0.4231 | 0.2597 | 0.1633 | False | 2026-10-19T15:46:16Z |
| draftkings|381249289|0QA381249289#2329855705_13L88808Q1-861767826Q20 | draftkings | Isaiah Likely | 2+ TDs | over | 0.2063 | 0.0476 | 0.1586 | False | 2026-10-21T20:17:03Z |
| draftkings|380429075|0QA380429075#2326686720_13L88808Q1-2078311456Q20 | draftkings | Jaylin Noel | Anytime TD Scorer | over | 0.3729 | 0.2174 | 0.1555 | False | 2026-10-21T20:17:03Z |
| draftkings|380428471|0QA380428471#2326683924_13L88808Q11714132096Q20 | draftkings | Josh Cuevas | Anytime TD Scorer | over | 0.2704 | 0.1176 | 0.1527 | False | 2026-10-20T23:16:14Z |
| betmgm|anytd|19314 | betmgm | Omar Cooper | anytd | over | 0.4182 | 0.2703 | 0.148 | False | 2026-10-21T13:58:59Z |
| draftkings|380407190|0QA380407190#2326583676_13L88808Q11579636272Q20 | draftkings | Malik Willis | Anytime TD Scorer | over | 0.3397 | 0.2 | 0.1397 | False | 2026-10-23T05:15:13Z |
| draftkings|380421806|0QA380421806#2326655297_13L88808Q1-2099105975Q20 | draftkings | George Kittle | Anytime TD Scorer | over | 0.5733 | 0.4348 | 0.1385 | False | 2026-10-21T05:03:46Z |
| draftkings|380421646|0QA380421646#2326654433_13L88808Q1-262322861Q20 | draftkings | Blake Whiteheart | Anytime TD Scorer | over | 0.2084 | 0.0714 | 0.137 | False | 2026-10-20T23:16:14Z |
| draftkings|380421806|0QA380421806#2326655287_13L88808Q1-419764349Q20 | draftkings | Jahan Dotson | Anytime TD Scorer | over | 0.357 | 0.2222 | 0.1348 | False | 2026-10-21T05:03:46Z |
| draftkings|381161194|0QA381161194#2329504817_13L88808Q1-2084365438Q20 | draftkings | Chuba Hubbard | 2+ TDs | over | 0.3247 | 0.1905 | 0.1342 | False | 2026-10-21T13:58:59Z |
| draftkings|381047910|0QA381047910#2329089074_13L88808Q1-703917339Q20 | draftkings | Kyle Pitts Sr. | 2+ TDs | over | 0.1645 | 0.0323 | 0.1323 | False | 2026-10-21T05:03:46Z |
| draftkings|380407199|0QA380407199#2326583780_13L88808Q1-1013491361Q20 | draftkings | Ollie Gordon II | 2+ TDs | over | 0.1947 | 0.0625 | 0.1322 | False | 2026-10-23T05:15:13Z |
| draftkings|380421806|0QA380421806#2326655290_13L88808Q1-189550648Q20 | draftkings | Austin Hooper | Anytime TD Scorer | over | 0.2084 | 0.0769 | 0.1315 | False | 2026-10-21T05:03:46Z |
| draftkings|380413767|0QA380413767#2326613365_13L88808Q144959304Q20 | draftkings | Tyler Shough | Anytime TD Scorer | over | 0.3173 | 0.1905 | 0.1268 | False | 2026-10-20T05:03:27Z |
| draftkings|381249289|0QA381249289#2329855701_13L88808Q1257323792Q20 | draftkings | Foster Moreau | 2+ TDs | over | 0.142 | 0.0164 | 0.1256 | False | 2026-10-21T20:17:03Z |
| draftkings|380421646|0QA380421646#2326654429_13L88808Q1-914474805Q20 | draftkings | Jaleel McLaughlin | Anytime TD Scorer | over | 0.2084 | 0.0833 | 0.1251 | False | 2026-10-23T20:01:31Z |
| draftkings|380413767|0QA380413767#2326613374_13L88808Q1-1532462247Q20 | draftkings | Darnell Washington | Anytime TD Scorer | over | 0.357 | 0.2439 | 0.1131 | False | 2026-10-20T05:03:27Z |
| draftkings|380726543|0QA380726543#2327888777_13L88808Q1839820985Q20 | draftkings | Alvin Kamara | 2+ TDs | over | 0.1472 | 0.0345 | 0.1127 | False | 2026-10-20T05:03:27Z |
| draftkings|380726543|0QA380726543#2327888819_13L88808Q1-162258478Q20 | draftkings | Pat Freiermuth | 2+ TDs | over | 0.15 | 0.0385 | 0.1116 | False | 2026-10-20T05:03:27Z |
| draftkings|381047910|0QA381047910#2329089082_13L88808Q11108077714Q20 | draftkings | George Kittle | 2+ TDs | over | 0.2099 | 0.1 | 0.1099 | False | 2026-10-21T05:03:46Z |
| draftkings|380412485|0QA380412485#2326607835_13L88808Q1259912862Q20 | draftkings | John Metchie III | Anytime TD Scorer | over | 0.2084 | 0.1053 | 0.1031 | False | 2026-10-21T13:58:59Z |
| draftkings|380413767|0QA380413767#2326613363_13L88808Q11438391772Q20 | draftkings | Bryce Lance | Anytime TD Scorer | over | 0.2277 | 0.125 | 0.1027 | False | 2026-10-20T05:03:27Z |
| draftkings|380429075|0QA380429075#2326686735_13L88808Q11930260006Q20 | draftkings | Devin Singletary | Anytime TD Scorer | over | 0.253 | 0.1538 | 0.0991 | False | 2026-10-21T20:17:03Z |
| draftkings|380428471|0QA380428471#2326683935_13L88808Q1219777051Q20 | draftkings | Joe Burrow | Anytime TD Scorer | over | 0.2015 | 0.1053 | 0.0962 | False | 2026-10-20T23:16:14Z |
| draftkings|380407190|0QA380407190#2326583667_13L88808Q12123082164Q20 | draftkings | Isaiah Williams | Anytime TD Scorer | over | 0.1675 | 0.0714 | 0.0961 | False | 2026-10-23T05:15:13Z |
| betmgm|anytd|14371 | betmgm | Jordan Love | anytd | over | 0.2277 | 0.1333 | 0.0943 | False | 2026-10-20T13:42:44Z |
| betmgm|anytd|19319 | betmgm | Bryce Lance | anytd | over | 0.2277 | 0.1333 | 0.0943 | False | 2026-10-20T13:42:44Z |
| draftkings|380726543|0QA380726543#2327888781_13L88808Q1669299964Q20 | draftkings | Noah Fant | 2+ TDs | over | 0.1026 | 0.0123 | 0.0902 | False | 2026-10-20T05:03:27Z |
| draftkings|381094650|0QA381094650#2329260714_13L88808Q1282689831Q20 | draftkings | Jonathan Taylor | 2+ TDs | over | 0.2783 | 0.1905 | 0.0879 | False | 2026-10-21T05:03:46Z |
| draftkings|380428471|0QA380428471#2326683921_13L88808Q1-1199795272Q20 | draftkings | Devontez Walker | Anytime TD Scorer | over | 0.2015 | 0.1176 | 0.0838 | False | 2026-10-20T23:16:14Z |
| draftkings|380407199|0QA380407199#2326583769_13L88808Q11556693862Q20 | draftkings | Omar Cooper Jr. | 2+ TDs | over | 0.1031 | 0.0244 | 0.0787 | False | 2026-10-23T05:15:13Z |
| draftkings|381161194|0QA381161194#2329504821_13L88808Q1372601323Q20 | draftkings | Tommy Tremble | 2+ TDs | over | 0.1057 | 0.0323 | 0.0735 | False | 2026-10-21T13:58:59Z |
| draftkings|380421806|0QA380421806#2326663462_13L88808Q1436278619Q20 | draftkings | Brandin Cooks | Anytime TD Scorer | over | 0.276 | 0.2041 | 0.0719 | False | 2026-10-21T05:03:46Z |
| draftkings|381031860|0QA381031860#2329023363_13L88808Q11526916627Q20 | draftkings | Ja'Marr Chase | 2+ TDs | over | 0.1894 | 0.1176 | 0.0718 | False | 2026-10-20T23:16:14Z |
| draftkings|380412485|0QA380412485#2326628064_13L88808Q1-1664922884Q20 | draftkings | Baker Mayfield | Anytime TD Scorer | over | 0.253 | 0.1818 | 0.0712 | False | 2026-10-21T13:58:59Z |
| draftkings|381249289|0QA381249289#2329855708_13L88808Q1-264458659Q20 | draftkings | Tyrone Tracy Jr. | 2+ TDs | over | 0.0953 | 0.0323 | 0.063 | False | 2026-10-21T20:17:03Z |
| draftkings|380428471|0QA380428471#2326683927_13L88808Q11365449708Q20 | draftkings | Ja'Marr Chase | Anytime TD Scorer | over | 0.5484 | 0.4878 | 0.0606 | False | 2026-10-19T15:46:16Z |
| draftkings|381161194|0QA381161194#2329504834_13L88808Q1-1540780736Q20 | draftkings | Sean Tucker | 2+ TDs | over | 0.0778 | 0.0217 | 0.0561 | False | 2026-10-21T13:58:59Z |
| betmgm|anytd|15875 | betmgm | Dameon Pierce | anytd | over | 0.4182 | 0.3636 | 0.0546 | False | 2026-10-22T13:57:22Z |
| draftkings|381249289|0QA381249289#2329855696_13L88808Q1-1591602463Q20 | draftkings | Jaylin Noel | 2+ TDs | over | 0.0803 | 0.0278 | 0.0525 | False | 2026-10-21T20:17:03Z |
| draftkings|380407199|0QA380407199#2326583776_13L88808Q1-1516021202Q20 | draftkings | Jeremy Ruckert | 2+ TDs | over | 0.0577 | 0.0058 | 0.0518 | False | 2026-10-23T05:15:13Z |
| draftkings|380408418|0QA380408418#2326589001_13L88808Q1-1969802282Q20 | draftkings | Daniel Jones | Anytime TD Scorer | over | 0.1675 | 0.1176 | 0.0499 | False | 2026-10-21T05:03:46Z |
| draftkings|381094650|0QA381094650#2329260720_13L88808Q1117002188Q20 | draftkings | Mo Alie-Cox | 2+ TDs | over | 0.0577 | 0.0099 | 0.0478 | False | 2026-10-21T05:03:46Z |
| draftkings|380421646|0QA380421646#2326654425_13L88808Q1466829631Q20 | draftkings | Harold Fannin Jr. | Anytime TD Scorer | over | 0.375 | 0.3279 | 0.0471 | False | 2026-10-20T05:03:27Z |
| draftkings|380421646|0QA380421646#2326654426_13L88808Q1-1280421193Q20 | draftkings | Denzel Boston | Anytime TD Scorer | over | 0.3397 | 0.2941 | 0.0455 | False | 2026-10-23T20:01:31Z |
| draftkings|381047910|0QA381047910#2329089075_13L88808Q1258503148Q20 | draftkings | Jahan Dotson | 2+ TDs | over | 0.0731 | 0.0278 | 0.0453 | False | 2026-10-21T05:03:46Z |
| draftkings|381047910|0QA381047910#2329089081_13L88808Q1-1442390665Q20 | draftkings | Christian McCaffrey | 2+ TDs | over | 0.3726 | 0.3279 | 0.0447 | False | 2026-10-21T05:03:46Z |
| draftkings|380413767|0QA380413767#2326613361_13L88808Q1873985604Q20 | draftkings | Juwan Johnson | Anytime TD Scorer | over | 0.3093 | 0.2667 | 0.0426 | False | 2026-10-20T05:03:27Z |
| draftkings|380429075|0QA380429075#2326686731_13L88808Q1-1087231219Q20 | draftkings | Malachi Fields | Anytime TD Scorer | over | 0.1675 | 0.125 | 0.0425 | False | 2026-10-22T05:06:55Z |
| draftkings|380429075|0QA380429075#2326686728_13L88808Q1-1380864812Q20 | draftkings | Malik Nabers | Anytime TD Scorer | over | 0.3241 | 0.2817 | 0.0424 | False | 2026-10-23T20:01:31Z |
| draftkings|380412485|0QA380412485#2326607833_13L88808Q1294436062Q20 | draftkings | Darren Waller | Anytime TD Scorer | over | 0.2739 | 0.2326 | 0.0413 | False | 2026-10-22T05:06:55Z |
| draftkings|380407199|0QA380407199#2326583781_13L88808Q11497893303Q20 | draftkings | Malik Willis | 2+ TDs | over | 0.0656 | 0.0244 | 0.0412 | False | 2026-10-23T05:15:13Z |
| draftkings|380726543|0QA380726543#2327888820_13L88808Q1854391200Q20 | draftkings | Darnell Washington | 2+ TDs | over | 0.0731 | 0.0323 | 0.0408 | False | 2026-10-20T05:03:27Z |
| draftkings|381034253|0QA381034253#2329031692_13L88808Q1-862670716Q20 | draftkings | Harold Fannin Jr. | 2+ TDs | over | 0.0812 | 0.0435 | 0.0378 | False | 2026-10-21T13:58:59Z |
| draftkings|380429075|0QA380429075#2326686716_13L88808Q11759839095Q20 | draftkings | Nico Collins | Anytime TD Scorer | over | 0.4819 | 0.4444 | 0.0375 | False | 2026-10-22T05:06:55Z |
| draftkings|381031860|0QA381031860#2329037525_13L88808Q1-1618269213Q20 | draftkings | Matthew Hibner | 2+ TDs | over | 0.0422 | 0.0062 | 0.036 | False | 2026-10-20T23:16:14Z |
| draftkings|380726543|0QA380726543#2327888779_13L88808Q1-1801413616Q20 | draftkings | Tyler Shough | 2+ TDs | over | 0.0567 | 0.0217 | 0.035 | False | 2026-10-20T05:03:27Z |
| draftkings|380421646|0QA380421646#2326654412_13L88808Q117668529Q20 | draftkings | Wan'Dale Robinson | Anytime TD Scorer | over | 0.2787 | 0.2439 | 0.0348 | False | 2026-10-20T23:16:14Z |
| draftkings|380429075|0QA380429075#2326686722_13L88808Q1242387080Q20 | draftkings | C.J. Stroud | Anytime TD Scorer | over | 0.1881 | 0.1538 | 0.0342 | False | 2026-10-24T12:49:27Z |
| draftkings|380407199|0QA380407199#2326583791_13L88808Q11465906394Q20 | draftkings | Kevin Coleman Jr. | 2+ TDs | over | 0.0404 | 0.0071 | 0.0333 | False | 2026-10-23T05:15:13Z |
| draftkings|381031860|0QA381031860#2329023407_13L88808Q1-966863650Q20 | draftkings | Josh Cuevas | 2+ TDs | over | 0.0404 | 0.009 | 0.0314 | False | 2026-10-21T13:58:59Z |
| draftkings|380421806|0QA380421806#2326655302_13L88808Q11061966518Q20 | draftkings | Kyle Juszczyk | Anytime TD Scorer | over | 0.1732 | 0.1429 | 0.0304 | False | 2026-10-24T12:49:27Z |
| draftkings|381249289|0QA381249289#2329855692_13L88808Q1-721675132Q20 | draftkings | Nico Collins | 2+ TDs | over | 0.1412 | 0.1111 | 0.0301 | False | 2026-10-21T20:17:03Z |
