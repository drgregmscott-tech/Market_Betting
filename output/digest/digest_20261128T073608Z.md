# Pipeline Digest -- 2026-11-28T07:36:08Z

## Run summary
- Ingestion: 60408 rows (PrizePicks OK, Underdog OK)
- Estimation: 60408 rows estimated (from 60408 ingested props)
- CLV logging: 52 newly flagged, 0 newly closed, 83 still open (112499 total ever logged)

## Currently open flags
Sizing is a manual step (sizing_engine.py, Session 2.6) -- this table is what to scan to pick a pair worth sizing.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_edge | first_flagged_at | game_start_time |
|---|---|---|---|---|---|---|---|
| prizepicks|17371820 | prizepicks | Anthony Richardson Sr. | Pass Yards | under | 0.35094246505677495 | 2026-11-24T14:47:41Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17572778 | prizepicks | Jake Moody | Fantasy Score | under | 0.35094246505677495 | 2026-11-28T07:42:51Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17575515 | prizepicks | Veronika Erjavec | Break Points Won | under | 0.35094246505677495 | 2026-11-28T07:42:51Z | 2026-11-28T12:00:00.000-05:00 |
| prizepicks|17564817 | prizepicks | J.J. McCarthy | Pass+Rush+Rec TDs | under | 0.35094246505677495 | 2026-11-28T07:42:51Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17433884 | prizepicks | Baker Mayfield | Pass+Rush+Rec TDs | under | 0.33619322591662215 | 2026-11-25T00:43:43Z | 2026-11-30T20:15:00.000-05:00 |
| prizepicks|17371817 | prizepicks | Michael Penix Jr. | Pass Yards | under | 0.3322469500724762 | 2026-11-24T14:47:41Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17564819 | prizepicks | Deshaun Watson | Pass+Rush+Rec TDs | under | 0.29732793624209364 | 2026-11-28T07:42:51Z | 2026-11-29T20:20:00.000-05:00 |
| prizepicks|17371831 | prizepicks | Baker Mayfield | Pass Yards | under | 0.2947317581520855 | 2026-11-24T14:47:41Z | 2026-11-30T20:15:00.000-05:00 |
| prizepicks|17371829 | prizepicks | Fernando Mendoza | Pass Yards | under | 0.2803073369792758 | 2026-11-24T14:47:41Z | 2026-11-29T20:20:00.000-05:00 |
| prizepicks|17371818 | prizepicks | Kirk Cousins | Pass Yards | under | 0.27218101538958084 | 2026-11-24T14:47:41Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17371819 | prizepicks | J.J. McCarthy | Pass Yards | under | 0.2535386920183703 | 2026-11-24T14:47:41Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17371825 | prizepicks | Tyler Shough | Pass Yards | under | 0.25049427754286013 | 2026-11-24T14:47:41Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17565602 | prizepicks | Zay Jones | Rec Targets | under | 0.23786523617587452 | 2026-11-28T07:42:51Z | 2026-11-29T16:25:00.000-05:00 |
| prizepicks|17372159 | prizepicks | Emeka Egbuka | Rec Yards | under | 0.21162247730210237 | 2026-11-24T14:47:41Z | 2026-11-30T20:15:00.000-05:00 |
| prizepicks|17564816 | prizepicks | Trevor Lawrence | Pass+Rush+Rec TDs | under | 0.18463126377958317 | 2026-11-28T07:42:51Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17372148 | prizepicks | Jordyn Tyson | Rec Yards | under | 0.17546756736578828 | 2026-11-24T14:47:41Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17565600 | prizepicks | Simi Fehoko | Rec Targets | under | 0.16596914229116055 | 2026-11-28T07:42:51Z | 2026-11-29T16:25:00.000-05:00 |
| prizepicks|17565645 | prizepicks | Josh Cameron | Rec Targets | under | 0.16576211439261157 | 2026-11-28T07:42:51Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17492664 | prizepicks | Anthony Gould | Recs | under | 0.16518930019593403 | 2026-11-26T00:22:01Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17575517 | prizepicks | Guiomar Maristany Zuleta de Reales | Break Points Won | under | 0.16491347935004086 | 2026-11-28T07:42:51Z | 2026-11-28T10:00:00.000-05:00 |
| prizepicks|17565638 | prizepicks | Deion Burks | Rec Targets | under | 0.14601428224317403 | 2026-11-28T07:42:51Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17565631 | prizepicks | Marvin Harrison Jr. | Rec Targets | under | 0.13804896051726423 | 2026-11-28T07:42:51Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17565708 | prizepicks | Jauan Jennings | Rec Targets | under | 0.13465439698611104 | 2026-11-28T07:42:51Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17374182 | prizepicks | Blake Whiteheart | Rec Yards | over | 0.13415129962029704 | 2026-11-24T14:47:41Z | 2026-11-29T20:20:00.000-05:00 |
| prizepicks|17565636 | prizepicks | Anthony Gould | Rec Targets | under | 0.13368501722708592 | 2026-11-28T07:42:51Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17565647 | prizepicks | Travis Hunter | Rec Targets | under | 0.12987045845776934 | 2026-11-28T07:42:51Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17372145 | prizepicks | Nico Collins | Rec Yards | under | 0.12214502875029642 | 2026-11-24T14:47:41Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17565731 | prizepicks | Breece Hall | Rec Targets | under | 0.12011046210802434 | 2026-11-28T07:42:51Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17565611 | prizepicks | Zay Flowers | Rec Targets | under | 0.1148511611879317 | 2026-11-28T07:42:51Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17574091 | prizepicks | Dilin Jones | Rush Atts | under | 0.11471655580483642 | 2026-11-28T07:42:51Z | 2026-11-28T12:45:00.000-05:00 |
| prizepicks|17565651 | prizepicks | Caleb Hawkins | Rush Atts | under | 0.11237886671369568 | 2026-11-28T07:42:51Z | 2026-11-28T18:15:00.000-05:00 |
| prizepicks|17565643 | prizepicks | Brian Thomas Jr. | Rec Targets | under | 0.10978765204358654 | 2026-11-28T07:42:51Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17565740 | prizepicks | Jaxon Smith-Njigba | Rec Targets | under | 0.10443554222865492 | 2026-11-28T07:42:51Z | 2026-11-29T16:25:00.000-05:00 |
| prizepicks|17565735 | prizepicks | Mike Evans | Rec Targets | under | 0.102402892661274 | 2026-11-28T07:42:51Z | 2026-11-29T16:25:00.000-05:00 |
| prizepicks|17437171 | prizepicks | Demond Williams Jr. | Rush Atts | under | 0.10225211166729276 | 2026-11-26T00:22:01Z | 2026-11-28T19:30:00.000-05:00 |
| prizepicks|17565747 | prizepicks | Chimere Dike | Rec Targets | under | 0.09907199962888125 | 2026-11-28T07:42:51Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17565605 | prizepicks | Kyle Pitts Sr. | Rec Targets | under | 0.09874261411003171 | 2026-11-28T07:42:51Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17565750 | prizepicks | Chig Okonkwo | Rec Targets | under | 0.09784777474421169 | 2026-11-28T07:42:51Z | 2026-11-29T16:25:00.000-05:00 |
| prizepicks|17565604 | prizepicks | Drake London | Rec Targets | under | 0.09568125883795053 | 2026-11-28T07:42:51Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17371814 | prizepicks | Fernando Mendoza | Rush Yards | under | 0.09433994398041257 | 2026-11-24T14:47:41Z | 2026-11-29T20:20:00.000-05:00 |
| prizepicks|17565743 | prizepicks | Carnell Tate | Rec Targets | under | 0.09392816638257973 | 2026-11-28T07:42:51Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17372072 | prizepicks | Travis Etienne Jr. | Rush Yards | under | 0.09284275226526228 | 2026-11-24T14:47:41Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17487990 | prizepicks | DeJuan Williams | Rush Atts | under | 0.0927157448521162 | 2026-11-28T07:42:51Z | 2026-11-28T15:30:00.000-05:00 |
| prizepicks|17565644 | prizepicks | Jakobi Meyers | Rec Targets | under | 0.09216834097326354 | 2026-11-28T07:42:51Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17374183 | prizepicks | Connor Heyward | Rush+Rec Yds | over | 0.09173826578691047 | 2026-11-24T14:47:41Z | 2026-11-29T20:20:00.000-05:00 |
| prizepicks|17565626 | prizepicks | KC Concepcion Jr. | Rec Targets | under | 0.09080952120105068 | 2026-11-28T07:42:51Z | 2026-11-29T20:20:00.000-05:00 |
| prizepicks|17372134 | prizepicks | Kyle Pitts Sr. | Rec Yards | under | 0.087793639145063 | 2026-11-24T14:47:41Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17565621 | prizepicks | Ja'Marr Chase | Rec Targets | under | 0.08394796421859552 | 2026-11-28T07:42:51Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17372068 | prizepicks | Cam Skattebo | Rush Yards | under | 0.08073939241194372 | 2026-11-24T14:47:41Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17433599 | prizepicks | Ja'Marr Chase | Rec Yards | under | 0.0790595573316959 | 2026-11-25T00:43:43Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17565601 | prizepicks | Trey McBride | Rec Targets | under | 0.07143907504854397 | 2026-11-28T07:42:51Z | 2026-11-29T16:25:00.000-05:00 |
| prizepicks|17565749 | prizepicks | Antonio Williams | Rec Targets | under | 0.06804764635999816 | 2026-11-28T07:42:51Z | 2026-11-29T16:25:00.000-05:00 |
| prizepicks|17372156 | prizepicks | KC Concepcion Jr. | Rec Yards | under | 0.06650304459863476 | 2026-11-24T14:47:41Z | 2026-11-29T20:20:00.000-05:00 |
| prizepicks|17565711 | prizepicks | T.J. Hockenson | Rec Targets | under | 0.0659176553976244 | 2026-11-28T07:42:51Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17565642 | prizepicks | Brenton Strange | Rec Targets | under | 0.06351604703282643 | 2026-11-28T07:42:51Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17421861 | prizepicks | Junior Sherrill | Recs | under | 0.06330419672118304 | 2026-11-28T07:42:51Z | 2026-11-28T19:00:00.000-05:00 |
| prizepicks|17565714 | prizepicks | Hunter Henry | Rec Targets | under | 0.05776299570119647 | 2026-11-28T07:42:51Z | 2026-11-29T16:05:00.000-05:00 |
| prizepicks|17492668 | prizepicks | Gunnar Helm | Recs | under | 0.05760478051949369 | 2026-11-26T00:22:01Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17548282 | prizepicks | Wayne Knight | Rush Atts | under | 0.05684403616124967 | 2026-11-28T07:42:51Z | 2026-11-28T15:30:00.000-05:00 |
| prizepicks|17565608 | prizepicks | Justice Hill | Rec Targets | under | 0.055734931821182276 | 2026-11-28T07:42:51Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17565630 | prizepicks | Xavier Hutchinson | Rec Targets | under | 0.054794624123657765 | 2026-11-28T07:42:51Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17492667 | prizepicks | Chimere Dike | Recs | under | 0.054578030690095924 | 2026-11-26T00:22:01Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17372152 | prizepicks | Trey McBride | Rec Yards | under | 0.05443598118688209 | 2026-11-24T14:47:41Z | 2026-11-29T16:25:00.000-05:00 |
| prizepicks|17492675 | prizepicks | Cade Otton | Recs | under | 0.051180334115476955 | 2026-11-26T00:22:01Z | 2026-11-30T20:15:00.000-05:00 |
| prizepicks|17459854 | prizepicks | Richard Young | Rush Atts | under | 0.04831822927567275 | 2026-11-28T07:42:51Z | 2026-11-28T14:00:00.000-05:00 |
| prizepicks|17565610 | prizepicks | Rashod Bateman | Rec Targets | under | 0.046406948782009017 | 2026-11-28T07:42:51Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17565751 | prizepicks | Stefon Diggs | Rec Targets | under | 0.04436378997402801 | 2026-11-28T07:42:51Z | 2026-11-29T16:25:00.000-05:00 |
| prizepicks|17372147 | prizepicks | Chris Olave | Rec Yards | under | 0.04392985951025752 | 2026-11-24T14:47:41Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17492663 | prizepicks | Drake London | Recs | under | 0.043057861482137194 | 2026-11-26T00:22:01Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17565719 | prizepicks | Jordyn Tyson | Rec Targets | under | 0.042183584880765346 | 2026-11-28T07:42:51Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17565625 | prizepicks | Harold Fannin Jr. | Rec Targets | under | 0.041627709557591985 | 2026-11-28T07:42:51Z | 2026-11-29T20:20:00.000-05:00 |
| prizepicks|17434921 | prizepicks | Que'Sean Brown | Recs | under | 0.04106916596687249 | 2026-11-28T07:42:51Z | 2026-11-28T15:00:00.000-05:00 |
| prizepicks|17417668 | prizepicks | John Mateer | Pass Attempts | under | 0.0388929627739093 | 2026-11-25T14:15:10Z | 2026-11-28T16:15:00.000-05:00 |
| prizepicks|17565755 | prizepicks | Cade Otton | Rec Targets | under | 0.03749170607158203 | 2026-11-28T07:42:51Z | 2026-11-30T20:15:00.000-05:00 |
| prizepicks|17565744 | prizepicks | Elic Ayomanor | Rec Targets | under | 0.036664858918087795 | 2026-11-28T07:42:51Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17565700 | prizepicks | Brock Bowers | Rec Targets | under | 0.03393870466278359 | 2026-11-28T07:42:51Z | 2026-11-29T20:20:00.000-05:00 |
| prizepicks|17372071 | prizepicks | Derrick Henry | Rush Yards | under | 0.03362279798660894 | 2026-11-24T14:47:41Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17372153 | prizepicks | Brock Bowers | Rec Yards | under | 0.03333738253060603 | 2026-11-24T14:47:41Z | 2026-11-29T20:20:00.000-05:00 |
| prizepicks|17492674 | prizepicks | Bucky Irving | Recs | under | 0.03203555418761461 | 2026-11-26T00:22:01Z | 2026-11-30T20:15:00.000-05:00 |
| prizepicks|17565745 | prizepicks | Gunnar Helm | Rec Targets | under | 0.03167472266316951 | 2026-11-28T07:42:51Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17565706 | prizepicks | Ollie Gordon II | Rec Targets | under | 0.031665800905143815 | 2026-11-28T07:42:51Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17565746 | prizepicks | Tyjae Spears | Rec Targets | under | 0.030714123813170624 | 2026-11-28T07:42:51Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17565599 | prizepicks | Harrison Wallace III | Rec Targets | under | 0.030665488412648823 | 2026-11-28T07:42:51Z | 2026-11-29T16:25:00.000-05:00 |
