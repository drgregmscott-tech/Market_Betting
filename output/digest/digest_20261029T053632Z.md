# Pipeline Digest -- 2026-10-29T05:36:32Z

## Run summary
- Ingestion: 35688 rows (PrizePicks OK, Underdog OK)
- Estimation: 35688 rows estimated (from 35688 ingested props)
- CLV logging: 369 newly flagged, 0 newly closed, 745 still open (106582 total ever logged)

## Currently open flags
Sizing is a manual step (sizing_engine.py, Session 2.6) -- this table is what to scan to pick a pair worth sizing.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_edge | first_flagged_at | game_start_time |
|---|---|---|---|---|---|---|---|
| underdog|d54271ea-1ac6-4f11-9ae3-1bc3517bc245 | underdog | Tanner McKee | Pass TDs | under | 0.5635514018691589 | 2026-10-29T05:46:21Z | 2026-11-02T01:20:00Z |
| underdog|79fbdd4e-9f95-4c05-91ab-801fa00b9f95 | underdog | Jacoby Brissett | Pass Yards | under | 0.4601730325335911 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|2f5aaa24-7fb0-41f8-a373-c3b035aa8e86 | underdog | Malik Willis | Pass Yards | under | 0.44253845031977934 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|cbd6e719-1d7b-4baf-b4b8-82e8e169d339 | underdog | Tanner McKee | Pass Yards | under | 0.4357142857142857 | 2026-10-29T05:46:21Z | 2026-11-02T01:20:00Z |
| underdog|00b8c4ae-47ab-4321-88dd-8e806f1bb14b | underdog | Chase Brown | Rush + Rec Yards | under | 0.42261306532663323 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|12009851-2423-4ab3-91bd-f13fd4301a82 | underdog | Josh Allen | Pass Yards | under | 0.42261306532663323 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|2a6bed3b-c7b3-4711-a725-7549471b16c3 | underdog | Bryce Young | Pass Yards | under | 0.4114535454340761 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| underdog|57616bdd-aab7-4f96-b4bc-4643e4882cbc | underdog | Stefon Diggs | Receiving Yards | under | 0.411308499153475 | 2026-10-29T05:46:21Z | 2026-11-02T01:20:00Z |
| underdog|3fafb547-a80e-4119-b750-f8178a9ec1d1 | underdog | Geno Smith | Pass Yards | under | 0.40697585543065895 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|5c715537-c01f-477b-b764-20a57b702bd8 | underdog | Lamar Jackson | Pass Attempts | under | 0.4 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|3c8a224d-a083-4783-83ce-39c3dcbaf581 | underdog | Michael Penix | Pass Yards | under | 0.4 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|85973a27-8bc2-47e0-9aa3-0742a98196d6 | underdog | Cam Ward | Pass Yards | under | 0.4 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|faa089e3-80fc-4158-84b9-d7879fc131d8 | underdog | Caleb Williams | Pass Attempts | under | 0.4 | 2026-10-28T05:43:27Z | 2026-11-03T01:15:00Z |
| underdog|db5463ff-e8bc-462f-b571-812b6f3c7077 | underdog | Cole Tabb | Receiving Yards | over | 0.4 | 2026-10-29T05:46:21Z | 2026-10-31T19:45:00Z |
| underdog|cbbf56fd-1783-40d2-a4e3-ee386ff04cac | underdog | Dak Prescott | Pass Yards | under | 0.4 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|09deeeb4-ca9f-4b83-b827-341d93c45b7c | underdog | Tommy Carr | Pass Yards | under | 0.4 | 2026-10-29T05:46:21Z | 2026-10-31T16:30:00Z |
| underdog|dc6b4600-d899-46fe-9510-3e8eddec37b8 | underdog | Justin Herbert | Pass Yards | under | 0.4 | 2026-10-29T05:46:21Z | 2026-11-01T21:05:00Z |
| underdog|551de737-4ed8-4f82-8609-b1e2a3e0c17e | underdog | Trevor Lawrence | Pass Yards | under | 0.4 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|2491f256-7fe6-4dbe-b49b-d313ec64d9ce | underdog | Justin Herbert | Pass Attempts | under | 0.3961059254162722 | 2026-10-29T05:46:21Z | 2026-11-01T21:05:00Z |
| underdog|79604ed7-d7d4-437f-9e7e-0be17c3600ec | underdog | Joe Burrow | Pass Yards | under | 0.38083915915549604 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|87da43a0-1884-4911-b9fa-cc92f8d15e16 | underdog | Bo Nix | Pass Yards | under | 0.3761948122970198 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|3acf5e4b-d2bd-4a59-a6eb-512b84c05a16 | underdog | Tanner McKee | Pass Attempts | under | 0.37114298002617396 | 2026-10-29T05:46:21Z | 2026-11-02T01:20:00Z |
| underdog|bf9042bc-ea80-4cab-aca0-04fc4ea24646 | underdog | Bhayshul Tuten | Rush + Rec Yards | under | 0.36606460045862976 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|7b31b809-c2af-4bb7-b306-9fadeadd490b | underdog | Aaron Rodgers | Pass Yards | under | 0.3642857142857143 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|51026806-71eb-47e0-b24c-3e735dc9face | underdog | Michael Penix | Pass Attempts | under | 0.36083693901821556 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|d7d276a3-6770-4024-9eaf-2d86637b63b4 | underdog | Jayden Daniels | Pass Yards | under | 0.3602245957330912 | 2026-10-29T05:46:21Z | 2026-11-02T01:20:00Z |
| underdog|899a68de-e102-4983-8a34-59a7909475f8 | underdog | Deshaun Watson | Pass Attempts | under | 0.3579985593698499 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|28a2ea78-e692-4c07-bd82-65806aa4b30c | underdog | Baker Mayfield | Pass Yards | under | 0.35685279187817265 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|3c898aa0-cf88-40c7-8f3e-bccf4eb2a341 | underdog | A.J. Brown | Receiving Yards | under | 0.35177664974619294 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| prizepicks|16237064 | prizepicks | Malik Willis | Pass Yards | under | 0.35094246505677495 | 2026-10-27T05:05:06Z | 2026-11-01T16:25:00.000-05:00 |
| underdog|edb405a9-2108-4e53-980d-f2bfe7c76348 | underdog | Josh Allen | Pass Attempts | under | 0.34457095080515066 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|c6b45392-15a5-4784-9f7e-de4a0ccd50be | underdog | Jared Goff | Pass Yards | under | 0.33718592964824123 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|86c0f981-7496-4227-9196-e2f09e3cc959 | underdog | Kyler Murray | Pass Yards | under | 0.3360431449180866 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|a787f9cc-5177-4e80-a5c5-3a1c910d0dbb | underdog | Lamar Jackson | Pass Yards | under | 0.3343434343434344 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|9774f98f-74a5-4e9d-8086-0b8f1394f05e | underdog | Deshaun Watson | Pass Yards | under | 0.3339921704274391 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|894dbf45-d7f8-4bd4-af0e-3db65a37745f | underdog | Drake Maye | Pass Yards | under | 0.3294558529152034 | 2026-10-28T05:43:27Z | 2026-11-01T21:25:00Z |
| underdog|f20c590d-7e42-4932-a3cf-4750126c8a0c | underdog | Rachaad White | Rush Yards | under | 0.3290278063292911 | 2026-10-29T05:46:21Z | 2026-11-02T01:20:00Z |
| prizepicks|16237068 | prizepicks | Caleb Williams | Pass Yards | under | 0.32839021953788883 | 2026-10-27T05:05:06Z | 2026-11-02T20:15:00.000-05:00 |
| underdog|064f376d-57f1-44fb-b420-650bdf4b6b47 | underdog | Jaylen Wright | Rush Yards | under | 0.3261539848934951 | 2026-10-29T05:46:21Z | 2026-11-01T21:25:00Z |
| prizepicks|16237067 | prizepicks | Jayden Daniels | Pass Yards | under | 0.32372482407821346 | 2026-10-27T05:05:06Z | 2026-11-01T20:20:00.000-05:00 |
| underdog|2f1d2e08-979d-4b41-9b7f-9882d725836d | underdog | Bo Nix | Pass Attempts | under | 0.32234118524297706 | 2026-10-29T05:46:21Z | 2026-11-01T21:25:00Z |
| underdog|a9c098a9-5051-4b9c-9177-f98d2f838c81 | underdog | Caleb Williams | Pass Yards | under | 0.3207245998457888 | 2026-10-27T05:05:06Z | 2026-11-03T01:15:00Z |
| underdog|41cd46eb-3a8a-4dd5-b1a6-c2b98317813f | underdog | Baker Mayfield | Pass TDs | under | 0.31870442998094306 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|a21ab088-aafe-432d-ada0-8ecf849c089e | underdog | Jackson Gutierrez | Pass Yards | over | 0.31697013211654346 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| underdog|39f3f7fc-6c39-444a-897e-8dfbc45427fa | underdog | Sam Darnold | Pass Yards | under | 0.3143741598167539 | 2026-10-27T05:05:06Z | 2026-11-03T01:15:00Z |
| underdog|7010fc48-e8bd-484a-a77d-ed3385b61098 | underdog | Ja'Marr Chase | Receiving Yards | under | 0.31405028667298107 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|f061b6f3-ad6b-4386-856f-0b3badbf9989 | underdog | Cam Ward | Pass Attempts | under | 0.3077298561599473 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|cc99b30f-5f59-43ff-b0e2-3e6d5670212b | underdog | Drew Stevens | Kicking Points | under | 0.3045316875544547 | 2026-10-29T05:46:21Z | 2026-11-02T01:20:00Z |
| underdog|4af1d2c4-9389-4932-bdbf-25ba879d7f98 | underdog | Kirk Cousins | Pass Yards | under | 0.3029545016904194 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|9f5cb0c8-1fbf-4866-bd6b-ecb5fe6c0fd9 | underdog | Tanner McKee | Rush Yards | under | 0.3028836980632086 | 2026-10-29T05:46:21Z | 2026-11-02T01:20:00Z |
| prizepicks|16237060 | prizepicks | Geno Smith | Pass Yards | under | 0.3012472919929988 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|f0925bda-0452-45bf-b5cb-e99abb959340 | underdog | Daniel Jones | Pass Yards | under | 0.30049745428740415 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|7e44dbb6-bebc-4d95-b84b-2172e298f971 | underdog | Drew Stevens | FG Made | under | 0.2989225028687452 | 2026-10-29T05:46:21Z | 2026-11-02T01:20:00Z |
| underdog|e186aaee-33d8-47a8-a671-d147d27ec573 | underdog | Bryce Young | Pass Attempts | under | 0.29886265932684264 | 2026-10-29T05:46:21Z | 2026-10-30T00:15:00Z |
| underdog|036b2b4a-4c13-4a88-98c4-08c2f91b6f5b | underdog | Malik Willis | Pass Attempts | under | 0.2950573943673964 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| prizepicks|16239378 | prizepicks | Savion Williams | Rec Targets | under | 0.29408939080290064 | 2026-10-27T05:05:06Z | 2026-10-29T20:15:00.000-04:00 |
| underdog|688d08a6-db4b-4741-9b64-3f2d4083db4c | underdog | Rhamondre Stevenson | Rush Yards | under | 0.29100110024273373 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|77134685-90f4-4cf7-b654-07f91bf45e2b | underdog | Jordan Love | Pass TDs | under | 0.28932884359695743 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| underdog|3e004d77-31b6-42d3-b335-ec61b9c5ca37 | underdog | Drake Maye | Pass Attempts | under | 0.28783365045991505 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|d5c345a0-7dae-4b78-9edb-954680fb81ee | underdog | Jordan Love | Pass Yards | under | 0.283637013212797 | 2026-10-28T05:43:27Z | 2026-10-30T00:15:00Z |
| underdog|96197cf8-42ed-46d7-9dc6-75ce2b734496 | underdog | Bhayshul Tuten | Rush Yards | under | 0.2830925953549398 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|6de5eab0-2d35-4f98-8799-55ec06c20902 | underdog | Puka Nacua | Receiving Yards | under | 0.28071098205655276 | 2026-10-29T05:46:21Z | 2026-11-01T21:05:00Z |
| underdog|7092f88f-46e2-415b-a562-fdb316594c91 | underdog | Trey McBride | Receptions | under | 0.27996701649605604 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|ada6c5be-5574-4704-84a8-170ae5ad6e25 | underdog | Bo Jackson | Rush Yards | under | 0.27700737850252466 | 2026-10-28T05:43:27Z | 2026-10-31T23:30:00Z |
| prizepicks|16237065 | prizepicks | Patrick Mahomes | Pass Yards | under | 0.27446569007052457 | 2026-10-27T05:05:06Z | 2026-11-01T16:25:00.000-05:00 |
| underdog|17dc7cec-3c82-4150-80af-68ab4e38fdf7 | underdog | Patrick Mahomes | Pass Yards | under | 0.27297421579815784 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|d9869842-86dc-4a54-8415-c94120bc72c3 | underdog | Emeka Egbuka | Receiving Yards | under | 0.27242401200514144 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|1b19b801-5dd2-4ad6-a834-00145631d33b | underdog | Brock Bowers | Receiving Yards | under | 0.27119252222161794 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|2333cf5c-2dc4-48f5-b002-20b236cb3f49 | underdog | Trey McBride | Receiving Yards | under | 0.269142467981241 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|f161a7dd-ea16-471a-896e-a8a0a18e4f7c | underdog | Patrick Mahomes | Pass Attempts | under | 0.2675186997366973 | 2026-10-29T05:46:21Z | 2026-11-01T21:25:00Z |
| prizepicks|16238609 | prizepicks | Puka Nacua | Rec Yards | under | 0.26601067771574083 | 2026-10-27T05:05:06Z | 2026-11-01T16:05:00.000-05:00 |
| prizepicks|16238598 | prizepicks | Ja'Marr Chase | Rec Yards | under | 0.2595902767393615 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|d11a4e9c-a4c2-4797-af01-622070bdd555 | underdog | Kyler Murray | Pass TDs | under | 0.25843685929932236 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16364186 | prizepicks | Trey McBride | Rec Targets | under | 0.25784568005227304 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|171776c8-2cba-4822-af8b-9cccabb0ba30 | underdog | Ja'Kobi Lane | Receiving Yards | under | 0.25079110375599434 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|d246086d-7c65-42e0-933e-6b8dd6601fbf | underdog | Joe Burrow | Pass Attempts | under | 0.24993731024741228 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|4ee6b97c-89c0-4981-b20f-3274ce84bf13 | underdog | Baker Mayfield | Pass Attempts | under | 0.2497362780760891 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|c6d1047f-d48a-4b4f-94b8-60a6ab509a0d | underdog | Jackson Gutierrez | Pass TDs | over | 0.24950392888425482 | 2026-10-28T05:43:27Z | 2026-10-31T16:00:00Z |
| underdog|8bde0391-ccde-4dfc-9cb2-8ef5c29b490f | underdog | Antonio Williams | Receptions | under | 0.2479315173455695 | 2026-10-29T05:46:21Z | 2026-11-02T01:20:00Z |
| underdog|48811b9c-7e60-4593-a528-2b9034180b39 | underdog | Jake Elliott | FG Made | under | 0.247649803080637 | 2026-10-29T05:46:21Z | 2026-11-02T01:20:00Z |
| underdog|3d52227b-cf66-4d88-a32a-5a8cc2a92833 | underdog | Tucker Kraft | Receiving Yards | under | 0.24652148805707685 | 2026-10-29T05:46:21Z | 2026-10-30T00:15:00Z |
| underdog|5eaaba0a-f069-47a9-b1b8-7c791844ccd3 | underdog | Geno Smith | Pass Attempts | under | 0.2429302888957946 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|2f557637-9041-4541-9fdc-a98aa4979f85 | underdog | Daniel Jones | Pass TDs | under | 0.24111157975554776 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|714c4e03-5b55-4f5c-949c-b056d52f89c5 | underdog | Aaron Rodgers | Pass Attempts | under | 0.23899560341545345 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|b5cab8eb-ac30-4ab2-bf1a-892f0f41a451 | underdog | Trevor Lawrence | Pass Attempts | under | 0.23880589410721487 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|b871d24e-b512-49bf-af0d-87e4256afb83 | underdog | Jared Goff | Pass Attempts | under | 0.23810199295358325 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|7a3c6b9e-58a0-4566-81c4-e690454cfeb6 | underdog | Joe McFadden | XP Made | over | 0.23621662260627513 | 2026-10-29T05:46:21Z | 2026-10-31T20:15:00Z |
| underdog|0964d4fd-2061-4374-9c1c-0aa1d0d2e8fd | underdog | Jahmyr Gibbs | Receptions | under | 0.23462427954615162 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|2accf469-d7a9-40b3-9fc4-b939f36ffe1d | underdog | Lamar Jackson | Pass TDs | under | 0.2311213220174536 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|279fd967-4a9b-4f11-82a9-bd2328494b9e | underdog | Ja'Marr Chase | Receptions | under | 0.2309204690720832 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|28a5790f-38b0-4885-a9cc-ce2ce1a8332b | underdog | Caden Veltkamp | Pass Yards | under | 0.22969999277707642 | 2026-10-29T05:46:21Z | 2026-10-29T23:30:00Z |
| underdog|a7958068-81fe-40ef-a70d-9dc09a562438 | underdog | Brendan Baird | XP Made | under | 0.22744796592916927 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| underdog|28b552af-0b9a-4f7a-8167-90e11dd3b5f6 | underdog | Kyle Pitts | Receiving Yards | under | 0.22471131955490853 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|da179e4a-1fa3-4518-9789-cb524e343dfe | underdog | Jayden Daniels | Pass Attempts | under | 0.22392278838988666 | 2026-10-29T05:46:21Z | 2026-11-02T01:20:00Z |
| underdog|dc982051-1283-44f9-9566-94eea47aa893 | underdog | Kyler Kasper | Receiving Yards | under | 0.2237656727032502 | 2026-10-29T05:46:21Z | 2026-10-31T19:30:00Z |
| underdog|d3529e40-391b-42c2-ada3-d6f7e3d476c0 | underdog | Jaxon Smith-Njigba | Receiving Yards | under | 0.2207891416703074 | 2026-10-27T05:05:06Z | 2026-11-03T01:15:00Z |
| underdog|66738651-7f99-4df0-b9b0-522c7620a839 | underdog | Holden Geriner | Pass TDs | under | 0.22032080131551335 | 2026-10-29T05:46:21Z | 2026-10-31T23:30:00Z |
| underdog|30c4939c-5645-40ae-8353-daea4cad9a36 | underdog | Savion Williams | Receptions | under | 0.22006641268961324 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| underdog|0e4d5ac6-81bf-450d-9497-23a66b4d41f0 | underdog | Jacoby Brissett | Pass Attempts | under | 0.21816784342592277 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|f7524e19-6d40-4ee0-b16e-2bb6e66f7a04 | underdog | Holden Geriner | Pass Yards | under | 0.21765002909131614 | 2026-10-29T05:46:21Z | 2026-10-31T23:30:00Z |
| underdog|94afae91-7080-4e19-b465-21ee5ba92e1e | underdog | Wan'Dale Robinson | Receiving Yards | under | 0.21730599801522976 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|6b4b4c00-4d70-41e2-adff-2c131eb5d27e | underdog | John Mateer | Pass Yards | under | 0.21717585441688603 | 2026-10-29T05:46:21Z | 2026-10-31T20:15:00Z |
| underdog|8fe6381c-70d0-44c4-840e-e579b9212e6b | underdog | Justin Herbert | Pass TDs | under | 0.2167420814479638 | 2026-10-27T05:05:06Z | 2026-11-01T21:05:00Z |
| prizepicks|16316136 | prizepicks | John Bates | Rec Yards | over | 0.2159230700072322 | 2026-10-28T05:43:27Z | 2026-11-01T20:20:00.000-05:00 |
| underdog|dd212962-6dca-4f26-abc7-d169783d01ac | underdog | Kyler Murray | Pass Attempts | under | 0.21576631517107925 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|e5a24c45-43a3-4338-af2a-9140730a85a3 | underdog | Cam Ward | Pass TDs | under | 0.2150615767583154 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| prizepicks|16238606 | prizepicks | Brock Bowers | Rec Yards | under | 0.2140636967499886 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|a521534e-bbf6-4dac-abfa-041b66362962 | underdog | Daniel Jones | Pass Attempts | under | 0.21258660675643404 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|6a748d90-5fb9-4ae4-87d9-be1bb9b4eef7 | underdog | Josh Allen | Pass TDs | under | 0.20834299379221988 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|034d7617-ad80-48f4-a6e1-4c37d782f395 | underdog | Matthew Stafford | Pass Yards | under | 0.20696325020402107 | 2026-10-28T05:43:27Z | 2026-11-01T21:05:00Z |
| underdog|3299abed-a981-4179-881a-08a58e180eee | underdog | Rece Verhoff | XP Made | over | 0.20670284300837638 | 2026-10-28T05:43:27Z | 2026-10-31T23:30:00Z |
| underdog|27893231-fb65-490d-a9b8-2391c00c9302 | underdog | Savion Williams | Receiving Yards | under | 0.20661248735369653 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| prizepicks|16238594 | prizepicks | Trey McBride | Rec Yards | under | 0.20630682894084595 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|631afbbe-b351-40e2-8a8f-19762138a645 | underdog | Stefon Diggs | Receptions | under | 0.20419601930534237 | 2026-10-29T05:46:21Z | 2026-11-02T01:20:00Z |
| underdog|dfa79e9f-f0fc-4d49-88c3-22f6bd24d524 | underdog | Ollie Gordon | Receiving Yards | under | 0.20149579334312173 | 2026-10-28T05:43:27Z | 2026-11-01T21:25:00Z |
| prizepicks|16237760 | prizepicks | Rhamondre Stevenson | Rush Yards | under | 0.20003838369682592 | 2026-10-27T05:05:06Z | 2026-11-01T16:25:00.000-05:00 |
| underdog|0631e5d6-eab6-465f-a56e-d362d91226c9 | underdog | Jordan Love | Pass Attempts | under | 0.19733015924696584 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| underdog|8ee5a905-2917-42eb-9a59-992b6d7530e2 | underdog | Jacoby Brissett | Pass TDs | under | 0.19731880187813977 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|d028c6bc-f38a-46d7-8b03-fcb2a9abb87c | underdog | George Pickens | Receiving Yards | under | 0.19725314760148782 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|50469855-5b2f-44cf-8413-7e8a99d15cd2 | underdog | Bryce Young | Rush Yards | under | 0.19504980897098123 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| underdog|d804b353-6d81-45a9-81d4-4821ccfb1227 | underdog | Carson Hilbert | XP Made | under | 0.1949100968222911 | 2026-10-29T05:46:21Z | 2026-10-31T19:15:00Z |
| underdog|09a6542e-f25f-48dd-9d53-85ac48fa25c1 | underdog | Matthew Golden | Receptions | under | 0.1933475355920763 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| underdog|37294e13-0fad-4e6d-9bb0-502d8d20e81d | underdog | Kenny Gainwell | Receiving Yards | under | 0.19226146698041036 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|17353939-73dc-440d-827b-d9413d18d844 | underdog | Dak Prescott | Pass Attempts | under | 0.19093639525880723 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|396fa408-0a5f-4be5-b9a7-b20f30dbd908 | underdog | Parker Washington | Receptions | under | 0.18996406742376704 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16364183 | prizepicks | Drake London | Rec Targets | under | 0.18922823043011128 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|db7df02f-c054-41a9-aa50-0fd66fb3afa1 | underdog | Amon-Ra St. Brown | Receiving Yards | under | 0.18760906654565868 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|665535ac-210f-4c3c-9efb-de102e073220 | underdog | Daniel Bellinger | Receiving Yards | under | 0.18709530086778547 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|a88da4c3-d490-41a8-b54a-86ce070351ec | underdog | Nolan Bartley | XP Made | over | 0.18701446242147501 | 2026-10-28T05:43:27Z | 2026-10-31T16:00:00Z |
| underdog|1a87dc5a-0387-436b-9d58-fbdb641c9bd8 | underdog | Alberto Mendoza | Pass Yards | under | 0.18681934501810127 | 2026-10-29T05:46:21Z | 2026-10-31T23:30:00Z |
| underdog|4f609d9d-58a0-47f7-b7e8-b812cc106fb0 | underdog | D'Andre Swift | Rush + Rec Yards | under | 0.18496961586725102 | 2026-10-29T05:46:21Z | 2026-11-03T01:15:00Z |
| underdog|f30e521b-39dc-4e16-8416-ee5e6bad58b9 | underdog | Colston Loveland | Receiving Yards | under | 0.18433645657794384 | 2026-10-28T05:43:27Z | 2026-11-03T01:15:00Z |
| underdog|afa68e3a-abf5-48e3-967b-2750d6d956ab | underdog | Derrick Henry | Rush Yards | under | 0.18337816433194976 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|410eda24-d2b6-440a-b958-aa33d85789c9 | underdog | Rachaad White | Rush + Rec Yards | under | 0.1828101063180283 | 2026-10-29T05:46:21Z | 2026-11-02T01:20:00Z |
| underdog|e75911b6-9cc3-4852-9c95-ea8aebde12fc | underdog | Kirk Cousins | Pass Attempts | under | 0.18259810381735442 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|cd108833-dd0c-40ec-bbc3-fb69c4c04b16 | underdog | Dru DeShields | Pass TDs | under | 0.18258589692008098 | 2026-10-29T05:46:21Z | 2026-10-31T02:30:00Z |
| underdog|e62da64a-4678-4964-bd5d-88acd4ec999d | underdog | Brevyn Spann-Ford | Receiving Yards | under | 0.18214542209116402 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|d0ae9eb4-c8f7-4862-8d7a-231c6b97a944 | underdog | Kaitlin Quevedo | Double Faults | under | 0.18178068498630018 | 2026-10-29T05:46:21Z | 2026-10-29T07:20:00Z |
| underdog|3ca5d2bb-528c-404a-bff3-edbe7514ece3 | underdog | Ladd McConkey | Receiving Yards | under | 0.1795212118159959 | 2026-10-29T05:46:21Z | 2026-11-01T21:05:00Z |
| underdog|3a83b28e-d200-4f72-b740-bff3d10e07eb | underdog | Chris Godwin | Receptions | under | 0.17933771848483437 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|684c3765-0511-4cc7-9d8a-5be14ac8cd71 | underdog | Germie Bernard | Receiving Yards | under | 0.17801647476795757 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16364188 | prizepicks | Denzel Boston | Rec Targets | under | 0.17748575411214362 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|103605f2-9b72-4426-885b-0238715e9ac0 | underdog | Matthew Stafford | Rush Yards | over | 0.17706361202904009 | 2026-10-27T05:05:06Z | 2026-11-01T21:05:00Z |
| underdog|cf672a90-aa86-4cd8-8f8b-dd0d13229542 | underdog | Tyler Warren | Receiving Yards | under | 0.17652993569650421 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|0b40bf0e-9d64-489d-8c90-b365276d4bd7 | underdog | Drew Mestemaker | Pass Yards | under | 0.17651399299740933 | 2026-10-29T05:46:21Z | 2026-10-31T23:00:00Z |
| prizepicks|16364180 | prizepicks | Ja'Kobi Lane | Rec Targets | under | 0.1763735536367902 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|38e0faee-0c91-422b-974f-d7d80ab6de29 | underdog | Gunnar Helm | Receiving Yards | under | 0.17598595760600988 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|af5c7d85-cb99-4044-9ef5-d2ddc3408b0e | underdog | Malik Washington | Receptions | under | 0.17563895451595535 | 2026-10-29T05:46:21Z | 2026-11-01T21:25:00Z |
| underdog|9303c8b4-2d98-4758-b335-51c9666b2989 | underdog | Ray Davis | Rush Yards | under | 0.1751366077070703 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|a0020a56-eca9-42bc-b548-2457584b7982 | underdog | Parker Washington | Receiving Yards | under | 0.17427174460304196 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|5b0fbf58-2d38-4bfa-a85d-c5ec591d6220 | underdog | Kyle Pitts | Receptions | under | 0.1729010034408106 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16345984 | prizepicks | Ja'Marr Chase | Rec Targets | under | 0.17261768944514488 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| prizepicks|16238621 | prizepicks | Jaxon Smith-Njigba | Rec Yards | under | 0.17173160672708232 | 2026-10-27T05:05:06Z | 2026-11-02T20:15:00.000-05:00 |
| underdog|1343a522-9c45-4117-98d2-02eb6ca31f2e | underdog | Darian Mensah | Rush Yards | over | 0.17156773564058403 | 2026-10-28T05:43:27Z | 2026-10-31T23:30:00Z |
| underdog|8d20d6cf-52a2-4503-b49b-4784d7ed4edd | underdog | Jonnu Smith | Receiving Yards | over | 0.1710903797997952 | 2026-10-29T05:46:21Z | 2026-10-30T00:15:00Z |
| underdog|8f8931b0-0f49-46a1-af8a-cf650f624c68 | underdog | Amon-Ra St. Brown | Receptions | under | 0.17005505014758315 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|4b334497-079e-4edb-89d2-f1aab306023d | underdog | Jameson Williams | Receiving Yards | under | 0.17002164741431403 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|7c5d072f-ccf3-471d-b5bf-82f1fb8cf5a0 | underdog | Tait Reynolds | Pass TDs | under | 0.16772614658985985 | 2026-10-29T05:46:21Z | 2026-10-31T23:00:00Z |
| underdog|487af6cb-d6c3-4cb8-9bd1-2b624f598c87 | underdog | Trinidad Chambliss | Pass Yards | under | 0.16767421434568486 | 2026-10-29T05:46:21Z | 2026-10-31T16:45:00Z |
| underdog|58beea02-ce1c-4111-9b19-274c2a209770 | underdog | Michael Wilson | Receiving Yards | under | 0.16679482576786897 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|975e879a-5e2a-4148-8e68-53843d4cf242 | underdog | Brock Bowers | Receptions | under | 0.16633992785137308 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|63f02d88-f21a-4014-b8d8-3067aa9100d3 | underdog | Derrick Henry | Rush + Rec Yards | under | 0.16630730952151507 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|c3e02d0f-f003-4f7e-8ad6-fffa1a0ec9fc | underdog | Braden Atkinson | Pass Yards | under | 0.16583125521128483 | 2026-10-29T05:46:21Z | 2026-11-01T03:00:00Z |
| underdog|f6c1be5e-e4e1-4bde-b99e-bfa2f10a50e5 | underdog | Javonte Williams | Rush + Rec Yards | under | 0.1644205723540778 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|6003f2fa-2374-436f-ad95-ade56cf40059 | underdog | Khalil Shakir | Receptions | under | 0.16378974695954318 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|d8d25309-128a-4374-999a-2ad2201aa96b | underdog | Breece Hall | Rush + Rec Yards | under | 0.16363073940516593 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|9aee412b-f046-4a7b-917c-207ef0bf657e | underdog | Zay Flowers | Receptions | under | 0.16336849774056705 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| prizepicks|16283156 | prizepicks | Kyler Murray | Fantasy Score | under | 0.16330900700221884 | 2026-10-28T05:43:27Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|2cf26b57-0452-47fb-9a95-cac7cef34370 | underdog | Colby Parkinson | Receiving Yards | under | 0.16302930851970687 | 2026-10-27T05:05:06Z | 2026-11-01T21:05:00Z |
| underdog|8e6927a7-a912-4c9d-a8f8-da4c36100e0f | underdog | Jaylen Wright | Rush + Rec Yards | under | 0.16000000000000003 | 2026-10-29T05:46:21Z | 2026-11-01T21:25:00Z |
| underdog|39bbd93a-c47e-49d9-8688-d284b1bba708 | underdog | Malik Willis | Pass TDs | under | 0.15983936929525455 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|f98df416-202b-4ab3-beba-521e0540581e | underdog | Billy Edwards Jr. | Pass Yards | under | 0.15837856813656637 | 2026-10-28T05:43:27Z | 2026-10-31T23:30:00Z |
| underdog|145d8ff5-2477-453e-a412-e28c5d64621c | underdog | Sam LaPorta | Receiving Yards | under | 0.1576776056199558 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|509d8eb8-b43e-47fd-8fa2-f7cf746a55c1 | underdog | Dak Prescott | Pass TDs | under | 0.15719525295831893 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|6ca856fe-84a5-4e1b-af59-dcf676216710 | underdog | Dru DeShields | Pass Yards | under | 0.1568354625708842 | 2026-10-29T05:46:21Z | 2026-10-31T02:30:00Z |
| prizepicks|16239377 | prizepicks | Tucker Kraft | Rec Targets | under | 0.15579549797772507 | 2026-10-27T05:05:06Z | 2026-10-29T20:15:00.000-04:00 |
| underdog|0d9340f9-d542-4642-8ad5-3a0264d45869 | underdog | Jalen Coker | Receiving Yards | under | 0.15506437267651652 | 2026-10-28T05:43:27Z | 2026-10-30T00:15:00Z |
| prizepicks|16283724 | prizepicks | Amon-Ra St. Brown | Rec Targets | under | 0.15422522569585284 | 2026-10-28T05:43:27Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|eaad8225-0b13-489d-9dfb-6a7415e9a871 | underdog | John Metchie III | Receptions | under | 0.15296044248863871 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| underdog|958b449c-8b51-4628-9101-92daad11f271 | underdog | Trey Smack | Kicking Points | under | 0.1525920290900875 | 2026-10-28T05:43:27Z | 2026-10-30T00:15:00Z |
| underdog|301f45d5-2a5a-449b-b397-68ad730d1370 | underdog | Garrett Wilson | Receiving Yards | under | 0.1515587767143275 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|eebe204a-45c0-403b-be16-321a9d1f6a5a | underdog | Rico Dowdle | Rush Yards | under | 0.1502305033665604 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|9566880e-8490-456d-b73a-5984e9ca91ff | underdog | Mark Andrews | Receiving Yards | under | 0.14977065038209925 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|5cb4098b-5bb4-45ef-ba4d-f91a68625257 | underdog | Jalen Coker | Receptions | under | 0.1495115674735762 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| prizepicks|16327007 | prizepicks | Yasmine Kabbaj | Total Games Won | over | 0.14931706747058515 | 2026-10-29T05:46:21Z | 2026-10-29T10:00:00.000-04:00 |
| underdog|b36420f5-f15b-4a56-89a1-7382ef291a53 | underdog | Lincoln Kienholz | Pass TDs | under | 0.14918083670510207 | 2026-10-29T05:46:21Z | 2026-10-31T19:15:00Z |
| underdog|1a9232ac-a9e6-4437-a14e-83b35514624a | underdog | Jahiem White | Rush Yards | under | 0.14866149259831307 | 2026-10-29T05:46:21Z | 2026-10-29T23:30:00Z |
| underdog|f9ff6dca-6916-4d44-8c58-756c6bb60455 | underdog | Tre Tucker | Receptions | under | 0.1484779084275395 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|bf3e998b-2c4a-42bb-b8d0-ae92c029a6c3 | underdog | Noah Fifita | Pass Yards | under | 0.1483775242207117 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| underdog|76504010-664b-4a0f-a892-b2ae5aa57b49 | underdog | Jesse Legree | Receptions | under | 0.1478639792128641 | 2026-10-29T05:46:21Z | 2026-11-01T03:00:00Z |
| underdog|c9fcbe6e-efd8-4eaa-9ad2-3ad49380bd62 | underdog | Nick Marsh | Receptions | under | 0.1476174693281791 | 2026-10-29T05:46:21Z | 2026-10-31T19:30:00Z |
| prizepicks|16238597 | prizepicks | Wan'Dale Robinson | Rec Yards | under | 0.1474324804852314 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|d5c2bc10-f8de-48ad-9888-e23da8986a27 | underdog | Gunner Stockton | Pass Yards | under | 0.1470432520894447 | 2026-10-28T05:43:27Z | 2026-10-31T19:30:00Z |
| underdog|facf9eef-31fc-49e7-8eb9-f6ee5f12ffff | underdog | Chris Godwin | Receiving Yards | under | 0.14668040701874563 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| prizepicks|16364205 | prizepicks | Ladd McConkey | Rec Targets | under | 0.14667292733946524 | 2026-10-29T05:46:21Z | 2026-11-01T16:05:00.000-05:00 |
| underdog|56955058-de76-456b-ac8e-8e0ae8753edd | underdog | Jared Goff | Rush Yards | over | 0.14467131524506371 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16364184 | prizepicks | Jahan Dotson | Rec Targets | under | 0.1446232979211045 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|ef8e9fb6-3170-4bc2-a654-18c691ac3b09 | underdog | D'Andre Swift | Rush Yards | under | 0.14431233667100896 | 2026-10-29T05:46:21Z | 2026-11-03T01:15:00Z |
| underdog|f6910e01-bfc1-4849-9d3d-899b8ee77c6f | underdog | Jahan Dotson | Receptions | under | 0.14404445231008522 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|aa7e1009-4548-4842-a8ff-64ad27e11221 | underdog | Ja'Kobi Lane | Receptions | under | 0.14398576918830674 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|3f7c2bd3-abfd-4725-b5db-fa8b6bd6aa55 | underdog | Devon Dampier | Pass Yards | under | 0.14368556374377595 | 2026-10-28T05:43:27Z | 2026-10-31T19:45:00Z |
| underdog|b7414544-5c15-4013-b6ae-37d6fb3cf0b6 | underdog | Antonio Williams | Receiving Yards | under | 0.14297460362734482 | 2026-10-29T05:46:21Z | 2026-11-02T01:20:00Z |
| underdog|b0d1d3de-f70f-4269-8112-3726934f8345 | underdog | Tucker Kraft | Receptions | under | 0.14139810535310193 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| prizepicks|16364222 | prizepicks | Stefon Diggs | Rec Targets | under | 0.14134166445347063 | 2026-10-29T05:46:21Z | 2026-11-01T20:20:00.000-05:00 |
| underdog|16e30719-f87f-4ad0-a848-6ec483ca90aa | underdog | Chuba Hubbard | Rush + Rec Yards | under | 0.141338144792028 | 2026-10-29T05:46:21Z | 2026-10-30T00:15:00Z |
| underdog|59da26a9-80c7-4a40-a23b-3757e949b385 | underdog | Jason Myers | FG Made | under | 0.14119220966516732 | 2026-10-27T05:05:06Z | 2026-11-03T01:15:00Z |
| underdog|58f2e2e3-3fa4-4c2a-a63e-0141b379bbe5 | underdog | Dylan Sampson | Receptions | under | 0.14093524678562463 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|994bbaea-5a64-4a42-9cfd-24b0ed8278bc | underdog | Denzel Boston | Receiving Yards | under | 0.13975537513182712 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|36ff0ba4-806f-4c4f-b71b-66f03d6e4721 | underdog | Zay Flowers | Receiving Yards | under | 0.1395259427543014 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|3ad48ee1-8d7d-466e-be99-e10ada3908a3 | underdog | Germie Bernard | Receptions | under | 0.1394253979904757 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|b2e7b5dc-0058-4dcb-ad3c-df98a1c058e3 | underdog | Malik Washington | Receiving Yards | under | 0.13931606450895906 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|4fced690-af5e-4f5d-8e5a-3f27d899311f | underdog | CJ Bailey | Pass TDs | under | 0.13906069575346958 | 2026-10-28T05:43:27Z | 2026-10-31T16:00:00Z |
| underdog|d45e52c5-341a-4f40-ad46-00461eb42b78 | underdog | Jake Elliott | Kicking Points | under | 0.13897742556141668 | 2026-10-29T05:46:21Z | 2026-11-02T01:20:00Z |
| underdog|b3e983ff-85d7-4d51-8ed3-8a2d17aa7262 | underdog | MarShawn Lloyd | Receptions | over | 0.13835587367388102 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| underdog|ede9d5df-0fd5-4851-8a4e-b9205aad6dc1 | underdog | Nolan Hauser | FG Made | over | 0.1382045276846529 | 2026-10-29T05:46:21Z | 2026-10-31T23:00:00Z |
| prizepicks|16364185 | prizepicks | Kyle Pitts Sr. | Rec Targets | under | 0.13793260511984728 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|16eae670-fe7a-45ef-95e5-9ba19c960b86 | underdog | Connor Calvert | FG Made | over | 0.13773351523629673 | 2026-10-29T05:46:21Z | 2026-10-31T19:45:00Z |
| underdog|6aafb4ed-173e-4c20-aa50-9b0737004ea2 | underdog | Mason Taylor | Receptions | under | 0.13759993099979895 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16364165 | prizepicks | A.J. Brown | Rec Targets | under | 0.13747852846435604 | 2026-10-29T05:46:21Z | 2026-11-01T16:25:00.000-05:00 |
| prizepicks|16364202 | prizepicks | Brock Bowers | Rec Targets | under | 0.13742860064955587 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|b1e35dcb-9dd0-40d5-b89e-624e1c04c652 | underdog | Tayven Jackson | Pass TDs | under | 0.1372770614864549 | 2026-10-28T05:43:27Z | 2026-10-29T23:30:00Z |
| underdog|889f8b63-e325-4aa4-b1b1-33d889f12100 | underdog | Chase Brown | Rush Yards | under | 0.13716921304829044 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|a62f7cce-1ae4-4dc6-a396-62b34f8117c1 | underdog | Ladd McConkey | Receptions | under | 0.13644727976504722 | 2026-10-29T05:46:21Z | 2026-11-01T21:05:00Z |
| underdog|3f9c4476-78f4-4ad8-95a2-5c8764a4d76e | underdog | Trevor Lawrence | Pass TDs | under | 0.136123979306918 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16364196 | prizepicks | Bhayshul Tuten | Rec Targets | under | 0.13598475807810717 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|99ccfe3c-2d1a-4a8b-aeb1-18afbb5f5154 | underdog | DK Metcalf | Receiving Yards | under | 0.13597344274054024 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|1a6cbb69-57e0-49bb-a5b1-c97ef13cb742 | underdog | Jonah Coleman | Rush Yards | under | 0.13593796227260369 | 2026-10-28T05:43:27Z | 2026-11-01T21:25:00Z |
| underdog|8e89428d-9bc2-417e-a764-081d96360e5c | underdog | Keyone Jenkins | Pass Yards | under | 0.13567122151918942 | 2026-10-29T05:46:21Z | 2026-10-30T23:30:00Z |
| underdog|af817726-c2ab-48c6-9400-8ea550264077 | underdog | Jayden Maiava | Pass Yards | under | 0.13504168109419978 | 2026-10-28T05:43:27Z | 2026-10-31T23:30:00Z |
| underdog|e7beb609-6a68-4956-9a67-99ef7eb2464f | underdog | Matthew Stafford | Pass Attempts | under | 0.1349833854689143 | 2026-10-29T05:46:21Z | 2026-11-01T21:05:00Z |
| underdog|30df1fbe-6d66-4007-b244-cea0fc5160f2 | underdog | Tyler Goodson | Rush + Rec Yards | under | 0.13481820413141865 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|aa19403b-6faa-472d-af3e-a642eb481c9c | underdog | Camden Coleman | Pass Yards | under | 0.13478287565803304 | 2026-10-29T05:46:21Z | 2026-10-29T23:30:00Z |
| underdog|4672a0de-a836-4b16-a6f6-0b21f98bd10e | underdog | Dawson Knox | Receiving Yards | under | 0.13474038768017405 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|b6b37aba-828b-4b2e-a2c1-ca8d4da057c8 | underdog | Wil Lutz | FG Made | under | 0.13416279453077506 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|1f8f23c6-88c6-4733-888c-ba2326bc988b | underdog | Chig Okonkwo | Receiving Yards | under | 0.13385829108769665 | 2026-10-29T05:46:21Z | 2026-11-02T01:20:00Z |
| underdog|4fafc90c-1967-429c-bde6-5442a20cdd77 | underdog | Christian Watson | Receptions | under | 0.13380819871657856 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| underdog|abe5bb36-eded-4179-8a4d-309e349e055f | underdog | Jordan Addison | Receptions | under | 0.1331259361407876 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16237758 | prizepicks | Kyren Williams | Rush Yards | under | 0.13309444803499015 | 2026-10-27T05:05:06Z | 2026-11-01T16:05:00.000-05:00 |
| prizepicks|16364167 | prizepicks | Hunter Henry | Rec Targets | under | 0.1324464875014063 | 2026-10-29T05:46:21Z | 2026-11-01T16:25:00.000-05:00 |
| underdog|5d9f5852-fc2e-417c-944a-8b2a3913277b | underdog | Breece Hall | Rush Yards | under | 0.1323005774569871 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|4c9eea8b-78fc-4981-96d9-686ced57e5f9 | underdog | Jordan Addison | Receiving Yards | under | 0.13128005851765068 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|73bf53dc-6bb2-45d1-8ca0-f2843567acf7 | underdog | Davis Allen | Receiving Yards | under | 0.1308943795657651 | 2026-10-29T05:46:21Z | 2026-11-01T21:05:00Z |
| underdog|44cb8b90-c1e9-4fc4-a57d-5fe54d0a842a | underdog | Drake Lindsey | Pass TDs | over | 0.13086097064389152 | 2026-10-29T05:46:21Z | 2026-10-31T19:30:00Z |
| underdog|d271bee3-dfd7-48f4-bdce-0cdea8ce8784 | underdog | Matthew Golden | Receiving Yards | under | 0.13021113286631225 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| underdog|551fc15e-7110-4b04-b038-3b949fc5f581 | underdog | Kanoah Vinesett | FG Made | over | 0.13014575003840156 | 2026-10-28T05:43:27Z | 2026-10-31T16:00:00Z |
| underdog|73ed8ff7-4427-4357-8826-42a9b682dd6b | underdog | Jonah Coleman | Rush + Rec Yards | under | 0.1295993717147006 | 2026-10-29T05:46:21Z | 2026-11-01T21:25:00Z |
| underdog|a0a1cd84-7140-4b79-94bb-c5dc8cffb254 | underdog | Cairo Santos | FG Made | under | 0.12940227002797755 | 2026-10-27T05:05:06Z | 2026-11-03T01:15:00Z |
| underdog|2adcc255-6e68-4788-bc5f-b4edfe5ca07a | underdog | Jonathan Taylor | Receptions | under | 0.1291779235770657 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|998c9e2f-447e-47e9-9a6f-9ded30f89aae | underdog | Justice Hill | Rush + Rec Yards | over | 0.12867881037577428 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|86bae6e8-dec3-4993-9b03-980cc9218653 | underdog | Jared Goff | Pass TDs | under | 0.12848407209017498 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|fb4ba9ce-ed53-41c1-8840-51f8498e1a55 | underdog | Ashton Jeanty | Rush + Rec Yards | under | 0.12826487466341152 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| prizepicks|16283725 | prizepicks | Jahmyr Gibbs | Rec Targets | under | 0.12770261716281617 | 2026-10-28T05:43:27Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|fede6610-0ae3-461a-a528-c9311a69e416 | underdog | Jakobi Meyers | Receiving Yards | under | 0.1270159615157731 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|3dc5fa2a-a302-4955-ab56-0d1ef1d65f9c | underdog | Jonathan Taylor | Rush Yards | under | 0.12612760876308726 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| prizepicks|16364208 | prizepicks | Greg Dulcich | Rec Targets | under | 0.1260559883327872 | 2026-10-29T05:46:21Z | 2026-11-01T16:25:00.000-05:00 |
| underdog|e0510146-16dc-4c71-a22c-6a1431b634c9 | underdog | Princely Umanmielen | Sacks | over | 0.1260307263481636 | 2026-10-29T05:46:21Z | 2026-10-30T00:15:00Z |
| underdog|c175aa40-b6a4-4b90-8ed1-993c3557c0d3 | underdog | Javonte Williams | Rush Yards | under | 0.12576473654626996 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|b295a429-a121-4509-9517-84f4b7c0a5b8 | underdog | Matthew Stafford | Pass TDs | under | 0.12550262949094826 | 2026-10-27T05:05:06Z | 2026-11-01T21:05:00Z |
| underdog|f70b7511-83e7-4d17-9f53-dadd50378e80 | underdog | JC French | Pass TDs | over | 0.1253467378686265 | 2026-10-29T05:46:21Z | 2026-10-31T19:45:00Z |
| underdog|0ee97bba-0118-41e3-a313-318a402ca03c | underdog | Tayven Jackson | Pass Yards | under | 0.12524863859868518 | 2026-10-27T05:05:06Z | 2026-10-29T23:30:00Z |
| underdog|f61c31f3-aeaa-4228-bd92-02cdb27ba725 | underdog | Easton Messer | Receiving Yards | under | 0.12454860215026164 | 2026-10-28T05:43:27Z | 2026-10-29T23:30:00Z |
| underdog|29c808a8-9d05-40c8-b849-a3377d6f2d93 | underdog | Jaylen Raynor | Pass Yards | under | 0.1244066748573942 | 2026-10-29T05:46:21Z | 2026-10-31T23:00:00Z |
| underdog|1a5870c8-2bf8-45e9-b218-a22be43cc0a0 | underdog | Deshaun Watson | Pass TDs | under | 0.12431385225063618 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|fd4864a0-5b0a-4779-8a28-6792f60fa96d | underdog | Denzel Boston | Receptions | under | 0.1242957023286192 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|cecaa735-d89c-4994-8c41-cbdc08e50000 | underdog | Jaron-Keawe Sagapolutele | Pass Yards | under | 0.12409056874769164 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| underdog|8cdb77cd-3925-4ee5-beb4-812a75583348 | underdog | Colby Parkinson | Receptions | under | 0.12334116882740842 | 2026-10-27T05:05:06Z | 2026-11-01T21:05:00Z |
| prizepicks|16364181 | prizepicks | Zay Flowers | Rec Targets | under | 0.12323292001142139 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|45ea7118-b8a7-4adb-90c6-d487299eacee | underdog | Carnell Tate | Receiving Yards | under | 0.12300903492048088 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|d76f6c73-df6d-480d-8ef1-5f4d9106de12 | underdog | Darnell Washington | Receptions | under | 0.12287634689571902 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|8814de67-b3fc-4dea-824c-84e1c36b6a07 | underdog | Jayden Daniels | Pass TDs | under | 0.12282845018311095 | 2026-10-29T05:46:21Z | 2026-11-02T01:20:00Z |
| underdog|2b7e72b5-e503-4272-8f85-2766fdb25eec | underdog | Bijan Robinson | Receptions | under | 0.12266143699231591 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|7c07455a-f277-48cd-ad69-7b2adac84d3e | underdog | Jake Bates | FG Made | under | 0.1226061500869009 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|1feb3eee-c29e-4b88-9571-6cdadadb7554 | underdog | Jordan Shipp | Receiving Yards | under | 0.12238215278329878 | 2026-10-29T05:46:21Z | 2026-10-31T23:30:00Z |
| underdog|cf3f87f9-0fe4-478d-b7bf-b213f8709c04 | underdog | James Cook | Rush + Rec Yards | under | 0.12131404815287872 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16364220 | prizepicks | Chris Godwin Jr. | Rec Targets | under | 0.12099460436306475 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|3d64f587-37b5-4075-b4ed-d119e585f6d7 | underdog | Nick Folk | Kicking Points | under | 0.12062606085130745 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|b60c1647-75fe-4f90-88a6-fbb03c468183 | underdog | Drake London | Receptions | under | 0.1204218989390401 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|1c819672-96ce-48b5-881b-75c45f1e0c6e | underdog | George Pickens | Receptions | under | 0.12005816443311146 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|176df220-cfc4-4a73-8aa3-da1b70016bd9 | underdog | Hank Brown | Pass Yards | under | 0.11986866627372694 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| underdog|1d457002-604b-429e-a411-f769176f22e3 | underdog | Mark Fletcher Jr. | Rush Yards | under | 0.11932651297467567 | 2026-10-28T05:43:27Z | 2026-10-31T23:30:00Z |
| underdog|a1bdb7e2-1c88-4f25-871e-3452559ed894 | underdog | Brevyn Spann-Ford | Receptions | under | 0.11929367596121321 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|3cb2102b-836e-4cca-af02-d3d30532f4dd | underdog | Blake Corum | Rush Yards | under | 0.11918877358070257 | 2026-10-27T05:05:06Z | 2026-11-01T21:05:00Z |
| underdog|66733f04-2f73-4846-9fee-a14dd49a87b5 | underdog | Malachi Toney | Receptions | under | 0.11891287925212268 | 2026-10-28T05:43:27Z | 2026-10-31T23:30:00Z |
| underdog|323eae11-630a-4d75-a6b3-71acae0b8fab | underdog | Trace Johnson | Pass Yards | under | 0.11838738758492195 | 2026-10-29T05:46:21Z | 2026-10-30T23:00:00Z |
| underdog|217bd354-9148-41f2-9cd5-c4bd95e6d92c | underdog | Rhamondre Stevenson | Rush + Rec Yards | under | 0.11826490624151575 | 2026-10-28T05:43:27Z | 2026-11-01T21:25:00Z |
| prizepicks|16364178 | prizepicks | Mark Andrews | Rec Targets | under | 0.1177866033639029 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| prizepicks|16356350 | prizepicks | Elsa Jacquemot | Break Points Won | under | 0.1177422964688647 | 2026-10-29T05:46:21Z | 2026-10-29T11:10:00.000-04:00 |
| underdog|84edf509-ff27-483d-b4f7-db4873957d66 | underdog | Lamar Jackson | Rush Yards | under | 0.11750214210193122 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|a8d65e72-cdf2-46c9-ad06-25735b026521 | underdog | Sam Darnold | Pass Attempts | under | 0.1167625142367642 | 2026-10-27T05:05:06Z | 2026-11-03T01:15:00Z |
| underdog|d71cdbfc-2e24-4347-8c79-b1148453d908 | underdog | Travis Kelce | Receptions | under | 0.11657078263704113 | 2026-10-29T05:46:21Z | 2026-11-01T21:25:00Z |
| underdog|04009dc7-d55c-42e0-8c30-cedd74969f69 | underdog | CJ Bailey | Pass Yards | under | 0.11567846584205332 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| underdog|808c6712-18ea-4550-9232-ecfae12e446a | underdog | Devon Dampier | Rush Yards | under | 0.11543354749603318 | 2026-10-29T05:46:21Z | 2026-10-31T19:45:00Z |
| underdog|cb84333c-b246-4493-acec-acedce99822c | underdog | Caleb Williams | Pass TDs | under | 0.11529745995363427 | 2026-10-27T05:05:06Z | 2026-11-03T01:15:00Z |
| underdog|40e1e8b9-936e-4e15-97c8-77ac12b78573 | underdog | Wil Lutz | Kicking Points | under | 0.11496311756471889 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|96102eeb-882d-48d6-bd89-01c3dc48fdc3 | underdog | Jayden Maiava | Pass TDs | over | 0.11429795145707633 | 2026-10-28T05:43:27Z | 2026-10-31T23:30:00Z |
| underdog|9307155f-3a4c-4ca6-828c-9545c446e309 | underdog | Deshaun Watson | Rush Yards | under | 0.11406987180102945 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|5d5e0ace-ca19-427d-b5ab-a6582a3c596b | underdog | Nolan James | Rush Yards | under | 0.11400689294997857 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| underdog|b7d6662c-6b16-43a0-9c59-996b95142c12 | underdog | Bo Nix | Pass TDs | under | 0.11391526566253873 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|625dacc0-9b5f-4a7d-b96b-7a162ccfaa00 | underdog | Arch Manning | Pass Yards | under | 0.11379889633880336 | 2026-10-29T05:46:21Z | 2026-10-31T23:30:00Z |
| underdog|83769162-c0c8-4c1c-b3cd-54e0c868c598 | underdog | Dylan Raiola | Pass Yards | under | 0.11327244617101795 | 2026-10-29T05:46:21Z | 2026-10-31T19:30:00Z |
| underdog|668a4a02-2699-4b23-a66f-b4d78c0ca876 | underdog | Nick Folk | FG Made | under | 0.11296010544794233 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|ff47be59-65fc-4501-a031-5f9897d4023d | underdog | Jason Myers | Kicking Points | under | 0.11198716898739403 | 2026-10-28T05:43:27Z | 2026-11-03T01:15:00Z |
| underdog|6f281cc7-2f96-40de-927a-51c9417310d3 | underdog | Trey Butkowski | FG Made | under | 0.11156540144260008 | 2026-10-29T05:46:21Z | 2026-10-31T16:30:00Z |
| underdog|39472ed8-bfcc-425b-a36b-4d7c794e141b | underdog | Byrum Brown | Pass TDs | over | 0.11110702198246591 | 2026-10-29T05:46:21Z | 2026-10-31T16:45:00Z |
| underdog|a76e2c22-fc99-4f26-b305-5156349b714d | underdog | Adonai Mitchell | Receiving Yards | under | 0.11108671220946464 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|d288a2db-0aab-4a8e-882a-4cd19ae79957 | underdog | Brendan Baird | FG Made | under | 0.11103855908681337 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| underdog|7e328141-5382-4550-b0dd-526277f19f6e | underdog | Antonio Chadha | FG Made | over | 0.10984663601068051 | 2026-10-29T05:46:21Z | 2026-10-31T23:30:00Z |
| underdog|5415d33b-e592-48da-9aa0-5ae5947a08a6 | underdog | Jonathan Taylor | Rush + Rec Yards | under | 0.10943203734227247 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|eb4c2d14-178e-431f-801d-2f408a5d44dd | underdog | Kenny Gainwell | Receptions | under | 0.1091654247547108 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|70a830b9-8d24-44e8-89db-49acb9f4a74c | underdog | Garrett Wilson | Receptions | under | 0.10773634557836387 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|3efdb3f2-4b15-4713-bf57-daa7e4d301a3 | underdog | Bucky Irving | Rush Yards | under | 0.10696383842535351 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|a747f734-6a7f-4f67-bb0d-b1f52a651910 | underdog | Kelby Valsin | Receiving Yards | under | 0.106590943504977 | 2026-10-29T05:46:21Z | 2026-10-29T23:30:00Z |
| underdog|b62f039b-0f9b-4cd6-9e9f-e9783c470857 | underdog | Ollie Gordon | Rush + Rec Yards | under | 0.10625843356924969 | 2026-10-28T05:43:27Z | 2026-11-01T21:25:00Z |
| underdog|182ee136-96d6-4d81-bfe6-e1a26c6e772f | underdog | Jahmyr Gibbs | Rush + Rec Yards | under | 0.10607821147759788 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|f05d8cc4-2b31-433f-8284-73733be5eae0 | underdog | Jordan Love | Rush Yards | under | 0.10597023269085659 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| underdog|d8e86dbd-b81c-4f69-a7ee-a5f68ef0926b | underdog | Travis Kelce | Receiving Yards | under | 0.10548155468571763 | 2026-10-29T05:46:21Z | 2026-11-01T21:25:00Z |
| underdog|3d1d6047-acac-47b2-a581-0b04d6d6af41 | underdog | Jahmyr Gibbs | Receiving Yards | under | 0.10531923406206589 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16238617 | prizepicks | Chig Okonkwo | Rec Yards | under | 0.1051404094349585 | 2026-10-27T05:05:06Z | 2026-11-01T20:20:00.000-05:00 |
| underdog|3f22f66a-41b9-480a-b6ab-5a45545197f6 | underdog | Pat Freiermuth | Receiving Yards | under | 0.10495785987094197 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|c50769bd-316a-45db-80cc-9539cf17da54 | underdog | Dohnte Meyers | Receptions | under | 0.10460151770038284 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|70c7a07b-fba3-43c1-83ba-7905926fef67 | underdog | Jayden Mandal | Pass Yards | under | 0.10433928305204221 | 2026-10-29T05:46:21Z | 2026-11-01T03:00:00Z |
| underdog|9c49082a-6082-48bd-a624-5fb9a4843e9d | underdog | Bhayshul Tuten | Receptions | under | 0.10402814965460072 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|c4a26ee5-46ee-4137-bd0d-213f8b9d258c | underdog | Jaden Craig | Pass Yards | under | 0.10380649740717707 | 2026-10-29T05:46:21Z | 2026-10-31T19:30:00Z |
| underdog|b99e96ea-5ec2-4c4e-a95e-abcf30e876f2 | underdog | Quinshon Judkins | Rush Yards | under | 0.1037066913938336 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|9f0f4774-c8ae-4fca-86b3-7e8949f6bded | underdog | Kirk Cousins | Rush Yards | over | 0.10334335183039561 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|7ca72607-5f5c-45be-becf-726a9827d1f1 | underdog | Ethan Moczulski | FG Made | over | 0.10328978596060573 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| underdog|35b2d5a2-c766-4bbf-bed6-1c678f5cead2 | underdog | Mark Andrews | Receptions | under | 0.10321357999549285 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|137e2104-c54e-41e9-800b-00dd98ceacaf | underdog | Elic Ayomanor | Receptions | under | 0.10297226753174415 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|59905fd2-4d5c-4646-a528-93b6094e86bb | underdog | Jaxon Smith-Njigba | Receptions | under | 0.10234847580734763 | 2026-10-27T05:05:06Z | 2026-11-03T01:15:00Z |
| underdog|6a8df612-85c8-48c6-9495-ad384554b4e5 | underdog | Rece Verhoff | FG Made | under | 0.10231534646673801 | 2026-10-29T05:46:21Z | 2026-10-31T23:30:00Z |
| underdog|fb0ebb52-5cd0-446a-a730-0d6d78e89d20 | underdog | Chuba Hubbard | Rush Yards | under | 0.10227682296643859 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| underdog|69633668-600e-45d5-9f40-8c2dc88d92a7 | underdog | Greg Dulcich | Receptions | under | 0.10220882757054206 | 2026-10-29T05:46:21Z | 2026-11-01T21:25:00Z |
| underdog|307e4ebb-a536-41e7-84dc-c9d2dae5a149 | underdog | Tershawn Wharton | Sacks | under | 0.10198675496688747 | 2026-10-29T05:46:21Z | 2026-10-30T00:15:00Z |
| underdog|74e6cac7-eab2-4c02-822a-1566aa9f481d | underdog | Christian Watson | Receiving Yards | under | 0.10161071542179834 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| prizepicks|16344699 | prizepicks | Connor Heyward | Rush+Rec Yds | over | 0.10154012747091701 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|dba955cf-89ee-43b5-ad32-57eccdde7426 | underdog | Rome Odunze | Receiving Yards | under | 0.10135838550360621 | 2026-10-28T05:43:27Z | 2026-11-03T01:15:00Z |
| underdog|7f3a1555-2591-4add-a3c4-6eb0e5bc4c64 | underdog | Tony Pollard | Rush + Rec Yards | under | 0.10091140694516076 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|a4f90109-232f-4dd5-83b1-359e0555887e | underdog | Bear Bachmeier | Pass Yards | under | 0.10074287452487363 | 2026-10-29T05:46:21Z | 2026-10-31T19:30:00Z |
| underdog|8b4746c7-cb72-4ecb-a00e-935e7143b817 | underdog | Rico Dowdle | Rush + Rec Yards | under | 0.09981514620881438 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|c2a40e0b-c299-4609-bb2a-f82e0e98ec53 | underdog | Kendrick Raphael | Rush Yards | under | 0.09978120029490634 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| underdog|14105848-15ac-4b84-9d6b-a582cb9a5177 | underdog | Gavin Freeman | Receiving Yards | under | 0.09971948564649324 | 2026-10-29T05:46:21Z | 2026-10-30T23:30:00Z |
| prizepicks|16364206 | prizepicks | Caleb Douglas | Rec Targets | under | 0.0996362260043121 | 2026-10-29T05:46:21Z | 2026-11-01T16:25:00.000-05:00 |
| underdog|f7f80b3b-52f5-4cdd-8a54-58bda6446c0a | underdog | Tait Reynolds | Pass Yards | under | 0.09947450960567161 | 2026-10-29T05:46:21Z | 2026-10-31T23:00:00Z |
| underdog|bf1470be-563b-42d9-8a74-2acc5a6ec09e | underdog | Wan'Dale Robinson | Receptions | under | 0.09927862778998076 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|d6d8f19d-e78e-4df1-8240-469070b06ea3 | underdog | Emeka Egbuka | Receptions | under | 0.09907031765655117 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| prizepicks|16249073 | prizepicks | Jesse Legree | Recs | under | 0.09819846081803829 | 2026-10-28T05:43:27Z | 2026-10-31T23:00:00.000-04:00 |
| underdog|cda2850a-e231-4018-83e6-6ca64bd5eda6 | underdog | Will Hammond | Pass Yards | under | 0.09744969932113756 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| underdog|2e0a010a-70b8-4d0d-a210-17287ae2730c | underdog | Ryan Fitzgerald | FG Made | under | 0.09744756346959127 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| prizepicks|16364209 | prizepicks | Malik Washington | Rec Targets | under | 0.09706503307304815 | 2026-10-29T05:46:21Z | 2026-11-01T16:25:00.000-05:00 |
| underdog|9e1d3567-3f8f-4d49-b463-e39fb8dfe8eb | underdog | Harrison Butker | FG Made | under | 0.09638494838462963 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|0ae2b107-e8a1-4f19-9af0-6abe299e4671 | underdog | CeeDee Lamb | Receiving Yards | under | 0.09554776768839468 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| prizepicks|16239374 | prizepicks | Christian Watson | Rec Targets | under | 0.09551948790177134 | 2026-10-27T05:05:06Z | 2026-10-29T20:15:00.000-04:00 |
| underdog|5998434f-948d-4ce6-a07a-c8ea7f5d1c65 | underdog | Jaylen Warren | Receiving Yards | over | 0.09533361799515139 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16364223 | prizepicks | Chig Okonkwo | Rec Targets | under | 0.09483291694542273 | 2026-10-29T05:46:21Z | 2026-11-01T20:20:00.000-05:00 |
| underdog|e10b87ae-c6a6-4551-bb87-d585e77e9965 | underdog | Brian Thomas | Receptions | over | 0.09404550627475516 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|fec089b1-2003-40c0-a50f-ebdc1a159192 | underdog | Trey Smack | FG Made | under | 0.09392813482019169 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| underdog|72447f28-a5ca-42bb-9be7-031e0f4620c2 | underdog | Joe McFadden | FG Made | under | 0.09390907363785272 | 2026-10-29T05:46:21Z | 2026-10-31T20:15:00Z |
| underdog|d17ab225-e529-4428-a9aa-ea656ecb35e5 | underdog | Tyler Robles | XP Made | over | 0.0937394398844259 | 2026-10-29T05:46:21Z | 2026-11-01T00:00:00Z |
| underdog|6207f1a3-38b0-4a82-bcbc-e8c63e0a7181 | underdog | TreVeyon Henderson | Receiving Yards | over | 0.09364324694734338 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|a7c11a4c-519b-4ffe-8595-86ffd84f2d9d | underdog | TreVeyon Henderson | Receptions | under | 0.09305154250073311 | 2026-10-29T05:46:21Z | 2026-11-01T21:25:00Z |
| underdog|f01c3c7e-ab04-46c4-8870-7691054b1337 | underdog | Tony Pollard | Receptions | under | 0.09290599399982635 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|4e50ec4a-dc6c-4856-a0b5-b6d28d2cfee4 | underdog | Jakobi Meyers | Receptions | under | 0.09288375907862756 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|b22a6f88-4281-4cb7-9112-901cbb528b99 | underdog | Will Bettridge | FG Made | under | 0.0928484830083991 | 2026-10-29T05:46:21Z | 2026-10-31T19:45:00Z |
| underdog|b9fd522c-e790-46b8-b35b-88e54e06e1ed | underdog | Hunter Henry | Receiving Yards | under | 0.09271224325362548 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|61a5de04-06b8-46e3-8ae4-8af1690f6227 | underdog | Will Stone | FG Made | under | 0.09268440319370341 | 2026-10-28T05:43:27Z | 2026-10-30T23:30:00Z |
| underdog|7ee62abb-426d-40f5-8049-83803048de15 | underdog | Malik Washington | Pass Yards | under | 0.09203228079816017 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| underdog|ed29d33f-b4cd-4c85-95e3-61ba3606a315 | underdog | Darian Mensah | Pass Yards | under | 0.0918747633899134 | 2026-10-28T05:43:27Z | 2026-10-31T23:30:00Z |
| underdog|32141e2b-baf9-4032-b5f0-32fc2265c1c3 | underdog | Noah Jennings | Receiving Yards | over | 0.09180485638454461 | 2026-10-29T05:46:21Z | 2026-10-31T19:30:00Z |
| underdog|d8053318-9e77-41f4-a87c-da664ca47279 | underdog | James Cook | Rush Yards | under | 0.09180295647498382 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16364191 | prizepicks | KC Concepcion Jr. | Rec Targets | under | 0.09171087847629222 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| prizepicks|16352536 | prizepicks | Ashton Daniels | Pass Attempts | under | 0.09138425718851007 | 2026-10-29T05:46:21Z | 2026-10-31T19:00:00.000-04:00 |
| underdog|77dc371f-f1e2-4307-9353-a2e180a8cf09 | underdog | Chris Rodriguez | Rush Yards | under | 0.09130943359892696 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|9cdd3d69-694a-432f-a2ba-c1111c92e710 | underdog | Jaron-Keawe Sagapolutele | Pass TDs | under | 0.09126593974479602 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| underdog|ef0f3c3c-48ff-482a-a3bf-4e4a444d4d0c | underdog | Jauan Jennings | Receptions | under | 0.09119904435326343 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16346147 | prizepicks | Carnell Tate | Rec Targets | under | 0.09109040404588509 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|177547b5-94a6-4d78-91a9-2199205a3905 | underdog | Khalil Shakir | Receiving Yards | under | 0.0909398055872559 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|489a27f6-b223-4f4e-ac5a-5842df306940 | underdog | Tyler Goodson | Rush Yards | under | 0.09036048124885299 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|412561be-c077-41b5-ad1f-cbccfa5800d2 | underdog | Jaylen Warren | Receptions | under | 0.09013968720518872 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| prizepicks|16300984 | prizepicks | Rome Odunze | Rec Targets | under | 0.09000083847025231 | 2026-10-28T05:43:27Z | 2026-11-02T20:15:00.000-05:00 |
| prizepicks|16238614 | prizepicks | Hunter Henry | Rec Yards | under | 0.08957307565733919 | 2026-10-27T05:05:06Z | 2026-11-01T16:25:00.000-05:00 |
| underdog|c0199a09-88d6-41bd-a286-a771e0428d9e | underdog | Luther Burden | Receiving Yards | under | 0.0891800401053029 | 2026-10-28T05:43:27Z | 2026-11-03T01:15:00Z |
| prizepicks|16359229 | prizepicks | Nikoloz Basilashvili | Total Games Won | over | 0.08890515101509322 | 2026-10-29T05:46:21Z | 2026-10-29T10:00:00.000-04:00 |
| prizepicks|16364224 | prizepicks | Antonio Williams | Rec Targets | under | 0.08846930883267912 | 2026-10-29T05:46:21Z | 2026-11-01T20:20:00.000-05:00 |
| prizepicks|16284250 | prizepicks | Jordan Addison | Rec Targets | under | 0.08846730165489147 | 2026-10-28T05:43:27Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|6f702c4c-bbe6-4860-9e9a-c16763e05176 | underdog | Conner Harrell | Pass TDs | under | 0.08834589756249811 | 2026-10-28T05:43:27Z | 2026-10-30T23:00:00Z |
| underdog|5f8f9fef-84e9-4582-9531-d0607f093d8a | underdog | Hank Brown | Pass TDs | over | 0.0882542333800242 | 2026-10-28T05:43:27Z | 2026-10-31T16:00:00Z |
| underdog|1a5a77f7-5e58-4569-b1aa-e89210132a70 | underdog | Jaden Craig | Pass TDs | under | 0.08817863679532056 | 2026-10-28T05:43:27Z | 2026-10-31T19:30:00Z |
| underdog|697d7786-7f45-4254-8c64-d850b87cba4c | underdog | Bo Jackson | Receiving Yards | over | 0.08807852290116602 | 2026-10-29T05:46:21Z | 2026-10-31T23:30:00Z |
| underdog|b9df65cc-b761-4559-a23d-251a85407bdc | underdog | Kendrick Bourne | Receiving Yards | under | 0.08801198338315153 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|89bf8626-6b97-4a03-a269-6d447eed5ea7 | underdog | Pat Freiermuth | Receptions | under | 0.08793132623164612 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|a4696dcd-4c5a-45b4-9974-3e154a5bd04e | underdog | Gabe Panikowski | XP Made | over | 0.08767909829509757 | 2026-10-29T05:46:21Z | 2026-10-31T23:00:00Z |
| underdog|9368aed3-4724-4cf4-b2b2-be4450c012a0 | underdog | Justice Hill | Receptions | under | 0.08757492719763116 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|6dc9b6cd-551f-440e-b4e5-d65b9b82b9ef | underdog | Kevin Jennings | Pass TDs | under | 0.08721499825054435 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| underdog|dddbc903-2c87-42d2-bf02-333cee694469 | underdog | Jason Sanders | FG Made | under | 0.08716403013921992 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16364213 | prizepicks | Omar Cooper Jr. | Rec Targets | under | 0.08710714459591429 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|fc5f4b6d-edab-410c-81af-051ab6bbca0e | underdog | Tetairoa McMillan | Receiving Yards | under | 0.08692804723586145 | 2026-10-29T05:46:21Z | 2026-10-30T00:15:00Z |
| prizepicks|16303204 | prizepicks | Ben Shelton | Total Games | over | 0.08688440176281631 | 2026-10-28T05:43:27Z | 2026-10-29T06:00:00.000-04:00 |
| underdog|f2c69c86-fa80-4b67-a398-58825285244c | underdog | Jake Ferguson | Receptions | under | 0.08623693827268275 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|cc091e15-6bc3-40aa-a886-17453738b517 | underdog | Sean O'Haire | FG Made | over | 0.08607263612268956 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| underdog|c094618b-d9f7-4fdf-806e-add690a369a1 | underdog | DeMario Douglas | Receptions | under | 0.08587440528378754 | 2026-10-29T05:46:21Z | 2026-11-01T21:25:00Z |
| prizepicks|16352571 | prizepicks | Kaitlin Quevedo | Break Points Won | under | 0.08560279853429065 | 2026-10-29T05:46:21Z | 2026-10-29T03:20:00.000-04:00 |
| underdog|a57bf8a6-36db-4e69-be1f-971f6a09a619 | underdog | Caleb Douglas | Receptions | under | 0.08550150897075826 | 2026-10-29T05:46:21Z | 2026-11-01T21:25:00Z |
| underdog|f7cfb2f5-b40a-475d-aa7c-b739f17e78f0 | underdog | MarShawn Lloyd | Rush Yards | under | 0.08542377705184623 | 2026-10-29T05:46:21Z | 2026-10-30T00:15:00Z |
| prizepicks|16364200 | prizepicks | Travis Kelce | Rec Targets | under | 0.08541097265923969 | 2026-10-29T05:46:21Z | 2026-11-01T16:25:00.000-05:00 |
| underdog|ce0094b8-608a-4f57-8db8-91acfa4ebf67 | underdog | D'Andre Swift | Receptions | under | 0.08536310216644005 | 2026-10-29T05:46:21Z | 2026-11-03T01:15:00Z |
| underdog|00fa635b-a085-487f-969e-9364f8522ac4 | underdog | Andre Szmyt | FG Made | under | 0.08496316251445146 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16244713 | prizepicks | Caden Veltkamp | Pass Attempts | under | 0.08431255828497985 | 2026-10-29T05:46:21Z | 2026-10-29T19:30:00.000-04:00 |
| underdog|0247c7be-a564-4aa3-a694-6199240b618c | underdog | Hunter Henry | Receptions | under | 0.08384245014413438 | 2026-10-29T05:46:21Z | 2026-11-01T21:25:00Z |
| prizepicks|16364170 | prizepicks | DJ Moore | Rec Targets | under | 0.0836818295883065 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|edc65d80-633a-49d5-b568-467b9dc26c82 | underdog | Chris Rodriguez | Rush + Rec Yards | under | 0.08351399754029376 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|1de4b590-c9a8-4590-ada7-552bf50550c5 | underdog | Ollie Gordon | Rush Yards | under | 0.08331726721322741 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|329814f9-a9e2-4cca-97a5-37a6a9d98a3d | underdog | Greg Dulcich | Receiving Yards | under | 0.08331303954427971 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|9bf96da1-b640-416c-9d74-efbdc0a699f1 | underdog | Byrum Brown | Pass Yards | under | 0.08325122002724061 | 2026-10-29T05:46:21Z | 2026-10-31T16:45:00Z |
| underdog|cc8cfbb1-e058-4e01-aaa4-4a08f7cd9394 | underdog | Aaron Rodgers | Rush Yards | over | 0.08323621946349369 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|16ee5833-fd42-4e71-b971-e39932752a8b | underdog | TreVeyon Henderson | Rush Yards | under | 0.08316140798485938 | 2026-10-29T05:46:21Z | 2026-11-01T21:25:00Z |
| underdog|c124caa4-7f08-4fa3-b0a7-647244cf531a | underdog | Harrison Butker | Kicking Points | under | 0.08302378472777494 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|390c24f1-9c5b-46f7-a624-c955bdc8a4ea | underdog | Michael Salgado-Medina | FG Made | under | 0.08238079086671868 | 2026-10-28T05:43:27Z | 2026-10-31T16:00:00Z |
| prizepicks|16237753 | prizepicks | Derrick Henry | Rush Yards | under | 0.08183379413197434 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|e3f2d3d4-40fc-41c4-a46f-fb13d7c0b757 | underdog | Geno Smith | Pass TDs | under | 0.0817951993038919 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|c4834b91-d688-4ab8-8927-69031c8efbc4 | underdog | Deuce Alexander | Receiving Yards | under | 0.08169099115486911 | 2026-10-29T05:46:21Z | 2026-10-31T16:45:00Z |
| prizepicks|16237756 | prizepicks | Ashton Jeanty | Rush Yards | under | 0.0816051738093021 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|ce1fe404-32bc-42d9-9b49-cab4bf747245 | underdog | Daniel Jones | Rush Yards | under | 0.08156509285685742 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16316043 | prizepicks | Jonnu Smith | Rec Yards | over | 0.08121651832595789 | 2026-10-28T05:43:27Z | 2026-10-29T20:15:00.000-04:00 |
| underdog|06d12339-a07f-421f-9db1-b57631721f57 | underdog | Noah Fifita | Pass TDs | over | 0.0809828208650083 | 2026-10-28T05:43:27Z | 2026-10-31T16:00:00Z |
| underdog|68246aad-20fd-405d-80db-3ad12ff7a40b | underdog | Kenyon Sadiq | Receptions | under | 0.0809538714276471 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|7b607118-d03a-475d-958d-71068c7dc831 | underdog | Trech Kekahuna | Receiving Yards | over | 0.08084359976015487 | 2026-10-28T05:43:27Z | 2026-10-31T23:30:00Z |
| underdog|2779b258-103f-4447-bbd2-4e32de9a6119 | underdog | Kyler Murray | Rush Yards | under | 0.0807146302213625 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|ad7f9e03-363a-4d30-9b4d-da66aee9eab6 | underdog | Josiah Freeman | Receiving Yards | under | 0.08070091626777509 | 2026-10-29T05:46:21Z | 2026-11-01T03:00:00Z |
| underdog|87384d05-6b0b-41cc-be57-65b4a4195a0c | underdog | Chris Boswell | FG Made | under | 0.08060150764940355 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|e5acb1c5-949b-4989-9bbb-0e9edeafa8f1 | underdog | Breece Hall | Receptions | under | 0.08027698920910142 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|6b123853-c961-42ef-bda8-debbf697b3a7 | underdog | Ty Dieffenbach | Pass Yards | under | 0.08024476905845901 | 2026-10-29T05:46:21Z | 2026-10-31T20:15:00Z |
| underdog|af47f3d7-7a13-4d4c-a07e-e37440eb8e97 | underdog | Jauan Jennings | Receiving Yards | under | 0.0801424432343455 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16364215 | prizepicks | Mason Taylor | Rec Targets | under | 0.08004599703900439 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|05eeccf3-c4fb-4520-9da6-a45b915f96a1 | underdog | Joey Slye | Kicking Points | under | 0.07982974801643872 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|dfac3d0b-440d-455f-9db9-be3be785ebbc | underdog | Daniel Bellinger | Receptions | under | 0.07970721189223906 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|17c26024-188c-4c83-b07f-02d0bbe0431a | underdog | Ryan Fitzgerald | Kicking Points | under | 0.07963366790517856 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| underdog|ebfdac74-66b1-4b80-8af0-a406ffc1ad26 | underdog | Dohnte Meyers | Receiving Yards | under | 0.07961527812463143 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|a5e8c666-ecef-4176-8b5a-c79039669f0d | underdog | Patrick Mahomes | Rush Yards | under | 0.07958627648203864 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|e1246340-c9ea-4250-920c-2e90410c9b6b | underdog | Noah Jennings | Receptions | over | 0.07941850478767742 | 2026-10-29T05:46:21Z | 2026-10-31T19:30:00Z |
| underdog|e2692ca9-45cb-4e9d-ae48-bd8f36e8f770 | underdog | Kenneth Walker III | Receiving Yards | under | 0.07925791496494905 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| prizepicks|16364218 | prizepicks | Germie Bernard | Rec Targets | under | 0.07924997261919642 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|97184200-5077-4667-bd97-4bf6317675c2 | underdog | Isaac TeSlaa | Receptions | under | 0.07907295172171624 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|29a57594-563b-446e-b1a8-c3d405a95378 | underdog | Sam Darnold | Pass TDs | under | 0.07875391297959822 | 2026-10-27T05:05:06Z | 2026-11-03T01:15:00Z |
| underdog|e9b8475b-f2fe-46f7-8e1c-42d4ee8076e4 | underdog | Devontez Walker | Receiving Yards | over | 0.0786942765304709 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| prizepicks|16364174 | prizepicks | Khalil Shakir | Rec Targets | under | 0.07852934480886664 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|3ca2a506-1290-4bed-9008-049dd17e2606 | underdog | Tyler Higbee | Receiving Yards | under | 0.07847610122114035 | 2026-10-28T05:43:27Z | 2026-11-01T21:05:00Z |
| underdog|e451e337-fb60-4fc0-8043-f8588253f0d2 | underdog | Adonai Mitchell | Receptions | under | 0.07829765351425 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|39d45cc3-0cd1-4b04-9cb8-ba760403ada6 | underdog | Yulia Putintseva | Double Faults | over | 0.07794362704670621 | 2026-10-29T05:46:21Z | 2026-10-29T08:00:00Z |
| underdog|ca7df8ab-fd4d-44e9-af34-84af2eb3f8f4 | underdog | Aidan Chiles | Pass TDs | over | 0.07771892927940771 | 2026-10-29T05:46:21Z | 2026-10-31T19:30:00Z |
| underdog|29a958df-a2b1-41e5-9344-22b37cb26cb1 | underdog | Mason Taylor | Receiving Yards | under | 0.07765735031426335 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16364195 | prizepicks | Tyler Warren | Rec Targets | under | 0.07762055921491584 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|b18a1790-47a1-4ae1-9f32-50eff0e7df43 | underdog | Tony Pollard | Rush Yards | under | 0.07758154832244912 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|d1d78185-1dc9-4c46-acca-78125906daae | underdog | Trevor Lawrence | Rush Yards | under | 0.07734924110519159 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|3c514266-18c3-470f-84b1-da3e8396317d | underdog | Sam LaPorta | Receptions | under | 0.07679022400127311 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|a2fa5306-9f14-4039-be86-f7477e7048c8 | underdog | Kyren Williams | Rush + Rec Yards | under | 0.07664715400572031 | 2026-10-29T05:46:21Z | 2026-11-01T21:05:00Z |
| underdog|f86416a6-4bb5-437a-8801-cb5cb0c98823 | underdog | Theo Melin Ohrstrom | Receiving Yards | over | 0.0766365795758529 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| underdog|1219f959-0903-4377-a0bc-a328a24db1b9 | underdog | Arch Manning | Pass TDs | under | 0.07609166857256278 | 2026-10-29T05:46:21Z | 2026-10-31T23:30:00Z |
| underdog|0ebcf308-a8de-44ee-97cc-b2c9a347875b | underdog | Drake London | Receiving Yards | under | 0.07608032624515215 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|68e22951-6601-471d-a12e-fbaea9277356 | underdog | Rashod Bateman | Receiving Yards | under | 0.07606275380805294 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|86034be6-d3b2-4841-b0a3-7cadb61884fc | underdog | D'Andre Swift | Receiving Yards | under | 0.07598977212251534 | 2026-10-29T05:46:21Z | 2026-11-03T01:15:00Z |
| underdog|ab4c4291-4fa3-4224-8f91-f1a8fb579e07 | underdog | J.K. Dobbins | Receptions | under | 0.07588074058074556 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|a471fcf1-a2a9-4bc8-95ee-33ca13fe3d7d | underdog | Jason Sanders | Kicking Points | under | 0.07535210830958228 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|447ef2be-9aed-498c-b0c9-a847a6c755d8 | underdog | Michael Mayer | Receiving Yards | under | 0.07524277884476527 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|a01ec37f-65ba-4176-afa3-c518f1b0c6e6 | underdog | Spencer Shrader | FG Made | over | 0.07516924076136433 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16238615 | prizepicks | Travis Kelce | Rec Yards | under | 0.07491212238443534 | 2026-10-27T05:05:06Z | 2026-11-01T16:25:00.000-05:00 |
| underdog|643ee736-d3da-4ff9-9257-7e6362eb9b8c | underdog | Keyone Jenkins | Pass TDs | over | 0.07442111817748337 | 2026-10-29T05:46:21Z | 2026-10-30T23:30:00Z |
| underdog|fda16c4d-dd48-4c72-a947-2a99435c8fb1 | underdog | Ahmad Miller | Rush Yards | under | 0.07428768813807607 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| underdog|d66a9fd2-3ad4-49d8-b430-b68d20eb4789 | underdog | Treylon Burks | Receptions | under | 0.07415346242378762 | 2026-10-29T05:46:21Z | 2026-11-02T01:20:00Z |
| underdog|163c74c6-8f61-492e-8f3e-2912f391c5dd | underdog | Devon Dampier | Pass TDs | over | 0.07411677035665121 | 2026-10-28T05:43:27Z | 2026-10-31T19:45:00Z |
| underdog|07d82f2e-a2b5-4970-ac35-068da04923d4 | underdog | LaNorris Sellers | Pass TDs | under | 0.07405136015775549 | 2026-10-29T05:46:21Z | 2026-10-31T20:15:00Z |
| underdog|c1b8e741-c488-4ec2-ba8a-ade9f6427194 | underdog | Trey Butkowski | XP Made | under | 0.07393229451427985 | 2026-10-27T05:05:06Z | 2026-10-31T16:30:00Z |
| underdog|93ae2a44-e3eb-4055-8da9-44a422173f58 | underdog | Ashton Daniels | Pass TDs | over | 0.07381214411367737 | 2026-10-29T05:46:21Z | 2026-10-31T23:00:00Z |
| underdog|f1e7b9c6-fe0f-4cff-82bb-7ded830f76bf | underdog | Darian Mensah | Pass TDs | under | 0.07373742700667696 | 2026-10-28T05:43:27Z | 2026-10-31T23:30:00Z |
| underdog|e5048c4a-9b13-45e4-a29f-056f8bfddf4d | underdog | Jonnu Smith | Receptions | over | 0.07367696912264177 | 2026-10-29T05:46:21Z | 2026-10-30T00:15:00Z |
| underdog|ce6e4bca-e4dd-4f39-a2d2-f5726f2e0057 | underdog | KC Concepcion | Receptions | under | 0.07353629953328678 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|e7ecbdd2-92b1-40d0-a848-792abd490475 | underdog | Kanoah Vinesett | XP Made | under | 0.07341237547890234 | 2026-10-28T05:43:27Z | 2026-10-31T16:00:00Z |
| underdog|902cbe97-9332-4c6a-a902-03593cb46651 | underdog | Rico Dowdle | Receptions | under | 0.07313092583642589 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|e435f6f0-ffa3-490c-b17d-c06d52fc20f9 | underdog | Samaje Perine | Rush Yards | under | 0.07258371600193658 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|c3f6dbbe-f79d-4e3d-adc2-755392988b2a | underdog | Drake Maye | Pass TDs | under | 0.07237975805283348 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|ce99f8b4-299c-4c0e-bbdd-253733297a38 | underdog | Davis Allen | Receptions | under | 0.07229700088471258 | 2026-10-29T05:46:21Z | 2026-11-01T21:05:00Z |
| underdog|32df8b3a-895a-4c2f-a465-59901c55ce98 | underdog | Malachi Toney | Receiving Yards | under | 0.07228214793009535 | 2026-10-29T05:46:21Z | 2026-10-31T23:30:00Z |
| underdog|e70899ec-2d6f-45a9-ba4c-3bd042d99cd0 | underdog | Harold Fannin | Receptions | under | 0.07210251211434926 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|0d036f46-6344-47bb-b2fa-bb6fd25e685f | underdog | Spencer Porath | FG Made | over | 0.07189003660273241 | 2026-10-28T05:43:27Z | 2026-10-31T16:00:00Z |
| underdog|127149bb-3491-47d8-a424-a412b2859785 | underdog | Blake Corum | Rush + Rec Yards | under | 0.0718580976652794 | 2026-10-27T05:05:06Z | 2026-11-01T21:05:00Z |
| underdog|45b2cebd-3957-48e7-8e14-9609e517784f | underdog | J.K. Dobbins | Receiving Yards | over | 0.07179068462409405 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|cf85c65e-45c3-4d84-b8cc-3cd5505c494f | underdog | Rayshon Luke | Receiving Yards | over | 0.07176712569482835 | 2026-10-29T05:46:21Z | 2026-11-01T03:00:00Z |
| underdog|c46b5924-22eb-404f-aaa1-b518e6d87289 | underdog | Dylan Sampson | Receiving Yards | under | 0.07158252096444151 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16265143 | prizepicks | Jonathan Taylor | Rush TDs | over | 0.07100695487408926 | 2026-10-28T05:43:27Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|347e949c-aed0-4263-80b1-bf253386ea34 | underdog | Ashton Jeanty | Rush Yards | under | 0.07098329396922187 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|aa32bf3e-4612-4433-960c-77abf50aeff0 | underdog | Brenton Strange | Receiving Yards | under | 0.07082871978056027 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|9eb907ba-1f51-4385-a30b-efb9c1576b37 | underdog | Chase McLaughlin | FG Made | under | 0.0707192810705145 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|510c8b69-a281-4f57-a69c-06edc72e891f | underdog | Cardae Mack | Rush Yards | under | 0.07006477470331085 | 2026-10-29T05:46:21Z | 2026-10-31T19:30:00Z |
| underdog|38c65ada-bd72-4a24-bba7-9cc1ccafd67f | underdog | Darnell Washington | Receiving Yards | under | 0.07003063145156818 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|a28a3a92-e695-4545-be4d-7f20f3c2cf85 | underdog | Dalton Kincaid | Receptions | under | 0.07001654956510595 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|dd1a8b64-c7cb-4bf4-a2b1-e409957fec6d | underdog | KC Concepcion | Receiving Yards | under | 0.06928901838504875 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|3b318665-3682-405c-b032-b679ee889d2a | underdog | Davis Warren | Pass TDs | over | 0.06901083848131273 | 2026-10-29T05:46:21Z | 2026-10-31T19:15:00Z |
| underdog|bab2e456-d14b-4bcb-967b-e23f2075580c | underdog | JC French | Rush Yards | over | 0.06883016771534489 | 2026-10-28T05:43:27Z | 2026-10-31T19:45:00Z |
| underdog|92c45e5f-3130-4b0e-afaa-ac9694c178e7 | underdog | Ty Dieffenbach | Pass TDs | under | 0.06870975528808276 | 2026-10-29T05:46:21Z | 2026-10-31T20:15:00Z |
| underdog|da8f6301-afcc-437d-9f60-dc3304fbdbe6 | underdog | Justin Herbert | Rush Yards | under | 0.06867310853633335 | 2026-10-29T05:46:21Z | 2026-11-01T21:05:00Z |
| underdog|587f36a1-5642-4bb1-bead-2c3473fa6ea6 | underdog | Mateen Bhaghani | XP Made | under | 0.06819342215573876 | 2026-10-29T05:46:21Z | 2026-10-31T20:15:00Z |
| prizepicks|16284249 | prizepicks | T.J. Hockenson | Rec Targets | under | 0.06775761944636594 | 2026-10-28T05:43:27Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|9493e7e9-c152-47ef-87d7-61177aa97a8a | underdog | J'Koby Williams | Receiving Yards | over | 0.06766110762216271 | 2026-10-28T05:43:27Z | 2026-10-31T16:00:00Z |
| underdog|81caa087-4032-4f09-9276-eb7bc36d98b0 | underdog | Omar Cooper | Receiving Yards | under | 0.0664932335028362 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|929bd902-5f8f-4e6b-8e6b-cbc968bb5973 | underdog | Kenneth Walker III | Rush Yards | under | 0.06618140649978566 | 2026-10-29T05:46:21Z | 2026-11-01T21:25:00Z |
| underdog|986fa224-9b7f-4eb5-86dd-0cef3ced7364 | underdog | Michael Mayer | Receptions | under | 0.0659709433914546 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|d9748f27-33c1-421f-b4bd-628dfde46f04 | underdog | Joe Burrow | Pass TDs | under | 0.06535420680993409 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|16d6e48b-3948-4277-8e98-69bfeda676cb | underdog | Ethan Moczulski | XP Made | over | 0.0651666116104308 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| underdog|435727be-5fbd-4cc1-b670-c8b031bf34d3 | underdog | Aidan Birr | XP Made | over | 0.06436112010722028 | 2026-10-29T05:46:21Z | 2026-10-31T23:30:00Z |
| underdog|d30c7d64-d8c9-4865-afdd-7418ae3b41bd | underdog | Elijah Higgins | Receiving Yards | under | 0.06373661570382627 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|64143154-aadc-45c7-a747-3bd0fa9821f1 | underdog | Jahmyr Gibbs | Rush Yards | under | 0.06350630569074456 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| prizepicks|16300983 | prizepicks | Luther Burden III | Rec Targets | under | 0.06341229986208663 | 2026-10-28T05:43:27Z | 2026-11-02T20:15:00.000-05:00 |
| underdog|846c8bc8-36cc-4c1a-8c70-e6ec2d66bc55 | underdog | Jadon Porter | Receiving Yards | over | 0.06335100923993253 | 2026-10-28T05:43:27Z | 2026-10-30T23:30:00Z |
| underdog|280d3d15-f8c9-44e8-9ba8-58789a2423a8 | underdog | Javonte Williams | Receptions | under | 0.06330301619118184 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|883b23cb-c9d9-4c70-9559-19170502bb28 | underdog | Ryan Wingo | Receiving Yards | under | 0.06329325454658252 | 2026-10-29T05:46:21Z | 2026-10-31T23:30:00Z |
| underdog|5b41b251-f891-4866-baa6-3172a85b6f42 | underdog | Kendrick Bourne | Receptions | under | 0.06320028651530141 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|01298330-4cd2-4997-afd2-79356f6caa5c | underdog | Lincoln Kienholz | Pass Yards | under | 0.06315374348395819 | 2026-10-29T05:46:21Z | 2026-10-31T19:15:00Z |
| underdog|baca9197-ba8b-4663-bd53-90146e8b84f9 | underdog | Jelani Thurman | Receiving Yards | under | 0.06300225759475764 | 2026-10-29T05:46:21Z | 2026-10-31T23:30:00Z |
| underdog|829af19d-6d7a-4c67-ad2d-e7700466a300 | underdog | Ashton Jeanty | Receiving Yards | over | 0.06284370429834163 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|484e2d7f-a4f8-4997-9d77-d2b39cbc54e4 | underdog | Tyler Goodson | Receiving Yards | over | 0.06257273013966114 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|c2ee8575-a516-49ad-b97c-0da52c295e72 | underdog | Rome Odunze | Receptions | under | 0.06252906711956707 | 2026-10-28T05:43:27Z | 2026-11-03T01:15:00Z |
| underdog|0b57f038-177b-4d34-b93a-95816320778a | underdog | Bo Nix | Rush Yards | under | 0.06252452212354309 | 2026-10-29T05:46:21Z | 2026-11-01T21:25:00Z |
| prizepicks|16347800 | prizepicks | Cameron Norrie | Total Games Won | over | 0.0623722265203247 | 2026-10-29T05:46:21Z | 2026-10-29T08:30:00.000-04:00 |
| underdog|bbb87a92-fdcb-4e0a-a501-3a3cbe524779 | underdog | Chris Rodriguez | Receiving Yards | over | 0.06234948855341682 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|e18a38b1-b957-45f7-b383-192e33d64f2e | underdog | Dalton Kincaid | Receiving Yards | under | 0.06147912296713087 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| prizepicks|16237751 | prizepicks | Tony Pollard | Rush Yards | under | 0.06140796389369363 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|7725104f-bdb6-4a8b-b4dd-872d39f95400 | underdog | T.J. Hockenson | Receptions | under | 0.06125765068766775 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16306526 | prizepicks | Francesca Jones | Total Games | over | 0.060903584365294194 | 2026-10-28T05:43:27Z | 2026-10-29T10:00:00.000-04:00 |
| underdog|d2a15f31-50f0-4ddb-9713-63caf82b161f | underdog | Bijan Robinson | Receiving Yards | under | 0.0608263421986458 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|8b6205f2-d917-417d-8d91-90bc4720c882 | underdog | Kyren Williams | Receiving Yards | over | 0.06069220762746541 | 2026-10-27T05:05:06Z | 2026-11-01T21:05:00Z |
| underdog|30294e8f-fb09-4591-8fec-13229ecc3549 | underdog | Kedrick Reescano | Rush Yards | under | 0.06056997571899836 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| underdog|ab18cec1-7142-4b7d-8dce-144cda4aba39 | underdog | T.J. Moore | Receiving Yards | under | 0.059983705190083 | 2026-10-29T05:46:21Z | 2026-10-31T23:00:00Z |
| underdog|08301f8a-0c44-4f66-8a15-9438be96f70d | underdog | Jake Bates | Kicking Points | under | 0.059904580386489825 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|0229aa5c-f68a-4aa4-a654-01431e2231fd | underdog | Carson Hilbert | FG Made | under | 0.05986076657907846 | 2026-10-29T05:46:21Z | 2026-10-31T19:15:00Z |
| underdog|d282b5b6-e850-4323-a633-6ddcde545cea | underdog | Tony Pollard | Receiving Yards | under | 0.059627955336889804 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|3026976c-9e97-4ac0-b388-38122ef04d9e | underdog | Bijan Robinson | Rush Yards | under | 0.0593041313288305 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|99475b75-f813-42b6-9fae-93d3ef6f713d | underdog | Chad Ryland | FG Made | over | 0.059292701651925794 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|9ac2c0bd-2c7f-4975-956e-724b7e1d2f9a | underdog | Bijan Robinson | Rush + Rec Yards | under | 0.059219928329845684 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|a0707940-d2db-45d7-9750-4ad46cf7ade6 | underdog | Drake Maye | Rush Yards | under | 0.0591966971934933 | 2026-10-28T05:43:27Z | 2026-11-01T21:25:00Z |
| underdog|17522f98-2927-48ee-aacf-7ac5feaad8e0 | underdog | Turbo Richard | Rush Yards | under | 0.0591882117234237 | 2026-10-29T05:46:21Z | 2026-10-31T19:30:00Z |
| underdog|5fa63acb-82d9-454b-aa06-0b1b0ea67bb5 | underdog | Keenan Allen | Receiving Yards | under | 0.059092087872505084 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|1909e47a-8882-45fe-a5ac-4ca977f1cf90 | underdog | Bryce Young | Pass TDs | under | 0.05906568723340133 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| prizepicks|16364189 | prizepicks | Harold Fannin Jr. | Rec Targets | under | 0.0590162864584155 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|15c359f6-49f6-417e-af04-7e3ac4910b59 | underdog | Treylon Burks | Receiving Yards | under | 0.058859686754247575 | 2026-10-29T05:46:21Z | 2026-11-02T01:20:00Z |
| underdog|21ccbd33-65c8-4adb-baf0-d54b8a99dde6 | underdog | Keon Coleman | Receiving Yards | under | 0.05861593824490208 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|98e2ad2f-6b25-437a-afa5-a57e1542c04f | underdog | Tommy Carr | Pass TDs | under | 0.05855747102412334 | 2026-10-27T05:05:06Z | 2026-10-31T16:30:00Z |
| underdog|c6a22cc5-e07d-4f81-bec2-d664844efafe | underdog | Camden Coleman | Rush Yards | over | 0.057483895532332685 | 2026-10-29T05:46:21Z | 2026-10-29T23:30:00Z |
| prizepicks|16238596 | prizepicks | Carnell Tate | Rec Yards | under | 0.05717982684838552 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| prizepicks|16301962 | prizepicks | Julia Riera | Total Games | over | 0.0569954131763547 | 2026-10-28T05:43:27Z | 2026-10-29T10:00:00.000-04:00 |
| prizepicks|16308172 | prizepicks | Julia Riera | Total Games | over | 0.0569954131763547 | 2026-10-28T05:43:27Z | 2026-10-29T10:00:00.000-04:00 |
| underdog|5fb87bff-c80d-4e34-8b35-ec63017df3e3 | underdog | Gunnar Helm | Receptions | under | 0.056747951711855205 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|c93c54b7-e461-409c-abe5-98bb72a80e11 | underdog | Jake Weinberg | FG Made | under | 0.05647385732766519 | 2026-10-29T05:46:21Z | 2026-10-31T23:30:00Z |
| underdog|1c4b412a-02d9-4d64-b73c-9c532f02117b | underdog | Keshaun Singleton | Receiving Yards | under | 0.056254835798307146 | 2026-10-29T05:46:21Z | 2026-10-31T16:45:00Z |
| underdog|534639cf-dfef-43e9-a654-d0e1df93574f | underdog | Cairo Santos | Kicking Points | under | 0.056155326916546455 | 2026-10-27T05:05:06Z | 2026-11-03T01:15:00Z |
| underdog|84f851cb-cc37-4d00-8260-116ed42334ff | underdog | Will Reichard | FG Made | under | 0.05615139676343428 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|6d42c914-27c3-438c-acbe-78fb08aa843b | underdog | Samaje Perine | Rush + Rec Yards | under | 0.05609614725030898 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|e43e01d6-98b5-4008-b8a0-38a770fa134f | underdog | Colton Joseph | Pass TDs | over | 0.05595494235457177 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| underdog|3612e26d-dc02-4174-8e0e-e28e06793eac | underdog | MarShawn Lloyd | Receiving Yards | over | 0.055857262958305065 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| underdog|ad2f8332-189a-4980-8d7f-6dc3712ba855 | underdog | Conner Harrell | Pass Yards | under | 0.05574141470793914 | 2026-10-29T05:46:21Z | 2026-10-30T23:00:00Z |
| prizepicks|16320579 | prizepicks | Justin Stevenson | Recs | under | 0.05551372280647482 | 2026-10-29T05:46:21Z | 2026-10-29T19:30:00.000-04:00 |
| underdog|4f579d9d-5e1f-4254-af57-b079cbe6a8f1 | underdog | Abu Sama | Rush Yards | under | 0.054633465022213445 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| prizepicks|16239372 | prizepicks | Jalen Coker | Rec Targets | under | 0.05453440832411327 | 2026-10-27T05:05:06Z | 2026-10-29T20:15:00.000-04:00 |
| underdog|614ac95f-50ff-496d-bcf5-dc76d3c3b006 | underdog | John Metchie III | Receiving Yards | under | 0.054499613013944126 | 2026-10-29T05:46:21Z | 2026-10-30T00:15:00Z |
| underdog|8230f1a8-97f9-4a79-b2fb-a7b30eaff15f | underdog | Bhayshul Tuten | Receiving Yards | under | 0.05432255572250255 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16238620 | prizepicks | Rome Odunze | Rec Yards | under | 0.054258843532627 | 2026-10-27T05:05:06Z | 2026-11-02T20:15:00.000-05:00 |
| underdog|f0a19a7f-3b51-4560-ac6e-749bf9bd2956 | underdog | Brenton Strange | Receptions | under | 0.054233780136315524 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|2faae4bd-a844-423e-b911-0b958f318d93 | underdog | Aidan Birr | FG Made | under | 0.05310544722157873 | 2026-10-29T05:46:21Z | 2026-10-31T23:30:00Z |
| underdog|1db0b382-7e86-4a18-890b-8f15c9278bfe | underdog | Carnell Tate | Receptions | under | 0.05308052318584133 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|5951bf0f-9641-4fe5-9ea3-d9ded8f398d2 | underdog | Kyle Cunanan | XP Made | over | 0.05267788600146506 | 2026-10-29T05:46:21Z | 2026-11-01T00:00:00Z |
| prizepicks|16237752 | prizepicks | James Cook III | Rush Yards | under | 0.05257854707589438 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|3490b0b5-7478-48ca-952a-8f7eb444d492 | underdog | TreVeyon Henderson | Rush + Rec Yards | under | 0.052478082271637194 | 2026-10-29T05:46:21Z | 2026-11-01T21:25:00Z |
| underdog|a688a6ab-bc4f-4c7b-b534-3f83979f56ab | underdog | Jameson Williams | Receptions | under | 0.05226576102064362 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16364217 | prizepicks | Darnell Washington | Rec Targets | under | 0.052041384305656635 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| prizepicks|16364179 | prizepicks | Rashod Bateman | Rec Targets | under | 0.051487447508205886 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|2213c610-5cc7-447a-a9d9-35da100d0a78 | underdog | Chad Ryland | Kicking Points | under | 0.05147593653628735 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|e2a75902-39bd-484e-a689-4b91f339a732 | underdog | Ezekiel Avit | Receiving Yards | under | 0.05141946070686243 | 2026-10-29T05:46:21Z | 2026-11-01T03:00:00Z |
| underdog|025c12db-56b2-4ddb-8c79-3abf440f1e88 | underdog | Ashton Daniels | Pass Yards | under | 0.05127908443137885 | 2026-10-29T05:46:21Z | 2026-10-31T23:00:00Z |
| underdog|eae32ced-5562-4171-9153-d6f892a851d8 | underdog | Jonah Coleman | Receptions | under | 0.05108606262017712 | 2026-10-28T05:43:27Z | 2026-11-01T21:25:00Z |
| underdog|8c6a2b69-3c72-4ca4-b012-907d8d700ba4 | underdog | Sean O'Haire | XP Made | under | 0.050970613562157374 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| prizepicks|16283727 | prizepicks | Sam LaPorta | Rec Targets | under | 0.05090193541573085 | 2026-10-28T05:43:27Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|527b6de2-ee73-45c1-83a6-8d18b7884caf | underdog | AJ Newberry | Receiving Yards | over | 0.05084450786730932 | 2026-10-29T05:46:21Z | 2026-11-01T03:00:00Z |
| prizepicks|16364212 | prizepicks | Garrett Wilson | Rec Targets | under | 0.0507311346043664 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|7e0462d2-a983-4059-a038-46671a9dad5a | underdog | Malik Washington | Pass TDs | under | 0.05070980152295568 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| underdog|1f7e9822-c406-4313-b611-dc7f4ec099b2 | underdog | Gavin Lahm | XP Made | over | 0.0506435068891391 | 2026-10-28T05:43:27Z | 2026-10-31T16:00:00Z |
| prizepicks|16282267 | prizepicks | Jared Goff | Fantasy Score | under | 0.050640325067197955 | 2026-10-28T05:43:27Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|74ef8b28-abe0-49ef-9c0b-31d23d58b6b7 | underdog | Gianni Spetic | FG Made | over | 0.05052028789972679 | 2026-10-29T05:46:21Z | 2026-10-31T23:30:00Z |
| underdog|93b6e997-487a-4a4e-aba9-a246d1bd4841 | underdog | Kevin Jennings | Pass Yards | under | 0.050513335450091956 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| underdog|ea542c11-cd5c-4842-a8fd-82e8af94d25f | underdog | Beau Pribula | Pass Yards | under | 0.050470485780179986 | 2026-10-29T05:46:21Z | 2026-10-31T19:45:00Z |
| underdog|05973e5c-c64d-495b-afe2-bc2861b239b1 | underdog | Tre Tucker | Receiving Yards | under | 0.050201006752433996 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|779ccae0-cd52-4c27-aeb5-6d2736e6178b | underdog | Kayden Dixon-Wyatt | Receiving Yards | over | 0.04982422068205983 | 2026-10-28T05:43:27Z | 2026-10-31T23:30:00Z |
| underdog|1932ca44-7aa4-4eb5-87a9-a049f89d1500 | underdog | Spencer Shrader | Kicking Points | over | 0.049734803311562326 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|8fdc408a-29d2-451e-b1ad-f4ae68023071 | underdog | T.J. Hockenson | Receiving Yards | under | 0.04970792234126764 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|16da61a8-68ed-4f43-a9cc-3a5ff016a453 | underdog | Jayden Mandal | Pass TDs | over | 0.04927710339745611 | 2026-10-29T05:46:21Z | 2026-11-01T03:00:00Z |
| underdog|18baf2c3-c45c-4f7a-9620-c0ccecf70cf5 | underdog | Chris Brooks Jr. | Receiving Yards | over | 0.04905589340720118 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| underdog|6735a668-2023-4b6b-ab9e-4d20931dd3f0 | underdog | Noah Bennee | Receptions | under | 0.04896750451664933 | 2026-10-29T05:46:21Z | 2026-10-31T19:45:00Z |
| underdog|de0945a1-afd6-4ffb-88f2-2b3a29d378ec | underdog | Caleb Williams | Rush Yards | under | 0.04850594420248733 | 2026-10-28T05:43:27Z | 2026-11-03T01:15:00Z |
| underdog|9c429295-348b-4e15-aa45-a34d7a58d78d | underdog | Jesse Legree | Receiving Yards | under | 0.048162633826316026 | 2026-10-29T05:46:21Z | 2026-11-01T03:00:00Z |
| underdog|8c5ae168-2fb7-4426-a1b4-ba3dc88d6e04 | underdog | RJ Harvey | Rush Yards | under | 0.04813187243949535 | 2026-10-29T05:46:21Z | 2026-11-01T21:25:00Z |
| underdog|b53d0902-7dac-4964-a15d-0a80ea884841 | underdog | Kalif Raymond | Receiving Yards | over | 0.048116048113270304 | 2026-10-28T05:43:27Z | 2026-11-03T01:15:00Z |
| underdog|30a83c24-84d5-41fd-8aff-52b353da4607 | underdog | Elic Ayomanor | Receiving Yards | under | 0.04801195329933672 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|50c47c24-28ca-49c3-9979-a5ba89e91038 | underdog | DJ Vonnahme | Receptions | under | 0.0479938812111137 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| underdog|0f765643-8169-4741-a28e-d9b60a95fe70 | underdog | Tate Sandell | XP Made | under | 0.047953647080236195 | 2026-10-29T05:46:21Z | 2026-10-31T20:15:00Z |
| underdog|d5f3d1ed-165b-44a8-a8b5-8618cb9266b0 | underdog | Nolan Hauser | XP Made | over | 0.04757407443121031 | 2026-10-29T05:46:21Z | 2026-10-31T23:00:00Z |
| prizepicks|16237001 | prizepicks | Jared Goff | Rush Yards | over | 0.04739043004803156 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|41490ebf-7cdd-41eb-9b66-e2d19e7deb83 | underdog | Jake Ferguson | Receiving Yards | under | 0.0472991412481123 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|321222b5-60cd-4361-8aea-73fc2575843a | underdog | Camden Coleman | Pass TDs | under | 0.047231747567130555 | 2026-10-27T05:05:06Z | 2026-10-29T23:30:00Z |
| prizepicks|16338686 | prizepicks | Ben Shelton | 1st Set Total Games | under | 0.047154678718495546 | 2026-10-29T05:46:21Z | 2026-10-29T14:10:00.000-04:00 |
| underdog|e44b5b57-b2a3-412d-9a94-e5caa236902c | underdog | Chris Bell | Receiving Yards | under | 0.047142394731641835 | 2026-10-28T05:43:27Z | 2026-11-01T21:25:00Z |
| underdog|606af54f-68bc-4f75-b3c3-3f62234232b2 | underdog | Elijah Higgins | Receptions | under | 0.04707934818798154 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|708bf473-ef2b-4551-bc19-c8f8e0500602 | underdog | Gavin Lahm | FG Made | under | 0.0470405683254459 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| prizepicks|16364193 | prizepicks | George Pickens | Rec Targets | under | 0.046942158355769203 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|d38d4943-2dba-4a2a-90bc-bdc04608ef33 | underdog | Yannick Smith | Receiving Yards | under | 0.04639267680093917 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| prizepicks|16302756 | prizepicks | Tatjana Maria | 1st Set Total Games | over | 0.04606460198283813 | 2026-10-28T05:43:27Z | 2026-10-29T16:00:00.000-04:00 |
| underdog|5981aff5-6dbd-46ef-bd40-7e07179c6e02 | underdog | Barryn Sorrell | Sacks | under | 0.04594682466041766 | 2026-10-29T05:46:21Z | 2026-10-30T00:15:00Z |
| prizepicks|16283726 | prizepicks | Jameson Williams | Rec Targets | under | 0.04588546580195274 | 2026-10-28T05:43:27Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|2c10d59f-2805-4247-b3a9-7f132630e8b7 | underdog | Caleb Douglas | Receiving Yards | under | 0.04572395459474321 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|ccf764a6-e25c-4a47-801c-bbf244f5ec13 | underdog | Colston Loveland | Receptions | under | 0.04553104131701269 | 2026-10-28T05:43:27Z | 2026-11-03T01:15:00Z |
| underdog|1d26f3cc-54a4-43a9-a529-6e4e40747d41 | underdog | Davis Warren | Pass Yards | under | 0.04548534706963725 | 2026-10-29T05:46:21Z | 2026-10-31T19:15:00Z |
| prizepicks|16295419 | prizepicks | Luciano Darderi | Total Games Won | over | 0.045447415604439434 | 2026-10-29T05:46:21Z | 2026-10-29T08:30:00.000-04:00 |
| underdog|830f369c-f207-4c9d-a288-ea0d11258ba3 | underdog | DK Metcalf | Receptions | under | 0.04537863534296749 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|c22f89a3-d617-447a-a58e-cd99f746e9de | underdog | Nolan Bartley | FG Made | over | 0.045360020231472564 | 2026-10-28T05:43:27Z | 2026-10-31T16:00:00Z |
| underdog|b610bf87-5fe8-4609-a169-6a3823d87fcc | underdog | Rashod Bateman | Receptions | under | 0.045179537492164634 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|e13649e5-fba3-4ab7-8e62-437ce584f560 | underdog | Mike Gesicki | Receiving Yards | under | 0.04487689705356923 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|6f538e31-bd0b-442f-a0c6-c806526a0af6 | underdog | Derrick Henry | Receiving Yards | over | 0.044786350412196085 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|c000965f-9220-48af-a50e-e406a9b82207 | underdog | Patrick Mahomes | Pass TDs | under | 0.044605755569356864 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|07c9159e-953d-4ca9-8a3d-7f2c24f3b622 | underdog | Konata Mumpfield | Receiving Yards | under | 0.04449810098666451 | 2026-10-27T05:05:06Z | 2026-11-01T21:05:00Z |
| underdog|87e3070a-8f03-4f71-93e8-9a33633359f7 | underdog | Colton Joseph | Pass Yards | over | 0.04443646141475743 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| underdog|a59eab77-29bf-422a-8460-35c449cac12a | underdog | Kirk Cousins | Pass TDs | under | 0.044346815076756196 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|3be5851f-dea0-40b3-9bb0-9f568d8723b4 | underdog | Samaje Perine | Receiving Yards | over | 0.04427871151764762 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|1e6fc878-8076-4363-92cd-c8b7f6254266 | underdog | Tommy Tremble | Receiving Yards | under | 0.0440297778283254 | 2026-10-28T05:43:27Z | 2026-10-30T00:15:00Z |
| prizepicks|16302758 | prizepicks | Tatjana Maria | Total Games | over | 0.043912578008937 | 2026-10-28T05:43:27Z | 2026-10-29T16:00:00.000-04:00 |
| underdog|fdf0e9c3-6e6b-478e-8aa9-6b45b8e1f195 | underdog | Tyler Goodson | Receptions | under | 0.04381326256994522 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|3240a9a9-a7e7-4cfa-9591-2bcad0bdb937 | underdog | Chris Bell | Receptions | under | 0.043709873908828745 | 2026-10-29T05:46:21Z | 2026-11-01T21:25:00Z |
| underdog|7db7fbf5-59dc-48bb-a58a-82abe396aa29 | underdog | Jaylen Warren | Rush + Rec Yards | under | 0.0436668571974157 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|76b1c95e-f2da-413c-bfdf-08dc4716e96d | underdog | Bryant Wesco | Receiving Yards | under | 0.04364958858262513 | 2026-10-29T05:46:21Z | 2026-10-31T23:00:00Z |
| underdog|f63cbd81-60b8-49ae-a679-586b512a716e | underdog | Byrum Brown | Rush Yards | under | 0.043629878324355165 | 2026-10-29T05:46:21Z | 2026-10-31T16:45:00Z |
| underdog|f9073931-b033-47be-b4c0-c21ae3da3381 | underdog | Duce Robinson | Receiving Yards | under | 0.043544683185050226 | 2026-10-29T05:46:21Z | 2026-10-31T23:00:00Z |
| underdog|d3cc7358-d7be-4564-b99a-af1f66ccb50f | underdog | Blake Corum | Receptions | over | 0.04322925578199588 | 2026-10-29T05:46:21Z | 2026-11-01T21:05:00Z |
| prizepicks|16364216 | prizepicks | DK Metcalf | Rec Targets | under | 0.04294350532078739 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|78fe307a-7e17-4bd9-9d8e-fd56b5fcaa2d | underdog | Dyami Brown | Receptions | over | 0.04281344784836044 | 2026-10-29T05:46:21Z | 2026-11-02T01:20:00Z |
| underdog|31b6cd09-6d41-4dce-bfef-ef128d55cad2 | underdog | Anthony Evans III | Receptions | under | 0.042671576227215735 | 2026-10-29T05:46:21Z | 2026-10-31T23:30:00Z |
| underdog|03de3a38-04de-414a-b7a5-843d90fdf6d0 | underdog | Malik Willis | Rush Yards | under | 0.042608298491113694 | 2026-10-28T05:43:27Z | 2026-11-01T21:25:00Z |
| underdog|21ec210e-8d38-4fb5-8cea-ec22dc7def12 | underdog | Charlie Becker | Receptions | under | 0.04239973318552892 | 2026-10-29T05:46:21Z | 2026-10-31T19:30:00Z |
| underdog|51d46586-a523-4495-90f8-ba3a7a79a2ca | underdog | Will Kacmarek | Receiving Yards | over | 0.042084427220204 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|c15e674d-1cff-45ca-856b-4c480e003161 | underdog | Josh Cameron | Receiving Yards | over | 0.04200192948698528 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|b4dedce4-c003-49dd-9798-feada7e5d80f | underdog | RJ Harvey | Receptions | over | 0.041882620116427405 | 2026-10-28T05:43:27Z | 2026-11-01T21:25:00Z |
| underdog|3b28befe-ffab-48de-94a7-aec131ad5e79 | underdog | Harold Fannin | Receiving Yards | under | 0.04179548726493032 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16364175 | prizepicks | Ty Johnson | Rec Targets | under | 0.04178599301145003 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|60c57a56-dc2f-4631-af7c-13c245ed2cc1 | underdog | Lukas Van Ness | Sacks | over | 0.041770309051133714 | 2026-10-29T05:46:21Z | 2026-10-30T00:15:00Z |
| underdog|8dd20ddf-9d01-4078-8e3c-311b59ce525a | underdog | Nate Boerkircher | Receiving Yards | under | 0.04155813247968276 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|3823a994-1046-4ef5-837b-f588e8417cbe | underdog | Michael Scott | Receiving Yards | under | 0.04151869200585112 | 2026-10-29T05:46:21Z | 2026-10-29T23:30:00Z |
| underdog|9b7821ea-2e53-461c-b921-cb3f9b0a8766 | underdog | Kenny Johnson | Receiving Yards | under | 0.041462374613398856 | 2026-10-28T05:43:27Z | 2026-10-31T16:00:00Z |
| prizepicks|16364197 | prizepicks | Brenton Strange | Rec Targets | under | 0.041443366540232285 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|e5d8e1c9-e08e-4e30-9779-e89a1ccad2d8 | underdog | James Cook | Receptions | under | 0.04119703252365636 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| prizepicks|16345985 | prizepicks | Tee Higgins | Rec Targets | under | 0.04097185814900839 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|5606a896-094d-4881-8dc0-335fec3d998c | underdog | Mike Washington | Rush Yards | under | 0.04074539618844153 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|e79cbf75-3522-461e-a424-eea0877fd852 | underdog | Josh Cuevas | Receiving Yards | over | 0.040617425881482316 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|30b2d4f9-6c5e-4bc6-8b2c-1d4427e03d96 | underdog | Efton Chism | Receptions | over | 0.04045962303919298 | 2026-10-29T05:46:21Z | 2026-11-01T21:25:00Z |
| underdog|61afb864-4e07-4a48-bd41-c4eb74160900 | underdog | Reed Harris | Receiving Yards | under | 0.04036453470122037 | 2026-10-29T05:46:21Z | 2026-10-31T19:30:00Z |
| underdog|fac6134d-822d-44dc-9f73-a71adfd62ab0 | underdog | Kyren Williams | Receptions | over | 0.03984826894881116 | 2026-10-27T05:05:06Z | 2026-11-01T21:05:00Z |
| prizepicks|16364221 | prizepicks | Emeka Egbuka | Rec Targets | under | 0.03957168775040509 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|7f01a8a1-7362-4713-9044-e7b15105374a | underdog | RJ Harvey | Receiving Yards | over | 0.039525740504224194 | 2026-10-28T05:43:27Z | 2026-11-01T21:25:00Z |
| underdog|b6d94039-076e-4d23-94d9-b0ea1abc0b69 | underdog | Ashton Daniels | Rush Yards | under | 0.03941215066956005 | 2026-10-29T05:46:21Z | 2026-10-31T23:00:00Z |
| underdog|2f7514c5-2b88-4864-88b6-649131ebb46e | underdog | Wayshawn Parker | Receiving Yards | over | 0.03934486821897232 | 2026-10-29T05:46:21Z | 2026-10-31T19:45:00Z |
| underdog|d06eb894-124b-4188-9763-d586cc1def8f | underdog | Tyler Warren | Receptions | under | 0.039251759862195756 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|4192d51e-49c7-433a-892e-6c32daf1a68a | underdog | Luther Burden | Receptions | under | 0.03905790770780704 | 2026-10-28T05:43:27Z | 2026-11-03T01:15:00Z |
| underdog|c1ec5863-ef74-439f-890c-5791b8837f26 | underdog | Trace Johnson | Pass TDs | under | 0.03888319613866498 | 2026-10-28T05:43:27Z | 2026-10-30T23:00:00Z |
| underdog|5e1335c5-ac9f-4444-8e0d-eb1495cf8f51 | underdog | Ryan Flournoy | Receiving Yards | under | 0.03866220721623803 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|ba5b752c-a956-46bc-8f78-425674b1c328 | underdog | Josh Downs | Receptions | under | 0.038610418627245346 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16290284 | prizepicks | Tommy Paul | Total Games | over | 0.038316615124551534 | 2026-10-28T05:43:27Z | 2026-10-29T08:00:00.000-04:00 |
| underdog|c09f952c-d7f7-4831-9e20-2fec7eb50f4d | underdog | Javon Tracy | Receptions | over | 0.03824889522091379 | 2026-10-29T05:46:21Z | 2026-10-31T19:30:00Z |
| underdog|178431a1-f0fe-4939-bf64-ca52aeaf6d23 | underdog | Michael Penix | Pass TDs | under | 0.03824422373301384 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|02d88dd0-0193-43d5-ac9b-4721fa50221e | underdog | Tony Diaz | Receptions | over | 0.03799071741717408 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| underdog|7ecdc2be-8a03-41cf-a4a6-70b7ea77d4a2 | underdog | Craig Dandridge | Receiving Yards | under | 0.037959336678760836 | 2026-10-29T05:46:21Z | 2026-10-31T19:30:00Z |
| underdog|bf6ca6da-af3f-4713-b41b-c325c3778b5a | underdog | Kenyon Sadiq | Receiving Yards | under | 0.0379541272976508 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|ce994eba-a6a8-45f5-b850-da23fb0d4bbd | underdog | Jaylen Warren | Rush Yards | under | 0.03784363197833929 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|5d02b860-79d7-44a4-ad10-fc9a11ad352d | underdog | Jonathan Taylor | Receiving Yards | over | 0.03782774826923374 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|128f7a57-b988-4344-ad48-34d2b59c9458 | underdog | Drew Mestemaker | Pass TDs | over | 0.03769838205409798 | 2026-10-29T05:46:21Z | 2026-10-31T23:00:00Z |
| underdog|009648c8-a8e6-4e1f-b73c-2db8a09d8d94 | underdog | Alberto Mendoza | Pass TDs | under | 0.03766539666977964 | 2026-10-29T05:46:21Z | 2026-10-31T23:30:00Z |
| underdog|ea1ca778-0c1f-41f0-aa6d-ee49d30fc0c6 | underdog | Eric Olsen | Receptions | under | 0.037652007406090426 | 2026-10-29T05:46:21Z | 2026-11-01T03:00:00Z |
| prizepicks|16300981 | prizepicks | Colston Loveland | Rec Targets | under | 0.03749133938696103 | 2026-10-28T05:43:27Z | 2026-11-02T20:15:00.000-05:00 |
| underdog|54cf05e2-86ba-4145-9c8a-43035b15a415 | underdog | Chase Brown | Receiving Yards | under | 0.03733610239343621 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|2e7942ca-9587-4276-b7a4-c2d60df5e093 | underdog | DeMario Douglas | Receiving Yards | under | 0.037301755521942925 | 2026-10-28T05:43:27Z | 2026-11-01T21:25:00Z |
| underdog|72087b6b-aeea-41cc-94c6-6ddc4788ffd5 | underdog | Jordan Lovett | Rush Yards | under | 0.037168484525488155 | 2026-10-29T05:46:21Z | 2026-10-29T23:30:00Z |
| underdog|a6465eb4-f35b-4df3-96fa-5fb54b912ba0 | underdog | Josh Cameron | Receptions | over | 0.03708353453092156 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|c202626d-b120-4dcb-b6f5-f780fcc05670 | underdog | Chase McLaughlin | Kicking Points | under | 0.036936611973116484 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|ad0ab0a2-d9e4-4e95-a294-1e3d5a21bc4a | underdog | Caden Veltkamp | Pass TDs | over | 0.03693271208921112 | 2026-10-27T05:05:06Z | 2026-10-29T23:30:00Z |
| underdog|331fd1c9-ac63-4ce8-b35f-6a26d2bc3576 | underdog | Keenan Allen | Receptions | under | 0.03657607896715964 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|5c4d4242-97a0-43dc-9262-319033e766a5 | underdog | Drake Lindsey | Pass Yards | over | 0.036344697021042816 | 2026-10-29T05:46:21Z | 2026-10-31T19:30:00Z |
| underdog|b813491c-788b-4736-a5c6-73ef18465a85 | underdog | Trent Mosley | Receiving Yards | under | 0.03630113995308826 | 2026-10-28T05:43:27Z | 2026-10-31T23:30:00Z |
| underdog|def7e19b-34f0-48f0-9fe7-90b650851a32 | underdog | AJ Newberry | Receptions | over | 0.036203441209521625 | 2026-10-29T05:46:21Z | 2026-11-01T03:00:00Z |
| underdog|e7fb2bbb-1d1d-4e90-999d-7d2bf0bdf4d5 | underdog | Eric Olsen | Receiving Yards | under | 0.03607044045465946 | 2026-10-29T05:46:21Z | 2026-11-01T03:00:00Z |
| underdog|60dcd824-4333-4248-9adb-7a2d45a8e21d | underdog | Aaron Rodgers | Pass TDs | over | 0.035917777674994156 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|2be7e738-53f7-4351-87dd-3388416e0910 | underdog | CeeDee Lamb | Receptions | under | 0.035657182557574885 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| prizepicks|16364198 | prizepicks | Jakobi Meyers | Rec Targets | under | 0.03556814695217747 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|632052a4-eb83-4978-ab06-3408d975b26d | underdog | Isaac TeSlaa | Receiving Yards | under | 0.035478587007757634 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|be4d1cc9-62d4-403b-b891-bd5fa7d681ae | underdog | Jaylen Raynor | Pass TDs | under | 0.03545607119174554 | 2026-10-29T05:46:21Z | 2026-10-31T23:00:00Z |
| prizepicks|16270047 | prizepicks | Elena Rybakina | Total Games | over | 0.0353914508451324 | 2026-10-29T05:46:21Z | 2026-10-29T04:00:00.000-04:00 |
| underdog|579466c0-c1f1-4bb6-bade-551753e538f0 | underdog | Bucky Irving | Receiving Yards | under | 0.035277747501728185 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|f3938f50-0ad5-46d6-8905-53a081b714ed | underdog | Jayden Mandal | Rush Yards | over | 0.03520194592809056 | 2026-10-29T05:46:21Z | 2026-11-01T03:00:00Z |
| underdog|d301a1b0-bd7d-4a02-9be6-b3c71ea603b1 | underdog | Darren Waller | Receiving Yards | over | 0.03506742195784279 | 2026-10-28T05:43:27Z | 2026-10-30T00:15:00Z |
| prizepicks|16332054 | prizepicks | Aidan Chiles | Pass Comp | under | 0.035035949799829935 | 2026-10-29T05:46:21Z | 2026-10-31T15:30:00.000-04:00 |
| underdog|87f9bdf4-f40f-4b04-9ebd-add8492f187a | underdog | Jerry Jeudy | Receiving Yards | under | 0.03475932480352539 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|c629e073-546f-4206-a875-39ce3682f009 | underdog | Mike Gesicki | Receptions | under | 0.034662618407678036 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|38be05a8-f1e4-46f7-a5d7-641d48560923 | underdog | Chris Rodriguez | Receptions | over | 0.034641968529540934 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|bfc06dd7-40ab-4a2a-8625-e8be732febf5 | underdog | Omarion Miller | Receiving Yards | over | 0.034223888783094125 | 2026-10-29T05:46:21Z | 2026-10-31T19:30:00Z |
| prizepicks|16236993 | prizepicks | Aaron Rodgers | Rush Yards | over | 0.03417868452026862 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|560d1c3b-e4d8-482b-bd34-a9ff0cb53ee6 | underdog | Jacoby Brissett | Rush Yards | under | 0.03413392339426191 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|e65eb02e-d60d-468f-a975-5ee41aa5b8ef | underdog | Duke Watson | Rush Yards | under | 0.03404499786728077 | 2026-10-28T05:43:27Z | 2026-10-30T23:30:00Z |
| underdog|0f681c42-8f76-4cb8-9522-05ec95d04f05 | underdog | Justice Hill | Rush Yards | under | 0.0339590282720027 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|a08c6057-39f2-45de-a1f6-14d94390ada6 | underdog | Charlie Becker | Receiving Yards | under | 0.03387812144126445 | 2026-10-29T05:46:21Z | 2026-10-31T19:30:00Z |
| underdog|b6d0b727-a1c5-4b46-a33f-d1812b1d91ea | underdog | Josh Downs | Receiving Yards | under | 0.0335880037665488 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|dfb622f5-ccf5-417d-85b5-4a212d464961 | underdog | Aidan Chiles | Pass Yards | under | 0.033567067119342764 | 2026-10-29T05:46:21Z | 2026-10-31T19:30:00Z |
| underdog|c247c38e-8847-4570-8f76-f033c195a0d7 | underdog | Ashton Jeanty | Receptions | under | 0.033565625285393086 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|69370026-9515-4c28-94a7-7b9ed03c4bdc | underdog | Derrick Henry | Receptions | over | 0.033424548277637356 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|c97a21be-74a7-497c-944c-4ddacac7dd6f | underdog | Kayden Dixon-Wyatt | Receptions | over | 0.03325325310824867 | 2026-10-28T05:43:27Z | 2026-10-31T23:30:00Z |
| underdog|77705afe-034d-4ac9-8061-f356d54de137 | underdog | Isaiah Marshall | Pass TDs | over | 0.032765243210280404 | 2026-10-28T05:43:27Z | 2026-10-31T19:30:00Z |
| underdog|c94fca32-9311-4c26-b4a0-04ea9a61b58d | underdog | Keon Coleman | Receptions | over | 0.03273798327050681 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|5f2d19d8-4bbb-4ea1-a272-1c7cdd003398 | underdog | Dylan Sampson | Rush + Rec Yards | under | 0.03267139201557545 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|95e3287a-859c-45f6-b5b3-d38de81f9186 | underdog | Lawson Luckie | Receiving Yards | over | 0.03260831179607715 | 2026-10-28T05:43:27Z | 2026-10-31T19:30:00Z |
| underdog|1f68e0f5-4758-426a-a308-b5c68e1c8048 | underdog | Sam Darnold | Rush Yards | over | 0.0325476533253789 | 2026-10-27T05:05:06Z | 2026-11-03T01:15:00Z |
| underdog|254bd294-909f-4b6a-bfbb-dd5313c81151 | underdog | Gabe Panikowski | FG Made | over | 0.032531030009363526 | 2026-10-29T05:46:21Z | 2026-10-31T23:00:00Z |
| underdog|b9a41163-712b-4516-b471-5bfa5ecae2d1 | underdog | Braden Pegan | Receiving Yards | under | 0.032292065704640605 | 2026-10-29T05:46:21Z | 2026-10-31T19:45:00Z |
| underdog|7399aede-c517-452b-bf90-398652b085c6 | underdog | Dyami Brown | Receiving Yards | under | 0.03201524823912261 | 2026-10-29T05:46:21Z | 2026-11-02T01:20:00Z |
| underdog|31c29fbb-9913-48cf-8fbb-3dcf69104679 | underdog | Tee Higgins | Receiving Yards | under | 0.031976149300329104 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|3c7d6af2-24a4-4712-868a-a3ddc96c35d6 | underdog | Bucky Irving | Receptions | over | 0.031934092041214335 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|e92c5de3-62fb-4c5f-ad3d-e754b69b5abd | underdog | Quinshon Judkins | Receiving Yards | over | 0.03191260382479533 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|a973e2a4-34d4-4bb0-bf44-199878fc388c | underdog | Cooper Barkate | Receptions | under | 0.031905349719951404 | 2026-10-28T05:43:27Z | 2026-10-31T23:30:00Z |
| underdog|68231f2d-2350-4cf6-aa11-1eb8922ae8bc | underdog | Chase Brown | Receptions | under | 0.03177557054308333 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|ea50e946-5a1f-4248-a186-6a00b37d7eee | underdog | Justice Hill | Receiving Yards | under | 0.0317235807676185 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| prizepicks|16236999 | prizepicks | Kyler Murray | Rush Yards | under | 0.031657095278137426 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|33f46818-cddb-41ab-a9fb-25a59017fa7e | underdog | Reece Vander Zee | Receptions | under | 0.031621174892085824 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| underdog|d073252d-8dea-4175-8e3c-264f6dd7d0a2 | underdog | Cole Tabb | Rush Yards | under | 0.0314468202815551 | 2026-10-29T05:46:21Z | 2026-10-31T19:45:00Z |
| underdog|67df3123-52a6-49f6-abdd-cc6b817ff9cc | underdog | Devontez Walker | Receptions | over | 0.03138105929047941 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|193613f4-ecf6-4d47-a1a4-8eb577ac8fad | underdog | Puka Nacua | Receptions | under | 0.031332412754902395 | 2026-10-28T05:43:27Z | 2026-11-01T21:05:00Z |
| underdog|e0abe106-06ec-42ad-94f5-0a6263c65def | underdog | Anna Bondar | Double Faults | under | 0.031219585779975634 | 2026-10-29T05:46:21Z | 2026-10-29T07:20:00Z |
| prizepicks|16364187 | prizepicks | Mike Gesicki | Rec Targets | under | 0.031142143077535156 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|82eb77cc-0d7d-4a88-81ca-87976f624ba3 | underdog | Kenneth Walker III | Receptions | under | 0.030962031950642066 | 2026-10-29T05:46:21Z | 2026-11-01T21:25:00Z |
| underdog|5124882c-f8a6-4e78-a04d-110145a51a3c | underdog | Arch Manning | Rush Yards | under | 0.030956685466541622 | 2026-10-29T05:46:21Z | 2026-10-31T23:30:00Z |
| underdog|7ec1e3c1-12a5-44b7-a8c4-b1243ccb2016 | underdog | Andre Szmyt | Kicking Points | under | 0.03089301505307862 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|8cc6f535-a1aa-477d-b96b-7a867a85aae3 | underdog | Bear Bachmeier | Pass TDs | under | 0.030732250232436864 | 2026-10-29T05:46:21Z | 2026-10-31T19:30:00Z |
| underdog|82b555cc-848d-4e23-b158-85217a0cb986 | underdog | Konata Mumpfield | Receptions | over | 0.03054904013493953 | 2026-10-29T05:46:21Z | 2026-11-01T21:05:00Z |
| underdog|c441577d-b8a7-46fb-95e6-9f780f63dd69 | underdog | Chuba Hubbard | Receptions | under | 0.030499835109236484 | 2026-10-28T05:43:27Z | 2026-10-30T00:15:00Z |
| underdog|8c835faa-8b75-4c85-a171-041dfd067b47 | underdog | Tyler Robles | FG Made | under | 0.030444708444404167 | 2026-10-29T05:46:21Z | 2026-11-01T00:00:00Z |
| underdog|838a86da-33a6-4072-a43a-84084793ee97 | underdog | Gideon Davidson | Rush Yards | under | 0.030286308383850602 | 2026-10-29T05:46:21Z | 2026-10-31T23:00:00Z |
| prizepicks|16357812 | prizepicks | Novak Djokovic | Total Games | over | 0.03016178777027345 | 2026-10-29T05:46:21Z | 2026-10-29T13:00:00.000-04:00 |
