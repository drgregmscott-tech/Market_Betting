# Pipeline Digest -- 2026-11-12T07:01:18Z

## Run summary
- Ingestion: 34371 rows (PrizePicks OK, Underdog OK)
- Estimation: 34371 rows estimated (from 34371 ingested props)
- CLV logging: 153 newly flagged, 0 newly closed, 755 still open (111012 total ever logged)

## Currently open flags
Sizing is a manual step (sizing_engine.py, Session 2.6) -- this table is what to scan to pick a pair worth sizing.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_edge | first_flagged_at | game_start_time |
|---|---|---|---|---|---|---|---|
| underdog|7f283249-7197-4320-966d-81114f429326 | underdog | Brandon McManus | Kicking Points | under | 0.4606060606060607 | 2026-11-12T07:07:56Z | 2026-11-15T21:05:00Z |
| underdog|852bdd5d-c436-40d0-86a8-84a59a2603af | underdog | Corey Kiner | Receptions | under | 0.4379075544164731 | 2026-11-11T06:09:33Z | 2026-11-15T14:30:00Z |
| underdog|80b3909d-45a5-4709-a8c3-38fcc77ad55c | underdog | Ben Sinnott | Receiving Yards | over | 0.40580057649126494 | 2026-11-11T06:09:33Z | 2026-11-13T01:15:00Z |
| underdog|5d66d040-96e3-4bb1-a05d-21919c0e925d | underdog | Justin Herbert | Pass Yards | under | 0.4 | 2026-11-12T07:07:56Z | 2026-11-17T01:15:00Z |
| underdog|053c3e50-6f32-466c-a249-84cee7048674 | underdog | Drew Lock | Pass Yards | under | 0.4 | 2026-11-11T22:47:13Z | 2026-11-15T21:05:00Z |
| underdog|6f7ce7ad-c378-4a2c-8288-e319a03afa27 | underdog | Lan Larison | Rush + Rec Yards | under | 0.4 | 2026-11-12T07:07:56Z | 2026-11-15T14:30:00Z |
| underdog|02236b14-ee6c-4f53-aa2b-4cc4244da560 | underdog | Drew Lock | Pass Attempts | under | 0.4 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|bd4195f9-d156-43b9-b229-f6dc8a9320ea | underdog | Brock Purdy | Pass Yards | under | 0.4 | 2026-11-11T06:09:33Z | 2026-11-15T21:25:00Z |
| underdog|f2bd5807-d1b0-4e49-aa0c-e9b7b92b497e | underdog | Dak Prescott | Pass Yards | under | 0.4 | 2026-11-11T16:13:16Z | 2026-11-15T21:25:00Z |
| underdog|e6543c89-d139-402a-be7b-4d5cb96ea168 | underdog | Josh Allen | Pass Yards | under | 0.4 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|2e87c175-9d1b-4753-bcff-d0876fa22d9d | underdog | Michael Penix | Pass Yards | under | 0.4 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|9e59b83b-5938-4c25-a018-11ba32864fe6 | underdog | Trevor Lawrence | Pass Yards | under | 0.4 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|146a5d3b-156f-4cb2-9957-793d78599811 | underdog | Aaron Rodgers | Pass Yards | under | 0.4 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|f3d5950a-1810-46f2-8ce2-a87e2affd8ff | underdog | King Miller | Receiving Yards | over | 0.4 | 2026-11-11T06:09:33Z | 2026-11-14T20:30:00Z |
| underdog|efb1059f-f136-4794-9a72-10de9d0a03a4 | underdog | Zach Charbonnet | Receiving Yards | under | 0.397859065932332 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|bf3b1159-fa11-42f9-ae28-7421be127235 | underdog | Eddy Pineiro | FG Made | under | 0.3826019825177006 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|f6ceb32d-c4b6-45e0-8097-a8cb64b11d1d | underdog | Drake Maye | Pass Yards | under | 0.3824554487729366 | 2026-11-11T16:13:16Z | 2026-11-15T14:30:00Z |
| underdog|187d6b13-fe43-46da-92bc-1770118291d9 | underdog | Simi Fehoko | Receiving Yards | under | 0.38019485256498564 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|08345c52-8552-4b04-813c-2f46ea4286f3 | underdog | Simi Fehoko | Receptions | under | 0.3799490814604448 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|909a895e-c402-4ce5-8f15-1633330541fb | underdog | Cam Ward | Pass Yards | under | 0.379731507012816 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|56efce95-8447-437f-9002-eae46ec70c0e | underdog | Lan Larison | Rush Yards | under | 0.3760016835987935 | 2026-11-12T07:07:56Z | 2026-11-15T14:30:00Z |
| underdog|9b68965c-3c26-46a8-baae-a65e2eecf9ad | underdog | Brandon McManus | FG Made | under | 0.35442585143255134 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| prizepicks|16869254 | prizepicks | Dominik Livakovic | Goalie Saves | under | 0.35094246505677495 | 2026-11-11T06:09:33Z | 2026-11-12T14:45:00.000-05:00 |
| prizepicks|16864061 | prizepicks | Jack Endries | Rec Yards | over | 0.35094246505677495 | 2026-11-11T06:09:33Z | 2026-11-15T20:20:00.000-05:00 |
| prizepicks|16834519 | prizepicks | Justin Herbert | Pass Yards | under | 0.35094246505677495 | 2026-11-10T12:33:48Z | 2026-11-16T20:15:00.000-05:00 |
| prizepicks|16834515 | prizepicks | Brock Purdy | Pass Yards | under | 0.35094246505677495 | 2026-11-10T12:33:48Z | 2026-11-15T16:25:00.000-05:00 |
| prizepicks|16834516 | prizepicks | Dak Prescott | Pass Yards | under | 0.35094246505677495 | 2026-11-10T12:33:48Z | 2026-11-15T16:25:00.000-05:00 |
| underdog|1a25507b-8125-4524-83eb-bd6dc420d8a6 | underdog | Jared Goff | Pass Yards | under | 0.3501184306337788 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|7ba17254-22b1-4b2c-9b2c-4eacf8338ebe | underdog | Michael Penix | Pass Attempts | under | 0.3427792036855505 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|5f6ecb8a-85b5-407a-ae58-df231bcd0038 | underdog | Bryce Young | Pass Yards | under | 0.33872136607667247 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|93bae4ac-e88e-42e6-b4b5-5b91cb563f7a | underdog | J.J. McCarthy | Pass Yards | under | 0.33389019760909844 | 2026-11-12T07:07:56Z | 2026-11-13T01:15:00Z |
| underdog|67efd67a-f251-4885-adb0-7eff9290b91e | underdog | Lan Larison | Receiving Yards | under | 0.33313315774229646 | 2026-11-12T07:07:56Z | 2026-11-15T14:30:00Z |
| underdog|c2a5c1ca-7520-4e9d-89e0-2f5050979d68 | underdog | Kirk Cousins | Pass Yards | under | 0.32486137327291564 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|5a8bc524-564a-4dab-a5db-95d4d162a85c | underdog | Patrick Mahomes | Pass Yards | under | 0.32398040614566614 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|88972dce-ca5d-40a3-88f8-6f384bd19f6a | underdog | Jayden Daniels | Pass Yards | under | 0.3233669077252188 | 2026-11-12T07:07:56Z | 2026-11-13T01:15:00Z |
| underdog|f9978ce2-db4f-472d-ae6b-7ae2ed4383c0 | underdog | Brock Purdy | Pass Attempts | under | 0.3095759047079447 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|b9826de6-517b-421f-aedc-9cd8b490bd07 | underdog | J.J. McCarthy | Pass TDs | under | 0.3081632653061225 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| underdog|00efed34-b5f2-4951-abad-8c8793e5c954 | underdog | Joe Burrow | Pass Yards | under | 0.3079937259333765 | 2026-11-12T07:07:56Z | 2026-11-16T01:20:00Z |
| underdog|fabc095d-0fa4-4eaa-be92-d8b57374fd64 | underdog | Geno Smith | Pass Yards | under | 0.3054135648235081 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| prizepicks|16834512 | prizepicks | Bryce Young | Pass Yards | under | 0.3052224897990242 | 2026-11-10T12:33:48Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|a4aff594-458d-4ab2-8741-d573c94fd29c | underdog | Tyler Shough | Pass Yards | under | 0.30396344221607396 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|97851d28-d152-45e8-b8be-e5917cdbe963 | underdog | Stefon Diggs | Receiving Yards | under | 0.30220112942827204 | 2026-11-12T07:07:56Z | 2026-11-13T01:15:00Z |
| underdog|73de581b-eac8-4c44-88e3-7998a70fce36 | underdog | Deshaun Watson | Pass Yards | under | 0.29953009358284066 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|be878b70-3c21-471e-ae3b-905d8c13efb6 | underdog | Daniel Jones | Pass Yards | under | 0.29807473152035446 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|04d9b629-2110-40ef-b134-82649932148a | underdog | Jacoby Brissett | Pass Yards | under | 0.2979783699769716 | 2026-11-12T07:07:56Z | 2026-11-17T01:15:00Z |
| prizepicks|16869672 | prizepicks | Jayden Daniels | Pass+Rush+Rec TDs | under | 0.2956782151280245 | 2026-11-11T06:09:33Z | 2026-11-12T20:15:00.000-05:00 |
| underdog|017de95e-24a8-4a55-9185-759ab5e39785 | underdog | Drake Maye | Pass Attempts | under | 0.2870204978984535 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|b5fb6661-40fc-4196-9686-d21c10809596 | underdog | Bryce Young | Pass Attempts | under | 0.2854974352714704 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|2b554710-678c-443f-bb14-2208a77f507c | underdog | Justin Herbert | Pass Attempts | under | 0.2847606859755615 | 2026-11-11T22:47:13Z | 2026-11-17T01:15:00Z |
| underdog|0bb6f8ee-7e48-4b03-a068-ba21652a6af6 | underdog | Christian McCaffrey | Rush + Rec Yards | under | 0.27813991747146116 | 2026-11-11T06:09:33Z | 2026-11-15T21:25:00Z |
| prizepicks|16834509 | prizepicks | Geno Smith | Pass Yards | under | 0.2763361682548745 | 2026-11-10T12:33:48Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|cae65947-99bd-4320-b592-67e741e8e3f3 | underdog | Cam Ward | Pass Attempts | under | 0.27575003596339265 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|e7b1ef0e-7cb3-4ac8-a525-bc2f937cd6d6 | underdog | Deshaun Watson | Pass Attempts | under | 0.2741744640843222 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|c8b72634-2199-44b4-918c-14b8b75a5665 | underdog | Josh Allen | Pass Attempts | under | 0.27359287330136317 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|4426e732-6666-4dad-8847-df60408b6e0e | underdog | Eddy Pineiro | Kicking Points | under | 0.27246339729437163 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|32431b7b-bc1f-4591-bb5c-40d5aa435fcf | underdog | Jayden Daniels | Pass Attempts | under | 0.27080781658432496 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| prizepicks|16864050 | prizepicks | Brock Wright | Rec Yards | over | 0.26570772133930776 | 2026-11-11T06:09:33Z | 2026-11-15T09:30:00.000-05:00 |
| underdog|a7f2cda3-7806-4825-94cb-3314772c5a43 | underdog | Mike Washington | Receiving Yards | over | 0.26259620989363885 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|8cf0d860-c740-4aa8-b1fe-3ddfdeff4a17 | underdog | Antonio Williams | Receptions | under | 0.2540644281719815 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| prizepicks|16864049 | prizepicks | Tyler Conklin | Rec Yards | over | 0.2534382625358713 | 2026-11-11T06:09:33Z | 2026-11-15T09:30:00.000-05:00 |
| underdog|7e50f8a8-2469-4c42-8b1b-a4594a66ff81 | underdog | C.J. Stroud | Pass Yards | under | 0.2501195185787335 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|fe8292b1-ce05-486d-b732-66142a05472c | underdog | Andy Borregales | FG Made | under | 0.2485620967855957 | 2026-11-11T06:09:33Z | 2026-11-15T14:30:00Z |
| underdog|580afe6a-a30e-4f45-9c8e-e5c5a1a14817 | underdog | J.J. McCarthy | Pass Attempts | under | 0.24770970756895838 | 2026-11-12T07:07:56Z | 2026-11-13T01:15:00Z |
| underdog|7279c326-d7e6-469c-9dd8-f0ec2a171e89 | underdog | Olamide Zaccheaus | Receiving Yards | under | 0.24593076762155852 | 2026-11-11T16:13:16Z | 2026-11-15T18:00:00Z |
| underdog|83373ed9-f9ce-45e1-9625-900830675049 | underdog | Luca Lombardo | XP Made | over | 0.24473454966597602 | 2026-11-11T06:09:33Z | 2026-11-14T20:30:00Z |
| underdog|6fd045da-e0dd-4ab0-8819-c11153822667 | underdog | Aaron Rodgers | Pass Attempts | under | 0.2422362767070224 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|5f2c5559-124b-4f6d-a460-9a9d59c40519 | underdog | Austin Ekeler | Rush + Rec Yards | under | 0.23690399366889536 | 2026-11-11T16:13:16Z | 2026-11-13T01:15:00Z |
| underdog|26d4ddfa-d9fc-4f08-86e6-a916620f7be4 | underdog | Jordan Love | Pass Yards | under | 0.2343087179750497 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|18257ea5-4768-4756-b29d-388462ad3bf5 | underdog | Corey Kiner | Rush + Rec Yards | under | 0.2324899829284336 | 2026-11-12T07:07:56Z | 2026-11-15T14:30:00Z |
| underdog|14b46430-d112-4bb9-8474-9f3e043c7262 | underdog | Kyle Pitts | Receiving Yards | under | 0.23074083814986768 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|ed57ccdb-f29c-4416-ae5f-4aded39dc014 | underdog | Andy Borregales | Kicking Points | under | 0.22609089805035 | 2026-11-12T07:07:56Z | 2026-11-15T14:30:00Z |
| underdog|bcd7b7ef-b301-42ef-a3a4-68a4441b0ee8 | underdog | Drew Mestemaker | Pass Yards | under | 0.22552583183104713 | 2026-11-12T07:07:56Z | 2026-11-15T02:30:00Z |
| underdog|6cd99d29-b2c1-46a8-9f9b-ef3d50cfb2fb | underdog | Jacobo Echeverria Lozano | FG Made | over | 0.22488673515002366 | 2026-11-11T22:47:13Z | 2026-11-15T00:30:00Z |
| underdog|ddfbe087-7837-4635-8b41-2fe2508e09cb | underdog | Chase Brown | Rush + Rec Yards | under | 0.2216543878483086 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|c056f71a-3a42-40b4-96f9-d2609cc9beed | underdog | Joe Burrow | Pass Attempts | under | 0.22141583740196058 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|169cb841-cffa-4109-8027-3415c4f4b563 | underdog | George Kittle | Receptions | under | 0.2194077839592593 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|1d59abaf-41f5-4b96-a4ed-b899acfcff7b | underdog | Ollie Gordon | Receiving Yards | under | 0.21813366412209023 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|1f2ebff3-f987-46d9-abc9-08ffeb81a54c | underdog | Jadarian Price | Rush Yards | under | 0.2178089223809373 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|9bfbce36-45b2-4344-ac93-eb0b12315080 | underdog | C.J. Stroud | Pass Attempts | under | 0.21600582785806877 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| prizepicks|16834513 | prizepicks | Tyler Shough | Pass Yards | under | 0.21404760098629738 | 2026-11-10T12:33:48Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|26141c16-4dd7-44ed-81fe-bda847b4c1f4 | underdog | Chuba Hubbard | Rush + Rec Yards | under | 0.21366490872884691 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|900a6acc-8f2e-4a73-8d6c-9a35b225cafb | underdog | Jared Goff | Pass Attempts | under | 0.2123603264736973 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|e3989919-ef82-4a61-b9bf-110eaf56d1db | underdog | Marta Kostyuk | Double Faults | under | 0.21027269034406948 | 2026-11-11T22:47:13Z | 2026-11-12T20:00:00Z |
| underdog|43eab978-b035-4b9e-91fe-97a8d57d94cb | underdog | Cooper Barkate | Receptions | under | 0.20979341100184778 | 2026-11-11T16:13:16Z | 2026-11-14T17:00:00Z |
| underdog|e94c9cd9-eb43-4a62-912e-a83f4184c727 | underdog | Trey McBride | Receptions | under | 0.20737779171812365 | 2026-11-12T07:07:56Z | 2026-11-15T21:05:00Z |
| underdog|34ffe77e-d083-49fe-a233-c2a7085b1a55 | underdog | Jordan Addison | Receptions | under | 0.20675489884434617 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|b1d2df50-d4e5-4b5a-bee1-6ae33e6b16ca | underdog | Reggie Virgil | Receiving Yards | under | 0.20622426514850978 | 2026-11-11T22:47:13Z | 2026-11-15T21:05:00Z |
| underdog|f56ab5cd-5f1b-4cfa-9d0b-04814d327fb1 | underdog | Woody Marks | Rush Yards | under | 0.20525939528062387 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|081218b4-9196-449c-9fdf-62d2d39e0e03 | underdog | Zane Gonzalez | Kicking Points | under | 0.2048077405855635 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|f8cde15a-8b1a-4730-848f-163f3f890c7d | underdog | George Kittle | Receiving Yards | under | 0.20443082432893867 | 2026-11-11T06:09:33Z | 2026-11-15T21:25:00Z |
| underdog|8a278f6d-96e4-480d-8e6c-314f6c27a8bb | underdog | Treylon Burks | Receptions | under | 0.20250077997706395 | 2026-11-11T06:09:33Z | 2026-11-13T01:15:00Z |
| underdog|c9f3747b-34ec-44e7-a3f7-ef6d5624f1e6 | underdog | Lan Larison | Receptions | under | 0.2024956727597459 | 2026-11-12T07:07:56Z | 2026-11-15T14:30:00Z |
| underdog|f90743a5-9d2a-47d3-a4e4-089c9764ad13 | underdog | Dak Prescott | Pass Attempts | under | 0.2011150399848315 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|b8f05002-fdd3-4c27-9de6-63ac37ce454e | underdog | Chris Rodriguez | Rush + Rec Yards | under | 0.20106576960368938 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|6170a823-3e05-4ebd-97d3-044e73ce874f | underdog | Christian McCaffrey | Rush Yards | under | 0.20034018401002118 | 2026-11-11T06:09:33Z | 2026-11-15T21:25:00Z |
| underdog|f1884e58-0528-49b7-b1dd-7d719390c4fc | underdog | Tramell Jones | Pass Yards | under | 0.1983246221978886 | 2026-11-12T07:07:56Z | 2026-11-14T23:15:00Z |
| underdog|8a1b591a-8990-49d6-b67d-de2ef4f6aacb | underdog | Rashee Rice | Receiving Yards | under | 0.1982963392264364 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|97f17a14-3d73-4de2-b8ed-5fe1812529d7 | underdog | Devonte Wyatt | Sacks | over | 0.1980309357726293 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|01a29c0e-6cd0-4916-8199-22ab69b235e1 | underdog | Corey Kiner | Rush Yards | under | 0.19730874045295632 | 2026-11-11T06:09:33Z | 2026-11-15T14:30:00Z |
| underdog|5066d8e1-f617-4f8b-ae0e-3354ea829f4a | underdog | Woody Marks | Rush + Rec Yards | under | 0.19725546483040635 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|e0ea43b7-986f-4181-bf2a-7e955fc62fcb | underdog | Anthony Colandrea | Pass Yards | under | 0.19725208384617943 | 2026-11-11T22:47:13Z | 2026-11-14T17:30:00Z |
| underdog|87bfd021-0498-4180-b485-15610037e2e5 | underdog | Kaelon Black | Receiving Yards | over | 0.1963921949855576 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|83b44129-9596-4ab7-910d-0d5b5037b4ab | underdog | Geno Smith | Pass Attempts | under | 0.19625166531744365 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|9eaa1edc-b002-4a7f-89ba-9aa687d5f074 | underdog | Stefon Diggs | Receptions | under | 0.19501378772836164 | 2026-11-11T22:47:13Z | 2026-11-13T01:15:00Z |
| underdog|3cf52d42-1fb6-47d6-904e-2dc8f9d0260f | underdog | Alonza Barnett | Pass Yards | under | 0.1949451400723652 | 2026-11-12T07:07:56Z | 2026-11-14T20:30:00Z |
| underdog|45eaa191-9cdc-463c-8d91-beefc80f7256 | underdog | Trevor Lawrence | Pass Attempts | under | 0.19395844303678533 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|e58d01fe-650d-4c2a-935c-96e3364cbfd2 | underdog | Jadarian Price | Rush + Rec Yards | under | 0.19375724072056666 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|df028c43-0eee-4273-830e-703d5cb09224 | underdog | Rachaad White | Rush Yards | under | 0.19157154630314255 | 2026-11-09T06:06:04Z | 2026-11-13T01:15:00Z |
| underdog|0ca5f198-cc15-4b12-b643-c3388a576202 | underdog | Tank Dell | Receptions | under | 0.19110284381179832 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|8bfeabc8-5299-494a-bfeb-85b8e61de674 | underdog | Daylyn Upshaw | Receptions | under | 0.1909920607875113 | 2026-11-11T16:13:16Z | 2026-11-14T17:00:00Z |
| underdog|37345e14-7b00-4714-8924-6d5839257691 | underdog | Billy Edwards Jr. | Pass Yards | under | 0.19041153920751197 | 2026-11-11T22:47:13Z | 2026-11-15T00:00:00Z |
| underdog|cf14b101-73f9-459c-bd0c-a86498e7b0f9 | underdog | Chris Rodriguez | Rush Yards | under | 0.18966095244098113 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| prizepicks|16864052 | prizepicks | Jackson Hawes | Rec Yards | over | 0.18803943875076268 | 2026-11-11T06:09:33Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|5bf588f4-9870-42b6-ad22-136e7d274837 | underdog | Bo Jackson | Rush Yards | under | 0.1860119693418283 | 2026-11-12T07:07:56Z | 2026-11-14T17:00:00Z |
| underdog|f4b1fd7b-145b-4e27-a9a4-39d2661cd5bd | underdog | Antonio Williams | Receiving Yards | under | 0.18591255763519654 | 2026-11-11T16:13:16Z | 2026-11-13T01:15:00Z |
| underdog|2fdd7b6e-347f-455f-8250-81c6c752a728 | underdog | Seth McGowan | Rush + Rec Yards | under | 0.1855411744664197 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|1e0b9273-b720-4a4b-9515-b69d611e23d5 | underdog | Zach Charbonnet | Rush + Rec Yards | under | 0.18394252594257776 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|0c90304b-97a9-4467-9736-313bc4155ac0 | underdog | Khalil Herbert | Rush Yards | under | 0.18354154495685115 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|145d0e7c-ebc2-4247-b8cd-ed5b0d92a96b | underdog | Ja'Marr Chase | Receiving Yards | under | 0.1833658811737735 | 2026-11-11T22:47:13Z | 2026-11-16T01:20:00Z |
| underdog|336befd7-fc3b-4fc6-be96-8f9f930dd43f | underdog | Jared Goff | Pass TDs | under | 0.1828305718973564 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|dfb1d829-da70-4da9-b657-ce5db7693f70 | underdog | Germie Bernard | Receiving Yards | under | 0.18255479380802853 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|2b2e87a1-8e51-41ec-9150-0c85b01fabcd | underdog | Tyler Warren | Receiving Yards | under | 0.1823268415850886 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|eb1c3c80-366a-4251-99fb-356251e8356f | underdog | Evan McPherson | FG Made | under | 0.18227554836779813 | 2026-11-11T16:13:16Z | 2026-11-16T01:20:00Z |
| prizepicks|16834801 | prizepicks | Kyle Pitts Sr. | Rec Yards | under | 0.1816833032066426 | 2026-11-10T12:33:48Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|f1ae34e8-674a-4744-a233-47c5f2216dd4 | underdog | Cam Ward | Pass TDs | under | 0.18083709268551018 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|c80fe49f-2c7d-4a01-bc9e-cb7b5e9546c4 | underdog | Steven Blanco | Rush Yards | under | 0.1808163492001581 | 2026-11-11T22:47:13Z | 2026-11-13T02:00:00Z |
| underdog|1e44ad53-a87f-4f4a-94f4-e818c147ca95 | underdog | Theo Melin Ohrstrom | Receiving Yards | over | 0.1806993957708365 | 2026-11-11T16:13:16Z | 2026-11-14T17:00:00Z |
| prizepicks|16864048 | prizepicks | John Bates | Rec Yards | over | 0.17898850698989321 | 2026-11-11T06:09:33Z | 2026-11-12T20:15:00.000-05:00 |
| prizepicks|16864055 | prizepicks | Blake Whiteheart | Rec Yards | over | 0.17800572418642757 | 2026-11-11T06:09:33Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|7d00d658-4fce-45ec-af18-37f320044289 | underdog | Austin Ekeler | Rush Yards | under | 0.17732770025327427 | 2026-11-11T16:13:16Z | 2026-11-13T01:15:00Z |
| underdog|607f5ae6-2116-4003-99af-5442503e0ae4 | underdog | Brock Purdy | Pass TDs | under | 0.17680376455348845 | 2026-11-11T06:09:33Z | 2026-11-15T21:25:00Z |
| underdog|ab208bdb-ddee-40f9-a2ed-f481ef72f216 | underdog | Drake London | Receptions | under | 0.17466437471048346 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|a75630ea-2383-47b7-8fae-6f061466e02d | underdog | John Mateer | Pass Yards | under | 0.17389307925246578 | 2026-11-11T06:09:33Z | 2026-11-14T21:15:00Z |
| underdog|8d4c7f07-fbef-47e3-9190-395925538167 | underdog | Zach Charbonnet | Rush Yards | under | 0.17380685630828774 | 2026-11-12T07:07:56Z | 2026-11-15T21:05:00Z |
| underdog|bed83661-cc7d-4b22-9b07-e0978ada4d5d | underdog | Jameson Williams | Receiving Yards | under | 0.1733097016002607 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|b59c83a6-7075-4cc3-84dd-27157fa643ac | underdog | Jahan Dotson | Receptions | under | 0.17063963423916995 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|bae18339-057c-4c73-8714-0a71b2b67ad7 | underdog | Charles Omenihu | Sacks | over | 0.1698741006068713 | 2026-11-11T06:09:33Z | 2026-11-13T01:15:00Z |
| prizepicks|16864057 | prizepicks | Oscar Delp | Rec Yards | over | 0.16971647479255814 | 2026-11-11T06:09:33Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|4e9d2b81-8437-409b-8ff4-2380820c1bc4 | underdog | Gianni Spetic | XP Made | over | 0.1690686381121324 | 2026-11-11T16:13:16Z | 2026-11-15T00:30:00Z |
| underdog|ee9a0405-33bb-456d-a2ef-754c6c2c03a7 | underdog | Tyler Shough | Pass Attempts | under | 0.1678377974371722 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|696c6b73-3e04-426b-a463-26276c4aee5c | underdog | Ryan Fitzgerald | FG Made | under | 0.16692795074675848 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|c97d330b-3d6f-4b03-83d5-f93c56394bed | underdog | Ollie Gordon | Rush + Rec Yards | under | 0.16641302347698494 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| prizepicks|16913746 | prizepicks | Vanja Milinkovic-Savic | Goalie Saves | under | 0.16609088018417573 | 2026-11-12T07:07:56Z | 2026-11-13T14:45:00.000-05:00 |
| underdog|ab3ca458-4792-4be4-86cf-cfcefafc1532 | underdog | Walker Eget | Pass Yards | under | 0.1656176011824837 | 2026-11-12T07:07:56Z | 2026-11-14T17:00:00Z |
| underdog|2c34ae7b-b85c-4936-9401-388dc41d3f04 | underdog | Breece Hall | Rush + Rec Yards | under | 0.16536584934937237 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|b81b56da-fe21-4e55-9f3d-fb0b1d061257 | underdog | Daniel Jones | Pass Attempts | under | 0.16440373749700898 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|659b286c-687a-43f0-b782-5a1234a05458 | underdog | Quinshon Judkins | Receptions | over | 0.16431586645270752 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|bc140f8f-77f3-4c5f-8bbd-c0f4d0769e0e | underdog | Jordan Mason | Rush + Rec Yards | under | 0.16218107970493112 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|f45737d6-5d7b-4255-837e-cbbc6b1583dd | underdog | Corey Kiner | Receiving Yards | under | 0.16208668186718833 | 2026-11-12T07:07:56Z | 2026-11-15T14:30:00Z |
| underdog|d3bf740e-28cf-4c5b-bdf6-b9b00b2f186a | underdog | Ja'Kobi Lane | Receiving Yards | under | 0.16167281192514082 | 2026-11-11T22:47:13Z | 2026-11-17T01:15:00Z |
| underdog|b9338725-50fc-40f4-8453-1eca37fc7ec6 | underdog | Austin Ekeler | Receptions | under | 0.1614508530669193 | 2026-11-09T06:06:04Z | 2026-11-13T01:15:00Z |
| prizepicks|16834640 | prizepicks | Woody Marks | Rush Yards | under | 0.16140868621854165 | 2026-11-10T12:33:48Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|5d9334d9-a335-471c-92f4-54bd683075ca | underdog | Hank Brown | Pass Yards | under | 0.16133319573176919 | 2026-11-11T06:09:33Z | 2026-11-15T00:30:00Z |
| underdog|9a9b4886-cd1f-4523-9dc3-cd8753a51f8b | underdog | Kirk Cousins | Pass Attempts | under | 0.16130209940228557 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|43d067f1-bb0f-4c09-acf1-fa7919bc9723 | underdog | Jared Goff | Rush Yards | over | 0.16011142578061638 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|a2bd1b57-9bee-4a1a-a27a-1cbfdd5681b8 | underdog | Elic Ayomanor | Receptions | under | 0.15978654253309588 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|0d051be2-f5ae-4b14-b42e-964de378c630 | underdog | Katin Houser | Pass TDs | over | 0.15938089279781648 | 2026-11-11T06:09:33Z | 2026-11-14T02:00:00Z |
| underdog|28e41540-e6d5-4ec1-b474-b3fb179168ec | underdog | Justin Herbert | Pass TDs | under | 0.1593713737739526 | 2026-11-10T12:33:48Z | 2026-11-17T01:15:00Z |
| underdog|3e4ae174-e4d9-4c59-b781-2aa8bc07c297 | underdog | Wayne Knight | Receiving Yards | over | 0.15917827448977762 | 2026-11-11T06:09:33Z | 2026-11-14T02:00:00Z |
| underdog|750a9a76-0db3-4590-9b8c-3906d9640c3e | underdog | Deebo Samuel | Receiving Yards | under | 0.15915891094208723 | 2026-11-11T22:47:13Z | 2026-11-15T21:25:00Z |
| underdog|f96a368b-744f-47f4-bd47-9731731f5d1b | underdog | Caden Buhr | FG Made | over | 0.15900548451896535 | 2026-11-11T16:13:16Z | 2026-11-15T00:30:00Z |
| prizepicks|16834646 | prizepicks | Christian McCaffrey | Rush Yards | under | 0.15848722202295062 | 2026-11-10T12:33:48Z | 2026-11-15T16:25:00.000-05:00 |
| underdog|f3733138-10af-46da-8e69-cf5ca4b940fc | underdog | Reggie Virgil | Receptions | under | 0.15825220568688703 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|d4535591-3a5f-4c28-b756-d85acd4fdf77 | underdog | Jordan Mason | Rush Yards | under | 0.15679467436665007 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| prizepicks|16864059 | prizepicks | Ian Thomas | Rec Yards | over | 0.15662706211871924 | 2026-11-11T06:09:33Z | 2026-11-15T16:05:00.000-05:00 |
| underdog|25185fe8-2e75-4f8e-a1b5-f6c471df1357 | underdog | Arch Manning | Pass TDs | over | 0.15631529903366037 | 2026-11-12T07:07:56Z | 2026-11-15T00:30:00Z |
| underdog|34592e3c-3b83-4af7-bd2b-617a52ca4334 | underdog | Trey McBride | Receiving Yards | under | 0.15553372270182042 | 2026-11-12T07:07:56Z | 2026-11-15T21:05:00Z |
| underdog|eb8162e7-e14c-4796-b160-d74fedaa7315 | underdog | Jordan Love | Pass Attempts | under | 0.1550294298047722 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|2531c206-f92d-4af6-9db2-55f5d500565f | underdog | Jessica Pegula | Double Faults | under | 0.15491358343596984 | 2026-11-11T22:47:13Z | 2026-11-12T21:10:00Z |
| underdog|97a67afc-3f9f-4982-8bae-be868c2c4737 | underdog | Devon Dampier | Pass Yards | under | 0.15303323942761993 | 2026-11-10T12:33:48Z | 2026-11-15T00:30:00Z |
| underdog|585b41b2-1294-443c-8440-2524471c4ddf | underdog | Laquon Treadwell | Receptions | under | 0.15250354276005051 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|0b6b9464-f3ca-4d21-bb53-19e9a2f9619a | underdog | Karl Brooks | Sacks | over | 0.15173315822223826 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|abcda181-8a45-42d8-bd51-8479c62c0cba | underdog | Holden Geriner | Pass TDs | under | 0.15167357913948876 | 2026-11-12T07:07:56Z | 2026-11-14T00:00:00Z |
| prizepicks|16849017 | prizepicks | Ty Dieffenbach | Rush Atts | under | 0.15134416123436234 | 2026-11-11T06:09:33Z | 2026-11-13T21:00:00.000-05:00 |
| underdog|4c954135-93e5-4714-8cdb-20d4324aaf2c | underdog | Matthew Stafford | Pass Yards | under | 0.15126279267854992 | 2026-11-12T07:07:56Z | 2026-11-15T21:05:00Z |
| underdog|c5c4fe7e-563e-4a77-ae50-060011c7dec8 | underdog | Xavier Hutchinson | Receptions | under | 0.1509666630300549 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|2e165ef5-272e-47fb-8214-52bc9d58510a | underdog | Amon-Ra St. Brown | Receptions | under | 0.14980442293467233 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|c6f5d95f-2b53-4656-bed1-792f520c72ba | underdog | Garrett Wilson | Receiving Yards | under | 0.14922011393352663 | 2026-11-11T16:13:16Z | 2026-11-15T18:00:00Z |
| underdog|e3317ebd-1d1a-4ac2-8dc1-999860638691 | underdog | Jameson Williams | Receptions | under | 0.1486746602368635 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|1a20f785-f85c-4e70-a420-adf5f0ed3164 | underdog | Ollie Gordon | Receptions | under | 0.148665850420447 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|7d76e9dd-5308-4c1a-ba1c-ba61b79e4408 | underdog | Jayden Maiava | Pass TDs | over | 0.14850033842731425 | 2026-11-11T22:47:13Z | 2026-11-14T20:30:00Z |
| underdog|3dd60339-cf17-45f0-b767-75c894f95225 | underdog | Cooper Barkate | Receiving Yards | under | 0.14832914398251418 | 2026-11-11T16:13:16Z | 2026-11-14T17:00:00Z |
| underdog|48062c02-a233-40fe-af0c-50fbb3849543 | underdog | Kyren Williams | Rush Yards | under | 0.14807568252359582 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|36662c72-eeb6-4098-8bda-06fdddb4bea7 | underdog | Jayden Daniels | Pass TDs | under | 0.1470544440824959 | 2026-11-09T06:06:04Z | 2026-11-13T01:15:00Z |
| underdog|7281e3b0-a702-402a-8b62-fc9add59bf36 | underdog | Chuba Hubbard | Rush Yards | under | 0.14389175335524607 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|4d0e9f33-30c1-4cbd-811b-3f0d61054bcb | underdog | Amon-Ra St. Brown | Receiving Yards | under | 0.14378965381475595 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|719da097-fa73-4b52-b900-3a7aeae402b9 | underdog | Parker Washington | Receiving Yards | under | 0.1436428243105664 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|21ace0c9-85f0-43f3-9392-a8bbadc5666b | underdog | Trey Butkowski | XP Made | over | 0.14320322887137465 | 2026-11-10T12:33:48Z | 2026-11-14T20:30:00Z |
| underdog|4c42a4f7-59bd-4cc5-96de-2caa245cf96e | underdog | Ja'Marr Chase | Receptions | under | 0.14198666098231127 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| prizepicks|16863692 | prizepicks | Chig Okonkwo | Rec Targets | under | 0.14157234406143948 | 2026-11-11T06:09:33Z | 2026-11-12T20:15:00.000-05:00 |
| underdog|a8df2bfd-753f-497d-81c7-7d8c49469970 | underdog | Foster Moreau | Receptions | over | 0.14124636142536817 | 2026-11-11T16:13:16Z | 2026-11-15T18:00:00Z |
| underdog|9225cf3c-9296-4248-97ac-5b3485eb6a24 | underdog | George MacIntyre | Pass TDs | under | 0.14047384523423212 | 2026-11-11T06:09:33Z | 2026-11-14T20:00:00Z |
| underdog|f4f19588-e974-4225-ada4-1143b557d4d0 | underdog | Jake Fette | Pass Yards | under | 0.1403220874170037 | 2026-11-12T07:07:56Z | 2026-11-14T20:30:00Z |
| underdog|fe324cdb-30f6-4ec0-b83b-b7cfbc3bb25f | underdog | Zay Flowers | Receptions | under | 0.13889916886043374 | 2026-11-11T22:47:13Z | 2026-11-17T01:15:00Z |
| underdog|aa70ba25-a303-4c52-9769-639de476cfcf | underdog | Javonte Williams | Receptions | under | 0.13847697518960522 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|d916e27f-ed11-420a-9678-c3711e981147 | underdog | Christian Watson | Receptions | under | 0.13831813948612726 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|3fbbf17c-6590-4475-9308-dab985190711 | underdog | Carson Hilbert | FG Made | over | 0.1382509177214999 | 2026-11-11T22:47:13Z | 2026-11-15T00:00:00Z |
| underdog|6d60371c-a310-43a2-802d-e74a4a8e389d | underdog | Jordan Addison | Receiving Yards | under | 0.1379492017007241 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| prizepicks|16834820 | prizepicks | Christian McCaffrey | Rec Yards | under | 0.1379306598172515 | 2026-11-10T12:33:48Z | 2026-11-15T16:25:00.000-05:00 |
| underdog|588fc6ae-425e-491d-b220-d3d4a9b6e0c6 | underdog | Deshaun Watson | Pass TDs | under | 0.1378756465029044 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|2f8ac096-b1ae-46b1-9dc8-139b8e01de0d | underdog | Bhayshul Tuten | Rush Yards | under | 0.137098991003073 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|ea76791d-135e-4d10-bb38-5059c94eda28 | underdog | Ollie Gordon | Rush Yards | under | 0.13620307901154893 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|97a856d7-a3cf-475d-8612-0b72b87c6603 | underdog | Mark Fletcher Jr. | Rush Yards | under | 0.13600948649593914 | 2026-11-11T06:09:33Z | 2026-11-14T17:00:00Z |
| underdog|fe724bab-b489-4c4c-8b33-22905a3abcf6 | underdog | Caden Buhr | XP Made | under | 0.1356076785255077 | 2026-11-11T06:09:33Z | 2026-11-15T00:30:00Z |
| underdog|d16f08ba-8dcb-45d6-82db-c36a28ca4b50 | underdog | Tucker Kraft | Receiving Yards | under | 0.13538807270342912 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|f360ab27-deb2-4f72-b437-6349dc28e573 | underdog | Parker Washington | Receptions | under | 0.13510031202715655 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|170532ef-6942-4db9-8607-c52a3838bfe9 | underdog | James Cook | Rush + Rec Yards | under | 0.13472649314653207 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|846407d4-b764-4983-8cd7-df2f8d86efc0 | underdog | Rachaad White | Rush + Rec Yards | under | 0.13438874915938148 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| underdog|357567dd-807d-4205-8940-b5dbeb224c9d | underdog | Christian McCaffrey | Receiving Yards | under | 0.1337306969230765 | 2026-11-11T06:09:33Z | 2026-11-15T21:25:00Z |
| underdog|d1cdc236-e834-416d-ade8-355041f47ac5 | underdog | Wan'Dale Robinson | Receiving Yards | under | 0.13308967125429916 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| prizepicks|16864054 | prizepicks | Jonnu Smith | Rec Yards | over | 0.13268296711964045 | 2026-11-11T06:09:33Z | 2026-11-15T13:00:00.000-05:00 |
| prizepicks|16863714 | prizepicks | Ja'Marr Chase | Rec Targets | under | 0.13261008662572327 | 2026-11-11T06:09:33Z | 2026-11-15T20:20:00.000-05:00 |
| underdog|66cc5cae-122e-48a4-8cc9-fad2d8ca1650 | underdog | Isaiah Marshall | Pass Yards | under | 0.13253118034035682 | 2026-11-12T07:07:56Z | 2026-11-14T22:30:00Z |
| underdog|f0100902-2759-4817-a164-2c7d3cb0236d | underdog | Quinshon Judkins | Receiving Yards | over | 0.13251091684739158 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|bfaa3637-e14b-42cb-b21c-99de2b3e6335 | underdog | Isaiah Marshall | Pass TDs | under | 0.13239358925386258 | 2026-11-11T22:47:13Z | 2026-11-14T22:30:00Z |
| underdog|8475bce1-90cf-43c8-9bdc-19e950db157a | underdog | AJ Barner | Receptions | under | 0.1321036071433428 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|71c62c10-f79b-498b-8216-e91bac6da29c | underdog | James Cook | Rush Yards | under | 0.13204906398667315 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|ad49c1a3-20cd-48ee-8447-3f9c6b778470 | underdog | Zach Charbonnet | Receptions | under | 0.13186048887942314 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|c5d93fba-443f-4254-bbb2-c9a81bae6bd5 | underdog | Derrick Henry | Rush Yards | under | 0.1311683774303094 | 2026-11-11T22:47:13Z | 2026-11-17T01:15:00Z |
| underdog|7a1ed30d-da55-441c-b6f0-c5cf7618c573 | underdog | Ryan Fitzgerald | Kicking Points | under | 0.13110361173012197 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| prizepicks|16834805 | prizepicks | Tucker Kraft | Rec Yards | under | 0.13048896157966627 | 2026-11-10T12:33:48Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|5265ce9f-d1a4-4ac8-8168-2476d15b68b4 | underdog | Rashee Rice | Receptions | under | 0.13038787864818369 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|59fe561f-9bc0-4412-aec3-95aa5ef4cbee | underdog | Woody Marks | Receptions | under | 0.1300378289193116 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|693fb5e3-148f-43fc-b054-d44605b4d1fb | underdog | Kimani Vidal | Receptions | under | 0.12943283574984177 | 2026-11-11T22:47:13Z | 2026-11-17T01:15:00Z |
| underdog|f85b42b7-b4f4-4491-9134-48fc276d0f4f | underdog | Nico Collins | Receiving Yards | under | 0.12810938806580408 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|c7678b73-9c60-4770-9676-d99c5e6b71c7 | underdog | Khalil Shakir | Receptions | under | 0.12759270653403465 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|a9eefe92-2e1c-4030-a75a-b21c902814cd | underdog | Jack Bech | Receiving Yards | over | 0.12645017335002828 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|6316e5dc-af73-4c98-8b96-f7165729f535 | underdog | Jaylen Warren | Receptions | under | 0.1263299336202357 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|276bddde-b0e2-434a-9406-d85bb1c0cc43 | underdog | Thomas Castellanos | Pass Yards | under | 0.12618587761538758 | 2026-11-12T07:07:56Z | 2026-11-15T02:30:00Z |
| underdog|7d4a66d7-5e66-4433-b339-05c2970ccb9f | underdog | Josh Allen | Pass TDs | under | 0.12444210905973119 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|9b61aff8-a93b-4671-b173-f7ca4286eead | underdog | Jakobi Meyers | Receiving Yards | under | 0.12435976055640752 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|64fe717c-14a9-4a4d-b286-fb2c31130ca5 | underdog | Jason Myers | FG Made | under | 0.12423824312528586 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|7e047dba-151c-4432-9416-d4e3155ae527 | underdog | Jordan Mason | Receptions | under | 0.12364698409171138 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|56ae8193-af03-4241-adc6-f96292e6ffd7 | underdog | Thomas Castellanos | Pass TDs | under | 0.12341954518838927 | 2026-11-11T16:13:16Z | 2026-11-15T02:30:00Z |
| underdog|54563a9e-5de4-414c-953e-7d91ee3b7be0 | underdog | Laquon Treadwell | Receiving Yards | under | 0.1233374248618031 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|94c55bd4-7e31-4d47-b147-9078d5c53331 | underdog | Jahmyr Gibbs | Rush + Rec Yards | under | 0.12317941215822503 | 2026-11-12T07:07:56Z | 2026-11-15T14:30:00Z |
| underdog|7da7556c-a1f4-42ec-ad80-c12d0d953524 | underdog | John Metchie III | Receptions | under | 0.12299883356747898 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| prizepicks|16910337 | prizepicks | Marina Bassols Ribera | Total Games Won | over | 0.12260578502852104 | 2026-11-12T07:07:56Z | 2026-11-12T11:10:00.000-05:00 |
| underdog|f5a259bb-3160-42f7-8263-8e839fdce757 | underdog | Derrick Henry | Rush + Rec Yards | under | 0.12232246611646624 | 2026-11-10T12:33:48Z | 2026-11-17T01:15:00Z |
| prizepicks|16887420 | prizepicks | Dilin Jones | Rush Atts | under | 0.12214678937678047 | 2026-11-12T07:07:56Z | 2026-11-14T19:30:00.000-05:00 |
| underdog|c67debe0-d69c-4cc0-b1eb-a1ea1e46a21b | underdog | Holden Geriner | Pass Yards | under | 0.12205332361800525 | 2026-11-11T16:13:16Z | 2026-11-14T00:00:00Z |
| underdog|e0503240-c774-4033-be53-f5a5fd070e6a | underdog | Trey Butkowski | FG Made | under | 0.12199600122555099 | 2026-11-12T07:07:56Z | 2026-11-14T20:30:00Z |
| underdog|7a9e2c86-7dba-4c5b-bb6a-3ef5749dc1c0 | underdog | Zane Gonzalez | FG Made | under | 0.1218622688697637 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|cf37c889-4eca-4cd0-acdb-5ef3caf76c5b | underdog | Ka'imi Fairbairn | FG Made | under | 0.12158788342133897 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|b74d6dd8-986c-4d47-a602-c9563892a472 | underdog | Seth McGowan | Receptions | under | 0.12157868635609315 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|f50cd189-6177-4b69-b305-61d234a7a82e | underdog | Rico Dowdle | Rush + Rec Yards | under | 0.12075474357899663 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|a5e30ad8-1103-42c0-a807-c001b30ff2c9 | underdog | Cam Little | FG Made | under | 0.12040122477593274 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|45f18132-2bc5-4802-9392-b9791841f245 | underdog | DK Metcalf | Receiving Yards | under | 0.1202334887553217 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|c3fada5d-af9e-4279-ab31-41a9254bacc6 | underdog | Devin Singletary | Rush + Rec Yards | under | 0.12014054525619822 | 2026-11-11T16:13:16Z | 2026-11-13T01:15:00Z |
| underdog|a30f47b1-84fb-4c17-b39e-005dac8e7a59 | underdog | D.J. Crowther | Rush Yards | under | 0.12003151476269758 | 2026-11-11T22:47:13Z | 2026-11-13T01:00:00Z |
| underdog|61af56d0-7bbf-44b8-95db-df3abfd900b4 | underdog | Michael Salgado-Medina | FG Made | over | 0.11962802201761302 | 2026-11-11T06:09:33Z | 2026-11-15T00:30:00Z |
| underdog|92ebf7f8-a827-44b7-a6a0-6cb0155e27ab | underdog | Darius Alexander | Sacks | over | 0.11959188689290401 | 2026-11-11T22:47:13Z | 2026-11-13T01:15:00Z |
| underdog|3d9421b9-e254-462a-9b90-44104f1ffa6a | underdog | Devin Singletary | Rush Yards | under | 0.11951995810711802 | 2026-11-11T06:09:33Z | 2026-11-13T01:15:00Z |
| underdog|dd1d9caa-101d-491b-badf-bb1b87735495 | underdog | Jonathan Taylor | Receptions | under | 0.1194495485112097 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|941cffba-4b42-4435-8769-a31cbd72dc50 | underdog | Tee Higgins | Receptions | under | 0.11877140010710996 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|77d45d7c-6c80-4ce0-845e-806b3103525f | underdog | Jasen Lopez | Receiving Yards | under | 0.11852010308283689 | 2026-11-11T06:09:33Z | 2026-11-14T00:00:00Z |
| underdog|392f9965-7ffd-4004-90d0-e08fae23e980 | underdog | AJ Surace | Pass Yards | under | 0.11808429999697911 | 2026-11-11T22:47:13Z | 2026-11-14T17:30:00Z |
| underdog|c8dd15d3-4419-45ae-a884-55bd1290a78f | underdog | Garrett Wilson | Receptions | under | 0.11792466411828051 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| prizepicks|16897545 | prizepicks | Stefon Diggs | Recs | under | 0.11792445150048858 | 2026-11-11T16:13:16Z | 2026-11-12T20:15:00.000-05:00 |
| underdog|c7c1feb1-0d59-4f4b-a9e9-7f9535f0df33 | underdog | Drew Mestemaker | Pass TDs | under | 0.11768525797870777 | 2026-11-11T16:13:16Z | 2026-11-15T02:30:00Z |
| underdog|9829884f-362f-4681-83e4-5a8cf098d924 | underdog | Dilin Jones | Rush Yards | under | 0.11759848836835818 | 2026-11-11T16:13:16Z | 2026-11-15T00:30:00Z |
| underdog|185591e2-8a87-4901-a817-5630cf1e58ae | underdog | Jackson Harris | Receptions | under | 0.11759493096585649 | 2026-11-11T16:13:16Z | 2026-11-15T00:30:00Z |
| underdog|face495c-8a7b-4b62-80b6-39d56abbc869 | underdog | Jordan Mason | Receiving Yards | over | 0.1167924234086879 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|471b086b-8e30-4b89-8030-a31f346304fa | underdog | Bryce Young | Rush Yards | under | 0.11671082433541491 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|3614f11e-aa5b-4d51-9032-b3f195f419d5 | underdog | Jacobo Echeverria Lozano | XP Made | over | 0.1161780296945728 | 2026-11-11T06:09:33Z | 2026-11-15T00:30:00Z |
| underdog|9ed7031f-72d3-48dd-81cc-6bbc38cce66e | underdog | Deshaun Watson | Rush Yards | under | 0.11586021786103828 | 2026-11-11T16:13:16Z | 2026-11-15T18:00:00Z |
| underdog|05cea4b6-15b2-4343-bb42-af5bdce812a8 | underdog | Blake Corum | Rush Yards | under | 0.11585019001059815 | 2026-11-11T22:47:13Z | 2026-11-15T21:05:00Z |
| underdog|8a5385b8-b496-4dba-87cc-e3767c58614f | underdog | Kenny Minchey | Pass Yards | under | 0.11548018899212209 | 2026-11-12T07:07:56Z | 2026-11-14T23:15:00Z |
| underdog|2420a1ae-3693-4c18-900e-a72641811872 | underdog | David Olano | FG Made | over | 0.11523648181086699 | 2026-11-11T06:09:33Z | 2026-11-14T20:00:00Z |
| prizepicks|16913759 | prizepicks | Jan Oblak | Goalie Saves | under | 0.11465066373203547 | 2026-11-12T07:07:56Z | 2026-11-13T14:45:00.000-05:00 |
| underdog|4980e13b-b332-4cb3-b311-c8aada8c0159 | underdog | Kyle Pitts | Receptions | under | 0.11437219464215653 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|d5d3af12-7a46-4f9c-98c3-eabb7e53bef5 | underdog | Byrum Brown | Pass Yards | under | 0.11414423121368844 | 2026-11-12T07:07:56Z | 2026-11-14T17:00:00Z |
| underdog|912710d6-801a-4cea-a9cc-a23dd1fbe21d | underdog | Ryan Hopkins | Pass Yards | under | 0.1138700233908767 | 2026-11-12T07:07:56Z | 2026-11-14T17:00:00Z |
| underdog|345499c4-2a0f-45d8-b903-b3226f8487c4 | underdog | Tyler Bass | Kicking Points | under | 0.11383354828420944 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|5c625434-b11a-46c4-a6af-d0fc53c2f2a9 | underdog | Dak Prescott | Pass TDs | under | 0.11340998483490083 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|7a6dd424-2fdc-466c-b847-16a47251614c | underdog | Connor Calvert | FG Made | over | 0.11328783871436227 | 2026-11-10T12:33:48Z | 2026-11-14T17:00:00Z |
| underdog|7857c427-00ea-44f3-9c45-48f9e7f2c9b5 | underdog | Trevor Lawrence | Pass TDs | under | 0.11317375136374375 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|865ea4d0-9767-4b60-8c93-3d426d51d7a8 | underdog | Breece Hall | Rush Yards | under | 0.11314740643781795 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|2d0249ee-b511-4b0d-bdd1-0ad34ded2758 | underdog | Khalil Herbert | Receiving Yards | over | 0.11264275449455008 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|cde7c70e-d481-4784-9d2e-2a93b9e2daa7 | underdog | Sam LaPorta | Receiving Yards | under | 0.11256764743862924 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|6086e8d6-6e5f-4cb1-83ee-df3e5ba8bc8b | underdog | Jaxon Smith-Njigba | Receiving Yards | under | 0.1124110163923393 | 2026-11-12T07:07:56Z | 2026-11-15T21:05:00Z |
| underdog|c521d73c-2a75-4a75-9c17-33b2205da002 | underdog | Rico Dowdle | Rush Yards | under | 0.11217901116890283 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|992fa67a-feec-4626-95dc-f2c04f2580cf | underdog | Matthew Stafford | Rush Yards | over | 0.11213733898109268 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|461f158a-b95d-4759-b48d-ca72ea246c1d | underdog | Jadarian Price | Receptions | under | 0.1116533229738974 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|3b01acf2-eefa-4496-a642-bf1c849db45d | underdog | Chris Bell | Receptions | under | 0.11116746721824522 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|de8768ae-7ee5-4e32-ab45-429dd19fee48 | underdog | Germie Bernard | Receptions | under | 0.1107095928613796 | 2026-11-11T16:13:16Z | 2026-11-16T01:20:00Z |
| underdog|611d5095-8649-470d-aad5-f9b1d3f8f85c | underdog | David Olano | XP Made | over | 0.11008098092875374 | 2026-11-11T06:09:33Z | 2026-11-14T20:00:00Z |
| prizepicks|16870373 | prizepicks | Brock Bowers | Rec Targets | under | 0.10995797661937423 | 2026-11-11T06:09:33Z | 2026-11-15T16:05:00.000-05:00 |
| underdog|4291930c-2315-4596-8a5b-40abfdbeb026 | underdog | Chris Rodriguez | Receptions | under | 0.10885395637178386 | 2026-11-11T16:13:16Z | 2026-11-15T18:00:00Z |
| underdog|6822a773-5f4b-457d-a3c1-4ba92bff9865 | underdog | Junior Sherrill | Receptions | under | 0.10806956997685557 | 2026-11-11T22:47:13Z | 2026-11-14T17:45:00Z |
| underdog|aa5f1d28-afdc-4975-bab5-0fd74120e14b | underdog | Ben Sinnott | Receptions | over | 0.10803356032447303 | 2026-11-11T06:09:33Z | 2026-11-13T01:15:00Z |
| underdog|2d9a6fb5-8c84-46f0-bcba-b14291360099 | underdog | Bijan Robinson | Rush + Rec Yards | under | 0.1075619962096197 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|fd21faaf-bffa-4216-93db-e8f524c4e0f0 | underdog | Gianni Spetic | FG Made | over | 0.10755910381656675 | 2026-11-11T16:13:16Z | 2026-11-15T00:30:00Z |
| underdog|701546e2-a3db-41a7-bc5e-2ea885b7f872 | underdog | Pat Freiermuth | Receiving Yards | under | 0.10737055695636832 | 2026-11-11T16:13:16Z | 2026-11-16T01:20:00Z |
| prizepicks|16897138 | prizepicks | Thomas Castellanos | Rush Atts | under | 0.10724354939051584 | 2026-11-12T07:07:56Z | 2026-11-14T21:30:00.000-05:00 |
| underdog|f5efb384-ba2a-4a09-a8fa-fa8a6bc84578 | underdog | Omarion Hampton | Receiving Yards | over | 0.10634249279179786 | 2026-11-11T22:47:13Z | 2026-11-17T01:15:00Z |
| underdog|02dfa4d1-6864-4a3b-a333-800bb999bca2 | underdog | Kirk Cousins | Pass TDs | over | 0.10613134956836634 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|75dd150d-8eff-4c18-b540-1b016ef92bd3 | underdog | Michael Salgado-Medina | XP Made | over | 0.10580276525925403 | 2026-11-11T22:47:13Z | 2026-11-15T00:30:00Z |
| underdog|325a8205-94f4-4430-8e00-d9d2ddc2a9ec | underdog | Mike Gesicki | Receptions | under | 0.10565045023732611 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|8f9dcfd5-c39d-4c69-bed4-30b823291de4 | underdog | Thomas Castellanos | Rush Yards | under | 0.10548061656829655 | 2026-11-12T07:07:56Z | 2026-11-15T02:30:00Z |
| underdog|5644a858-15de-44fe-a1f7-0fd329feac31 | underdog | Javonte Williams | Rush + Rec Yards | under | 0.10415675245658362 | 2026-11-11T06:09:33Z | 2026-11-15T21:25:00Z |
| underdog|9b902c48-bdaf-41d6-a2bc-2a1798df028c | underdog | Matt Gay | Kicking Points | over | 0.10370064668973422 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|6a941d47-82e3-491e-9755-22dea3004ecd | underdog | Malik Nabers | Receptions | under | 0.10346829848265682 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| prizepicks|16863694 | prizepicks | Stefon Diggs | Rec Targets | under | 0.10325434302363778 | 2026-11-11T06:09:33Z | 2026-11-12T20:15:00.000-05:00 |
| underdog|077e30e4-9320-449b-a228-b1b97a8abd83 | underdog | Trey Smack | FG Made | under | 0.10289090955929303 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|9c43b165-9063-4640-8f8c-8e20683e481c | underdog | Terrance Carter | Receptions | under | 0.10281447863595972 | 2026-11-11T16:13:16Z | 2026-11-15T02:30:00Z |
| underdog|ef335d54-8710-47c6-86c5-e478aad1bf57 | underdog | Blake Corum | Rush + Rec Yards | under | 0.10250887840950917 | 2026-11-12T07:07:56Z | 2026-11-15T21:05:00Z |
| underdog|b58d4951-3cf7-4235-9f2b-f9836e774dae | underdog | Drake London | Receiving Yards | under | 0.1020493545084814 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|2d00be5f-dba3-4c34-a708-079e49994847 | underdog | Calvin Ridley | Receptions | under | 0.10167650278337226 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|51820dd7-063c-4751-be38-84c9a6983fed | underdog | Christian McCaffrey | Receptions | under | 0.1016183424097532 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|dd69b512-b698-428c-bd34-5a8e020ae6e3 | underdog | Tyler Bass | FG Made | under | 0.10117399188091525 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|e44dcdeb-f082-4537-a094-f55041798c31 | underdog | J'Koby Williams | Rush Yards | under | 0.1007044471669244 | 2026-11-12T07:07:56Z | 2026-11-15T02:30:00Z |
| underdog|5ca0340a-c96a-430f-891c-91362f1afc44 | underdog | Marvin Harrison | Receiving Yards | under | 0.10005828705530906 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|6e7a5219-ee88-466f-80b7-208dc41a4a98 | underdog | DeSean Bishop | Rush Yards | under | 0.09973628451165995 | 2026-11-11T16:13:16Z | 2026-11-14T20:00:00Z |
| underdog|aa77f012-39a7-4b67-9652-280f9e079534 | underdog | Makhi Hughes | Rush Yards | under | 0.09953928158338443 | 2026-11-11T06:09:33Z | 2026-11-14T03:15:00Z |
| underdog|45ba4e91-0c61-4d77-8f2e-8c7026f69033 | underdog | Cam Skattebo | Rush + Rec Yards | under | 0.09939226316945038 | 2026-11-12T07:07:56Z | 2026-11-13T01:15:00Z |
| underdog|e914c0c2-ab3b-433f-a62e-1f595c231acb | underdog | Elija Lofton | Receiving Yards | under | 0.09914235007728434 | 2026-11-11T16:13:16Z | 2026-11-14T17:00:00Z |
| underdog|ffdf6928-c765-4901-bcf9-925978a42dfd | underdog | Jacoby Brissett | Pass Attempts | under | 0.09857496516557318 | 2026-11-12T07:07:56Z | 2026-11-17T01:15:00Z |
| underdog|8150638b-9a7e-427a-aba6-76704ed97855 | underdog | Ethan Moczulski | FG Made | over | 0.09839210553400768 | 2026-11-10T12:33:48Z | 2026-11-14T02:00:00Z |
| underdog|44e533e5-9200-4c4b-92ea-1d11b251745d | underdog | DJ Reader | Sacks | over | 0.09832038501142126 | 2026-11-11T22:47:13Z | 2026-11-13T01:15:00Z |
| underdog|6f6e76ef-69e3-4315-83cb-ea6ec48daea1 | underdog | Chad Ryland | FG Made | over | 0.09807717467815241 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|5f95b22a-44d2-4c89-b35c-17c275ad8b09 | underdog | Gunner Stockton | Pass Yards | under | 0.09783371432939425 | 2026-11-11T16:13:16Z | 2026-11-14T20:30:00Z |
| underdog|89777911-6168-4f57-8662-8d3f09ac1716 | underdog | Chris Boswell | FG Made | under | 0.09775400624264463 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|25743011-bfd4-464d-90b1-673d77a0f244 | underdog | K'Lavon Chaisson | Sacks | over | 0.09769809701212023 | 2026-11-11T06:09:33Z | 2026-11-13T01:15:00Z |
| underdog|369bb4d5-4bfc-4124-8e50-51030898365a | underdog | Tony Pollard | Receptions | under | 0.09758293132802409 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|16dc39f4-bd6e-4e92-89f9-ae72c02b8c0a | underdog | Jonathan Dimas | FG Made | under | 0.09709066624784901 | 2026-11-11T16:13:16Z | 2026-11-14T03:15:00Z |
| underdog|6055c679-9c49-4f97-9d3d-7258ad5d7595 | underdog | Terrance Carter | Receiving Yards | under | 0.09663577177035454 | 2026-11-11T16:13:16Z | 2026-11-15T02:30:00Z |
| underdog|7d1b7f21-aa87-4f17-bf44-77c18f015227 | underdog | Kyren Williams | Rush + Rec Yards | under | 0.09657686894256146 | 2026-11-12T07:07:56Z | 2026-11-15T21:05:00Z |
| underdog|69040f4e-db3c-4d25-a8e0-657a2dfbf9c3 | underdog | Anthony Colandrea | Pass TDs | under | 0.09648140885681478 | 2026-11-11T06:09:33Z | 2026-11-14T17:30:00Z |
| underdog|4449e604-1137-41ce-845a-cf2d65eee460 | underdog | Darian Mensah | Pass TDs | over | 0.09646249729861844 | 2026-11-11T06:09:33Z | 2026-11-14T17:00:00Z |
| underdog|506821c8-a453-4a20-a85b-f97bfaa4e1fe | underdog | Zay Flowers | Receiving Yards | under | 0.09632328774235666 | 2026-11-11T22:47:13Z | 2026-11-17T01:15:00Z |
| underdog|92efc1e0-6e09-45b5-9380-ed2ef9424766 | underdog | Noah Fifita | Pass Yards | under | 0.0962718991546474 | 2026-11-10T12:33:48Z | 2026-11-15T00:30:00Z |
| underdog|0e196ee8-4db3-4fce-a18c-a14e74e12905 | underdog | Marcel Reed | Pass TDs | under | 0.09624315580046416 | 2026-11-11T16:13:16Z | 2026-11-14T20:00:00Z |
| underdog|c3d405f2-f65d-4f28-9dab-86ac43a8d975 | underdog | Kenneth Walker III | Receptions | under | 0.0960980842757887 | 2026-11-11T16:13:16Z | 2026-11-15T18:00:00Z |
| underdog|5d124f4c-22e7-4e63-aabe-d97f5d3a856e | underdog | Jakobi Meyers | Receptions | under | 0.09590453564859014 | 2026-11-11T16:13:16Z | 2026-11-15T18:00:00Z |
| underdog|4dd1c032-49a9-4847-8314-d8ddb529ceae | underdog | KC Concepcion | Receiving Yards | under | 0.09574048321212925 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|382be9ea-4cd8-4981-9243-ba13a3e9bca4 | underdog | Evan McPherson | Kicking Points | under | 0.09540198598918959 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|a0d2c31e-f6cb-4bee-81be-02dcf80d0449 | underdog | Carnell Tate | Receiving Yards | under | 0.09537210117181494 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|8284c067-29a7-4c39-a06b-fd41c094c2f0 | underdog | Connor Hawkins | FG Made | under | 0.09500557365097495 | 2026-11-12T07:07:56Z | 2026-11-14T17:00:00Z |
| underdog|6ea29960-71f2-4c50-b308-5014bf65c42d | underdog | Jahmyr Gibbs | Rush Yards | under | 0.09464878956736067 | 2026-11-12T07:07:56Z | 2026-11-15T14:30:00Z |
| underdog|0789564f-aac7-4796-ad55-71434916df49 | underdog | T.J. Hockenson | Receiving Yards | under | 0.09463140071749987 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|d2cdc210-fcc2-4276-9810-a70ee7020fdd | underdog | Bear Bachmeier | Pass Yards | under | 0.09458764346729465 | 2026-11-11T16:13:16Z | 2026-11-14T20:30:00Z |
| underdog|f141f96d-3046-48f6-b72d-1ed6c977faa4 | underdog | Tommy Tremble | Receiving Yards | under | 0.09438586255707826 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|1d37f459-f6d1-4307-99ec-bf177e3a6437 | underdog | Jason Sanders | FG Made | over | 0.09433045418762181 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|fa4c7f93-3a59-4d24-a659-ab3a46d49e2b | underdog | Greg Dulcich | Receiving Yards | under | 0.09403894171268923 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|8a49ae43-c040-451b-bc3d-b83ae4ccecdc | underdog | Bhayshul Tuten | Rush + Rec Yards | under | 0.09384976943653545 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|192016d6-c59a-4f73-bd58-5a17cebf9824 | underdog | Keelon Russell | Pass Yards | under | 0.09373932422374998 | 2026-11-11T22:47:13Z | 2026-11-14T17:45:00Z |
| underdog|abf6366a-98c0-4dca-a13b-5a0221de2afa | underdog | Trinidad Chambliss | Pass TDs | over | 0.09346167782668713 | 2026-11-11T22:47:13Z | 2026-11-14T21:15:00Z |
| underdog|f8f6356d-592e-4e3a-8d8b-6bfaa2874eef | underdog | Luke Fahey | Pass Yards | under | 0.09241833281916434 | 2026-11-12T07:07:56Z | 2026-11-14T17:00:00Z |
| underdog|a30b2228-d396-4ac4-9b08-37b91b85f9cf | underdog | J.J. McCarthy | Rush Yards | under | 0.09240883385153875 | 2026-11-11T22:47:13Z | 2026-11-13T01:15:00Z |
| prizepicks|16864060 | prizepicks | Luke Farrell | Rec Yards | over | 0.0923962774082826 | 2026-11-11T06:09:33Z | 2026-11-15T16:25:00.000-05:00 |
| underdog|147243e6-fcee-4814-8b0f-73b49c924682 | underdog | Chris Olave | Receiving Yards | under | 0.09207479159828746 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|7aa6308c-d5e6-4a77-a069-483e31e47c22 | underdog | Willie Rodriguez | Receptions | under | 0.09080568724128812 | 2026-11-12T07:07:56Z | 2026-11-14T23:15:00Z |
| underdog|cde77409-6c4b-4d8e-9073-074e686e1b6d | underdog | Cam Little | Kicking Points | under | 0.09049138686982805 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|70d825fa-79f7-4bda-8041-97183baab862 | underdog | Ethan Grunkemeyer | Pass Yards | under | 0.09021080786382596 | 2026-11-12T07:07:56Z | 2026-11-15T00:30:00Z |
| prizepicks|16834826 | prizepicks | DK Metcalf | Rec Yards | under | 0.09020306892719043 | 2026-11-10T12:33:48Z | 2026-11-15T20:20:00.000-05:00 |
| underdog|b5f4f16e-c55f-49b2-9819-c1bcae832c7e | underdog | Jonathan Taylor | Rush Yards | under | 0.08936972765302831 | 2026-11-11T16:13:16Z | 2026-11-15T18:00:00Z |
| underdog|fa0d49ab-2e45-40fb-aa7c-44f1124f350a | underdog | Davis Warren | Pass Yards | under | 0.08927213596097106 | 2026-11-12T07:07:56Z | 2026-11-15T00:30:00Z |
| underdog|e93b4a70-c115-466d-bbee-09d35b69688b | underdog | Trae'shawn Brown | Rush Yards | under | 0.08901098051360323 | 2026-11-11T22:47:13Z | 2026-11-14T17:45:00Z |
| underdog|6d262b69-f916-40a2-99ea-783ddb6319aa | underdog | CeeDee Lamb | Receiving Yards | under | 0.08883462987533675 | 2026-11-11T06:09:33Z | 2026-11-15T21:25:00Z |
| underdog|60f56ef3-30f8-4f82-853c-39b4fb03c274 | underdog | Isaiah Likely | Receiving Yards | under | 0.08839971393428592 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| prizepicks|16894974 | prizepicks | Ashton Daniels | Rush Atts | under | 0.08812597680513468 | 2026-11-12T07:07:56Z | 2026-11-13T19:00:00.000-05:00 |
| underdog|f9fc5b80-57fb-4d48-b0d6-01920f66516f | underdog | Rece Verhoff | FG Made | under | 0.08797576918997374 | 2026-11-11T06:09:33Z | 2026-11-15T00:00:00Z |
| underdog|9ea2bc5d-65cf-4749-b4f2-ef74fea29512 | underdog | Arch Manning | Pass Yards | under | 0.0878083317921382 | 2026-11-11T16:13:16Z | 2026-11-15T00:30:00Z |
| underdog|c728a2e0-0649-4d67-b4b2-706b179c03ee | underdog | Chig Okonkwo | Receiving Yards | under | 0.08753661477187691 | 2026-11-12T07:07:56Z | 2026-11-13T01:15:00Z |
| underdog|7b9cbde9-983a-4d99-84fd-1e3dd0ea2c7f | underdog | Tre Tucker | Receiving Yards | over | 0.0875329970402473 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|0c761c58-be15-416b-b703-6a586bf39be5 | underdog | Kenny Johnson | Receptions | under | 0.08742722952237947 | 2026-11-11T16:13:16Z | 2026-11-15T02:30:00Z |
| prizepicks|16863709 | prizepicks | Germie Bernard | Rec Targets | under | 0.0868140274679029 | 2026-11-11T06:09:33Z | 2026-11-15T20:20:00.000-05:00 |
| underdog|568c3de8-7943-4733-a62e-0ad545ed654c | underdog | Emmett Johnson | Receptions | under | 0.0867952807296627 | 2026-11-11T16:13:16Z | 2026-11-15T18:00:00Z |
| prizepicks|16834650 | prizepicks | Derrick Henry | Rush Yards | under | 0.08663217446763538 | 2026-11-10T12:33:48Z | 2026-11-16T20:15:00.000-05:00 |
| underdog|0bfc6753-5f10-4e6f-9e3c-1785134a300d | underdog | Hank Brown | Pass TDs | under | 0.08611303327074238 | 2026-11-11T22:47:13Z | 2026-11-15T00:30:00Z |
| underdog|bde27c75-ca7b-4775-ab57-ca6a518c19bf | underdog | Trinidad Chambliss | Pass Yards | under | 0.0860800893356608 | 2026-11-11T22:47:13Z | 2026-11-14T21:15:00Z |
| underdog|a0f28536-1ea4-460f-8056-53d93cf15ad8 | underdog | Dani Dennis-Sutton | Sacks | over | 0.08579135002694815 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|d9c81d05-b6b1-48b8-81ad-3dda0ae5e50d | underdog | Chase Brown | Rush Yards | under | 0.08560410498710846 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|61e1b16e-fc64-4a20-aaf7-c86a2ed3ba0c | underdog | Travis Kelce | Receiving Yards | under | 0.08538377569690225 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|b31f3fa0-6f4a-45f4-949e-38b59a516e08 | underdog | Kaelon Black | Rush + Rec Yards | under | 0.08529394052891348 | 2026-11-12T07:07:56Z | 2026-11-15T21:25:00Z |
| underdog|0791176b-ca45-4db5-adce-5e0033f90282 | underdog | Kenneth Walker III | Rush + Rec Yards | under | 0.08517285225941984 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|0149f1ed-8d01-4fb3-8c29-ee43cba33fce | underdog | Kaleb Johnson | Rush Yards | under | 0.08513771358831856 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|4e80cfd3-9149-446e-be59-5f3a2eb65ffd | underdog | Luke Fahey | Pass TDs | under | 0.08510893174475809 | 2026-11-12T07:07:56Z | 2026-11-14T17:00:00Z |
| underdog|fe742815-78d4-49a8-89d4-b09df9d494f8 | underdog | Jaxon Smith-Njigba | Receptions | under | 0.08495752665294976 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|2241dc3b-3cce-4713-948a-899c19938a90 | underdog | Bhayshul Tuten | Receptions | under | 0.08488347843269772 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|16a163f8-37a8-4814-9673-e9079fc7d360 | underdog | Khalil Shakir | Receiving Yards | under | 0.08458463166509522 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|095d7662-7876-4544-a661-85a9352bc8b9 | underdog | Darnell Washington | Receptions | under | 0.08429478520005662 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|6a800e8e-f81b-4bdb-9cee-fc7e90da63ae | underdog | Chuba Hubbard | Receptions | under | 0.08408782592218833 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|37738fae-4753-4e52-b227-99303a546958 | underdog | Caleb Hawkins | Rush Yards | under | 0.0840529047691323 | 2026-11-11T16:13:16Z | 2026-11-15T02:30:00Z |
| underdog|2d6f2c26-3679-4462-b5f9-154fdf837d9a | underdog | Malik Washington | Receptions | under | 0.08380896020559803 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|38344d58-adc1-4dc0-b791-82d655b56a31 | underdog | Jared Curtis | Pass Yards | under | 0.08375652359206187 | 2026-11-11T22:47:13Z | 2026-11-14T17:45:00Z |
| underdog|5978a0c4-b089-4243-93ce-fed7ae99460e | underdog | Kenny Johnson | Receiving Yards | under | 0.08365563340133153 | 2026-11-11T16:13:16Z | 2026-11-15T02:30:00Z |
| underdog|caaa9f08-a4f1-4c28-9550-d4eb485c37e1 | underdog | Beau Pribula | Pass TDs | over | 0.08359900244748819 | 2026-11-11T06:09:33Z | 2026-11-14T20:30:00Z |
| underdog|7f654e7f-ce6f-4514-b607-3b45826bc886 | underdog | Carnell Tate | Receptions | under | 0.08352541400712155 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|30b534aa-3c8d-4e2a-8532-7046212f8423 | underdog | Keon Coleman | Receptions | over | 0.08351427326810018 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|719af474-27cd-45cb-bbbe-2919ccabbbb0 | underdog | Arvell Reese | Sacks | over | 0.08350295443289074 | 2026-11-11T22:47:13Z | 2026-11-13T01:15:00Z |
| underdog|fa89e139-2ff7-4471-9a99-3cff435d0b81 | underdog | Michael Mayer | Receiving Yards | over | 0.083113027814818 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|b4b14665-4501-496c-8be0-d530e6e1fbe5 | underdog | CeeDee Lamb | Receptions | under | 0.08142420706840037 | 2026-11-11T06:09:33Z | 2026-11-15T21:25:00Z |
| underdog|879eaed1-2f48-4ebf-82ba-fffcc451343a | underdog | Pat Freiermuth | Receptions | under | 0.08099921416069444 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|0948aa96-7ab1-4a01-8009-90f637fe281c | underdog | Walker Eget | Pass TDs | under | 0.08075629229645986 | 2026-11-11T06:09:33Z | 2026-11-14T17:00:00Z |
| underdog|2c6a1766-9888-43db-8463-79a5e3158ac9 | underdog | Foster Moreau | Receiving Yards | over | 0.08074063361249817 | 2026-11-11T16:13:16Z | 2026-11-15T18:00:00Z |
| underdog|88e2ab41-d0f1-460f-8fd8-dd80d3de0840 | underdog | George MacIntyre | Pass Yards | under | 0.0805852696407322 | 2026-11-12T07:07:56Z | 2026-11-14T20:00:00Z |
| underdog|c4e5cef0-a68c-4f30-8bf1-e0db1f36c83b | underdog | Tetairoa McMillan | Receiving Yards | under | 0.08046760762807637 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|23238e4a-a453-48b3-888b-37d8d5c24a0e | underdog | Caleb Douglas | Receiving Yards | under | 0.08033066710225367 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|204edb39-0ec5-4aa9-ba48-567e3460bfff | underdog | Kayshon Boutte | Receiving Yards | over | 0.08013742496044951 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|67d69720-f75a-4a58-8666-e3e822ae68f8 | underdog | Kimani Vidal | Rush + Rec Yards | under | 0.08006957549511673 | 2026-11-11T22:47:13Z | 2026-11-17T01:15:00Z |
| underdog|5e94977c-0093-48e8-becf-5e8910977a9b | underdog | Drake Maye | Rush Yards | under | 0.08004423976338015 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|0b2e9d13-d865-4ce4-8130-1811f8c75f1f | underdog | Jahmyr Gibbs | Receptions | under | 0.07974674760702072 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|28b73f9a-7464-4028-9994-b3e9777c631e | underdog | Juwan Johnson | Receptions | under | 0.07927138801736044 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|aec9f942-d44c-43ee-8847-b10728935f0d | underdog | Omarion Hampton | Receptions | over | 0.0790537300117724 | 2026-11-11T22:47:13Z | 2026-11-17T01:15:00Z |
| underdog|00e694e5-aa6d-4774-acbc-93a1f551069a | underdog | Mitchell Evans | Receiving Yards | over | 0.07877319492081836 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|fcf60ef4-6d8a-4e5f-a5dc-ab09c139b1d7 | underdog | Olamide Zaccheaus | Receptions | under | 0.07875857917335316 | 2026-11-11T16:13:16Z | 2026-11-15T18:00:00Z |
| underdog|8450e859-24f2-4721-9b6d-6aceb59b963a | underdog | Aaron Rodgers | Pass TDs | under | 0.07874658502524756 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|e783dc26-5825-408b-ba88-074ae8338f79 | underdog | Tyler Allgeier | Receptions | under | 0.07858479788991879 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|ef561390-3448-4772-923f-2907512618eb | underdog | Jaron-Keawe Sagapolutele | Pass Yards | under | 0.07837522924219475 | 2026-11-12T07:07:56Z | 2026-11-14T20:30:00Z |
| underdog|c56fb924-60e5-4a74-adb3-8288fc679008 | underdog | Drew Stevens | Kicking Points | under | 0.0778937129166114 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| underdog|cdc2071a-3842-44a4-9f0d-c3706f5c9309 | underdog | Bijan Robinson | Rush Yards | under | 0.07770038799830425 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|0abd8ddf-26d7-4577-a9e6-a3adbd2f8a3e | underdog | Denzel Boston | Receiving Yards | under | 0.07763959474610682 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| prizepicks|16906374 | prizepicks | Ryan Hopkins | Pass Comp | under | 0.07753883763235836 | 2026-11-12T07:07:56Z | 2026-11-14T12:00:00.000-05:00 |
| underdog|e7f1bbea-2d7b-4c56-8e47-9e0b571c984f | underdog | Will Bettridge | FG Made | over | 0.07725741826529164 | 2026-11-11T06:09:33Z | 2026-11-14T20:30:00Z |
| underdog|943b6125-955d-4c4e-a9cb-d4c65e6b426a | underdog | Aaron Rodgers | Rush Yards | over | 0.07712631679230819 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|b25fcb52-8786-406a-858d-52e7672af5fc | underdog | Antonio Chadha | FG Made | over | 0.07704066761603501 | 2026-11-10T12:33:48Z | 2026-11-14T00:00:00Z |
| underdog|b60a1138-01f1-4292-b874-5acaf191af21 | underdog | Dylan Sampson | Rush + Rec Yards | under | 0.0767893063215298 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|058b0488-9d5f-43ce-ae6a-dde3d1e4de82 | underdog | Nate Frazier | Rush Yards | under | 0.07674922775801507 | 2026-11-11T22:47:13Z | 2026-11-14T20:30:00Z |
| underdog|4172a2e0-cc73-4a02-8e18-e7b1e77ef4fa | underdog | Chig Okonkwo | Receptions | under | 0.07662959369636402 | 2026-11-09T06:06:04Z | 2026-11-13T01:15:00Z |
| underdog|2f3c01e8-56f2-4972-80d6-96a7c641e276 | underdog | Jahmyr Gibbs | Receiving Yards | under | 0.07651862763115314 | 2026-11-11T16:13:16Z | 2026-11-15T14:30:00Z |
| underdog|693f5fff-95ff-4e29-b913-be01aef304c7 | underdog | Savion Williams | Receiving Yards | under | 0.0763692412291278 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|9afc918c-33f0-4d49-94c8-ae1c1087877a | underdog | London Humphreys | Receiving Yards | over | 0.07632980997810002 | 2026-11-11T16:13:16Z | 2026-11-14T20:30:00Z |
| underdog|c654c51c-10ef-484a-bdc0-907c83372ccc | underdog | Isaac Wilson | Pass Yards | under | 0.07623255608807167 | 2026-11-11T22:47:13Z | 2026-11-14T03:15:00Z |
| underdog|93f57aed-6f22-4917-bbcd-a64859bd454f | underdog | KC Concepcion | Receptions | under | 0.07613263220312116 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|921893b1-e130-4cc1-9e68-fae07083d8d6 | underdog | Tee Higgins | Receiving Yards | under | 0.07552956056808402 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|81ff0621-4501-4f89-a90c-53b654828353 | underdog | Tucker Kraft | Receptions | under | 0.07531614878084558 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|4dfa0157-e1a7-41c5-98a2-53df06995587 | underdog | Brendan Baird | FG Made | under | 0.07501720483065888 | 2026-11-10T12:33:48Z | 2026-11-14T17:00:00Z |
| underdog|0c1b8205-16c9-4bba-b677-32477bbf7cc6 | underdog | Aaron Jones | Receptions | under | 0.07498021252064768 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|4e8a8c5e-9abc-498a-8341-e4e9ef398393 | underdog | Malik Washington | Pass TDs | under | 0.07400696409454255 | 2026-11-12T07:07:56Z | 2026-11-14T17:00:00Z |
| underdog|7eda251b-5bb5-4672-b317-2b57fa7740b9 | underdog | Jadon Porter | Receiving Yards | over | 0.07400421754769337 | 2026-11-11T16:13:16Z | 2026-11-14T20:30:00Z |
| underdog|80d5b669-4608-4a70-af3d-0ca04f2a9ce7 | underdog | Braylon Staley | Receptions | under | 0.07334461051353225 | 2026-11-11T16:13:16Z | 2026-11-14T20:00:00Z |
| underdog|1401b805-b55d-4f62-9585-45359cf41b66 | underdog | Patrick Mahomes | Pass TDs | under | 0.07319579691346556 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|7fddc7b2-9d72-4ff1-b1b0-9b0333b60dbd | underdog | Gunnar Helm | Receptions | under | 0.07318955792213211 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|15895332-a1f7-4ca9-9f82-51abcab141d4 | underdog | Seth McGowan | Receiving Yards | under | 0.07317673931460811 | 2026-11-11T16:13:16Z | 2026-11-15T18:00:00Z |
| underdog|06ae6764-4717-4fd0-90d4-cba7d420c077 | underdog | Sam Leavitt | Pass TDs | over | 0.07311759928344974 | 2026-11-11T16:13:16Z | 2026-11-15T00:30:00Z |
| underdog|228e3396-f2f2-4d99-afc3-05ad8927a249 | underdog | Keelon Russell | Pass TDs | under | 0.07311368179295119 | 2026-11-12T07:07:56Z | 2026-11-14T17:45:00Z |
| underdog|5aa07c5c-3160-4bf9-bae2-17272d017de0 | underdog | Tetairoa McMillan | Receptions | under | 0.07291530262227885 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|58530279-d194-481f-a949-e22dc1d2b1ae | underdog | Marcel Reed | Pass Yards | under | 0.072912428099693 | 2026-11-11T16:13:16Z | 2026-11-14T20:00:00Z |
| underdog|846cd3db-4808-49d5-8f07-8ef2145cd893 | underdog | Kenyon Sadiq | Receptions | under | 0.07290174754695289 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|9d2c3daf-6c48-4a77-a490-9c83580440b2 | underdog | Dylan Sampson | Rush Yards | under | 0.07283020578686128 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|f65d31f8-6cb0-46ef-973a-612d369e3cc2 | underdog | Lukas Van Ness | Sacks | over | 0.0725672770341067 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|707d8339-a7f0-468c-a5f3-2b025bfa73d7 | underdog | Mateen Bhaghani | XP Made | over | 0.07183282096813365 | 2026-11-10T12:33:48Z | 2026-11-14T02:00:00Z |
| underdog|858c7d02-f1ef-43e2-ac44-a0e9447d8e99 | underdog | Tommy Tremble | Receptions | under | 0.07126105154425799 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|7a75e646-5664-41bf-83d2-fea36aea9458 | underdog | AJ Barner | Receiving Yards | under | 0.07075613788298196 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| prizepicks|16863705 | prizepicks | Jameson Williams | Rec Targets | under | 0.07067193012939765 | 2026-11-11T06:09:33Z | 2026-11-15T09:30:00.000-05:00 |
| underdog|deecab8f-370d-4516-9f25-df02775fef96 | underdog | Odafe Oweh | Sacks | over | 0.07066129881666916 | 2026-11-12T07:07:56Z | 2026-11-13T01:15:00Z |
| underdog|d3703433-0613-4609-8f73-ccbe69309032 | underdog | Dominic Zvada | FG Made | under | 0.07048776383240163 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| underdog|96b084f0-e61e-4d6f-bbda-ee645d2f7d65 | underdog | Jason Myers | Kicking Points | under | 0.07035458570297104 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|59d01cde-8219-4313-bd2e-4282a5c538fb | underdog | Drew Stevens | FG Made | under | 0.07032400194327204 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| underdog|ce3ccd0a-3e20-41f2-9333-20fd3629fc36 | underdog | Wayne Knight | Rush Yards | under | 0.06999553654669133 | 2026-11-11T06:09:33Z | 2026-11-14T02:00:00Z |
| underdog|8956556f-aef4-479b-9d48-db3491601b08 | underdog | Trey'Dez Green | Receptions | under | 0.06996883223576089 | 2026-11-11T16:13:16Z | 2026-11-15T00:30:00Z |
| underdog|32afa744-a7db-46b1-8166-59407c4e4dd5 | underdog | Nico Collins | Receptions | under | 0.06991731066614237 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|8dc776e9-341d-424e-97a4-cb1076f15650 | underdog | Darren Waller | Receptions | under | 0.06987874258747295 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|3a0a1923-9d00-45fe-b0ce-7f76d9913a34 | underdog | Darian Mensah | Rush Yards | over | 0.06986848826057779 | 2026-11-11T16:13:16Z | 2026-11-14T17:00:00Z |
| underdog|10729dc7-2bc5-45f6-b6a1-f2e8ec1605d7 | underdog | Conner Weigman | Pass Yards | under | 0.06985803494675158 | 2026-11-11T22:47:13Z | 2026-11-14T03:15:00Z |
| underdog|42e0039c-07fd-41cb-b58f-c045f2906c65 | underdog | Quinshon Judkins | Rush Yards | under | 0.06976167861231075 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|46bfc64a-8a7e-4772-a161-dfa994992a76 | underdog | Mason McKenzie | Pass TDs | over | 0.069588650452449 | 2026-11-11T06:09:33Z | 2026-11-14T20:30:00Z |
| underdog|9fb692ca-1ded-474d-ace1-e954d47e3038 | underdog | Isaac TeSlaa | Receptions | under | 0.06945554268955467 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|edd8f0e4-7008-474c-8413-041ca06749b0 | underdog | Drew Sample | Receptions | over | 0.0693941433699456 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|7672d1dc-c9b9-446e-9d21-394707cb25f3 | underdog | Malik Nabers | Receiving Yards | under | 0.06928711935386878 | 2026-11-11T16:13:16Z | 2026-11-13T01:15:00Z |
| underdog|cdb9abab-d092-4db1-9de3-928df219fa5a | underdog | Khalil Herbert | Rush + Rec Yards | under | 0.06928381220197244 | 2026-11-11T16:13:16Z | 2026-11-15T18:00:00Z |
| underdog|0f5f2541-1db6-4c5c-8f7b-f83a3c899da1 | underdog | Theo Johnson | Receiving Yards | over | 0.06916896259016725 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| underdog|44222ca6-7319-4558-9011-4baebd4dae89 | underdog | Chris Olave | Receptions | under | 0.06860046597796887 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|ab5a705a-6a78-49b7-bcfd-7321ae88e69f | underdog | Kaelon Black | Receptions | under | 0.0685332352021717 | 2026-11-10T12:33:48Z | 2026-11-15T21:25:00Z |
| underdog|8aa2ecd1-22be-421d-828e-4d205fe6b04f | underdog | Micahi Danzy | Receiving Yards | under | 0.06844881191786067 | 2026-11-11T06:09:33Z | 2026-11-14T00:00:00Z |
| prizepicks|16863716 | prizepicks | Tee Higgins | Rec Targets | under | 0.06814305302582702 | 2026-11-11T06:09:33Z | 2026-11-15T20:20:00.000-05:00 |
| underdog|0a2dcbf7-b7e8-4d71-8034-a024ef71e687 | underdog | Tate Sandell | XP Made | under | 0.06802582102225152 | 2026-11-11T06:09:33Z | 2026-11-14T21:15:00Z |
| underdog|b7573824-7d88-45cc-8bc1-9e98836c986d | underdog | Bijan Robinson | Receiving Yards | under | 0.06782521035230094 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|a3d15510-be5c-4878-a700-cfa17b56a9c5 | underdog | Marcus Stokes | Pass TDs | over | 0.0676381067821199 | 2026-11-11T22:47:13Z | 2026-11-13T01:00:00Z |
| underdog|67bb66e0-36f8-4bfb-b364-8db821ce624f | underdog | Daylyn Upshaw | Receiving Yards | under | 0.0674153490159497 | 2026-11-11T16:13:16Z | 2026-11-14T17:00:00Z |
| underdog|7627dd31-dcb0-4356-b6c1-21656c34392a | underdog | Ashton Daniels | Pass TDs | over | 0.06711574287975197 | 2026-11-12T07:07:56Z | 2026-11-14T00:00:00Z |
| underdog|500509cc-70ed-419e-b01b-6be54d934764 | underdog | Amari Thomas | Rush Yards | under | 0.06674668340859635 | 2026-11-11T16:13:16Z | 2026-11-14T00:00:00Z |
| underdog|28a6f2e6-c201-4e00-9b8a-71e36e17333b | underdog | Devon Dampier | Pass TDs | over | 0.06672449840713934 | 2026-11-10T12:33:48Z | 2026-11-15T00:30:00Z |
| underdog|75d6f3fa-7734-49c4-9e25-90076e135660 | underdog | Darian Mensah | Pass Yards | under | 0.06666845712800784 | 2026-11-11T06:09:33Z | 2026-11-14T17:00:00Z |
| underdog|11524372-bbae-47eb-abc7-77f03ee31c7a | underdog | Dawson Knox | Receptions | under | 0.06664316355524857 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| prizepicks|16910237 | prizepicks | Bianca Andreescu | Total Games | over | 0.06662320386382004 | 2026-11-12T07:07:56Z | 2026-11-12T11:10:00.000-05:00 |
| underdog|e3895608-8c85-4816-aad0-fe8098f92933 | underdog | Dawson Knox | Receiving Yards | under | 0.06643222901337464 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|f7e068ff-ada4-4eb9-b1d0-4d71a142c5fe | underdog | Griffin Wilde | Receiving Yards | over | 0.06622569678186274 | 2026-11-12T07:07:56Z | 2026-11-14T17:00:00Z |
| underdog|97733708-ed62-42d6-891a-4827e8fe144e | underdog | Noah Gray | Receiving Yards | over | 0.06572912691694155 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| prizepicks|16834811 | prizepicks | Jalen Coker | Rec Yards | under | 0.0652772475778256 | 2026-11-10T12:33:48Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|d4150a17-b459-4876-b557-7ba5873c9026 | underdog | Barryn Sorrell | Sacks | over | 0.06498589556022877 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|8a5a2942-cbf3-4389-befa-f6325f90a1a2 | underdog | Tyler Warren | Receptions | under | 0.06494609926234585 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|6904bdb5-d67c-4c2b-98d5-76350f320cab | underdog | Chris Rodriguez | Receiving Yards | over | 0.06420883262089416 | 2026-11-11T16:13:16Z | 2026-11-15T18:00:00Z |
| underdog|067410a9-e4e9-468e-ac1c-c09828fb5b19 | underdog | Matthew Golden | Receiving Yards | under | 0.06410870794329593 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|03043c1e-1e3f-4dfd-82ba-0f958a2d15b8 | underdog | Antonio Chadha | XP Made | over | 0.06383233498092222 | 2026-11-10T12:33:48Z | 2026-11-14T00:00:00Z |
| underdog|2ef3cdfc-603a-4a90-8dd1-c78a10783d71 | underdog | Greg Dulcich | Receptions | under | 0.06371545917699406 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|fda0caed-9d57-43e7-9044-29c91c2e00c6 | underdog | Josh Cuevas | Receiving Yards | over | 0.0634698842147925 | 2026-11-11T22:47:13Z | 2026-11-17T01:15:00Z |
| underdog|596900c0-2992-46b0-93af-3b4b152ea578 | underdog | Cam Skattebo | Rush Yards | under | 0.06344227437228722 | 2026-11-12T07:07:56Z | 2026-11-13T01:15:00Z |
| underdog|c2bca2ad-2a98-4de6-b991-436c1c63c0a9 | underdog | Dylan Raiola | Pass Yards | under | 0.06320887649050189 | 2026-11-11T16:13:16Z | 2026-11-14T20:30:00Z |
| underdog|c489387a-fbec-48c8-ba91-c6a7f48a4d0a | underdog | Tyler Shough | Pass TDs | under | 0.06300540300276691 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|10a3c810-4d63-4b32-8043-7bd1c8a89bb3 | underdog | Kevin Jennings | Pass Yards | under | 0.06270576499724212 | 2026-11-11T16:13:16Z | 2026-11-14T17:00:00Z |
| underdog|4abe8ddb-6b44-4f13-93fc-d21d8063aeea | underdog | Seth McGowan | Rush Yards | under | 0.06258220256214175 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|5bdb985b-410f-409b-bea2-806a19ab995e | underdog | Malik Washington | Receiving Yards | under | 0.06237938849093194 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|15b388f2-4a79-44ae-ac0d-792c32c9a60f | underdog | Dominic Zvada | Kicking Points | under | 0.06222974703966089 | 2026-11-11T06:09:33Z | 2026-11-13T01:15:00Z |
| prizepicks|16870372 | prizepicks | Ashton Jeanty | Rec Targets | under | 0.06214267328538181 | 2026-11-11T06:09:33Z | 2026-11-15T16:05:00.000-05:00 |
| underdog|1fc490c3-56ff-42f6-9bac-1f901b919265 | underdog | Linda Noskova | Double Faults | under | 0.06198479596809958 | 2026-11-12T07:07:56Z | 2026-11-12T21:10:00Z |
| underdog|4cecc174-35d7-4651-9676-27d5756251d2 | underdog | Javonte Williams | Rush Yards | under | 0.06196379751073866 | 2026-11-12T07:07:56Z | 2026-11-15T21:25:00Z |
| underdog|ed3edfdf-e961-497c-bb90-9e936d3d5b3e | underdog | Trey Smack | Kicking Points | under | 0.061936591489977766 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|74035606-4682-41d0-8085-255b16e43f27 | underdog | Bhayshul Tuten | Receiving Yards | over | 0.06181328099453465 | 2026-11-11T16:13:16Z | 2026-11-15T18:00:00Z |
| underdog|76a68710-9ef5-42b0-86d7-66fcc5b58d9c | underdog | Tre Tucker | Receptions | over | 0.06172070169914223 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|7f662455-94a7-4b44-98d9-3a1141a6e561 | underdog | Kayden Dixon-Wyatt | Receptions | over | 0.06160934850898092 | 2026-11-11T06:09:33Z | 2026-11-14T20:30:00Z |
| underdog|9c30f32f-0641-45c9-98cd-31914710134a | underdog | Conner Weigman | Pass TDs | under | 0.06146923964179296 | 2026-11-11T06:09:33Z | 2026-11-14T03:15:00Z |
| underdog|eb4e770e-7d6c-4302-9ca3-5b8ab646e8e3 | underdog | Tate Sandell | FG Made | over | 0.06064011194939378 | 2026-11-11T06:09:33Z | 2026-11-14T21:15:00Z |
| underdog|2ca12ee0-e6d2-41c8-b151-acf00be8c9a3 | underdog | Noah Bennee | Receiving Yards | over | 0.0605452926650496 | 2026-11-10T12:33:48Z | 2026-11-15T00:30:00Z |
| underdog|15dacbb1-1137-4ecd-813a-83e3d65404ec | underdog | Chase Brown | Receiving Yards | under | 0.06031556029363805 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|d2aca639-0fcc-421f-bff6-1dc28f8b4fa4 | underdog | Dalton Kincaid | Receptions | under | 0.060234650924518074 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|04662721-bba7-4c79-a581-c177d22b5264 | underdog | Austin Ekeler | Receiving Yards | under | 0.05996233246066052 | 2026-11-11T16:13:16Z | 2026-11-13T01:15:00Z |
| underdog|11b4b2af-a1af-4863-a1d3-2077193d67fe | underdog | Drake Maye | Pass TDs | under | 0.05982086422742261 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
| underdog|8ae06971-abf9-4235-88c3-08c0d0340567 | underdog | Tony Pollard | Receiving Yards | under | 0.059755840017869266 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|78748d91-4060-44ca-959a-a5962e13a530 | underdog | Brandon Aubrey | Kicking Points | under | 0.059463924496844345 | 2026-11-11T06:09:33Z | 2026-11-15T21:25:00Z |
| prizepicks|16814264 | prizepicks | Chig Okonkwo | Recs | under | 0.05931986937840705 | 2026-11-11T16:13:16Z | 2026-11-12T20:15:00.000-05:00 |
| underdog|bf6d8568-1c2e-4352-aa80-f22b9a01d700 | underdog | Elijah Higgins | Receptions | under | 0.05927277420068855 | 2026-11-12T07:07:56Z | 2026-11-15T21:05:00Z |
| underdog|24457ce7-a29e-4e65-aaab-d2f2d38d5a63 | underdog | Mark Andrews | Receptions | over | 0.05909484948085142 | 2026-11-10T12:33:48Z | 2026-11-17T01:15:00Z |
| underdog|f98bcaef-cb0f-4d55-8ff1-cfc91128d8a3 | underdog | Kenneth Walker III | Rush Yards | under | 0.058828765527661475 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|627584fd-bc28-48e0-a2fc-aeaeb413490c | underdog | Alonza Barnett | Pass TDs | under | 0.05875457764959491 | 2026-11-12T07:07:56Z | 2026-11-14T20:30:00Z |
| underdog|4d0fcffd-ad43-47a6-82aa-6629600c756c | underdog | Drew Lock | Pass TDs | under | 0.058702533200966744 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|f5777302-cf71-4ed0-a67e-fe6c6156946c | underdog | C.J. Stroud | Pass TDs | over | 0.058654369818583796 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|4b1fed48-15ba-428c-bb91-a7555f1b384a | underdog | Tony Pollard | Rush + Rec Yards | under | 0.05854451151910145 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|290e195d-8e34-4596-b14f-bf19adc896d6 | underdog | Kyle Juszczyk | Receptions | over | 0.05854227335361084 | 2026-11-11T22:47:13Z | 2026-11-15T21:25:00Z |
| underdog|0d79f3cf-17cf-4dde-9490-e60cbe3b9a83 | underdog | Noah Fant | Receptions | over | 0.058522070576161545 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|e85a0b19-b548-4442-98b0-3ecfd04f953c | underdog | Chris Boswell | Kicking Points | under | 0.05833293094762393 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|0b91d70f-0d9f-42b6-a4c3-7dcfdcbc4892 | underdog | Mike Matthews | Receptions | under | 0.058284766086376116 | 2026-11-11T16:13:16Z | 2026-11-14T20:00:00Z |
| underdog|888fa28c-e758-43a2-8045-d5e4ca7f7e60 | underdog | Junior Sherrill | Receiving Yards | under | 0.05824464639264759 | 2026-11-11T22:47:13Z | 2026-11-14T17:45:00Z |
| underdog|96e2d673-829f-4b11-8bcf-36b6baf3b013 | underdog | Walker Lyons | Receiving Yards | under | 0.05808358415812187 | 2026-11-12T07:07:56Z | 2026-11-14T20:30:00Z |
| underdog|3781f038-1e2d-4add-834e-b1c8ce30f9eb | underdog | Bryce Young | Pass TDs | under | 0.05761978630482656 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|cfe9dc12-c7f7-46a2-a5b3-7062507b4b7a | underdog | Spencer Porath | XP Made | under | 0.05746279372126262 | 2026-11-11T06:09:33Z | 2026-11-14T20:30:00Z |
| underdog|5e97417a-5e1a-46ec-a628-38d2ce6156ba | underdog | Spencer Shrader | FG Made | under | 0.05723488095356977 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|d574c7ec-e37c-4a11-9707-70d6710cd050 | underdog | Jake Bates | Kicking Points | under | 0.057056345727721 | 2026-11-11T06:09:33Z | 2026-11-15T14:30:00Z |
| underdog|ad5e8781-bd90-4378-89a8-d05b327c7f69 | underdog | Kayden Dixon-Wyatt | Receiving Yards | over | 0.056683977237381056 | 2026-11-11T06:09:33Z | 2026-11-14T20:30:00Z |
| underdog|1fcaea85-7de8-4228-8b8c-94bc768e0933 | underdog | Waymond Jordan | Rush Yards | over | 0.056657622533493046 | 2026-11-11T22:47:13Z | 2026-11-14T20:30:00Z |
| underdog|450e6500-80eb-4a39-b11d-91501af45e2b | underdog | Gunner Stockton | Pass TDs | under | 0.05640008620207193 | 2026-11-11T16:13:16Z | 2026-11-14T20:30:00Z |
| underdog|6baaf9ac-5c5a-4c60-a6f1-7c72d78c06a5 | underdog | Katin Houser | Pass Yards | under | 0.05637977765636992 | 2026-11-11T22:47:13Z | 2026-11-14T02:00:00Z |
| underdog|9db900b6-98c4-44c5-9401-d670160cd60b | underdog | Matthew Golden | Receptions | under | 0.05633066769825512 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|ccd6f642-f3f5-4fc3-8498-72ce41161385 | underdog | Conner Weigman | Rush Yards | under | 0.05627406593607254 | 2026-11-11T06:09:33Z | 2026-11-14T03:15:00Z |
| underdog|6ff9e080-87bc-43bf-8eae-1fce157fe0a1 | underdog | Ty Dieffenbach | Pass Yards | under | 0.05615621354279021 | 2026-11-11T22:47:13Z | 2026-11-14T02:00:00Z |
| underdog|4e3c103d-08d3-4d73-8de0-db283bb23858 | underdog | Abdul Carter | Sacks | under | 0.05603762263895218 | 2026-11-11T22:47:13Z | 2026-11-13T01:15:00Z |
| underdog|0400f1e3-d2ae-4ff4-8ac8-6cc9df35a44e | underdog | Caleb Hawkins | Receptions | under | 0.05602218902003142 | 2026-11-11T16:13:16Z | 2026-11-15T02:30:00Z |
| prizepicks|16834814 | prizepicks | Jaxon Smith-Njigba | Rec Yards | under | 0.05595171947998501 | 2026-11-10T12:33:48Z | 2026-11-15T16:05:00.000-05:00 |
| underdog|52152886-deb7-483b-a6b2-a4f956b59162 | underdog | Jerry Jeudy | Receiving Yards | over | 0.055922448448904705 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|7fc13d80-5c19-4981-95c0-1c5a9a22a74b | underdog | Walker Lyons | Receptions | under | 0.055913215695103435 | 2026-11-12T07:07:56Z | 2026-11-14T20:30:00Z |
| underdog|f080a415-e7c5-4b6a-bf89-f005fdf79946 | underdog | Matt Gay | FG Made | over | 0.05586119946761431 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|214cbd24-84bb-458e-b1f4-1bd3a2149b36 | underdog | Brenton Strange | Receiving Yards | under | 0.05577611188639431 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|f0b24d0a-f51d-4ec6-8f8f-ac17d8e0d0eb | underdog | Jalen Nailor | Receptions | over | 0.05545990463319178 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|d6e20642-ba8c-4e0a-b6c4-641e9e94c7ee | underdog | Cam Skattebo | Receptions | over | 0.055431027597783344 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| underdog|f2067b31-0d16-4656-91cd-454d91ca62bd | underdog | Brandon Aubrey | FG Made | under | 0.05538164462438755 | 2026-11-11T06:09:33Z | 2026-11-15T21:25:00Z |
| underdog|629bc6c2-9bf0-441d-adb3-1db31adf446b | underdog | Jayden Daniels | Rush Yards | under | 0.05534006929391311 | 2026-11-11T22:47:13Z | 2026-11-13T01:15:00Z |
| underdog|f9982662-f335-40b3-9dff-dcf0a72383a9 | underdog | Deebo Samuel | Receptions | under | 0.05533870914257788 | 2026-11-11T22:47:13Z | 2026-11-15T21:25:00Z |
| underdog|fe5d778f-f0e2-4f2d-8e4c-020384f0b6ca | underdog | Samaje Perine | Rush + Rec Yards | under | 0.055115547168950174 | 2026-11-11T22:47:13Z | 2026-11-16T01:20:00Z |
| underdog|889fdb00-e4eb-4bbd-8c81-a59ba7668209 | underdog | Beau Pribula | Pass Yards | under | 0.0550759908941616 | 2026-11-12T07:07:56Z | 2026-11-14T20:30:00Z |
| underdog|f8b50df0-df15-4845-9173-0adba2cfe7e2 | underdog | Samaje Perine | Receptions | under | 0.05489044582304281 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|2fb6b68c-630e-4d2a-a229-4d0133bb4f00 | underdog | Creed Whittemore | Receiving Yards | over | 0.05483588486226332 | 2026-11-10T12:33:48Z | 2026-11-15T00:30:00Z |
| underdog|3dd950b0-0c21-4346-85ae-f62f9682e66b | underdog | Damon Ferguson | Rush Yards | under | 0.05482425247734968 | 2026-11-11T06:09:33Z | 2026-11-14T00:00:00Z |
| underdog|857e7589-a9fd-4059-a56e-7b2e53af9c87 | underdog | Jalen Coker | Receiving Yards | under | 0.054822380623741895 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|987a0d35-cb17-455e-9291-4c6100b8eeeb | underdog | Chris Bell | Receiving Yards | under | 0.05476631144946331 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|7d6dc651-52a7-4727-98fb-91379f9a62c0 | underdog | Ashton Daniels | Pass Yards | under | 0.05468119763041812 | 2026-11-12T07:07:56Z | 2026-11-14T00:00:00Z |
| underdog|5a28b010-365f-4fb1-9087-b88df07ee519 | underdog | Sedrick Alexander | Receptions | under | 0.054244200164998424 | 2026-11-11T22:47:13Z | 2026-11-14T17:45:00Z |
| underdog|fbe45286-3dac-4714-a84e-232b93107bf8 | underdog | Lee Beebe | Rush Yards | under | 0.05413272472602093 | 2026-11-12T07:07:56Z | 2026-11-14T20:30:00Z |
| underdog|b8b27a97-5567-4989-bcf6-bb423b467b6a | underdog | Sedrick Alexander | Receiving Yards | over | 0.0540799838987972 | 2026-11-11T22:47:13Z | 2026-11-14T17:45:00Z |
| prizepicks|16864051 | prizepicks | Charlie Woerner | Rec Yards | over | 0.05401463087599445 | 2026-11-11T06:09:33Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|09e85dc1-6ddb-434e-a936-6fd8aed43b03 | underdog | Andre Szmyt | FG Made | under | 0.05378693771750487 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|05021bd0-e3fc-49d1-a237-3f7d1f691846 | underdog | Tank Dell | Receiving Yards | under | 0.05366192035705808 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|13232d73-80db-49f5-af92-e9949b4fcb2a | underdog | JJ Garner | Rush Yards | under | 0.05345327101124242 | 2026-11-12T07:07:56Z | 2026-11-13T02:00:00Z |
| underdog|752fb99e-c305-4d7e-b195-0395288a569d | underdog | Kaelon Black | Rush Yards | under | 0.05338295577490937 | 2026-11-11T06:09:33Z | 2026-11-15T21:25:00Z |
| underdog|5f5a3116-6c86-495f-b0cc-76ebd5261b14 | underdog | Justin Bowick | Receiving Yards | under | 0.053320411307768434 | 2026-11-11T16:13:16Z | 2026-11-15T02:30:00Z |
| prizepicks|16864058 | prizepicks | Eric Saubert | Rec Yards | over | 0.05300845751715566 | 2026-11-11T06:09:33Z | 2026-11-15T16:05:00.000-05:00 |
| prizepicks|16834798 | prizepicks | Drake London | Rec Yards | under | 0.05299181956525634 | 2026-11-10T12:33:48Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|91182b7e-e16b-4101-841e-43ecd4142863 | underdog | Rece Verhoff | XP Made | over | 0.052896617495658715 | 2026-11-11T06:09:33Z | 2026-11-15T00:00:00Z |
| underdog|115d1147-17ab-4f53-af6d-903795d66814 | underdog | Wayshawn Parker | Receiving Yards | over | 0.052795762377819244 | 2026-11-10T12:33:48Z | 2026-11-15T00:30:00Z |
| underdog|cfa3359c-93fb-4dec-8875-330c5bb338fe | underdog | Ty Dieffenbach | Pass TDs | over | 0.0524472047601649 | 2026-11-11T06:09:33Z | 2026-11-14T02:00:00Z |
| underdog|f48fdb97-2987-4a39-9762-8108b030233c | underdog | Jerry Jeudy | Receptions | over | 0.0520295111392754 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|6255d985-1786-44eb-a32c-d63bc33f898d | underdog | Mason Taylor | Receiving Yards | under | 0.052019637057471924 | 2026-11-11T16:13:16Z | 2026-11-15T18:00:00Z |
| underdog|a4cdc3ef-e490-44f7-9d22-9688f41616da | underdog | Jackson Kleather | XP Made | over | 0.051919363673327945 | 2026-11-11T06:09:33Z | 2026-11-14T17:00:00Z |
| underdog|feaedf13-f1cb-4e76-92bf-d9d0f7f8348f | underdog | Darnell Washington | Receiving Yards | under | 0.051680680891570296 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|c81f7f2e-696e-4498-b8ca-7a5799d1ee5a | underdog | Matthew Stafford | Pass TDs | under | 0.05151171430881951 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|3389d477-d409-4d1e-9768-b597fda63358 | underdog | Jaron-Keawe Sagapolutele | Pass TDs | over | 0.05145929241335612 | 2026-11-11T06:09:33Z | 2026-11-14T20:30:00Z |
| underdog|1cad5c50-a14c-4264-b134-2fea30d0ce4b | underdog | Michael Hawkins | Pass TDs | under | 0.05140454628829705 | 2026-11-11T22:47:13Z | 2026-11-14T22:30:00Z |
| underdog|2617048a-16d2-4090-93bd-da80e31dbd5d | underdog | Will Reichard | FG Made | under | 0.05137550778273203 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|fadbfc09-db71-4ef8-826d-37562bfd53c3 | underdog | Darnell Mooney | Receptions | under | 0.05131724403966509 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| underdog|7cb811fe-c69d-4856-ac57-f73eaad0a230 | underdog | Emmett Johnson | Receiving Yards | over | 0.051125680051020694 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|18a023c5-4ecc-4a21-8aaf-37db43e1f379 | underdog | Ka'imi Fairbairn | Kicking Points | under | 0.051123365189716385 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|098448c6-792b-4aaf-8f02-ba09091cf1ab | underdog | Jacoby Brissett | Rush Yards | over | 0.05093240883796324 | 2026-11-11T22:47:13Z | 2026-11-17T01:15:00Z |
| underdog|6f162ba5-023c-43aa-a379-1d9313eee6b7 | underdog | Byrum Brown | Pass TDs | over | 0.0508137269370349 | 2026-11-11T16:13:16Z | 2026-11-14T17:00:00Z |
| underdog|41d0472a-ee6d-4c60-89cd-d9f433caba37 | underdog | Matthew Stafford | Pass Attempts | under | 0.05081255657798445 | 2026-11-12T07:07:56Z | 2026-11-15T21:05:00Z |
| prizepicks|16910229 | prizepicks | Laura Samson | Total Games | over | 0.05072214408901943 | 2026-11-12T07:07:56Z | 2026-11-12T10:00:00.000-05:00 |
| underdog|3ca28cbe-3045-437d-b482-074b9e547595 | underdog | Justice Hill | Receptions | under | 0.050695143750179694 | 2026-11-10T12:33:48Z | 2026-11-17T01:15:00Z |
| underdog|95bb1f37-aede-4d17-9905-18286a2f0b06 | underdog | Justin Bowick | Receptions | under | 0.05059544511891889 | 2026-11-11T16:13:16Z | 2026-11-15T02:30:00Z |
| underdog|6f3992ec-ac05-417d-a59f-5320790a1d41 | underdog | Peyton Woodring | XP Made | over | 0.050105935886552544 | 2026-11-12T07:07:56Z | 2026-11-14T20:30:00Z |
| underdog|59e2f566-77d5-47c2-be43-7e60e746892c | underdog | Quinshon Judkins | Rush + Rec Yards | under | 0.05000923524525169 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| prizepicks|16863710 | prizepicks | Jaylen Warren | Rec Targets | under | 0.04958776690173983 | 2026-11-11T06:09:33Z | 2026-11-15T20:20:00.000-05:00 |
| underdog|b38d0fe8-eeff-48b0-b233-c1b9ed0a7e6b | underdog | Ja'Cory Thomas | Receptions | over | 0.04930579434434934 | 2026-11-11T22:47:13Z | 2026-11-14T17:45:00Z |
| underdog|0e47b5e3-2f9a-43f5-b530-f47623ccfa9d | underdog | Drew Sample | Receiving Yards | over | 0.049239250011618774 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|b0cca6f8-4778-4c16-a13b-0a64187791a6 | underdog | Malachi Fields | Receptions | under | 0.049099800290027695 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| underdog|e1ac2eb5-1b06-4c10-bdf8-7f90226e99da | underdog | Tyler Allgeier | Rush + Rec Yards | under | 0.04905091174473275 | 2026-11-12T07:07:56Z | 2026-11-15T21:05:00Z |
| prizepicks|16898722 | prizepicks | CJ Baxter Jr. | Rush Atts | under | 0.04899163749296942 | 2026-11-12T07:07:56Z | 2026-11-14T18:15:00.000-05:00 |
| underdog|9023da88-45ca-48fc-8bec-4e8f73ece9ba | underdog | Xavier Hutchinson | Receiving Yards | under | 0.04896690384698854 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| prizepicks|16834806 | prizepicks | Caleb Douglas | Rec Yards | under | 0.048911928496814694 | 2026-11-10T12:33:48Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|c84a3beb-c4ce-43b0-b1c9-9dedf70a41a8 | underdog | Ethan Grunkemeyer | Pass TDs | under | 0.048739349247589714 | 2026-11-11T22:47:13Z | 2026-11-15T00:30:00Z |
| underdog|a866c628-b0be-4b1d-97ea-bb7cbe41078a | underdog | Elija Lofton | Receptions | under | 0.048515481309444164 | 2026-11-11T16:13:16Z | 2026-11-14T17:00:00Z |
| underdog|9cd6e319-56d8-4146-8720-122e222c0af3 | underdog | Kimani Vidal | Receiving Yards | under | 0.04845077626655159 | 2026-11-11T22:47:13Z | 2026-11-17T01:15:00Z |
| underdog|d33dfd23-5d28-400c-9285-f07b81124821 | underdog | Braelon Allen | Receiving Yards | over | 0.04840674330017225 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|320e4928-163a-4eb4-baca-1fffe8cf4cf0 | underdog | Jamal Roberts | Rush Yards | over | 0.04837798218349576 | 2026-11-11T16:13:16Z | 2026-11-14T20:30:00Z |
| underdog|95231ceb-e90a-420c-98e0-a38f678fbb41 | underdog | Joe Burrow | Pass TDs | over | 0.04830047288438544 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| underdog|6acbfb7a-1667-4143-82f8-d566e5c26ae3 | underdog | Brock Bowers | Receptions | under | 0.04826815873810608 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|9989e1b9-b4e8-419b-a6df-1817c05c39eb | underdog | Mark Andrews | Receiving Yards | under | 0.04815263125185609 | 2026-11-12T07:07:56Z | 2026-11-17T01:15:00Z |
| underdog|62eb81c8-587e-4412-aa01-e88467fb3ba9 | underdog | Aidan Mizell | Receptions | over | 0.04807968139293489 | 2026-11-11T06:09:33Z | 2026-11-14T02:00:00Z |
| underdog|7c39f112-919c-49a0-afa7-1531cb9e8151 | underdog | Dylan Sampson | Receptions | under | 0.04803084524216095 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|f8ae7a0e-0afb-41bd-98a8-4bfa74cfc4b7 | underdog | Kirk Cousins | Rush Yards | over | 0.04794648374314203 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|1032257e-1efc-462a-bf42-9b9ad9a98765 | underdog | Tyler Allgeier | Rush Yards | under | 0.04793242597393543 | 2026-11-12T07:07:56Z | 2026-11-15T21:05:00Z |
| underdog|0e9a4487-87c8-4333-aeb3-599e0ba3e2d4 | underdog | Dylan Sampson | Receiving Yards | under | 0.047889791154614225 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|cbb27715-4c5c-4930-9405-886767da9aa0 | underdog | Spencer Porath | FG Made | under | 0.04726926706009371 | 2026-11-11T06:09:33Z | 2026-11-14T20:30:00Z |
| underdog|492d7a4a-5e80-462d-8498-0157b894b60d | underdog | Theo Johnson | Receptions | under | 0.047168476751986876 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| underdog|783ad07f-c3c8-40af-b1e7-144e266dc642 | underdog | Tristen Brown | Receiving Yards | over | 0.04716464158769673 | 2026-11-11T22:47:13Z | 2026-11-14T17:45:00Z |
| underdog|0ea9a1f4-b2c7-49f5-ae0a-5fb13ab0b949 | underdog | Jake Bates | FG Made | under | 0.04711758110912212 | 2026-11-11T06:09:33Z | 2026-11-15T14:30:00Z |
| underdog|8c8303ef-c5eb-4ffc-b6a8-c74177ec1ef5 | underdog | Marcus Stokes | Rush Yards | over | 0.047041918727074306 | 2026-11-12T07:07:56Z | 2026-11-13T01:00:00Z |
| underdog|fd31bc9e-cff4-44fb-ae49-6c536d56bce8 | underdog | Caleb Douglas | Receptions | under | 0.046873180612608145 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|3ea61498-fa94-4af5-8484-07f8ebe802f1 | underdog | Jackson Kleather | FG Made | under | 0.04681472825576749 | 2026-11-11T06:09:33Z | 2026-11-14T17:00:00Z |
| underdog|f388882e-bf96-4bf0-ab4f-c20217916353 | underdog | Harold Fannin | Receptions | under | 0.046638245325585026 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|0954ce59-bee3-4a2d-bc77-5496d047c7b0 | underdog | Devin Singletary | Receptions | over | 0.04661474918471048 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| underdog|d4acec1c-8f8f-4897-8e60-b7c7b956d82d | underdog | James Cook | Receptions | under | 0.0465337444974383 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|4d4ccc74-d749-4dd8-96a1-300b915bbbb9 | underdog | Brock Purdy | Rush Yards | under | 0.04644274743930077 | 2026-11-11T16:13:16Z | 2026-11-15T21:25:00Z |
| underdog|64bae3d3-f674-4a45-807a-d51d2feb6d54 | underdog | Jaylen Warren | Rush + Rec Yards | under | 0.046435927839737046 | 2026-11-11T22:47:13Z | 2026-11-16T01:20:00Z |
| underdog|8f7554a9-0fe8-46d2-b5ad-c793b08971f5 | underdog | Raleek Brown | Rush Yards | under | 0.04627628939768902 | 2026-11-11T16:13:16Z | 2026-11-15T00:30:00Z |
| prizepicks|16899263 | prizepicks | Chuba Hubbard | Rush TDs | under | 0.04625994985710902 | 2026-11-11T22:47:13Z | 2026-11-15T13:00:00.000-05:00 |
| underdog|6c90d765-2043-4abc-be89-2441e45fdbc2 | underdog | Josh Downs | Receptions | over | 0.04620180299105142 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|49dbe735-a6e1-435e-b05b-067376ee32f9 | underdog | Joey Slye | FG Made | under | 0.04617041472475325 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|f5af09ce-6733-4b1b-9e56-a6de2b4cbcf4 | underdog | Rocco Becht | Pass TDs | over | 0.04606321132899205 | 2026-11-11T06:09:33Z | 2026-11-15T00:00:00Z |
| underdog|0d7845b0-7f5f-4d31-91af-99fe5edf24ed | underdog | James Cook | Receiving Yards | over | 0.04596118738224697 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|593907c0-a952-4ce2-a792-fa5c25e0a816 | underdog | Marvin Harrison | Receptions | under | 0.04586912171191271 | 2026-11-11T16:13:16Z | 2026-11-15T18:00:00Z |
| underdog|56e8eb86-0cbf-469f-8c79-3ef93f017dea | underdog | Denzel Boston | Receptions | under | 0.045152048025238756 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|ae810589-81e6-4ea2-8235-0aef0fd1070e | underdog | Joey Slye | Kicking Points | under | 0.04505178064548698 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|78c07d75-953d-4627-8898-e0a1e9304e2c | underdog | Makhilyn Young | Rush Yards | over | 0.044951919440831434 | 2026-11-11T22:47:13Z | 2026-11-14T17:45:00Z |
| underdog|f0780ba2-8037-4cc2-a253-38e5dd6c1369 | underdog | Brendan Baird | XP Made | under | 0.04490246123339292 | 2026-11-10T12:33:48Z | 2026-11-14T17:00:00Z |
| underdog|8aa26f4f-6c4a-4c9b-bbb8-477e19ee6923 | underdog | Griffin Wilde | Receptions | under | 0.04484180164367657 | 2026-11-11T22:47:13Z | 2026-11-14T17:00:00Z |
| underdog|0d0ed7cc-e252-4db3-99ec-cdfe05a7bff4 | underdog | Davis Warren | Pass TDs | over | 0.04483350875789249 | 2026-11-11T22:47:13Z | 2026-11-15T00:30:00Z |
| prizepicks|16906356 | prizepicks | DeJuan Williams | Rush Atts | under | 0.04472446734389435 | 2026-11-12T07:07:56Z | 2026-11-14T12:00:00.000-05:00 |
| underdog|5bf6a659-5022-4ed2-a1e5-712c8112fb8e | underdog | Towns McGough | XP Made | under | 0.04462742213713622 | 2026-11-11T22:47:13Z | 2026-11-14T20:30:00Z |
| underdog|90d793ad-ef81-488f-944e-0ae32e36a829 | underdog | Eric Singleton | Receiving Yards | under | 0.04453515030062438 | 2026-11-12T07:07:56Z | 2026-11-14T23:15:00Z |
| underdog|2fd3b25f-aae4-417f-9d95-7162bc43f705 | underdog | Brian Rowe | Receiving Yards | over | 0.04452429303055938 | 2026-11-11T06:09:33Z | 2026-11-14T02:00:00Z |
| underdog|abd2a971-8dda-402b-88df-314e26b682f2 | underdog | Raleek Brown | Receiving Yards | over | 0.04450253600200227 | 2026-11-11T16:13:16Z | 2026-11-15T00:30:00Z |
| underdog|64386d41-4d93-4b84-b120-db1c96ed93b4 | underdog | Josh Cuevas | Receptions | over | 0.04428788516490878 | 2026-11-11T22:47:13Z | 2026-11-17T01:15:00Z |
| underdog|1f7f7044-5b58-4a4d-9b16-261d3cdb43ec | underdog | Travis Kelce | Receptions | under | 0.04401834231992152 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|d6eb2c7e-a907-43ce-96e7-68dc113793ec | underdog | Lincoln Kienholz | Pass Yards | under | 0.04377069081243479 | 2026-11-12T07:07:56Z | 2026-11-15T00:00:00Z |
| underdog|6a359aa0-6068-4eb0-8c11-237d31a4d274 | underdog | Chuba Hubbard | Receiving Yards | under | 0.04371106231349298 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|06aa0f5f-6f09-44bd-a64c-29b236608b45 | underdog | Scott Starzyk | FG Made | over | 0.043538923860573675 | 2026-11-11T16:13:16Z | 2026-11-15T00:30:00Z |
| underdog|b0083ee0-93e7-47cb-83c8-b293cc47bfc2 | underdog | Keaton Mitchell | Rush Yards | over | 0.04345065280751048 | 2026-11-11T22:47:13Z | 2026-11-17T01:15:00Z |
| underdog|b36f306c-d699-4184-8d28-66eb945fc1c2 | underdog | Elijah Higgins | Receiving Yards | under | 0.043442453369481826 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|b1961b19-7c23-4d20-8d28-8fd0c9426352 | underdog | AJ Surace | Pass TDs | under | 0.04326562864797223 | 2026-11-11T22:47:13Z | 2026-11-14T17:30:00Z |
| prizepicks|16907455 | prizepicks | Taylor Fritz | Total Games | over | 0.04290846956186811 | 2026-11-12T07:07:56Z | 2026-11-12T12:30:00.000-05:00 |
| underdog|7329e355-2a86-45ec-82e8-9c94abd631d1 | underdog | Craig Dandridge | Receiving Yards | over | 0.04273914522921507 | 2026-11-11T22:47:13Z | 2026-11-14T20:30:00Z |
| underdog|4e030a9e-3ae0-425d-a208-3a2abd4ed094 | underdog | Christian Watson | Receiving Yards | under | 0.04268826437734097 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|dd9ccb7a-bffb-4472-be26-448ceee6db64 | underdog | Keaton Mitchell | Receptions | under | 0.04260594560207376 | 2026-11-11T22:47:13Z | 2026-11-17T01:15:00Z |
| underdog|b03c56fa-f1b4-4ed3-8f2c-6e053fa36930 | underdog | Justice Hill | Receiving Yards | under | 0.042334380979668684 | 2026-11-11T22:47:13Z | 2026-11-17T01:15:00Z |
| underdog|741b63a8-a778-45dc-8a3c-618f25571627 | underdog | Harrison Butker | FG Made | under | 0.04233008949187933 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|aac8322b-1ee8-46b4-92bf-a2afefe76f97 | underdog | Braden Pegan | Receiving Yards | under | 0.04226457688012075 | 2026-11-10T12:33:48Z | 2026-11-15T00:30:00Z |
| underdog|95c05909-55d3-4c40-baa2-21c12deb1a59 | underdog | Justin Herbert | Rush Yards | under | 0.04188540886632808 | 2026-11-11T22:47:13Z | 2026-11-17T01:15:00Z |
| underdog|0ef8efe3-b6d5-4ed4-b722-1eeab13065a6 | underdog | Lincoln Kienholz | Pass TDs | under | 0.04176370900092663 | 2026-11-11T06:09:33Z | 2026-11-15T00:00:00Z |
| underdog|96a329b5-38e7-4b8b-a27e-6589f2d3bc55 | underdog | CJ Baxter | Rush Yards | under | 0.04174879097274642 | 2026-11-12T07:07:56Z | 2026-11-14T23:15:00Z |
| underdog|94cc4393-ed78-41f3-bde5-b30173c95a06 | underdog | J'Koby Williams | Receiving Yards | over | 0.041689854183781794 | 2026-11-12T07:07:56Z | 2026-11-15T02:30:00Z |
| underdog|c667e18c-a628-4d36-9edc-d635b9011f35 | underdog | Van Jefferson | Receptions | over | 0.041663000758345836 | 2026-11-11T06:09:33Z | 2026-11-13T01:15:00Z |
| underdog|55cb13c1-ee46-47e8-b0ce-5d68bc2910db | underdog | Connor Calvert | XP Made | over | 0.04166023250717721 | 2026-11-10T12:33:48Z | 2026-11-14T17:00:00Z |
| underdog|b96e5afb-b999-4933-8781-cd4c11d325c9 | underdog | Jack Bech | Receptions | under | 0.04163575481719084 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|42d3755e-92d9-474a-802d-e950a7184b31 | underdog | Jonathan Dimas | XP Made | under | 0.04162851872089324 | 2026-11-11T16:13:16Z | 2026-11-14T03:15:00Z |
| underdog|79e5a165-4bcb-4fa2-ba0d-6d6d063dcefa | underdog | Collin Dixon | Receiving Yards | under | 0.04153024391434135 | 2026-11-11T06:09:33Z | 2026-11-14T02:00:00Z |
| underdog|2fa9e2b4-614d-4a17-9548-927d0f196189 | underdog | Derrick Henry | Receptions | under | 0.04138130744755619 | 2026-11-10T12:33:48Z | 2026-11-17T01:15:00Z |
| underdog|b519b161-4417-4dbb-8e1c-64a49cbe1b03 | underdog | Jayden Maiava | Pass Yards | under | 0.04136793364471936 | 2026-11-11T22:47:13Z | 2026-11-14T20:30:00Z |
| underdog|992f3e80-6aa2-4ce0-bca9-9bd0cba69874 | underdog | Ashton Jeanty | Receptions | under | 0.041325909181133325 | 2026-11-10T12:33:48Z | 2026-11-15T21:05:00Z |
| underdog|c84b896f-85cf-4660-b039-6206a109df86 | underdog | Harrison Butker | Kicking Points | under | 0.04132208878674781 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|debd4cd0-78bb-46dd-9ec0-a3950267fe75 | underdog | Jeremiah Smith | Receiving Yards | under | 0.0411375305041668 | 2026-11-11T22:47:13Z | 2026-11-14T17:00:00Z |
| underdog|67747872-704b-4454-82f2-7a9d062419d0 | underdog | Donovan Olugbode | Receiving Yards | over | 0.04082423386128298 | 2026-11-11T16:13:16Z | 2026-11-14T20:30:00Z |
| underdog|6c901193-65b8-4432-bdf1-ea670655b227 | underdog | Amare Thomas | Receiving Yards | under | 0.04060844427005095 | 2026-11-11T06:09:33Z | 2026-11-14T03:15:00Z |
| underdog|63f35c03-cf3a-4a60-9e48-e6b9aee69d0c | underdog | Jordan Love | Pass TDs | under | 0.04051564232645721 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|f3acd35c-51ac-4b98-81d7-5f632298e45c | underdog | Pierre Strong Jr. | Rush Yards | under | 0.040405873993211716 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|2f4553e1-0da4-4d71-8b67-1fd42e9cdc71 | underdog | Josh Downs | Receiving Yards | over | 0.04029482074756141 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|1db7ecd1-0702-4cb8-a4f2-92623b86e6db | underdog | Tony Pollard | Rush Yards | under | 0.03993806716619375 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|38a660e4-afcb-4a9a-88da-cbc720d6058c | underdog | Blake Corum | Receiving Yards | over | 0.03956691390896483 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|e1b62a44-6489-415e-b6fb-d10b9253bfcf | underdog | Dilin Jones | Receiving Yards | over | 0.039459116156089324 | 2026-11-11T16:13:16Z | 2026-11-15T00:30:00Z |
| underdog|bb750385-cd4b-427e-99bb-aa1c719550b9 | underdog | Ashton Jeanty | Rush + Rec Yards | under | 0.03931795414340944 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|07a0eb6c-d8d9-46bf-aac3-dfed58d52aa7 | underdog | Braelon Allen | Receptions | over | 0.039314624923994734 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|d8b03841-950e-438e-b854-d18417ae6d47 | underdog | Bear Bachmeier | Rush Yards | under | 0.03919720056348952 | 2026-11-11T22:47:13Z | 2026-11-14T20:30:00Z |
| underdog|03361ce4-9586-4b1b-b660-d9a3da6d9a64 | underdog | Ethan Moczulski | XP Made | over | 0.03851062357902946 | 2026-11-10T12:33:48Z | 2026-11-14T02:00:00Z |
| underdog|a8ce8a0d-b252-405b-97ec-d2c24fe29262 | underdog | Dalton Kincaid | Receiving Yards | under | 0.03848081974045625 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|9dd7c202-7b28-46bd-a054-da7dca89c2e5 | underdog | Isaiah Likely | Receptions | under | 0.03790936636152842 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| underdog|ae1c8874-c0a0-434d-a31d-809ff3d59e49 | underdog | Kenneth Walker III | Receiving Yards | under | 0.03781672498542721 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|a5a6d1c9-ded0-4642-a1f5-1ea9ec0675f8 | underdog | Aidan Mizell | Receiving Yards | over | 0.03779757086546476 | 2026-11-11T06:09:33Z | 2026-11-14T02:00:00Z |
| underdog|62feb1a5-364b-40b5-b222-2b6392c3100f | underdog | Rocco Becht | Pass Yards | under | 0.03760487762117248 | 2026-11-12T07:07:56Z | 2026-11-15T00:00:00Z |
| underdog|eb9cd0d1-1393-4883-af70-ad82a20cc4ad | underdog | Mike Washington | Rush + Rec Yards | under | 0.03738270996578963 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|024cff8f-3c0b-41d3-b64f-ea8842dfe2e7 | underdog | Ashton Jeanty | Rush Yards | under | 0.03729288076056669 | 2026-11-12T07:07:56Z | 2026-11-15T21:05:00Z |
| underdog|79b51a9d-10f0-4647-b5d6-01757cccc2e1 | underdog | Breece Hall | Receiving Yards | over | 0.037205470306806765 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|fa9bddc8-e6d7-4bba-8ace-9ab2de5ab31e | underdog | Darren Waller | Receiving Yards | under | 0.037039947520251415 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|4d82b7f0-d383-413f-97c1-7d74814849b1 | underdog | Geno Smith | Pass TDs | over | 0.03690270527418432 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|77980a28-dcb2-41d0-8eab-38ec4e2aa752 | underdog | Ashton Daniels | Rush Yards | under | 0.03683393764457632 | 2026-11-11T16:13:16Z | 2026-11-14T00:00:00Z |
| underdog|a98832ad-cc1c-4f28-9746-8d27fb8ec062 | underdog | Joe Burrow | Rush Yards | over | 0.03676432878965474 | 2026-11-10T12:33:48Z | 2026-11-16T01:20:00Z |
| underdog|160f76fd-f374-4e88-b8cd-db6a5cad7742 | underdog | Ty Clark | Rush Yards | under | 0.03667004373890259 | 2026-11-11T16:13:16Z | 2026-11-14T17:00:00Z |
| underdog|d5e53e5c-71f4-4086-99fb-69639e63e727 | underdog | Mateen Bhaghani | FG Made | over | 0.036598637318603355 | 2026-11-10T12:33:48Z | 2026-11-14T02:00:00Z |
| underdog|e651acf4-4d9b-4e70-bf0a-715a88f6ef9b | underdog | Devaughn Vele | Receiving Yards | over | 0.03657711025657884 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|815884cd-c47a-4bea-9164-10c9864f1b76 | underdog | Samaje Perine | Rush Yards | under | 0.036568016460259756 | 2026-11-12T07:07:56Z | 2026-11-16T01:20:00Z |
| underdog|efa064e1-1d12-4402-b56d-f10cd02509c3 | underdog | Michael Hawkins | Pass Yards | under | 0.03650439461465371 | 2026-11-11T22:47:13Z | 2026-11-14T22:30:00Z |
| underdog|9cd574f3-89de-4e8a-9ceb-5e892f3875dc | underdog | Rashod Bateman | Receptions | over | 0.036295203210838234 | 2026-11-11T22:47:13Z | 2026-11-17T01:15:00Z |
| prizepicks|16863708 | prizepicks | Darnell Washington | Rec Targets | under | 0.03622440116764336 | 2026-11-11T06:09:33Z | 2026-11-15T20:20:00.000-05:00 |
| underdog|0fbebad7-ef4b-4c1e-b622-c8921e501f7f | underdog | King Miller | Rush Yards | over | 0.036196766847854 | 2026-11-11T06:09:33Z | 2026-11-14T20:30:00Z |
| underdog|584121f2-3498-45db-86d2-51230f6e6643 | underdog | Asaad Waseem | Receiving Yards | over | 0.036152712041357615 | 2026-11-11T06:09:33Z | 2026-11-15T00:30:00Z |
| underdog|7e214067-4ba0-412c-845a-dce679ce43cc | underdog | Scott Starzyk | XP Made | over | 0.03604303058757463 | 2026-11-11T22:47:13Z | 2026-11-15T00:30:00Z |
| underdog|f8e1b6cd-77a0-4be1-a219-14bcfd3cd8d7 | underdog | Mark Bowman | Receptions | over | 0.03586401830463126 | 2026-11-12T07:07:56Z | 2026-11-14T20:30:00Z |
| underdog|faa2c8d5-23df-4a3b-b36e-a445e23f4bcc | underdog | Wyatt Young | Receiving Yards | under | 0.03581009761990406 | 2026-11-11T16:13:16Z | 2026-11-15T02:30:00Z |
| underdog|33c569ea-e2cc-4587-bc5d-c61aea1dfe3a | underdog | Devaughn Vele | Receptions | over | 0.03560111354860207 | 2026-11-11T16:13:16Z | 2026-11-15T18:00:00Z |
| prizepicks|16863713 | prizepicks | Chase Brown | Rec Targets | under | 0.03548427625308703 | 2026-11-11T06:09:33Z | 2026-11-15T20:20:00.000-05:00 |
| underdog|f9718fc2-efda-4a87-aef5-4567c95c0b12 | underdog | Elic Ayomanor | Receiving Yards | under | 0.03545112441580822 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|274f14ba-1d4b-469e-8cfb-8fcd873ebcb8 | underdog | Andre Szmyt | Kicking Points | under | 0.035194355906048136 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|d3533652-67c2-4228-8da4-9887e1218937 | underdog | Noah Gray | Receptions | over | 0.03516926483455424 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|ae363647-2d9e-4fd4-b548-fc834f69a4fd | underdog | Bijan Robinson | Receptions | under | 0.0351075871491785 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|15e7da85-b67a-45cf-aab7-f91b96bcec06 | underdog | Ryan Hopkins | Pass TDs | over | 0.03505060031602475 | 2026-11-12T07:07:56Z | 2026-11-14T17:00:00Z |
| underdog|e9f2c10c-6978-4134-9666-1cdc9df3a448 | underdog | Will Reichard | Kicking Points | under | 0.03483187705738011 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|6f97d46e-a116-4fdf-b56f-fa4f859335c6 | underdog | Patrick Mahomes | Rush Yards | under | 0.03479240021177232 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|6c90a01b-7358-4ad0-94ff-073fe0feb8c2 | underdog | Bo Jackson | Receiving Yards | over | 0.034524710439674866 | 2026-11-11T22:47:13Z | 2026-11-14T17:00:00Z |
| underdog|0d992edd-d005-49b6-bc13-742d0c606adb | underdog | Gunnar Helm | Receiving Yards | under | 0.03448784863389276 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|48b3d0ad-b5d3-4fa9-922e-3cd734113bba | underdog | Treylon Burks | Receiving Yards | under | 0.03432763870733557 | 2026-11-12T07:07:56Z | 2026-11-13T01:15:00Z |
| underdog|c41bdf61-ec11-47ea-aa1a-d7caf74b5490 | underdog | Javonte Williams | Receiving Yards | under | 0.03421399617321885 | 2026-11-11T06:09:33Z | 2026-11-15T21:25:00Z |
| underdog|89bf8183-bd08-4703-ace9-5a6a0f2494b9 | underdog | Jaylen Warren | Rush Yards | under | 0.034088465358187325 | 2026-11-11T22:47:13Z | 2026-11-16T01:20:00Z |
| underdog|5eed7261-a329-46a9-8b9b-e6510e877a59 | underdog | Rico Dowdle | Receiving Yards | under | 0.03408492305432431 | 2026-11-11T06:09:33Z | 2026-11-16T01:20:00Z |
| prizepicks|16897307 | prizepicks | Treylon Burks | Rec Targets | under | 0.03401161640581851 | 2026-11-11T16:13:16Z | 2026-11-12T20:15:00.000-05:00 |
| underdog|23b66a37-6604-4da4-9c56-8777d5d8be05 | underdog | Sam Leavitt | Pass Yards | under | 0.033960722668088916 | 2026-11-11T16:13:16Z | 2026-11-15T00:30:00Z |
| underdog|eda6defe-1ce6-482b-97c1-2f177b9337e9 | underdog | Cam Skattebo | Receiving Yards | over | 0.03385701304435074 | 2026-11-10T12:33:48Z | 2026-11-13T01:15:00Z |
| underdog|f04cdcb8-a7b9-444b-82cd-d9c4f68b5331 | underdog | Braelon Allen | Rush Yards | over | 0.03360981687067632 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|6b057709-d6dc-4521-be96-04631e1d5383 | underdog | Devin McCuin | Receptions | over | 0.03350696128296665 | 2026-11-11T22:47:13Z | 2026-11-14T17:00:00Z |
| underdog|1ceddca8-fe53-49f8-831a-62aa046bb636 | underdog | Wan'Dale Robinson | Receptions | under | 0.033293997712305456 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|b7e99795-da26-48e8-8250-77ae145b57a0 | underdog | Omar Cooper | Receptions | over | 0.033145857239147036 | 2026-11-12T07:07:56Z | 2026-11-15T18:00:00Z |
| underdog|e5a1d8cc-9fd0-4363-a0ec-b6077999af5f | underdog | Savion Williams | Receptions | under | 0.03308677892440648 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|1532deaf-e39a-42f6-9444-fb37fb0c6508 | underdog | Jordan Love | Rush Yards | under | 0.03279240845654863 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| prizepicks|16863704 | prizepicks | Jahmyr Gibbs | Rec Targets | under | 0.032604420063334416 | 2026-11-11T06:09:33Z | 2026-11-15T09:30:00.000-05:00 |
| underdog|ccea17c8-e390-4da5-badf-d4cc345723dd | underdog | Jared Curtis | Pass TDs | under | 0.03245948310828595 | 2026-11-11T22:47:13Z | 2026-11-14T17:45:00Z |
| underdog|6497b72f-8917-4fb8-bf75-fee9b6802c4b | underdog | Mitchell Evans | Receptions | over | 0.032392458273830194 | 2026-11-10T12:33:48Z | 2026-11-15T18:00:00Z |
| underdog|98477925-df33-489d-b2b9-aea1be0fb8df | underdog | Van Jefferson | Receiving Yards | over | 0.0323146860417286 | 2026-11-11T16:13:16Z | 2026-11-13T01:15:00Z |
| underdog|8524a49e-70e8-44ba-b50f-e5749a1f9e20 | underdog | Marcus Stokes | Pass Yards | under | 0.03212516938121879 | 2026-11-12T07:07:56Z | 2026-11-13T01:00:00Z |
| underdog|025f64b9-c0b3-46a3-a947-ad3479490326 | underdog | Adonai Mitchell | Receiving Yards | under | 0.031903411083543554 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|8206c911-50a1-4311-a9ab-a4bce1c90765 | underdog | Ja'Cory Thomas | Receiving Yards | over | 0.03176549797720041 | 2026-11-11T22:47:13Z | 2026-11-14T17:45:00Z |
| underdog|7e7631f5-e3d4-46ed-b5f1-266bf3d7b45a | underdog | Jalen Coker | Receptions | under | 0.031714257024792025 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| underdog|e15b1902-efc1-481a-ac83-fb2fee335221 | underdog | Ashton Jeanty | Receiving Yards | over | 0.031645254793110755 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|665ae279-78e6-4223-a74c-26d667482925 | underdog | Drake Lindsey | Pass Yards | under | 0.031633010395235694 | 2026-11-12T07:07:56Z | 2026-11-15T00:00:00Z |
| underdog|02db5ac0-d83a-4739-b360-6691e089d776 | underdog | Aaron Jones | Rush Yards | over | 0.03155148511107231 | 2026-11-11T22:47:13Z | 2026-11-15T18:00:00Z |
| underdog|792b0d48-a54c-4ebf-9850-d82cd32eb4e1 | underdog | Mario Craver | Receptions | over | 0.03154931517292969 | 2026-11-11T16:13:16Z | 2026-11-14T20:00:00Z |
| underdog|4e3d83a3-32df-4adc-a6cb-19c47ccd3314 | underdog | Mike Washington | Rush Yards | under | 0.031494264716392606 | 2026-11-11T22:47:13Z | 2026-11-15T21:05:00Z |
| underdog|fc87e960-7746-4e65-90af-f9d3506e7fc4 | underdog | T.J. Hockenson | Receptions | under | 0.031480752318138516 | 2026-11-11T06:09:33Z | 2026-11-15T18:00:00Z |
| prizepicks|16869349 | prizepicks | Guillaume Restes | Goalie Saves | under | 0.031223900098698354 | 2026-11-11T06:09:33Z | 2026-11-12T14:45:00.000-05:00 |
| underdog|2141e4e3-e6bd-419a-b8b6-ce264d9e74f3 | underdog | Charlie Becker | Receiving Yards | under | 0.03107999426582564 | 2026-11-10T12:33:48Z | 2026-11-14T20:30:00Z |
| underdog|3c55b8d7-f72b-4d57-b825-1e0f75a1c9f1 | underdog | Fame Ijeboi | Rush Yards | over | 0.031074656707587134 | 2026-11-11T06:09:33Z | 2026-11-15T00:30:00Z |
| prizepicks|16834647 | prizepicks | Javonte Williams | Rush Yards | under | 0.030973438538770326 | 2026-11-10T12:33:48Z | 2026-11-15T16:25:00.000-05:00 |
| underdog|701a1df8-3bb4-4f3b-b85e-2aa6a225c316 | underdog | Cameron Dicker | Kicking Points | under | 0.03086807179622797 | 2026-11-11T22:47:13Z | 2026-11-17T01:15:00Z |
| underdog|242c333e-4229-4bd6-981b-3f85497b6e4e | underdog | Brock Bowers | Receiving Yards | under | 0.0306330498389088 | 2026-11-11T06:09:33Z | 2026-11-15T21:05:00Z |
| underdog|d649c6df-5a33-430f-ad49-de2a7613706b | underdog | Peyton Woodring | FG Made | over | 0.030478185796160684 | 2026-11-11T16:13:16Z | 2026-11-14T20:30:00Z |
| underdog|f1fb25a0-6179-4fbc-935a-268c21e6a711 | underdog | Re'Shaun Sanford | Rush Yards | under | 0.03045602797791802 | 2026-11-11T06:09:33Z | 2026-11-14T03:15:00Z |
| underdog|fd930764-9c2d-48e5-af2b-e31c158a80ef | underdog | Dylan Raiola | Pass TDs | over | 0.030427485178013636 | 2026-11-12T07:07:56Z | 2026-11-14T20:30:00Z |
| underdog|d86772b1-c024-41b8-93d5-7c5dc8255d49 | underdog | Miles Coleman | Receiving Yards | under | 0.030316694491087315 | 2026-11-11T16:13:16Z | 2026-11-15T02:30:00Z |
| underdog|b357c9e8-27ef-4f86-9497-cac10d884f8c | underdog | Sam LaPorta | Receptions | under | 0.030234889226053996 | 2026-11-10T12:33:48Z | 2026-11-15T14:30:00Z |
