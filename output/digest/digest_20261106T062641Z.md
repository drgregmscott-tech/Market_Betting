# Pipeline Digest -- 2026-11-06T06:26:41Z

## Run summary
- Ingestion: 47623 rows (PrizePicks OK, Underdog OK)
- Estimation: 47623 rows estimated (from 47623 ingested props)
- CLV logging: 91 newly flagged, 0 newly closed, 925 still open (109034 total ever logged)

## Currently open flags
Sizing is a manual step (sizing_engine.py, Session 2.6) -- this table is what to scan to pick a pair worth sizing.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_edge | first_flagged_at | game_start_time |
|---|---|---|---|---|---|---|---|
| underdog|9eff3818-6fca-4bae-89ed-d1ef14a6fa24 | underdog | Shedeur Sanders | Pass Attempts | under | 0.42261306532663323 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| underdog|7984c1b8-4987-4395-9955-ab4b9006dd75 | underdog | Eddy Pineiro | FG Made | under | 0.41306807406928026 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|72f89744-f92a-449b-a0bb-cf8069d05cd8 | underdog | Jack Larsen | Receiving Yards | over | 0.4 | 2026-11-03T02:21:46Z | 2026-11-08T00:30:00Z |
| underdog|3fb4f5c1-99aa-4469-8c43-2255a6229eca | underdog | Caleb Williams | Pass Yards | under | 0.4 | 2026-11-05T12:22:13Z | 2026-11-09T01:20:00Z |
| underdog|f8712edc-1b94-4a23-93b0-f3a909f7347a | underdog | Drew Lock | Pass Attempts | under | 0.4 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|3e831f69-cf67-408d-9148-2f2a2205f140 | underdog | Brandon McManus | Kicking Points | under | 0.4 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|d71953b3-f84a-41de-8164-f5fbcaae145d | underdog | Malik Willis | Pass Yards | under | 0.4 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|a958d6b8-a05d-4422-9e27-954de20b555e | underdog | Brock Purdy | Pass Yards | under | 0.4 | 2026-11-05T22:06:44Z | 2026-11-08T21:25:00Z |
| underdog|d8ad0bb9-b405-4c0c-ae21-8bf79eeeb536 | underdog | Josh Jacobs | Rush Yards | under | 0.4 | 2026-11-05T22:06:44Z | 2026-11-08T21:25:00Z |
| underdog|ef491658-8813-4a6b-b4ba-95567d182453 | underdog | Shedeur Sanders | Rush Yards | under | 0.4 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| underdog|869349aa-5399-4c3f-b961-edd9aca6684e | underdog | Michael Penix | Pass Yards | under | 0.4 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|219e2a58-c671-46ae-b5ae-d1255e6cbb62 | underdog | Jack Bech | Receiving Yards | under | 0.4 | 2026-11-06T06:34:07Z | 2026-11-08T21:25:00Z |
| underdog|6f27da8d-bb0a-4f02-83f7-fc4ae893292c | underdog | Shedeur Sanders | Pass Yards | under | 0.4 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| underdog|268d2fc5-2abe-4849-b4a0-390d7485e453 | underdog | Caleb Williams | Pass Attempts | under | 0.4 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|92973889-f958-46e1-9d56-1a45851bb88e | underdog | Dak Prescott | Pass Yards | under | 0.4 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|de26ab9a-3ba2-440e-a2bf-2a103bb05bc9 | underdog | Carson Wentz | Pass Yards | under | 0.4 | 2026-11-05T22:06:44Z | 2026-11-10T01:15:00Z |
| underdog|57a8861e-d69d-4cfe-936e-0c47010e012e | underdog | Jadarian Price | Receiving Yards | under | 0.4 | 2026-11-05T22:06:44Z | 2026-11-08T21:25:00Z |
| underdog|754ec181-3723-4eeb-9d81-6ac2f38d4b05 | underdog | Josh Allen | Pass Yards | under | 0.4 | 2026-11-04T12:10:41Z | 2026-11-10T01:15:00Z |
| underdog|47ec053c-388c-4d74-a581-14d22b98c92a | underdog | Carson Wentz | Pass Attempts | under | 0.4 | 2026-11-05T22:06:44Z | 2026-11-10T01:15:00Z |
| underdog|159c0350-eab4-41f1-b826-0de1e1e3b5bd | underdog | Justin Herbert | Pass Yards | under | 0.4 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|339df7bd-03f5-482d-ab9a-8634b6201c7e | underdog | Drew Lock | Pass Yards | under | 0.4 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|88a67ef6-decb-440a-98f8-fb4b22c34d26 | underdog | Brandon McManus | FG Made | under | 0.3956303597430939 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|87dc86a8-1b6c-4fe8-9e0a-55c0dda258af | underdog | Stefon Diggs | Receiving Yards | under | 0.39541758268765004 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|a31d98a6-bf53-440e-a5b5-a2b50e20038d | underdog | Bo Nix | Pass Yards | under | 0.39297059903848375 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|3457fac4-96e9-46e5-a38e-f8575853e01c | underdog | Jayden Daniels | Pass Yards | under | 0.3893084725552035 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|29356dc8-01cb-4b38-a414-1571c2ae47db | underdog | Baker Mayfield | Pass Yards | under | 0.386000173495637 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|91257feb-8a6e-4897-a344-a682b8f407f8 | underdog | Justin Herbert | Pass Attempts | under | 0.382571560879172 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|705e8042-bbe1-42e5-a50a-844d254c8900 | underdog | Kirk Cousins | Pass Yards | under | 0.3761461839014639 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|f9976ec1-4523-4b7a-bd0c-bca9b9dd4fb5 | underdog | Eddy Pineiro | Kicking Points | under | 0.3662333132187251 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|e3631ab4-a4e3-47d6-93c4-59cc4023bd88 | underdog | Daniel Jones | Pass Yards | under | 0.3637643979429024 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|927a0917-e0d0-4e12-ad02-7bc4c72c9b98 | underdog | DeSean Bishop | Receiving Yards | over | 0.3546355960210914 | 2026-11-05T12:22:13Z | 2026-11-07T23:15:00Z |
| underdog|20ded54a-d3d9-4991-b45f-4aab1465f143 | underdog | Jordan Love | Pass Yards | under | 0.35357762783010915 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| prizepicks|16557936 | prizepicks | Dak Prescott | Pass Yards | under | 0.35094246505677495 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| prizepicks|16557944 | prizepicks | Josh Allen | Pass Yards | under | 0.35094246505677495 | 2026-11-03T02:21:46Z | 2026-11-09T20:15:00.000-05:00 |
| prizepicks|16577043 | prizepicks | Stefon Diggs | Rec Yards | under | 0.35094246505677495 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| prizepicks|16722860 | prizepicks | Demarcus Robinson | Rec Targets | under | 0.35094246505677495 | 2026-11-06T06:34:07Z | 2026-11-08T16:25:00.000-05:00 |
| prizepicks|16557940 | prizepicks | Brock Purdy | Pass Yards | under | 0.35094246505677495 | 2026-11-03T02:21:46Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|76903731-5a31-4b71-aa02-3cf5f1f66632 | underdog | Jared Goff | Pass Yards | under | 0.34472431347503396 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|248aba17-77a9-49a7-96ad-e3085571e3b7 | underdog | Patrick Mahomes | Pass Yards | under | 0.34460651530387776 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|ccf6b612-28dd-444f-9b72-2ec8c5cafef7 | underdog | Deshaun Watson | Pass Yards | under | 0.33983627444145803 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|e9d2e9b2-53ab-4961-a149-c873d488c7e7 | underdog | Michael Penix | Pass Attempts | under | 0.3393140079675465 | 2026-11-05T22:06:44Z | 2026-11-08T14:30:00Z |
| underdog|d3d67fd6-1e23-402d-9e23-43cbc35a2f8c | underdog | Josh Allen | Pass Attempts | under | 0.33795668909357257 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| prizepicks|16557935 | prizepicks | Jayden Daniels | Pass Yards | under | 0.3359949609424918 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|37f53eaf-c7e4-4925-a45a-ca84b8d9ea68 | underdog | C.J. Stroud | Pass Yards | under | 0.33338439151254773 | 2026-11-05T22:06:44Z | 2026-11-08T21:05:00Z |
| underdog|91cd9a90-2bbb-4479-9d44-9025494f5dbb | underdog | Bo Nix | Pass Attempts | under | 0.33308348303432955 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|dfd26c17-46c2-49e7-80e7-7bd5bf224448 | underdog | Alonza Barnett | Pass Yards | under | 0.32277006367640626 | 2026-11-05T22:06:44Z | 2026-11-07T20:45:00Z |
| underdog|e6d5777b-8939-4202-8ed4-51f40d7be001 | underdog | Christian McCaffrey | Rush + Rec Yards | under | 0.3198836335711852 | 2026-11-05T22:06:44Z | 2026-11-08T21:25:00Z |
| underdog|efda5476-bc73-4e5c-8d29-c3b22c80a111 | underdog | Drake Maye | Pass Yards | under | 0.3169471849941047 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|c180ec24-04be-4d76-92bd-f2b1a7387ad4 | underdog | Josh Jacobs | Receptions | under | 0.3138562329893375 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| prizepicks|16718547 | prizepicks | Josh Jacobs | Rec Targets | under | 0.3126463971775677 | 2026-11-05T22:06:44Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|9b917f87-4065-4257-ba6e-cf63e69dd2b5 | underdog | Demarcus Robinson | Receiving Yards | under | 0.3106260675585195 | 2026-11-06T06:34:07Z | 2026-11-08T21:25:00Z |
| prizepicks|16557939 | prizepicks | Kirk Cousins | Pass Yards | under | 0.3094515764679242 | 2026-11-03T02:21:46Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|9d14ec55-11a1-45e7-b650-84b9a5ebf34c | underdog | J.J. McCarthy | Pass Yards | under | 0.304744428527313 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|37896abf-b78c-4078-bf55-90cf3966fe31 | underdog | Puka Nacua | Receiving Yards | under | 0.30330510113385567 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|953f2e63-4439-4406-97e7-6acf78bc2cee | underdog | Jadarian Price | Rush + Rec Yards | under | 0.3006267673891302 | 2026-11-05T22:06:44Z | 2026-11-08T21:25:00Z |
| underdog|5f0cd76c-a7f5-445c-83c0-0f0a646cceec | underdog | Brock Bowers | Receiving Yards | under | 0.29946639988592183 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|c276a65a-ae82-4954-9d4c-13d68aa92353 | underdog | Emeka Egbuka | Receiving Yards | under | 0.29901932004324594 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|b3820062-ff10-4245-afb1-048cb910cd60 | underdog | Brock Purdy | Pass Attempts | under | 0.29563370361590136 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|c1d7ae0f-d0c1-449e-be5b-2f61fd0f8ae7 | underdog | Shedeur Sanders | Pass TDs | under | 0.29393939393939406 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| underdog|33b0e243-2f4a-4a3e-9b10-fdf1a7f0985c | underdog | Bryce Young | Pass Yards | under | 0.2932756252152141 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|37eb3153-ffda-4141-b82c-9fe58b2797d9 | underdog | Saquon Barkley | Receptions | under | 0.29195979899497493 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|a4f7e2ea-445a-4746-9a01-bb8681efb55d | underdog | Drake Maye | Pass Attempts | under | 0.2890709907617405 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|b1871eee-1be7-4d3b-b76e-1f9f7f70baca | underdog | J.J. McCarthy | Pass TDs | under | 0.2875734861947701 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|7dc2a808-0f7f-4a12-a56c-9b8c0eb39095 | underdog | Thomas Castellanos | Pass Yards | under | 0.2822212178373662 | 2026-11-04T12:10:41Z | 2026-11-08T02:30:00Z |
| underdog|869e5022-5250-4ed5-aa69-9d68a2ffe1aa | underdog | Jarvis Green | Rush Yards | under | 0.2821015873424052 | 2026-11-05T22:06:44Z | 2026-11-07T17:00:00Z |
| underdog|dd2f4f79-4283-42e8-afb4-2092a78921a4 | underdog | Geno Smith | Pass Yards | under | 0.2812427694504944 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|c65ae7a0-14dd-4948-bd2b-2216fbebe1d1 | underdog | Daniel Jones | Pass TDs | under | 0.27974205004038677 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|95751aad-a038-411c-a867-51d3c11fc96c | underdog | Braden Atkinson | Pass Yards | under | 0.2786956332075442 | 2026-11-05T22:06:44Z | 2026-11-08T03:30:00Z |
| underdog|457dec03-fb15-48fc-bc38-09756507b0fb | underdog | Joe Burrow | Pass Yards | under | 0.2767456512747548 | 2026-11-05T22:06:44Z | 2026-11-08T14:30:00Z |
| underdog|df8dac90-be57-4491-8f0d-566482090ae9 | underdog | Corey Kiner | Receiving Yards | over | 0.27647574749151815 | 2026-11-06T06:34:07Z | 2026-11-08T21:25:00Z |
| underdog|a3499f76-dc57-40ca-a12b-ccab39f10be5 | underdog | Bryce Young | Pass Attempts | under | 0.27237481147034737 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|bd628484-6e46-438d-aedc-ed875436387c | underdog | Demarcus Robinson | Receptions | under | 0.2692251142156261 | 2026-11-06T06:34:07Z | 2026-11-08T21:25:00Z |
| underdog|2419efc4-e3a9-4d41-9ba4-8bc839a152e5 | underdog | Matthew Stafford | Pass Yards | under | 0.26613222526837244 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|5a0ff8aa-ab28-4f6c-9ec5-e95c971f8458 | underdog | Andy Borregales | Kicking Points | under | 0.2640899467628497 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|029429a0-88e2-4188-bb6a-963cd5a7c4e2 | underdog | Baker Mayfield | Pass TDs | under | 0.26332788339696256 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| prizepicks|16719183 | prizepicks | Saquon Barkley | Rec Targets | under | 0.26316628788845475 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|85a54f87-6df5-478c-84dd-35885591b2ce | underdog | Jadarian Price | Rush Yards | under | 0.26013202471957786 | 2026-11-05T22:06:44Z | 2026-11-08T21:25:00Z |
| underdog|3adb5b8e-9fc9-4c71-8c0d-2be1644fe037 | underdog | Jayden Daniels | Pass Attempts | under | 0.25997924896274693 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|8a93dc4a-7496-47f2-af11-b0faff063a96 | underdog | Antonio Williams | Receptions | under | 0.25960481049135886 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|81f4d26f-b937-419a-9eb5-47d6844b04eb | underdog | Robin Montgomery | Double Faults | under | 0.25955840929772456 | 2026-11-06T06:34:07Z | 2026-11-06T10:40:00Z |
| underdog|d484d774-fbd8-467b-bbfa-b6f85cfcf83f | underdog | Courtland Sutton | Receptions | under | 0.25834377385355134 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|c7d0412f-1aba-47dd-8ce0-e06060ca7b59 | underdog | Kyle Pitts | Receiving Yards | under | 0.25799821779938514 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|9d4fa631-2131-4a0c-9be8-fc96c08e2585 | underdog | Jake Weinberg | XP Made | over | 0.25701675995779105 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|42260fca-3f4a-4284-b57d-b9e07b027ca8 | underdog | Chase Brown | Rush + Rec Yards | under | 0.256995610592043 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| prizepicks|16557933 | prizepicks | Patrick Mahomes | Pass Yards | under | 0.256531424485161 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|88b26255-d953-47cf-aa2d-032da6db6cbf | underdog | Caleb Williams | Pass TDs | under | 0.256421951810362 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|7d8224fa-b4e1-41e0-a6a9-4bc8204d4355 | underdog | Courtland Sutton | Receiving Yards | under | 0.25289719817255274 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|25d18fbf-8c15-4a17-895c-3635dd1ce944 | underdog | Malik Willis | Pass Attempts | under | 0.2526482871588408 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|b72f06e1-815c-4c36-b978-4fcc8dfeeef1 | underdog | Andy Borregales | FG Made | under | 0.25213168723502966 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| prizepicks|16577042 | prizepicks | Puka Nacua | Rec Yards | under | 0.24801878589627235 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|e024fb9a-fb01-4280-b8d3-916ec7203a51 | underdog | Cooper Barkate | Receptions | under | 0.24425377274268656 | 2026-11-05T22:06:44Z | 2026-11-08T00:30:00Z |
| underdog|e84e4aa4-7537-48ef-99a7-49d36a0d5fc7 | underdog | Geno Smith | Pass Attempts | under | 0.2432377584583152 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|36f40fe9-a03a-493b-9f0f-897b45c681ba | underdog | Chris Godwin | Receiving Yards | under | 0.23879931607926252 | 2026-11-05T22:06:44Z | 2026-11-09T01:20:00Z |
| underdog|240a0d7b-e2a5-4220-94b5-19f2d695e3bd | underdog | George Kittle | Receiving Yards | under | 0.238058384025166 | 2026-11-06T06:34:07Z | 2026-11-08T21:25:00Z |
| underdog|086d3034-b329-4134-984b-2b6ded88d1f4 | underdog | Olamide Zaccheaus | Receiving Yards | under | 0.2371867613668348 | 2026-11-05T12:22:13Z | 2026-11-08T14:30:00Z |
| underdog|09559dbb-4dfd-4714-895d-7e3f21511df7 | underdog | Tyler Shough | Pass Yards | under | 0.23545769312634657 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|4e219bc4-540f-4254-8899-fb2c0a6c9ef1 | underdog | Jordan Love | Pass Attempts | under | 0.23509904882189492 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| prizepicks|16719160 | prizepicks | Brock Bowers | Rec Targets | under | 0.23351025534582692 | 2026-11-05T22:06:44Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|bba3c903-4ede-426b-98a4-5c60cb6bed88 | underdog | Jonah Coleman | Rush Yards | under | 0.233288763818978 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|a00ae86a-3ecc-4216-86f7-81d675f73f16 | underdog | Daniel Jones | Pass Attempts | under | 0.23121215443621368 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|d4b658ff-a41e-4bb2-9c00-52a5ed667ad4 | underdog | J.J. McCarthy | Pass Attempts | under | 0.22887506876878727 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|47a8aedd-ba46-4b2b-95b6-f2a2ae8ecb50 | underdog | D'Andre Swift | Rush + Rec Yards | under | 0.22773597443387839 | 2026-11-05T22:06:44Z | 2026-11-09T01:20:00Z |
| underdog|4e54a271-1412-4d2d-98d4-0ba49bfa6122 | underdog | Josh Jacobs | Rush + Rec Yards | under | 0.22766679996482564 | 2026-11-05T22:06:44Z | 2026-11-08T21:25:00Z |
| underdog|60cbaa38-c568-4879-a6f8-94b6e4e69559 | underdog | Tucker Kraft | Receiving Yards | under | 0.22559324997910668 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|58d83f19-bbad-408b-8378-a58d5e2757d3 | underdog | Antonio Williams | Receiving Yards | under | 0.22551109665563784 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|713b2721-78da-4cec-8f94-3e8a3e141d5d | underdog | Mike Washington | Receiving Yards | over | 0.22513540135851895 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|c1f72f3f-5755-4036-9793-3b0e1f55b9b2 | underdog | Rashee Rice | Receiving Yards | under | 0.2246943029433517 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|b7a27035-0410-4524-9b9f-8504019e9e93 | underdog | Malik Washington | Receiving Yards | under | 0.22383503418957196 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|631c967b-a514-419c-9c13-e3adac5b77c6 | underdog | Daylyn Upshaw | Receptions | under | 0.2217742619649793 | 2026-11-05T22:06:44Z | 2026-11-08T00:30:00Z |
| underdog|6d8eb0bb-0195-4e81-b62a-94edbb4b8341 | underdog | George Kittle | Receptions | under | 0.2205590308515778 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|6bbf2a5a-63d8-4774-b146-9892eacd1ce1 | underdog | Kirk Cousins | Pass Attempts | under | 0.21906706972458956 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|3d11ff54-e68e-46fd-9bee-9f64e201a532 | underdog | Ladd McConkey | Receptions | under | 0.2182531395719538 | 2026-11-03T02:21:46Z | 2026-11-08T21:05:00Z |
| underdog|bfe8c590-b7cd-46fa-97ef-a6f89b54cba6 | underdog | Christian McCaffrey | Rush Yards | under | 0.21748885231877868 | 2026-11-05T22:06:44Z | 2026-11-08T21:25:00Z |
| underdog|5e5ead91-81b9-4b8e-a5ef-e2aa3b7a5ed0 | underdog | Woody Marks | Rush Yards | under | 0.21579731650075495 | 2026-11-05T12:22:13Z | 2026-11-08T21:05:00Z |
| underdog|d88c56d2-1395-401b-bd3e-3d1d31728d14 | underdog | Woody Marks | Rush + Rec Yards | under | 0.2133596409286077 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|dabb5287-277e-4a23-8946-40925b7c6a45 | underdog | Sione Vaki | Receiving Yards | over | 0.2124555475324016 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|e47b24f2-df72-42a9-8d7a-51e07176520b | underdog | Kendre Miller | Rush + Rec Yards | under | 0.21245360203567454 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| underdog|e509bdfb-161e-4b4e-a5ba-0fea710f2ab8 | underdog | Rachaad White | Rush Yards | under | 0.21238054015985097 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|47643075-a2e0-4286-848c-4cbc6b64643e | underdog | Jaylen Wright | Rush + Rec Yards | under | 0.21167080472030686 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|84acac62-4ba9-4be2-b2e0-edfc9f3d2252 | underdog | Thomas Castellanos | Pass TDs | under | 0.21044509816332535 | 2026-11-05T22:06:44Z | 2026-11-08T02:30:00Z |
| prizepicks|16577049 | prizepicks | Trey McBride | Rec Yards | under | 0.20935259101009185 | 2026-11-03T02:21:46Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|96d514bd-16df-438e-a060-00f5c8573329 | underdog | Patrick Mahomes | Pass Attempts | under | 0.20613805218871373 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|1f7dd0bf-f127-468a-b32d-11be5fc22ca6 | underdog | Quinshon Judkins | Rush Yards | under | 0.20487468569814804 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| underdog|c0462df6-b3da-4b63-b678-808191fb8671 | underdog | Colston Loveland | Receiving Yards | under | 0.20437151822603095 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|1fa93360-83ec-4148-833b-a2ac7223bcde | underdog | Evan McPherson | FG Made | under | 0.20387134321469125 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|da853143-4fe2-4a01-8ba7-a057da028104 | underdog | Quinshon Judkins | Rush + Rec Yards | under | 0.20303883340681128 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| underdog|17d58030-f59c-4e6a-b95e-5e22592343f4 | underdog | Nico Collins | Receiving Yards | under | 0.20265644684978057 | 2026-11-05T22:06:44Z | 2026-11-08T21:05:00Z |
| underdog|b99d6014-b4c3-451f-bc57-c1109aa968ed | underdog | Christian McCaffrey | Receiving Yards | under | 0.20231096643705238 | 2026-11-05T22:06:44Z | 2026-11-08T21:25:00Z |
| underdog|c61022bc-362a-4e1c-8d69-48a576ea6c00 | underdog | Justin Herbert | Pass TDs | under | 0.20191287593682095 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|838239fd-0f4c-4832-b6a8-a19978944845 | underdog | Saquon Barkley | Rush + Rec Yards | under | 0.19878933592568027 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|ba147c3b-9fb6-467d-a96b-1997119f919e | underdog | Ja'Marr Chase | Receiving Yards | under | 0.19869817739603746 | 2026-11-05T22:06:44Z | 2026-11-08T14:30:00Z |
| prizepicks|16577051 | prizepicks | Brock Bowers | Rec Yards | under | 0.19828126826604298 | 2026-11-03T02:21:46Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|d9931ebc-f2b4-4965-a907-7e5426461db5 | underdog | Trey McBride | Receptions | under | 0.19807043328611007 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|d3d2a2d2-5f18-48d0-9316-dcd5ad29df72 | underdog | Rachaad White | Rush + Rec Yards | under | 0.19664442091925727 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|35f55b20-95d8-4be7-8a2a-b64ada15b21e | underdog | Daniel Hill | Receiving Yards | over | 0.1951439191257699 | 2026-11-05T12:22:13Z | 2026-11-07T20:30:00Z |
| underdog|9a2902e7-4ecf-4ea5-a36e-c5c8f6e59bb7 | underdog | Harrison Butker | FG Made | under | 0.19473086921391436 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|410efb5a-6f14-4f58-846b-fb76cf98cec4 | underdog | Matthew Stafford | Rush Yards | over | 0.1944521898255368 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|0aeefc8a-3585-4426-9ce7-dfe6849d6817 | underdog | C.J. Stroud | Pass Attempts | under | 0.1912506788453352 | 2026-11-05T12:22:13Z | 2026-11-08T21:05:00Z |
| underdog|1f3de6fd-36c2-46ee-b345-bd743ca17f3c | underdog | Junior Sherrill | Receiving Yards | under | 0.19109132486949432 | 2026-11-05T22:06:44Z | 2026-11-07T21:15:00Z |
| underdog|05a9a31f-443e-4d40-8995-576d11e8f8e6 | underdog | Elija Lofton | Receptions | under | 0.1900201737721301 | 2026-11-05T22:06:44Z | 2026-11-08T00:30:00Z |
| underdog|872eac2a-4e79-4367-a987-6a15c41a88dc | underdog | Kyle Pitts | Receptions | under | 0.1884927972756335 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| prizepicks|16718554 | prizepicks | Nico Collins | Rec Targets | under | 0.1883756713204645 | 2026-11-05T22:06:44Z | 2026-11-08T16:05:00.000-05:00 |
| underdog|e8b42489-088d-4fa3-8358-e7bd4e883b98 | underdog | Marvin Harrison | Receiving Yards | under | 0.18582900335069386 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|118bfb2f-2d3c-47bf-abe2-6b54b0710e9a | underdog | Jake Fette | Pass Yards | under | 0.18479901571055346 | 2026-11-05T22:06:44Z | 2026-11-08T00:30:00Z |
| prizepicks|16718534 | prizepicks | Courtland Sutton | Rec Targets | under | 0.18479411301214343 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|6af5960a-1d9d-4f3c-ab5d-c2bcd805cfc7 | underdog | Baker Mayfield | Pass Attempts | under | 0.1838540296279383 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|df0fcb9f-5100-4910-b141-a65adc25e74e | underdog | Joe Burrow | Pass Attempts | under | 0.18375588026906453 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|9f26a74b-8f4c-4c6c-8c75-268881535808 | underdog | Byrum Brown | Pass Yards | under | 0.18288023106013962 | 2026-11-06T06:34:07Z | 2026-11-07T17:45:00Z |
| underdog|f4c69603-6218-4437-8fdd-275d6fcfe8ef | underdog | Jason Myers | FG Made | under | 0.1827109251134501 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| prizepicks|16722856 | prizepicks | George Kittle | Rec Targets | under | 0.18223845481624534 | 2026-11-06T06:34:07Z | 2026-11-08T16:25:00.000-05:00 |
| prizepicks|16685557 | prizepicks | Justin Herbert | Pass TDs | under | 0.18176877497841348 | 2026-11-05T12:22:13Z | 2026-11-08T16:05:00.000-05:00 |
| underdog|cfae8805-6e9b-4151-aae5-009efb71986a | underdog | Brock Bowers | Receptions | under | 0.17887742031236042 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|9100eaf4-8232-4056-8f1f-336a475cc678 | underdog | Rhamondre Stevenson | Rush Yards | under | 0.17609187646102753 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| prizepicks|16718553 | prizepicks | Marvin Harrison Jr. | Rec Targets | under | 0.17607823157106484 | 2026-11-05T22:06:44Z | 2026-11-08T16:05:00.000-05:00 |
| underdog|3a64bb74-f554-4133-8100-a705c07fec61 | underdog | Jonah Coleman | Rush + Rec Yards | under | 0.17519915897290428 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| underdog|0cac5c54-f95c-45a2-a6e1-c24270fad37c | underdog | Jesse Legree | Receptions | under | 0.17518304433037357 | 2026-11-05T22:06:44Z | 2026-11-08T03:30:00Z |
| underdog|a2ee3b2c-3a41-4508-ad81-1d0ca5c6f707 | underdog | Jared Goff | Pass Attempts | under | 0.17494980056194276 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| prizepicks|16734086 | prizepicks | Robin Montgomery | Double Faults | under | 0.1747865886402138 | 2026-11-06T06:34:07Z | 2026-11-06T05:40:00.000-05:00 |
| underdog|58473198-16c0-4f1f-98ce-794fe0d452fd | underdog | Rashee Rice | Receptions | under | 0.17383563925443812 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|1549847b-61b5-487a-babb-144ef07fdec6 | underdog | Jordan Mason | Rush + Rec Yards | under | 0.17302938259729017 | 2026-11-05T22:06:44Z | 2026-11-10T01:15:00Z |
| underdog|e67e9ba5-8b23-46cb-a546-85415df91843 | underdog | Luke Fahey | Pass TDs | under | 0.17214479173554886 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| prizepicks|16719194 | prizepicks | Stefon Diggs | Rec Targets | under | 0.17139963879683195 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|afe1bdf8-c20d-4613-ad24-60cc80891977 | underdog | Luther Burden | Receiving Yards | under | 0.1708136555455848 | 2026-11-05T22:06:44Z | 2026-11-09T01:20:00Z |
| underdog|887f2a53-22c4-4389-9e34-a398c51050dd | underdog | Keenan Allen | Receiving Yards | under | 0.16925713477116489 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|d1484ee9-014f-45d1-a126-1d177aec34ed | underdog | Makhi Hughes | Rush Yards | under | 0.1692475397419455 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|6268b499-98fa-4069-8241-11ee20410ea6 | underdog | Bo Jackson | Rush Yards | under | 0.16887965113928916 | 2026-11-05T22:06:44Z | 2026-11-07T20:30:00Z |
| underdog|a2c32829-5741-4600-bdac-f990a7052b23 | underdog | Rhamondre Stevenson | Rush + Rec Yards | under | 0.1684921629314633 | 2026-11-03T11:59:28Z | 2026-11-08T21:25:00Z |
| underdog|1e0723e6-39f5-401c-9ecb-73146c38ec61 | underdog | Marvin Harrison | Receptions | under | 0.16835016265867342 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| prizepicks|16718485 | prizepicks | Kyle Pitts Sr. | Rec Targets | under | 0.16781899621209362 | 2026-11-05T22:06:44Z | 2026-11-08T09:30:00.000-05:00 |
| underdog|a8a9bed2-5d3a-4afa-b7f7-de3a2c658f75 | underdog | Jared Goff | Rush Yards | over | 0.1677182366005825 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|cf74ea13-4c83-486b-a699-efa71530a041 | underdog | Amon-Ra St. Brown | Receptions | under | 0.16742438992001507 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|21a1acab-2608-4d98-a630-1f326444c663 | underdog | Jalen Royals | Receiving Yards | over | 0.16685710651601937 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|3c2c0991-0e80-4489-9557-56d68aa8268c | underdog | Wil Lutz | FG Made | under | 0.1665329706004408 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|c7fbbf68-83ff-44a2-a032-87a9503edea0 | underdog | Cairo Santos | FG Made | under | 0.16650636156632292 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|15045f83-f7c4-4e88-a249-0602b4dfe33f | underdog | Jordan Mason | Rush Yards | under | 0.1664614051365807 | 2026-11-05T12:22:13Z | 2026-11-10T01:15:00Z |
| underdog|4a902d41-198f-4763-ad4f-c1aabaf04d56 | underdog | Darian Mensah | Pass TDs | over | 0.16623847690906796 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|bd6835b3-2c6e-4ba0-aa21-2002c9c11af4 | underdog | Jackson Kleather | FG Made | over | 0.16618416805976138 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|dccc8f0d-749c-4e93-9f1c-2d0eef11ef7d | underdog | Dawson Knox | Receiving Yards | under | 0.1661235575343949 | 2026-11-05T22:06:44Z | 2026-11-10T01:15:00Z |
| underdog|73f2643f-52d1-490b-a801-df52538bf621 | underdog | Austin Hooper | Receiving Yards | over | 0.16565211889871145 | 2026-11-05T12:22:13Z | 2026-11-08T14:30:00Z |
| underdog|1618355e-edef-449f-bc87-1cc1db3b63f7 | underdog | Tyler Warren | Receiving Yards | under | 0.16541696176617582 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|6b0a254c-fbec-481c-b649-05d1a353bcae | underdog | Harrison Butker | Kicking Points | under | 0.16442129921836235 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|26b34dbd-c8b5-4155-8b09-75b12c1ecd7a | underdog | Stefon Diggs | Receptions | under | 0.1623657419982183 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|5862450c-7de6-4db1-9b65-c3ccfa0529c6 | underdog | Ladd McConkey | Receiving Yards | under | 0.162300971534745 | 2026-11-06T06:34:07Z | 2026-11-08T21:05:00Z |
| underdog|9ff29ccb-f4c3-4664-9330-39133772a9f1 | underdog | Tucker Kraft | Receptions | under | 0.1615364063191952 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|9cc36ab9-fd71-4bfb-813b-54422aecd68a | underdog | Anthony Colandrea | Pass Yards | under | 0.16122272665769133 | 2026-11-04T12:10:41Z | 2026-11-07T01:00:00Z |
| underdog|528a645e-8439-47f6-91f3-89566cf92574 | underdog | Greg Dulcich | Receptions | under | 0.15981895291377868 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|8f289276-834c-4a60-ac19-2b8e634918e6 | underdog | Ollie Gordon | Rush + Rec Yards | under | 0.15941145377301513 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|7d8aca5c-098a-4cd2-ac18-2986be8ea813 | underdog | Matthew Golden | Receptions | under | 0.15935064858874126 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| prizepicks|16718548 | prizepicks | Tucker Kraft | Rec Targets | under | 0.1589344482639552 | 2026-11-05T22:06:44Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|de6281e6-e72c-4f7d-9b19-ea93df015060 | underdog | Drake London | Receptions | under | 0.1588244841998091 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| prizepicks|16718557 | prizepicks | Tyler Warren | Rec Targets | under | 0.15855243884293413 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|698f97b3-863e-4773-97b1-02795f52198b | underdog | Dak Prescott | Pass Attempts | under | 0.15742541666457277 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|549e9cef-a3a5-4d2d-80da-e1502e502bd7 | underdog | Tyler Goodson | Rush + Rec Yards | under | 0.15738112185450548 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|e41a0da4-0291-4499-9b1b-ed6fe79cddc8 | underdog | Ollie Gordon | Receiving Yards | under | 0.15660530020212726 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|37b70014-c646-417c-9dda-4626c7ea528a | underdog | Tyler Shough | Pass Attempts | under | 0.15655653928608748 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|0b592d73-46b4-4456-918c-8d00242be932 | underdog | Dawson Knox | Receptions | under | 0.15649493040707285 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|28aa1264-fc74-4c1c-9f5a-0f2b5396c62e | underdog | Garrett Wilson | Receiving Yards | under | 0.15645468065321244 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|56924a18-ffc6-4e33-a992-256d8235fd2d | underdog | Jordan Faison | Receptions | under | 0.15642286280966766 | 2026-11-05T22:06:44Z | 2026-11-08T00:30:00Z |
| prizepicks|16675752 | prizepicks | J'Koby Williams | Rush Atts | under | 0.15626612680045937 | 2026-11-05T12:22:13Z | 2026-11-07T21:30:00.000-05:00 |
| underdog|1345bde9-df5c-4cdb-8382-38d63c6c46e1 | underdog | Mark Fletcher Jr. | Receiving Yards | over | 0.15426435166645103 | 2026-11-05T22:06:44Z | 2026-11-08T00:30:00Z |
| underdog|ccbdcf12-c470-43c7-959a-45b6e6b5c4f0 | underdog | George Pickens | Receiving Yards | under | 0.15396395671628538 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|778c51f9-bef3-4899-aabb-503d51edce9d | underdog | Kaelon Black | Receiving Yards | under | 0.15355971496531262 | 2026-11-06T06:34:07Z | 2026-11-08T21:25:00Z |
| underdog|f6cfe146-eab9-41e2-9ffc-5dae6dd020db | underdog | Isaiah Mizell | Receptions | under | 0.15348737235866394 | 2026-11-05T12:22:13Z | 2026-11-07T03:15:00Z |
| underdog|b3ceb3cb-33f0-446d-a058-dddfaa2a7301 | underdog | Jacobo Echeverria Lozano | FG Made | over | 0.1533441022676829 | 2026-11-05T22:06:44Z | 2026-11-07T17:30:00Z |
| underdog|c3a8e703-937f-4b67-87af-d63af0313595 | underdog | Liam Boyd | XP Made | over | 0.15303281462856144 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| prizepicks|16718455 | prizepicks | Trey McBride | Rec Targets | under | 0.1522364381770983 | 2026-11-05T22:06:44Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|305da5df-b90a-4800-95eb-e6d63bb1b2d7 | underdog | Billy Edwards Jr. | Pass Yards | under | 0.15147454244557224 | 2026-11-06T06:34:07Z | 2026-11-07T17:00:00Z |
| prizepicks|16718472 | prizepicks | Drake London | Rec Targets | under | 0.15145440458702286 | 2026-11-05T22:06:44Z | 2026-11-08T09:30:00.000-05:00 |
| underdog|03d4f9d3-c01c-43c2-9cca-d2ca40095a7c | underdog | Kenneth Williams | Rush Yards | under | 0.15110360930808275 | 2026-11-06T06:34:07Z | 2026-11-08T00:30:00Z |
| underdog|b2b3468d-c1e9-49b8-856f-d0397a899334 | underdog | Alvin Kamara | Rush Yards | under | 0.15094440136484844 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| prizepicks|16718538 | prizepicks | Jonah Coleman | Rec Targets | under | 0.15073744374037423 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|5eea8199-5dbe-4649-a20a-2405bd63d177 | underdog | Jaxon Smith-Njigba | Receptions | under | 0.15026450962994486 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|7f44b052-27a1-42a5-8108-ca43bdfcb5bb | underdog | Chuba Hubbard | Rush + Rec Yards | under | 0.14959006456056478 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|e0c22419-0dff-4556-a05e-9acfa3ab7a09 | underdog | Brandon Aubrey | FG Made | under | 0.14958269462275497 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|b0ce99d7-ccca-47c0-a454-e6f920eab8e2 | underdog | Bo Nix | Pass TDs | under | 0.14921921703126695 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|40a7914d-b7b6-4103-8c07-ba36fd938142 | underdog | Omar Cooper | Receptions | under | 0.14826986085592442 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|69ba3a63-bb92-4f39-984a-ed5566438f78 | underdog | Nick Folk | FG Made | under | 0.1481435952641591 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|c4587fdc-fe2d-47dc-997d-d0b08663b00a | underdog | Ka'imi Fairbairn | FG Made | under | 0.1479318682678138 | 2026-11-03T02:21:46Z | 2026-11-08T21:05:00Z |
| underdog|1b370830-3867-4ade-9a8d-418a06dbd1c1 | underdog | Christian Watson | Receptions | under | 0.1479168165648339 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|17dd63b2-9a95-4d2f-8fdc-a8e6d733bc1a | underdog | Kaelon Black | Rush + Rec Yards | under | 0.1478860595863125 | 2026-11-06T06:34:07Z | 2026-11-08T21:25:00Z |
| underdog|1aeae776-d0b1-4470-b144-6de49c2cb956 | underdog | Bear Bachmeier | Pass TDs | over | 0.14784749034407785 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|2484637b-dd6a-4882-be40-ce0e68d4e559 | underdog | Kenny Gainwell | Receptions | under | 0.1475602481670133 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|13d49fc8-9559-45e1-9bac-6f15a20a2c72 | underdog | Ollie Gordon | Receptions | under | 0.14682805397570908 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| prizepicks|16718558 | prizepicks | Rashee Rice | Rec Targets | under | 0.14673204243829352 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|ad5841e3-f51c-4e2d-a883-064eb9b2257f | underdog | Malik Washington | Receptions | under | 0.14645959659878283 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| prizepicks|16718549 | prizepicks | Savion Williams | Rec Targets | under | 0.14623445121083523 | 2026-11-05T22:06:44Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|f57c0032-b5b1-4228-af7c-d6bb6f08e67e | underdog | Emeka Egbuka | Receptions | under | 0.1460648049345178 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|b5acd5c8-143c-4860-995f-2366f9a662f7 | underdog | Kalieb Osborne | Pass TDs | over | 0.1460045485512973 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|ace1606b-2e1b-4aa9-9bdd-7b9a81772688 | underdog | Jaden Craig | Pass TDs | over | 0.14576974859587555 | 2026-11-05T22:06:44Z | 2026-11-07T03:15:00Z |
| underdog|05cc47cb-d23e-4419-9af1-81291611e3a4 | underdog | Saquon Barkley | Rush Yards | under | 0.14498790320221477 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|a5687c54-7273-4922-8cf8-a0383ebb4afa | underdog | Trey McBride | Receiving Yards | under | 0.14497443435005852 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|16b01cae-a42d-4c7f-86cc-d05b5ca88fce | underdog | Trinidad Chambliss | Pass Yards | under | 0.14383809485501364 | 2026-11-05T22:06:44Z | 2026-11-08T00:30:00Z |
| underdog|d1ad5738-520b-4373-b127-b15ab45c351a | underdog | Jaxon Smith-Njigba | Receiving Yards | under | 0.14355065406302003 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|154a1940-c81e-490b-85b4-83bd1bac4598 | underdog | Jalen Nailor | Receiving Yards | under | 0.14280205217730946 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|1acc37b7-16ae-4dfe-9876-857c87ea3b17 | underdog | Quentin Johnston | Receiving Yards | under | 0.1413979010411639 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|3389df2b-6562-4259-9cf1-6f54c8f866e9 | underdog | Walker Eget | Pass Yards | under | 0.1410353141986187 | 2026-11-05T22:06:44Z | 2026-11-07T17:30:00Z |
| underdog|ef1c0be0-812d-44f6-9397-3e1355f6994d | underdog | Rocco Becht | Pass TDs | over | 0.14073851519469394 | 2026-11-05T22:06:44Z | 2026-11-07T20:30:00Z |
| underdog|19182bf3-3972-4fb8-ad6e-ff29a13cff8c | underdog | Chase Brown | Rush Yards | under | 0.13989207436771856 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|c092b660-5290-4932-8177-8f7f70620dde | underdog | Kendre Miller | Rush Yards | under | 0.13985740642259525 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|d750f1b4-ebcd-49c0-9b03-97137f1f422f | underdog | Carson Wentz | Rush Yards | under | 0.1396304799819178 | 2026-11-05T22:06:44Z | 2026-11-10T01:15:00Z |
| underdog|e1775404-5113-460c-9eec-b13c0226b55b | underdog | Olamide Zaccheaus | Receptions | under | 0.1396223249639138 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|03e0d95d-f3f0-4f64-bea2-e9e8bbb684e3 | underdog | AJ Barner | Receptions | under | 0.13910664132787998 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|f31a1e8b-9aa9-4022-b468-859f852768cb | underdog | Devaughn Vele | Receptions | under | 0.13901253046609652 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|3c114bc2-839b-4e55-9ec0-5de96e8522a9 | underdog | Caleb Douglas | Receptions | under | 0.1384724673367177 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|5df51a97-b605-4c0d-b9a5-6038554d83e4 | underdog | Amon-Ra St. Brown | Receiving Yards | under | 0.13837637499846278 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|83b965d9-e75e-4d7b-8886-44573ffbcdfb | underdog | Dilin Jones | Rush Yards | under | 0.13798927114368054 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|7510d34a-d239-42b9-90b3-80b4726c3715 | underdog | Janice Tjen | Double Faults | over | 0.1374447464413906 | 2026-11-05T12:22:13Z | 2026-11-06T09:30:00Z |
| underdog|62752957-b2d2-43f1-8caa-62560a2db86a | underdog | Brock Purdy | Pass TDs | under | 0.13705484641190113 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|e9e775c1-e65e-481a-8e80-4451df551d94 | underdog | James Cook | Receptions | under | 0.13675024566789118 | 2026-11-05T22:06:44Z | 2026-11-10T01:15:00Z |
| underdog|e51659c8-5120-4ea6-8cda-0855726b1435 | underdog | Matthew Stafford | Pass Attempts | under | 0.13674658781617022 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| underdog|f51527ca-57c4-493e-a8c4-957bb43c94a5 | underdog | Jahmyr Gibbs | Rush + Rec Yards | under | 0.1362414547608164 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|d6cbee1a-cecf-45c3-92bd-590b34f8135a | underdog | Nick Folk | Kicking Points | under | 0.1351811208582573 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|0a1d4a28-f4ed-433b-a45b-953e95969acb | underdog | Jadarian Price | Receptions | under | 0.13399424688283068 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|5790a889-8601-4824-ac78-b9c766ba1891 | underdog | Marvin Mims Jr. | Receptions | under | 0.13357422686133513 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|e5b104d0-4d4a-40f8-b1af-c7a433122290 | underdog | Ethan Moczulski | FG Made | over | 0.13305034470819216 | 2026-11-04T12:10:41Z | 2026-11-07T01:00:00Z |
| underdog|8f57d401-69ae-4953-9170-5de81718dad4 | underdog | Jeremiah Cobb | Rush Yards | under | 0.13275075113520285 | 2026-11-06T06:34:07Z | 2026-11-07T17:45:00Z |
| underdog|d0b6fbf3-ddeb-4be4-a4c6-1ac1581835e5 | underdog | Cade Otton | Receptions | under | 0.13207335081342486 | 2026-11-05T12:22:13Z | 2026-11-09T01:20:00Z |
| prizepicks|16718540 | prizepicks | Amon-Ra St. Brown | Rec Targets | under | 0.13196308606307305 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|6856bd41-edf8-48c4-a2b6-b84819ec4ae5 | underdog | Marcel Reed | Pass Yards | under | 0.13137009479314776 | 2026-11-05T22:06:44Z | 2026-11-07T20:00:00Z |
| underdog|6a4ea7ca-8051-400b-a435-f94e0a7067ee | underdog | Jameson Williams | Receiving Yards | under | 0.131077359753479 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|46de9f5f-9969-4389-9c6e-d578d8c4dd70 | underdog | Nate Adkins | Receiving Yards | over | 0.13095935698202643 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| underdog|d1b4b6ad-79e2-42da-8b2f-39932216e6ef | underdog | Magda Linette | Double Faults | under | 0.13067143321143349 | 2026-11-05T22:06:44Z | 2026-11-06T11:50:00Z |
| underdog|fcc59928-c671-462f-b566-25093f2522a8 | underdog | Caden Buhr | FG Made | over | 0.1306453456015051 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|14d37ea9-87e7-4e15-ad26-f93259d0facd | underdog | Drew Lock | Pass TDs | under | 0.12966967278207253 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| prizepicks|16718556 | prizepicks | Jonathan Taylor | Rec Targets | under | 0.12923033670188888 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|3aa93bf4-8e56-4a6e-8771-99a3e7b252f0 | underdog | Kaleb Edwards | Receiving Yards | over | 0.1291255418811703 | 2026-11-05T12:22:13Z | 2026-11-07T20:30:00Z |
| underdog|8a77a4e3-ad8b-4d5e-962d-b25ce8bf9a4d | underdog | Jared Curtis | Pass Yards | under | 0.1288672358376597 | 2026-11-05T22:06:44Z | 2026-11-07T21:15:00Z |
| underdog|ccfe2bba-71d1-4e46-bf46-d00e2a8c975c | underdog | Javonte Williams | Rush + Rec Yards | under | 0.12875496760840743 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|5869b7ef-5cbd-40b2-b17d-2b4591a92144 | underdog | Matthew Golden | Receiving Yards | under | 0.12870107458299462 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|7a288207-299b-4695-b585-940ac0294fdc | underdog | Luke Fahey | Pass Yards | under | 0.12864978345130762 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|a9d2cbf9-b134-4d3d-97b8-16d220ba4894 | underdog | George MacIntyre | Pass Yards | under | 0.1273705463987821 | 2026-11-05T12:22:13Z | 2026-11-07T23:15:00Z |
| underdog|f9408da3-4c03-47a1-91ac-c4ac94507742 | underdog | Drake London | Receiving Yards | under | 0.12714827801752404 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|76e6cc64-cc3a-46d3-8690-4230bd756233 | underdog | Rome Odunze | Receiving Yards | under | 0.1268651524326092 | 2026-11-06T06:34:07Z | 2026-11-09T01:20:00Z |
| underdog|ae0024e2-e6f7-4496-90a2-739f7b072ef9 | underdog | Jaylen Waddle | Receiving Yards | under | 0.12663902325289267 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|27f67693-fa31-45d9-8812-41afd1687e68 | underdog | Junior Sherrill | Receptions | under | 0.12629619877526765 | 2026-11-05T22:06:44Z | 2026-11-07T21:15:00Z |
| underdog|71898269-3068-4a79-8c30-e9bd7f73610e | underdog | Sam LaPorta | Receiving Yards | under | 0.12611632753723168 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| underdog|2936a29d-847a-463b-9f08-0a5f9847dfa7 | underdog | Jalen Nailor | Receptions | under | 0.1260310148407855 | 2026-11-05T22:06:44Z | 2026-11-08T21:25:00Z |
| prizepicks|16719191 | prizepicks | Antonio Williams | Rec Targets | under | 0.1251897897385651 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|5adfe6e8-e91f-44dd-842d-5be373846225 | underdog | Chris Olave | Receptions | under | 0.12468750167033804 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|58790b19-dd02-48db-9994-baaab8acbb8b | underdog | Rachaad White | Receptions | under | 0.12456515053371986 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|abe5fb36-b140-496d-8138-08cf2021eab6 | underdog | Jayden Daniels | Pass TDs | under | 0.12401048501725953 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|a5a84e5b-2d1a-407b-ad40-5e0faa4d1d12 | underdog | Wil Lutz | Kicking Points | under | 0.12375220362671835 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|6fa07966-69ad-4e19-932b-f21a9e51b66b | underdog | Ollie Gordon | Rush Yards | under | 0.12319862002616433 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|f845366e-f357-4371-8c2c-1081790bdb5f | underdog | Kenny Minchey | Pass TDs | over | 0.12253590116069402 | 2026-11-05T22:06:44Z | 2026-11-07T23:15:00Z |
| underdog|a75d0892-12c3-4a3d-bea7-a07236a8702c | underdog | Conner Weigman | Pass Yards | under | 0.12251598812778575 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| prizepicks|16718519 | prizepicks | Rome Odunze | Rec Targets | under | 0.122368232187266 | 2026-11-05T22:06:44Z | 2026-11-08T20:20:00.000-05:00 |
| underdog|f3d5e2f8-b078-48d2-b5d6-54ca6ca199e6 | underdog | Cairo Santos | Kicking Points | under | 0.12236507723893952 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|bf5c8287-a719-4bc8-a84d-21b682a39a7b | underdog | Kenny Gainwell | Receiving Yards | under | 0.12233318149565453 | 2026-11-05T12:22:13Z | 2026-11-09T01:20:00Z |
| underdog|e75848b9-9179-435a-93b3-ad5ac9f22f56 | underdog | Fame Ijeboi | Rush Yards | under | 0.12226295996532677 | 2026-11-06T06:34:07Z | 2026-11-07T17:30:00Z |
| underdog|9a6bf26d-777c-4ed1-a55d-58f8fc621644 | underdog | Kaelon Black | Receptions | under | 0.12200046497800188 | 2026-11-06T06:34:07Z | 2026-11-08T21:25:00Z |
| underdog|06a98b20-5b6a-4641-963b-748d6b6ac027 | underdog | Ja'Marr Chase | Receptions | under | 0.12198379656106328 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|9bf843c7-11d8-47c1-8d3d-ba3eb2bfbad1 | underdog | Maria Sakkari | Double Faults | under | 0.12150011152757467 | 2026-11-05T12:22:13Z | 2026-11-06T10:30:00Z |
| prizepicks|16719168 | prizepicks | Caleb Douglas | Rec Targets | under | 0.12141200380041606 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|18971421-29b9-4aa5-b533-b3255d1a9695 | underdog | Bijan Robinson | Rush + Rec Yards | under | 0.12137057551043673 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|16510e89-3e9d-4b33-9549-19154015507d | underdog | Tyler Allgeier | Receptions | under | 0.12089928730863053 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|e2e50040-7336-4b84-8687-56a75634b32f | underdog | Lucrezia Stefanini | Double Faults | over | 0.1206255184944251 | 2026-11-05T22:06:44Z | 2026-11-06T13:00:00Z |
| underdog|8cb9a75f-fe5e-4f64-ae35-a1448f74f310 | underdog | D'Andre Swift | Rush Yards | under | 0.12040396519613183 | 2026-11-05T22:06:44Z | 2026-11-09T01:20:00Z |
| underdog|0187bc04-2901-4ba3-8977-4bd9fb0d707b | underdog | Katin Houser | Rush Yards | over | 0.1201508756895383 | 2026-11-04T12:10:41Z | 2026-11-07T01:00:00Z |
| underdog|03b3eb0d-b146-440d-843d-79223ef0bf2b | underdog | Jahan Dotson | Receptions | under | 0.1200345581620813 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| prizepicks|16619686 | prizepicks | Chris Dawn Jr. | Recs | under | 0.11978140668783599 | 2026-11-04T12:10:41Z | 2026-11-07T22:30:00.000-05:00 |
| underdog|e96392d4-2e7b-476c-b8c5-d0f6a5a4072c | underdog | Denzel Boston | Receiving Yards | under | 0.1195381161154726 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| prizepicks|16576409 | prizepicks | Christian McCaffrey | Rush Yards | under | 0.11950744181162642 | 2026-11-03T02:21:46Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|3ca0797a-6c45-46f4-8b61-0d000eda9dc5 | underdog | Ayden Greene | Receptions | over | 0.11935754910617813 | 2026-11-05T12:22:13Z | 2026-11-07T00:00:00Z |
| underdog|c7bb0bb6-dc60-4c38-93e2-684dacb04b02 | underdog | Josh Allen | Pass TDs | under | 0.11926653211048077 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|33ffb548-94a1-44e7-9da3-17dc0d7f1d49 | underdog | J'Koby Williams | Receiving Yards | over | 0.11825318810941854 | 2026-11-04T12:10:41Z | 2026-11-08T02:30:00Z |
| underdog|1c07119d-7fe4-4eba-b8f2-c7008e344979 | underdog | Harold Fannin | Receptions | under | 0.11801150156707052 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|eccd30c3-ed5b-4cc6-aad4-06299d22c529 | underdog | Malik Nabers | Receptions | under | 0.11783962166306128 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|ca704392-ce3d-435e-b595-a41f7b2b2a55 | underdog | Sorana Cirstea | Double Faults | under | 0.11675435248083976 | 2026-11-06T06:34:07Z | 2026-11-06T08:30:00Z |
| underdog|2d49afa9-bf55-4cd2-8efe-1f0dc62786fc | underdog | Tait Reynolds | Pass TDs | under | 0.11668508117452292 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|2ffb2fff-77a4-4abe-8a15-f1d4564e0592 | underdog | Keelon Russell | Pass TDs | over | 0.11664993848736266 | 2026-11-05T22:06:44Z | 2026-11-07T20:30:00Z |
| underdog|c3130728-988e-4cdf-9fa4-96cbff03e330 | underdog | Kyren Williams | Rush Yards | under | 0.11604746503488483 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|6efc22a4-0d91-487b-822d-d7f27a3218b2 | underdog | George MacIntyre | Pass TDs | under | 0.11581459797425153 | 2026-11-05T12:22:13Z | 2026-11-07T23:15:00Z |
| underdog|649d4cf3-3d96-4754-b6ba-149b97bba842 | underdog | Kenneth Walker III | Receptions | under | 0.11559688528805712 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|b131a074-2cef-4b49-ba41-a233aa6adac0 | underdog | Cade Otton | Receiving Yards | under | 0.1153806979626707 | 2026-11-05T12:22:13Z | 2026-11-09T01:20:00Z |
| underdog|9825e0ba-f877-4bf7-812c-f9129d57348c | underdog | Patrick Mahomes | Pass TDs | under | 0.11537751808865182 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|df8cc29e-c9c7-46e3-9773-066f25acc7a6 | underdog | CeeDee Lamb | Receptions | under | 0.11512462845971994 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| prizepicks|16718536 | prizepicks | Jaylen Waddle | Rec Targets | under | 0.11494202569891032 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|f2f45b87-957b-46ab-9edf-e31974176078 | underdog | Thomas Castellanos | Rush Yards | under | 0.11460442719465413 | 2026-11-04T12:10:41Z | 2026-11-08T02:30:00Z |
| underdog|2608df37-9cb1-4e77-ab6e-559449ba8a70 | underdog | Marcel Reed | Pass TDs | under | 0.11387285965261762 | 2026-11-05T22:06:44Z | 2026-11-07T20:00:00Z |
| underdog|27e5d450-ecd5-4fa1-ba46-e64b8ac2c1eb | underdog | Xavier Worthy | Receiving Yards | under | 0.11373393892426464 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|8dda3f2c-43bd-496a-91aa-283c7a072e7b | underdog | Chuba Hubbard | Receptions | under | 0.11351803648802827 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|fdc2cba3-5628-496b-92fe-05b5d00d90e6 | underdog | Braylon Staley | Receptions | under | 0.11333666895548766 | 2026-11-05T12:22:13Z | 2026-11-07T23:15:00Z |
| underdog|980ef0c9-e7c6-40c1-ae91-d71c59322e06 | underdog | Travis Kelce | Receptions | under | 0.11333613992057967 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|48e760c2-4eac-4eb7-a8a9-531f0ca1ef83 | underdog | Ryan Fitzgerald | Kicking Points | under | 0.11326096940715735 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|1f37a02f-1db6-464f-9fa6-211296f14cbc | underdog | Aliaksandra Sasnovich | Double Faults | over | 0.1129708424047684 | 2026-11-05T12:22:13Z | 2026-11-06T10:30:00Z |
| underdog|516cd42e-4751-4b27-abbb-5cc40fef6cbf | underdog | Jaylen Wright | Rush Yards | under | 0.11295640133296947 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|3b806c99-c348-44de-86cc-461e6cf2d3f2 | underdog | Jake Bates | FG Made | under | 0.11285240847954703 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|3d6312d6-5e09-42e3-adbc-489866eb20db | underdog | Fluff Bothwell | Rush Yards | under | 0.11256240110035287 | 2026-11-06T06:34:07Z | 2026-11-07T21:15:00Z |
| prizepicks|16577048 | prizepicks | George Pickens | Rec Yards | under | 0.11245540278204647 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|f48da050-199d-44b1-b56e-450cb1cc55b9 | underdog | Raleek Brown | Receiving Yards | over | 0.11219282113360729 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|e14b44d7-6880-4cde-a5d0-be585bd64366 | underdog | Denzel Boston | Receptions | under | 0.11215354306007119 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|fadb69a5-2f84-42de-a83a-f7bd3242f9db | underdog | Greg Dulcich | Receiving Yards | under | 0.1120073367268899 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|62c2d195-f122-4e9d-99d9-b2a2717e3ae6 | underdog | Elija Lofton | Receiving Yards | under | 0.11190817707311462 | 2026-11-05T22:06:44Z | 2026-11-08T00:30:00Z |
| underdog|d057f822-2dbd-4436-adc8-eadda12bcc00 | underdog | Tim Patrick | Receiving Yards | under | 0.11158456730208843 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| underdog|f3f39226-3573-463d-bbd7-3f0178e7ebdf | underdog | Alvin Kamara | Rush + Rec Yards | under | 0.11139213822218441 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|ba27855c-f306-460f-8d0b-850a557fe3e5 | underdog | James Cook | Rush + Rec Yards | under | 0.11131941599424644 | 2026-11-04T12:10:41Z | 2026-11-10T01:15:00Z |
| prizepicks|16719170 | prizepicks | Greg Dulcich | Rec Targets | under | 0.1112945325708179 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|fc8e948f-e862-45a9-9635-07a454ffb0a7 | underdog | J.K. Dobbins | Receiving Yards | over | 0.11121136707341117 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| underdog|e5a98dfb-9339-4ca9-801d-33553d13e197 | underdog | Michael Salgado-Medina | XP Made | over | 0.11114188305762779 | 2026-11-06T06:34:07Z | 2026-11-07T03:15:00Z |
| underdog|4781b322-c16f-488a-b23d-ff4462376142 | underdog | Matthew Stafford | Pass TDs | under | 0.11063723570251016 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| prizepicks|16719176 | prizepicks | Rhamondre Stevenson | Rec Targets | under | 0.1104895168364537 | 2026-11-05T22:06:44Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|1fecccd3-7915-4b3d-9923-95b353ee0c90 | underdog | J.K. Dobbins | Receptions | under | 0.11024990718515137 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|4bde96ab-c2a0-4521-99f1-927de9f655d5 | underdog | Noah Fifita | Pass Yards | under | 0.10990429484338526 | 2026-11-05T12:22:13Z | 2026-11-07T03:15:00Z |
| prizepicks|16685556 | prizepicks | Dak Prescott | Pass TDs | under | 0.10986040123516894 | 2026-11-05T12:22:13Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|87ced712-c478-425d-ab92-8115cd35eba6 | underdog | Lincoln Kienholz | Pass TDs | under | 0.10982554717127524 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|685edd25-24fb-4af2-a25d-548ec56bea29 | underdog | Tyler Warren | Receptions | under | 0.10969276868099631 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|643576c1-446e-4d42-a0fb-007c8ec84a4d | underdog | CeeDee Lamb | Receiving Yards | under | 0.10963618384661089 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|0c982e54-179a-4101-a215-70855b7eaf00 | underdog | D'Andre Swift | Receptions | under | 0.10961929542717408 | 2026-11-05T12:22:13Z | 2026-11-09T01:20:00Z |
| underdog|b842a878-03ae-4920-8675-e8b6372b0b0d | underdog | KC Concepcion | Receiving Yards | under | 0.10961606364164644 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| prizepicks|16722858 | prizepicks | Kyle Juszczyk | Rec Targets | under | 0.10961448099981719 | 2026-11-06T06:34:07Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|b34d3248-ec10-4121-9c7b-b4746dee816d | underdog | Charlie Kolar | Receptions | under | 0.10960132616239582 | 2026-11-05T12:22:13Z | 2026-11-08T21:05:00Z |
| underdog|57815146-a656-43d6-9668-35d136e67d23 | underdog | Devon Dampier | Pass Yards | under | 0.10960047075501667 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|69a82857-d297-4b15-a385-2a023ebcf054 | underdog | Dalton Kincaid | Receptions | under | 0.10948029145485216 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|29346c18-d730-4e5c-b4eb-9fd6bf0022e3 | underdog | Eric Singleton | Receiving Yards | under | 0.1094767255431981 | 2026-11-05T12:22:13Z | 2026-11-08T00:45:00Z |
| underdog|ba47c124-db10-4b69-b5cf-5ba62f5c4d37 | underdog | Jahmyr Gibbs | Receptions | under | 0.10946590257471323 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|14dd7e40-30bd-4230-aa09-2bcee96f116b | underdog | Katin Houser | Pass Yards | under | 0.10931626492452251 | 2026-11-04T12:10:41Z | 2026-11-07T01:00:00Z |
| underdog|3cd2b418-6262-4bea-8204-d5c65be18a7d | underdog | Adonai Mitchell | Receptions | under | 0.10924843875645252 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|e2b4bad8-1412-4ef1-807c-2d9921b75224 | underdog | John Love | FG Made | over | 0.10906649198025498 | 2026-11-04T12:10:41Z | 2026-11-07T00:00:00Z |
| underdog|b839652f-0e46-467f-9992-35c5469cf144 | underdog | D'Andre Swift | Receiving Yards | under | 0.10895292459147943 | 2026-11-05T12:22:13Z | 2026-11-09T01:20:00Z |
| underdog|84862c77-4fed-4053-8529-6f08d478c203 | underdog | MarShawn Lloyd | Receiving Yards | over | 0.10891889187033654 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|73cebe73-e574-4642-bd7c-dc1ec1949ca6 | underdog | Tait Reynolds | Pass Yards | under | 0.10867407609944801 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|a0eb3048-bcf7-483f-a312-d719004e816e | underdog | Conner Weigman | Pass TDs | under | 0.10842608409629839 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|869fd267-0830-4342-93d3-5dd40662de63 | underdog | Kanoah Vinesett | FG Made | over | 0.10836586366933354 | 2026-11-05T22:06:44Z | 2026-11-07T17:30:00Z |
| underdog|2a03ddda-093f-4ef6-a512-af233e05477d | underdog | Chad Ryland | FG Made | over | 0.10832807545342293 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|7182897d-112d-4bbe-8f0b-571fe8c23a77 | underdog | Cam Cook | Receiving Yards | over | 0.10825855385349281 | 2026-11-05T12:22:13Z | 2026-11-08T02:30:00Z |
| underdog|4c17b548-6dd0-41a7-be94-4eeba93de71a | underdog | Nico Collins | Receptions | under | 0.10808570977681886 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|1022f42b-a007-4d3a-b5ed-9a614c441a49 | underdog | Tim Patrick | Receptions | under | 0.10753144499846912 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| prizepicks|16722855 | prizepicks | Christian McCaffrey | Rec Targets | under | 0.10741475862792937 | 2026-11-06T06:34:07Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|1b7021b4-b333-4256-bc1e-7c9f88464431 | underdog | Jonah Coleman | Receptions | under | 0.10693828108030978 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|5be18191-a04f-4092-a1cd-458a07b6ec60 | underdog | Savion Williams | Receptions | under | 0.10693644241407008 | 2026-11-05T22:06:44Z | 2026-11-08T21:25:00Z |
| underdog|cd533a47-12ae-4545-8253-499e867aa38a | underdog | Tommy Carr | Pass Yards | under | 0.10688800874227689 | 2026-11-05T22:06:44Z | 2026-11-08T00:30:00Z |
| underdog|d599a5ae-1ff8-4df6-9eac-c397c998888d | underdog | Colston Loveland | Receptions | under | 0.10664747026618215 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|552d6ed3-57fe-4ea3-8bd6-3bcec6e29b71 | underdog | Jordan Addison | Receiving Yards | under | 0.10614115606118668 | 2026-11-05T22:06:44Z | 2026-11-10T01:15:00Z |
| underdog|e5e1e737-f54e-41c9-b53a-20d0cd8f6afb | underdog | LaNorris Sellers | Pass Yards | under | 0.1061346822098691 | 2026-11-05T22:06:44Z | 2026-11-07T20:00:00Z |
| underdog|b2610581-1dba-42be-9214-d3cf13c4be2f | underdog | Brian Rowe | Receptions | over | 0.10600187240860914 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|866fa3e8-bc09-4ddc-a0f3-84f88eaf57ce | underdog | John Metchie III | Receptions | under | 0.1060012724235827 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|68027fbe-2681-4510-8eea-3775ceb54e92 | underdog | Dalton Schultz | Receptions | under | 0.10596561958189699 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| prizepicks|16719195 | prizepicks | Treylon Burks | Rec Targets | under | 0.1057451980384182 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|5de198eb-f79d-4e25-a5ba-36c67723d4e8 | underdog | Cooper Barkate | Receiving Yards | under | 0.10552685993347988 | 2026-11-05T22:06:44Z | 2026-11-08T00:30:00Z |
| prizepicks|16718516 | prizepicks | Colston Loveland | Rec Targets | under | 0.1053686257660188 | 2026-11-05T22:06:44Z | 2026-11-08T20:20:00.000-05:00 |
| underdog|e7f08b32-425e-419c-877c-710222411f64 | underdog | Kaelon Black | Rush Yards | under | 0.10507484645254817 | 2026-11-06T06:34:07Z | 2026-11-08T21:25:00Z |
| underdog|575a4b9f-96a0-494c-a0ef-bcd27ce4bdb5 | underdog | Carson Hilbert | XP Made | under | 0.10478017790698868 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|3dd97269-7090-4494-b0ba-aef942cacee8 | underdog | Jared Goff | Pass TDs | under | 0.10432511994565019 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|2b07303d-fe20-4bc5-8345-34bde54e95a1 | underdog | Dak Prescott | Pass TDs | under | 0.10429726760636782 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|2dad27dc-0ecc-4279-8e29-43fe9a205c40 | underdog | Chig Okonkwo | Receiving Yards | under | 0.10425935108835926 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| underdog|4a328574-9067-45a3-b2c8-168d822b5e16 | underdog | T.J. Hockenson | Receiving Yards | under | 0.10407541804729603 | 2026-11-03T11:59:28Z | 2026-11-10T01:15:00Z |
| underdog|1db30023-5914-439c-ac51-c556c30f7a5b | underdog | Marshall Pritchett | Receiving Yards | over | 0.1040578939603718 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|a3d2a9ad-7c96-4647-8be0-43a6f0c7e9c6 | underdog | Mike Matthews | Receptions | under | 0.10398872315492169 | 2026-11-05T12:22:13Z | 2026-11-07T23:15:00Z |
| underdog|0f82b2da-dcf8-4249-afaa-5bb76abe7b55 | underdog | Cardae Mack | Rush Yards | under | 0.10364304070027608 | 2026-11-06T06:34:07Z | 2026-11-08T00:30:00Z |
| underdog|4d4a6a56-43e2-4efe-9cca-06528df03d2e | underdog | Arch Manning | Pass TDs | over | 0.10334919497088374 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|2165bea4-d104-4d1f-b293-9b27eee23074 | underdog | Mitch Griffis | Pass TDs | under | 0.10329919863948966 | 2026-11-05T22:06:44Z | 2026-11-07T00:30:00Z |
| prizepicks|16718518 | prizepicks | Luther Burden III | Rec Targets | under | 0.10325655879442341 | 2026-11-05T22:06:44Z | 2026-11-08T20:20:00.000-05:00 |
| prizepicks|16577039 | prizepicks | Rashee Rice | Rec Yards | under | 0.10318750310261049 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|d82bd3c6-2a60-4879-b845-18484787d341 | underdog | Blake Barnett | Pass Yards | under | 0.1031517391686223 | 2026-11-05T12:22:13Z | 2026-11-07T18:00:00Z |
| underdog|3f7838a7-6e6e-47ac-8296-165647381eb8 | underdog | Jerry Jeudy | Receptions | under | 0.10245858231518723 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|ca26a97e-7e0e-4c51-b8fa-d172c750426d | underdog | Cyrus Allen | Receiving Yards | under | 0.10236946222568843 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|c4b8e03b-86f2-4d6c-b024-04caa813ed63 | underdog | Andre Szmyt | FG Made | under | 0.10236818666743885 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|b125dded-6859-4064-af4c-c4f319765f24 | underdog | Josh Downs | Receiving Yards | under | 0.10226988976676299 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|aaf30715-a58e-484d-b64b-5c9d91157d42 | underdog | Ted Hurst | Receptions | over | 0.10215868472628065 | 2026-11-05T22:06:44Z | 2026-11-09T01:20:00Z |
| underdog|d9d08697-3dd2-4d24-bc73-42297b125227 | underdog | Jameson Williams | Receptions | under | 0.10208410937911938 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|eafb7b4c-e268-458f-85c1-7eeb9d09daba | underdog | Breece Hall | Rush + Rec Yards | under | 0.10207990107922993 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| underdog|7bf309d3-cb09-4113-b642-82526d074215 | underdog | Christian Watson | Receiving Yards | under | 0.10173017572558107 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|f4bba20a-76ec-4df5-9de0-3c7c20bd1a76 | underdog | Keon Coleman | Receptions | under | 0.10169343136994924 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|24a49a3b-5f76-4977-9e37-fd6d51db08c2 | underdog | Jahmyr Gibbs | Rush Yards | under | 0.10154569505675504 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|1c53d9c0-2826-46db-bcf1-524d8e57331a | underdog | Brad Jackson | Pass Yards | under | 0.10145533676347196 | 2026-11-05T22:06:44Z | 2026-11-08T03:30:00Z |
| underdog|23fa46de-8f35-4b86-b931-58c2c9be738f | underdog | Javonte Williams | Rush Yards | under | 0.10095549971421969 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|528efebf-508e-4983-936c-690477ebd224 | underdog | Christian McCaffrey | Receptions | under | 0.10087596308915803 | 2026-11-05T22:06:44Z | 2026-11-08T21:25:00Z |
| underdog|ebb77964-40c0-4665-83be-7d32ded07673 | underdog | Kyle Cunanan | XP Made | over | 0.10085105463048971 | 2026-11-05T12:22:13Z | 2026-11-07T01:00:00Z |
| underdog|6b56f67a-0cb3-4d32-aad1-5ebdb5004b45 | underdog | David Olano | XP Made | over | 0.10069986321094648 | 2026-11-05T12:22:13Z | 2026-11-07T20:00:00Z |
| underdog|e93d4601-6009-4fb8-a624-98b9dcc034f9 | underdog | Treylon Burks | Receiving Yards | under | 0.10064121250380376 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|bdf4a4f2-c1e9-47fc-8fe5-b93626e43e6b | underdog | James Cook | Rush Yards | under | 0.10046089264064739 | 2026-11-05T22:06:44Z | 2026-11-10T01:15:00Z |
| underdog|4c0c83a7-22fc-43b3-9db9-d140c271a605 | underdog | Oronde Gadsden | Receptions | under | 0.10018871071931101 | 2026-11-05T12:22:13Z | 2026-11-08T21:05:00Z |
| underdog|d4a5094c-9736-4dde-95d2-0ea510ff3258 | underdog | Bijan Robinson | Rush Yards | under | 0.10013138750495743 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|381db12f-635c-43b4-898c-04b39c11f438 | underdog | Jamal Polite | Receptions | under | 0.1001216115286192 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| prizepicks|16719192 | prizepicks | Chig Okonkwo | Rec Targets | under | 0.09999749377857736 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|fd8e3565-4701-45c9-840c-5fc035e777ac | underdog | DeSean Bishop | Rush Yards | under | 0.09988529285895009 | 2026-11-05T12:22:13Z | 2026-11-07T23:15:00Z |
| underdog|ad219443-0404-4391-b1bf-2707df6b9de7 | underdog | Omarion Hampton | Receptions | over | 0.09981815938380334 | 2026-11-05T12:22:13Z | 2026-11-08T21:05:00Z |
| underdog|8b5c8f6a-cfbf-4dc8-9e78-0d5df9495d56 | underdog | Sam Leavitt | Pass Yards | under | 0.09949234058268874 | 2026-11-05T22:06:44Z | 2026-11-07T20:30:00Z |
| underdog|d79eb508-80f6-4bcb-aef0-844f3f99f095 | underdog | Michael Hawkins | Pass TDs | over | 0.09931913444464169 | 2026-11-05T22:06:44Z | 2026-11-08T02:30:00Z |
| underdog|54d1f64a-341e-4b14-9c54-93ead4e7667f | underdog | Saquon Barkley | Receiving Yards | under | 0.09931837820137668 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|85ccf44b-f7bc-4dcb-8e44-34d938c7b0be | underdog | Tyler Goodson | Rush Yards | under | 0.09926361066374967 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|e322429d-650a-4a9b-90ae-7c12e88c2be5 | underdog | David Olano | FG Made | over | 0.09919826629893125 | 2026-11-05T12:22:13Z | 2026-11-07T20:00:00Z |
| underdog|39f45cca-973d-4355-ba85-f1085b70cd7c | underdog | Mitchell Evans | Receiving Yards | over | 0.09918365229749104 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|57f73ccb-63b1-451c-bbeb-fbaac3456b03 | underdog | Aaron Jones | Receptions | under | 0.09908473856146005 | 2026-11-05T12:22:13Z | 2026-11-10T01:15:00Z |
| underdog|be48005a-e911-48a5-89d3-0071ee0d1592 | underdog | Devon Dampier | Pass TDs | over | 0.09858639656620943 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|d1e744f7-e48f-432b-ac36-9994d2f0347b | underdog | Chuba Hubbard | Rush Yards | under | 0.09846599432023506 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| prizepicks|16685623 | prizepicks | D'Andre Swift | Rush TDs | over | 0.09831155568334193 | 2026-11-05T12:22:13Z | 2026-11-08T20:20:00.000-05:00 |
| prizepicks|16619747 | prizepicks | Jesse Legree | Recs | under | 0.09789260962625501 | 2026-11-04T12:10:41Z | 2026-11-07T22:30:00.000-05:00 |
| prizepicks|16718529 | prizepicks | KC Concepcion Jr. | Rec Targets | under | 0.09759613041448167 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|ca0b739f-619d-44bc-a06f-c2bc8dfffd97 | underdog | Mitchell Evans | Receptions | over | 0.09744221623392268 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|1337c674-49d5-46cf-939d-084150e82186 | underdog | Trey'Dez Green | Receptions | under | 0.09742503499893362 | 2026-11-05T12:22:13Z | 2026-11-07T20:30:00Z |
| underdog|96e04406-2dc9-4e27-a7a3-24fef33ac8dd | underdog | Mason Taylor | Receiving Yards | under | 0.09725922451571889 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| prizepicks|16623390 | prizepicks | Kyle Pitts Sr. | Recs | under | 0.09724751553828881 | 2026-11-04T12:10:41Z | 2026-11-08T09:30:00.000-05:00 |
| underdog|ac3b4aa2-3e0c-40e9-9fd4-a169b44549a3 | underdog | Mitch Griffis | Pass Yards | under | 0.09722945822861095 | 2026-11-05T22:06:44Z | 2026-11-07T00:30:00Z |
| underdog|dd95402c-e9ca-44e5-a5a3-179e2734707c | underdog | Jordan Addison | Receptions | under | 0.09707338503094809 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|777a6934-83da-4fc6-ae05-670614aac4c8 | underdog | Luther Burden | Receptions | under | 0.0970050304666229 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|a01da2b4-f7eb-47d0-8346-e42d146e6db8 | underdog | Ryan Browne | Pass TDs | under | 0.0966373760343806 | 2026-11-05T22:06:44Z | 2026-11-07T17:30:00Z |
| underdog|1d8cac75-0a34-4da2-b758-1163f0cb3502 | underdog | Fluff Bothwell | Receiving Yards | over | 0.09656381239076028 | 2026-11-06T06:34:07Z | 2026-11-07T21:15:00Z |
| prizepicks|16623392 | prizepicks | Jahan Dotson | Recs | under | 0.09637295072919405 | 2026-11-04T12:10:41Z | 2026-11-08T09:30:00.000-05:00 |
| underdog|382dbb6b-8636-4f45-9336-4f48e41a9ec0 | underdog | Mark Fletcher Jr. | Rush Yards | under | 0.09637086124647443 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|58cc4e38-9328-496c-9c35-0f5e659e9cab | underdog | Keaton Mitchell | Receiving Yards | under | 0.09615862648255569 | 2026-11-06T06:34:07Z | 2026-11-08T21:05:00Z |
| underdog|2bac7b08-fac7-40ce-8ab4-52eed070b62a | underdog | Jordan Love | Pass TDs | under | 0.0961519218860859 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|0c57932e-0ffc-411c-bd91-b60cf90168b0 | underdog | Brandon Aubrey | Kicking Points | under | 0.09590964792109724 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|a02c87fe-f8cd-4593-b8f9-3c37dcab1bfd | underdog | Jake Bates | Kicking Points | under | 0.09584127441212353 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|8e794760-3f49-4bee-81bf-4c5f29c7dc27 | underdog | Tyler Allgeier | Receiving Yards | under | 0.09577866004051383 | 2026-11-05T22:06:44Z | 2026-11-08T21:25:00Z |
| underdog|9c1b45cb-d2e6-4535-a044-78a3bddd6ed8 | underdog | CJ Bailey | Pass TDs | over | 0.09573235892369791 | 2026-11-05T22:06:44Z | 2026-11-07T17:30:00Z |
| underdog|78e5553f-26dc-4ce9-abca-9245000f86c3 | underdog | Polina Kudermetova | Double Faults | under | 0.09567949538698428 | 2026-11-05T12:22:13Z | 2026-11-06T09:30:00Z |
| underdog|50ab1583-86de-4d93-ad49-f9c77e284022 | underdog | Kyle Juszczyk | Receptions | under | 0.09555935955530548 | 2026-11-05T22:06:44Z | 2026-11-08T21:25:00Z |
| underdog|70b674bf-14ef-4526-b90e-42cba3c6d3a5 | underdog | Adam Trautman | Receptions | under | 0.09545112973787573 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|08a1b820-a2ad-448b-890b-dcd34fc73d91 | underdog | Jonathan Taylor | Rush + Rec Yards | under | 0.09516310971670605 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|a186b02c-a2f9-4b57-9502-3efc07964e5f | underdog | KJ Jackson | Pass Yards | under | 0.09509448313433777 | 2026-11-06T06:34:07Z | 2026-11-07T17:45:00Z |
| underdog|f3df021b-e87e-4d22-a9e7-273fdfdebcdf | underdog | Charlie Woerner | Receptions | under | 0.09501160407184561 | 2026-11-05T12:22:13Z | 2026-11-08T14:30:00Z |
| underdog|816cce36-5f20-4e9b-9bab-bf7a84334bda | underdog | J.J. McCarthy | Rush Yards | under | 0.09483178381445445 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|eb5bdb41-4646-402d-82b4-302710f7c29c | underdog | Jalen Coker | Receiving Yards | under | 0.09425398437096033 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|c578d8d7-01f0-4d79-9d4f-3b0725511b5a | underdog | Legend Glasker | Receptions | under | 0.0939339008632083 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|06453bc8-3c32-4402-b79a-c09f64d23356 | underdog | Braden Atkinson | Pass TDs | under | 0.0938819023831381 | 2026-11-05T12:22:13Z | 2026-11-08T03:30:00Z |
| prizepicks|16718561 | prizepicks | Xavier Worthy | Rec Targets | under | 0.09379298905605571 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| prizepicks|16718478 | prizepicks | Jahan Dotson | Rec Targets | under | 0.09297043171542263 | 2026-11-05T22:06:44Z | 2026-11-08T09:30:00.000-05:00 |
| underdog|5b87e878-a87a-4833-a5f2-0c56bd5e34a3 | underdog | Rachaad White | Receiving Yards | under | 0.09288707490475656 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| prizepicks|16685554 | prizepicks | Jared Goff | Pass TDs | under | 0.09280845049511621 | 2026-11-05T12:22:13Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|7abbae0b-0d7f-4ab0-a12b-c6736269a236 | underdog | Jake Fette | Pass TDs | under | 0.09233132561279922 | 2026-11-05T22:06:44Z | 2026-11-08T00:30:00Z |
| underdog|7cee03ac-78b3-4d7b-9754-834e5953a2f4 | underdog | Bryce Young | Rush Yards | under | 0.09215881426223937 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|641f366c-fc02-422d-94ef-532b420c9770 | underdog | Arch Manning | Pass Yards | under | 0.09190007823413737 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|3643f56d-0243-4332-a358-5a0e8e33a064 | underdog | Brendan Baird | FG Made | under | 0.09178178550541316 | 2026-11-04T12:10:41Z | 2026-11-07T00:00:00Z |
| prizepicks|16716167 | prizepicks | Maria Sakkari | Break Points Won | under | 0.09174328646119967 | 2026-11-05T22:06:44Z | 2026-11-06T05:30:00.000-05:00 |
| underdog|93a92a80-a9c0-4066-901b-6e9bb3e6ed82 | underdog | Mateen Bhaghani | XP Made | over | 0.09160309321993065 | 2026-11-04T12:10:41Z | 2026-11-07T17:00:00Z |
| underdog|891e30f8-7158-4065-8c46-b0bc62da09ae | underdog | Nate Frazier | Rush Yards | under | 0.09112227092117486 | 2026-11-04T12:10:41Z | 2026-11-08T00:30:00Z |
| underdog|f9eddbe0-38b8-4913-b9a3-86f9f6cb2cda | underdog | Blake Corum | Rush Yards | under | 0.09068718633654116 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|bd4b0a59-3cf1-4e27-baa9-e6e999015754 | underdog | Yannick Smith | Receptions | under | 0.09048971514892568 | 2026-11-05T12:22:13Z | 2026-11-07T00:00:00Z |
| underdog|21d71ac4-4518-4c20-a927-ee93fc159f14 | underdog | Cameron Dickey | Rush Yards | under | 0.09045418368836045 | 2026-11-04T12:10:41Z | 2026-11-08T02:30:00Z |
| underdog|d52dc310-ea00-4c21-bb95-3798608a708f | underdog | Quentin Johnston | Receptions | under | 0.08995109550904856 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|29ab1834-aeb6-45ca-884e-25275084440c | underdog | Scottre Humphrey | Rush Yards | under | 0.0899130526265629 | 2026-11-06T06:34:07Z | 2026-11-07T02:00:00Z |
| underdog|fe00760f-ecb0-4aa5-ab52-59df3e5772d3 | underdog | Kiefer Sibley | Rush Yards | under | 0.08957248235205661 | 2026-11-06T06:34:07Z | 2026-11-07T02:00:00Z |
| underdog|c90518a9-3b7b-4a28-b1f8-edec396b50bb | underdog | Gavin Lahm | XP Made | under | 0.08887474946252161 | 2026-11-05T12:22:13Z | 2026-11-07T21:15:00Z |
| underdog|50f0cc28-915a-4dd2-ae88-cf03efcede73 | underdog | Caleb Douglas | Receiving Yards | under | 0.08861402690077047 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|27cb9670-5382-48df-ab83-f72399dbeeac | underdog | Travis Kelce | Receiving Yards | under | 0.08860625184263005 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|a9535e18-69cb-422f-bcff-2ba17b1e95cd | underdog | Malik Washington | Pass Yards | under | 0.08846757636534097 | 2026-11-05T22:06:44Z | 2026-11-07T17:30:00Z |
| underdog|ce0b8e2e-29af-4ee3-8d0c-808709b28ece | underdog | Josh Downs | Receptions | under | 0.08810265686695051 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|47cec350-6d8d-442d-8a9d-7cb64d51ca35 | underdog | Nate Roberts | Receiving Yards | over | 0.08795420739677307 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|93c23b7a-e00a-436d-bdbf-012f847dcbfb | underdog | Jonah Coleman | Receiving Yards | under | 0.08784628755770052 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|b722c0eb-24f9-4457-aca1-c570a4906039 | underdog | Chris Olave | Receiving Yards | under | 0.08783600387699941 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|8e5148e6-e9b7-4f81-8abb-ff57d91e4cd0 | underdog | Sione Vaki | Rush Yards | under | 0.08774010921056974 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|e2b129c7-4ce7-4ac8-abb8-cf4529dbd83a | underdog | Kenneth Walker III | Rush + Rec Yards | under | 0.08768372599524399 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|c4f3253c-3c43-48da-989e-430a41e60938 | underdog | Ethan Grunkemeyer | Pass TDs | over | 0.08701299636099313 | 2026-11-04T12:10:41Z | 2026-11-07T00:00:00Z |
| underdog|85d0f744-992b-44c1-8a7c-101d9724dfdc | underdog | Bucky Irving | Receiving Yards | under | 0.08678510565293707 | 2026-11-05T12:22:13Z | 2026-11-09T01:20:00Z |
| underdog|12a2d911-b12a-443c-8611-c6a04a06c827 | underdog | Keenan Allen | Receptions | under | 0.08657096839321532 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|427822f7-2e93-4e7a-8b27-7d7d73610e48 | underdog | TreyShun Hurry | Receiving Yards | under | 0.08650477450845984 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|30d142c6-8017-4e94-b781-4eb760e26d96 | underdog | Evan McPherson | Kicking Points | under | 0.08624660748610669 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|3c25e1f6-5855-4e10-b07c-c168b58f8e8b | underdog | Andre Szmyt | Kicking Points | under | 0.08606085228469695 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|9ecd4e1a-816a-4939-bf25-73902d23441b | underdog | Max Gilbert | FG Made | over | 0.08600901002958494 | 2026-11-06T06:34:07Z | 2026-11-07T17:45:00Z |
| underdog|363e0d87-b2da-4895-b884-c43c948fb886 | underdog | Matt Gay | Kicking Points | over | 0.08600765666946059 | 2026-11-06T06:34:07Z | 2026-11-08T21:25:00Z |
| underdog|a97deb63-dca1-44ac-8812-af3d07f16bb7 | underdog | Jamal Roberts | Receiving Yards | over | 0.08558559107633923 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|2de77434-e9f7-416c-b3f4-c8c99c086db0 | underdog | Braelon Allen | Receptions | under | 0.08548177488523989 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|573a09d8-1d66-4418-8ca5-3e2e403d8b93 | underdog | Trevor Etienne | Rush Yards | under | 0.08500270395062026 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| underdog|771df1cb-a4e1-4db3-a22c-43a4bb5f2de5 | underdog | Isaiah West | Rush Yards | under | 0.08496689908690391 | 2026-11-05T12:22:13Z | 2026-11-07T20:30:00Z |
| underdog|9a11ea53-966f-452f-a1c2-ab1154cc943e | underdog | Jalen Coker | Receptions | under | 0.08455880625865009 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|a2cb61d7-3bf4-4a6c-9e29-6b96da6f7cf6 | underdog | Anthony Colandrea | Total TDs | under | 0.08449392630961017 | 2026-11-05T22:06:44Z | 2026-11-07T01:00:00Z |
| underdog|a8b4d56b-3190-4729-a3e3-fa4952f7fe19 | underdog | Malachi Fields | Receptions | under | 0.08444567676815706 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|82404d76-19b0-4744-8dfc-f7f2fd7987a3 | underdog | Chris Dawn | Receiving Yards | under | 0.08426691261711605 | 2026-11-05T12:22:13Z | 2026-11-08T03:30:00Z |
| underdog|fca3da4f-9476-4b17-ad79-8f80aef153b9 | underdog | Elina Svitolina | Double Faults | under | 0.08423149243173988 | 2026-11-05T12:22:13Z | 2026-11-09T21:10:00Z |
| underdog|3716c38e-c313-439c-8c4e-db38996e9297 | underdog | Liam Boyd | FG Made | under | 0.08392246570987505 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|dc852b5a-38ce-4b3c-ae21-0cf24eb1dfdf | underdog | Gunner Stockton | Pass Yards | under | 0.08391345541361206 | 2026-11-05T22:06:44Z | 2026-11-08T00:30:00Z |
| underdog|d75b9cd4-be57-4ea5-90e6-66b407f1e96b | underdog | Gavin Freeman | Receiving Yards | under | 0.08368894661308302 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|de3a28c0-990e-45e6-b955-eb21bc4ad9a4 | underdog | Patrick Mahomes | Rush Yards | under | 0.08365133891580678 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|ca923a9a-2e8e-46ad-acaf-0b4ecc69a8bd | underdog | Malik Nabers | Receiving Yards | under | 0.08364693870895912 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|4e7cab7c-a9a4-4533-ae0e-b7d96c3d425b | underdog | Jack Bech | Receptions | under | 0.08300134151445937 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|89634d56-a423-40d0-a5c7-22df4d7069ec | underdog | Eric Olsen | Receptions | under | 0.08296120253641759 | 2026-11-05T12:22:13Z | 2026-11-08T03:30:00Z |
| underdog|bef17621-f7f3-4d07-924b-e623b34c8d46 | underdog | Michael Salgado-Medina | FG Made | over | 0.08281383712782858 | 2026-11-04T12:10:41Z | 2026-11-07T03:15:00Z |
| underdog|e0ced813-8b2c-4455-b57b-71da99a39e7d | underdog | Blake Corum | Rush + Rec Yards | under | 0.0827040556047397 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| prizepicks|16719186 | prizepicks | Jaxon Smith-Njigba | Rec Targets | under | 0.08268085501976197 | 2026-11-05T22:06:44Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|aee3048e-e798-412c-b8fd-d7fd1c076061 | underdog | Adonai Mitchell | Receiving Yards | under | 0.0823100615309108 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| underdog|db8a215c-a32b-461f-a74f-392bfed6cd47 | underdog | Sam LaPorta | Receptions | under | 0.08195280346786493 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|5bfcedee-c588-4da9-9ff5-8c14db50399a | underdog | Tyler Allgeier | Rush + Rec Yards | under | 0.08172525609617687 | 2026-11-05T22:06:44Z | 2026-11-08T21:25:00Z |
| underdog|d0e3754b-de87-459c-841a-8b19d795471a | underdog | Demond Williams | Pass Yards | under | 0.08171232837944165 | 2026-11-05T22:06:44Z | 2026-11-07T20:30:00Z |
| underdog|0767ecdc-6c88-403c-a631-567d0902ae5f | underdog | Bijan Robinson | Receptions | under | 0.08140314785642488 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|30c987cb-9450-418a-b4ff-d450e9c0183f | underdog | Ashton Jeanty | Receptions | under | 0.08123630317472041 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|3f37b916-250a-4972-965b-ecb6efeb0ce3 | underdog | Chris Bell | Receiving Yards | under | 0.08090076495058063 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|0ea0b642-98a0-416f-b69d-b7ce615c61b3 | underdog | Drew Stevens | FG Made | under | 0.0806709260026024 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| prizepicks|16718522 | prizepicks | Ja'Marr Chase | Rec Targets | under | 0.08048121700428967 | 2026-11-05T22:06:44Z | 2026-11-08T09:30:00.000-05:00 |
| underdog|08ed069a-7c2b-4c44-b2e2-e31d964f1940 | underdog | Nate Sheppard | Rush Yards | under | 0.08047432863612769 | 2026-11-05T22:06:44Z | 2026-11-07T17:30:00Z |
| underdog|a93191dc-5ab3-4d60-9b3c-0635b721460f | underdog | Baker Mayfield | Rush Yards | under | 0.0804542415617544 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|bbca7d89-86d1-4fba-98a2-ed49d2d91057 | underdog | Quinshon Judkins | Receiving Yards | over | 0.08024791367730699 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| underdog|12bd4374-687f-4ccd-8483-775c124afda4 | underdog | Khalil Shakir | Receptions | under | 0.08011792675984464 | 2026-11-04T12:10:41Z | 2026-11-10T01:15:00Z |
| underdog|dda694e4-f8c1-4755-a1ae-d76fdbf8e245 | underdog | Daylyn Upshaw | Receiving Yards | under | 0.08006662090427419 | 2026-11-05T22:06:44Z | 2026-11-08T00:30:00Z |
| underdog|d64d6002-cbe6-4802-b5c1-a7cdd75e4898 | underdog | Blake Corum | Receiving Yards | over | 0.07956662715644236 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|a2f8424e-28d4-487d-9875-bae9673e09e0 | underdog | Dylan Raiola | Pass TDs | under | 0.0793130185765103 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|18422288-44f7-431d-82a8-cf114d5022be | underdog | Carson Hilbert | FG Made | under | 0.07929489595444217 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|a57c34c5-0685-4573-826a-2780a1571932 | underdog | Kyren Williams | Rush + Rec Yards | under | 0.07885524524463117 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|33218830-4e75-460f-b41a-469bc409fee1 | underdog | Ryan Browne | Pass Yards | under | 0.07827030756965858 | 2026-11-06T06:34:07Z | 2026-11-07T17:30:00Z |
| underdog|b26c659b-559e-4818-854d-5118f2c3403c | underdog | Ed Small | Receptions | over | 0.07823065203309115 | 2026-11-04T12:10:41Z | 2026-11-07T03:15:00Z |
| underdog|c2a92d88-0d14-4da9-a1dd-d6afa0887605 | underdog | Jonathan Taylor | Rush Yards | under | 0.07760504837036786 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| prizepicks|16718545 | prizepicks | Christian Watson | Rec Targets | under | 0.07759156462609396 | 2026-11-05T22:06:44Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|4a89e10d-0ca4-474d-97f5-0bc040a68326 | underdog | Keaton Mitchell | Receptions | under | 0.07757945660569399 | 2026-11-06T06:34:07Z | 2026-11-08T21:05:00Z |
| underdog|416d2a9c-7e4f-40a8-8d3a-2a7bb7bb21a0 | underdog | Tre Richardson | Receiving Yards | under | 0.07720878613309701 | 2026-11-05T22:06:44Z | 2026-11-08T00:30:00Z |
| underdog|62465cef-4749-4f24-a49e-a2d29fb6d9af | underdog | Jaron Tibbs | Receiving Yards | under | 0.07704359216338097 | 2026-11-05T12:22:13Z | 2026-11-07T18:00:00Z |
| underdog|273b4f1f-bf42-4a41-a69b-e9b2f4dd10f1 | underdog | Reggie Virgil | Receiving Yards | under | 0.07701412532993002 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|99f3ae4b-6e3f-48d9-a87c-1281715f1b43 | underdog | Nolan James | Rush Yards | under | 0.0769268807412854 | 2026-11-03T02:21:46Z | 2026-11-08T00:30:00Z |
| underdog|178f08bc-b24b-44cb-8e32-0c49a45abb6e | underdog | AJ Surace | Pass TDs | over | 0.07667779004543462 | 2026-11-05T12:22:13Z | 2026-11-07T21:15:00Z |
| underdog|b037dd4d-81a9-4275-bf43-602a7252c49e | underdog | George Pickens | Receptions | under | 0.0766522668294094 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| prizepicks|16566879 | prizepicks | Drake London | Recs | under | 0.07645666700581077 | 2026-11-04T12:10:41Z | 2026-11-08T09:30:00.000-05:00 |
| underdog|0922f90a-0901-4f10-a983-e4aa2c121442 | underdog | Gianni Spetic | FG Made | over | 0.07604097650812291 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|3db483c9-2cbd-4a61-a415-da9945e7783b | underdog | J'Koby Williams | Rush Yards | under | 0.0751641814121301 | 2026-11-04T12:10:41Z | 2026-11-08T02:30:00Z |
| underdog|80d395a7-fff7-4ff4-9710-ea3c03ad9d49 | underdog | Troy Franklin | Receptions | under | 0.07479838510150683 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|c9f42cb3-782a-42ae-8d36-b838a2e16e5b | underdog | Tyler Goodson | Receptions | under | 0.07447307028831152 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| prizepicks|16719159 | prizepicks | Ashton Jeanty | Rec Targets | under | 0.07445513690876382 | 2026-11-05T22:06:44Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|3896af71-474b-40dd-bd62-e77ad94feb79 | underdog | Byrum Brown | Pass TDs | under | 0.0743093392837626 | 2026-11-06T06:34:07Z | 2026-11-07T17:45:00Z |
| underdog|f7c17ddd-b7da-47e1-b7cc-3c831055be6b | underdog | Dominic Zvada | FG Made | under | 0.0741063683238431 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|63562270-b0a9-458b-9e26-274956838599 | underdog | Jalen Hale | Receptions | over | 0.07399445228452806 | 2026-11-05T12:22:13Z | 2026-11-07T00:00:00Z |
| underdog|55d21c52-58bc-419f-ace8-32daf98964d4 | underdog | Walker Eget | Pass TDs | under | 0.07387684664850058 | 2026-11-05T22:06:44Z | 2026-11-07T17:30:00Z |
| underdog|ae08266e-6845-4eb5-8ae0-c55a994092c7 | underdog | Dylan Raiola | Pass Yards | under | 0.07375588900233532 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|bc765a50-b954-4613-82ce-93029d04d412 | underdog | Aiden Flora | Receiving Yards | over | 0.07359553190708512 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|5571a9d9-5257-413c-94f7-b30035400e37 | underdog | Evan Engram | Receiving Yards | under | 0.07358911959876246 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|a06d5616-3ce4-4197-850d-f0b0c73b34d5 | underdog | Drake Maye | Rush Yards | under | 0.0735599469387288 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| prizepicks|16719174 | prizepicks | T.J. Hockenson | Rec Targets | under | 0.07349799752159802 | 2026-11-05T22:06:44Z | 2026-11-09T20:15:00.000-05:00 |
| underdog|5b58cd6d-7ddf-4a45-ae02-f60cc7eccbd6 | underdog | Brian Bonner | Rush Yards | over | 0.07348526852040016 | 2026-11-05T22:06:44Z | 2026-11-07T20:30:00Z |
| prizepicks|16576406 | prizepicks | Kyren Williams | Rush Yards | under | 0.0734640730790519 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|98370739-8ce7-4116-9352-2a9e7a795fa3 | underdog | C.J. Stroud | Pass TDs | under | 0.07344784426946727 | 2026-11-03T02:21:46Z | 2026-11-08T21:05:00Z |
| underdog|c10a0922-5357-4d12-a34a-fef19f41ae93 | underdog | Dylan Sampson | Receptions | under | 0.073210778810199 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|f7413d7e-001a-4315-8bef-ee5b8c474c0d | underdog | Keelon Russell | Pass Yards | under | 0.07313844310922835 | 2026-11-05T12:22:13Z | 2026-11-07T20:30:00Z |
| underdog|c09e8f25-de98-485a-9a92-3e90c88df8aa | underdog | Cameron Dicker | Kicking Points | under | 0.07288428793483492 | 2026-11-05T22:06:44Z | 2026-11-08T21:05:00Z |
| underdog|d2e52864-35a5-457b-8665-0e135956c290 | underdog | Bear Bachmeier | Pass Yards | under | 0.07282645353132333 | 2026-11-05T22:06:44Z | 2026-11-07T17:00:00Z |
| underdog|d45e253c-f252-4509-a696-99b545feffe9 | underdog | Gianni Spetic | XP Made | over | 0.07268509835321124 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|5c589e9f-50cb-4f4d-bc6c-31a94652a555 | underdog | Darren Waller | Receptions | under | 0.07257323185856346 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|50880572-71dc-48d8-ba1c-131b91584d8d | underdog | DeJuan Williams | Rush Yards | under | 0.07191226289630914 | 2026-11-06T06:34:07Z | 2026-11-07T17:30:00Z |
| prizepicks|16718507 | prizepicks | Khalil Shakir | Rec Targets | under | 0.07175951421598903 | 2026-11-05T22:06:44Z | 2026-11-09T20:15:00.000-05:00 |
| underdog|099c1a61-fff7-42fd-8b84-2a802a10131d | underdog | Charlie Woerner | Receiving Yards | over | 0.0716218067675457 | 2026-11-06T06:34:07Z | 2026-11-08T14:30:00Z |
| underdog|143ec305-dbfc-4481-a66a-798b8b5fdca8 | underdog | Mike Washington | Rush + Rec Yards | under | 0.07125476656934071 | 2026-11-06T06:34:07Z | 2026-11-08T21:25:00Z |
| underdog|21dd5168-ffc9-47c2-b593-f2c831987013 | underdog | Aidan Chiles | Pass Yards | under | 0.07121642529040784 | 2026-11-05T22:06:44Z | 2026-11-08T00:30:00Z |
| underdog|0b0ff05a-c487-4d3f-905d-e95f4a83ca3a | underdog | Nate McCashland | FG Made | over | 0.07120946541515932 | 2026-11-05T12:22:13Z | 2026-11-07T03:15:00Z |
| underdog|82a0c739-4fe5-4f9c-ab98-3f993aa6a3a8 | underdog | Blake Corum | Receptions | under | 0.07120017552093771 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|18ff5fdd-98d5-4665-8d7e-c7c3a7fe48af | underdog | Hudson Clement | Receptions | under | 0.07103456992748092 | 2026-11-05T22:06:44Z | 2026-11-07T01:00:00Z |
| underdog|8f0250ed-dbb2-49a7-8dab-019bc7fb9cec | underdog | Aidan Chiles | Pass TDs | over | 0.07091925513129682 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| prizepicks|16718564 | prizepicks | Cyrus Allen | Rec Targets | under | 0.07077470405848951 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|01068677-aea6-428e-b880-63933e5e7c56 | underdog | Kwazi Gilmer | Receptions | under | 0.07076791839692675 | 2026-11-04T12:10:41Z | 2026-11-07T01:00:00Z |
| underdog|7bff2e43-ab12-4a98-b7e5-04d0c0bbf914 | underdog | Mike Washington | Receptions | under | 0.07071209556400804 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|1f1d13a1-afea-41e0-842f-8af4981136b9 | underdog | Kenneth Walker III | Rush Yards | under | 0.0706968503684764 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|1f8aad36-740c-4ed3-89c7-2156ee173e1e | underdog | Isaiah Likely | Receiving Yards | under | 0.07068676575263688 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|958a8ef4-1b6d-4503-a239-7be87f36e5ec | underdog | AJ Barner | Receiving Yards | under | 0.07065955368582844 | 2026-11-05T22:06:44Z | 2026-11-08T21:25:00Z |
| underdog|555d44e8-8a5e-4431-a64a-05813ba16c93 | underdog | Xavier Williams | Rush Yards | under | 0.07057992950020597 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| prizepicks|16719178 | prizepicks | Chris Olave | Rec Targets | under | 0.07047505206770643 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|d1cbb3da-3a91-40ba-bdec-e8d68a069937 | underdog | Luke Dehnicke | Receptions | under | 0.07046274395456875 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|dc7085a5-bd2b-4e90-9aa5-7e11f5f57193 | underdog | Dohnte Meyers | Receptions | under | 0.07018273167311495 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| prizepicks|16719171 | prizepicks | Malik Washington | Rec Targets | under | 0.07012174955976103 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|9cac1640-ca39-4f1b-931a-e2c850308466 | underdog | Noah Gray | Receptions | over | 0.06995762914057951 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|653afc15-7559-442b-b34d-1f0091847e3b | underdog | Chase Brown | Receptions | under | 0.06992427729238937 | 2026-11-05T12:22:13Z | 2026-11-08T14:30:00Z |
| underdog|4f42e71e-9977-4467-9c6f-587a1fb01921 | underdog | Malik Willis | Pass TDs | under | 0.0698898131874599 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|a8b07aaf-9e96-48ee-8ca1-37bcc89b9eb4 | underdog | Jackson Kleather | XP Made | over | 0.06961802625005475 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|645d1e24-ea6b-4524-966f-4ad8a9808469 | underdog | DaSaahn Brame | Receptions | under | 0.06953393528194685 | 2026-11-05T12:22:13Z | 2026-11-07T23:15:00Z |
| underdog|bd8faee7-5c2b-4852-b7fb-5e270f687f55 | underdog | Tee Higgins | Receiving Yards | under | 0.06937703329058331 | 2026-11-05T12:22:13Z | 2026-11-08T14:30:00Z |
| prizepicks|16576408 | prizepicks | Javonte Williams | Rush Yards | under | 0.06913799764143458 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|48250e63-bacd-4255-aa11-0624333d259c | underdog | Ryan Flournoy | Receiving Yards | under | 0.0689284286792391 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|acb7cde5-643f-4f05-8d8c-f460baaa6de2 | underdog | Drake Lindsey | Pass TDs | under | 0.06876657393878849 | 2026-11-05T22:06:44Z | 2026-11-07T17:00:00Z |
| underdog|e79ceeb9-6532-4b64-84f7-b2bff2c5f1f3 | underdog | Juwan Johnson | Receiving Yards | under | 0.06874994112405464 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| underdog|f9fe24e6-dd92-40f6-a6d8-49347d9716b3 | underdog | Tylik Hill | Rush Yards | over | 0.0687067760591078 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|1676285c-b66c-440c-ba94-3e1e1dd2226c | underdog | Jesse Legree | Receiving Yards | under | 0.06868793139917972 | 2026-11-05T12:22:13Z | 2026-11-08T03:30:00Z |
| prizepicks|16722854 | prizepicks | Brandin Cooks | Rec Targets | under | 0.068448315251599 | 2026-11-06T06:34:07Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|95b9556b-02ea-4716-95a3-378600721291 | underdog | Kanoah Vinesett | XP Made | over | 0.0683250670662876 | 2026-11-05T22:06:44Z | 2026-11-07T17:30:00Z |
| prizepicks|16683643 | prizepicks | Jake Bates | Kicking Points | under | 0.06818662504942608 | 2026-11-05T12:22:13Z | 2026-11-08T13:00:00.000-05:00 |
| prizepicks|16718491 | prizepicks | Olamide Zaccheaus | Rec Targets | under | 0.06800425311674296 | 2026-11-05T22:06:44Z | 2026-11-08T09:30:00.000-05:00 |
| underdog|90c3977f-8381-4a61-9dbd-94f49ffcf439 | underdog | Drew Sample | Receiving Yards | over | 0.0679032038021633 | 2026-11-05T12:22:13Z | 2026-11-08T14:30:00Z |
| underdog|a41d4208-558b-4e9e-ace0-423efa6d914f | underdog | Brendan Baird | XP Made | under | 0.06786423255342389 | 2026-11-04T12:10:41Z | 2026-11-07T00:00:00Z |
| underdog|b479ca9d-4d1c-454f-bfff-733cb2735065 | underdog | Jason Myers | Kicking Points | under | 0.06786338640966882 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|01b515f8-720e-4e59-87d0-c60899b62954 | underdog | Jamal Rule | Rush Yards | under | 0.06781922288970477 | 2026-11-06T06:34:07Z | 2026-11-07T01:00:00Z |
| underdog|aa2400e1-61c6-42b8-a00e-4df185d8e29a | underdog | Peyton Woodring | XP Made | over | 0.06770360800211805 | 2026-11-04T12:10:41Z | 2026-11-08T00:30:00Z |
| prizepicks|16734081 | prizepicks | Sorana Cirstea | Double Faults | under | 0.0676968175376147 | 2026-11-06T06:34:07Z | 2026-11-06T03:30:00.000-05:00 |
| underdog|b4a11205-f19f-4256-9e1e-6703e6a4644a | underdog | Jaylen Waddle | Receptions | under | 0.06756067788820463 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|f9330e16-1ebe-495a-a353-0a85b5f209b9 | underdog | CJ Bailey | Pass Yards | under | 0.06742293822419498 | 2026-11-05T22:06:44Z | 2026-11-07T17:30:00Z |
| underdog|7db9e716-c382-497b-88b9-f6f6c10c7108 | underdog | Max Gilbert | XP Made | over | 0.06722338435736108 | 2026-11-06T06:34:07Z | 2026-11-07T17:45:00Z |
| underdog|8f9a7a73-acd6-4922-a1e5-c9b931fd47c8 | underdog | Samaje Perine | Receiving Yards | over | 0.06675361243904465 | 2026-11-06T06:34:07Z | 2026-11-08T14:30:00Z |
| underdog|480b8a53-750b-4531-914d-b24d9cc3be67 | underdog | Gunner Stockton | Pass TDs | over | 0.06653840324761084 | 2026-11-04T12:10:41Z | 2026-11-08T00:30:00Z |
| prizepicks|16719164 | prizepicks | Quentin Johnston | Rec Targets | under | 0.06632694700699171 | 2026-11-05T22:06:44Z | 2026-11-08T16:05:00.000-05:00 |
| underdog|d4f2b5ca-0b3f-4658-962d-e49d13b62596 | underdog | Mike Gesicki | Receptions | under | 0.06624716319361124 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|fc8a7d1c-fc88-48bd-9122-4cea2b71c647 | underdog | Xavier Hutchinson | Receptions | under | 0.06623799366444505 | 2026-11-05T12:22:13Z | 2026-11-08T21:05:00Z |
| underdog|cdc62382-2a50-4934-b1a5-b8921613a738 | underdog | Tyler Robles | FG Made | over | 0.06621739274981686 | 2026-11-05T22:06:44Z | 2026-11-07T20:30:00Z |
| underdog|23d0cc4b-98bb-4088-a807-e58efa7a08e7 | underdog | Caleb Cunningham | Receiving Yards | over | 0.06618295356151871 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|97eab18d-9198-41a6-9923-15704c5dbe65 | underdog | Breece Hall | Rush Yards | under | 0.0661698771066409 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|75e1cf1b-6b66-49ca-b1a6-9f711b760bf0 | underdog | Malik Washington | Pass TDs | under | 0.06594882399474966 | 2026-11-05T22:06:44Z | 2026-11-07T17:30:00Z |
| underdog|cbc93e7f-1d7b-4b99-bb7d-ed15c78a51cd | underdog | Trinidad Chambliss | Pass TDs | over | 0.06592267044885508 | 2026-11-05T22:06:44Z | 2026-11-08T00:30:00Z |
| underdog|c7130de7-7997-4c25-8f1b-bb6b535a8608 | underdog | Antonia Ruzic | Double Faults | over | 0.06582373042117506 | 2026-11-05T22:06:44Z | 2026-11-06T11:40:00Z |
| underdog|17d196b6-916b-4467-86c8-3e43337d1b9d | underdog | Josh Jacobs | Receiving Yards | under | 0.06580018595374104 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|e2076474-ba9e-4c4a-8a5e-8756583f0c4e | underdog | Woody Marks | Receiving Yards | under | 0.06554944061032464 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|b6d69e49-b79f-407a-8114-42990a99457e | underdog | Isaac Wilson | Pass Yards | under | 0.0654418546647958 | 2026-11-05T22:06:44Z | 2026-11-08T00:30:00Z |
| underdog|34afce0e-7ed1-435f-a354-760712a31ef4 | underdog | Jacory Barney | Receptions | under | 0.06536795043669508 | 2026-11-05T22:06:44Z | 2026-11-07T01:00:00Z |
| prizepicks|16629444 | prizepicks | Wayne Knight | Rush Atts | under | 0.06520056369225546 | 2026-11-05T12:22:13Z | 2026-11-07T12:00:00.000-05:00 |
| underdog|f89d903a-bd78-4938-a9b8-bfc8c1768685 | underdog | Que'Sean Brown | Receptions | under | 0.06494340682637201 | 2026-11-05T12:22:13Z | 2026-11-07T00:00:00Z |
| underdog|1d02ab45-4ffa-4cd8-80e2-89f52af64442 | underdog | Drew Sample | Receptions | under | 0.0648910280627768 | 2026-11-05T22:06:44Z | 2026-11-08T14:30:00Z |
| underdog|b13bd436-9bc2-4867-9041-17de5aa4b928 | underdog | Michael Wilson | Receiving Yards | under | 0.06474486073770425 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|1466368e-c6ce-4de6-8814-1a5e1d544d1d | underdog | Spencer Porath | FG Made | under | 0.06463882026125989 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|e00a37ed-d410-4482-ad2c-a051ecd9d5f1 | underdog | Jeffrey Overton | Receiving Yards | over | 0.06457901851406311 | 2026-11-04T12:10:41Z | 2026-11-07T00:00:00Z |
| underdog|1e146d1e-95ac-4e18-b97f-874278e4440b | underdog | Emmett Johnson | Rush Yards | under | 0.06444132725080376 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|62e87ebf-5eeb-4023-abde-cbc9d852fb85 | underdog | TJ Engleman | Rush Yards | under | 0.06430958971903533 | 2026-11-05T22:06:44Z | 2026-11-07T00:30:00Z |
| underdog|a886d218-e5f0-47b6-88c2-0a782007cb39 | underdog | Tyler Allgeier | Rush Yards | under | 0.06416014757999955 | 2026-11-05T22:06:44Z | 2026-11-08T21:25:00Z |
| prizepicks|16719175 | prizepicks | Jordan Addison | Rec Targets | under | 0.06403524396214921 | 2026-11-05T22:06:44Z | 2026-11-09T20:15:00.000-05:00 |
| prizepicks|16718525 | prizepicks | Tee Higgins | Rec Targets | under | 0.06403084263606129 | 2026-11-05T22:06:44Z | 2026-11-08T09:30:00.000-05:00 |
| underdog|e5598605-b771-40d4-a896-945151550af7 | underdog | JC French | Pass Yards | under | 0.0637897607221598 | 2026-11-05T12:22:13Z | 2026-11-07T20:30:00Z |
| underdog|8ece24e0-b2e4-4fa3-b6b4-5845b58f2de9 | underdog | Kenny Minchey | Pass Yards | under | 0.06358679107944964 | 2026-11-05T12:22:13Z | 2026-11-07T23:15:00Z |
| underdog|21931440-adec-46d4-b530-994878d9e427 | underdog | T.J. Hockenson | Receptions | under | 0.06344057443403939 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|20e2d065-8b33-44d8-b704-2f53c8db5429 | underdog | DJ Epps | Receiving Yards | over | 0.06272142066281527 | 2026-11-05T12:22:13Z | 2026-11-08T02:30:00Z |
| underdog|e85c31f7-9c9e-4d10-b893-980e11cee71d | underdog | Chas Nimrod | Receiving Yards | under | 0.062088814076110665 | 2026-11-06T06:34:07Z | 2026-11-07T17:45:00Z |
| underdog|dd1f7172-8330-424d-ac7f-1765ab353fcc | underdog | Dominic Zvada | Kicking Points | under | 0.062049653446879294 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| prizepicks|16567865 | prizepicks | Michael Penix Jr. | Pass TDs | under | 0.06194406494725502 | 2026-11-05T12:22:13Z | 2026-11-08T09:30:00.000-05:00 |
| underdog|e10eb242-4e7d-4ce2-8e47-3d911d92bb30 | underdog | Kalieb Osborne | Pass Yards | under | 0.06190495259316475 | 2026-11-06T06:34:07Z | 2026-11-07T17:00:00Z |
| underdog|adeae18f-e6d9-4b71-855a-d10140f61576 | underdog | Jadon Porter | Receiving Yards | over | 0.06181736022618467 | 2026-11-05T22:06:44Z | 2026-11-07T17:00:00Z |
| prizepicks|16577034 | prizepicks | Denzel Boston | Rec Yards | under | 0.06162987154195598 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| prizepicks|16718512 | prizepicks | Tetairoa McMillan | Rec Targets | under | 0.06149813023951123 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|94533c8c-852b-436b-8c3e-30871f71ee63 | underdog | Devin McCuin | Receptions | over | 0.061271839861702426 | 2026-11-05T12:22:13Z | 2026-11-07T20:30:00Z |
| prizepicks|16713256 | prizepicks | Ben Shelton | Total Games | over | 0.061040211655997934 | 2026-11-05T22:06:44Z | 2026-11-06T08:00:00.000-05:00 |
| underdog|8c265bcd-7b60-4798-8607-03c1259a21e4 | underdog | Trey Smack | FG Made | under | 0.06104007152947344 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|c2bc47c2-6d3f-48ee-b74d-c4f141f4a11a | underdog | Kayshon Boutte | Receiving Yards | over | 0.060977623679458914 | 2026-11-05T22:06:44Z | 2026-11-08T21:05:00Z |
| underdog|fac4af10-165a-4177-944e-51ad9c5660f6 | underdog | Matt Gay | FG Made | over | 0.06076705695301998 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|07cbccc8-0fba-4542-8414-c5920607d6bf | underdog | Kevin Jennings | Pass Yards | under | 0.06069823598347823 | 2026-11-04T12:10:41Z | 2026-11-07T00:00:00Z |
| prizepicks|16722942 | prizepicks | Kenny Gainwell | Recs | under | 0.06053274770535577 | 2026-11-06T06:34:07Z | 2026-11-08T20:20:00.000-05:00 |
| underdog|b0a240d5-44af-42ff-a812-2f1b16380d9b | underdog | Nyziah Hunter | Receptions | under | 0.06044397243255828 | 2026-11-05T12:22:13Z | 2026-11-07T01:00:00Z |
| underdog|99a82066-3195-47f8-b8e0-1a8bb7c63ca5 | underdog | Wayshawn Parker | Receiving Yards | over | 0.060436074136964946 | 2026-11-06T06:34:07Z | 2026-11-07T17:00:00Z |
| underdog|3814f339-5522-40ce-a555-8b7dbed6eb31 | underdog | Richard Young | Rush Yards | under | 0.060345052741267335 | 2026-11-05T22:06:44Z | 2026-11-08T00:30:00Z |
| underdog|75fc0d6b-fc95-4755-9dca-a70f72575381 | underdog | Kimani Vidal | Rush + Rec Yards | under | 0.060182508715502125 | 2026-11-05T22:06:44Z | 2026-11-08T21:05:00Z |
| underdog|ca398302-b7f2-41c3-b0f0-22bb229c27a0 | underdog | Tre' Harris | Receiving Yards | under | 0.060182129409127705 | 2026-11-05T22:06:44Z | 2026-11-08T21:05:00Z |
| underdog|d29599ad-f597-4f28-9d87-acf1c29a3761 | underdog | Elijah Higgins | Receptions | under | 0.060018765343776814 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|ce15f976-d7f9-425f-ad6c-ee1a00299302 | underdog | Jahmyr Gibbs | Receiving Yards | under | 0.059821904171410645 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| underdog|be36f808-dbd3-4226-adee-a8537113a1e5 | underdog | Ethan Grunkemeyer | Pass Yards | under | 0.05966040798874328 | 2026-11-04T12:10:41Z | 2026-11-07T00:00:00Z |
| underdog|d0960391-8a29-49e1-adce-9b8b9a13efe6 | underdog | Kimani Vidal | Receptions | under | 0.0595189274468374 | 2026-11-05T12:22:13Z | 2026-11-08T21:05:00Z |
| underdog|2878805f-db94-4b6a-b6bd-36a2b9ac7078 | underdog | Kendrick Raphael | Rush Yards | under | 0.05944789530063532 | 2026-11-05T22:06:44Z | 2026-11-07T00:00:00Z |
| underdog|5a604162-06d7-42a5-b871-10416c6fa8b6 | underdog | Tommy Carr | Pass TDs | under | 0.059415967714466 | 2026-11-05T22:06:44Z | 2026-11-08T00:30:00Z |
| underdog|78f92e19-5c31-4d49-a704-dea3e1ea7994 | underdog | Foster Moreau | Receptions | over | 0.05932154173705445 | 2026-11-05T12:22:13Z | 2026-11-08T21:05:00Z |
| underdog|8d5e4fd2-08fe-4ab9-9a82-f4b75d3bea05 | underdog | Tetairoa McMillan | Receiving Yards | under | 0.059188927073352327 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|3b554414-84d2-41b4-93ac-fceb51bfce89 | underdog | Dilin Jones | Receptions | under | 0.05910993829171962 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|a10e90f9-892e-489b-87e7-98258489a4ec | underdog | Chig Okonkwo | Receptions | under | 0.05901702938378406 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|9010dad9-5de4-4ca5-b504-7ea92845c328 | underdog | Rocco Becht | Rush Yards | over | 0.059015051888118064 | 2026-11-05T22:06:44Z | 2026-11-07T20:30:00Z |
| underdog|5f83ba00-76c5-472d-91b8-5490a16ef0d6 | underdog | Anthony Colandrea | Pass TDs | over | 0.05889302378542982 | 2026-11-05T12:22:13Z | 2026-11-07T01:00:00Z |
| underdog|9a2c1919-44e1-42d6-9c2e-ad2da3f1b8df | underdog | Lincoln Kienholz | Pass Yards | under | 0.05879251340946767 | 2026-11-05T22:06:44Z | 2026-11-08T00:30:00Z |
| underdog|464fbf32-ce38-4c8f-bc70-190cf5d64c92 | underdog | MarShawn Lloyd | Receptions | under | 0.05868983465783262 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| prizepicks|16718559 | prizepicks | Travis Kelce | Rec Targets | under | 0.058686248860410406 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|cd4c17b5-3de5-4eab-a1a1-61fb1258f334 | underdog | Noah Gray | Receiving Yards | over | 0.05866094475782779 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| prizepicks|16719167 | prizepicks | Puka Nacua | Rec Targets | under | 0.05865213234044242 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|82d0621c-9442-4056-a754-bae0db9ca37a | underdog | Xavier Hutchinson | Receiving Yards | over | 0.0586476446665154 | 2026-11-05T22:06:44Z | 2026-11-08T21:05:00Z |
| underdog|5c1dad6e-619c-4575-9b10-738e17d39df7 | underdog | Ashton Jeanty | Receiving Yards | under | 0.05850227908119554 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|d146dfb3-fcb5-4654-a1f6-64215170adeb | underdog | Jessica Pegula | Double Faults | under | 0.05846688292835567 | 2026-11-05T12:22:13Z | 2026-11-08T21:10:00Z |
| underdog|afda48e8-0d61-4673-aecd-d18deb0ca8b9 | underdog | Ed Small | Receiving Yards | over | 0.05839356214069036 | 2026-11-04T12:10:41Z | 2026-11-07T03:15:00Z |
| underdog|8a748e05-956a-4a40-a6dc-c7788188b33f | underdog | Carson Wentz | Pass TDs | under | 0.058336194057320934 | 2026-11-05T22:06:44Z | 2026-11-10T01:15:00Z |
| underdog|097f1c9d-9fd7-4c66-b024-b6f792a6ddbe | underdog | Raleek Brown | Rush Yards | under | 0.05828535641008248 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|cc8d9cae-e2d7-46b3-b82e-af84fe68c16d | underdog | Beau Sparks | Receiving Yards | under | 0.058018388049906444 | 2026-11-05T12:22:13Z | 2026-11-08T03:30:00Z |
| underdog|089ce83f-49f9-46ad-83c1-06b27856f11e | underdog | Tyler Shough | Pass TDs | under | 0.0579713928349842 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|c7f223f5-1db6-4b90-9fbb-b219544bd20b | underdog | Jaleel Skinner | Receiving Yards | over | 0.0579671544436442 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|9dae6194-3778-427b-aa64-184da5cacda0 | underdog | Cornell Hatcher | Rush Yards | under | 0.057928275348360314 | 2026-11-05T12:22:13Z | 2026-11-08T03:30:00Z |
| underdog|0cbe8572-f373-40c7-bc91-3896efd0ba18 | underdog | Evan Stewart | Receiving Yards | over | 0.05781868428032133 | 2026-11-05T12:22:13Z | 2026-11-07T20:30:00Z |
| underdog|ef93512e-7037-4e52-adab-e5a0e92cb14b | underdog | Kyler Kasper | Receptions | under | 0.0577929902830534 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| prizepicks|16685553 | prizepicks | Malik Willis | Pass TDs | under | 0.05774292119343538 | 2026-11-05T12:22:13Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|03683cb5-d08b-46d2-8daf-b7a187b04861 | underdog | Collin Dixon | Receiving Yards | under | 0.05774001382855143 | 2026-11-04T12:10:41Z | 2026-11-07T01:00:00Z |
| underdog|363f2a86-aea7-488d-8f25-6c2926e28588 | underdog | Michael Penix | Pass TDs | under | 0.05769866616807584 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|94b26160-85f3-4b0e-a636-0a205a4a8a14 | underdog | Omarion Hampton | Rush + Rec Yards | under | 0.057685561031392885 | 2026-11-05T22:06:44Z | 2026-11-08T21:05:00Z |
| underdog|d02386e9-a6be-491a-b11c-0db9561342f3 | underdog | Omarion Hampton | Rush Yards | under | 0.0574974439645306 | 2026-11-05T22:06:44Z | 2026-11-08T21:05:00Z |
| underdog|6cea53c4-9d13-4b3e-8f35-09016359467a | underdog | Katin Houser | Pass TDs | over | 0.05741840076591065 | 2026-11-04T12:10:41Z | 2026-11-07T01:00:00Z |
| underdog|1a9bb6cc-8c99-4567-9740-702629fc8b15 | underdog | Mazeo Bennett | Receptions | under | 0.05730068954397416 | 2026-11-05T22:06:44Z | 2026-11-07T20:00:00Z |
| underdog|4ed6c534-a882-4037-a5c5-3d3c36ee0467 | underdog | Jordan Faison | Receiving Yards | under | 0.05721438415905 | 2026-11-03T02:21:46Z | 2026-11-08T00:30:00Z |
| underdog|82215f35-d978-41ed-b4b6-3e1171e32afc | underdog | Austin Simmons | Pass TDs | under | 0.05701792055392729 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|623fe967-1a3e-408f-b0cb-0bf7da802b8a | underdog | Dak Prescott | Rush Yards | over | 0.0570102313442149 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|b094236c-ba86-4187-9f50-dfd372652b8b | underdog | Tre Tucker | Receptions | under | 0.05656143515129497 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|befbd56b-e648-4437-a050-c9ecb32ce65a | underdog | Corey Kiner | Rush + Rec Yards | under | 0.05651284215717434 | 2026-11-06T06:34:07Z | 2026-11-08T21:25:00Z |
| underdog|2cf795d7-7279-4cdf-9ea4-10556bd4239d | underdog | Kenyon Sadiq | Receptions | over | 0.056179967492667515 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| underdog|4c30ef86-b02d-428c-be83-36d212c6eb21 | underdog | Rocco Becht | Pass Yards | under | 0.056166509243936735 | 2026-11-05T22:06:44Z | 2026-11-07T20:30:00Z |
| prizepicks|16623321 | prizepicks | Isaiah Mizell | Recs | under | 0.05613807100115675 | 2026-11-04T12:10:41Z | 2026-11-06T22:15:00.000-05:00 |
| underdog|72424239-3938-4c03-a39e-4cf5eebc76fd | underdog | Ashton Daniels | Rush Yards | under | 0.05590103432432425 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|e5503b49-7874-4785-b938-ac08739aa23c | underdog | Billy Edwards Jr. | Pass TDs | under | 0.055860973923938406 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|48603add-d136-41df-b578-2323b8a1caa7 | underdog | Rome Odunze | Receptions | under | 0.05570918963942184 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|2d9d75ee-81b8-4cf9-afb2-5697717dba80 | underdog | Gary Givens | Receiving Yards | over | 0.05567743579484841 | 2026-11-05T22:06:44Z | 2026-11-07T02:00:00Z |
| prizepicks|16719193 | prizepicks | Rachaad White | Rec Targets | under | 0.055479385567673956 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|3c4aee76-fb32-4603-82d0-81351387b1e1 | underdog | Kalif Raymond | Receptions | under | 0.05532157679971539 | 2026-11-05T12:22:13Z | 2026-11-09T01:20:00Z |
| underdog|a31317ee-e954-402a-9e50-4a55ffc781d1 | underdog | Jaylen Raynor | Pass TDs | under | 0.0548056389593522 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|19a672f3-50fe-4033-813c-78daf721de03 | underdog | Mike Washington | Rush Yards | under | 0.05471570014322025 | 2026-11-05T22:06:44Z | 2026-11-08T21:25:00Z |
| underdog|844d8994-eb1a-4135-917e-a68c00abf5fd | underdog | Tre' Harris | Receptions | under | 0.05470210954117727 | 2026-11-05T12:22:13Z | 2026-11-08T21:05:00Z |
| prizepicks|16691320 | prizepicks | Robin Montgomery | Total Games | over | 0.05466987949254476 | 2026-11-05T22:06:44Z | 2026-11-06T05:40:00.000-05:00 |
| underdog|e5de3304-8e95-4124-954c-9ff251883bab | underdog | Kenny Minchey | Rush Yards | over | 0.05425628323804066 | 2026-11-05T12:22:13Z | 2026-11-07T23:15:00Z |
| underdog|a90c4033-4dc0-4bff-8788-579fa5420077 | underdog | Treylon Burks | Receptions | under | 0.05419147947818659 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| prizepicks|16577036 | prizepicks | KC Concepcion Jr. | Rec Yards | under | 0.054101039282902996 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|cce8999b-73b6-4a3b-a40d-76aad63c8cba | underdog | Drake Lindsey | Pass Yards | under | 0.05406000313128101 | 2026-11-04T12:10:41Z | 2026-11-07T17:00:00Z |
| underdog|1c2cde05-b6d7-4474-9d9e-8f9b3062e070 | underdog | Puka Nacua | Receptions | under | 0.05380728482585917 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|e01ed5ff-4bf0-4328-80bb-372c2a56d1cb | underdog | Jeremiah Smith | Receptions | under | 0.053719870131973324 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|2f6615ec-e303-4723-8de9-515407930761 | underdog | Kedrick Reescano | Rush Yards | under | 0.05350218820934205 | 2026-11-04T12:10:41Z | 2026-11-07T03:15:00Z |
| underdog|71d9b967-8695-476c-a378-0a790c548319 | underdog | Nyziah Hunter | Receiving Yards | under | 0.053407546528774996 | 2026-11-04T12:10:41Z | 2026-11-07T01:00:00Z |
| underdog|e55382b2-c395-46d4-8518-8309c9d2f8e4 | underdog | JC French | Rush Yards | over | 0.053385662154178726 | 2026-11-05T12:22:13Z | 2026-11-07T20:30:00Z |
| underdog|97889cee-bb36-4d05-b351-a674927b93e5 | underdog | Braylon Staley | Receiving Yards | under | 0.053369351238770846 | 2026-11-05T12:22:13Z | 2026-11-07T23:15:00Z |
| underdog|1f6ec128-0f98-4fab-b889-6fa33628a38b | underdog | Reggie Virgil | Receptions | under | 0.053005643668652125 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|c576f022-bc2d-4dc5-977d-7e4dc4f852fc | underdog | Bijan Robinson | Receiving Yards | under | 0.052599299690431756 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|9e0cfe1d-3ce4-4cf3-bce8-09e661cb3cda | underdog | Ryan Flournoy | Receptions | under | 0.052546796586534494 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|5d4a6a94-4490-4488-8f26-0d4ccba55e0b | underdog | Savion Williams | Receiving Yards | under | 0.0525122155374117 | 2026-11-05T22:06:44Z | 2026-11-08T21:25:00Z |
| underdog|f4af8d61-8588-4d80-ac8d-fd8686a33979 | underdog | Malik Willis | Rush Yards | under | 0.052470845197019944 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|57089bc8-aea4-4d62-9dfe-fb04c853be84 | underdog | D.J. Crowther | Rush Yards | under | 0.05232250537979799 | 2026-11-05T22:06:44Z | 2026-11-07T00:30:00Z |
| underdog|74b76a65-dbd7-4d0a-88a8-11aa3d120252 | underdog | Willie Rodriguez | Receiving Yards | under | 0.052230432348502775 | 2026-11-05T12:22:13Z | 2026-11-07T23:15:00Z |
| underdog|e3313430-aacf-44db-883d-52e439eff18b | underdog | Drew Wagner | Receiving Yards | over | 0.05222919720332875 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|7c09637f-ba5b-48d9-a7b4-45cc01362313 | underdog | Justin Herbert | Rush Yards | under | 0.05178516711907766 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| prizepicks|16718497 | prizepicks | DJ Moore | Rec Targets | under | 0.051713641503083774 | 2026-11-05T22:06:44Z | 2026-11-09T20:15:00.000-05:00 |
| prizepicks|16578332 | prizepicks | Braylon Staley | Recs | under | 0.05153228331798554 | 2026-11-05T12:22:13Z | 2026-11-07T18:15:00.000-05:00 |
| underdog|0bd7ee4e-5003-468e-a88a-b15e135713a5 | underdog | Keshaun Singleton | Receiving Yards | under | 0.05152161739055083 | 2026-11-06T06:34:07Z | 2026-11-07T17:45:00Z |
| underdog|56673d79-098e-485c-841d-1347c9ef4713 | underdog | Byrum Brown | Rush Yards | under | 0.05125785355040946 | 2026-11-06T06:34:07Z | 2026-11-07T17:45:00Z |
| underdog|02327278-6fbb-4fd1-82b5-da6a4d3a51cd | underdog | Abu Sama | Rush Yards | under | 0.05111838731377327 | 2026-11-05T22:06:44Z | 2026-11-07T21:15:00Z |
| underdog|f53b7417-9f4b-452e-8790-b2f174f6e53e | underdog | Demond Williams | Rush Yards | under | 0.050867144294761135 | 2026-11-05T22:06:44Z | 2026-11-07T20:30:00Z |
| underdog|30fb664e-b7e5-416c-84d9-9981ffc6a84f | underdog | Rico Scott | Receptions | under | 0.050697211562924394 | 2026-11-05T22:06:44Z | 2026-11-07T20:30:00Z |
| underdog|e46702d6-ae35-43c0-ab3b-2e638d0153d9 | underdog | Chad Ryland | Kicking Points | over | 0.0506262653818188 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| prizepicks|16718517 | prizepicks | D'Andre Swift | Rec Targets | under | 0.0506216499863863 | 2026-11-05T22:06:44Z | 2026-11-08T20:20:00.000-05:00 |
| underdog|a823d7dd-f020-47c2-abc7-ab9d25d21cbf | underdog | JC French | Pass TDs | over | 0.05059286004736313 | 2026-11-05T12:22:13Z | 2026-11-07T20:30:00Z |
| underdog|b4bf9f2b-e849-446b-a805-eda4d01af7be | underdog | Khalil Shakir | Receiving Yards | under | 0.05058312311415858 | 2026-11-04T12:10:41Z | 2026-11-10T01:15:00Z |
| underdog|6d2ef97d-85ec-4784-b781-eb26c8048aba | underdog | Ashton Daniels | Pass Yards | under | 0.050551246622958734 | 2026-11-06T06:34:07Z | 2026-11-07T17:00:00Z |
| underdog|d8a6f1af-49f3-4881-bd57-1d0c23846f83 | underdog | John Metchie III | Receiving Yards | under | 0.05051349271703243 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| prizepicks|16718531 | prizepicks | George Pickens | Rec Targets | under | 0.050469580643767276 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|065a2ce0-b802-4321-9321-acb62214d65b | underdog | Nyck Harbor | Receptions | under | 0.05046765911819062 | 2026-11-05T22:06:44Z | 2026-11-07T20:00:00Z |
| underdog|abdc520a-150d-45db-a145-74983f031284 | underdog | Keaton Mitchell | Rush + Rec Yards | under | 0.0504631749843939 | 2026-11-06T06:34:07Z | 2026-11-08T21:05:00Z |
| underdog|cc6e5df1-5a0b-4ad2-972e-574952cbd39c | underdog | Tez Johnson | Receptions | over | 0.050436099256353284 | 2026-11-05T22:06:44Z | 2026-11-09T01:20:00Z |
| underdog|6a30bff5-d45d-45f9-a712-6c98fba34405 | underdog | Lloyd Avant | Rush Yards | over | 0.05041483365885191 | 2026-11-05T12:22:13Z | 2026-11-08T00:45:00Z |
| underdog|306d32c9-76be-44a5-b65c-2d983b4ebc2f | underdog | Ashton Jeanty | Rush + Rec Yards | under | 0.05021547727948117 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| prizepicks|16719165 | prizepicks | Tre' Harris | Rec Targets | under | 0.050059523885883084 | 2026-11-05T22:06:44Z | 2026-11-08T16:05:00.000-05:00 |
| prizepicks|16718528 | prizepicks | Harold Fannin Jr. | Rec Targets | under | 0.05005687630552147 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|97875f93-6930-4cda-9c97-1ad33e8d4022 | underdog | Harold Fannin | Receiving Yards | under | 0.04999003573194083 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|ff3f65e5-9fbe-4b2a-b0f2-9abc59d7b211 | underdog | Kendre Miller | Receptions | over | 0.04992471595146514 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|fc8c7bdd-6f0b-4802-8874-c12236925669 | underdog | Jaylen Raynor | Pass Yards | under | 0.04980050697892513 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|da32429e-2136-492e-ade0-808946db1392 | underdog | Dalton Kincaid | Receiving Yards | under | 0.049312018647535094 | 2026-11-05T12:22:13Z | 2026-11-10T01:15:00Z |
| underdog|807c529e-31ff-4c65-9ac7-c60639f1a1f4 | underdog | Jayden Daniels | Rush Yards | under | 0.049059514309005126 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|ed56e197-54b7-4d14-9254-cc19f9dfbd99 | underdog | Yannick Smith | Receiving Yards | under | 0.04899083677379246 | 2026-11-04T12:10:41Z | 2026-11-07T00:00:00Z |
| prizepicks|16577037 | prizepicks | Chris Olave | Rec Yards | under | 0.04898251964490763 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|22050342-7a21-4957-b097-7d3e03600849 | underdog | Omar Cooper | Receiving Yards | under | 0.048708537557002884 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| underdog|f846cfba-c825-4e6b-aac9-0975e8c6604a | underdog | Kayshon Boutte | Receptions | over | 0.04870573326693556 | 2026-11-05T12:22:13Z | 2026-11-08T21:05:00Z |
| prizepicks|16687773 | prizepicks | Aidan Chiles | Pass Attempts | under | 0.04858649581932972 | 2026-11-05T12:22:13Z | 2026-11-07T19:30:00.000-05:00 |
| underdog|6b69088c-d4a8-4159-bbd0-3e2170aae7d7 | underdog | Brad Jackson | Pass TDs | under | 0.048348152610976136 | 2026-11-05T12:22:13Z | 2026-11-08T03:30:00Z |
| prizepicks|16718496 | prizepicks | Dalton Kincaid | Rec Targets | under | 0.04809003370519738 | 2026-11-05T22:06:44Z | 2026-11-09T20:15:00.000-05:00 |
| underdog|1b0eb045-4271-4dec-a604-a4c38773225d | underdog | Aidan Birr | XP Made | over | 0.048078044601977676 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| prizepicks|16718501 | prizepicks | James Cook III | Rec Targets | under | 0.04803584807788108 | 2026-11-05T22:06:44Z | 2026-11-09T20:15:00.000-05:00 |
| underdog|c4be67dc-c7c4-48f2-9278-1cc9a6e5fc5f | underdog | Jacobo Echeverria Lozano | XP Made | under | 0.04797316880475955 | 2026-11-05T22:06:44Z | 2026-11-07T17:30:00Z |
| prizepicks|16718533 | prizepicks | Ryan Flournoy | Rec Targets | under | 0.04782445339134278 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|b8fec16e-e184-416c-9fab-8a457d0f893f | underdog | Cayden Lee | Receiving Yards | under | 0.047650204243950056 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|1441af20-ca44-43f2-b7f8-3dc65dac1fb6 | underdog | Jadan Baugh | Rush Yards | under | 0.047469000409556705 | 2026-11-05T12:22:13Z | 2026-11-08T00:45:00Z |
| underdog|0729c05e-e380-4efb-b2ae-e1403174fb84 | underdog | Samaje Perine | Receptions | over | 0.04737537544984716 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| prizepicks|16567035 | prizepicks | Jordan Love | Pass TDs | under | 0.04710112679060341 | 2026-11-04T12:10:41Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|8d98abf4-bc5e-4549-90db-f4eca6824ba0 | underdog | Bucky Irving | Rush + Rec Yards | under | 0.04692066418821539 | 2026-11-05T12:22:13Z | 2026-11-09T01:20:00Z |
| underdog|85850fda-bdb6-4970-9de6-4c327b723dbd | underdog | Torrance Burgess | Receptions | under | 0.04685698559541274 | 2026-11-05T12:22:13Z | 2026-11-08T03:30:00Z |
| underdog|e5156db0-79be-42ba-8302-5fcd0cfd7d61 | underdog | Ethan Moczulski | XP Made | over | 0.046690949261277925 | 2026-11-04T12:10:41Z | 2026-11-07T01:00:00Z |
| underdog|79efae80-1726-417d-9fba-673881fec86c | underdog | Kyler Kasper | Receiving Yards | under | 0.046656667808123276 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|0139142a-48ff-4686-a88c-d6871199a540 | underdog | Trey'Dez Green | Receiving Yards | under | 0.046595703298682234 | 2026-11-05T22:06:44Z | 2026-11-07T20:30:00Z |
| underdog|8ac17bbc-0479-482d-b6ca-4651a3b3a2f0 | underdog | Drew Stevens | Kicking Points | under | 0.04644611027329182 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|40da3ee9-17d9-44f6-984c-7575298a9713 | underdog | Michael Hawkins | Rush Yards | under | 0.04627747558472772 | 2026-11-05T12:22:13Z | 2026-11-08T02:30:00Z |
| prizepicks|16719177 | prizepicks | Alvin Kamara | Rec Targets | under | 0.04592092233766798 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|6840c1d4-0dc2-48d1-9e3d-699321becaf1 | underdog | LaNorris Sellers | Pass TDs | under | 0.04584495188446647 | 2026-11-05T22:06:44Z | 2026-11-07T20:00:00Z |
| underdog|9a3d5951-42b0-4cdc-9a0d-f3d820453d9b | underdog | Mike Matthews | Receiving Yards | under | 0.045793510434076534 | 2026-11-05T12:22:13Z | 2026-11-07T23:15:00Z |
| underdog|e4023e77-9713-4947-a229-d8d0c01daa5c | underdog | Jojo Phillips | Receiving Yards | over | 0.04551214414039517 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|f4c06e1a-224a-4c62-b703-ec0468d2809a | underdog | Ty Dieffenbach | Pass Yards | under | 0.04550553825367998 | 2026-11-05T22:06:44Z | 2026-11-07T17:00:00Z |
| prizepicks|16722941 | prizepicks | Emeka Egbuka | Recs | under | 0.04538182348359732 | 2026-11-06T06:34:07Z | 2026-11-08T20:20:00.000-05:00 |
| underdog|ee7283f4-fd73-422d-bd13-d29f537b4bbd | underdog | Griffin Wilde | Receiving Yards | under | 0.04521349801132524 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|4de62797-41a0-4d69-977b-0286517b1b34 | underdog | Alvin Kamara | Receptions | under | 0.0452076759340746 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|7a72d0be-60ae-4376-8aa1-07e785aab859 | underdog | Jonathan Taylor | Receptions | under | 0.04508721237534341 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|0f9959d0-f9a2-474d-82e2-77981b9f03c0 | underdog | J.K. Dobbins | Rush + Rec Yards | under | 0.04497859513044955 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| underdog|64b35a78-7c9c-4a69-ab32-52beb9943671 | underdog | Kenny Johnson | Receiving Yards | under | 0.04474185000019171 | 2026-11-05T22:06:44Z | 2026-11-08T02:30:00Z |
| underdog|51e7af2b-f9a1-43ea-aa78-584f372553e2 | underdog | Trey Smack | Kicking Points | under | 0.04455434973971151 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|ea125837-d29b-4284-a90d-fee5aa2a9a96 | underdog | Chris Godwin | Receptions | under | 0.04434472697680247 | 2026-11-05T12:22:13Z | 2026-11-09T01:20:00Z |
| underdog|e5d081ab-9efa-43d3-bfb8-a43e2d593f85 | underdog | Drake Maye | Pass TDs | under | 0.04430737897190651 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|f30dd4e7-dacd-455c-8ed4-95be1fa5e74c | underdog | Karolina Muchova | Double Faults | under | 0.044153512874079426 | 2026-11-05T12:22:13Z | 2026-11-09T20:00:00Z |
| underdog|997e67da-c8d3-4a83-9610-e8d3e6b73ebb | underdog | Caleb Odom | Receiving Yards | over | 0.0440665088048563 | 2026-11-04T12:10:41Z | 2026-11-08T00:30:00Z |
| underdog|fa268a96-c011-4c35-9f2c-71018831b22d | underdog | Chase Brown | Receiving Yards | under | 0.044036182985406125 | 2026-11-05T12:22:13Z | 2026-11-08T14:30:00Z |
| prizepicks|16718543 | prizepicks | Jameson Williams | Rec Targets | under | 0.04401078613436993 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|5e087ca0-c81b-466a-a4ab-b25feaca7f84 | underdog | Noah Bennee | Receiving Yards | over | 0.04389551607024966 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|9815d49d-2af1-48c2-b6e4-cbe7c87349ac | underdog | Emmett Johnson | Receiving Yards | over | 0.043799798929959555 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|7da11b8f-5399-4a1b-be01-2cbe1a58ddeb | underdog | Malachi Fields | Receiving Yards | under | 0.04372469851815042 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|386a24ab-997f-4524-98d3-c932af517a2a | underdog | Rocky Beers | Receiving Yards | over | 0.04368039628251896 | 2026-11-05T22:06:44Z | 2026-11-08T00:45:00Z |
| underdog|d6a57db5-49c6-43d4-997b-75c80e636d09 | underdog | Jayden Limar | Rush Yards | under | 0.043609864830960965 | 2026-11-05T22:06:44Z | 2026-11-07T20:30:00Z |
| underdog|2008fc2d-4b3f-4d3b-b372-948ea75bf0ff | underdog | AJ Newberry | Receptions | under | 0.04358383404136057 | 2026-11-06T06:34:07Z | 2026-11-08T03:30:00Z |
| underdog|ad635a6c-9e35-4040-a33e-b3858910cc27 | underdog | Collin Dixon | Receptions | under | 0.04349628521930127 | 2026-11-05T22:06:44Z | 2026-11-07T01:00:00Z |
| underdog|9f8d5a76-cbb3-4565-b2d4-601b302e1c66 | underdog | Jojo Phillips | Receptions | over | 0.04343832039629403 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|c2e9acd7-4e88-4f30-ae76-a25816dd4141 | underdog | Ricky Johnson | Receiving Yards | over | 0.043306631735705814 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|1075e7a4-7835-48a5-a2db-a78bbb0c36aa | underdog | Kalif Raymond | Receiving Yards | over | 0.04323294702184943 | 2026-11-05T12:22:13Z | 2026-11-09T01:20:00Z |
| prizepicks|16557917 | prizepicks | Jordan Love | Rush Yards | under | 0.0431179313386405 | 2026-11-03T02:21:46Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|fe7a85f2-c21c-4535-88b9-b246e6af4d70 | underdog | Jason Sanders | FG Made | over | 0.04309576984353114 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|69d33979-906e-439f-b526-f612ed22aaaa | underdog | Gavin Lahm | FG Made | under | 0.04308668218923806 | 2026-11-05T12:22:13Z | 2026-11-07T21:15:00Z |
| underdog|7461ed14-7d77-45bb-9a57-07a5b4a25c13 | underdog | Wayshawn Parker | Receptions | over | 0.04308151190165166 | 2026-11-06T06:34:07Z | 2026-11-07T17:00:00Z |
| underdog|ef68a74d-d7a0-476d-bf6c-f7f526abd93c | underdog | Tyler Shough | Rush Yards | under | 0.042790287547065375 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|91f4a8ca-8e1b-4038-a81f-33103051637f | underdog | Darnell Mooney | Receptions | over | 0.04273058695676135 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|a5088759-dcc4-4d0c-acb8-516ddb05b069 | underdog | Noah Fant | Receptions | over | 0.04270940205899032 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|7cb3fbf6-c9e4-47ff-8fdc-7ad015eff5a9 | underdog | Kenneth Walker III | Receiving Yards | under | 0.042196979680496294 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| prizepicks|16729642 | prizepicks | Bianca Andreescu | Total Games | over | 0.042047604343236844 | 2026-11-06T06:34:07Z | 2026-11-06T13:30:00.000-05:00 |
| underdog|06609665-f084-4b1b-affa-8cc4f9a90e0b | underdog | Omari Hayes | Receptions | over | 0.041906589246400505 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|085c90df-5803-45fc-ac14-b28618abec44 | underdog | Aaron Jones | Receiving Yards | over | 0.04183150381663703 | 2026-11-05T22:06:44Z | 2026-11-10T01:15:00Z |
| underdog|25efe389-0f9d-4419-983d-72da4b9d01ba | underdog | Cyrus Allen | Receptions | under | 0.041551213577819546 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|306be0c1-9650-4027-8391-6aeca88bcf4d | underdog | Lotzeir Brooks | Receptions | over | 0.04144434396768071 | 2026-11-05T12:22:13Z | 2026-11-07T20:30:00Z |
| underdog|0c69b287-a405-436f-ac40-7401e48709ea | underdog | Tramell Jones | Pass TDs | under | 0.04138598652817316 | 2026-11-05T22:06:44Z | 2026-11-08T00:45:00Z |
| prizepicks|16667335 | prizepicks | Puka Nacua | Recs | under | 0.04136046632707657 | 2026-11-05T12:22:13Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|127ded5d-257a-4c2a-bb25-88e0bd0debad | underdog | Jordan Love | Rush Yards | under | 0.04127202084950954 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|8154216f-d782-4c05-b8db-e78e6c5ae26f | underdog | Jerry Jeudy | Receiving Yards | under | 0.04125837265686039 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|6af1f579-11d3-4d3e-a5c5-36d75a14e37a | underdog | Bo Jackson | Receiving Yards | over | 0.04104279325152682 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| prizepicks|16718546 | prizepicks | Matthew Golden | Rec Targets | under | 0.04103027600826581 | 2026-11-05T22:06:44Z | 2026-11-08T16:25:00.000-05:00 |
| prizepicks|16701852 | prizepicks | Antwan Raymond | Rush Atts | under | 0.040920919788068 | 2026-11-05T12:22:13Z | 2026-11-07T16:15:00.000-05:00 |
| underdog|7adbec65-2635-4418-bf09-ab9e23b46b18 | underdog | CJ Bailey | Rush Yards | over | 0.04084183957976073 | 2026-11-05T22:06:44Z | 2026-11-07T17:30:00Z |
| underdog|d63b8166-7ed3-4784-a290-53c755df307b | underdog | Rhamondre Stevenson | Receiving Yards | under | 0.04073261149509677 | 2026-11-06T06:34:07Z | 2026-11-08T21:25:00Z |
| underdog|b4fcd29b-0159-45f7-bd83-8bb9de66f917 | underdog | Ted Hurst | Receiving Yards | over | 0.04068354371181715 | 2026-11-05T22:06:44Z | 2026-11-09T01:20:00Z |
| underdog|37ad3b9b-b644-4db3-95fd-a6dda1efec53 | underdog | Marshall Pritchett | Receptions | over | 0.04061687669708042 | 2026-11-05T12:22:13Z | 2026-11-07T20:30:00Z |
| underdog|67ecfc13-7baa-495f-be1d-d0ec1521310e | underdog | Zechariah Sample | Receiving Yards | over | 0.040524746237519005 | 2026-11-05T12:22:13Z | 2026-11-08T03:30:00Z |
| underdog|bcc3366d-03c4-4686-b8c4-9911098d7a7d | underdog | Jaylen Raynor | Rush Yards | over | 0.040483745848692076 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| prizepicks|16577047 | prizepicks | Ryan Flournoy | Rec Yards | under | 0.04046234355837319 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|c4eff874-a6ec-42ee-89c1-4143adf59be3 | underdog | Jamal Roberts | Receptions | under | 0.04041960521612786 | 2026-11-05T22:06:44Z | 2026-11-07T17:00:00Z |
| prizepicks|16721632 | prizepicks | Tommy Paul | Break Points Won | over | 0.040369610348702234 | 2026-11-05T22:06:44Z | 2026-11-06T08:00:00.000-05:00 |
| underdog|19911946-1f92-42a4-aa1c-15e5815fb816 | underdog | Tee Higgins | Receptions | under | 0.04018031305357561 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| prizepicks|16670099 | prizepicks | Anthony Colandrea | Rush Atts | under | 0.040074430799448724 | 2026-11-05T12:22:13Z | 2026-11-06T20:00:00.000-05:00 |
| underdog|106bc837-0742-4a70-8024-e1818eafcf7d | underdog | Kari Ashley | Receiving Yards | over | 0.04002793372455549 | 2026-11-05T22:06:44Z | 2026-11-07T03:15:00Z |
| underdog|3bd01e57-9195-4088-a564-fe508f2d81f0 | underdog | Isaiah Likely | Receptions | under | 0.039903034181366426 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|7a5a7c7a-46d9-4665-9112-650361479cc3 | underdog | Dalen Penson | Receiving Yards | under | 0.039666610643468436 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|51793da7-f50f-4605-9f8b-5f37ddfbd171 | underdog | Jamari Johnson | Receptions | under | 0.039549403867083055 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|b510b6c8-aa64-436f-a890-a3ad7f41278d | underdog | Keelon Russell | Rush Yards | over | 0.03954798492547018 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| prizepicks|16577038 | prizepicks | Travis Kelce | Rec Yards | under | 0.039492224251563846 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|4d2d8848-1cc7-4afb-b184-d2ce33f20639 | underdog | Kaleb Webb | Receiving Yards | under | 0.03917272336846056 | 2026-11-05T22:06:44Z | 2026-11-07T17:30:00Z |
| underdog|cefb0596-2c7e-431b-8408-7a1ed12d8db4 | underdog | Bryce Young | Pass TDs | under | 0.039094010660283285 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|b928a5ef-308e-4395-97c3-f7cbc952337a | underdog | Ayden Greene | Receiving Yards | over | 0.038935127218449606 | 2026-11-04T12:10:41Z | 2026-11-07T00:00:00Z |
| underdog|7ec6b8e6-f4bc-4ceb-9977-2343e6cf733c | underdog | Patrick Overmyer | Receiving Yards | under | 0.03891506317250926 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| prizepicks|16718511 | prizepicks | Jalen Coker | Rec Targets | under | 0.03878118544429088 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|d1d3e66e-276b-43d4-9e06-fe5ed3964b6c | underdog | Geno Smith | Pass TDs | over | 0.038346590420210214 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| prizepicks|16718513 | prizepicks | Tommy Tremble | Rec Targets | under | 0.038026067477504255 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|30207658-d186-4c70-8ce0-0f79ac92f94f | underdog | Trae'shawn Brown | Rush Yards | over | 0.037999199829431785 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|24135e0b-bdb0-493a-8b08-4ef9d8baaddd | underdog | Omarion Hampton | Receiving Yards | over | 0.0379426659535288 | 2026-11-05T22:06:44Z | 2026-11-08T21:05:00Z |
| prizepicks|16719172 | prizepicks | Ollie Gordon II | Rec Targets | under | 0.03764949184168209 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|c9385892-f356-4349-8fb6-7d5113bc5518 | underdog | Kimani Vidal | Rush Yards | under | 0.037649407143210745 | 2026-11-05T22:06:44Z | 2026-11-08T21:05:00Z |
| underdog|b6818540-727b-4e7c-bc3e-a1e823ca4bed | underdog | Landon Sides | Receiving Yards | under | 0.03764821401781726 | 2026-11-05T22:06:44Z | 2026-11-07T00:30:00Z |
| underdog|ed498511-b16f-46d2-bc03-e9dd42b5220b | underdog | Ahmad Miller | Rush Yards | under | 0.037559554816855245 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|10c2407f-5738-4e43-8822-e60a7494336d | underdog | Devaughn Vele | Receiving Yards | under | 0.03754483168355782 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| underdog|4a60e445-01a6-4494-af71-30be934f5ff2 | underdog | Jalen Royals | Receptions | over | 0.03740054606007237 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|1997f55a-78b3-4c4c-909c-a6a479005d46 | underdog | Eric Olsen | Receiving Yards | under | 0.0372510438778374 | 2026-11-05T12:22:13Z | 2026-11-08T03:30:00Z |
| underdog|36c54cdf-d1a5-4421-add6-c8c475dc2cbb | underdog | Linda Noskova | Double Faults | under | 0.037236525846527924 | 2026-11-05T12:22:13Z | 2026-11-08T20:00:00Z |
| prizepicks|16718503 | prizepicks | Keon Coleman | Rec Targets | under | 0.037191314735347314 | 2026-11-05T22:06:44Z | 2026-11-09T20:15:00.000-05:00 |
| underdog|fae9f83c-94b0-42c3-b5e4-38e0ba845826 | underdog | Coco Gauff | Double Faults | under | 0.03701305154789125 | 2026-11-05T12:22:13Z | 2026-11-08T21:10:00Z |
| underdog|2f401558-103b-44dd-b0ae-941e6998fc51 | underdog | Wayne Knight | Rush Yards | under | 0.03693588139563031 | 2026-11-04T12:10:41Z | 2026-11-07T17:00:00Z |
| underdog|f7590ee7-e756-4a52-ba98-6e7f95977886 | underdog | Tez Johnson | Receiving Yards | over | 0.03686868794151077 | 2026-11-05T22:06:44Z | 2026-11-09T01:20:00Z |
| underdog|3e8e39eb-d463-45bc-a696-888d37fa2c28 | underdog | Tyler Robles | XP Made | over | 0.03669915689642389 | 2026-11-05T22:06:44Z | 2026-11-07T20:30:00Z |
| underdog|6c714eaf-7d73-41a2-a920-202ca837066f | underdog | Corey Kiner | Rush Yards | under | 0.036586404611637424 | 2026-11-06T06:34:07Z | 2026-11-08T21:25:00Z |
| underdog|4bd88e72-8a1e-4707-b805-02d3c1b83426 | underdog | Chrishon McCray | Receptions | over | 0.03644387034168628 | 2026-11-06T06:34:07Z | 2026-11-08T00:30:00Z |
| underdog|0a022c63-2671-4f23-9feb-269bf1714179 | underdog | Mario Craver | Receptions | over | 0.03644227791425586 | 2026-11-05T22:06:44Z | 2026-11-07T20:00:00Z |
| underdog|93cdf1c0-b682-44c5-91cb-5bb24ea6f0a8 | underdog | Jordan Dwyer | Receptions | under | 0.03597740333053934 | 2026-11-05T22:06:44Z | 2026-11-07T03:15:00Z |
| underdog|119f4d77-645c-42cd-9e5d-3c3aa99ea03d | underdog | Cameron Dicker | FG Made | under | 0.03597583144986216 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|865227cf-17df-4e89-9c98-4311b47f982a | underdog | Tetairoa McMillan | Receptions | under | 0.03583202783628714 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| prizepicks|16576405 | prizepicks | Puka Nacua | Rush Yards | over | 0.035802440511908284 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|63535c0e-f25f-4020-b229-60487df1cb5e | underdog | Kenny Darby | Receptions | over | 0.035572200850898905 | 2026-11-05T12:22:13Z | 2026-11-07T23:15:00Z |
| underdog|f77c4659-c571-4380-bb17-0f290c20cfdb | underdog | Braden Pegan | Receiving Yards | under | 0.03535065146715288 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|0e852f18-35a2-4c1c-873c-20e33540cb73 | underdog | Mario Craver | Receiving Yards | under | 0.035278791718292735 | 2026-11-05T22:06:44Z | 2026-11-07T20:00:00Z |
| underdog|2f083c55-dfe0-4021-bc6a-5e7f16540cf5 | underdog | Ryan Fitzgerald | FG Made | under | 0.035264256773103186 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|8d80495b-f792-49a4-9e27-200df0bf6a4a | underdog | Alonza Barnett | Pass TDs | under | 0.03520294894563547 | 2026-11-05T22:06:44Z | 2026-11-07T20:45:00Z |
| underdog|ace9e75f-3fab-448d-a35d-0f1676382ace | underdog | Daniel Jones | Rush Yards | over | 0.03511058164603342 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|76b2a70a-293f-40f9-a916-eb743ce0a710 | underdog | Omari Hayes | Receiving Yards | over | 0.035032468841684095 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|d956ff35-5891-430d-a052-ebaf442bf737 | underdog | Spencer Shrader | Kicking Points | under | 0.03493687122664446 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|2a6fac37-d0cb-4800-b741-f75709238aac | underdog | DJ Black | Receiving Yards | over | 0.03489153401663336 | 2026-11-05T22:06:44Z | 2026-11-07T20:00:00Z |
| prizepicks|16722414 | prizepicks | Taylor Fritz | Total Games Won | over | 0.0347523897003702 | 2026-11-06T06:34:07Z | 2026-11-06T13:00:00.000-05:00 |
| underdog|e766e342-b4d6-46d8-ba50-79465996cad2 | underdog | JJ Buchanan | Receiving Yards | under | 0.03474313249081806 | 2026-11-05T22:06:44Z | 2026-11-08T00:30:00Z |
| underdog|642b6aa4-d8ad-47ca-a6e2-02bf1db1abde | underdog | Rhamondre Stevenson | Receptions | under | 0.03473410197552751 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| prizepicks|16557908 | prizepicks | Patrick Mahomes | Rush Yards | under | 0.034534369510793694 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|2e86c763-78d4-470d-ac21-5be7449f9ade | underdog | Mazeo Bennett | Receiving Yards | under | 0.0344095937486365 | 2026-11-05T22:06:44Z | 2026-11-07T20:00:00Z |
| underdog|ad6f21f6-79ae-4c5d-a258-6ddedefe83f6 | underdog | Ka'imi Fairbairn | Kicking Points | under | 0.03438415374739645 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|488c064e-4a42-4665-a6fc-407585fb9afe | underdog | Lawson Luckie | Receiving Yards | over | 0.03431423503130593 | 2026-11-04T12:10:41Z | 2026-11-08T00:30:00Z |
| underdog|66b37aff-aa69-48ba-984e-2a3c3e131cd4 | underdog | Tommy Tremble | Receptions | over | 0.03430222685481554 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|d07411a2-861f-46d8-9b37-7f958305aba8 | underdog | Miles Coleman | Receiving Yards | over | 0.03415913777769475 | 2026-11-05T12:22:13Z | 2026-11-07T18:00:00Z |
| underdog|2633c44b-2778-4c40-80af-982da493b8f5 | underdog | Landon Sides | Receptions | under | 0.034111869325997746 | 2026-11-05T22:06:44Z | 2026-11-07T00:30:00Z |
| underdog|a7cebf17-ff00-4409-a5bc-8ce129dd77a1 | underdog | Quinshon Judkins | Receptions | under | 0.03394034349269137 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|b4164f31-211e-44a6-819f-02c4a0dae617 | underdog | Xavier Worthy | Receptions | under | 0.033937644307545756 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|163463eb-db49-4cf6-bfaf-3c9e13571bb6 | underdog | Dylan Sampson | Rush + Rec Yards | under | 0.033767533205674494 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| underdog|d61c807a-66b1-4a4f-9972-cba41bc45ee6 | underdog | Javonte Williams | Receiving Yards | over | 0.03365125001838698 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|c326b335-e702-421f-9f11-eec8ab8fdfaa | underdog | Dalton Schultz | Receiving Yards | under | 0.03359570617331076 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|27088af6-5b7d-4152-b246-6ea59730b4c5 | underdog | Davian Jackson | Rush Yards | over | 0.0334712784456449 | 2026-11-05T12:22:13Z | 2026-11-08T03:30:00Z |
| underdog|d0e1ebf4-acf9-49c2-b302-9afd0130cb50 | underdog | Brian Robinson | Rush Yards | under | 0.03332487637927317 | 2026-11-05T22:06:44Z | 2026-11-08T14:30:00Z |
| underdog|c4b7c726-6ba5-4b7b-a3f2-640e9d52771a | underdog | Samaje Perine | Rush + Rec Yards | under | 0.03322821780525986 | 2026-11-05T12:22:13Z | 2026-11-08T14:30:00Z |
| underdog|fe1331bb-39d1-4681-8d5a-f9d951e31392 | underdog | KC Concepcion | Receptions | under | 0.033021846340560934 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|43d4f051-ed64-4b5e-904b-24f2c6efea26 | underdog | Samaje Perine | Rush Yards | under | 0.03301262915252379 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|a2d14611-eeff-4586-80bd-d349331a9d9f | underdog | Blake Barnett | Pass TDs | under | 0.03293401410353347 | 2026-11-05T12:22:13Z | 2026-11-07T18:00:00Z |
| underdog|dd38b9d2-b29f-4f0c-a098-a272047c146d | underdog | Michael Mayer | Receiving Yards | under | 0.032893313880521746 | 2026-11-05T22:06:44Z | 2026-11-08T21:25:00Z |
| underdog|8a29eea1-d895-407b-8658-b0db6edb5801 | underdog | Nate Adkins | Receptions | over | 0.03282306378556943 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|a5fbd6d5-3e62-4a23-883d-9f5cf14d5654 | underdog | Shekai Mills-Knight | Rush Yards | under | 0.0327826010465021 | 2026-11-04T12:10:41Z | 2026-11-08T00:30:00Z |
| underdog|e6b1bd36-4a4b-44b3-8d57-b0ffc66e6084 | underdog | Jake Weinberg | FG Made | under | 0.032781270811728436 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|2fdcf276-eb1c-48b0-99cd-8ca8a12bd9f6 | underdog | Wyatt Young | Receiving Yards | under | 0.03277323062096282 | 2026-11-05T12:22:13Z | 2026-11-07T18:00:00Z |
| underdog|b9c1a1a8-01ac-40a2-baab-d2706b32bde2 | underdog | Kyren Williams | Receptions | under | 0.032587481000593055 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|cb747884-9dfd-4e72-bb6f-c8093300338d | underdog | Spencer Porath | XP Made | under | 0.03248900119255549 | 2026-11-06T06:34:07Z | 2026-11-08T00:30:00Z |
| prizepicks|16719169 | prizepicks | Chris Bell | Rec Targets | under | 0.032460366105138805 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|041b30d5-fdc3-4489-bb29-a89e6667b68d | underdog | Charlie Kolar | Receiving Yards | under | 0.03242651143957387 | 2026-11-05T12:22:13Z | 2026-11-08T21:05:00Z |
| underdog|b396969a-1df9-4211-a0ab-b055cda96fd1 | underdog | Ashton Daniels | Pass TDs | over | 0.03222984779982624 | 2026-11-05T22:06:44Z | 2026-11-07T17:00:00Z |
| underdog|2cfb2c38-eea2-4115-8859-b21897508d6e | underdog | Michael Mayer | Receptions | under | 0.03208971752720258 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|cc8591f7-05de-4f55-87ee-18c509911539 | underdog | Troy Franklin | Receiving Yards | under | 0.03204712122097875 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|d703eccc-f6a7-4718-81f1-d643a93e6e55 | underdog | Dawson Pough | Receiving Yards | over | 0.031808546432040785 | 2026-11-06T06:34:07Z | 2026-11-07T17:00:00Z |
| underdog|29834b95-ffb3-48a3-8130-df8f76762419 | underdog | Peyton Woodring | FG Made | over | 0.03151348868814757 | 2026-11-04T12:10:41Z | 2026-11-08T00:30:00Z |
| underdog|9d179035-df06-49bf-a90b-e1c8c7831fff | underdog | Omar Mabson | Rush Yards | under | 0.03137483548799547 | 2026-11-06T06:34:07Z | 2026-11-07T17:45:00Z |
| underdog|28e88963-6ce3-4dfb-ad09-da506039d8c8 | underdog | Cole Spence | Receptions | over | 0.030828022750417128 | 2026-11-05T22:06:44Z | 2026-11-07T21:15:00Z |
| underdog|ec21afa7-ad82-4b47-954d-22041573aade | underdog | Raleek Brown | Receptions | over | 0.030773355877860176 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|3005b6a0-46ad-4a80-8375-b890de97dd55 | underdog | AJ Newberry | Receiving Yards | over | 0.030590482240790196 | 2026-11-05T12:22:13Z | 2026-11-08T03:30:00Z |
| underdog|9cc0a4d7-680c-4eec-9408-bd7d2f7270f8 | underdog | Andrew Marsh | Receptions | over | 0.03051906600607368 | 2026-11-05T22:06:44Z | 2026-11-08T00:30:00Z |
| underdog|f7062588-3eb0-4f0e-b3fb-0c5e028853bd | underdog | Juwan Johnson | Receptions | over | 0.030368013536360206 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|9bd8c698-9241-4468-a7b5-e37b14252e48 | underdog | Reece Vander Zee | Receptions | under | 0.030171557685573003 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|f1715ec8-5f20-46c7-ba87-5af729c439a0 | underdog | Cam Cook | Rush Yards | under | 0.03009783990413606 | 2026-11-05T12:22:13Z | 2026-11-08T02:30:00Z |
| underdog|161f9cb0-fb2d-4022-8e16-4b0bf4bdcf05 | underdog | Wayshawn Parker | Rush Yards | under | 0.03005398542967841 | 2026-11-06T06:34:07Z | 2026-11-07T17:00:00Z |
