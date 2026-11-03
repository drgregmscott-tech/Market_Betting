# Pipeline Digest -- 2026-11-03T11:51:44Z

## Run summary
- Ingestion: 22972 rows (PrizePicks OK, Underdog OK)
- Estimation: 22972 rows estimated (from 22972 ingested props)
- CLV logging: 88 newly flagged, 0 newly closed, 373 still open (107889 total ever logged)

## Currently open flags
Sizing is a manual step (sizing_engine.py, Session 2.6) -- this table is what to scan to pick a pair worth sizing.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_edge | first_flagged_at | game_start_time |
|---|---|---|---|---|---|---|---|
| underdog|46d87258-a353-4999-9cff-fd42341aa58c | underdog | Malik Willis | Pass Yards | under | 0.4 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|b343d3c5-a65e-4e28-a5f2-42058d73327d | underdog | Tanner McKee | Pass Yards | under | 0.4 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|9115261a-247e-4ae2-ab20-07224ee66937 | underdog | Josh Allen | Pass Yards | under | 0.4 | 2026-11-03T11:59:28Z | 2026-11-10T01:15:00Z |
| underdog|4a863902-d11a-4d1a-87cb-b706ca003cb8 | underdog | Josh Jacobs | Rush Yards | under | 0.4 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|86ab6380-a8a1-4dcd-8110-71c1e0bb6d45 | underdog | Olamide Zaccheaus | Receiving Yards | under | 0.4 | 2026-11-03T11:59:28Z | 2026-11-08T14:30:00Z |
| underdog|72f89744-f92a-449b-a0bb-cf8069d05cd8 | underdog | Jack Larsen | Receiving Yards | over | 0.4 | 2026-11-03T02:21:46Z | 2026-11-08T00:30:00Z |
| underdog|b52c7395-e7ee-4951-a4fd-43f9a6eedb90 | underdog | Dak Prescott | Pass Yards | under | 0.4 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|53fe70b7-afb1-4e62-a2f3-dd14caccc774 | underdog | Justin Herbert | Pass Yards | under | 0.4 | 2026-11-03T02:21:46Z | 2026-11-08T21:05:00Z |
| underdog|a07aac01-1d31-403d-9994-7e1aa59da29a | underdog | Trevor Lawrence | Pass Yards | under | 0.4 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|869349aa-5399-4c3f-b961-edd9aca6684e | underdog | Michael Penix | Pass Yards | under | 0.4 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|9ca444aa-fd64-4c0d-b983-eb0f7367c91e | underdog | Bo Nix | Pass Yards | under | 0.39779554925976657 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|694e9331-767a-42df-94e6-718404cad8fc | underdog | Kyler Murray | Pass Yards | under | 0.3877310591537684 | 2026-11-03T11:59:28Z | 2026-11-10T01:15:00Z |
| underdog|3b541bb0-6dda-479a-a907-c082e233ed4c | underdog | Tanner McKee | Pass Attempts | under | 0.38702227943265677 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|7eedc362-5891-4451-820d-93536c2bee6e | underdog | Dawson Knox | Receiving Yards | under | 0.3666926454678271 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|73c39bbf-e996-45c9-922f-f150cfd70060 | underdog | Ollie Gordon | Receiving Yards | under | 0.36183860489134134 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| prizepicks|16557936 | prizepicks | Dak Prescott | Pass Yards | under | 0.35094246505677495 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| prizepicks|16557938 | prizepicks | Justin Herbert | Pass Yards | under | 0.35094246505677495 | 2026-11-03T02:21:46Z | 2026-11-08T16:05:00.000-05:00 |
| prizepicks|16557929 | prizepicks | Bo Nix | Pass Yards | under | 0.35094246505677495 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| prizepicks|16557925 | prizepicks | Tanner McKee | Pass Yards | under | 0.35094246505677495 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| prizepicks|16557927 | prizepicks | Malik Willis | Pass Yards | under | 0.35094246505677495 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| prizepicks|16577043 | prizepicks | Stefon Diggs | Rec Yards | under | 0.35094246505677495 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| prizepicks|16557944 | prizepicks | Josh Allen | Pass Yards | under | 0.35094246505677495 | 2026-11-03T02:21:46Z | 2026-11-09T20:15:00.000-05:00 |
| prizepicks|16557940 | prizepicks | Brock Purdy | Pass Yards | under | 0.35094246505677495 | 2026-11-03T02:21:46Z | 2026-11-08T16:25:00.000-05:00 |
| prizepicks|16557943 | prizepicks | Baker Mayfield | Pass Yards | under | 0.34786953020441724 | 2026-11-03T02:21:46Z | 2026-11-08T20:20:00.000-05:00 |
| underdog|1a23b189-2c6e-49d5-a334-b9b71be06e3d | underdog | Jordan Love | Pass Yards | under | 0.3439276315737799 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|ccf6b612-28dd-444f-9b72-2ec8c5cafef7 | underdog | Deshaun Watson | Pass Yards | under | 0.33983627444145803 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|d3d67fd6-1e23-402d-9e23-43cbc35a2f8c | underdog | Josh Allen | Pass Attempts | under | 0.33795668909357257 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| prizepicks|16557935 | prizepicks | Jayden Daniels | Pass Yards | under | 0.3359949609424918 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|f196ff34-8cc3-496c-a352-6384f3c46102 | underdog | Patrick Mahomes | Pass Yards | under | 0.3313155331357345 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| prizepicks|16557945 | prizepicks | Kyler Murray | Pass Yards | under | 0.32685614816516073 | 2026-11-03T02:21:46Z | 2026-11-09T20:15:00.000-05:00 |
| underdog|fa35b61f-7cc4-4f4b-9185-6e6a5167ad20 | underdog | Michael Penix | Pass Attempts | under | 0.3245304925645227 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|443acad6-170c-4ba9-941f-010152d0078c | underdog | Jared Goff | Pass Yards | under | 0.3209086296504421 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|851c01c3-f216-4ca4-a7c3-a849bbbdeb8d | underdog | Jahan Dotson | Receptions | under | 0.3194165460499485 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|c180ec24-04be-4d76-92bd-f2b1a7387ad4 | underdog | Josh Jacobs | Receptions | under | 0.3138562329893375 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|c5c6faa1-e8d5-47f3-ad9e-9b7573bca761 | underdog | Bo Nix | Pass Attempts | under | 0.31377812931007676 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|9a750cb7-700f-436f-9538-1ce6918d995a | underdog | Deshaun Watson | Pass Attempts | under | 0.3135328194560545 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|cbf0d149-d120-49d4-b8d9-6df900ee39de | underdog | Bryce Young | Pass Yards | under | 0.31348509126095614 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|3720fd10-47a9-4f6b-9494-df98a36c299d | underdog | Drake Maye | Pass Yards | under | 0.3104863109077214 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|fc53216f-8950-4687-9389-255981bfe3e3 | underdog | J.J. McCarthy | Pass Yards | under | 0.3094939656727945 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| prizepicks|16557939 | prizepicks | Kirk Cousins | Pass Yards | under | 0.3094515764679242 | 2026-11-03T02:21:46Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|aeba1606-29dc-42b1-9656-1380a668a06e | underdog | Justin Herbert | Pass Attempts | under | 0.2990676223610106 | 2026-11-03T11:59:28Z | 2026-11-08T21:05:00Z |
| underdog|7acd79f8-9e86-4f32-962c-1a82d0263eae | underdog | Malik Willis | Pass Attempts | under | 0.29807427067794556 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|cac0e559-74a5-448a-a3b7-221223acb5dc | underdog | Tyler Shough | Pass Yards | under | 0.29263132852775464 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| prizepicks|16557932 | prizepicks | Geno Smith | Pass Yards | under | 0.2900076533834668 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|a4f7e2ea-445a-4746-9a01-bb8681efb55d | underdog | Drake Maye | Pass Attempts | under | 0.2890709907617405 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|b1871eee-1be7-4d3b-b76e-1f9f7f70baca | underdog | J.J. McCarthy | Pass TDs | under | 0.2875734861947701 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|de09d226-640d-4e88-92bd-dfffde819245 | underdog | C.J. Stroud | Pass Yards | under | 0.28615234252036514 | 2026-11-03T11:59:28Z | 2026-11-08T21:05:00Z |
| underdog|13693c77-71a5-4911-85ec-522b3e1bee88 | underdog | Chase Brown | Rush + Rec Yards | under | 0.2799252854646834 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|47489557-ed6c-4a10-9589-5fa0d20aebc7 | underdog | Joe Burrow | Pass Yards | under | 0.27909410307333227 | 2026-11-03T11:59:28Z | 2026-11-08T14:30:00Z |
| underdog|034db5e8-e2a4-4f3a-b113-160fa7977d4f | underdog | Jake Elliott | FG Made | under | 0.27609595620105687 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|7791482e-083e-4c1c-a690-c0aab4962cd4 | underdog | Courtland Sutton | Receiving Yards | under | 0.2751386803940128 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|ab7d6a69-7520-4194-bb53-8478f9ad4866 | underdog | Geno Smith | Pass Yards | under | 0.2737068829684248 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| prizepicks|16557930 | prizepicks | Deshaun Watson | Pass Yards | under | 0.26980869531882257 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|5a0ff8aa-ab28-4f6c-9ec5-e95c971f8458 | underdog | Andy Borregales | Kicking Points | under | 0.2640899467628497 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| prizepicks|16557924 | prizepicks | J.J. McCarthy | Pass Yards | under | 0.2619885947590418 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|d484d774-fbd8-467b-bbfa-b6f85cfcf83f | underdog | Courtland Sutton | Receptions | under | 0.25834377385355134 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|a5d8af7b-ec41-4296-ae4d-19f0d58f11e6 | underdog | Geno Smith | Pass Attempts | under | 0.2582445722188248 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| prizepicks|16557928 | prizepicks | Bryce Young | Pass Yards | under | 0.25782403523201924 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| prizepicks|16557933 | prizepicks | Patrick Mahomes | Pass Yards | under | 0.256531424485161 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|2e6395f2-6b10-41e0-bb9d-05b1def655e4 | underdog | Tanner McKee | Pass TDs | under | 0.25424608115904224 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|b72f06e1-815c-4c36-b978-4fcc8dfeeef1 | underdog | Andy Borregales | FG Made | under | 0.25213168723502966 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|b0acc6d8-af77-4a6d-b9eb-733cc7eaa8ca | underdog | Kyle Pitts | Receiving Yards | under | 0.24876685205852123 | 2026-11-03T11:59:28Z | 2026-11-08T14:30:00Z |
| prizepicks|16577042 | prizepicks | Puka Nacua | Rec Yards | under | 0.24801878589627235 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|c743d944-5b59-4fcc-8a1d-ec5ba444e562 | underdog | Jaylen Wright | Rush + Rec Yards | under | 0.239068644264523 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|7363a42c-3847-408e-a571-1c08fe3b2cf8 | underdog | J.J. McCarthy | Pass Attempts | under | 0.23728517572363184 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|20a27a8d-6bfe-4d21-a0d6-47e5c998b308 | underdog | Bryce Young | Pass Attempts | under | 0.23552865307819393 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|4e219bc4-540f-4254-8899-fb2c0a6c9ef1 | underdog | Jordan Love | Pass Attempts | under | 0.23509904882189492 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| prizepicks|16557934 | prizepicks | Matthew Stafford | Pass Yards | under | 0.23485070755351956 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|bba3c903-4ede-426b-98a4-5c60cb6bed88 | underdog | Jonah Coleman | Rush Yards | under | 0.233288763818978 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|795e26e5-5e3d-4ef7-a7e2-9b57067a7815 | underdog | Jaylen Wright | Rush Yards | under | 0.23202348740139422 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|1080b2cb-f33c-4f63-b95e-c4c81bdc6edd | underdog | Devaughn Vele | Receiving Yards | under | 0.23125785463944104 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|302cdcd3-7c43-4099-94f3-7f5a9272e438 | underdog | Jake Weinberg | XP Made | over | 0.23037328315622718 | 2026-11-03T02:21:46Z | 2026-11-08T00:30:00Z |
| underdog|60cbaa38-c568-4879-a6f8-94b6e4e69559 | underdog | Tucker Kraft | Receiving Yards | under | 0.22559324997910668 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|4eb90e37-0394-4c4c-8d2e-e31385ee2cfb | underdog | Patrick Mahomes | Pass Attempts | under | 0.22176745268767095 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|da210a50-3071-4e2c-adcb-afd5d0cf32dd | underdog | Cam Little | FG Made | under | 0.22067313990849302 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|662e7f18-782c-47f5-b0f3-20dce9028abf | underdog | Kyler Murray | Pass Attempts | under | 0.21913394627361626 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|b1b292ca-18cf-40bc-bd9f-e12fefdf9774 | underdog | Josh Jacobs | Rush + Rec Yards | under | 0.2185373608497626 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|3d11ff54-e68e-46fd-9bee-9f64e201a532 | underdog | Ladd McConkey | Receptions | under | 0.2182531395719538 | 2026-11-03T02:21:46Z | 2026-11-08T21:05:00Z |
| prizepicks|16557922 | prizepicks | Joe Burrow | Pass Yards | under | 0.2181379417292847 | 2026-11-03T02:21:46Z | 2026-11-08T09:30:00.000-05:00 |
| underdog|bb01a810-46d8-4752-866c-0052c1f4e20d | underdog | Justin Herbert | Pass TDs | under | 0.20993615337654958 | 2026-11-03T02:21:46Z | 2026-11-08T21:05:00Z |
| prizepicks|16577049 | prizepicks | Trey McBride | Rec Yards | under | 0.20935259101009185 | 2026-11-03T02:21:46Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|03213d6b-9ff4-4b08-8ab9-3ecd87dfe78f | underdog | Dak Prescott | Pass TDs | under | 0.2061162118075327 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| prizepicks|16577051 | prizepicks | Brock Bowers | Rec Yards | under | 0.19828126826604298 | 2026-11-03T02:21:46Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|90cecaf5-d459-433e-b301-94163ffec93e | underdog | Joe Burrow | Pass Attempts | under | 0.19748546886911345 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|fd73053c-c0f9-4bea-b66c-20ede4728695 | underdog | Rashee Rice | Receiving Yards | under | 0.1966277935664762 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|f9beee99-bf11-4d3d-8d93-9a1099560025 | underdog | James Cook | Receptions | under | 0.19213415801783407 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|4d49f60c-e264-4756-8301-a0888a80b80f | underdog | Patrick Mahomes | Pass TDs | under | 0.19093001677595678 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|65ce174a-1c8b-49d3-82f3-393686c6422c | underdog | Malik Washington | Receiving Yards | under | 0.18885937610779013 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|872eac2a-4e79-4367-a987-6a15c41a88dc | underdog | Kyle Pitts | Receptions | under | 0.1884927972756335 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|bf90486c-95b3-42f7-a1e0-b5f3e4e5d56a | underdog | Trevor Lawrence | Pass Attempts | under | 0.18495496158550828 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|bf1e2d87-2476-48f1-8f57-5993442a580d | underdog | Chuba Hubbard | Rush + Rec Yards | under | 0.18312722082807886 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|293a9074-3245-40ed-acbe-ab687921f3f3 | underdog | Bhayshul Tuten | Rush Yards | under | 0.181890192392258 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|60b87c07-2cae-46b9-8a7c-d2f711bdcddf | underdog | Ollie Gordon | Rush + Rec Yards | under | 0.18185508779425652 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|e218a11c-9086-4de7-9478-faae2805f52c | underdog | Jonah Coleman | Rush + Rec Yards | under | 0.17822581983705676 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|2f911baa-b813-435c-9dd7-2d924671a17c | underdog | Ja'Marr Chase | Receiving Yards | under | 0.17727145964551094 | 2026-11-03T11:59:28Z | 2026-11-08T14:30:00Z |
| underdog|a1310588-918d-4510-86a7-bd4a239fec69 | underdog | C.J. Stroud | Pass Attempts | under | 0.17725867468837075 | 2026-11-03T02:21:46Z | 2026-11-08T21:05:00Z |
| underdog|9100eaf4-8232-4056-8f1f-336a475cc678 | underdog | Rhamondre Stevenson | Rush Yards | under | 0.17609187646102753 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|a2ee3b2c-3a41-4508-ad81-1d0ca5c6f707 | underdog | Jared Goff | Pass Attempts | under | 0.17494980056194276 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|58473198-16c0-4f1f-98ce-794fe0d452fd | underdog | Rashee Rice | Receptions | under | 0.17383563925443812 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|fdc20714-2850-4478-a9ae-058d3a14ba1b | underdog | Jake Elliott | Kicking Points | under | 0.1717042647640432 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|72118ad8-505e-46b9-bf85-bcdfe4d1c4fa | underdog | Javonte Williams | Rush + Rec Yards | under | 0.17137554153322443 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|5294f95e-70ef-47dd-8cdf-91081da98280 | underdog | Kyler Murray | Pass TDs | under | 0.17036826288931617 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|a2c32829-5741-4600-bdac-f990a7052b23 | underdog | Rhamondre Stevenson | Rush + Rec Yards | under | 0.1684921629314633 | 2026-11-03T11:59:28Z | 2026-11-08T21:25:00Z |
| underdog|c81c430d-1ad6-4eb4-b890-71c907c1c75b | underdog | Nico Collins | Receiving Yards | under | 0.16822736987760967 | 2026-11-03T02:21:46Z | 2026-11-08T21:05:00Z |
| underdog|a8a9bed2-5d3a-4afa-b7f7-de3a2c658f75 | underdog | Jared Goff | Rush Yards | over | 0.1677182366005825 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|cf74ea13-4c83-486b-a699-efa71530a041 | underdog | Amon-Ra St. Brown | Receptions | under | 0.16742438992001507 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|6630eef7-0476-4c1a-a41a-970cbeef97d4 | underdog | Amon-Ra St. Brown | Receiving Yards | under | 0.16310454928625107 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|9ff29ccb-f4c3-4664-9330-39133772a9f1 | underdog | Tucker Kraft | Receptions | under | 0.1615364063191952 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|528a645e-8439-47f6-91f3-89566cf92574 | underdog | Greg Dulcich | Receptions | under | 0.15981895291377868 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|7d8aca5c-098a-4cd2-ac18-2986be8ea813 | underdog | Matthew Golden | Receptions | under | 0.15935064858874126 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|8d971c6a-aba4-499d-98e1-0611d04325c1 | underdog | Chris Rodriguez | Receiving Yards | over | 0.1589915127531274 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|de6281e6-e72c-4f7d-9b19-ea93df015060 | underdog | Drake London | Receptions | under | 0.1588244841998091 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|13a0f632-2376-465f-909f-036cd0269375 | underdog | Chase Brown | Rush Yards | under | 0.158724054234063 | 2026-11-03T11:59:28Z | 2026-11-08T14:30:00Z |
| underdog|37b70014-c646-417c-9dda-4626c7ea528a | underdog | Tyler Shough | Pass Attempts | under | 0.15655653928608748 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|0b592d73-46b4-4456-918c-8d00242be932 | underdog | Dawson Knox | Receptions | under | 0.15649493040707285 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|28aa1264-fc74-4c1c-9f5a-0f2b5396c62e | underdog | Garrett Wilson | Receiving Yards | under | 0.15645468065321244 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|95510857-490c-405c-b41d-020672de0828 | underdog | Nico Collins | Receptions | under | 0.1546467813222513 | 2026-11-03T02:21:46Z | 2026-11-08T21:05:00Z |
| prizepicks|16577045 | prizepicks | Antonio Williams | Rec Yards | under | 0.15279763651234368 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|b0ce99d7-ccca-47c0-a454-e6f920eab8e2 | underdog | Bo Nix | Pass TDs | under | 0.14921921703126695 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|78f69cb1-b2ea-4410-853d-44094574eb64 | underdog | Parker Washington | Receiving Yards | under | 0.1490737198822808 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|73c50709-0cdb-4743-8e4e-1d490c5adec8 | underdog | Duncan Brune | Rush Yards | under | 0.14811690497856356 | 2026-11-03T11:59:28Z | 2026-11-04T00:00:00Z |
| underdog|c4587fdc-fe2d-47dc-997d-d0b08663b00a | underdog | Ka'imi Fairbairn | FG Made | under | 0.1479318682678138 | 2026-11-03T02:21:46Z | 2026-11-08T21:05:00Z |
| underdog|1b370830-3867-4ade-9a8d-418a06dbd1c1 | underdog | Christian Watson | Receptions | under | 0.1479168165648339 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|d204e0bd-cd91-4817-9c35-69876cf608f9 | underdog | Tyler Goodson | Rush + Rec Yards | under | 0.14661488441558534 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|b7643678-a5f1-4389-8abd-57e6a13920ae | underdog | Jaylen Waddle | Receptions | under | 0.1458868002155338 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|b739a15f-4dfa-4f63-9c1f-ddf4d1cc6dbb | underdog | Cam Skattebo | Rush + Rec Yards | under | 0.14574273316819908 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|27b32f6d-4d30-4750-8096-b0dc4daa3f52 | underdog | Matthew Golden | Receiving Yards | under | 0.14263761923795182 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| prizepicks|16558454 | prizepicks | Ignacio Buse | Total Games Won | over | 0.14014082984014242 | 2026-11-03T02:21:46Z | 2026-11-04T05:00:00.000-05:00 |
| underdog|e1775404-5113-460c-9eec-b13c0226b55b | underdog | Olamide Zaccheaus | Receptions | under | 0.1396223249639138 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|f31a1e8b-9aa9-4022-b468-859f852768cb | underdog | Devaughn Vele | Receptions | under | 0.13901253046609652 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|3c114bc2-839b-4e55-9ec0-5de96e8522a9 | underdog | Caleb Douglas | Receptions | under | 0.1384724673367177 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|a27717e2-b673-40e8-95cc-89ea0eae37ba | underdog | Deshaun Watson | Pass TDs | under | 0.13610875973967107 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|5790a889-8601-4824-ac78-b9c766ba1891 | underdog | Marvin Mims Jr. | Receptions | under | 0.13357422686133513 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|a9423304-185a-456f-aa8a-e12bb9b1b579 | underdog | Jakobi Meyers | Receiving Yards | under | 0.13343229218485075 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|5e40b255-1407-4830-b514-7e459361a46c | underdog | Quinshon Judkins | Rush + Rec Yards | under | 0.13131976775142173 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|6a4ea7ca-8051-400b-a435-f94e0a7067ee | underdog | Jameson Williams | Receiving Yards | under | 0.131077359753479 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|f7a6d60f-c6be-4a0c-a284-fa515f45685d | underdog | Magda Linette | Double Faults | under | 0.13067143321143349 | 2026-11-03T02:21:46Z | 2026-11-03T10:10:00Z |
| underdog|c2ddeb9f-7361-42cc-9e8d-96707debdc6f | underdog | Jahmyr Gibbs | Rush + Rec Yards | under | 0.12990836667624628 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|49dfd4ee-dd3e-46c0-b47e-4a77a2cd1893 | underdog | Cam Little | Kicking Points | under | 0.12899634811527072 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|3959eb98-8af8-4021-99d6-2d65c85b315c | underdog | Dak Prescott | Pass Attempts | under | 0.12713717008438152 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|c6421db7-4444-410f-bcf6-c6f880161f15 | underdog | Ollie Gordon | Rush Yards | under | 0.12693712025019466 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|aa5f8dd6-ca45-4e71-a789-592ff9da84c5 | underdog | Travis Kelce | Receiving Yards | under | 0.12665701332300316 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|5b5258bd-8a25-4c68-8c0a-784ed100f265 | underdog | Jordan Gant | Receiving Yards | over | 0.12634514299388655 | 2026-11-03T11:59:28Z | 2026-11-04T00:00:00Z |
| underdog|f5c38bf0-85ac-4489-b4e7-b51f3c72ffc9 | underdog | Javonte Williams | Receiving Yards | under | 0.12591828129631966 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|e23ce818-a3b4-4638-a29b-c8357eb981eb | underdog | Isaiah Likely | Receiving Yards | under | 0.1253831860396818 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| prizepicks|16577041 | prizepicks | Garrett Wilson | Rec Yards | under | 0.12215435750439496 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|06a98b20-5b6a-4641-963b-748d6b6ac027 | underdog | Ja'Marr Chase | Receptions | under | 0.12198379656106328 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|e0185cca-1a27-4e8e-8859-8afaabde877b | underdog | Spencer Porath | FG Made | over | 0.12185258966611756 | 2026-11-03T02:21:46Z | 2026-11-08T00:30:00Z |
| prizepicks|16537744 | prizepicks | Despina Papamichail | Total Games Won | over | 0.121762089081205 | 2026-11-03T02:21:46Z | 2026-11-03T12:10:00.000-05:00 |
| underdog|b9ef35c4-c26d-41a0-a631-083433e4878f | underdog | Jalen Coker | Receptions | under | 0.12166598689815067 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|247b1df6-4f80-4eed-ae74-bfcc7582ec7a | underdog | Bhayshul Tuten | Receptions | under | 0.12077038979546606 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|94fc7a75-ac49-46e5-aa74-e6a67b1bd62c | underdog | Tyler Goodson | Rush Yards | under | 0.11960752661139407 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| prizepicks|16576409 | prizepicks | Christian McCaffrey | Rush Yards | under | 0.11950744181162642 | 2026-11-03T02:21:46Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|c7bb0bb6-dc60-4c38-93e2-684dacb04b02 | underdog | Josh Allen | Pass TDs | under | 0.11926653211048077 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|f125b760-3701-4fd9-bc3e-022046ab9f1e | underdog | Drake London | Receiving Yards | under | 0.11863450575767398 | 2026-11-03T11:59:28Z | 2026-11-08T14:30:00Z |
| underdog|37e33f92-e74e-411f-ad69-62dfb21c5326 | underdog | Javonte Williams | Rush Yards | under | 0.11819553258465965 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|1c07119d-7fe4-4eba-b8f2-c7008e344979 | underdog | Harold Fannin | Receptions | under | 0.11801150156707052 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|eccd30c3-ed5b-4cc6-aad4-06299d22c529 | underdog | Malik Nabers | Receptions | under | 0.11783962166306128 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|1a302e32-ea50-4ad7-9fcd-27c67675614e | underdog | Josh Cameron | Receptions | under | 0.1176734146378754 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|b55f6d8a-558a-467f-b5c1-6f4835859648 | underdog | Ollie Gordon | Receptions | under | 0.11678261482630548 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|649d4cf3-3d96-4754-b6ba-149b97bba842 | underdog | Kenneth Walker III | Receptions | under | 0.11559688528805712 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|df8cc29e-c9c7-46e3-9773-066f25acc7a6 | underdog | CeeDee Lamb | Receptions | under | 0.11512462845971994 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|0d64e017-b859-433b-8b93-491525d6f2eb | underdog | Bhayshul Tuten | Rush + Rec Yards | under | 0.11408094268080893 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|8dda3f2c-43bd-496a-91aa-283c7a072e7b | underdog | Chuba Hubbard | Receptions | under | 0.11351803648802827 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|980ef0c9-e7c6-40c1-ae91-d71c59322e06 | underdog | Travis Kelce | Receptions | under | 0.11333613992057967 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|c3c0340b-5595-4605-a838-cdd48f0e3545 | underdog | Chris Olave | Receiving Yards | under | 0.11329346880000801 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| prizepicks|16557903 | prizepicks | Bryce Young | Rush Yards | under | 0.11312986015089133 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| prizepicks|16577048 | prizepicks | George Pickens | Rec Yards | under | 0.11245540278204647 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|b60bc42b-b33b-44fb-9a56-1e3746ac0210 | underdog | Brayden Roggow | Pass TDs | under | 0.11244007240740739 | 2026-11-03T11:59:28Z | 2026-11-04T00:00:00Z |
| underdog|e14b44d7-6880-4cde-a5d0-be585bd64366 | underdog | Denzel Boston | Receptions | under | 0.11215354306007119 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|778014fa-0b1d-4120-8eac-121c9d4e8db4 | underdog | Jalen Royals | Receiving Yards | over | 0.11116256315833206 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|3538ac55-6662-42cf-861c-d0f0d77e4816 | underdog | Denzel Boston | Receiving Yards | under | 0.11068740648518105 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|1fecccd3-7915-4b3d-9923-95b353ee0c90 | underdog | J.K. Dobbins | Receptions | under | 0.11024990718515137 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|a54f26bd-e573-47dd-bafe-bc24be27d76e | underdog | Claire Liu | Double Faults | under | 0.10963497817462542 | 2026-11-03T11:59:28Z | 2026-11-04T07:10:00Z |
| underdog|57815146-a656-43d6-9668-35d136e67d23 | underdog | Devon Dampier | Pass Yards | under | 0.10960047075501667 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|69a82857-d297-4b15-a385-2a023ebcf054 | underdog | Dalton Kincaid | Receptions | under | 0.10948029145485216 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|ba47c124-db10-4b69-b5cf-5ba62f5c4d37 | underdog | Jahmyr Gibbs | Receptions | under | 0.10946590257471323 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|a614e89c-f4b2-4fa3-aea8-25fba31e38bc | underdog | Bijan Robinson | Rush Yards | under | 0.10926567089440631 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|1c8b629e-7699-49b7-9618-d25dbf35d4f9 | underdog | Nick Poulos | Pass Yards | under | 0.10826262564897982 | 2026-11-03T11:59:28Z | 2026-11-04T00:00:00Z |
| underdog|ac95f7ce-5d00-4bb6-8a40-e18fda6f308c | underdog | Bijan Robinson | Rush + Rec Yards | under | 0.10805644555943927 | 2026-11-03T11:59:28Z | 2026-11-08T14:30:00Z |
| underdog|0c245092-8866-4e55-b3d5-f3c0bcce5a54 | underdog | Noah Fifita | Pass Yards | under | 0.1075217402806683 | 2026-11-03T11:59:28Z | 2026-11-07T03:15:00Z |
| underdog|fea7ee2e-73b1-4ba4-878b-0a6c68f8d431 | underdog | Chris Bell | Receptions | under | 0.10732281232729646 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|1eb3d420-163f-4f53-9c3b-935932e16df9 | underdog | Ladd McConkey | Receiving Yards | under | 0.10712402164602675 | 2026-11-03T02:21:46Z | 2026-11-08T21:05:00Z |
| underdog|1b7021b4-b333-4256-bc1e-7c9f88464431 | underdog | Jonah Coleman | Receptions | under | 0.10693828108030978 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|e035af2c-3907-4779-ab21-f9829c14e425 | underdog | CeeDee Lamb | Receiving Yards | under | 0.10542105871246699 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|aa2414f6-9b31-4532-b1cb-045d89a12d45 | underdog | Adonai Mitchell | Receptions | under | 0.10517197384243948 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|25b6438e-fd3e-419a-b15c-3fa732828d67 | underdog | Jahmyr Gibbs | Rush Yards | under | 0.10460455615674824 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|3dd97269-7090-4494-b0ba-aef942cacee8 | underdog | Jared Goff | Pass TDs | under | 0.10432511994565019 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|4a328574-9067-45a3-b2c8-168d822b5e16 | underdog | T.J. Hockenson | Receiving Yards | under | 0.10407541804729603 | 2026-11-03T11:59:28Z | 2026-11-10T01:15:00Z |
| prizepicks|16577039 | prizepicks | Rashee Rice | Rec Yards | under | 0.10318750310261049 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|a69c7259-5cc4-4207-8a64-47ec96c6c5b0 | underdog | Jaylen Waddle | Receiving Yards | under | 0.10317750601720066 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|fdb43e68-4917-450f-8dc2-f6ae9972edee | underdog | Quinshon Judkins | Rush Yards | under | 0.10256176001471462 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|c4b8e03b-86f2-4d6c-b024-04caa813ed63 | underdog | Andre Szmyt | FG Made | under | 0.10236818666743885 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|c31081a6-c8f1-4e82-af45-590d8aa34b39 | underdog | Greg Dulcich | Receiving Yards | under | 0.1023319243442552 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|d9d08697-3dd2-4d24-bc73-42297b125227 | underdog | Jameson Williams | Receptions | under | 0.10208410937911938 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|7bf309d3-cb09-4113-b642-82526d074215 | underdog | Christian Watson | Receiving Yards | under | 0.10173017572558107 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|f4bba20a-76ec-4df5-9de0-3c7c20bd1a76 | underdog | Keon Coleman | Receptions | under | 0.10169343136994924 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|b5d747fa-73cd-4acb-88a8-538cb0bc7051 | underdog | Jordan Addison | Receiving Yards | under | 0.098653067032206 | 2026-11-03T11:59:28Z | 2026-11-10T01:15:00Z |
| underdog|be48005a-e911-48a5-89d3-0071ee0d1592 | underdog | Devon Dampier | Pass TDs | over | 0.09858639656620943 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|24324e94-375f-47e6-81b8-1367b471a178 | underdog | Juwan Johnson | Receptions | under | 0.09851839400207829 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|66168ee0-2f6e-45af-939a-9b1a407399d0 | underdog | Cam Skattebo | Rush Yards | under | 0.09724141723929802 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|d0d98a61-131b-421d-a06f-55b85065ec52 | underdog | Jonah Coleman | Receiving Yards | under | 0.09720873998836776 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|dd95402c-e9ca-44e5-a5a3-179e2734707c | underdog | Jordan Addison | Receptions | under | 0.09707338503094809 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|28bf8588-d36c-4307-89a2-c8474a1e72d5 | underdog | KC Concepcion | Receiving Yards | under | 0.09674254879120081 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|2bac7b08-fac7-40ce-8ab4-52eed070b62a | underdog | Jordan Love | Pass TDs | under | 0.0961519218860859 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|70b674bf-14ef-4526-b90e-42cba3c6d3a5 | underdog | Adam Trautman | Receptions | under | 0.09545112973787573 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|a908f7df-e2eb-4cc0-97d1-8641fe7b1a4f | underdog | Brayden Roggow | Pass Yards | under | 0.09540432984442637 | 2026-11-03T11:59:28Z | 2026-11-04T00:00:00Z |
| underdog|a5eb6366-cd82-4d6b-bd95-f5e0ede614e0 | underdog | Ka'imi Fairbairn | Kicking Points | under | 0.09495465902987144 | 2026-11-03T02:21:46Z | 2026-11-08T21:05:00Z |
| underdog|e6a6d9c4-cede-4db1-8127-fadccb0830a1 | underdog | Parker Washington | Receptions | under | 0.09473178992722764 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|416669b4-69d5-46be-ab92-479de3a87805 | underdog | James Cook | Rush + Rec Yards | under | 0.09431259142927861 | 2026-11-03T11:59:28Z | 2026-11-10T01:15:00Z |
| underdog|c578d8d7-01f0-4d79-9d4f-3b0725511b5a | underdog | Legend Glasker | Receptions | under | 0.0939339008632083 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|b57be690-f19d-4c93-9059-74db24fa851c | underdog | Derrick Henry | Rush Yards | under | 0.09317962638787114 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|c8ccca2b-13b2-403a-bb00-b6f2284f88e4 | underdog | Kenneth Walker III | Rush + Rec Yards | under | 0.09278676109466322 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|7cee03ac-78b3-4d7b-9754-834e5953a2f4 | underdog | Bryce Young | Rush Yards | under | 0.09215881426223937 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|9017c9d1-d4b6-4f91-be05-cd89711e572a | underdog | Derrick Henry | Rush + Rec Yards | under | 0.09211628908550895 | 2026-11-03T11:59:28Z | 2026-11-06T01:15:00Z |
| underdog|202e5494-d855-4806-80a0-ba10825ed719 | underdog | Chris Rodriguez | Rush Yards | under | 0.09160429923596058 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|ae5bbb4e-2e0c-43fc-887c-2641f8e8a38f | underdog | Malik Washington | Receptions | under | 0.08862849982270438 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|97528620-100f-4ff8-bdaf-28d77419865d | underdog | Savion Williams | Receiving Yards | under | 0.08856960710705053 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|06cdafae-7a83-47d5-b1fd-aa62835f03d4 | underdog | Chris Olave | Receptions | under | 0.0884086875583634 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|70ea33eb-2a51-4ae0-aa58-a5c7f1cdf1e9 | underdog | Justice Hill | Rush + Rec Yards | under | 0.08770930137695676 | 2026-11-03T11:59:28Z | 2026-11-06T01:15:00Z |
| prizepicks|16563334 | prizepicks | Ben Shelton | Total Games | over | 0.08688440176281631 | 2026-11-03T02:21:46Z | 2026-11-03T13:00:00.000-05:00 |
| underdog|d841a892-a21f-46e6-bc65-e0c20662a38e | underdog | Travis Hunter | Receptions | over | 0.08655057759181062 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|3c25e1f6-5855-4e10-b07c-c168b58f8e8b | underdog | Andre Szmyt | Kicking Points | under | 0.08606085228469695 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|d406ecdc-7559-4d9d-ab12-358c24990647 | underdog | Chris Rodriguez | Receptions | under | 0.08594491081353095 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|56001164-8f8a-46b9-8577-1174e7dff9c7 | underdog | Chuba Hubbard | Rush Yards | under | 0.0859349892986011 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|88038378-9240-40c3-a678-b25494753c18 | underdog | Xavier Worthy | Receiving Yards | under | 0.08541649458259926 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|ba34356a-c5a8-4f07-9671-c83995982867 | underdog | J.J. McCarthy | Rush Yards | under | 0.08453068040593992 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|a8b4d56b-3190-4729-a3e3-fa4952f7fe19 | underdog | Malachi Fields | Receptions | under | 0.08444567676815706 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|1cf10def-da38-4ff8-ae2b-ed870438b843 | underdog | Drew Sample | Receptions | over | 0.0839013767051019 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|ca923a9a-2e8e-46ad-acaf-0b4ecc69a8bd | underdog | Malik Nabers | Receiving Yards | under | 0.08364693870895912 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|db8a215c-a32b-461f-a74f-392bfed6cd47 | underdog | Sam LaPorta | Receptions | under | 0.08195280346786493 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|0767ecdc-6c88-403c-a631-567d0902ae5f | underdog | Bijan Robinson | Receptions | under | 0.08140314785642488 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|8f2a1812-fbba-4519-9282-247f7e5f6498 | underdog | Chris Rodriguez | Rush + Rec Yards | under | 0.08013290456542521 | 2026-11-03T11:59:28Z | 2026-11-06T01:15:00Z |
| underdog|1f157a7f-368c-48a0-ac57-7c1fd80f6abd | underdog | Dylan Raiola | Pass TDs | over | 0.07921835624192675 | 2026-11-03T11:59:28Z | 2026-11-07T20:30:00Z |
| underdog|8e108182-4c87-46e4-9018-ab3d52427b04 | underdog | Brian Thomas | Receptions | over | 0.07859887169586088 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|9cc6d7af-582b-4a55-b998-6d8b9a90cae1 | underdog | Trevor Lawrence | Pass TDs | under | 0.07694789832016491 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|99f3ae4b-6e3f-48d9-a87c-1281715f1b43 | underdog | Nolan James | Rush Yards | under | 0.0769268807412854 | 2026-11-03T02:21:46Z | 2026-11-08T00:30:00Z |
| prizepicks|16578148 | prizepicks | Derrick Henry | Rec Targets | under | 0.07676775725558316 | 2026-11-03T02:21:46Z | 2026-11-05T20:15:00.000-05:00 |
| underdog|b037dd4d-81a9-4275-bf43-602a7252c49e | underdog | George Pickens | Receptions | under | 0.0766522668294094 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|cf660a4f-4e16-40b9-9246-2751c5a47ffc | underdog | Chuba Hubbard | Receiving Yards | under | 0.07635365995898569 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| prizepicks|16578153 | prizepicks | Bhayshul Tuten | Rec Targets | under | 0.07632106872332856 | 2026-11-03T02:21:46Z | 2026-11-05T20:15:00.000-05:00 |
| underdog|54a02cb0-3fee-497f-9e40-ed483acb5ef9 | underdog | J.K. Dobbins | Rush + Rec Yards | under | 0.07576898608649796 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|b0f90105-2991-41ea-bc6c-2264f297449b | underdog | Nate Boerkircher | Receptions | under | 0.07569655692539734 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|c9f42cb3-782a-42ae-8d36-b838a2e16e5b | underdog | Tyler Goodson | Receptions | under | 0.07447307028831152 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|f7c17ddd-b7da-47e1-b7cc-3c831055be6b | underdog | Dominic Zvada | FG Made | under | 0.0741063683238431 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|a3d7b763-0cf0-497a-8a22-6f2b174f0c3a | underdog | Jordan Gant | Rush Yards | under | 0.07375412194161368 | 2026-11-03T11:59:28Z | 2026-11-04T00:00:00Z |
| underdog|a06d5616-3ce4-4197-850d-f0b0c73b34d5 | underdog | Drake Maye | Rush Yards | under | 0.0735599469387288 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| prizepicks|16576406 | prizepicks | Kyren Williams | Rush Yards | under | 0.0734640730790519 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|98370739-8ce7-4116-9352-2a9e7a795fa3 | underdog | C.J. Stroud | Pass TDs | under | 0.07344784426946727 | 2026-11-03T02:21:46Z | 2026-11-08T21:05:00Z |
| underdog|5f0b23b3-c959-4870-8412-71a8ccc5d09d | underdog | Michael Penix | Rush Yards | under | 0.07331631931313753 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|c10a0922-5357-4d12-a34a-fef19f41ae93 | underdog | Dylan Sampson | Receptions | under | 0.073210778810199 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| prizepicks|16577044 | prizepicks | Chig Okonkwo | Rec Yards | under | 0.07319171131719704 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| prizepicks|16572192 | prizepicks | Ja'Marr Chase | Recs | under | 0.07292626161783822 | 2026-11-03T02:21:46Z | 2026-11-08T09:30:00.000-05:00 |
| underdog|60d4c44c-f10d-4e36-a661-dd1c631f3414 | underdog | Omar Cooper | Receptions | under | 0.07236240548376671 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|2654ed1f-f909-41a8-9668-e28a31a28973 | underdog | Bhayshul Tuten | Receiving Yards | over | 0.07230312851767462 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|1adc0acb-33e0-4c49-8afc-9b6c4b1a14fd | underdog | Derrick Henry | Receptions | under | 0.07220955982843835 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|5decb5a9-f1ab-48b5-bdf2-ec7cff2a45da | underdog | Dominic Zvada | Kicking Points | under | 0.07189248960202987 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|dc7085a5-bd2b-4e90-9aa5-7e11f5f57193 | underdog | Dohnte Meyers | Receptions | under | 0.07018273167311495 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|2e941ef0-d7f5-4f4c-8018-abecc0ca312c | underdog | Nate Boerkircher | Receiving Yards | over | 0.07009713968929643 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|4f42e71e-9977-4467-9c6f-587a1fb01921 | underdog | Malik Willis | Pass TDs | under | 0.0698898131874599 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| prizepicks|16576408 | prizepicks | Javonte Williams | Rush Yards | under | 0.06913799764143458 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|5f633a93-4862-49ae-b90f-177413652bc3 | underdog | Dylan Raiola | Pass Yards | under | 0.06911494032105181 | 2026-11-03T11:59:28Z | 2026-11-07T20:30:00Z |
| underdog|7d1040e5-04ee-4e25-8fbf-f12f99828e9e | underdog | Cam Skattebo | Receptions | under | 0.06884453220929898 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|1204206e-1f86-4289-b59a-d537d4970c9e | underdog | Malik Willis | Rush Yards | under | 0.06868783647995347 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|4b82770a-7a57-4eae-87eb-44aba7f2eb02 | underdog | Noah Gray | Receptions | under | 0.06840206314519737 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|b8c47a57-f800-4f0c-885f-f5ff1d8c731a | underdog | Trevor Lawrence | Rush Yards | under | 0.06787768680871364 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|db07f361-6d11-4943-88ab-8c0ade090561 | underdog | Trey Smack | Kicking Points | under | 0.06754595893616899 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|5553828b-6797-4e54-b506-f648ccd47ced | underdog | Emmett Johnson | Receiving Yards | over | 0.06748156118753235 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|5b65b2a2-6156-4220-bfb0-fe9f33514bf2 | underdog | Rashod Bateman | Receiving Yards | over | 0.06671226866932445 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|60850929-c71c-42fe-8e2a-2897c3611dad | underdog | Simona Waltert | Double Faults | under | 0.0666632481681847 | 2026-11-03T02:21:46Z | 2026-11-03T10:10:00Z |
| underdog|a0b77c27-3f8d-489a-a00a-a4dab75bfce8 | underdog | Sam LaPorta | Receiving Yards | under | 0.06659663091661994 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|d4f2b5ca-0b3f-4658-962d-e49d13b62596 | underdog | Mike Gesicki | Receptions | under | 0.06624716319361124 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|17d196b6-916b-4467-86c8-3e43337d1b9d | underdog | Josh Jacobs | Receiving Yards | under | 0.06580018595374104 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|cf323095-2321-408c-89fd-7d1d5f7d89a0 | underdog | Javonte Williams | Receptions | under | 0.06563070619990474 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|84c8ff8f-479b-4e5a-91df-b47cb4924be2 | underdog | Xavier Worthy | Receptions | under | 0.06547220658559605 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|d029c1c5-255a-403c-b549-ddf4719278e6 | underdog | Nick Poulos | Pass TDs | under | 0.0647923556641622 | 2026-11-03T11:59:28Z | 2026-11-04T00:00:00Z |
| underdog|1e146d1e-95ac-4e18-b97f-874278e4440b | underdog | Emmett Johnson | Rush Yards | under | 0.06444132725080376 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|de701dad-dc41-4c39-b386-ddaa87ab0c04 | underdog | J.K. Dobbins | Rush Yards | under | 0.06421471109901433 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|8e09b065-9e64-4fb1-962e-2ce3b2acd571 | underdog | Darian Mensah | Pass TDs | over | 0.06371661097790937 | 2026-11-03T02:21:46Z | 2026-11-08T00:30:00Z |
| underdog|c9cba434-16a2-44a1-acf3-d92dc9f828a5 | underdog | Ja'Kobi Lane | Receiving Yards | under | 0.06358680985081022 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|21931440-adec-46d4-b530-994878d9e427 | underdog | T.J. Hockenson | Receptions | under | 0.06344057443403939 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|9e4ac678-53eb-48dd-9eb6-5829262bab83 | underdog | Bear Bachmeier | Pass Yards | under | 0.06313209167616829 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|71bce265-4a82-4c47-8d7d-3083d07176e4 | underdog | Kyler Murray | Rush Yards | under | 0.062051594008981636 | 2026-11-03T11:59:28Z | 2026-11-10T01:15:00Z |
| underdog|b473523b-f152-4e1a-83c4-4eedd7e91563 | underdog | Jaden Craig | Pass TDs | under | 0.06168729699532993 | 2026-11-03T02:21:46Z | 2026-11-07T03:15:00Z |
| prizepicks|16577034 | prizepicks | Denzel Boston | Rec Yards | under | 0.06162987154195598 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|ec27f580-1a71-4c96-833a-5b2bb78974b7 | underdog | Evan Engram | Receiving Yards | under | 0.06123051749536734 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|8c265bcd-7b60-4798-8607-03c1259a21e4 | underdog | Trey Smack | FG Made | under | 0.06104007152947344 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|f5d504e6-2b53-4eb6-bf8c-868ed6d671c4 | underdog | Cyrus Allen | Receiving Yards | under | 0.060834544249166234 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|eca0d130-1e71-423a-b2e6-4f1e8076fc73 | underdog | Justin Herbert | Rush Yards | under | 0.060339905746108924 | 2026-11-03T02:21:46Z | 2026-11-08T21:05:00Z |
| underdog|ddd9638a-9bf9-4d34-95f5-f5062fa4d6e9 | underdog | James Cook | Receiving Yards | under | 0.060031957811591874 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|7f70d6a0-eb6f-450d-bbb2-8ec7fc00a5d5 | underdog | Chris Bell | Receiving Yards | under | 0.059798518872956175 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|99a6085b-1064-4093-9351-7582b8a8a281 | underdog | Garrett Wilson | Receptions | under | 0.05978302669415658 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|1d902e2b-3919-4c19-b84a-8ffa99b10e62 | underdog | Brenton Strange | Receptions | under | 0.05946848028138785 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|ec66e518-4fe9-4188-a971-3856c8ad70b9 | underdog | Justice Hill | Receiving Yards | under | 0.05928474626324787 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|fe4d076e-daf4-4620-a5d9-81c9dcde46d9 | underdog | Mark Andrews | Receptions | under | 0.059115555543941656 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|285dab5f-ea1a-4d60-a385-159091689a27 | underdog | Savion Williams | Receptions | under | 0.058569519420755056 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|10bb608a-0288-452f-b2c1-0d0c058bf13f | underdog | James Cook | Rush Yards | under | 0.058244629667191794 | 2026-11-03T11:59:28Z | 2026-11-10T01:15:00Z |
| underdog|f6a0cb16-5759-468b-93f6-772a13d42630 | underdog | Marvin Mims Jr. | Receiving Yards | under | 0.05807117435666043 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|089ce83f-49f9-46ad-83c1-06b27856f11e | underdog | Tyler Shough | Pass TDs | under | 0.0579713928349842 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|ef93512e-7037-4e52-adab-e5a0e92cb14b | underdog | Kyler Kasper | Receptions | under | 0.0577929902830534 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|363f2a86-aea7-488d-8f25-6c2926e28588 | underdog | Michael Penix | Pass TDs | under | 0.05769866616807584 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|8a5f26a7-a3cf-4ac9-9f81-5d1a15fb3f24 | underdog | Keon Coleman | Receiving Yards | under | 0.057368923062176336 | 2026-11-03T11:59:28Z | 2026-11-10T01:15:00Z |
| underdog|4ed6c534-a882-4037-a5c5-3d3c36ee0467 | underdog | Jordan Faison | Receiving Yards | under | 0.05721438415905 | 2026-11-03T02:21:46Z | 2026-11-08T00:30:00Z |
| prizepicks|16577046 | prizepicks | CeeDee Lamb | Rec Yards | under | 0.0563405843653354 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|2e9a220f-7272-467e-b8e3-61ae45f85737 | underdog | Kenneth Walker III | Receiving Yards | under | 0.05507859411436211 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|db5a41ef-fc1d-4035-aa5e-7a30cf987986 | underdog | Troy Franklin | Receiving Yards | under | 0.05495631871264228 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|e2c22ff1-6209-4e3e-bbac-653eba1f1994 | underdog | Wayshawn Parker | Receiving Yards | over | 0.05434117214846301 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| prizepicks|16577036 | prizepicks | KC Concepcion Jr. | Rec Yards | under | 0.054101039282902996 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| prizepicks|16576403 | prizepicks | Quinshon Judkins | Rush Yards | under | 0.05350422507148955 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|fef1ffad-3a58-4a63-92a6-b3dfb1b6d88c | underdog | Deshaun Watson | Rush Yards | under | 0.05323742178232693 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|c56012e4-30e8-4196-bad4-730dcf525d19 | underdog | Ja'Kobi Lane | Receptions | under | 0.05292315297453021 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|27464760-8c59-4037-b749-3733f4a504cd | underdog | J.K. Dobbins | Receiving Yards | over | 0.052791170452059166 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|a902f30e-e69e-4a01-b2d0-1e8c66137193 | underdog | Noah Fifita | Pass TDs | under | 0.05263153895913575 | 2026-11-03T02:21:46Z | 2026-11-07T03:15:00Z |
| underdog|4268d138-80dd-44fb-8f09-ac7bb509ef59 | underdog | Tyler Goodson | Receiving Yards | over | 0.052016336879189495 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|cc22fac7-2f59-456b-9cae-e6eb0d0a9e39 | underdog | Troy Franklin | Receptions | under | 0.05174111879222043 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|2e7d4026-d4ff-4af2-96a3-e1353a1575b1 | underdog | Darian Mensah | Pass Yards | under | 0.051013863209490085 | 2026-11-03T11:59:28Z | 2026-11-08T00:30:00Z |
| underdog|7d4ea536-a682-47cb-bb01-adb82305747f | underdog | Drew Sample | Receiving Yards | over | 0.0505426052020973 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|97875f93-6930-4cda-9c97-1ad33e8d4022 | underdog | Harold Fannin | Receiving Yards | under | 0.04999003573194083 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|3ba5bfa4-fba8-486d-a689-89a74dd43fb9 | underdog | Juwan Johnson | Receiving Yards | under | 0.04994944129573198 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| prizepicks|16577037 | prizepicks | Chris Olave | Rec Yards | under | 0.04898251964490763 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|b73b2349-67bd-4725-869e-3e946a7c225e | underdog | Jakobi Meyers | Receptions | under | 0.04885583654522818 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|2ca5c958-8b8e-4a3a-b2e1-b1a084f73f5d | underdog | Jahan Dotson | Receiving Yards | under | 0.048393071940462495 | 2026-11-03T11:59:28Z | 2026-11-08T14:30:00Z |
| underdog|cc6e8fa9-fd9c-4ef8-b198-bb27be272161 | underdog | Quinshon Judkins | Receptions | over | 0.04707698015484607 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|79efae80-1726-417d-9fba-673881fec86c | underdog | Kyler Kasper | Receiving Yards | under | 0.046656667808123276 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|60ae2057-2007-4cae-9f42-087799172fc0 | underdog | Brenton Strange | Receiving Yards | under | 0.04608906136624302 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|e4023e77-9713-4947-a229-d8d0c01daa5c | underdog | Jojo Phillips | Receiving Yards | over | 0.04551214414039517 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|c14f5e7c-1500-4165-8dc5-f303be9c13ed | underdog | Tetairoa McMillan | Receiving Yards | under | 0.04544016578859289 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| prizepicks|16578154 | prizepicks | Brenton Strange | Rec Targets | under | 0.045215014696700084 | 2026-11-03T02:21:46Z | 2026-11-05T20:15:00.000-05:00 |
| underdog|823dc29d-c557-49c0-a1e9-a35682ddbb2b | underdog | Bijan Robinson | Receiving Yards | under | 0.04488526605093979 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| prizepicks|16552439 | prizepicks | Marina Bassols Ribera | Total Games | over | 0.04485535393303386 | 2026-11-03T02:21:46Z | 2026-11-03T13:20:00.000-05:00 |
| underdog|3c448b23-dacd-41f8-bfcf-5ba85bf85e76 | underdog | Josh Cameron | Receiving Yards | under | 0.044817529310626214 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|e5d081ab-9efa-43d3-bfb8-a43e2d593f85 | underdog | Drake Maye | Pass TDs | under | 0.04430737897190651 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|f9a76c6b-34a5-4243-a5ac-d0c7c9e1014a | underdog | Mark Fletcher Jr. | Rush Yards | under | 0.04410149704615496 | 2026-11-03T02:21:46Z | 2026-11-08T00:30:00Z |
| underdog|5e087ca0-c81b-466a-a4ab-b25feaca7f84 | underdog | Noah Bennee | Receiving Yards | over | 0.04389551607024966 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|46e3d4a9-5052-4f6b-9df2-d71dac46eb5f | underdog | Derrick Henry | Receiving Yards | over | 0.0437423600982455 | 2026-11-03T11:59:28Z | 2026-11-06T01:15:00Z |
| underdog|9f8d5a76-cbb3-4565-b2d4-601b302e1c66 | underdog | Jojo Phillips | Receptions | over | 0.04343832039629403 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|c2e9acd7-4e88-4f30-ae76-a25816dd4141 | underdog | Ricky Johnson | Receiving Yards | over | 0.043306631735705814 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| prizepicks|16557917 | prizepicks | Jordan Love | Rush Yards | under | 0.0431179313386405 | 2026-11-03T02:21:46Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|fe7a85f2-c21c-4535-88b9-b246e6af4d70 | underdog | Jason Sanders | FG Made | over | 0.04309576984353114 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|a5088759-dcc4-4d0c-acb8-516ddb05b069 | underdog | Noah Fant | Receptions | over | 0.04270940205899032 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|a797f932-ce6e-4e56-9b01-1f5c227fbc2e | underdog | Samaje Perine | Receiving Yards | over | 0.04251414252076868 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|10bfb7dc-9f91-4b58-abd5-8ad32df282c4 | underdog | Paula Badosa | Double Faults | over | 0.042475527310124384 | 2026-11-03T02:21:46Z | 2026-11-03T11:40:00Z |
| prizepicks|16578156 | prizepicks | Jakobi Meyers | Rec Targets | under | 0.04242041013161002 | 2026-11-03T02:21:46Z | 2026-11-05T20:15:00.000-05:00 |
| underdog|092a8f21-e061-4c26-a496-3bc5dd1ba46b | underdog | Mason Taylor | Receiving Yards | under | 0.04225142157026962 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| prizepicks|16564307 | prizepicks | Bianca Andreescu | Total Games | over | 0.042047604343236844 | 2026-11-03T02:21:46Z | 2026-11-03T13:20:00.000-05:00 |
| underdog|de6628da-2358-4822-a9a8-cf3d44824d9c | underdog | Zay Flowers | Receptions | over | 0.041882993253793854 | 2026-11-03T11:59:28Z | 2026-11-06T01:15:00Z |
| underdog|c250bf20-e931-4ea8-a99b-3c98802a0ae0 | underdog | Caleb Douglas | Receiving Yards | under | 0.04120672813171311 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|bdcd674d-5257-4323-97f7-4acfb97d1537 | underdog | Antonia Ruzic | Double Faults | over | 0.04082373042117504 | 2026-11-03T11:59:28Z | 2026-11-04T06:00:00Z |
| underdog|b4876ca4-f7e7-4fd2-ac05-6f01d5d72d89 | underdog | Justice Hill | Receptions | under | 0.040539917044618345 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| prizepicks|16577047 | prizepicks | Ryan Flournoy | Rec Yards | under | 0.04046234355837319 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| prizepicks|16557901 | prizepicks | Jared Goff | Rush Yards | over | 0.03998049861167219 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| prizepicks|16557921 | prizepicks | Kyler Murray | Rush Yards | under | 0.0398853265542245 | 2026-11-03T02:21:46Z | 2026-11-09T20:15:00.000-05:00 |
| underdog|f5e9749a-e6c4-43b9-9aaf-80fabfca565d | underdog | Tee Higgins | Receiving Yards | under | 0.0397142724789038 | 2026-11-03T11:59:28Z | 2026-11-08T14:30:00Z |
| underdog|696a8231-6e96-4a91-ab84-7ddf61a08941 | underdog | Riley Neer | Receiving Yards | under | 0.03961878890805015 | 2026-11-03T11:59:28Z | 2026-11-04T00:00:00Z |
| prizepicks|16577038 | prizepicks | Travis Kelce | Rec Yards | under | 0.039492224251563846 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|a02c710b-933f-4b18-907c-27053f219320 | underdog | Isaiah Likely | Receptions | under | 0.039343800400331586 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|d1d3e66e-276b-43d4-9e06-fe5ed3964b6c | underdog | Geno Smith | Pass TDs | over | 0.038346590420210214 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|0071a601-862e-44fa-ab60-3a5c7d3aaaf9 | underdog | Ryan Flournoy | Receptions | under | 0.03817671228052344 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|c9e2a183-7d96-4eaf-8ca8-3838a96ed892 | underdog | Ryan Flournoy | Receiving Yards | under | 0.03756251114817222 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|54df54a9-e16c-4b99-aa65-293d5ba8e703 | underdog | Omar Cooper | Receiving Yards | over | 0.03625910747796235 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| prizepicks|16576405 | prizepicks | Puka Nacua | Rush Yards | over | 0.035802440511908284 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|d3863d46-06f3-458d-b460-f6272d79e37f | underdog | Wayshawn Parker | Rush Yards | under | 0.03539702630366759 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|f77c4659-c571-4380-bb17-0f290c20cfdb | underdog | Braden Pegan | Receiving Yards | under | 0.03535065146715288 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|642b6aa4-d8ad-47ca-a6e2-02bf1db1abde | underdog | Rhamondre Stevenson | Receptions | under | 0.03473410197552751 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|2a845c17-55da-4173-bcf4-2994ccedf857 | underdog | Zay Flowers | Receiving Yards | over | 0.03460496018002179 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| prizepicks|16557908 | prizepicks | Patrick Mahomes | Rush Yards | under | 0.034534369510793694 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| prizepicks|16578159 | prizepicks | Nate Boerkircher | Rec Targets | under | 0.0344311591015668 | 2026-11-03T02:21:46Z | 2026-11-05T20:15:00.000-05:00 |
| underdog|71a4edea-2598-40b1-97fa-ce6bcc620a20 | underdog | Kenyon Sadiq | Receptions | under | 0.03442572108508024 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| prizepicks|16566857 | prizepicks | Novak Djokovic | Total Tie Breaks | under | 0.03391727992328841 | 2026-11-03T02:21:46Z | 2026-11-03T07:20:00.000-05:00 |
| underdog|acbc8a4f-c167-461b-87c7-68382ca800ab | underdog | Patrick Mahomes | Rush Yards | under | 0.03319109365485895 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|fe1331bb-39d1-4681-8d5a-f9d951e31392 | underdog | KC Concepcion | Receptions | under | 0.033021846340560934 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|09e2c2b3-1417-4229-b643-579ef34eb27a | underdog | Jordan Love | Rush Yards | under | 0.031106062142976287 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|88f782ab-7e8a-49e5-bf11-bca8a332538e | underdog | Tetairoa McMillan | Receptions | under | 0.030163771366317427 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
