# Pipeline Digest -- 2026-11-07T05:49:55Z

## Run summary
- Ingestion: 53884 rows (PrizePicks OK, Underdog OK)
- Estimation: 53884 rows estimated (from 53884 ingested props)
- CLV logging: 351 newly flagged, 0 newly closed, 1071 still open (109487 total ever logged)

## Currently open flags
Sizing is a manual step (sizing_engine.py, Session 2.6) -- this table is what to scan to pick a pair worth sizing.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_edge | first_flagged_at | game_start_time |
|---|---|---|---|---|---|---|---|
| underdog|9eff3818-6fca-4bae-89ed-d1ef14a6fa24 | underdog | Shedeur Sanders | Pass Attempts | under | 0.42261306532663323 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| underdog|7984c1b8-4987-4395-9955-ab4b9006dd75 | underdog | Eddy Pineiro | FG Made | under | 0.41306807406928026 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|cff1cd78-fac0-43f9-9cb4-b5bc70191160 | underdog | Shedeur Sanders | Pass Yards | under | 0.4 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|f67c8dc8-7534-4729-b16e-24c0a4242862 | underdog | Shedeur Sanders | Rush Yards | under | 0.4 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|7b3a0636-bb73-4927-9931-6db6e2b9a2da | underdog | Elijah Mitchell | Rush + Rec Yards | under | 0.4 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|ceef1db1-03fc-4c85-a16e-584faee3ad8c | underdog | Michael Penix | Pass Yards | under | 0.4 | 2026-11-07T05:59:57Z | 2026-11-08T14:30:00Z |
| underdog|b52c7395-e7ee-4951-a4fd-43f9a6eedb90 | underdog | Dak Prescott | Pass Yards | under | 0.4 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|ccdb42d1-d42c-45e7-9506-09039c4def86 | underdog | Jack Larsen | Receiving Yards | over | 0.4 | 2026-11-06T16:02:47Z | 2026-11-08T00:30:00Z |
| underdog|6f655839-d390-4b43-8c4f-9e9362052e1a | underdog | Carson Wentz | Pass Yards | under | 0.4 | 2026-11-06T16:02:47Z | 2026-11-10T01:15:00Z |
| underdog|f8f22600-df6e-4a85-ab30-0af2b9247426 | underdog | Stefon Diggs | Receiving Yards | under | 0.4 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|ba45158c-55cc-48e5-9aa2-cc1efeb6e624 | underdog | Drew Lock | Pass Attempts | under | 0.4 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|3e831f69-cf67-408d-9148-2f2a2205f140 | underdog | Brandon McManus | Kicking Points | under | 0.4 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|ce087efd-74be-4e03-b867-d767dd7439b1 | underdog | Caleb Williams | Pass Yards | under | 0.4 | 2026-11-07T05:59:57Z | 2026-11-09T01:20:00Z |
| underdog|d71953b3-f84a-41de-8164-f5fbcaae145d | underdog | Malik Willis | Pass Yards | under | 0.4 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|a958d6b8-a05d-4422-9e27-954de20b555e | underdog | Brock Purdy | Pass Yards | under | 0.4 | 2026-11-05T22:06:44Z | 2026-11-08T21:25:00Z |
| underdog|159c0350-eab4-41f1-b826-0de1e1e3b5bd | underdog | Justin Herbert | Pass Yards | under | 0.4 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|268d2fc5-2abe-4849-b4a0-390d7485e453 | underdog | Caleb Williams | Pass Attempts | under | 0.4 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|57a8861e-d69d-4cfe-936e-0c47010e012e | underdog | Jadarian Price | Receiving Yards | under | 0.4 | 2026-11-05T22:06:44Z | 2026-11-08T21:25:00Z |
| underdog|47ec053c-388c-4d74-a581-14d22b98c92a | underdog | Carson Wentz | Pass Attempts | under | 0.4 | 2026-11-05T22:06:44Z | 2026-11-10T01:15:00Z |
| underdog|2f23291e-eb46-4b0f-96d3-43d76315dc36 | underdog | Josh Jacobs | Rush Yards | under | 0.4 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|25f20e70-7454-41c9-808c-0518a23b77f3 | underdog | Emari Demercado | Rush Yards | under | 0.4 | 2026-11-07T05:59:57Z | 2026-11-08T21:05:00Z |
| underdog|326cd261-b3b4-4f5a-98a2-f3c400a5af12 | underdog | Drew Lock | Pass Yards | under | 0.4 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|754ec181-3723-4eeb-9d81-6ac2f38d4b05 | underdog | Josh Allen | Pass Yards | under | 0.4 | 2026-11-04T12:10:41Z | 2026-11-10T01:15:00Z |
| underdog|96033226-3c76-446f-9bf6-5d25b104b846 | underdog | DeSean Bishop | Receiving Yards | over | 0.39702698699338135 | 2026-11-07T05:59:57Z | 2026-11-07T23:15:00Z |
| underdog|88a67ef6-decb-440a-98f8-fb4b22c34d26 | underdog | Brandon McManus | FG Made | under | 0.3956303597430939 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|a31d98a6-bf53-440e-a5b5-a2b50e20038d | underdog | Bo Nix | Pass Yards | under | 0.39297059903848375 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|d889190a-2c86-4441-a789-7f8d68386db5 | underdog | Skyler Bell | Receiving Yards | under | 0.39223309295827813 | 2026-11-07T05:59:57Z | 2026-11-10T01:15:00Z |
| underdog|3457fac4-96e9-46e5-a38e-f8575853e01c | underdog | Jayden Daniels | Pass Yards | under | 0.3893084725552035 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|53645bb3-c943-40ab-8bf6-8cac981c28ca | underdog | Baker Mayfield | Pass Yards | under | 0.3826968412880367 | 2026-11-07T05:59:57Z | 2026-11-09T01:20:00Z |
| underdog|91257feb-8a6e-4897-a344-a682b8f407f8 | underdog | Justin Herbert | Pass Attempts | under | 0.382571560879172 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|01618ae6-c47b-4863-8ed5-5588a5af1039 | underdog | Devin Singletary | Rush Yards | under | 0.379407090167039 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|705e8042-bbe1-42e5-a50a-844d254c8900 | underdog | Kirk Cousins | Pass Yards | under | 0.3761461839014639 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|f9976ec1-4523-4b7a-bd0c-bca9b9dd4fb5 | underdog | Eddy Pineiro | Kicking Points | under | 0.3662333132187251 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|e3631ab4-a4e3-47d6-93c4-59cc4023bd88 | underdog | Daniel Jones | Pass Yards | under | 0.3637643979429024 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|5527bc92-0137-44d7-86c7-ca58439b3c0e | underdog | Devin Singletary | Rush + Rec Yards | under | 0.36215403846684935 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|20ded54a-d3d9-4991-b45f-4aab1465f143 | underdog | Jordan Love | Pass Yards | under | 0.35357762783010915 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| prizepicks|16557936 | prizepicks | Dak Prescott | Pass Yards | under | 0.35094246505677495 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| prizepicks|16557940 | prizepicks | Brock Purdy | Pass Yards | under | 0.35094246505677495 | 2026-11-03T02:21:46Z | 2026-11-08T16:25:00.000-05:00 |
| prizepicks|16557944 | prizepicks | Josh Allen | Pass Yards | under | 0.35094246505677495 | 2026-11-03T02:21:46Z | 2026-11-09T20:15:00.000-05:00 |
| prizepicks|16722860 | prizepicks | Demarcus Robinson | Rec Targets | under | 0.35094246505677495 | 2026-11-06T06:34:07Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|8590c432-1edf-4107-977c-54550d8fdfa4 | underdog | Olamide Zaccheaus | Receiving Yards | under | 0.34722235681746216 | 2026-11-07T05:59:57Z | 2026-11-08T14:30:00Z |
| underdog|76903731-5a31-4b71-aa02-3cf5f1f66632 | underdog | Jared Goff | Pass Yards | under | 0.34472431347503396 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|248aba17-77a9-49a7-96ad-e3085571e3b7 | underdog | Patrick Mahomes | Pass Yards | under | 0.34460651530387776 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|b4edad16-13cb-4bd3-8856-373011648386 | underdog | Brandin Cooks | Receiving Yards | under | 0.3413682969028984 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| prizepicks|16557935 | prizepicks | Jayden Daniels | Pass Yards | under | 0.3359949609424918 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|37f53eaf-c7e4-4925-a45a-ca84b8d9ea68 | underdog | C.J. Stroud | Pass Yards | under | 0.33338439151254773 | 2026-11-05T22:06:44Z | 2026-11-08T21:05:00Z |
| underdog|91cd9a90-2bbb-4479-9d44-9025494f5dbb | underdog | Bo Nix | Pass Attempts | under | 0.33308348303432955 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|9e14cfdb-3be3-4ec4-a9b0-18a08e517978 | underdog | Skyler Bell | Receptions | under | 0.32591289918005106 | 2026-11-07T05:59:57Z | 2026-11-10T01:15:00Z |
| underdog|fa35b61f-7cc4-4f4b-9185-6e6a5167ad20 | underdog | Michael Penix | Pass Attempts | under | 0.3245304925645227 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|c3559a9a-0b12-4da5-bd9d-295bc350acb1 | underdog | Jadarian Price | Rush + Rec Yards | under | 0.3228916482644886 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|dfd26c17-46c2-49e7-80e7-7bd5bf224448 | underdog | Alonza Barnett | Pass Yards | under | 0.32277006367640626 | 2026-11-05T22:06:44Z | 2026-11-07T20:45:00Z |
| underdog|4fd3a242-cf5f-4eb3-a5db-95f253c0db3a | underdog | Josh Allen | Pass Attempts | under | 0.3201476032121736 | 2026-11-04T12:10:41Z | 2026-11-10T01:15:00Z |
| underdog|e6d5777b-8939-4202-8ed4-51f40d7be001 | underdog | Christian McCaffrey | Rush + Rec Yards | under | 0.3198836335711852 | 2026-11-05T22:06:44Z | 2026-11-08T21:25:00Z |
| underdog|efda5476-bc73-4e5c-8d29-c3b22c80a111 | underdog | Drake Maye | Pass Yards | under | 0.3169471849941047 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|c180ec24-04be-4d76-92bd-f2b1a7387ad4 | underdog | Josh Jacobs | Receptions | under | 0.3138562329893375 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| prizepicks|16718547 | prizepicks | Josh Jacobs | Rec Targets | under | 0.3126463971775677 | 2026-11-05T22:06:44Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|9b917f87-4065-4257-ba6e-cf63e69dd2b5 | underdog | Demarcus Robinson | Receiving Yards | under | 0.3106260675585195 | 2026-11-06T06:34:07Z | 2026-11-08T21:25:00Z |
| prizepicks|16557939 | prizepicks | Kirk Cousins | Pass Yards | under | 0.3094515764679242 | 2026-11-03T02:21:46Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|9d14ec55-11a1-45e7-b650-84b9a5ebf34c | underdog | J.J. McCarthy | Pass Yards | under | 0.304744428527313 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|9971b293-5127-4010-a044-631202a9dc81 | underdog | Jarvis Green | Rush Yards | under | 0.30473946073238456 | 2026-11-07T05:59:57Z | 2026-11-07T17:00:00Z |
| underdog|930f200c-47f6-4926-8c1e-7fd5e0f96871 | underdog | Thomas Castellanos | Pass Yards | under | 0.30366673535514543 | 2026-11-07T05:59:57Z | 2026-11-08T02:30:00Z |
| underdog|37896abf-b78c-4078-bf55-90cf3966fe31 | underdog | Puka Nacua | Receiving Yards | under | 0.30330510113385567 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| prizepicks|16763489 | prizepicks | Jayden Daniels | Pass+Rush+Rec TDs | under | 0.2995481890476045 | 2026-11-07T05:59:57Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|5f0cd76c-a7f5-445c-83c0-0f0a646cceec | underdog | Brock Bowers | Receiving Yards | under | 0.29946639988592183 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|c276a65a-ae82-4954-9d4c-13d68aa92353 | underdog | Emeka Egbuka | Receiving Yards | under | 0.29901932004324594 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|c565d953-1a25-421d-a6bd-cb2d0b4b8cf9 | underdog | Jonathon Cooper | Sacks | under | 0.29698492462311565 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|b3820062-ff10-4245-afb1-048cb910cd60 | underdog | Brock Purdy | Pass Attempts | under | 0.29563370361590136 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|c1d7ae0f-d0c1-449e-be5b-2f61fd0f8ae7 | underdog | Shedeur Sanders | Pass TDs | under | 0.29393939393939406 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| underdog|33b0e243-2f4a-4a3e-9b10-fdf1a7f0985c | underdog | Bryce Young | Pass Yards | under | 0.2932756252152141 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|a024c408-1fb1-43f6-b5cf-788ae51041e2 | underdog | Kyler Gordon | Sacks | over | 0.2919017834621568 | 2026-11-07T05:59:57Z | 2026-11-09T01:20:00Z |
| underdog|d45635fa-67f4-47c8-9b6b-5839c880bd23 | underdog | Antonio Williams | Receiving Yards | under | 0.29034431660648385 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|a4f7e2ea-445a-4746-9a01-bb8681efb55d | underdog | Drake Maye | Pass Attempts | under | 0.2890709907617405 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|b1871eee-1be7-4d3b-b76e-1f9f7f70baca | underdog | J.J. McCarthy | Pass TDs | under | 0.2875734861947701 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|dd2f4f79-4283-42e8-afb4-2092a78921a4 | underdog | Geno Smith | Pass Yards | under | 0.2812427694504944 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|aa1a021c-c0c9-409d-8179-529bd6bc7f25 | underdog | Zane Gonzalez | Kicking Points | under | 0.2811321303826997 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|c65ae7a0-14dd-4948-bd2b-2216fbebe1d1 | underdog | Daniel Jones | Pass TDs | under | 0.27974205004038677 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|4cca7077-ba32-4aba-8ed4-90e312b20ac2 | underdog | Jadarian Price | Rush Yards | under | 0.2787804746448542 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|95751aad-a038-411c-a867-51d3c11fc96c | underdog | Braden Atkinson | Pass Yards | under | 0.2786956332075442 | 2026-11-05T22:06:44Z | 2026-11-08T03:30:00Z |
| underdog|457dec03-fb15-48fc-bc38-09756507b0fb | underdog | Joe Burrow | Pass Yards | under | 0.2767456512747548 | 2026-11-05T22:06:44Z | 2026-11-08T14:30:00Z |
| underdog|df8dac90-be57-4491-8f0d-566482090ae9 | underdog | Corey Kiner | Receiving Yards | over | 0.27647574749151815 | 2026-11-06T06:34:07Z | 2026-11-08T21:25:00Z |
| underdog|034db5e8-e2a4-4f3a-b113-160fa7977d4f | underdog | Jake Elliott | FG Made | under | 0.27609595620105687 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|9575a38e-86fe-4a9a-93ec-f8617ef793bd | underdog | Brandin Cooks | Receptions | under | 0.2755434284462872 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|93824785-dfec-403f-b1b6-5c9307c52772 | underdog | Antonio Williams | Receptions | under | 0.27536916730692296 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|a3499f76-dc57-40ca-a12b-ccab39f10be5 | underdog | Bryce Young | Pass Attempts | under | 0.27237481147034737 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|bd628484-6e46-438d-aedc-ed875436387c | underdog | Demarcus Robinson | Receptions | under | 0.2692251142156261 | 2026-11-06T06:34:07Z | 2026-11-08T21:25:00Z |
| underdog|5a0ff8aa-ab28-4f6c-9ec5-e95c971f8458 | underdog | Andy Borregales | Kicking Points | under | 0.2640899467628497 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|029429a0-88e2-4188-bb6a-963cd5a7c4e2 | underdog | Baker Mayfield | Pass TDs | under | 0.26332788339696256 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| prizepicks|16719183 | prizepicks | Saquon Barkley | Rec Targets | under | 0.26316628788845475 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|e66581ae-3fdf-48bb-b13e-4de3cf47a5fe | underdog | Saquon Barkley | Receptions | under | 0.26082333678953884 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|d484d774-fbd8-467b-bbfa-b6f85cfcf83f | underdog | Courtland Sutton | Receptions | under | 0.25834377385355134 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|c7d0412f-1aba-47dd-8ce0-e06060ca7b59 | underdog | Kyle Pitts | Receiving Yards | under | 0.25799821779938514 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|9d4fa631-2131-4a0c-9be8-fc96c08e2585 | underdog | Jake Weinberg | XP Made | over | 0.25701675995779105 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|42260fca-3f4a-4284-b57d-b9e07b027ca8 | underdog | Chase Brown | Rush + Rec Yards | under | 0.256995610592043 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| prizepicks|16557933 | prizepicks | Patrick Mahomes | Pass Yards | under | 0.256531424485161 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|88b26255-d953-47cf-aa2d-032da6db6cbf | underdog | Caleb Williams | Pass TDs | under | 0.256421951810362 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|129a3cfd-80c7-4c48-a51b-24b6b5c538e9 | underdog | Matthew Stafford | Pass Yards | under | 0.25290413933089306 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|25d18fbf-8c15-4a17-895c-3635dd1ce944 | underdog | Malik Willis | Pass Attempts | under | 0.2526482871588408 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|b72f06e1-815c-4c36-b978-4fcc8dfeeef1 | underdog | Andy Borregales | FG Made | under | 0.25213168723502966 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|29ee597a-b184-4464-a729-cbc3fa05fa26 | underdog | Jayden Daniels | Pass Attempts | under | 0.24644808366574278 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|fc0a7b7f-a597-4192-b95e-8c3194038f1b | underdog | George Kittle | Receiving Yards | under | 0.2450159013262515 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|e84e4aa4-7537-48ef-99a7-49d36a0d5fc7 | underdog | Geno Smith | Pass Attempts | under | 0.2432377584583152 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|d16124d4-b93a-4762-a226-001e30eb0d99 | underdog | Thomas Castellanos | Total TDs | under | 0.242385578961412 | 2026-11-07T05:59:57Z | 2026-11-08T02:30:00Z |
| underdog|fd4d3dee-d726-4ef3-b768-54f851728aac | underdog | Cooper Barkate | Receptions | under | 0.2419006148895373 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| underdog|09559dbb-4dfd-4714-895d-7e3f21511df7 | underdog | Tyler Shough | Pass Yards | under | 0.23545769312634657 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|4e219bc4-540f-4254-8899-fb2c0a6c9ef1 | underdog | Jordan Love | Pass Attempts | under | 0.23509904882189492 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| prizepicks|16557934 | prizepicks | Matthew Stafford | Pass Yards | under | 0.23485070755351956 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| prizepicks|16719160 | prizepicks | Brock Bowers | Rec Targets | under | 0.23351025534582692 | 2026-11-05T22:06:44Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|bba3c903-4ede-426b-98a4-5c60cb6bed88 | underdog | Jonah Coleman | Rush Yards | under | 0.233288763818978 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|df5ddaa9-7070-4491-b561-d6a0b56df972 | underdog | Daniel Hill | Receiving Yards | over | 0.23200655516820978 | 2026-11-07T05:59:57Z | 2026-11-07T20:30:00Z |
| underdog|a00ae86a-3ecc-4216-86f7-81d675f73f16 | underdog | Daniel Jones | Pass Attempts | under | 0.23121215443621368 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|dee5b9d6-8a0c-4661-9571-38d4e5b70f5c | underdog | Dexter Lawrence II | Sacks | over | 0.2311576629174456 | 2026-11-07T05:59:57Z | 2026-11-08T14:30:00Z |
| underdog|4e54a271-1412-4d2d-98d4-0ba49bfa6122 | underdog | Josh Jacobs | Rush + Rec Yards | under | 0.22766679996482564 | 2026-11-05T22:06:44Z | 2026-11-08T21:25:00Z |
| underdog|60cbaa38-c568-4879-a6f8-94b6e4e69559 | underdog | Tucker Kraft | Receiving Yards | under | 0.22559324997910668 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|713b2721-78da-4cec-8f94-3e8a3e141d5d | underdog | Mike Washington | Receiving Yards | over | 0.22513540135851895 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|bec6e496-16bb-4fa1-ab70-03d725748d98 | underdog | Austin Booker | Sacks | over | 0.22495368063922305 | 2026-11-07T05:59:57Z | 2026-11-09T01:20:00Z |
| underdog|c1f72f3f-5755-4036-9793-3b0e1f55b9b2 | underdog | Rashee Rice | Receiving Yards | under | 0.2246943029433517 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|ac7c7dd4-b2ae-4952-9e36-546744465357 | underdog | Princely Umanmielen | Sacks | over | 0.22436862922498058 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|b7a27035-0410-4524-9b9f-8504019e9e93 | underdog | Malik Washington | Receiving Yards | under | 0.22383503418957196 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|4610e541-5d71-4664-b765-2e6313fa472a | underdog | Nick Bosa | Sacks | under | 0.22272727272727277 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|4eb90e37-0394-4c4c-8d2e-e31385ee2cfb | underdog | Patrick Mahomes | Pass Attempts | under | 0.22176745268767095 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|6d8eb0bb-0195-4e81-b62a-94edbb4b8341 | underdog | George Kittle | Receptions | under | 0.2205590308515778 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|a9694f7d-6e59-4ba1-a1ef-0ee910195888 | underdog | J.J. McCarthy | Pass Attempts | under | 0.22026861920931884 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|cae9a0a8-d1f3-4eb2-87c8-2c8e433a8a8d | underdog | Colston Loveland | Receiving Yards | under | 0.2198455782755615 | 2026-11-06T16:02:47Z | 2026-11-09T01:20:00Z |
| underdog|c4b91ddb-76bd-4bb3-887a-1c4e2540d49f | underdog | Odafe Oweh | Sacks | over | 0.21917035096013796 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|6bbf2a5a-63d8-4774-b146-9892eacd1ce1 | underdog | Kirk Cousins | Pass Attempts | under | 0.21906706972458956 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|5ce7b43f-6c56-458c-8e7b-dc6749b86b93 | underdog | Zach Sieler | Sacks | over | 0.21881747292660894 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|948a45cd-0a83-479c-91ff-a753defb03d8 | underdog | Quinshon Judkins | Rush + Rec Yards | under | 0.21863111489144205 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|3d11ff54-e68e-46fd-9bee-9f64e201a532 | underdog | Ladd McConkey | Receptions | under | 0.2182531395719538 | 2026-11-03T02:21:46Z | 2026-11-08T21:05:00Z |
| underdog|277508aa-b1fd-4e0e-a4da-945da69c5b35 | underdog | Courtland Sutton | Receiving Yards | under | 0.2175392615020647 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|bfe8c590-b7cd-46fa-97ef-a6f89b54cba6 | underdog | Christian McCaffrey | Rush Yards | under | 0.21748885231877868 | 2026-11-05T22:06:44Z | 2026-11-08T21:25:00Z |
| underdog|5e5ead91-81b9-4b8e-a5ef-e2aa3b7a5ed0 | underdog | Woody Marks | Rush Yards | under | 0.21579731650075495 | 2026-11-05T12:22:13Z | 2026-11-08T21:05:00Z |
| underdog|49e20d5a-2cc0-46f5-a3cd-2901fcc1ca46 | underdog | Will McDonald IV | Sacks | over | 0.21361991879405742 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|d88c56d2-1395-401b-bd3e-3d1d31728d14 | underdog | Woody Marks | Rush + Rec Yards | under | 0.2133596409286077 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|dabb5287-277e-4a23-8946-40925b7c6a45 | underdog | Sione Vaki | Receiving Yards | over | 0.2124555475324016 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|47643075-a2e0-4286-848c-4cbc6b64643e | underdog | Jaylen Wright | Rush + Rec Yards | under | 0.21167080472030686 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|84acac62-4ba9-4be2-b2e0-edfc9f3d2252 | underdog | Thomas Castellanos | Pass TDs | under | 0.21044509816332535 | 2026-11-05T22:06:44Z | 2026-11-08T02:30:00Z |
| underdog|ce0c66a5-e095-4a55-a3a2-dce5222c3917 | underdog | D'Andre Swift | Rush + Rec Yards | under | 0.2097482313264234 | 2026-11-07T05:59:57Z | 2026-11-09T01:20:00Z |
| prizepicks|16577049 | prizepicks | Trey McBride | Rec Yards | under | 0.20935259101009185 | 2026-11-03T02:21:46Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|23a46bfb-a057-45dc-a412-fb89efb5a4c5 | underdog | Chris Godwin | Receiving Yards | under | 0.20786795867893026 | 2026-11-07T05:59:57Z | 2026-11-09T01:20:00Z |
| underdog|cd3d1726-9c42-4e75-8563-3073cf914224 | underdog | Derrick Barnes | Sacks | over | 0.2049580222093775 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|1f7dd0bf-f127-468a-b32d-11be5fc22ca6 | underdog | Quinshon Judkins | Rush Yards | under | 0.20487468569814804 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| underdog|1fa93360-83ec-4148-833b-a2ac7223bcde | underdog | Evan McPherson | FG Made | under | 0.20387134321469125 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|17d58030-f59c-4e6a-b95e-5e22592343f4 | underdog | Nico Collins | Receiving Yards | under | 0.20265644684978057 | 2026-11-05T22:06:44Z | 2026-11-08T21:05:00Z |
| underdog|b99d6014-b4c3-451f-bc57-c1109aa968ed | underdog | Christian McCaffrey | Receiving Yards | under | 0.20231096643705238 | 2026-11-05T22:06:44Z | 2026-11-08T21:25:00Z |
| underdog|c61022bc-362a-4e1c-8d69-48a576ea6c00 | underdog | Justin Herbert | Pass TDs | under | 0.20191287593682095 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|e8ee0b8d-e450-43e3-8f03-13ce4aaca7ad | underdog | Nick Emmanwori | Sacks | over | 0.19892946238095685 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|745083a1-ab04-465f-bafc-84949eddc5e7 | underdog | Harrison Butker | FG Made | under | 0.19838860610882936 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| prizepicks|16577051 | prizepicks | Brock Bowers | Rec Yards | under | 0.19828126826604298 | 2026-11-03T02:21:46Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|d9931ebc-f2b4-4965-a907-7e5426461db5 | underdog | Trey McBride | Receptions | under | 0.19807043328611007 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|7585e384-c943-4397-90d7-253ec9d11767 | underdog | Jake Fette | Pass Yards | under | 0.19806979923398782 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| underdog|46c1178c-c789-477e-a9af-5ac326ce4d84 | underdog | Tait Reynolds | Total TDs | under | 0.1957648528752154 | 2026-11-07T05:59:57Z | 2026-11-07T17:00:00Z |
| underdog|410efb5a-6f14-4f58-846b-fb76cf98cec4 | underdog | Matthew Stafford | Rush Yards | over | 0.1944521898255368 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|6f7bad5f-65db-4a33-bd35-58f7ef0693d9 | underdog | Devonte Wyatt | Sacks | over | 0.19391242057130526 | 2026-11-06T16:02:47Z | 2026-11-08T21:25:00Z |
| underdog|fd6fe187-a62e-4b28-98d1-7629a2c05b20 | underdog | Alex Singleton | Sacks | over | 0.1921046498261034 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|6d173119-25d4-4548-83ad-03156b0cf2dd | underdog | Ben Yurosek | Receptions | over | 0.19167896654283034 | 2026-11-07T05:59:57Z | 2026-11-10T01:15:00Z |
| underdog|1f3de6fd-36c2-46ee-b345-bd743ca17f3c | underdog | Junior Sherrill | Receiving Yards | under | 0.19109132486949432 | 2026-11-05T22:06:44Z | 2026-11-07T21:15:00Z |
| underdog|872eac2a-4e79-4367-a987-6a15c41a88dc | underdog | Kyle Pitts | Receptions | under | 0.1884927972756335 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| prizepicks|16718554 | prizepicks | Nico Collins | Rec Targets | under | 0.1883756713204645 | 2026-11-05T22:06:44Z | 2026-11-08T16:05:00.000-05:00 |
| underdog|d34c91c5-ef7c-4feb-9ff3-c957645da483 | underdog | Ja'Marr Chase | Receiving Yards | under | 0.18806437242923668 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|047d8b01-9a11-4b7e-b998-0a58025cda6b | underdog | Makhi Hughes | Rush Yards | under | 0.18737645689160087 | 2026-11-07T05:59:57Z | 2026-11-07T20:30:00Z |
| underdog|23e55a57-7467-474d-be5d-65040e14440a | underdog | Josh Downs | Receiving Yards | under | 0.18588799861791883 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|f578cc15-698b-4a56-b103-e35ad36d927d | underdog | Makai Lemon | Receiving Yards | under | 0.1856316687037486 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| prizepicks|16718534 | prizepicks | Courtland Sutton | Rec Targets | under | 0.18479411301214343 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|6af5960a-1d9d-4f3c-ab5d-c2bcd805cfc7 | underdog | Baker Mayfield | Pass Attempts | under | 0.1838540296279383 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|df0fcb9f-5100-4910-b141-a65adc25e74e | underdog | Joe Burrow | Pass Attempts | under | 0.18375588026906453 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|9f26a74b-8f4c-4c6c-8c75-268881535808 | underdog | Byrum Brown | Pass Yards | under | 0.18288023106013962 | 2026-11-06T06:34:07Z | 2026-11-07T17:45:00Z |
| underdog|f4c69603-6218-4437-8fdd-275d6fcfe8ef | underdog | Jason Myers | FG Made | under | 0.1827109251134501 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|211341a3-9825-4471-afb3-2983cc461c69 | underdog | Pete Werner | Sacks | over | 0.18270979216902497 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| prizepicks|16685557 | prizepicks | Justin Herbert | Pass TDs | under | 0.18176877497841348 | 2026-11-05T12:22:13Z | 2026-11-08T16:05:00.000-05:00 |
| underdog|1c0db1c8-fa7a-44b2-9930-6a857ba2ba91 | underdog | K'Lavon Chaisson | Sacks | over | 0.17978981617373657 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|0f6dd14f-41c6-4dfc-ab8c-d9f6791ef944 | underdog | Daylyn Upshaw | Receptions | under | 0.17908539546612534 | 2026-11-06T16:02:47Z | 2026-11-08T00:30:00Z |
| underdog|cfae8805-6e9b-4151-aae5-009efb71986a | underdog | Brock Bowers | Receptions | under | 0.17887742031236042 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| prizepicks|16764334 | prizepicks | Jalen Nailor | Rec Targets | under | 0.17792466796619333 | 2026-11-07T05:59:57Z | 2026-11-08T16:25:00.000-05:00 |
| prizepicks|16764339 | prizepicks | Hunter Henry | Rec Targets | under | 0.17791529772379444 | 2026-11-07T05:59:57Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|a1310588-918d-4510-86a7-bd4a239fec69 | underdog | C.J. Stroud | Pass Attempts | under | 0.17725867468837075 | 2026-11-03T02:21:46Z | 2026-11-08T21:05:00Z |
| underdog|83fdf531-1a1c-459d-b9c6-34b164621fc6 | underdog | Chop Robinson | Sacks | over | 0.17694658079074554 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|9100eaf4-8232-4056-8f1f-336a475cc678 | underdog | Rhamondre Stevenson | Rush Yards | under | 0.17609187646102753 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|3a64bb74-f554-4133-8100-a705c07fec61 | underdog | Jonah Coleman | Rush + Rec Yards | under | 0.17519915897290428 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| underdog|a2ee3b2c-3a41-4508-ad81-1d0ca5c6f707 | underdog | Jared Goff | Pass Attempts | under | 0.17494980056194276 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|03cedfad-8324-45d0-912c-866b25e8ac91 | underdog | Rachaad White | Rush Yards | under | 0.1747980079171697 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|37e126de-fff2-4c67-a157-52b0e4dfbba1 | underdog | Jaylen Wright | Rush Yards | under | 0.1747833961336338 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|58473198-16c0-4f1f-98ce-794fe0d452fd | underdog | Rashee Rice | Receptions | under | 0.17383563925443812 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|08cf2061-fd87-4572-ad89-293508054cf6 | underdog | Mason Graham | Sacks | over | 0.17262353350724963 | 2026-11-06T16:02:47Z | 2026-11-08T18:00:00Z |
| underdog|e67e9ba5-8b23-46cb-a546-85415df91843 | underdog | Luke Fahey | Pass TDs | under | 0.17214479173554886 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|22d007c4-5d23-4435-9e6a-d9aea95af1d2 | underdog | Romello Height | Sacks | over | 0.1721000021783672 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| prizepicks|16719194 | prizepicks | Stefon Diggs | Rec Targets | under | 0.17139963879683195 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|13aa29a4-8a9e-43f5-a6d7-2d727dd925d8 | underdog | Kendre Miller | Rush + Rec Yards | under | 0.1710175182384528 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|fc2c3e80-7a6d-4b89-bc16-d5647edb73dd | underdog | Jackson Kleather | FG Made | over | 0.17099140480563446 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| underdog|afe1bdf8-c20d-4613-ad24-60cc80891977 | underdog | Luther Burden | Receiving Yards | under | 0.1708136555455848 | 2026-11-05T22:06:44Z | 2026-11-09T01:20:00Z |
| prizepicks|16701919 | prizepicks | George Kittle | Recs | under | 0.17046516255208966 | 2026-11-07T05:59:57Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|fffb6531-d47b-40e4-ba8b-ec5a34809f52 | underdog | Cale Hellums | Pass TDs | over | 0.16925020895400672 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| underdog|6268b499-98fa-4069-8241-11ee20410ea6 | underdog | Bo Jackson | Rush Yards | under | 0.16887965113928916 | 2026-11-05T22:06:44Z | 2026-11-07T20:30:00Z |
| underdog|d5030e40-3006-4824-ba3f-2e99ee58ec46 | underdog | Saquon Barkley | Rush + Rec Yards | under | 0.16859915804427605 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|a2c32829-5741-4600-bdac-f990a7052b23 | underdog | Rhamondre Stevenson | Rush + Rec Yards | under | 0.1684921629314633 | 2026-11-03T11:59:28Z | 2026-11-08T21:25:00Z |
| underdog|1e0723e6-39f5-401c-9ecb-73146c38ec61 | underdog | Marvin Harrison | Receptions | under | 0.16835016265867342 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|407ff730-9a50-4ee0-a6e5-2e91574ef6f1 | underdog | Rachaad White | Rush + Rec Yards | under | 0.16822537025107998 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| prizepicks|16718485 | prizepicks | Kyle Pitts Sr. | Rec Targets | under | 0.16781899621209362 | 2026-11-05T22:06:44Z | 2026-11-08T09:30:00.000-05:00 |
| underdog|a8a9bed2-5d3a-4afa-b7f7-de3a2c658f75 | underdog | Jared Goff | Rush Yards | over | 0.1677182366005825 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|ce5575f0-bb41-462f-a7c5-1ad9b1c12b56 | underdog | Eric Wilson | Sacks | over | 0.16745324148343438 | 2026-11-07T05:59:57Z | 2026-11-10T01:15:00Z |
| underdog|cf74ea13-4c83-486b-a699-efa71530a041 | underdog | Amon-Ra St. Brown | Receptions | under | 0.16742438992001507 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|21a1acab-2608-4d98-a630-1f326444c663 | underdog | Jalen Royals | Receiving Yards | over | 0.16685710651601937 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|3c2c0991-0e80-4489-9557-56d68aa8268c | underdog | Wil Lutz | FG Made | under | 0.1665329706004408 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|c7fbbf68-83ff-44a2-a032-87a9503edea0 | underdog | Cairo Santos | FG Made | under | 0.16650636156632292 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|4a902d41-198f-4763-ad4f-c1aabaf04d56 | underdog | Darian Mensah | Pass TDs | over | 0.16623847690906796 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|73f2643f-52d1-490b-a801-df52538bf621 | underdog | Austin Hooper | Receiving Yards | over | 0.16565211889871145 | 2026-11-05T12:22:13Z | 2026-11-08T14:30:00Z |
| underdog|1618355e-edef-449f-bc87-1cc1db3b63f7 | underdog | Tyler Warren | Receiving Yards | under | 0.16541696176617582 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|f3750bd4-2998-4958-948b-378b41f868ef | underdog | Cade Otton | Receiving Yards | under | 0.16512553256579154 | 2026-11-07T05:59:57Z | 2026-11-09T01:20:00Z |
| underdog|14727280-75e6-47c5-aa99-a15c0090d9d3 | underdog | Jadeveon Clowney | Sacks | over | 0.16506617094106288 | 2026-11-06T16:02:47Z | 2026-11-08T21:05:00Z |
| underdog|6b0a254c-fbec-481c-b649-05d1a353bcae | underdog | Harrison Butker | Kicking Points | under | 0.16442129921836235 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|18b57f5b-5104-4c5c-9e62-65e5b6963fff | underdog | Jalen Nailor | Receiving Yards | under | 0.1640019884226247 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|c062087f-1ff6-45d0-998c-daffb90ce602 | underdog | Mark Fletcher Jr. | Receiving Yards | over | 0.16342266388320292 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| underdog|fff5e46e-dcc1-406e-a32c-75974dc225bb | underdog | Efton Chism | Receiving Yards | under | 0.16266623473699537 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|26b34dbd-c8b5-4155-8b09-75b12c1ecd7a | underdog | Stefon Diggs | Receptions | under | 0.1623657419982183 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|5862450c-7de6-4db1-9b65-c3ccfa0529c6 | underdog | Ladd McConkey | Receiving Yards | under | 0.162300971534745 | 2026-11-06T06:34:07Z | 2026-11-08T21:05:00Z |
| underdog|6986991c-1be4-4314-926e-cebf3701f52d | underdog | Arvell Reese | Sacks | over | 0.16160822893044927 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|9ff29ccb-f4c3-4664-9330-39133772a9f1 | underdog | Tucker Kraft | Receptions | under | 0.1615364063191952 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|6fa6b797-97de-4e8d-9665-e5b9a3e71d27 | underdog | Kaelon Black | Rush + Rec Yards | under | 0.16005979420539762 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|528a645e-8439-47f6-91f3-89566cf92574 | underdog | Greg Dulcich | Receptions | under | 0.15981895291377868 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|ccb7af37-6f52-4013-99b6-0b977f2535d6 | underdog | Kingsley Enagbare | Sacks | over | 0.15973360653003466 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|8f289276-834c-4a60-ac19-2b8e634918e6 | underdog | Ollie Gordon | Rush + Rec Yards | under | 0.15941145377301513 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|6abcf9ad-c64b-43c5-ba90-775a263074b1 | underdog | Kenny Minchey | Pass TDs | over | 0.1593946531109242 | 2026-11-07T05:59:57Z | 2026-11-07T23:15:00Z |
| underdog|7d8aca5c-098a-4cd2-ac18-2986be8ea813 | underdog | Matthew Golden | Receptions | under | 0.15935064858874126 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|f91be1d5-74dc-4555-9736-6b8edde55ba9 | underdog | Cooper Kupp | Receptions | under | 0.15901675324842612 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| prizepicks|16718548 | prizepicks | Tucker Kraft | Rec Targets | under | 0.1589344482639552 | 2026-11-05T22:06:44Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|de6281e6-e72c-4f7d-9b19-ea93df015060 | underdog | Drake London | Receptions | under | 0.1588244841998091 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| prizepicks|16718557 | prizepicks | Tyler Warren | Rec Targets | under | 0.15855243884293413 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|26363e50-ce4d-4af5-96f1-fc389dcca744 | underdog | Blake Cashman | Sacks | over | 0.15839987964028668 | 2026-11-07T05:59:57Z | 2026-11-10T01:15:00Z |
| underdog|698f97b3-863e-4773-97b1-02795f52198b | underdog | Dak Prescott | Pass Attempts | under | 0.15742541666457277 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|549e9cef-a3a5-4d2d-80da-e1502e502bd7 | underdog | Tyler Goodson | Rush + Rec Yards | under | 0.15738112185450548 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|e41a0da4-0291-4499-9b1b-ed6fe79cddc8 | underdog | Ollie Gordon | Receiving Yards | under | 0.15660530020212726 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|37b70014-c646-417c-9dda-4626c7ea528a | underdog | Tyler Shough | Pass Attempts | under | 0.15655653928608748 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|0b592d73-46b4-4456-918c-8d00242be932 | underdog | Dawson Knox | Receptions | under | 0.15649493040707285 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|56924a18-ffc6-4e33-a992-256d8235fd2d | underdog | Jordan Faison | Receptions | under | 0.15642286280966766 | 2026-11-05T22:06:44Z | 2026-11-08T00:30:00Z |
| prizepicks|16675752 | prizepicks | J'Koby Williams | Rush Atts | under | 0.15626612680045937 | 2026-11-05T12:22:13Z | 2026-11-07T21:30:00.000-05:00 |
| underdog|12942562-7741-43e6-8b60-7a3b9d1167db | underdog | Magda Linette | Double Faults | under | 0.15603165522454465 | 2026-11-07T05:59:57Z | 2026-11-07T13:40:00Z |
| underdog|d905a533-71d6-4f33-b5cf-e47acac8a884 | underdog | Billy Edwards Jr. | Pass Yards | under | 0.15589085379140033 | 2026-11-07T05:59:57Z | 2026-11-07T17:00:00Z |
| prizepicks|16763487 | prizepicks | Malik Willis | Pass+Rush+Rec TDs | under | 0.1558092367821141 | 2026-11-07T05:59:57Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|dc298725-6b1d-47d4-8dac-3617ff5e42ae | underdog | Jordan Mason | Rush Yards | under | 0.15576327193870432 | 2026-11-06T16:02:47Z | 2026-11-10T01:15:00Z |
| underdog|e87908ef-c5c6-44c2-9c92-cef0106c5c75 | underdog | Blake Barnett | Total TDs | under | 0.15566718269549085 | 2026-11-07T05:59:57Z | 2026-11-07T18:00:00Z |
| underdog|8898d1df-cad0-48ed-9aab-c49b53a783d1 | underdog | Adetomiwa Adebawore | Sacks | over | 0.15560774164609692 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|02524fc1-2c2c-4351-9030-2facb6210680 | underdog | Sam LaPorta | Receiving Yards | under | 0.15480965770515087 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| prizepicks|16747853 | prizepicks | Omar Cooper Jr. | Rec Targets | under | 0.15377247066602107 | 2026-11-07T05:59:57Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|532d33d0-64eb-4500-bfe5-8f549e052fa2 | underdog | Tory Horton | Receptions | under | 0.15338264840885663 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|b3ceb3cb-33f0-446d-a058-dddfaa2a7301 | underdog | Jacobo Echeverria Lozano | FG Made | over | 0.1533441022676829 | 2026-11-05T22:06:44Z | 2026-11-07T17:30:00Z |
| underdog|c3a8e703-937f-4b67-87af-d63af0313595 | underdog | Liam Boyd | XP Made | over | 0.15303281462856144 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|f31632ab-697b-47b3-a647-5a82eb0defa9 | underdog | James Houston | Sacks | over | 0.15251939631897432 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| prizepicks|16718455 | prizepicks | Trey McBride | Rec Targets | under | 0.1522364381770983 | 2026-11-05T22:06:44Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|dea50bd8-dac4-4230-8d1a-ba7397c222aa | underdog | Jake Elliott | Kicking Points | under | 0.1517957553250162 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|cb8a7959-37d5-4d0e-b9e9-d1149ed712c1 | underdog | Jordan Mason | Rush + Rec Yards | under | 0.1517324211162261 | 2026-11-07T05:59:57Z | 2026-11-10T01:15:00Z |
| prizepicks|16718472 | prizepicks | Drake London | Rec Targets | under | 0.15145440458702286 | 2026-11-05T22:06:44Z | 2026-11-08T09:30:00.000-05:00 |
| underdog|04c2b5c2-1fd7-497c-9390-1f0f58b1d195 | underdog | DeForest Buckner | Sacks | over | 0.15102958799908306 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|b2b3468d-c1e9-49b8-856f-d0397a899334 | underdog | Alvin Kamara | Rush Yards | under | 0.15094440136484844 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|30134834-5074-4d86-8b64-95e2d04921fb | underdog | Akheem Mesidor | Sacks | over | 0.15079011479236937 | 2026-11-07T05:59:57Z | 2026-11-08T21:05:00Z |
| prizepicks|16718538 | prizepicks | Jonah Coleman | Rec Targets | under | 0.15073744374037423 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|7adbcb60-fb8e-4713-afc1-f7cf4af22909 | underdog | Zane Gonzalez | FG Made | under | 0.15052117503385665 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|fb92b870-f8fc-4382-bb4a-e7dc0d0bd054 | underdog | Ted Hurst | Receiving Yards | under | 0.15035485870905774 | 2026-11-07T05:59:57Z | 2026-11-09T01:20:00Z |
| underdog|5eea8199-5dbe-4649-a20a-2405bd63d177 | underdog | Jaxon Smith-Njigba | Receptions | under | 0.15026450962994486 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|42d092cc-c62c-45cf-88dd-cebcde7f86d3 | underdog | Darius Cooper | Receptions | under | 0.15015667703429225 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|d0e344fe-0a79-4dad-a9fd-6d477eff98c4 | underdog | Keion White | Sacks | over | 0.1496843494227773 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|7f44b052-27a1-42a5-8108-ca43bdfcb5bb | underdog | Chuba Hubbard | Rush + Rec Yards | under | 0.14959006456056478 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|e0c22419-0dff-4556-a05e-9acfa3ab7a09 | underdog | Brandon Aubrey | FG Made | under | 0.14958269462275497 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|b0ce99d7-ccca-47c0-a454-e6f920eab8e2 | underdog | Bo Nix | Pass TDs | under | 0.14921921703126695 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|cbdf09ae-f630-4eb9-af31-a11d7f637572 | underdog | Jackson Kleather | XP Made | over | 0.14881354680064662 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| underdog|69ba3a63-bb92-4f39-984a-ed5566438f78 | underdog | Nick Folk | FG Made | under | 0.1481435952641591 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|c4587fdc-fe2d-47dc-997d-d0b08663b00a | underdog | Ka'imi Fairbairn | FG Made | under | 0.1479318682678138 | 2026-11-03T02:21:46Z | 2026-11-08T21:05:00Z |
| underdog|1b370830-3867-4ade-9a8d-418a06dbd1c1 | underdog | Christian Watson | Receptions | under | 0.1479168165648339 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|0d4c6cfb-de76-4218-a701-c556a938fb8d | underdog | Bear Bachmeier | Pass TDs | over | 0.14781543153753518 | 2026-11-07T05:59:57Z | 2026-11-07T17:00:00Z |
| underdog|2484637b-dd6a-4882-be40-ce0e68d4e559 | underdog | Kenny Gainwell | Receptions | under | 0.1475602481670133 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|13d49fc8-9559-45e1-9bac-6f15a20a2c72 | underdog | Ollie Gordon | Receptions | under | 0.14682805397570908 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| prizepicks|16718558 | prizepicks | Rashee Rice | Rec Targets | under | 0.14673204243829352 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|ad5841e3-f51c-4e2d-a883-064eb9b2257f | underdog | Malik Washington | Receptions | under | 0.14645959659878283 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|f57c0032-b5b1-4228-af7c-d6bb6f08e67e | underdog | Emeka Egbuka | Receptions | under | 0.1460648049345178 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|b5acd5c8-143c-4860-995f-2366f9a662f7 | underdog | Kalieb Osborne | Pass TDs | over | 0.1460045485512973 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|d85a1cad-b5a6-47ea-b06c-bdafe9c3c797 | underdog | Ben Yurosek | Receiving Yards | over | 0.14559715708175824 | 2026-11-07T05:59:57Z | 2026-11-10T01:15:00Z |
| underdog|72935fa4-465c-4354-a696-7c61c0ca891f | underdog | Jesse Legree | Receptions | under | 0.14506295421143045 | 2026-11-06T16:02:47Z | 2026-11-08T03:30:00Z |
| underdog|a5687c54-7273-4922-8cf8-a0383ebb4afa | underdog | Trey McBride | Receiving Yards | under | 0.14497443435005852 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|9e881772-2cab-49d1-98b4-4a20360513e2 | underdog | Osa Odighizuwa | Sacks | over | 0.14450890275099865 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|16b01cae-a42d-4c7f-86cc-d05b5ca88fce | underdog | Trinidad Chambliss | Pass Yards | under | 0.14383809485501364 | 2026-11-05T22:06:44Z | 2026-11-08T00:30:00Z |
| underdog|941b56c8-ad29-471c-986f-fba334187fce | underdog | Marvin Harrison | Receiving Yards | under | 0.143598479908011 | 2026-11-07T05:59:57Z | 2026-11-08T21:05:00Z |
| underdog|d1ad5738-520b-4373-b127-b15ab45c351a | underdog | Jaxon Smith-Njigba | Receiving Yards | under | 0.14355065406302003 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|a761c371-7b4a-476a-8c8f-cc6724d3bbe9 | underdog | Elijah Mitchell | Rush Yards | under | 0.14326354478391035 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|d88bebf6-1f92-4275-b707-d4301ca0f0f0 | underdog | Mason McKenzie | Total TDs | under | 0.14264624173321128 | 2026-11-07T05:59:57Z | 2026-11-07T17:00:00Z |
| underdog|9dd26bb3-66ee-4b2b-a885-d1637fe0157c | underdog | Montez Sweat | Sacks | over | 0.14167101106208047 | 2026-11-07T05:59:57Z | 2026-11-09T01:20:00Z |
| underdog|17c2615c-c738-4c56-9130-b5fe441bf0f0 | underdog | Kenneth Williams | Rush Yards | under | 0.14150700363411983 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| underdog|1acc37b7-16ae-4dfe-9876-857c87ea3b17 | underdog | Quentin Johnston | Receiving Yards | under | 0.1413979010411639 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|3389df2b-6562-4259-9cf1-6f54c8f866e9 | underdog | Walker Eget | Pass Yards | under | 0.1410353141986187 | 2026-11-05T22:06:44Z | 2026-11-07T17:30:00Z |
| underdog|ef1c0be0-812d-44f6-9397-3e1355f6994d | underdog | Rocco Becht | Pass TDs | over | 0.14073851519469394 | 2026-11-05T22:06:44Z | 2026-11-07T20:30:00Z |
| underdog|19182bf3-3972-4fb8-ad6e-ff29a13cff8c | underdog | Chase Brown | Rush Yards | under | 0.13989207436771856 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|8b40fd14-adb3-47ff-866a-2f2dbd8bb371 | underdog | Tutu Atwell | Receptions | under | 0.13968039382130393 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|d750f1b4-ebcd-49c0-9b03-97137f1f422f | underdog | Carson Wentz | Rush Yards | under | 0.1396304799819178 | 2026-11-05T22:06:44Z | 2026-11-10T01:15:00Z |
| underdog|e1775404-5113-460c-9eec-b13c0226b55b | underdog | Olamide Zaccheaus | Receptions | under | 0.1396223249639138 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|e8a0cf82-8318-4dd2-ab55-ad25e07ea0af | underdog | Javon Tracy | Receptions | under | 0.13935717251562496 | 2026-11-07T05:59:57Z | 2026-11-07T17:00:00Z |
| underdog|e42ef2e3-8dca-4bed-b445-63f2f22ce402 | underdog | Kemper Hodges | Rush Yards | under | 0.1393189799110066 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| underdog|03e0d95d-f3f0-4f64-bea2-e9e8bbb684e3 | underdog | AJ Barner | Receptions | under | 0.13910664132787998 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|8b11a49e-1f76-4d12-9052-b165b603495e | underdog | Makai Lemon | Receptions | under | 0.13853947895546503 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|3c114bc2-839b-4e55-9ec0-5de96e8522a9 | underdog | Caleb Douglas | Receptions | under | 0.1384724673367177 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|5df51a97-b605-4c0d-b9a5-6038554d83e4 | underdog | Amon-Ra St. Brown | Receiving Yards | under | 0.13837637499846278 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|83b965d9-e75e-4d7b-8886-44573ffbcdfb | underdog | Dilin Jones | Rush Yards | under | 0.13798927114368054 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|ab666f53-3f97-4d16-9e8b-997aaaba0cfc | underdog | Kaelon Black | Rush Yards | under | 0.1371496838847872 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|62752957-b2d2-43f1-8caa-62560a2db86a | underdog | Brock Purdy | Pass TDs | under | 0.13705484641190113 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|e9e775c1-e65e-481a-8e80-4451df551d94 | underdog | James Cook | Receptions | under | 0.13675024566789118 | 2026-11-05T22:06:44Z | 2026-11-10T01:15:00Z |
| underdog|e51659c8-5120-4ea6-8cda-0855726b1435 | underdog | Matthew Stafford | Pass Attempts | under | 0.13674658781617022 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| underdog|af5adabc-bebb-4583-a724-ec24ce745588 | underdog | Cooper Kupp | Receiving Yards | under | 0.13648768280929058 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|f51527ca-57c4-493e-a8c4-957bb43c94a5 | underdog | Jahmyr Gibbs | Rush + Rec Yards | under | 0.1362414547608164 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|f8bf5f47-2588-4a90-b8b2-56da915487ad | underdog | Lincoln Kienholz | Total TDs | under | 0.1361731298012243 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| underdog|a0563313-b8f6-4974-a05b-d5e6a15f4169 | underdog | Barryn Sorrell | Sacks | over | 0.13529244398588483 | 2026-11-06T16:02:47Z | 2026-11-08T21:25:00Z |
| underdog|d6cbee1a-cecf-45c3-92bd-590b34f8135a | underdog | Nick Folk | Kicking Points | under | 0.1351811208582573 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|66507112-ab94-4d1a-8c46-b47d9c9feac9 | underdog | Isaiah McGuire | Sacks | over | 0.134580924202244 | 2026-11-06T16:02:47Z | 2026-11-08T18:00:00Z |
| underdog|1c7fca18-3551-4899-a491-ecbe9d6cea9b | underdog | Bijan Robinson | Rush + Rec Yards | under | 0.13456240647252893 | 2026-11-06T16:02:47Z | 2026-11-08T14:30:00Z |
| underdog|0a1d4a28-f4ed-433b-a45b-953e95969acb | underdog | Jadarian Price | Receptions | under | 0.13399424688283068 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|2a5c61aa-250d-4225-a934-f6373d8e7821 | underdog | Savion Hiter | Rush Yards | under | 0.13384746886731413 | 2026-11-06T16:02:47Z | 2026-11-08T00:30:00Z |
| underdog|5790a889-8601-4824-ac78-b9c766ba1891 | underdog | Marvin Mims Jr. | Receptions | under | 0.13357422686133513 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|57fb6acd-6aa0-4948-a9fd-fd2437835618 | underdog | Austin Ekeler | Rush + Rec Yards | under | 0.13340078478837036 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|5ebe042f-0411-409e-958b-f2fce6dcbd98 | underdog | Devin Singletary | Receiving Yards | under | 0.1330346125830013 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|290aae16-44ea-44db-878b-286c352fe54b | underdog | Josh Sweat | Sacks | over | 0.13238191021882117 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|5401c857-2a59-4661-833b-05097fd12d90 | underdog | Demond Williams | Total TDs | under | 0.13238087381379038 | 2026-11-07T05:59:57Z | 2026-11-07T20:30:00Z |
| prizepicks|16718540 | prizepicks | Amon-Ra St. Brown | Rec Targets | under | 0.13196308606307305 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|f3261195-1b3a-49d4-b1b9-944aba364e1b | underdog | Alonza Barnett | Total TDs | under | 0.13195395645064156 | 2026-11-07T05:59:57Z | 2026-11-07T20:45:00Z |
| underdog|e3eafc58-286e-42f2-b4ee-056ef1f4f612 | underdog | Chig Okonkwo | Receiving Yards | under | 0.13137551735878683 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|6856bd41-edf8-48c4-a2b6-b84819ec4ae5 | underdog | Marcel Reed | Pass Yards | under | 0.13137009479314776 | 2026-11-05T22:06:44Z | 2026-11-07T20:00:00Z |
| underdog|6a4ea7ca-8051-400b-a435-f94e0a7067ee | underdog | Jameson Williams | Receiving Yards | under | 0.131077359753479 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|1fe6e8b8-cac6-4226-9aae-720046537852 | underdog | Chris Jones | Sacks | under | 0.13058136732118086 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|b0c497f1-a404-41ae-9572-74da843984b3 | underdog | MarShawn Lloyd | Receiving Yards | over | 0.13020219018489343 | 2026-11-06T16:02:47Z | 2026-11-08T21:25:00Z |
| underdog|896c369b-dfe7-4cdf-816a-54fd6d2a64c6 | underdog | Darius Cooper | Receiving Yards | under | 0.12982985729704266 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|14d37ea9-87e7-4e15-ad26-f93259d0facd | underdog | Drew Lock | Pass TDs | under | 0.12966967278207253 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| prizepicks|16718556 | prizepicks | Jonathan Taylor | Rec Targets | under | 0.12923033670188888 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|40e5a0ef-776f-47dc-991d-3b3c24cfdabb | underdog | Efton Chism | Receptions | under | 0.12920163225844472 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|3aa93bf4-8e56-4a6e-8771-99a3e7b252f0 | underdog | Kaleb Edwards | Receiving Yards | over | 0.1291255418811703 | 2026-11-05T12:22:13Z | 2026-11-07T20:30:00Z |
| underdog|8a77a4e3-ad8b-4d5e-962d-b25ce8bf9a4d | underdog | Jared Curtis | Pass Yards | under | 0.1288672358376597 | 2026-11-05T22:06:44Z | 2026-11-07T21:15:00Z |
| underdog|ccfe2bba-71d1-4e46-bf46-d00e2a8c975c | underdog | Javonte Williams | Rush + Rec Yards | under | 0.12875496760840743 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|5869b7ef-5cbd-40b2-b17d-2b4591a92144 | underdog | Matthew Golden | Receiving Yards | under | 0.12870107458299462 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|7a288207-299b-4695-b585-940ac0294fdc | underdog | Luke Fahey | Pass Yards | under | 0.12864978345130762 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| prizepicks|16750496 | prizepicks | Dierre Hill Jr. | Rush Atts | under | 0.12748253428509304 | 2026-11-07T05:59:57Z | 2026-11-07T15:30:00.000-05:00 |
| underdog|f9408da3-4c03-47a1-91ac-c4ac94507742 | underdog | Drake London | Receiving Yards | under | 0.12714827801752404 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|76e6cc64-cc3a-46d3-8690-4230bd756233 | underdog | Rome Odunze | Receiving Yards | under | 0.1268651524326092 | 2026-11-06T06:34:07Z | 2026-11-09T01:20:00Z |
| underdog|ae0024e2-e6f7-4496-90a2-739f7b072ef9 | underdog | Jaylen Waddle | Receiving Yards | under | 0.12663902325289267 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|27f67693-fa31-45d9-8812-41afd1687e68 | underdog | Junior Sherrill | Receptions | under | 0.12629619877526765 | 2026-11-05T22:06:44Z | 2026-11-07T21:15:00Z |
| underdog|718f4381-f4aa-4349-8ddf-87b76363c39b | underdog | Pat Bryant | Receptions | under | 0.1253436724768694 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|b78af82a-6121-4425-9929-49b0396c30fe | underdog | J.J. McCarthy | Rush Yards | under | 0.1251574833333048 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|4571a1eb-0784-4ead-88bd-ea8d6a67b552 | underdog | Boye Mafe | Sacks | over | 0.12473116706289278 | 2026-11-07T05:59:57Z | 2026-11-08T14:30:00Z |
| underdog|5adfe6e8-e91f-44dd-842d-5be373846225 | underdog | Chris Olave | Receptions | under | 0.12468750167033804 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|58790b19-dd02-48db-9994-baaab8acbb8b | underdog | Rachaad White | Receptions | under | 0.12456515053371986 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|831816f5-127a-4ad6-940a-256afa82be52 | underdog | Isaiah Marshall | Total TDs | under | 0.12448898601494052 | 2026-11-07T05:59:57Z | 2026-11-07T20:45:00Z |
| underdog|80af3a76-a6e2-4ad2-ac92-48eac9389557 | underdog | Luis Rodriguez | FG Made | over | 0.12411479613558368 | 2026-11-06T16:02:47Z | 2026-11-07T18:00:00Z |
| underdog|abe5fb36-b140-496d-8138-08cf2021eab6 | underdog | Jayden Daniels | Pass TDs | under | 0.12401048501725953 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|a5a84e5b-2d1a-407b-ad40-5e0faa4d1d12 | underdog | Wil Lutz | Kicking Points | under | 0.12375220362671835 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|6fa07966-69ad-4e19-932b-f21a9e51b66b | underdog | Ollie Gordon | Rush Yards | under | 0.12319862002616433 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|09f01959-ca96-4222-92c2-371c26012979 | underdog | George MacIntyre | Pass Yards | under | 0.12295647142573496 | 2026-11-06T16:02:47Z | 2026-11-07T23:15:00Z |
| underdog|a75d0892-12c3-4a3d-bea7-a07236a8702c | underdog | Conner Weigman | Pass Yards | under | 0.12251598812778575 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|1201b560-8b4d-42d0-a55c-a46f4bb3c3b4 | underdog | Seth McGowan | Rush + Rec Yards | under | 0.12244206340619479 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|f3d5e2f8-b078-48d2-b5d6-54ca6ca199e6 | underdog | Cairo Santos | Kicking Points | under | 0.12236507723893952 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|5b41e18b-fe87-4483-b80d-3133407033e6 | underdog | Hunter Henry | Receptions | under | 0.12233979989646315 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|bf5c8287-a719-4bc8-a84d-21b682a39a7b | underdog | Kenny Gainwell | Receiving Yards | under | 0.12233318149565453 | 2026-11-05T12:22:13Z | 2026-11-09T01:20:00Z |
| underdog|4e28084d-f1eb-4a2f-8137-29d9def7b365 | underdog | Kendre Miller | Rush Yards | under | 0.12201969500814158 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|9a6bf26d-777c-4ed1-a55d-58f8fc621644 | underdog | Kaelon Black | Receptions | under | 0.12200046497800188 | 2026-11-06T06:34:07Z | 2026-11-08T21:25:00Z |
| underdog|06a98b20-5b6a-4641-963b-748d6b6ac027 | underdog | Ja'Marr Chase | Receptions | under | 0.12198379656106328 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|cc098e45-ccc0-4139-b477-e6e52ec1417e | underdog | Hunter Henry | Receiving Yards | under | 0.12177355998086026 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| prizepicks|16719168 | prizepicks | Caleb Douglas | Rec Targets | under | 0.12141200380041606 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|16510e89-3e9d-4b33-9549-19154015507d | underdog | Tyler Allgeier | Receptions | under | 0.12089928730863053 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|c9b4676b-7e29-4e74-b6db-88fe1c329530 | underdog | Elija Lofton | Receptions | under | 0.12074661100876782 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| underdog|1d0d1a24-84f2-494e-b408-57fa31871b73 | underdog | Maxx Crosby | Sacks | over | 0.12068546506850075 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| prizepicks|16747855 | prizepicks | Mason Taylor | Rec Targets | under | 0.12041082710254603 | 2026-11-07T05:59:57Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|03b3eb0d-b146-440d-843d-79223ef0bf2b | underdog | Jahan Dotson | Receptions | under | 0.1200345581620813 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| prizepicks|16619686 | prizepicks | Chris Dawn Jr. | Recs | under | 0.11978140668783599 | 2026-11-04T12:10:41Z | 2026-11-07T22:30:00.000-05:00 |
| prizepicks|16576409 | prizepicks | Christian McCaffrey | Rush Yards | under | 0.11950744181162642 | 2026-11-03T02:21:46Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|c7bb0bb6-dc60-4c38-93e2-684dacb04b02 | underdog | Josh Allen | Pass TDs | under | 0.11926653211048077 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|2b68b5b9-1589-40de-8c77-e9c12e25c3a5 | underdog | Drew Mestemaker | Pass Yards | under | 0.11898504991735337 | 2026-11-07T05:59:57Z | 2026-11-07T18:00:00Z |
| underdog|33ffb548-94a1-44e7-9da3-17dc0d7f1d49 | underdog | J'Koby Williams | Receiving Yards | over | 0.11825318810941854 | 2026-11-04T12:10:41Z | 2026-11-08T02:30:00Z |
| underdog|f4bfe3bd-d628-4573-9415-7680b5b2c40d | underdog | CeeDee Lamb | Receiving Yards | under | 0.11812765591021201 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|1c07119d-7fe4-4eba-b8f2-c7008e344979 | underdog | Harold Fannin | Receptions | under | 0.11801150156707052 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|eccd30c3-ed5b-4cc6-aad4-06299d22c529 | underdog | Malik Nabers | Receptions | under | 0.11783962166306128 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|2d49afa9-bf55-4cd2-8efe-1f0dc62786fc | underdog | Tait Reynolds | Pass TDs | under | 0.11668508117452292 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|2ffb2fff-77a4-4abe-8a15-f1d4564e0592 | underdog | Keelon Russell | Pass TDs | over | 0.11664993848736266 | 2026-11-05T22:06:44Z | 2026-11-07T20:30:00Z |
| underdog|a2c99cc9-08b9-47ba-a659-2ab43cdbd1d8 | underdog | Saquon Barkley | Rush Yards | under | 0.1165322243623439 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|b97ea732-c9bd-475b-9b65-9472160330d6 | underdog | Colby Wooden | Sacks | over | 0.11627675972376245 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|c3130728-988e-4cdf-9fa4-96cbff03e330 | underdog | Kyren Williams | Rush Yards | under | 0.11604746503488483 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|6efc22a4-0d91-487b-822d-d7f27a3218b2 | underdog | George MacIntyre | Pass TDs | under | 0.11581459797425153 | 2026-11-05T12:22:13Z | 2026-11-07T23:15:00Z |
| underdog|649d4cf3-3d96-4754-b6ba-149b97bba842 | underdog | Kenneth Walker III | Receptions | under | 0.11559688528805712 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|0f9ce4d1-2444-4f3f-95ac-925550a22ae5 | underdog | Gage LaDue | Rush Yards | under | 0.11556512515389195 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| underdog|9825e0ba-f877-4bf7-812c-f9129d57348c | underdog | Patrick Mahomes | Pass TDs | under | 0.11537751808865182 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|0deea4e6-05e4-4225-8d6c-cbb0e6843919 | underdog | Bijan Robinson | Rush Yards | under | 0.11533915091880831 | 2026-11-06T16:02:47Z | 2026-11-08T14:30:00Z |
| underdog|0f36cfe0-2748-4fa2-b50e-3ea3b3076149 | underdog | Jeremiah Cobb | Rush Yards | under | 0.11531829757558598 | 2026-11-07T05:59:57Z | 2026-11-07T17:45:00Z |
| underdog|df8cc29e-c9c7-46e3-9773-066f25acc7a6 | underdog | CeeDee Lamb | Receptions | under | 0.11512462845971994 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|5334039e-1617-41f9-b7fd-e419fb6bce7e | underdog | Roschon Johnson | Receiving Yards | over | 0.11497715109531126 | 2026-11-07T05:59:57Z | 2026-11-09T01:20:00Z |
| prizepicks|16718536 | prizepicks | Jaylen Waddle | Rec Targets | under | 0.11494202569891032 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|2e063984-c9f0-457e-90a8-3e51d56586ae | underdog | Thomas Castellanos | Rush Yards | under | 0.11476512458112476 | 2026-11-07T05:59:57Z | 2026-11-08T02:30:00Z |
| prizepicks|16764340 | prizepicks | Kyle Williams | Rec Targets | under | 0.11404754178635423 | 2026-11-07T05:59:57Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|3a5ae6bb-5bc7-48b9-b294-74e6475ea418 | underdog | DeMario Douglas | Receptions | under | 0.11403945725604647 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|2608df37-9cb1-4e77-ab6e-559449ba8a70 | underdog | Marcel Reed | Pass TDs | under | 0.11387285965261762 | 2026-11-05T22:06:44Z | 2026-11-07T20:00:00Z |
| underdog|bc4e2511-6040-4a80-9398-a16ad8530216 | underdog | Keenan Allen | Receiving Yards | under | 0.11353905024788158 | 2026-11-06T16:02:47Z | 2026-11-08T18:00:00Z |
| underdog|8dda3f2c-43bd-496a-91aa-283c7a072e7b | underdog | Chuba Hubbard | Receptions | under | 0.11351803648802827 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|48228a58-a613-4e86-a016-564193407916 | underdog | Tate Sandell | FG Made | over | 0.11341177760495819 | 2026-11-06T16:02:47Z | 2026-11-08T00:45:00Z |
| underdog|fdc2cba3-5628-496b-92fe-05b5d00d90e6 | underdog | Braylon Staley | Receptions | under | 0.11333666895548766 | 2026-11-05T12:22:13Z | 2026-11-07T23:15:00Z |
| underdog|980ef0c9-e7c6-40c1-ae91-d71c59322e06 | underdog | Travis Kelce | Receptions | under | 0.11333613992057967 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|48e760c2-4eac-4eb7-a8a9-531f0ca1ef83 | underdog | Ryan Fitzgerald | Kicking Points | under | 0.11326096940715735 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|014ae5b3-7060-4465-9773-3eb5afda3c88 | underdog | Jauan Jennings | Receptions | under | 0.11315886516593598 | 2026-11-07T05:59:57Z | 2026-11-10T01:15:00Z |
| prizepicks|16747632 | prizepicks | Matthew Golden | Recs | under | 0.11305017989971933 | 2026-11-07T05:59:57Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|3b806c99-c348-44de-86cc-461e6cf2d3f2 | underdog | Jake Bates | FG Made | under | 0.11285240847954703 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|36391894-b67e-489e-a9ba-6d5745343435 | underdog | Nate Adkins | Receiving Yards | over | 0.11258180819122365 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| prizepicks|16577048 | prizepicks | George Pickens | Rec Yards | under | 0.11245540278204647 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|f48da050-199d-44b1-b56e-450cb1cc55b9 | underdog | Raleek Brown | Receiving Yards | over | 0.11219282113360729 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|e14b44d7-6880-4cde-a5d0-be585bd64366 | underdog | Denzel Boston | Receptions | under | 0.11215354306007119 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|fadb69a5-2f84-42de-a83a-f7bd3242f9db | underdog | Greg Dulcich | Receiving Yards | under | 0.1120073367268899 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|3613f79c-7561-44de-9383-40ad6756dd4c | underdog | DeSean Bishop | Rush Yards | under | 0.11160184109299542 | 2026-11-07T05:59:57Z | 2026-11-07T23:15:00Z |
| underdog|d057f822-2dbd-4436-adc8-eadda12bcc00 | underdog | Tim Patrick | Receiving Yards | under | 0.11158456730208843 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| underdog|f3f39226-3573-463d-bbd7-3f0178e7ebdf | underdog | Alvin Kamara | Rush + Rec Yards | under | 0.11139213822218441 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|ba27855c-f306-460f-8d0b-850a557fe3e5 | underdog | James Cook | Rush + Rec Yards | under | 0.11131941599424644 | 2026-11-04T12:10:41Z | 2026-11-10T01:15:00Z |
| prizepicks|16719170 | prizepicks | Greg Dulcich | Rec Targets | under | 0.1112945325708179 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|fc8e948f-e862-45a9-9635-07a454ffb0a7 | underdog | J.K. Dobbins | Receiving Yards | over | 0.11121136707341117 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| underdog|0e6f2449-c494-4814-bbd6-ca8c5b7337d2 | underdog | Chris Dawn | Receiving Yards | under | 0.11070492518822139 | 2026-11-07T05:59:57Z | 2026-11-08T03:30:00Z |
| underdog|4781b322-c16f-488a-b23d-ff4462376142 | underdog | Matthew Stafford | Pass TDs | under | 0.11063723570251016 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| prizepicks|16719176 | prizepicks | Rhamondre Stevenson | Rec Targets | under | 0.1104895168364537 | 2026-11-05T22:06:44Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|1fecccd3-7915-4b3d-9923-95b353ee0c90 | underdog | J.K. Dobbins | Receptions | under | 0.11024990718515137 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|cb8fe87c-c267-4e98-8768-a199b4f8338b | underdog | Simi Fehoko | Receptions | under | 0.11023737676758572 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| prizepicks|16758738 | prizepicks | Adrian Mannarino | Total Games | over | 0.11000801191540133 | 2026-11-07T05:59:57Z | 2026-11-07T08:50:00.000-05:00 |
| prizepicks|16685556 | prizepicks | Dak Prescott | Pass TDs | under | 0.10986040123516894 | 2026-11-05T12:22:13Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|87ced712-c478-425d-ab92-8115cd35eba6 | underdog | Lincoln Kienholz | Pass TDs | under | 0.10982554717127524 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|685edd25-24fb-4af2-a25d-548ec56bea29 | underdog | Tyler Warren | Receptions | under | 0.10969276868099631 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|0c982e54-179a-4101-a215-70855b7eaf00 | underdog | D'Andre Swift | Receptions | under | 0.10961929542717408 | 2026-11-05T12:22:13Z | 2026-11-09T01:20:00Z |
| underdog|b842a878-03ae-4920-8675-e8b6372b0b0d | underdog | KC Concepcion | Receiving Yards | under | 0.10961606364164644 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| prizepicks|16722858 | prizepicks | Kyle Juszczyk | Rec Targets | under | 0.10961448099981719 | 2026-11-06T06:34:07Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|b34d3248-ec10-4121-9c7b-b4746dee816d | underdog | Charlie Kolar | Receptions | under | 0.10960132616239582 | 2026-11-05T12:22:13Z | 2026-11-08T21:05:00Z |
| underdog|57815146-a656-43d6-9668-35d136e67d23 | underdog | Devon Dampier | Pass Yards | under | 0.10960047075501667 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|69a82857-d297-4b15-a385-2a023ebcf054 | underdog | Dalton Kincaid | Receptions | under | 0.10948029145485216 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|ba47c124-db10-4b69-b5cf-5ba62f5c4d37 | underdog | Jahmyr Gibbs | Receptions | under | 0.10946590257471323 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|3cd2b418-6262-4bea-8204-d5c65be18a7d | underdog | Adonai Mitchell | Receptions | under | 0.10924843875645252 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|b839652f-0e46-467f-9992-35c5469cf144 | underdog | D'Andre Swift | Receiving Yards | under | 0.10895292459147943 | 2026-11-05T12:22:13Z | 2026-11-09T01:20:00Z |
| underdog|b013ebe8-ebe5-49ab-bca5-9dc91172a347 | underdog | Sam Leavitt | Pass Yards | under | 0.1086995785134075 | 2026-11-07T05:59:57Z | 2026-11-07T20:30:00Z |
| underdog|869fd267-0830-4342-93d3-5dd40662de63 | underdog | Kanoah Vinesett | FG Made | over | 0.10836586366933354 | 2026-11-05T22:06:44Z | 2026-11-07T17:30:00Z |
| underdog|d7069825-963a-42c2-8f57-2a72e8bd8f60 | underdog | Cayden Lee | Receptions | under | 0.10835640160204774 | 2026-11-07T05:59:57Z | 2026-11-07T17:00:00Z |
| underdog|2a03ddda-093f-4ef6-a512-af233e05477d | underdog | Chad Ryland | FG Made | over | 0.10832807545342293 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|7182897d-112d-4bbe-8f0b-571fe8c23a77 | underdog | Cam Cook | Receiving Yards | over | 0.10825855385349281 | 2026-11-05T12:22:13Z | 2026-11-08T02:30:00Z |
| underdog|f9939d8d-e8e7-430a-a317-6ed41f3f532f | underdog | Khalil Mack | Sacks | over | 0.10825235349267631 | 2026-11-07T05:59:57Z | 2026-11-08T21:05:00Z |
| underdog|4c17b548-6dd0-41a7-be94-4eeba93de71a | underdog | Nico Collins | Receptions | under | 0.10808570977681886 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|a62e4f9b-09d4-4c48-9347-428cc536d6b2 | underdog | Byrum Brown | Total TDs | under | 0.10756501336963253 | 2026-11-07T05:59:57Z | 2026-11-07T17:45:00Z |
| underdog|1022f42b-a007-4d3a-b5ed-9a614c441a49 | underdog | Tim Patrick | Receptions | under | 0.10753144499846912 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| prizepicks|16722855 | prizepicks | Christian McCaffrey | Rec Targets | under | 0.10741475862792937 | 2026-11-06T06:34:07Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|78f9496e-f6e5-43f5-8498-67f840fb3218 | underdog | George Pickens | Receiving Yards | under | 0.10727572162247179 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| prizepicks|16764730 | prizepicks | Magda Linette | Double Faults | under | 0.10697412028131958 | 2026-11-07T05:59:57Z | 2026-11-07T08:40:00.000-05:00 |
| underdog|1b7021b4-b333-4256-bc1e-7c9f88464431 | underdog | Jonah Coleman | Receptions | under | 0.10693828108030978 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|5be18191-a04f-4092-a1cd-458a07b6ec60 | underdog | Savion Williams | Receptions | under | 0.10693644241407008 | 2026-11-05T22:06:44Z | 2026-11-08T21:25:00Z |
| underdog|5ab82051-a064-47b2-8021-52ba43560c79 | underdog | Conner Weigman | Total TDs | under | 0.10676649434244134 | 2026-11-07T05:59:57Z | 2026-11-07T20:30:00Z |
| underdog|d599a5ae-1ff8-4df6-9eac-c397c998888d | underdog | Colston Loveland | Receptions | under | 0.10664747026618215 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|32711800-db27-440c-a743-4d137cde2fad | underdog | Breece Hall | Rush + Rec Yards | under | 0.10656138323472575 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|1707d15e-91ac-4357-aa4f-c6f1e93ab1ba | underdog | Fluff Bothwell | Rush Yards | under | 0.10641678526793563 | 2026-11-06T16:02:47Z | 2026-11-07T21:15:00Z |
| underdog|5b61aab8-a7d2-414b-8490-9bbaa9548e23 | underdog | Jordan Watkins | Receptions | under | 0.10633140598140345 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|60ec289f-7b77-41f0-bbf9-3e683c8cbf11 | underdog | Jack Cassidy | XP Made | over | 0.10622021739551402 | 2026-11-06T16:02:47Z | 2026-11-08T02:30:00Z |
| underdog|552d6ed3-57fe-4ea3-8bd6-3bcec6e29b71 | underdog | Jordan Addison | Receiving Yards | under | 0.10614115606118668 | 2026-11-05T22:06:44Z | 2026-11-10T01:15:00Z |
| underdog|e5e1e737-f54e-41c9-b53a-20d0cd8f6afb | underdog | LaNorris Sellers | Pass Yards | under | 0.1061346822098691 | 2026-11-05T22:06:44Z | 2026-11-07T20:00:00Z |
| underdog|866fa3e8-bc09-4ddc-a0f3-84f88eaf57ce | underdog | John Metchie III | Receptions | under | 0.1060012724235827 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|68027fbe-2681-4510-8eea-3775ceb54e92 | underdog | Dalton Schultz | Receptions | under | 0.10596561958189699 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| prizepicks|16718516 | prizepicks | Colston Loveland | Rec Targets | under | 0.1053686257660188 | 2026-11-05T22:06:44Z | 2026-11-08T20:20:00.000-05:00 |
| prizepicks|16747705 | prizepicks | Nate Sheppard | Rush Atts | under | 0.10505321492422393 | 2026-11-07T05:59:57Z | 2026-11-07T12:30:00.000-05:00 |
| underdog|54a4a86f-12fb-48ce-ae28-78d9e65e325f | underdog | D'Andre Swift | Rush Yards | under | 0.10486667539877703 | 2026-11-07T05:59:57Z | 2026-11-09T01:20:00Z |
| underdog|6e9175f3-1f09-4d37-8de1-95aa4f0698e8 | underdog | Caden Buhr | FG Made | over | 0.10484583692775895 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| underdog|3dd97269-7090-4494-b0ba-aef942cacee8 | underdog | Jared Goff | Pass TDs | under | 0.10432511994565019 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|2b07303d-fe20-4bc5-8345-34bde54e95a1 | underdog | Dak Prescott | Pass TDs | under | 0.10429726760636782 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|a34fbd98-b819-47f8-ad35-0910f6aa4848 | underdog | DeMario Douglas | Receiving Yards | under | 0.10423741151490673 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|4a328574-9067-45a3-b2c8-168d822b5e16 | underdog | T.J. Hockenson | Receiving Yards | under | 0.10407541804729603 | 2026-11-03T11:59:28Z | 2026-11-10T01:15:00Z |
| underdog|1db30023-5914-439c-ac51-c556c30f7a5b | underdog | Marshall Pritchett | Receiving Yards | over | 0.1040578939603718 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|a3d2a9ad-7c96-4647-8be0-43a6f0c7e9c6 | underdog | Mike Matthews | Receptions | under | 0.10398872315492169 | 2026-11-05T12:22:13Z | 2026-11-07T23:15:00Z |
| underdog|40ff9eb2-56b6-4e1b-b6c4-833f171090a3 | underdog | Gunner Stockton | Pass Yards | under | 0.10381587336751552 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| underdog|0f82b2da-dcf8-4249-afaa-5bb76abe7b55 | underdog | Cardae Mack | Rush Yards | under | 0.10364304070027608 | 2026-11-06T06:34:07Z | 2026-11-08T00:30:00Z |
| underdog|4d4a6a56-43e2-4efe-9cca-06528df03d2e | underdog | Arch Manning | Pass TDs | over | 0.10334919497088374 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|a9b8a6e5-7405-489a-94a1-d068a323e253 | underdog | Dallas Goedert | Receptions | under | 0.1033306586731757 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| prizepicks|16718518 | prizepicks | Luther Burden III | Rec Targets | under | 0.10325655879442341 | 2026-11-05T22:06:44Z | 2026-11-08T20:20:00.000-05:00 |
| underdog|c71c7cdb-dcfc-4a27-b97c-06c3401aaf2c | underdog | Dani Dennis-Sutton | Sacks | over | 0.10322188894736123 | 2026-11-06T16:02:47Z | 2026-11-08T21:25:00Z |
| prizepicks|16577039 | prizepicks | Rashee Rice | Rec Yards | under | 0.10318750310261049 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|d82bd3c6-2a60-4879-b845-18484787d341 | underdog | Blake Barnett | Pass Yards | under | 0.1031517391686223 | 2026-11-05T12:22:13Z | 2026-11-07T18:00:00Z |
| underdog|144d701d-fac2-49f5-9273-5cb7b3f34376 | underdog | Carson Hilbert | FG Made | under | 0.10291406226096578 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| underdog|8ca38ea4-fb7d-450d-93e0-ad698309f00c | underdog | Dawson Knox | Receiving Yards | under | 0.10256010348325972 | 2026-11-07T05:59:57Z | 2026-11-10T01:15:00Z |
| underdog|3f7838a7-6e6e-47ac-8296-165647381eb8 | underdog | Jerry Jeudy | Receptions | under | 0.10245858231518723 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|ca26a97e-7e0e-4c51-b8fa-d172c750426d | underdog | Cyrus Allen | Receiving Yards | under | 0.10236946222568843 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|c4b8e03b-86f2-4d6c-b024-04caa813ed63 | underdog | Andre Szmyt | FG Made | under | 0.10236818666743885 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|12960d99-1bc5-4bb2-85a2-a6c71f2e076f | underdog | Gervon Dexter | Sacks | over | 0.10220042229850446 | 2026-11-07T05:59:57Z | 2026-11-08T14:30:00Z |
| underdog|31e52c16-e777-46f7-8a0d-7d8ae63b8bef | underdog | Jonathan Dimas | FG Made | over | 0.10217263105918573 | 2026-11-06T16:02:47Z | 2026-11-07T20:30:00Z |
| underdog|aaf30715-a58e-484d-b64b-5c9d91157d42 | underdog | Ted Hurst | Receptions | over | 0.10215868472628065 | 2026-11-05T22:06:44Z | 2026-11-09T01:20:00Z |
| underdog|d9d08697-3dd2-4d24-bc73-42297b125227 | underdog | Jameson Williams | Receptions | under | 0.10208410937911938 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|b92969bb-beb9-42fa-99d0-a200defe9980 | underdog | Tommy Carr | Pass Yards | under | 0.10196677346662242 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| underdog|f9a5045c-cce6-493b-920c-1ba0ce5bab59 | underdog | Kenny Clark | Sacks | over | 0.10188075110106326 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|e81a04c0-c35a-48e0-98c7-426fb2586fff | underdog | Tait Reynolds | Pass Yards | under | 0.10170450577146917 | 2026-11-07T05:59:57Z | 2026-11-07T17:00:00Z |
| underdog|f4bba20a-76ec-4df5-9de0-3c7c20bd1a76 | underdog | Keon Coleman | Receptions | under | 0.10169343136994924 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|24a49a3b-5f76-4977-9e37-fd6d51db08c2 | underdog | Jahmyr Gibbs | Rush Yards | under | 0.10154569505675504 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|1c53d9c0-2826-46db-bcf1-524d8e57331a | underdog | Brad Jackson | Pass Yards | under | 0.10145533676347196 | 2026-11-05T22:06:44Z | 2026-11-08T03:30:00Z |
| prizepicks|16764343 | prizepicks | Devin Singletary | Rec Targets | under | 0.10107442699598002 | 2026-11-07T05:59:57Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|23fa46de-8f35-4b86-b931-58c2c9be738f | underdog | Javonte Williams | Rush Yards | under | 0.10095549971421969 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|fd428c8a-dfcf-4715-a574-4a7eef1b0362 | underdog | Jeffery Simmons | Sacks | over | 0.100893411926745 | 2026-11-07T05:59:57Z | 2026-11-09T01:20:00Z |
| underdog|528efebf-508e-4983-936c-690477ebd224 | underdog | Christian McCaffrey | Receptions | under | 0.10087596308915803 | 2026-11-05T22:06:44Z | 2026-11-08T21:25:00Z |
| underdog|f4a312d6-9cf6-4524-92ca-1634f58b5769 | underdog | Cameron Dickey | Rush Yards | under | 0.10075968272343716 | 2026-11-07T05:59:57Z | 2026-11-08T02:30:00Z |
| underdog|6b56f67a-0cb3-4d32-aad1-5ebdb5004b45 | underdog | David Olano | XP Made | over | 0.10069986321094648 | 2026-11-05T12:22:13Z | 2026-11-07T20:00:00Z |
| underdog|bcf0586b-f2c4-464a-862b-6a09dc77b05a | underdog | John Bates | Receiving Yards | over | 0.10056043833569972 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|bdf4a4f2-c1e9-47fc-8fe5-b93626e43e6b | underdog | James Cook | Rush Yards | under | 0.10046089264064739 | 2026-11-05T22:06:44Z | 2026-11-10T01:15:00Z |
| underdog|4c0c83a7-22fc-43b3-9db9-d140c271a605 | underdog | Oronde Gadsden | Receptions | under | 0.10018871071931101 | 2026-11-05T12:22:13Z | 2026-11-08T21:05:00Z |
| underdog|381db12f-635c-43b4-898c-04b39c11f438 | underdog | Jamal Polite | Receptions | under | 0.1001216115286192 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|ad219443-0404-4391-b1bf-2707df6b9de7 | underdog | Omarion Hampton | Receptions | over | 0.09981815938380334 | 2026-11-05T12:22:13Z | 2026-11-08T21:05:00Z |
| underdog|6cfb6598-271c-42e3-a216-07ab2df66dce | underdog | Dylan Edwards | Receiving Yards | over | 0.09975639595755925 | 2026-11-07T05:59:57Z | 2026-11-07T20:45:00Z |
| prizepicks|16750454 | prizepicks | Ben Shelton | Total Games | over | 0.09958641463796192 | 2026-11-07T05:59:57Z | 2026-11-07T08:30:00.000-05:00 |
| underdog|7b619085-9839-4b60-97b5-ddf7349bd813 | underdog | Quinshon Judkins | Receiving Yards | over | 0.0993742616887544 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|d79eb508-80f6-4bcb-aef0-844f3f99f095 | underdog | Michael Hawkins | Pass TDs | over | 0.09931913444464169 | 2026-11-05T22:06:44Z | 2026-11-08T02:30:00Z |
| underdog|85ccf44b-f7bc-4dcb-8e44-34d938c7b0be | underdog | Tyler Goodson | Rush Yards | under | 0.09926361066374967 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|e322429d-650a-4a9b-90ae-7c12e88c2be5 | underdog | David Olano | FG Made | over | 0.09919826629893125 | 2026-11-05T12:22:13Z | 2026-11-07T20:00:00Z |
| underdog|39f45cca-973d-4355-ba85-f1085b70cd7c | underdog | Mitchell Evans | Receiving Yards | over | 0.09918365229749104 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|aa444c6b-f74f-4284-97b4-ed7efef8cd13 | underdog | Jack Bech | Receiving Yards | over | 0.09915193262395117 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|9059c9c2-5e70-4e5e-a13c-0e510a160455 | underdog | Austin Ekeler | Rush Yards | under | 0.09915082840145573 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|57f73ccb-63b1-451c-bbeb-fbaac3456b03 | underdog | Aaron Jones | Receptions | under | 0.09908473856146005 | 2026-11-05T12:22:13Z | 2026-11-10T01:15:00Z |
| underdog|be48005a-e911-48a5-89d3-0071ee0d1592 | underdog | Devon Dampier | Pass TDs | over | 0.09858639656620943 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|24324e94-375f-47e6-81b8-1367b471a178 | underdog | Juwan Johnson | Receptions | under | 0.09851839400207829 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|d1e744f7-e48f-432b-ac36-9994d2f0347b | underdog | Chuba Hubbard | Rush Yards | under | 0.09846599432023506 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|dd1718df-3886-4aed-b604-7175a167d9b3 | underdog | Arch Manning | Pass Yards | under | 0.09842107757177954 | 2026-11-07T05:59:57Z | 2026-11-07T17:00:00Z |
| prizepicks|16685623 | prizepicks | D'Andre Swift | Rush TDs | over | 0.09831155568334193 | 2026-11-05T12:22:13Z | 2026-11-08T20:20:00.000-05:00 |
| prizepicks|16619747 | prizepicks | Jesse Legree | Recs | under | 0.09789260962625501 | 2026-11-04T12:10:41Z | 2026-11-07T22:30:00.000-05:00 |
| underdog|ca0fc4a6-2158-45f4-acb6-cb6dfb5923c3 | underdog | Jason Myers | Kicking Points | under | 0.09767305134966542 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| prizepicks|16718529 | prizepicks | KC Concepcion Jr. | Rec Targets | under | 0.09759613041448167 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|ca0b739f-619d-44bc-a06f-c2bc8dfffd97 | underdog | Mitchell Evans | Receptions | over | 0.09744221623392268 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|7952a26e-6d89-4b9b-a7dc-4640eb8fcc39 | underdog | Tate Sandell | XP Made | over | 0.09738689793935634 | 2026-11-06T16:02:47Z | 2026-11-08T00:45:00Z |
| underdog|96e04406-2dc9-4e27-a7a3-24fef33ac8dd | underdog | Mason Taylor | Receiving Yards | under | 0.09725922451571889 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| prizepicks|16623390 | prizepicks | Kyle Pitts Sr. | Recs | under | 0.09724751553828881 | 2026-11-04T12:10:41Z | 2026-11-08T09:30:00.000-05:00 |
| underdog|dd95402c-e9ca-44e5-a5a3-179e2734707c | underdog | Jordan Addison | Receptions | under | 0.09707338503094809 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|777a6934-83da-4fc6-ae05-670614aac4c8 | underdog | Luther Burden | Receptions | under | 0.0970050304666229 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|a01da2b4-f7eb-47d0-8346-e42d146e6db8 | underdog | Ryan Browne | Pass TDs | under | 0.0966373760343806 | 2026-11-05T22:06:44Z | 2026-11-07T17:30:00Z |
| underdog|1d8cac75-0a34-4da2-b758-1163f0cb3502 | underdog | Fluff Bothwell | Receiving Yards | over | 0.09656381239076028 | 2026-11-06T06:34:07Z | 2026-11-07T21:15:00Z |
| underdog|d81755ee-3b9d-4b52-866f-6b234a018dd8 | underdog | Caleb Douglas | Receiving Yards | under | 0.09649565964839524 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| prizepicks|16623392 | prizepicks | Jahan Dotson | Recs | under | 0.09637295072919405 | 2026-11-04T12:10:41Z | 2026-11-08T09:30:00.000-05:00 |
| underdog|2bac7b08-fac7-40ce-8ab4-52eed070b62a | underdog | Jordan Love | Pass TDs | under | 0.0961519218860859 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|148230ba-2a81-454f-85f0-f149da127ba2 | underdog | Jamal Roberts | Receiving Yards | over | 0.09599782259397949 | 2026-11-07T05:59:57Z | 2026-11-07T17:00:00Z |
| underdog|0c57932e-0ffc-411c-bd91-b60cf90168b0 | underdog | Brandon Aubrey | Kicking Points | under | 0.09590964792109724 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|a02c87fe-f8cd-4593-b8f9-3c37dcab1bfd | underdog | Jake Bates | Kicking Points | under | 0.09584127441212353 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|0f4bff94-0106-4f5e-b376-4f86353dfda5 | underdog | Dallas Goedert | Receiving Yards | under | 0.095781750919261 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|8e794760-3f49-4bee-81bf-4c5f29c7dc27 | underdog | Tyler Allgeier | Receiving Yards | under | 0.09577866004051383 | 2026-11-05T22:06:44Z | 2026-11-08T21:25:00Z |
| underdog|9c1b45cb-d2e6-4535-a044-78a3bddd6ed8 | underdog | CJ Bailey | Pass TDs | over | 0.09573235892369791 | 2026-11-05T22:06:44Z | 2026-11-07T17:30:00Z |
| underdog|50ab1583-86de-4d93-ad49-f9c77e284022 | underdog | Kyle Juszczyk | Receptions | under | 0.09555935955530548 | 2026-11-05T22:06:44Z | 2026-11-08T21:25:00Z |
| underdog|70b674bf-14ef-4526-b90e-42cba3c6d3a5 | underdog | Adam Trautman | Receptions | under | 0.09545112973787573 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|a186b02c-a2f9-4b57-9502-3efc07964e5f | underdog | KJ Jackson | Pass Yards | under | 0.09509448313433777 | 2026-11-06T06:34:07Z | 2026-11-07T17:45:00Z |
| underdog|f3df021b-e87e-4d22-a9e7-273fdfdebcdf | underdog | Charlie Woerner | Receptions | under | 0.09501160407184561 | 2026-11-05T12:22:13Z | 2026-11-08T14:30:00Z |
| underdog|a5eb6366-cd82-4d6b-bd95-f5e0ede614e0 | underdog | Ka'imi Fairbairn | Kicking Points | under | 0.09495465902987144 | 2026-11-03T02:21:46Z | 2026-11-08T21:05:00Z |
| underdog|f84d7aab-a448-4292-871a-1f620651db5e | underdog | Henry To'oTo'o | Sacks | over | 0.09474105605500435 | 2026-11-06T16:02:47Z | 2026-11-08T21:05:00Z |
| underdog|f4515f6e-3d00-4276-a15c-6d64d8befc49 | underdog | Nate Roberts | Receiving Yards | over | 0.09471755110925595 | 2026-11-07T05:59:57Z | 2026-11-07T20:30:00Z |
| underdog|eb5bdb41-4646-402d-82b4-302710f7c29c | underdog | Jalen Coker | Receiving Yards | under | 0.09425398437096033 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|c578d8d7-01f0-4d79-9d4f-3b0725511b5a | underdog | Legend Glasker | Receptions | under | 0.0939339008632083 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|06453bc8-3c32-4402-b79a-c09f64d23356 | underdog | Braden Atkinson | Pass TDs | under | 0.0938819023831381 | 2026-11-05T12:22:13Z | 2026-11-08T03:30:00Z |
| underdog|285b8cc1-e70a-497a-b860-ab7fc239dce6 | underdog | Denzel Boston | Receiving Yards | under | 0.0930300815809536 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| prizepicks|16718478 | prizepicks | Jahan Dotson | Rec Targets | under | 0.09297043171542263 | 2026-11-05T22:06:44Z | 2026-11-08T09:30:00.000-05:00 |
| underdog|5b87e878-a87a-4833-a5f2-0c56bd5e34a3 | underdog | Rachaad White | Receiving Yards | under | 0.09288707490475656 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| prizepicks|16685554 | prizepicks | Jared Goff | Pass TDs | under | 0.09280845049511621 | 2026-11-05T12:22:13Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|7abbae0b-0d7f-4ab0-a12b-c6736269a236 | underdog | Jake Fette | Pass TDs | under | 0.09233132561279922 | 2026-11-05T22:06:44Z | 2026-11-08T00:30:00Z |
| underdog|7cee03ac-78b3-4d7b-9754-834e5953a2f4 | underdog | Bryce Young | Rush Yards | under | 0.09215881426223937 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|93a92a80-a9c0-4066-901b-6e9bb3e6ed82 | underdog | Mateen Bhaghani | XP Made | over | 0.09160309321993065 | 2026-11-04T12:10:41Z | 2026-11-07T17:00:00Z |
| underdog|e817a19f-8ec3-4eb9-9651-08edf2d48808 | underdog | Chase Young | Sacks | under | 0.09158465620785661 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|764ae055-8ed5-4ee5-9017-eaaf0396e43b | underdog | Jordan Faison | Receiving Yards | under | 0.09123018479039069 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| underdog|5bfbf81c-b9d3-40ce-8633-2da40ea3ff0e | underdog | Andrew Van Ginkel | Sacks | over | 0.09057151864856627 | 2026-11-07T05:59:57Z | 2026-11-10T01:15:00Z |
| prizepicks|16699521 | prizepicks | Kenneth Williams | Rush Atts | under | 0.09015574174620566 | 2026-11-07T05:59:57Z | 2026-11-07T19:30:00.000-05:00 |
| underdog|d52dc310-ea00-4c21-bb95-3798608a708f | underdog | Quentin Johnston | Receptions | under | 0.08995109550904856 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|6699fb40-5a95-41f1-9466-35c2c70f45a0 | underdog | Christian Watson | Receiving Yards | under | 0.08988230264780483 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|f4fc26f2-7539-454f-b714-3e49abdd9e04 | underdog | Ryan Flournoy | Receiving Yards | under | 0.08965363558029227 | 2026-11-06T16:02:47Z | 2026-11-08T18:00:00Z |
| underdog|c90518a9-3b7b-4a28-b1f8-edec396b50bb | underdog | Gavin Lahm | XP Made | under | 0.08887474946252161 | 2026-11-05T12:22:13Z | 2026-11-07T21:15:00Z |
| underdog|27cb9670-5382-48df-ab83-f72399dbeeac | underdog | Travis Kelce | Receiving Yards | under | 0.08860625184263005 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|a9535e18-69cb-422f-bcff-2ba17b1e95cd | underdog | Malik Washington | Pass Yards | under | 0.08846757636534097 | 2026-11-05T22:06:44Z | 2026-11-07T17:30:00Z |
| underdog|dc019ad3-02a7-4415-86a9-45d5cd14ee38 | underdog | Seth McGowan | Rush Yards | under | 0.08821220509749816 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|6726b20f-c66f-4680-b28e-59c7720ceb2a | underdog | Quinnen Williams | Sacks | over | 0.08804791190061612 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|93c23b7a-e00a-436d-bdbf-012f847dcbfb | underdog | Jonah Coleman | Receiving Yards | under | 0.08784628755770052 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|b722c0eb-24f9-4457-aca1-c570a4906039 | underdog | Chris Olave | Receiving Yards | under | 0.08783600387699941 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|e2b129c7-4ce7-4ac8-abb8-cf4529dbd83a | underdog | Kenneth Walker III | Rush + Rec Yards | under | 0.08768372599524399 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|d6f14494-641b-4ed4-9b04-4ed516e0f469 | underdog | Josh Downs | Receptions | under | 0.08767799557017741 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| prizepicks|16764338 | prizepicks | Efton Chism III | Rec Targets | under | 0.08767504270499804 | 2026-11-07T05:59:57Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|02084d0c-6d32-4b45-bc7a-54262029491a | underdog | Elijah Mitchell | Receptions | under | 0.08726398545769454 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|85d0f744-992b-44c1-8a7c-101d9724dfdc | underdog | Bucky Irving | Receiving Yards | under | 0.08678510565293707 | 2026-11-05T12:22:13Z | 2026-11-09T01:20:00Z |
| underdog|87e67aff-abb3-4158-9ac0-1b237a7b4a43 | underdog | Jonathan Taylor | Rush + Rec Yards | under | 0.08666188699419164 | 2026-11-06T16:02:47Z | 2026-11-08T18:00:00Z |
| underdog|12a2d911-b12a-443c-8611-c6a04a06c827 | underdog | Keenan Allen | Receptions | under | 0.08657096839321532 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|30d142c6-8017-4e94-b781-4eb760e26d96 | underdog | Evan McPherson | Kicking Points | under | 0.08624660748610669 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|53c4cbb1-3a54-417e-8c63-81475d2485d6 | underdog | Xavier Williams | Rush Yards | under | 0.08612072539405491 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| underdog|3c25e1f6-5855-4e10-b07c-c168b58f8e8b | underdog | Andre Szmyt | Kicking Points | under | 0.08606085228469695 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|9ecd4e1a-816a-4939-bf25-73902d23441b | underdog | Max Gilbert | FG Made | over | 0.08600901002958494 | 2026-11-06T06:34:07Z | 2026-11-07T17:45:00Z |
| underdog|2de77434-e9f7-416c-b3f4-c8c99c086db0 | underdog | Braelon Allen | Receptions | under | 0.08548177488523989 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|573a09d8-1d66-4418-8ca5-3e2e403d8b93 | underdog | Trevor Etienne | Rush Yards | under | 0.08500270395062026 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| underdog|771df1cb-a4e1-4db3-a22c-43a4bb5f2de5 | underdog | Isaiah West | Rush Yards | under | 0.08496689908690391 | 2026-11-05T12:22:13Z | 2026-11-07T20:30:00Z |
| underdog|7aed8570-87de-4d2b-848e-af0dfdec99fa | underdog | Owen Allen | Rush Yards | under | 0.08455936724717117 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| underdog|9a11ea53-966f-452f-a1c2-ab1154cc943e | underdog | Jalen Coker | Receptions | under | 0.08455880625865009 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|a8b4d56b-3190-4729-a3e3-fa4952f7fe19 | underdog | Malachi Fields | Receptions | under | 0.08444567676815706 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|fca3da4f-9476-4b17-ad79-8f80aef153b9 | underdog | Elina Svitolina | Double Faults | under | 0.08423149243173988 | 2026-11-05T12:22:13Z | 2026-11-09T21:10:00Z |
| underdog|3716c38e-c313-439c-8c4e-db38996e9297 | underdog | Liam Boyd | FG Made | under | 0.08392246570987505 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|de3a28c0-990e-45e6-b955-eb21bc4ad9a4 | underdog | Patrick Mahomes | Rush Yards | under | 0.08365133891580678 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|ca923a9a-2e8e-46ad-acaf-0b4ecc69a8bd | underdog | Malik Nabers | Receiving Yards | under | 0.08364693870895912 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| prizepicks|16747634 | prizepicks | Christian McCaffrey | Recs | under | 0.08327349289890928 | 2026-11-07T05:59:57Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|d2a2884a-9482-4454-8f62-b11b25cf9301 | underdog | AJ Barner | Receiving Yards | under | 0.08315373110424162 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|4e7cab7c-a9a4-4533-ae0e-b7d96c3d425b | underdog | Jack Bech | Receptions | under | 0.08300134151445937 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|4c0f438a-882b-475b-89c0-cfc4196bd71a | underdog | Griffin Wilde | Receptions | under | 0.0828345646052695 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| prizepicks|16719186 | prizepicks | Jaxon Smith-Njigba | Rec Targets | under | 0.08268085501976197 | 2026-11-05T22:06:44Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|9929c86c-1621-47ce-a261-f5b28c6fee14 | underdog | Gavin Freeman | Receptions | under | 0.08248533194104546 | 2026-11-07T05:59:57Z | 2026-11-07T17:00:00Z |
| underdog|25255a20-7079-4a1c-93c7-d22ff200d39d | underdog | Desirrio Riles | Receiving Yards | over | 0.082356492885021 | 2026-11-07T05:59:57Z | 2026-11-07T17:00:00Z |
| underdog|290801af-3706-4e63-a371-7ea08d5847a6 | underdog | Omar Cooper | Receiving Yards | under | 0.0822464922995011 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|ca872cd6-7216-4aaa-9e91-7d7ba62bfc3e | underdog | Rocky Beers | Receptions | under | 0.08203459759950504 | 2026-11-07T05:59:57Z | 2026-11-08T00:45:00Z |
| underdog|db8a215c-a32b-461f-a74f-392bfed6cd47 | underdog | Sam LaPorta | Receptions | under | 0.08195280346786493 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|68173c0b-2080-4055-b4ae-bddf30f8835f | underdog | Omar Cooper | Receptions | under | 0.08175619641694731 | 2026-11-06T16:02:47Z | 2026-11-08T18:00:00Z |
| underdog|1bc615c1-043a-4445-9e64-11eb22ceba0a | underdog | Seth McGowan | Receptions | under | 0.08155867442257059 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| prizepicks|16764729 | prizepicks | Magda Linette | Aces | under | 0.08147253454524372 | 2026-11-07T05:59:57Z | 2026-11-07T08:40:00.000-05:00 |
| prizepicks|16764337 | prizepicks | DeMario Douglas | Rec Targets | under | 0.08146301973318348 | 2026-11-07T05:59:57Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|5c337aed-de12-4dd6-8f6c-b4f90680d29f | underdog | Tutu Atwell | Receiving Yards | under | 0.08144794777681263 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| prizepicks|16591330 | prizepicks | Wayshawn Parker | Rush Atts | under | 0.08144706043100858 | 2026-11-07T05:59:57Z | 2026-11-07T12:00:00.000-05:00 |
| underdog|0767ecdc-6c88-403c-a631-567d0902ae5f | underdog | Bijan Robinson | Receptions | under | 0.08140314785642488 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|33001675-032f-4e6e-88c9-c0fa433d7f5e | underdog | Cooper Barkate | Receiving Yards | under | 0.08136010842040942 | 2026-11-06T16:02:47Z | 2026-11-08T00:30:00Z |
| underdog|114e40cb-83b3-4b38-a44f-7fd853dbc826 | underdog | Blake Corum | Rush Yards | under | 0.08133865297637977 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|30c987cb-9450-418a-b4ff-d450e9c0183f | underdog | Ashton Jeanty | Receptions | under | 0.08123630317472041 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|8603a67e-b64c-4937-a332-1ee911b5f8e3 | underdog | Elijah Moore | Receiving Yards | over | 0.08099514490247195 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|3f37b916-250a-4972-965b-ecb6efeb0ce3 | underdog | Chris Bell | Receiving Yards | under | 0.08090076495058063 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|92f4c898-131c-47c3-9d60-dc8c4ba199d9 | underdog | Fame Ijeboi | Rush Yards | under | 0.08075098988128293 | 2026-11-07T05:59:57Z | 2026-11-07T17:30:00Z |
| underdog|0ea0b642-98a0-416f-b69d-b7ce615c61b3 | underdog | Drew Stevens | FG Made | under | 0.0806709260026024 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|a93191dc-5ab3-4d60-9b3c-0635b721460f | underdog | Baker Mayfield | Rush Yards | under | 0.0804542415617544 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|068c2845-f537-4906-af08-4f8ad8d42f86 | underdog | JC French | Pass TDs | over | 0.08029728756815707 | 2026-11-06T16:02:47Z | 2026-11-07T20:30:00Z |
| underdog|12bd4374-687f-4ccd-8483-775c124afda4 | underdog | Khalil Shakir | Receptions | under | 0.08011792675984464 | 2026-11-04T12:10:41Z | 2026-11-10T01:15:00Z |
| underdog|d64d6002-cbe6-4802-b5c1-a7cdd75e4898 | underdog | Blake Corum | Receiving Yards | over | 0.07956662715644236 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|a2f8424e-28d4-487d-9875-bae9673e09e0 | underdog | Dylan Raiola | Pass TDs | under | 0.0793130185765103 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|ff70b613-e13b-4266-9d3b-50e215560c82 | underdog | Tyler Allgeier | Rush + Rec Yards | under | 0.07924262731427245 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|a57c34c5-0685-4573-826a-2780a1571932 | underdog | Kyren Williams | Rush + Rec Yards | under | 0.07885524524463117 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|52729c68-1a93-49ba-90ca-6d0ebfffe7aa | underdog | Conner Weigman | Pass TDs | under | 0.07858724997809308 | 2026-11-07T05:59:57Z | 2026-11-07T20:30:00Z |
| underdog|7736c2b9-bcdb-4bfd-bd4f-4271f590b609 | underdog | Lukas Van Ness | Sacks | over | 0.07844016411325083 | 2026-11-06T16:02:47Z | 2026-11-08T21:25:00Z |
| underdog|33218830-4e75-460f-b41a-469bc409fee1 | underdog | Ryan Browne | Pass Yards | under | 0.07827030756965858 | 2026-11-06T06:34:07Z | 2026-11-07T17:30:00Z |
| underdog|a1219294-4b95-4821-8c16-704f4691a0e3 | underdog | Blake Corum | Rush + Rec Yards | under | 0.0779904413997341 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|c2a92d88-0d14-4da9-a1dd-d6afa0887605 | underdog | Jonathan Taylor | Rush Yards | under | 0.07760504837036786 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| prizepicks|16718545 | prizepicks | Christian Watson | Rec Targets | under | 0.07759156462609396 | 2026-11-05T22:06:44Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|4a89e10d-0ca4-474d-97f5-0bc040a68326 | underdog | Keaton Mitchell | Receptions | under | 0.07757945660569399 | 2026-11-06T06:34:07Z | 2026-11-08T21:05:00Z |
| underdog|62465cef-4749-4f24-a49e-a2d29fb6d9af | underdog | Jaron Tibbs | Receiving Yards | under | 0.07704359216338097 | 2026-11-05T12:22:13Z | 2026-11-07T18:00:00Z |
| underdog|273b4f1f-bf42-4a41-a69b-e9b2f4dd10f1 | underdog | Reggie Virgil | Receiving Yards | under | 0.07701412532993002 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|178f08bc-b24b-44cb-8e32-0c49a45abb6e | underdog | AJ Surace | Pass TDs | over | 0.07667779004543462 | 2026-11-05T12:22:13Z | 2026-11-07T21:15:00Z |
| underdog|b037dd4d-81a9-4275-bf43-602a7252c49e | underdog | George Pickens | Receptions | under | 0.0766522668294094 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| prizepicks|16566879 | prizepicks | Drake London | Recs | under | 0.07645666700581077 | 2026-11-04T12:10:41Z | 2026-11-08T09:30:00.000-05:00 |
| underdog|0922f90a-0901-4f10-a983-e4aa2c121442 | underdog | Gianni Spetic | FG Made | over | 0.07604097650812291 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|1f34226e-ef7d-422d-8d28-1ed92c62e738 | underdog | Michael Turner | Rush Yards | under | 0.07600603661448901 | 2026-11-07T05:59:57Z | 2026-11-07T17:00:00Z |
| underdog|15876ce1-1149-41e6-94b3-73569712726f | underdog | Sam Leavitt | Total TDs | under | 0.07556482851099611 | 2026-11-07T05:59:57Z | 2026-11-07T20:30:00Z |
| underdog|47a5a56d-1fdf-4c6f-9f05-0fc430cbbbea | underdog | Cade Otton | Receptions | under | 0.07553932484130521 | 2026-11-07T05:59:57Z | 2026-11-09T01:20:00Z |
| underdog|877722b0-7930-4ac0-a92f-610609e5a5e3 | underdog | Aidan Hutchinson | Sacks | under | 0.07530978400549204 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|b40659e4-2add-461a-ada3-aae1160149b6 | underdog | Laiatu Latu | Sacks | over | 0.07522082045184025 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|3db483c9-2cbd-4a61-a415-da9945e7783b | underdog | J'Koby Williams | Rush Yards | under | 0.0751641814121301 | 2026-11-04T12:10:41Z | 2026-11-08T02:30:00Z |
| underdog|4c70a18d-75ed-4e4c-975d-5d6dc25b10bb | underdog | Seth McGowan | Receiving Yards | over | 0.07512746071341281 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|23c52bc4-f652-498c-afbb-4702005baace | underdog | Dylan Edwards | Rush Yards | under | 0.07510654961176477 | 2026-11-07T05:59:57Z | 2026-11-07T20:45:00Z |
| underdog|80d395a7-fff7-4ff4-9710-ea3c03ad9d49 | underdog | Troy Franklin | Receptions | under | 0.07479838510150683 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|c9f42cb3-782a-42ae-8d36-b838a2e16e5b | underdog | Tyler Goodson | Receptions | under | 0.07447307028831152 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| prizepicks|16719159 | prizepicks | Ashton Jeanty | Rec Targets | under | 0.07445513690876382 | 2026-11-05T22:06:44Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|3896af71-474b-40dd-bd62-e77ad94feb79 | underdog | Byrum Brown | Pass TDs | under | 0.0743093392837626 | 2026-11-06T06:34:07Z | 2026-11-07T17:45:00Z |
| underdog|f7c17ddd-b7da-47e1-b7cc-3c831055be6b | underdog | Dominic Zvada | FG Made | under | 0.0741063683238431 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|c7fde436-b10f-4b32-ade3-6592960e545e | underdog | Roschon Johnson | Receptions | under | 0.0740765133334802 | 2026-11-06T16:02:47Z | 2026-11-09T01:20:00Z |
| underdog|55d21c52-58bc-419f-ace8-32daf98964d4 | underdog | Walker Eget | Pass TDs | under | 0.07387684664850058 | 2026-11-05T22:06:44Z | 2026-11-07T17:30:00Z |
| underdog|ae08266e-6845-4eb5-8ae0-c55a994092c7 | underdog | Dylan Raiola | Pass Yards | under | 0.07375588900233532 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|bc765a50-b954-4613-82ce-93029d04d412 | underdog | Aiden Flora | Receiving Yards | over | 0.07359553190708512 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|5571a9d9-5257-413c-94f7-b30035400e37 | underdog | Evan Engram | Receiving Yards | under | 0.07358911959876246 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|6adc5eae-4fa6-4375-bf9b-07b83534e121 | underdog | Keaton Mitchell | Receiving Yards | under | 0.07350289086331441 | 2026-11-06T16:02:47Z | 2026-11-08T21:05:00Z |
| prizepicks|16719174 | prizepicks | T.J. Hockenson | Rec Targets | under | 0.07349799752159802 | 2026-11-05T22:06:44Z | 2026-11-09T20:15:00.000-05:00 |
| prizepicks|16576406 | prizepicks | Kyren Williams | Rush Yards | under | 0.0734640730790519 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|98370739-8ce7-4116-9352-2a9e7a795fa3 | underdog | C.J. Stroud | Pass TDs | under | 0.07344784426946727 | 2026-11-03T02:21:46Z | 2026-11-08T21:05:00Z |
| underdog|d1addd18-ecc3-4df8-800b-3e1fd494f623 | underdog | Demond Williams | Pass Yards | under | 0.07341407765648678 | 2026-11-07T05:59:57Z | 2026-11-07T20:30:00Z |
| underdog|c10a0922-5357-4d12-a34a-fef19f41ae93 | underdog | Dylan Sampson | Receptions | under | 0.073210778810199 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|f7413d7e-001a-4315-8bef-ee5b8c474c0d | underdog | Keelon Russell | Pass Yards | under | 0.07313844310922835 | 2026-11-05T12:22:13Z | 2026-11-07T20:30:00Z |
| underdog|c09e8f25-de98-485a-9a92-3e90c88df8aa | underdog | Cameron Dicker | Kicking Points | under | 0.07288428793483492 | 2026-11-05T22:06:44Z | 2026-11-08T21:05:00Z |
| underdog|d45e253c-f252-4509-a696-99b545feffe9 | underdog | Gianni Spetic | XP Made | over | 0.07268509835321124 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|5c589e9f-50cb-4f4d-bc6c-31a94652a555 | underdog | Darren Waller | Receptions | under | 0.07257323185856346 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|1060d4eb-fa5c-48ec-98f5-952162284f9c | underdog | Brenton Cox | Sacks | over | 0.07234169347564967 | 2026-11-06T16:02:47Z | 2026-11-08T21:25:00Z |
| underdog|274a5cd2-ea5e-4311-b899-27e6829d3d33 | underdog | Jaylahn Tuimoloau | Sacks | over | 0.07234169347564967 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|8075a453-ac40-490d-9ce6-4a8ef520927d | underdog | Brian Rowe | Receptions | over | 0.07222546717268308 | 2026-11-06T16:02:47Z | 2026-11-07T17:00:00Z |
| prizepicks|16760101 | prizepicks | Casper Ruud | Total Games Won | over | 0.07204273579211529 | 2026-11-07T05:59:57Z | 2026-11-07T11:00:00.000-05:00 |
| underdog|50880572-71dc-48d8-ba1c-131b91584d8d | underdog | DeJuan Williams | Rush Yards | under | 0.07191226289630914 | 2026-11-06T06:34:07Z | 2026-11-07T17:30:00Z |
| underdog|099c1a61-fff7-42fd-8b84-2a802a10131d | underdog | Charlie Woerner | Receiving Yards | over | 0.0716218067675457 | 2026-11-06T06:34:07Z | 2026-11-08T14:30:00Z |
| underdog|4ff201eb-6873-438f-b135-cd456ff3b4ad | underdog | Tory Horton | Receiving Yards | under | 0.07152796009804019 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|143ec305-dbfc-4481-a66a-798b8b5fdca8 | underdog | Mike Washington | Rush + Rec Yards | under | 0.07125476656934071 | 2026-11-06T06:34:07Z | 2026-11-08T21:25:00Z |
| underdog|82a0c739-4fe5-4f9c-ab98-3f993aa6a3a8 | underdog | Blake Corum | Receptions | under | 0.07120017552093771 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| prizepicks|16718564 | prizepicks | Cyrus Allen | Rec Targets | under | 0.07077470405848951 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|7bff2e43-ab12-4a98-b7e5-04d0c0bbf914 | underdog | Mike Washington | Receptions | under | 0.07071209556400804 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|1f1d13a1-afea-41e0-842f-8af4981136b9 | underdog | Kenneth Walker III | Rush Yards | under | 0.0706968503684764 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|bcd18f2c-cead-4a49-bdf1-35b14e6ddb98 | underdog | Bo Jackson | Receiving Yards | over | 0.07068112888468336 | 2026-11-07T05:59:57Z | 2026-11-07T20:30:00Z |
| underdog|6eb74445-a1e8-47a9-a686-945b61216684 | underdog | Jack Cassidy | FG Made | under | 0.07067146122833412 | 2026-11-06T16:02:47Z | 2026-11-08T02:30:00Z |
| underdog|04eeed7a-c4fd-4327-b514-a03cc068f198 | underdog | Jojo Phillips | Receiving Yards | over | 0.07065767890617458 | 2026-11-07T05:59:57Z | 2026-11-07T17:00:00Z |
| prizepicks|16719178 | prizepicks | Chris Olave | Rec Targets | under | 0.07047505206770643 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|d1cbb3da-3a91-40ba-bdec-e8d68a069937 | underdog | Luke Dehnicke | Receptions | under | 0.07046274395456875 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|b13b2682-93bb-45e1-89e3-94c1fd65b925 | underdog | Tyler Allgeier | Rush Yards | under | 0.07029518340467622 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|dc7085a5-bd2b-4e90-9aa5-7e11f5f57193 | underdog | Dohnte Meyers | Receptions | under | 0.07018273167311495 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| prizepicks|16719171 | prizepicks | Malik Washington | Rec Targets | under | 0.07012174955976103 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|9cac1640-ca39-4f1b-931a-e2c850308466 | underdog | Noah Gray | Receptions | over | 0.06995762914057951 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|653afc15-7559-442b-b34d-1f0091847e3b | underdog | Chase Brown | Receptions | under | 0.06992427729238937 | 2026-11-05T12:22:13Z | 2026-11-08T14:30:00Z |
| underdog|4f42e71e-9977-4467-9c6f-587a1fb01921 | underdog | Malik Willis | Pass TDs | under | 0.0698898131874599 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|c2cb23ed-e9e1-4001-b399-a993cb57457a | underdog | Nate Sheppard | Rush Yards | under | 0.06971997605393809 | 2026-11-07T05:59:57Z | 2026-11-07T17:30:00Z |
| underdog|5d3f8406-244c-41e6-b2c6-a84f6c15c709 | underdog | Chris Durr | Receiving Yards | under | 0.06971444822886719 | 2026-11-07T05:59:57Z | 2026-11-07T17:30:00Z |
| underdog|645d1e24-ea6b-4524-966f-4ad8a9808469 | underdog | DaSaahn Brame | Receptions | under | 0.06953393528194685 | 2026-11-05T12:22:13Z | 2026-11-07T23:15:00Z |
| underdog|6b6a3c19-7e0e-4a1d-836d-a9b45d3a993c | underdog | Carson Hilbert | XP Made | under | 0.06949109112699159 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| underdog|097a88ee-d188-4ac6-90fa-1746ae2b9b19 | underdog | Tyler Higbee | Receptions | under | 0.0692665656780046 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| prizepicks|16576408 | prizepicks | Javonte Williams | Rush Yards | under | 0.06913799764143458 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|c33ff82e-ba83-46d9-aa6d-6fbdf146a0e8 | underdog | Adonai Mitchell | Receiving Yards | under | 0.06912273937461644 | 2026-11-06T16:02:47Z | 2026-11-08T18:00:00Z |
| underdog|78acf4d1-e262-4f4a-984c-e277c267c22e | underdog | Brian Bonner | Rush Yards | over | 0.06885898616279384 | 2026-11-07T05:59:57Z | 2026-11-07T20:30:00Z |
| underdog|f9fe24e6-dd92-40f6-a6d8-49347d9716b3 | underdog | Tylik Hill | Rush Yards | over | 0.0687067760591078 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|1676285c-b66c-440c-ba94-3e1e1dd2226c | underdog | Jesse Legree | Receiving Yards | under | 0.06868793139917972 | 2026-11-05T12:22:13Z | 2026-11-08T03:30:00Z |
| prizepicks|16722854 | prizepicks | Brandin Cooks | Rec Targets | under | 0.068448315251599 | 2026-11-06T06:34:07Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|95b9556b-02ea-4716-95a3-378600721291 | underdog | Kanoah Vinesett | XP Made | over | 0.0683250670662876 | 2026-11-05T22:06:44Z | 2026-11-07T17:30:00Z |
| prizepicks|16683643 | prizepicks | Jake Bates | Kicking Points | under | 0.06818662504942608 | 2026-11-05T12:22:13Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|3d5a0cce-f39d-4b6e-81b5-4ee1dba17254 | underdog | Drew Mestemaker | Pass TDs | over | 0.06800685495810133 | 2026-11-07T05:59:57Z | 2026-11-07T18:00:00Z |
| prizepicks|16718491 | prizepicks | Olamide Zaccheaus | Rec Targets | under | 0.06800425311674296 | 2026-11-05T22:06:44Z | 2026-11-08T09:30:00.000-05:00 |
| underdog|90c3977f-8381-4a61-9dbd-94f49ffcf439 | underdog | Drew Sample | Receiving Yards | over | 0.0679032038021633 | 2026-11-05T12:22:13Z | 2026-11-08T14:30:00Z |
| underdog|291cc650-4ebe-481a-a001-eab2766f55a1 | underdog | Elija Lofton | Receiving Yards | under | 0.06771764807076375 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| underdog|aa2400e1-61c6-42b8-a00e-4df185d8e29a | underdog | Peyton Woodring | XP Made | over | 0.06770360800211805 | 2026-11-04T12:10:41Z | 2026-11-08T00:30:00Z |
| underdog|b4a11205-f19f-4256-9e1e-6703e6a4644a | underdog | Jaylen Waddle | Receptions | under | 0.06756067788820463 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|f9330e16-1ebe-495a-a353-0a85b5f209b9 | underdog | CJ Bailey | Pass Yards | under | 0.06742293822419498 | 2026-11-05T22:06:44Z | 2026-11-07T17:30:00Z |
| underdog|1fb4d5c3-a828-43b8-9854-3c7496d50c54 | underdog | Dierre Hill | Receptions | over | 0.06742273754518746 | 2026-11-07T05:59:57Z | 2026-11-07T20:30:00Z |
| underdog|d6013cb6-759f-412b-979f-06ad898147f7 | underdog | Rodney Fields | Rush Yards | under | 0.0673522265722456 | 2026-11-06T16:02:47Z | 2026-11-07T18:00:00Z |
| underdog|7db9e716-c382-497b-88b9-f6f6c10c7108 | underdog | Max Gilbert | XP Made | over | 0.06722338435736108 | 2026-11-06T06:34:07Z | 2026-11-07T17:45:00Z |
| underdog|08570f7c-18e1-4be6-a12f-2affc9c308ea | underdog | Fredrick Moore | Receiving Yards | over | 0.06716368701428133 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| underdog|797eb995-dcca-45f1-8e08-0b28a12ceed4 | underdog | Isaac Wilson | Pass Yards | under | 0.06692344939876449 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| underdog|d2d0c7f6-8c34-47ab-83c4-c4cc40e11773 | underdog | Elijah Moore | Receptions | over | 0.06688940577179958 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|8f9a7a73-acd6-4922-a1e5-c9b931fd47c8 | underdog | Samaje Perine | Receiving Yards | over | 0.06675361243904465 | 2026-11-06T06:34:07Z | 2026-11-08T14:30:00Z |
| underdog|480b8a53-750b-4531-914d-b24d9cc3be67 | underdog | Gunner Stockton | Pass TDs | over | 0.06653840324761084 | 2026-11-04T12:10:41Z | 2026-11-08T00:30:00Z |
| underdog|2e7bbe15-ae7b-4e61-95a5-06eb33a2c36c | underdog | TreyShun Hurry | Receiving Yards | under | 0.06646789670162756 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| underdog|d626307e-fd2a-4fe3-92e2-930891893f36 | underdog | Xavier Worthy | Receiving Yards | under | 0.06645128079909246 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|04e3d271-e34b-44fe-afc2-3053765e9382 | underdog | Rocco Becht | Pass Yards | under | 0.06641234513659888 | 2026-11-06T16:02:47Z | 2026-11-07T20:30:00Z |
| underdog|1d53d129-af23-4475-a215-9d2a7ab7ccdc | underdog | Aaron Butler | Receiving Yards | over | 0.06636089137826207 | 2026-11-07T05:59:57Z | 2026-11-08T03:30:00Z |
| prizepicks|16719164 | prizepicks | Quentin Johnston | Rec Targets | under | 0.06632694700699171 | 2026-11-05T22:06:44Z | 2026-11-08T16:05:00.000-05:00 |
| underdog|d4f2b5ca-0b3f-4658-962d-e49d13b62596 | underdog | Mike Gesicki | Receptions | under | 0.06624716319361124 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|fc8a7d1c-fc88-48bd-9122-4cea2b71c647 | underdog | Xavier Hutchinson | Receptions | under | 0.06623799366444505 | 2026-11-05T12:22:13Z | 2026-11-08T21:05:00Z |
| underdog|cdc62382-2a50-4934-b1a5-b8921613a738 | underdog | Tyler Robles | FG Made | over | 0.06621739274981686 | 2026-11-05T22:06:44Z | 2026-11-07T20:30:00Z |
| underdog|97eab18d-9198-41a6-9923-15704c5dbe65 | underdog | Breece Hall | Rush Yards | under | 0.0661698771066409 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|75e1cf1b-6b66-49ca-b1a6-9f711b760bf0 | underdog | Malik Washington | Pass TDs | under | 0.06594882399474966 | 2026-11-05T22:06:44Z | 2026-11-07T17:30:00Z |
| underdog|cbc93e7f-1d7b-4b99-bb7d-ed15c78a51cd | underdog | Trinidad Chambliss | Pass TDs | over | 0.06592267044885508 | 2026-11-05T22:06:44Z | 2026-11-08T00:30:00Z |
| underdog|17d196b6-916b-4467-86c8-3e43337d1b9d | underdog | Josh Jacobs | Receiving Yards | under | 0.06580018595374104 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|6aa63bf6-5f9f-49aa-ac6c-61b07f0550b9 | underdog | Nate Frazier | Rush Yards | under | 0.06577512496131055 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| underdog|e2076474-ba9e-4c4a-8a5e-8756583f0c4e | underdog | Woody Marks | Receiving Yards | under | 0.06554944061032464 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|71e69c89-9416-48e2-8510-0ea58166063c | underdog | Nolan James | Rush Yards | under | 0.0654334067101523 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| underdog|c86a5941-5458-4c00-a866-b4c36c12b698 | underdog | Abu Sama | Rush Yards | under | 0.06542451129512794 | 2026-11-07T05:59:57Z | 2026-11-07T21:15:00Z |
| prizepicks|16629444 | prizepicks | Wayne Knight | Rush Atts | under | 0.06520056369225546 | 2026-11-05T12:22:13Z | 2026-11-07T12:00:00.000-05:00 |
| underdog|e4642e1c-4d1c-4cf5-ae5c-ecefd90f40fa | underdog | Bear Bachmeier | Pass Yards | under | 0.06516151905997936 | 2026-11-07T05:59:57Z | 2026-11-07T17:00:00Z |
| underdog|08c193ae-a42a-4cef-baae-3446408bfea6 | underdog | Brandon Dorlus | Sacks | over | 0.06498885077008221 | 2026-11-07T05:59:57Z | 2026-11-08T14:30:00Z |
| underdog|1d02ab45-4ffa-4cd8-80e2-89f52af64442 | underdog | Drew Sample | Receptions | under | 0.0648910280627768 | 2026-11-05T22:06:44Z | 2026-11-08T14:30:00Z |
| underdog|f73cd894-e700-447a-a19a-ffd9430bccf9 | underdog | Fame Ijeboi | Receiving Yards | over | 0.06485217903342089 | 2026-11-07T05:59:57Z | 2026-11-07T17:30:00Z |
| underdog|b13bd436-9bc2-4867-9041-17de5aa4b928 | underdog | Michael Wilson | Receiving Yards | under | 0.06474486073770425 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|1466368e-c6ce-4de6-8814-1a5e1d544d1d | underdog | Spencer Porath | FG Made | under | 0.06463882026125989 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|02786b90-2bf8-4d28-b6ba-7f67d543487c | underdog | Kenny Minchey | Rush Yards | over | 0.06459483050649784 | 2026-11-06T16:02:47Z | 2026-11-07T23:15:00Z |
| underdog|c2e72da7-57b8-4745-88a0-0d4c76c0605f | underdog | Dierre Hill | Receiving Yards | over | 0.06458080316330339 | 2026-11-06T16:02:47Z | 2026-11-07T20:30:00Z |
| underdog|eca101aa-7a51-4f52-8a79-df3c0476d223 | underdog | Tee Higgins | Receiving Yards | under | 0.06449641229795078 | 2026-11-07T05:59:57Z | 2026-11-08T14:30:00Z |
| underdog|c003d9a0-b854-4b49-a3a5-76ff450c728f | underdog | Drake Maye | Rush Yards | under | 0.06447110335510176 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|1e146d1e-95ac-4e18-b97f-874278e4440b | underdog | Emmett Johnson | Rush Yards | under | 0.06444132725080376 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| prizepicks|16719175 | prizepicks | Jordan Addison | Rec Targets | under | 0.06403524396214921 | 2026-11-05T22:06:44Z | 2026-11-09T20:15:00.000-05:00 |
| prizepicks|16718525 | prizepicks | Tee Higgins | Rec Targets | under | 0.06403084263606129 | 2026-11-05T22:06:44Z | 2026-11-08T09:30:00.000-05:00 |
| underdog|e5598605-b771-40d4-a896-945151550af7 | underdog | JC French | Pass Yards | under | 0.0637897607221598 | 2026-11-05T12:22:13Z | 2026-11-07T20:30:00Z |
| underdog|ad403e28-28f4-44aa-b294-d189aa2c4052 | underdog | Tre Richardson | Receiving Yards | under | 0.0636759078749245 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| underdog|8ece24e0-b2e4-4fa3-b6b4-5845b58f2de9 | underdog | Kenny Minchey | Pass Yards | under | 0.06358679107944964 | 2026-11-05T12:22:13Z | 2026-11-07T23:15:00Z |
| underdog|21931440-adec-46d4-b530-994878d9e427 | underdog | T.J. Hockenson | Receptions | under | 0.06344057443403939 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|030a66ea-977b-4f3f-80ab-d9d5dfb20bb1 | underdog | Josaiah Stewart | Sacks | over | 0.06277768727226701 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|6e1d2faa-53bc-4614-85f1-5eff7dde4705 | underdog | Micahi Danzy | Receiving Yards | under | 0.06268918018385916 | 2026-11-07T05:59:57Z | 2026-11-07T17:00:00Z |
| underdog|0ee8521a-fe6c-45c4-b60f-27c989d509bb | underdog | Isaiah Sategna | Receptions | under | 0.06266066906186729 | 2026-11-07T05:59:57Z | 2026-11-08T00:45:00Z |
| underdog|e85c31f7-9c9e-4d10-b893-980e11cee71d | underdog | Chas Nimrod | Receiving Yards | under | 0.062088814076110665 | 2026-11-06T06:34:07Z | 2026-11-07T17:45:00Z |
| underdog|dd1f7172-8330-424d-ac7f-1765ab353fcc | underdog | Dominic Zvada | Kicking Points | under | 0.062049653446879294 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|9dfe3551-4211-4740-9630-00673ecb5fd1 | underdog | Lawson Luckie | Receiving Yards | over | 0.062012665421168345 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| prizepicks|16567865 | prizepicks | Michael Penix Jr. | Pass TDs | under | 0.06194406494725502 | 2026-11-05T12:22:13Z | 2026-11-08T09:30:00.000-05:00 |
| underdog|adeae18f-e6d9-4b71-855a-d10140f61576 | underdog | Jadon Porter | Receiving Yards | over | 0.06181736022618467 | 2026-11-05T22:06:44Z | 2026-11-07T17:00:00Z |
| prizepicks|16577034 | prizepicks | Denzel Boston | Rec Yards | under | 0.06162987154195598 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| prizepicks|16718512 | prizepicks | Tetairoa McMillan | Rec Targets | under | 0.06149813023951123 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|94533c8c-852b-436b-8c3e-30871f71ee63 | underdog | Devin McCuin | Receptions | over | 0.061271839861702426 | 2026-11-05T12:22:13Z | 2026-11-07T20:30:00Z |
| underdog|8c265bcd-7b60-4798-8607-03c1259a21e4 | underdog | Trey Smack | FG Made | under | 0.06104007152947344 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|c2bc47c2-6d3f-48ee-b74d-c4f141f4a11a | underdog | Kayshon Boutte | Receiving Yards | over | 0.060977623679458914 | 2026-11-05T22:06:44Z | 2026-11-08T21:05:00Z |
| underdog|a61e4818-f9a9-40ba-9525-901a49827383 | underdog | Ashton Gillotte | Sacks | over | 0.06091287239348786 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| prizepicks|16747633 | prizepicks | Jaxon Smith-Njigba | Recs | under | 0.060819500508052626 | 2026-11-07T05:59:57Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|fac4af10-165a-4177-944e-51ad9c5660f6 | underdog | Matt Gay | FG Made | over | 0.06076705695301998 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| prizepicks|16722942 | prizepicks | Kenny Gainwell | Recs | under | 0.06053274770535577 | 2026-11-06T06:34:07Z | 2026-11-08T20:20:00.000-05:00 |
| underdog|99a82066-3195-47f8-b8e0-1a8bb7c63ca5 | underdog | Wayshawn Parker | Receiving Yards | over | 0.060436074136964946 | 2026-11-06T06:34:07Z | 2026-11-07T17:00:00Z |
| underdog|3814f339-5522-40ce-a555-8b7dbed6eb31 | underdog | Richard Young | Rush Yards | under | 0.060345052741267335 | 2026-11-05T22:06:44Z | 2026-11-08T00:30:00Z |
| underdog|b63dda4c-3a4d-4fab-ae5b-aff547a35d1a | underdog | Byron Murphy | Sacks | over | 0.06032788374603604 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|89bf3086-6c57-4848-8ed7-79f582630a28 | underdog | Bijan Robinson | Receiving Yards | under | 0.060310445002568436 | 2026-11-07T05:59:57Z | 2026-11-08T14:30:00Z |
| underdog|75fc0d6b-fc95-4755-9dca-a70f72575381 | underdog | Kimani Vidal | Rush + Rec Yards | under | 0.060182508715502125 | 2026-11-05T22:06:44Z | 2026-11-08T21:05:00Z |
| underdog|a8ad8c01-d305-4c34-acba-08ca7c916fe2 | underdog | Fredrick Moore | Receptions | over | 0.06015246576576805 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| underdog|d29599ad-f597-4f28-9d87-acf1c29a3761 | underdog | Elijah Higgins | Receptions | under | 0.060018765343776814 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|ce15f976-d7f9-425f-ad6c-ee1a00299302 | underdog | Jahmyr Gibbs | Receiving Yards | under | 0.059821904171410645 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| underdog|d0960391-8a29-49e1-adce-9b8b9a13efe6 | underdog | Kimani Vidal | Receptions | under | 0.0595189274468374 | 2026-11-05T12:22:13Z | 2026-11-08T21:05:00Z |
| underdog|5a604162-06d7-42a5-b871-10416c6fa8b6 | underdog | Tommy Carr | Pass TDs | under | 0.059415967714466 | 2026-11-05T22:06:44Z | 2026-11-08T00:30:00Z |
| underdog|916f1df1-ba2e-4941-afab-e810893e7a42 | underdog | T.J. Moore | Receiving Yards | under | 0.059412338792715014 | 2026-11-07T05:59:57Z | 2026-11-07T17:00:00Z |
| underdog|78f92e19-5c31-4d49-a704-dea3e1ea7994 | underdog | Foster Moreau | Receptions | over | 0.05932154173705445 | 2026-11-05T12:22:13Z | 2026-11-08T21:05:00Z |
| underdog|9e0726a2-3823-4a1d-af18-84f75d474180 | underdog | Laquon Treadwell | Receiving Yards | over | 0.0592842827369362 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|3b554414-84d2-41b4-93ac-fceb51bfce89 | underdog | Dilin Jones | Receptions | under | 0.05910993829171962 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|a10e90f9-892e-489b-87e7-98258489a4ec | underdog | Chig Okonkwo | Receptions | under | 0.05901702938378406 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|9010dad9-5de4-4ca5-b504-7ea92845c328 | underdog | Rocco Becht | Rush Yards | over | 0.059015051888118064 | 2026-11-05T22:06:44Z | 2026-11-07T20:30:00Z |
| underdog|2a653086-3e16-4ac1-914c-1cb0566bc49c | underdog | Drake Lindsey | Pass Yards | under | 0.058996248550600816 | 2026-11-07T05:59:57Z | 2026-11-07T17:00:00Z |
| underdog|709de301-20f0-40b2-94fe-988e8519057f | underdog | Derrick Salley | Receptions | over | 0.05885146289683518 | 2026-11-06T16:02:47Z | 2026-11-07T18:00:00Z |
| underdog|464fbf32-ce38-4c8f-bc70-190cf5d64c92 | underdog | MarShawn Lloyd | Receptions | under | 0.05868983465783262 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| prizepicks|16718559 | prizepicks | Travis Kelce | Rec Targets | under | 0.058686248860410406 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|cd4c17b5-3de5-4eab-a1a1-61fb1258f334 | underdog | Noah Gray | Receiving Yards | over | 0.05866094475782779 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| prizepicks|16719167 | prizepicks | Puka Nacua | Rec Targets | under | 0.05865213234044242 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|5c1dad6e-619c-4575-9b10-738e17d39df7 | underdog | Ashton Jeanty | Receiving Yards | under | 0.05850227908119554 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|d146dfb3-fcb5-4654-a1f6-64215170adeb | underdog | Jessica Pegula | Double Faults | under | 0.05846688292835567 | 2026-11-05T12:22:13Z | 2026-11-08T21:10:00Z |
| underdog|8a748e05-956a-4a40-a6dc-c7788188b33f | underdog | Carson Wentz | Pass TDs | under | 0.058336194057320934 | 2026-11-05T22:06:44Z | 2026-11-10T01:15:00Z |
| underdog|097f1c9d-9fd7-4c66-b024-b6f792a6ddbe | underdog | Raleek Brown | Rush Yards | under | 0.05828535641008248 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| prizepicks|16764331 | prizepicks | Keenan Allen | Rec Targets | under | 0.05809862236222918 | 2026-11-07T05:59:57Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|48976ef6-8d95-4c1d-a8fa-44dfc3933b21 | underdog | Sedrick Alexander | Receiving Yards | over | 0.05801941082225981 | 2026-11-06T16:02:47Z | 2026-11-07T21:15:00Z |
| underdog|089ce83f-49f9-46ad-83c1-06b27856f11e | underdog | Tyler Shough | Pass TDs | under | 0.0579713928349842 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|c7f223f5-1db6-4b90-9fbb-b219544bd20b | underdog | Jaleel Skinner | Receiving Yards | over | 0.0579671544436442 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|ad0ea752-bb12-4e4b-9043-e33648c25e24 | underdog | Caden Buhr | XP Made | over | 0.057932058232053274 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| underdog|0cbe8572-f373-40c7-bc91-3896efd0ba18 | underdog | Evan Stewart | Receiving Yards | over | 0.05781868428032133 | 2026-11-05T12:22:13Z | 2026-11-07T20:30:00Z |
| underdog|ef93512e-7037-4e52-adab-e5a0e92cb14b | underdog | Kyler Kasper | Receptions | under | 0.0577929902830534 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|363f2a86-aea7-488d-8f25-6c2926e28588 | underdog | Michael Penix | Pass TDs | under | 0.05769866616807584 | 2026-11-03T02:21:46Z | 2026-11-08T14:30:00Z |
| underdog|94b26160-85f3-4b0e-a636-0a205a4a8a14 | underdog | Omarion Hampton | Rush + Rec Yards | under | 0.057685561031392885 | 2026-11-05T22:06:44Z | 2026-11-08T21:05:00Z |
| underdog|d02386e9-a6be-491a-b11c-0db9561342f3 | underdog | Omarion Hampton | Rush Yards | under | 0.0574974439645306 | 2026-11-05T22:06:44Z | 2026-11-08T21:05:00Z |
| underdog|46de4846-772b-426c-98aa-b79baea8c771 | underdog | Daylyn Upshaw | Receiving Yards | under | 0.05737593089779203 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| underdog|1a9bb6cc-8c99-4567-9740-702629fc8b15 | underdog | Mazeo Bennett | Receptions | under | 0.05730068954397416 | 2026-11-05T22:06:44Z | 2026-11-07T20:00:00Z |
| underdog|82215f35-d978-41ed-b4b6-3e1171e32afc | underdog | Austin Simmons | Pass TDs | under | 0.05701792055392729 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|623fe967-1a3e-408f-b0cb-0bf7da802b8a | underdog | Dak Prescott | Rush Yards | over | 0.0570102313442149 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|339dfeab-cb61-44a6-9848-fa07b1efb7d6 | underdog | Isaiah Likely | Receiving Yards | under | 0.056810368159812774 | 2026-11-06T16:02:47Z | 2026-11-08T18:00:00Z |
| underdog|b094236c-ba86-4187-9f50-dfd372652b8b | underdog | Tre Tucker | Receptions | under | 0.05656143515129497 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|befbd56b-e648-4437-a050-c9ecb32ce65a | underdog | Corey Kiner | Rush + Rec Yards | under | 0.05651284215717434 | 2026-11-06T06:34:07Z | 2026-11-08T21:25:00Z |
| underdog|2cf795d7-7279-4cdf-9ea4-10556bd4239d | underdog | Kenyon Sadiq | Receptions | over | 0.056179967492667515 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| underdog|c552c9c9-592c-4f2a-96df-9a5186ec5288 | underdog | Jordan Watkins | Receiving Yards | under | 0.055954042538513216 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|72424239-3938-4c03-a39e-4cf5eebc76fd | underdog | Ashton Daniels | Rush Yards | under | 0.05590103432432425 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|e5503b49-7874-4785-b938-ac08739aa23c | underdog | Billy Edwards Jr. | Pass TDs | under | 0.055860973923938406 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|48603add-d136-41df-b578-2323b8a1caa7 | underdog | Rome Odunze | Receptions | under | 0.05570918963942184 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| prizepicks|16719193 | prizepicks | Rachaad White | Rec Targets | under | 0.055479385567673956 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|576dea48-0362-40ff-bbc7-4d600aa0c3eb | underdog | Jasen Lopez | Receiving Yards | under | 0.05534967196718521 | 2026-11-07T05:59:57Z | 2026-11-07T17:00:00Z |
| underdog|3c4aee76-fb32-4603-82d0-81351387b1e1 | underdog | Kalif Raymond | Receptions | under | 0.05532157679971539 | 2026-11-05T12:22:13Z | 2026-11-09T01:20:00Z |
| underdog|427bc80b-e945-486b-9ec5-7ba8b62834fc | underdog | Xavier Townsend | Receptions | under | 0.05517067322536984 | 2026-11-07T05:59:57Z | 2026-11-07T17:30:00Z |
| underdog|34449ba5-6c3b-4058-89ac-dc2b1a964011 | underdog | Gavin Freeman | Receiving Yards | under | 0.055022448485784525 | 2026-11-07T05:59:57Z | 2026-11-07T17:00:00Z |
| prizepicks|16591338 | prizepicks | Legend Glasker | Recs | under | 0.05484893867418028 | 2026-11-07T05:59:57Z | 2026-11-07T12:00:00.000-05:00 |
| underdog|a31317ee-e954-402a-9e50-4a55ffc781d1 | underdog | Jaylen Raynor | Pass TDs | under | 0.0548056389593522 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|19a672f3-50fe-4033-813c-78daf721de03 | underdog | Mike Washington | Rush Yards | under | 0.05471570014322025 | 2026-11-05T22:06:44Z | 2026-11-08T21:25:00Z |
| underdog|844d8994-eb1a-4135-917e-a68c00abf5fd | underdog | Tre' Harris | Receptions | under | 0.05470210954117727 | 2026-11-05T12:22:13Z | 2026-11-08T21:05:00Z |
| prizepicks|16577036 | prizepicks | KC Concepcion Jr. | Rec Yards | under | 0.054101039282902996 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|c8bc6703-2575-48fb-882d-552dec5fa35b | underdog | Will Anderson | Sacks | under | 0.05383010059274007 | 2026-11-06T16:02:47Z | 2026-11-08T21:05:00Z |
| underdog|1c2cde05-b6d7-4474-9d9e-8f9b3062e070 | underdog | Puka Nacua | Receptions | under | 0.05380728482585917 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|842bc578-6187-4436-957e-ffb1f930407f | underdog | Jalen Carter | Sacks | over | 0.05377588226612223 | 2026-11-06T16:02:47Z | 2026-11-08T18:00:00Z |
| underdog|e01ed5ff-4bf0-4328-80bb-372c2a56d1cb | underdog | Jeremiah Smith | Receptions | under | 0.053719870131973324 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|c94fc177-351e-4cf6-b5ae-279382f8d5d6 | underdog | DJ Epps | Receiving Yards | over | 0.05362823071314371 | 2026-11-07T05:59:57Z | 2026-11-08T02:30:00Z |
| underdog|e55382b2-c395-46d4-8518-8309c9d2f8e4 | underdog | JC French | Rush Yards | over | 0.053385662154178726 | 2026-11-05T12:22:13Z | 2026-11-07T20:30:00Z |
| underdog|97889cee-bb36-4d05-b351-a674927b93e5 | underdog | Braylon Staley | Receiving Yards | under | 0.053369351238770846 | 2026-11-05T12:22:13Z | 2026-11-07T23:15:00Z |
| underdog|99270f6f-8733-4028-bd25-d928db30fcf7 | underdog | Nolan Smith | Sacks | over | 0.053314777961707804 | 2026-11-06T16:02:47Z | 2026-11-08T18:00:00Z |
| underdog|1f6ec128-0f98-4fab-b889-6fa33628a38b | underdog | Reggie Virgil | Receptions | under | 0.053005643668652125 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|9e0cfe1d-3ce4-4cf3-bce8-09e661cb3cda | underdog | Ryan Flournoy | Receptions | under | 0.052546796586534494 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|5d4a6a94-4490-4488-8f26-0d4ccba55e0b | underdog | Savion Williams | Receiving Yards | under | 0.0525122155374117 | 2026-11-05T22:06:44Z | 2026-11-08T21:25:00Z |
| underdog|f4af8d61-8588-4d80-ac8d-fd8686a33979 | underdog | Malik Willis | Rush Yards | under | 0.052470845197019944 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|94778805-8555-4a67-807c-f8d41fd8a493 | underdog | Devin Singletary | Receptions | under | 0.05222811479089262 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|7c09637f-ba5b-48d9-a7b4-45cc01362313 | underdog | Justin Herbert | Rush Yards | under | 0.05178516711907766 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| prizepicks|16718497 | prizepicks | DJ Moore | Rec Targets | under | 0.051713641503083774 | 2026-11-05T22:06:44Z | 2026-11-09T20:15:00.000-05:00 |
| underdog|869a7e09-7c79-4455-8086-4b56a7f32e78 | underdog | Cale Hellums | Rush Yards | under | 0.05162659325917196 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| prizepicks|16578332 | prizepicks | Braylon Staley | Recs | under | 0.05153228331798554 | 2026-11-05T12:22:13Z | 2026-11-07T18:15:00.000-05:00 |
| underdog|0bd7ee4e-5003-468e-a88a-b15e135713a5 | underdog | Keshaun Singleton | Receiving Yards | under | 0.05152161739055083 | 2026-11-06T06:34:07Z | 2026-11-07T17:45:00Z |
| underdog|56673d79-098e-485c-841d-1347c9ef4713 | underdog | Byrum Brown | Rush Yards | under | 0.05125785355040946 | 2026-11-06T06:34:07Z | 2026-11-07T17:45:00Z |
| underdog|ae9feb9a-cc75-49a8-9744-feccd9e646e8 | underdog | Caleb Cunningham | Receiving Yards | over | 0.0512343320727765 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| underdog|2c7f04e3-5df3-4a7c-b23f-467ddcc56597 | underdog | Felix Anudike-Uzomah | Sacks | over | 0.05076321889237018 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|30fb664e-b7e5-416c-84d9-9981ffc6a84f | underdog | Rico Scott | Receptions | under | 0.050697211562924394 | 2026-11-05T22:06:44Z | 2026-11-07T20:30:00Z |
| underdog|e46702d6-ae35-43c0-ab3b-2e638d0153d9 | underdog | Chad Ryland | Kicking Points | over | 0.0506262653818188 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| prizepicks|16718517 | prizepicks | D'Andre Swift | Rec Targets | under | 0.0506216499863863 | 2026-11-05T22:06:44Z | 2026-11-08T20:20:00.000-05:00 |
| underdog|b4bf9f2b-e849-446b-a805-eda4d01af7be | underdog | Khalil Shakir | Receiving Yards | under | 0.05058312311415858 | 2026-11-04T12:10:41Z | 2026-11-10T01:15:00Z |
| underdog|6d2ef97d-85ec-4784-b781-eb26c8048aba | underdog | Ashton Daniels | Pass Yards | under | 0.050551246622958734 | 2026-11-06T06:34:07Z | 2026-11-07T17:00:00Z |
| underdog|1693d984-d750-403e-a1ed-b4bd544d6f9f | underdog | Kalieb Osborne | Pass Yards | under | 0.05049321800349771 | 2026-11-07T05:59:57Z | 2026-11-07T17:00:00Z |
| prizepicks|16718531 | prizepicks | George Pickens | Rec Targets | under | 0.050469580643767276 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|065a2ce0-b802-4321-9321-acb62214d65b | underdog | Nyck Harbor | Receptions | under | 0.05046765911819062 | 2026-11-05T22:06:44Z | 2026-11-07T20:00:00Z |
| underdog|cc6e5df1-5a0b-4ad2-972e-574952cbd39c | underdog | Tez Johnson | Receptions | over | 0.050436099256353284 | 2026-11-05T22:06:44Z | 2026-11-09T01:20:00Z |
| underdog|6a30bff5-d45d-45f9-a712-6c98fba34405 | underdog | Lloyd Avant | Rush Yards | over | 0.05041483365885191 | 2026-11-05T12:22:13Z | 2026-11-08T00:45:00Z |
| underdog|10137e54-30a8-4417-bed5-eaf56c7f25f2 | underdog | Keelon Russell | Total TDs | under | 0.05041396131611464 | 2026-11-07T05:59:57Z | 2026-11-07T20:30:00Z |
| prizepicks|16747852 | prizepicks | Adonai Mitchell | Rec Targets | under | 0.050348304928793275 | 2026-11-07T05:59:57Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|73d6a771-2b52-47b4-973b-dd93929c3b04 | underdog | Mark Fletcher Jr. | Rush Yards | under | 0.0502651918263225 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| underdog|306d32c9-76be-44a5-b65c-2d983b4ebc2f | underdog | Ashton Jeanty | Rush + Rec Yards | under | 0.05021547727948117 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|d2238038-a14f-4a2b-b446-901361297d68 | underdog | Bryant Wesco | Receiving Yards | under | 0.05009854214019316 | 2026-11-07T05:59:57Z | 2026-11-07T17:00:00Z |
| prizepicks|16719165 | prizepicks | Tre' Harris | Rec Targets | under | 0.050059523885883084 | 2026-11-05T22:06:44Z | 2026-11-08T16:05:00.000-05:00 |
| prizepicks|16718528 | prizepicks | Harold Fannin Jr. | Rec Targets | under | 0.05005687630552147 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|e0bc863f-aad7-4457-ae95-0614baf0c40d | underdog | Tetairoa McMillan | Receiving Yards | under | 0.05000311569825844 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| prizepicks|16764330 | prizepicks | Josh Downs | Rec Targets | under | 0.049962199665539164 | 2026-11-07T05:59:57Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|ff3f65e5-9fbe-4b2a-b0f2-9abc59d7b211 | underdog | Kendre Miller | Receptions | over | 0.04992471595146514 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| prizepicks|16689247 | prizepicks | Jaylen Raynor | Pass Comp | under | 0.04991824096266417 | 2026-11-06T16:02:47Z | 2026-11-07T12:00:00.000-05:00 |
| underdog|baa91d86-f682-4be6-b563-5276f85cf08e | underdog | Laquon Treadwell | Receptions | over | 0.04989017476712326 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|fc8c7bdd-6f0b-4802-8874-c12236925669 | underdog | Jaylen Raynor | Pass Yards | under | 0.04980050697892513 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|0e903253-2ce7-4e04-915a-52f50072a481 | underdog | Micah Gilbert | Receptions | under | 0.04969367825159132 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| underdog|5c7db0c1-b817-4e58-97f1-3b1644efad4e | underdog | Eric Olsen | Receptions | under | 0.049626369625917044 | 2026-11-06T16:02:47Z | 2026-11-08T03:30:00Z |
| underdog|05dd22e1-8750-4c3e-8ee3-e81b03fc6a7e | underdog | CJ Brown | Receiving Yards | over | 0.04946085419622448 | 2026-11-07T05:59:57Z | 2026-11-07T17:45:00Z |
| underdog|da32429e-2136-492e-ade0-808946db1392 | underdog | Dalton Kincaid | Receiving Yards | under | 0.049312018647535094 | 2026-11-05T12:22:13Z | 2026-11-10T01:15:00Z |
| underdog|16a598cc-777f-476a-94bd-894a6aea7c88 | underdog | Saquon Barkley | Receiving Yards | under | 0.04908165109388163 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|807c529e-31ff-4c65-9ac7-c60639f1a1f4 | underdog | Jayden Daniels | Rush Yards | under | 0.049059514309005126 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| prizepicks|16577037 | prizepicks | Chris Olave | Rec Yards | under | 0.04898251964490763 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|0e309daa-2938-4ba3-bfed-2478a9165635 | underdog | Sheldon Rankins | Sacks | over | 0.04891440650428508 | 2026-11-06T16:02:47Z | 2026-11-08T21:05:00Z |
| underdog|076c3eea-9331-4033-a108-3edf0279b36a | underdog | Ty Johnson | Receiving Yards | over | 0.048848215340260515 | 2026-11-07T05:59:57Z | 2026-11-10T01:15:00Z |
| underdog|f846cfba-c825-4e6b-aac9-0975e8c6604a | underdog | Kayshon Boutte | Receptions | over | 0.04870573326693556 | 2026-11-05T12:22:13Z | 2026-11-08T21:05:00Z |
| underdog|6b69088c-d4a8-4159-bbd0-3e2170aae7d7 | underdog | Brad Jackson | Pass TDs | under | 0.048348152610976136 | 2026-11-05T12:22:13Z | 2026-11-08T03:30:00Z |
| prizepicks|16718496 | prizepicks | Dalton Kincaid | Rec Targets | under | 0.04809003370519738 | 2026-11-05T22:06:44Z | 2026-11-09T20:15:00.000-05:00 |
| underdog|1b0eb045-4271-4dec-a604-a4c38773225d | underdog | Aidan Birr | XP Made | over | 0.048078044601977676 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| prizepicks|16718501 | prizepicks | James Cook III | Rec Targets | under | 0.04803584807788108 | 2026-11-05T22:06:44Z | 2026-11-09T20:15:00.000-05:00 |
| underdog|c4be67dc-c7c4-48f2-9278-1cc9a6e5fc5f | underdog | Jacobo Echeverria Lozano | XP Made | under | 0.04797316880475955 | 2026-11-05T22:06:44Z | 2026-11-07T17:30:00Z |
| underdog|af9d31c5-4093-48e5-9c73-16834bfcafca | underdog | Kyle Williams | Receptions | under | 0.04785175956387744 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|948ab33a-471b-43e9-a769-d9b49a5d2f46 | underdog | Keyjuan Brown | Rush Yards | under | 0.04782822287222155 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| prizepicks|16718533 | prizepicks | Ryan Flournoy | Rec Targets | under | 0.04782445339134278 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|3a32e19a-0fef-4030-8ab3-2d408c35ef7c | underdog | Roschon Johnson | Rush Yards | under | 0.04778124403200101 | 2026-11-06T16:02:47Z | 2026-11-09T01:20:00Z |
| underdog|2ed7f40f-b244-40e5-84d0-d9f0b5d07cd6 | underdog | Dylan Sampson | Rush + Rec Yards | under | 0.04775265425710307 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|1441af20-ca44-43f2-b7f8-3dc65dac1fb6 | underdog | Jadan Baugh | Rush Yards | under | 0.047469000409556705 | 2026-11-05T12:22:13Z | 2026-11-08T00:45:00Z |
| underdog|0729c05e-e380-4efb-b2ae-e1403174fb84 | underdog | Samaje Perine | Receptions | over | 0.04737537544984716 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|19b2351e-eb15-4140-b1bf-fe796bd84c84 | underdog | Mario Craver | Receiving Yards | under | 0.04715427984540055 | 2026-11-07T05:59:57Z | 2026-11-07T20:00:00Z |
| prizepicks|16567035 | prizepicks | Jordan Love | Pass TDs | under | 0.04710112679060341 | 2026-11-04T12:10:41Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|8d98abf4-bc5e-4549-90db-f4eca6824ba0 | underdog | Bucky Irving | Rush + Rec Yards | under | 0.04692066418821539 | 2026-11-05T12:22:13Z | 2026-11-09T01:20:00Z |
| underdog|c31e50a6-b4e5-4af9-ac64-d81b415e67e7 | underdog | Eli Stowers | Receptions | under | 0.04667380971321278 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|456f6f92-c8bc-4cf8-a392-d17744c18fd9 | underdog | Torrance Burgess | Receiving Yards | over | 0.04649235335470303 | 2026-11-06T16:02:47Z | 2026-11-08T03:30:00Z |
| underdog|8ac17bbc-0479-482d-b6ca-4651a3b3a2f0 | underdog | Drew Stevens | Kicking Points | under | 0.04644611027329182 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|c500a3b7-b47d-4d68-a519-a1138350ca4a | underdog | Danielle Hunter | Sacks | under | 0.04641239576866374 | 2026-11-06T16:02:47Z | 2026-11-08T21:05:00Z |
| prizepicks|16719177 | prizepicks | Alvin Kamara | Rec Targets | under | 0.04592092233766798 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|6840c1d4-0dc2-48d1-9e3d-699321becaf1 | underdog | LaNorris Sellers | Pass TDs | under | 0.04584495188446647 | 2026-11-05T22:06:44Z | 2026-11-07T20:00:00Z |
| underdog|f4c06e1a-224a-4c62-b703-ec0468d2809a | underdog | Ty Dieffenbach | Pass Yards | under | 0.04550553825367998 | 2026-11-05T22:06:44Z | 2026-11-07T17:00:00Z |
| prizepicks|16722941 | prizepicks | Emeka Egbuka | Recs | under | 0.04538182348359732 | 2026-11-06T06:34:07Z | 2026-11-08T20:20:00.000-05:00 |
| underdog|76f3f1d7-5244-48ed-80c8-4f59cff15006 | underdog | George Karlaftis | Sacks | under | 0.04533238139975149 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|4de62797-41a0-4d69-977b-0286517b1b34 | underdog | Alvin Kamara | Receptions | under | 0.0452076759340746 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|7a72d0be-60ae-4376-8aa1-07e785aab859 | underdog | Jonathan Taylor | Receptions | under | 0.04508721237534341 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|0f9959d0-f9a2-474d-82e2-77981b9f03c0 | underdog | J.K. Dobbins | Rush + Rec Yards | under | 0.04497859513044955 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| underdog|ed64751e-387e-4ef6-a650-bd99d8ebe329 | underdog | Maria Sakkari | Double Faults | under | 0.044969499282676684 | 2026-11-07T05:59:57Z | 2026-11-07T08:00:00Z |
| underdog|cf17c955-70db-444c-8dd5-7a49295bfd2d | underdog | Harold Fannin | Receiving Yards | under | 0.044875701368678134 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|64b35a78-7c9c-4a69-ab32-52beb9943671 | underdog | Kenny Johnson | Receiving Yards | under | 0.04474185000019171 | 2026-11-05T22:06:44Z | 2026-11-08T02:30:00Z |
| underdog|51e7af2b-f9a1-43ea-aa78-584f372553e2 | underdog | Trey Smack | Kicking Points | under | 0.04455434973971151 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|ea125837-d29b-4284-a90d-fee5aa2a9a96 | underdog | Chris Godwin | Receptions | under | 0.04434472697680247 | 2026-11-05T12:22:13Z | 2026-11-09T01:20:00Z |
| underdog|e5d081ab-9efa-43d3-bfb8-a43e2d593f85 | underdog | Drake Maye | Pass TDs | under | 0.04430737897190651 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|f30dd4e7-dacd-455c-8ed4-95be1fa5e74c | underdog | Karolina Muchova | Double Faults | under | 0.044153512874079426 | 2026-11-05T12:22:13Z | 2026-11-09T20:00:00Z |
| underdog|fa268a96-c011-4c35-9f2c-71018831b22d | underdog | Chase Brown | Receiving Yards | under | 0.044036182985406125 | 2026-11-05T12:22:13Z | 2026-11-08T14:30:00Z |
| prizepicks|16718543 | prizepicks | Jameson Williams | Rec Targets | under | 0.04401078613436993 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|5e087ca0-c81b-466a-a4ab-b25feaca7f84 | underdog | Noah Bennee | Receiving Yards | over | 0.04389551607024966 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|9815d49d-2af1-48c2-b6e4-cbe7c87349ac | underdog | Emmett Johnson | Receiving Yards | over | 0.043799798929959555 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|386a24ab-997f-4524-98d3-c932af517a2a | underdog | Rocky Beers | Receiving Yards | over | 0.04368039628251896 | 2026-11-05T22:06:44Z | 2026-11-08T00:45:00Z |
| underdog|d6a57db5-49c6-43d4-997b-75c80e636d09 | underdog | Jayden Limar | Rush Yards | under | 0.043609864830960965 | 2026-11-05T22:06:44Z | 2026-11-07T20:30:00Z |
| underdog|cead8aa7-e4be-42d2-921d-06cf913bc2f1 | underdog | Cornell Hatcher | Rush Yards | under | 0.04360260687627826 | 2026-11-06T16:02:47Z | 2026-11-08T03:30:00Z |
| underdog|2008fc2d-4b3f-4d3b-b372-948ea75bf0ff | underdog | AJ Newberry | Receptions | under | 0.04358383404136057 | 2026-11-06T06:34:07Z | 2026-11-08T03:30:00Z |
| underdog|87497741-2b97-4476-8dcf-178e6068cf64 | underdog | Ahmad Miller | Rush Yards | under | 0.04345194455899304 | 2026-11-07T05:59:57Z | 2026-11-07T17:00:00Z |
| underdog|9f8d5a76-cbb3-4565-b2d4-601b302e1c66 | underdog | Jojo Phillips | Receptions | over | 0.04343832039629403 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|cd71e455-3e3d-451d-bfb8-50f3d953f57f | underdog | Austin Ekeler | Receiving Yards | over | 0.04336736062987501 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| prizepicks|16763962 | prizepicks | Rasean Jones | Rec Yards | under | 0.04336721497026119 | 2026-11-07T05:59:57Z | 2026-11-07T18:00:00.000-05:00 |
| underdog|c2e9acd7-4e88-4f30-ae76-a25816dd4141 | underdog | Ricky Johnson | Receiving Yards | over | 0.043306631735705814 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|1075e7a4-7835-48a5-a2db-a78bbb0c36aa | underdog | Kalif Raymond | Receiving Yards | over | 0.04323294702184943 | 2026-11-05T12:22:13Z | 2026-11-09T01:20:00Z |
| underdog|4f3318f1-ea06-4e21-8393-c8600f035006 | underdog | Drake Lindsey | Pass TDs | under | 0.043228870596444424 | 2026-11-06T16:02:47Z | 2026-11-07T17:00:00Z |
| prizepicks|16557917 | prizepicks | Jordan Love | Rush Yards | under | 0.0431179313386405 | 2026-11-03T02:21:46Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|fe7a85f2-c21c-4535-88b9-b246e6af4d70 | underdog | Jason Sanders | FG Made | over | 0.04309576984353114 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|69d33979-906e-439f-b526-f612ed22aaaa | underdog | Gavin Lahm | FG Made | under | 0.04308668218923806 | 2026-11-05T12:22:13Z | 2026-11-07T21:15:00Z |
| underdog|7461ed14-7d77-45bb-9a57-07a5b4a25c13 | underdog | Wayshawn Parker | Receptions | over | 0.04308151190165166 | 2026-11-06T06:34:07Z | 2026-11-07T17:00:00Z |
| underdog|ef68a74d-d7a0-476d-bf6c-f7f526abd93c | underdog | Tyler Shough | Rush Yards | under | 0.042790287547065375 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|91f4a8ca-8e1b-4038-a81f-33103051637f | underdog | Darnell Mooney | Receptions | over | 0.04273058695676135 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|a5088759-dcc4-4d0c-acb8-516ddb05b069 | underdog | Noah Fant | Receptions | over | 0.04270940205899032 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|13125f3d-b469-4730-9996-2868e19905eb | underdog | Beau Sparks | Receiving Yards | under | 0.04258606297362333 | 2026-11-06T16:02:47Z | 2026-11-08T03:30:00Z |
| underdog|fd84fbbc-027f-4a5d-85f4-5775e64c1507 | underdog | Lincoln Kienholz | Pass Yards | under | 0.04238508942404251 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| underdog|e06a7ed3-05d6-4cba-9877-ecedc30f014a | underdog | Waden Charles | Receiving Yards | over | 0.042320465993419654 | 2026-11-07T05:59:57Z | 2026-11-07T20:45:00Z |
| prizepicks|16750457 | prizepicks | Luca Van Assche | Total Games Won | over | 0.04224858068907933 | 2026-11-07T05:59:57Z | 2026-11-07T08:30:00.000-05:00 |
| underdog|bce41d64-aa62-40b6-aed3-71790cf51f35 | underdog | Dallas Turner | Sacks | over | 0.04224694817072938 | 2026-11-07T05:59:57Z | 2026-11-10T01:15:00Z |
| underdog|7cb3fbf6-c9e4-47ff-8fdc-7ad015eff5a9 | underdog | Kenneth Walker III | Receiving Yards | under | 0.042196979680496294 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|06609665-f084-4b1b-affa-8cc4f9a90e0b | underdog | Omari Hayes | Receptions | over | 0.041906589246400505 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|da61ddb5-3d41-407e-89da-e6a14cbf2e38 | underdog | Jackson Harris | Receptions | under | 0.04185022899426438 | 2026-11-07T05:59:57Z | 2026-11-07T20:30:00Z |
| underdog|085c90df-5803-45fc-ac14-b28618abec44 | underdog | Aaron Jones | Receiving Yards | over | 0.04183150381663703 | 2026-11-05T22:06:44Z | 2026-11-10T01:15:00Z |
| underdog|f3620b29-6124-4e19-a85f-132532eb6a7f | underdog | Dierre Hill | Rush Yards | under | 0.041655654836731615 | 2026-11-07T05:59:57Z | 2026-11-07T20:30:00Z |
| underdog|25efe389-0f9d-4419-983d-72da4b9d01ba | underdog | Cyrus Allen | Receptions | under | 0.041551213577819546 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|5a21526e-525c-4f7e-868f-9d69447b4586 | underdog | Lotzeir Brooks | Receptions | over | 0.04144599539561733 | 2026-11-06T16:02:47Z | 2026-11-07T20:30:00Z |
| underdog|0c69b287-a405-436f-ac40-7401e48709ea | underdog | Tramell Jones | Pass TDs | under | 0.04138598652817316 | 2026-11-05T22:06:44Z | 2026-11-08T00:45:00Z |
| prizepicks|16667335 | prizepicks | Puka Nacua | Recs | under | 0.04136046632707657 | 2026-11-05T12:22:13Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|02cf2783-116d-4d08-a6ef-89bfcda4941e | underdog | Jalen Nailor | Receptions | under | 0.04129568937899364 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|127ded5d-257a-4c2a-bb25-88e0bd0debad | underdog | Jordan Love | Rush Yards | under | 0.04127202084950954 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| prizepicks|16718546 | prizepicks | Matthew Golden | Rec Targets | under | 0.04103027600826581 | 2026-11-05T22:06:44Z | 2026-11-08T16:25:00.000-05:00 |
| prizepicks|16701852 | prizepicks | Antwan Raymond | Rush Atts | under | 0.040920919788068 | 2026-11-05T12:22:13Z | 2026-11-07T16:15:00.000-05:00 |
| underdog|7adbec65-2635-4418-bf09-ab9e23b46b18 | underdog | CJ Bailey | Rush Yards | over | 0.04084183957976073 | 2026-11-05T22:06:44Z | 2026-11-07T17:30:00Z |
| underdog|6d997f10-2a2c-4d41-9c7d-f8d1105ddf10 | underdog | Devaughn Vele | Receptions | under | 0.04073632816474482 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|d63b8166-7ed3-4784-a290-53c755df307b | underdog | Rhamondre Stevenson | Receiving Yards | under | 0.04073261149509677 | 2026-11-06T06:34:07Z | 2026-11-08T21:25:00Z |
| underdog|52b06c24-0ece-49ed-9cd7-54e8013cf2b8 | underdog | Juwan Johnson | Receiving Yards | under | 0.04062551161927608 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|37ad3b9b-b644-4db3-95fd-a6dda1efec53 | underdog | Marshall Pritchett | Receptions | over | 0.04061687669708042 | 2026-11-05T12:22:13Z | 2026-11-07T20:30:00Z |
| prizepicks|16569328 | prizepicks | Nolan James Jr. | Rush Atts | under | 0.040603229600475466 | 2026-11-07T05:59:57Z | 2026-11-07T19:30:00.000-05:00 |
| prizepicks|16763961 | prizepicks | Rasean Jones | Recs | under | 0.040574880394428026 | 2026-11-07T05:59:57Z | 2026-11-07T18:00:00.000-05:00 |
| underdog|67ecfc13-7baa-495f-be1d-d0ec1521310e | underdog | Zechariah Sample | Receiving Yards | over | 0.040524746237519005 | 2026-11-05T12:22:13Z | 2026-11-08T03:30:00Z |
| underdog|34b16482-774a-4ce6-ac21-15407edb5036 | underdog | Braelon Allen | Receiving Yards | under | 0.04049280926701315 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|bcc3366d-03c4-4686-b8c4-9911098d7a7d | underdog | Jaylen Raynor | Rush Yards | over | 0.040483745848692076 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| prizepicks|16577047 | prizepicks | Ryan Flournoy | Rec Yards | under | 0.04046234355837319 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|19911946-1f92-42a4-aa1c-15e5815fb816 | underdog | Tee Higgins | Receptions | under | 0.04018031305357561 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|3bd01e57-9195-4088-a564-fe508f2d81f0 | underdog | Isaiah Likely | Receptions | under | 0.039903034181366426 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|7a5a7c7a-46d9-4665-9112-650361479cc3 | underdog | Dalen Penson | Receiving Yards | under | 0.039666610643468436 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|51793da7-f50f-4605-9f8b-5f37ddfbd171 | underdog | Jamari Johnson | Receptions | under | 0.039549403867083055 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|b510b6c8-aa64-436f-a890-a3ad7f41278d | underdog | Keelon Russell | Rush Yards | over | 0.03954798492547018 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| prizepicks|16577038 | prizepicks | Travis Kelce | Rec Yards | under | 0.039492224251563846 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|2cc87b1f-4074-49af-842b-adeac581d2e0 | underdog | Javon Tracy | Receiving Yards | under | 0.03941654428924801 | 2026-11-07T05:59:57Z | 2026-11-07T17:00:00Z |
| underdog|4d2d8848-1cc7-4afb-b184-d2ce33f20639 | underdog | Kaleb Webb | Receiving Yards | under | 0.03917272336846056 | 2026-11-05T22:06:44Z | 2026-11-07T17:30:00Z |
| underdog|cefb0596-2c7e-431b-8408-7a1ed12d8db4 | underdog | Bryce Young | Pass TDs | under | 0.039094010660283285 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| prizepicks|16764324 | prizepicks | Ty Johnson | Rec Targets | under | 0.03893224664571926 | 2026-11-07T05:59:57Z | 2026-11-09T20:15:00.000-05:00 |
| underdog|7ec6b8e6-f4bc-4ceb-9977-2343e6cf733c | underdog | Patrick Overmyer | Receiving Yards | under | 0.03891506317250926 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| prizepicks|16718511 | prizepicks | Jalen Coker | Rec Targets | under | 0.03878118544429088 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|ee84b567-7737-40cc-9b79-eb4387ebafef | underdog | Tre' Harris | Receiving Yards | under | 0.038717746022169375 | 2026-11-07T05:59:57Z | 2026-11-08T21:05:00Z |
| underdog|d1d3e66e-276b-43d4-9e06-fe5ed3964b6c | underdog | Geno Smith | Pass TDs | over | 0.038346590420210214 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|89797038-f669-4061-8bf0-a25c2c9b7871 | underdog | Godspower Nwawuihe | Rush Yards | under | 0.03811248713392412 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| prizepicks|16718513 | prizepicks | Tommy Tremble | Rec Targets | under | 0.038026067477504255 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|30207658-d186-4c70-8ce0-0f79ac92f94f | underdog | Trae'shawn Brown | Rush Yards | over | 0.037999199829431785 | 2026-11-04T12:10:41Z | 2026-11-07T20:30:00Z |
| underdog|24135e0b-bdb0-493a-8b08-4ef9d8baaddd | underdog | Omarion Hampton | Receiving Yards | over | 0.0379426659535288 | 2026-11-05T22:06:44Z | 2026-11-08T21:05:00Z |
| prizepicks|16719172 | prizepicks | Ollie Gordon II | Rec Targets | under | 0.03764949184168209 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|c9385892-f356-4349-8fb6-7d5113bc5518 | underdog | Kimani Vidal | Rush Yards | under | 0.037649407143210745 | 2026-11-05T22:06:44Z | 2026-11-08T21:05:00Z |
| underdog|fdb2283d-2b96-4d98-9749-7be1a9524421 | underdog | Eli Stowers | Receiving Yards | over | 0.03763479754869259 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|10c2407f-5738-4e43-8822-e60a7494336d | underdog | Devaughn Vele | Receiving Yards | under | 0.03754483168355782 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| prizepicks|16763490 | prizepicks | Josh Allen | Pass+Rush+Rec TDs | under | 0.037410921153935406 | 2026-11-07T05:59:57Z | 2026-11-09T20:15:00.000-05:00 |
| underdog|4a60e445-01a6-4494-af71-30be934f5ff2 | underdog | Jalen Royals | Receptions | over | 0.03740054606007237 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|b4d00e06-6a73-4ae1-aea2-db028bdcbe70 | underdog | Mike Matthews | Receiving Yards | under | 0.03727111221779744 | 2026-11-06T16:02:47Z | 2026-11-07T23:15:00Z |
| underdog|36c54cdf-d1a5-4421-add6-c8c475dc2cbb | underdog | Linda Noskova | Double Faults | under | 0.037236525846527924 | 2026-11-05T12:22:13Z | 2026-11-08T20:00:00Z |
| underdog|d654da8a-dcae-477e-b52e-6a2ec419e69b | underdog | Troy Franklin | Receiving Yards | over | 0.037228791049771504 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| prizepicks|16718503 | prizepicks | Keon Coleman | Rec Targets | under | 0.037191314735347314 | 2026-11-05T22:06:44Z | 2026-11-09T20:15:00.000-05:00 |
| underdog|a084c765-2f93-4d6d-8cce-dec31a4a1d25 | underdog | Derek Eusebio | Receptions | under | 0.03708316996324568 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| underdog|fae9f83c-94b0-42c3-b5e4-38e0ba845826 | underdog | Coco Gauff | Double Faults | under | 0.03701305154789125 | 2026-11-05T12:22:13Z | 2026-11-08T21:10:00Z |
| underdog|417cba44-2483-40b8-9dca-cb37554b2e7c | underdog | Alim McNeill | Sacks | over | 0.03694453187853869 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|2f401558-103b-44dd-b0ae-941e6998fc51 | underdog | Wayne Knight | Rush Yards | under | 0.03693588139563031 | 2026-11-04T12:10:41Z | 2026-11-07T17:00:00Z |
| underdog|06935d04-2d39-4365-a221-83b5141405cb | underdog | Caleb Odom | Receiving Yards | over | 0.036864288579971705 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| underdog|3e8e39eb-d463-45bc-a696-888d37fa2c28 | underdog | Tyler Robles | XP Made | over | 0.03669915689642389 | 2026-11-05T22:06:44Z | 2026-11-07T20:30:00Z |
| underdog|6c714eaf-7d73-41a2-a920-202ca837066f | underdog | Corey Kiner | Rush Yards | under | 0.036586404611637424 | 2026-11-06T06:34:07Z | 2026-11-08T21:25:00Z |
| underdog|4bd88e72-8a1e-4707-b805-02d3c1b83426 | underdog | Chrishon McCray | Receptions | over | 0.03644387034168628 | 2026-11-06T06:34:07Z | 2026-11-08T00:30:00Z |
| underdog|0a022c63-2671-4f23-9feb-269bf1714179 | underdog | Mario Craver | Receptions | over | 0.03644227791425586 | 2026-11-05T22:06:44Z | 2026-11-07T20:00:00Z |
| underdog|bafb2d39-561e-4802-a9d9-613f7bb7f677 | underdog | Keaton Mitchell | Rush + Rec Yards | under | 0.03631637632687834 | 2026-11-07T05:59:57Z | 2026-11-08T21:05:00Z |
| underdog|119f4d77-645c-42cd-9e5d-3c3aa99ea03d | underdog | Cameron Dicker | FG Made | under | 0.03597583144986216 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|27a63c39-071a-4c0d-9446-49a889e0cd4f | underdog | Derek Eusebio | Receiving Yards | under | 0.03590974499170774 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| underdog|865227cf-17df-4e89-9c98-4311b47f982a | underdog | Tetairoa McMillan | Receptions | under | 0.03583202783628714 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| prizepicks|16576405 | prizepicks | Puka Nacua | Rush Yards | over | 0.035802440511908284 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|63535c0e-f25f-4020-b229-60487df1cb5e | underdog | Kenny Darby | Receptions | over | 0.035572200850898905 | 2026-11-05T12:22:13Z | 2026-11-07T23:15:00Z |
| prizepicks|16701857 | prizepicks | Abu Sama III | Rush Atts | under | 0.035558095156955294 | 2026-11-07T05:59:57Z | 2026-11-07T16:15:00.000-05:00 |
| underdog|78ad258c-63f7-4bb8-a118-729b81ef3ae2 | underdog | Wayshawn Parker | Rush Yards | under | 0.03553177488727011 | 2026-11-07T05:59:57Z | 2026-11-07T17:00:00Z |
| underdog|2938dd7e-e105-48a9-b857-0c9a5cb45bdd | underdog | Willie Rodriguez | Receiving Yards | under | 0.03551812537664045 | 2026-11-06T16:02:47Z | 2026-11-07T23:15:00Z |
| underdog|f77c4659-c571-4380-bb17-0f290c20cfdb | underdog | Braden Pegan | Receiving Yards | under | 0.03535065146715288 | 2026-11-03T11:59:28Z | 2026-11-07T17:00:00Z |
| underdog|2f083c55-dfe0-4021-bc6a-5e7f16540cf5 | underdog | Ryan Fitzgerald | FG Made | under | 0.035264256773103186 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|8d80495b-f792-49a4-9e27-200df0bf6a4a | underdog | Alonza Barnett | Pass TDs | under | 0.03520294894563547 | 2026-11-05T22:06:44Z | 2026-11-07T20:45:00Z |
| underdog|ace9e75f-3fab-448d-a35d-0f1676382ace | underdog | Daniel Jones | Rush Yards | over | 0.03511058164603342 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|486c1a0d-e7ec-444f-bc88-040daaa5c7e7 | underdog | Fame Ijeboi | Receptions | over | 0.03505792792498785 | 2026-11-07T05:59:57Z | 2026-11-07T17:30:00Z |
| underdog|76b2a70a-293f-40f9-a916-eb743ce0a710 | underdog | Omari Hayes | Receiving Yards | over | 0.035032468841684095 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|d956ff35-5891-430d-a052-ebaf442bf737 | underdog | Spencer Shrader | Kicking Points | under | 0.03493687122664446 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|2a6fac37-d0cb-4800-b741-f75709238aac | underdog | DJ Black | Receiving Yards | over | 0.03489153401663336 | 2026-11-05T22:06:44Z | 2026-11-07T20:00:00Z |
| underdog|7553015d-56e4-47cb-9e15-d6a03e59966e | underdog | Samari Howard | Rush Yards | over | 0.0348766608443164 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| underdog|642b6aa4-d8ad-47ca-a6e2-02bf1db1abde | underdog | Rhamondre Stevenson | Receptions | under | 0.03473410197552751 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|b94e3cd0-3dff-4a4e-b5ec-e40578cb5f0a | underdog | Rashan Gary | Sacks | over | 0.03464923685125493 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|d4b75ea9-1465-40a5-8432-420f2c0b0e6e | underdog | Jaden Greathouse | Receiving Yards | under | 0.03456034476454173 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| underdog|1d8dbbfc-8b64-4087-bcb1-fc966080d598 | underdog | AJ Newberry | Receiving Yards | over | 0.03455291037392327 | 2026-11-06T16:02:47Z | 2026-11-08T03:30:00Z |
| prizepicks|16557908 | prizepicks | Patrick Mahomes | Rush Yards | under | 0.034534369510793694 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| prizepicks|16764327 | prizepicks | Pat Bryant | Rec Targets | under | 0.03453011724848243 | 2026-11-07T05:59:57Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|3bda549b-d1ec-4ec5-80e5-b29728603413 | underdog | Drew Wagner | Receiving Yards | over | 0.03452603403228793 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| underdog|66b37aff-aa69-48ba-984e-2a3c3e131cd4 | underdog | Tommy Tremble | Receptions | over | 0.03430222685481554 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|d07411a2-861f-46d8-9b37-7f958305aba8 | underdog | Miles Coleman | Receiving Yards | over | 0.03415913777769475 | 2026-11-05T12:22:13Z | 2026-11-07T18:00:00Z |
| underdog|8f38b7cd-66b8-4a9c-a51f-4a6edf46faaf | underdog | Mateen Bhaghani | FG Made | over | 0.03404654620887371 | 2026-11-06T16:02:47Z | 2026-11-07T17:00:00Z |
| underdog|a7cebf17-ff00-4409-a5bc-8ce129dd77a1 | underdog | Quinshon Judkins | Receptions | under | 0.03394034349269137 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|b4164f31-211e-44a6-819f-02c4a0dae617 | underdog | Xavier Worthy | Receptions | under | 0.033937644307545756 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|85a37a16-5893-4b92-ab30-289e06ffaa1a | underdog | Joe Burrow | Rush Yards | under | 0.03391319721842656 | 2026-11-07T05:59:57Z | 2026-11-08T14:30:00Z |
| underdog|1ac3ac51-8da4-4620-ad7b-98039d4a2113 | underdog | Isaac Brown | Rush Yards | under | 0.033702277504882194 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| underdog|49f0e5bd-dce7-4b34-a825-a52b5e213aca | underdog | Kyler Kasper | Receiving Yards | under | 0.0336523956518473 | 2026-11-07T05:59:57Z | 2026-11-07T17:00:00Z |
| underdog|d61c807a-66b1-4a4f-9972-cba41bc45ee6 | underdog | Javonte Williams | Receiving Yards | over | 0.03365125001838698 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|c326b335-e702-421f-9f11-eec8ab8fdfaa | underdog | Dalton Schultz | Receiving Yards | under | 0.03359570617331076 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|3811ee1b-f753-4213-82e8-b5b82a264172 | underdog | Michael Hawkins | Total TDs | under | 0.033378986607446426 | 2026-11-07T05:59:57Z | 2026-11-08T02:30:00Z |
| underdog|3b6b3ee7-c95c-4137-837a-d1f099813bd1 | underdog | Davian Jackson | Rush Yards | over | 0.033312274963038124 | 2026-11-07T05:59:57Z | 2026-11-08T03:30:00Z |
| underdog|982c2a85-82e0-4367-a651-1e019e8ef92e | underdog | Omarion Miller | Receptions | under | 0.0332576388461131 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| underdog|c4b7c726-6ba5-4b7b-a3f2-640e9d52771a | underdog | Samaje Perine | Rush + Rec Yards | under | 0.03322821780525986 | 2026-11-05T12:22:13Z | 2026-11-08T14:30:00Z |
| underdog|0233c0b9-e584-4501-a813-536ed9f80c2a | underdog | Michael Hawkins | Rush Yards | under | 0.03311372227579079 | 2026-11-06T16:02:47Z | 2026-11-08T02:30:00Z |
| underdog|fe1331bb-39d1-4681-8d5a-f9d951e31392 | underdog | KC Concepcion | Receptions | under | 0.033021846340560934 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|43d4f051-ed64-4b5e-904b-24f2c6efea26 | underdog | Samaje Perine | Rush Yards | under | 0.03301262915252379 | 2026-11-04T12:10:41Z | 2026-11-08T14:30:00Z |
| underdog|a2d14611-eeff-4586-80bd-d349331a9d9f | underdog | Blake Barnett | Pass TDs | under | 0.03293401410353347 | 2026-11-05T12:22:13Z | 2026-11-07T18:00:00Z |
| underdog|eed1a8db-19b4-4ad2-95b8-2280756b3e8c | underdog | JC French | Total TDs | under | 0.032900936841054995 | 2026-11-07T05:59:57Z | 2026-11-07T20:30:00Z |
| underdog|8ec38e88-0841-4587-886f-3ccdce8616e7 | underdog | John Mateer | Pass TDs | under | 0.032881661150447994 | 2026-11-06T16:02:47Z | 2026-11-08T00:45:00Z |
| underdog|8a29eea1-d895-407b-8658-b0db6edb5801 | underdog | Nate Adkins | Receptions | over | 0.03282306378556943 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|e6b1bd36-4a4b-44b3-8d57-b0ffc66e6084 | underdog | Jake Weinberg | FG Made | under | 0.032781270811728436 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|2fdcf276-eb1c-48b0-99cd-8ca8a12bd9f6 | underdog | Wyatt Young | Receiving Yards | under | 0.03277323062096282 | 2026-11-05T12:22:13Z | 2026-11-07T18:00:00Z |
| underdog|13caba41-6c85-4e45-92ad-9a617d35c20f | underdog | Dylan Sampson | Receiving Yards | under | 0.032711018039744744 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|b9c1a1a8-01ac-40a2-baab-d2706b32bde2 | underdog | Kyren Williams | Receptions | under | 0.032587481000593055 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| prizepicks|16758518 | prizepicks | Hugo Cuypers | Shots | over | 0.03255708984736638 | 2026-11-07T05:59:57Z | 2026-11-07T20:00:00.000-05:00 |
| underdog|cb747884-9dfd-4e72-bb6f-c8093300338d | underdog | Spencer Porath | XP Made | under | 0.03248900119255549 | 2026-11-06T06:34:07Z | 2026-11-08T00:30:00Z |
| prizepicks|16719169 | prizepicks | Chris Bell | Rec Targets | under | 0.032460366105138805 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|041b30d5-fdc3-4489-bb29-a89e6667b68d | underdog | Charlie Kolar | Receiving Yards | under | 0.03242651143957387 | 2026-11-05T12:22:13Z | 2026-11-08T21:05:00Z |
| underdog|0f008320-92cf-4f41-8668-21ea1cfb4f85 | underdog | Corey Kiner | Receptions | under | 0.03236272786970029 | 2026-11-06T16:02:47Z | 2026-11-08T21:25:00Z |
| underdog|efb57ef9-cd9e-4c17-8c69-4ca008e502a4 | underdog | Sione Vaki | Rush Yards | under | 0.03235069862327555 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|3b50b4b2-754e-4f73-a50b-e6b138ec4bd1 | underdog | Demond Williams | Rush Yards | under | 0.032240924877480426 | 2026-11-07T05:59:57Z | 2026-11-07T20:30:00Z |
| underdog|b396969a-1df9-4211-a0ab-b055cda96fd1 | underdog | Ashton Daniels | Pass TDs | over | 0.03222984779982624 | 2026-11-05T22:06:44Z | 2026-11-07T17:00:00Z |
| underdog|846cb4ab-3732-4ee4-9201-cc1a38b9bfaa | underdog | Simi Fehoko | Receiving Yards | over | 0.03211849704046699 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|2cfb2c38-eea2-4115-8859-b21897508d6e | underdog | Michael Mayer | Receptions | under | 0.03208971752720258 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|e458b44f-8472-4296-a09e-bc9842ae3727 | underdog | Austin Ekeler | Receptions | under | 0.03201422929910369 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|9766187b-a023-41ad-99d5-856a526ab1c8 | underdog | Ty Dieffenbach | Pass TDs | over | 0.031941299156751035 | 2026-11-06T16:02:47Z | 2026-11-07T17:00:00Z |
| underdog|d703eccc-f6a7-4718-81f1-d643a93e6e55 | underdog | Dawson Pough | Receiving Yards | over | 0.031808546432040785 | 2026-11-06T06:34:07Z | 2026-11-07T17:00:00Z |
| underdog|5b552096-e6eb-465b-84c2-9d4ee564e033 | underdog | Luke Dehnicke | Receiving Yards | over | 0.03179714828291913 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| underdog|07b4e0a9-97bd-4458-8a02-81a0f4ada5d4 | underdog | Xavier Hutchinson | Receiving Yards | over | 0.03157278603746505 | 2026-11-07T05:59:57Z | 2026-11-08T21:05:00Z |
| underdog|29834b95-ffb3-48a3-8130-df8f76762419 | underdog | Peyton Woodring | FG Made | over | 0.03151348868814757 | 2026-11-04T12:10:41Z | 2026-11-08T00:30:00Z |
| underdog|6e602c5e-7648-4c8a-b2e3-7f8166007740 | underdog | Micah Gilbert | Receiving Yards | over | 0.031476796159226605 | 2026-11-06T16:02:47Z | 2026-11-08T00:30:00Z |
| underdog|80942a8d-4513-4ce4-8e31-33f1be09d550 | underdog | Eric Olsen | Receiving Yards | under | 0.03141710972104428 | 2026-11-07T05:59:57Z | 2026-11-08T03:30:00Z |
| underdog|9d179035-df06-49bf-a90b-e1c8c7831fff | underdog | Omar Mabson | Rush Yards | under | 0.03137483548799547 | 2026-11-06T06:34:07Z | 2026-11-07T17:45:00Z |
| underdog|6e23e6cd-27f4-4bf6-b2ba-404b92954a5d | underdog | Nahzae Cox | Receiving Yards | over | 0.0312824438863063 | 2026-11-07T05:59:57Z | 2026-11-07T20:45:00Z |
| underdog|28e88963-6ce3-4dfb-ad09-da506039d8c8 | underdog | Cole Spence | Receptions | over | 0.030828022750417128 | 2026-11-05T22:06:44Z | 2026-11-07T21:15:00Z |
| underdog|ca6f9189-e313-4cd6-b37b-968777b35be5 | underdog | David Bailey | Sacks | over | 0.030807914842874817 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|ec21afa7-ad82-4b47-954d-22041573aade | underdog | Raleek Brown | Receptions | over | 0.030773355877860176 | 2026-11-05T12:22:13Z | 2026-11-07T17:00:00Z |
| underdog|f4d1d3da-bf52-4470-9fbb-c6e45ba2ea6c | underdog | Daniel Hill | Rush Yards | over | 0.030628445210237998 | 2026-11-07T05:59:57Z | 2026-11-07T20:30:00Z |
| underdog|83f920ca-4dab-484a-8ee0-245a7ae40d01 | underdog | Alexandra Eala | Double Faults | under | 0.030614609272419657 | 2026-11-07T05:59:57Z | 2026-11-07T08:00:00Z |
| underdog|9cc0a4d7-680c-4eec-9408-bd7d2f7270f8 | underdog | Andrew Marsh | Receptions | over | 0.03051906600607368 | 2026-11-05T22:06:44Z | 2026-11-08T00:30:00Z |
| underdog|f8241562-d12f-499e-85fe-2a980e36fd5a | underdog | Trinidad Chambliss | Rush Yards | over | 0.030197712764061135 | 2026-11-07T05:59:57Z | 2026-11-08T00:30:00Z |
| underdog|9bd8c698-9241-4468-a7b5-e37b14252e48 | underdog | Reece Vander Zee | Receptions | under | 0.030171557685573003 | 2026-11-05T12:22:13Z | 2026-11-08T00:30:00Z |
| underdog|f1715ec8-5f20-46c7-ba87-5af729c439a0 | underdog | Cam Cook | Rush Yards | under | 0.03009783990413606 | 2026-11-05T12:22:13Z | 2026-11-08T02:30:00Z |
| underdog|442726c3-e877-4bb4-9521-baf1f4122ee5 | underdog | Conner Weigman | Rush Yards | under | 0.030085288774177488 | 2026-11-07T05:59:57Z | 2026-11-07T20:30:00Z |
| underdog|b26ca2bb-149c-48e8-a968-913ca91b91fe | underdog | Jeremiah Trotter | Sacks | under | 0.030078365485903147 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
