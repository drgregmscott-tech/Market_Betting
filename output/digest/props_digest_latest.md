# Props Pipeline Digest -- 2026-09-09T18:54:42Z

## Run summary
- DraftKings ingestion: 674 rows across 8 events (OK)
- FanDuel ingestion: 141 rows (OK)
- Estimation: 815 rows written (from 815 ingested rows) -- status breakdown: {'estimated': 397, 'no_player_match': 191, 'unsupported_market_first_scorer': 164, 'season_complete_no_remaining_games': 63}
- CLV logging: 1 newly flagged, 0 newly closed, 229 still open (229 total ever logged)

## Currently open flags
Sizing is a manual step (`sizing_engine.py props size`, Session 6.4) -- this table is what to scan to pick a flag worth sizing. `implied_prob_includes_field_vig` matters here more than for the other tracks: a row still reporting True carries a real, separate uncertainty (Session 6.4's `PROPS_FIELD_VIG_UNRESOLVED_MULTIPLIER` dampener) that a bigger raw edge number does not describe.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_model_prob | first_flagged_market_price | first_flagged_edge | implied_prob_includes_field_vig | first_flagged_at |
|---|---|---|---|---|---|---|---|---|---|
| draftkings|0QA334323199#2150675737_13L88808Q1-1571700727Q20 | draftkings | Matthew Stafford | Anytime TD Scorer | over | 0.9417 | 0.0476 | 0.8941 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA361399049#2250882595_13L88808Q1219777051Q20 | draftkings | Joe Burrow | Anytime TD Scorer | over | 0.9091 | 0.1176 | 0.7914 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA334323199#2150675797_13L88808Q1579133715Q20 | draftkings | Brock Purdy | Anytime TD Scorer | over | 0.9302 | 0.1429 | 0.7874 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA361397313#2250875292_13L88808Q1-1939996255Q20 | draftkings | Jared Goff | Anytime TD Scorer | over | 0.838 | 0.0625 | 0.7755 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA334323197#2150675645_13L88808Q1878830924Q20 | draftkings | Matthew Stafford | 2+ TDs | over | 0.7761 | 0.0055 | 0.7706 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA334323197#2150675739_13L88808Q11557081727Q20 | draftkings | Brock Purdy | 2+ TDs | over | 0.7445 | 0.0132 | 0.7313 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA363196021#2258143631_13L88808Q1274701345Q20 | draftkings | Trevor Lawrence | 2+ TDs | over | 0.7572 | 0.0476 | 0.7096 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA334613199#2151928226_13L88808Q1-725127430Q20 | draftkings | Drake Maye | Anytime TD Scorer | over | 0.8924 | 0.1905 | 0.7019 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA362350810#2254581531_13L88808Q1242387080Q20 | draftkings | C.J. Stroud | Anytime TD Scorer | over | 0.8049 | 0.1053 | 0.6996 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA362104903#2253619465_13L88808Q11112660000Q20 | draftkings | Bryce Young | Anytime TD Scorer | over | 0.8053 | 0.1176 | 0.6876 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA363175928#2258086117_13L88808Q1158576549Q20 | draftkings | Joe Burrow | 2+ TDs | over | 0.691 | 0.011 | 0.68 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA362104903#2253619480_13L88808Q11505799344Q20 | draftkings | Caleb Williams | Anytime TD Scorer | over | 0.8522 | 0.2 | 0.6522 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA362382884#2254729903_13L88808Q1-1192653454Q20 | draftkings | Trevor Lawrence | Anytime TD Scorer | over | 0.935 | 0.2941 | 0.6408 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA334612412#2151925331_13L88808Q11724982079Q20 | draftkings | Drake Maye | 2+ TDs | over | 0.6525 | 0.0196 | 0.6329 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA361399049#2250882694_13L88808Q1-1664922884Q20 | draftkings | Baker Mayfield | Anytime TD Scorer | over | 0.7722 | 0.1538 | 0.6183 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA361505183#2251317180_13L88808Q1-1969802282Q20 | draftkings | Daniel Jones | Anytime TD Scorer | over | 0.7798 | 0.1667 | 0.6131 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA334613199#2151928218_13L88808Q11771646792Q20 | draftkings | Sam Darnold | Anytime TD Scorer | over | 0.6928 | 0.0952 | 0.5976 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA361397313#2250875356_13L88808Q144959304Q20 | draftkings | Tyler Shough | Anytime TD Scorer | over | 0.7609 | 0.2083 | 0.5526 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA363171670#2258072381_13L88808Q1-77651570Q20 | draftkings | Caleb Williams | 2+ TDs | over | 0.5696 | 0.0217 | 0.5478 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA363177179#2258089983_13L88808Q1398394097Q20 | draftkings | Jared Goff | 2+ TDs | over | 0.5431 | 0.0055 | 0.5376 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA361505183#2251317256_13L88808Q1-1643070992Q20 | draftkings | Lamar Jackson | Anytime TD Scorer | over | 0.8226 | 0.2857 | 0.5369 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA363186669#2258117165_13L88808Q11587218485Q20 | draftkings | Josh Allen | 2+ TDs | over | 0.6427 | 0.1111 | 0.5316 | True | 2026-09-09T17:34:29Z |
| fanduel|98506671 | fanduel | Bryce Young | Passing TDs | over | 0.9997 | 0.4858 | 0.5139 | False | 2026-09-09T17:34:29Z |
| fanduel|98496714 | fanduel | Brock Purdy | Passing TDs | over | 0.9916 | 0.4858 | 0.5058 | False | 2026-09-09T17:34:29Z |
| fanduel|99965603 | fanduel | De'Von Achane | Rushing Yards | over | 1.0 | 0.5 | 0.5 | False | 2026-09-09T17:34:29Z |
| fanduel|98241183 | fanduel | Josh Allen | Rushing Yards | over | 1.0 | 0.5 | 0.5 | False | 2026-09-09T17:34:29Z |
| fanduel|100252251 | fanduel | Javonte Williams | Rushing Yards | over | 1.0 | 0.5 | 0.5 | False | 2026-09-09T17:34:29Z |
| fanduel|102441629 | fanduel | Davante Adams | Receiving Yards | over | 1.0 | 0.5 | 0.5 | False | 2026-09-09T17:34:29Z |
| fanduel|100630901 | fanduel | George Kittle | Receiving Yards | over | 1.0 | 0.5 | 0.5 | False | 2026-09-09T17:34:29Z |
| fanduel|98240844 | fanduel | Justin Herbert | Passing Yards | over | 1.0 | 0.5 | 0.5 | False | 2026-09-09T17:34:29Z |
| fanduel|99153350 | fanduel | D'Andre Swift | Rushing Yards | over | 1.0 | 0.5 | 0.5 | False | 2026-09-09T17:34:29Z |
| fanduel|100993965 | fanduel | Jaylen Warren | Rushing Yards | over | 1.0 | 0.5 | 0.5 | False | 2026-09-09T17:34:29Z |
| fanduel|99171620 | fanduel | Breece Hall | Rushing Yards | over | 1.0 | 0.5 | 0.5 | False | 2026-09-09T17:34:29Z |
| fanduel|99952803 | fanduel | Aaron Rodgers | Passing Yards | over | 1.0 | 0.5 | 0.5 | False | 2026-09-09T17:34:29Z |
| fanduel|99983944 | fanduel | Saquon Barkley | Rushing Yards | over | 1.0 | 0.5 | 0.5 | False | 2026-09-09T17:34:29Z |
| fanduel|98467741 | fanduel | Chris Olave | Receiving Yards | over | 1.0 | 0.5 | 0.5 | False | 2026-09-09T17:34:29Z |
| fanduel|99811594 | fanduel | J.K. Dobbins | Rushing Yards | over | 1.0 | 0.5 | 0.5 | False | 2026-09-09T17:34:29Z |
| fanduel|102441625 | fanduel | Puka Nacua | Receiving Yards | over | 1.0 | 0.5 | 0.5 | False | 2026-09-09T17:34:29Z |
| fanduel|99787478 | fanduel | Sam LaPorta | Receiving Yards | over | 0.9999 | 0.5 | 0.4999 | False | 2026-09-09T17:34:29Z |
| fanduel|100252260 | fanduel | Josh Allen | Passing Yards | over | 0.9999 | 0.5 | 0.4999 | False | 2026-09-09T17:34:29Z |
| fanduel|99983884 | fanduel | Ja'Marr Chase | Receiving Yards | over | 0.9999 | 0.5 | 0.4999 | False | 2026-09-09T17:34:29Z |
| fanduel|98948331 | fanduel | Jalen Hurts | Passing Yards | over | 0.9998 | 0.5 | 0.4998 | False | 2026-09-09T17:34:29Z |
| fanduel|102392662 | fanduel | Daniel Jones | Passing Yards | over | 0.9998 | 0.5 | 0.4998 | False | 2026-09-09T17:34:29Z |
| fanduel|100970787 | fanduel | Lamar Jackson | Rushing Yards | under | 0.9997 | 0.5 | 0.4997 | False | 2026-09-09T17:34:29Z |
| fanduel|101468537 | fanduel | Bryce Young | Passing Yards | over | 0.9996 | 0.5 | 0.4996 | False | 2026-09-09T17:34:29Z |
| fanduel|102304878 | fanduel | Christian Watson | Receiving Yards | over | 0.9993 | 0.5 | 0.4993 | False | 2026-09-09T17:34:29Z |
| fanduel|98948526 | fanduel | Jayden Daniels | Passing Yards | under | 0.9988 | 0.5 | 0.4988 | False | 2026-09-09T17:34:29Z |
| fanduel|101808022 | fanduel | Tyler Shough | Passing Yards | over | 0.9973 | 0.5 | 0.4973 | False | 2026-09-09T17:34:29Z |
| fanduel|102600784 | fanduel | Rhamondre Stevenson | Rushing Yards | over | 0.997 | 0.5 | 0.497 | False | 2026-09-09T17:34:29Z |
| fanduel|100731539 | fanduel | Ladd McConkey | Receiving Yards | under | 0.9961 | 0.5 | 0.4961 | False | 2026-09-09T17:34:29Z |
| fanduel|100958530 | fanduel | Jaxson Dart | Rushing Yards | over | 0.9956 | 0.5 | 0.4956 | False | 2026-09-09T17:34:29Z |
| fanduel|98497164 | fanduel | Justin Herbert | Passing TDs | over | 0.9807 | 0.4858 | 0.4948 | False | 2026-09-09T17:34:29Z |
| fanduel|102052697 | fanduel | Nico Collins | Receiving Yards | over | 0.9942 | 0.5 | 0.4942 | False | 2026-09-09T17:34:29Z |
| fanduel|100454290 | fanduel | Jaxson Dart | Rushing TDs | over | 0.9999 | 0.5061 | 0.4939 | False | 2026-09-09T17:34:29Z |
| fanduel|100215516 | fanduel | Jalen Hurts | Passing TDs | over | 1.0 | 0.5142 | 0.4858 | False | 2026-09-09T17:34:29Z |
| fanduel|98467989 | fanduel | Garrett Wilson | Receiving Yards | under | 0.98 | 0.5 | 0.48 | False | 2026-09-09T17:34:29Z |
| draftkings|0QA363171670#2258072365_13L88808Q1-2021448682Q20 | draftkings | Bryce Young | 2+ TDs | over | 0.4867 | 0.0099 | 0.4768 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA363186669#2258117155_13L88808Q1389233581Q20 | draftkings | C.J. Stroud | 2+ TDs | over | 0.4861 | 0.0099 | 0.4762 | True | 2026-09-09T17:34:29Z |
| fanduel|99006745 | fanduel | Josh Allen | Rushing TDs | over | 1.0 | 0.5241 | 0.4759 | False | 2026-09-09T17:34:29Z |
| fanduel|99006750 | fanduel | Javonte Williams | Rushing TDs | over | 0.999 | 0.5241 | 0.4749 | False | 2026-09-09T17:34:29Z |
| fanduel|98496370 | fanduel | Joe Burrow | Passing TDs | over | 0.9744 | 0.5 | 0.4744 | False | 2026-09-09T17:34:29Z |
| draftkings|0QA363187905#2258120976_13L88808Q1-1605206671Q20 | draftkings | Lamar Jackson | 2+ TDs | over | 0.5159 | 0.0476 | 0.4683 | True | 2026-09-09T17:34:29Z |
| fanduel|97984775 | fanduel | Jaxson Dart | Passing Yards | under | 0.9647 | 0.5 | 0.4647 | False | 2026-09-09T17:34:29Z |
| fanduel|101396948 | fanduel | Daniel Jones | Passing TDs | over | 0.9992 | 0.5379 | 0.4613 | False | 2026-09-09T17:34:29Z |
| fanduel|99007129 | fanduel | Rhamondre Stevenson | Rushing TDs | over | 0.9999 | 0.5419 | 0.458 | False | 2026-09-09T17:34:29Z |
| fanduel|99787247 | fanduel | Terry McLaurin | Receiving Yards | over | 0.9577 | 0.5 | 0.4577 | False | 2026-09-09T17:34:29Z |
| fanduel|102089548 | fanduel | Tee Higgins | Receiving Yards | over | 0.9545 | 0.5 | 0.4545 | False | 2026-09-09T17:34:29Z |
| fanduel|101185683 | fanduel | Jayden Daniels | Passing TDs | under | 0.9821 | 0.5282 | 0.454 | False | 2026-09-09T17:34:29Z |
| fanduel|98996829 | fanduel | Tyler Shough | Passing TDs | under | 0.8884 | 0.4415 | 0.4469 | False | 2026-09-09T17:34:29Z |
| fanduel|102401539 | fanduel | C.J. Stroud | Passing Yards | over | 0.9451 | 0.5 | 0.4451 | False | 2026-09-09T17:34:29Z |
| draftkings|0QA362350810#2254581562_13L88808Q1-677035407Q20 | draftkings | Josh Allen | Anytime TD Scorer | over | 0.8879 | 0.4444 | 0.4435 | True | 2026-09-09T17:34:29Z |
| fanduel|99007823 | fanduel | Lamar Jackson | Rushing TDs | under | 0.9128 | 0.4718 | 0.4409 | False | 2026-09-09T17:34:29Z |
| fanduel|98948304 | fanduel | Brock Purdy | Passing Yards | over | 0.9324 | 0.5 | 0.4324 | False | 2026-09-09T17:34:29Z |
| draftkings|0QA363187905#2258120966_13L88808Q1-1687698446Q20 | draftkings | Daniel Jones | 2+ TDs | over | 0.4465 | 0.0164 | 0.4301 | True | 2026-09-09T17:34:29Z |
| fanduel|99007008 | fanduel | D'Andre Swift | Rushing TDs | over | 1.0 | 0.5717 | 0.4283 | False | 2026-09-09T17:34:29Z |
| draftkings|0QA363175928#2258086128_13L88808Q12009212996Q20 | draftkings | Baker Mayfield | 2+ TDs | over | 0.4352 | 0.0152 | 0.42 | True | 2026-09-09T17:34:29Z |
| fanduel|101978806 | fanduel | Quinshon Judkins | Rushing Yards | over | 0.9192 | 0.5 | 0.4192 | False | 2026-09-09T17:34:29Z |
| fanduel|99007763 | fanduel | Breece Hall | Rushing TDs | under | 0.9681 | 0.567 | 0.4011 | False | 2026-09-09T17:34:29Z |
| fanduel|98497218 | fanduel | Josh Allen | Passing TDs | over | 0.9092 | 0.5101 | 0.3991 | False | 2026-09-09T17:34:29Z |
| fanduel|102089043 | fanduel | Colston Loveland | Receiving Yards | under | 0.8966 | 0.5 | 0.3966 | False | 2026-09-09T17:34:29Z |
| draftkings|0QA363177179#2258089993_13L88808Q1-1801413616Q20 | draftkings | Tyler Shough | 2+ TDs | over | 0.4188 | 0.0244 | 0.3944 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA334613199#2233956178_13L88808Q1-2108815135Q20 | draftkings | Tory Horton | Anytime TD Scorer | over | 0.5145 | 0.125 | 0.3895 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA362382884#2254729946_13L88808Q11230695518Q20 | draftkings | Bhayshul Tuten | Anytime TD Scorer | over | 0.4475 | 0.089 | 0.3585 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA334323199#2150675668_13L88808Q1691932532Q20 | draftkings | Colby Parkinson | Anytime TD Scorer | over | 0.5487 | 0.2 | 0.3487 | True | 2026-09-09T17:34:29Z |
| fanduel|98467861 | fanduel | Drake London | Receiving Yards | over | 0.8379 | 0.5 | 0.3379 | False | 2026-09-09T17:34:29Z |
| draftkings|0QA334612412#2151924870_13L88808Q11096856495Q20 | draftkings | Sam Darnold | 2+ TDs | over | 0.3302 | 0.0076 | 0.3226 | True | 2026-09-09T17:34:29Z |
| fanduel|98228114 | fanduel | Jalen Hurts | Rushing Yards | over | 0.8195 | 0.5 | 0.3195 | False | 2026-09-09T17:34:29Z |
| fanduel|99983892 | fanduel | CeeDee Lamb | Receiving Yards | over | 0.81 | 0.5 | 0.31 | False | 2026-09-09T17:34:29Z |
| fanduel|98497244 | fanduel | Lamar Jackson | Passing TDs | over | 0.8226 | 0.5142 | 0.3084 | False | 2026-09-09T17:34:29Z |
| fanduel|99171616 | fanduel | Lamar Jackson | Passing Yards | over | 0.8061 | 0.5 | 0.3061 | False | 2026-09-09T17:34:29Z |
| draftkings|0QA334613199#2151928211_13L88808Q11896367839Q20 | draftkings | Jaxon Smith-Njigba | Anytime TD Scorer | over | 0.3776 | 0.0803 | 0.2973 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA362350810#2254581570_13L88808Q11362443903Q20 | draftkings | Ty Johnson | Anytime TD Scorer | over | 0.4496 | 0.1538 | 0.2957 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA362382884#2254729962_13L88808Q1466829631Q20 | draftkings | Harold Fannin Jr. | Anytime TD Scorer | over | 0.5247 | 0.2381 | 0.2866 | True | 2026-09-09T17:34:29Z |
| fanduel|98498215 | fanduel | Jaxson Dart | Passing TDs | under | 0.7978 | 0.5142 | 0.2836 | False | 2026-09-09T17:34:29Z |
| draftkings|0QA362350810#2254581548_13L88808Q11759839095Q20 | draftkings | Nico Collins | Anytime TD Scorer | over | 0.3771 | 0.0944 | 0.2826 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA362382884#2254729951_13L88808Q1-849064763Q20 | draftkings | Parker Washington | Anytime TD Scorer | over | 0.3503 | 0.0722 | 0.2781 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA361505183#2251321881_13L88808Q1-1866642147Q20 | draftkings | Alec Pierce | Anytime TD Scorer | over | 0.5276 | 0.25 | 0.2776 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA362104903#2253619481_13L88808Q1-1770507643Q20 | draftkings | Jahdae Walker | Anytime TD Scorer | over | 0.357 | 0.0833 | 0.2737 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA334613199#2169981631_13L88808Q11457589561Q20 | draftkings | A.J. Brown | Anytime TD Scorer | over | 0.3386 | 0.0727 | 0.2659 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA334323199#2150675755_13L88808Q11665839176Q20 | draftkings | Mike Evans | Anytime TD Scorer | over | 0.338 | 0.0778 | 0.2602 | False | 2026-09-09T17:54:53Z |
| fanduel|98468425 | fanduel | Marvin Harrison Jr. | Receiving Yards | under | 0.7554 | 0.5 | 0.2554 | False | 2026-09-09T17:34:29Z |
| draftkings|0QA334323199#2150675640_13L88808Q11373713880Q20 | draftkings | Blake Corum | Anytime TD Scorer | over | 0.3406 | 0.0868 | 0.2538 | False | 2026-09-09T17:54:53Z |
| fanduel|100861633 | fanduel | Brock Bowers | Receiving Yards | under | 0.7533 | 0.5 | 0.2533 | False | 2026-09-09T17:34:29Z |
| draftkings|0QA361397313#2250875331_13L88808Q1472584472Q20 | draftkings | Sam LaPorta | Anytime TD Scorer | over | 0.3241 | 0.0833 | 0.2408 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA361397313#2250875329_13L88808Q1-1466210203Q20 | draftkings | Amon-Ra St. Brown | Anytime TD Scorer | over | 0.3582 | 0.1187 | 0.2395 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA334323199#2150675820_13L88808Q11147507867Q20 | draftkings | Jake Tonges | Anytime TD Scorer | over | 0.3843 | 0.1538 | 0.2305 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA362104903#2253619464_13L88808Q1294436062Q20 | draftkings | Darren Waller | Anytime TD Scorer | over | 0.4134 | 0.1905 | 0.2229 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA362104903#2253619460_13L88808Q1-719490824Q20 | draftkings | Tetairoa McMillan | Anytime TD Scorer | over | 0.2924 | 0.0767 | 0.2157 | False | 2026-09-09T17:54:53Z |
| fanduel|102245252 | fanduel | A.J. Brown | Receiving Yards | over | 0.7123 | 0.5 | 0.2123 | False | 2026-09-09T17:34:29Z |
| draftkings|0QA334612412#2151925101_13L88808Q1-1063669179Q20 | draftkings | Rhamondre Stevenson | 2+ TDs | over | 0.3361 | 0.125 | 0.2111 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA334613199#2151928221_13L88808Q1-1828996474Q20 | draftkings | Rhamondre Stevenson | Anytime TD Scorer | over | 0.6977 | 0.4878 | 0.2099 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA362350810#2254581569_13L88808Q11470829306Q20 | draftkings | Dawson Knox | Anytime TD Scorer | over | 0.343 | 0.1333 | 0.2096 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA361505183#2251317263_13L88808Q1-1199795272Q20 | draftkings | Devontez Walker | Anytime TD Scorer | over | 0.3041 | 0.0952 | 0.2088 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA361397313#2250875335_13L88808Q11283746776Q20 | draftkings | Isaac TeSlaa | Anytime TD Scorer | over | 0.3808 | 0.1739 | 0.2069 | True | 2026-09-09T17:34:29Z |
| fanduel|100861626 | fanduel | Jaylen Waddle | Receiving Yards | over | 0.7023 | 0.5 | 0.2023 | False | 2026-09-09T17:34:29Z |
| draftkings|0QA362382884#2254729961_13L88808Q1-1895349765Q20 | draftkings | Quinshon Judkins | Anytime TD Scorer | over | 0.2811 | 0.079 | 0.2021 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA362104903#2253619477_13L88808Q1-848465730Q20 | draftkings | Rome Odunze | Anytime TD Scorer | over | 0.2666 | 0.0645 | 0.202 | False | 2026-09-09T17:54:53Z |
| fanduel|99006927 | fanduel | Jalen Hurts | Rushing TDs | over | 0.7532 | 0.5585 | 0.1947 | False | 2026-09-09T17:34:29Z |
| draftkings|0QA361399049#2250882690_13L88808Q1532397873Q20 | draftkings | Chris Godwin | Anytime TD Scorer | over | 0.2563 | 0.0624 | 0.1939 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA362350810#2258204273_13L88808Q1401138925Q20 | draftkings | Kayshon Boutte | Anytime TD Scorer | over | 0.2399 | 0.0522 | 0.1876 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA361505183#2251317257_13L88808Q12018204784Q20 | draftkings | Zay Flowers | Anytime TD Scorer | over | 0.5558 | 0.3704 | 0.1854 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA362350810#2254581567_13L88808Q1-81077793Q20 | draftkings | Dalton Kincaid | Anytime TD Scorer | over | 0.2353 | 0.0571 | 0.1782 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA334323199#2150675659_13L88808Q1-1261907500Q20 | draftkings | Puka Nacua | Anytime TD Scorer | over | 0.603 | 0.4255 | 0.1774 | True | 2026-09-09T17:34:29Z |
| fanduel|98497299 | fanduel | C.J. Stroud | Passing TDs | over | 0.6868 | 0.5142 | 0.1726 | False | 2026-09-09T17:34:29Z |
| draftkings|0QA334323197#2150675597_13L88808Q11942991799Q20 | draftkings | Colby Parkinson | 2+ TDs | over | 0.1897 | 0.0217 | 0.1679 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA334323199#2150675679_13L88808Q1244078380Q20 | draftkings | Tyler Higbee | Anytime TD Scorer | over | 0.3195 | 0.1538 | 0.1657 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA362382884#2254729955_13L88808Q1-1307850565Q20 | draftkings | Quintin Morris | Anytime TD Scorer | over | 0.1978 | 0.0323 | 0.1656 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA361397313#2250875349_13L88808Q1-1726186093Q20 | draftkings | Chris Olave | Anytime TD Scorer | over | 0.571 | 0.4082 | 0.1628 | True | 2026-09-09T17:34:29Z |
| fanduel|102300985 | fanduel | Jordan Love | Passing TDs | under | 0.6759 | 0.5142 | 0.1617 | False | 2026-09-09T17:34:29Z |
| fanduel|102301001 | fanduel | Jordan Love | Passing Yards | over | 0.6601 | 0.5 | 0.1601 | False | 2026-09-09T17:34:29Z |
| draftkings|0QA362350810#2254581549_13L88808Q12038958166Q20 | draftkings | Dalton Schultz | Anytime TD Scorer | over | 0.2198 | 0.0614 | 0.1584 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA334613199#2151928228_13L88808Q11958986630Q20 | draftkings | Kyle Williams | Anytime TD Scorer | over | 0.219 | 0.0625 | 0.1565 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA361399049#2250882675_13L88808Q1-1846552455Q20 | draftkings | Mike Gesicki | Anytime TD Scorer | over | 0.2002 | 0.0437 | 0.1565 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA362350810#2254581566_13L88808Q1-2072232579Q20 | draftkings | Keon Coleman | Anytime TD Scorer | over | 0.2787 | 0.125 | 0.1537 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA334323199#2150675689_13L88808Q1610822396Q20 | draftkings | Terrance Ferguson | Anytime TD Scorer | over | 0.3536 | 0.2 | 0.1536 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA361399049#2250882692_13L88808Q11141276074Q20 | draftkings | Sean Tucker | Anytime TD Scorer | over | 0.3529 | 0.2 | 0.1529 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA334612412#2233956191_13L88808Q11556454751Q20 | draftkings | Tory Horton | 2+ TDs | over | 0.1637 | 0.011 | 0.1527 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA334323199#2150675803_13L88808Q1-2099105975Q20 | draftkings | George Kittle | Anytime TD Scorer | over | 0.4191 | 0.2667 | 0.1524 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA361397313#2250875332_13L88808Q1480222870Q20 | draftkings | Jameson Williams | Anytime TD Scorer | over | 0.2335 | 0.0848 | 0.1487 | False | 2026-09-09T17:54:53Z |
| fanduel|98516979 | fanduel | Rome Odunze | Receiving Yards | over | 0.6483 | 0.5 | 0.1483 | False | 2026-09-09T17:34:29Z |
| draftkings|0QA334323197#2150675579_13L88808Q11214736899Q20 | draftkings | Puka Nacua | 2+ TDs | over | 0.2362 | 0.0909 | 0.1453 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA363196021#2258143640_13L88808Q1-862670716Q20 | draftkings | Harold Fannin Jr. | 2+ TDs | over | 0.1711 | 0.0278 | 0.1434 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA361397313#2251041117_13L88808Q1138922171Q20 | draftkings | Devaughn Vele | Anytime TD Scorer | over | 0.1903 | 0.0495 | 0.1409 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA361399049#2250882696_13L88808Q1-1181521367Q20 | draftkings | Cade Otton | Anytime TD Scorer | over | 0.1881 | 0.0479 | 0.1401 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA363187905#2258120965_13L88808Q1-80697860Q20 | draftkings | Alec Pierce | 2+ TDs | over | 0.1734 | 0.0345 | 0.1389 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA363175928#2258086108_13L88808Q11277985563Q20 | draftkings | Chase Brown | 2+ TDs | over | 0.3114 | 0.1739 | 0.1375 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA363187905#2258120975_13L88808Q1-1364480320Q20 | draftkings | Zay Flowers | 2+ TDs | over | 0.1953 | 0.0667 | 0.1287 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA362350810#2254581550_13L88808Q1-2078311456Q20 | draftkings | Jaylin Noel | Anytime TD Scorer | over | 0.1679 | 0.0409 | 0.127 | False | 2026-09-09T17:54:53Z |
| fanduel|98663740 | fanduel | Malik Nabers | Receiving Yards | over | 0.6266 | 0.5 | 0.1266 | False | 2026-09-09T17:34:29Z |
| draftkings|0QA361399049#2250882688_13L88808Q1666446492Q20 | draftkings | Bucky Irving | Anytime TD Scorer | over | 0.2134 | 0.0873 | 0.126 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA362382884#2254729960_13L88808Q1-286456608Q20 | draftkings | Raheim Sanders | Anytime TD Scorer | over | 0.1732 | 0.0476 | 0.1256 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA363177179#2258089990_13L88808Q12022577872Q20 | draftkings | Chris Olave | 2+ TDs | over | 0.2079 | 0.0833 | 0.1246 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA334323199#2150675650_13L88808Q1-1719984573Q20 | draftkings | Davante Adams | Anytime TD Scorer | over | 0.5768 | 0.4545 | 0.1223 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA334323199#2238859996_13L88808Q1-1863661381Q20 | draftkings | Deebo Samuel | Anytime TD Scorer | over | 0.171 | 0.0502 | 0.1208 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA361399049#2250882697_13L88808Q1-1654530021Q20 | draftkings | Tez Johnson | Anytime TD Scorer | over | 0.1535 | 0.0342 | 0.1193 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA362104903#2253619467_13L88808Q1-1009547054Q20 | draftkings | Ja'Tavion Sanders | Anytime TD Scorer | over | 0.1948 | 0.0769 | 0.1179 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA362350810#2254581547_13L88808Q11052217445Q20 | draftkings | Woody Marks | Anytime TD Scorer | over | 0.1945 | 0.0767 | 0.1177 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA362382884#2254729950_13L88808Q1-458881524Q20 | draftkings | Travis Hunter | Anytime TD Scorer | over | 0.2184 | 0.1053 | 0.1131 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA362350810#2254581564_13L88808Q12079458734Q20 | draftkings | Khalil Shakir | Anytime TD Scorer | over | 0.1689 | 0.0571 | 0.1118 | False | 2026-09-09T17:54:53Z |
| fanduel|99787353 | fanduel | Mike Evans | Receiving Yards | under | 0.61 | 0.5 | 0.11 | False | 2026-09-09T17:34:29Z |
| draftkings|0QA334613199#2252728011_13L88808Q1-2056923875Q20 | draftkings | Efton Chism III | Anytime TD Scorer | over | 0.171 | 0.0625 | 0.1085 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA363186669#2258117172_13L88808Q11837409965Q20 | draftkings | Ty Johnson | 2+ TDs | over | 0.1209 | 0.0141 | 0.1068 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA361505183#2251317241_13L88808Q1-883785420Q20 | draftkings | Josh Downs | Anytime TD Scorer | over | 0.1689 | 0.0646 | 0.1043 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA334323197#2150675560_13L88808Q1273996050Q20 | draftkings | Davante Adams | 2+ TDs | over | 0.2129 | 0.1111 | 0.1018 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA334323199#2150675809_13L88808Q1785301666Q20 | draftkings | Demarcus Robinson | Anytime TD Scorer | over | 0.1269 | 0.0251 | 0.1018 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA362104903#2253619479_13L88808Q12086988331Q20 | draftkings | Luther Burden III | Anytime TD Scorer | over | 0.1744 | 0.0739 | 0.1005 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA362104903#2253619324_13L88808Q1633357284Q20 | draftkings | Kalif Raymond | Anytime TD Scorer | over | 0.1248 | 0.0254 | 0.0994 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA362382884#2254729947_13L88808Q1-271780635Q20 | draftkings | Brian Thomas Jr. | Anytime TD Scorer | over | 0.1539 | 0.0566 | 0.0974 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA334613199#2151928224_13L88808Q1-1762786291Q20 | draftkings | Hunter Henry | Anytime TD Scorer | over | 0.3501 | 0.2532 | 0.0969 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA362104903#2253619461_13L88808Q1-537154100Q20 | draftkings | Jalen Coker | Anytime TD Scorer | over | 0.3373 | 0.2439 | 0.0934 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA334613199#2151928217_13L88808Q12121391530Q20 | draftkings | George Holani | Anytime TD Scorer | over | 0.1605 | 0.0676 | 0.0929 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA361399049#2250882691_13L88808Q1621783265Q20 | draftkings | Emeka Egbuka | Anytime TD Scorer | over | 0.1618 | 0.0714 | 0.0903 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA361399049#2250882672_13L88808Q1106346443Q20 | draftkings | Tee Higgins | Anytime TD Scorer | over | 0.5331 | 0.4444 | 0.0887 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA361505183#2251317261_13L88808Q11994625172Q20 | draftkings | Justice Hill | Anytime TD Scorer | over | 0.2404 | 0.1538 | 0.0866 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA362382884#2254729945_13L88808Q11137102484Q20 | draftkings | Chris Rodriguez Jr. | Anytime TD Scorer | over | 0.4566 | 0.3704 | 0.0863 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA361397313#2250875357_13L88808Q11213714519Q20 | draftkings | Noah Fant | Anytime TD Scorer | over | 0.109 | 0.0237 | 0.0852 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA362350810#2254581571_13L88808Q11731434928Q20 | draftkings | Jackson Hawes | Anytime TD Scorer | over | 0.1609 | 0.0769 | 0.0839 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA361397313#2250875355_13L88808Q1-403572542Q20 | draftkings | Kendre Miller | Anytime TD Scorer | over | 0.1232 | 0.0396 | 0.0836 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA334323199#2262588466_13L88808Q1-1276590114Q20 | draftkings | Tutu Atwell | Anytime TD Scorer | over | 0.0974 | 0.0141 | 0.0833 | False | 2026-09-09T18:54:58Z |
| draftkings|0QA363171670#2258072364_13L88808Q1637812501Q20 | draftkings | Darren Waller | 2+ TDs | over | 0.1005 | 0.0196 | 0.0809 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA334323199#2150675727_13L88808Q1-822030320Q20 | draftkings | Davis Allen | Anytime TD Scorer | over | 0.0952 | 0.015 | 0.0801 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA361505183#2251317258_13L88808Q1-1031442765Q20 | draftkings | Mark Andrews | Anytime TD Scorer | over | 0.1618 | 0.0822 | 0.0796 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA362382884#2254729965_13L88808Q11127564074Q20 | draftkings | Dylan Sampson | Anytime TD Scorer | over | 0.1012 | 0.0262 | 0.075 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA361505183#2251317262_13L88808Q11574112063Q20 | draftkings | Rasheen Ali | Anytime TD Scorer | over | 0.0891 | 0.0162 | 0.073 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA363175928#2258086110_13L88808Q1-1865349726Q20 | draftkings | Tee Higgins | 2+ TDs | over | 0.1775 | 0.1053 | 0.0722 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA334323197#2150675773_13L88808Q11567635031Q20 | draftkings | Jake Tonges | 2+ TDs | over | 0.0857 | 0.0141 | 0.0716 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA362104903#2253619476_13L88808Q1655740791Q20 | draftkings | Kyle Monangai | Anytime TD Scorer | over | 0.1368 | 0.0656 | 0.0712 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA362104903#2253619478_13L88808Q1-2109230062Q20 | draftkings | Colston Loveland | Anytime TD Scorer | over | 0.4099 | 0.339 | 0.0709 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA362104903#2253619459_13L88808Q1850190615Q20 | draftkings | Chuba Hubbard | Anytime TD Scorer | over | 0.1591 | 0.0884 | 0.0707 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA363177179#2258089979_13L88808Q1-2063073039Q20 | draftkings | Isaac TeSlaa | 2+ TDs | over | 0.084 | 0.0179 | 0.0661 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA363171670#2258072386_13L88808Q1-704328598Q20 | draftkings | Jahdae Walker | 2+ TDs | over | 0.0731 | 0.0071 | 0.066 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA362350810#2254581565_13L88808Q1614963414Q20 | draftkings | Ray Davis | Anytime TD Scorer | over | 0.2085 | 0.1429 | 0.0656 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA361505183#2251317239_13L88808Q1-297522584Q20 | draftkings | Tyler Warren | Anytime TD Scorer | over | 0.1368 | 0.0713 | 0.0655 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA334613199#2151928229_13L88808Q1-205213128Q20 | draftkings | Demario Douglas | Anytime TD Scorer | over | 0.0895 | 0.0241 | 0.0654 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA334323197#2150675714_13L88808Q11108077714Q20 | draftkings | George Kittle | 2+ TDs | over | 0.1036 | 0.0385 | 0.0651 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA362382884#2254729948_13L88808Q1-992648746Q20 | draftkings | Jakobi Meyers | Anytime TD Scorer | over | 0.1252 | 0.0615 | 0.0636 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA362104903#2253619462_13L88808Q1922326735Q20 | draftkings | Xavier Legette | Anytime TD Scorer | over | 0.0952 | 0.0339 | 0.0613 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA334323199#2150675815_13L88808Q11061966518Q20 | draftkings | Kyle Juszczyk | Anytime TD Scorer | over | 0.171 | 0.1111 | 0.0599 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA362382884#2254729963_13L88808Q1526503198Q20 | draftkings | Jerry Jeudy | Anytime TD Scorer | over | 0.0941 | 0.038 | 0.056 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA362104903#2253619463_13L88808Q1259912862Q20 | draftkings | John Metchie III | Anytime TD Scorer | over | 0.074 | 0.0185 | 0.0556 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA363187905#2258120974_13L88808Q11746484724Q20 | draftkings | Derrick Henry | 2+ TDs | over | 0.3267 | 0.2716 | 0.0551 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA363186669#2258117170_13L88808Q1-116043467Q20 | draftkings | Dawson Knox | 2+ TDs | over | 0.067 | 0.0123 | 0.0546 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA361505183#2251317240_13L88808Q1716026518Q20 | draftkings | Keenan Allen | Anytime TD Scorer | over | 0.111 | 0.0564 | 0.0546 | False | 2026-09-09T17:54:53Z |
| fanduel|99006961 | fanduel | Saquon Barkley | Rushing TDs | over | 0.5543 | 0.5 | 0.0543 | False | 2026-09-09T17:34:29Z |
| draftkings|0QA334613199#2151928227_13L88808Q1950577073Q20 | draftkings | Mack Hollins | Anytime TD Scorer | over | 0.0689 | 0.0161 | 0.0529 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA362104903#2253619470_13L88808Q1-619052431Q20 | draftkings | Mitchell Evans | Anytime TD Scorer | over | 0.0689 | 0.0169 | 0.052 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA334613199#2151928212_13L88808Q11707072676Q20 | draftkings | Emanuel Wilson | Anytime TD Scorer | over | 0.0845 | 0.0335 | 0.0509 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA361399049#2250882674_13L88808Q11111630045Q20 | draftkings | Samaje Perine | Anytime TD Scorer | over | 0.2775 | 0.2273 | 0.0502 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA362350810#2254581552_13L88808Q1-1444150535Q20 | draftkings | Xavier Hutchinson | Anytime TD Scorer | over | 0.0895 | 0.0409 | 0.0486 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA363196021#2258143627_13L88808Q1-1327690156Q20 | draftkings | Chris Rodriguez Jr. | 2+ TDs | over | 0.1252 | 0.0769 | 0.0483 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA334323197#2150675635_13L88808Q12084623368Q20 | draftkings | Terrance Ferguson | 2+ TDs | over | 0.0716 | 0.0244 | 0.0472 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA363175928#2258086127_13L88808Q1-1540780736Q20 | draftkings | Sean Tucker | 2+ TDs | over | 0.0713 | 0.0244 | 0.0469 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA363186669#2258117164_13L88808Q1503159412Q20 | draftkings | James Cook | 2+ TDs | over | 0.1883 | 0.1429 | 0.0454 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA334613199#2151928214_13L88808Q1-1216598181Q20 | draftkings | Cooper Kupp | Anytime TD Scorer | over | 0.0974 | 0.0528 | 0.0446 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA361505183#2251317246_13L88808Q11956512748Q20 | draftkings | Andrew Ogletree | Anytime TD Scorer | over | 0.1001 | 0.0556 | 0.0445 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA363187905#2258120982_13L88808Q1-464941358Q20 | draftkings | Devontez Walker | 2+ TDs | over | 0.0518 | 0.0076 | 0.0442 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA362382884#2254729949_13L88808Q1-1393332464Q20 | draftkings | Brenton Strange | Anytime TD Scorer | over | 0.3297 | 0.2857 | 0.044 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA334323197#2150675609_13L88808Q11735898398Q20 | draftkings | Tyler Higbee | 2+ TDs | over | 0.0576 | 0.0141 | 0.0435 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA362104903#2253619468_13L88808Q1-813345382Q20 | draftkings | Tommy Tremble | Anytime TD Scorer | over | 0.2147 | 0.1739 | 0.0408 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA363171670#2258072377_13L88808Q1-244560726Q20 | draftkings | Colston Loveland | 2+ TDs | over | 0.0987 | 0.0588 | 0.0398 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA361505183#2251317245_13L88808Q1-1885662408Q20 | draftkings | Mo Alie-Cox | Anytime TD Scorer | over | 0.1567 | 0.1176 | 0.0391 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA362382884#2254729969_13L88808Q11011846392Q20 | draftkings | Tylan Wallace | Anytime TD Scorer | over | 0.0444 | 0.0068 | 0.0377 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA334613199#2151928223_13L88808Q1-349638135Q20 | draftkings | Romeo Doubs | Anytime TD Scorer | over | 0.2971 | 0.2597 | 0.0373 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA334323197#2150675684_13L88808Q1-1442390665Q20 | draftkings | Christian McCaffrey | 2+ TDs | over | 0.2367 | 0.2 | 0.0367 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA334612412#2151925232_13L88808Q11740203848Q20 | draftkings | Hunter Henry | 2+ TDs | over | 0.07 | 0.0345 | 0.0355 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA361397313#2250875333_13L88808Q1779951428Q20 | draftkings | Brock Wright | Anytime TD Scorer | over | 0.1175 | 0.0833 | 0.0342 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA363171670#2258072363_13L88808Q1131228805Q20 | draftkings | Jalen Coker | 2+ TDs | over | 0.0646 | 0.0323 | 0.0324 | True | 2026-09-09T17:34:29Z |
| draftkings|0QA334323199#2150675719_13L88808Q1-1508640754Q20 | draftkings | Konata Mumpfield | Anytime TD Scorer | over | 0.0488 | 0.0174 | 0.0314 | False | 2026-09-09T17:54:53Z |
| draftkings|0QA363186669#2258117169_13L88808Q1-2143181684Q20 | draftkings | Keon Coleman | 2+ TDs | over | 0.043 | 0.0123 | 0.0307 | True | 2026-09-09T17:34:29Z |
