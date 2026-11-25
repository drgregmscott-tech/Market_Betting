# Pipeline Digest -- 2026-11-25T00:35:37Z

## Run summary
- Ingestion: 40427 rows (PrizePicks OK, Underdog OK)
- Estimation: 40427 rows estimated (from 40427 ingested props)
- CLV logging: 10 newly flagged, 0 newly closed, 70 still open (112425 total ever logged)

## Currently open flags
Sizing is a manual step (sizing_engine.py, Session 2.6) -- this table is what to scan to pick a pair worth sizing.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_edge | first_flagged_at | game_start_time |
|---|---|---|---|---|---|---|---|
| prizepicks|17376736 | prizepicks | Joe Milton III | Pass TDs | under | 0.35094246505677495 | 2026-11-24T14:47:41Z | 2026-11-26T16:30:00.000-05:00 |
| prizepicks|17371820 | prizepicks | Anthony Richardson Sr. | Pass Yards | under | 0.35094246505677495 | 2026-11-24T14:47:41Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17371806 | prizepicks | Anthony Richardson Sr. | Rush Yards | under | 0.35094246505677495 | 2026-11-24T14:47:41Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17446306 | prizepicks | Veronika Erjavec | Break Points Won | under | 0.35094246505677495 | 2026-11-25T00:43:43Z | 2026-11-25T13:00:00.000-05:00 |
| prizepicks|17433884 | prizepicks | Baker Mayfield | Pass+Rush+Rec TDs | under | 0.33619322591662215 | 2026-11-25T00:43:43Z | 2026-11-30T20:15:00.000-05:00 |
| prizepicks|17371817 | prizepicks | Michael Penix Jr. | Pass Yards | under | 0.3322469500724762 | 2026-11-24T14:47:41Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17371821 | prizepicks | Cam Ward | Pass Yards | under | 0.29940984744104104 | 2026-11-24T14:47:41Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17371831 | prizepicks | Baker Mayfield | Pass Yards | under | 0.2947317581520855 | 2026-11-24T14:47:41Z | 2026-11-30T20:15:00.000-05:00 |
| prizepicks|17439045 | prizepicks | Artur | Shots | under | 0.28061501019743784 | 2026-11-25T00:43:43Z | 2026-11-26T18:00:00.000-05:00 |
| prizepicks|17371829 | prizepicks | Fernando Mendoza | Pass Yards | under | 0.2803073369792758 | 2026-11-24T14:47:41Z | 2026-11-29T20:20:00.000-05:00 |
| prizepicks|17371818 | prizepicks | Kirk Cousins | Pass Yards | under | 0.27218101538958084 | 2026-11-24T14:47:41Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17433597 | prizepicks | Joe Burrow | Pass Yards | under | 0.2546774543055056 | 2026-11-25T00:43:43Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17371819 | prizepicks | J.J. McCarthy | Pass Yards | under | 0.2535386920183703 | 2026-11-24T14:47:41Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17371825 | prizepicks | Tyler Shough | Pass Yards | under | 0.25049427754286013 | 2026-11-24T14:47:41Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17374178 | prizepicks | Luke Schoonmaker | Rec Yards | over | 0.24709938862810488 | 2026-11-24T14:47:41Z | 2026-11-26T16:30:00.000-05:00 |
| prizepicks|17376733 | prizepicks | Caleb Williams | Pass TDs | under | 0.22618451942065032 | 2026-11-24T14:47:41Z | 2026-11-26T13:00:00.000-05:00 |
| prizepicks|17372159 | prizepicks | Emeka Egbuka | Rec Yards | under | 0.21162247730210237 | 2026-11-24T14:47:41Z | 2026-11-30T20:15:00.000-05:00 |
| prizepicks|17357057 | prizepicks | James Cook III | Rush TDs | over | 0.17860906817196054 | 2026-11-25T00:43:43Z | 2026-11-26T20:20:00.000-05:00 |
| prizepicks|17368909 | prizepicks | Savion Williams | Rec Targets | under | 0.17703587874794857 | 2026-11-24T14:47:41Z | 2026-11-25T20:00:00.000-05:00 |
| prizepicks|17372148 | prizepicks | Jordyn Tyson | Rec Yards | under | 0.17546756736578828 | 2026-11-24T14:47:41Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17446312 | prizepicks | Solana Sierra | Break Points Won | under | 0.15100392627850068 | 2026-11-25T00:43:43Z | 2026-11-25T16:00:00.000-05:00 |
| prizepicks|17374177 | prizepicks | Tyler Conklin | Rec Yards | over | 0.14453528870302534 | 2026-11-24T14:47:41Z | 2026-11-26T13:00:00.000-05:00 |
| prizepicks|17372744 | prizepicks | Konata Mumpfield | Recs | under | 0.14402648332567214 | 2026-11-24T14:47:41Z | 2026-11-25T20:00:00.000-05:00 |
| prizepicks|17374182 | prizepicks | Blake Whiteheart | Rec Yards | over | 0.13415129962029704 | 2026-11-24T14:47:41Z | 2026-11-29T20:20:00.000-05:00 |
| prizepicks|17374176 | prizepicks | Jonnu Smith | Rec Yards | over | 0.1317224516341905 | 2026-11-24T14:47:41Z | 2026-11-25T20:00:00.000-05:00 |
| prizepicks|17374179 | prizepicks | Jake Briningstool | Rec Yards | over | 0.12717407730455854 | 2026-11-24T14:47:41Z | 2026-11-26T20:20:00.000-05:00 |
| prizepicks|17372145 | prizepicks | Nico Collins | Rec Yards | under | 0.12214502875029642 | 2026-11-24T14:47:41Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17368911 | prizepicks | Rashee Rice | Rec Targets | under | 0.11367790298741587 | 2026-11-24T14:47:41Z | 2026-11-26T20:20:00.000-05:00 |
| prizepicks|17374492 | prizepicks | Hunter Luepke | Rush+Rec Yds | over | 0.11349189597497333 | 2026-11-24T14:47:41Z | 2026-11-26T16:30:00.000-05:00 |
| prizepicks|17435600 | prizepicks | Tristan Schoolkate | Break Points Won | under | 0.10423747051885313 | 2026-11-25T00:43:43Z | 2026-11-24T19:30:00.000-05:00 |
| prizepicks|17424869 | prizepicks | Caleb Williams | Fantasy Score | under | 0.09915000911388916 | 2026-11-25T00:43:43Z | 2026-11-26T13:00:00.000-05:00 |
| prizepicks|17372747 | prizepicks | Amon-Ra St. Brown | Recs | under | 0.09858384545439602 | 2026-11-24T14:47:41Z | 2026-11-26T13:00:00.000-05:00 |
| prizepicks|17211188 | prizepicks | Tucker Kraft | Rec Yards | under | 0.09637535679363307 | 2026-11-20T07:05:43Z | 2026-11-25T20:00:00.000-05:00 |
| prizepicks|17371814 | prizepicks | Fernando Mendoza | Rush Yards | under | 0.09433994398041257 | 2026-11-24T14:47:41Z | 2026-11-29T20:20:00.000-05:00 |
| prizepicks|17373288 | prizepicks | Amon-Ra St. Brown | Rec Targets | under | 0.09380535266091272 | 2026-11-24T14:47:41Z | 2026-11-26T13:00:00.000-05:00 |
| prizepicks|17372072 | prizepicks | Travis Etienne Jr. | Rush Yards | under | 0.09284275226526228 | 2026-11-24T14:47:41Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17374183 | prizepicks | Connor Heyward | Rush+Rec Yds | over | 0.09173826578691047 | 2026-11-24T14:47:41Z | 2026-11-29T20:20:00.000-05:00 |
| prizepicks|17372136 | prizepicks | T.J. Hockenson | Rec Yards | under | 0.08923767000655458 | 2026-11-24T14:47:41Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17372134 | prizepicks | Kyle Pitts Sr. | Rec Yards | under | 0.087793639145063 | 2026-11-24T14:47:41Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17368907 | prizepicks | Matthew Golden | Rec Targets | under | 0.08584953005925267 | 2026-11-24T14:47:41Z | 2026-11-25T20:00:00.000-05:00 |
| prizepicks|17372074 | prizepicks | Christian McCaffrey | Rush Yards | under | 0.08436808591439793 | 2026-11-24T14:47:41Z | 2026-11-29T16:25:00.000-05:00 |
| prizepicks|17372068 | prizepicks | Cam Skattebo | Rush Yards | under | 0.08073939241194372 | 2026-11-24T14:47:41Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17433599 | prizepicks | Ja'Marr Chase | Rec Yards | under | 0.0790595573316959 | 2026-11-25T00:43:43Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17374181 | prizepicks | Nate Adkins | Rec Yards | over | 0.07780241499840279 | 2026-11-24T14:47:41Z | 2026-11-27T15:00:00.000-05:00 |
| prizepicks|17368908 | prizepicks | Tucker Kraft | Rec Targets | under | 0.07313399044158142 | 2026-11-24T14:47:41Z | 2026-11-25T20:00:00.000-05:00 |
| prizepicks|17374180 | prizepicks | Keleki Latu | Rec Yards | over | 0.07300884938107377 | 2026-11-24T14:47:41Z | 2026-11-26T20:20:00.000-05:00 |
| prizepicks|17373284 | prizepicks | Luther Burden III | Rec Targets | under | 0.07209710110439815 | 2026-11-24T14:47:41Z | 2026-11-26T13:00:00.000-05:00 |
| prizepicks|17376734 | prizepicks | Jared Goff | Pass TDs | under | 0.06849850023648807 | 2026-11-24T14:47:41Z | 2026-11-26T13:00:00.000-05:00 |
| prizepicks|17372156 | prizepicks | KC Concepcion Jr. | Rec Yards | under | 0.06650304459863476 | 2026-11-24T14:47:41Z | 2026-11-29T20:20:00.000-05:00 |
| prizepicks|17435193 | prizepicks | Jaylen Waddle | Recs | under | 0.06530391369667332 | 2026-11-25T00:43:43Z | 2026-11-27T15:00:00.000-05:00 |
| prizepicks|17368916 | prizepicks | Tutu Atwell | Rec Targets | under | 0.06401471703420925 | 2026-11-24T14:47:41Z | 2026-11-25T20:00:00.000-05:00 |
| prizepicks|17372073 | prizepicks | Omarion Hampton | Rush Yards | under | 0.05826369784344709 | 2026-11-24T14:47:41Z | 2026-11-29T16:05:00.000-05:00 |
| prizepicks|17372746 | prizepicks | Luther Burden III | Recs | under | 0.05479051799806922 | 2026-11-24T14:47:41Z | 2026-11-26T13:00:00.000-05:00 |
| prizepicks|17372152 | prizepicks | Trey McBride | Rec Yards | under | 0.05443598118688209 | 2026-11-24T14:47:41Z | 2026-11-29T16:25:00.000-05:00 |
| prizepicks|17368891 | prizepicks | DJ Moore | Rec Targets | under | 0.0524800403243999 | 2026-11-24T14:47:41Z | 2026-11-26T20:20:00.000-05:00 |
| prizepicks|17368920 | prizepicks | Davis Allen | Rec Targets | under | 0.05227331479279318 | 2026-11-24T14:47:41Z | 2026-11-25T20:00:00.000-05:00 |
| prizepicks|17368905 | prizepicks | Pat Bryant | Rec Targets | under | 0.04785879407879767 | 2026-11-24T14:47:41Z | 2026-11-27T15:00:00.000-05:00 |
| prizepicks|17372154 | prizepicks | Denzel Boston | Rec Yards | under | 0.046147804038233264 | 2026-11-24T14:47:41Z | 2026-11-29T20:20:00.000-05:00 |
| prizepicks|17368915 | prizepicks | Colby Parkinson | Rec Targets | under | 0.04524925987526707 | 2026-11-24T14:47:41Z | 2026-11-25T20:00:00.000-05:00 |
| prizepicks|17372743 | prizepicks | Colby Parkinson | Recs | under | 0.04522350453487245 | 2026-11-24T14:47:41Z | 2026-11-25T20:00:00.000-05:00 |
| prizepicks|17373290 | prizepicks | Jahmyr Gibbs | Rec Targets | under | 0.04472872162225283 | 2026-11-24T14:47:41Z | 2026-11-26T13:00:00.000-05:00 |
| prizepicks|17372147 | prizepicks | Chris Olave | Rec Yards | under | 0.04392985951025752 | 2026-11-24T14:47:41Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17368921 | prizepicks | Tyler Higbee | Rec Targets | under | 0.04034320992524143 | 2026-11-24T14:47:41Z | 2026-11-25T20:00:00.000-05:00 |
| prizepicks|17375680 | prizepicks | DJ Moore | Rush Yards | over | 0.040094841349221144 | 2026-11-24T14:47:41Z | 2026-11-26T20:20:00.000-05:00 |
| prizepicks|17373291 | prizepicks | Jameson Williams | Rec Targets | under | 0.03888526726404218 | 2026-11-24T14:47:41Z | 2026-11-26T13:00:00.000-05:00 |
| prizepicks|17372137 | prizepicks | Malik Nabers | Rec Yards | under | 0.037999440713761046 | 2026-11-24T14:47:41Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17372748 | prizepicks | Sam LaPorta | Recs | under | 0.036857342929897396 | 2026-11-24T14:47:41Z | 2026-11-26T13:00:00.000-05:00 |
| prizepicks|17368901 | prizepicks | Jaylen Waddle | Rec Targets | under | 0.03559653356251935 | 2026-11-24T14:47:41Z | 2026-11-27T15:00:00.000-05:00 |
| prizepicks|17372071 | prizepicks | Derrick Henry | Rush Yards | under | 0.03362279798660894 | 2026-11-24T14:47:41Z | 2026-11-29T13:00:00.000-05:00 |
| prizepicks|17372153 | prizepicks | Brock Bowers | Rec Yards | under | 0.03333738253060603 | 2026-11-24T14:47:41Z | 2026-11-29T20:20:00.000-05:00 |
