# Props Pipeline Digest -- 2026-11-25T14:41:07Z

## Run summary
- DraftKings ingestion: 655 rows across 8 events (OK)
- FanDuel ingestion: 0 rows (OK)
- BetMGM ingestion (via Rotowire): 804 rows (OK)
- Estimation: 1459 rows written (from 1459 ingested rows) -- status breakdown: {'estimated': 735, 'unsupported_market_first_scorer': 415, 'unsupported_stat_type': 211, 'no_player_match': 72, 'insufficient_history': 26}
- CLV logging: 33 newly flagged, 0 newly closed, 84 still open (1794 total ever logged)

## Currently open flags
Sizing is a manual step (`sizing_engine.py props size`, Session 6.4) -- this table is what to scan to pick a flag worth sizing. `implied_prob_includes_field_vig` matters here more than for the other tracks: a row still reporting True carries a real, separate uncertainty (Session 6.4's `PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER` dampener) that a bigger raw edge number does not describe.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_model_prob | first_flagged_market_price | first_flagged_edge | implied_prob_includes_field_vig | first_flagged_at |
|---|---|---|---|---|---|---|---|---|---|
| draftkings|391937589|0QA391937589#2378060839_13L88808Q1-1683593135Q20 | draftkings | Marlin Klein | Anytime TD Scorer | over | 0.4182 | 0.0588 | 0.3594 | False | 2026-11-25T14:41:23Z |
| betmgm|recs|19259 | betmgm | Zavion Thomas | recs | over | 1.0 | 0.6667 | 0.3333 | False | 2026-11-24T15:02:23Z |
| betmgm|recs|17467 | betmgm | Xavier Smith | recs | over | 0.9992 | 0.6667 | 0.3325 | False | 2026-11-24T15:02:23Z |
| betmgm|anytd|19352 | betmgm | Marlin Klein | anytd | over | 0.4182 | 0.087 | 0.3313 | False | 2026-11-25T14:41:23Z |
| draftkings|391617129|0QA391617129#2376389698_13L88808Q1-822030320Q20 | draftkings | Davis Allen | Anytime TD Scorer | over | 0.4182 | 0.1176 | 0.3006 | False | 2026-11-23T15:01:11Z |
| betmgm|anytd|18498 | betmgm | Kyle McCord | anytd | over | 0.3677 | 0.1053 | 0.2624 | False | 2026-11-25T14:41:23Z |
| draftkings|391879785|0QA391879785#2377763120_13L88808Q1917552914Q20 | draftkings | Kenneth Walker III | 2+ TDs | over | 0.4125 | 0.1818 | 0.2307 | False | 2026-11-23T15:01:11Z |
| draftkings|391839147|0QA391839147#2377480792_13L88808Q11402568200Q20 | draftkings | Pat Freiermuth | Anytime TD Scorer | over | 0.4084 | 0.1818 | 0.2266 | False | 2026-11-23T15:01:11Z |
| draftkings|391937589|0QA391937589#2378060835_13L88808Q1-1461677560Q20 | draftkings | Foster Moreau | Anytime TD Scorer | over | 0.3961 | 0.1739 | 0.2222 | False | 2026-11-25T14:41:23Z |
| draftkings|391984111|0QA391984111#2378253787_13L88808Q1872485381Q20 | draftkings | Jonah Coleman | 2+ TDs | over | 0.3696 | 0.1538 | 0.2158 | False | 2026-11-23T15:01:11Z |
| draftkings|391839147|0QA391839147#2377480810_13L88808Q1-577361648Q20 | draftkings | Nate Adkins | Anytime TD Scorer | over | 0.2983 | 0.0833 | 0.215 | False | 2026-11-23T15:01:11Z |
| betmgm|anytd|19447 | betmgm | Colbie Young | anytd | over | 0.3198 | 0.1081 | 0.2117 | False | 2026-11-25T14:41:23Z |
| draftkings|391937589|0QA391937589#2378060836_13L88808Q1401138925Q20 | draftkings | Kayshon Boutte | Anytime TD Scorer | over | 0.4084 | 0.2 | 0.2084 | False | 2026-11-25T14:41:23Z |
| draftkings|391833992|0QA391833992#2377459269_13L88808Q1-511040682Q20 | draftkings | Travis Kelce | Anytime TD Scorer | over | 0.5034 | 0.303 | 0.2004 | False | 2026-11-23T15:01:11Z |
| draftkings|391839147|0QA391839147#2377480811_13L88808Q1-1398413387Q20 | draftkings | Adam Trautman | Anytime TD Scorer | over | 0.2277 | 0.0476 | 0.18 | False | 2026-11-23T15:01:11Z |
| draftkings|391973083|0QA391973083#2378204469_13L88808Q1877705888Q20 | draftkings | Kirk Cousins | Anytime TD Scorer | over | 0.2219 | 0.0556 | 0.1664 | False | 2026-11-25T14:41:23Z |
| draftkings|391617129|0QA391617129#2376389716_13L88808Q1957158759Q20 | draftkings | J. Michael Sturdivant | Anytime TD Scorer | over | 0.2059 | 0.0435 | 0.1624 | False | 2026-11-23T15:01:11Z |
| draftkings|391876015|0QA391876015#2377741453_13L88808Q1-1008695778Q20 | draftkings | D'Andre Swift | 2+ TDs | over | 0.3247 | 0.1667 | 0.158 | False | 2026-11-23T15:01:11Z |
| betmgm|anytd|17467 | betmgm | Xavier Smith | anytd | over | 0.2704 | 0.1143 | 0.1561 | False | 2026-11-24T15:02:23Z |
| draftkings|391617129|0QA391617129#2376389715_13L88808Q1-1213243313Q20 | draftkings | Jordan Love | Anytime TD Scorer | over | 0.2328 | 0.0769 | 0.1559 | False | 2026-11-23T15:01:11Z |
| draftkings|391845390|0QA391845390#2377517123_13L88808Q1795642865Q20 | draftkings | Dak Prescott | Anytime TD Scorer | over | 0.2781 | 0.1333 | 0.1448 | False | 2026-11-23T15:01:11Z |
| draftkings|391959446|0QA391959446#2378143040_13L88808Q1-271780635Q20 | draftkings | Brian Thomas Jr. | Anytime TD Scorer | over | 0.357 | 0.2128 | 0.1443 | False | 2026-11-25T14:41:23Z |
| betmgm|anytd|14541 | betmgm | Adam Trautman | anytd | over | 0.2277 | 0.087 | 0.1407 | False | 2026-11-24T15:02:23Z |
| draftkings|391617129|0QA391617129#2376389703_13L88808Q1-1604380439Q20 | draftkings | Xavier Smith | Anytime TD Scorer | over | 0.2704 | 0.1333 | 0.137 | False | 2026-11-23T15:01:11Z |
| draftkings|391973083|0QA391973083#2378204485_13L88808Q11180641602Q20 | draftkings | Nick Muse | Anytime TD Scorer | over | 0.1575 | 0.0217 | 0.1358 | False | 2026-11-25T14:41:23Z |
| draftkings|391833992|0QA391833992#2377459594_13L88808Q1-985183007Q20 | draftkings | Andrew Armstrong | Anytime TD Scorer | over | 0.1881 | 0.0556 | 0.1325 | False | 2026-11-23T15:01:11Z |
| draftkings|391842938|0QA391842938#2377503377_13L88808Q1480222870Q20 | draftkings | Jameson Williams | Anytime TD Scorer | over | 0.4594 | 0.3279 | 0.1315 | False | 2026-11-23T15:01:11Z |
| draftkings|391973083|0QA391973083#2378204471_13L88808Q1-1841072915Q20 | draftkings | Gavin Bartholomew | Anytime TD Scorer | over | 0.2015 | 0.0714 | 0.1301 | False | 2026-11-25T14:41:23Z |
| draftkings|391845390|0QA391845390#2377517158_13L88808Q1744413187Q20 | draftkings | KaVontae Turpin | Anytime TD Scorer | over | 0.2592 | 0.1333 | 0.1258 | False | 2026-11-23T15:01:11Z |
| draftkings|391839147|0QA391839147#2377480789_13L88808Q11665380004Q20 | draftkings | Roman Wilson | Anytime TD Scorer | over | 0.2787 | 0.1538 | 0.1248 | False | 2026-11-23T15:01:11Z |
| draftkings|391845390|0QA391845390#2377517154_13L88808Q1-1127265655Q20 | draftkings | George Pickens | Anytime TD Scorer | over | 0.5975 | 0.4762 | 0.1213 | False | 2026-11-23T15:01:11Z |
| draftkings|391937589|0QA391937589#2378060845_13L88808Q11994625172Q20 | draftkings | Justice Hill | Anytime TD Scorer | over | 0.3064 | 0.1905 | 0.116 | False | 2026-11-25T14:41:23Z |
| draftkings|391937589|0QA391937589#2378060851_13L88808Q1-1199795272Q20 | draftkings | Devontez Walker | Anytime TD Scorer | over | 0.1675 | 0.0556 | 0.112 | False | 2026-11-25T14:41:23Z |
| draftkings|391973083|0QA391973083#2378204480_13L88808Q1-1356990742Q20 | draftkings | Charlie Woerner | Anytime TD Scorer | over | 0.1783 | 0.0667 | 0.1117 | False | 2026-11-25T14:41:23Z |
| draftkings|391879785|0QA391879785#2377763110_13L88808Q1503159412Q20 | draftkings | James Cook | 2+ TDs | over | 0.2642 | 0.1538 | 0.1104 | False | 2026-11-23T15:01:11Z |
| draftkings|392500152|0QA392500152#2380763534_13L88808Q11746484724Q20 | draftkings | Derrick Henry | 2+ TDs | over | 0.2754 | 0.1667 | 0.1088 | False | 2026-11-25T14:41:23Z |
| draftkings|391879785|0QA391879785#2377763122_13L88808Q1321951862Q20 | draftkings | Travis Kelce | 2+ TDs | over | 0.1558 | 0.0476 | 0.1082 | False | 2026-11-23T15:01:11Z |
| draftkings|391877054|0QA391877054#2377747270_13L88808Q11452024780Q20 | draftkings | George Pickens | 2+ TDs | over | 0.2312 | 0.125 | 0.1062 | False | 2026-11-23T15:01:11Z |
| draftkings|391839147|0QA391839147#2377480806_13L88808Q164075827Q20 | draftkings | Pat Bryant | Anytime TD Scorer | over | 0.2965 | 0.1905 | 0.106 | False | 2026-11-23T15:01:11Z |
| draftkings|391839147|0QA391839147#2377480796_13L88808Q1292660006Q20 | draftkings | Ben Skowronek | Anytime TD Scorer | over | 0.1479 | 0.0435 | 0.1044 | False | 2026-11-23T15:01:11Z |
| draftkings|391959446|0QA391959446#2378143055_13L88808Q1546774868Q20 | draftkings | Calvin Ridley | Anytime TD Scorer | over | 0.2184 | 0.1176 | 0.1008 | False | 2026-11-25T14:41:23Z |
| draftkings|391959446|0QA391959446#2378143047_13L88808Q1410823711Q20 | draftkings | Tony Pollard | Anytime TD Scorer | over | 0.5747 | 0.4762 | 0.0985 | False | 2026-11-25T14:41:23Z |
| draftkings|392500152|0QA392500152#2380763481_13L88808Q11568418663Q20 | draftkings | Marlin Klein | 2+ TDs | over | 0.1031 | 0.0062 | 0.0969 | False | 2026-11-25T14:41:23Z |
| draftkings|391617129|0QA391617129#2376389694_13L88808Q11373713880Q20 | draftkings | Blake Corum | Anytime TD Scorer | over | 0.5507 | 0.4545 | 0.0961 | False | 2026-11-24T02:59:57Z |
| draftkings|391891812|0QA391891812#2377834481_13L88808Q1-1802470485Q20 | draftkings | Davis Allen | 2+ TDs | over | 0.1031 | 0.0099 | 0.0932 | False | 2026-11-23T15:01:11Z |
| draftkings|392601119|0QA392601119#2381201036_13L88808Q11612572832Q20 | draftkings | Tony Pollard | 2+ TDs | over | 0.2111 | 0.125 | 0.0861 | False | 2026-11-25T14:41:23Z |
| draftkings|391876015|0QA391876015#2377741443_13L88808Q11455054237Q20 | draftkings | Jahmyr Gibbs | 2+ TDs | over | 0.4455 | 0.3636 | 0.0819 | False | 2026-11-23T15:01:11Z |
| draftkings|391973083|0QA391973083#2378204475_13L88808Q1999478588Q20 | draftkings | Kyle Pitts Sr. | Anytime TD Scorer | over | 0.2882 | 0.2083 | 0.0799 | False | 2026-11-25T14:41:23Z |
| draftkings|391984111|0QA391984111#2378253776_13L88808Q1-162258478Q20 | draftkings | Pat Freiermuth | 2+ TDs | over | 0.0979 | 0.0196 | 0.0783 | False | 2026-11-23T15:01:11Z |
| draftkings|391833992|0QA391833992#2377459096_13L88808Q11235745545Q20 | draftkings | Keleki Latu | Anytime TD Scorer | over | 0.1441 | 0.0667 | 0.0774 | False | 2026-11-23T15:01:11Z |
| draftkings|392500152|0QA392500152#2380763478_13L88808Q1-1010510811Q20 | draftkings | Kayshon Boutte | 2+ TDs | over | 0.0979 | 0.0217 | 0.0761 | False | 2026-11-25T14:41:23Z |
| draftkings|391617129|0QA391617129#2376389706_13L88808Q11480921309Q20 | draftkings | Matthew Golden | Anytime TD Scorer | over | 0.4025 | 0.3279 | 0.0746 | False | 2026-11-23T15:01:11Z |
| draftkings|391937589|0QA391937589#2378060831_13L88808Q11759839095Q20 | draftkings | Nico Collins | Anytime TD Scorer | over | 0.5393 | 0.4651 | 0.0742 | False | 2026-11-25T14:41:23Z |
| draftkings|391891812|0QA391891812#2377834475_13L88808Q11181433178Q20 | draftkings | Blake Corum | 2+ TDs | over | 0.1912 | 0.1176 | 0.0736 | False | 2026-11-24T02:59:57Z |
| draftkings|392500152|0QA392500152#2380763479_13L88808Q1257323792Q20 | draftkings | Foster Moreau | 2+ TDs | over | 0.0915 | 0.0196 | 0.0719 | False | 2026-11-25T14:41:23Z |
| draftkings|391876015|0QA391876015#2377741446_13L88808Q1-106544391Q20 | draftkings | Jameson Williams | 2+ TDs | over | 0.1269 | 0.0556 | 0.0713 | False | 2026-11-23T15:01:11Z |
| draftkings|391937589|0QA391937589#2378060834_13L88808Q1-1444150535Q20 | draftkings | Xavier Hutchinson | Anytime TD Scorer | over | 0.3527 | 0.2817 | 0.071 | False | 2026-11-25T14:41:23Z |
| draftkings|392500152|0QA392500152#2380763474_13L88808Q1-721675132Q20 | draftkings | Nico Collins | 2+ TDs | over | 0.1823 | 0.1176 | 0.0646 | False | 2026-11-25T14:41:23Z |
| draftkings|391845390|0QA391845390#2377517177_13L88808Q197731504Q20 | draftkings | Will Shipley | Anytime TD Scorer | over | 0.1881 | 0.125 | 0.0631 | False | 2026-11-24T02:59:57Z |
| draftkings|391959446|0QA391959446#2378143056_13L88808Q11550208160Q20 | draftkings | Daniel Bellinger | Anytime TD Scorer | over | 0.1605 | 0.1053 | 0.0553 | False | 2026-11-25T14:41:23Z |
| draftkings|391959446|0QA391959446#2378143039_13L88808Q11380693923Q20 | draftkings | Josh Cameron | Anytime TD Scorer | over | 0.2404 | 0.1905 | 0.05 | False | 2026-11-25T14:41:23Z |
| draftkings|391833992|0QA391833992#2377459341_13L88808Q1439564023Q20 | draftkings | Xavier Worthy | Anytime TD Scorer | over | 0.2404 | 0.1905 | 0.05 | False | 2026-11-23T15:01:11Z |
| draftkings|391973083|0QA391973083#2378204470_13L88808Q1313197721Q20 | draftkings | Myles Price | Anytime TD Scorer | over | 0.1605 | 0.1111 | 0.0494 | False | 2026-11-25T14:41:23Z |
| draftkings|391959446|0QA391959446#2378143042_13L88808Q1-292926888Q20 | draftkings | Nate Boerkircher | Anytime TD Scorer | over | 0.248 | 0.2 | 0.048 | False | 2026-11-25T14:41:23Z |
| draftkings|391879785|0QA391879785#2377763111_13L88808Q11587218485Q20 | draftkings | Josh Allen | 2+ TDs | over | 0.2129 | 0.1667 | 0.0463 | False | 2026-11-23T15:01:11Z |
| draftkings|391833992|0QA391833992#2377459394_13L88808Q1-1195662886Q20 | draftkings | Cyrus Allen | Anytime TD Scorer | over | 0.171 | 0.125 | 0.046 | False | 2026-11-23T15:01:11Z |
| draftkings|391842938|0QA391842938#2377503391_13L88808Q1655740791Q20 | draftkings | Kyle Monangai | Anytime TD Scorer | over | 0.4457 | 0.4 | 0.0457 | False | 2026-11-23T15:01:11Z |
| draftkings|392601119|0QA392601119#2381200976_13L88808Q11304672355Q20 | draftkings | Brian Thomas Jr. | 2+ TDs | over | 0.0731 | 0.0278 | 0.0453 | False | 2026-11-25T14:41:23Z |
| draftkings|391877054|0QA391877054#2377747268_13L88808Q12056061885Q20 | draftkings | Javonte Williams | 2+ TDs | over | 0.2773 | 0.2326 | 0.0447 | False | 2026-11-23T15:01:11Z |
| draftkings|391845390|0QA391845390#2377517165_13L88808Q11750821948Q20 | draftkings | Saquon Barkley | Anytime TD Scorer | over | 0.5084 | 0.4651 | 0.0432 | False | 2026-11-25T14:41:23Z |
| draftkings|391984111|0QA391984111#2378253795_13L88808Q1-1564766902Q20 | draftkings | Nate Adkins | 2+ TDs | over | 0.0497 | 0.0066 | 0.0431 | False | 2026-11-23T15:01:11Z |
| draftkings|391891812|0QA391891812#2377834488_13L88808Q1905210328Q20 | draftkings | Matthew Golden | 2+ TDs | over | 0.0948 | 0.0526 | 0.0422 | False | 2026-11-23T15:01:11Z |
| draftkings|391877054|0QA391877054#2377747269_13L88808Q1-1472312629Q20 | draftkings | CeeDee Lamb | 2+ TDs | over | 0.2235 | 0.1818 | 0.0417 | False | 2026-11-23T15:01:11Z |
| draftkings|391617129|0QA391617129#2376389707_13L88808Q1-135035926Q20 | draftkings | MarShawn Lloyd | Anytime TD Scorer | over | 0.2186 | 0.1818 | 0.0368 | False | 2026-11-23T15:01:11Z |
| draftkings|391959446|0QA391959446#2378143048_13L88808Q11703123874Q20 | draftkings | Carnell Tate | Anytime TD Scorer | over | 0.3297 | 0.2941 | 0.0356 | False | 2026-11-25T14:41:23Z |
| draftkings|391876015|0QA391876015#2377741455_13L88808Q1902102257Q20 | draftkings | Kyle Monangai | 2+ TDs | over | 0.1186 | 0.0833 | 0.0353 | False | 2026-11-23T15:01:11Z |
| draftkings|391617129|0QA391617129#2376389709_13L88808Q11154264979Q20 | draftkings | Savion Williams | Anytime TD Scorer | over | 0.2015 | 0.1667 | 0.0348 | False | 2026-11-23T15:01:11Z |
| draftkings|391877054|0QA391877054#2377747405_13L88808Q113349962Q20 | draftkings | Saquon Barkley | 2+ TDs | over | 0.1593 | 0.125 | 0.0343 | False | 2026-11-23T15:01:11Z |
| draftkings|391937589|0QA391937589#2378060847_13L88808Q1-511742258Q20 | draftkings | Rashod Bateman | Anytime TD Scorer | over | 0.2335 | 0.2 | 0.0335 | False | 2026-11-25T14:41:23Z |
| draftkings|391877054|0QA391877054#2377747273_13L88808Q11269559575Q20 | draftkings | Dak Prescott | 2+ TDs | over | 0.0429 | 0.011 | 0.0319 | False | 2026-11-24T02:59:57Z |
| draftkings|392500152|0QA392500152#2380763536_13L88808Q11902362131Q20 | draftkings | Justice Hill | 2+ TDs | over | 0.0527 | 0.0217 | 0.0309 | False | 2026-11-25T14:41:23Z |
| draftkings|391984111|0QA391984111#2378253777_13L88808Q1-773934870Q20 | draftkings | Roman Wilson | 2+ TDs | over | 0.043 | 0.0123 | 0.0307 | False | 2026-11-23T15:01:11Z |
| draftkings|391839147|0QA391839147#2377480791_13L88808Q1-1532462247Q20 | draftkings | Darnell Washington | Anytime TD Scorer | over | 0.2212 | 0.1905 | 0.0307 | False | 2026-11-24T02:59:57Z |
| draftkings|391891812|0QA391891812#2377834482_13L88808Q1-1231088963Q20 | draftkings | Xavier Smith | 2+ TDs | over | 0.0404 | 0.0099 | 0.0305 | False | 2026-11-24T02:59:57Z |
