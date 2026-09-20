# Pipeline Digest -- 2026-09-20T22:23:24Z

## Run summary
- Ingestion: 10515 rows (PrizePicks OK, Underdog OK)
- Estimation: 10515 rows estimated (from 10515 ingested props)
- CLV logging: 48 newly flagged, 0 newly closed, 146 still open (81449 total ever logged)

## Currently open flags
Sizing is a manual step (sizing_engine.py, Session 2.6) -- this table is what to scan to pick a pair worth sizing.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_edge | first_flagged_at | game_start_time |
|---|---|---|---|---|---|---|---|
| prizepicks|15020920 | prizepicks | Sam LaPorta | Rec Yards | under | 0.4999998908997208 | 2026-09-19T04:39:42Z | 2026-09-27T13:00:00.000-04:00 |
| prizepicks|15020919 | prizepicks | Jameson Williams | Rec Yards | under | 0.4984267311890689 | 2026-09-19T04:39:42Z | 2026-09-27T13:00:00.000-04:00 |
| underdog|25a81783-971e-45dd-bd24-021ebe143408 | underdog | Pete Alonso | RBIs | over | 0.3839341692789968 | 2026-09-20T22:27:50Z | 2026-09-20T23:20:00Z |
| underdog|89b6ab3a-b7b6-41fd-84c8-04b76440ddbd | underdog | Kaitlin Quevedo | Double Faults | under | 0.251826584125199 | 2026-09-20T18:49:37Z | 2026-09-20T18:50:00Z |
| prizepicks|13975919 | prizepicks | Jayson Tatum | Pts+Asts | under | 0.2451279480496665 | 2026-09-12T11:28:56Z | 2026-10-20T15:10:00.000-04:00 |
| prizepicks|13975925 | prizepicks | Jayson Tatum | Pts+Rebs | under | 0.2442060163021608 | 2026-09-12T11:28:56Z | 2026-10-20T15:10:00.000-04:00 |
| prizepicks|13952668 | prizepicks | LeBron James | Points | over | 0.2397149568250941 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| prizepicks|14745308 | prizepicks | Matthew Stafford | Rush Yards | over | 0.2309141879479694 | 2026-09-11T16:24:54Z | 2026-09-21T20:15:00.000-04:00 |
| prizepicks|15073126 | prizepicks | Lanlana Tararudee | Break Points Won | under | 0.2280858421818844 | 2026-09-20T18:49:37Z | 2026-09-20T23:00:00.000-04:00 |
| prizepicks|13975988 | prizepicks | LeBron James | Pts+Rebs | over | 0.2247745517150446 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| prizepicks|13952667 | prizepicks | Jalen Brunson | Points | over | 0.2135813857285506 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| prizepicks|14745311 | prizepicks | Matthew Stafford | Pass Yards | over | 0.1999038485589053 | 2026-09-11T16:24:54Z | 2026-09-21T20:15:00.000-04:00 |
| prizepicks|15020918 | prizepicks | Amon-Ra St. Brown | Rec Yards | under | 0.1912444819607222 | 2026-09-19T04:39:42Z | 2026-09-27T13:00:00.000-04:00 |
| underdog|b628bf1b-5bd7-4957-bd4c-ced5615857d3 | underdog | Gunnar Henderson | Runs | over | 0.1900617186263649 | 2026-09-20T18:49:37Z | 2026-09-20T23:20:00Z |
| prizepicks|13975959 | prizepicks | Jalen Brunson | Pts+Rebs | over | 0.1892442263984233 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| prizepicks|13975931 | prizepicks | Jayson Tatum | PRA | under | 0.1859948657142129 | 2026-09-12T11:28:56Z | 2026-10-20T15:10:00.000-04:00 |
| underdog|e522f682-75fa-40e9-abd7-47543c664ac5 | underdog | Coby Mayo | Runs | over | 0.1813953488372093 | 2026-09-20T18:49:37Z | 2026-09-20T23:20:00Z |
| underdog|fe719bbc-dbff-4446-af96-cc905f2ad80e | underdog | Colton Cowser | Total Bases | over | 0.1810801668733792 | 2026-09-20T18:49:37Z | 2026-09-20T23:20:00Z |
| prizepicks|13975984 | prizepicks | LeBron James | Pts+Asts | over | 0.1791375054527176 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|126ebc9e-1d4a-4c32-abbf-b08537e203de | underdog | Pete Alonso | Runs | over | 0.1771991108288347 | 2026-09-20T22:27:50Z | 2026-09-20T23:20:00Z |
| underdog|6d36a2b7-c636-44e7-a5c1-be05981bc1cb | underdog | Jeremiah Jackson | RBIs | over | 0.1721460514030173 | 2026-09-20T22:27:50Z | 2026-09-20T23:20:00Z |
| underdog|bfbc4ae0-0079-46a4-9cbc-aa3ba52a04b1 | underdog | Jake Bauers | Batter Walks | over | 0.1714285714285713 | 2026-09-20T18:49:37Z | 2026-09-20T23:20:00Z |
| underdog|fc0253d6-50ee-46a2-bcf2-44f57e862683 | underdog | Brice Turang | Batter Walks | over | 0.1714285714285713 | 2026-09-20T18:49:37Z | 2026-09-20T23:20:00Z |
| prizepicks|13975992 | prizepicks | LeBron James | PRA | over | 0.1710160714309272 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|c4a51be0-a2b8-4c01-bfb0-78c2098605d9 | underdog | Leody Taveras | Total Bases | over | 0.1635500779147187 | 2026-09-20T22:27:50Z | 2026-09-20T23:20:00Z |
| prizepicks|13975964 | prizepicks | Jalen Brunson | PRA | over | 0.1594536543882333 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| prizepicks|13975883 | prizepicks | Cade Cunningham | Assists | under | 0.1583653539789251 | 2026-09-12T11:28:56Z | 2026-10-20T15:10:00.000-04:00 |
| prizepicks|15072771 | prizepicks | Maja Chwalinska | Break Points Won | under | 0.156393217977166 | 2026-09-20T18:49:37Z | 2026-09-21T01:40:00.000-04:00 |
| prizepicks|14745233 | prizepicks | Puka Nacua | Rec Yards | over | 0.1539916674633568 | 2026-09-11T16:24:54Z | 2026-09-21T20:15:00.000-04:00 |
| prizepicks|13975900 | prizepicks | Cade Cunningham | PRA | under | 0.1531773965770679 | 2026-09-12T11:28:56Z | 2026-10-20T15:10:00.000-04:00 |
| prizepicks|13975955 | prizepicks | Jalen Brunson | Pts+Asts | over | 0.1457490982774579 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|5fbcdd84-1fd1-4b75-a1a0-8b6a74565f19 | underdog | Coby Mayo | Total Bases | over | 0.1428163544997716 | 2026-09-20T18:49:37Z | 2026-09-20T23:20:00Z |
| underdog|1768786d-b0ed-4585-8ecb-514b41d133ef | underdog | Jackson Chourio | Total Bases | over | 0.1402638403427669 | 2026-09-20T22:27:50Z | 2026-09-20T23:20:00Z |
| prizepicks|13976081 | prizepicks | Jalen Brunson | Rebounds | over | 0.1400370452709755 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|a49d7058-4be8-483a-8e1a-1be009b28a2e | underdog | Garrett Mitchell | Runs | over | 0.139078887368901 | 2026-09-20T22:27:50Z | 2026-09-20T23:20:00Z |
| underdog|65cfe6c3-5608-4514-a298-6941c78de969 | underdog | Coby Mayo | RBIs | over | 0.1355192146014698 | 2026-09-20T22:27:50Z | 2026-09-20T23:20:00Z |
| prizepicks|15020924 | prizepicks | James Cook III | Rush Yards | under | 0.1353753051756937 | 2026-09-19T04:39:42Z | 2026-09-27T13:00:00.000-04:00 |
| prizepicks|15020921 | prizepicks | Jahmyr Gibbs | Rec Yards | under | 0.1333703389598928 | 2026-09-19T04:39:42Z | 2026-09-27T13:00:00.000-04:00 |
| underdog|755d6490-d819-4747-8f1c-26fb7ef6de4a | underdog | Jacob Misiorowski | Earned Runs Allowed | over | 0.1318960640248991 | 2026-09-20T22:27:50Z | 2026-09-20T23:20:00Z |
| underdog|b7b60f9d-592b-49dd-87fd-76381b3ea7a9 | underdog | Christian Yelich | Runs | over | 0.1309907586503332 | 2026-09-20T18:49:37Z | 2026-09-20T23:20:00Z |
| underdog|25a2493a-6634-4ce2-9fa6-732019c1d4a5 | underdog | Brice Turang | RBIs | over | 0.1306423852090389 | 2026-09-20T18:49:37Z | 2026-09-20T23:20:00Z |
| prizepicks|13975891 | prizepicks | Cade Cunningham | Pts+Asts | under | 0.1301298534041951 | 2026-09-12T11:28:56Z | 2026-10-20T15:10:00.000-04:00 |
| underdog|170e75b8-030b-418e-b4c2-64b6a96385c6 | underdog | Samuel Basallo | RBIs | over | 0.1290781305548717 | 2026-09-20T22:27:50Z | 2026-09-20T23:20:00Z |
| prizepicks|13975904 | prizepicks | Cade Cunningham | Rebs+Asts | under | 0.1276349180264445 | 2026-09-12T11:28:56Z | 2026-10-20T15:10:00.000-04:00 |
| underdog|7df6f464-8dc3-449a-8ea5-6c27996dbce2 | underdog | Leody Taveras | Runs | over | 0.12529374677595 | 2026-09-20T18:49:37Z | 2026-09-20T23:20:00Z |
| prizepicks|13976014 | prizepicks | Shai Gilgeous-Alexander | Pts+Rebs | under | 0.1235832751001789 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| underdog|ad7c7537-6987-44b1-82a8-2ce2a290689e | underdog | Carlos Narváez | Total Bases | over | 0.1226164079822613 | 2026-09-20T22:27:50Z | 2026-09-20T23:20:00Z |
| underdog|4d7adb04-2278-4c64-93a8-b0c1800ec0ea | underdog | Colton Cowser | Hits + Runs + RBIs | over | 0.1220987135203883 | 2026-09-20T18:49:37Z | 2026-09-20T23:20:00Z |
| prizepicks|13976082 | prizepicks | Shai Gilgeous-Alexander | Rebounds | under | 0.1216050430415754 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| prizepicks|13975945 | prizepicks | Jalen Brunson | Assists | under | 0.1210560575434291 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|166d4984-17fd-4913-9f3b-90bfa43cc6b4 | underdog | Colton Cowser | Hits | over | 0.1208529141453846 | 2026-09-20T18:49:37Z | 2026-09-20T23:20:00Z |
| underdog|666f893c-6f5b-4618-9d0c-fb6d4ab80134 | underdog | Pete Alonso | Hits + Runs + RBIs | over | 0.1203512790851769 | 2026-09-20T22:27:50Z | 2026-09-20T23:20:00Z |
| prizepicks|15020926 | prizepicks | Jahmyr Gibbs | Rush Yards | under | 0.1197756097336648 | 2026-09-19T04:39:42Z | 2026-09-27T13:00:00.000-04:00 |
| underdog|5faebea4-4718-4745-b606-8d10d6ed4d81 | underdog | Dylan Beavers | RBIs | over | 0.1193311036789298 | 2026-09-20T18:49:37Z | 2026-09-20T23:20:00Z |
| prizepicks|15039314 | prizepicks | Robin Montgomery | Total Games | over | 0.1188183128015181 | 2026-09-20T04:56:02Z | 2026-09-20T23:00:00.000-04:00 |
| prizepicks|15073137 | prizepicks | Magda Linette | Break Points Won | under | 0.1180779654629361 | 2026-09-20T18:49:37Z | 2026-09-21T02:10:00.000-04:00 |
| underdog|8ebf8410-5ceb-4b39-9350-eda82ca36577 | underdog | Polina Kudermetova | Double Faults | under | 0.117634722930922 | 2026-09-20T18:49:37Z | 2026-09-21T04:10:00Z |
| underdog|f8c366c0-5edf-40ea-aa37-e114d13fd594 | underdog | Carlos Narváez | Hits + Runs + RBIs | over | 0.116824951093588 | 2026-09-20T22:27:50Z | 2026-09-20T23:20:00Z |
| prizepicks|13976095 | prizepicks | Cade Cunningham | 3PTM | over | 0.1168098507846668 | 2026-09-12T11:28:56Z | 2026-10-20T15:10:00.000-04:00 |
| underdog|45e96c68-9995-44d1-ac83-5d6672770e16 | underdog | William Contreras | Runs | over | 0.1164061369228543 | 2026-09-20T18:49:37Z | 2026-09-20T23:20:00Z |
| underdog|45423149-50ae-4405-94d2-b17d13fd8979 | underdog | Jacob Misiorowski | Walks Allowed | over | 0.1147301369483729 | 2026-09-20T18:49:37Z | 2026-09-20T23:20:00Z |
| underdog|e9925e71-122c-4b49-9028-b943afaef6b6 | underdog | Pete Alonso | Total Bases | over | 0.1134453781512604 | 2026-09-20T18:49:37Z | 2026-09-20T23:20:00Z |
| underdog|4ce86dff-8686-41da-8c06-16f870cc819f | underdog | Brice Turang | Total Bases | over | 0.113339970134395 | 2026-09-20T22:27:50Z | 2026-09-20T23:20:00Z |
| underdog|b4b03f83-e1d3-4b34-8b97-e70f0f797932 | underdog | Leody Taveras | Hits | over | 0.1086502780322454 | 2026-09-20T18:49:37Z | 2026-09-20T23:20:00Z |
| prizepicks|15073131 | prizepicks | Kamilla Rakhimova | Break Points Won | under | 0.1037644317304841 | 2026-09-20T18:49:37Z | 2026-09-21T00:10:00.000-04:00 |
| prizepicks|13976040 | prizepicks | Victor Wembanyama | Pts+Asts | under | 0.1021735734863812 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| underdog|b626b643-f2b7-428a-a81f-177947866898 | underdog | Brandon Young | Earned Runs Allowed | under | 0.1007022964829303 | 2026-09-20T22:27:50Z | 2026-09-20T23:20:00Z |
| prizepicks|13975896 | prizepicks | Cade Cunningham | Pts+Rebs | under | 0.1002719704236944 | 2026-09-12T11:28:56Z | 2026-10-20T15:10:00.000-04:00 |
| underdog|d1ddf32e-6022-461f-b53a-ad2704209e0b | underdog | Dylan Beavers | Total Bases | over | 0.0994475138121546 | 2026-09-20T18:49:37Z | 2026-09-20T23:20:00Z |
| underdog|d5067f78-46f3-428c-b2d3-222c9c6a63f8 | underdog | Jeremiah Jackson | Total Bases | over | 0.0994475138121546 | 2026-09-20T22:27:50Z | 2026-09-20T23:20:00Z |
| underdog|a6cce16c-6d50-4ef5-9200-1bf235ac66cd | underdog | Samuel Basallo | Total Bases | over | 0.0994475138121546 | 2026-09-20T18:49:37Z | 2026-09-20T23:20:00Z |
| underdog|448fa8c1-9527-4a57-943a-337eeee6fa7a | underdog | Christian Yelich | Total Bases | over | 0.0978456373156402 | 2026-09-20T22:27:50Z | 2026-09-20T23:20:00Z |
| underdog|1f4fe333-51a5-46c7-8a5e-cf1e20858b7f | underdog | Leody Taveras | Batter Walks | over | 0.097604084838963 | 2026-09-20T22:27:50Z | 2026-09-20T23:20:00Z |
| prizepicks|15073129 | prizepicks | Katie Volynets | Break Points Won | under | 0.0961432684490362 | 2026-09-20T18:49:37Z | 2026-09-20T23:00:00.000-04:00 |
| underdog|2f56dd81-2400-494a-9de5-eb23a07ef71b | underdog | Garrett Mitchell | Batter Walks | over | 0.0961327180839375 | 2026-09-20T22:27:50Z | 2026-09-20T23:20:00Z |
| underdog|99e23f52-12b5-46c2-868d-145b14f4a19a | underdog | Brandon Young | Walks Allowed | under | 0.0957151776427044 | 2026-09-20T22:27:50Z | 2026-09-20T23:20:00Z |
| prizepicks|15072774 | prizepicks | Leylah Fernandez | Break Points Won | under | 0.0945781535059221 | 2026-09-20T18:49:37Z | 2026-09-21T06:30:00.000-04:00 |
| prizepicks|15043546 | prizepicks | Linda Fruhvirtova | 1st Set Total Games Won | over | 0.093062823732776 | 2026-09-20T04:56:02Z | 2026-09-20T23:00:00.000-04:00 |
| underdog|8ba300af-e60c-4549-9278-0f4493b468b5 | underdog | Coby Mayo | Hits | over | 0.0927472491662126 | 2026-09-20T18:49:37Z | 2026-09-20T23:20:00Z |
| prizepicks|15039952 | prizepicks | Yue Yuan | Total Games | over | 0.0926970873133662 | 2026-09-20T04:56:02Z | 2026-09-20T23:00:00.000-04:00 |
| underdog|5d7de2cf-49f0-445b-bad6-47858dea282c | underdog | William Contreras | RBIs | over | 0.0919776667646193 | 2026-09-20T22:27:50Z | 2026-09-20T23:20:00Z |
| underdog|1aa0001a-e9a4-4883-9c26-b83f6dfc6a11 | underdog | Jake Bauers | Total Bases | over | 0.088821892393321 | 2026-09-20T18:49:37Z | 2026-09-20T23:20:00Z |
| underdog|ecad93de-ea9f-476e-8766-d22e9b217ad8 | underdog | Cooper Pratt | RBIs | over | 0.0884866767219708 | 2026-09-20T22:27:50Z | 2026-09-20T23:20:00Z |
| underdog|019f732a-d703-4db6-8fad-411ee4d4e9c1 | underdog | Jake Bauers | Runs | over | 0.0879218788980364 | 2026-09-20T22:27:50Z | 2026-09-20T23:20:00Z |
| underdog|07f732a6-469b-4ad4-8cf9-be8b3071b776 | underdog | Leody Taveras | Hits + Runs + RBIs | over | 0.0878855575272699 | 2026-09-20T18:49:37Z | 2026-09-20T23:20:00Z |
| underdog|a2796a6f-e70a-4166-b59e-9badc5b7ac8d | underdog | Jackson Chourio | Runs | over | 0.0867768595041319 | 2026-09-20T18:49:37Z | 2026-09-20T23:20:00Z |
| underdog|3053ad6a-0b66-4677-933c-d478ae025902 | underdog | Brice Turang | Runs | over | 0.0867768595041319 | 2026-09-20T22:27:50Z | 2026-09-20T23:20:00Z |
| underdog|d9c51cb5-174a-45a9-91eb-5efb58479bb5 | underdog | Carlos Narváez | Hits | over | 0.0842708695011316 | 2026-09-20T22:27:50Z | 2026-09-20T23:20:00Z |
| underdog|03d03b15-42fc-4002-a582-112346996542 | underdog | Samuel Basallo | Hits | over | 0.084175821206152 | 2026-09-20T18:49:37Z | 2026-09-20T23:20:00Z |
| prizepicks|15020925 | prizepicks | Josh Allen | Rush Yards | under | 0.084024205820317 | 2026-09-19T04:39:42Z | 2026-09-27T13:00:00.000-04:00 |
| underdog|294bd585-876c-417f-bf09-75b8f224c215 | underdog | Dylan Beavers | Hits | over | 0.0834256872964591 | 2026-09-20T18:49:37Z | 2026-09-20T23:20:00Z |
| underdog|798b08ce-5f10-412c-ad93-5c6ccfebb080 | underdog | William Contreras | Batter Walks | over | 0.0828043211938969 | 2026-09-20T18:49:37Z | 2026-09-20T23:20:00Z |
| underdog|6590d057-b13e-4b4e-92ab-b5b9a85bdaec | underdog | Jackson Chourio | RBIs | over | 0.0815937015388285 | 2026-09-20T22:27:50Z | 2026-09-20T23:20:00Z |
| prizepicks|15066453 | prizepicks | Yue Yuan | Total Games | over | 0.0810151439258699 | 2026-09-20T18:49:37Z | 2026-09-21T01:00:00.000-04:00 |
| underdog|9d2982c9-a981-45d9-8e2b-8a62798a7f54 | underdog | Christian Yelich | Batter Walks | under | 0.0805194805194805 | 2026-09-20T22:27:50Z | 2026-09-20T23:20:00Z |
| underdog|1c31988f-4b60-407f-8004-91839a6d5d68 | underdog | William Contreras | Total Bases | over | 0.0804676201189138 | 2026-09-20T18:49:37Z | 2026-09-20T23:20:00Z |
| underdog|96b58e07-3be4-4eb7-aae6-f9fd5b15e5f0 | underdog | Gunnar Henderson | Hits | over | 0.0798946936308806 | 2026-09-20T22:27:50Z | 2026-09-20T23:20:00Z |
| underdog|4874c00e-5254-437f-97e1-4224d86f5e1f | underdog | Pete Alonso | Hits | over | 0.0789011566502864 | 2026-09-20T22:27:50Z | 2026-09-20T23:20:00Z |
| underdog|0f780f7d-76c1-4d28-b80e-bd7d9a41fdfd | underdog | Gunnar Henderson | Batter Walks | over | 0.0783649503161698 | 2026-09-20T22:27:50Z | 2026-09-20T23:20:00Z |
| underdog|24e8f5eb-15d7-421d-ac29-082a8e399ded | underdog | Colton Cowser | Batter Walks | over | 0.0769788644840447 | 2026-09-20T22:27:50Z | 2026-09-20T23:20:00Z |
| prizepicks|13952671 | prizepicks | Victor Wembanyama | Points | under | 0.0750528755951651 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| underdog|b73aafb1-c509-4381-9e4c-a49f7199b533 | underdog | Jackson Chourio | Hits + Runs + RBIs | over | 0.0749351029401079 | 2026-09-20T22:27:50Z | 2026-09-20T23:20:00Z |
| underdog|eeabc208-fb3b-4fb6-95f0-048ed61edb25 | underdog | Garrett Mitchell | Hits + Runs + RBIs | over | 0.0729704615235541 | 2026-09-20T22:27:50Z | 2026-09-20T23:20:00Z |
| prizepicks|15066381 | prizepicks | Sofia Kenin | Total Games Won | under | 0.0692569659087233 | 2026-09-20T18:49:37Z | 2026-09-21T23:00:00.000-04:00 |
| prizepicks|13976051 | prizepicks | Victor Wembanyama | PRA | under | 0.0685309144464778 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| underdog|84debc87-29b3-4087-8bec-f163624c7813 | underdog | Christian Yelich | RBIs | over | 0.06720058915585 | 2026-09-20T22:27:50Z | 2026-09-20T23:20:00Z |
| underdog|39b36b87-6989-4cf5-b1e8-1675050c2f56 | underdog | Jake Bauers | RBIs | over | 0.0658715263062298 | 2026-09-20T22:27:50Z | 2026-09-20T23:20:00Z |
| prizepicks|13976018 | prizepicks | Shai Gilgeous-Alexander | PRA | under | 0.0657969563767089 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| prizepicks|13976046 | prizepicks | Victor Wembanyama | Pts+Rebs | under | 0.0636568093159484 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| prizepicks|13976096 | prizepicks | Victor Wembanyama | 3PTM | under | 0.0631157689671098 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| underdog|0b74472f-f19a-4d00-acdf-66049128aa29 | underdog | Pete Alonso | Batter Walks | over | 0.0628163828808099 | 2026-09-20T22:27:50Z | 2026-09-20T23:20:00Z |
| underdog|22cb8f39-4336-4f92-8111-a168891d9b34 | underdog | Jacob Misiorowski | Hits Allowed | over | 0.060544948336585 | 2026-09-20T22:27:50Z | 2026-09-20T23:20:00Z |
| underdog|3fc68bba-43df-471a-bd85-a322d83ba02e | underdog | Sal Frelick | Hits + Runs + RBIs | over | 0.0598663409204534 | 2026-09-20T22:27:50Z | 2026-09-20T23:20:00Z |
| underdog|f310d259-09d2-499c-a632-7e9d91bfd262 | underdog | Garrett Mitchell | RBIs | over | 0.0592571941888918 | 2026-09-20T22:27:50Z | 2026-09-20T23:20:00Z |
| prizepicks|15039924 | prizepicks | Renata Zarazua | 1st Set Total Games Won | under | 0.058752563037674 | 2026-09-20T18:49:37Z | 2026-09-21T23:00:00.000-04:00 |
| prizepicks|15039092 | prizepicks | Alina Korneeva | Total Games | over | 0.0580417564948919 | 2026-09-20T04:56:02Z | 2026-09-20T23:00:00.000-04:00 |
| underdog|6e3a8f34-fad3-4bcb-99bd-6841c4e53335 | underdog | Samuel Basallo | Hits + Runs + RBIs | over | 0.05667404970745 | 2026-09-20T18:49:37Z | 2026-09-20T23:20:00Z |
| prizepicks|15042294 | prizepicks | Linda Fruhvirtova | Total Games Won | over | 0.0541658841081486 | 2026-09-20T04:56:02Z | 2026-09-20T23:00:00.000-04:00 |
| underdog|35fcf457-bd17-43c3-b6fc-c24cf845da53 | underdog | Jackson Chourio | Batter Walks | over | 0.0504663557628247 | 2026-09-20T18:49:37Z | 2026-09-20T23:20:00Z |
| prizepicks|15073133 | prizepicks | Yue Yuan | Break Points Won | under | 0.0502978382273101 | 2026-09-20T18:49:37Z | 2026-09-21T01:00:00.000-04:00 |
| prizepicks|14007606 | prizepicks | LeBron James | Rebs+Asts | under | 0.04958671453074 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|1abe8948-8da8-4eae-81d6-4c37a9b59ea3 | underdog | Sal Frelick | RBIs | over | 0.0491666666666666 | 2026-09-20T22:27:50Z | 2026-09-20T23:20:00Z |
| underdog|71f41b8a-dd9c-45d6-8807-2b35791ab002 | underdog | Gunnar Henderson | RBIs | over | 0.0491666666666666 | 2026-09-20T18:49:37Z | 2026-09-20T23:20:00Z |
| underdog|f5294976-b605-424e-97b3-d51beba89000 | underdog | Joey Ortiz | Hits | under | 0.0486938924045229 | 2026-09-20T22:27:50Z | 2026-09-20T23:20:00Z |
| underdog|76cf1952-32be-4966-8b8d-a5479fb00b06 | underdog | Dylan Beavers | Batter Walks | under | 0.0475813177648041 | 2026-09-20T22:27:50Z | 2026-09-20T23:20:00Z |
| prizepicks|15072779 | prizepicks | Talia Gibson | Break Points Won | under | 0.0471238958288736 | 2026-09-20T18:49:37Z | 2026-09-21T02:00:00.000-04:00 |
| underdog|e5b38d47-4147-408d-b1e4-d4e905fe1a18 | underdog | Gunnar Henderson | Total Bases | over | 0.0461480214263678 | 2026-09-20T18:49:37Z | 2026-09-20T23:20:00Z |
| underdog|cbe17caa-1a98-44d3-88ed-f0cb493d8ab2 | underdog | Cooper Pratt | Batter Walks | over | 0.0456855658459453 | 2026-09-20T22:27:50Z | 2026-09-20T23:20:00Z |
| underdog|a29f09b8-b62d-4f59-bd2c-7b57d162ec4a | underdog | Sal Frelick | Batter Walks | over | 0.0433253516911103 | 2026-09-20T22:27:50Z | 2026-09-20T23:20:00Z |
| prizepicks|13976010 | prizepicks | Shai Gilgeous-Alexander | Pts+Asts | under | 0.0419653653034837 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| underdog|6a89dfa6-09b4-47f4-a554-7229e07e5c41 | underdog | Jake Bauers | Hits + Runs + RBIs | over | 0.0397330112357015 | 2026-09-20T18:49:37Z | 2026-09-20T23:20:00Z |
| underdog|ccaa46ef-48b5-4a07-a895-09e843ce7877 | underdog | Joey Ortiz | Total Bases | over | 0.0390117401660253 | 2026-09-20T18:49:37Z | 2026-09-20T23:20:00Z |
| underdog|f116a023-c2d8-494f-b8d2-41a68782fab3 | underdog | Joey Ortiz | RBIs | under | 0.0385809312638582 | 2026-09-20T22:27:50Z | 2026-09-20T23:20:00Z |
| prizepicks|15072775 | prizepicks | Storm Hunter | Break Points Won | under | 0.0380084157410456 | 2026-09-20T18:49:37Z | 2026-09-21T07:40:00.000-04:00 |
| underdog|360f970a-200e-4a76-929c-de5055f8a691 | underdog | Kamilla Rakhimova | Double Faults | under | 0.0379095992141229 | 2026-09-20T22:27:50Z | 2026-09-21T04:10:00Z |
| prizepicks|13976083 | prizepicks | Victor Wembanyama | Rebounds | over | 0.0374835925599008 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| underdog|25b799da-ddab-43f0-95d3-3f39875f51b4 | underdog | Brandon Young | Strikeouts | over | 0.0372876739076417 | 2026-09-20T18:49:37Z | 2026-09-20T23:20:00Z |
| underdog|568538af-4ede-43a7-8625-840be66f4102 | underdog | Christian Yelich | Hits + Runs + RBIs | over | 0.0371713213857302 | 2026-09-20T18:49:37Z | 2026-09-20T23:20:00Z |
| underdog|16bc6acc-7283-4427-86a0-8dccab2fdaa4 | underdog | Coby Mayo | Hits + Runs + RBIs | over | 0.0369382068417737 | 2026-09-20T22:27:50Z | 2026-09-20T23:20:00Z |
| underdog|7a8d475b-6069-4aa9-b68b-1afd86352484 | underdog | Jacob Misiorowski | Pitching Outs | over | 0.0365487329369398 | 2026-09-20T18:49:37Z | 2026-09-20T23:20:00Z |
| prizepicks|14745234 | prizepicks | Davante Adams | Rec Yards | over | 0.0351398325190843 | 2026-09-11T16:24:54Z | 2026-09-21T20:15:00.000-04:00 |
| prizepicks|15066741 | prizepicks | Fiona Ferro | 1st Set Total Games Won | under | 0.0343574335161322 | 2026-09-20T18:49:37Z | 2026-09-21T02:00:00.000-04:00 |
| underdog|9378c61f-5bbc-4ca7-98e0-6bc05c984c9c | underdog | Garrett Mitchell | Hits | over | 0.0337133395018499 | 2026-09-20T22:27:50Z | 2026-09-20T23:20:00Z |
| underdog|bbc5573b-052f-4875-bead-b6eb1cdade69 | underdog | Jackson Chourio | Hits | over | 0.0333314921827009 | 2026-09-20T22:27:50Z | 2026-09-20T23:20:00Z |
| underdog|d94e408d-3ecf-4cce-bf67-84f61d664d5a | underdog | Dylan Beavers | Hits + Runs + RBIs | over | 0.0316028226248358 | 2026-09-20T18:49:37Z | 2026-09-20T23:20:00Z |
| prizepicks|15067246 | prizepicks | Aliaksandra Sasnovich | 1st Set Total Games Won | under | 0.0301367538109708 | 2026-09-20T18:49:37Z | 2026-09-20T23:00:00.000-04:00 |
