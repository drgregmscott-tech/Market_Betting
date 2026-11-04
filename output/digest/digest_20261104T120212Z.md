# Pipeline Digest -- 2026-11-04T12:02:12Z

## Run summary
- Ingestion: 34092 rows (PrizePicks OK, Underdog OK)
- Estimation: 34092 rows estimated (from 34092 ingested props)
- CLV logging: 298 newly flagged, 0 newly closed, 533 still open (108187 total ever logged)

## Currently open flags
Sizing is a manual step (sizing_engine.py, Session 2.6) -- this table is what to scan to pick a pair worth sizing.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_edge | first_flagged_at | game_start_time |
|---|---|---|---|---|---|---|---|
| underdog|b45ed7b6-dd57-4168-b33f-b1d23e0fe0ba | underdog | Dawson Knox | Receiving Yards | under | 0.4 | 2026-11-04T12:10:41Z | 2026-11-10T01:15:00Z |
| underdog|159c0350-eab4-41f1-b826-0de1e1e3b5bd | underdog | Justin Herbert | Pass Yards | under | 0.4 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|268d2fc5-2abe-4849-b4a0-390d7485e453 | underdog | Caleb Williams | Pass Attempts | under | 0.4 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|754ec181-3723-4eeb-9d81-6ac2f38d4b05 | underdog | Josh Allen | Pass Yards | under | 0.4 | 2026-11-04T12:10:41Z | 2026-11-10T01:15:00Z |
| underdog|4a863902-d11a-4d1a-87cb-b706ca003cb8 | underdog | Josh Jacobs | Rush Yards | under | 0.4 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|d71953b3-f84a-41de-8164-f5fbcaae145d | underdog | Malik Willis | Pass Yards | under | 0.4 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|a07aac01-1d31-403d-9994-7e1aa59da29a | underdog | Trevor Lawrence | Pass Yards | under | 0.4 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|b343d3c5-a65e-4e28-a5f2-42058d73327d | underdog | Tanner McKee | Pass Yards | under | 0.4 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|869349aa-5399-4c3f-b961-edd9aca6684e | underdog | Michael Penix | Pass Yards | under | 0.4 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|b6204b0d-6199-4268-8d9a-88230d2297d4 | underdog | Olamide Zaccheaus | Receiving Yards | under | 0.4 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|b52c7395-e7ee-4951-a4fd-43f9a6eedb90 | underdog | Dak Prescott | Pass Yards | under | 0.4 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|72f89744-f92a-449b-a0bb-cf8069d05cd8 | underdog | Jack Larsen | Receiving Yards | over | 0.4 | 2026-11-03T02:21:46Z | 2026-11-08T00:30:00Z |
| underdog|a31d98a6-bf53-440e-a5b5-a2b50e20038d | underdog | Bo Nix | Pass Yards | under | 0.39297059903848375 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|3b541bb0-6dda-479a-a907-c082e233ed4c | underdog | Tanner McKee | Pass Attempts | under | 0.38702227943265677 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|29356dc8-01cb-4b38-a414-1571c2ae47db | underdog | Baker Mayfield | Pass Yards | under | 0.386000173495637 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|91257feb-8a6e-4897-a344-a682b8f407f8 | underdog | Justin Herbert | Pass Attempts | under | 0.382571560879172 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|b8d21dd7-97bf-498f-bf28-1b8190ab101b | underdog | Kyler Murray | Pass Yards | under | 0.3779532546313993 | 2026-11-04T12:10:41Z | 2026-11-10T01:15:00Z |
| underdog|20ded54a-d3d9-4991-b45f-4aab1465f143 | underdog | Jordan Love | Pass Yards | under | 0.35357762783010915 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| prizepicks|16557936 | prizepicks | Dak Prescott | Pass Yards | under | 0.35094246505677495 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| prizepicks|16577043 | prizepicks | Stefon Diggs | Rec Yards | under | 0.35094246505677495 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| prizepicks|16557940 | prizepicks | Brock Purdy | Pass Yards | under | 0.35094246505677495 | 2026-11-03T02:21:46Z | 2026-11-08T16:25:00.000-05:00 |
| prizepicks|16557925 | prizepicks | Tanner McKee | Pass Yards | under | 0.35094246505677495 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| prizepicks|16557944 | prizepicks | Josh Allen | Pass Yards | under | 0.35094246505677495 | 2026-11-03T02:21:46Z | 2026-11-09T20:15:00.000-05:00 |
| underdog|76903731-5a31-4b71-aa02-3cf5f1f66632 | underdog | Jared Goff | Pass Yards | under | 0.34472431347503396 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|ccf6b612-28dd-444f-9b72-2ec8c5cafef7 | underdog | Deshaun Watson | Pass Yards | under | 0.33983627444145803 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| prizepicks|16557935 | prizepicks | Jayden Daniels | Pass Yards | under | 0.3359949609424918 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|91cd9a90-2bbb-4479-9d44-9025494f5dbb | underdog | Bo Nix | Pass Attempts | under | 0.33308348303432955 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| prizepicks|16557945 | prizepicks | Kyler Murray | Pass Yards | under | 0.32685614816516073 | 2026-11-03T02:21:46Z | 2026-11-09T20:15:00.000-05:00 |
| underdog|57c9dc6a-5777-44c4-a352-8a75f42ba5fd | underdog | C.J. Stroud | Pass Yards | under | 0.3255781753629867 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|fa35b61f-7cc4-4f4b-9185-6e6a5167ad20 | underdog | Michael Penix | Pass Attempts | under | 0.3245304925645227 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|e2fd6e29-4327-4edb-afe4-e211903f4676 | underdog | J.J. McCarthy | Pass Yards | under | 0.32331174305176313 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|4fd3a242-cf5f-4eb3-a5db-95f253c0db3a | underdog | Josh Allen | Pass Attempts | under | 0.3201476032121736 | 2026-11-04T12:10:41Z | 2026-11-10T01:15:00Z |
| underdog|efda5476-bc73-4e5c-8d29-c3b22c80a111 | underdog | Drake Maye | Pass Yards | under | 0.3169471849941047 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|c180ec24-04be-4d76-92bd-f2b1a7387ad4 | underdog | Josh Jacobs | Receptions | under | 0.3138562329893375 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|9a750cb7-700f-436f-9538-1ce6918d995a | underdog | Deshaun Watson | Pass Attempts | under | 0.3135328194560545 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|cbf0d149-d120-49d4-b8d9-6df900ee39de | underdog | Bryce Young | Pass Yards | under | 0.31348509126095614 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| prizepicks|16557939 | prizepicks | Kirk Cousins | Pass Yards | under | 0.3094515764679242 | 2026-11-03T02:21:46Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|c276a65a-ae82-4954-9d4c-13d68aa92353 | underdog | Emeka Egbuka | Receiving Yards | under | 0.29901932004324594 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|cac0e559-74a5-448a-a3b7-221223acb5dc | underdog | Tyler Shough | Pass Yards | under | 0.29263132852775464 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| prizepicks|16557932 | prizepicks | Geno Smith | Pass Yards | under | 0.2900076533834668 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|a4f7e2ea-445a-4746-9a01-bb8681efb55d | underdog | Drake Maye | Pass Attempts | under | 0.2890709907617405 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|b1871eee-1be7-4d3b-b76e-1f9f7f70baca | underdog | J.J. McCarthy | Pass TDs | under | 0.2875734861947701 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|7dc2a808-0f7f-4a12-a56c-9b8c0eb39095 | underdog | Thomas Castellanos | Pass Yards | under | 0.2822212178373662 | 2026-11-04T12:10:41Z | 2026-11-08T02:30:00Z |
| underdog|034db5e8-e2a4-4f3a-b113-160fa7977d4f | underdog | Jake Elliott | FG Made | under | 0.27609595620105687 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|ab7d6a69-7520-4194-bb53-8478f9ad4866 | underdog | Geno Smith | Pass Yards | under | 0.2737068829684248 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|a3499f76-dc57-40ca-a12b-ccab39f10be5 | underdog | Bryce Young | Pass Attempts | under | 0.27237481147034737 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| prizepicks|16557930 | prizepicks | Deshaun Watson | Pass Yards | under | 0.26980869531882257 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|5a0ff8aa-ab28-4f6c-9ec5-e95c971f8458 | underdog | Andy Borregales | Kicking Points | under | 0.2640899467628497 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|029429a0-88e2-4188-bb6a-963cd5a7c4e2 | underdog | Baker Mayfield | Pass TDs | under | 0.26332788339696256 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|99b3f099-bf0e-494a-983b-03ca62b2b244 | underdog | Joe Burrow | Pass Yards | under | 0.26236014873001245 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| prizepicks|16557924 | prizepicks | J.J. McCarthy | Pass Yards | under | 0.2619885947590418 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|d484d774-fbd8-467b-bbfa-b6f85cfcf83f | underdog | Courtland Sutton | Receptions | under | 0.25834377385355134 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|a5d8af7b-ec41-4296-ae4d-19f0d58f11e6 | underdog | Geno Smith | Pass Attempts | under | 0.2582445722188248 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|c7d0412f-1aba-47dd-8ce0-e06060ca7b59 | underdog | Kyle Pitts | Receiving Yards | under | 0.25799821779938514 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| prizepicks|16557928 | prizepicks | Bryce Young | Pass Yards | under | 0.25782403523201924 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|42260fca-3f4a-4284-b57d-b9e07b027ca8 | underdog | Chase Brown | Rush + Rec Yards | under | 0.256995610592043 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| prizepicks|16557933 | prizepicks | Patrick Mahomes | Pass Yards | under | 0.256531424485161 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|88b26255-d953-47cf-aa2d-032da6db6cbf | underdog | Caleb Williams | Pass TDs | under | 0.256421951810362 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|2e6395f2-6b10-41e0-bb9d-05b1def655e4 | underdog | Tanner McKee | Pass TDs | under | 0.25424608115904224 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|25d18fbf-8c15-4a17-895c-3635dd1ce944 | underdog | Malik Willis | Pass Attempts | under | 0.2526482871588408 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|b72f06e1-815c-4c36-b978-4fcc8dfeeef1 | underdog | Andy Borregales | FG Made | under | 0.25213168723502966 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|9b0cfbcc-d59f-4d12-81d9-fc5d0ccbfd46 | underdog | Jadarian Price | Rush + Rec Yards | under | 0.25148275849233626 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| prizepicks|16577042 | prizepicks | Puka Nacua | Rec Yards | under | 0.24801878589627235 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|9fb52355-1d13-4cb0-9975-0ed2d6885e99 | underdog | Jordan Love | Pass Attempts | under | 0.24800187930178297 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|3f906d00-db91-4d33-827f-c952d6132d6e | underdog | Rashee Rice | Receiving Yards | under | 0.2382316723012532 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|4fda8e9c-363d-4afa-a7ea-bfd6e658b497 | underdog | Jadarian Price | Receiving Yards | under | 0.23745283835166386 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|7363a42c-3847-408e-a571-1c08fe3b2cf8 | underdog | J.J. McCarthy | Pass Attempts | under | 0.23728517572363184 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|7c495c78-612c-41d9-be4e-e90c4d640b25 | underdog | Ollie Gordon | Receiving Yards | under | 0.23628252484520373 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| prizepicks|16557934 | prizepicks | Matthew Stafford | Pass Yards | under | 0.23485070755351956 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|bba3c903-4ede-426b-98a4-5c60cb6bed88 | underdog | Jonah Coleman | Rush Yards | under | 0.233288763818978 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|1080b2cb-f33c-4f63-b95e-c4c81bdc6edd | underdog | Devaughn Vele | Receiving Yards | under | 0.23125785463944104 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|35d1779b-9b98-4325-9460-84c896b08ff2 | underdog | Courtland Sutton | Receiving Yards | under | 0.22953019104290462 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|28f20130-96a3-4e62-a067-ffd59150a903 | underdog | Woody Marks | Rush Yards | under | 0.2263548060433499 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|60cbaa38-c568-4879-a6f8-94b6e4e69559 | underdog | Tucker Kraft | Receiving Yards | under | 0.22559324997910668 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|b7a27035-0410-4524-9b9f-8504019e9e93 | underdog | Malik Washington | Receiving Yards | under | 0.22383503418957196 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|da210a50-3071-4e2c-adcb-afd5d0cf32dd | underdog | Cam Little | FG Made | under | 0.22067313990849302 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|b1b292ca-18cf-40bc-bd9f-e12fefdf9774 | underdog | Josh Jacobs | Rush + Rec Yards | under | 0.2185373608497626 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|3d11ff54-e68e-46fd-9bee-9f64e201a532 | underdog | Ladd McConkey | Receptions | under | 0.2182531395719538 | 2026-11-03T02:21:46Z | 2026-11-08T21:05:00Z |
| prizepicks|16557922 | prizepicks | Joe Burrow | Pass Yards | under | 0.2181379417292847 | 2026-11-03T02:21:46Z | 2026-11-08T09:30:00.000-05:00 |
| underdog|001b39ad-51d5-486c-b027-7d046d1fe6d7 | underdog | Bhayshul Tuten | Rush Yards | under | 0.21597127421289886 | 2026-11-04T12:10:41Z | 2026-11-06T01:15:00Z |
| underdog|0da29ba5-b418-4fcb-95cb-7843a0f651e2 | underdog | Jadarian Price | Rush Yards | under | 0.21347849926575668 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|d88c56d2-1395-401b-bd3e-3d1d31728d14 | underdog | Woody Marks | Rush + Rec Yards | under | 0.2133596409286077 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|47643075-a2e0-4286-848c-4cbc6b64643e | underdog | Jaylen Wright | Rush + Rec Yards | under | 0.21167080472030686 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| prizepicks|16577049 | prizepicks | Trey McBride | Rec Yards | under | 0.20935259101009185 | 2026-11-03T02:21:46Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|124b3b05-13c3-459b-a56a-4e57de87b55b | underdog | Kyler Murray | Pass Attempts | under | 0.2075409708914847 | 2026-11-04T12:10:41Z | 2026-11-10T01:15:00Z |
| underdog|96d514bd-16df-438e-a060-00f5c8573329 | underdog | Patrick Mahomes | Pass Attempts | under | 0.20613805218871373 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|03213d6b-9ff4-4b08-8ab9-3ecd87dfe78f | underdog | Dak Prescott | Pass TDs | under | 0.2061162118075327 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|8f89d0b9-f92a-4c38-a221-ee558e759c84 | underdog | Will Henderson | Rush Yards | under | 0.20565821012077623 | 2026-11-04T12:10:41Z | 2026-11-06T00:30:00Z |
| underdog|c0462df6-b3da-4b63-b678-808191fb8671 | underdog | Colston Loveland | Receiving Yards | under | 0.20437151822603095 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|1fa93360-83ec-4148-833b-a2ac7223bcde | underdog | Evan McPherson | FG Made | under | 0.20387134321469125 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|c61022bc-362a-4e1c-8d69-48a576ea6c00 | underdog | Justin Herbert | Pass TDs | under | 0.20191287593682095 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| prizepicks|16577051 | prizepicks | Brock Bowers | Rec Yards | under | 0.19828126826604298 | 2026-11-03T02:21:46Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|d9931ebc-f2b4-4965-a907-7e5426461db5 | underdog | Trey McBride | Receptions | under | 0.19807043328611007 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|c20d5abc-f610-4b73-8254-c304d61d594e | underdog | Bo Jackson | Rush Yards | under | 0.19693326906461994 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|75048265-2171-4068-88a1-2648aea119ae | underdog | Jake Weinberg | XP Made | over | 0.19575299180434336 | 2026-11-04T12:10:41Z | 2026-11-08T00:30:00Z |
| underdog|9a2902e7-4ecf-4ea5-a36e-c5c8f6e59bb7 | underdog | Harrison Butker | FG Made | under | 0.19473086921391436 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|f9beee99-bf11-4d3d-8d93-9a1099560025 | underdog | James Cook | Receptions | under | 0.19213415801783407 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|4d49f60c-e264-4756-8301-a0888a80b80f | underdog | Patrick Mahomes | Pass TDs | under | 0.19093001677595678 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|872eac2a-4e79-4367-a987-6a15c41a88dc | underdog | Kyle Pitts | Receptions | under | 0.1884927972756335 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|d34c91c5-ef7c-4feb-9ff3-c957645da483 | underdog | Ja'Marr Chase | Receiving Yards | under | 0.18806437242923668 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|e8b42489-088d-4fa3-8358-e7bd4e883b98 | underdog | Marvin Harrison | Receiving Yards | under | 0.18582900335069386 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|b8d4dab3-6a1d-41b4-83ea-0448c7b54f32 | underdog | Caden Veltkamp | Pass Yards | under | 0.18508162154040408 | 2026-11-04T12:10:41Z | 2026-11-06T00:30:00Z |
| underdog|c3ce2577-98dd-42a0-addf-2c82951bd5c7 | underdog | Jadyn Glasser | Pass Yards | under | 0.18508120203412437 | 2026-11-04T12:10:41Z | 2026-11-05T00:30:00Z |
| underdog|6af5960a-1d9d-4f3c-ab5d-c2bcd805cfc7 | underdog | Baker Mayfield | Pass Attempts | under | 0.1838540296279383 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|df0fcb9f-5100-4910-b141-a65adc25e74e | underdog | Joe Burrow | Pass Attempts | under | 0.18375588026906453 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|f4c69603-6218-4437-8fdd-275d6fcfe8ef | underdog | Jason Myers | FG Made | under | 0.1827109251134501 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| prizepicks|16644550 | prizepicks | Despina Papamichail | Total Games Won | over | 0.1826578017625795 | 2026-11-04T12:10:41Z | 2026-11-04T12:10:00.000-05:00 |
| underdog|85f1fb0a-6fd7-41b4-9c18-0dff6bbb3dc0 | underdog | C.J. Stroud | Pass Attempts | under | 0.1823525950518372 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|1d52713b-91a1-43dd-a9d1-f9121a9ce5ef | underdog | Trevor Lawrence | Pass Attempts | under | 0.18222502497258852 | 2026-11-04T12:10:41Z | 2026-11-06T01:15:00Z |
| prizepicks|16600354 | prizepicks | Mary Stoiana | Total Games Won | over | 0.18220396773912617 | 2026-11-04T12:10:41Z | 2026-11-05T06:40:00.000-05:00 |
| underdog|14f41be8-d78a-41fa-acf5-d4ff3eae967e | underdog | Jonah Coleman | Rush + Rec Yards | under | 0.18135259270870874 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|63c520e3-4fd1-4a1f-a7a9-3a7b0b8c1291 | underdog | Nico Collins | Receiving Yards | under | 0.1799086895550015 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|6b30c374-5ba2-46ea-96aa-44e0f745815e | underdog | Ollie Gordon | Rush + Rec Yards | under | 0.17815773368015286 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|9100eaf4-8232-4056-8f1f-336a475cc678 | underdog | Rhamondre Stevenson | Rush Yards | under | 0.17609187646102753 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|d76f74e5-bd98-4fcc-b798-aa1424ca2b99 | underdog | Daniel Hill | Receiving Yards | over | 0.1760656995962664 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|58473198-16c0-4f1f-98ce-794fe0d452fd | underdog | Rashee Rice | Receptions | under | 0.17383563925443812 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|e67e9ba5-8b23-46cb-a546-85415df91843 | underdog | Luke Fahey | Pass TDs | under | 0.17214479173554886 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|fdc20714-2850-4478-a9ae-058d3a14ba1b | underdog | Jake Elliott | Kicking Points | under | 0.1717042647640432 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|5294f95e-70ef-47dd-8cdf-91081da98280 | underdog | Kyler Murray | Pass TDs | under | 0.17036826288931617 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|abca8845-91ef-49e4-a440-99722625b839 | underdog | Tyler Shough | Pass Attempts | under | 0.16933621783832775 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|d1484ee9-014f-45d1-a126-1d177aec34ed | underdog | Makhi Hughes | Rush Yards | under | 0.1692475397419455 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|a2c32829-5741-4600-bdac-f990a7052b23 | underdog | Rhamondre Stevenson | Rush + Rec Yards | under | 0.1684921629314633 | 2026-11-03T11:59:28Z | 2026-11-08T21:25:00Z |
| underdog|1e0723e6-39f5-401c-9ecb-73146c38ec61 | underdog | Marvin Harrison | Receptions | under | 0.16835016265867342 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|a8a9bed2-5d3a-4afa-b7f7-de3a2c658f75 | underdog | Jared Goff | Rush Yards | over | 0.1677182366005825 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|6f512073-b3c1-42b4-b03f-6ac4f5107180 | underdog | Javonte Williams | Rush + Rec Yards | under | 0.16761201615437293 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|bb97cdd4-5519-4c3d-ae4c-e420804962fe | underdog | Cam Little | Kicking Points | under | 0.16744281795199767 | 2026-11-04T12:10:41Z | 2026-11-06T01:15:00Z |
| underdog|cf74ea13-4c83-486b-a699-efa71530a041 | underdog | Amon-Ra St. Brown | Receptions | under | 0.16742438992001507 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|c25ee6c2-0d8f-4131-aea1-9893c5a2a07d | underdog | Harrison Butker | Kicking Points | under | 0.16675032754030605 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|3c2c0991-0e80-4489-9557-56d68aa8268c | underdog | Wil Lutz | FG Made | under | 0.1665329706004408 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|c7fbbf68-83ff-44a2-a032-87a9503edea0 | underdog | Cairo Santos | FG Made | under | 0.16650636156632292 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|c4f952f7-59ce-4967-935e-c3c059ff4420 | underdog | Thomas Castellanos | Pass TDs | under | 0.16265526234623773 | 2026-11-04T12:10:41Z | 2026-11-08T02:30:00Z |
| underdog|9ff29ccb-f4c3-4664-9330-39133772a9f1 | underdog | Tucker Kraft | Receptions | under | 0.1615364063191952 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|9cc36ab9-fd71-4bfb-813b-54422aecd68a | underdog | Anthony Colandrea | Pass Yards | under | 0.16122272665769133 | 2026-11-04T12:10:41Z | 2026-11-07T01:00:00Z |
| underdog|528a645e-8439-47f6-91f3-89566cf92574 | underdog | Greg Dulcich | Receptions | under | 0.15981895291377868 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|bb77573a-4a49-460a-b9a5-e71be79f2ce2 | underdog | Jared Goff | Pass Attempts | under | 0.15940465299458384 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|7d8aca5c-098a-4cd2-ac18-2986be8ea813 | underdog | Matthew Golden | Receptions | under | 0.15935064858874126 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|de6281e6-e72c-4f7d-9b19-ea93df015060 | underdog | Drake London | Receptions | under | 0.1588244841998091 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|31bddf30-7315-4f04-8016-019b04650ac5 | underdog | Owen McCown | Pass TDs | under | 0.15660665947473018 | 2026-11-04T12:10:41Z | 2026-11-06T00:30:00Z |
| underdog|0b592d73-46b4-4456-918c-8d00242be932 | underdog | Dawson Knox | Receptions | under | 0.15649493040707285 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|28aa1264-fc74-4c1c-9f5a-0f2b5396c62e | underdog | Garrett Wilson | Receiving Yards | under | 0.15645468065321244 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|a0b5e5bf-c392-400b-a1cb-acf5cfb9f992 | underdog | Kenny Gainwell | Receiving Yards | under | 0.15479819065062306 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|fb2f63dc-6a61-48c3-bf9a-663636155fa3 | underdog | Quinshon Judkins | Rush + Rec Yards | under | 0.15401249415477758 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| prizepicks|16577045 | prizepicks | Antonio Williams | Rec Yards | under | 0.15279763651234368 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|d310ea33-b4f2-49b4-9cfc-5a4bbcaab30b | underdog | Sam Darnold | Pass TDs | under | 0.15277086609279655 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|7f44b052-27a1-42a5-8108-ca43bdfcb5bb | underdog | Chuba Hubbard | Rush + Rec Yards | under | 0.14959006456056478 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|e0c22419-0dff-4556-a05e-9acfa3ab7a09 | underdog | Brandon Aubrey | FG Made | under | 0.14958269462275497 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|b0ce99d7-ccca-47c0-a454-e6f920eab8e2 | underdog | Bo Nix | Pass TDs | under | 0.14921921703126695 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|78f69cb1-b2ea-4410-853d-44094574eb64 | underdog | Parker Washington | Receiving Yards | under | 0.1490737198822808 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|766e4fdf-cab3-4844-ae20-2539e12866ad | underdog | Rome Odunze | Receiving Yards | under | 0.14901628948911372 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|69ba3a63-bb92-4f39-984a-ed5566438f78 | underdog | Nick Folk | FG Made | under | 0.1481435952641591 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|c4587fdc-fe2d-47dc-997d-d0b08663b00a | underdog | Ka'imi Fairbairn | FG Made | under | 0.1479318682678138 | 2026-11-03T02:21:46Z | 2026-11-08T21:05:00Z |
| underdog|1b370830-3867-4ade-9a8d-418a06dbd1c1 | underdog | Christian Watson | Receptions | under | 0.1479168165648339 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|2484637b-dd6a-4882-be40-ce0e68d4e559 | underdog | Kenny Gainwell | Receptions | under | 0.1475602481670133 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|1b3fdb16-4544-40a7-9bfa-f369d645d9fa | underdog | Jadyn Glasser | Pass TDs | under | 0.14730596525102757 | 2026-11-04T12:10:41Z | 2026-11-05T00:30:00Z |
| underdog|13d49fc8-9559-45e1-9bac-6f15a20a2c72 | underdog | Ollie Gordon | Receptions | under | 0.14682805397570908 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|d204e0bd-cd91-4817-9c35-69876cf608f9 | underdog | Tyler Goodson | Rush + Rec Yards | under | 0.14661488441558534 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|ad5841e3-f51c-4e2d-a883-064eb9b2257f | underdog | Malik Washington | Receptions | under | 0.14645959659878283 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|f57c0032-b5b1-4228-af7c-d6bb6f08e67e | underdog | Emeka Egbuka | Receptions | under | 0.1460648049345178 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|b739a15f-4dfa-4f63-9c1f-ddf4d1cc6dbb | underdog | Cam Skattebo | Rush + Rec Yards | under | 0.14574273316819908 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|a5687c54-7273-4922-8cf8-a0383ebb4afa | underdog | Trey McBride | Receiving Yards | under | 0.14497443435005852 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|d9c83072-0b9d-4dd6-ac46-9ee7193a65c2 | underdog | Jake Bates | Kicking Points | under | 0.14384173611237716 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|d5b2c525-007e-40f6-b372-72fd93826950 | underdog | Jahmyr Gibbs | Rush + Rec Yards | under | 0.14253753750183595 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|bfda4bd7-7ec5-4e97-a7a8-773f8955cd86 | underdog | Dak Prescott | Pass Attempts | under | 0.1423958530059607 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|8d2750d2-9d3b-48ff-8e00-77d67f7ecdc8 | underdog | Ladd McConkey | Receiving Yards | under | 0.14192042119468462 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|1acc37b7-16ae-4dfe-9876-857c87ea3b17 | underdog | Quentin Johnston | Receiving Yards | under | 0.1413979010411639 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| prizepicks|16590528 | prizepicks | Ignacio Buse | Total Games Won | over | 0.14014082984014242 | 2026-11-04T12:10:41Z | 2026-11-04T07:30:00.000-05:00 |
| prizepicks|16558454 | prizepicks | Ignacio Buse | Total Games Won | over | 0.14014082984014242 | 2026-11-03T02:21:46Z | 2026-11-04T05:00:00.000-05:00 |
| prizepicks|16645104 | prizepicks | Jazmin Ortenzi | Total Games Won | over | 0.13997775741539353 | 2026-11-04T12:10:41Z | 2026-11-04T17:00:00.000-05:00 |
| underdog|19182bf3-3972-4fb8-ad6e-ff29a13cff8c | underdog | Chase Brown | Rush Yards | under | 0.13989207436771856 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|e1775404-5113-460c-9eec-b13c0226b55b | underdog | Olamide Zaccheaus | Receptions | under | 0.1396223249639138 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|309d5f3b-4a5e-4fc0-84e4-e7b9dc576c6c | underdog | Jalen Royals | Receiving Yards | over | 0.13929767687854722 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|03e0d95d-f3f0-4f64-bea2-e9e8bbb684e3 | underdog | AJ Barner | Receptions | under | 0.13910664132787998 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|3c114bc2-839b-4e55-9ec0-5de96e8522a9 | underdog | Caleb Douglas | Receptions | under | 0.1384724673367177 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|5df51a97-b605-4c0d-b9a5-6038554d83e4 | underdog | Amon-Ra St. Brown | Receiving Yards | under | 0.13837637499846278 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|8f656585-f55b-4b3e-a4bb-20189b851dd4 | underdog | KC Concepcion | Receptions | under | 0.13828986383989172 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|0155effd-3be4-45b8-81fb-a8dcbdf86d26 | underdog | Ollie Gordon | Rush Yards | under | 0.13813773558226028 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|edf3942e-d179-4b05-bc85-891a5ccd55b8 | underdog | Jaxon Smith-Njigba | Receptions | under | 0.13807285295610772 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|83b965d9-e75e-4d7b-8886-44573ffbcdfb | underdog | Dilin Jones | Rush Yards | under | 0.13798927114368054 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|a27717e2-b673-40e8-95cc-89ea0eae37ba | underdog | Deshaun Watson | Pass TDs | under | 0.13610875973967107 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|d2fcfed3-fc34-4384-a422-ff8ea1412db3 | underdog | Travis Kelce | Receiving Yards | under | 0.13606357340573372 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|d6cbee1a-cecf-45c3-92bd-590b34f8135a | underdog | Nick Folk | Kicking Points | under | 0.1351811208582573 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|0a1d4a28-f4ed-433b-a45b-953e95969acb | underdog | Jadarian Price | Receptions | under | 0.13399424688283068 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|e21796c6-8678-416e-9378-62322f8b2400 | underdog | Rudy Kessinger | FG Made | over | 0.13388091783386746 | 2026-11-04T12:10:41Z | 2026-11-05T00:30:00Z |
| underdog|5790a889-8601-4824-ac78-b9c766ba1891 | underdog | Marvin Mims Jr. | Receptions | under | 0.13357422686133513 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|a9423304-185a-456f-aa8a-e12bb9b1b579 | underdog | Jakobi Meyers | Receiving Yards | under | 0.13343229218485075 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|e5b104d0-4d4a-40f8-b1af-c7a433122290 | underdog | Ethan Moczulski | FG Made | over | 0.13305034470819216 | 2026-11-04T12:10:41Z | 2026-11-07T01:00:00Z |
| underdog|798ddc6d-4d87-400d-913e-60f592707c85 | underdog | Isaiah Likely | Receiving Yards | under | 0.1320310141321548 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|6a4ea7ca-8051-400b-a435-f94e0a7067ee | underdog | Jameson Williams | Receiving Yards | under | 0.131077359753479 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|5869b7ef-5cbd-40b2-b17d-2b4591a92144 | underdog | Matthew Golden | Receiving Yards | under | 0.12870107458299462 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|7a288207-299b-4695-b585-940ac0294fdc | underdog | Luke Fahey | Pass Yards | under | 0.12864978345130762 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|f9408da3-4c03-47a1-91ac-c4ac94507742 | underdog | Drake London | Receiving Yards | under | 0.12714827801752404 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|f5c38bf0-85ac-4489-b4e7-b51f3c72ffc9 | underdog | Javonte Williams | Receiving Yards | under | 0.12591828129631966 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|a5a84e5b-2d1a-407b-ad40-5e0faa4d1d12 | underdog | Wil Lutz | Kicking Points | under | 0.12375220362671835 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| prizepicks|16634247 | prizepicks | Lucrezia Stefanini | Break Points Won | under | 0.12337388858051412 | 2026-11-04T12:10:41Z | 2026-11-05T04:30:00.000-05:00 |
| underdog|a75d0892-12c3-4a3d-bea7-a07236a8702c | underdog | Conner Weigman | Pass Yards | under | 0.12251598812778575 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|f3d5e2f8-b078-48d2-b5d6-54ca6ca199e6 | underdog | Cairo Santos | Kicking Points | under | 0.12236507723893952 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| prizepicks|16577041 | prizepicks | Garrett Wilson | Rec Yards | under | 0.12215435750439496 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|06a98b20-5b6a-4641-963b-748d6b6ac027 | underdog | Ja'Marr Chase | Receptions | under | 0.12198379656106328 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|e0185cca-1a27-4e8e-8859-8afaabde877b | underdog | Spencer Porath | FG Made | over | 0.12185258966611756 | 2026-11-03T02:21:46Z | 2026-11-08T00:30:00Z |
| underdog|18971421-29b9-4aa5-b533-b3255d1a9695 | underdog | Bijan Robinson | Rush + Rec Yards | under | 0.12137057551043673 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|247b1df6-4f80-4eed-ae74-bfcc7582ec7a | underdog | Bhayshul Tuten | Receptions | under | 0.12077038979546606 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|0187bc04-2901-4ba3-8977-4bd9fb0d707b | underdog | Katin Houser | Rush Yards | over | 0.1201508756895383 | 2026-11-04T12:10:41Z | 2026-11-07T01:00:00Z |
| underdog|03b3eb0d-b146-440d-843d-79223ef0bf2b | underdog | Jahan Dotson | Receptions | under | 0.1200345581620813 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| prizepicks|16619686 | prizepicks | Chris Dawn Jr. | Recs | under | 0.11978140668783599 | 2026-11-04T12:10:41Z | 2026-11-07T22:30:00.000-05:00 |
| underdog|94fc7a75-ac49-46e5-aa74-e6a67b1bd62c | underdog | Tyler Goodson | Rush Yards | under | 0.11960752661139407 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|e96392d4-2e7b-476c-b8c5-d0f6a5a4072c | underdog | Denzel Boston | Receiving Yards | under | 0.1195381161154726 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| prizepicks|16576409 | prizepicks | Christian McCaffrey | Rush Yards | under | 0.11950744181162642 | 2026-11-03T02:21:46Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|c7bb0bb6-dc60-4c38-93e2-684dacb04b02 | underdog | Josh Allen | Pass TDs | under | 0.11926653211048077 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|d6f7661e-2b78-4499-9a77-5003d9a91d7f | underdog | Kyle Cunanan | XP Made | over | 0.11924361207919232 | 2026-11-04T12:10:41Z | 2026-11-07T01:00:00Z |
| underdog|33ffb548-94a1-44e7-9da3-17dc0d7f1d49 | underdog | J'Koby Williams | Receiving Yards | over | 0.11825318810941854 | 2026-11-04T12:10:41Z | 2026-11-08T02:30:00Z |
| underdog|1c07119d-7fe4-4eba-b8f2-c7008e344979 | underdog | Harold Fannin | Receptions | under | 0.11801150156707052 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|3af0bcc2-f9da-427a-9708-fd1b9e5e5f2d | underdog | Trinidad Chambliss | Pass Yards | under | 0.11770205880824303 | 2026-11-04T12:10:41Z | 2026-11-08T00:30:00Z |
| underdog|1a302e32-ea50-4ad7-9fcd-27c67675614e | underdog | Josh Cameron | Receptions | under | 0.1176734146378754 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|226a14c9-0c56-43cb-b3cc-a0032a489375 | underdog | Grant Meadors | XP Made | over | 0.11720642605229831 | 2026-11-04T12:10:41Z | 2026-11-05T00:00:00Z |
| underdog|649d4cf3-3d96-4754-b6ba-149b97bba842 | underdog | Kenneth Walker III | Receptions | under | 0.11559688528805712 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|df8cc29e-c9c7-46e3-9773-066f25acc7a6 | underdog | CeeDee Lamb | Receptions | under | 0.11512462845971994 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|24776d41-9ab8-4829-8813-d00f6ac87075 | underdog | Javonte Williams | Rush Yards | under | 0.11477410078296513 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|f2f45b87-957b-46ab-9edf-e31974176078 | underdog | Thomas Castellanos | Rush Yards | under | 0.11460442719465413 | 2026-11-04T12:10:41Z | 2026-11-08T02:30:00Z |
| underdog|422529cb-6975-4301-bce0-938e9ad74ce9 | underdog | Owen McCown | Pass Yards | under | 0.114395530840953 | 2026-11-04T12:10:41Z | 2026-11-06T00:30:00Z |
| underdog|0d64e017-b859-433b-8b93-491525d6f2eb | underdog | Bhayshul Tuten | Rush + Rec Yards | under | 0.11408094268080893 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|d8eff3f4-0952-455a-8a4c-7bb5a9015f58 | underdog | CeeDee Lamb | Receiving Yards | under | 0.11388405923937717 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|8dda3f2c-43bd-496a-91aa-283c7a072e7b | underdog | Chuba Hubbard | Receptions | under | 0.11351803648802827 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|980ef0c9-e7c6-40c1-ae91-d71c59322e06 | underdog | Travis Kelce | Receptions | under | 0.11333613992057967 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| prizepicks|16557903 | prizepicks | Bryce Young | Rush Yards | under | 0.11312986015089133 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|516cd42e-4751-4b27-abbb-5cc40fef6cbf | underdog | Jaylen Wright | Rush Yards | under | 0.11295640133296947 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|3b806c99-c348-44de-86cc-461e6cf2d3f2 | underdog | Jake Bates | FG Made | under | 0.11285240847954703 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| prizepicks|16577048 | prizepicks | George Pickens | Rec Yards | under | 0.11245540278204647 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|e14b44d7-6880-4cde-a5d0-be585bd64366 | underdog | Denzel Boston | Receptions | under | 0.11215354306007119 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|ba27855c-f306-460f-8d0b-850a557fe3e5 | underdog | James Cook | Rush + Rec Yards | under | 0.11131941599424644 | 2026-11-04T12:10:41Z | 2026-11-10T01:15:00Z |
| underdog|d1042d88-2d40-4bee-8ec8-aa067d1ceaac | underdog | Jahmyr Gibbs | Rush Yards | under | 0.11069192642370285 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|1fecccd3-7915-4b3d-9923-95b353ee0c90 | underdog | J.K. Dobbins | Receptions | under | 0.11024990718515137 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|57815146-a656-43d6-9668-35d136e67d23 | underdog | Devon Dampier | Pass Yards | under | 0.10960047075501667 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|69a82857-d297-4b15-a385-2a023ebcf054 | underdog | Dalton Kincaid | Receptions | under | 0.10948029145485216 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|ba47c124-db10-4b69-b5cf-5ba62f5c4d37 | underdog | Jahmyr Gibbs | Receptions | under | 0.10946590257471323 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|14dd7e40-30bd-4230-aa09-2bcee96f116b | underdog | Katin Houser | Pass Yards | under | 0.10931626492452251 | 2026-11-04T12:10:41Z | 2026-11-07T01:00:00Z |
| underdog|e2b4bad8-1412-4ef1-807c-2d9921b75224 | underdog | John Love | FG Made | over | 0.10906649198025498 | 2026-11-04T12:10:41Z | 2026-11-07T00:00:00Z |
| underdog|a0eb3048-bcf7-483f-a312-d719004e816e | underdog | Conner Weigman | Pass TDs | under | 0.10842608409629839 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|2a03ddda-093f-4ef6-a512-af233e05477d | underdog | Chad Ryland | FG Made | over | 0.10832807545342293 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|f311252f-9e6c-408d-be8b-7d0a3faa63f2 | underdog | Chris Olave | Receiving Yards | under | 0.10820736969347688 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|4c17b548-6dd0-41a7-be94-4eeba93de71a | underdog | Nico Collins | Receptions | under | 0.10808570977681886 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|1b7021b4-b333-4256-bc1e-7c9f88464431 | underdog | Jonah Coleman | Receptions | under | 0.10693828108030978 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|d599a5ae-1ff8-4df6-9eac-c397c998888d | underdog | Colston Loveland | Receptions | under | 0.10664747026618215 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| prizepicks|16571203 | prizepicks | Jordan Faison | Recs | under | 0.10659393574032039 | 2026-11-04T12:10:41Z | 2026-11-07T19:30:00.000-05:00 |
| underdog|b3f31006-6c8e-4e0e-8a7c-3b31c58669df | underdog | Jonah Coleman | Receiving Yards | under | 0.10644334717594295 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|68027fbe-2681-4510-8eea-3775ceb54e92 | underdog | Dalton Schultz | Receptions | under | 0.10596561958189699 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|fd7968a6-baa5-4e26-b5e2-e9a235b96210 | underdog | Caden VanHuis | FG Made | under | 0.1058826884528653 | 2026-11-04T12:10:41Z | 2026-11-05T00:30:00Z |
| underdog|14b3f2c6-ee66-4fa0-8984-b74db108ebf3 | underdog | Malik Nabers | Receiving Yards | under | 0.1056526902792364 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|f12a1637-afba-463e-8173-b76d2a2beadd | underdog | Isaiah Mizell | Receptions | under | 0.10519560594438182 | 2026-11-04T12:10:41Z | 2026-11-07T03:15:00Z |
| underdog|aa2414f6-9b31-4532-b1cb-045d89a12d45 | underdog | Adonai Mitchell | Receptions | under | 0.10517197384243948 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|3dd97269-7090-4494-b0ba-aef942cacee8 | underdog | Jared Goff | Pass TDs | under | 0.10432511994565019 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|4a328574-9067-45a3-b2c8-168d822b5e16 | underdog | T.J. Hockenson | Receiving Yards | under | 0.10407541804729603 | 2026-11-03T11:59:28Z | 2026-11-10T01:15:00Z |
| underdog|1db30023-5914-439c-ac51-c556c30f7a5b | underdog | Marshall Pritchett | Receiving Yards | over | 0.1040578939603718 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| prizepicks|16577039 | prizepicks | Rashee Rice | Rec Yards | under | 0.10318750310261049 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|a69c7259-5cc4-4207-8a64-47ec96c6c5b0 | underdog | Jaylen Waddle | Receiving Yards | under | 0.10317750601720066 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|fdb43e68-4917-450f-8dc2-f6ae9972edee | underdog | Quinshon Judkins | Rush Yards | under | 0.10256176001471462 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|c4b8e03b-86f2-4d6c-b024-04caa813ed63 | underdog | Andre Szmyt | FG Made | under | 0.10236818666743885 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|c31081a6-c8f1-4e82-af45-590d8aa34b39 | underdog | Greg Dulcich | Receiving Yards | under | 0.1023319243442552 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|d9d08697-3dd2-4d24-bc73-42297b125227 | underdog | Jameson Williams | Receptions | under | 0.10208410937911938 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|e6b315b3-1d05-4863-a312-804d6b22ba5d | underdog | Cam Skattebo | Rush Yards | under | 0.10199709963178782 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|7bf309d3-cb09-4113-b642-82526d074215 | underdog | Christian Watson | Receiving Yards | under | 0.10173017572558107 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|f4bba20a-76ec-4df5-9de0-3c7c20bd1a76 | underdog | Keon Coleman | Receptions | under | 0.10169343136994924 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|286912ed-323c-4195-8bb0-aae532cca8e5 | underdog | Michael Petro | FG Made | over | 0.10165952350252716 | 2026-11-04T12:10:41Z | 2026-11-06T00:30:00Z |
| underdog|d4a5094c-9736-4dde-95d2-0ea510ff3258 | underdog | Bijan Robinson | Rush Yards | under | 0.10013138750495743 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|b5d747fa-73cd-4acb-88a8-538cb0bc7051 | underdog | Jordan Addison | Receiving Yards | under | 0.098653067032206 | 2026-11-03T11:59:28Z | 2026-11-10T01:15:00Z |
| underdog|be48005a-e911-48a5-89d3-0071ee0d1592 | underdog | Devon Dampier | Pass TDs | over | 0.09858639656620943 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|d1e744f7-e48f-432b-ac36-9994d2f0347b | underdog | Chuba Hubbard | Rush Yards | under | 0.09846599432023506 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| prizepicks|16619747 | prizepicks | Jesse Legree | Recs | under | 0.09789260962625501 | 2026-11-04T12:10:41Z | 2026-11-07T22:30:00.000-05:00 |
| underdog|ca0fc4a6-2158-45f4-acb6-cb6dfb5923c3 | underdog | Jason Myers | Kicking Points | under | 0.09767305134966542 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| prizepicks|16623390 | prizepicks | Kyle Pitts Sr. | Recs | under | 0.09724751553828881 | 2026-11-04T12:10:41Z | 2026-11-08T09:30:00.000-05:00 |
| underdog|1282186b-1e17-4f39-80bb-f115ba16b931 | underdog | Michael Salgado-Medina | XP Made | over | 0.09720055842492309 | 2026-11-04T12:10:41Z | 2026-11-07T03:15:00Z |
| underdog|dd95402c-e9ca-44e5-a5a3-179e2734707c | underdog | Jordan Addison | Receptions | under | 0.09707338503094809 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|777a6934-83da-4fc6-ae05-670614aac4c8 | underdog | Luther Burden | Receptions | under | 0.0970050304666229 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|6ad7651f-c6d0-47b2-8c0b-3d2f8e5f2a3d | underdog | Keldric Luster | Pass Yards | under | 0.09641969172093356 | 2026-11-04T12:10:41Z | 2026-11-05T00:00:00Z |
| prizepicks|16623392 | prizepicks | Jahan Dotson | Recs | under | 0.09637295072919405 | 2026-11-04T12:10:41Z | 2026-11-08T09:30:00.000-05:00 |
| underdog|1f00fe69-5e5d-44a5-a6cb-75f2957605fa | underdog | Sam Darnold | Pass Attempts | under | 0.09624325509984921 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|2bac7b08-fac7-40ce-8ab4-52eed070b62a | underdog | Jordan Love | Pass TDs | under | 0.0961519218860859 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|0c57932e-0ffc-411c-bd91-b60cf90168b0 | underdog | Brandon Aubrey | Kicking Points | under | 0.09590964792109724 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|9fdc5d99-c95b-4a2a-872e-519a6d3ef378 | underdog | AJ Barner | Receiving Yards | under | 0.09556447149129821 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|70b674bf-14ef-4526-b90e-42cba3c6d3a5 | underdog | Adam Trautman | Receptions | under | 0.09545112973787573 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|5e7d7ef3-a508-4d6c-8762-1b785d65fdc7 | underdog | Xavier Worthy | Receiving Yards | under | 0.0949498557542463 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|816cce36-5f20-4e9b-9bab-bf7a84334bda | underdog | J.J. McCarthy | Rush Yards | under | 0.09483178381445445 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|e6a6d9c4-cede-4db1-8127-fadccb0830a1 | underdog | Parker Washington | Receptions | under | 0.09473178992722764 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|c578d8d7-01f0-4d79-9d4f-3b0725511b5a | underdog | Legend Glasker | Receptions | under | 0.0939339008632083 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|b57be690-f19d-4c93-9059-74db24fa851c | underdog | Derrick Henry | Rush Yards | under | 0.09317962638787114 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|7cee03ac-78b3-4d7b-9754-834e5953a2f4 | underdog | Bryce Young | Rush Yards | under | 0.09215881426223937 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|9017c9d1-d4b6-4f91-be05-cd89711e572a | underdog | Derrick Henry | Rush + Rec Yards | under | 0.09211628908550895 | 2026-11-03T11:59:28Z | 2026-11-06T01:15:00Z |
| underdog|3643f56d-0243-4332-a358-5a0e8e33a064 | underdog | Brendan Baird | FG Made | under | 0.09178178550541316 | 2026-11-04T12:10:41Z | 2026-11-07T00:00:00Z |
| underdog|93a92a80-a9c0-4066-901b-6e9bb3e6ed82 | underdog | Mateen Bhaghani | XP Made | over | 0.09160309321993065 | 2026-11-04T12:10:41Z | 2026-11-07T17:00:00Z |
| underdog|891e30f8-7158-4065-8c46-b0bc62da09ae | underdog | Nate Frazier | Rush Yards | under | 0.09112227092117486 | 2026-11-04T12:10:41Z | 2026-11-08T00:30:00Z |
| underdog|21d71ac4-4518-4c20-a927-ee93fc159f14 | underdog | Cameron Dickey | Rush Yards | under | 0.09045418368836045 | 2026-11-04T12:10:41Z | 2026-11-08T02:30:00Z |
| underdog|d52dc310-ea00-4c21-bb95-3798608a708f | underdog | Quentin Johnston | Receptions | under | 0.08995109550904856 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|cc8ff1c4-2fcb-4c4c-af18-4a127eb7feb3 | underdog | Leonard Farrow | Rush Yards | under | 0.0896959331352698 | 2026-11-04T12:10:41Z | 2026-11-06T00:30:00Z |
| underdog|191ad2e3-f555-4222-9200-863334e65430 | underdog | Keelon Russell | Pass TDs | over | 0.08967851076359068 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|8da7c404-cb04-41ba-b938-8ff3599f80e5 | underdog | Noah Fifita | Pass Yards | under | 0.08943593369670233 | 2026-11-04T12:10:41Z | 2026-11-07T03:15:00Z |
| underdog|30c2e39e-bf25-4ab7-8130-054ae15d2165 | underdog | Kimani Vidal | Rush Yards | under | 0.08934185310329501 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|50f0cc28-915a-4dd2-ae88-cf03efcede73 | underdog | Caleb Douglas | Receiving Yards | under | 0.08861402690077047 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|7654abf8-5803-42de-aedf-d9f2b8287091 | underdog | Sam Leavitt | Pass Yards | under | 0.08859798975792943 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|97528620-100f-4ff8-bdaf-28d77419865d | underdog | Savion Williams | Receiving Yards | under | 0.08856960710705053 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|06cdafae-7a83-47d5-b1fd-aa62835f03d4 | underdog | Chris Olave | Receptions | under | 0.0884086875583634 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|dc4a83e2-3137-4afd-a2d6-b5c8c8f9f2e6 | underdog | Justice Hill | Receiving Yards | under | 0.08813754375680705 | 2026-11-04T12:10:41Z | 2026-11-06T01:15:00Z |
| underdog|47cec350-6d8d-442d-8a9d-7cb64d51ca35 | underdog | Nate Roberts | Receiving Yards | over | 0.08795420739677307 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|c4f3253c-3c43-48da-989e-430a41e60938 | underdog | Ethan Grunkemeyer | Pass TDs | over | 0.08701299636099313 | 2026-11-04T12:10:41Z | 2026-11-07T00:00:00Z |
| underdog|8e0a482a-9348-4990-9ac8-325c2d8f6cd7 | underdog | Sam LaPorta | Receiving Yards | under | 0.08668859616617386 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|d841a892-a21f-46e6-bc65-e0c20662a38e | underdog | Travis Hunter | Receptions | over | 0.08655057759181062 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|de0e129b-50fb-4ad3-af58-61dedd2d5451 | underdog | Tetairoa McMillan | Receiving Yards | under | 0.08645743049382315 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|30d142c6-8017-4e94-b781-4eb760e26d96 | underdog | Evan McPherson | Kicking Points | under | 0.08624660748610669 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|3c25e1f6-5855-4e10-b07c-c168b58f8e8b | underdog | Andre Szmyt | Kicking Points | under | 0.08606085228469695 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|905709ae-0ade-40a9-bd3d-a0bf427ddf75 | underdog | Kenneth Walker III | Rush + Rec Yards | under | 0.0851144565638311 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|9a11ea53-966f-452f-a1c2-ab1154cc943e | underdog | Jalen Coker | Receptions | under | 0.08455880625865009 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|b0730afb-5658-4515-9649-4569440f87d3 | underdog | Jordan Dwyer | Receptions | under | 0.0844983292993815 | 2026-11-04T12:10:41Z | 2026-11-07T03:15:00Z |
| underdog|a8b4d56b-3190-4729-a3e3-fa4952f7fe19 | underdog | Malachi Fields | Receptions | under | 0.08444567676815706 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|73ac4d64-aaad-4fcb-9557-df787fb34605 | underdog | Reice Griffith | FG Made | over | 0.08391603718080415 | 2026-11-04T12:10:41Z | 2026-11-05T00:00:00Z |
| underdog|1cf10def-da38-4ff8-ae2b-ed870438b843 | underdog | Drew Sample | Receptions | over | 0.0839013767051019 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|066fc569-e18b-4e8e-a0ef-474a26367226 | underdog | Rashod Bateman | Receiving Yards | over | 0.08376752430324541 | 2026-11-04T12:10:41Z | 2026-11-06T01:15:00Z |
| underdog|8984ae54-5d9c-420f-b668-58ea0c8178c5 | underdog | KC Concepcion | Receiving Yards | under | 0.08376331939036208 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|de3a28c0-990e-45e6-b955-eb21bc4ad9a4 | underdog | Patrick Mahomes | Rush Yards | under | 0.08365133891580678 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|a862f215-05b2-41f1-b321-fdf2e05a97a8 | underdog | J.K. Dobbins | Rush + Rec Yards | under | 0.08350036786571535 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|bef17621-f7f3-4d07-924b-e623b34c8d46 | underdog | Michael Salgado-Medina | FG Made | over | 0.08281383712782858 | 2026-11-04T12:10:41Z | 2026-11-07T03:15:00Z |
| underdog|db8a215c-a32b-461f-a74f-392bfed6cd47 | underdog | Sam LaPorta | Receptions | under | 0.08195280346786493 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|f28458a4-47e6-4da8-a937-f0ae0f4d0549 | underdog | Bear Bachmeier | Pass TDs | under | 0.08166979261822749 | 2026-11-04T12:10:41Z | 2026-11-07T17:00:00Z |
| underdog|0767ecdc-6c88-403c-a631-567d0902ae5f | underdog | Bijan Robinson | Receptions | under | 0.08140314785642488 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|d6f2f6f9-7c2b-436b-8597-589fa149c149 | underdog | Dakorien Moore | Receptions | under | 0.0811338453354351 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|3f37b916-250a-4972-965b-ecb6efeb0ce3 | underdog | Chris Bell | Receiving Yards | under | 0.08090076495058063 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|a93191dc-5ab3-4d60-9b3c-0635b721460f | underdog | Baker Mayfield | Rush Yards | under | 0.0804542415617544 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|12bd4374-687f-4ccd-8483-775c124afda4 | underdog | Khalil Shakir | Receptions | under | 0.08011792675984464 | 2026-11-04T12:10:41Z | 2026-11-10T01:15:00Z |
| prizepicks|16609136 | prizepicks | Tomas Martin Etcheverry | Total Games Won | over | 0.07995249100898583 | 2026-11-04T12:10:41Z | 2026-11-04T07:40:00.000-05:00 |
| underdog|a313aef7-90e0-4414-8c8e-e66290d3ad2b | underdog | James Cook | Rush Yards | under | 0.0794670395584336 | 2026-11-04T12:10:41Z | 2026-11-10T01:15:00Z |
| underdog|a2f8424e-28d4-487d-9875-bae9673e09e0 | underdog | Dylan Raiola | Pass TDs | under | 0.0793130185765103 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| prizepicks|16644346 | prizepicks | Laura Samson | Total Games | over | 0.07906446165005843 | 2026-11-04T12:10:41Z | 2026-11-04T11:00:00.000-05:00 |
| underdog|8e108182-4c87-46e4-9018-ab3d52427b04 | underdog | Brian Thomas | Receptions | over | 0.07859887169586088 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|b26c659b-559e-4818-854d-5118f2c3403c | underdog | Ed Small | Receptions | over | 0.07823065203309115 | 2026-11-04T12:10:41Z | 2026-11-07T03:15:00Z |
| underdog|4e78b0cf-ba79-4645-9eef-18616e239d26 | underdog | Ryan Fitzgerald | Kicking Points | under | 0.07806948496608823 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|9cc6d7af-582b-4a55-b998-6d8b9a90cae1 | underdog | Trevor Lawrence | Pass TDs | under | 0.07694789832016491 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|99f3ae4b-6e3f-48d9-a87c-1281715f1b43 | underdog | Nolan James | Rush Yards | under | 0.0769268807412854 | 2026-11-03T02:21:46Z | 2026-11-08T00:30:00Z |
| underdog|374f597e-854d-4418-8329-9618f7343eaa | underdog | Michael Petro | XP Made | under | 0.07677360225334395 | 2026-11-04T12:10:41Z | 2026-11-06T00:30:00Z |
| underdog|b037dd4d-81a9-4275-bf43-602a7252c49e | underdog | George Pickens | Receptions | under | 0.0766522668294094 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| prizepicks|16566879 | prizepicks | Drake London | Recs | under | 0.07645666700581077 | 2026-11-04T12:10:41Z | 2026-11-08T09:30:00.000-05:00 |
| prizepicks|16578153 | prizepicks | Bhayshul Tuten | Rec Targets | under | 0.07632106872332856 | 2026-11-03T02:21:46Z | 2026-11-05T20:15:00.000-05:00 |
| prizepicks|16624991 | prizepicks | Alex Michelsen | Total Games Won | over | 0.076053975730065 | 2026-11-04T12:10:41Z | 2026-11-04T13:00:00.000-05:00 |
| underdog|b0f90105-2991-41ea-bc6c-2264f297449b | underdog | Nate Boerkircher | Receptions | under | 0.07569655692539734 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|3db483c9-2cbd-4a61-a415-da9945e7783b | underdog | J'Koby Williams | Rush Yards | under | 0.0751641814121301 | 2026-11-04T12:10:41Z | 2026-11-08T02:30:00Z |
| underdog|c9f42cb3-782a-42ae-8d36-b838a2e16e5b | underdog | Tyler Goodson | Receptions | under | 0.07447307028831152 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|2a09662c-9e69-4f3f-922f-fcdb9b98b17f | underdog | Tee Higgins | Receiving Yards | under | 0.07428759040645827 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|ebc419a7-0a1d-40cd-9537-5616da066033 | underdog | Camden Coleman | Pass TDs | over | 0.07415791142401901 | 2026-11-04T12:10:41Z | 2026-11-06T01:00:00Z |
| underdog|f7c17ddd-b7da-47e1-b7cc-3c831055be6b | underdog | Dominic Zvada | FG Made | under | 0.0741063683238431 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|ae08266e-6845-4eb5-8ae0-c55a994092c7 | underdog | Dylan Raiola | Pass Yards | under | 0.07375588900233532 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|a06d5616-3ce4-4197-850d-f0b0c73b34d5 | underdog | Drake Maye | Rush Yards | under | 0.0735599469387288 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| prizepicks|16576406 | prizepicks | Kyren Williams | Rush Yards | under | 0.0734640730790519 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|98370739-8ce7-4116-9352-2a9e7a795fa3 | underdog | C.J. Stroud | Pass TDs | under | 0.07344784426946727 | 2026-11-03T02:21:46Z | 2026-11-08T21:05:00Z |
| underdog|5b70e14f-144b-40c0-a3ac-91c3c7b9c69b | underdog | Emmett Johnson | Receiving Yards | over | 0.07340212124411849 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|5f0b23b3-c959-4870-8412-71a8ccc5d09d | underdog | Michael Penix | Rush Yards | under | 0.07331631931313753 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|c10a0922-5357-4d12-a34a-fef19f41ae93 | underdog | Dylan Sampson | Receptions | under | 0.073210778810199 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| prizepicks|16577044 | prizepicks | Chig Okonkwo | Rec Yards | under | 0.07319171131719704 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|126188b0-7b25-4684-b82a-c40972332c2b | underdog | Gunner Stockton | Pass Yards | under | 0.07289838569890572 | 2026-11-04T12:10:41Z | 2026-11-08T00:30:00Z |
| underdog|5c589e9f-50cb-4f4d-bc6c-31a94652a555 | underdog | Darren Waller | Receptions | under | 0.07257323185856346 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|60d4c44c-f10d-4e36-a661-dd1c631f3414 | underdog | Omar Cooper | Receptions | under | 0.07236240548376671 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|2654ed1f-f909-41a8-9668-e28a31a28973 | underdog | Bhayshul Tuten | Receiving Yards | over | 0.07230312851767462 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|1adc0acb-33e0-4c49-8afc-9b6c4b1a14fd | underdog | Derrick Henry | Receptions | under | 0.07220955982843835 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|5decb5a9-f1ab-48b5-bdf2-ec7cff2a45da | underdog | Dominic Zvada | Kicking Points | under | 0.07189248960202987 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|ac77ab58-0289-4973-976b-a2333a4b5231 | underdog | Bucky Irving | Receiving Yards | under | 0.07090392613756524 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|01068677-aea6-428e-b880-63933e5e7c56 | underdog | Kwazi Gilmer | Receptions | under | 0.07076791839692675 | 2026-11-04T12:10:41Z | 2026-11-07T01:00:00Z |
| underdog|809ce3ed-a6d6-4419-9069-ddbb0a938b7e | underdog | Elijah Faulkner | Rush Yards | under | 0.07062250729199371 | 2026-11-04T12:10:41Z | 2026-11-05T00:00:00Z |
| underdog|dc7085a5-bd2b-4e90-9aa5-7e11f5f57193 | underdog | Dohnte Meyers | Receptions | under | 0.07018273167311495 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|2e941ef0-d7f5-4f4c-8018-abecc0ca312c | underdog | Nate Boerkircher | Receiving Yards | over | 0.07009713968929643 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|4f42e71e-9977-4467-9c6f-587a1fb01921 | underdog | Malik Willis | Pass TDs | under | 0.0698898131874599 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| prizepicks|16576408 | prizepicks | Javonte Williams | Rush Yards | under | 0.06913799764143458 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|7d1040e5-04ee-4e25-8fbf-f12f99828e9e | underdog | Cam Skattebo | Receptions | under | 0.06884453220929898 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|4b82770a-7a57-4eae-87eb-44aba7f2eb02 | underdog | Noah Gray | Receptions | under | 0.06840206314519737 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|b8c47a57-f800-4f0c-885f-f5ff1d8c731a | underdog | Trevor Lawrence | Rush Yards | under | 0.06787768680871364 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|a41d4208-558b-4e9e-ace0-423efa6d914f | underdog | Brendan Baird | XP Made | under | 0.06786423255342389 | 2026-11-04T12:10:41Z | 2026-11-07T00:00:00Z |
| underdog|aa2400e1-61c6-42b8-a00e-4df185d8e29a | underdog | Peyton Woodring | XP Made | over | 0.06770360800211805 | 2026-11-04T12:10:41Z | 2026-11-08T00:30:00Z |
| underdog|b4a11205-f19f-4256-9e1e-6703e6a4644a | underdog | Jaylen Waddle | Receptions | under | 0.06756067788820463 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|480b8a53-750b-4531-914d-b24d9cc3be67 | underdog | Gunner Stockton | Pass TDs | over | 0.06653840324761084 | 2026-11-04T12:10:41Z | 2026-11-08T00:30:00Z |
| underdog|d4f2b5ca-0b3f-4658-962d-e49d13b62596 | underdog | Mike Gesicki | Receptions | under | 0.06624716319361124 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|17d196b6-916b-4467-86c8-3e43337d1b9d | underdog | Josh Jacobs | Receiving Yards | under | 0.06580018595374104 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|cf323095-2321-408c-89fd-7d1d5f7d89a0 | underdog | Javonte Williams | Receptions | under | 0.06563070619990474 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|e2076474-ba9e-4c4a-8a5e-8756583f0c4e | underdog | Woody Marks | Receiving Yards | under | 0.06554944061032464 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|3bd3bab1-6fee-4e45-9094-a8744ea6587c | underdog | Keelon Russell | Pass Yards | under | 0.06553248219961838 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|84c8ff8f-479b-4e5a-91df-b47cb4924be2 | underdog | Xavier Worthy | Receptions | under | 0.06547220658559605 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|7a1d759e-64e7-41bd-af94-dcd4d25dbeb7 | underdog | Kenneth Walker III | Rush Yards | under | 0.06528010484919622 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|ad36e65d-c7a8-4a0e-8d4c-a2b596d93edb | underdog | Cameron Dicker | Kicking Points | under | 0.06479235639855563 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|e00a37ed-d410-4482-ad2c-a051ecd9d5f1 | underdog | Jeffrey Overton | Receiving Yards | over | 0.06457901851406311 | 2026-11-04T12:10:41Z | 2026-11-07T00:00:00Z |
| underdog|1e146d1e-95ac-4e18-b97f-874278e4440b | underdog | Emmett Johnson | Rush Yards | under | 0.06444132725080376 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|de701dad-dc41-4c39-b386-ddaa87ab0c04 | underdog | J.K. Dobbins | Rush Yards | under | 0.06421471109901433 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|37660a08-dd6f-471b-8821-195e3f484c98 | underdog | Deshaun Watson | Rush Yards | under | 0.06384461069907932 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|c9cba434-16a2-44a1-acf3-d92dc9f828a5 | underdog | Ja'Kobi Lane | Receiving Yards | under | 0.06358680985081022 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|21931440-adec-46d4-b530-994878d9e427 | underdog | T.J. Hockenson | Receptions | under | 0.06344057443403939 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|9e4ac678-53eb-48dd-9eb6-5829262bab83 | underdog | Bear Bachmeier | Pass Yards | under | 0.06313209167616829 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|4a904250-e9de-4e18-92c0-892c286a7ec0 | underdog | Jabari Smith | Receiving Yards | over | 0.062386863455661024 | 2026-11-04T12:10:41Z | 2026-11-05T00:00:00Z |
| prizepicks|16622151 | prizepicks | Taylor Fritz | Total Games | over | 0.061670395845261794 | 2026-11-04T12:10:41Z | 2026-11-04T08:50:00.000-05:00 |
| prizepicks|16577034 | prizepicks | Denzel Boston | Rec Yards | under | 0.06162987154195598 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|3fcc0c03-2591-4dd0-b14b-c923f2c57f01 | underdog | Darian Mensah | Pass TDs | over | 0.06129839754242772 | 2026-11-04T12:10:41Z | 2026-11-08T00:30:00Z |
| underdog|ec27f580-1a71-4c96-833a-5b2bb78974b7 | underdog | Evan Engram | Receiving Yards | under | 0.06123051749536734 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|8c265bcd-7b60-4798-8607-03c1259a21e4 | underdog | Trey Smack | FG Made | under | 0.06104007152947344 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|f5d504e6-2b53-4eb6-bf8c-868ed6d671c4 | underdog | Cyrus Allen | Receiving Yards | under | 0.060834544249166234 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|07cbccc8-0fba-4542-8414-c5920607d6bf | underdog | Kevin Jennings | Pass Yards | under | 0.06069823598347823 | 2026-11-04T12:10:41Z | 2026-11-07T00:00:00Z |
| underdog|2e60e4ca-c287-4928-a19f-b526008bed0c | underdog | Dalton Kincaid | Receiving Yards | under | 0.06026883839015584 | 2026-11-04T12:10:41Z | 2026-11-10T01:15:00Z |
| underdog|bfe23dd9-356e-415c-a095-bd4a6fb3ffde | underdog | Devaughn Vele | Receptions | under | 0.06024795187111609 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|99a6085b-1064-4093-9351-7582b8a8a281 | underdog | Garrett Wilson | Receptions | under | 0.05978302669415658 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|be36f808-dbd3-4226-adee-a8537113a1e5 | underdog | Ethan Grunkemeyer | Pass Yards | under | 0.05966040798874328 | 2026-11-04T12:10:41Z | 2026-11-07T00:00:00Z |
| underdog|b616e371-482e-4731-8abc-6f8beee55185 | underdog | Adjatay Dabbs | Receiving Yards | under | 0.05961542071150383 | 2026-11-04T12:10:41Z | 2026-11-05T00:00:00Z |
| underdog|1d902e2b-3919-4c19-b84a-8ffa99b10e62 | underdog | Brenton Strange | Receptions | under | 0.05946848028138785 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|08232b78-fe17-41d7-87da-edc95136c5f1 | underdog | Juwan Johnson | Receiving Yards | under | 0.05935519841942771 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|52ee049e-693a-4c59-9f9f-9fb009989ba6 | underdog | Harold Mack | Receiving Yards | over | 0.05931117214696269 | 2026-11-04T12:10:41Z | 2026-11-05T00:30:00Z |
| underdog|fe4d076e-daf4-4620-a5d9-81c9dcde46d9 | underdog | Mark Andrews | Receptions | under | 0.059115555543941656 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|3b554414-84d2-41b4-93ac-fceb51bfce89 | underdog | Dilin Jones | Receptions | under | 0.05910993829171962 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|41f2b902-44c6-48b4-9eee-82534c0b54f4 | underdog | Justice Hill | Rush + Rec Yards | under | 0.0590474598746793 | 2026-11-04T12:10:41Z | 2026-11-06T01:15:00Z |
| underdog|285dab5f-ea1a-4d60-a385-159091689a27 | underdog | Savion Williams | Receptions | under | 0.058569519420755056 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|afda48e8-0d61-4673-aecd-d18deb0ca8b9 | underdog | Ed Small | Receiving Yards | over | 0.05839356214069036 | 2026-11-04T12:10:41Z | 2026-11-07T03:15:00Z |
| underdog|f6a0cb16-5759-468b-93f6-772a13d42630 | underdog | Marvin Mims Jr. | Receiving Yards | under | 0.05807117435666043 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|089ce83f-49f9-46ad-83c1-06b27856f11e | underdog | Tyler Shough | Pass TDs | under | 0.0579713928349842 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|ef93512e-7037-4e52-adab-e5a0e92cb14b | underdog | Kyler Kasper | Receptions | under | 0.0577929902830534 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|03683cb5-d08b-46d2-8daf-b7a187b04861 | underdog | Collin Dixon | Receiving Yards | under | 0.05774001382855143 | 2026-11-04T12:10:41Z | 2026-11-07T01:00:00Z |
| underdog|363f2a86-aea7-488d-8f25-6c2926e28588 | underdog | Michael Penix | Pass TDs | under | 0.05769866616807584 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|6cea53c4-9d13-4b3e-8f35-09016359467a | underdog | Katin Houser | Pass TDs | over | 0.05741840076591065 | 2026-11-04T12:10:41Z | 2026-11-07T01:00:00Z |
| underdog|4ed6c534-a882-4037-a5c5-3d3c36ee0467 | underdog | Jordan Faison | Receiving Yards | under | 0.05721438415905 | 2026-11-03T02:21:46Z | 2026-11-08T00:30:00Z |
| underdog|e705b9ff-1dc6-4f77-b9a5-e0e842d13aa2 | underdog | Michael Wilson | Receiving Yards | under | 0.05719341092584018 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| prizepicks|16577046 | prizepicks | CeeDee Lamb | Rec Yards | under | 0.0563405843653354 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| prizepicks|16623321 | prizepicks | Isaiah Mizell | Recs | under | 0.05613807100115675 | 2026-11-04T12:10:41Z | 2026-11-06T22:15:00.000-05:00 |
| underdog|fa5fce7c-1ad5-412b-aabf-7565370e86f6 | underdog | Nate McCashland | FG Made | under | 0.056080710226557806 | 2026-11-04T12:10:41Z | 2026-11-07T03:15:00Z |
| underdog|48603add-d136-41df-b578-2323b8a1caa7 | underdog | Rome Odunze | Receptions | under | 0.05570918963942184 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|fded4867-36f9-448a-8735-b41071d2dd45 | underdog | Camden Coleman | Pass Yards | under | 0.0555391812713939 | 2026-11-04T12:10:41Z | 2026-11-06T01:00:00Z |
| underdog|2e9a220f-7272-467e-b8e3-61ae45f85737 | underdog | Kenneth Walker III | Receiving Yards | under | 0.05507859411436211 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|db5a41ef-fc1d-4035-aa5e-7a30cf987986 | underdog | Troy Franklin | Receiving Yards | under | 0.05495631871264228 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|e2c22ff1-6209-4e3e-bbac-653eba1f1994 | underdog | Wayshawn Parker | Receiving Yards | over | 0.05434117214846301 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| prizepicks|16577036 | prizepicks | KC Concepcion Jr. | Rec Yards | under | 0.054101039282902996 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|cce8999b-73b6-4a3b-a40d-76aad63c8cba | underdog | Drake Lindsey | Pass Yards | under | 0.05406000313128101 | 2026-11-04T12:10:41Z | 2026-11-07T17:00:00Z |
| underdog|e01ed5ff-4bf0-4328-80bb-372c2a56d1cb | underdog | Jeremiah Smith | Receptions | under | 0.053719870131973324 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| prizepicks|16576403 | prizepicks | Quinshon Judkins | Rush Yards | under | 0.05350422507148955 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|2f6615ec-e303-4723-8de9-515407930761 | underdog | Kedrick Reescano | Rush Yards | under | 0.05350218820934205 | 2026-11-04T12:10:41Z | 2026-11-07T03:15:00Z |
| underdog|71d9b967-8695-476c-a378-0a790c548319 | underdog | Nyziah Hunter | Receiving Yards | under | 0.053407546528774996 | 2026-11-04T12:10:41Z | 2026-11-07T01:00:00Z |
| underdog|bbe5db1f-ec2b-4a91-83d5-67a2eb6dd543 | underdog | Bucky Irving | Rush + Rec Yards | under | 0.052973897403356895 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|c56012e4-30e8-4196-bad4-730dcf525d19 | underdog | Ja'Kobi Lane | Receptions | under | 0.05292315297453021 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|27464760-8c59-4037-b749-3733f4a504cd | underdog | J.K. Dobbins | Receiving Yards | over | 0.052791170452059166 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|6a12afa7-eab7-4b3f-81dc-0806d2113ac5 | underdog | Reice Griffith | XP Made | under | 0.05262596560808974 | 2026-11-04T12:10:41Z | 2026-11-05T00:00:00Z |
| underdog|c576f022-bc2d-4dc5-977d-7e4dc4f852fc | underdog | Bijan Robinson | Receiving Yards | under | 0.052599299690431756 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|f4af8d61-8588-4d80-ac8d-fd8686a33979 | underdog | Malik Willis | Rush Yards | under | 0.052470845197019944 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|4268d138-80dd-44fb-8f09-ac7bb509ef59 | underdog | Tyler Goodson | Receiving Yards | over | 0.052016336879189495 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|7c09637f-ba5b-48d9-a7b4-45cc01362313 | underdog | Justin Herbert | Rush Yards | under | 0.05178516711907766 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|cc22fac7-2f59-456b-9cae-e6eb0d0a9e39 | underdog | Troy Franklin | Receptions | under | 0.05174111879222043 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|cff2f20d-c0f8-478c-a322-03efc0d1ab97 | underdog | Caleb Cunningham | Receiving Yards | over | 0.05142102235991175 | 2026-11-04T12:10:41Z | 2026-11-08T00:30:00Z |
| underdog|663dc645-fc87-463b-a68e-bf2e97ecda97 | underdog | Darian Mensah | Pass Yards | under | 0.05089906872032768 | 2026-11-04T12:10:41Z | 2026-11-08T00:30:00Z |
| underdog|b4bf9f2b-e849-446b-a805-eda4d01af7be | underdog | Khalil Shakir | Receiving Yards | under | 0.05058312311415858 | 2026-11-04T12:10:41Z | 2026-11-10T01:15:00Z |
| underdog|97875f93-6930-4cda-9c97-1ad33e8d4022 | underdog | Harold Fannin | Receiving Yards | under | 0.04999003573194083 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|d014a1a2-0d40-4dfc-b478-da703028bd90 | underdog | Kendrick Raphael | Rush Yards | under | 0.0493823595087185 | 2026-11-04T12:10:41Z | 2026-11-07T00:00:00Z |
| underdog|ed56e197-54b7-4d14-9254-cc19f9dfbd99 | underdog | Yannick Smith | Receiving Yards | under | 0.04899083677379246 | 2026-11-04T12:10:41Z | 2026-11-07T00:00:00Z |
| prizepicks|16577037 | prizepicks | Chris Olave | Rec Yards | under | 0.04898251964490763 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|b73b2349-67bd-4725-869e-3e946a7c225e | underdog | Jakobi Meyers | Receptions | under | 0.04885583654522818 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|cdea3734-6a4c-48b4-9b84-869b97a4bf61 | underdog | Keldric Luster | Pass TDs | over | 0.04791724992833729 | 2026-11-04T12:10:41Z | 2026-11-05T00:00:00Z |
| underdog|0729c05e-e380-4efb-b2ae-e1403174fb84 | underdog | Samaje Perine | Receptions | over | 0.04737537544984716 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| prizepicks|16567035 | prizepicks | Jordan Love | Pass TDs | under | 0.04710112679060341 | 2026-11-04T12:10:41Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|cc6e8fa9-fd9c-4ef8-b198-bb27be272161 | underdog | Quinshon Judkins | Receptions | over | 0.04707698015484607 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|e5156db0-79be-42ba-8302-5fcd0cfd7d61 | underdog | Ethan Moczulski | XP Made | over | 0.046690949261277925 | 2026-11-04T12:10:41Z | 2026-11-07T01:00:00Z |
| underdog|79efae80-1726-417d-9fba-673881fec86c | underdog | Kyler Kasper | Receiving Yards | under | 0.046656667808123276 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|d3bf6324-2946-408d-8923-048c559dfff8 | underdog | Jahmyr Gibbs | Receiving Yards | under | 0.04649516222888994 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|60ae2057-2007-4cae-9f42-087799172fc0 | underdog | Brenton Strange | Receiving Yards | under | 0.04608906136624302 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|4fc85cf5-e79e-4bc5-aacc-88688db334d4 | underdog | Ty Dieffenbach | Pass Yards | under | 0.04552768234336835 | 2026-11-04T12:10:41Z | 2026-11-07T17:00:00Z |
| underdog|e4023e77-9713-4947-a229-d8d0c01daa5c | underdog | Jojo Phillips | Receiving Yards | over | 0.04551214414039517 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| prizepicks|16578154 | prizepicks | Brenton Strange | Rec Targets | under | 0.045215014696700084 | 2026-11-03T02:21:46Z | 2026-11-05T20:15:00.000-05:00 |
| underdog|fb09c8f8-3ddb-4f94-af1e-f2ab7b5179ca | underdog | Grant Meadors | FG Made | over | 0.045169378847931485 | 2026-11-04T12:10:41Z | 2026-11-05T00:00:00Z |
| underdog|631d77f9-8605-4a67-aad4-017f6922271b | underdog | Isaiah Mizell | Receiving Yards | under | 0.04506296792047704 | 2026-11-04T12:10:41Z | 2026-11-07T03:15:00Z |
| underdog|51e7af2b-f9a1-43ea-aa78-584f372553e2 | underdog | Trey Smack | Kicking Points | under | 0.04455434973971151 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|e5d081ab-9efa-43d3-bfb8-a43e2d593f85 | underdog | Drake Maye | Pass TDs | under | 0.04430737897190651 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|f9a76c6b-34a5-4243-a5ac-d0c7c9e1014a | underdog | Mark Fletcher Jr. | Rush Yards | under | 0.04410149704615496 | 2026-11-03T02:21:46Z | 2026-11-08T00:30:00Z |
| underdog|997e67da-c8d3-4a83-9610-e8d3e6b73ebb | underdog | Caleb Odom | Receiving Yards | over | 0.0440665088048563 | 2026-11-04T12:10:41Z | 2026-11-08T00:30:00Z |
| underdog|5e087ca0-c81b-466a-a4ab-b25feaca7f84 | underdog | Noah Bennee | Receiving Yards | over | 0.04389551607024966 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|46e3d4a9-5052-4f6b-9df2-d71dac46eb5f | underdog | Derrick Henry | Receiving Yards | over | 0.0437423600982455 | 2026-11-03T11:59:28Z | 2026-11-06T01:15:00Z |
| underdog|9f8d5a76-cbb3-4565-b2d4-601b302e1c66 | underdog | Jojo Phillips | Receptions | over | 0.04343832039629403 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|10896a71-38d6-4d0a-ba05-1619df431b90 | underdog | Jackson Sharman | Pass Yards | under | 0.043377147595038856 | 2026-11-04T12:10:41Z | 2026-11-05T00:00:00Z |
| underdog|c915c70f-8f54-4197-8611-3803fd334eba | underdog | Adam Trautman | Receiving Yards | over | 0.043328405440068996 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|c8c7079d-1a74-48ed-ae76-add235e9bf50 | underdog | Trinidad Chambliss | Pass TDs | over | 0.043317722650847656 | 2026-11-04T12:10:41Z | 2026-11-08T00:30:00Z |
| underdog|c2e9acd7-4e88-4f30-ae76-a25816dd4141 | underdog | Ricky Johnson | Receiving Yards | over | 0.043306631735705814 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|1cb4a3d5-3e86-4f3c-9e43-3fa7edb4fca9 | underdog | Raiden Brown | Receiving Yards | over | 0.043153731365787484 | 2026-11-04T12:10:41Z | 2026-11-05T00:00:00Z |
| prizepicks|16557917 | prizepicks | Jordan Love | Rush Yards | under | 0.0431179313386405 | 2026-11-03T02:21:46Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|fe7a85f2-c21c-4535-88b9-b246e6af4d70 | underdog | Jason Sanders | FG Made | over | 0.04309576984353114 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|a5088759-dcc4-4d0c-acb8-516ddb05b069 | underdog | Noah Fant | Receptions | over | 0.04270940205899032 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|a797f932-ce6e-4e56-9b01-1f5c227fbc2e | underdog | Samaje Perine | Receiving Yards | over | 0.04251414252076868 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| prizepicks|16578156 | prizepicks | Jakobi Meyers | Rec Targets | under | 0.04242041013161002 | 2026-11-03T02:21:46Z | 2026-11-05T20:15:00.000-05:00 |
| underdog|de6628da-2358-4822-a9a8-cf3d44824d9c | underdog | Zay Flowers | Receptions | over | 0.041882993253793854 | 2026-11-03T11:59:28Z | 2026-11-06T01:15:00Z |
| underdog|127ded5d-257a-4c2a-bb25-88e0bd0debad | underdog | Jordan Love | Rush Yards | under | 0.04127202084950954 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|6af1f579-11d3-4d3e-a5c5-36d75a14e37a | underdog | Bo Jackson | Receiving Yards | over | 0.04104279325152682 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|b4876ca4-f7e7-4fd2-ac05-6f01d5d72d89 | underdog | Justice Hill | Receptions | under | 0.040539917044618345 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| prizepicks|16577047 | prizepicks | Ryan Flournoy | Rec Yards | under | 0.04046234355837319 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|19911946-1f92-42a4-aa1c-15e5815fb816 | underdog | Tee Higgins | Receptions | under | 0.04018031305357561 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| prizepicks|16557901 | prizepicks | Jared Goff | Rush Yards | over | 0.03998049861167219 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| prizepicks|16557921 | prizepicks | Kyler Murray | Rush Yards | under | 0.0398853265542245 | 2026-11-03T02:21:46Z | 2026-11-09T20:15:00.000-05:00 |
| underdog|51793da7-f50f-4605-9f8b-5f37ddfbd171 | underdog | Jamari Johnson | Receptions | under | 0.039549403867083055 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|b510b6c8-aa64-436f-a890-a3ad7f41278d | underdog | Keelon Russell | Rush Yards | over | 0.03954798492547018 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| prizepicks|16577038 | prizepicks | Travis Kelce | Rec Yards | under | 0.039492224251563846 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|a02c710b-933f-4b18-907c-27053f219320 | underdog | Isaiah Likely | Receptions | under | 0.039343800400331586 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|9051164e-05e3-41a4-b605-6b9dae5d49a4 | underdog | Drake Lindsey | Pass TDs | under | 0.03931495181306932 | 2026-11-04T12:10:41Z | 2026-11-07T17:00:00Z |
| underdog|67227c17-ffd5-4f66-9765-3cd9776434fd | underdog | Javon Tracy | Receiving Yards | under | 0.03931316931304407 | 2026-11-04T12:10:41Z | 2026-11-07T17:00:00Z |
| underdog|cefb0596-2c7e-431b-8408-7a1ed12d8db4 | underdog | Bryce Young | Pass TDs | under | 0.039094010660283285 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|b928a5ef-308e-4395-97c3-f7cbc952337a | underdog | Ayden Greene | Receiving Yards | over | 0.038935127218449606 | 2026-11-04T12:10:41Z | 2026-11-07T00:00:00Z |
| underdog|7ec6b8e6-f4bc-4ceb-9977-2343e6cf733c | underdog | Patrick Overmyer | Receiving Yards | under | 0.03891506317250926 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|06d92faa-959d-4010-ab64-7447944a34ab | underdog | Caden VanHuis | XP Made | over | 0.03864279540819021 | 2026-11-04T12:10:41Z | 2026-11-05T00:30:00Z |
| underdog|7e7669a6-9cf5-4f0f-9b42-7af12752dc41 | underdog | Evan Stewart | Receiving Yards | over | 0.0384686535093306 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|d1d3e66e-276b-43d4-9e06-fe5ed3964b6c | underdog | Geno Smith | Pass TDs | over | 0.038346590420210214 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|0071a601-862e-44fa-ab60-3a5c7d3aaaf9 | underdog | Ryan Flournoy | Receptions | under | 0.03817671228052344 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|30207658-d186-4c70-8ce0-0f79ac92f94f | underdog | Trae'shawn Brown | Rush Yards | over | 0.037999199829431785 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| prizepicks|16609161 | prizepicks | Karen Khachanov | Total Games | over | 0.037702032201934466 | 2026-11-04T12:10:41Z | 2026-11-04T09:30:00.000-05:00 |
| underdog|c9e2a183-7d96-4eaf-8ca8-3838a96ed892 | underdog | Ryan Flournoy | Receiving Yards | under | 0.03756251114817222 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|24cd298e-c323-419c-99a4-3aefd02e7505 | underdog | Caden Veltkamp | Pass TDs | over | 0.03709853986997952 | 2026-11-04T12:10:41Z | 2026-11-06T00:30:00Z |
| prizepicks|16646617 | prizepicks | Ugo Humbert | 1st Set Total Games | under | 0.03702755692783888 | 2026-11-04T12:10:41Z | 2026-11-04T10:40:00.000-05:00 |
| underdog|b1c944ba-9c90-4448-ad12-9ffc6ea4ffe1 | underdog | Malik Nabers | Receptions | under | 0.03702491255946161 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|2f401558-103b-44dd-b0ae-941e6998fc51 | underdog | Wayne Knight | Rush Yards | under | 0.03693588139563031 | 2026-11-04T12:10:41Z | 2026-11-07T17:00:00Z |
| underdog|54df54a9-e16c-4b99-aa65-293d5ba8e703 | underdog | Omar Cooper | Receiving Yards | over | 0.03625910747796235 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|119f4d77-645c-42cd-9e5d-3c3aa99ea03d | underdog | Cameron Dicker | FG Made | under | 0.03597583144986216 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|865227cf-17df-4e89-9c98-4311b47f982a | underdog | Tetairoa McMillan | Receptions | under | 0.03583202783628714 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| prizepicks|16576405 | prizepicks | Puka Nacua | Rush Yards | over | 0.035802440511908284 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|d3863d46-06f3-458d-b460-f6272d79e37f | underdog | Wayshawn Parker | Rush Yards | under | 0.03539702630366759 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|f77c4659-c571-4380-bb17-0f290c20cfdb | underdog | Braden Pegan | Receiving Yards | under | 0.03535065146715288 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|2f083c55-dfe0-4021-bc6a-5e7f16540cf5 | underdog | Ryan Fitzgerald | FG Made | under | 0.035264256773103186 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|43ce05c0-6560-4ef9-866d-9fa540761d25 | underdog | Elijah Higgins | Receiving Yards | under | 0.034975019147323816 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|642b6aa4-d8ad-47ca-a6e2-02bf1db1abde | underdog | Rhamondre Stevenson | Receptions | under | 0.03473410197552751 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| prizepicks|16557908 | prizepicks | Patrick Mahomes | Rush Yards | under | 0.034534369510793694 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| prizepicks|16578159 | prizepicks | Nate Boerkircher | Rec Targets | under | 0.0344311591015668 | 2026-11-03T02:21:46Z | 2026-11-05T20:15:00.000-05:00 |
| underdog|71a4edea-2598-40b1-97fa-ce6bcc620a20 | underdog | Kenyon Sadiq | Receptions | under | 0.03442572108508024 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|ad6f21f6-79ae-4c5d-a258-6ddedefe83f6 | underdog | Ka'imi Fairbairn | Kicking Points | under | 0.03438415374739645 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|b22893f7-7a36-49d0-aff9-c15df2d5deab | underdog | Trey'Dez Green | Receiving Yards | under | 0.03435452781320025 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|488c064e-4a42-4665-a6fc-407585fb9afe | underdog | Lawson Luckie | Receiving Yards | over | 0.03431423503130593 | 2026-11-04T12:10:41Z | 2026-11-08T00:30:00Z |
| underdog|66b37aff-aa69-48ba-984e-2a3c3e131cd4 | underdog | Tommy Tremble | Receptions | over | 0.03430222685481554 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|9f01e485-7324-47e4-9df3-b5b1bac12c11 | underdog | Sam Darnold | Rush Yards | over | 0.03399236213741741 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|c326b335-e702-421f-9f11-eec8ab8fdfaa | underdog | Dalton Schultz | Receiving Yards | under | 0.03359570617331076 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| prizepicks|16625054 | prizepicks | Taylor Fritz | Break Points Won | under | 0.03349653015238896 | 2026-11-04T12:10:41Z | 2026-11-04T08:50:00.000-05:00 |
| underdog|52aeb3b1-21f6-46b8-ac2b-fc5807bc0810 | underdog | Tommy Tremble | Receiving Yards | under | 0.03318632750764128 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|43d4f051-ed64-4b5e-904b-24f2c6efea26 | underdog | Samaje Perine | Rush Yards | under | 0.03301262915252379 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|a5fbd6d5-3e62-4a23-883d-9f5cf14d5654 | underdog | Shekai Mills-Knight | Rush Yards | under | 0.0327826010465021 | 2026-11-04T12:10:41Z | 2026-11-08T00:30:00Z |
| underdog|29834b95-ffb3-48a3-8130-df8f76762419 | underdog | Peyton Woodring | FG Made | over | 0.03151348868814757 | 2026-11-04T12:10:41Z | 2026-11-08T00:30:00Z |
| prizepicks|16619620 | prizepicks | Alexandra Eala | Break Points Won | under | 0.03149117435378479 | 2026-11-04T12:10:41Z | 2026-11-05T05:30:00.000-05:00 |
| underdog|654f922d-18fe-4a8a-908c-b90771f020ab | underdog | Mason Taylor | Receiving Yards | under | 0.031038269706022303 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|f7062588-3eb0-4f0e-b3fb-0c5e028853bd | underdog | Juwan Johnson | Receptions | over | 0.030368013536360206 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| prizepicks|16619153 | prizepicks | Novak Djokovic | Total Games | over | 0.03016178777027345 | 2026-11-04T12:10:41Z | 2026-11-04T08:40:00.000-05:00 |
