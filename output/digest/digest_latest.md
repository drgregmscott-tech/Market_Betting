# Pipeline Digest -- 2026-11-22T06:33:12Z

## Run summary
- Ingestion: 32277 rows (PrizePicks OK, Underdog OK)
- Estimation: 32277 rows estimated (from 32277 ingested props)
- CLV logging: 6 newly flagged, 0 newly closed, 80 still open (112344 total ever logged)

## Currently open flags
Sizing is a manual step (sizing_engine.py, Session 2.6) -- this table is what to scan to pick a pair worth sizing.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_edge | first_flagged_at | game_start_time |
|---|---|---|---|---|---|---|---|
| underdog|00b55c3f-8b0c-4d3b-b154-5539e4b0cb6a | underdog | Josh Allen | Pass Yards | under | 0.4 | 2026-11-16T06:19:05Z | 2026-11-22T18:00:00Z |
| prizepicks|17061845 | prizepicks | Caleb Williams | Pass Yards | under | 0.35094246505677495 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17209810 | prizepicks | Justin Herbert | Pass+Rush+Rec TDs | under | 0.35094246505677495 | 2026-11-20T07:05:43Z | 2026-11-22T16:05:00.000-05:00 |
| prizepicks|17061851 | prizepicks | Fernando Mendoza | Pass Yards | under | 0.35094246505677495 | 2026-11-17T13:14:06Z | 2026-11-22T16:25:00.000-05:00 |
| prizepicks|17247808 | prizepicks | Charlie Smyth | Fantasy Score | under | 0.35094246505677495 | 2026-11-21T01:31:21Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17061840 | prizepicks | Aaron Rodgers | Pass Yards | under | 0.3252779099272486 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17061852 | prizepicks | Bo Nix | Pass Yards | under | 0.3207875090752025 | 2026-11-17T13:14:06Z | 2026-11-22T16:25:00.000-05:00 |
| prizepicks|17061849 | prizepicks | Jared Goff | Pass Yards | under | 0.2998952886937002 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17172881 | prizepicks | Simi Fehoko | Rec Targets | under | 0.27241322394721845 | 2026-11-19T12:57:27Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17173322 | prizepicks | Saquon Barkley | Rec Targets | under | 0.2614113836150421 | 2026-11-19T12:57:27Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17061844 | prizepicks | Tyler Shough | Pass Yards | under | 0.249596263938357 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17211170 | prizepicks | Jordan Love | Pass Yards | under | 0.22441508177359581 | 2026-11-20T07:05:43Z | 2026-11-25T20:00:00.000-05:00 |
| prizepicks|17062823 | prizepicks | Jordyn Tyson | Rec Yards | under | 0.20121645364759722 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17062826 | prizepicks | Colston Loveland | Rec Yards | under | 0.18934940884625828 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17051036 | prizepicks | J.J. McCarthy | Pass Attempts | under | 0.17200392454345736 | 2026-11-19T12:57:27Z | 2026-11-22T16:25:00.000-05:00 |
| prizepicks|17173278 | prizepicks | Bryce Young | Pass Attempts | under | 0.16981258723647652 | 2026-11-19T12:57:27Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17108500 | prizepicks | Josh Allen | Pass+Rush+Rec TDs | under | 0.15592492640886924 | 2026-11-18T07:21:08Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17172918 | prizepicks | Jonah Coleman | Rec Targets | under | 0.14978688180069022 | 2026-11-19T12:57:27Z | 2026-11-22T16:25:00.000-05:00 |
| prizepicks|17211171 | prizepicks | Matthew Stafford | Pass Yards | under | 0.14419129979406875 | 2026-11-20T07:05:43Z | 2026-11-25T20:00:00.000-05:00 |
| prizepicks|17248811 | prizepicks | Elic Ayomanor | Rec Targets | under | 0.12915827014313408 | 2026-11-21T01:31:21Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17279285 | prizepicks | Ollie Gordon II | Rec Targets | under | 0.1196228330640291 | 2026-11-22T06:35:39Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17173329 | prizepicks | Carnell Tate | Rec Targets | under | 0.11936405589873289 | 2026-11-19T12:57:27Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17248821 | prizepicks | Breece Hall | Rec Targets | under | 0.11553094976662859 | 2026-11-21T01:31:21Z | 2026-11-22T16:05:00.000-05:00 |
| underdog|1c3ab1ad-e32d-483c-ba65-a163b75164ae | underdog | Javonte Williams | Rush Yards | under | 0.11519863917518858 | 2026-11-16T06:19:05Z | 2026-11-22T18:00:00Z |
| prizepicks|17172934 | prizepicks | Rashee Rice | Rec Targets | under | 0.11021925715465086 | 2026-11-19T12:57:27Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17172901 | prizepicks | Rome Odunze | Rec Targets | under | 0.11012854291659335 | 2026-11-19T12:57:27Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17062819 | prizepicks | Saquon Barkley | Rec Yards | under | 0.09863869301169803 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17248600 | prizepicks | Amon-Ra St. Brown | Recs | under | 0.09820830997244945 | 2026-11-21T01:31:21Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17211188 | prizepicks | Tucker Kraft | Rec Yards | under | 0.09637535679363307 | 2026-11-20T07:05:43Z | 2026-11-25T20:00:00.000-05:00 |
| prizepicks|17172885 | prizepicks | Mark Andrews | Rec Targets | under | 0.09572067811479934 | 2026-11-19T12:57:27Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17172915 | prizepicks | Courtland Sutton | Rec Targets | under | 0.09246124133941824 | 2026-11-19T12:57:27Z | 2026-11-22T16:25:00.000-05:00 |
| prizepicks|17172910 | prizepicks | Brevyn Spann-Ford | Rec Targets | under | 0.09246107865183517 | 2026-11-19T12:57:27Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17248814 | prizepicks | Chimere Dike | Rec Targets | under | 0.09177504146213011 | 2026-11-21T01:31:21Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17172879 | prizepicks | Elijah Higgins | Rec Targets | under | 0.09033332967696128 | 2026-11-19T12:57:27Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17279286 | prizepicks | T.J. Hockenson | Rec Targets | under | 0.08973245004510766 | 2026-11-22T06:35:39Z | 2026-11-22T20:20:00.000-05:00 |
| prizepicks|17208894 | prizepicks | Chris Godwin Jr. | Rec Targets | under | 0.08728266970728604 | 2026-11-20T07:05:43Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17119127 | prizepicks | Jacoby Brissett | Pass Attempts | under | 0.08559829317755474 | 2026-11-20T07:05:43Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17248828 | prizepicks | Pat Bryant | Rec Targets | under | 0.08472459040450653 | 2026-11-21T01:31:21Z | 2026-11-22T16:25:00.000-05:00 |
| prizepicks|17248815 | prizepicks | Daniel Bellinger | Rec Targets | under | 0.08288961820827778 | 2026-11-21T01:31:21Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17172929 | prizepicks | Nate Boerkircher | Rec Targets | under | 0.07673950782785632 | 2026-11-19T12:57:27Z | 2026-11-22T16:25:00.000-05:00 |
| prizepicks|17061961 | prizepicks | Chuba Hubbard | Rush Yards | under | 0.07421460278652392 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17051049 | prizepicks | Trevor Lawrence | INT | under | 0.0739461455291528 | 2026-11-22T06:35:39Z | 2026-11-22T16:25:00.000-05:00 |
| prizepicks|17208897 | prizepicks | Tez Johnson | Rec Targets | under | 0.07055231695542874 | 2026-11-20T07:05:43Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17062825 | prizepicks | Rome Odunze | Rec Yards | under | 0.06934931203037698 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17248588 | prizepicks | Dawson Knox | Recs | under | 0.06730137030890238 | 2026-11-21T01:31:21Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17191488 | prizepicks | D'Andre Swift | Rush TDs | over | 0.06649943732229935 | 2026-11-21T01:31:21Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17062820 | prizepicks | Trey McBride | Rec Yards | under | 0.06498754344887514 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17208893 | prizepicks | Cade Otton | Rec Targets | under | 0.06396227145584843 | 2026-11-20T07:05:43Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17172930 | prizepicks | Parker Washington | Rec Targets | under | 0.0633590315023902 | 2026-11-19T12:57:27Z | 2026-11-22T16:25:00.000-05:00 |
| prizepicks|17248593 | prizepicks | Carnell Tate | Recs | under | 0.06293821087167073 | 2026-11-21T01:31:21Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17061832 | prizepicks | Jared Goff | Rush Yards | over | 0.060379424163094386 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17172886 | prizepicks | Rashod Bateman | Rec Targets | under | 0.05903617850266274 | 2026-11-19T12:57:27Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17061958 | prizepicks | Javonte Williams | Rush Yards | under | 0.05867691672271225 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17062828 | prizepicks | George Pickens | Rec Yards | under | 0.057941658909858806 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17164365 | prizepicks | Derrick Henry | Rush TDs | over | 0.055743913320280725 | 2026-11-21T01:31:21Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17172916 | prizepicks | Evan Engram | Rec Targets | under | 0.055149375824596114 | 2026-11-19T12:57:27Z | 2026-11-22T16:25:00.000-05:00 |
| prizepicks|17172882 | prizepicks | Trey McBride | Rec Targets | under | 0.05110290304981535 | 2026-11-19T12:57:27Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17248818 | prizepicks | Garrett Wilson | Rec Targets | under | 0.0483168914265828 | 2026-11-21T01:31:21Z | 2026-11-22T16:05:00.000-05:00 |
| prizepicks|17062838 | prizepicks | Ja'Marr Chase | Rec Yards | under | 0.04762708868780563 | 2026-11-17T13:14:06Z | 2026-11-23T20:15:00.000-05:00 |
| prizepicks|17248601 | prizepicks | Emeka Egbuka | Recs | under | 0.04762545486751779 | 2026-11-21T01:31:21Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17248595 | prizepicks | Emmett Johnson | Recs | under | 0.047411245235581934 | 2026-11-21T01:31:21Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17061833 | prizepicks | Bryce Young | Rush Yards | under | 0.047291172718622376 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17279282 | prizepicks | Mike Evans | Rec Targets | under | 0.04711333969029463 | 2026-11-22T06:35:39Z | 2026-11-22T20:20:00.000-05:00 |
| prizepicks|17172897 | prizepicks | Colston Loveland | Rec Targets | under | 0.04606205650067807 | 2026-11-19T12:57:27Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17172900 | prizepicks | Luther Burden III | Rec Targets | under | 0.04402870912635659 | 2026-11-19T12:57:27Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17279281 | prizepicks | Deebo Samuel Sr. | Rec Targets | under | 0.04371063655666785 | 2026-11-22T06:35:39Z | 2026-11-22T20:20:00.000-05:00 |
| prizepicks|17172911 | prizepicks | CeeDee Lamb | Rec Targets | under | 0.04290639274739827 | 2026-11-19T12:57:27Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17173316 | prizepicks | Isaiah Likely | Rec Targets | under | 0.04213161314240221 | 2026-11-19T12:57:27Z | 2026-11-22T16:25:00.000-05:00 |
| prizepicks|17062822 | prizepicks | Chris Olave | Rec Yards | under | 0.04199283253040853 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17248602 | prizepicks | Kenny Gainwell | Recs | under | 0.040972667776200455 | 2026-11-21T01:31:21Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17245968 | prizepicks | Darnell Washington | Rec Targets | under | 0.03964044983398973 | 2026-11-21T01:31:21Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17062827 | prizepicks | CeeDee Lamb | Rec Yards | under | 0.0391841333439954 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17248591 | prizepicks | Mark Andrews | Recs | under | 0.039029007973070184 | 2026-11-21T01:31:21Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17248829 | prizepicks | Treylon Burks | Rec Targets | under | 0.03756172625102483 | 2026-11-21T01:31:21Z | 2026-11-23T20:15:00.000-05:00 |
| prizepicks|17172889 | prizepicks | DJ Moore | Rec Targets | under | 0.03600478749616709 | 2026-11-19T12:57:27Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17188713 | prizepicks | T.J. Hockenson | Recs | under | 0.035792831884043586 | 2026-11-22T06:35:39Z | 2026-11-22T20:20:00.000-05:00 |
| prizepicks|17172922 | prizepicks | Jameson Williams | Rec Targets | under | 0.03533413292464671 | 2026-11-19T12:57:27Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17172914 | prizepicks | Ryan Flournoy | Rec Targets | under | 0.03478762538563951 | 2026-11-19T12:57:27Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17061960 | prizepicks | Jahmyr Gibbs | Rush Yards | under | 0.034137148515200666 | 2026-11-17T13:14:06Z | 2026-11-22T13:00:00.000-05:00 |
| prizepicks|17062839 | prizepicks | Tee Higgins | Rec Yards | under | 0.03001893073314066 | 2026-11-17T13:14:06Z | 2026-11-23T20:15:00.000-05:00 |
