# Pipeline Digest -- 2026-11-08T15:02:27Z

## Run summary
- Ingestion: 33261 rows (PrizePicks OK, Underdog OK)
- Estimation: 33261 rows estimated (from 33261 ingested props)
- CLV logging: 38 newly flagged, 0 newly closed, 681 still open (109655 total ever logged)

## Currently open flags
Sizing is a manual step (sizing_engine.py, Session 2.6) -- this table is what to scan to pick a pair worth sizing.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_edge | first_flagged_at | game_start_time |
|---|---|---|---|---|---|---|---|
| underdog|9eff3818-6fca-4bae-89ed-d1ef14a6fa24 | underdog | Shedeur Sanders | Pass Attempts | under | 0.42261306532663323 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| underdog|7984c1b8-4987-4395-9955-ab4b9006dd75 | underdog | Eddy Pineiro | FG Made | under | 0.41306807406928026 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|df8df649-116d-4f79-aac3-9d4b0ddca963 | underdog | Josh Allen | Pass Yards | under | 0.4 | 2026-11-08T06:01:51Z | 2026-11-10T01:15:00Z |
| underdog|8f31f84d-84e2-4a6a-8efd-4f3adfdd581b | underdog | Shedeur Sanders | Pass Yards | under | 0.4 | 2026-11-08T15:09:02Z | 2026-11-08T18:00:00Z |
| underdog|ba45158c-55cc-48e5-9aa2-cc1efeb6e624 | underdog | Drew Lock | Pass Attempts | under | 0.4 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|47ec053c-388c-4d74-a581-14d22b98c92a | underdog | Carson Wentz | Pass Attempts | under | 0.4 | 2026-11-05T22:06:44Z | 2026-11-10T01:15:00Z |
| underdog|57a8861e-d69d-4cfe-936e-0c47010e012e | underdog | Jadarian Price | Receiving Yards | under | 0.4 | 2026-11-05T22:06:44Z | 2026-11-08T21:25:00Z |
| underdog|3e831f69-cf67-408d-9148-2f2a2205f140 | underdog | Brandon McManus | Kicking Points | under | 0.4 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|15f36835-fa87-4b4b-a7c7-94aa0186ca19 | underdog | Justin Herbert | Pass Yards | under | 0.4 | 2026-11-08T06:01:51Z | 2026-11-08T21:05:00Z |
| underdog|6a510ed6-82d6-4f71-9908-b86541fe67cb | underdog | Shedeur Sanders | Rush Yards | under | 0.4 | 2026-11-08T06:01:51Z | 2026-11-08T18:00:00Z |
| underdog|a8354067-c8b4-49a3-87d1-f9f7ce0fbf31 | underdog | Elijah Mitchell | Rush + Rec Yards | under | 0.4 | 2026-11-08T15:09:02Z | 2026-11-08T18:00:00Z |
| underdog|f8f22600-df6e-4a85-ab30-0af2b9247426 | underdog | Stefon Diggs | Receiving Yards | under | 0.4 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|92973889-f958-46e1-9d56-1a45851bb88e | underdog | Dak Prescott | Pass Yards | under | 0.4 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|25f20e70-7454-41c9-808c-0518a23b77f3 | underdog | Emari Demercado | Rush Yards | under | 0.4 | 2026-11-07T05:59:57Z | 2026-11-08T21:05:00Z |
| underdog|2f23291e-eb46-4b0f-96d3-43d76315dc36 | underdog | Josh Jacobs | Rush Yards | under | 0.4 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|a958d6b8-a05d-4422-9e27-954de20b555e | underdog | Brock Purdy | Pass Yards | under | 0.4 | 2026-11-05T22:06:44Z | 2026-11-08T21:25:00Z |
| underdog|ce087efd-74be-4e03-b867-d767dd7439b1 | underdog | Caleb Williams | Pass Yards | under | 0.4 | 2026-11-07T05:59:57Z | 2026-11-09T01:20:00Z |
| underdog|268d2fc5-2abe-4849-b4a0-390d7485e453 | underdog | Caleb Williams | Pass Attempts | under | 0.4 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|6f655839-d390-4b43-8c4f-9e9362052e1a | underdog | Carson Wentz | Pass Yards | under | 0.4 | 2026-11-06T16:02:47Z | 2026-11-10T01:15:00Z |
| underdog|d71953b3-f84a-41de-8164-f5fbcaae145d | underdog | Malik Willis | Pass Yards | under | 0.4 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|77e18b43-44a4-42c0-8dac-0b7254af5899 | underdog | Drew Lock | Pass Yards | under | 0.4 | 2026-11-08T06:01:51Z | 2026-11-08T21:25:00Z |
| underdog|88a67ef6-decb-440a-98f8-fb4b22c34d26 | underdog | Brandon McManus | FG Made | under | 0.3956303597430939 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|a31d98a6-bf53-440e-a5b5-a2b50e20038d | underdog | Bo Nix | Pass Yards | under | 0.39297059903848375 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|d889190a-2c86-4441-a789-7f8d68386db5 | underdog | Skyler Bell | Receiving Yards | under | 0.39223309295827813 | 2026-11-07T05:59:57Z | 2026-11-10T01:15:00Z |
| underdog|3457fac4-96e9-46e5-a38e-f8575853e01c | underdog | Jayden Daniels | Pass Yards | under | 0.3893084725552035 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|53645bb3-c943-40ab-8bf6-8cac981c28ca | underdog | Baker Mayfield | Pass Yards | under | 0.3826968412880367 | 2026-11-07T05:59:57Z | 2026-11-09T01:20:00Z |
| underdog|01618ae6-c47b-4863-8ed5-5588a5af1039 | underdog | Devin Singletary | Rush Yards | under | 0.379407090167039 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|705e8042-bbe1-42e5-a50a-844d254c8900 | underdog | Kirk Cousins | Pass Yards | under | 0.3761461839014639 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|f9976ec1-4523-4b7a-bd0c-bca9b9dd4fb5 | underdog | Eddy Pineiro | Kicking Points | under | 0.3662333132187251 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|c115bc14-6cde-40db-84ab-498b3e7ca62f | underdog | Justin Herbert | Pass Attempts | under | 0.3654901563373757 | 2026-11-08T06:01:51Z | 2026-11-08T21:05:00Z |
| underdog|e3631ab4-a4e3-47d6-93c4-59cc4023bd88 | underdog | Daniel Jones | Pass Yards | under | 0.3637643979429024 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|5527bc92-0137-44d7-86c7-ca58439b3c0e | underdog | Devin Singletary | Rush + Rec Yards | under | 0.36215403846684935 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|b3567951-6e42-4050-9275-47e8aa47a159 | underdog | Demarcus Robinson | Receiving Yards | under | 0.353947768946699 | 2026-11-08T15:09:02Z | 2026-11-08T21:25:00Z |
| prizepicks|16557944 | prizepicks | Josh Allen | Pass Yards | under | 0.35094246505677495 | 2026-11-03T02:21:46Z | 2026-11-09T20:15:00.000-05:00 |
| prizepicks|16557940 | prizepicks | Brock Purdy | Pass Yards | under | 0.35094246505677495 | 2026-11-03T02:21:46Z | 2026-11-08T16:25:00.000-05:00 |
| prizepicks|16781987 | prizepicks | Brandon McManus | Fantasy Score | under | 0.35094246505677495 | 2026-11-08T06:01:51Z | 2026-11-08T13:00:00.000-05:00 |
| prizepicks|16557936 | prizepicks | Dak Prescott | Pass Yards | under | 0.35094246505677495 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| prizepicks|16722860 | prizepicks | Demarcus Robinson | Rec Targets | under | 0.35094246505677495 | 2026-11-06T06:34:07Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|76903731-5a31-4b71-aa02-3cf5f1f66632 | underdog | Jared Goff | Pass Yards | under | 0.34472431347503396 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|248aba17-77a9-49a7-96ad-e3085571e3b7 | underdog | Patrick Mahomes | Pass Yards | under | 0.34460651530387776 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|b4edad16-13cb-4bd3-8856-373011648386 | underdog | Brandin Cooks | Receiving Yards | under | 0.3413682969028984 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|99bc9f99-cca0-4271-ad36-c14fce24fce1 | underdog | Jordan Love | Pass Yards | under | 0.33893470681795934 | 2026-11-08T15:09:02Z | 2026-11-08T21:25:00Z |
| prizepicks|16557935 | prizepicks | Jayden Daniels | Pass Yards | under | 0.3359949609424918 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|37f53eaf-c7e4-4925-a45a-ca84b8d9ea68 | underdog | C.J. Stroud | Pass Yards | under | 0.33338439151254773 | 2026-11-05T22:06:44Z | 2026-11-08T21:05:00Z |
| underdog|91cd9a90-2bbb-4479-9d44-9025494f5dbb | underdog | Bo Nix | Pass Attempts | under | 0.33308348303432955 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|9e14cfdb-3be3-4ec4-a9b0-18a08e517978 | underdog | Skyler Bell | Receptions | under | 0.32591289918005106 | 2026-11-07T05:59:57Z | 2026-11-10T01:15:00Z |
| underdog|c3559a9a-0b12-4da5-bd9d-295bc350acb1 | underdog | Jadarian Price | Rush + Rec Yards | under | 0.3228916482644886 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|4fd3a242-cf5f-4eb3-a5db-95f253c0db3a | underdog | Josh Allen | Pass Attempts | under | 0.3201476032121736 | 2026-11-04T12:10:41Z | 2026-11-10T01:15:00Z |
| underdog|e6d5777b-8939-4202-8ed4-51f40d7be001 | underdog | Christian McCaffrey | Rush + Rec Yards | under | 0.3198836335711852 | 2026-11-05T22:06:44Z | 2026-11-08T21:25:00Z |
| underdog|efda5476-bc73-4e5c-8d29-c3b22c80a111 | underdog | Drake Maye | Pass Yards | under | 0.3169471849941047 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|c180ec24-04be-4d76-92bd-f2b1a7387ad4 | underdog | Josh Jacobs | Receptions | under | 0.3138562329893375 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| prizepicks|16718547 | prizepicks | Josh Jacobs | Rec Targets | under | 0.3126463971775677 | 2026-11-05T22:06:44Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|5c6fd482-eaa6-4f0b-9844-03c0ca175eb2 | underdog | Jonathon Cooper | Sacks | under | 0.31116751269035536 | 2026-11-08T06:01:51Z | 2026-11-08T18:00:00Z |
| underdog|c277dcc4-f254-4c7f-a17e-b758db8b9f68 | underdog | Antonio Williams | Receiving Yards | under | 0.3097464694839125 | 2026-11-08T15:09:02Z | 2026-11-08T18:00:00Z |
| prizepicks|16557939 | prizepicks | Kirk Cousins | Pass Yards | under | 0.3094515764679242 | 2026-11-03T02:21:46Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|81cc5510-e0d0-4426-ab7e-5e5c6a8c71c9 | underdog | Sione Vaki | Receiving Yards | over | 0.3091157904607309 | 2026-11-08T06:01:51Z | 2026-11-08T18:00:00Z |
| underdog|37896abf-b78c-4078-bf55-90cf3966fe31 | underdog | Puka Nacua | Receiving Yards | under | 0.30330510113385567 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|fc740f12-73f1-4f72-891a-31b0e366a807 | underdog | J.J. McCarthy | Pass Yards | under | 0.3015002874871391 | 2026-11-08T06:01:51Z | 2026-11-08T18:00:00Z |
| prizepicks|16763489 | prizepicks | Jayden Daniels | Pass+Rush+Rec TDs | under | 0.2995481890476045 | 2026-11-07T05:59:57Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|5f0cd76c-a7f5-445c-83c0-0f0a646cceec | underdog | Brock Bowers | Receiving Yards | under | 0.29946639988592183 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|b3820062-ff10-4245-afb1-048cb910cd60 | underdog | Brock Purdy | Pass Attempts | under | 0.29563370361590136 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|c1d7ae0f-d0c1-449e-be5b-2f61fd0f8ae7 | underdog | Shedeur Sanders | Pass TDs | under | 0.29393939393939406 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| underdog|a024c408-1fb1-43f6-b5cf-788ae51041e2 | underdog | Kyler Gordon | Sacks | over | 0.2919017834621568 | 2026-11-07T05:59:57Z | 2026-11-09T01:20:00Z |
| underdog|6fedbe9c-d9ae-4099-8f1a-24ecc472d1b9 | underdog | Nolan Smith | Sacks | over | 0.2905252383441529 | 2026-11-08T06:01:51Z | 2026-11-08T18:00:00Z |
| underdog|a4f7e2ea-445a-4746-9a01-bb8681efb55d | underdog | Drake Maye | Pass Attempts | under | 0.2890709907617405 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|b1871eee-1be7-4d3b-b76e-1f9f7f70baca | underdog | J.J. McCarthy | Pass TDs | under | 0.2875734861947701 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|0df9f965-8d0d-483f-852a-1830100071fe | underdog | Emeka Egbuka | Receiving Yards | under | 0.28187860828102784 | 2026-11-08T06:01:51Z | 2026-11-09T01:20:00Z |
| underdog|dd2f4f79-4283-42e8-afb4-2092a78921a4 | underdog | Geno Smith | Pass Yards | under | 0.2812427694504944 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|c65ae7a0-14dd-4948-bd2b-2216fbebe1d1 | underdog | Daniel Jones | Pass TDs | under | 0.27974205004038677 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|972c4c59-9985-4e4b-a01a-8ce4abbb0ac8 | underdog | Bryce Young | Pass Yards | under | 0.2790374647417364 | 2026-11-08T15:09:02Z | 2026-11-08T18:00:00Z |
| underdog|4cca7077-ba32-4aba-8ed4-90e312b20ac2 | underdog | Jadarian Price | Rush Yards | under | 0.2787804746448542 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|9f83e51f-0f48-4482-8998-0ba3dc634a2f | underdog | Bryce Young | Pass Attempts | under | 0.2768538252552345 | 2026-11-08T06:01:51Z | 2026-11-08T18:00:00Z |
| underdog|df8dac90-be57-4491-8f0d-566482090ae9 | underdog | Corey Kiner | Receiving Yards | over | 0.27647574749151815 | 2026-11-06T06:34:07Z | 2026-11-08T21:25:00Z |
| underdog|034db5e8-e2a4-4f3a-b113-160fa7977d4f | underdog | Jake Elliott | FG Made | under | 0.27609595620105687 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|9575a38e-86fe-4a9a-93ec-f8617ef793bd | underdog | Brandin Cooks | Receptions | under | 0.2755434284462872 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|93824785-dfec-403f-b1b6-5c9307c52772 | underdog | Antonio Williams | Receptions | under | 0.27536916730692296 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|bd628484-6e46-438d-aedc-ed875436387c | underdog | Demarcus Robinson | Receptions | under | 0.2692251142156261 | 2026-11-06T06:34:07Z | 2026-11-08T21:25:00Z |
| underdog|5a0ff8aa-ab28-4f6c-9ec5-e95c971f8458 | underdog | Andy Borregales | Kicking Points | under | 0.2640899467628497 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|35c1d584-b215-4b34-8d33-999226294c46 | underdog | Alvin Kamara | Rush Yards | under | 0.26372033067232636 | 2026-11-08T15:09:02Z | 2026-11-08T18:00:00Z |
| underdog|029429a0-88e2-4188-bb6a-963cd5a7c4e2 | underdog | Baker Mayfield | Pass TDs | under | 0.26332788339696256 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| prizepicks|16719183 | prizepicks | Saquon Barkley | Rec Targets | under | 0.26316628788845475 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|e66581ae-3fdf-48bb-b13e-4de3cf47a5fe | underdog | Saquon Barkley | Receptions | under | 0.26082333678953884 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|3adb5b8e-9fc9-4c71-8c0d-2be1644fe037 | underdog | Jayden Daniels | Pass Attempts | under | 0.25997924896274693 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|d484d774-fbd8-467b-bbfa-b6f85cfcf83f | underdog | Courtland Sutton | Receptions | under | 0.25834377385355134 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| prizepicks|16557933 | prizepicks | Patrick Mahomes | Pass Yards | under | 0.256531424485161 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|88b26255-d953-47cf-aa2d-032da6db6cbf | underdog | Caleb Williams | Pass TDs | under | 0.256421951810362 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|129a3cfd-80c7-4c48-a51b-24b6b5c538e9 | underdog | Matthew Stafford | Pass Yards | under | 0.25290413933089306 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|25d18fbf-8c15-4a17-895c-3635dd1ce944 | underdog | Malik Willis | Pass Attempts | under | 0.2526482871588408 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|b72f06e1-815c-4c36-b978-4fcc8dfeeef1 | underdog | Andy Borregales | FG Made | under | 0.25213168723502966 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|d15eec69-619f-4cff-973e-fcd9d5548e6b | underdog | Tyler Shough | Pass Yards | under | 0.25106506104349036 | 2026-11-08T15:09:02Z | 2026-11-08T18:00:00Z |
| underdog|9fb52355-1d13-4cb0-9975-0ed2d6885e99 | underdog | Jordan Love | Pass Attempts | under | 0.24800187930178297 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|fc0a7b7f-a597-4192-b95e-8c3194038f1b | underdog | George Kittle | Receiving Yards | under | 0.2450159013262515 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|e84e4aa4-7537-48ef-99a7-49d36a0d5fc7 | underdog | Geno Smith | Pass Attempts | under | 0.2432377584583152 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|76c6ce87-6460-400f-8181-465455daacfa | underdog | Zane Gonzalez | Kicking Points | under | 0.24239048934978857 | 2026-11-08T06:01:51Z | 2026-11-08T18:00:00Z |
| prizepicks|16557934 | prizepicks | Matthew Stafford | Pass Yards | under | 0.23485070755351956 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| prizepicks|16719160 | prizepicks | Brock Bowers | Rec Targets | under | 0.23351025534582692 | 2026-11-05T22:06:44Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|bba3c903-4ede-426b-98a4-5c60cb6bed88 | underdog | Jonah Coleman | Rush Yards | under | 0.233288763818978 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|a00ae86a-3ecc-4216-86f7-81d675f73f16 | underdog | Daniel Jones | Pass Attempts | under | 0.23121215443621368 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|4e54a271-1412-4d2d-98d4-0ba49bfa6122 | underdog | Josh Jacobs | Rush + Rec Yards | under | 0.22766679996482564 | 2026-11-05T22:06:44Z | 2026-11-08T21:25:00Z |
| underdog|60cbaa38-c568-4879-a6f8-94b6e4e69559 | underdog | Tucker Kraft | Receiving Yards | under | 0.22559324997910668 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|713b2721-78da-4cec-8f94-3e8a3e141d5d | underdog | Mike Washington | Receiving Yards | over | 0.22513540135851895 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|bec6e496-16bb-4fa1-ab70-03d725748d98 | underdog | Austin Booker | Sacks | over | 0.22495368063922305 | 2026-11-07T05:59:57Z | 2026-11-09T01:20:00Z |
| underdog|b7a27035-0410-4524-9b9f-8504019e9e93 | underdog | Malik Washington | Receiving Yards | under | 0.22383503418957196 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|4610e541-5d71-4664-b765-2e6313fa472a | underdog | Nick Bosa | Sacks | under | 0.22272727272727277 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|6d8eb0bb-0195-4e81-b62a-94edbb4b8341 | underdog | George Kittle | Receptions | under | 0.2205590308515778 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|a9694f7d-6e59-4ba1-a1ef-0ee910195888 | underdog | J.J. McCarthy | Pass Attempts | under | 0.22026861920931884 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|cae9a0a8-d1f3-4eb2-87c8-2c8e433a8a8d | underdog | Colston Loveland | Receiving Yards | under | 0.2198455782755615 | 2026-11-06T16:02:47Z | 2026-11-09T01:20:00Z |
| underdog|6bbf2a5a-63d8-4774-b146-9892eacd1ce1 | underdog | Kirk Cousins | Pass Attempts | under | 0.21906706972458956 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|5ce7b43f-6c56-458c-8e7b-dc6749b86b93 | underdog | Zach Sieler | Sacks | over | 0.21881747292660894 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|3d11ff54-e68e-46fd-9bee-9f64e201a532 | underdog | Ladd McConkey | Receptions | under | 0.2182531395719538 | 2026-11-03T02:21:46Z | 2026-11-08T21:05:00Z |
| underdog|bfe8c590-b7cd-46fa-97ef-a6f89b54cba6 | underdog | Christian McCaffrey | Rush Yards | under | 0.21748885231877868 | 2026-11-05T22:06:44Z | 2026-11-08T21:25:00Z |
| underdog|5e5ead91-81b9-4b8e-a5ef-e2aa3b7a5ed0 | underdog | Woody Marks | Rush Yards | under | 0.21579731650075495 | 2026-11-05T12:22:13Z | 2026-11-08T21:05:00Z |
| underdog|49e20d5a-2cc0-46f5-a3cd-2901fcc1ca46 | underdog | Will McDonald IV | Sacks | over | 0.21361991879405742 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|d88c56d2-1395-401b-bd3e-3d1d31728d14 | underdog | Woody Marks | Rush + Rec Yards | under | 0.2133596409286077 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|ce0c66a5-e095-4a55-a3a2-dce5222c3917 | underdog | D'Andre Swift | Rush + Rec Yards | under | 0.2097482313264234 | 2026-11-07T05:59:57Z | 2026-11-09T01:20:00Z |
| prizepicks|16577049 | prizepicks | Trey McBride | Rec Yards | under | 0.20935259101009185 | 2026-11-03T02:21:46Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|54ab195f-b38f-43ea-9168-30743fdbabca | underdog | Quinshon Judkins | Rush + Rec Yards | under | 0.2082800596334483 | 2026-11-08T15:09:02Z | 2026-11-08T18:00:00Z |
| underdog|1a84ed45-d8ba-4f03-8227-091e6daa83e6 | underdog | K'Lavon Chaisson | Sacks | over | 0.2081946476515919 | 2026-11-08T06:01:51Z | 2026-11-08T18:00:00Z |
| underdog|23a46bfb-a057-45dc-a412-fb89efb5a4c5 | underdog | Chris Godwin | Receiving Yards | under | 0.20786795867893026 | 2026-11-07T05:59:57Z | 2026-11-09T01:20:00Z |
| underdog|96d514bd-16df-438e-a060-00f5c8573329 | underdog | Patrick Mahomes | Pass Attempts | under | 0.20613805218871373 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|cd3d1726-9c42-4e75-8563-3073cf914224 | underdog | Derrick Barnes | Sacks | over | 0.2049580222093775 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|1f7dd0bf-f127-468a-b32d-11be5fc22ca6 | underdog | Quinshon Judkins | Rush Yards | under | 0.20487468569814804 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| underdog|2baac9c0-74d9-4404-8f02-428133e9ba49 | underdog | Jowon Briggs | Sacks | over | 0.20370912125948692 | 2026-11-08T06:01:51Z | 2026-11-08T18:00:00Z |
| underdog|17d58030-f59c-4e6a-b95e-5e22592343f4 | underdog | Nico Collins | Receiving Yards | under | 0.20265644684978057 | 2026-11-05T22:06:44Z | 2026-11-08T21:05:00Z |
| underdog|b99d6014-b4c3-451f-bc57-c1109aa968ed | underdog | Christian McCaffrey | Receiving Yards | under | 0.20231096643705238 | 2026-11-05T22:06:44Z | 2026-11-08T21:25:00Z |
| underdog|c61022bc-362a-4e1c-8d69-48a576ea6c00 | underdog | Justin Herbert | Pass TDs | under | 0.20191287593682095 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|e8ee0b8d-e450-43e3-8f03-13ce4aaca7ad | underdog | Nick Emmanwori | Sacks | over | 0.19892946238095685 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|ba7f8f62-5f54-4656-b88d-1d130e0f5f4e | underdog | Jared Goff | Pass TDs | under | 0.19843367199986595 | 2026-11-08T06:01:51Z | 2026-11-08T18:00:00Z |
| prizepicks|16577051 | prizepicks | Brock Bowers | Rec Yards | under | 0.19828126826604298 | 2026-11-03T02:21:46Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|d9931ebc-f2b4-4965-a907-7e5426461db5 | underdog | Trey McBride | Receptions | under | 0.19807043328611007 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|fd73053c-c0f9-4bea-b66c-20ede4728695 | underdog | Rashee Rice | Receiving Yards | under | 0.1966277935664762 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|9a2902e7-4ecf-4ea5-a36e-c5c8f6e59bb7 | underdog | Harrison Butker | FG Made | under | 0.19473086921391436 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|410efb5a-6f14-4f58-846b-fb76cf98cec4 | underdog | Matthew Stafford | Rush Yards | over | 0.1944521898255368 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|fd6fe187-a62e-4b28-98d1-7629a2c05b20 | underdog | Alex Singleton | Sacks | over | 0.1921046498261034 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|6d173119-25d4-4548-83ad-03156b0cf2dd | underdog | Ben Yurosek | Receptions | over | 0.19167896654283034 | 2026-11-07T05:59:57Z | 2026-11-10T01:15:00Z |
| prizepicks|16718554 | prizepicks | Nico Collins | Rec Targets | under | 0.1883756713204645 | 2026-11-05T22:06:44Z | 2026-11-08T16:05:00.000-05:00 |
| underdog|bb3e6e35-adc8-404a-8667-3340d6c7628a | underdog | Rashee Rice | Receptions | under | 0.18655451075752905 | 2026-11-08T06:01:51Z | 2026-11-08T18:00:00Z |
| underdog|23e55a57-7467-474d-be5d-65040e14440a | underdog | Josh Downs | Receiving Yards | under | 0.18588799861791883 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|f578cc15-698b-4a56-b103-e35ad36d927d | underdog | Makai Lemon | Receiving Yards | under | 0.1856316687037486 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| prizepicks|16718534 | prizepicks | Courtland Sutton | Rec Targets | under | 0.18479411301214343 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|6af5960a-1d9d-4f3c-ab5d-c2bcd805cfc7 | underdog | Baker Mayfield | Pass Attempts | under | 0.1838540296279383 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|b62bb0ab-c033-4670-bdbe-45edf695da31 | underdog | Isaiah McGuire | Sacks | over | 0.18318931337316957 | 2026-11-08T06:01:51Z | 2026-11-08T18:00:00Z |
| underdog|f4c69603-6218-4437-8fdd-275d6fcfe8ef | underdog | Jason Myers | FG Made | under | 0.1827109251134501 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|211341a3-9825-4471-afb3-2983cc461c69 | underdog | Pete Werner | Sacks | over | 0.18270979216902497 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| prizepicks|16685557 | prizepicks | Justin Herbert | Pass TDs | under | 0.18176877497841348 | 2026-11-05T12:22:13Z | 2026-11-08T16:05:00.000-05:00 |
| underdog|ac801e69-7d78-4483-b68c-0b71e1f6b8cb | underdog | Devonte Wyatt | Sacks | over | 0.18075903008997662 | 2026-11-08T06:01:51Z | 2026-11-08T21:25:00Z |
| underdog|cfae8805-6e9b-4151-aae5-009efb71986a | underdog | Brock Bowers | Receptions | under | 0.17887742031236042 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|e65f0b6c-3aa6-42eb-9f7f-b36fd4ccc1fd | underdog | Ryan Flournoy | Receiving Yards | under | 0.17877700640809546 | 2026-11-08T06:01:51Z | 2026-11-08T18:00:00Z |
| underdog|88a405b6-380d-4d54-a1c8-91d3bf9ce680 | underdog | Alvin Kamara | Rush + Rec Yards | under | 0.17851297395908294 | 2026-11-08T15:09:02Z | 2026-11-08T18:00:00Z |
| prizepicks|16764334 | prizepicks | Jalen Nailor | Rec Targets | under | 0.17792466796619333 | 2026-11-07T05:59:57Z | 2026-11-08T16:25:00.000-05:00 |
| prizepicks|16764339 | prizepicks | Hunter Henry | Rec Targets | under | 0.17791529772379444 | 2026-11-07T05:59:57Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|a1310588-918d-4510-86a7-bd4a239fec69 | underdog | C.J. Stroud | Pass Attempts | under | 0.17725867468837075 | 2026-11-03T02:21:46Z | 2026-11-08T21:05:00Z |
| underdog|83fdf531-1a1c-459d-b9c6-34b164621fc6 | underdog | Chop Robinson | Sacks | over | 0.17694658079074554 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|9100eaf4-8232-4056-8f1f-336a475cc678 | underdog | Rhamondre Stevenson | Rush Yards | under | 0.17609187646102753 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|3a64bb74-f554-4133-8100-a705c07fec61 | underdog | Jonah Coleman | Rush + Rec Yards | under | 0.17519915897290428 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| underdog|a2ee3b2c-3a41-4508-ad81-1d0ca5c6f707 | underdog | Jared Goff | Pass Attempts | under | 0.17494980056194276 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|03cedfad-8324-45d0-912c-866b25e8ac91 | underdog | Rachaad White | Rush Yards | under | 0.1747980079171697 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|37e75b3c-df4a-4076-81fa-4c6bb2d3c8dc | underdog | Tyler Warren | Receiving Yards | under | 0.1742754565895258 | 2026-11-08T06:01:51Z | 2026-11-08T18:00:00Z |
| underdog|49ed43ea-4e5d-463c-925e-076cdf258f6c | underdog | Seth McGowan | Receiving Yards | over | 0.17369446851452397 | 2026-11-08T06:01:51Z | 2026-11-08T18:00:00Z |
| underdog|08cf2061-fd87-4572-ad89-293508054cf6 | underdog | Mason Graham | Sacks | over | 0.17262353350724963 | 2026-11-06T16:02:47Z | 2026-11-08T18:00:00Z |
| underdog|22d007c4-5d23-4435-9e6a-d9aea95af1d2 | underdog | Romello Height | Sacks | over | 0.1721000021783672 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|fdc20714-2850-4478-a9ae-058d3a14ba1b | underdog | Jake Elliott | Kicking Points | under | 0.1717042647640432 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| prizepicks|16719194 | prizepicks | Stefon Diggs | Rec Targets | under | 0.17139963879683195 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|afe1bdf8-c20d-4613-ad24-60cc80891977 | underdog | Luther Burden | Receiving Yards | under | 0.1708136555455848 | 2026-11-05T22:06:44Z | 2026-11-09T01:20:00Z |
| prizepicks|16701919 | prizepicks | George Kittle | Recs | under | 0.17046516255208966 | 2026-11-07T05:59:57Z | 2026-11-08T16:25:00.000-05:00 |
| prizepicks|16647367 | prizepicks | Kirk Cousins | Pass Attempts | under | 0.16995161634207256 | 2026-11-08T06:01:51Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|8d152fc4-c66d-4c70-a95d-b1d825710984 | underdog | Ben Yurosek | Receiving Yards | over | 0.16984442336545214 | 2026-11-08T06:01:51Z | 2026-11-10T01:15:00Z |
| underdog|55a9824f-bf0e-4ead-b0d2-a87e066918e7 | underdog | Courtland Sutton | Receiving Yards | under | 0.16948914184321828 | 2026-11-08T15:09:02Z | 2026-11-08T18:00:00Z |
| underdog|443482c4-7dec-4fc0-ac02-58ebb74cafe5 | underdog | Kenny Clark | Sacks | over | 0.16901184891391496 | 2026-11-08T06:01:51Z | 2026-11-08T18:00:00Z |
| underdog|136a1623-2e16-4023-ae01-56630f63f198 | underdog | Ladd McConkey | Receiving Yards | under | 0.1689736300607736 | 2026-11-08T06:01:51Z | 2026-11-08T21:05:00Z |
| underdog|d5030e40-3006-4824-ba3f-2e99ee58ec46 | underdog | Saquon Barkley | Rush + Rec Yards | under | 0.16859915804427605 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|a2c32829-5741-4600-bdac-f990a7052b23 | underdog | Rhamondre Stevenson | Rush + Rec Yards | under | 0.1684921629314633 | 2026-11-03T11:59:28Z | 2026-11-08T21:25:00Z |
| underdog|1e0723e6-39f5-401c-9ecb-73146c38ec61 | underdog | Marvin Harrison | Receptions | under | 0.16835016265867342 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|407ff730-9a50-4ee0-a6e5-2e91574ef6f1 | underdog | Rachaad White | Rush + Rec Yards | under | 0.16822537025107998 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|a8a9bed2-5d3a-4afa-b7f7-de3a2c658f75 | underdog | Jared Goff | Rush Yards | over | 0.1677182366005825 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|ce5575f0-bb41-462f-a7c5-1ad9b1c12b56 | underdog | Eric Wilson | Sacks | over | 0.16745324148343438 | 2026-11-07T05:59:57Z | 2026-11-10T01:15:00Z |
| underdog|3a4be27f-f52f-4a62-8c7f-9b533bb4088d | underdog | Austin Ekeler | Rush + Rec Yards | under | 0.16745195094192344 | 2026-11-08T06:01:51Z | 2026-11-08T18:00:00Z |
| underdog|cf74ea13-4c83-486b-a699-efa71530a041 | underdog | Amon-Ra St. Brown | Receptions | under | 0.16742438992001507 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|21a1acab-2608-4d98-a630-1f326444c663 | underdog | Jalen Royals | Receiving Yards | over | 0.16685710651601937 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|3c2c0991-0e80-4489-9557-56d68aa8268c | underdog | Wil Lutz | FG Made | under | 0.1665329706004408 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|c7fbbf68-83ff-44a2-a032-87a9503edea0 | underdog | Cairo Santos | FG Made | under | 0.16650636156632292 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|f3750bd4-2998-4958-948b-378b41f868ef | underdog | Cade Otton | Receiving Yards | under | 0.16512553256579154 | 2026-11-07T05:59:57Z | 2026-11-09T01:20:00Z |
| underdog|14727280-75e6-47c5-aa99-a15c0090d9d3 | underdog | Jadeveon Clowney | Sacks | over | 0.16506617094106288 | 2026-11-06T16:02:47Z | 2026-11-08T21:05:00Z |
| underdog|6b0a254c-fbec-481c-b649-05d1a353bcae | underdog | Harrison Butker | Kicking Points | under | 0.16442129921836235 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|18b57f5b-5104-4c5c-9e62-65e5b6963fff | underdog | Jalen Nailor | Receiving Yards | under | 0.1640019884226247 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|fdac6a05-fb95-4a60-a4df-dcf01949a793 | underdog | Montez Sweat | Sacks | over | 0.16370398320793605 | 2026-11-08T06:01:51Z | 2026-11-09T01:20:00Z |
| underdog|c532ae7d-f4dc-49b5-aeda-dbb9e803078d | underdog | Jaxon Smith-Njigba | Receiving Yards | under | 0.16249913286034545 | 2026-11-08T06:01:51Z | 2026-11-08T21:25:00Z |
| underdog|89a5bb97-1393-4679-8d6e-45b1bd8a62ea | underdog | Jordan Mason | Rush + Rec Yards | under | 0.1624124156770972 | 2026-11-05T12:22:13Z | 2026-11-10T01:15:00Z |
| underdog|26b34dbd-c8b5-4155-8b09-75b12c1ecd7a | underdog | Stefon Diggs | Receptions | under | 0.1623657419982183 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|e118f74f-7897-4d80-b846-aa5f907a649b | underdog | Bryce Young | Rush Yards | under | 0.16231242116840527 | 2026-11-08T06:01:51Z | 2026-11-08T18:00:00Z |
| underdog|6986991c-1be4-4314-926e-cebf3701f52d | underdog | Arvell Reese | Sacks | over | 0.16160822893044927 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|9ff29ccb-f4c3-4664-9330-39133772a9f1 | underdog | Tucker Kraft | Receptions | under | 0.1615364063191952 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|528a645e-8439-47f6-91f3-89566cf92574 | underdog | Greg Dulcich | Receptions | under | 0.15981895291377868 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|ccb7af37-6f52-4013-99b6-0b977f2535d6 | underdog | Kingsley Enagbare | Sacks | over | 0.15973360653003466 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|8f289276-834c-4a60-ac19-2b8e634918e6 | underdog | Ollie Gordon | Rush + Rec Yards | under | 0.15941145377301513 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|7d8aca5c-098a-4cd2-ac18-2986be8ea813 | underdog | Matthew Golden | Receptions | under | 0.15935064858874126 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|f91be1d5-74dc-4555-9736-6b8edde55ba9 | underdog | Cooper Kupp | Receptions | under | 0.15901675324842612 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| prizepicks|16718548 | prizepicks | Tucker Kraft | Rec Targets | under | 0.1589344482639552 | 2026-11-05T22:06:44Z | 2026-11-08T16:25:00.000-05:00 |
| prizepicks|16718557 | prizepicks | Tyler Warren | Rec Targets | under | 0.15855243884293413 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|26363e50-ce4d-4af5-96f1-fc389dcca744 | underdog | Blake Cashman | Sacks | over | 0.15839987964028668 | 2026-11-07T05:59:57Z | 2026-11-10T01:15:00Z |
| underdog|698f97b3-863e-4773-97b1-02795f52198b | underdog | Dak Prescott | Pass Attempts | under | 0.15742541666457277 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|549e9cef-a3a5-4d2d-80da-e1502e502bd7 | underdog | Tyler Goodson | Rush + Rec Yards | under | 0.15738112185450548 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|e41a0da4-0291-4499-9b1b-ed6fe79cddc8 | underdog | Ollie Gordon | Receiving Yards | under | 0.15660530020212726 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|37b70014-c646-417c-9dda-4626c7ea528a | underdog | Tyler Shough | Pass Attempts | under | 0.15655653928608748 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|0b592d73-46b4-4456-918c-8d00242be932 | underdog | Dawson Knox | Receptions | under | 0.15649493040707285 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| prizepicks|16763487 | prizepicks | Malik Willis | Pass+Rush+Rec TDs | under | 0.1558092367821141 | 2026-11-07T05:59:57Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|dc298725-6b1d-47d4-8dac-3617ff5e42ae | underdog | Jordan Mason | Rush Yards | under | 0.15576327193870432 | 2026-11-06T16:02:47Z | 2026-11-10T01:15:00Z |
| underdog|8898d1df-cad0-48ed-9aab-c49b53a783d1 | underdog | Adetomiwa Adebawore | Sacks | over | 0.15560774164609692 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|02524fc1-2c2c-4351-9030-2facb6210680 | underdog | Sam LaPorta | Receiving Yards | under | 0.15480965770515087 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|2ec42f15-1310-4109-bdeb-ac91c573b24e | underdog | Kaelon Black | Rush + Rec Yards | under | 0.15399282245244306 | 2026-11-08T06:01:51Z | 2026-11-08T21:25:00Z |
| prizepicks|16747853 | prizepicks | Omar Cooper Jr. | Rec Targets | under | 0.15377247066602107 | 2026-11-07T05:59:57Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|532d33d0-64eb-4500-bfe5-8f549e052fa2 | underdog | Tory Horton | Receptions | under | 0.15338264840885663 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|f31632ab-697b-47b3-a647-5a82eb0defa9 | underdog | James Houston | Sacks | over | 0.15251939631897432 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| prizepicks|16718455 | prizepicks | Trey McBride | Rec Targets | under | 0.1522364381770983 | 2026-11-05T22:06:44Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|04c2b5c2-1fd7-497c-9390-1f0f58b1d195 | underdog | DeForest Buckner | Sacks | over | 0.15102958799908306 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| prizepicks|16718538 | prizepicks | Jonah Coleman | Rec Targets | under | 0.15073744374037423 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|7adbcb60-fb8e-4713-afc1-f7cf4af22909 | underdog | Zane Gonzalez | FG Made | under | 0.15052117503385665 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|5eea8199-5dbe-4649-a20a-2405bd63d177 | underdog | Jaxon Smith-Njigba | Receptions | under | 0.15026450962994486 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|42d092cc-c62c-45cf-88dd-cebcde7f86d3 | underdog | Darius Cooper | Receptions | under | 0.15015667703429225 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|d0e344fe-0a79-4dad-a9fd-6d477eff98c4 | underdog | Keion White | Sacks | over | 0.1496843494227773 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|7f44b052-27a1-42a5-8108-ca43bdfcb5bb | underdog | Chuba Hubbard | Rush + Rec Yards | under | 0.14959006456056478 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|e0c22419-0dff-4556-a05e-9acfa3ab7a09 | underdog | Brandon Aubrey | FG Made | under | 0.14958269462275497 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|b0ce99d7-ccca-47c0-a454-e6f920eab8e2 | underdog | Bo Nix | Pass TDs | under | 0.14921921703126695 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|c4587fdc-fe2d-47dc-997d-d0b08663b00a | underdog | Ka'imi Fairbairn | FG Made | under | 0.1479318682678138 | 2026-11-03T02:21:46Z | 2026-11-08T21:05:00Z |
| underdog|1b370830-3867-4ade-9a8d-418a06dbd1c1 | underdog | Christian Watson | Receptions | under | 0.1479168165648339 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|2484637b-dd6a-4882-be40-ce0e68d4e559 | underdog | Kenny Gainwell | Receptions | under | 0.1475602481670133 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|13d49fc8-9559-45e1-9bac-6f15a20a2c72 | underdog | Ollie Gordon | Receptions | under | 0.14682805397570908 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| prizepicks|16718558 | prizepicks | Rashee Rice | Rec Targets | under | 0.14673204243829352 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|ad5841e3-f51c-4e2d-a883-064eb9b2257f | underdog | Malik Washington | Receptions | under | 0.14645959659878283 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|f57c0032-b5b1-4228-af7c-d6bb6f08e67e | underdog | Emeka Egbuka | Receptions | under | 0.1460648049345178 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|a5687c54-7273-4922-8cf8-a0383ebb4afa | underdog | Trey McBride | Receiving Yards | under | 0.14497443435005852 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|9e881772-2cab-49d1-98b4-4a20360513e2 | underdog | Osa Odighizuwa | Sacks | over | 0.14450890275099865 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|d9c83072-0b9d-4dd6-ac46-9ee7193a65c2 | underdog | Jake Bates | Kicking Points | under | 0.14384173611237716 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|941b56c8-ad29-471c-986f-fba334187fce | underdog | Marvin Harrison | Receiving Yards | under | 0.143598479908011 | 2026-11-07T05:59:57Z | 2026-11-08T21:05:00Z |
| underdog|a761c371-7b4a-476a-8c8f-cc6724d3bbe9 | underdog | Elijah Mitchell | Rush Yards | under | 0.14326354478391035 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|4bcbca35-fe46-4882-9576-1077ee02e5e9 | underdog | Odafe Oweh | Sacks | over | 0.14292355211879115 | 2026-11-08T06:01:51Z | 2026-11-08T18:00:00Z |
| underdog|1acc37b7-16ae-4dfe-9876-857c87ea3b17 | underdog | Quentin Johnston | Receiving Yards | under | 0.1413979010411639 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|a139a0db-5e8b-4ce6-ab23-a7e4208c2793 | underdog | Greg Dulcich | Receiving Yards | under | 0.14092453833106433 | 2026-11-08T06:01:51Z | 2026-11-08T18:00:00Z |
| underdog|8b40fd14-adb3-47ff-866a-2f2dbd8bb371 | underdog | Tutu Atwell | Receptions | under | 0.13968039382130393 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|d750f1b4-ebcd-49c0-9b03-97137f1f422f | underdog | Carson Wentz | Rush Yards | under | 0.1396304799819178 | 2026-11-05T22:06:44Z | 2026-11-10T01:15:00Z |
| underdog|d14f7c92-88e3-467c-9ffe-8d4636169797 | underdog | Jahmyr Gibbs | Rush + Rec Yards | under | 0.13942056193480923 | 2026-11-08T15:09:02Z | 2026-11-08T18:00:00Z |
| underdog|03e0d95d-f3f0-4f64-bea2-e9e8bbb684e3 | underdog | AJ Barner | Receptions | under | 0.13910664132787998 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|f31a1e8b-9aa9-4022-b468-859f852768cb | underdog | Devaughn Vele | Receptions | under | 0.13901253046609652 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|8b11a49e-1f76-4d12-9052-b165b603495e | underdog | Makai Lemon | Receptions | under | 0.13853947895546503 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|3c114bc2-839b-4e55-9ec0-5de96e8522a9 | underdog | Caleb Douglas | Receptions | under | 0.1384724673367177 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|5df51a97-b605-4c0d-b9a5-6038554d83e4 | underdog | Amon-Ra St. Brown | Receiving Yards | under | 0.13837637499846278 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|ab666f53-3f97-4d16-9e8b-997aaaba0cfc | underdog | Kaelon Black | Rush Yards | under | 0.1371496838847872 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|62752957-b2d2-43f1-8caa-62560a2db86a | underdog | Brock Purdy | Pass TDs | under | 0.13705484641190113 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|f02afff8-8b37-426d-aa01-6612112f4ed8 | underdog | Quinshon Judkins | Receiving Yards | over | 0.13687863592857885 | 2026-11-08T15:09:02Z | 2026-11-08T18:00:00Z |
| underdog|e9e775c1-e65e-481a-8e80-4451df551d94 | underdog | James Cook | Receptions | under | 0.13675024566789118 | 2026-11-05T22:06:44Z | 2026-11-10T01:15:00Z |
| underdog|e51659c8-5120-4ea6-8cda-0855726b1435 | underdog | Matthew Stafford | Pass Attempts | under | 0.13674658781617022 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| underdog|af5adabc-bebb-4583-a724-ec24ce745588 | underdog | Cooper Kupp | Receiving Yards | under | 0.13648768280929058 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|a0563313-b8f6-4974-a05b-d5e6a15f4169 | underdog | Barryn Sorrell | Sacks | over | 0.13529244398588483 | 2026-11-06T16:02:47Z | 2026-11-08T21:25:00Z |
| underdog|0a1d4a28-f4ed-433b-a45b-953e95969acb | underdog | Jadarian Price | Receptions | under | 0.13399424688283068 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|5790a889-8601-4824-ac78-b9c766ba1891 | underdog | Marvin Mims Jr. | Receptions | under | 0.13357422686133513 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|5ebe042f-0411-409e-958b-f2fce6dcbd98 | underdog | Devin Singletary | Receiving Yards | under | 0.1330346125830013 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|e3eafc58-286e-42f2-b4ee-056ef1f4f612 | underdog | Chig Okonkwo | Receiving Yards | under | 0.13137551735878683 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|b844923b-243b-45bc-9061-7b5db0d00768 | underdog | Jalen Carter | Sacks | over | 0.13121128593265297 | 2026-11-08T15:09:02Z | 2026-11-08T18:00:00Z |
| underdog|6a4ea7ca-8051-400b-a435-f94e0a7067ee | underdog | Jameson Williams | Receiving Yards | under | 0.131077359753479 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|b0c497f1-a404-41ae-9572-74da843984b3 | underdog | MarShawn Lloyd | Receiving Yards | over | 0.13020219018489343 | 2026-11-06T16:02:47Z | 2026-11-08T21:25:00Z |
| underdog|896c369b-dfe7-4cdf-816a-54fd6d2a64c6 | underdog | Darius Cooper | Receiving Yards | under | 0.12982985729704266 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|14d37ea9-87e7-4e15-ad26-f93259d0facd | underdog | Drew Lock | Pass TDs | under | 0.12966967278207253 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| prizepicks|16718556 | prizepicks | Jonathan Taylor | Rec Targets | under | 0.12923033670188888 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|40e5a0ef-776f-47dc-991d-3b3c24cfdabb | underdog | Efton Chism | Receptions | under | 0.12920163225844472 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|ccfe2bba-71d1-4e46-bf46-d00e2a8c975c | underdog | Javonte Williams | Rush + Rec Yards | under | 0.12875496760840743 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|5869b7ef-5cbd-40b2-b17d-2b4591a92144 | underdog | Matthew Golden | Receiving Yards | under | 0.12870107458299462 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|ae0024e2-e6f7-4496-90a2-739f7b072ef9 | underdog | Jaylen Waddle | Receiving Yards | under | 0.12663902325289267 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|718f4381-f4aa-4349-8ddf-87b76363c39b | underdog | Pat Bryant | Receptions | under | 0.1253436724768694 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|b78af82a-6121-4425-9929-49b0396c30fe | underdog | J.J. McCarthy | Rush Yards | under | 0.1251574833333048 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|d0291dbd-b80d-4ff4-974c-7a7cafb72c56 | underdog | Malcolm Roach | Sacks | over | 0.1247782827043179 | 2026-11-08T06:01:51Z | 2026-11-08T18:00:00Z |
| underdog|5adfe6e8-e91f-44dd-842d-5be373846225 | underdog | Chris Olave | Receptions | under | 0.12468750167033804 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|58790b19-dd02-48db-9994-baaab8acbb8b | underdog | Rachaad White | Receptions | under | 0.12456515053371986 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|abe5fb36-b140-496d-8138-08cf2021eab6 | underdog | Jayden Daniels | Pass TDs | under | 0.12401048501725953 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|a5a84e5b-2d1a-407b-ad40-5e0faa4d1d12 | underdog | Wil Lutz | Kicking Points | under | 0.12375220362671835 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|6fa07966-69ad-4e19-932b-f21a9e51b66b | underdog | Ollie Gordon | Rush Yards | under | 0.12319862002616433 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|f976dc5d-1a44-411e-af88-3d28a1f7fc27 | underdog | Cyrus Allen | Receiving Yards | under | 0.12286875427405008 | 2026-11-08T15:09:02Z | 2026-11-08T18:00:00Z |
| underdog|f3d5e2f8-b078-48d2-b5d6-54ca6ca199e6 | underdog | Cairo Santos | Kicking Points | under | 0.12236507723893952 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|6af67397-ef8c-4d66-8d08-e0c828317ac8 | underdog | Austin Ekeler | Rush Yards | under | 0.12236362056805405 | 2026-11-08T06:01:51Z | 2026-11-08T18:00:00Z |
| underdog|5b41e18b-fe87-4483-b80d-3133407033e6 | underdog | Hunter Henry | Receptions | under | 0.12233979989646315 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|9a6bf26d-777c-4ed1-a55d-58f8fc621644 | underdog | Kaelon Black | Receptions | under | 0.12200046497800188 | 2026-11-06T06:34:07Z | 2026-11-08T21:25:00Z |
| underdog|cc098e45-ccc0-4139-b477-e6e52ec1417e | underdog | Hunter Henry | Receiving Yards | under | 0.12177355998086026 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| prizepicks|16719168 | prizepicks | Caleb Douglas | Rec Targets | under | 0.12141200380041606 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|16510e89-3e9d-4b33-9549-19154015507d | underdog | Tyler Allgeier | Receptions | under | 0.12089928730863053 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|1d0d1a24-84f2-494e-b408-57fa31871b73 | underdog | Maxx Crosby | Sacks | over | 0.12068546506850075 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| prizepicks|16747855 | prizepicks | Mason Taylor | Rec Targets | under | 0.12041082710254603 | 2026-11-07T05:59:57Z | 2026-11-08T13:00:00.000-05:00 |
| prizepicks|16576409 | prizepicks | Christian McCaffrey | Rush Yards | under | 0.11950744181162642 | 2026-11-03T02:21:46Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|c7bb0bb6-dc60-4c38-93e2-684dacb04b02 | underdog | Josh Allen | Pass TDs | under | 0.11926653211048077 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|f4bfe3bd-d628-4573-9415-7680b5b2c40d | underdog | CeeDee Lamb | Receiving Yards | under | 0.11812765591021201 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|1c07119d-7fe4-4eba-b8f2-c7008e344979 | underdog | Harold Fannin | Receptions | under | 0.11801150156707052 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|eccd30c3-ed5b-4cc6-aad4-06299d22c529 | underdog | Malik Nabers | Receptions | under | 0.11783962166306128 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|a2c99cc9-08b9-47ba-a659-2ab43cdbd1d8 | underdog | Saquon Barkley | Rush Yards | under | 0.1165322243623439 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|b97ea732-c9bd-475b-9b65-9472160330d6 | underdog | Colby Wooden | Sacks | over | 0.11627675972376245 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|c3130728-988e-4cdf-9fa4-96cbff03e330 | underdog | Kyren Williams | Rush Yards | under | 0.11604746503488483 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|649d4cf3-3d96-4754-b6ba-149b97bba842 | underdog | Kenneth Walker III | Receptions | under | 0.11559688528805712 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|e8cae3b1-b533-4e01-9ccd-2c3925dd344f | underdog | Rome Odunze | Receiving Yards | under | 0.11558163710749247 | 2026-11-08T06:01:51Z | 2026-11-09T01:20:00Z |
| underdog|9825e0ba-f877-4bf7-812c-f9129d57348c | underdog | Patrick Mahomes | Pass TDs | under | 0.11537751808865182 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|df8cc29e-c9c7-46e3-9773-066f25acc7a6 | underdog | CeeDee Lamb | Receptions | under | 0.11512462845971994 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| prizepicks|16718536 | prizepicks | Jaylen Waddle | Rec Targets | under | 0.11494202569891032 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|cdd1233d-4582-4e6e-8e8e-b108508a6271 | underdog | Seth McGowan | Rush + Rec Yards | under | 0.11412565644664707 | 2026-11-08T15:09:02Z | 2026-11-08T18:00:00Z |
| prizepicks|16764340 | prizepicks | Kyle Williams | Rec Targets | under | 0.11404754178635423 | 2026-11-07T05:59:57Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|3a5ae6bb-5bc7-48b9-b294-74e6475ea418 | underdog | DeMario Douglas | Receptions | under | 0.11403945725604647 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|9cbde803-209b-4f3b-a56f-61eec08692cf | underdog | David Bailey | Sacks | over | 0.11369104032590455 | 2026-11-08T06:01:51Z | 2026-11-08T18:00:00Z |
| underdog|bc4e2511-6040-4a80-9398-a16ad8530216 | underdog | Keenan Allen | Receiving Yards | under | 0.11353905024788158 | 2026-11-06T16:02:47Z | 2026-11-08T18:00:00Z |
| underdog|8dda3f2c-43bd-496a-91aa-283c7a072e7b | underdog | Chuba Hubbard | Receptions | under | 0.11351803648802827 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|980ef0c9-e7c6-40c1-ae91-d71c59322e06 | underdog | Travis Kelce | Receptions | under | 0.11333613992057967 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|48e760c2-4eac-4eb7-a8a9-531f0ca1ef83 | underdog | Ryan Fitzgerald | Kicking Points | under | 0.11326096940715735 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| prizepicks|16747632 | prizepicks | Matthew Golden | Recs | under | 0.11305017989971933 | 2026-11-07T05:59:57Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|3b806c99-c348-44de-86cc-461e6cf2d3f2 | underdog | Jake Bates | FG Made | under | 0.11285240847954703 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|36391894-b67e-489e-a9ba-6d5745343435 | underdog | Nate Adkins | Receiving Yards | over | 0.11258180819122365 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|d057f822-2dbd-4436-adc8-eadda12bcc00 | underdog | Tim Patrick | Receiving Yards | under | 0.11158456730208843 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| prizepicks|16719170 | prizepicks | Greg Dulcich | Rec Targets | under | 0.1112945325708179 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|fc8e948f-e862-45a9-9635-07a454ffb0a7 | underdog | J.K. Dobbins | Receiving Yards | over | 0.11121136707341117 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| underdog|6dd32214-c772-4921-8a71-e54023a58664 | underdog | Efton Chism | Receiving Yards | under | 0.11109690477811329 | 2026-11-08T06:01:51Z | 2026-11-08T21:25:00Z |
| underdog|4781b322-c16f-488a-b23d-ff4462376142 | underdog | Matthew Stafford | Pass TDs | under | 0.11063723570251016 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|79412c48-0236-4716-a47b-8ce152fec2ea | underdog | Akheem Mesidor | Sacks | over | 0.11060330554897452 | 2026-11-08T06:01:51Z | 2026-11-08T21:05:00Z |
| prizepicks|16719176 | prizepicks | Rhamondre Stevenson | Rec Targets | under | 0.1104895168364537 | 2026-11-05T22:06:44Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|1fecccd3-7915-4b3d-9923-95b353ee0c90 | underdog | J.K. Dobbins | Receptions | under | 0.11024990718515137 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|cb8fe87c-c267-4e98-8768-a199b4f8338b | underdog | Simi Fehoko | Receptions | under | 0.11023737676758572 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| prizepicks|16685556 | prizepicks | Dak Prescott | Pass TDs | under | 0.10986040123516894 | 2026-11-05T12:22:13Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|685edd25-24fb-4af2-a25d-548ec56bea29 | underdog | Tyler Warren | Receptions | under | 0.10969276868099631 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|0c982e54-179a-4101-a215-70855b7eaf00 | underdog | D'Andre Swift | Receptions | under | 0.10961929542717408 | 2026-11-05T12:22:13Z | 2026-11-09T01:20:00Z |
| prizepicks|16722858 | prizepicks | Kyle Juszczyk | Rec Targets | under | 0.10961448099981719 | 2026-11-06T06:34:07Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|b34d3248-ec10-4121-9c7b-b4746dee816d | underdog | Charlie Kolar | Receptions | under | 0.10960132616239582 | 2026-11-05T12:22:13Z | 2026-11-08T21:05:00Z |
| underdog|69a82857-d297-4b15-a385-2a023ebcf054 | underdog | Dalton Kincaid | Receptions | under | 0.10948029145485216 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|ba47c124-db10-4b69-b5cf-5ba62f5c4d37 | underdog | Jahmyr Gibbs | Receptions | under | 0.10946590257471323 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|3cd2b418-6262-4bea-8204-d5c65be18a7d | underdog | Adonai Mitchell | Receptions | under | 0.10924843875645252 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|b839652f-0e46-467f-9992-35c5469cf144 | underdog | D'Andre Swift | Receiving Yards | under | 0.10895292459147943 | 2026-11-05T12:22:13Z | 2026-11-09T01:20:00Z |
| underdog|2a03ddda-093f-4ef6-a512-af233e05477d | underdog | Chad Ryland | FG Made | over | 0.10832807545342293 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|4c17b548-6dd0-41a7-be94-4eeba93de71a | underdog | Nico Collins | Receptions | under | 0.10808570977681886 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|1022f42b-a007-4d3a-b5ed-9a614c441a49 | underdog | Tim Patrick | Receptions | under | 0.10753144499846912 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| prizepicks|16722855 | prizepicks | Christian McCaffrey | Rec Targets | under | 0.10741475862792937 | 2026-11-06T06:34:07Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|1b7021b4-b333-4256-bc1e-7c9f88464431 | underdog | Jonah Coleman | Receptions | under | 0.10693828108030978 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|5be18191-a04f-4092-a1cd-458a07b6ec60 | underdog | Savion Williams | Receptions | under | 0.10693644241407008 | 2026-11-05T22:06:44Z | 2026-11-08T21:25:00Z |
| underdog|d599a5ae-1ff8-4df6-9eac-c397c998888d | underdog | Colston Loveland | Receptions | under | 0.10664747026618215 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|32711800-db27-440c-a743-4d137cde2fad | underdog | Breece Hall | Rush + Rec Yards | under | 0.10656138323472575 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|5b61aab8-a7d2-414b-8490-9bbaa9548e23 | underdog | Jordan Watkins | Receptions | under | 0.10633140598140345 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|c63b731c-e508-484e-a7b0-4ac96e4df7e8 | underdog | Seth McGowan | Rush Yards | under | 0.10632668122712119 | 2026-11-08T06:01:51Z | 2026-11-08T18:00:00Z |
| underdog|552d6ed3-57fe-4ea3-8bd6-3bcec6e29b71 | underdog | Jordan Addison | Receiving Yards | under | 0.10614115606118668 | 2026-11-05T22:06:44Z | 2026-11-10T01:15:00Z |
| prizepicks|16794694 | prizepicks | Cade Otton | Rec Targets | under | 0.10608279987092917 | 2026-11-08T06:01:51Z | 2026-11-08T20:20:00.000-05:00 |
| underdog|866fa3e8-bc09-4ddc-a0f3-84f88eaf57ce | underdog | John Metchie III | Receptions | under | 0.1060012724235827 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|68027fbe-2681-4510-8eea-3775ceb54e92 | underdog | Dalton Schultz | Receptions | under | 0.10596561958189699 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|6cca36dd-8c03-48ab-b0f3-670b30e36d49 | underdog | Zach Allen | Sacks | over | 0.10569837398396476 | 2026-11-08T06:01:51Z | 2026-11-08T18:00:00Z |
| underdog|d8cc7000-c796-46ee-8039-4c6784611f7c | underdog | Quinnen Williams | Sacks | over | 0.10569102457609608 | 2026-11-08T06:01:51Z | 2026-11-08T18:00:00Z |
| prizepicks|16718516 | prizepicks | Colston Loveland | Rec Targets | under | 0.1053686257660188 | 2026-11-05T22:06:44Z | 2026-11-08T20:20:00.000-05:00 |
| underdog|54a4a86f-12fb-48ce-ae28-78d9e65e325f | underdog | D'Andre Swift | Rush Yards | under | 0.10486667539877703 | 2026-11-07T05:59:57Z | 2026-11-09T01:20:00Z |
| underdog|2b07303d-fe20-4bc5-8345-34bde54e95a1 | underdog | Dak Prescott | Pass TDs | under | 0.10429726760636782 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|a34fbd98-b819-47f8-ad35-0910f6aa4848 | underdog | DeMario Douglas | Receiving Yards | under | 0.10423741151490673 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|4a328574-9067-45a3-b2c8-168d822b5e16 | underdog | T.J. Hockenson | Receiving Yards | under | 0.10407541804729603 | 2026-11-03T11:59:28Z | 2026-11-10T01:15:00Z |
| underdog|a9b8a6e5-7405-489a-94a1-d068a323e253 | underdog | Dallas Goedert | Receptions | under | 0.1033306586731757 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| prizepicks|16718518 | prizepicks | Luther Burden III | Rec Targets | under | 0.10325655879442341 | 2026-11-05T22:06:44Z | 2026-11-08T20:20:00.000-05:00 |
| underdog|c71c7cdb-dcfc-4a27-b97c-06c3401aaf2c | underdog | Dani Dennis-Sutton | Sacks | over | 0.10322188894736123 | 2026-11-06T16:02:47Z | 2026-11-08T21:25:00Z |
| prizepicks|16577039 | prizepicks | Rashee Rice | Rec Yards | under | 0.10318750310261049 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|0956c551-7636-4e3a-9169-b3769b75c668 | underdog | James Cook | Rush + Rec Yards | under | 0.10280034547108508 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|8ca38ea4-fb7d-450d-93e0-ad698309f00c | underdog | Dawson Knox | Receiving Yards | under | 0.10256010348325972 | 2026-11-07T05:59:57Z | 2026-11-10T01:15:00Z |
| underdog|3f7838a7-6e6e-47ac-8296-165647381eb8 | underdog | Jerry Jeudy | Receptions | under | 0.10245858231518723 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|c4b8e03b-86f2-4d6c-b024-04caa813ed63 | underdog | Andre Szmyt | FG Made | under | 0.10236818666743885 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|45750299-7aad-4237-aad2-7938789941f4 | underdog | Mack Hollins | Receptions | under | 0.1023289370166569 | 2026-11-08T06:01:51Z | 2026-11-08T21:25:00Z |
| underdog|aaf30715-a58e-484d-b64b-5c9d91157d42 | underdog | Ted Hurst | Receptions | over | 0.10215868472628065 | 2026-11-05T22:06:44Z | 2026-11-09T01:20:00Z |
| underdog|0151cf48-ec7a-4946-9402-cd00b223e299 | underdog | Josh Sweat | Sacks | under | 0.10215084756182702 | 2026-11-08T06:01:51Z | 2026-11-08T21:25:00Z |
| underdog|d9d08697-3dd2-4d24-bc73-42297b125227 | underdog | Jameson Williams | Receptions | under | 0.10208410937911938 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| prizepicks|16779729 | prizepicks | Makai Lemon | Rec Targets | under | 0.1019457043102242 | 2026-11-08T06:01:51Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|f4bba20a-76ec-4df5-9de0-3c7c20bd1a76 | underdog | Keon Coleman | Receptions | under | 0.10169343136994924 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|24a49a3b-5f76-4977-9e37-fd6d51db08c2 | underdog | Jahmyr Gibbs | Rush Yards | under | 0.10154569505675504 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| prizepicks|16764343 | prizepicks | Devin Singletary | Rec Targets | under | 0.10107442699598002 | 2026-11-07T05:59:57Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|23fa46de-8f35-4b86-b931-58c2c9be738f | underdog | Javonte Williams | Rush Yards | under | 0.10095549971421969 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|528efebf-508e-4983-936c-690477ebd224 | underdog | Christian McCaffrey | Receptions | under | 0.10087596308915803 | 2026-11-05T22:06:44Z | 2026-11-08T21:25:00Z |
| underdog|bcf0586b-f2c4-464a-862b-6a09dc77b05a | underdog | John Bates | Receiving Yards | over | 0.10056043833569972 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|bdf4a4f2-c1e9-47fc-8fe5-b93626e43e6b | underdog | James Cook | Rush Yards | under | 0.10046089264064739 | 2026-11-05T22:06:44Z | 2026-11-10T01:15:00Z |
| underdog|4c0c83a7-22fc-43b3-9db9-d140c271a605 | underdog | Oronde Gadsden | Receptions | under | 0.10018871071931101 | 2026-11-05T12:22:13Z | 2026-11-08T21:05:00Z |
| underdog|4afc2300-5142-4b1d-8549-f4057b069707 | underdog | George Pickens | Receptions | under | 0.10004029761411559 | 2026-11-08T06:01:51Z | 2026-11-08T18:00:00Z |
| underdog|ad219443-0404-4391-b1bf-2707df6b9de7 | underdog | Omarion Hampton | Receptions | over | 0.09981815938380334 | 2026-11-05T12:22:13Z | 2026-11-08T21:05:00Z |
| underdog|85ccf44b-f7bc-4dcb-8e44-34d938c7b0be | underdog | Tyler Goodson | Rush Yards | under | 0.09926361066374967 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|39f45cca-973d-4355-ba85-f1085b70cd7c | underdog | Mitchell Evans | Receiving Yards | over | 0.09918365229749104 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|aa444c6b-f74f-4284-97b4-ed7efef8cd13 | underdog | Jack Bech | Receiving Yards | over | 0.09915193262395117 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|57f73ccb-63b1-451c-bbeb-fbaac3456b03 | underdog | Aaron Jones | Receptions | under | 0.09908473856146005 | 2026-11-05T12:22:13Z | 2026-11-10T01:15:00Z |
| underdog|b8cedee8-c662-401f-874c-21a9a3c20ec5 | underdog | Roschon Johnson | Receiving Yards | over | 0.09908023934505272 | 2026-11-06T16:02:47Z | 2026-11-09T01:20:00Z |
| underdog|24324e94-375f-47e6-81b8-1367b471a178 | underdog | Juwan Johnson | Receptions | under | 0.09851839400207829 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|d1e744f7-e48f-432b-ac36-9994d2f0347b | underdog | Chuba Hubbard | Rush Yards | under | 0.09846599432023506 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| prizepicks|16685623 | prizepicks | D'Andre Swift | Rush TDs | over | 0.09831155568334193 | 2026-11-05T12:22:13Z | 2026-11-08T20:20:00.000-05:00 |
| prizepicks|16718529 | prizepicks | KC Concepcion Jr. | Rec Targets | under | 0.09759613041448167 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|ca0b739f-619d-44bc-a06f-c2bc8dfffd97 | underdog | Mitchell Evans | Receptions | over | 0.09744221623392268 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|96e04406-2dc9-4e27-a7a3-24fef33ac8dd | underdog | Mason Taylor | Receiving Yards | under | 0.09725922451571889 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|dd95402c-e9ca-44e5-a5a3-179e2734707c | underdog | Jordan Addison | Receptions | under | 0.09707338503094809 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|777a6934-83da-4fc6-ae05-670614aac4c8 | underdog | Luther Burden | Receptions | under | 0.0970050304666229 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| underdog|30c1bb35-0142-4f31-bbb5-91dd02464159 | underdog | Noah Fant | Receiving Yards | over | 0.09664098735490922 | 2026-11-08T15:09:02Z | 2026-11-08T18:00:00Z |
| underdog|d81755ee-3b9d-4b52-866f-6b234a018dd8 | underdog | Caleb Douglas | Receiving Yards | under | 0.09649565964839524 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|2bac7b08-fac7-40ce-8ab4-52eed070b62a | underdog | Jordan Love | Pass TDs | under | 0.0961519218860859 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|0f4bff94-0106-4f5e-b376-4f86353dfda5 | underdog | Dallas Goedert | Receiving Yards | under | 0.095781750919261 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|8e794760-3f49-4bee-81bf-4c5f29c7dc27 | underdog | Tyler Allgeier | Receiving Yards | under | 0.09577866004051383 | 2026-11-05T22:06:44Z | 2026-11-08T21:25:00Z |
| underdog|50ab1583-86de-4d93-ad49-f9c77e284022 | underdog | Kyle Juszczyk | Receptions | under | 0.09555935955530548 | 2026-11-05T22:06:44Z | 2026-11-08T21:25:00Z |
| underdog|70b674bf-14ef-4526-b90e-42cba3c6d3a5 | underdog | Adam Trautman | Receptions | under | 0.09545112973787573 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|d85cf0d6-2695-4b3d-b020-2d7b0b8d5c22 | underdog | Aidan Hutchinson | Sacks | under | 0.09526576932404729 | 2026-11-08T06:01:51Z | 2026-11-08T18:00:00Z |
| underdog|a5eb6366-cd82-4d6b-bd95-f5e0ede614e0 | underdog | Ka'imi Fairbairn | Kicking Points | under | 0.09495465902987144 | 2026-11-03T02:21:46Z | 2026-11-08T21:05:00Z |
| underdog|f84d7aab-a448-4292-871a-1f620651db5e | underdog | Henry To'oTo'o | Sacks | over | 0.09474105605500435 | 2026-11-06T16:02:47Z | 2026-11-08T21:05:00Z |
| underdog|f9590851-6bea-45e6-a553-0c5a188abda2 | underdog | Khalil Mack | Sacks | over | 0.09358576864044105 | 2026-11-08T06:01:51Z | 2026-11-08T21:05:00Z |
| underdog|f3b449a7-fca2-44b0-928e-0e8f33156504 | underdog | Ted Hurst | Receiving Yards | under | 0.09331723842757189 | 2026-11-08T06:01:51Z | 2026-11-09T01:20:00Z |
| underdog|285b8cc1-e70a-497a-b860-ab7fc239dce6 | underdog | Denzel Boston | Receiving Yards | under | 0.0930300815809536 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|5b87e878-a87a-4833-a5f2-0c56bd5e34a3 | underdog | Rachaad White | Receiving Yards | under | 0.09288707490475656 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| prizepicks|16685554 | prizepicks | Jared Goff | Pass TDs | under | 0.09280845049511621 | 2026-11-05T12:22:13Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|e817a19f-8ec3-4eb9-9651-08edf2d48808 | underdog | Chase Young | Sacks | under | 0.09158465620785661 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|b18c0d78-0755-4448-8b08-b78e942b1cc3 | underdog | George Pickens | Receiving Yards | under | 0.09130378441499509 | 2026-11-08T06:01:51Z | 2026-11-08T18:00:00Z |
| underdog|e58343c7-9920-47f1-a65f-5bee919ad58f | underdog | Theo Johnson | Receptions | under | 0.0903910099865256 | 2026-11-08T06:01:51Z | 2026-11-08T18:00:00Z |
| underdog|d52dc310-ea00-4c21-bb95-3798608a708f | underdog | Quentin Johnston | Receptions | under | 0.08995109550904856 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|6699fb40-5a95-41f1-9466-35c2c70f45a0 | underdog | Christian Watson | Receiving Yards | under | 0.08988230264780483 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|e821ebad-cf32-4e72-8584-78c56c0445d0 | underdog | Kenny Gainwell | Receiving Yards | under | 0.0892368124618752 | 2026-11-08T15:09:02Z | 2026-11-09T01:20:00Z |
| underdog|abb09631-9c55-4d39-9cfb-5c32edeee8a5 | underdog | Jalen Coker | Receiving Yards | under | 0.08920861688542747 | 2026-11-08T15:09:02Z | 2026-11-08T18:00:00Z |
| underdog|27cb9670-5382-48df-ab83-f72399dbeeac | underdog | Travis Kelce | Receiving Yards | under | 0.08860625184263005 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|86292b7c-6c42-4233-8f3e-77467258ebb0 | underdog | Ryan Flournoy | Receptions | under | 0.08859702462308638 | 2026-11-08T06:01:51Z | 2026-11-08T18:00:00Z |
| underdog|166779ae-821b-470d-b0bc-1713be514bda | underdog | Jeffery Simmons | Sacks | over | 0.08816301575517055 | 2026-11-08T06:01:51Z | 2026-11-09T01:20:00Z |
| underdog|6bfed22d-3db5-4ee3-ac23-251ee8be1c2e | underdog | Byron Young | Sacks | over | 0.08809169586862114 | 2026-11-08T06:01:51Z | 2026-11-08T18:00:00Z |
| underdog|c530e70f-d7bb-44d6-b035-04f7d6fe85bc | underdog | Denzel Boston | Receptions | under | 0.0880374444037425 | 2026-11-08T15:09:02Z | 2026-11-08T18:00:00Z |
| underdog|93c23b7a-e00a-436d-bdbf-012f847dcbfb | underdog | Jonah Coleman | Receiving Yards | under | 0.08784628755770052 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|b722c0eb-24f9-4457-aca1-c570a4906039 | underdog | Chris Olave | Receiving Yards | under | 0.08783600387699941 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|e2b129c7-4ce7-4ac8-abb8-cf4529dbd83a | underdog | Kenneth Walker III | Rush + Rec Yards | under | 0.08768372599524399 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|d6f14494-641b-4ed4-9b04-4ed516e0f469 | underdog | Josh Downs | Receptions | under | 0.08767799557017741 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| prizepicks|16764338 | prizepicks | Efton Chism III | Rec Targets | under | 0.08767504270499804 | 2026-11-07T05:59:57Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|02084d0c-6d32-4b45-bc7a-54262029491a | underdog | Elijah Mitchell | Receptions | under | 0.08726398545769454 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|04964b73-2a28-4fed-a846-cc5f58153c54 | underdog | Drew Stevens | Kicking Points | under | 0.08711701512948622 | 2026-11-08T06:01:51Z | 2026-11-08T18:00:00Z |
| underdog|85d0f744-992b-44c1-8a7c-101d9724dfdc | underdog | Bucky Irving | Receiving Yards | under | 0.08678510565293707 | 2026-11-05T12:22:13Z | 2026-11-09T01:20:00Z |
| underdog|87e67aff-abb3-4158-9ac0-1b237a7b4a43 | underdog | Jonathan Taylor | Rush + Rec Yards | under | 0.08666188699419164 | 2026-11-06T16:02:47Z | 2026-11-08T18:00:00Z |
| underdog|12a2d911-b12a-443c-8611-c6a04a06c827 | underdog | Keenan Allen | Receptions | under | 0.08657096839321532 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|d34832e9-294d-4fd4-ab86-c2274d39c601 | underdog | Kyren Williams | Rush + Rec Yards | under | 0.08637385722111368 | 2026-11-08T06:01:51Z | 2026-11-08T18:00:00Z |
| underdog|3c25e1f6-5855-4e10-b07c-c168b58f8e8b | underdog | Andre Szmyt | Kicking Points | under | 0.08606085228469695 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|2de77434-e9f7-416c-b3f4-c8c99c086db0 | underdog | Braelon Allen | Receptions | under | 0.08548177488523989 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|573a09d8-1d66-4418-8ca5-3e2e403d8b93 | underdog | Trevor Etienne | Rush Yards | under | 0.08500270395062026 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| underdog|9a11ea53-966f-452f-a1c2-ab1154cc943e | underdog | Jalen Coker | Receptions | under | 0.08455880625865009 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|a8b4d56b-3190-4729-a3e3-fa4952f7fe19 | underdog | Malachi Fields | Receptions | under | 0.08444567676815706 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|fca3da4f-9476-4b17-ad79-8f80aef153b9 | underdog | Elina Svitolina | Double Faults | under | 0.08423149243173988 | 2026-11-05T12:22:13Z | 2026-11-09T21:10:00Z |
| underdog|6a86fd4e-71ed-4ef4-ae70-3e3ad04165e2 | underdog | Danielle Hunter | Sacks | under | 0.08383939910950078 | 2026-11-08T06:01:51Z | 2026-11-08T21:05:00Z |
| underdog|de3a28c0-990e-45e6-b955-eb21bc4ad9a4 | underdog | Patrick Mahomes | Rush Yards | under | 0.08365133891580678 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|ca923a9a-2e8e-46ad-acaf-0b4ecc69a8bd | underdog | Malik Nabers | Receiving Yards | under | 0.08364693870895912 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| prizepicks|16747634 | prizepicks | Christian McCaffrey | Recs | under | 0.08327349289890928 | 2026-11-07T05:59:57Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|d2a2884a-9482-4454-8f62-b11b25cf9301 | underdog | AJ Barner | Receiving Yards | under | 0.08315373110424162 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|4e7cab7c-a9a4-4533-ae0e-b7d96c3d425b | underdog | Jack Bech | Receptions | under | 0.08300134151445937 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|5dac4379-344e-4827-a776-61da116ee26a | underdog | Jonathan Taylor | Rush Yards | under | 0.08275096271826443 | 2026-11-08T15:09:02Z | 2026-11-08T18:00:00Z |
| underdog|e0ced813-8b2c-4455-b57b-71da99a39e7d | underdog | Blake Corum | Rush + Rec Yards | under | 0.0827040556047397 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| prizepicks|16719186 | prizepicks | Jaxon Smith-Njigba | Rec Targets | under | 0.08268085501976197 | 2026-11-05T22:06:44Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|da62c07e-9a73-4df4-b991-a41eacd49ff3 | underdog | Drake Maye | Rush Yards | under | 0.08267152286343105 | 2026-11-08T15:09:02Z | 2026-11-08T21:25:00Z |
| underdog|09d08c07-2b49-48fa-a8ec-90fcf779eab1 | underdog | Isaiah Williams | Receiving Yards | over | 0.08233947364479088 | 2026-11-08T06:01:51Z | 2026-11-08T18:00:00Z |
| underdog|db8a215c-a32b-461f-a74f-392bfed6cd47 | underdog | Sam LaPorta | Receptions | under | 0.08195280346786493 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|68173c0b-2080-4055-b4ae-bddf30f8835f | underdog | Omar Cooper | Receptions | under | 0.08175619641694731 | 2026-11-06T16:02:47Z | 2026-11-08T18:00:00Z |
| underdog|1bc615c1-043a-4445-9e64-11eb22ceba0a | underdog | Seth McGowan | Receptions | under | 0.08155867442257059 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|114e40cb-83b3-4b38-a44f-7fd853dbc826 | underdog | Blake Corum | Rush Yards | under | 0.08133865297637977 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|30c987cb-9450-418a-b4ff-d450e9c0183f | underdog | Ashton Jeanty | Receptions | under | 0.08123630317472041 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|30991dac-153e-4344-b3ff-ad0dab588a17 | underdog | Khalil Shakir | Receptions | under | 0.08115998065425789 | 2026-11-08T06:01:51Z | 2026-11-10T01:15:00Z |
| underdog|8603a67e-b64c-4937-a332-1ee911b5f8e3 | underdog | Elijah Moore | Receiving Yards | over | 0.08099514490247195 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|3f37b916-250a-4972-965b-ecb6efeb0ce3 | underdog | Chris Bell | Receiving Yards | under | 0.08090076495058063 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|0ea0b642-98a0-416f-b69d-b7ce615c61b3 | underdog | Drew Stevens | FG Made | under | 0.0806709260026024 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|a93191dc-5ab3-4d60-9b3c-0635b721460f | underdog | Baker Mayfield | Rush Yards | under | 0.0804542415617544 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| prizepicks|16794695 | prizepicks | Chris Godwin Jr. | Rec Targets | under | 0.08026078072409382 | 2026-11-08T06:01:51Z | 2026-11-08T20:20:00.000-05:00 |
| underdog|ff70b613-e13b-4266-9d3b-50e215560c82 | underdog | Tyler Allgeier | Rush + Rec Yards | under | 0.07924262731427245 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|9cf08033-8542-40f3-b9be-f073096d2ae5 | underdog | Brandon Aubrey | Kicking Points | under | 0.07917497791850081 | 2026-11-08T06:01:51Z | 2026-11-08T18:00:00Z |
| underdog|7736c2b9-bcdb-4bfd-bd4f-4271f590b609 | underdog | Lukas Van Ness | Sacks | over | 0.07844016411325083 | 2026-11-06T16:02:47Z | 2026-11-08T21:25:00Z |
| prizepicks|16718545 | prizepicks | Christian Watson | Rec Targets | under | 0.07759156462609396 | 2026-11-05T22:06:44Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|4a89e10d-0ca4-474d-97f5-0bc040a68326 | underdog | Keaton Mitchell | Receptions | under | 0.07757945660569399 | 2026-11-06T06:34:07Z | 2026-11-08T21:05:00Z |
| underdog|b8df26b0-9693-4eea-be77-02dde4afac4a | underdog | KC Concepcion | Receiving Yards | under | 0.07728816268623151 | 2026-11-08T15:09:02Z | 2026-11-08T18:00:00Z |
| underdog|273b4f1f-bf42-4a41-a69b-e9b2f4dd10f1 | underdog | Reggie Virgil | Receiving Yards | under | 0.07701412532993002 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|725f645e-532d-464c-93cb-f84b3ced729a | underdog | Omar Cooper | Receiving Yards | under | 0.07669141354034092 | 2026-11-08T06:01:51Z | 2026-11-08T18:00:00Z |
| underdog|47a5a56d-1fdf-4c6f-9f05-0fc430cbbbea | underdog | Cade Otton | Receptions | under | 0.07553932484130521 | 2026-11-07T05:59:57Z | 2026-11-09T01:20:00Z |
| underdog|375ce9fc-2de7-4481-8fa3-2726e095eb69 | underdog | Sione Vaki | Receptions | over | 0.07552389420860717 | 2026-11-08T06:01:51Z | 2026-11-08T18:00:00Z |
| underdog|b40659e4-2add-461a-ada3-aae1160149b6 | underdog | Laiatu Latu | Sacks | over | 0.07522082045184025 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|80d395a7-fff7-4ff4-9710-ea3c03ad9d49 | underdog | Troy Franklin | Receptions | under | 0.07479838510150683 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|c9f42cb3-782a-42ae-8d36-b838a2e16e5b | underdog | Tyler Goodson | Receptions | under | 0.07447307028831152 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|631d9189-59fb-41d1-b8f1-881c439ff102 | underdog | Saquon Barkley | Receiving Yards | under | 0.07446466609001934 | 2026-11-08T15:09:02Z | 2026-11-08T18:00:00Z |
| prizepicks|16719159 | prizepicks | Ashton Jeanty | Rec Targets | under | 0.07445513690876382 | 2026-11-05T22:06:44Z | 2026-11-08T16:25:00.000-05:00 |
| prizepicks|16794697 | prizepicks | Tez Johnson | Rec Targets | under | 0.07415366833027626 | 2026-11-08T06:01:51Z | 2026-11-08T20:20:00.000-05:00 |
| underdog|f7c17ddd-b7da-47e1-b7cc-3c831055be6b | underdog | Dominic Zvada | FG Made | under | 0.0741063683238431 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|c7fde436-b10f-4b32-ade3-6592960e545e | underdog | Roschon Johnson | Receptions | under | 0.0740765133334802 | 2026-11-06T16:02:47Z | 2026-11-09T01:20:00Z |
| underdog|5571a9d9-5257-413c-94f7-b30035400e37 | underdog | Evan Engram | Receiving Yards | under | 0.07358911959876246 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| prizepicks|16719174 | prizepicks | T.J. Hockenson | Rec Targets | under | 0.07349799752159802 | 2026-11-05T22:06:44Z | 2026-11-09T20:15:00.000-05:00 |
| prizepicks|16576406 | prizepicks | Kyren Williams | Rush Yards | under | 0.0734640730790519 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|98370739-8ce7-4116-9352-2a9e7a795fa3 | underdog | C.J. Stroud | Pass TDs | under | 0.07344784426946727 | 2026-11-03T02:21:46Z | 2026-11-08T21:05:00Z |
| underdog|c10a0922-5357-4d12-a34a-fef19f41ae93 | underdog | Dylan Sampson | Receptions | under | 0.073210778810199 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| prizepicks|16577044 | prizepicks | Chig Okonkwo | Rec Yards | under | 0.07319171131719704 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|c09e8f25-de98-485a-9a92-3e90c88df8aa | underdog | Cameron Dicker | Kicking Points | under | 0.07288428793483492 | 2026-11-05T22:06:44Z | 2026-11-08T21:05:00Z |
| underdog|5c589e9f-50cb-4f4d-bc6c-31a94652a555 | underdog | Darren Waller | Receptions | under | 0.07257323185856346 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|274a5cd2-ea5e-4311-b899-27e6829d3d33 | underdog | Jaylahn Tuimoloau | Sacks | over | 0.07234169347564967 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|1060d4eb-fa5c-48ec-98f5-952162284f9c | underdog | Brenton Cox | Sacks | over | 0.07234169347564967 | 2026-11-06T16:02:47Z | 2026-11-08T21:25:00Z |
| underdog|6634eb0b-5d46-4989-bf92-f74b55194b0d | underdog | Braelon Allen | Receiving Yards | over | 0.07204591738738031 | 2026-11-08T06:01:51Z | 2026-11-08T18:00:00Z |
| underdog|4ff201eb-6873-438f-b135-cd456ff3b4ad | underdog | Tory Horton | Receiving Yards | under | 0.07152796009804019 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|143ec305-dbfc-4481-a66a-798b8b5fdca8 | underdog | Mike Washington | Rush + Rec Yards | under | 0.07125476656934071 | 2026-11-06T06:34:07Z | 2026-11-08T21:25:00Z |
| underdog|82a0c739-4fe5-4f9c-ab98-3f993aa6a3a8 | underdog | Blake Corum | Receptions | under | 0.07120017552093771 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| prizepicks|16779126 | prizepicks | Jared Goff | Fantasy Score | under | 0.0710045807783578 | 2026-11-08T06:01:51Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|eb3df861-975e-402b-9a2f-6d3b86ff283c | underdog | Tre' Harris | Receiving Yards | under | 0.0709968580126602 | 2026-11-08T06:01:51Z | 2026-11-08T21:05:00Z |
| underdog|1bc31085-4e77-40d3-8b0f-fb3e585817e6 | underdog | Andrew Van Ginkel | Sacks | under | 0.07086304367418039 | 2026-11-08T06:01:51Z | 2026-11-10T01:15:00Z |
| prizepicks|16718564 | prizepicks | Cyrus Allen | Rec Targets | under | 0.07077470405848951 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|7bff2e43-ab12-4a98-b7e5-04d0c0bbf914 | underdog | Mike Washington | Receptions | under | 0.07071209556400804 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|1f1d13a1-afea-41e0-842f-8af4981136b9 | underdog | Kenneth Walker III | Rush Yards | under | 0.0706968503684764 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| prizepicks|16719178 | prizepicks | Chris Olave | Rec Targets | under | 0.07047505206770643 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|b13b2682-93bb-45e1-89e3-94c1fd65b925 | underdog | Tyler Allgeier | Rush Yards | under | 0.07029518340467622 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| prizepicks|16719171 | prizepicks | Malik Washington | Rec Targets | under | 0.07012174955976103 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|9cac1640-ca39-4f1b-931a-e2c850308466 | underdog | Noah Gray | Receptions | over | 0.06995762914057951 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|4f42e71e-9977-4467-9c6f-587a1fb01921 | underdog | Malik Willis | Pass TDs | under | 0.0698898131874599 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|89115aaa-6933-4814-bd99-d0c015645a91 | underdog | Simi Fehoko | Receiving Yards | over | 0.06937030085848273 | 2026-11-08T06:01:51Z | 2026-11-08T21:25:00Z |
| underdog|097a88ee-d188-4ac6-90fa-1746ae2b9b19 | underdog | Tyler Higbee | Receptions | under | 0.0692665656780046 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| prizepicks|16576408 | prizepicks | Javonte Williams | Rush Yards | under | 0.06913799764143458 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|c33ff82e-ba83-46d9-aa6d-6fbdf146a0e8 | underdog | Adonai Mitchell | Receiving Yards | under | 0.06912273937461644 | 2026-11-06T16:02:47Z | 2026-11-08T18:00:00Z |
| underdog|bb96d7f5-6a27-4519-8c7f-1cf0fd95f193 | underdog | MarShawn Lloyd | Rush Yards | over | 0.0684165411137505 | 2026-11-08T06:01:51Z | 2026-11-08T21:25:00Z |
| prizepicks|16683643 | prizepicks | Jake Bates | Kicking Points | under | 0.06818662504942608 | 2026-11-05T12:22:13Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|b479ca9d-4d1c-454f-bfff-733cb2735065 | underdog | Jason Myers | Kicking Points | under | 0.06786338640966882 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|b4a11205-f19f-4256-9e1e-6703e6a4644a | underdog | Jaylen Waddle | Receptions | under | 0.06756067788820463 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|d2d0c7f6-8c34-47ab-83c4-c4cc40e11773 | underdog | Elijah Moore | Receptions | over | 0.06688940577179958 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|d626307e-fd2a-4fe3-92e2-930891893f36 | underdog | Xavier Worthy | Receiving Yards | under | 0.06645128079909246 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| prizepicks|16719164 | prizepicks | Quentin Johnston | Rec Targets | under | 0.06632694700699171 | 2026-11-05T22:06:44Z | 2026-11-08T16:05:00.000-05:00 |
| underdog|fc8a7d1c-fc88-48bd-9122-4cea2b71c647 | underdog | Xavier Hutchinson | Receptions | under | 0.06623799366444505 | 2026-11-05T12:22:13Z | 2026-11-08T21:05:00Z |
| underdog|17d196b6-916b-4467-86c8-3e43337d1b9d | underdog | Josh Jacobs | Receiving Yards | under | 0.06580018595374104 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|e2076474-ba9e-4c4a-8a5e-8756583f0c4e | underdog | Woody Marks | Receiving Yards | under | 0.06554944061032464 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|71a179c9-8c81-4c4d-b746-d1a7a8edf706 | underdog | Blake Corum | Receiving Yards | over | 0.06495743915599017 | 2026-11-08T15:09:02Z | 2026-11-08T18:00:00Z |
| underdog|31bfe094-caf9-4d49-8816-cf4aaf31197b | underdog | Keaton Mitchell | Receiving Yards | over | 0.06489959084845753 | 2026-11-08T06:01:51Z | 2026-11-08T21:05:00Z |
| underdog|b13bd436-9bc2-4867-9041-17de5aa4b928 | underdog | Michael Wilson | Receiving Yards | under | 0.06474486073770425 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|1e146d1e-95ac-4e18-b97f-874278e4440b | underdog | Emmett Johnson | Rush Yards | under | 0.06444132725080376 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| prizepicks|16719175 | prizepicks | Jordan Addison | Rec Targets | under | 0.06403524396214921 | 2026-11-05T22:06:44Z | 2026-11-09T20:15:00.000-05:00 |
| underdog|21931440-adec-46d4-b530-994878d9e427 | underdog | T.J. Hockenson | Receptions | under | 0.06344057443403939 | 2026-11-03T02:21:46Z | 2026-11-10T01:15:00Z |
| underdog|030a66ea-977b-4f3f-80ab-d9d5dfb20bb1 | underdog | Josaiah Stewart | Sacks | over | 0.06277768727226701 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|a7c53c49-5fba-44ef-a7c0-6ecb7e1df828 | underdog | Dylan Sampson | Rush Yards | under | 0.06257432947997765 | 2026-11-08T15:09:02Z | 2026-11-08T18:00:00Z |
| underdog|dd1f7172-8330-424d-ac7f-1765ab353fcc | underdog | Dominic Zvada | Kicking Points | under | 0.062049653446879294 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|77b4877d-3f71-4431-a58c-c47849c98483 | underdog | Dylan Sampson | Rush + Rec Yards | under | 0.06167877071919203 | 2026-11-08T15:09:02Z | 2026-11-08T18:00:00Z |
| prizepicks|16577034 | prizepicks | Denzel Boston | Rec Yards | under | 0.06162987154195598 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| prizepicks|16718512 | prizepicks | Tetairoa McMillan | Rec Targets | under | 0.06149813023951123 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|25c1c609-f02b-479e-a8e9-207d8a1d915c | underdog | Will Anderson | Sacks | under | 0.0614850441388457 | 2026-11-08T06:01:51Z | 2026-11-08T21:05:00Z |
| underdog|d438953d-b4ac-4cdc-b67d-098f59b5e645 | underdog | Isaiah Williams | Receptions | over | 0.0614145132494156 | 2026-11-08T06:01:51Z | 2026-11-08T18:00:00Z |
| underdog|a76c333d-8463-47f6-85d4-807d8ecf25c3 | underdog | Chad Ryland | Kicking Points | over | 0.06114744870498551 | 2026-11-08T15:09:02Z | 2026-11-08T21:25:00Z |
| underdog|8c265bcd-7b60-4798-8607-03c1259a21e4 | underdog | Trey Smack | FG Made | under | 0.06104007152947344 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|c2bc47c2-6d3f-48ee-b74d-c4f141f4a11a | underdog | Kayshon Boutte | Receiving Yards | over | 0.060977623679458914 | 2026-11-05T22:06:44Z | 2026-11-08T21:05:00Z |
| underdog|a61e4818-f9a9-40ba-9525-901a49827383 | underdog | Ashton Gillotte | Sacks | over | 0.06091287239348786 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| prizepicks|16747633 | prizepicks | Jaxon Smith-Njigba | Recs | under | 0.060819500508052626 | 2026-11-07T05:59:57Z | 2026-11-08T16:25:00.000-05:00 |
| prizepicks|16778054 | prizepicks | Tomas Martin Etcheverry | Total Games | over | 0.06076899465086305 | 2026-11-08T06:01:51Z | 2026-11-09T06:00:00.000-05:00 |
| underdog|fac4af10-165a-4177-944e-51ad9c5660f6 | underdog | Matt Gay | FG Made | over | 0.06076705695301998 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| prizepicks|16722942 | prizepicks | Kenny Gainwell | Recs | under | 0.06053274770535577 | 2026-11-06T06:34:07Z | 2026-11-08T20:20:00.000-05:00 |
| underdog|b63dda4c-3a4d-4fab-ae5b-aff547a35d1a | underdog | Byron Murphy | Sacks | over | 0.06032788374603604 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|75fc0d6b-fc95-4755-9dca-a70f72575381 | underdog | Kimani Vidal | Rush + Rec Yards | under | 0.060182508715502125 | 2026-11-05T22:06:44Z | 2026-11-08T21:05:00Z |
| underdog|d29599ad-f597-4f28-9d87-acf1c29a3761 | underdog | Elijah Higgins | Receptions | under | 0.060018765343776814 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|ce15f976-d7f9-425f-ad6c-ee1a00299302 | underdog | Jahmyr Gibbs | Receiving Yards | under | 0.059821904171410645 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| underdog|9437e438-3e22-45ed-9cfc-a9ad1d0cb11e | underdog | MarShawn Lloyd | Rush + Rec Yards | over | 0.05972271045730859 | 2026-11-08T06:01:51Z | 2026-11-08T21:25:00Z |
| underdog|d0960391-8a29-49e1-adce-9b8b9a13efe6 | underdog | Kimani Vidal | Receptions | under | 0.0595189274468374 | 2026-11-05T12:22:13Z | 2026-11-08T21:05:00Z |
| underdog|a22ef5bc-9d9e-46ae-9837-be37e361cecc | underdog | Chuba Hubbard | Receiving Yards | under | 0.05951438839462142 | 2026-11-08T06:01:51Z | 2026-11-08T18:00:00Z |
| underdog|78f92e19-5c31-4d49-a704-dea3e1ea7994 | underdog | Foster Moreau | Receptions | over | 0.05932154173705445 | 2026-11-05T12:22:13Z | 2026-11-08T21:05:00Z |
| underdog|de5a0bd7-b8b5-4b22-a054-258960283e42 | underdog | Breece Hall | Rush Yards | under | 0.05905485091136442 | 2026-11-08T06:01:51Z | 2026-11-08T18:00:00Z |
| underdog|a10e90f9-892e-489b-87e7-98258489a4ec | underdog | Chig Okonkwo | Receptions | under | 0.05901702938378406 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|c40f88c2-ee56-4915-be33-642988c74174 | underdog | Nik Bonitto | Sacks | over | 0.05880767797837183 | 2026-11-08T15:09:02Z | 2026-11-08T18:00:00Z |
| underdog|464fbf32-ce38-4c8f-bc70-190cf5d64c92 | underdog | MarShawn Lloyd | Receptions | under | 0.05868983465783262 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| prizepicks|16718559 | prizepicks | Travis Kelce | Rec Targets | under | 0.058686248860410406 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|5c1dad6e-619c-4575-9b10-738e17d39df7 | underdog | Ashton Jeanty | Receiving Yards | under | 0.05850227908119554 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|d146dfb3-fcb5-4654-a1f6-64215170adeb | underdog | Jessica Pegula | Double Faults | under | 0.05846688292835567 | 2026-11-05T12:22:13Z | 2026-11-08T21:10:00Z |
| underdog|8a748e05-956a-4a40-a6dc-c7788188b33f | underdog | Carson Wentz | Pass TDs | under | 0.058336194057320934 | 2026-11-05T22:06:44Z | 2026-11-10T01:15:00Z |
| prizepicks|16764331 | prizepicks | Keenan Allen | Rec Targets | under | 0.05809862236222918 | 2026-11-07T05:59:57Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|089ce83f-49f9-46ad-83c1-06b27856f11e | underdog | Tyler Shough | Pass TDs | under | 0.0579713928349842 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|94b26160-85f3-4b0e-a636-0a205a4a8a14 | underdog | Omarion Hampton | Rush + Rec Yards | under | 0.057685561031392885 | 2026-11-05T22:06:44Z | 2026-11-08T21:05:00Z |
| underdog|d02386e9-a6be-491a-b11c-0db9561342f3 | underdog | Omarion Hampton | Rush Yards | under | 0.0574974439645306 | 2026-11-05T22:06:44Z | 2026-11-08T21:05:00Z |
| underdog|623fe967-1a3e-408f-b0cb-0bf7da802b8a | underdog | Dak Prescott | Rush Yards | over | 0.0570102313442149 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| prizepicks|16779728 | prizepicks | Darius Cooper | Rec Targets | under | 0.05682751553763188 | 2026-11-08T06:01:51Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|339dfeab-cb61-44a6-9848-fa07b1efb7d6 | underdog | Isaiah Likely | Receiving Yards | under | 0.056810368159812774 | 2026-11-06T16:02:47Z | 2026-11-08T18:00:00Z |
| underdog|b094236c-ba86-4187-9f50-dfd372652b8b | underdog | Tre Tucker | Receptions | under | 0.05656143515129497 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|befbd56b-e648-4437-a050-c9ecb32ce65a | underdog | Corey Kiner | Rush + Rec Yards | under | 0.05651284215717434 | 2026-11-06T06:34:07Z | 2026-11-08T21:25:00Z |
| underdog|2cf795d7-7279-4cdf-9ea4-10556bd4239d | underdog | Kenyon Sadiq | Receptions | over | 0.056179967492667515 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| underdog|c552c9c9-592c-4f2a-96df-9a5186ec5288 | underdog | Jordan Watkins | Receiving Yards | under | 0.055954042538513216 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|48603add-d136-41df-b578-2323b8a1caa7 | underdog | Rome Odunze | Receptions | under | 0.05570918963942184 | 2026-11-04T12:10:41Z | 2026-11-09T01:20:00Z |
| prizepicks|16719193 | prizepicks | Rachaad White | Rec Targets | under | 0.055479385567673956 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|3c4aee76-fb32-4603-82d0-81351387b1e1 | underdog | Kalif Raymond | Receptions | under | 0.05532157679971539 | 2026-11-05T12:22:13Z | 2026-11-09T01:20:00Z |
| underdog|6298df95-6fe5-4a45-9901-b7bac37798c9 | underdog | Harold Fannin | Receiving Yards | under | 0.05517446409123983 | 2026-11-08T15:09:02Z | 2026-11-08T18:00:00Z |
| underdog|2e9a220f-7272-467e-b8e3-61ae45f85737 | underdog | Kenneth Walker III | Receiving Yards | under | 0.05507859411436211 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|19a672f3-50fe-4033-813c-78daf721de03 | underdog | Mike Washington | Rush Yards | under | 0.05471570014322025 | 2026-11-05T22:06:44Z | 2026-11-08T21:25:00Z |
| underdog|844d8994-eb1a-4135-917e-a68c00abf5fd | underdog | Tre' Harris | Receptions | under | 0.05470210954117727 | 2026-11-05T12:22:13Z | 2026-11-08T21:05:00Z |
| underdog|57907b2f-4a94-41a7-abb1-1393b01de777 | underdog | Mack Hollins | Receiving Yards | under | 0.05441456476566975 | 2026-11-08T15:09:02Z | 2026-11-08T21:25:00Z |
| prizepicks|16577036 | prizepicks | KC Concepcion Jr. | Rec Yards | under | 0.054101039282902996 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|1c2cde05-b6d7-4474-9d9e-8f9b3062e070 | underdog | Puka Nacua | Receptions | under | 0.05380728482585917 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|1f6ec128-0f98-4fab-b889-6fa33628a38b | underdog | Reggie Virgil | Receptions | under | 0.053005643668652125 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|5d4a6a94-4490-4488-8f26-0d4ccba55e0b | underdog | Savion Williams | Receiving Yards | under | 0.0525122155374117 | 2026-11-05T22:06:44Z | 2026-11-08T21:25:00Z |
| underdog|f4af8d61-8588-4d80-ac8d-fd8686a33979 | underdog | Malik Willis | Rush Yards | under | 0.052470845197019944 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|94778805-8555-4a67-807c-f8d41fd8a493 | underdog | Devin Singletary | Receptions | under | 0.05222811479089262 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|7c09637f-ba5b-48d9-a7b4-45cc01362313 | underdog | Justin Herbert | Rush Yards | under | 0.05178516711907766 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| prizepicks|16718497 | prizepicks | DJ Moore | Rec Targets | under | 0.051713641503083774 | 2026-11-05T22:06:44Z | 2026-11-09T20:15:00.000-05:00 |
| underdog|2c7f04e3-5df3-4a7c-b23f-467ddcc56597 | underdog | Felix Anudike-Uzomah | Sacks | over | 0.05076321889237018 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| prizepicks|16718517 | prizepicks | D'Andre Swift | Rec Targets | under | 0.0506216499863863 | 2026-11-05T22:06:44Z | 2026-11-08T20:20:00.000-05:00 |
| underdog|b4bf9f2b-e849-446b-a805-eda4d01af7be | underdog | Khalil Shakir | Receiving Yards | under | 0.05058312311415858 | 2026-11-04T12:10:41Z | 2026-11-10T01:15:00Z |
| underdog|cc6e5df1-5a0b-4ad2-972e-574952cbd39c | underdog | Tez Johnson | Receptions | over | 0.050436099256353284 | 2026-11-05T22:06:44Z | 2026-11-09T01:20:00Z |
| prizepicks|16747852 | prizepicks | Adonai Mitchell | Rec Targets | under | 0.050348304928793275 | 2026-11-07T05:59:57Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|306d32c9-76be-44a5-b65c-2d983b4ebc2f | underdog | Ashton Jeanty | Rush + Rec Yards | under | 0.05021547727948117 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| prizepicks|16719165 | prizepicks | Tre' Harris | Rec Targets | under | 0.050059523885883084 | 2026-11-05T22:06:44Z | 2026-11-08T16:05:00.000-05:00 |
| prizepicks|16718528 | prizepicks | Harold Fannin Jr. | Rec Targets | under | 0.05005687630552147 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|e0bc863f-aad7-4457-ae95-0614baf0c40d | underdog | Tetairoa McMillan | Receiving Yards | under | 0.05000311569825844 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| prizepicks|16764330 | prizepicks | Josh Downs | Rec Targets | under | 0.049962199665539164 | 2026-11-07T05:59:57Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|baa91d86-f682-4be6-b563-5276f85cf08e | underdog | Laquon Treadwell | Receptions | over | 0.04989017476712326 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|807c529e-31ff-4c65-9ac7-c60639f1a1f4 | underdog | Jayden Daniels | Rush Yards | under | 0.049059514309005126 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| prizepicks|16577037 | prizepicks | Chris Olave | Rec Yards | under | 0.04898251964490763 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|0e309daa-2938-4ba3-bfed-2478a9165635 | underdog | Sheldon Rankins | Sacks | over | 0.04891440650428508 | 2026-11-06T16:02:47Z | 2026-11-08T21:05:00Z |
| underdog|076c3eea-9331-4033-a108-3edf0279b36a | underdog | Ty Johnson | Receiving Yards | over | 0.048848215340260515 | 2026-11-07T05:59:57Z | 2026-11-10T01:15:00Z |
| underdog|f846cfba-c825-4e6b-aac9-0975e8c6604a | underdog | Kayshon Boutte | Receptions | over | 0.04870573326693556 | 2026-11-05T12:22:13Z | 2026-11-08T21:05:00Z |
| prizepicks|16718501 | prizepicks | James Cook III | Rec Targets | under | 0.04803584807788108 | 2026-11-05T22:06:44Z | 2026-11-09T20:15:00.000-05:00 |
| underdog|af9d31c5-4093-48e5-9c73-16834bfcafca | underdog | Kyle Williams | Receptions | under | 0.04785175956387744 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| prizepicks|16718533 | prizepicks | Ryan Flournoy | Rec Targets | under | 0.04782445339134278 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|3a32e19a-0fef-4030-8ab3-2d408c35ef7c | underdog | Roschon Johnson | Rush Yards | under | 0.04778124403200101 | 2026-11-06T16:02:47Z | 2026-11-09T01:20:00Z |
| prizepicks|16567035 | prizepicks | Jordan Love | Pass TDs | under | 0.04710112679060341 | 2026-11-04T12:10:41Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|8d98abf4-bc5e-4549-90db-f4eca6824ba0 | underdog | Bucky Irving | Rush + Rec Yards | under | 0.04692066418821539 | 2026-11-05T12:22:13Z | 2026-11-09T01:20:00Z |
| underdog|c31e50a6-b4e5-4af9-ac64-d81b415e67e7 | underdog | Eli Stowers | Receptions | under | 0.04667380971321278 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| prizepicks|16779732 | prizepicks | Tory Horton | Rec Targets | under | 0.04665988777898644 | 2026-11-08T06:01:51Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|3f83003e-b176-4542-8450-1bfb48461403 | underdog | Jerry Jeudy | Receiving Yards | over | 0.04664839040468083 | 2026-11-08T15:09:02Z | 2026-11-08T18:00:00Z |
| underdog|910cd28d-adbb-4735-b415-f8c186adcc63 | underdog | Noah Gray | Receiving Yards | over | 0.04596747569131443 | 2026-11-08T15:09:02Z | 2026-11-08T18:00:00Z |
| prizepicks|16719177 | prizepicks | Alvin Kamara | Rec Targets | under | 0.04592092233766798 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|9c7c7b03-922c-4480-a4d2-0180ec763c4e | underdog | Marta Kostyuk | Double Faults | under | 0.045559516738841954 | 2026-11-08T15:09:02Z | 2026-11-08T20:00:00Z |
| prizepicks|16722941 | prizepicks | Emeka Egbuka | Recs | under | 0.04538182348359732 | 2026-11-06T06:34:07Z | 2026-11-08T20:20:00.000-05:00 |
| underdog|76f3f1d7-5244-48ed-80c8-4f59cff15006 | underdog | George Karlaftis | Sacks | under | 0.04533238139975149 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|4de62797-41a0-4d69-977b-0286517b1b34 | underdog | Alvin Kamara | Receptions | under | 0.0452076759340746 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|7a72d0be-60ae-4376-8aa1-07e785aab859 | underdog | Jonathan Taylor | Receptions | under | 0.04508721237534341 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|e08d4f66-a7e7-4286-8e10-12e06db8fcac | underdog | James Cook | Receiving Yards | over | 0.04487381857719097 | 2026-11-08T15:09:02Z | 2026-11-10T01:15:00Z |
| underdog|51e7af2b-f9a1-43ea-aa78-584f372553e2 | underdog | Trey Smack | Kicking Points | under | 0.04455434973971151 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| underdog|ea125837-d29b-4284-a90d-fee5aa2a9a96 | underdog | Chris Godwin | Receptions | under | 0.04434472697680247 | 2026-11-05T12:22:13Z | 2026-11-09T01:20:00Z |
| underdog|e5d081ab-9efa-43d3-bfb8-a43e2d593f85 | underdog | Drake Maye | Pass TDs | under | 0.04430737897190651 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|f30dd4e7-dacd-455c-8ed4-95be1fa5e74c | underdog | Karolina Muchova | Double Faults | under | 0.044153512874079426 | 2026-11-05T12:22:13Z | 2026-11-09T20:00:00Z |
| prizepicks|16718543 | prizepicks | Jameson Williams | Rec Targets | under | 0.04401078613436993 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|9815d49d-2af1-48c2-b6e4-cbe7c87349ac | underdog | Emmett Johnson | Receiving Yards | over | 0.043799798929959555 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|1075e7a4-7835-48a5-a2db-a78bbb0c36aa | underdog | Kalif Raymond | Receiving Yards | over | 0.04323294702184943 | 2026-11-05T12:22:13Z | 2026-11-09T01:20:00Z |
| prizepicks|16557917 | prizepicks | Jordan Love | Rush Yards | under | 0.0431179313386405 | 2026-11-03T02:21:46Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|fe7a85f2-c21c-4535-88b9-b246e6af4d70 | underdog | Jason Sanders | FG Made | over | 0.04309576984353114 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| underdog|ef68a74d-d7a0-476d-bf6c-f7f526abd93c | underdog | Tyler Shough | Rush Yards | under | 0.042790287547065375 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|91f4a8ca-8e1b-4038-a81f-33103051637f | underdog | Darnell Mooney | Receptions | over | 0.04273058695676135 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|3b4d0796-2e1f-4eab-ad1f-caf2c6b0c704 | underdog | Drew Lock | Rush Yards | under | 0.042410547162090584 | 2026-11-08T06:01:51Z | 2026-11-08T21:25:00Z |
| underdog|bce41d64-aa62-40b6-aed3-71790cf51f35 | underdog | Dallas Turner | Sacks | over | 0.04224694817072938 | 2026-11-07T05:59:57Z | 2026-11-10T01:15:00Z |
| underdog|085c90df-5803-45fc-ac14-b28618abec44 | underdog | Aaron Jones | Receiving Yards | over | 0.04183150381663703 | 2026-11-05T22:06:44Z | 2026-11-10T01:15:00Z |
| underdog|25efe389-0f9d-4419-983d-72da4b9d01ba | underdog | Cyrus Allen | Receptions | under | 0.041551213577819546 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| prizepicks|16667335 | prizepicks | Puka Nacua | Recs | under | 0.04136046632707657 | 2026-11-05T12:22:13Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|02cf2783-116d-4d08-a6ef-89bfcda4941e | underdog | Jalen Nailor | Receptions | under | 0.04129568937899364 | 2026-11-07T05:59:57Z | 2026-11-08T21:25:00Z |
| underdog|127ded5d-257a-4c2a-bb25-88e0bd0debad | underdog | Jordan Love | Rush Yards | under | 0.04127202084950954 | 2026-11-04T12:10:41Z | 2026-11-08T21:25:00Z |
| prizepicks|16718546 | prizepicks | Matthew Golden | Rec Targets | under | 0.04103027600826581 | 2026-11-05T22:06:44Z | 2026-11-08T16:25:00.000-05:00 |
| underdog|d63b8166-7ed3-4784-a290-53c755df307b | underdog | Rhamondre Stevenson | Receiving Yards | under | 0.04073261149509677 | 2026-11-06T06:34:07Z | 2026-11-08T21:25:00Z |
| prizepicks|16577047 | prizepicks | Ryan Flournoy | Rec Yards | under | 0.04046234355837319 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|3bd01e57-9195-4088-a564-fe508f2d81f0 | underdog | Isaiah Likely | Receptions | under | 0.039903034181366426 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| prizepicks|16577038 | prizepicks | Travis Kelce | Rec Yards | under | 0.039492224251563846 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|cefb0596-2c7e-431b-8408-7a1ed12d8db4 | underdog | Bryce Young | Pass TDs | under | 0.039094010660283285 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| prizepicks|16764324 | prizepicks | Ty Johnson | Rec Targets | under | 0.03893224664571926 | 2026-11-07T05:59:57Z | 2026-11-09T20:15:00.000-05:00 |
| prizepicks|16718511 | prizepicks | Jalen Coker | Rec Targets | under | 0.03878118544429088 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| prizepicks|16779127 | prizepicks | Matthew Stafford | Fantasy Score | under | 0.03870698651267224 | 2026-11-08T06:01:51Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|d1d3e66e-276b-43d4-9e06-fe5ed3964b6c | underdog | Geno Smith | Pass TDs | over | 0.038346590420210214 | 2026-11-03T02:21:46Z | 2026-11-08T18:00:00Z |
| prizepicks|16718513 | prizepicks | Tommy Tremble | Rec Targets | under | 0.038026067477504255 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|24135e0b-bdb0-493a-8b08-4ef9d8baaddd | underdog | Omarion Hampton | Receiving Yards | over | 0.0379426659535288 | 2026-11-05T22:06:44Z | 2026-11-08T21:05:00Z |
| prizepicks|16719172 | prizepicks | Ollie Gordon II | Rec Targets | under | 0.03764949184168209 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|c9385892-f356-4349-8fb6-7d5113bc5518 | underdog | Kimani Vidal | Rush Yards | under | 0.037649407143210745 | 2026-11-05T22:06:44Z | 2026-11-08T21:05:00Z |
| underdog|fdb2283d-2b96-4d98-9749-7be1a9524421 | underdog | Eli Stowers | Receiving Yards | over | 0.03763479754869259 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|10c2407f-5738-4e43-8822-e60a7494336d | underdog | Devaughn Vele | Receiving Yards | under | 0.03754483168355782 | 2026-11-06T06:34:07Z | 2026-11-08T18:00:00Z |
| prizepicks|16763490 | prizepicks | Josh Allen | Pass+Rush+Rec TDs | under | 0.037410921153935406 | 2026-11-07T05:59:57Z | 2026-11-09T20:15:00.000-05:00 |
| underdog|4a60e445-01a6-4494-af71-30be934f5ff2 | underdog | Jalen Royals | Receptions | over | 0.03740054606007237 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|d654da8a-dcae-477e-b52e-6a2ec419e69b | underdog | Troy Franklin | Receiving Yards | over | 0.037228791049771504 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| prizepicks|16718503 | prizepicks | Keon Coleman | Rec Targets | under | 0.037191314735347314 | 2026-11-05T22:06:44Z | 2026-11-09T20:15:00.000-05:00 |
| underdog|814cd76d-0d09-43b6-b742-bc1186e15b37 | underdog | Alvin Kamara | Receiving Yards | under | 0.03714854856919103 | 2026-11-08T06:01:51Z | 2026-11-08T18:00:00Z |
| underdog|417cba44-2483-40b8-9dca-cb37554b2e7c | underdog | Alim McNeill | Sacks | over | 0.03694453187853869 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|0bfdaf51-6b45-47cf-841f-e2ef80666205 | underdog | Jalen Redmond | Sacks | under | 0.036716350712867496 | 2026-11-08T06:01:51Z | 2026-11-10T01:15:00Z |
| underdog|6c714eaf-7d73-41a2-a920-202ca837066f | underdog | Corey Kiner | Rush Yards | under | 0.036586404611637424 | 2026-11-06T06:34:07Z | 2026-11-08T21:25:00Z |
| underdog|119f4d77-645c-42cd-9e5d-3c3aa99ea03d | underdog | Cameron Dicker | FG Made | under | 0.03597583144986216 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|6125e755-6fb9-4db7-bb7b-9a6a3e470fee | underdog | Breece Hall | Receptions | over | 0.03592281448134871 | 2026-11-08T15:09:02Z | 2026-11-08T18:00:00Z |
| underdog|865227cf-17df-4e89-9c98-4311b47f982a | underdog | Tetairoa McMillan | Receptions | under | 0.03583202783628714 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| prizepicks|16576405 | prizepicks | Puka Nacua | Rush Yards | over | 0.035802440511908284 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|2f083c55-dfe0-4021-bc6a-5e7f16540cf5 | underdog | Ryan Fitzgerald | FG Made | under | 0.035264256773103186 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|d956ff35-5891-430d-a052-ebaf442bf737 | underdog | Spencer Shrader | Kicking Points | under | 0.03493687122664446 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|d54bca32-8097-4be0-8aa0-b936d30cfb9c | underdog | Caleb Williams | Rush Yards | under | 0.03491962218449696 | 2026-11-08T15:09:02Z | 2026-11-09T01:20:00Z |
| underdog|4d2cb96e-0fcb-4c58-9b4e-82c1c8ec4298 | underdog | Chris Jones | Sacks | under | 0.03486791199846795 | 2026-11-08T06:01:51Z | 2026-11-08T18:00:00Z |
| underdog|642b6aa4-d8ad-47ca-a6e2-02bf1db1abde | underdog | Rhamondre Stevenson | Receptions | under | 0.03473410197552751 | 2026-11-03T02:21:46Z | 2026-11-08T21:25:00Z |
| underdog|b94e3cd0-3dff-4a4e-b5ec-e40578cb5f0a | underdog | Rashan Gary | Sacks | over | 0.03464923685125493 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| prizepicks|16557908 | prizepicks | Patrick Mahomes | Rush Yards | under | 0.034534369510793694 | 2026-11-03T02:21:46Z | 2026-11-08T13:00:00.000-05:00 |
| prizepicks|16764327 | prizepicks | Pat Bryant | Rec Targets | under | 0.03453011724848243 | 2026-11-07T05:59:57Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|55ddfc8b-cc00-4a5c-8b38-c25c73c91f11 | underdog | Noah Fant | Receptions | under | 0.03452368152175711 | 2026-11-08T06:01:51Z | 2026-11-08T18:00:00Z |
| underdog|66b37aff-aa69-48ba-984e-2a3c3e131cd4 | underdog | Tommy Tremble | Receptions | over | 0.03430222685481554 | 2026-11-04T12:10:41Z | 2026-11-08T18:00:00Z |
| underdog|f35bd4b7-7903-4753-9b3a-bdec441abb92 | underdog | Tuli Tuipulotu | Sacks | over | 0.03417794141333974 | 2026-11-08T06:01:51Z | 2026-11-08T21:05:00Z |
| underdog|a7cebf17-ff00-4409-a5bc-8ce129dd77a1 | underdog | Quinshon Judkins | Receptions | under | 0.03394034349269137 | 2026-11-05T22:06:44Z | 2026-11-08T18:00:00Z |
| underdog|b4164f31-211e-44a6-819f-02c4a0dae617 | underdog | Xavier Worthy | Receptions | under | 0.033937644307545756 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|dd559c53-2b12-4f84-87a2-a48db1199969 | underdog | Matt Gay | Kicking Points | over | 0.033883190773937144 | 2026-11-08T15:09:02Z | 2026-11-08T21:25:00Z |
| underdog|caf09287-ff2b-436f-81b7-c0461c306d78 | underdog | Braelon Allen | Rush Yards | over | 0.03375722225668776 | 2026-11-08T06:01:51Z | 2026-11-08T18:00:00Z |
| underdog|d61c807a-66b1-4a4f-9972-cba41bc45ee6 | underdog | Javonte Williams | Receiving Yards | over | 0.03365125001838698 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|c326b335-e702-421f-9f11-eec8ab8fdfaa | underdog | Dalton Schultz | Receiving Yards | under | 0.03359570617331076 | 2026-11-04T12:10:41Z | 2026-11-08T21:05:00Z |
| underdog|fe1331bb-39d1-4681-8d5a-f9d951e31392 | underdog | KC Concepcion | Receptions | under | 0.033021846340560934 | 2026-11-03T11:59:28Z | 2026-11-08T18:00:00Z |
| underdog|8a29eea1-d895-407b-8658-b0db6edb5801 | underdog | Nate Adkins | Receptions | over | 0.03282306378556943 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| underdog|13caba41-6c85-4e45-92ad-9a617d35c20f | underdog | Dylan Sampson | Receiving Yards | under | 0.032711018039744744 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|b9c1a1a8-01ac-40a2-baab-d2706b32bde2 | underdog | Kyren Williams | Receptions | under | 0.032587481000593055 | 2026-11-05T12:22:13Z | 2026-11-08T18:00:00Z |
| prizepicks|16719169 | prizepicks | Chris Bell | Rec Targets | under | 0.032460366105138805 | 2026-11-05T22:06:44Z | 2026-11-08T13:00:00.000-05:00 |
| underdog|041b30d5-fdc3-4489-bb29-a89e6667b68d | underdog | Charlie Kolar | Receiving Yards | under | 0.03242651143957387 | 2026-11-05T12:22:13Z | 2026-11-08T21:05:00Z |
| underdog|0f008320-92cf-4f41-8668-21ea1cfb4f85 | underdog | Corey Kiner | Receptions | under | 0.03236272786970029 | 2026-11-06T16:02:47Z | 2026-11-08T21:25:00Z |
| underdog|efb57ef9-cd9e-4c17-8c69-4ca008e502a4 | underdog | Sione Vaki | Rush Yards | under | 0.03235069862327555 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|2cfb2c38-eea2-4115-8859-b21897508d6e | underdog | Michael Mayer | Receptions | under | 0.03208971752720258 | 2026-11-05T12:22:13Z | 2026-11-08T21:25:00Z |
| underdog|e458b44f-8472-4296-a09e-bc9842ae3727 | underdog | Austin Ekeler | Receptions | under | 0.03201422929910369 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
| underdog|07b4e0a9-97bd-4458-8a02-81a0f4ada5d4 | underdog | Xavier Hutchinson | Receiving Yards | over | 0.03157278603746505 | 2026-11-07T05:59:57Z | 2026-11-08T21:05:00Z |
| underdog|29548098-f738-43bd-b997-aebc834c752e | underdog | Javonte Williams | Receptions | under | 0.030300543156345672 | 2026-11-08T06:01:51Z | 2026-11-08T18:00:00Z |
| underdog|b26ca2bb-149c-48e8-a968-913ca91b91fe | underdog | Jeremiah Trotter | Sacks | under | 0.030078365485903147 | 2026-11-07T05:59:57Z | 2026-11-08T18:00:00Z |
