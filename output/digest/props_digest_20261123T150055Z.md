# Props Pipeline Digest -- 2026-11-23T15:00:55Z

## Run summary
- DraftKings ingestion: 513 rows across 8 events (OK)
- FanDuel ingestion: 0 rows (OK)
- BetMGM ingestion (via Rotowire): 86 rows (OK)
- Estimation: 599 rows written (from 599 ingested rows) -- status breakdown: {'estimated': 326, 'unsupported_market_first_scorer': 175, 'no_player_match': 59, 'unsupported_stat_type': 26, 'insufficient_history': 13}
- CLV logging: 55 newly flagged, 0 newly closed, 55 still open (1749 total ever logged)

## Currently open flags
Sizing is a manual step (`sizing_engine.py props size`, Session 6.4) -- this table is what to scan to pick a flag worth sizing. `implied_prob_includes_field_vig` matters here more than for the other tracks: a row still reporting True carries a real, separate uncertainty (Session 6.4's `PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER` dampener) that a bigger raw edge number does not describe.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_model_prob | first_flagged_market_price | first_flagged_edge | implied_prob_includes_field_vig | first_flagged_at |
|---|---|---|---|---|---|---|---|---|---|
| draftkings|389828085|0QA389828085#2368213505_13L88808Q1-115201972Q20 | draftkings | Van Jefferson | Anytime TD Scorer | over | 0.4182 | 0.1111 | 0.3071 | False | 2026-11-23T15:01:11Z |
| draftkings|391617129|0QA391617129#2376389698_13L88808Q1-822030320Q20 | draftkings | Davis Allen | Anytime TD Scorer | over | 0.4182 | 0.1176 | 0.3006 | False | 2026-11-23T15:01:11Z |
| draftkings|389828085|0QA389828085#2368214033_13L88808Q1-409986828Q20 | draftkings | Drew Sample | Anytime TD Scorer | over | 0.3935 | 0.1538 | 0.2396 | False | 2026-11-23T15:01:11Z |
| draftkings|391879785|0QA391879785#2377763120_13L88808Q1917552914Q20 | draftkings | Kenneth Walker III | 2+ TDs | over | 0.4125 | 0.1818 | 0.2307 | False | 2026-11-23T15:01:11Z |
| draftkings|391839147|0QA391839147#2377480792_13L88808Q11402568200Q20 | draftkings | Pat Freiermuth | Anytime TD Scorer | over | 0.4084 | 0.1818 | 0.2266 | False | 2026-11-23T15:01:11Z |
| draftkings|391984111|0QA391984111#2378253787_13L88808Q1872485381Q20 | draftkings | Jonah Coleman | 2+ TDs | over | 0.3696 | 0.1538 | 0.2158 | False | 2026-11-23T15:01:11Z |
| draftkings|391839147|0QA391839147#2377480810_13L88808Q1-577361648Q20 | draftkings | Nate Adkins | Anytime TD Scorer | over | 0.2983 | 0.0833 | 0.215 | False | 2026-11-23T15:01:11Z |
| draftkings|391833992|0QA391833992#2377459269_13L88808Q1-511040682Q20 | draftkings | Travis Kelce | Anytime TD Scorer | over | 0.5034 | 0.303 | 0.2004 | False | 2026-11-23T15:01:11Z |
| draftkings|391839147|0QA391839147#2377480811_13L88808Q1-1398413387Q20 | draftkings | Adam Trautman | Anytime TD Scorer | over | 0.2277 | 0.0476 | 0.18 | False | 2026-11-23T15:01:11Z |
| draftkings|389828085|0QA389828085#2368213439_13L88808Q11678347508Q20 | draftkings | Ben Sinnott | Anytime TD Scorer | over | 0.2704 | 0.1053 | 0.1651 | False | 2026-11-23T15:01:11Z |
| draftkings|391617129|0QA391617129#2376389716_13L88808Q1957158759Q20 | draftkings | J. Michael Sturdivant | Anytime TD Scorer | over | 0.2059 | 0.0435 | 0.1624 | False | 2026-11-23T15:01:11Z |
| draftkings|391876015|0QA391876015#2377741453_13L88808Q1-1008695778Q20 | draftkings | D'Andre Swift | 2+ TDs | over | 0.3247 | 0.1667 | 0.158 | False | 2026-11-23T15:01:11Z |
| draftkings|391617129|0QA391617129#2376389715_13L88808Q1-1213243313Q20 | draftkings | Jordan Love | Anytime TD Scorer | over | 0.2328 | 0.0769 | 0.1559 | False | 2026-11-23T15:01:11Z |
| draftkings|389828085|0QA389828085#2368213284_13L88808Q1622596392Q20 | draftkings | Stefon Diggs | Anytime TD Scorer | over | 0.5084 | 0.3571 | 0.1512 | False | 2026-11-23T15:01:11Z |
| draftkings|391845390|0QA391845390#2377517123_13L88808Q1795642865Q20 | draftkings | Dak Prescott | Anytime TD Scorer | over | 0.2781 | 0.1333 | 0.1448 | False | 2026-11-23T15:01:11Z |
| draftkings|391617129|0QA391617129#2376389703_13L88808Q1-1604380439Q20 | draftkings | Xavier Smith | Anytime TD Scorer | over | 0.2704 | 0.1333 | 0.137 | False | 2026-11-23T15:01:11Z |
| draftkings|389828085|0QA389828085#2368214016_13L88808Q1219777051Q20 | draftkings | Joe Burrow | Anytime TD Scorer | over | 0.3241 | 0.1905 | 0.1336 | False | 2026-11-23T15:01:11Z |
| draftkings|391833992|0QA391833992#2377459594_13L88808Q1-985183007Q20 | draftkings | Andrew Armstrong | Anytime TD Scorer | over | 0.1881 | 0.0556 | 0.1325 | False | 2026-11-23T15:01:11Z |
| draftkings|391842938|0QA391842938#2377503377_13L88808Q1480222870Q20 | draftkings | Jameson Williams | Anytime TD Scorer | over | 0.4594 | 0.3279 | 0.1315 | False | 2026-11-23T15:01:11Z |
| draftkings|391845390|0QA391845390#2377517158_13L88808Q1744413187Q20 | draftkings | KaVontae Turpin | Anytime TD Scorer | over | 0.2592 | 0.1333 | 0.1258 | False | 2026-11-23T15:01:11Z |
| draftkings|391839147|0QA391839147#2377480789_13L88808Q11665380004Q20 | draftkings | Roman Wilson | Anytime TD Scorer | over | 0.2787 | 0.1538 | 0.1248 | False | 2026-11-23T15:01:11Z |
| draftkings|391845390|0QA391845390#2377517154_13L88808Q1-1127265655Q20 | draftkings | George Pickens | Anytime TD Scorer | over | 0.5975 | 0.4762 | 0.1213 | False | 2026-11-23T15:01:11Z |
| draftkings|389828085|0QA389828085#2368213928_13L88808Q11452425719Q20 | draftkings | Jack Endries | Anytime TD Scorer | over | 0.253 | 0.1333 | 0.1196 | False | 2026-11-23T15:01:11Z |
| draftkings|391879785|0QA391879785#2377763110_13L88808Q1503159412Q20 | draftkings | James Cook | 2+ TDs | over | 0.2642 | 0.1538 | 0.1104 | False | 2026-11-23T15:01:11Z |
| draftkings|391879785|0QA391879785#2377763122_13L88808Q1321951862Q20 | draftkings | Travis Kelce | 2+ TDs | over | 0.1558 | 0.0476 | 0.1082 | False | 2026-11-23T15:01:11Z |
| draftkings|391877054|0QA391877054#2377747270_13L88808Q11452024780Q20 | draftkings | George Pickens | 2+ TDs | over | 0.2312 | 0.125 | 0.1062 | False | 2026-11-23T15:01:11Z |
| draftkings|391839147|0QA391839147#2377480806_13L88808Q164075827Q20 | draftkings | Pat Bryant | Anytime TD Scorer | over | 0.2965 | 0.1905 | 0.106 | False | 2026-11-23T15:01:11Z |
| draftkings|391839147|0QA391839147#2377480796_13L88808Q1292660006Q20 | draftkings | Ben Skowronek | Anytime TD Scorer | over | 0.1479 | 0.0435 | 0.1044 | False | 2026-11-23T15:01:11Z |
| draftkings|389828891|0QA389828891#2368214961_13L88808Q11585686638Q20 | draftkings | Van Jefferson | 2+ TDs | over | 0.1031 | 0.0099 | 0.0932 | False | 2026-11-23T15:01:11Z |
| draftkings|391891812|0QA391891812#2377834481_13L88808Q1-1802470485Q20 | draftkings | Davis Allen | 2+ TDs | over | 0.1031 | 0.0099 | 0.0932 | False | 2026-11-23T15:01:11Z |
| draftkings|389828891|0QA389828891#2368214957_13L88808Q1-60147958Q20 | draftkings | Stefon Diggs | 2+ TDs | over | 0.1593 | 0.0667 | 0.0926 | False | 2026-11-23T15:01:11Z |
| draftkings|391839147|0QA391839147#2377480804_13L88808Q11696076099Q20 | draftkings | J.K. Dobbins | Anytime TD Scorer | over | 0.2212 | 0.1333 | 0.0879 | False | 2026-11-23T15:01:11Z |
| draftkings|389828085|0QA389828085#2368213822_13L88808Q1-1846552455Q20 | draftkings | Mike Gesicki | Anytime TD Scorer | over | 0.4373 | 0.3509 | 0.0864 | False | 2026-11-23T15:01:11Z |
| draftkings|391876015|0QA391876015#2377741443_13L88808Q11455054237Q20 | draftkings | Jahmyr Gibbs | 2+ TDs | over | 0.4455 | 0.3636 | 0.0819 | False | 2026-11-23T15:01:11Z |
| draftkings|391984111|0QA391984111#2378253776_13L88808Q1-162258478Q20 | draftkings | Pat Freiermuth | 2+ TDs | over | 0.0979 | 0.0196 | 0.0783 | False | 2026-11-23T15:01:11Z |
| draftkings|391833992|0QA391833992#2377459096_13L88808Q11235745545Q20 | draftkings | Keleki Latu | Anytime TD Scorer | over | 0.1441 | 0.0667 | 0.0774 | False | 2026-11-23T15:01:11Z |
| draftkings|389828891|0QA389828891#2368214975_13L88808Q1992963390Q20 | draftkings | Drew Sample | 2+ TDs | over | 0.0902 | 0.0152 | 0.0751 | False | 2026-11-23T15:01:11Z |
| draftkings|391617129|0QA391617129#2376389706_13L88808Q11480921309Q20 | draftkings | Matthew Golden | Anytime TD Scorer | over | 0.4025 | 0.3279 | 0.0746 | False | 2026-11-23T15:01:11Z |
| draftkings|391876015|0QA391876015#2377741446_13L88808Q1-106544391Q20 | draftkings | Jameson Williams | 2+ TDs | over | 0.1269 | 0.0556 | 0.0713 | False | 2026-11-23T15:01:11Z |
| draftkings|389828891|0QA389828891#2368214967_13L88808Q1-1865349726Q20 | draftkings | Tee Higgins | 2+ TDs | over | 0.2069 | 0.1429 | 0.064 | False | 2026-11-23T15:01:11Z |
| draftkings|389828891|0QA389828891#2368214968_13L88808Q1-1016060448Q20 | draftkings | Mike Gesicki | 2+ TDs | over | 0.1137 | 0.0625 | 0.0512 | False | 2026-11-23T15:01:11Z |
| draftkings|391833992|0QA391833992#2377459341_13L88808Q1439564023Q20 | draftkings | Xavier Worthy | Anytime TD Scorer | over | 0.2404 | 0.1905 | 0.05 | False | 2026-11-23T15:01:11Z |
| draftkings|391879785|0QA391879785#2377763111_13L88808Q11587218485Q20 | draftkings | Josh Allen | 2+ TDs | over | 0.2129 | 0.1667 | 0.0463 | False | 2026-11-23T15:01:11Z |
| draftkings|391833992|0QA391833992#2377459394_13L88808Q1-1195662886Q20 | draftkings | Cyrus Allen | Anytime TD Scorer | over | 0.171 | 0.125 | 0.046 | False | 2026-11-23T15:01:11Z |
| draftkings|391842938|0QA391842938#2377503391_13L88808Q1655740791Q20 | draftkings | Kyle Monangai | Anytime TD Scorer | over | 0.4457 | 0.4 | 0.0457 | False | 2026-11-23T15:01:11Z |
| draftkings|391877054|0QA391877054#2377747268_13L88808Q12056061885Q20 | draftkings | Javonte Williams | 2+ TDs | over | 0.2773 | 0.2326 | 0.0447 | False | 2026-11-23T15:01:11Z |
| draftkings|391984111|0QA391984111#2378253795_13L88808Q1-1564766902Q20 | draftkings | Nate Adkins | 2+ TDs | over | 0.0497 | 0.0066 | 0.0431 | False | 2026-11-23T15:01:11Z |
| draftkings|391891812|0QA391891812#2377834488_13L88808Q1905210328Q20 | draftkings | Matthew Golden | 2+ TDs | over | 0.0948 | 0.0526 | 0.0422 | False | 2026-11-23T15:01:11Z |
| draftkings|391877054|0QA391877054#2377747269_13L88808Q1-1472312629Q20 | draftkings | CeeDee Lamb | 2+ TDs | over | 0.2235 | 0.1818 | 0.0417 | False | 2026-11-23T15:01:11Z |
| draftkings|389828891|0QA389828891#2368214973_13L88808Q1158576549Q20 | draftkings | Joe Burrow | 2+ TDs | over | 0.0593 | 0.0217 | 0.0376 | False | 2026-11-23T15:01:11Z |
| draftkings|391617129|0QA391617129#2376389707_13L88808Q1-135035926Q20 | draftkings | MarShawn Lloyd | Anytime TD Scorer | over | 0.2186 | 0.1818 | 0.0368 | False | 2026-11-23T15:01:11Z |
| draftkings|391876015|0QA391876015#2377741455_13L88808Q1902102257Q20 | draftkings | Kyle Monangai | 2+ TDs | over | 0.1186 | 0.0833 | 0.0353 | False | 2026-11-23T15:01:11Z |
| draftkings|391617129|0QA391617129#2376389709_13L88808Q11154264979Q20 | draftkings | Savion Williams | Anytime TD Scorer | over | 0.2015 | 0.1667 | 0.0348 | False | 2026-11-23T15:01:11Z |
| draftkings|391877054|0QA391877054#2377747405_13L88808Q113349962Q20 | draftkings | Saquon Barkley | 2+ TDs | over | 0.1593 | 0.125 | 0.0343 | False | 2026-11-23T15:01:11Z |
| draftkings|391984111|0QA391984111#2378253777_13L88808Q1-773934870Q20 | draftkings | Roman Wilson | 2+ TDs | over | 0.043 | 0.0123 | 0.0307 | False | 2026-11-23T15:01:11Z |
