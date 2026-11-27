# Pipeline Digest -- 2026-11-27T00:31:45Z

## Run summary
- Ingestion: 43872 rows (PrizePicks OK, Underdog OK)
- Estimation: 43872 rows estimated (from 43872 ingested props)
- CLV logging: 0 newly flagged, 0 newly closed, 45 still open (112444 total ever logged)

## Currently open flags
Sizing is a manual step (sizing_engine.py, Session 2.6) -- this table is what to scan to pick a pair worth sizing.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_edge | first_flagged_at | game_start_time |
|---|---|---|---|---|---|---|---|
| prizepicks|17371820 | prizepicks | Anthony Richardson Sr. | Pass Yards | under | 0.35094246505677495 | 2026-11-24T14:47:41Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17433884 | prizepicks | Baker Mayfield | Pass+Rush+Rec TDs | under | 0.33619322591662215 | 2026-11-25T00:43:43Z | 2026-11-30T20:15:00.000-05:00 |
| prizepicks|17371817 | prizepicks | Michael Penix Jr. | Pass Yards | under | 0.3322469500724762 | 2026-11-24T14:47:41Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17371831 | prizepicks | Baker Mayfield | Pass Yards | under | 0.2947317581520855 | 2026-11-24T14:47:41Z | 2026-11-30T20:15:00.000-05:00 |
| prizepicks|17371829 | prizepicks | Fernando Mendoza | Pass Yards | under | 0.2803073369792758 | 2026-11-24T14:47:41Z | 2026-11-29T20:20:00.000-05:00 |
| prizepicks|17371818 | prizepicks | Kirk Cousins | Pass Yards | under | 0.27218101538958084 | 2026-11-24T14:47:41Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17371819 | prizepicks | J.J. McCarthy | Pass Yards | under | 0.2535386920183703 | 2026-11-24T14:47:41Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17371825 | prizepicks | Tyler Shough | Pass Yards | under | 0.25049427754286013 | 2026-11-24T14:47:41Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17372159 | prizepicks | Emeka Egbuka | Rec Yards | under | 0.21162247730210237 | 2026-11-24T14:47:41Z | 2026-11-30T20:15:00.000-05:00 |
| prizepicks|17357057 | prizepicks | James Cook III | Rush TDs | over | 0.17860906817196054 | 2026-11-25T00:43:43Z | 2026-11-26T20:20:00.000-05:00 |
| prizepicks|17372148 | prizepicks | Jordyn Tyson | Rec Yards | under | 0.17546756736578828 | 2026-11-24T14:47:41Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17492664 | prizepicks | Anthony Gould | Recs | under | 0.16518930019593403 | 2026-11-26T00:22:01Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17374182 | prizepicks | Blake Whiteheart | Rec Yards | over | 0.13415129962029704 | 2026-11-24T14:47:41Z | 2026-11-29T20:20:00.000-05:00 |
| prizepicks|17374179 | prizepicks | Jake Briningstool | Rec Yards | over | 0.12717407730455854 | 2026-11-24T14:47:41Z | 2026-11-26T20:20:00.000-05:00 |
| prizepicks|17372145 | prizepicks | Nico Collins | Rec Yards | under | 0.12214502875029642 | 2026-11-24T14:47:41Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17368911 | prizepicks | Rashee Rice | Rec Targets | under | 0.11367790298741587 | 2026-11-24T14:47:41Z | 2026-11-26T20:20:00.000-05:00 |
| prizepicks|17489251 | prizepicks | Emmett Johnson | Rec Targets | under | 0.10762928436674857 | 2026-11-26T00:22:01Z | 2026-11-26T20:20:00.000-05:00 |
| prizepicks|17437171 | prizepicks | Demond Williams Jr. | Rush Atts | under | 0.10225211166729276 | 2026-11-26T00:22:01Z | 2026-11-28T19:30:00.000-05:00 |
| prizepicks|17371814 | prizepicks | Fernando Mendoza | Rush Yards | under | 0.09433994398041257 | 2026-11-24T14:47:41Z | 2026-11-29T20:20:00.000-05:00 |
| prizepicks|17372072 | prizepicks | Travis Etienne Jr. | Rush Yards | under | 0.09284275226526228 | 2026-11-24T14:47:41Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17374183 | prizepicks | Connor Heyward | Rush+Rec Yds | over | 0.09173826578691047 | 2026-11-24T14:47:41Z | 2026-11-29T20:20:00.000-05:00 |
| prizepicks|17372134 | prizepicks | Kyle Pitts Sr. | Rec Yards | under | 0.087793639145063 | 2026-11-24T14:47:41Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17372074 | prizepicks | Christian McCaffrey | Rush Yards | under | 0.08436808591439793 | 2026-11-24T14:47:41Z | 2026-11-29T16:25:00.000-05:00 |
| prizepicks|17492670 | prizepicks | Breece Hall | Recs | under | 0.083991392942528 | 2026-11-26T00:22:01Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17372068 | prizepicks | Cam Skattebo | Rush Yards | under | 0.08073939241194372 | 2026-11-24T14:47:41Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17433599 | prizepicks | Ja'Marr Chase | Rec Yards | under | 0.0790595573316959 | 2026-11-25T00:43:43Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17374181 | prizepicks | Nate Adkins | Rec Yards | over | 0.07780241499840279 | 2026-11-24T14:47:41Z | 2026-11-27T15:00:00.000-05:00 |
| prizepicks|17374180 | prizepicks | Keleki Latu | Rec Yards | over | 0.07300884938107377 | 2026-11-24T14:47:41Z | 2026-11-26T20:20:00.000-05:00 |
| prizepicks|17372156 | prizepicks | KC Concepcion Jr. | Rec Yards | under | 0.06650304459863476 | 2026-11-24T14:47:41Z | 2026-11-29T20:20:00.000-05:00 |
| prizepicks|17435193 | prizepicks | Jaylen Waddle | Recs | under | 0.06530391369667332 | 2026-11-25T00:43:43Z | 2026-11-27T15:00:00.000-05:00 |
| prizepicks|17492668 | prizepicks | Gunnar Helm | Recs | under | 0.05760478051949369 | 2026-11-26T00:22:01Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17492667 | prizepicks | Chimere Dike | Recs | under | 0.054578030690095924 | 2026-11-26T00:22:01Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17372152 | prizepicks | Trey McBride | Rec Yards | under | 0.05443598118688209 | 2026-11-24T14:47:41Z | 2026-11-29T16:25:00.000-05:00 |
| prizepicks|17492675 | prizepicks | Cade Otton | Recs | under | 0.051180334115476955 | 2026-11-26T00:22:01Z | 2026-11-30T20:15:00.000-05:00 |
| prizepicks|17368905 | prizepicks | Pat Bryant | Rec Targets | under | 0.04785879407879767 | 2026-11-24T14:47:41Z | 2026-11-27T15:00:00.000-05:00 |
| prizepicks|17372154 | prizepicks | Denzel Boston | Rec Yards | under | 0.046147804038233264 | 2026-11-24T14:47:41Z | 2026-11-29T20:20:00.000-05:00 |
| prizepicks|17372147 | prizepicks | Chris Olave | Rec Yards | under | 0.04392985951025752 | 2026-11-24T14:47:41Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17492663 | prizepicks | Drake London | Recs | under | 0.043057861482137194 | 2026-11-26T00:22:01Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17375680 | prizepicks | DJ Moore | Rush Yards | over | 0.040094841349221144 | 2026-11-24T14:47:41Z | 2026-11-26T20:20:00.000-05:00 |
| prizepicks|17417668 | prizepicks | John Mateer | Pass Attempts | under | 0.0388929627739093 | 2026-11-25T14:15:10Z | 2026-11-28T16:15:00.000-05:00 |
| prizepicks|17489004 | prizepicks | Travis Kelce | Recs | under | 0.03807178174763237 | 2026-11-26T13:54:58Z | 2026-11-26T20:20:00.000-05:00 |
| prizepicks|17368901 | prizepicks | Jaylen Waddle | Rec Targets | under | 0.03559653356251935 | 2026-11-24T14:47:41Z | 2026-11-27T15:00:00.000-05:00 |
| prizepicks|17372071 | prizepicks | Derrick Henry | Rush Yards | under | 0.03362279798660894 | 2026-11-24T14:47:41Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17372153 | prizepicks | Brock Bowers | Rec Yards | under | 0.03333738253060603 | 2026-11-24T14:47:41Z | 2026-11-29T20:20:00.000-05:00 |
| prizepicks|17492674 | prizepicks | Bucky Irving | Recs | under | 0.03203555418761461 | 2026-11-26T00:22:01Z | 2026-11-30T20:15:00.000-05:00 |
