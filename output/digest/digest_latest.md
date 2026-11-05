# Pipeline Digest -- 2026-11-05T12:12:40Z

## Run summary
- Ingestion: 37232 rows (PrizePicks OK, Underdog OK)
- Estimation: 37232 rows estimated (from 37232 ingested props)
- CLV logging: 421 newly flagged, 0 newly closed, 767 still open (108608 total ever logged)

## Currently open flags
Sizing is a manual step (sizing_engine.py, Session 2.6) -- this table is what to scan to pick a pair worth sizing.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_edge | first_flagged_at | game_start_time |
|---|---|---|---|---|---|---|---|
| underdog|7984c1b8-4987-4395-9955-ab4b9006dd75 | underdog | Eddy Pineiro | FG Made | under | 0.41306807406928026 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|afba29c5-f2e4-45ae-964a-5e63268558cf | underdog | Trevor Lawrence | Pass Yards | under | 0.4 | 2026-11-05T12:22:13Z | 2026-11-06T01:15:00Z |
| underdog|3fb4f5c1-99aa-4469-8c43-2255a6229eca | underdog | Caleb Williams | Pass Yards | under | 0.4 | 2026-11-05T12:22:13Z | 2026-11-09T01:20:00Z |
| underdog|339df7bd-03f5-482d-ab9a-8634b6201c7e | underdog | Drew Lock | Pass Yards | under | 0.4 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|f8712edc-1b94-4a23-93b0-f3a909f7347a | underdog | Drew Lock | Pass Attempts | under | 0.4 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|102268c4-9750-440c-bdea-6fdb3af216a7 | underdog | Brock Purdy | Pass Yards | under | 0.4 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|3e831f69-cf67-408d-9148-2f2a2205f140 | underdog | Brandon McManus | Kicking Points | under | 0.4 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|72f89744-f92a-449b-a0bb-cf8069d05cd8 | underdog | Jack Larsen | Receiving Yards | over | 0.4 | 2026-11-03T02:21:46Z | 2026-11-08T00:30:00Z |
| underdog|23ade03d-dd8f-4bf4-9862-4c89e14da2ef | underdog | Jack Bech | Receiving Yards | under | 0.4 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|159c0350-eab4-41f1-b826-0de1e1e3b5bd | underdog | Justin Herbert | Pass Yards | under | 0.4 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|4a863902-d11a-4d1a-87cb-b706ca003cb8 | underdog | Josh Jacobs | Rush Yards | under | 0.4 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|268d2fc5-2abe-4849-b4a0-390d7485e453 | underdog | Caleb Williams | Pass Attempts | under | 0.4 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|c86fa511-af54-455c-8d40-3f535e58651a | underdog | Dak Prescott | Pass Yards | under | 0.4 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|d71953b3-f84a-41de-8164-f5fbcaae145d | underdog | Malik Willis | Pass Yards | under | 0.4 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|869349aa-5399-4c3f-b961-edd9aca6684e | underdog | Michael Penix | Pass Yards | under | 0.4 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|754ec181-3723-4eeb-9d81-6ac2f38d4b05 | underdog | Josh Allen | Pass Yards | under | 0.4 | 2026-11-04T12:10:41Z | 2026-11-10T01:15:00Z |
| underdog|88a67ef6-decb-440a-98f8-fb4b22c34d26 | underdog | Brandon McManus | FG Made | under | 0.3956303597430939 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|87dc86a8-1b6c-4fe8-9e0a-55c0dda258af | underdog | Stefon Diggs | Receiving Yards | under | 0.39541758268765004 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|a31d98a6-bf53-440e-a5b5-a2b50e20038d | underdog | Bo Nix | Pass Yards | under | 0.39297059903848375 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|3457fac4-96e9-46e5-a38e-f8575853e01c | underdog | Jayden Daniels | Pass Yards | under | 0.3893084725552035 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|29356dc8-01cb-4b38-a414-1571c2ae47db | underdog | Baker Mayfield | Pass Yards | under | 0.386000173495637 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|91257feb-8a6e-4897-a344-a682b8f407f8 | underdog | Justin Herbert | Pass Attempts | under | 0.382571560879172 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|b8d21dd7-97bf-498f-bf28-1b8190ab101b | underdog | Kyler Murray | Pass Yards | under | 0.3779532546313993 | 2026-11-04T12:10:41Z | 2026-11-10T01:15:00Z |
| underdog|705e8042-bbe1-42e5-a50a-844d254c8900 | underdog | Kirk Cousins | Pass Yards | under | 0.3761461839014639 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|6b226ab0-139b-4d9d-b539-7e92052bef30 | underdog | Daniel Jones | Pass Yards | under | 0.37242865327478003 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|7eedc362-5891-4451-820d-93536c2bee6e | underdog | Dawson Knox | Receiving Yards | under | 0.3666926454678271 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|f9976ec1-4523-4b7a-bd0c-bca9b9dd4fb5 | underdog | Eddy Pineiro | Kicking Points | under | 0.3662333132187251 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|927a0917-e0d0-4e12-ad02-7bc4c72c9b98 | underdog | DeSean Bishop | Receiving Yards | over | 0.3546355960210914 | 2026-11-05T12:22:13Z | 2026-11-07T23:15:00Z |
| underdog|20ded54a-d3d9-4991-b45f-4aab1465f143 | underdog | Jordan Love | Pass Yards | under | 0.35357762783010915 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| prizepicks|16577043 | prizepicks | Stefon Diggs | Rec Yards | under | 0.35094246505677495 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| prizepicks|16557936 | prizepicks | Dak Prescott | Pass Yards | under | 0.35094246505677495 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| prizepicks|16557944 | prizepicks | Josh Allen | Pass Yards | under | 0.35094246505677495 | 2026-11-03T02:21:46Z | 2026-11-09T20:15:00.000-05:00 |
| prizepicks|16557940 | prizepicks | Brock Purdy | Pass Yards | under | 0.35094246505677495 | 2026-11-03T02:21:46Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|76903731-5a31-4b71-aa02-3cf5f1f66632 | underdog | Jared Goff | Pass Yards | under | 0.34472431347503396 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| prizepicks|16557935 | prizepicks | Jayden Daniels | Pass Yards | under | 0.3359949609424918 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|91cd9a90-2bbb-4479-9d44-9025494f5dbb | underdog | Bo Nix | Pass Attempts | under | 0.33308348303432955 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|467e327e-fa6b-4a88-8db1-d41c35eecd45 | underdog | Alonza Barnett | Pass Yards | under | 0.32998572032187845 | 2026-11-05T12:22:13Z | 2026-11-07T20:45:00Z |
| prizepicks|16557945 | prizepicks | Kyler Murray | Pass Yards | under | 0.32685614816516073 | 2026-11-03T02:21:46Z | 2026-11-09T20:15:00.000-05:00 |
| underdog|57c9dc6a-5777-44c4-a352-8a75f42ba5fd | underdog | C.J. Stroud | Pass Yards | under | 0.3255781753629867 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|fa35b61f-7cc4-4f4b-9185-6e6a5167ad20 | underdog | Michael Penix | Pass Attempts | under | 0.3245304925645227 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|4fd3a242-cf5f-4eb3-a5db-95f253c0db3a | underdog | Josh Allen | Pass Attempts | under | 0.3201476032121736 | 2026-11-04T12:10:41Z | 2026-11-10T01:15:00Z |
| underdog|efda5476-bc73-4e5c-8d29-c3b22c80a111 | underdog | Drake Maye | Pass Yards | under | 0.3169471849941047 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|c180ec24-04be-4d76-92bd-f2b1a7387ad4 | underdog | Josh Jacobs | Receptions | under | 0.3138562329893375 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|cbf0d149-d120-49d4-b8d9-6df900ee39de | underdog | Bryce Young | Pass Yards | under | 0.31348509126095614 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| prizepicks|16557939 | prizepicks | Kirk Cousins | Pass Yards | under | 0.3094515764679242 | 2026-11-03T02:21:46Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|9d14ec55-11a1-45e7-b650-84b9a5ebf34c | underdog | J.J. McCarthy | Pass Yards | under | 0.304744428527313 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|37896abf-b78c-4078-bf55-90cf3966fe31 | underdog | Puka Nacua | Receiving Yards | under | 0.30330510113385567 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|5f0cd76c-a7f5-445c-83c0-0f0a646cceec | underdog | Brock Bowers | Receiving Yards | under | 0.29946639988592183 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|c276a65a-ae82-4954-9d4c-13d68aa92353 | underdog | Emeka Egbuka | Receiving Yards | under | 0.29901932004324594 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|b3820062-ff10-4245-afb1-048cb910cd60 | underdog | Brock Purdy | Pass Attempts | under | 0.29563370361590136 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|37eb3153-ffda-4141-b82c-9fe58b2797d9 | underdog | Saquon Barkley | Receptions | under | 0.29195979899497493 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|a4f7e2ea-445a-4746-9a01-bb8681efb55d | underdog | Drake Maye | Pass Attempts | under | 0.2890709907617405 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|f8c77f08-eed2-4650-9d24-1d0d679cc6bc | underdog | Geno Smith | Pass Yards | under | 0.2886104538649702 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|b1871eee-1be7-4d3b-b76e-1f9f7f70baca | underdog | J.J. McCarthy | Pass TDs | under | 0.2875734861947701 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|9b3c5181-13cc-4e03-a91e-71523f8cf2a6 | underdog | Christian McCaffrey | Rush + Rec Yards | under | 0.2845090099537876 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|fdc58256-b6a2-4c9d-8320-be20ed84dd8c | underdog | Jadarian Price | Rush + Rec Yards | under | 0.28292209777903254 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|7dc2a808-0f7f-4a12-a56c-9b8c0eb39095 | underdog | Thomas Castellanos | Pass Yards | under | 0.2822212178373662 | 2026-11-04T12:10:41Z | 2026-11-08T02:30:00Z |
| underdog|c65ae7a0-14dd-4948-bd2b-2216fbebe1d1 | underdog | Daniel Jones | Pass TDs | under | 0.27974205004038677 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|034db5e8-e2a4-4f3a-b113-160fa7977d4f | underdog | Jake Elliott | FG Made | under | 0.27609595620105687 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|54dd4224-8be5-455c-9f88-5f314596b5b4 | underdog | Jarvis Green | Rush Yards | under | 0.274989889070679 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|5247ba45-452a-4d52-a32f-e162e098e08e | underdog | Chase Brown | Rush + Rec Yards | under | 0.27247098122393076 | 2026-11-05T12:22:13Z | 2026-11-08T14:30:00Z |
| underdog|a3499f76-dc57-40ca-a12b-ccab39f10be5 | underdog | Bryce Young | Pass Attempts | under | 0.27237481147034737 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|2419efc4-e3a9-4d41-9ba4-8bc839a152e5 | underdog | Matthew Stafford | Pass Yards | under | 0.26613222526837244 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|5a0ff8aa-ab28-4f6c-9ec5-e95c971f8458 | underdog | Andy Borregales | Kicking Points | under | 0.2640899467628497 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|029429a0-88e2-4188-bb6a-963cd5a7c4e2 | underdog | Baker Mayfield | Pass TDs | under | 0.26332788339696256 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|99b3f099-bf0e-494a-983b-03ca62b2b244 | underdog | Joe Burrow | Pass Yards | under | 0.26236014873001245 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|3adb5b8e-9fc9-4c71-8c0d-2be1644fe037 | underdog | Jayden Daniels | Pass Attempts | under | 0.25997924896274693 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|8a93dc4a-7496-47f2-af11-b0faff063a96 | underdog | Antonio Williams | Receptions | under | 0.25960481049135886 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|d484d774-fbd8-467b-bbfa-b6f85cfcf83f | underdog | Courtland Sutton | Receptions | under | 0.25834377385355134 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|c7d0412f-1aba-47dd-8ce0-e06060ca7b59 | underdog | Kyle Pitts | Receiving Yards | under | 0.25799821779938514 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| prizepicks|16557928 | prizepicks | Bryce Young | Pass Yards | under | 0.25782403523201924 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|9d4fa631-2131-4a0c-9be8-fc96c08e2585 | underdog | Jake Weinberg | XP Made | over | 0.25701675995779105 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| prizepicks|16557933 | prizepicks | Patrick Mahomes | Pass Yards | under | 0.256531424485161 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|88b26255-d953-47cf-aa2d-032da6db6cbf | underdog | Caleb Williams | Pass TDs | under | 0.256421951810362 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|a83e0570-43a7-48e4-9c3b-282b1d3c4c77 | underdog | Braden Atkinson | Pass Yards | under | 0.255936044436764 | 2026-11-05T12:22:13Z | 2026-11-08T03:30:00Z |
| underdog|25d18fbf-8c15-4a17-895c-3635dd1ce944 | underdog | Malik Willis | Pass Attempts | under | 0.2526482871588408 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|b72f06e1-815c-4c36-b978-4fcc8dfeeef1 | underdog | Andy Borregales | FG Made | under | 0.25213168723502966 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| prizepicks|16577042 | prizepicks | Puka Nacua | Rec Yards | under | 0.24801878589627235 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|8da97392-7984-4efa-babd-cf659abd7f87 | underdog | Jadarian Price | Rush Yards | under | 0.24723910127654525 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|873e1627-8fef-41df-a8a8-a532b901c73f | underdog | Tyler Shough | Pass Yards | under | 0.24594495901612323 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|fc0a7b7f-a597-4192-b95e-8c3194038f1b | underdog | George Kittle | Receiving Yards | under | 0.2450159013262515 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|e84e4aa4-7537-48ef-99a7-49d36a0d5fc7 | underdog | Geno Smith | Pass Attempts | under | 0.2432377584583152 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|4fda8e9c-363d-4afa-a7ea-bfd6e658b497 | underdog | Jadarian Price | Receiving Yards | under | 0.23745283835166386 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|086d3034-b329-4134-984b-2b6ded88d1f4 | underdog | Olamide Zaccheaus | Receiving Yards | under | 0.2371867613668348 | 2026-11-05T12:22:13Z | 2026-11-08T14:30:00Z |
| underdog|4e219bc4-540f-4254-8899-fb2c0a6c9ef1 | underdog | Jordan Love | Pass Attempts | under | 0.23509904882189492 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|3112a9df-1d7e-4adb-a055-f42d8889ac90 | underdog | Elijah Moore | Receiving Yards | over | 0.23431853269243114 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|7a1a69b8-8f00-4ba4-8683-057a92c53d2e | underdog | D'Andre Swift | Rush + Rec Yards | under | 0.23362142851147583 | 2026-11-05T12:22:13Z | 2026-11-09T01:20:00Z |
| underdog|35d1779b-9b98-4325-9460-84c896b08ff2 | underdog | Courtland Sutton | Receiving Yards | under | 0.22953019104290462 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|d4b658ff-a41e-4bb2-9c00-52a5ed667ad4 | underdog | J.J. McCarthy | Pass Attempts | under | 0.22887506876878727 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|60cbaa38-c568-4879-a6f8-94b6e4e69559 | underdog | Tucker Kraft | Receiving Yards | under | 0.22559324997910668 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|58d83f19-bbad-408b-8378-a58d5e2757d3 | underdog | Antonio Williams | Receiving Yards | under | 0.22551109665563784 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|713b2721-78da-4cec-8f94-3e8a3e141d5d | underdog | Mike Washington | Receiving Yards | over | 0.22513540135851895 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|c1f72f3f-5755-4036-9793-3b0e1f55b9b2 | underdog | Rashee Rice | Receiving Yards | under | 0.2246943029433517 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|b7a27035-0410-4524-9b9f-8504019e9e93 | underdog | Malik Washington | Receiving Yards | under | 0.22383503418957196 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|56c89a0f-dc6e-4b4c-96e3-bf99a8fa6c9a | underdog | Chris Godwin | Receiving Yards | under | 0.22348657645878034 | 2026-11-05T12:22:13Z | 2026-11-09T01:20:00Z |
| underdog|da210a50-3071-4e2c-adcb-afd5d0cf32dd | underdog | Cam Little | FG Made | under | 0.22067313990849302 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|6d8eb0bb-0195-4e81-b62a-94edbb4b8341 | underdog | George Kittle | Receptions | under | 0.2205590308515778 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|cbe81fae-0fd4-4c4a-a372-73e62564617f | underdog | Daniel Jones | Pass Attempts | under | 0.22042723148484367 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|74c0e85c-ae6e-4468-95e9-12b7349db2dc | underdog | Thomas Castellanos | Pass TDs | under | 0.2196184644795488 | 2026-11-05T12:22:13Z | 2026-11-08T02:30:00Z |
| underdog|6bbf2a5a-63d8-4774-b146-9892eacd1ce1 | underdog | Kirk Cousins | Pass Attempts | under | 0.21906706972458956 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|b1b292ca-18cf-40bc-bd9f-e12fefdf9774 | underdog | Josh Jacobs | Rush + Rec Yards | under | 0.2185373608497626 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|3d11ff54-e68e-46fd-9bee-9f64e201a532 | underdog | Ladd McConkey | Receptions | under | 0.2182531395719538 | 2026-11-03T02:21:46Z | 2026-11-08T21:05:00Z |
| prizepicks|16557922 | prizepicks | Joe Burrow | Pass Yards | under | 0.2181379417292847 | 2026-11-03T02:21:46Z | 2026-11-08T09:30:00.000-05:00 |
| underdog|dda53bac-956f-44fb-bbf8-a19154368592 | underdog | Jonah Coleman | Rush Yards | under | 0.2173023237738393 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|5e5ead91-81b9-4b8e-a5ef-e2aa3b7a5ed0 | underdog | Woody Marks | Rush Yards | under | 0.21579731650075495 | 2026-11-05T12:22:13Z | 2026-11-08T21:05:00Z |
| underdog|d88c56d2-1395-401b-bd3e-3d1d31728d14 | underdog | Woody Marks | Rush + Rec Yards | under | 0.2133596409286077 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|dabb5287-277e-4a23-8946-40925b7c6a45 | underdog | Sione Vaki | Receiving Yards | over | 0.2124555475324016 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|e509bdfb-161e-4b4e-a5ba-0fea710f2ab8 | underdog | Rachaad White | Rush Yards | under | 0.21238054015985097 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|47643075-a2e0-4286-848c-4cbc6b64643e | underdog | Jaylen Wright | Rush + Rec Yards | under | 0.21167080472030686 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| prizepicks|16577049 | prizepicks | Trey McBride | Rec Yards | under | 0.20935259101009185 | 2026-11-03T02:21:46Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|124b3b05-13c3-459b-a56a-4e57de87b55b | underdog | Kyler Murray | Pass Attempts | under | 0.2075409708914847 | 2026-11-04T12:10:41Z | 2026-11-10T01:15:00Z |
| underdog|96d514bd-16df-438e-a060-00f5c8573329 | underdog | Patrick Mahomes | Pass Attempts | under | 0.20613805218871373 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|8f89d0b9-f92a-4c38-a221-ee558e759c84 | underdog | Will Henderson | Rush Yards | under | 0.20565821012077623 | 2026-11-04T12:10:41Z | 2026-11-06T00:30:00Z |
| underdog|c0462df6-b3da-4b63-b678-808191fb8671 | underdog | Colston Loveland | Receiving Yards | under | 0.20437151822603095 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|1fa93360-83ec-4148-833b-a2ac7223bcde | underdog | Evan McPherson | FG Made | under | 0.20387134321469125 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|e128c268-1e27-4d43-8afe-f312b35f36ff | underdog | Jake Fette | Pass Yards | under | 0.2026382938473199 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|c61022bc-362a-4e1c-8d69-48a576ea6c00 | underdog | Justin Herbert | Pass TDs | under | 0.20191287593682095 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|8a470514-a5ed-4184-858d-54e932096311 | underdog | Devaughn Vele | Receiving Yards | under | 0.2018443386221901 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|838239fd-0f4c-4832-b6a8-a19978944845 | underdog | Saquon Barkley | Rush + Rec Yards | under | 0.19878933592568027 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| prizepicks|16577051 | prizepicks | Brock Bowers | Rec Yards | under | 0.19828126826604298 | 2026-11-03T02:21:46Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|d9931ebc-f2b4-4965-a907-7e5426461db5 | underdog | Trey McBride | Receptions | under | 0.19807043328611007 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|d3d2a2d2-5f18-48d0-9316-dcd5ad29df72 | underdog | Rachaad White | Rush + Rec Yards | under | 0.19664442091925727 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|0ec8b169-3cec-4eea-b102-5daa0f8822ae | underdog | Keenan Allen | Receiving Yards | under | 0.19589128216315532 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|35f55b20-95d8-4be7-8a2a-b64ada15b21e | underdog | Daniel Hill | Receiving Yards | over | 0.1951439191257699 | 2026-11-05T12:22:13Z | 2026-11-07T20:30:00Z |
| underdog|9a2902e7-4ecf-4ea5-a36e-c5c8f6e59bb7 | underdog | Harrison Butker | FG Made | under | 0.19473086921391436 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|410efb5a-6f14-4f58-846b-fb76cf98cec4 | underdog | Matthew Stafford | Rush Yards | over | 0.1944521898255368 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|f9beee99-bf11-4d3d-8d93-9a1099560025 | underdog | James Cook | Receptions | under | 0.19213415801783407 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|0aeefc8a-3585-4426-9ce7-dfe6849d6817 | underdog | C.J. Stroud | Pass Attempts | under | 0.1912506788453352 | 2026-11-05T12:22:13Z | 2026-11-08T21:05:00Z |
| underdog|fd3d0aae-bac1-483e-950c-971927275c97 | underdog | Trevor Lawrence | Pass Attempts | under | 0.19109471904869135 | 2026-11-05T12:22:13Z | 2026-11-06T01:15:00Z |
| underdog|872eac2a-4e79-4367-a987-6a15c41a88dc | underdog | Kyle Pitts | Receptions | under | 0.1884927972756335 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|d34c91c5-ef7c-4feb-9ff3-c957645da483 | underdog | Ja'Marr Chase | Receiving Yards | under | 0.18806437242923668 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|8dbf386b-4f79-48a2-bac6-e537c9e7cc3f | underdog | Bo Jackson | Rush Yards | under | 0.1858711887675657 | 2026-11-05T12:22:13Z | 2026-11-07T20:30:00Z |
| underdog|e8b42489-088d-4fa3-8358-e7bd4e883b98 | underdog | Marvin Harrison | Receiving Yards | under | 0.18582900335069386 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|b8d4dab3-6a1d-41b4-83ea-0448c7b54f32 | underdog | Caden Veltkamp | Pass Yards | under | 0.18508162154040408 | 2026-11-04T12:10:41Z | 2026-11-06T00:30:00Z |
| underdog|6af5960a-1d9d-4f3c-ab5d-c2bcd805cfc7 | underdog | Baker Mayfield | Pass Attempts | under | 0.1838540296279383 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|df0fcb9f-5100-4910-b141-a65adc25e74e | underdog | Joe Burrow | Pass Attempts | under | 0.18375588026906453 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|f4c69603-6218-4437-8fdd-275d6fcfe8ef | underdog | Jason Myers | FG Made | under | 0.1827109251134501 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| prizepicks|16685557 | prizepicks | Justin Herbert | Pass TDs | under | 0.18176877497841348 | 2026-11-05T12:22:13Z | 2026-11-08T16:05:00.000-05:00 |
| underdog|63c520e3-4fd1-4a1f-a7a9-3a7b0b8c1291 | underdog | Nico Collins | Receiving Yards | under | 0.1799086895550015 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|cfae8805-6e9b-4151-aae5-009efb71986a | underdog | Brock Bowers | Receptions | under | 0.17887742031236042 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|e218a11c-9086-4de7-9478-faae2805f52c | underdog | Jonah Coleman | Rush + Rec Yards | under | 0.17822581983705676 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|9100eaf4-8232-4056-8f1f-336a475cc678 | underdog | Rhamondre Stevenson | Rush Yards | under | 0.17609187646102753 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|320f34c3-44ad-4de3-af16-d746b08151c9 | underdog | Seth Cromwell | Rush Yards | under | 0.17410598482385498 | 2026-11-05T12:22:13Z | 2026-11-06T01:00:00Z |
| underdog|58473198-16c0-4f1f-98ce-794fe0d452fd | underdog | Rashee Rice | Receptions | under | 0.17383563925443812 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|1679c0a9-3ab3-4b8b-8082-3f7d6934a2fe | underdog | JC Evans | Pass TDs | over | 0.1729071155551049 | 2026-11-05T12:22:13Z | 2026-11-06T01:00:00Z |
| underdog|e67e9ba5-8b23-46cb-a546-85415df91843 | underdog | Luke Fahey | Pass TDs | under | 0.17214479173554886 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|fdc20714-2850-4478-a9ae-058d3a14ba1b | underdog | Jake Elliott | Kicking Points | under | 0.1717042647640432 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|1837c09f-5acf-4d77-bac8-5140547ef104 | underdog | Tyler Shough | Pass Attempts | under | 0.17124267278734184 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|5294f95e-70ef-47dd-8cdf-91081da98280 | underdog | Kyler Murray | Pass TDs | under | 0.17036826288931617 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|622e16fe-4fbe-4da3-a317-19e2d3ef55e5 | underdog | Josh Hines-Allen | Sacks | under | 0.1703162171599144 | 2026-11-05T12:22:13Z | 2026-11-06T01:15:00Z |
| underdog|d1484ee9-014f-45d1-a126-1d177aec34ed | underdog | Makhi Hughes | Rush Yards | under | 0.1692475397419455 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|1e0723e6-39f5-401c-9ecb-73146c38ec61 | underdog | Marvin Harrison | Receptions | under | 0.16835016265867342 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|a8a9bed2-5d3a-4afa-b7f7-de3a2c658f75 | underdog | Jared Goff | Rush Yards | over | 0.1677182366005825 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|cf74ea13-4c83-486b-a699-efa71530a041 | underdog | Amon-Ra St. Brown | Receptions | under | 0.16742438992001507 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|3c2c0991-0e80-4489-9557-56d68aa8268c | underdog | Wil Lutz | FG Made | under | 0.1665329706004408 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|c7fbbf68-83ff-44a2-a032-87a9503edea0 | underdog | Cairo Santos | FG Made | under | 0.16650636156632292 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|15045f83-f7c4-4e88-a249-0602b4dfe33f | underdog | Jordan Mason | Rush Yards | under | 0.1664614051365807 | 2026-11-05T12:22:13Z | 2026-11-10T01:15:00Z |
| underdog|4a902d41-198f-4763-ad4f-c1aabaf04d56 | underdog | Darian Mensah | Pass TDs | over | 0.16623847690906796 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|bd6835b3-2c6e-4ba0-aa21-2002c9c11af4 | underdog | Jackson Kleather | FG Made | over | 0.16618416805976138 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|73f2643f-52d1-490b-a801-df52538bf621 | underdog | Austin Hooper | Receiving Yards | over | 0.16565211889871145 | 2026-11-05T12:22:13Z | 2026-11-08T14:30:00Z |
| underdog|1618355e-edef-449f-bc87-1cc1db3b63f7 | underdog | Tyler Warren | Receiving Yards | under | 0.16541696176617582 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|6b0a254c-fbec-481c-b649-05d1a353bcae | underdog | Harrison Butker | Kicking Points | under | 0.16442129921836235 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|2e9b040f-7cc3-4024-aec9-be035736f3c3 | underdog | Christian McCaffrey | Receiving Yards | under | 0.1641803329215591 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|034db9bb-ff4a-44ae-a77d-895b9e9c1070 | underdog | Rhamondre Stevenson | Rush + Rec Yards | under | 0.16385789880177226 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|89a5bb97-1393-4679-8d6e-45b1bd8a62ea | underdog | Jordan Mason | Rush + Rec Yards | under | 0.1624124156770972 | 2026-11-05T12:22:13Z | 2026-11-10T01:15:00Z |
| underdog|26b34dbd-c8b5-4155-8b09-75b12c1ecd7a | underdog | Stefon Diggs | Receptions | under | 0.1623657419982183 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|9ff29ccb-f4c3-4664-9330-39133772a9f1 | underdog | Tucker Kraft | Receptions | under | 0.1615364063191952 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|9cc36ab9-fd71-4bfb-813b-54422aecd68a | underdog | Anthony Colandrea | Pass Yards | under | 0.16122272665769133 | 2026-11-04T12:10:41Z | 2026-11-07T01:00:00Z |
| underdog|6338b794-ef8d-4a6b-96b1-87b6d36e7627 | underdog | Kenny Minchey | Pass TDs | over | 0.16092549766911135 | 2026-11-05T12:22:13Z | 2026-11-07T23:15:00Z |
| underdog|528a645e-8439-47f6-91f3-89566cf92574 | underdog | Greg Dulcich | Receptions | under | 0.15981895291377868 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|8f289276-834c-4a60-ac19-2b8e634918e6 | underdog | Ollie Gordon | Rush + Rec Yards | under | 0.15941145377301513 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|bb77573a-4a49-460a-b9a5-e71be79f2ce2 | underdog | Jared Goff | Pass Attempts | under | 0.15940465299458384 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|7d8aca5c-098a-4cd2-ac18-2986be8ea813 | underdog | Matthew Golden | Receptions | under | 0.15935064858874126 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|de6281e6-e72c-4f7d-9b19-ea93df015060 | underdog | Drake London | Receptions | under | 0.1588244841998091 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|698f97b3-863e-4773-97b1-02795f52198b | underdog | Dak Prescott | Pass Attempts | under | 0.15742541666457277 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|549e9cef-a3a5-4d2d-80da-e1502e502bd7 | underdog | Tyler Goodson | Rush + Rec Yards | under | 0.15738112185450548 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|e41a0da4-0291-4499-9b1b-ed6fe79cddc8 | underdog | Ollie Gordon | Receiving Yards | under | 0.15660530020212726 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|0b592d73-46b4-4456-918c-8d00242be932 | underdog | Dawson Knox | Receptions | under | 0.15649493040707285 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| prizepicks|16675752 | prizepicks | J'Koby Williams | Rush Atts | under | 0.15626612680045937 | 2026-11-05T12:22:13Z | 2026-11-07T21:30:00.000-05:00 |
| underdog|f6cfe146-eab9-41e2-9ffc-5dae6dd020db | underdog | Isaiah Mizell | Receptions | under | 0.15348737235866394 | 2026-11-05T12:22:13Z | 2026-11-07T03:15:00Z |
| underdog|c3a8e703-937f-4b67-87af-d63af0313595 | underdog | Liam Boyd | XP Made | over | 0.15303281462856144 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|e8cea968-ba0e-4062-bbde-a10b4c491b27 | underdog | Billy Edwards Jr. | Pass Yards | under | 0.15110868554995638 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|5eea8199-5dbe-4649-a20a-2405bd63d177 | underdog | Jaxon Smith-Njigba | Receptions | under | 0.15026450962994486 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|7f44b052-27a1-42a5-8108-ca43bdfcb5bb | underdog | Chuba Hubbard | Rush + Rec Yards | under | 0.14959006456056478 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|e0c22419-0dff-4556-a05e-9acfa3ab7a09 | underdog | Brandon Aubrey | FG Made | under | 0.14958269462275497 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|b0ce99d7-ccca-47c0-a454-e6f920eab8e2 | underdog | Bo Nix | Pass TDs | under | 0.14921921703126695 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|78f69cb1-b2ea-4410-853d-44094574eb64 | underdog | Parker Washington | Receiving Yards | under | 0.1490737198822808 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|69ba3a63-bb92-4f39-984a-ed5566438f78 | underdog | Nick Folk | FG Made | under | 0.1481435952641591 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|c4587fdc-fe2d-47dc-997d-d0b08663b00a | underdog | Ka'imi Fairbairn | FG Made | under | 0.1479318682678138 | 2026-11-03T02:21:46Z | 2026-11-08T21:05:00Z |
| underdog|1b370830-3867-4ade-9a8d-418a06dbd1c1 | underdog | Christian Watson | Receptions | under | 0.1479168165648339 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|1aeae776-d0b1-4470-b144-6de49c2cb956 | underdog | Bear Bachmeier | Pass TDs | over | 0.14784749034407785 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|2484637b-dd6a-4882-be40-ce0e68d4e559 | underdog | Kenny Gainwell | Receptions | under | 0.1475602481670133 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|13d49fc8-9559-45e1-9bac-6f15a20a2c72 | underdog | Ollie Gordon | Receptions | under | 0.14682805397570908 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|ad5841e3-f51c-4e2d-a883-064eb9b2257f | underdog | Malik Washington | Receptions | under | 0.14645959659878283 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|f57c0032-b5b1-4228-af7c-d6bb6f08e67e | underdog | Emeka Egbuka | Receptions | under | 0.1460648049345178 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|b5acd5c8-143c-4860-995f-2366f9a662f7 | underdog | Kalieb Osborne | Pass TDs | over | 0.1460045485512973 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|05cc47cb-d23e-4419-9af1-81291611e3a4 | underdog | Saquon Barkley | Rush Yards | under | 0.14498790320221477 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|a5687c54-7273-4922-8cf8-a0383ebb4afa | underdog | Trey McBride | Receiving Yards | under | 0.14497443435005852 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|d1ad5738-520b-4373-b127-b15ab45c351a | underdog | Jaxon Smith-Njigba | Receiving Yards | under | 0.14355065406302003 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|154a1940-c81e-490b-85b4-83bd1bac4598 | underdog | Jalen Nailor | Receiving Yards | under | 0.14280205217730946 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|64d2b206-1322-4e8d-af48-ca203fadf3f7 | underdog | Foyesade Oluokun | Sacks | over | 0.14246574303285914 | 2026-11-05T12:22:13Z | 2026-11-06T01:15:00Z |
| underdog|8d2750d2-9d3b-48ff-8e00-77d67f7ecdc8 | underdog | Ladd McConkey | Receiving Yards | under | 0.14192042119468462 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|1acc37b7-16ae-4dfe-9876-857c87ea3b17 | underdog | Quentin Johnston | Receiving Yards | under | 0.1413979010411639 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|19182bf3-3972-4fb8-ad6e-ff29a13cff8c | underdog | Chase Brown | Rush Yards | under | 0.13989207436771856 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|a1cfa87e-a290-405f-a34d-0e0743d79fc0 | underdog | Matthew Stafford | Pass Attempts | under | 0.13964289370674687 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|e1775404-5113-460c-9eec-b13c0226b55b | underdog | Olamide Zaccheaus | Receptions | under | 0.1396223249639138 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|03e0d95d-f3f0-4f64-bea2-e9e8bbb684e3 | underdog | AJ Barner | Receptions | under | 0.13910664132787998 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|f31a1e8b-9aa9-4022-b468-859f852768cb | underdog | Devaughn Vele | Receptions | under | 0.13901253046609652 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|3c114bc2-839b-4e55-9ec0-5de96e8522a9 | underdog | Caleb Douglas | Receptions | under | 0.1384724673367177 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|5df51a97-b605-4c0d-b9a5-6038554d83e4 | underdog | Amon-Ra St. Brown | Receiving Yards | under | 0.13837637499846278 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|83b965d9-e75e-4d7b-8886-44573ffbcdfb | underdog | Dilin Jones | Rush Yards | under | 0.13798927114368054 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|982d244a-334a-42a6-88f1-48e550976962 | underdog | Rome Odunze | Receiving Yards | under | 0.13795611798722607 | 2026-11-05T12:22:13Z | 2026-11-09T01:20:00Z |
| underdog|8b70666b-7c44-46a9-b6c6-97917dd6b54e | underdog | David Amador | Receiving Yards | under | 0.137814752890017 | 2026-11-05T12:22:13Z | 2026-11-06T00:30:00Z |
| underdog|7510d34a-d239-42b9-90b3-80b4726c3715 | underdog | Janice Tjen | Double Faults | over | 0.1374447464413906 | 2026-11-05T12:22:13Z | 2026-11-06T09:30:00Z |
| underdog|62752957-b2d2-43f1-8caa-62560a2db86a | underdog | Brock Purdy | Pass TDs | under | 0.13705484641190113 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|d6cbee1a-cecf-45c3-92bd-590b34f8135a | underdog | Nick Folk | Kicking Points | under | 0.1351811208582573 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|562e6f84-dc38-442e-a399-2241e5054d3a | underdog | Cam Skattebo | Rush + Rec Yards | under | 0.13431542192173662 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|0a1d4a28-f4ed-433b-a45b-953e95969acb | underdog | Jadarian Price | Receptions | under | 0.13399424688283068 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|5790a889-8601-4824-ac78-b9c766ba1891 | underdog | Marvin Mims Jr. | Receptions | under | 0.13357422686133513 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|e5b104d0-4d4a-40f8-b1af-c7a433122290 | underdog | Ethan Moczulski | FG Made | over | 0.13305034470819216 | 2026-11-04T12:10:41Z | 2026-11-07T01:00:00Z |
| underdog|43fc0caa-1949-4da2-a325-7ae1d7d9021c | underdog | Mitchell Evans | Receiving Yards | over | 0.13294828591332086 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|a8bd5139-d684-40d6-bc24-4b66faf6fb16 | underdog | Xavier Worthy | Receiving Yards | under | 0.1322551321739447 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|d0b6fbf3-ddeb-4be4-a4c6-1ac1581835e5 | underdog | Cade Otton | Receptions | under | 0.13207335081342486 | 2026-11-05T12:22:13Z | 2026-11-09T01:20:00Z |
| underdog|6a4ea7ca-8051-400b-a435-f94e0a7067ee | underdog | Jameson Williams | Receiving Yards | under | 0.131077359753479 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|fcc59928-c671-462f-b566-25093f2522a8 | underdog | Caden Buhr | FG Made | over | 0.1306453456015051 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|0a8f4ddd-5226-46c0-8e8f-2032e61d488a | underdog | Mike Green | Sacks | over | 0.1306071769202533 | 2026-11-05T12:22:13Z | 2026-11-06T01:15:00Z |
| underdog|c2ddeb9f-7361-42cc-9e8d-96707debdc6f | underdog | Jahmyr Gibbs | Rush + Rec Yards | under | 0.12990836667624628 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|14d37ea9-87e7-4e15-ad26-f93259d0facd | underdog | Drew Lock | Pass TDs | under | 0.12966967278207253 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|3aa93bf4-8e56-4a6e-8771-99a3e7b252f0 | underdog | Kaleb Edwards | Receiving Yards | over | 0.1291255418811703 | 2026-11-05T12:22:13Z | 2026-11-07T20:30:00Z |
| underdog|49dfd4ee-dd3e-46c0-b47e-4a77a2cd1893 | underdog | Cam Little | Kicking Points | under | 0.12899634811527072 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|ccfe2bba-71d1-4e46-bf46-d00e2a8c975c | underdog | Javonte Williams | Rush + Rec Yards | under | 0.12875496760840743 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|5869b7ef-5cbd-40b2-b17d-2b4591a92144 | underdog | Matthew Golden | Receiving Yards | under | 0.12870107458299462 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|7a288207-299b-4695-b585-940ac0294fdc | underdog | Luke Fahey | Pass Yards | under | 0.12864978345130762 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|62f9a543-0bcb-4809-a0ad-a3fb06f0fd56 | underdog | Kimani Vidal | Rush + Rec Yards | under | 0.12847033899950944 | 2026-11-05T12:22:13Z | 2026-11-08T21:05:00Z |
| underdog|19e203ae-9eb3-4093-92c9-c8ba8618d75a | underdog | Jonathan Taylor | Rush Yards | under | 0.12832301351138986 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|a9d2cbf9-b134-4d3d-97b8-16d220ba4894 | underdog | George MacIntyre | Pass Yards | under | 0.1273705463987821 | 2026-11-05T12:22:13Z | 2026-11-07T23:15:00Z |
| underdog|f9408da3-4c03-47a1-91ac-c4ac94507742 | underdog | Drake London | Receiving Yards | under | 0.12714827801752404 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|d0824875-ecc3-4eba-84bf-42adc38d8c61 | underdog | Owen McCown | Pass Yards | under | 0.12672126941237805 | 2026-11-05T12:22:13Z | 2026-11-06T00:30:00Z |
| underdog|5adfe6e8-e91f-44dd-842d-5be373846225 | underdog | Chris Olave | Receptions | under | 0.12468750167033804 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|58790b19-dd02-48db-9994-baaab8acbb8b | underdog | Rachaad White | Receptions | under | 0.12456515053371986 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|abe5fb36-b140-496d-8138-08cf2021eab6 | underdog | Jayden Daniels | Pass TDs | under | 0.12401048501725953 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|a5a84e5b-2d1a-407b-ad40-5e0faa4d1d12 | underdog | Wil Lutz | Kicking Points | under | 0.12375220362671835 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|6fa07966-69ad-4e19-932b-f21a9e51b66b | underdog | Ollie Gordon | Rush Yards | under | 0.12319862002616433 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|a75d0892-12c3-4a3d-bea7-a07236a8702c | underdog | Conner Weigman | Pass Yards | under | 0.12251598812778575 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|f3d5e2f8-b078-48d2-b5d6-54ca6ca199e6 | underdog | Cairo Santos | Kicking Points | under | 0.12236507723893952 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|bf5c8287-a719-4bc8-a84d-21b682a39a7b | underdog | Kenny Gainwell | Receiving Yards | under | 0.12233318149565453 | 2026-11-05T12:22:13Z | 2026-11-09T01:20:00Z |
| underdog|06a98b20-5b6a-4641-963b-748d6b6ac027 | underdog | Ja'Marr Chase | Receptions | under | 0.12198379656106328 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|49c7fddc-e499-4259-8ee1-32af7aa9b5e7 | underdog | Jakobi Meyers | Receiving Yards | under | 0.12197721086956004 | 2026-11-05T12:22:13Z | 2026-11-06T01:15:00Z |
| underdog|9bf843c7-11d8-47c1-8d3d-ba3eb2bfbad1 | underdog | Maria Sakkari | Double Faults | under | 0.12150011152757467 | 2026-11-05T12:22:13Z | 2026-11-06T10:30:00Z |
| underdog|18971421-29b9-4aa5-b533-b3255d1a9695 | underdog | Bijan Robinson | Rush + Rec Yards | under | 0.12137057551043673 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|16510e89-3e9d-4b33-9549-19154015507d | underdog | Tyler Allgeier | Receptions | under | 0.12089928730863053 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|24fc1491-af1a-4979-9f5b-37e947f9cfc6 | underdog | Jared Curtis | Pass Yards | under | 0.12016813000663651 | 2026-11-05T12:22:13Z | 2026-11-07T21:15:00Z |
| underdog|0187bc04-2901-4ba3-8977-4bd9fb0d707b | underdog | Katin Houser | Rush Yards | over | 0.1201508756895383 | 2026-11-04T12:10:41Z | 2026-11-07T01:00:00Z |
| underdog|03b3eb0d-b146-440d-843d-79223ef0bf2b | underdog | Jahan Dotson | Receptions | under | 0.1200345581620813 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| prizepicks|16619686 | prizepicks | Chris Dawn Jr. | Recs | under | 0.11978140668783599 | 2026-11-04T12:10:41Z | 2026-11-07T22:30:00.000-05:00 |
| underdog|94fc7a75-ac49-46e5-aa74-e6a67b1bd62c | underdog | Tyler Goodson | Rush Yards | under | 0.11960752661139407 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| prizepicks|16576409 | prizepicks | Christian McCaffrey | Rush Yards | under | 0.11950744181162642 | 2026-11-03T02:21:46Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|3ca0797a-6c45-46f4-8b61-0d000eda9dc5 | underdog | Ayden Greene | Receptions | over | 0.11935754910617813 | 2026-11-05T12:22:13Z | 2026-11-07T00:00:00Z |
| underdog|c7bb0bb6-dc60-4c38-93e2-684dacb04b02 | underdog | Josh Allen | Pass TDs | under | 0.11926653211048077 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|33ffb548-94a1-44e7-9da3-17dc0d7f1d49 | underdog | J'Koby Williams | Receiving Yards | over | 0.11825318810941854 | 2026-11-04T12:10:41Z | 2026-11-08T02:30:00Z |
| underdog|eccd30c3-ed5b-4cc6-aad4-06299d22c529 | underdog | Malik Nabers | Receptions | under | 0.11783962166306128 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|3af0bcc2-f9da-427a-9708-fd1b9e5e5f2d | underdog | Trinidad Chambliss | Pass Yards | under | 0.11770205880824303 | 2026-11-04T12:10:41Z | 2026-11-08T00:30:00Z |
| underdog|1a302e32-ea50-4ad7-9fcd-27c67675614e | underdog | Josh Cameron | Receptions | under | 0.1176734146378754 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|8ff7795f-8993-4343-8cf8-c00a7c1b313f | underdog | Kayshon Boutte | Receiving Yards | over | 0.1168823575350102 | 2026-11-05T12:22:13Z | 2026-11-08T21:05:00Z |
| underdog|2d49afa9-bf55-4cd2-8efe-1f0dc62786fc | underdog | Tait Reynolds | Pass TDs | under | 0.11668508117452292 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|706748df-749d-45e6-b110-12bf7e014254 | underdog | Justice Hill | Receiving Yards | under | 0.11637029719305003 | 2026-11-05T12:22:13Z | 2026-11-06T01:15:00Z |
| underdog|c3130728-988e-4cdf-9fa4-96cbff03e330 | underdog | Kyren Williams | Rush Yards | under | 0.11604746503488483 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|6efc22a4-0d91-487b-822d-d7f27a3218b2 | underdog | George MacIntyre | Pass TDs | under | 0.11581459797425153 | 2026-11-05T12:22:13Z | 2026-11-07T23:15:00Z |
| underdog|70e0d2d6-f516-4a04-89fe-7a65b42428ad | underdog | Mike Washington | Rush + Rec Yards | under | 0.11579638293438832 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|a1bd5dce-96e7-4c34-80a7-d778c68817e3 | underdog | Jonah Coleman | Receiving Yards | under | 0.11576234619439185 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|649d4cf3-3d96-4754-b6ba-149b97bba842 | underdog | Kenneth Walker III | Receptions | under | 0.11559688528805712 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|b131a074-2cef-4b49-ba41-a233aa6adac0 | underdog | Cade Otton | Receiving Yards | under | 0.1153806979626707 | 2026-11-05T12:22:13Z | 2026-11-09T01:20:00Z |
| underdog|9825e0ba-f877-4bf7-812c-f9129d57348c | underdog | Patrick Mahomes | Pass TDs | under | 0.11537751808865182 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|df8cc29e-c9c7-46e3-9773-066f25acc7a6 | underdog | CeeDee Lamb | Receptions | under | 0.11512462845971994 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|f2f45b87-957b-46ab-9edf-e31974176078 | underdog | Thomas Castellanos | Rush Yards | under | 0.11460442719465413 | 2026-11-04T12:10:41Z | 2026-11-08T02:30:00Z |
| underdog|38de0e6f-f49d-4e9a-8d80-f5db22277565 | underdog | Michael Salgado-Medina | XP Made | over | 0.11420342060199357 | 2026-11-05T12:22:13Z | 2026-11-07T03:15:00Z |
| underdog|79b8fb2e-5394-44ef-904f-e9e780d978d2 | underdog | Michael Hawkins | Pass TDs | over | 0.11376347858114072 | 2026-11-05T12:22:13Z | 2026-11-08T02:30:00Z |
| underdog|f998ca60-532c-4d98-99b2-c1491adee125 | underdog | John Metchie III | Receiving Yards | under | 0.11354540433749227 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|8dda3f2c-43bd-496a-91aa-283c7a072e7b | underdog | Chuba Hubbard | Receptions | under | 0.11351803648802827 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|fdc2cba3-5628-496b-92fe-05b5d00d90e6 | underdog | Braylon Staley | Receptions | under | 0.11333666895548766 | 2026-11-05T12:22:13Z | 2026-11-07T23:15:00Z |
| underdog|980ef0c9-e7c6-40c1-ae91-d71c59322e06 | underdog | Travis Kelce | Receptions | under | 0.11333613992057967 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|48e760c2-4eac-4eb7-a8a9-531f0ca1ef83 | underdog | Ryan Fitzgerald | Kicking Points | under | 0.11326096940715735 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|1f37a02f-1db6-464f-9fa6-211296f14cbc | underdog | Aliaksandra Sasnovich | Double Faults | over | 0.1129708424047684 | 2026-11-05T12:22:13Z | 2026-11-06T10:30:00Z |
| underdog|516cd42e-4751-4b27-abbb-5cc40fef6cbf | underdog | Jaylen Wright | Rush Yards | under | 0.11295640133296947 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|3b806c99-c348-44de-86cc-461e6cf2d3f2 | underdog | Jake Bates | FG Made | under | 0.11285240847954703 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|36391894-b67e-489e-a9ba-6d5745343435 | underdog | Nate Adkins | Receiving Yards | over | 0.11258180819122365 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|03ec69f5-d3df-44c5-8fb2-3316fd0932df | underdog | LaNorris Sellers | Pass Yards | under | 0.11247455420063979 | 2026-11-05T12:22:13Z | 2026-11-07T20:00:00Z |
| prizepicks|16577048 | prizepicks | George Pickens | Rec Yards | under | 0.11245540278204647 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|f48da050-199d-44b1-b56e-450cb1cc55b9 | underdog | Raleek Brown | Receiving Yards | over | 0.11219282113360729 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|fadb69a5-2f84-42de-a83a-f7bd3242f9db | underdog | Greg Dulcich | Receiving Yards | under | 0.1120073367268899 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|ba27855c-f306-460f-8d0b-850a557fe3e5 | underdog | James Cook | Rush + Rec Yards | under | 0.11131941599424644 | 2026-11-04T12:10:41Z | 2026-11-10T01:15:00Z |
| underdog|928f2702-cf72-4a70-a6d0-5ec09e5f5230 | underdog | Elena Rybakina | Double Faults | under | 0.11131635357439684 | 2026-11-05T12:22:13Z | 2026-11-08T20:00:00Z |
| underdog|778014fa-0b1d-4120-8eac-121c9d4e8db4 | underdog | Jalen Royals | Receiving Yards | over | 0.11116256315833206 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|4781b322-c16f-488a-b23d-ff4462376142 | underdog | Matthew Stafford | Pass TDs | under | 0.11063723570251016 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|1fecccd3-7915-4b3d-9923-95b353ee0c90 | underdog | J.K. Dobbins | Receptions | under | 0.11024990718515137 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|4bde96ab-c2a0-4521-99f1-927de9f655d5 | underdog | Noah Fifita | Pass Yards | under | 0.10990429484338526 | 2026-11-05T12:22:13Z | 2026-11-07T03:15:00Z |
| prizepicks|16685556 | prizepicks | Dak Prescott | Pass TDs | under | 0.10986040123516894 | 2026-11-05T12:22:13Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|87ced712-c478-425d-ab92-8115cd35eba6 | underdog | Lincoln Kienholz | Pass TDs | under | 0.10982554717127524 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|685edd25-24fb-4af2-a25d-548ec56bea29 | underdog | Tyler Warren | Receptions | under | 0.10969276868099631 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|643576c1-446e-4d42-a0fb-007c8ec84a4d | underdog | CeeDee Lamb | Receiving Yards | under | 0.10963618384661089 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|0c982e54-179a-4101-a215-70855b7eaf00 | underdog | D'Andre Swift | Receptions | under | 0.10961929542717408 | 2026-11-05T12:22:13Z | 2026-11-09T01:20:00Z |
| underdog|b34d3248-ec10-4121-9c7b-b4746dee816d | underdog | Charlie Kolar | Receptions | under | 0.10960132616239582 | 2026-11-05T12:22:13Z | 2026-11-08T21:05:00Z |
| underdog|57815146-a656-43d6-9668-35d136e67d23 | underdog | Devon Dampier | Pass Yards | under | 0.10960047075501667 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|69a82857-d297-4b15-a385-2a023ebcf054 | underdog | Dalton Kincaid | Receptions | under | 0.10948029145485216 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|29346c18-d730-4e5c-b4eb-9fd6bf0022e3 | underdog | Eric Singleton | Receiving Yards | under | 0.1094767255431981 | 2026-11-05T12:22:13Z | 2026-11-08T00:45:00Z |
| underdog|ba47c124-db10-4b69-b5cf-5ba62f5c4d37 | underdog | Jahmyr Gibbs | Receptions | under | 0.10946590257471323 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|14dd7e40-30bd-4230-aa09-2bcee96f116b | underdog | Katin Houser | Pass Yards | under | 0.10931626492452251 | 2026-11-04T12:10:41Z | 2026-11-07T01:00:00Z |
| underdog|e2b4bad8-1412-4ef1-807c-2d9921b75224 | underdog | John Love | FG Made | over | 0.10906649198025498 | 2026-11-04T12:10:41Z | 2026-11-07T00:00:00Z |
| underdog|b839652f-0e46-467f-9992-35c5469cf144 | underdog | D'Andre Swift | Receiving Yards | under | 0.10895292459147943 | 2026-11-05T12:22:13Z | 2026-11-09T01:20:00Z |
| underdog|84862c77-4fed-4053-8529-6f08d478c203 | underdog | MarShawn Lloyd | Receiving Yards | over | 0.10891889187033654 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|73cebe73-e574-4642-bd7c-dc1ec1949ca6 | underdog | Tait Reynolds | Pass Yards | under | 0.10867407609944801 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|a0eb3048-bcf7-483f-a312-d719004e816e | underdog | Conner Weigman | Pass TDs | under | 0.10842608409629839 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|2a03ddda-093f-4ef6-a512-af233e05477d | underdog | Chad Ryland | FG Made | over | 0.10832807545342293 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|7182897d-112d-4bbe-8f0b-571fe8c23a77 | underdog | Cam Cook | Receiving Yards | over | 0.10825855385349281 | 2026-11-05T12:22:13Z | 2026-11-08T02:30:00Z |
| underdog|4c17b548-6dd0-41a7-be94-4eeba93de71a | underdog | Nico Collins | Receptions | under | 0.10808570977681886 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|eb2fa42f-cb81-4a92-9c6c-ac9cde6fd8a9 | underdog | Mario Sanders | Receptions | under | 0.10801479925554192 | 2026-11-05T12:22:13Z | 2026-11-06T01:00:00Z |
| underdog|b0650bc9-efe4-4dbf-9416-709a9e27dd86 | underdog | Jonathan Taylor | Rush + Rec Yards | under | 0.10787887825189812 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|aae53e01-f29b-4b40-935d-82fd3dc57c69 | underdog | Ventrell Miller | Sacks | over | 0.10718233883676231 | 2026-11-05T12:22:13Z | 2026-11-06T01:15:00Z |
| underdog|1b7021b4-b333-4256-bc1e-7c9f88464431 | underdog | Jonah Coleman | Receptions | under | 0.10693828108030978 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|d599a5ae-1ff8-4df6-9eac-c397c998888d | underdog | Colston Loveland | Receptions | under | 0.10664747026618215 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|aa3a8e1a-50c0-490a-b9e5-fc10a40c31ef | underdog | Sam LaPorta | Receiving Yards | under | 0.10649841022955198 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|0e82f134-dd2d-4ebd-a343-0e5e5b207c73 | underdog | Marcel Reed | Pass Yards | under | 0.1062227368573625 | 2026-11-05T12:22:13Z | 2026-11-07T20:00:00Z |
| underdog|b2610581-1dba-42be-9214-d3cf13c4be2f | underdog | Brian Rowe | Receptions | over | 0.10600187240860914 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|866fa3e8-bc09-4ddc-a0f3-84f88eaf57ce | underdog | John Metchie III | Receptions | under | 0.1060012724235827 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|68027fbe-2681-4510-8eea-3775ceb54e92 | underdog | Dalton Schultz | Receptions | under | 0.10596561958189699 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|94d85ea2-59b0-4c35-8b60-0bb7774ade8d | underdog | Josh Cuevas | Receiving Yards | over | 0.10550899825954008 | 2026-11-05T12:22:13Z | 2026-11-06T01:15:00Z |
| underdog|575a4b9f-96a0-494c-a0ef-bcd27ce4bdb5 | underdog | Carson Hilbert | XP Made | under | 0.10478017790698868 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|3dd97269-7090-4494-b0ba-aef942cacee8 | underdog | Jared Goff | Pass TDs | under | 0.10432511994565019 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|2b07303d-fe20-4bc5-8345-34bde54e95a1 | underdog | Dak Prescott | Pass TDs | under | 0.10429726760636782 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|4a328574-9067-45a3-b2c8-168d822b5e16 | underdog | T.J. Hockenson | Receiving Yards | under | 0.10407541804729603 | 2026-11-03T11:59:28Z | 2026-11-10T01:15:00Z |
| underdog|1db30023-5914-439c-ac51-c556c30f7a5b | underdog | Marshall Pritchett | Receiving Yards | over | 0.1040578939603718 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|a3d2a9ad-7c96-4647-8be0-43a6f0c7e9c6 | underdog | Mike Matthews | Receptions | under | 0.10398872315492169 | 2026-11-05T12:22:13Z | 2026-11-07T23:15:00Z |
| underdog|4d4a6a56-43e2-4efe-9cca-06528df03d2e | underdog | Arch Manning | Pass TDs | over | 0.10334919497088374 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| prizepicks|16577039 | prizepicks | Rashee Rice | Rec Yards | under | 0.10318750310261049 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|a69c7259-5cc4-4207-8a64-47ec96c6c5b0 | underdog | Jaylen Waddle | Receiving Yards | under | 0.10317750601720066 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|d82bd3c6-2a60-4879-b845-18484787d341 | underdog | Blake Barnett | Pass Yards | under | 0.1031517391686223 | 2026-11-05T12:22:13Z | 2026-11-07T18:00:00Z |
| underdog|afa04e8f-d1f5-4384-a5d8-c3ffdfc746f4 | underdog | Kelby Valsin | Receiving Yards | under | 0.10288010512318424 | 2026-11-05T12:22:13Z | 2026-11-06T00:30:00Z |
| underdog|d9d08697-3dd2-4d24-bc73-42297b125227 | underdog | Jameson Williams | Receptions | under | 0.10208410937911938 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|7bf309d3-cb09-4113-b642-82526d074215 | underdog | Christian Watson | Receiving Yards | under | 0.10173017572558107 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|f4bba20a-76ec-4df5-9de0-3c7c20bd1a76 | underdog | Keon Coleman | Receptions | under | 0.10169343136994924 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|286912ed-323c-4195-8bb0-aae532cca8e5 | underdog | Michael Petro | FG Made | over | 0.10165952350252716 | 2026-11-04T12:10:41Z | 2026-11-06T00:30:00Z |
| underdog|24a49a3b-5f76-4977-9e37-fd6d51db08c2 | underdog | Jahmyr Gibbs | Rush Yards | under | 0.10154569505675504 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|23fa46de-8f35-4b86-b931-58c2c9be738f | underdog | Javonte Williams | Rush Yards | under | 0.10095549971421969 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|ebb77964-40c0-4665-83be-7d32ded07673 | underdog | Kyle Cunanan | XP Made | over | 0.10085105463048971 | 2026-11-05T12:22:13Z | 2026-11-07T01:00:00Z |
| underdog|6b56f67a-0cb3-4d32-aad1-5ebdb5004b45 | underdog | David Olano | XP Made | over | 0.10069986321094648 | 2026-11-05T12:22:13Z | 2026-11-07T20:00:00Z |
| underdog|e93d4601-6009-4fb8-a624-98b9dcc034f9 | underdog | Treylon Burks | Receiving Yards | under | 0.10064121250380376 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| prizepicks|16704458 | prizepicks | Maria Sakkari | Aces | under | 0.10028565424702363 | 2026-11-05T12:22:13Z | 2026-11-06T05:30:00.000-05:00 |
| underdog|4c0c83a7-22fc-43b3-9db9-d140c271a605 | underdog | Oronde Gadsden | Receptions | under | 0.10018871071931101 | 2026-11-05T12:22:13Z | 2026-11-08T21:05:00Z |
| underdog|d4a5094c-9736-4dde-95d2-0ea510ff3258 | underdog | Bijan Robinson | Rush Yards | under | 0.10013138750495743 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|381db12f-635c-43b4-898c-04b39c11f438 | underdog | Jamal Polite | Receptions | under | 0.1001216115286192 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|fd8e3565-4701-45c9-840c-5fc035e777ac | underdog | DeSean Bishop | Rush Yards | under | 0.09988529285895009 | 2026-11-05T12:22:13Z | 2026-11-07T23:15:00Z |
| underdog|ad219443-0404-4391-b1bf-2707df6b9de7 | underdog | Omarion Hampton | Receptions | over | 0.09981815938380334 | 2026-11-05T12:22:13Z | 2026-11-08T21:05:00Z |
| underdog|c06c5aac-29f9-4d72-9b5b-e1476303d8cd | underdog | Ryan Flournoy | Receiving Yards | under | 0.09981020004669383 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|54d1f64a-341e-4b14-9c54-93ead4e7667f | underdog | Saquon Barkley | Receiving Yards | under | 0.09931837820137668 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|76ae1508-2f42-4416-a35a-62d61a54ffff | underdog | Mike Washington | Rush Yards | under | 0.09929350923839264 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|e322429d-650a-4a9b-90ae-7c12e88c2be5 | underdog | David Olano | FG Made | over | 0.09919826629893125 | 2026-11-05T12:22:13Z | 2026-11-07T20:00:00Z |
| underdog|57f73ccb-63b1-451c-bbeb-fbaac3456b03 | underdog | Aaron Jones | Receptions | under | 0.09908473856146005 | 2026-11-05T12:22:13Z | 2026-11-10T01:15:00Z |
| underdog|b5d747fa-73cd-4acb-88a8-538cb0bc7051 | underdog | Jordan Addison | Receiving Yards | under | 0.098653067032206 | 2026-11-03T11:59:28Z | 2026-11-10T01:15:00Z |
| underdog|23189170-4b07-4efb-b4d6-4f54e4b31d79 | underdog | Christian McCaffrey | Receptions | under | 0.09862529752702964 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|be48005a-e911-48a5-89d3-0071ee0d1592 | underdog | Devon Dampier | Pass TDs | over | 0.09858639656620943 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|24324e94-375f-47e6-81b8-1367b471a178 | underdog | Juwan Johnson | Receptions | under | 0.09851839400207829 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|d1e744f7-e48f-432b-ac36-9994d2f0347b | underdog | Chuba Hubbard | Rush Yards | under | 0.09846599432023506 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| prizepicks|16685623 | prizepicks | D'Andre Swift | Rush TDs | over | 0.09831155568334193 | 2026-11-05T12:22:13Z | 2026-11-08T20:20:00.000-05:00 |
| underdog|bd2f0df8-0385-402d-b550-782b20315e95 | underdog | Tommy Carr | Pass Yards | under | 0.09795522264297585 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| prizepicks|16619747 | prizepicks | Jesse Legree | Recs | under | 0.09789260962625501 | 2026-11-04T12:10:41Z | 2026-11-07T22:30:00.000-05:00 |
| underdog|11c90112-0f72-4993-8f80-cfd19a4b9a48 | underdog | Marcel Reed | Pass TDs | over | 0.09776773307959336 | 2026-11-05T12:22:13Z | 2026-11-07T20:00:00Z |
| underdog|1337c674-49d5-46cf-939d-084150e82186 | underdog | Trey'Dez Green | Receptions | under | 0.09742503499893362 | 2026-11-05T12:22:13Z | 2026-11-07T20:30:00Z |
| prizepicks|16623390 | prizepicks | Kyle Pitts Sr. | Recs | under | 0.09724751553828881 | 2026-11-04T12:10:41Z | 2026-11-08T09:30:00.000-05:00 |
| underdog|dd95402c-e9ca-44e5-a5a3-179e2734707c | underdog | Jordan Addison | Receptions | under | 0.09707338503094809 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|777a6934-83da-4fc6-ae05-670614aac4c8 | underdog | Luther Burden | Receptions | under | 0.0970050304666229 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|b9011ea7-ea46-4c2b-b318-ad09d38e3d30 | underdog | Jaden Craig | Pass TDs | under | 0.09648102116025947 | 2026-11-05T12:22:13Z | 2026-11-07T03:15:00Z |
| underdog|8d1f8dab-3871-4b93-8ad4-f5badbe6b185 | underdog | Rachaad White | Receiving Yards | under | 0.09638605617776375 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| prizepicks|16623392 | prizepicks | Jahan Dotson | Recs | under | 0.09637295072919405 | 2026-11-04T12:10:41Z | 2026-11-08T09:30:00.000-05:00 |
| underdog|382dbb6b-8636-4f45-9336-4f48e41a9ec0 | underdog | Mark Fletcher Jr. | Rush Yards | under | 0.09637086124647443 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|2bac7b08-fac7-40ce-8ab4-52eed070b62a | underdog | Jordan Love | Pass TDs | under | 0.0961519218860859 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|0c57932e-0ffc-411c-bd91-b60cf90168b0 | underdog | Brandon Aubrey | Kicking Points | under | 0.09590964792109724 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|a02c87fe-f8cd-4593-b8f9-3c37dcab1bfd | underdog | Jake Bates | Kicking Points | under | 0.09584127441212353 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|78e5553f-26dc-4ce9-abca-9245000f86c3 | underdog | Polina Kudermetova | Double Faults | under | 0.09567949538698428 | 2026-11-05T12:22:13Z | 2026-11-06T09:30:00Z |
| underdog|70b674bf-14ef-4526-b90e-42cba3c6d3a5 | underdog | Adam Trautman | Receptions | under | 0.09545112973787573 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|29858a3a-b135-43e3-a433-f5286dccf11c | underdog | David Amador | Receptions | under | 0.0952030712910944 | 2026-11-05T12:22:13Z | 2026-11-06T00:30:00Z |
| underdog|f3df021b-e87e-4d22-a9e7-273fdfdebcdf | underdog | Charlie Woerner | Receptions | under | 0.09501160407184561 | 2026-11-05T12:22:13Z | 2026-11-08T14:30:00Z |
| underdog|a5eb6366-cd82-4d6b-bd95-f5e0ede614e0 | underdog | Ka'imi Fairbairn | Kicking Points | under | 0.09495465902987144 | 2026-11-03T02:21:46Z | 2026-11-08T21:05:00Z |
| underdog|e6a6d9c4-cede-4db1-8127-fadccb0830a1 | underdog | Parker Washington | Receptions | under | 0.09473178992722764 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|5305eb00-f865-44e1-b331-cdab51c593d9 | underdog | Sam Leavitt | Pass Yards | under | 0.09404552285320211 | 2026-11-05T12:22:13Z | 2026-11-07T20:30:00Z |
| underdog|c578d8d7-01f0-4d79-9d4f-3b0725511b5a | underdog | Legend Glasker | Receptions | under | 0.0939339008632083 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|06453bc8-3c32-4402-b79a-c09f64d23356 | underdog | Braden Atkinson | Pass TDs | under | 0.0938819023831381 | 2026-11-05T12:22:13Z | 2026-11-08T03:30:00Z |
| prizepicks|16685554 | prizepicks | Jared Goff | Pass TDs | under | 0.09280845049511621 | 2026-11-05T12:22:13Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|c8ccca2b-13b2-403a-bb00-b6f2284f88e4 | underdog | Kenneth Walker III | Rush + Rec Yards | under | 0.09278676109466322 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|5aba41cc-7e6c-464f-ba01-1503a4083ba6 | underdog | Cam Skattebo | Rush Yards | under | 0.09245259372443404 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|7cee03ac-78b3-4d7b-9754-834e5953a2f4 | underdog | Bryce Young | Rush Yards | under | 0.09215881426223937 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|641f366c-fc02-422d-94ef-532b420c9770 | underdog | Arch Manning | Pass Yards | under | 0.09190007823413737 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|3643f56d-0243-4332-a358-5a0e8e33a064 | underdog | Brendan Baird | FG Made | under | 0.09178178550541316 | 2026-11-04T12:10:41Z | 2026-11-07T00:00:00Z |
| underdog|93a92a80-a9c0-4066-901b-6e9bb3e6ed82 | underdog | Mateen Bhaghani | XP Made | over | 0.09160309321993065 | 2026-11-04T12:10:41Z | 2026-11-07T17:00:00Z |
| underdog|ae6c7719-9f5c-4983-b97f-e7e5228cddcd | underdog | Samaje Perine | Receiving Yards | over | 0.09128532626079078 | 2026-11-05T12:22:13Z | 2026-11-08T14:30:00Z |
| underdog|891e30f8-7158-4065-8c46-b0bc62da09ae | underdog | Nate Frazier | Rush Yards | under | 0.09112227092117486 | 2026-11-04T12:10:41Z | 2026-11-08T00:30:00Z |
| underdog|f9eddbe0-38b8-4913-b9a3-86f9f6cb2cda | underdog | Blake Corum | Rush Yards | under | 0.09068718633654116 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|bd4b0a59-3cf1-4e27-baa9-e6e999015754 | underdog | Yannick Smith | Receptions | under | 0.09048971514892568 | 2026-11-05T12:22:13Z | 2026-11-07T00:00:00Z |
| underdog|21d71ac4-4518-4c20-a927-ee93fc159f14 | underdog | Cameron Dickey | Rush Yards | under | 0.09045418368836045 | 2026-11-04T12:10:41Z | 2026-11-08T02:30:00Z |
| underdog|fb9ae694-461a-4753-afa7-28558c1516d0 | underdog | Camden Coleman | Pass Yards | under | 0.09043672317315898 | 2026-11-05T12:22:13Z | 2026-11-06T01:00:00Z |
| underdog|d52dc310-ea00-4c21-bb95-3798608a708f | underdog | Quentin Johnston | Receptions | under | 0.08995109550904856 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|cc8ff1c4-2fcb-4c4c-af18-4a127eb7feb3 | underdog | Leonard Farrow | Rush Yards | under | 0.0896959331352698 | 2026-11-04T12:10:41Z | 2026-11-06T00:30:00Z |
| underdog|191ad2e3-f555-4222-9200-863334e65430 | underdog | Keelon Russell | Pass TDs | over | 0.08967851076359068 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|30c2e39e-bf25-4ab7-8130-054ae15d2165 | underdog | Kimani Vidal | Rush Yards | under | 0.08934185310329501 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|c90518a9-3b7b-4a28-b1f8-edec396b50bb | underdog | Gavin Lahm | XP Made | under | 0.08887474946252161 | 2026-11-05T12:22:13Z | 2026-11-07T21:15:00Z |
| underdog|0d028507-619d-4a18-ab03-a71a586e4d6d | underdog | Derrick Henry | Rush Yards | under | 0.0887019263584169 | 2026-11-05T12:22:13Z | 2026-11-06T01:15:00Z |
| underdog|50f0cc28-915a-4dd2-ae88-cf03efcede73 | underdog | Caleb Douglas | Receiving Yards | under | 0.08861402690077047 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|27cb9670-5382-48df-ab83-f72399dbeeac | underdog | Travis Kelce | Receiving Yards | under | 0.08860625184263005 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|97528620-100f-4ff8-bdaf-28d77419865d | underdog | Savion Williams | Receiving Yards | under | 0.08856960710705053 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|3de9a574-245c-4174-a9a3-36f61f6c0d85 | underdog | Mario Sanders | Receiving Yards | under | 0.0881936984101791 | 2026-11-05T12:22:13Z | 2026-11-06T01:00:00Z |
| underdog|faf17d73-8e05-4b6e-bfe7-8bc21c81ee3b | underdog | Malik Nabers | Receiving Yards | under | 0.08807150028885424 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|47cec350-6d8d-442d-8a9d-7cb64d51ca35 | underdog | Nate Roberts | Receiving Yards | over | 0.08795420739677307 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|b722c0eb-24f9-4457-aca1-c570a4906039 | underdog | Chris Olave | Receiving Yards | under | 0.08783600387699941 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|8e5148e6-e9b7-4f81-8abb-ff57d91e4cd0 | underdog | Sione Vaki | Rush Yards | under | 0.08774010921056974 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|0c6aa873-f488-4691-92b1-807b07d325fc | underdog | Mekhi Anderson | Receptions | under | 0.08760565018567046 | 2026-11-05T12:22:13Z | 2026-11-06T00:30:00Z |
| underdog|c4f3253c-3c43-48da-989e-430a41e60938 | underdog | Ethan Grunkemeyer | Pass TDs | over | 0.08701299636099313 | 2026-11-04T12:10:41Z | 2026-11-07T00:00:00Z |
| underdog|85d0f744-992b-44c1-8a7c-101d9724dfdc | underdog | Bucky Irving | Receiving Yards | under | 0.08678510565293707 | 2026-11-05T12:22:13Z | 2026-11-09T01:20:00Z |
| underdog|12a2d911-b12a-443c-8611-c6a04a06c827 | underdog | Keenan Allen | Receptions | under | 0.08657096839321532 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|4d325428-7592-41b0-a7ae-2d3bd6cbed54 | underdog | Brad Jackson | Pass Yards | under | 0.08655808932745823 | 2026-11-05T12:22:13Z | 2026-11-08T03:30:00Z |
| underdog|d841a892-a21f-46e6-bc65-e0c20662a38e | underdog | Travis Hunter | Receptions | over | 0.08655057759181062 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|427822f7-2e93-4e7a-8b27-7d7d73610e48 | underdog | TreyShun Hurry | Receiving Yards | under | 0.08650477450845984 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|de0e129b-50fb-4ad3-af58-61dedd2d5451 | underdog | Tetairoa McMillan | Receiving Yards | under | 0.08645743049382315 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|30d142c6-8017-4e94-b781-4eb760e26d96 | underdog | Evan McPherson | Kicking Points | under | 0.08624660748610669 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|9aab6d7f-49c3-4795-bd3f-ed7713dea93a | underdog | Chig Okonkwo | Receiving Yards | under | 0.08579655598831837 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|a97deb63-dca1-44ac-8812-af3d07f16bb7 | underdog | Jamal Roberts | Receiving Yards | over | 0.08558559107633923 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|771df1cb-a4e1-4db3-a22c-43a4bb5f2de5 | underdog | Isaiah West | Rush Yards | under | 0.08496689908690391 | 2026-11-05T12:22:13Z | 2026-11-07T20:30:00Z |
| underdog|9a11ea53-966f-452f-a1c2-ab1154cc943e | underdog | Jalen Coker | Receptions | under | 0.08455880625865009 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|ba34356a-c5a8-4f07-9671-c83995982867 | underdog | J.J. McCarthy | Rush Yards | under | 0.08453068040593992 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|a8b4d56b-3190-4729-a3e3-fa4952f7fe19 | underdog | Malachi Fields | Receptions | under | 0.08444567676815706 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|168b1bbc-71d2-4735-8ceb-c776ca885988 | underdog | Derrick Henry | Rush + Rec Yards | under | 0.08436577171555504 | 2026-11-05T12:22:13Z | 2026-11-06T01:15:00Z |
| underdog|82404d76-19b0-4744-8dfc-f7f2fd7987a3 | underdog | Chris Dawn | Receiving Yards | under | 0.08426691261711605 | 2026-11-05T12:22:13Z | 2026-11-08T03:30:00Z |
| underdog|fca3da4f-9476-4b17-ad79-8f80aef153b9 | underdog | Elina Svitolina | Double Faults | under | 0.08423149243173988 | 2026-11-05T12:22:13Z | 2026-11-09T21:10:00Z |
| underdog|a459485a-7a31-48df-9e88-9165908577c0 | underdog | Jalen Coker | Receiving Yards | under | 0.08405630218891369 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|3716c38e-c313-439c-8c4e-db38996e9297 | underdog | Liam Boyd | FG Made | under | 0.08392246570987505 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|1cf10def-da38-4ff8-ae2b-ed870438b843 | underdog | Drew Sample | Receptions | over | 0.0839013767051019 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|d75b9cd4-be57-4ea5-90e6-66b407f1e96b | underdog | Gavin Freeman | Receiving Yards | under | 0.08368894661308302 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|de3a28c0-990e-45e6-b955-eb21bc4ad9a4 | underdog | Patrick Mahomes | Rush Yards | under | 0.08365133891580678 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|ae467ddf-c18e-44ab-997b-025c17ee41ce | underdog | Noah Gray | Receiving Yards | over | 0.08365016561241356 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|d2a2884a-9482-4454-8f62-b11b25cf9301 | underdog | AJ Barner | Receiving Yards | under | 0.08315373110424162 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|4e7cab7c-a9a4-4533-ae0e-b7d96c3d425b | underdog | Jack Bech | Receptions | under | 0.08300134151445937 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|89634d56-a423-40d0-a5c7-22df4d7069ec | underdog | Eric Olsen | Receptions | under | 0.08296120253641759 | 2026-11-05T12:22:13Z | 2026-11-08T03:30:00Z |
| underdog|bef17621-f7f3-4d07-924b-e623b34c8d46 | underdog | Michael Salgado-Medina | FG Made | over | 0.08281383712782858 | 2026-11-04T12:10:41Z | 2026-11-07T03:15:00Z |
| underdog|e0ced813-8b2c-4455-b57b-71da99a39e7d | underdog | Blake Corum | Rush + Rec Yards | under | 0.0827040556047397 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|db8a215c-a32b-461f-a74f-392bfed6cd47 | underdog | Sam LaPorta | Receptions | under | 0.08195280346786493 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|1b223689-eebc-43e2-a902-52c225dd98f4 | underdog | Cyrus Allen | Receiving Yards | under | 0.08178866252619377 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|0767ecdc-6c88-403c-a631-567d0902ae5f | underdog | Bijan Robinson | Receptions | under | 0.08140314785642488 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|30c987cb-9450-418a-b4ff-d450e9c0183f | underdog | Ashton Jeanty | Receptions | under | 0.08123630317472041 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|3f37b916-250a-4972-965b-ecb6efeb0ce3 | underdog | Chris Bell | Receiving Yards | under | 0.08090076495058063 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|ff5d6072-bfd1-4111-b890-2b71997773ff | underdog | Josh Cuevas | Receptions | under | 0.08055246374706548 | 2026-11-05T12:22:13Z | 2026-11-06T01:15:00Z |
| underdog|a93191dc-5ab3-4d60-9b3c-0635b721460f | underdog | Baker Mayfield | Rush Yards | under | 0.0804542415617544 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|12bd4374-687f-4ccd-8483-775c124afda4 | underdog | Khalil Shakir | Receptions | under | 0.08011792675984464 | 2026-11-04T12:10:41Z | 2026-11-10T01:15:00Z |
| underdog|d64d6002-cbe6-4802-b5c1-a7cdd75e4898 | underdog | Blake Corum | Receiving Yards | over | 0.07956662715644236 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|a313aef7-90e0-4414-8c8e-e66290d3ad2b | underdog | James Cook | Rush Yards | under | 0.0794670395584336 | 2026-11-04T12:10:41Z | 2026-11-10T01:15:00Z |
| underdog|a2f8424e-28d4-487d-9875-bae9673e09e0 | underdog | Dylan Raiola | Pass TDs | under | 0.0793130185765103 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|18422288-44f7-431d-82a8-cf114d5022be | underdog | Carson Hilbert | FG Made | under | 0.07929489595444217 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|a57c34c5-0685-4573-826a-2780a1571932 | underdog | Kyren Williams | Rush + Rec Yards | under | 0.07885524524463117 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|8e108182-4c87-46e4-9018-ab3d52427b04 | underdog | Brian Thomas | Receptions | over | 0.07859887169586088 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|cbd6fe24-f6ed-44fb-9f60-0d162af5a52b | underdog | Easton Messer | Receiving Yards | under | 0.078482351350454 | 2026-11-05T12:22:13Z | 2026-11-06T00:30:00Z |
| underdog|b26c659b-559e-4818-854d-5118f2c3403c | underdog | Ed Small | Receptions | over | 0.07823065203309115 | 2026-11-04T12:10:41Z | 2026-11-07T03:15:00Z |
| underdog|62465cef-4749-4f24-a49e-a2d29fb6d9af | underdog | Jaron Tibbs | Receiving Yards | under | 0.07704359216338097 | 2026-11-05T12:22:13Z | 2026-11-07T18:00:00Z |
| underdog|273b4f1f-bf42-4a41-a69b-e9b2f4dd10f1 | underdog | Reggie Virgil | Receiving Yards | under | 0.07701412532993002 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|9cc6d7af-582b-4a55-b998-6d8b9a90cae1 | underdog | Trevor Lawrence | Pass TDs | under | 0.07694789832016491 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|99f3ae4b-6e3f-48d9-a87c-1281715f1b43 | underdog | Nolan James | Rush Yards | under | 0.0769268807412854 | 2026-11-03T02:21:46Z | 2026-11-08T00:30:00Z |
| underdog|374f597e-854d-4418-8329-9618f7343eaa | underdog | Michael Petro | XP Made | under | 0.07677360225334395 | 2026-11-04T12:10:41Z | 2026-11-06T00:30:00Z |
| underdog|178f08bc-b24b-44cb-8e32-0c49a45abb6e | underdog | AJ Surace | Pass TDs | over | 0.07667779004543462 | 2026-11-05T12:22:13Z | 2026-11-07T21:15:00Z |
| underdog|b037dd4d-81a9-4275-bf43-602a7252c49e | underdog | George Pickens | Receptions | under | 0.0766522668294094 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| prizepicks|16566879 | prizepicks | Drake London | Recs | under | 0.07645666700581077 | 2026-11-04T12:10:41Z | 2026-11-08T09:30:00.000-05:00 |
| prizepicks|16578153 | prizepicks | Bhayshul Tuten | Rec Targets | under | 0.07632106872332856 | 2026-11-03T02:21:46Z | 2026-11-05T20:15:00.000-05:00 |
| underdog|0922f90a-0901-4f10-a983-e4aa2c121442 | underdog | Gianni Spetic | FG Made | over | 0.07604097650812291 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|b0f90105-2991-41ea-bc6c-2264f297449b | underdog | Nate Boerkircher | Receptions | under | 0.07569655692539734 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|d1462d19-7a87-4f00-8195-3e0280a9658a | underdog | Rashod Bateman | Receiving Yards | over | 0.07523439898983075 | 2026-11-05T12:22:13Z | 2026-11-06T01:15:00Z |
| underdog|3db483c9-2cbd-4a61-a415-da9945e7783b | underdog | J'Koby Williams | Rush Yards | under | 0.0751641814121301 | 2026-11-04T12:10:41Z | 2026-11-08T02:30:00Z |
| underdog|c9f42cb3-782a-42ae-8d36-b838a2e16e5b | underdog | Tyler Goodson | Receptions | under | 0.07447307028831152 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|f7c17ddd-b7da-47e1-b7cc-3c831055be6b | underdog | Dominic Zvada | FG Made | under | 0.0741063683238431 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|63562270-b0a9-458b-9e26-274956838599 | underdog | Jalen Hale | Receptions | over | 0.07399445228452806 | 2026-11-05T12:22:13Z | 2026-11-07T00:00:00Z |
| underdog|ae08266e-6845-4eb5-8ae0-c55a994092c7 | underdog | Dylan Raiola | Pass Yards | under | 0.07375588900233532 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|bc765a50-b954-4613-82ce-93029d04d412 | underdog | Aiden Flora | Receiving Yards | over | 0.07359553190708512 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|5571a9d9-5257-413c-94f7-b30035400e37 | underdog | Evan Engram | Receiving Yards | under | 0.07358911959876246 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|a06d5616-3ce4-4197-850d-f0b0c73b34d5 | underdog | Drake Maye | Rush Yards | under | 0.0735599469387288 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| prizepicks|16576406 | prizepicks | Kyren Williams | Rush Yards | under | 0.0734640730790519 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|98370739-8ce7-4116-9352-2a9e7a795fa3 | underdog | C.J. Stroud | Pass TDs | under | 0.07344784426946727 | 2026-11-03T02:21:46Z | 2026-11-08T21:05:00Z |
| underdog|38800c60-ebd7-4479-9aff-c1e3afe469bb | underdog | Tyler Allgeier | Rush Yards | under | 0.07335598227990359 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|f7413d7e-001a-4315-8bef-ee5b8c474c0d | underdog | Keelon Russell | Pass Yards | under | 0.07313844310922835 | 2026-11-05T12:22:13Z | 2026-11-07T20:30:00Z |
| underdog|126188b0-7b25-4684-b82a-c40972332c2b | underdog | Gunner Stockton | Pass Yards | under | 0.07289838569890572 | 2026-11-04T12:10:41Z | 2026-11-08T00:30:00Z |
| underdog|d45e253c-f252-4509-a696-99b545feffe9 | underdog | Gianni Spetic | XP Made | over | 0.07268509835321124 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|5c589e9f-50cb-4f4d-bc6c-31a94652a555 | underdog | Darren Waller | Receptions | under | 0.07257323185856346 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| prizepicks|16704459 | prizepicks | Maria Sakkari | Double Faults | under | 0.0724425765843496 | 2026-11-05T12:22:13Z | 2026-11-06T05:30:00.000-05:00 |
| underdog|1adc0acb-33e0-4c49-8afc-9b6c4b1a14fd | underdog | Derrick Henry | Receptions | under | 0.07220955982843835 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|5decb5a9-f1ab-48b5-bdf2-ec7cff2a45da | underdog | Dominic Zvada | Kicking Points | under | 0.07189248960202987 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|1914f4a9-93a4-410c-928a-0e45a89f9e0a | underdog | Jadon Porter | Receiving Yards | over | 0.07181632856109332 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|8e5ead28-4c4c-4948-979d-a8ab4eac277d | underdog | Tyler Allgeier | Rush + Rec Yards | under | 0.07169855906591827 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|0b0ff05a-c487-4d3f-905d-e95f4a83ca3a | underdog | Nate McCashland | FG Made | over | 0.07120946541515932 | 2026-11-05T12:22:13Z | 2026-11-07T03:15:00Z |
| underdog|82a0c739-4fe5-4f9c-ab98-3f993aa6a3a8 | underdog | Blake Corum | Receptions | under | 0.07120017552093771 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|8f0250ed-dbb2-49a7-8dab-019bc7fb9cec | underdog | Aidan Chiles | Pass TDs | over | 0.07091925513129682 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|32412c4f-01cc-4cce-9b84-a65cdd858a85 | underdog | Jamal Rule | Rush Yards | under | 0.07079654381437117 | 2026-11-05T12:22:13Z | 2026-11-07T01:00:00Z |
| underdog|01068677-aea6-428e-b880-63933e5e7c56 | underdog | Kwazi Gilmer | Receptions | under | 0.07076791839692675 | 2026-11-04T12:10:41Z | 2026-11-07T01:00:00Z |
| underdog|7bff2e43-ab12-4a98-b7e5-04d0c0bbf914 | underdog | Mike Washington | Receptions | under | 0.07071209556400804 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|1f1d13a1-afea-41e0-842f-8af4981136b9 | underdog | Kenneth Walker III | Rush Yards | under | 0.0706968503684764 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|1f8aad36-740c-4ed3-89c7-2156ee173e1e | underdog | Isaiah Likely | Receiving Yards | under | 0.07068676575263688 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|555d44e8-8a5e-4431-a64a-05813ba16c93 | underdog | Xavier Williams | Rush Yards | under | 0.07057992950020597 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|d1cbb3da-3a91-40ba-bdec-e8d68a069937 | underdog | Luke Dehnicke | Receptions | under | 0.07046274395456875 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|dc7085a5-bd2b-4e90-9aa5-7e11f5f57193 | underdog | Dohnte Meyers | Receptions | under | 0.07018273167311495 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|2e941ef0-d7f5-4f4c-8018-abecc0ca312c | underdog | Nate Boerkircher | Receiving Yards | over | 0.07009713968929643 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|9cac1640-ca39-4f1b-931a-e2c850308466 | underdog | Noah Gray | Receptions | over | 0.06995762914057951 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|653afc15-7559-442b-b34d-1f0091847e3b | underdog | Chase Brown | Receptions | under | 0.06992427729238937 | 2026-11-05T12:22:13Z | 2026-11-08T14:30:00Z |
| underdog|4f42e71e-9977-4467-9c6f-587a1fb01921 | underdog | Malik Willis | Pass TDs | under | 0.0698898131874599 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|a8b07aaf-9e96-48ee-8ca1-37bcc89b9eb4 | underdog | Jackson Kleather | XP Made | over | 0.06961802625005475 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|645d1e24-ea6b-4524-966f-4ad8a9808469 | underdog | DaSaahn Brame | Receptions | under | 0.06953393528194685 | 2026-11-05T12:22:13Z | 2026-11-07T23:15:00Z |
| underdog|bd8faee7-5c2b-4852-b7fb-5e270f687f55 | underdog | Tee Higgins | Receiving Yards | under | 0.06937703329058331 | 2026-11-05T12:22:13Z | 2026-11-08T14:30:00Z |
| prizepicks|16576408 | prizepicks | Javonte Williams | Rush Yards | under | 0.06913799764143458 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|7e747515-989f-4a5d-aa99-13f10fe69a0d | underdog | DJ Allen | Receptions | over | 0.06890970101657368 | 2026-11-05T12:22:13Z | 2026-11-06T00:30:00Z |
| underdog|7d1040e5-04ee-4e25-8fbf-f12f99828e9e | underdog | Cam Skattebo | Receptions | under | 0.06884453220929898 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|f9fe24e6-dd92-40f6-a6d8-49347d9716b3 | underdog | Tylik Hill | Rush Yards | over | 0.0687067760591078 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|1676285c-b66c-440c-ba94-3e1e1dd2226c | underdog | Jesse Legree | Receiving Yards | under | 0.06868793139917972 | 2026-11-05T12:22:13Z | 2026-11-08T03:30:00Z |
| prizepicks|16683643 | prizepicks | Jake Bates | Kicking Points | under | 0.06818662504942608 | 2026-11-05T12:22:13Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|90c3977f-8381-4a61-9dbd-94f49ffcf439 | underdog | Drew Sample | Receiving Yards | over | 0.0679032038021633 | 2026-11-05T12:22:13Z | 2026-11-08T14:30:00Z |
| underdog|b8c47a57-f800-4f0c-885f-f5ff1d8c731a | underdog | Trevor Lawrence | Rush Yards | under | 0.06787768680871364 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|a41d4208-558b-4e9e-ace0-423efa6d914f | underdog | Brendan Baird | XP Made | under | 0.06786423255342389 | 2026-11-04T12:10:41Z | 2026-11-07T00:00:00Z |
| underdog|b479ca9d-4d1c-454f-bfff-733cb2735065 | underdog | Jason Myers | Kicking Points | under | 0.06786338640966882 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|aa2400e1-61c6-42b8-a00e-4df185d8e29a | underdog | Peyton Woodring | XP Made | over | 0.06770360800211805 | 2026-11-04T12:10:41Z | 2026-11-08T00:30:00Z |
| underdog|b4a11205-f19f-4256-9e1e-6703e6a4644a | underdog | Jaylen Waddle | Receptions | under | 0.06756067788820463 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|e1167eac-c3e7-496f-842c-3278288780c6 | underdog | Omarion Hampton | Receiving Yards | over | 0.06732794012007637 | 2026-11-05T12:22:13Z | 2026-11-08T21:05:00Z |
| underdog|d2d0c7f6-8c34-47ab-83c4-c4cc40e11773 | underdog | Elijah Moore | Receptions | over | 0.06688940577179958 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| prizepicks|16700131 | prizepicks | Bianca Andreescu | Total Games | over | 0.06662320386382004 | 2026-11-05T12:22:13Z | 2026-11-05T14:00:00.000-05:00 |
| underdog|480b8a53-750b-4531-914d-b24d9cc3be67 | underdog | Gunner Stockton | Pass TDs | over | 0.06653840324761084 | 2026-11-04T12:10:41Z | 2026-11-08T00:30:00Z |
| underdog|67a2d02f-4c71-4e31-a4a2-f05031800c7b | underdog | AJ Wilson | Receptions | under | 0.06628411280953905 | 2026-11-05T12:22:13Z | 2026-11-06T00:30:00Z |
| underdog|d4f2b5ca-0b3f-4658-962d-e49d13b62596 | underdog | Mike Gesicki | Receptions | under | 0.06624716319361124 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|fc8a7d1c-fc88-48bd-9122-4cea2b71c647 | underdog | Xavier Hutchinson | Receptions | under | 0.06623799366444505 | 2026-11-05T12:22:13Z | 2026-11-08T21:05:00Z |
| underdog|23d0cc4b-98bb-4088-a807-e58efa7a08e7 | underdog | Caleb Cunningham | Receiving Yards | over | 0.06618295356151871 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|899c3bf4-8fd1-439d-998f-28a39c557ea3 | underdog | Jared Curtis | Pass TDs | under | 0.06614423452531004 | 2026-11-05T12:22:13Z | 2026-11-07T21:15:00Z |
| underdog|17d196b6-916b-4467-86c8-3e43337d1b9d | underdog | Josh Jacobs | Receiving Yards | under | 0.06580018595374104 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|e2076474-ba9e-4c4a-8a5e-8756583f0c4e | underdog | Woody Marks | Receiving Yards | under | 0.06554944061032464 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|61aa57cd-da96-4e0c-9d49-c178e588cdbf | underdog | Easton Messer | Receptions | under | 0.06524656774781878 | 2026-11-05T12:22:13Z | 2026-11-06T00:30:00Z |
| prizepicks|16629444 | prizepicks | Wayne Knight | Rush Atts | under | 0.06520056369225546 | 2026-11-05T12:22:13Z | 2026-11-07T12:00:00.000-05:00 |
| underdog|1730d324-21b9-4287-9ce7-7f49a1ead0df | underdog | Lincoln Kienholz | Pass Yards | under | 0.06499509554963379 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|f89d903a-bd78-4938-a9b8-bfc8c1768685 | underdog | Que'Sean Brown | Receptions | under | 0.06494340682637201 | 2026-11-05T12:22:13Z | 2026-11-07T00:00:00Z |
| underdog|ad36e65d-c7a8-4a0e-8d4c-a2b596d93edb | underdog | Cameron Dicker | Kicking Points | under | 0.06479235639855563 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|b13bd436-9bc2-4867-9041-17de5aa4b928 | underdog | Michael Wilson | Receiving Yards | under | 0.06474486073770425 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|1466368e-c6ce-4de6-8814-1a5e1d544d1d | underdog | Spencer Porath | FG Made | under | 0.06463882026125989 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|e00a37ed-d410-4482-ad2c-a051ecd9d5f1 | underdog | Jeffrey Overton | Receiving Yards | over | 0.06457901851406311 | 2026-11-04T12:10:41Z | 2026-11-07T00:00:00Z |
| underdog|1e146d1e-95ac-4e18-b97f-874278e4440b | underdog | Emmett Johnson | Rush Yards | under | 0.06444132725080376 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|78f9483b-dd36-4ca4-8e6b-d362bb4eb49a | underdog | Aidan Chiles | Pass Yards | under | 0.06435632861852159 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|836deb6a-d2c7-47dd-9ab2-df7843607601 | underdog | Kalieb Osborne | Pass Yards | under | 0.06425760515239431 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|373f4976-2946-4808-996d-0e08da020130 | underdog | Ashton Daniels | Pass Yards | under | 0.06380997745165684 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|e5598605-b771-40d4-a896-945151550af7 | underdog | JC French | Pass Yards | under | 0.0637897607221598 | 2026-11-05T12:22:13Z | 2026-11-07T20:30:00Z |
| underdog|c9cba434-16a2-44a1-acf3-d92dc9f828a5 | underdog | Ja'Kobi Lane | Receiving Yards | under | 0.06358680985081022 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|8ece24e0-b2e4-4fa3-b6b4-5845b58f2de9 | underdog | Kenny Minchey | Pass Yards | under | 0.06358679107944964 | 2026-11-05T12:22:13Z | 2026-11-07T23:15:00Z |
| underdog|21931440-adec-46d4-b530-994878d9e427 | underdog | T.J. Hockenson | Receptions | under | 0.06344057443403939 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|9e4ac678-53eb-48dd-9eb6-5829262bab83 | underdog | Bear Bachmeier | Pass Yards | under | 0.06313209167616829 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|20e2d065-8b33-44d8-b704-2f53c8db5429 | underdog | DJ Epps | Receiving Yards | over | 0.06272142066281527 | 2026-11-05T12:22:13Z | 2026-11-08T02:30:00Z |
| underdog|a7347881-8e1d-40cc-b5a6-fc23b791b44c | underdog | Rashod Bateman | Receptions | over | 0.06228976648419543 | 2026-11-05T12:22:13Z | 2026-11-06T01:15:00Z |
| prizepicks|16567865 | prizepicks | Michael Penix Jr. | Pass TDs | under | 0.06194406494725502 | 2026-11-05T12:22:13Z | 2026-11-08T09:30:00.000-05:00 |
| underdog|dccb9e1d-9636-4376-b377-bd2b72f840dd | underdog | Isaac Wilson | Pass Yards | under | 0.061444589147963136 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|94533c8c-852b-436b-8c3e-30871f71ee63 | underdog | Devin McCuin | Receptions | over | 0.061271839861702426 | 2026-11-05T12:22:13Z | 2026-11-07T20:30:00Z |
| underdog|13479cee-4641-48e8-9f1b-b2b908f4847c | underdog | LaNorris Sellers | Pass TDs | under | 0.0610733782804056 | 2026-11-05T12:22:13Z | 2026-11-07T20:00:00Z |
| underdog|8c265bcd-7b60-4798-8607-03c1259a21e4 | underdog | Trey Smack | FG Made | under | 0.06104007152947344 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|fac4af10-165a-4177-944e-51ad9c5660f6 | underdog | Matt Gay | FG Made | over | 0.06076705695301998 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|07cbccc8-0fba-4542-8414-c5920607d6bf | underdog | Kevin Jennings | Pass Yards | under | 0.06069823598347823 | 2026-11-04T12:10:41Z | 2026-11-07T00:00:00Z |
| underdog|b0a240d5-44af-42ff-a812-2f1b16380d9b | underdog | Nyziah Hunter | Receptions | under | 0.06044397243255828 | 2026-11-05T12:22:13Z | 2026-11-07T01:00:00Z |
| underdog|d29599ad-f597-4f28-9d87-acf1c29a3761 | underdog | Elijah Higgins | Receptions | under | 0.060018765343776814 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|be36f808-dbd3-4226-adee-a8537113a1e5 | underdog | Ethan Grunkemeyer | Pass Yards | under | 0.05966040798874328 | 2026-11-04T12:10:41Z | 2026-11-07T00:00:00Z |
| underdog|d0960391-8a29-49e1-adce-9b8b9a13efe6 | underdog | Kimani Vidal | Receptions | under | 0.0595189274468374 | 2026-11-05T12:22:13Z | 2026-11-08T21:05:00Z |
| underdog|1d902e2b-3919-4c19-b84a-8ffa99b10e62 | underdog | Brenton Strange | Receptions | under | 0.05946848028138785 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|78f92e19-5c31-4d49-a704-dea3e1ea7994 | underdog | Foster Moreau | Receptions | over | 0.05932154173705445 | 2026-11-05T12:22:13Z | 2026-11-08T21:05:00Z |
| underdog|fe4d076e-daf4-4620-a5d9-81c9dcde46d9 | underdog | Mark Andrews | Receptions | under | 0.059115555543941656 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|3b554414-84d2-41b4-93ac-fceb51bfce89 | underdog | Dilin Jones | Receptions | under | 0.05910993829171962 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|41f2b902-44c6-48b4-9eee-82534c0b54f4 | underdog | Justice Hill | Rush + Rec Yards | under | 0.0590474598746793 | 2026-11-04T12:10:41Z | 2026-11-06T01:15:00Z |
| underdog|a10e90f9-892e-489b-87e7-98258489a4ec | underdog | Chig Okonkwo | Receptions | under | 0.05901702938378406 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|5f83ba00-76c5-472d-91b8-5490a16ef0d6 | underdog | Anthony Colandrea | Pass TDs | over | 0.05889302378542982 | 2026-11-05T12:22:13Z | 2026-11-07T01:00:00Z |
| underdog|464fbf32-ce38-4c8f-bc70-190cf5d64c92 | underdog | MarShawn Lloyd | Receptions | under | 0.05868983465783262 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|285dab5f-ea1a-4d60-a385-159091689a27 | underdog | Savion Williams | Receptions | under | 0.058569519420755056 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|5c1dad6e-619c-4575-9b10-738e17d39df7 | underdog | Ashton Jeanty | Receiving Yards | under | 0.05850227908119554 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|d146dfb3-fcb5-4654-a1f6-64215170adeb | underdog | Jessica Pegula | Double Faults | under | 0.05846688292835567 | 2026-11-05T12:22:13Z | 2026-11-08T21:10:00Z |
| underdog|afda48e8-0d61-4673-aecd-d18deb0ca8b9 | underdog | Ed Small | Receiving Yards | over | 0.05839356214069036 | 2026-11-04T12:10:41Z | 2026-11-07T03:15:00Z |
| underdog|082a1ca6-ce1d-4690-8ec9-9b8d07894a90 | underdog | Josh Downs | Receiving Yards | under | 0.05836821075814247 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|097f1c9d-9fd7-4c66-b024-b6f792a6ddbe | underdog | Raleek Brown | Rush Yards | under | 0.05828535641008248 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|f6a0cb16-5759-468b-93f6-772a13d42630 | underdog | Marvin Mims Jr. | Receiving Yards | under | 0.05807117435666043 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|cc8d9cae-e2d7-46b3-b82e-af84fe68c16d | underdog | Beau Sparks | Receiving Yards | under | 0.058018388049906444 | 2026-11-05T12:22:13Z | 2026-11-08T03:30:00Z |
| underdog|089ce83f-49f9-46ad-83c1-06b27856f11e | underdog | Tyler Shough | Pass TDs | under | 0.0579713928349842 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|c7f223f5-1db6-4b90-9fbb-b219544bd20b | underdog | Jaleel Skinner | Receiving Yards | over | 0.0579671544436442 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|9dae6194-3778-427b-aa64-184da5cacda0 | underdog | Cornell Hatcher | Rush Yards | under | 0.057928275348360314 | 2026-11-05T12:22:13Z | 2026-11-08T03:30:00Z |
| underdog|0cbe8572-f373-40c7-bc91-3896efd0ba18 | underdog | Evan Stewart | Receiving Yards | over | 0.05781868428032133 | 2026-11-05T12:22:13Z | 2026-11-07T20:30:00Z |
| underdog|ef93512e-7037-4e52-adab-e5a0e92cb14b | underdog | Kyler Kasper | Receptions | under | 0.0577929902830534 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| prizepicks|16685553 | prizepicks | Malik Willis | Pass TDs | under | 0.05774292119343538 | 2026-11-05T12:22:13Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|03683cb5-d08b-46d2-8daf-b7a187b04861 | underdog | Collin Dixon | Receiving Yards | under | 0.05774001382855143 | 2026-11-04T12:10:41Z | 2026-11-07T01:00:00Z |
| underdog|363f2a86-aea7-488d-8f25-6c2926e28588 | underdog | Michael Penix | Pass TDs | under | 0.05769866616807584 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|6cea53c4-9d13-4b3e-8f35-09016359467a | underdog | Katin Houser | Pass TDs | over | 0.05741840076591065 | 2026-11-04T12:10:41Z | 2026-11-07T01:00:00Z |
| underdog|4ed6c534-a882-4037-a5c5-3d3c36ee0467 | underdog | Jordan Faison | Receiving Yards | under | 0.05721438415905 | 2026-11-03T02:21:46Z | 2026-11-08T00:30:00Z |
| underdog|82215f35-d978-41ed-b4b6-3e1171e32afc | underdog | Austin Simmons | Pass TDs | under | 0.05701792055392729 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|623fe967-1a3e-408f-b0cb-0bf7da802b8a | underdog | Dak Prescott | Rush Yards | over | 0.0570102313442149 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|b094236c-ba86-4187-9f50-dfd372652b8b | underdog | Tre Tucker | Receptions | under | 0.05656143515129497 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| prizepicks|16577046 | prizepicks | CeeDee Lamb | Rec Yards | under | 0.0563405843653354 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| prizepicks|16623321 | prizepicks | Isaiah Mizell | Recs | under | 0.05613807100115675 | 2026-11-04T12:10:41Z | 2026-11-06T22:15:00.000-05:00 |
| underdog|72424239-3938-4c03-a39e-4cf5eebc76fd | underdog | Ashton Daniels | Rush Yards | under | 0.05590103432432425 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|e5503b49-7874-4785-b938-ac08739aa23c | underdog | Billy Edwards Jr. | Pass TDs | under | 0.055860973923938406 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|48603add-d136-41df-b578-2323b8a1caa7 | underdog | Rome Odunze | Receptions | under | 0.05570918963942184 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|3c4aee76-fb32-4603-82d0-81351387b1e1 | underdog | Kalif Raymond | Receptions | under | 0.05532157679971539 | 2026-11-05T12:22:13Z | 2026-11-09T01:20:00Z |
| underdog|a31317ee-e954-402a-9e50-4a55ffc781d1 | underdog | Jaylen Raynor | Pass TDs | under | 0.0548056389593522 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|844d8994-eb1a-4135-917e-a68c00abf5fd | underdog | Tre' Harris | Receptions | under | 0.05470210954117727 | 2026-11-05T12:22:13Z | 2026-11-08T21:05:00Z |
| underdog|e2c22ff1-6209-4e3e-bbac-653eba1f1994 | underdog | Wayshawn Parker | Receiving Yards | over | 0.05434117214846301 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|e5de3304-8e95-4124-954c-9ff251883bab | underdog | Kenny Minchey | Rush Yards | over | 0.05425628323804066 | 2026-11-05T12:22:13Z | 2026-11-07T23:15:00Z |
| underdog|a90c4033-4dc0-4bff-8788-579fa5420077 | underdog | Treylon Burks | Receptions | under | 0.05419147947818659 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|cce8999b-73b6-4a3b-a40d-76aad63c8cba | underdog | Drake Lindsey | Pass Yards | under | 0.05406000313128101 | 2026-11-04T12:10:41Z | 2026-11-07T17:00:00Z |
| underdog|1c2cde05-b6d7-4474-9d9e-8f9b3062e070 | underdog | Puka Nacua | Receptions | under | 0.05380728482585917 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|e01ed5ff-4bf0-4328-80bb-372c2a56d1cb | underdog | Jeremiah Smith | Receptions | under | 0.053719870131973324 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|a0103c1b-46a3-4e96-a03e-ab9465f59573 | underdog | Arik Armstead | Sacks | under | 0.05366854242936148 | 2026-11-05T12:22:13Z | 2026-11-06T01:15:00Z |
| underdog|2f6615ec-e303-4723-8de9-515407930761 | underdog | Kedrick Reescano | Rush Yards | under | 0.05350218820934205 | 2026-11-04T12:10:41Z | 2026-11-07T03:15:00Z |
| underdog|71d9b967-8695-476c-a378-0a790c548319 | underdog | Nyziah Hunter | Receiving Yards | under | 0.053407546528774996 | 2026-11-04T12:10:41Z | 2026-11-07T01:00:00Z |
| underdog|e55382b2-c395-46d4-8518-8309c9d2f8e4 | underdog | JC French | Rush Yards | over | 0.053385662154178726 | 2026-11-05T12:22:13Z | 2026-11-07T20:30:00Z |
| underdog|97889cee-bb36-4d05-b351-a674927b93e5 | underdog | Braylon Staley | Receiving Yards | under | 0.053369351238770846 | 2026-11-05T12:22:13Z | 2026-11-07T23:15:00Z |
| underdog|6096a1da-ac09-4e48-a5c3-073489c51cf3 | underdog | Trey Hendrickson | Sacks | over | 0.05329708818405582 | 2026-11-05T12:22:13Z | 2026-11-06T01:15:00Z |
| underdog|1f6ec128-0f98-4fab-b889-6fa33628a38b | underdog | Reggie Virgil | Receptions | under | 0.053005643668652125 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|c56012e4-30e8-4196-bad4-730dcf525d19 | underdog | Ja'Kobi Lane | Receptions | under | 0.05292315297453021 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|27464760-8c59-4037-b749-3733f4a504cd | underdog | J.K. Dobbins | Receiving Yards | over | 0.052791170452059166 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|64461b17-4f11-42f0-b391-880b79ac1375 | underdog | J.K. Dobbins | Rush + Rec Yards | under | 0.052680985711279105 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|c576f022-bc2d-4dc5-977d-7e4dc4f852fc | underdog | Bijan Robinson | Receiving Yards | under | 0.052599299690431756 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|9e0cfe1d-3ce4-4cf3-bce8-09e661cb3cda | underdog | Ryan Flournoy | Receptions | under | 0.052546796586534494 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|f4af8d61-8588-4d80-ac8d-fd8686a33979 | underdog | Malik Willis | Rush Yards | under | 0.052470845197019944 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|74b76a65-dbd7-4d0a-88a8-11aa3d120252 | underdog | Willie Rodriguez | Receiving Yards | under | 0.052230432348502775 | 2026-11-05T12:22:13Z | 2026-11-07T23:15:00Z |
| underdog|e3313430-aacf-44db-883d-52e439eff18b | underdog | Drew Wagner | Receiving Yards | over | 0.05222919720332875 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|7c09637f-ba5b-48d9-a7b4-45cc01362313 | underdog | Justin Herbert | Rush Yards | under | 0.05178516711907766 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|cc22fac7-2f59-456b-9cae-e6eb0d0a9e39 | underdog | Troy Franklin | Receptions | under | 0.05174111879222043 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| prizepicks|16578332 | prizepicks | Braylon Staley | Recs | under | 0.05153228331798554 | 2026-11-05T12:22:13Z | 2026-11-07T18:15:00.000-05:00 |
| underdog|b176aba6-ab0b-46be-b198-5db26078c7c0 | underdog | Rico Scott | Receptions | under | 0.050697211562924394 | 2026-11-05T12:22:13Z | 2026-11-07T20:30:00Z |
| underdog|e46702d6-ae35-43c0-ab3b-2e638d0153d9 | underdog | Chad Ryland | Kicking Points | over | 0.0506262653818188 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|a823d7dd-f020-47c2-abc7-ab9d25d21cbf | underdog | JC French | Pass TDs | over | 0.05059286004736313 | 2026-11-05T12:22:13Z | 2026-11-07T20:30:00Z |
| underdog|b4bf9f2b-e849-446b-a805-eda4d01af7be | underdog | Khalil Shakir | Receiving Yards | under | 0.05058312311415858 | 2026-11-04T12:10:41Z | 2026-11-10T01:15:00Z |
| underdog|6a30bff5-d45d-45f9-a712-6c98fba34405 | underdog | Lloyd Avant | Rush Yards | over | 0.05041483365885191 | 2026-11-05T12:22:13Z | 2026-11-08T00:45:00Z |
| underdog|306d32c9-76be-44a5-b65c-2d983b4ebc2f | underdog | Ashton Jeanty | Rush + Rec Yards | under | 0.05021547727948117 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|fc8c7bdd-6f0b-4802-8874-c12236925669 | underdog | Jaylen Raynor | Pass Yards | under | 0.04980050697892513 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|d014a1a2-0d40-4dfc-b478-da703028bd90 | underdog | Kendrick Raphael | Rush Yards | under | 0.0493823595087185 | 2026-11-04T12:10:41Z | 2026-11-07T00:00:00Z |
| underdog|da32429e-2136-492e-ade0-808946db1392 | underdog | Dalton Kincaid | Receiving Yards | under | 0.049312018647535094 | 2026-11-05T12:22:13Z | 2026-11-10T01:15:00Z |
| underdog|807c529e-31ff-4c65-9ac7-c60639f1a1f4 | underdog | Jayden Daniels | Rush Yards | under | 0.049059514309005126 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|ed56e197-54b7-4d14-9254-cc19f9dfbd99 | underdog | Yannick Smith | Receiving Yards | under | 0.04899083677379246 | 2026-11-04T12:10:41Z | 2026-11-07T00:00:00Z |
| prizepicks|16577037 | prizepicks | Chris Olave | Rec Yards | under | 0.04898251964490763 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|b73b2349-67bd-4725-869e-3e946a7c225e | underdog | Jakobi Meyers | Receptions | under | 0.04885583654522818 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|f846cfba-c825-4e6b-aac9-0975e8c6604a | underdog | Kayshon Boutte | Receptions | over | 0.04870573326693556 | 2026-11-05T12:22:13Z | 2026-11-08T21:05:00Z |
| prizepicks|16687773 | prizepicks | Aidan Chiles | Pass Attempts | under | 0.04858649581932972 | 2026-11-05T12:22:13Z | 2026-11-07T19:30:00.000-05:00 |
| underdog|6b69088c-d4a8-4159-bbd0-3e2170aae7d7 | underdog | Brad Jackson | Pass TDs | under | 0.048348152610976136 | 2026-11-05T12:22:13Z | 2026-11-08T03:30:00Z |
| underdog|1b0eb045-4271-4dec-a604-a4c38773225d | underdog | Aidan Birr | XP Made | over | 0.048078044601977676 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|06cbdc53-991e-4be9-877a-27b6e3d70c05 | underdog | Jonathan Taylor | Receiving Yards | over | 0.0476798762525088 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|b8fec16e-e184-416c-9fab-8a457d0f893f | underdog | Cayden Lee | Receiving Yards | under | 0.047650204243950056 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|1441af20-ca44-43f2-b7f8-3dc65dac1fb6 | underdog | Jadan Baugh | Rush Yards | under | 0.047469000409556705 | 2026-11-05T12:22:13Z | 2026-11-08T00:45:00Z |
| underdog|0729c05e-e380-4efb-b2ae-e1403174fb84 | underdog | Samaje Perine | Receptions | over | 0.04737537544984716 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| prizepicks|16567035 | prizepicks | Jordan Love | Pass TDs | under | 0.04710112679060341 | 2026-11-04T12:10:41Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|8d98abf4-bc5e-4549-90db-f4eca6824ba0 | underdog | Bucky Irving | Rush + Rec Yards | under | 0.04692066418821539 | 2026-11-05T12:22:13Z | 2026-11-09T01:20:00Z |
| underdog|85850fda-bdb6-4970-9de6-4c327b723dbd | underdog | Torrance Burgess | Receptions | under | 0.04685698559541274 | 2026-11-05T12:22:13Z | 2026-11-08T03:30:00Z |
| underdog|e5156db0-79be-42ba-8302-5fcd0cfd7d61 | underdog | Ethan Moczulski | XP Made | over | 0.046690949261277925 | 2026-11-04T12:10:41Z | 2026-11-07T01:00:00Z |
| underdog|79efae80-1726-417d-9fba-673881fec86c | underdog | Kyler Kasper | Receiving Yards | under | 0.046656667808123276 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|65627c47-2fdc-4cc1-89a0-b5b9ae949e7a | underdog | Tre Richardson | Receiving Yards | under | 0.04659616037697645 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|d3bf6324-2946-408d-8923-048c559dfff8 | underdog | Jahmyr Gibbs | Receiving Yards | under | 0.04649516222888994 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|8ac17bbc-0479-482d-b6ca-4651a3b3a2f0 | underdog | Drew Stevens | Kicking Points | under | 0.04644611027329182 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|40da3ee9-17d9-44f6-984c-7575298a9713 | underdog | Michael Hawkins | Rush Yards | under | 0.04627747558472772 | 2026-11-05T12:22:13Z | 2026-11-08T02:30:00Z |
| underdog|60ae2057-2007-4cae-9f42-087799172fc0 | underdog | Brenton Strange | Receiving Yards | under | 0.04608906136624302 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|9a3d5951-42b0-4cdc-9a0d-f3d820453d9b | underdog | Mike Matthews | Receiving Yards | under | 0.045793510434076534 | 2026-11-05T12:22:13Z | 2026-11-07T23:15:00Z |
| underdog|e4023e77-9713-4947-a229-d8d0c01daa5c | underdog | Jojo Phillips | Receiving Yards | over | 0.04551214414039517 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| prizepicks|16578154 | prizepicks | Brenton Strange | Rec Targets | under | 0.045215014696700084 | 2026-11-03T02:21:46Z | 2026-11-05T20:15:00.000-05:00 |
| underdog|ee7283f4-fd73-422d-bd13-d29f537b4bbd | underdog | Griffin Wilde | Receiving Yards | under | 0.04521349801132524 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|c3a647e6-584b-4bdb-8682-1f001d85eb33 | underdog | Isaiah Mizell | Receiving Yards | under | 0.04508966097581346 | 2026-11-05T12:22:13Z | 2026-11-07T03:15:00Z |
| underdog|7a72d0be-60ae-4376-8aa1-07e785aab859 | underdog | Jonathan Taylor | Receptions | under | 0.04508721237534341 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|51e7af2b-f9a1-43ea-aa78-584f372553e2 | underdog | Trey Smack | Kicking Points | under | 0.04455434973971151 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|ea125837-d29b-4284-a90d-fee5aa2a9a96 | underdog | Chris Godwin | Receptions | under | 0.04434472697680247 | 2026-11-05T12:22:13Z | 2026-11-09T01:20:00Z |
| underdog|e5d081ab-9efa-43d3-bfb8-a43e2d593f85 | underdog | Drake Maye | Pass TDs | under | 0.04430737897190651 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|f30dd4e7-dacd-455c-8ed4-95be1fa5e74c | underdog | Karolina Muchova | Double Faults | under | 0.044153512874079426 | 2026-11-05T12:22:13Z | 2026-11-09T20:00:00Z |
| underdog|c9267be5-809f-4560-bc25-5715ad03401b | underdog | Jake Fette | Pass TDs | under | 0.044107975358992135 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|997e67da-c8d3-4a83-9610-e8d3e6b73ebb | underdog | Caleb Odom | Receiving Yards | over | 0.0440665088048563 | 2026-11-04T12:10:41Z | 2026-11-08T00:30:00Z |
| underdog|fa268a96-c011-4c35-9f2c-71018831b22d | underdog | Chase Brown | Receiving Yards | under | 0.044036182985406125 | 2026-11-05T12:22:13Z | 2026-11-08T14:30:00Z |
| underdog|5e087ca0-c81b-466a-a4ab-b25feaca7f84 | underdog | Noah Bennee | Receiving Yards | over | 0.04389551607024966 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|9815d49d-2af1-48c2-b6e4-cbe7c87349ac | underdog | Emmett Johnson | Receiving Yards | over | 0.043799798929959555 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|46e3d4a9-5052-4f6b-9df2-d71dac46eb5f | underdog | Derrick Henry | Receiving Yards | over | 0.0437423600982455 | 2026-11-03T11:59:28Z | 2026-11-06T01:15:00Z |
| underdog|7da11b8f-5399-4a1b-be01-2cbe1a58ddeb | underdog | Malachi Fields | Receiving Yards | under | 0.04372469851815042 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|0b62bd90-29f0-4ad6-b3d0-29cc65e4abc0 | underdog | Camden Coleman | Pass TDs | over | 0.04354120619370039 | 2026-11-05T12:22:13Z | 2026-11-06T01:00:00Z |
| underdog|d7858e4c-fb76-4a26-a042-d8bbe31cdf27 | underdog | Kelby Valsin | Receptions | under | 0.04351852989099758 | 2026-11-05T12:22:13Z | 2026-11-06T00:30:00Z |
| underdog|9f8d5a76-cbb3-4565-b2d4-601b302e1c66 | underdog | Jojo Phillips | Receptions | over | 0.04343832039629403 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|c8c7079d-1a74-48ed-ae76-add235e9bf50 | underdog | Trinidad Chambliss | Pass TDs | over | 0.043317722650847656 | 2026-11-04T12:10:41Z | 2026-11-08T00:30:00Z |
| underdog|c2e9acd7-4e88-4f30-ae76-a25816dd4141 | underdog | Ricky Johnson | Receiving Yards | over | 0.043306631735705814 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|1075e7a4-7835-48a5-a2db-a78bbb0c36aa | underdog | Kalif Raymond | Receiving Yards | over | 0.04323294702184943 | 2026-11-05T12:22:13Z | 2026-11-09T01:20:00Z |
| prizepicks|16557917 | prizepicks | Jordan Love | Rush Yards | under | 0.0431179313386405 | 2026-11-03T02:21:46Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|fe7a85f2-c21c-4535-88b9-b246e6af4d70 | underdog | Jason Sanders | FG Made | over | 0.04309576984353114 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|69d33979-906e-439f-b526-f612ed22aaaa | underdog | Gavin Lahm | FG Made | under | 0.04308668218923806 | 2026-11-05T12:22:13Z | 2026-11-07T21:15:00Z |
| underdog|91f4a8ca-8e1b-4038-a81f-33103051637f | underdog | Darnell Mooney | Receptions | over | 0.04273058695676135 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|a5088759-dcc4-4d0c-acb8-516ddb05b069 | underdog | Noah Fant | Receptions | over | 0.04270940205899032 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| prizepicks|16578156 | prizepicks | Jakobi Meyers | Rec Targets | under | 0.04242041013161002 | 2026-11-03T02:21:46Z | 2026-11-05T20:15:00.000-05:00 |
| prizepicks|16677125 | prizepicks | Luca Van Assche | Total Games Won | over | 0.04224858068907933 | 2026-11-05T12:22:13Z | 2026-11-05T07:30:00.000-05:00 |
| underdog|7cb3fbf6-c9e4-47ff-8fdc-7ad015eff5a9 | underdog | Kenneth Walker III | Receiving Yards | under | 0.042196979680496294 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|06609665-f084-4b1b-affa-8cc4f9a90e0b | underdog | Omari Hayes | Receptions | over | 0.041906589246400505 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|de6628da-2358-4822-a9a8-cf3d44824d9c | underdog | Zay Flowers | Receptions | over | 0.041882993253793854 | 2026-11-03T11:59:28Z | 2026-11-06T01:15:00Z |
| underdog|306be0c1-9650-4027-8391-6aeca88bcf4d | underdog | Lotzeir Brooks | Receptions | over | 0.04144434396768071 | 2026-11-05T12:22:13Z | 2026-11-07T20:30:00Z |
| prizepicks|16667335 | prizepicks | Puka Nacua | Recs | under | 0.04136046632707657 | 2026-11-05T12:22:13Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|127ded5d-257a-4c2a-bb25-88e0bd0debad | underdog | Jordan Love | Rush Yards | under | 0.04127202084950954 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|f2277cdd-5e31-44a1-8b8a-5cb8c668ea11 | underdog | Steven Robinson | Rush Yards | under | 0.04112669577799255 | 2026-11-05T12:22:13Z | 2026-11-06T01:00:00Z |
| underdog|6af1f579-11d3-4d3e-a5c5-36d75a14e37a | underdog | Bo Jackson | Receiving Yards | over | 0.04104279325152682 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| prizepicks|16701852 | prizepicks | Antwan Raymond | Rush Atts | under | 0.040920919788068 | 2026-11-05T12:22:13Z | 2026-11-07T16:15:00.000-05:00 |
| underdog|3f9b8b2b-6598-411d-beb2-956ffc189285 | underdog | Wayshawn Parker | Rush Yards | under | 0.04086926461579954 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|52b06c24-0ece-49ed-9cd7-54e8013cf2b8 | underdog | Juwan Johnson | Receiving Yards | under | 0.04062551161927608 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|37ad3b9b-b644-4db3-95fd-a6dda1efec53 | underdog | Marshall Pritchett | Receptions | over | 0.04061687669708042 | 2026-11-05T12:22:13Z | 2026-11-07T20:30:00Z |
| underdog|b4876ca4-f7e7-4fd2-ac05-6f01d5d72d89 | underdog | Justice Hill | Receptions | under | 0.040539917044618345 | 2026-11-03T02:21:46Z | 2026-11-06T01:15:00Z |
| underdog|239a68da-0f8c-4169-995a-f65fc56b29f1 | underdog | AJ Wilson | Receiving Yards | under | 0.04053967621814614 | 2026-11-05T12:22:13Z | 2026-11-06T00:30:00Z |
| underdog|67ecfc13-7baa-495f-be1d-d0ec1521310e | underdog | Zechariah Sample | Receiving Yards | over | 0.040524746237519005 | 2026-11-05T12:22:13Z | 2026-11-08T03:30:00Z |
| underdog|bcc3366d-03c4-4686-b8c4-9911098d7a7d | underdog | Jaylen Raynor | Rush Yards | over | 0.040483745848692076 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| prizepicks|16577047 | prizepicks | Ryan Flournoy | Rec Yards | under | 0.04046234355837319 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|19911946-1f92-42a4-aa1c-15e5815fb816 | underdog | Tee Higgins | Receptions | under | 0.04018031305357561 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| prizepicks|16670099 | prizepicks | Anthony Colandrea | Rush Atts | under | 0.040074430799448724 | 2026-11-05T12:22:13Z | 2026-11-06T20:00:00.000-05:00 |
| underdog|3bd01e57-9195-4088-a564-fe508f2d81f0 | underdog | Isaiah Likely | Receptions | under | 0.039903034181366426 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|ba8fef99-d422-4b62-9db9-af856bcc16e0 | underdog | Noah Fifita | Rush Yards | over | 0.039892924691395826 | 2026-11-05T12:22:13Z | 2026-11-07T03:15:00Z |
| prizepicks|16557921 | prizepicks | Kyler Murray | Rush Yards | under | 0.0398853265542245 | 2026-11-03T02:21:46Z | 2026-11-09T20:15:00.000-05:00 |
| underdog|7a5a7c7a-46d9-4665-9112-650361479cc3 | underdog | Dalen Penson | Receiving Yards | under | 0.039666610643468436 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|51793da7-f50f-4605-9f8b-5f37ddfbd171 | underdog | Jamari Johnson | Receptions | under | 0.039549403867083055 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|b510b6c8-aa64-436f-a890-a3ad7f41278d | underdog | Keelon Russell | Rush Yards | over | 0.03954798492547018 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| prizepicks|16577038 | prizepicks | Travis Kelce | Rec Yards | under | 0.039492224251563846 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|9051164e-05e3-41a4-b605-6b9dae5d49a4 | underdog | Drake Lindsey | Pass TDs | under | 0.03931495181306932 | 2026-11-04T12:10:41Z | 2026-11-07T17:00:00Z |
| underdog|a596db47-839a-48c6-ad4e-2d4ee22fa105 | underdog | Kimani Vidal | Receiving Yards | under | 0.039258403243146445 | 2026-11-05T12:22:13Z | 2026-11-08T21:05:00Z |
| underdog|5546b374-d2d2-4ee9-9f08-e5723cc2fe5a | underdog | Ty Dieffenbach | Pass Yards | under | 0.03912471738390366 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|cefb0596-2c7e-431b-8408-7a1ed12d8db4 | underdog | Bryce Young | Pass TDs | under | 0.039094010660283285 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|b928a5ef-308e-4395-97c3-f7cbc952337a | underdog | Ayden Greene | Receiving Yards | over | 0.038935127218449606 | 2026-11-04T12:10:41Z | 2026-11-07T00:00:00Z |
| underdog|7ec6b8e6-f4bc-4ceb-9977-2343e6cf733c | underdog | Patrick Overmyer | Receiving Yards | under | 0.03891506317250926 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|d1d3e66e-276b-43d4-9e06-fe5ed3964b6c | underdog | Geno Smith | Pass TDs | over | 0.038346590420210214 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|3d8c6433-e8fe-4594-ab61-abba3e53d029 | underdog | Jaden Greathouse | Receiving Yards | under | 0.03830657413311467 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|30207658-d186-4c70-8ce0-0f79ac92f94f | underdog | Trae'shawn Brown | Rush Yards | over | 0.037999199829431785 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|ed498511-b16f-46d2-bc03-e9dd42b5220b | underdog | Ahmad Miller | Rush Yards | under | 0.037559554816855245 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|4efc08ed-4ee8-4a2a-abd8-2a0dfb2ef0df | underdog | Foster Moreau | Receiving Yards | over | 0.03742864021984749 | 2026-11-05T12:22:13Z | 2026-11-08T21:05:00Z |
| underdog|9b900847-d883-49fd-af7c-83a453dd7469 | underdog | J.K. Dobbins | Rush Yards | under | 0.03728319521425405 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|1997f55a-78b3-4c4c-909c-a6a479005d46 | underdog | Eric Olsen | Receiving Yards | under | 0.0372510438778374 | 2026-11-05T12:22:13Z | 2026-11-08T03:30:00Z |
| underdog|36c54cdf-d1a5-4421-add6-c8c475dc2cbb | underdog | Linda Noskova | Double Faults | under | 0.037236525846527924 | 2026-11-05T12:22:13Z | 2026-11-08T20:00:00Z |
| underdog|fae9f83c-94b0-42c3-b5e4-38e0ba845826 | underdog | Coco Gauff | Double Faults | under | 0.03701305154789125 | 2026-11-05T12:22:13Z | 2026-11-08T21:10:00Z |
| underdog|2f401558-103b-44dd-b0ae-941e6998fc51 | underdog | Wayne Knight | Rush Yards | under | 0.03693588139563031 | 2026-11-04T12:10:41Z | 2026-11-07T17:00:00Z |
| underdog|6fa25cd4-f116-4af5-97e6-750b63501adc | underdog | Tre Tucker | Receiving Yards | under | 0.03665729041337662 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|119f4d77-645c-42cd-9e5d-3c3aa99ea03d | underdog | Cameron Dicker | FG Made | under | 0.03597583144986216 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| prizepicks|16686176 | prizepicks | Omari Hutchinson | SOT | under | 0.03583319523359496 | 2026-11-05T12:22:13Z | 2026-11-05T12:45:00.000-05:00 |
| underdog|865227cf-17df-4e89-9c98-4311b47f982a | underdog | Tetairoa McMillan | Receptions | under | 0.03583202783628714 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| prizepicks|16576405 | prizepicks | Puka Nacua | Rush Yards | over | 0.035802440511908284 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|63535c0e-f25f-4020-b229-60487df1cb5e | underdog | Kenny Darby | Receptions | over | 0.035572200850898905 | 2026-11-05T12:22:13Z | 2026-11-07T23:15:00Z |
| underdog|f77c4659-c571-4380-bb17-0f290c20cfdb | underdog | Braden Pegan | Receiving Yards | under | 0.03535065146715288 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|2f083c55-dfe0-4021-bc6a-5e7f16540cf5 | underdog | Ryan Fitzgerald | FG Made | under | 0.035264256773103186 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|ace9e75f-3fab-448d-a35d-0f1676382ace | underdog | Daniel Jones | Rush Yards | over | 0.03511058164603342 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|76b2a70a-293f-40f9-a916-eb743ce0a710 | underdog | Omari Hayes | Receiving Yards | over | 0.035032468841684095 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|d956ff35-5891-430d-a052-ebaf442bf737 | underdog | Spencer Shrader | Kicking Points | under | 0.03493687122664446 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|642b6aa4-d8ad-47ca-a6e2-02bf1db1abde | underdog | Rhamondre Stevenson | Receptions | under | 0.03473410197552751 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| prizepicks|16557908 | prizepicks | Patrick Mahomes | Rush Yards | under | 0.034534369510793694 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| prizepicks|16578159 | prizepicks | Nate Boerkircher | Rec Targets | under | 0.0344311591015668 | 2026-11-03T02:21:46Z | 2026-11-05T20:15:00.000-05:00 |
| underdog|b22893f7-7a36-49d0-aff9-c15df2d5deab | underdog | Trey'Dez Green | Receiving Yards | under | 0.03435452781320025 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|488c064e-4a42-4665-a6fc-407585fb9afe | underdog | Lawson Luckie | Receiving Yards | over | 0.03431423503130593 | 2026-11-04T12:10:41Z | 2026-11-08T00:30:00Z |
| underdog|66b37aff-aa69-48ba-984e-2a3c3e131cd4 | underdog | Tommy Tremble | Receptions | over | 0.03430222685481554 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|d07411a2-861f-46d8-9b37-7f958305aba8 | underdog | Miles Coleman | Receiving Yards | over | 0.03415913777769475 | 2026-11-05T12:22:13Z | 2026-11-07T18:00:00Z |
| underdog|b4164f31-211e-44a6-819f-02c4a0dae617 | underdog | Xavier Worthy | Receptions | under | 0.033937644307545756 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|d61c807a-66b1-4a4f-9972-cba41bc45ee6 | underdog | Javonte Williams | Receiving Yards | over | 0.03365125001838698 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|c326b335-e702-421f-9f11-eec8ab8fdfaa | underdog | Dalton Schultz | Receiving Yards | under | 0.03359570617331076 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|27088af6-5b7d-4152-b246-6ea59730b4c5 | underdog | Davian Jackson | Rush Yards | over | 0.0334712784456449 | 2026-11-05T12:22:13Z | 2026-11-08T03:30:00Z |
| underdog|bd3c755a-e5dc-496f-801d-3b5e36bbcd5c | underdog | Mitchell Evans | Receptions | under | 0.03341124042463872 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|c4b7c726-6ba5-4b7b-a3f2-640e9d52771a | underdog | Samaje Perine | Rush + Rec Yards | under | 0.03322821780525986 | 2026-11-05T12:22:13Z | 2026-11-08T14:30:00Z |
| underdog|43d4f051-ed64-4b5e-904b-24f2c6efea26 | underdog | Samaje Perine | Rush Yards | under | 0.03301262915252379 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|a2d14611-eeff-4586-80bd-d349331a9d9f | underdog | Blake Barnett | Pass TDs | under | 0.03293401410353347 | 2026-11-05T12:22:13Z | 2026-11-07T18:00:00Z |
| underdog|8a29eea1-d895-407b-8658-b0db6edb5801 | underdog | Nate Adkins | Receptions | over | 0.03282306378556943 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|a5fbd6d5-3e62-4a23-883d-9f5cf14d5654 | underdog | Shekai Mills-Knight | Rush Yards | under | 0.0327826010465021 | 2026-11-04T12:10:41Z | 2026-11-08T00:30:00Z |
| underdog|e6b1bd36-4a4b-44b3-8d57-b0ffc66e6084 | underdog | Jake Weinberg | FG Made | under | 0.032781270811728436 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|2fdcf276-eb1c-48b0-99cd-8ca8a12bd9f6 | underdog | Wyatt Young | Receiving Yards | under | 0.03277323062096282 | 2026-11-05T12:22:13Z | 2026-11-07T18:00:00Z |
| underdog|b9c1a1a8-01ac-40a2-baab-d2706b32bde2 | underdog | Kyren Williams | Receptions | under | 0.032587481000593055 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|041b30d5-fdc3-4489-bb29-a89e6667b68d | underdog | Charlie Kolar | Receiving Yards | under | 0.03242651143957387 | 2026-11-05T12:22:13Z | 2026-11-08T21:05:00Z |
| underdog|2cfb2c38-eea2-4115-8859-b21897508d6e | underdog | Michael Mayer | Receptions | under | 0.03208971752720258 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|cc8591f7-05de-4f55-87ee-18c509911539 | underdog | Troy Franklin | Receiving Yards | under | 0.03204712122097875 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|9af22aae-0a61-42ed-aeeb-388172d1ad5b | underdog | Tommy Carr | Pass TDs | under | 0.03196836767817157 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|29834b95-ffb3-48a3-8130-df8f76762419 | underdog | Peyton Woodring | FG Made | over | 0.03151348868814757 | 2026-11-04T12:10:41Z | 2026-11-08T00:30:00Z |
| underdog|93b0f412-1f61-4724-8899-f2fb313f7df6 | underdog | Rocky Beers | Receiving Yards | over | 0.031055653380843484 | 2026-11-05T12:22:13Z | 2026-11-08T00:45:00Z |
| underdog|ec21afa7-ad82-4b47-954d-22041573aade | underdog | Raleek Brown | Receptions | over | 0.030773355877860176 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|3005b6a0-46ad-4a80-8375-b890de97dd55 | underdog | AJ Newberry | Receiving Yards | over | 0.030590482240790196 | 2026-11-05T12:22:13Z | 2026-11-08T03:30:00Z |
| underdog|74739193-9a3d-4605-bea1-a4ce527c1306 | underdog | Charlie Woerner | Receiving Yards | over | 0.030266726338770478 | 2026-11-05T12:22:13Z | 2026-11-08T14:30:00Z |
| underdog|9bd8c698-9241-4468-a7b5-e37b14252e48 | underdog | Reece Vander Zee | Receptions | under | 0.030171557685573003 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|f1715ec8-5f20-46c7-ba87-5af729c439a0 | underdog | Cam Cook | Rush Yards | under | 0.03009783990413606 | 2026-11-05T12:22:13Z | 2026-11-08T02:30:00Z |
