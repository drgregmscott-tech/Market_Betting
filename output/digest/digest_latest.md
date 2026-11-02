# Pipeline Digest -- 2026-11-02T05:51:59Z

## Run summary
- Ingestion: 19160 rows (PrizePicks OK, Underdog OK)
- Estimation: 19160 rows estimated (from 19160 ingested props)
- CLV logging: 23 newly flagged, 0 newly closed, 81 still open (107435 total ever logged)

## Currently open flags
Sizing is a manual step (sizing_engine.py, Session 2.6) -- this table is what to scan to pick a pair worth sizing.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_edge | first_flagged_at | game_start_time |
|---|---|---|---|---|---|---|---|
| underdog|faa089e3-80fc-4158-84b9-d7879fc131d8 | underdog | Caleb Williams | Pass Attempts | under | 0.4 | 2026-10-28T05:43:27Z | 2026-11-03T01:15:00Z |
| underdog|06ea1ec2-a39c-4302-8a00-22c5c81cc2b9 | underdog | Jadarian Price | Receiving Yards | over | 0.3922114493789265 | 2026-11-02T05:58:22Z | 2026-11-03T01:15:00Z |
| underdog|a9c098a9-5051-4b9c-9177-f98d2f838c81 | underdog | Caleb Williams | Pass Yards | under | 0.3207245998457888 | 2026-10-27T05:05:06Z | 2026-11-03T01:15:00Z |
| underdog|34a729d2-8161-40be-8a72-e15b9b64bb65 | underdog | Roschon Johnson | Receiving Yards | over | 0.26691790110944374 | 2026-11-01T06:01:49Z | 2026-11-03T01:15:00Z |
| underdog|8d7639cc-8c81-4bcd-89b0-a4d9587e8e59 | underdog | Leonard Williams | Sacks | over | 0.2330168881714022 | 2026-11-01T06:01:49Z | 2026-11-03T01:15:00Z |
| underdog|d3529e40-391b-42c2-ada3-d6f7e3d476c0 | underdog | Jaxon Smith-Njigba | Receiving Yards | under | 0.2207891416703074 | 2026-10-27T05:05:06Z | 2026-11-03T01:15:00Z |
| underdog|51ec653e-5829-4a08-8863-dc9fc0d26f27 | underdog | Nick Emmanwori | Sacks | over | 0.21274555999025022 | 2026-11-01T06:01:49Z | 2026-11-03T01:15:00Z |
| prizepicks|16534595 | prizepicks | Alina Charaeva | Aces | under | 0.20966246836377844 | 2026-11-02T05:58:22Z | 2026-11-02T21:00:00.000-05:00 |
| underdog|5b66effa-dd53-4035-839e-d2b3e15234ff | underdog | Sam Darnold | Pass Yards | under | 0.2094286719511248 | 2026-10-28T05:43:27Z | 2026-11-03T01:15:00Z |
| underdog|89f2aab7-d0de-46e1-a11c-4c7a519886ce | underdog | D'Andre Swift | Rush + Rec Yards | under | 0.19774091218346235 | 2026-11-01T06:01:49Z | 2026-11-03T01:15:00Z |
| underdog|f30e521b-39dc-4e16-8416-ee5e6bad58b9 | underdog | Colston Loveland | Receiving Yards | under | 0.18433645657794384 | 2026-10-28T05:43:27Z | 2026-11-03T01:15:00Z |
| underdog|649b6491-c509-4735-9316-861b90da8365 | underdog | Tory Horton | Receptions | under | 0.1817783211185915 | 2026-11-01T06:01:49Z | 2026-11-03T01:15:00Z |
| prizepicks|16238621 | prizepicks | Jaxon Smith-Njigba | Rec Yards | under | 0.17173160672708232 | 2026-10-27T05:05:06Z | 2026-11-02T20:15:00.000-05:00 |
| underdog|675961cf-bf8f-40bf-94da-0ca8d7bbcbb8 | underdog | Cooper Kupp | Receiving Yards | under | 0.1705919192288129 | 2026-11-01T06:01:49Z | 2026-11-03T01:15:00Z |
| underdog|9cceb1e6-82fb-466f-83fd-bea1572902f1 | underdog | AJ Barner | Receiving Yards | under | 0.1566729249501455 | 2026-11-01T06:01:49Z | 2026-11-03T01:15:00Z |
| prizepicks|16505871 | prizepicks | Suzan Lamens | 1st Set Total Games | over | 0.15639504930132797 | 2026-11-02T05:58:22Z | 2026-11-03T04:00:00.000-05:00 |
| underdog|c88a2927-a91e-410d-85bb-d364689d7194 | underdog | Sam Roush | Receptions | under | 0.15548621869608115 | 2026-11-02T05:58:22Z | 2026-11-03T01:15:00Z |
| underdog|583b83a3-6c19-4067-8b0c-fd0cac61a0a5 | underdog | Jarran Reed | Sacks | over | 0.15207198982432332 | 2026-10-31T05:34:00Z | 2026-11-03T01:15:00Z |
| underdog|06bd3a71-c486-4744-88f1-02bd31f7da20 | underdog | Cooper Kupp | Receptions | under | 0.15204934584969454 | 2026-11-01T06:01:49Z | 2026-11-03T01:15:00Z |
| prizepicks|16472461 | prizepicks | Mary Stoiana | Total Games | over | 0.15121696332276746 | 2026-11-01T06:01:49Z | 2026-11-01T21:00:00.000-05:00 |
| underdog|ef8e9fb6-3170-4bc2-a654-18c691ac3b09 | underdog | D'Andre Swift | Rush Yards | under | 0.14431233667100896 | 2026-10-29T05:46:21Z | 2026-11-03T01:15:00Z |
| underdog|59da26a9-80c7-4a40-a23b-3757e949b385 | underdog | Jason Myers | FG Made | under | 0.14119220966516732 | 2026-10-27T05:05:06Z | 2026-11-03T01:15:00Z |
| underdog|2a1701b8-ad0b-40ec-82bd-73af7b04907b | underdog | Magda Linette | Double Faults | under | 0.1321890427148089 | 2026-11-02T05:58:22Z | 2026-11-02T09:30:00Z |
| underdog|a0a1cd84-7140-4b79-94bb-c5dc8cffb254 | underdog | Cairo Santos | FG Made | under | 0.12940227002797755 | 2026-10-27T05:05:06Z | 2026-11-03T01:15:00Z |
| underdog|382cb467-86c1-4335-b776-6b7b833a1198 | underdog | Derick Hall | Sacks | over | 0.12228685163868297 | 2026-10-31T05:34:00Z | 2026-11-03T01:15:00Z |
| underdog|a8d65e72-cdf2-46c9-ad06-25735b026521 | underdog | Sam Darnold | Pass Attempts | under | 0.1167625142367642 | 2026-10-27T05:05:06Z | 2026-11-03T01:15:00Z |
| underdog|cb84333c-b246-4493-acec-acedce99822c | underdog | Caleb Williams | Pass TDs | under | 0.11529745995363427 | 2026-10-27T05:05:06Z | 2026-11-03T01:15:00Z |
| underdog|59905fd2-4d5c-4646-a528-93b6094e86bb | underdog | Jaxon Smith-Njigba | Receptions | under | 0.10234847580734763 | 2026-10-27T05:05:06Z | 2026-11-03T01:15:00Z |
| underdog|dba955cf-89ee-43b5-ad32-57eccdde7426 | underdog | Rome Odunze | Receiving Yards | under | 0.10135838550360621 | 2026-10-28T05:43:27Z | 2026-11-03T01:15:00Z |
| underdog|bf2203c2-c26a-40bf-a554-05c60e73d874 | underdog | Tory Horton | Receiving Yards | under | 0.09831055653888243 | 2026-11-01T06:01:49Z | 2026-11-03T01:15:00Z |
| prizepicks|16485533 | prizepicks | Tory Horton | Rec Targets | under | 0.09761239143770795 | 2026-11-01T06:01:49Z | 2026-11-02T20:15:00.000-05:00 |
| underdog|1fbcbf15-9d3a-4432-8f21-b665d10c38cb | underdog | Jeffery Simmons | Sacks | over | 0.09179338266897208 | 2026-11-02T05:58:22Z | 2026-11-03T01:15:00Z |
| prizepicks|16514653 | prizepicks | Maria Sakkari | Break Points Won | under | 0.09174328646119967 | 2026-11-02T05:58:22Z | 2026-11-02T02:10:00.000-05:00 |
| prizepicks|16485510 | prizepicks | D'Andre Swift | Rec Targets | under | 0.09093687084110336 | 2026-11-01T06:01:49Z | 2026-11-02T20:15:00.000-05:00 |
| prizepicks|16300984 | prizepicks | Rome Odunze | Rec Targets | under | 0.09000083847025231 | 2026-10-28T05:43:27Z | 2026-11-02T20:15:00.000-05:00 |
| underdog|c0199a09-88d6-41bd-a286-a771e0428d9e | underdog | Luther Burden | Receiving Yards | under | 0.0891800401053029 | 2026-10-28T05:43:27Z | 2026-11-03T01:15:00Z |
| underdog|990bd281-01f3-48ff-95f8-73098785a3f4 | underdog | Jadarian Price | Rush Yards | under | 0.08898714918086637 | 2026-11-01T06:01:49Z | 2026-11-03T01:15:00Z |
| underdog|c4405f0d-d269-40cb-b12e-2a6c886c9fd5 | underdog | Linda Fruhvirtova | Double Faults | under | 0.08751480890183694 | 2026-11-02T05:58:22Z | 2026-11-02T10:40:00Z |
| underdog|c8365fab-d29d-4b40-90e6-c5e32d2cbb0b | underdog | Sam Roush | Receiving Yards | under | 0.0872644346155037 | 2026-11-02T05:58:22Z | 2026-11-03T01:15:00Z |
| underdog|8d8ba36d-d4a7-4d82-a0cb-8f123a92b269 | underdog | Austin Booker | Sacks | over | 0.08704457438004476 | 2026-11-02T05:58:22Z | 2026-11-03T01:15:00Z |
| underdog|ce0094b8-608a-4f57-8db8-91acfa4ebf67 | underdog | D'Andre Swift | Receptions | under | 0.08536310216644005 | 2026-10-29T05:46:21Z | 2026-11-03T01:15:00Z |
| underdog|bc8b8b0a-5c41-4af1-96aa-d8f6e5ab57cf | underdog | Montez Sweat | Sacks | over | 0.0853087453461654 | 2026-11-02T05:58:22Z | 2026-11-03T01:15:00Z |
| prizepicks|16397378 | prizepicks | Caleb Williams | Pass+Rush+Rec TDs | under | 0.08370139667072873 | 2026-10-30T05:46:05Z | 2026-11-02T20:15:00.000-05:00 |
| underdog|29a57594-563b-446e-b1a8-c3d405a95378 | underdog | Sam Darnold | Pass TDs | under | 0.07875391297959822 | 2026-10-27T05:05:06Z | 2026-11-03T01:15:00Z |
| underdog|2ceab409-005c-44b1-9b76-c720516ef3f9 | underdog | AJ Barner | Receptions | under | 0.07759190318537934 | 2026-11-01T06:01:49Z | 2026-11-03T01:15:00Z |
| underdog|86034be6-d3b2-4841-b0a3-7cadb61884fc | underdog | D'Andre Swift | Receiving Yards | under | 0.07598977212251534 | 2026-10-29T05:46:21Z | 2026-11-03T01:15:00Z |
| prizepicks|16475392 | prizepicks | Simona Waltert | Total Games | over | 0.07491901065229767 | 2026-11-01T06:01:49Z | 2026-11-02T04:30:00.000-05:00 |
| prizepicks|16508636 | prizepicks | Maria Sakkari | Double Faults | under | 0.0724425765843496 | 2026-11-01T15:07:06Z | 2026-11-02T02:10:00.000-05:00 |
| prizepicks|16517327 | prizepicks | Benjamin Bonzi | Total Games Won | over | 0.07097145073166045 | 2026-11-02T05:58:22Z | 2026-11-03T05:00:00.000-05:00 |
| underdog|45a75d3a-e480-4f99-8f17-b68114c68f23 | underdog | Jadarian Price | Rush + Rec Yards | under | 0.07021629155409614 | 2026-11-02T05:58:22Z | 2026-11-03T01:15:00Z |
| underdog|a86885c8-11b3-4b77-99a3-0334c0e5be55 | underdog | Byron Murphy | Sacks | over | 0.06895126284676217 | 2026-10-31T05:34:00Z | 2026-11-03T01:15:00Z |
| prizepicks|16505872 | prizepicks | Suzan Lamens | Total Games | over | 0.06760957907495702 | 2026-11-02T05:58:22Z | 2026-11-03T04:00:00.000-05:00 |
| prizepicks|16300983 | prizepicks | Luther Burden III | Rec Targets | under | 0.06341229986208663 | 2026-10-28T05:43:27Z | 2026-11-02T20:15:00.000-05:00 |
| underdog|bccdaeba-931d-4bd2-815a-9c1a918714bd | underdog | Kalif Raymond | Receptions | over | 0.06292693874293909 | 2026-10-31T05:34:00Z | 2026-11-03T01:15:00Z |
| underdog|c2ee8575-a516-49ad-b97c-0da52c295e72 | underdog | Rome Odunze | Receptions | under | 0.06252906711956707 | 2026-10-28T05:43:27Z | 2026-11-03T01:15:00Z |
| underdog|e8b237a6-6015-4f5e-9939-49170f8e7a3c | underdog | Emanuel Wilson | Rush Yards | over | 0.06193256713556616 | 2026-11-01T06:01:49Z | 2026-11-03T01:15:00Z |
| underdog|e27c2406-eb38-4a14-8a00-80ac48b87304 | underdog | Simona Waltert | Double Faults | under | 0.06156120735185833 | 2026-11-02T05:58:22Z | 2026-11-02T11:50:00Z |
| prizepicks|16474537 | prizepicks | Janice Tjen | Total Games | over | 0.058911065496728865 | 2026-11-01T15:07:06Z | 2026-11-02T04:30:00.000-05:00 |
| underdog|53512f83-07fe-452f-801a-d8eb1ffb6954 | underdog | Katie Volynets | Double Faults | over | 0.056846779308753315 | 2026-11-02T05:58:22Z | 2026-11-02T07:10:00Z |
| underdog|b981d159-2a60-4c40-bbf7-6bd3366441b5 | underdog | Claire Liu | Double Faults | under | 0.056335485788838624 | 2026-11-02T05:58:22Z | 2026-11-02T06:00:00Z |
| underdog|534639cf-dfef-43e9-a654-d0e1df93574f | underdog | Cairo Santos | Kicking Points | under | 0.056155326916546455 | 2026-10-27T05:05:06Z | 2026-11-03T01:15:00Z |
| prizepicks|16466101 | prizepicks | Alycia Parks | Total Games Won | over | 0.050732012209038224 | 2026-11-01T06:01:49Z | 2026-11-01T21:00:00.000-05:00 |
| underdog|e153ec57-b9e4-428e-bcf9-73980fc4e0b1 | underdog | Aliaksandra Sasnovich | Double Faults | over | 0.048868278302204304 | 2026-11-02T05:58:22Z | 2026-11-02T07:10:00Z |
| prizepicks|16509138 | prizepicks | Oleksandra Oliynykova | Total Games Won | over | 0.04844112653570121 | 2026-11-02T05:58:22Z | 2026-11-02T21:00:00.000-05:00 |
| prizepicks|16465389 | prizepicks | Oleksandra Oliynykova | Total Games Won | over | 0.04844112653570121 | 2026-11-01T06:01:49Z | 2026-11-01T21:00:00.000-05:00 |
| prizepicks|16485531 | prizepicks | AJ Barner | Rec Targets | under | 0.04794042788369968 | 2026-11-01T06:01:49Z | 2026-11-02T20:15:00.000-05:00 |
| prizepicks|16523117 | prizepicks | Lorenzo Musetti | Break Points Won | over | 0.047623054826978595 | 2026-11-02T05:58:22Z | 2026-11-02T05:00:00.000-05:00 |
| underdog|ccf764a6-e25c-4a47-801c-bbf244f5ec13 | underdog | Colston Loveland | Receptions | under | 0.04553104131701269 | 2026-10-28T05:43:27Z | 2026-11-03T01:15:00Z |
| prizepicks|16485115 | prizepicks | D'Andre Swift | Recs | under | 0.04380787067268588 | 2026-11-01T06:01:49Z | 2026-11-02T20:15:00.000-05:00 |
| prizepicks|16478916 | prizepicks | Alejandro Tabilo | Total Games Won | over | 0.04147539456045368 | 2026-11-01T06:01:49Z | 2026-11-02T05:00:00.000-05:00 |
| underdog|1b24433d-6c5b-4706-82e2-09b5cde10318 | underdog | Roschon Johnson | Receptions | over | 0.041411964645610255 | 2026-11-01T06:01:49Z | 2026-11-03T01:15:00Z |
| prizepicks|16519585 | prizepicks | Mattia Bellucci | Total Tie Breaks | under | 0.04026317138264501 | 2026-11-02T05:58:22Z | 2026-11-02T08:30:00.000-05:00 |
| prizepicks|16485116 | prizepicks | Rome Odunze | Recs | under | 0.039140237826882696 | 2026-11-01T06:01:49Z | 2026-11-02T20:15:00.000-05:00 |
| underdog|4192d51e-49c7-433a-892e-6c32daf1a68a | underdog | Luther Burden | Receptions | under | 0.03905790770780704 | 2026-10-28T05:43:27Z | 2026-11-03T01:15:00Z |
| prizepicks|16300981 | prizepicks | Colston Loveland | Rec Targets | under | 0.03749133938696103 | 2026-10-28T05:43:27Z | 2026-11-02T20:15:00.000-05:00 |
| prizepicks|16473345 | prizepicks | Talia Gibson | Total Games | over | 0.03709645990115418 | 2026-11-01T06:01:49Z | 2026-11-01T21:00:00.000-05:00 |
| underdog|c7e7a148-f8c4-4cad-88bc-76bcb8c8e203 | underdog | Jason Myers | Kicking Points | under | 0.03595495125259396 | 2026-10-27T05:05:06Z | 2026-11-03T01:15:00Z |
| prizepicks|16516172 | prizepicks | Alex Molcan | Total Games | under | 0.03584941460722113 | 2026-11-02T05:58:22Z | 2026-11-02T10:40:00.000-05:00 |
| prizepicks|16534931 | prizepicks | Maria Timofeeva | Aces | over | 0.034221609148076815 | 2026-11-02T05:58:22Z | 2026-11-02T21:00:00.000-05:00 |
| underdog|1f68e0f5-4758-426a-a308-b5c68e1c8048 | underdog | Sam Darnold | Rush Yards | over | 0.0325476533253789 | 2026-10-27T05:05:06Z | 2026-11-03T01:15:00Z |
| prizepicks|16451315 | prizepicks | Ignacio Buse | Total Games Won | over | 0.031061051357671343 | 2026-11-01T06:01:49Z | 2026-11-02T05:00:00.000-05:00 |
