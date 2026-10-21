# Props Pipeline Digest -- 2026-10-21T13:58:44Z

## Run summary
- DraftKings ingestion: 577 rows across 8 events (OK)
- FanDuel ingestion: 0 rows (OK)
- BetMGM ingestion (via Rotowire): 598 rows (OK)
- Estimation: 1175 rows written (from 1175 ingested rows) -- status breakdown: {'estimated': 627, 'unsupported_market_first_scorer': 333, 'unsupported_stat_type': 99, 'no_player_match': 86, 'insufficient_history': 30}
- CLV logging: 12 newly flagged, 0 newly closed, 72 still open (1183 total ever logged)

## Currently open flags
Sizing is a manual step (`sizing_engine.py props size`, Session 6.4) -- this table is what to scan to pick a flag worth sizing. `implied_prob_includes_field_vig` matters here more than for the other tracks: a row still reporting True carries a real, separate uncertainty (Session 6.4's `PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER` dampener) that a bigger raw edge number does not describe.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_model_prob | first_flagged_market_price | first_flagged_edge | implied_prob_includes_field_vig | first_flagged_at |
|---|---|---|---|---|---|---|---|---|---|
| betmgm|recs|13432 | betmgm | A.J. Brown | recs | over | 1.0 | 0.4248 | 0.5752 | False | 2026-10-20T13:42:44Z |
| betmgm|recs|19126 | betmgm | Kyle Williams | recs | over | 1.0 | 0.4425 | 0.5575 | False | 2026-10-20T13:42:44Z |
| betmgm|recs|19348 | betmgm | Eli Raridon | recs | over | 1.0 | 0.4653 | 0.5347 | False | 2026-10-20T13:42:44Z |
| draftkings|380428471|0QA380428471#2326683930_13L88808Q1-1846552455Q20 | draftkings | Mike Gesicki | Anytime TD Scorer | over | 0.6321 | 0.2083 | 0.4238 | False | 2026-10-20T23:16:14Z |
| draftkings|380413767|0QA380413767#2326613364_13L88808Q11213714519Q20 | draftkings | Noah Fant | Anytime TD Scorer | over | 0.4173 | 0.1333 | 0.2839 | False | 2026-10-20T05:03:27Z |
| draftkings|380414163|0QA380414163#2326615207_13L88808Q1-205213128Q20 | draftkings | Demario Douglas | Anytime TD Scorer | over | 0.4908 | 0.2174 | 0.2735 | False | 2026-10-19T04:57:20Z |
| draftkings|380421806|0QA380421806#2326655286_13L88808Q1999478588Q20 | draftkings | Kyle Pitts Sr. | Anytime TD Scorer | over | 0.5157 | 0.25 | 0.2657 | False | 2026-10-21T05:03:46Z |
| draftkings|381031860|0QA381031860#2329023414_13L88808Q1-1016060448Q20 | draftkings | Mike Gesicki | 2+ TDs | over | 0.2642 | 0.0244 | 0.2399 | False | 2026-10-20T23:16:14Z |
| draftkings|380421806|0QA380421806#2326655285_13L88808Q12077388378Q20 | draftkings | Brian Robinson Jr. | Anytime TD Scorer | over | 0.5001 | 0.2632 | 0.2369 | False | 2026-10-21T05:03:46Z |
| draftkings|380414163|0QA380414163#2326615197_13L88808Q11505799344Q20 | draftkings | Caleb Williams | Anytime TD Scorer | over | 0.442 | 0.2174 | 0.2246 | False | 2026-10-19T04:57:20Z |
| draftkings|380413767|0QA380413767#2326613373_13L88808Q11402568200Q20 | draftkings | Pat Freiermuth | Anytime TD Scorer | over | 0.4951 | 0.274 | 0.2211 | False | 2026-10-20T05:03:27Z |
| draftkings|380414163|0QA380414163#2326615199_13L88808Q1-1770507643Q20 | draftkings | Jahdae Walker | Anytime TD Scorer | over | 0.253 | 0.0435 | 0.2095 | False | 2026-10-19T04:57:20Z |
| draftkings|380408418|0QA380408418#2326589002_13L88808Q1-1885662408Q20 | draftkings | Mo Alie-Cox | Anytime TD Scorer | over | 0.3198 | 0.1111 | 0.2087 | False | 2026-10-21T05:03:46Z |
| draftkings|380429075|0QA380429075#2326686729_13L88808Q1-1809117535Q20 | draftkings | Isaiah Likely | Anytime TD Scorer | over | 0.569 | 0.3636 | 0.2054 | False | 2026-10-19T15:46:16Z |
| draftkings|380428471|0QA380428471#2329037509_13L88808Q1-700661814Q20 | draftkings | Matthew Hibner | Anytime TD Scorer | over | 0.276 | 0.0769 | 0.199 | False | 2026-10-20T23:16:14Z |
| draftkings|380413767|0QA380413767#2326613357_13L88808Q11055160431Q20 | draftkings | Alvin Kamara | Anytime TD Scorer | over | 0.4908 | 0.2941 | 0.1967 | False | 2026-10-19T15:46:16Z |
| draftkings|380412485|0QA380412485#2326628065_13L88808Q11141276074Q20 | draftkings | Sean Tucker | Anytime TD Scorer | over | 0.3677 | 0.1818 | 0.1858 | False | 2026-10-21T13:58:59Z |
| betmgm|anytd|10729 | betmgm | Jared Goff | anytd | over | 0.2404 | 0.0645 | 0.1759 | False | 2026-10-20T13:42:44Z |
| draftkings|380412485|0QA380412485#2326607832_13L88808Q1-813345382Q20 | draftkings | Tommy Tremble | Anytime TD Scorer | over | 0.4231 | 0.2597 | 0.1633 | False | 2026-10-19T15:46:16Z |
| draftkings|380408418|0QA380408418#2326606650_13L88808Q1-297522584Q20 | draftkings | Tyler Warren | Anytime TD Scorer | over | 0.4373 | 0.2778 | 0.1595 | False | 2026-10-21T05:03:46Z |
| draftkings|380428471|0QA380428471#2326683924_13L88808Q11714132096Q20 | draftkings | Josh Cuevas | Anytime TD Scorer | over | 0.2704 | 0.1176 | 0.1527 | False | 2026-10-20T23:16:14Z |
| betmgm|anytd|19314 | betmgm | Omar Cooper | anytd | over | 0.4182 | 0.2703 | 0.148 | False | 2026-10-21T13:58:59Z |
| draftkings|380421806|0QA380421806#2326655297_13L88808Q1-2099105975Q20 | draftkings | George Kittle | Anytime TD Scorer | over | 0.5733 | 0.4348 | 0.1385 | False | 2026-10-21T05:03:46Z |
| draftkings|380421646|0QA380421646#2326654433_13L88808Q1-262322861Q20 | draftkings | Blake Whiteheart | Anytime TD Scorer | over | 0.2084 | 0.0714 | 0.137 | False | 2026-10-20T23:16:14Z |
| betmgm|anytd|19322 | betmgm | Kevin Coleman | anytd | over | 0.2704 | 0.1333 | 0.137 | False | 2026-10-21T13:58:59Z |
| draftkings|380421806|0QA380421806#2326655287_13L88808Q1-419764349Q20 | draftkings | Jahan Dotson | Anytime TD Scorer | over | 0.357 | 0.2222 | 0.1348 | False | 2026-10-21T05:03:46Z |
| draftkings|381161194|0QA381161194#2329504817_13L88808Q1-2084365438Q20 | draftkings | Chuba Hubbard | 2+ TDs | over | 0.3247 | 0.1905 | 0.1342 | False | 2026-10-21T13:58:59Z |
| draftkings|381047910|0QA381047910#2329089074_13L88808Q1-703917339Q20 | draftkings | Kyle Pitts Sr. | 2+ TDs | over | 0.1645 | 0.0323 | 0.1323 | False | 2026-10-21T05:03:46Z |
| draftkings|380421806|0QA380421806#2326655290_13L88808Q1-189550648Q20 | draftkings | Austin Hooper | Anytime TD Scorer | over | 0.2084 | 0.0769 | 0.1315 | False | 2026-10-21T05:03:46Z |
| draftkings|380413767|0QA380413767#2326613365_13L88808Q144959304Q20 | draftkings | Tyler Shough | Anytime TD Scorer | over | 0.3173 | 0.1905 | 0.1268 | False | 2026-10-20T05:03:27Z |
| draftkings|380457140|0QA380457140#2326805310_13L88808Q1573901773Q20 | draftkings | Demario Douglas | 2+ TDs | over | 0.1472 | 0.0278 | 0.1194 | False | 2026-10-19T04:57:20Z |
| draftkings|381047910|0QA381047910#2329089073_13L88808Q1-2016866086Q20 | draftkings | Brian Robinson Jr. | 2+ TDs | over | 0.1535 | 0.0385 | 0.115 | False | 2026-10-21T05:03:46Z |
| draftkings|380413767|0QA380413767#2326613374_13L88808Q1-1532462247Q20 | draftkings | Darnell Washington | Anytime TD Scorer | over | 0.357 | 0.2439 | 0.1131 | False | 2026-10-20T05:03:27Z |
| draftkings|380726543|0QA380726543#2327888777_13L88808Q1839820985Q20 | draftkings | Alvin Kamara | 2+ TDs | over | 0.1472 | 0.0345 | 0.1127 | False | 2026-10-20T05:03:27Z |
| draftkings|380726543|0QA380726543#2327888819_13L88808Q1-162258478Q20 | draftkings | Pat Freiermuth | 2+ TDs | over | 0.15 | 0.0385 | 0.1116 | False | 2026-10-20T05:03:27Z |
| draftkings|381047910|0QA381047910#2329089082_13L88808Q11108077714Q20 | draftkings | George Kittle | 2+ TDs | over | 0.2099 | 0.1 | 0.1099 | False | 2026-10-21T05:03:46Z |
| draftkings|380412485|0QA380412485#2326607835_13L88808Q1259912862Q20 | draftkings | John Metchie III | Anytime TD Scorer | over | 0.2084 | 0.1053 | 0.1031 | False | 2026-10-21T13:58:59Z |
| draftkings|380413767|0QA380413767#2326613363_13L88808Q11438391772Q20 | draftkings | Bryce Lance | Anytime TD Scorer | over | 0.2277 | 0.125 | 0.1027 | False | 2026-10-20T05:03:27Z |
| draftkings|380428471|0QA380428471#2326683935_13L88808Q1219777051Q20 | draftkings | Joe Burrow | Anytime TD Scorer | over | 0.2015 | 0.1053 | 0.0962 | False | 2026-10-20T23:16:14Z |
| betmgm|anytd|19319 | betmgm | Bryce Lance | anytd | over | 0.2277 | 0.1333 | 0.0943 | False | 2026-10-20T13:42:44Z |
| betmgm|anytd|14371 | betmgm | Jordan Love | anytd | over | 0.2277 | 0.1333 | 0.0943 | False | 2026-10-20T13:42:44Z |
| draftkings|380726543|0QA380726543#2327888781_13L88808Q1669299964Q20 | draftkings | Noah Fant | 2+ TDs | over | 0.1026 | 0.0123 | 0.0902 | False | 2026-10-20T05:03:27Z |
| draftkings|380457140|0QA380457140#2326805300_13L88808Q1-77651570Q20 | draftkings | Caleb Williams | 2+ TDs | over | 0.1164 | 0.0278 | 0.0887 | False | 2026-10-19T04:57:20Z |
| draftkings|381094650|0QA381094650#2329260714_13L88808Q1282689831Q20 | draftkings | Jonathan Taylor | 2+ TDs | over | 0.2783 | 0.1905 | 0.0879 | False | 2026-10-21T05:03:46Z |
| draftkings|380428471|0QA380428471#2326683921_13L88808Q1-1199795272Q20 | draftkings | Devontez Walker | Anytime TD Scorer | over | 0.2015 | 0.1176 | 0.0838 | False | 2026-10-20T23:16:14Z |
| draftkings|380414163|0QA380414163#2326615211_13L88808Q11958986630Q20 | draftkings | Kyle Williams | Anytime TD Scorer | over | 0.1881 | 0.1111 | 0.077 | False | 2026-10-19T04:57:20Z |
| draftkings|381094650|0QA381094650#2329260717_13L88808Q11041398384Q20 | draftkings | Tyler Warren | 2+ TDs | over | 0.1137 | 0.0385 | 0.0753 | False | 2026-10-21T05:03:46Z |
| draftkings|381161194|0QA381161194#2329504821_13L88808Q1372601323Q20 | draftkings | Tommy Tremble | 2+ TDs | over | 0.1057 | 0.0323 | 0.0735 | False | 2026-10-21T13:58:59Z |
| draftkings|380421806|0QA380421806#2326663462_13L88808Q1436278619Q20 | draftkings | Brandin Cooks | Anytime TD Scorer | over | 0.276 | 0.2041 | 0.0719 | False | 2026-10-21T05:03:46Z |
| draftkings|381031860|0QA381031860#2329023363_13L88808Q11526916627Q20 | draftkings | Ja'Marr Chase | 2+ TDs | over | 0.1894 | 0.1176 | 0.0718 | False | 2026-10-20T23:16:14Z |
| draftkings|380412485|0QA380412485#2326628064_13L88808Q1-1664922884Q20 | draftkings | Baker Mayfield | Anytime TD Scorer | over | 0.253 | 0.1818 | 0.0712 | False | 2026-10-21T13:58:59Z |
| draftkings|380412485|0QA380412485#2326607841_13L88808Q1621783265Q20 | draftkings | Emeka Egbuka | Anytime TD Scorer | over | 0.4457 | 0.3774 | 0.0683 | False | 2026-10-19T15:46:16Z |
| draftkings|381161194|0QA381161194#2329504830_13L88808Q11465714566Q20 | draftkings | Emeka Egbuka | 2+ TDs | over | 0.1186 | 0.0526 | 0.066 | False | 2026-10-21T13:58:59Z |
| betmgm|anytd|17968 | betmgm | George Holani | anytd | over | 0.2277 | 0.1667 | 0.061 | False | 2026-10-21T13:58:59Z |
| draftkings|380428471|0QA380428471#2326683927_13L88808Q11365449708Q20 | draftkings | Ja'Marr Chase | Anytime TD Scorer | over | 0.5484 | 0.4878 | 0.0606 | False | 2026-10-19T15:46:16Z |
| draftkings|380414163|0QA380414163#2326615206_13L88808Q1-1762786291Q20 | draftkings | Hunter Henry | Anytime TD Scorer | over | 0.3729 | 0.3125 | 0.0604 | False | 2026-10-19T04:57:20Z |
| draftkings|381161194|0QA381161194#2329504834_13L88808Q1-1540780736Q20 | draftkings | Sean Tucker | 2+ TDs | over | 0.0778 | 0.0217 | 0.0561 | False | 2026-10-21T13:58:59Z |
| draftkings|380408418|0QA380408418#2326589001_13L88808Q1-1969802282Q20 | draftkings | Daniel Jones | Anytime TD Scorer | over | 0.1675 | 0.1176 | 0.0499 | False | 2026-10-21T05:03:46Z |
| draftkings|381094650|0QA381094650#2329260720_13L88808Q1117002188Q20 | draftkings | Mo Alie-Cox | 2+ TDs | over | 0.0577 | 0.0099 | 0.0478 | False | 2026-10-21T05:03:46Z |
| draftkings|380421646|0QA380421646#2326654425_13L88808Q1466829631Q20 | draftkings | Harold Fannin Jr. | Anytime TD Scorer | over | 0.375 | 0.3279 | 0.0471 | False | 2026-10-20T05:03:27Z |
| draftkings|381047910|0QA381047910#2329089075_13L88808Q1258503148Q20 | draftkings | Jahan Dotson | 2+ TDs | over | 0.0731 | 0.0278 | 0.0453 | False | 2026-10-21T05:03:46Z |
| draftkings|381047910|0QA381047910#2329089081_13L88808Q1-1442390665Q20 | draftkings | Christian McCaffrey | 2+ TDs | over | 0.3726 | 0.3279 | 0.0447 | False | 2026-10-21T05:03:46Z |
| draftkings|380413767|0QA380413767#2326613361_13L88808Q1873985604Q20 | draftkings | Juwan Johnson | Anytime TD Scorer | over | 0.3093 | 0.2667 | 0.0426 | False | 2026-10-20T05:03:27Z |
| draftkings|380726543|0QA380726543#2327888820_13L88808Q1854391200Q20 | draftkings | Darnell Washington | 2+ TDs | over | 0.0731 | 0.0323 | 0.0408 | False | 2026-10-20T05:03:27Z |
| draftkings|381034253|0QA381034253#2329031692_13L88808Q1-862670716Q20 | draftkings | Harold Fannin Jr. | 2+ TDs | over | 0.0812 | 0.0435 | 0.0378 | False | 2026-10-21T13:58:59Z |
| draftkings|381031860|0QA381031860#2329037525_13L88808Q1-1618269213Q20 | draftkings | Matthew Hibner | 2+ TDs | over | 0.0422 | 0.0062 | 0.036 | False | 2026-10-20T23:16:14Z |
| draftkings|380726543|0QA380726543#2327888779_13L88808Q1-1801413616Q20 | draftkings | Tyler Shough | 2+ TDs | over | 0.0567 | 0.0217 | 0.035 | False | 2026-10-20T05:03:27Z |
| draftkings|380421646|0QA380421646#2326654412_13L88808Q117668529Q20 | draftkings | Wan'Dale Robinson | Anytime TD Scorer | over | 0.2787 | 0.2439 | 0.0348 | False | 2026-10-20T23:16:14Z |
| draftkings|380457140|0QA380457140#2326805294_13L88808Q1-1008695778Q20 | draftkings | D'Andre Swift | 2+ TDs | over | 0.255 | 0.2222 | 0.0328 | False | 2026-10-19T04:57:20Z |
| draftkings|381031860|0QA381031860#2329023407_13L88808Q1-966863650Q20 | draftkings | Josh Cuevas | 2+ TDs | over | 0.0404 | 0.009 | 0.0314 | False | 2026-10-21T13:58:59Z |
| draftkings|380457140|0QA380457140#2326805307_13L88808Q11740203848Q20 | draftkings | Hunter Henry | 2+ TDs | over | 0.0803 | 0.05 | 0.0303 | False | 2026-10-19T04:57:20Z |
| draftkings|380457140|0QA380457140#2326805304_13L88808Q1-704328598Q20 | draftkings | Jahdae Walker | 2+ TDs | over | 0.0351 | 0.005 | 0.0301 | False | 2026-10-19T04:57:20Z |
