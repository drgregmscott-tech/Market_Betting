# Pipeline Digest -- 2026-10-19T04:29:38Z

## Run summary
- Ingestion: 14736 rows (PrizePicks OK, Underdog OK)
- Estimation: 14736 rows estimated (from 14736 ingested props)
- CLV logging: 148 newly flagged, 0 newly closed, 228 still open (103391 total ever logged)

## Currently open flags
Sizing is a manual step (sizing_engine.py, Session 2.6) -- this table is what to scan to pick a pair worth sizing.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_edge | first_flagged_at | game_start_time |
|---|---|---|---|---|---|---|---|
| underdog|2fd919bf-4db7-4293-91d7-aa62423b3b0a | underdog | Jayden Daniels | Pass Yards | under | 0.4532994923857868 | 2026-10-15T04:38:48Z | 2026-10-20T00:15:00Z |
| underdog|75ade92a-c724-43d5-abea-6c2a3f2816a9 | underdog | Brock Purdy | Pass Attempts | under | 0.4226130653266332 | 2026-10-16T04:33:49Z | 2026-10-20T00:15:00Z |
| underdog|4b6d59d8-b0bf-48e9-93d3-6c2fdb92b62e | underdog | Stefon Diggs | Receiving Yards | under | 0.411130384316266 | 2026-10-18T04:33:13Z | 2026-10-20T00:15:00Z |
| underdog|9be84160-7fb1-4284-a17a-a04f2125c5de | underdog | Brock Purdy | Completions | under | 0.4 | 2026-10-15T04:38:48Z | 2026-10-20T00:15:00Z |
| underdog|3f6a4e08-cdcb-4e3a-ad6e-22acec0014c9 | underdog | Brock Purdy | Pass Yards | under | 0.4 | 2026-10-15T04:38:48Z | 2026-10-20T00:15:00Z |
| underdog|8155d555-4db3-4397-a837-8d3b7269a93d | underdog | Caleb Williams | Pass Attempts | under | 0.4 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| underdog|ba12fda6-c538-42ce-8c47-c81107c54e3f | underdog | A.J. Brown | Receiving Yards | under | 0.4 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| underdog|7a520285-f44f-4692-8b2c-e0a7ebd6e60c | underdog | A.J. Brown | Receptions | under | 0.4 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| underdog|8ddd3d29-fe64-4279-87e3-2a09c8b64156 | underdog | Caleb Williams | Pass Yards | under | 0.4 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| underdog|9ac2fb87-7b6f-4695-9458-ccea6878beba | underdog | Drake Maye | Pass Yards | under | 0.4 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| underdog|77b97767-248e-4dda-b829-806b9a567a91 | underdog | Christian McCaffrey | Rush + Rec Yards | under | 0.397850431989636 | 2026-10-15T04:38:48Z | 2026-10-20T00:15:00Z |
| underdog|b290a7f7-2448-41b8-8395-aaf31553b5b0 | underdog | Christian McCaffrey | Receptions | under | 0.382768282723803 | 2026-10-15T04:38:48Z | 2026-10-20T00:15:00Z |
| underdog|50252889-3a21-4531-8598-2fc199a73bb7 | underdog | Christian McCaffrey | Receiving Yards | under | 0.3646000607706979 | 2026-10-15T04:38:48Z | 2026-10-20T00:15:00Z |
| underdog|c88864cd-10ff-4b61-a84b-29dc767a03b9 | underdog | Drake Maye | Pass Attempts | under | 0.3635582410030858 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| prizepicks|15683924 | prizepicks | Jayden Daniels | Pass Yards | under | 0.3509424650567749 | 2026-10-14T13:48:29Z | 2026-10-19T20:15:00.000-04:00 |
| prizepicks|15683925 | prizepicks | Brock Purdy | Pass Yards | under | 0.3509424650567749 | 2026-10-14T13:48:29Z | 2026-10-19T20:15:00.000-04:00 |
| prizepicks|15723443 | prizepicks | George Kittle | Rec Targets | under | 0.341921366253107 | 2026-10-14T13:48:29Z | 2026-10-19T20:15:00.000-04:00 |
| prizepicks|15851449 | prizepicks | Jayden Daniels | Pass+Rush+Rec TDs | under | 0.3373929181917084 | 2026-10-17T04:25:02Z | 2026-10-19T20:15:00.000-04:00 |
| underdog|f91f6288-1b31-4637-bad9-e887cc68a203 | underdog | Cyril Ngonge | Shots Attempted | under | 0.3307692307692308 | 2026-10-16T04:33:49Z | 2026-10-19T16:30:00Z |
| underdog|73652f9d-4324-4e95-8866-6aab14c1dbc5 | underdog | Stefon Diggs | Receptions | under | 0.3285714285714286 | 2026-10-18T04:33:13Z | 2026-10-20T00:15:00Z |
| underdog|7ebc0057-5e8c-4445-9d57-4f16b8dc8a61 | underdog | Rachaad White | Rush Yards | under | 0.3257593259117504 | 2026-10-18T04:33:13Z | 2026-10-20T00:15:00Z |
| underdog|6f78287f-f313-4cac-be1f-ea808ea44528 | underdog | Cyril Ngonge | Shots on Target | under | 0.3162436548223351 | 2026-10-16T04:33:49Z | 2026-10-19T16:30:00Z |
| underdog|f89af6c6-e75c-473e-80e2-2b566253d4f5 | underdog | Jayden Daniels | Pass Attempts | under | 0.3149988412199163 | 2026-10-15T04:38:48Z | 2026-10-20T00:15:00Z |
| underdog|56db0e00-47df-49cf-bbb9-5483053087be | underdog | Mike Evans | Receiving Yards | under | 0.3131898190585049 | 2026-10-17T04:25:02Z | 2026-10-20T00:15:00Z |
| prizepicks|15851333 | prizepicks | Brock Purdy | Pass+Rush+Rec TDs | under | 0.3122548350258745 | 2026-10-17T04:25:02Z | 2026-10-19T20:15:00.000-04:00 |
| underdog|6d8aebea-e99e-4ad3-9208-0114be3daec8 | underdog | Steven Kwan | Batter Walks | over | 0.3122052704576975 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|a2995dec-b1f5-450c-8270-e44367503da7 | underdog | Jorge De Frutos | Shots Attempted | under | 0.3081632653061225 | 2026-10-19T04:39:53Z | 2026-10-19T19:00:00Z |
| underdog|76e1327a-8ef9-47e2-a4fd-e6915d169ac8 | underdog | Austin Ekeler | Receptions | under | 0.303061224489796 | 2026-10-18T04:33:13Z | 2026-10-20T00:15:00Z |
| underdog|e296ce35-a81f-49e2-af2f-4786a54b96b7 | underdog | Caleb Williams | Pass TDs | under | 0.2699980933802138 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| underdog|1464b0b8-b102-43a6-8a12-ba26d199aaa5 | underdog | Mike Evans | Receptions | under | 0.2538678668382569 | 2026-10-15T04:38:48Z | 2026-10-20T00:15:00Z |
| underdog|af90435f-fdf2-4368-aab3-46a55f067a66 | underdog | George Kittle | Receiving Yards | under | 0.2469843361186776 | 2026-10-18T04:33:13Z | 2026-10-20T00:15:00Z |
| underdog|29b2a43f-7f8a-4846-9b2d-a61aec1b5747 | underdog | Andy Borregales | Kicking Points | under | 0.2444283245360812 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| underdog|65ef2c13-cfea-42a7-bdbf-93a8550656e2 | underdog | Drew Stevens | FG Made | under | 0.2421453388790657 | 2026-10-14T13:48:29Z | 2026-10-20T00:15:00Z |
| underdog|ecd259a7-684f-4fc4-9de3-021052d9f72a | underdog | Austin Ekeler | Receiving Yards | over | 0.2398624069071242 | 2026-10-18T04:33:13Z | 2026-10-20T00:15:00Z |
| prizepicks|13952668 | prizepicks | LeBron James | Points | over | 0.2397149568250941 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|f797f059-a1fe-4002-984b-c8fcde57a8e9 | underdog | George Kittle | Receptions | under | 0.2391505701291185 | 2026-10-15T04:38:48Z | 2026-10-20T00:15:00Z |
| prizepicks|15687743 | prizepicks | Mike Evans | Rec Yards | under | 0.2385575580504614 | 2026-10-14T13:48:29Z | 2026-10-19T20:15:00.000-04:00 |
| underdog|751c6c65-bb0e-4b5a-bdd1-24aa64b44573 | underdog | Colston Loveland | Receiving Yards | under | 0.2310302617610162 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| underdog|4d576151-8dfd-4253-b495-f9e32f0fbfcb | underdog | Luther Burden | Receiving Yards | under | 0.2288068722746987 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| underdog|e5387e46-b4ff-4987-a8d3-521750cb98a8 | underdog | Diane Parry | Double Faults | under | 0.2275873546686131 | 2026-10-19T04:39:53Z | 2026-10-19T11:30:00Z |
| underdog|067aeca1-b338-4cee-81cb-4e31ca8ace7f | underdog | Brayan Rocchio | Total Bases | over | 0.225455995215788 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| prizepicks|13975988 | prizepicks | LeBron James | Pts+Rebs | over | 0.2247745517150446 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|9f90af16-920b-43e1-98f4-358f6abe9aa7 | underdog | Drew Stevens | Kicking Points | under | 0.2243861026972581 | 2026-10-15T04:38:48Z | 2026-10-20T00:15:00Z |
| underdog|ae0a75f0-8fde-4629-9e70-516e0115471c | underdog | Cairo Santos | FG Made | under | 0.2234479238389184 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| prizepicks|13952667 | prizepicks | Jalen Brunson | Points | over | 0.2135813857285506 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|342f942a-6d5c-4551-9998-9a3d4fef42d5 | underdog | Chig Okonkwo | Receptions | under | 0.2130000137131517 | 2026-10-19T04:39:53Z | 2026-10-20T00:15:00Z |
| underdog|58162609-cca2-4003-b155-d7934421107a | underdog | D'Andre Swift | Rush + Rec Yards | under | 0.2123378357657818 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| underdog|3c9367c2-7aba-4ef7-be43-29e8b2638218 | underdog | Tait Reynolds | Pass TDs | under | 0.212066897965787 | 2026-10-19T04:39:53Z | 2026-10-24T23:00:00Z |
| underdog|8e649781-fed8-4594-a239-03dfa39986a0 | underdog | Taylor Walls | Runs | over | 0.205509242479159 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|18a8053e-96a8-43b5-909e-4c6210c3a9b2 | underdog | Andy Borregales | FG Made | under | 0.2038454190489985 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| underdog|65b69cd0-bded-44dd-a209-1f19dd444632 | underdog | Rachaad White | Rush + Rec Yards | under | 0.2037667545752868 | 2026-10-19T04:39:53Z | 2026-10-20T00:15:00Z |
| underdog|34385afe-49f2-48b5-8b4a-6630c3ae7446 | underdog | Rhamondre Stevenson | Rush Yards | under | 0.2023355512513842 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| underdog|327827c6-8602-4d01-a9f7-488a94b86d43 | underdog | Junior Caminero | Total Bases | over | 0.2004576148222556 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|2241e611-67e0-476c-a3fc-6a3f0fd6d8a6 | underdog | Christian McCaffrey | Rush Yards | under | 0.1997397401763914 | 2026-10-15T04:38:48Z | 2026-10-20T00:15:00Z |
| underdog|b03fb4e6-13b7-45b2-9c97-c69989117ea4 | underdog | El Bilal Toure | Shots Attempted | under | 0.1988128603077319 | 2026-10-16T04:33:49Z | 2026-10-19T18:45:00Z |
| underdog|bb4011ff-dfcc-4b2d-b103-24aa51254b81 | underdog | Petey Halpin | Total Bases | over | 0.1907530336983636 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| prizepicks|13975959 | prizepicks | Jalen Brunson | Pts+Rebs | over | 0.1892442263984233 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|268042f8-735d-44f8-8e36-d1ae91114cb0 | underdog | Brayan Rocchio | RBIs | over | 0.1850121516717396 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|c9aeee67-69bf-441f-b778-fb44bd9f8639 | underdog | Travis Bazzana | Total Bases | over | 0.1844925634295714 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|0221511d-5a31-4f53-ada9-b51ee05dd80f | underdog | Liam Hicks | RBIs | over | 0.1793503126429769 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| prizepicks|13975984 | prizepicks | LeBron James | Pts+Asts | over | 0.1791375054527176 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|f093053a-9984-4287-b61b-8877f650409f | underdog | Terry McLaurin | Receiving Yards | under | 0.1786940622638401 | 2026-10-18T04:33:13Z | 2026-10-20T00:15:00Z |
| prizepicks|15890685 | prizepicks | Diane Parry | Double Faults | under | 0.178529819725388 | 2026-10-19T04:39:53Z | 2026-10-19T07:30:00.000-04:00 |
| underdog|a26fde07-0e44-4e6a-8f85-d9eca9aceaf3 | underdog | Sorana Cirstea | Double Faults | under | 0.1779788422767582 | 2026-10-19T04:39:53Z | 2026-10-19T05:15:00Z |
| prizepicks|13975992 | prizepicks | LeBron James | PRA | over | 0.1710160714309272 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|926047f6-6919-45a0-b3ef-9cb03a59cc77 | underdog | Daniel Maldini | Shots Attempted | under | 0.1702392253406577 | 2026-10-16T04:33:49Z | 2026-10-19T16:30:00Z |
| underdog|caa95152-4aaf-44df-873b-d38752fbebe7 | underdog | Richie Palacios | RBIs | over | 0.1619855149266913 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|14996e29-0463-4ef6-b4f4-d2d2a3562e45 | underdog | Gustavo Varela | Shots Attempted | under | 0.161107508887347 | 2026-10-16T04:33:49Z | 2026-10-19T16:30:00Z |
| prizepicks|13975964 | prizepicks | Jalen Brunson | PRA | over | 0.1594536543882333 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|5ccd8c1c-4078-4c1e-9029-820aee35e94a | underdog | Terry McLaurin | Receptions | under | 0.1569422183629093 | 2026-10-18T04:33:13Z | 2026-10-20T00:15:00Z |
| prizepicks|15684004 | prizepicks | Christian McCaffrey | Rush Yards | under | 0.1568613213703028 | 2026-10-14T13:48:29Z | 2026-10-19T20:15:00.000-04:00 |
| underdog|b0053690-83ec-4373-838d-29728db0f497 | underdog | José Ramírez | Runs | over | 0.1562432839028584 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|658296a2-6059-4613-9d10-858d6840aac5 | underdog | Chase DeLauter | Total Bases | over | 0.1554696933107943 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|dcaa0300-d695-4e07-b1a6-eb8ff327f186 | underdog | Yandy Díaz | Runs | over | 0.1537871687824824 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|17ca61d5-a99a-4805-8005-7b560cb4f8b2 | underdog | Steven Kwan | Runs | over | 0.1537056511872474 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|4d0beeea-bb82-4aca-a56a-bcbe6630b224 | underdog | Taylor Walls | Total Bases | over | 0.15046792197542 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|6cd40a1f-1e9f-45e8-8de2-60ebf0b846c6 | underdog | Rome Odunze | Receiving Yards | under | 0.1501463657464657 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| underdog|f649e406-fd37-43ad-8bae-7bb995d397fd | underdog | Beau Pribula | Pass TDs | over | 0.1499521545038517 | 2026-10-19T04:39:53Z | 2026-10-23T23:00:00Z |
| prizepicks|15874224 | prizepicks | Stefon Diggs | Rec Targets | under | 0.1484182869513028 | 2026-10-18T04:33:13Z | 2026-10-19T20:15:00.000-04:00 |
| underdog|3f6d8ded-c9ad-43ad-a855-6faf4e024489 | underdog | Jo Adell | Total Bases | over | 0.148167777104785 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| prizepicks|15723441 | prizepicks | Christian McCaffrey | Rec Targets | under | 0.147919974847375 | 2026-10-14T13:48:29Z | 2026-10-19T20:15:00.000-04:00 |
| underdog|9c7c2779-8bda-486d-acc5-3d994a05dc3b | underdog | Katie Boulter | Double Faults | under | 0.1469264342880455 | 2026-10-19T04:39:53Z | 2026-10-19T06:25:00Z |
| underdog|3be9b58d-14da-43e2-8d1a-bf9936a89a74 | underdog | Travis Bazzana | RBIs | over | 0.1461194464290439 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|d534a9b8-272b-4fe7-a285-76fddcf89548 | underdog | D'Andre Swift | Rush Yards | under | 0.1460517246856272 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| prizepicks|13975955 | prizepicks | Jalen Brunson | Pts+Asts | over | 0.1457490982774579 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|2be59240-69ee-4552-b9d2-af3c4d18e2e7 | underdog | Kaelon Black | Rush + Rec Yards | under | 0.1444614976184334 | 2026-10-15T04:38:48Z | 2026-10-20T00:15:00Z |
| underdog|5d22600f-71f4-4fee-8276-f0c78c5e50eb | underdog | Junior Caminero | Runs | over | 0.1440400331209275 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|18ffffcc-676c-4f5e-9733-dbc3872fc7d1 | underdog | Jonathan Aranda | RBIs | over | 0.141089243853241 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|78b8577c-506d-4e2b-88d2-e8354b0bdd00 | underdog | Brayan Rocchio | Hits | over | 0.1408732118166504 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|df19f4d0-f523-4664-b374-9a661848e7bd | underdog | Nathaniel Lowe | RBIs | over | 0.1407659482525792 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| prizepicks|13976081 | prizepicks | Jalen Brunson | Rebounds | over | 0.1400370452709755 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|53eda10b-bf8c-4c6f-85bc-22a77273c413 | underdog | Brock Purdy | Pass TDs | under | 0.1373225827661014 | 2026-10-14T13:48:29Z | 2026-10-20T00:15:00Z |
| underdog|a36d3b0c-087b-4e18-84f8-70f064fd3aad | underdog | Rhamondre Stevenson | Rush + Rec Yards | under | 0.136283636992093 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| underdog|0e1dd9cb-4ac6-440c-ab72-589ce1b98411 | underdog | Jayden Daniels | Pass TDs | under | 0.1352637925651718 | 2026-10-14T13:48:29Z | 2026-10-20T00:15:00Z |
| underdog|3bb43b62-aafa-432c-8bfc-7b0907d78cfc | underdog | Yandy Díaz | RBIs | over | 0.1352506801399144 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|96598eb7-171b-44ef-8842-bbd789d6d72d | underdog | Cairo Santos | Kicking Points | under | 0.1348240121618629 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| underdog|2d2ba075-d08a-456b-b5e4-2a446760115e | underdog | Patrick Bailey | Total Bases | over | 0.1338867102935536 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|606b0925-6155-487f-8a03-5228a08ddf06 | underdog | Colston Loveland | Receptions | under | 0.1336120349687193 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| underdog|0fb50bc9-621b-4b85-99e0-28b0e5f153b2 | underdog | Rhamondre Stevenson | Receptions | under | 0.1315147469871405 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| underdog|fbb7616f-d409-4ccf-a93b-0ea706500f6a | underdog | Jorge De Frutos | Shots on Target | under | 0.1312669295969791 | 2026-10-19T04:39:53Z | 2026-10-19T19:00:00Z |
| underdog|c8a87133-1e1f-4cf2-b08a-13bdd20a2be3 | underdog | Walker Eget | Pass Yards | under | 0.1308982267738939 | 2026-10-19T04:39:53Z | 2026-10-23T23:00:00Z |
| prizepicks|13975891 | prizepicks | Cade Cunningham | Pts+Asts | under | 0.1301298534041951 | 2026-09-12T11:28:56Z | 2026-10-20T15:10:00.000-04:00 |
| prizepicks|13975904 | prizepicks | Cade Cunningham | Rebs+Asts | under | 0.1276349180264445 | 2026-09-12T11:28:56Z | 2026-10-20T15:10:00.000-04:00 |
| underdog|81938db7-82ff-43a8-8827-bb168b8137e0 | underdog | Hunter Henry | Receptions | under | 0.1255866606998207 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| underdog|bc93cc19-c969-43a8-b2b3-a7db327a1c36 | underdog | Jo Adell | RBIs | over | 0.1244979919678714 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| prizepicks|15874226 | prizepicks | Chig Okonkwo | Rec Targets | under | 0.1239452842800243 | 2026-10-18T04:33:13Z | 2026-10-19T20:15:00.000-04:00 |
| prizepicks|13976014 | prizepicks | Shai Gilgeous-Alexander | Pts+Rebs | under | 0.1235832751001789 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| underdog|8178330e-e733-4944-b938-28323fe6241f | underdog | Nathaniel Lowe | Total Bases | over | 0.1229891744233103 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|16e98a71-fc5a-4b1e-a2ae-73f8d9b6d911 | underdog | Junior Caminero | RBIs | over | 0.1229476043709722 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|795c9d09-fdb5-4b73-879b-4c1bdef593ca | underdog | Gustavo Varela | Shots on Target | under | 0.1216821892215763 | 2026-10-16T04:33:49Z | 2026-10-19T16:30:00Z |
| prizepicks|13975945 | prizepicks | Jalen Brunson | Assists | under | 0.1210560575434291 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|9e2cf2ea-88d3-48df-ab17-6654e6fe6856 | underdog | Chig Okonkwo | Receiving Yards | under | 0.1199547516828379 | 2026-10-19T04:39:53Z | 2026-10-20T00:15:00Z |
| underdog|566ebc59-8f3f-4e55-b73b-ea18eb4cf2f0 | underdog | Jo Adell | Hits + Runs + RBIs | over | 0.1196604140328941 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|111430f8-7f07-467a-84be-620dba781de3 | underdog | Paul Mendy | Shots Attempted | under | 0.119250767652726 | 2026-10-16T04:33:49Z | 2026-10-19T16:30:00Z |
| underdog|7803be79-801c-4ae2-a404-d0ef795a44e3 | underdog | Jonny DeLuca | Hits + Runs + RBIs | over | 0.1190534202220864 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|07f962c7-42d4-4b27-b320-5d80c5562c16 | underdog | Taylor Walls | Hits | over | 0.1169263092379782 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| prizepicks|13976095 | prizepicks | Cade Cunningham | 3PTM | over | 0.1168098507846668 | 2026-09-12T11:28:56Z | 2026-10-20T15:10:00.000-04:00 |
| underdog|415a960b-11e1-4be3-9d24-17e600e58819 | underdog | Chandler Simpson | RBIs | under | 0.1165951359084406 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|04f5fcbc-4780-4d20-9c3d-345e6cd2ea8a | underdog | D'Andre Swift | Receptions | under | 0.1151747294320429 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| underdog|231c4c82-8c83-44fa-95a3-a3748a7aee08 | underdog | Rhamondre Stevenson | Receiving Yards | under | 0.1146179526454099 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| prizepicks|15898737 | prizepicks | Gustavo Varela | Shots | under | 0.1125417599242365 | 2026-10-19T04:39:53Z | 2026-10-19T12:30:00.000-04:00 |
| underdog|8c55eee2-f4ea-4d6d-a5c3-a3abe7a37567 | underdog | Jonny DeLuca | RBIs | over | 0.1113691090471275 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|73cfc407-9b54-4eab-ad71-1b16cfe226ef | underdog | Nikola Vlasic | Shots Attempted | under | 0.1109519945595428 | 2026-10-16T04:33:49Z | 2026-10-19T18:45:00Z |
| underdog|d4d93466-5b2b-4c37-b066-4ac5c5f4b495 | underdog | Travis Bazzana | Batter Walks | over | 0.1085793752674368 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|f9d79590-7541-413d-b445-46273a40b5bc | underdog | Yandy Díaz | Total Bases | over | 0.1082379293180685 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|4aa8e250-9ec3-4a6f-af5b-0e94c3781b14 | underdog | Victor Mesa | Runs | over | 0.1075875029363401 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|109635a3-7422-44dd-970d-4396be7b26b9 | underdog | Liam Hicks | Total Bases | over | 0.1070027688047992 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|d3850c26-85bc-4082-a18f-1f8853b6f594 | underdog | Drake Maye | Rush Yards | under | 0.1068196271586217 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| underdog|33b6fb1b-243f-4946-8212-e797f561fe8b | underdog | Luther Burden | Receptions | under | 0.1067635448973685 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| underdog|c37e8b02-5a63-42c1-9c11-0ea2d8522dde | underdog | Chase DeLauter | Hits + Runs + RBIs | over | 0.1064745981596016 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|9efdcbbe-860e-48e4-9bc2-3c0c8cb3ac82 | underdog | Liam Hicks | Hits + Runs + RBIs | over | 0.1059573228082308 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|22f89fb1-de44-4c53-8f29-21521c74c93f | underdog | Victor Mesa | Total Bases | over | 0.1049471088841167 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|255c6b4a-50e3-4bd1-8b32-aac892019ee0 | underdog | Jonathan Aranda | Total Bases | over | 0.1049471088841167 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|7e602675-b79a-4d0e-8cde-6b83ea8f79ea | underdog | Jonny DeLuca | Total Bases | over | 0.1041280148423005 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|94eb6fa4-a98b-487e-ae4d-898fb33841c1 | underdog | Kaelon Black | Receptions | under | 0.1036569699005706 | 2026-10-15T04:38:48Z | 2026-10-20T00:15:00Z |
| underdog|552135f1-bf7a-41fb-84e5-2c8a30e5973b | underdog | Jonathan Aranda | Hits + Runs + RBIs | over | 0.1028513916997484 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|1f61ca69-a504-485e-89f7-66bd2aced799 | underdog | Ethan Grunkemeyer | Pass TDs | over | 0.1027014115660162 | 2026-10-19T04:39:53Z | 2026-10-24T23:00:00Z |
| prizepicks|13976040 | prizepicks | Victor Wembanyama | Pts+Asts | under | 0.1021735734863812 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| underdog|dc43bfc5-2b41-41db-8810-d052c606851a | underdog | José Ramírez | RBIs | over | 0.1016573295985059 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| prizepicks|13975896 | prizepicks | Cade Cunningham | Pts+Rebs | under | 0.1002719704236944 | 2026-09-12T11:28:56Z | 2026-10-20T15:10:00.000-04:00 |
| underdog|1bc55bec-f57f-4b52-a357-53f8d8ffb8ed | underdog | Richie Palacios | Total Bases | over | 0.0994475138121546 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|3e0754f3-d8ab-4245-a5c1-8a8936db8303 | underdog | José Ramírez | Hits + Runs + RBIs | over | 0.0981356139544705 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|7cb79f7c-9ea6-42e1-90af-667e6406c15e | underdog | Brayan Rocchio | Runs | over | 0.0964285714285714 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|0cebdd97-0b79-46ba-af3e-beef4573af6c | underdog | Himeno Sakatsume | Double Faults | under | 0.0963289707867027 | 2026-10-19T04:39:53Z | 2026-10-19T06:25:00Z |
| prizepicks|15889969 | prizepicks | Mary Stoiana | Total Games | over | 0.0953776196201968 | 2026-10-19T04:39:53Z | 2026-10-19T22:30:00.000-04:00 |
| underdog|34c5f3b9-0e89-4afb-b8e0-b4b84cf716e9 | underdog | Jacopo Fazzini | Shots Attempted | under | 0.094910178919513 | 2026-10-16T04:33:49Z | 2026-10-19T16:30:00Z |
| underdog|0a2b1589-4881-4634-94f0-dd474301eb37 | underdog | Austin Ekeler | Rush Yards | under | 0.0931846876934673 | 2026-10-18T04:33:13Z | 2026-10-20T00:15:00Z |
| underdog|43b79c8c-4c76-4894-9750-af569cf1b0ee | underdog | Yandy Díaz | Batter Walks | under | 0.0897141848976712 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|717037ac-e2f5-4ceb-9dbb-1606cdf93765 | underdog | Kamilla Rakhimova | Double Faults | under | 0.0890878024541818 | 2026-10-19T04:39:53Z | 2026-10-19T09:10:00Z |
| underdog|0450c315-4c40-4ff0-9c21-121dc6ad5851 | underdog | Taylor Walls | Batter Walks | under | 0.0849064925899788 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|5d998182-2b8a-4737-b72d-f3b325faa1d2 | underdog | D'Andre Swift | Receiving Yards | under | 0.084587733906124 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| underdog|e64a05e0-de75-4f34-99f8-f249fcf91a7e | underdog | Chase DeLauter | RBIs | over | 0.0841278407387419 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|018a1f81-e58c-49ed-8b6e-c46d5672efba | underdog | Steven Kwan | Total Bases | over | 0.0840681482663687 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| prizepicks|15873226 | prizepicks | Facundo Diaz Acosta | 1st Set Total Games Won | over | 0.0837962956155924 | 2026-10-19T04:39:53Z | 2026-10-19T02:30:00.000-04:00 |
| underdog|7b599fd8-33f9-4434-a1d4-a37b51679249 | underdog | Liam Hicks | Runs | over | 0.0834862385321101 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|001efed2-d0c0-4cf8-a231-73977f916c32 | underdog | Travis Bazzana | Hits | over | 0.0831477182456037 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|dcfd88d0-6fed-4df9-a0e2-f45991b6ce1d | underdog | Rolando Mandragora | Shots Attempted | under | 0.0829025730753998 | 2026-10-16T04:33:49Z | 2026-10-19T18:45:00Z |
| underdog|c550c55c-0598-4bfe-ad06-c624a4a05b72 | underdog | Travis Bazzana | Runs | over | 0.0820276497695852 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| prizepicks|15890751 | prizepicks | Sho Shimabukuro | Total Games Won | over | 0.0818372198872333 | 2026-10-19T04:39:53Z | 2026-10-20T02:30:00.000-04:00 |
| underdog|000a3555-a6b3-4c42-b508-c8aff1a074c4 | underdog | Victor Mesa | Hits + Runs + RBIs | over | 0.0806655288681479 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|7eb4744f-6719-43fe-8b73-4540ba39e408 | underdog | Chandler Simpson | Hits + Runs + RBIs | over | 0.0800478490965003 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|dc942526-6ae9-4383-b80f-bb8e9de609c2 | underdog | Hunter Henry | Receiving Yards | under | 0.0794098847181414 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| underdog|f7612dc7-b0f9-49ec-8602-e2e75b404f01 | underdog | Junior Caminero | Hits | over | 0.0778888260639179 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|81ed5d97-0fb1-4167-9899-2b5bc2c55dd4 | underdog | Antonio Williams | Receptions | under | 0.0777888765836508 | 2026-10-18T04:33:13Z | 2026-10-20T00:15:00Z |
| underdog|30c9760e-c4a2-4ce6-aa42-962b22c68ac5 | underdog | Steven Kwan | Hits + Runs + RBIs | over | 0.0767804889943058 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|b39b15ab-2220-4f36-9e04-a74781197ebb | underdog | Chase DeLauter | Hits | over | 0.0764119919519842 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|7456ca8f-1b95-4cd8-a22d-28ab0bacef33 | underdog | Jonathan Aranda | Hits | over | 0.0760391581823314 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| prizepicks|13952671 | prizepicks | Victor Wembanyama | Points | under | 0.0750528755951651 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| underdog|40f1b776-36bb-4f04-81b4-27ba9629f3a5 | underdog | Rachaad White | Receiving Yards | under | 0.0742268388080018 | 2026-10-17T04:25:02Z | 2026-10-20T00:15:00Z |
| underdog|6b762064-fcb8-43b4-8c01-c19307e3f99a | underdog | Daria Kasatkina | Double Faults | under | 0.0740218568934312 | 2026-10-19T04:39:53Z | 2026-10-19T08:00:00Z |
| underdog|ef0129f3-b541-4334-b9e6-6c575cb06872 | underdog | Brock Purdy | Rush Yards | under | 0.070348800774928 | 2026-10-18T04:33:13Z | 2026-10-20T00:15:00Z |
| underdog|5aebb7b4-5a9d-476a-bbb6-65c89963ee08 | underdog | Jo Adell | Hits | over | 0.069000819813213 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| prizepicks|13976051 | prizepicks | Victor Wembanyama | PRA | under | 0.0685309144464778 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| underdog|d40bf574-5ac9-446b-89ec-dbd9fbc96f19 | underdog | Richie Palacios | Hits | over | 0.068078264914871 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| prizepicks|15898953 | prizepicks | Daniel Altmaier | 1st Set Total Games Won | under | 0.0672393649020705 | 2026-10-19T04:39:53Z | 2026-10-20T05:00:00.000-04:00 |
| underdog|e0fb727d-e67a-4f7e-b368-a5ac3dc38af1 | underdog | Liam Hicks | Hits | over | 0.0670546894788648 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|78fca0a4-5488-4843-8f6c-958cba15f4ac | underdog | Kaelon Black | Rush Yards | under | 0.0657007230138554 | 2026-10-15T04:38:48Z | 2026-10-20T00:15:00Z |
| underdog|cb49c65a-d9c3-4097-a44f-5fdeb899d702 | underdog | Rome Odunze | Receptions | under | 0.0646316627856106 | 2026-10-19T04:39:53Z | 2026-10-23T00:15:00Z |
| prizepicks|13976046 | prizepicks | Victor Wembanyama | Pts+Rebs | under | 0.0636568093159484 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| prizepicks|13976096 | prizepicks | Victor Wembanyama | 3PTM | under | 0.0631157689671098 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| prizepicks|15874225 | prizepicks | Terry McLaurin | Rec Targets | under | 0.0597497378960204 | 2026-10-18T04:33:13Z | 2026-10-19T20:15:00.000-04:00 |
| underdog|b76da6bb-110a-4b7a-9486-268b4a36d7dd | underdog | Janice Tjen | Double Faults | under | 0.059252822413354 | 2026-10-19T04:39:53Z | 2026-10-19T05:10:00Z |
| underdog|0b7f214d-8955-4d08-9cd0-f00f5cff2a44 | underdog | Yandy Díaz | Hits + Runs + RBIs | over | 0.0585517656929617 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|98496538-8b8c-46b0-9014-897a44f83a9d | underdog | Freddy Peralta | Strikeouts | over | 0.0579576151153298 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|ec84feaf-2aeb-42b6-909a-ffbc3fc3bfa8 | underdog | Brayan Rocchio | Batter Walks | over | 0.0571182548794488 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|4b3a7d57-7756-4d73-84c6-6c545b4fda0d | underdog | Austin Ekeler | Rush + Rec Yards | under | 0.0567601516875453 | 2026-10-18T04:33:13Z | 2026-10-20T00:15:00Z |
| underdog|14780cc0-80ce-4e69-a65e-9bac9020139b | underdog | Will Bettridge | XP Made | over | 0.0558018821462565 | 2026-10-19T04:39:53Z | 2026-10-23T23:00:00Z |
| underdog|b92b9e9a-2ba4-443d-bdf1-33ea7bf4484e | underdog | Patrick Bailey | Batter Walks | over | 0.0553788316946211 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|c05af95f-82e4-4e0c-8e1f-188d077be2a2 | underdog | Junior Caminero | Hits + Runs + RBIs | over | 0.0553114269321142 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|f1a92693-6502-40c5-81c5-4257348b8215 | underdog | José Ramírez | Batter Walks | over | 0.0548199767711962 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|2776d7fc-1f49-4081-b866-e7d48f8a7c1d | underdog | Chandler Simpson | Total Bases | over | 0.0544492584569237 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|09a26752-b81a-470b-a44a-1b1efa32df3d | underdog | Jo Adell | Batter Walks | under | 0.0521267723102585 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|f49b82cf-9c43-4794-8eab-7c12b861a016 | underdog | Will Bettridge | FG Made | over | 0.0516947110884357 | 2026-10-19T04:39:53Z | 2026-10-23T23:00:00Z |
| underdog|4acff687-70d1-45b2-a939-11f396141504 | underdog | Richie Palacios | Batter Walks | over | 0.0516364440513046 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|a2209891-797a-484e-9822-d0b991bf8681 | underdog | Alexandra Eala | Double Faults | under | 0.0510497341926291 | 2026-10-19T04:39:53Z | 2026-10-19T11:30:00Z |
| underdog|e25acd6e-08c6-41f6-bf9f-0c8f78de6ce3 | underdog | Jayden Daniels | Rush Yards | under | 0.0502423742824463 | 2026-10-19T04:39:53Z | 2026-10-20T00:15:00Z |
| prizepicks|15885688 | prizepicks | Aleksandar Vukic | 1st Set Total Games Won | under | 0.0500714716499679 | 2026-10-19T04:39:53Z | 2026-10-19T03:40:00.000-04:00 |
| prizepicks|14007606 | prizepicks | LeBron James | Rebs+Asts | under | 0.04958671453074 | 2026-09-12T11:28:56Z | 2026-10-20T19:10:00.000-04:00 |
| underdog|fc729837-3bee-4852-8d1e-8c1171698fa6 | underdog | Chandler Simpson | Hits | over | 0.0484087653001488 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| prizepicks|15865014 | prizepicks | Mattia Bellucci | Total Games Won | under | 0.0481533361077964 | 2026-10-18T04:33:13Z | 2026-10-19T02:00:00.000-04:00 |
| underdog|2455b278-bf83-4974-ae73-d7cc8aa2c796 | underdog | Petey Halpin | Hits + Runs + RBIs | over | 0.0462920891285554 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|eb5303f8-f1a3-41c1-992a-23560decb427 | underdog | Victor Mesa | RBIs | over | 0.0460054571990607 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|d563533e-93ce-48ba-8058-f64b64c95573 | underdog | Junior Caminero | Batter Walks | over | 0.0449511016849298 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|a8261b54-b271-49bc-b2ad-fc3146869a5b | underdog | Jonathan Aranda | Batter Walks | over | 0.04321572341937 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|bfc377ac-3446-4a3e-bf1d-0d8e589d52f5 | underdog | Steven Kwan | RBIs | under | 0.0429553264604811 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|cf35b696-eddc-405d-a92c-9080b0b4184f | underdog | Kaelon Black | Receiving Yards | over | 0.0425272702416632 | 2026-10-18T04:33:13Z | 2026-10-20T00:15:00Z |
| underdog|ba0841ad-0f8f-4aef-8a59-d43699a62651 | underdog | Ashlyn Krueger | Double Faults | under | 0.0419540885710685 | 2026-10-19T04:39:53Z | 2026-10-19T05:10:00Z |
| underdog|60bfb729-486a-4dfd-88b2-25d697e2b09a | underdog | Walker Eget | Pass TDs | over | 0.0416200699641525 | 2026-10-19T04:39:53Z | 2026-10-23T23:00:00Z |
| underdog|daaa18c9-97e9-4360-b6bc-51e14b677f78 | underdog | José Ramírez | Hits | over | 0.0413743305053191 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|26cef225-82c3-4d11-83bf-331a114deafe | underdog | Nathaniel Lowe | Hits | over | 0.0411305761641253 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|3949b9f7-f2f0-409d-b45b-379ac68a155b | underdog | Taylor Walls | Hits + Runs + RBIs | over | 0.0409095883181092 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|e0a77b3e-fffe-496a-8826-c4becfed9924 | underdog | Sergio Camello | Shots Attempted | over | 0.0406532402784616 | 2026-10-19T04:39:53Z | 2026-10-19T19:00:00Z |
| prizepicks|15889915 | prizepicks | Ann Li | Total Games | over | 0.0395168655381616 | 2026-10-19T04:39:53Z | 2026-10-19T22:30:00.000-04:00 |
| underdog|5613e792-e44c-48d0-b58b-8b64bb39e5ef | underdog | Brayan Rocchio | Hits + Runs + RBIs | over | 0.0393357799278372 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|6a3e8ec0-68e8-4f7b-83b1-16a013eca5d7 | underdog | Chandler Simpson | Runs | over | 0.0380369730017288 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| prizepicks|13976083 | prizepicks | Victor Wembanyama | Rebounds | over | 0.0374835925599008 | 2026-09-12T11:28:56Z | 2026-10-20T21:40:00.000-04:00 |
| prizepicks|15898946 | prizepicks | Stan Wawrinka | 1st Set Total Games Won | under | 0.037085438867904 | 2026-10-19T04:39:53Z | 2026-10-20T05:00:00.000-04:00 |
| underdog|a48c3549-d6cf-4d08-a902-0fd86f858ff1 | underdog | Steven Kwan | Hits | over | 0.0370454430955765 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|818ac172-0731-46ae-b1e4-987ef153fe76 | underdog | José Ramírez | Total Bases | over | 0.0361422497100888 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|7cbe28b4-009c-4072-9ab1-492275f541d6 | underdog | Paul Mendy | Shots on Target | under | 0.0359344207126597 | 2026-10-16T04:33:49Z | 2026-10-19T16:30:00Z |
| prizepicks|15890799 | prizepicks | Katarzyna Kawa | Total Games Won | over | 0.0351657615789161 | 2026-10-19T04:39:53Z | 2026-10-19T22:00:00.000-04:00 |
| prizepicks|13975911 | prizepicks | Jayson Tatum | Assists | over | 0.0344807325358837 | 2026-09-12T11:28:56Z | 2026-10-20T15:10:00.000-04:00 |
| prizepicks|15884632 | prizepicks | Fabian Marozsan | Total Games | over | 0.0341429999953971 | 2026-10-19T04:39:53Z | 2026-10-20T02:30:00.000-04:00 |
| underdog|2851bf99-6b61-412c-817f-ce127de6ddb9 | underdog | Nathaniel Lowe | Batter Walks | under | 0.0335044254940791 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| underdog|83b919df-e9d8-4ed8-b8cd-301f340f528c | underdog | Yandy Díaz | Hits | over | 0.0331435939567932 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
| prizepicks|15869847 | prizepicks | Titouan Droguet | Total Games | over | 0.0328003587292179 | 2026-10-18T04:33:13Z | 2026-10-19T05:00:00.000-04:00 |
| prizepicks|15896905 | prizepicks | Alex Michelsen | Total Games | over | 0.0325513797649851 | 2026-10-19T04:39:53Z | 2026-10-19T09:30:00.000-04:00 |
| underdog|4cc79c33-4a88-4ce6-a767-6b89ca4dac71 | underdog | Patrick Bailey | Hits | over | 0.0314764217426378 | 2026-10-19T04:39:53Z | 2026-10-20T00:08:00Z |
