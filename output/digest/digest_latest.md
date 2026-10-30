# Pipeline Digest -- 2026-10-30T05:36:02Z

## Run summary
- Ingestion: 43222 rows (PrizePicks OK, Underdog OK)
- Estimation: 43222 rows estimated (from 43222 ingested props)
- CLV logging: 271 newly flagged, 0 newly closed, 838 still open (106853 total ever logged)

## Currently open flags
Sizing is a manual step (sizing_engine.py, Session 2.6) -- this table is what to scan to pick a pair worth sizing.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_edge | first_flagged_at | game_start_time |
|---|---|---|---|---|---|---|---|
| underdog|d54271ea-1ac6-4f11-9ae3-1bc3517bc245 | underdog | Tanner McKee | Pass TDs | under | 0.5635514018691589 | 2026-10-29T05:46:21Z | 2026-11-02T01:20:00Z |
| underdog|79fbdd4e-9f95-4c05-91ab-801fa00b9f95 | underdog | Jacoby Brissett | Pass Yards | under | 0.4601730325335911 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|2f5aaa24-7fb0-41f8-a373-c3b035aa8e86 | underdog | Malik Willis | Pass Yards | under | 0.44253845031977934 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|cbd6e719-1d7b-4baf-b4b8-82e8e169d339 | underdog | Tanner McKee | Pass Yards | under | 0.4357142857142857 | 2026-10-29T05:46:21Z | 2026-11-02T01:20:00Z |
| underdog|12009851-2423-4ab3-91bd-f13fd4301a82 | underdog | Josh Allen | Pass Yards | under | 0.42261306532663323 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|00b8c4ae-47ab-4321-88dd-8e806f1bb14b | underdog | Chase Brown | Rush + Rec Yards | under | 0.42261306532663323 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|57616bdd-aab7-4f96-b4bc-4643e4882cbc | underdog | Stefon Diggs | Receiving Yards | under | 0.411308499153475 | 2026-10-29T05:46:21Z | 2026-11-02T01:20:00Z |
| underdog|3fafb547-a80e-4119-b750-f8178a9ec1d1 | underdog | Geno Smith | Pass Yards | under | 0.40697585543065895 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|f3eebd9b-62e1-4a04-8832-64b7a01ba1db | underdog | Brandon White | Rush Yards | under | 0.4 | 2026-10-30T05:46:05Z | 2026-10-31T02:30:00Z |
| underdog|4fb2db3b-a9af-4572-978e-2cf5136dc27b | underdog | Tommy Carr | Pass Yards | under | 0.4 | 2026-10-30T05:46:05Z | 2026-10-31T16:30:00Z |
| underdog|cbbf56fd-1783-40d2-a4e3-ee386ff04cac | underdog | Dak Prescott | Pass Yards | under | 0.4 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|faa089e3-80fc-4158-84b9-d7879fc131d8 | underdog | Caleb Williams | Pass Attempts | under | 0.4 | 2026-10-28T05:43:27Z | 2026-11-03T01:15:00Z |
| underdog|85973a27-8bc2-47e0-9aa3-0742a98196d6 | underdog | Cam Ward | Pass Yards | under | 0.4 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|db5463ff-e8bc-462f-b571-812b6f3c7077 | underdog | Cole Tabb | Receiving Yards | over | 0.4 | 2026-10-29T05:46:21Z | 2026-10-31T19:45:00Z |
| underdog|dc6b4600-d899-46fe-9510-3e8eddec37b8 | underdog | Justin Herbert | Pass Yards | under | 0.4 | 2026-10-29T05:46:21Z | 2026-11-01T21:05:00Z |
| underdog|551de737-4ed8-4f82-8609-b1e2a3e0c17e | underdog | Trevor Lawrence | Pass Yards | under | 0.4 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|5c715537-c01f-477b-b764-20a57b702bd8 | underdog | Lamar Jackson | Pass Attempts | under | 0.4 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|3c8a224d-a083-4783-83ce-39c3dcbaf581 | underdog | Michael Penix | Pass Yards | under | 0.4 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|aebf7015-fdf5-409a-af16-dd8969119164 | underdog | A.J. Brown | Receiving Yards | under | 0.4 | 2026-10-30T05:46:05Z | 2026-11-01T21:25:00Z |
| underdog|2491f256-7fe6-4dbe-b49b-d313ec64d9ce | underdog | Justin Herbert | Pass Attempts | under | 0.3961059254162722 | 2026-10-29T05:46:21Z | 2026-11-01T21:05:00Z |
| underdog|79604ed7-d7d4-437f-9e7e-0be17c3600ec | underdog | Joe Burrow | Pass Yards | under | 0.38083915915549604 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|87da43a0-1884-4911-b9fa-cc92f8d15e16 | underdog | Bo Nix | Pass Yards | under | 0.3761948122970198 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|3acf5e4b-d2bd-4a59-a6eb-512b84c05a16 | underdog | Tanner McKee | Pass Attempts | under | 0.37114298002617396 | 2026-10-29T05:46:21Z | 2026-11-02T01:20:00Z |
| underdog|7b31b809-c2af-4bb7-b306-9fadeadd490b | underdog | Aaron Rodgers | Pass Yards | under | 0.3642857142857143 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|d7d276a3-6770-4024-9eaf-2d86637b63b4 | underdog | Jayden Daniels | Pass Yards | under | 0.3602245957330912 | 2026-10-29T05:46:21Z | 2026-11-02T01:20:00Z |
| underdog|e91de51c-d8ee-463f-a902-d48962430cd8 | underdog | Jordan Marshall | Rush Yards | under | 0.3587416887171023 | 2026-10-30T05:46:05Z | 2026-10-31T16:30:00Z |
| underdog|899a68de-e102-4983-8a34-59a7909475f8 | underdog | Deshaun Watson | Pass Attempts | under | 0.3579985593698499 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|b84a0641-785c-4170-b552-78db2c176462 | underdog | Bhayshul Tuten | Rush + Rec Yards | under | 0.35703450764454703 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| underdog|28a2ea78-e692-4c07-bd82-65806aa4b30c | underdog | Baker Mayfield | Pass Yards | under | 0.35685279187817265 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| prizepicks|16395222 | prizepicks | Kyler Murray | Pass+Rush+Rec TDs | under | 0.35094246505677495 | 2026-10-30T05:46:05Z | 2026-11-01T13:00:00.000-05:00 |
| prizepicks|16237064 | prizepicks | Malik Willis | Pass Yards | under | 0.35094246505677495 | 2026-10-27T05:05:06Z | 2026-11-01T16:25:00.000-05:00 |
| underdog|47a05125-b997-4bb8-bcf1-8fa0b85c1365 | underdog | Michael Penix | Pass Attempts | under | 0.34674579695250174 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| underdog|edb405a9-2108-4e53-980d-f2bfe7c76348 | underdog | Josh Allen | Pass Attempts | under | 0.34457095080515066 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|c6b45392-15a5-4784-9f7e-de4a0ccd50be | underdog | Jared Goff | Pass Yards | under | 0.33718592964824123 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|86c0f981-7496-4227-9196-e2f09e3cc959 | underdog | Kyler Murray | Pass Yards | under | 0.3360431449180866 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|a787f9cc-5177-4e80-a5c5-3a1c910d0dbb | underdog | Lamar Jackson | Pass Yards | under | 0.3343434343434344 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|894dbf45-d7f8-4bd4-af0e-3db65a37745f | underdog | Drake Maye | Pass Yards | under | 0.3294558529152034 | 2026-10-28T05:43:27Z | 2026-11-01T21:25:00Z |
| underdog|f20c590d-7e42-4932-a3cf-4750126c8a0c | underdog | Rachaad White | Rush Yards | under | 0.3290278063292911 | 2026-10-29T05:46:21Z | 2026-11-02T01:20:00Z |
| underdog|4362bea0-10bb-40b2-91e8-38d658875ef5 | underdog | Deshaun Watson | Pass Yards | under | 0.3285714285714286 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| underdog|064f376d-57f1-44fb-b420-650bdf4b6b47 | underdog | Jaylen Wright | Rush Yards | under | 0.3261539848934951 | 2026-10-29T05:46:21Z | 2026-11-01T21:25:00Z |
| underdog|2f1d2e08-979d-4b41-9b7f-9882d725836d | underdog | Bo Nix | Pass Attempts | under | 0.32234118524297706 | 2026-10-29T05:46:21Z | 2026-11-01T21:25:00Z |
| underdog|a9c098a9-5051-4b9c-9177-f98d2f838c81 | underdog | Caleb Williams | Pass Yards | under | 0.3207245998457888 | 2026-10-27T05:05:06Z | 2026-11-03T01:15:00Z |
| underdog|41cd46eb-3a8a-4dd5-b1a6-c2b98317813f | underdog | Baker Mayfield | Pass TDs | under | 0.31870442998094306 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|2e93eda3-791e-4fa2-80f0-7e25cd240adc | underdog | Andy Borregales | Kicking Points | under | 0.31509235428704496 | 2026-10-30T05:46:05Z | 2026-11-01T21:25:00Z |
| underdog|39f3f7fc-6c39-444a-897e-8dfbc45427fa | underdog | Sam Darnold | Pass Yards | under | 0.3143741598167539 | 2026-10-27T05:05:06Z | 2026-11-03T01:15:00Z |
| underdog|7010fc48-e8bd-484a-a77d-ed3385b61098 | underdog | Ja'Marr Chase | Receiving Yards | under | 0.31405028667298107 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|34072e00-3750-4675-9357-c57cfd17cc0f | underdog | Jackson Gutierrez | Pass Yards | over | 0.31152667792558986 | 2026-10-30T05:46:05Z | 2026-10-31T16:00:00Z |
| underdog|f061b6f3-ad6b-4386-856f-0b3badbf9989 | underdog | Cam Ward | Pass Attempts | under | 0.3077298561599473 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|cc99b30f-5f59-43ff-b0e2-3e6d5670212b | underdog | Drew Stevens | Kicking Points | under | 0.3045316875544547 | 2026-10-29T05:46:21Z | 2026-11-02T01:20:00Z |
| underdog|4af1d2c4-9389-4932-bdbf-25ba879d7f98 | underdog | Kirk Cousins | Pass Yards | under | 0.3029545016904194 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|9f5cb0c8-1fbf-4866-bd6b-ecb5fe6c0fd9 | underdog | Tanner McKee | Rush Yards | under | 0.3028836980632086 | 2026-10-29T05:46:21Z | 2026-11-02T01:20:00Z |
| prizepicks|16408774 | prizepicks | Kaitlin Quevedo | Aces | under | 0.30247987480655014 | 2026-10-30T05:46:05Z | 2026-10-30T02:10:00.000-04:00 |
| prizepicks|16237060 | prizepicks | Geno Smith | Pass Yards | under | 0.3012472919929988 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|f0925bda-0452-45bf-b5cb-e99abb959340 | underdog | Daniel Jones | Pass Yards | under | 0.30049745428740415 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|7e44dbb6-bebc-4d95-b84b-2172e298f971 | underdog | Drew Stevens | FG Made | under | 0.2989225028687452 | 2026-10-29T05:46:21Z | 2026-11-02T01:20:00Z |
| underdog|036b2b4a-4c13-4a88-98c4-08c2f91b6f5b | underdog | Malik Willis | Pass Attempts | under | 0.2950573943673964 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|688d08a6-db4b-4741-9b64-3f2d4083db4c | underdog | Rhamondre Stevenson | Rush Yards | under | 0.29100110024273373 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|a972f3cc-e6b0-44c0-8669-24337bceb6fb | underdog | Andy Borregales | FG Made | under | 0.2908084829232864 | 2026-10-30T05:46:05Z | 2026-11-01T21:25:00Z |
| prizepicks|16397374 | prizepicks | Dak Prescott | Pass+Rush+Rec TDs | under | 0.2878998776701259 | 2026-10-30T05:46:05Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|3e004d77-31b6-42d3-b335-ec61b9c5ca37 | underdog | Drake Maye | Pass Attempts | under | 0.28783365045991505 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|96197cf8-42ed-46d7-9dc6-75ce2b734496 | underdog | Bhayshul Tuten | Rush Yards | under | 0.2830925953549398 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|54c10fbf-aedf-432a-b4e5-08da3112f990 | underdog | Raleek Brown | Rush Yards | under | 0.28245832792574277 | 2026-10-30T05:46:05Z | 2026-10-31T23:30:00Z |
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
| underdog|171776c8-2cba-4822-af8b-9cccabb0ba30 | underdog | Ja'Kobi Lane | Receiving Yards | under | 0.25079110375599434 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|c6d1047f-d48a-4b4f-94b8-60a6ab509a0d | underdog | Jackson Gutierrez | Pass TDs | over | 0.24950392888425482 | 2026-10-28T05:43:27Z | 2026-10-31T16:00:00Z |
| underdog|8bde0391-ccde-4dfc-9cb2-8ef5c29b490f | underdog | Antonio Williams | Receptions | under | 0.2479315173455695 | 2026-10-29T05:46:21Z | 2026-11-02T01:20:00Z |
| underdog|48811b9c-7e60-4593-a528-2b9034180b39 | underdog | Jake Elliott | FG Made | under | 0.247649803080637 | 2026-10-29T05:46:21Z | 2026-11-02T01:20:00Z |
| underdog|5eaaba0a-f069-47a9-b1b8-7c791844ccd3 | underdog | Geno Smith | Pass Attempts | under | 0.2429302888957946 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| prizepicks|16351052 | prizepicks | Aidan Laughery | Rush Atts | under | 0.2412546735959482 | 2026-10-30T05:46:05Z | 2026-10-31T12:00:00.000-04:00 |
| underdog|2f557637-9041-4541-9fdc-a98aa4979f85 | underdog | Daniel Jones | Pass TDs | under | 0.24111157975554776 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|714c4e03-5b55-4f5c-949c-b056d52f89c5 | underdog | Aaron Rodgers | Pass Attempts | under | 0.23899560341545345 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|b5cab8eb-ac30-4ab2-bf1a-892f0f41a451 | underdog | Trevor Lawrence | Pass Attempts | under | 0.23880589410721487 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|b871d24e-b512-49bf-af0d-87e4256afb83 | underdog | Jared Goff | Pass Attempts | under | 0.23810199295358325 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|1266754d-2b95-4bf3-bc09-fb5b0319ea98 | underdog | Joe Burrow | Pass Attempts | under | 0.23653667794004585 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| underdog|7a3c6b9e-58a0-4566-81c4-e690454cfeb6 | underdog | Joe McFadden | XP Made | over | 0.23621662260627513 | 2026-10-29T05:46:21Z | 2026-10-31T20:15:00Z |
| underdog|0964d4fd-2061-4374-9c1c-0aa1d0d2e8fd | underdog | Jahmyr Gibbs | Receptions | under | 0.23462427954615162 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|3e6bc69a-76fe-4321-9cfa-bb90e9a0289c | underdog | Baker Mayfield | Pass Attempts | under | 0.23349661293905155 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| underdog|2accf469-d7a9-40b3-9fc4-b939f36ffe1d | underdog | Lamar Jackson | Pass TDs | under | 0.2311213220174536 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|d65d9143-733b-46d7-a510-137a908f510e | underdog | Cam Little | FG Made | under | 0.23102908443710635 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| underdog|279fd967-4a9b-4f11-82a9-bd2328494b9e | underdog | Ja'Marr Chase | Receptions | under | 0.2309204690720832 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|a7958068-81fe-40ef-a70d-9dc09a562438 | underdog | Brendan Baird | XP Made | under | 0.22744796592916927 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| prizepicks|16402746 | prizepicks | Jonathan Taylor | Rec Targets | under | 0.22689259146833007 | 2026-10-30T05:46:05Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|28b552af-0b9a-4f7a-8167-90e11dd3b5f6 | underdog | Kyle Pitts | Receiving Yards | under | 0.22471131955490853 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|da179e4a-1fa3-4518-9789-cb524e343dfe | underdog | Jayden Daniels | Pass Attempts | under | 0.22392278838988666 | 2026-10-29T05:46:21Z | 2026-11-02T01:20:00Z |
| underdog|15827bb6-3d10-43fb-942b-bb2057c57b32 | underdog | Quentin Johnston | Receptions | under | 0.22388025176435578 | 2026-10-30T05:46:05Z | 2026-11-01T21:05:00Z |
| underdog|d3529e40-391b-42c2-ada3-d6f7e3d476c0 | underdog | Jaxon Smith-Njigba | Receiving Yards | under | 0.2207891416703074 | 2026-10-27T05:05:06Z | 2026-11-03T01:15:00Z |
| underdog|66738651-7f99-4df0-b9b0-522c7620a839 | underdog | Holden Geriner | Pass TDs | under | 0.22032080131551335 | 2026-10-29T05:46:21Z | 2026-10-31T23:30:00Z |
| underdog|0e4d5ac6-81bf-450d-9497-23a66b4d41f0 | underdog | Jacoby Brissett | Pass Attempts | under | 0.21816784342592277 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|94afae91-7080-4e19-b465-21ee5ba92e1e | underdog | Wan'Dale Robinson | Receiving Yards | under | 0.21730599801522976 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|8fe6381c-70d0-44c4-840e-e579b9212e6b | underdog | Justin Herbert | Pass TDs | under | 0.2167420814479638 | 2026-10-27T05:05:06Z | 2026-11-01T21:05:00Z |
| prizepicks|16316136 | prizepicks | John Bates | Rec Yards | over | 0.2159230700072322 | 2026-10-28T05:43:27Z | 2026-11-01T20:20:00.000-05:00 |
| underdog|dd212962-6dca-4f26-abc7-d169783d01ac | underdog | Kyler Murray | Pass Attempts | under | 0.21576631517107925 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|e5a24c45-43a3-4338-af2a-9140730a85a3 | underdog | Cam Ward | Pass TDs | under | 0.2150615767583154 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|ac161d11-d41f-45d3-bb47-5edf0ea511fd | underdog | Holden Geriner | Pass Yards | under | 0.21453901394549224 | 2026-10-30T05:46:05Z | 2026-10-31T23:30:00Z |
| prizepicks|16238606 | prizepicks | Brock Bowers | Rec Yards | under | 0.2140636967499886 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|57c43912-6db9-4273-8c0b-774840baaffd | underdog | John Mateer | Pass Yards | under | 0.2140390671831961 | 2026-10-30T05:46:05Z | 2026-10-31T20:15:00Z |
| underdog|9d5994b4-d803-4b80-af59-288b8020987e | underdog | Evan McPherson | FG Made | under | 0.21368497936007513 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| underdog|a521534e-bbf6-4dac-abfa-041b66362962 | underdog | Daniel Jones | Pass Attempts | under | 0.21258660675643404 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|6a748d90-5fb9-4ae4-87d9-be1bb9b4eef7 | underdog | Josh Allen | Pass TDs | under | 0.20834299379221988 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|034d7617-ad80-48f4-a6e1-4c37d782f395 | underdog | Matthew Stafford | Pass Yards | under | 0.20696325020402107 | 2026-10-28T05:43:27Z | 2026-11-01T21:05:00Z |
| underdog|19802c00-cb0c-4170-a796-fe441d09a959 | underdog | Jalen Nailor | Receiving Yards | under | 0.20690312892352902 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| underdog|3299abed-a981-4179-881a-08a58e180eee | underdog | Rece Verhoff | XP Made | over | 0.20670284300837638 | 2026-10-28T05:43:27Z | 2026-10-31T23:30:00Z |
| prizepicks|16238594 | prizepicks | Trey McBride | Rec Yards | under | 0.20630682894084595 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|631afbbe-b351-40e2-8a8f-19762138a645 | underdog | Stefon Diggs | Receptions | under | 0.20419601930534237 | 2026-10-29T05:46:21Z | 2026-11-02T01:20:00Z |
| prizepicks|16402339 | prizepicks | Justin Herbert | Pass TDs | under | 0.20234143900444856 | 2026-10-30T05:46:05Z | 2026-11-01T16:05:00.000-05:00 |
| underdog|2f14e9e2-9fa9-4fe6-897b-08dd7fc82bc2 | underdog | Akheem Mesidor | Sacks | over | 0.20192331894179272 | 2026-10-30T05:46:05Z | 2026-11-01T21:05:00Z |
| underdog|dfa79e9f-f0fc-4d49-88c3-22f6bd24d524 | underdog | Ollie Gordon | Receiving Yards | under | 0.20149579334312173 | 2026-10-28T05:43:27Z | 2026-11-01T21:25:00Z |
| prizepicks|16237760 | prizepicks | Rhamondre Stevenson | Rush Yards | under | 0.20003838369682592 | 2026-10-27T05:05:06Z | 2026-11-01T16:25:00.000-05:00 |
| underdog|c62f3f33-cc15-4b35-b432-01caad4bb4de | underdog | Javonte Williams | Rush + Rec Yards | under | 0.199272959384853 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| underdog|53842c9f-1d9a-41da-b48c-abce8bc5f770 | underdog | Aidan Laughery | Rush Yards | under | 0.19902066857867684 | 2026-10-30T05:46:05Z | 2026-10-31T16:00:00Z |
| underdog|8ee5a905-2917-42eb-9a59-992b6d7530e2 | underdog | Jacoby Brissett | Pass TDs | under | 0.19731880187813977 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|d028c6bc-f38a-46d7-8b03-fcb2a9abb87c | underdog | George Pickens | Receiving Yards | under | 0.19725314760148782 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|1bfe643b-e084-40da-a952-bfc8b63db7a4 | underdog | Ladd McConkey | Receiving Yards | under | 0.1966721089474388 | 2026-10-30T05:46:05Z | 2026-11-01T21:05:00Z |
| underdog|549546b5-52c9-4c01-b7f9-c9922a56a689 | underdog | Dru DeShields | Pass TDs | under | 0.19509496145960248 | 2026-10-30T05:46:05Z | 2026-10-31T02:30:00Z |
| underdog|d804b353-6d81-45a9-81d4-4821ccfb1227 | underdog | Carson Hilbert | XP Made | under | 0.1949100968222911 | 2026-10-29T05:46:21Z | 2026-10-31T19:15:00Z |
| underdog|37294e13-0fad-4e6d-9bb0-502d8d20e81d | underdog | Kenny Gainwell | Receiving Yards | under | 0.19226146698041036 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|17353939-73dc-440d-827b-d9413d18d844 | underdog | Dak Prescott | Pass Attempts | under | 0.19093639525880723 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|396fa408-0a5f-4be5-b9a7-b20f30dbd908 | underdog | Parker Washington | Receptions | under | 0.18996406742376704 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16364183 | prizepicks | Drake London | Rec Targets | under | 0.18922823043011128 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|1830ded7-1214-4f85-a1e2-a61b41b0488a | underdog | Cade Otton | Receiving Yards | under | 0.18822705527763905 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| underdog|db7df02f-c054-41a9-aa50-0fd66fb3afa1 | underdog | Amon-Ra St. Brown | Receiving Yards | under | 0.18760906654565868 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|71fafed0-c738-4389-bb62-2f305194764b | underdog | Carson Hansen | Rush Yards | under | 0.18721282127875039 | 2026-10-30T05:46:05Z | 2026-10-31T20:15:00Z |
| underdog|665535ac-210f-4c3c-9efb-de102e073220 | underdog | Daniel Bellinger | Receiving Yards | under | 0.18709530086778547 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|a88da4c3-d490-41a8-b54a-86ce070351ec | underdog | Nolan Bartley | XP Made | over | 0.18701446242147501 | 2026-10-28T05:43:27Z | 2026-10-31T16:00:00Z |
| underdog|654a11cd-6a7c-4368-b150-848fe82d278d | underdog | Kyler Kasper | Receiving Yards | under | 0.1854733472531831 | 2026-10-30T05:46:05Z | 2026-10-31T19:30:00Z |
| underdog|4f609d9d-58a0-47f7-b7e8-b812cc106fb0 | underdog | D'Andre Swift | Rush + Rec Yards | under | 0.18496961586725102 | 2026-10-29T05:46:21Z | 2026-11-03T01:15:00Z |
| underdog|f30e521b-39dc-4e16-8416-ee5e6bad58b9 | underdog | Colston Loveland | Receiving Yards | under | 0.18433645657794384 | 2026-10-28T05:43:27Z | 2026-11-03T01:15:00Z |
| underdog|afa68e3a-abf5-48e3-967b-2750d6d956ab | underdog | Derrick Henry | Rush Yards | under | 0.18337816433194976 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|410eda24-d2b6-440a-b958-aa33d85789c9 | underdog | Rachaad White | Rush + Rec Yards | under | 0.1828101063180283 | 2026-10-29T05:46:21Z | 2026-11-02T01:20:00Z |
| underdog|e75911b6-9cc3-4852-9c95-ea8aebde12fc | underdog | Kirk Cousins | Pass Attempts | under | 0.18259810381735442 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|e62da64a-4678-4964-bd5d-88acd4ec999d | underdog | Brevyn Spann-Ford | Receiving Yards | under | 0.18214542209116402 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|d823d283-051f-48b2-8b96-0aeef065f4d7 | underdog | Drew Mestemaker | Pass Yards | under | 0.1817039306776982 | 2026-10-30T05:46:05Z | 2026-10-31T23:00:00Z |
| underdog|a5571717-a5a9-456e-acd0-34ad286a065d | underdog | Cam Little | Kicking Points | under | 0.1797294561674304 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| underdog|3a83b28e-d200-4f72-b740-bff3d10e07eb | underdog | Chris Godwin | Receptions | under | 0.17933771848483437 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|684c3765-0511-4cc7-9d8a-5be14ac8cd71 | underdog | Germie Bernard | Receiving Yards | under | 0.17801647476795757 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|94cb4524-9308-4fb7-884b-66643c6f0f50 | underdog | Rashee Rice | Receiving Yards | under | 0.17788699074851555 | 2026-10-30T05:46:05Z | 2026-11-01T21:25:00Z |
| underdog|76518c7a-d4dc-4e57-a8ba-023d49539bd2 | underdog | Alberto Mendoza | Pass Yards | under | 0.1776437856297597 | 2026-10-30T05:46:05Z | 2026-10-31T23:30:00Z |
| prizepicks|16270983 | prizepicks | Bo Jackson | Rush Atts | under | 0.1774637831677669 | 2026-10-30T05:46:05Z | 2026-10-31T19:30:00.000-04:00 |
| prizepicks|16397375 | prizepicks | Josh Allen | Pass+Rush+Rec TDs | under | 0.17723965985031953 | 2026-10-30T05:46:05Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|103605f2-9b72-4426-885b-0238715e9ac0 | underdog | Matthew Stafford | Rush Yards | over | 0.17706361202904009 | 2026-10-27T05:05:06Z | 2026-11-01T21:05:00Z |
| underdog|cf672a90-aa86-4cd8-8f8b-dd0d13229542 | underdog | Tyler Warren | Receiving Yards | under | 0.17652993569650421 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16364180 | prizepicks | Ja'Kobi Lane | Rec Targets | under | 0.1763735536367902 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|38e0faee-0c91-422b-974f-d7d80ab6de29 | underdog | Gunnar Helm | Receiving Yards | under | 0.17598595760600988 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|af5c7d85-cb99-4044-9ef5-d2ddc3408b0e | underdog | Malik Washington | Receptions | under | 0.17563895451595535 | 2026-10-29T05:46:21Z | 2026-11-01T21:25:00Z |
| underdog|9303c8b4-2d98-4758-b335-51c9666b2989 | underdog | Ray Davis | Rush Yards | under | 0.1751366077070703 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|a0020a56-eca9-42bc-b548-2457584b7982 | underdog | Parker Washington | Receiving Yards | under | 0.17427174460304196 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|c0f1afab-a440-467e-a5b3-269bee623613 | underdog | Quentin Johnston | Receiving Yards | under | 0.17376903661241794 | 2026-10-30T05:46:05Z | 2026-11-01T21:05:00Z |
| underdog|5b0fbf58-2d38-4bfa-a85d-c5ec591d6220 | underdog | Kyle Pitts | Receptions | under | 0.1729010034408106 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16345984 | prizepicks | Ja'Marr Chase | Rec Targets | under | 0.17261768944514488 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| prizepicks|16238621 | prizepicks | Jaxon Smith-Njigba | Rec Yards | under | 0.17173160672708232 | 2026-10-27T05:05:06Z | 2026-11-02T20:15:00.000-05:00 |
| underdog|1343a522-9c45-4117-98d2-02eb6ca31f2e | underdog | Darian Mensah | Rush Yards | over | 0.17156773564058403 | 2026-10-28T05:43:27Z | 2026-10-31T23:30:00Z |
| underdog|8f8931b0-0f49-46a1-af8a-cf650f624c68 | underdog | Amon-Ra St. Brown | Receptions | under | 0.17005505014758315 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|4b334497-079e-4edb-89d2-f1aab306023d | underdog | Jameson Williams | Receiving Yards | under | 0.17002164741431403 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|7c5d072f-ccf3-471d-b5bf-82f1fb8cf5a0 | underdog | Tait Reynolds | Pass TDs | under | 0.16772614658985985 | 2026-10-29T05:46:21Z | 2026-10-31T23:00:00Z |
| underdog|487af6cb-d6c3-4cb8-9bd1-2b624f598c87 | underdog | Trinidad Chambliss | Pass Yards | under | 0.16767421434568486 | 2026-10-29T05:46:21Z | 2026-10-31T16:45:00Z |
| underdog|58beea02-ce1c-4111-9b19-274c2a209770 | underdog | Michael Wilson | Receiving Yards | under | 0.16679482576786897 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|975e879a-5e2a-4148-8e68-53843d4cf242 | underdog | Brock Bowers | Receptions | under | 0.16633992785137308 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|63f02d88-f21a-4014-b8d8-3067aa9100d3 | underdog | Derrick Henry | Rush + Rec Yards | under | 0.16630730952151507 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|1ea534b5-1087-423c-9c11-aea2e7e65405 | underdog | Tyler Loop | FG Made | under | 0.1646467741587787 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| underdog|046d1ab4-e9e2-440f-a810-ab5cb6366091 | underdog | Keenan Allen | Receiving Yards | under | 0.16422890387887545 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| underdog|6003f2fa-2374-436f-ad95-ade56cf40059 | underdog | Khalil Shakir | Receptions | under | 0.16378974695954318 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|9ba4682e-c401-413f-a65e-94a4720dde1c | underdog | Rhamondre Stevenson | Rush + Rec Yards | under | 0.16367391292288413 | 2026-10-30T05:46:05Z | 2026-11-01T21:25:00Z |
| underdog|d8d25309-128a-4374-999a-2ad2201aa96b | underdog | Breece Hall | Rush + Rec Yards | under | 0.16363073940516593 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|9aee412b-f046-4a7b-917c-207ef0bf657e | underdog | Zay Flowers | Receptions | under | 0.16336849774056705 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| prizepicks|16283156 | prizepicks | Kyler Murray | Fantasy Score | under | 0.16330900700221884 | 2026-10-28T05:43:27Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|2cf26b57-0452-47fb-9a95-cac7cef34370 | underdog | Colby Parkinson | Receiving Yards | under | 0.16302930851970687 | 2026-10-27T05:05:06Z | 2026-11-01T21:05:00Z |
| underdog|4447d011-a159-49e9-a6e9-991cdbbb234a | underdog | Dru DeShields | Pass Yards | under | 0.16181097012541235 | 2026-10-30T05:46:05Z | 2026-10-31T02:30:00Z |
| underdog|8e6927a7-a912-4c9d-a8f8-da4c36100e0f | underdog | Jaylen Wright | Rush + Rec Yards | under | 0.16000000000000003 | 2026-10-29T05:46:21Z | 2026-11-01T21:25:00Z |
| underdog|39bbd93a-c47e-49d9-8688-d284b1bba708 | underdog | Malik Willis | Pass TDs | under | 0.15983936929525455 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| prizepicks|16238595 | prizepicks | Michael Wilson | Rec Yards | under | 0.1584241015647775 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|f98df416-202b-4ab3-beba-521e0540581e | underdog | Billy Edwards Jr. | Pass Yards | under | 0.15837856813656637 | 2026-10-28T05:43:27Z | 2026-10-31T23:30:00Z |
| underdog|480e3448-f74a-4788-95d3-d19b082022eb | underdog | Malachi Toney | Receptions | under | 0.15770821316401618 | 2026-10-30T05:46:05Z | 2026-10-31T23:30:00Z |
| underdog|145d8ff5-2477-453e-a412-e28c5d64621c | underdog | Sam LaPorta | Receiving Yards | under | 0.1576776056199558 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|509d8eb8-b43e-47fd-8fa2-f7cf746a55c1 | underdog | Dak Prescott | Pass TDs | under | 0.15719525295831893 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|45425159-0fc8-4bfc-86e9-d59f986a6a5c | underdog | Brandon Aubrey | FG Made | under | 0.15607322229724607 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| underdog|d69a3693-2cfb-400e-bb85-77d1eb4a6b19 | underdog | Rocco Becht | Pass Yards | under | 0.15490091325185817 | 2026-10-30T05:46:05Z | 2026-10-31T20:15:00Z |
| prizepicks|16283724 | prizepicks | Amon-Ra St. Brown | Rec Targets | under | 0.15422522569585284 | 2026-10-28T05:43:27Z | 2026-11-01T13:00:00.000-05:00 |
| prizepicks|16389063 | prizepicks | AJ Newberry | Rush Atts | under | 0.15373370115690232 | 2026-10-30T05:46:05Z | 2026-10-31T23:00:00.000-04:00 |
| underdog|7abb99f5-32f2-4d61-831c-b654943bda50 | underdog | Drake Lindsey | Pass TDs | over | 0.15181632662462818 | 2026-10-30T05:46:05Z | 2026-10-31T19:30:00Z |
| underdog|301f45d5-2a5a-449b-b397-68ad730d1370 | underdog | Garrett Wilson | Receiving Yards | under | 0.1515587767143275 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|83068603-e006-4ca8-8057-c6e4d2c865fd | underdog | Calais Campbell | Sacks | over | 0.15098618436294584 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| underdog|9566880e-8490-456d-b73a-5984e9ca91ff | underdog | Mark Andrews | Receiving Yards | under | 0.14977065038209925 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|b36420f5-f15b-4a56-89a1-7382ef291a53 | underdog | Lincoln Kienholz | Pass TDs | under | 0.14918083670510207 | 2026-10-29T05:46:21Z | 2026-10-31T19:15:00Z |
| underdog|f9ff6dca-6916-4d44-8c58-756c6bb60455 | underdog | Tre Tucker | Receptions | under | 0.1484779084275395 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|bf3e998b-2c4a-42bb-b8d0-ae92c029a6c3 | underdog | Noah Fifita | Pass Yards | under | 0.1483775242207117 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| underdog|76504010-664b-4a0f-a892-b2ae5aa57b49 | underdog | Jesse Legree | Receptions | under | 0.1478639792128641 | 2026-10-29T05:46:21Z | 2026-11-01T03:00:00Z |
| underdog|c9fcbe6e-efd8-4eaa-9ad2-3ad49380bd62 | underdog | Nick Marsh | Receptions | under | 0.1476174693281791 | 2026-10-29T05:46:21Z | 2026-10-31T19:30:00Z |
| prizepicks|16238597 | prizepicks | Wan'Dale Robinson | Rec Yards | under | 0.1474324804852314 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|d5c2bc10-f8de-48ad-9888-e23da8986a27 | underdog | Gunner Stockton | Pass Yards | under | 0.1470432520894447 | 2026-10-28T05:43:27Z | 2026-10-31T19:30:00Z |
| underdog|880587d5-32c3-4241-94ed-d525daba9240 | underdog | Cameron Dicker | Kicking Points | under | 0.14685401872520443 | 2026-10-30T05:46:05Z | 2026-11-01T21:05:00Z |
| underdog|facf9eef-31fc-49e7-8eb9-f6ee5f12ffff | underdog | Chris Godwin | Receiving Yards | under | 0.14668040701874563 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|08416910-e20b-40a5-b4dd-e2cc4230da8e | underdog | Rashee Rice | Receptions | under | 0.14555417660157777 | 2026-10-30T05:46:05Z | 2026-11-01T21:25:00Z |
| underdog|a5be7003-cabd-440e-9964-d80e3facc58d | underdog | Jacobo Echeverria Lozano | FG Made | over | 0.14524560284009447 | 2026-10-30T05:46:05Z | 2026-10-31T20:15:00Z |
| underdog|56955058-de76-456b-ac8e-8e0ae8753edd | underdog | Jared Goff | Rush Yards | over | 0.14467131524506371 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16364184 | prizepicks | Jahan Dotson | Rec Targets | under | 0.1446232979211045 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|ef8e9fb6-3170-4bc2-a654-18c691ac3b09 | underdog | D'Andre Swift | Rush Yards | under | 0.14431233667100896 | 2026-10-29T05:46:21Z | 2026-11-03T01:15:00Z |
| underdog|aa7e1009-4548-4842-a8ff-64ad27e11221 | underdog | Ja'Kobi Lane | Receptions | under | 0.14398576918830674 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|3f7c2bd3-abfd-4725-b5db-fa8b6bd6aa55 | underdog | Devon Dampier | Pass Yards | under | 0.14368556374377595 | 2026-10-28T05:43:27Z | 2026-10-31T19:45:00Z |
| underdog|36966575-be9c-4110-8913-2c34541405e2 | underdog | Braden Atkinson | Pass Yards | under | 0.1435769662822608 | 2026-10-30T05:46:05Z | 2026-11-01T03:00:00Z |
| underdog|b7414544-5c15-4013-b6ae-37d6fb3cf0b6 | underdog | Antonio Williams | Receiving Yards | under | 0.14297460362734482 | 2026-10-29T05:46:21Z | 2026-11-02T01:20:00Z |
| underdog|69204bc4-ee21-4371-8569-f19bd4cdb2ee | underdog | Aidan Chiles | Pass TDs | over | 0.14248978818221675 | 2026-10-30T05:46:05Z | 2026-10-31T19:30:00Z |
| underdog|8c265679-ba2c-4251-9787-e80bd5c4dcd0 | underdog | Jahan Dotson | Receptions | under | 0.14199975402127674 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| prizepicks|16364222 | prizepicks | Stefon Diggs | Rec Targets | under | 0.14134166445347063 | 2026-10-29T05:46:21Z | 2026-11-01T20:20:00.000-05:00 |
| underdog|59da26a9-80c7-4a40-a23b-3757e949b385 | underdog | Jason Myers | FG Made | under | 0.14119220966516732 | 2026-10-27T05:05:06Z | 2026-11-03T01:15:00Z |
| underdog|994bbaea-5a64-4a42-9cfd-24b0ed8278bc | underdog | Denzel Boston | Receiving Yards | under | 0.13975537513182712 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|36ff0ba4-806f-4c4f-b71b-66f03d6e4721 | underdog | Zay Flowers | Receiving Yards | under | 0.1395259427543014 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|3ad48ee1-8d7d-466e-be99-e10ada3908a3 | underdog | Germie Bernard | Receptions | under | 0.1394253979904757 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|b2e7b5dc-0058-4dcb-ad3c-df98a1c058e3 | underdog | Malik Washington | Receiving Yards | under | 0.13931606450895906 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|6a3e561e-440e-4d25-8bd9-2107c44e44b8 | underdog | Rico Dowdle | Receptions | under | 0.1392082116360751 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| underdog|d45e52c5-341a-4f40-ad46-00461eb42b78 | underdog | Jake Elliott | Kicking Points | under | 0.13897742556141668 | 2026-10-29T05:46:21Z | 2026-11-02T01:20:00Z |
| underdog|ede9d5df-0fd5-4851-8a4e-b9205aad6dc1 | underdog | Nolan Hauser | FG Made | over | 0.1382045276846529 | 2026-10-29T05:46:21Z | 2026-10-31T23:00:00Z |
| underdog|1252ee81-6cb0-4cb2-a848-493edb24b851 | underdog | Dane Pizzaro | XP Made | over | 0.13808985982548394 | 2026-10-30T05:46:05Z | 2026-10-31T16:30:00Z |
| prizepicks|16364185 | prizepicks | Kyle Pitts Sr. | Rec Targets | under | 0.13793260511984728 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|16eae670-fe7a-45ef-95e5-9ba19c960b86 | underdog | Connor Calvert | FG Made | over | 0.13773351523629673 | 2026-10-29T05:46:21Z | 2026-10-31T19:45:00Z |
| underdog|6aafb4ed-173e-4c20-aa50-9b0737004ea2 | underdog | Mason Taylor | Receptions | under | 0.13759993099979895 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|a62f7cce-1ae4-4dc6-a396-62b34f8117c1 | underdog | Ladd McConkey | Receptions | under | 0.13644727976504722 | 2026-10-29T05:46:21Z | 2026-11-01T21:05:00Z |
| underdog|3f9c4476-78f4-4ad8-95a2-5c8764a4d76e | underdog | Trevor Lawrence | Pass TDs | under | 0.136123979306918 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|99ccfe3c-2d1a-4a8b-aeb1-18afbb5f5154 | underdog | DK Metcalf | Receiving Yards | under | 0.13597344274054024 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|1a6cbb69-57e0-49bb-a5b1-c97ef13cb742 | underdog | Jonah Coleman | Rush Yards | under | 0.13593796227260369 | 2026-10-28T05:43:27Z | 2026-11-01T21:25:00Z |
| underdog|8e89428d-9bc2-417e-a764-081d96360e5c | underdog | Keyone Jenkins | Pass Yards | under | 0.13567122151918942 | 2026-10-29T05:46:21Z | 2026-10-30T23:30:00Z |
| underdog|3ea0cc0b-aa69-47aa-80aa-4cc9c7fc22a3 | underdog | Caleb Komolafe | Receiving Yards | over | 0.13515296799579812 | 2026-10-30T05:46:05Z | 2026-10-31T19:30:00Z |
| underdog|af817726-c2ab-48c6-9400-8ea550264077 | underdog | Jayden Maiava | Pass Yards | under | 0.13504168109419978 | 2026-10-28T05:43:27Z | 2026-10-31T23:30:00Z |
| underdog|e7beb609-6a68-4956-9a67-99ef7eb2464f | underdog | Matthew Stafford | Pass Attempts | under | 0.1349833854689143 | 2026-10-29T05:46:21Z | 2026-11-01T21:05:00Z |
| underdog|30df1fbe-6d66-4007-b244-cea0fc5160f2 | underdog | Tyler Goodson | Rush + Rec Yards | under | 0.13481820413141865 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|4672a0de-a836-4b16-a6f6-0b21f98bd10e | underdog | Dawson Knox | Receiving Yards | under | 0.13474038768017405 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|b6b37aba-828b-4b2e-a2c1-ca8d4da057c8 | underdog | Wil Lutz | FG Made | under | 0.13416279453077506 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|1f8f23c6-88c6-4733-888c-ba2326bc988b | underdog | Chig Okonkwo | Receiving Yards | under | 0.13385829108769665 | 2026-10-29T05:46:21Z | 2026-11-02T01:20:00Z |
| underdog|abe5bb36-eded-4179-8a4d-309e349e055f | underdog | Jordan Addison | Receptions | under | 0.1331259361407876 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16237758 | prizepicks | Kyren Williams | Rush Yards | under | 0.13309444803499015 | 2026-10-27T05:05:06Z | 2026-11-01T16:05:00.000-05:00 |
| underdog|1890912d-a6a9-4f13-b90f-b21680002271 | underdog | Max Gilbert | FG Made | over | 0.13307560846424188 | 2026-10-30T05:46:05Z | 2026-10-31T23:45:00Z |
| prizepicks|16364167 | prizepicks | Hunter Henry | Rec Targets | under | 0.1324464875014063 | 2026-10-29T05:46:21Z | 2026-11-01T16:25:00.000-05:00 |
| underdog|5d9f5852-fc2e-417c-944a-8b2a3913277b | underdog | Breece Hall | Rush Yards | under | 0.1323005774569871 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|692b2d71-e462-4af8-a729-3181f592ae38 | underdog | Chris Rodriguez | Rush Yards | under | 0.1314388619504312 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| underdog|4c9eea8b-78fc-4981-96d9-686ced57e5f9 | underdog | Jordan Addison | Receiving Yards | under | 0.13128005851765068 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|5b28838e-a8ec-494c-90d3-da43f6c2b0e9 | underdog | Dierre Hill | Rush Yards | under | 0.13092498490062177 | 2026-10-30T05:46:05Z | 2026-10-31T19:30:00Z |
| underdog|73bf53dc-6bb2-45d1-8ca0-f2843567acf7 | underdog | Davis Allen | Receiving Yards | under | 0.1308943795657651 | 2026-10-29T05:46:21Z | 2026-11-01T21:05:00Z |
| underdog|8e6f5a42-893b-4880-98ce-28c9fed28162 | underdog | Tony Pollard | Rush + Rec Yards | under | 0.13067007445861256 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| underdog|7c5a1102-e6cc-4f4c-af62-ce2bf786b71e | underdog | Chase Brown | Rush Yards | under | 0.13037383587023132 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| underdog|551fc15e-7110-4b04-b038-3b949fc5f581 | underdog | Kanoah Vinesett | FG Made | over | 0.13014575003840156 | 2026-10-28T05:43:27Z | 2026-10-31T16:00:00Z |
| prizepicks|16347548 | prizepicks | Isaiah Sategna III | Recs | under | 0.12961684674885476 | 2026-10-30T05:46:05Z | 2026-10-31T16:15:00.000-04:00 |
| underdog|a0a1cd84-7140-4b79-94bb-c5dc8cffb254 | underdog | Cairo Santos | FG Made | under | 0.12940227002797755 | 2026-10-27T05:05:06Z | 2026-11-03T01:15:00Z |
| underdog|2adcc255-6e68-4788-bc5f-b4edfe5ca07a | underdog | Jonathan Taylor | Receptions | under | 0.1291779235770657 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|998c9e2f-447e-47e9-9a6f-9ded30f89aae | underdog | Justice Hill | Rush + Rec Yards | over | 0.12867881037577428 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|86bae6e8-dec3-4993-9b03-980cc9218653 | underdog | Jared Goff | Pass TDs | under | 0.12848407209017498 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|fb4ba9ce-ed53-41c1-8840-51f8498e1a55 | underdog | Ashton Jeanty | Rush + Rec Yards | under | 0.12826487466341152 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|ab399613-6753-4652-8d47-52136e369736 | underdog | Rocco Becht | Pass TDs | under | 0.1278894922532613 | 2026-10-30T05:46:05Z | 2026-10-31T20:15:00Z |
| underdog|9aff587f-d05a-40bb-9294-0458828098f2 | underdog | Jaron-Keawe Sagapolutele | Pass Yards | under | 0.12783589591675737 | 2026-10-30T05:46:05Z | 2026-10-31T16:00:00Z |
| prizepicks|16283725 | prizepicks | Jahmyr Gibbs | Rec Targets | under | 0.12770261716281617 | 2026-10-28T05:43:27Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|29f07b36-fedc-42ad-b047-67c888876ab7 | underdog | Trace Johnson | Pass Yards | under | 0.1276342732404807 | 2026-10-30T05:46:05Z | 2026-10-30T23:00:00Z |
| underdog|e6a0bf9d-9729-4f08-8f67-4f3f7b703ff9 | underdog | Rico Dowdle | Rush Yards | under | 0.1273193511792693 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| underdog|fede6610-0ae3-461a-a528-c9311a69e416 | underdog | Jakobi Meyers | Receiving Yards | under | 0.1270159615157731 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|ebff5c56-e0b8-4e67-9893-86c9c69072f1 | underdog | Ryan Wingo | Receptions | under | 0.12628744948391923 | 2026-10-30T05:46:05Z | 2026-10-31T23:30:00Z |
| underdog|3dc5fa2a-a302-4955-ab56-0d1ef1d65f9c | underdog | Jonathan Taylor | Rush Yards | under | 0.12612760876308726 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| prizepicks|16364208 | prizepicks | Greg Dulcich | Rec Targets | under | 0.1260559883327872 | 2026-10-29T05:46:21Z | 2026-11-01T16:25:00.000-05:00 |
| underdog|83529b40-ccf1-457b-9ef1-4c0f8dc47451 | underdog | Dylan Raiola | Pass Yards | under | 0.1259078893671226 | 2026-10-30T05:46:05Z | 2026-10-31T19:30:00Z |
| underdog|c175aa40-b6a4-4b90-8ed1-993c3557c0d3 | underdog | Javonte Williams | Rush Yards | under | 0.12576473654626996 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|b295a429-a121-4509-9517-84f4b7c0a5b8 | underdog | Matthew Stafford | Pass TDs | under | 0.12550262949094826 | 2026-10-27T05:05:06Z | 2026-11-01T21:05:00Z |
| underdog|f70b7511-83e7-4d17-9f53-dadd50378e80 | underdog | JC French | Pass TDs | over | 0.1253467378686265 | 2026-10-29T05:46:21Z | 2026-10-31T19:45:00Z |
| underdog|1a5870c8-2bf8-45e9-b218-a22be43cc0a0 | underdog | Deshaun Watson | Pass TDs | under | 0.12431385225063618 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|fd4864a0-5b0a-4779-8a28-6792f60fa96d | underdog | Denzel Boston | Receptions | under | 0.1242957023286192 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|1287e320-0177-49b3-b24f-f5090ea9ef0c | underdog | Khalil Mack | Sacks | over | 0.12370291928537502 | 2026-10-30T05:46:05Z | 2026-11-01T21:05:00Z |
| underdog|b8a0bb75-0647-4f8d-a4f1-0a75e90ac7f4 | underdog | Anthony Colandrea | Pass Yards | under | 0.12335637017113399 | 2026-10-30T05:46:05Z | 2026-11-01T00:00:00Z |
| underdog|8cdb77cd-3925-4ee5-beb4-812a75583348 | underdog | Colby Parkinson | Receptions | under | 0.12334116882740842 | 2026-10-27T05:05:06Z | 2026-11-01T21:05:00Z |
| underdog|45ea7118-b8a7-4adb-90c6-d487299eacee | underdog | Carnell Tate | Receiving Yards | under | 0.12300903492048088 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|d76f6c73-df6d-480d-8ef1-5f4d9106de12 | underdog | Darnell Washington | Receptions | under | 0.12287634689571902 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|8814de67-b3fc-4dea-824c-84e1c36b6a07 | underdog | Jayden Daniels | Pass TDs | under | 0.12282845018311095 | 2026-10-29T05:46:21Z | 2026-11-02T01:20:00Z |
| underdog|2b7e72b5-e503-4272-8f85-2766fdb25eec | underdog | Bijan Robinson | Receptions | under | 0.12266143699231591 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|7c07455a-f277-48cd-ad69-7b2adac84d3e | underdog | Jake Bates | FG Made | under | 0.1226061500869009 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|1feb3eee-c29e-4b88-9571-6cdadadb7554 | underdog | Jordan Shipp | Receiving Yards | under | 0.12238215278329878 | 2026-10-29T05:46:21Z | 2026-10-31T23:30:00Z |
| underdog|197eec9f-4d07-4f19-8228-d62d67b609d1 | underdog | Tyler Higbee | Receptions | under | 0.12238209731011584 | 2026-10-30T05:46:05Z | 2026-11-01T21:05:00Z |
| underdog|78d27b11-b46f-49a5-b123-946d3ec967af | underdog | Jaylen Raynor | Pass Yards | under | 0.12214201156896531 | 2026-10-30T05:46:05Z | 2026-10-31T23:00:00Z |
| prizepicks|16399007 | prizepicks | Tommy Paul | Total Games Won | over | 0.12207530815445433 | 2026-10-30T05:46:05Z | 2026-10-30T10:00:00.000-04:00 |
| underdog|cf3f87f9-0fe4-478d-b7bf-b213f8709c04 | underdog | James Cook | Rush + Rec Yards | under | 0.12131404815287872 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16364220 | prizepicks | Chris Godwin Jr. | Rec Targets | under | 0.12099460436306475 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|9f00ab98-d69e-4fd1-b6cc-9a45b7ede50e | underdog | Jonah Coleman | Rush + Rec Yards | under | 0.12079711394415726 | 2026-10-30T05:46:05Z | 2026-11-01T21:25:00Z |
| underdog|3d64f587-37b5-4075-b4ed-d119e585f6d7 | underdog | Nick Folk | Kicking Points | under | 0.12062606085130745 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|9d9ea5f8-24c7-482e-b5c0-01769b89c6c8 | underdog | Garrett Wilson | Receptions | under | 0.12062398862594181 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| underdog|b60c1647-75fe-4f90-88a6-fbb03c468183 | underdog | Drake London | Receptions | under | 0.1204218989390401 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|a919c0b3-6f16-44b0-8f1b-8b67af55e957 | underdog | Dylan Edwards | Rush Yards | under | 0.12040322877087684 | 2026-10-30T05:46:05Z | 2026-10-31T19:30:00Z |
| underdog|dce9eee8-4de5-4b77-b9ae-2c11da3cc8e3 | underdog | Emmett Johnson | Receiving Yards | over | 0.12033387832991782 | 2026-10-30T05:46:05Z | 2026-11-01T21:25:00Z |
| underdog|e5f79e7b-ca75-4a07-91c2-245911819dcb | underdog | Savion Hiter | Rush Yards | under | 0.12005951430093897 | 2026-10-30T05:46:05Z | 2026-10-31T16:30:00Z |
| underdog|1c819672-96ce-48b5-881b-75c45f1e0c6e | underdog | George Pickens | Receptions | under | 0.12005816443311146 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|868554ef-8215-4c66-b388-a4a2f7bffc1e | underdog | Dylan Sampson | Receiving Yards | under | 0.11950762310259633 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| underdog|1d457002-604b-429e-a411-f769176f22e3 | underdog | Mark Fletcher Jr. | Rush Yards | under | 0.11932651297467567 | 2026-10-28T05:43:27Z | 2026-10-31T23:30:00Z |
| underdog|a1bdb7e2-1c88-4f25-871e-3452559ed894 | underdog | Brevyn Spann-Ford | Receptions | under | 0.11929367596121321 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|52da651b-1f42-4e2e-897c-7ec37d07aeb2 | underdog | Arch Manning | Pass Yards | under | 0.11898645108028916 | 2026-10-30T05:46:05Z | 2026-10-31T23:30:00Z |
| underdog|235c8fc8-c25a-473e-b395-37edfa2b6352 | underdog | Baker Mayfield | Rush Yards | under | 0.1187368758684273 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| underdog|53b36529-01ce-46e2-9f74-7491367f6857 | underdog | Jalen Nailor | Receptions | under | 0.118498069886117 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| prizepicks|16364178 | prizepicks | Mark Andrews | Rec Targets | under | 0.1177866033639029 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|84edf509-ff27-483d-b4f7-db4873957d66 | underdog | Lamar Jackson | Rush Yards | under | 0.11750214210193122 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|382c9732-657e-4c92-a816-f5b262c2b044 | underdog | Charlie Kolar | Receiving Yards | under | 0.11734751150619038 | 2026-10-30T05:46:05Z | 2026-11-01T21:05:00Z |
| underdog|a8d65e72-cdf2-46c9-ad06-25735b026521 | underdog | Sam Darnold | Pass Attempts | under | 0.1167625142367642 | 2026-10-27T05:05:06Z | 2026-11-03T01:15:00Z |
| underdog|d71cdbfc-2e24-4347-8c79-b1148453d908 | underdog | Travis Kelce | Receptions | under | 0.11657078263704113 | 2026-10-29T05:46:21Z | 2026-11-01T21:25:00Z |
| underdog|cb84333c-b246-4493-acec-acedce99822c | underdog | Caleb Williams | Pass TDs | under | 0.11529745995363427 | 2026-10-27T05:05:06Z | 2026-11-03T01:15:00Z |
| underdog|40e1e8b9-936e-4e15-97c8-77ac12b78573 | underdog | Wil Lutz | Kicking Points | under | 0.11496311756471889 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|96102eeb-882d-48d6-bd89-01c3dc48fdc3 | underdog | Jayden Maiava | Pass TDs | over | 0.11429795145707633 | 2026-10-28T05:43:27Z | 2026-10-31T23:30:00Z |
| underdog|0a0cc866-1e0c-4275-bdf7-8630e285c53d | underdog | Jordan Shipp | Receptions | under | 0.1142339755203059 | 2026-10-30T05:46:05Z | 2026-10-31T23:30:00Z |
| underdog|9307155f-3a4c-4ca6-828c-9545c446e309 | underdog | Deshaun Watson | Rush Yards | under | 0.11406987180102945 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|5d5e0ace-ca19-427d-b5ab-a6582a3c596b | underdog | Nolan James | Rush Yards | under | 0.11400689294997857 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| underdog|b7d6662c-6b16-43a0-9c59-996b95142c12 | underdog | Bo Nix | Pass TDs | under | 0.11391526566253873 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|668a4a02-2699-4b23-a66f-b4d78c0ca876 | underdog | Nick Folk | FG Made | under | 0.11296010544794233 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|ff47be59-65fc-4501-a031-5f9897d4023d | underdog | Jason Myers | Kicking Points | under | 0.11198716898739403 | 2026-10-28T05:43:27Z | 2026-11-03T01:15:00Z |
| underdog|39472ed8-bfcc-425b-a36b-4d7c794e141b | underdog | Byrum Brown | Pass TDs | over | 0.11110702198246591 | 2026-10-29T05:46:21Z | 2026-10-31T16:45:00Z |
| underdog|a76e2c22-fc99-4f26-b305-5156349b714d | underdog | Adonai Mitchell | Receiving Yards | under | 0.11108671220946464 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|3be7845f-da03-44cb-b76c-97e05e6c16cd | underdog | Emmett Johnson | Rush + Rec Yards | over | 0.11108538469969459 | 2026-10-30T05:46:05Z | 2026-11-01T21:25:00Z |
| underdog|d288a2db-0aab-4a8e-882a-4cd19ae79957 | underdog | Brendan Baird | FG Made | under | 0.11103855908681337 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| prizepicks|16414680 | prizepicks | Francesca Jones | Break Points Won | under | 0.11078305761547302 | 2026-10-30T05:46:05Z | 2026-10-30T12:10:00.000-04:00 |
| underdog|d51a68c2-cf19-48ff-a51e-735652c9b1df | underdog | Kyren Williams | Rush Yards | under | 0.10985813254569032 | 2026-10-30T05:46:05Z | 2026-11-01T21:05:00Z |
| underdog|7e328141-5382-4550-b0dd-526277f19f6e | underdog | Antonio Chadha | FG Made | over | 0.10984663601068051 | 2026-10-29T05:46:21Z | 2026-10-31T23:30:00Z |
| underdog|b01487c9-91b2-49c2-8b60-ff32310be97f | underdog | Tyler Higbee | Receiving Yards | under | 0.1097008860634413 | 2026-10-30T05:46:05Z | 2026-11-01T21:05:00Z |
| underdog|71cabcd9-76ca-4ac5-b58e-99339093aac0 | underdog | CJ Bailey | Pass TDs | under | 0.10947916617194009 | 2026-10-30T05:46:05Z | 2026-10-31T16:00:00Z |
| underdog|5415d33b-e592-48da-9aa0-5ae5947a08a6 | underdog | Jonathan Taylor | Rush + Rec Yards | under | 0.10943203734227247 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| prizepicks|16352272 | prizepicks | Dru DeShields | Pass Comp | under | 0.10918859291400151 | 2026-10-30T05:46:05Z | 2026-10-30T22:30:00.000-04:00 |
| underdog|eb4c2d14-178e-431f-801d-2f408a5d44dd | underdog | Kenny Gainwell | Receptions | under | 0.1091654247547108 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|b3393ebe-5c4b-4a04-9593-c31d96dc31db | underdog | Tony Pollard | Receiving Yards | under | 0.10868184811978632 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| prizepicks|16272123 | prizepicks | Drake London | Recs | under | 0.10857932543800086 | 2026-10-30T05:46:05Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|f05afc00-4a03-4d4f-8692-b5f2c8f8b0e3 | underdog | Brandon Aubrey | Kicking Points | under | 0.10784001741173144 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| underdog|8364c775-9927-445d-be06-74249e64f712 | underdog | Nnamdi Madubuike | Sacks | under | 0.10780551503385549 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| underdog|bbcd3a9e-bf46-4334-aeb3-cdd428a2aa87 | underdog | Max Gilbert | XP Made | over | 0.10718978416340291 | 2026-10-30T05:46:05Z | 2026-10-31T23:45:00Z |
| underdog|06a4a710-6458-43df-ba8f-a036706974c4 | underdog | Jaden Craig | Pass Yards | under | 0.1071761192045757 | 2026-10-30T05:46:05Z | 2026-10-31T19:30:00Z |
| underdog|3efdb3f2-4b15-4713-bf57-daa7e4d301a3 | underdog | Bucky Irving | Rush Yards | under | 0.10696383842535351 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|b62f039b-0f9b-4cd6-9e9f-e9783c470857 | underdog | Ollie Gordon | Rush + Rec Yards | under | 0.10625843356924969 | 2026-10-28T05:43:27Z | 2026-11-01T21:25:00Z |
| underdog|182ee136-96d6-4d81-bfe6-e1a26c6e772f | underdog | Jahmyr Gibbs | Rush + Rec Yards | under | 0.10607821147759788 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|d8e86dbd-b81c-4f69-a7ee-a5f68ef0926b | underdog | Travis Kelce | Receiving Yards | under | 0.10548155468571763 | 2026-10-29T05:46:21Z | 2026-11-01T21:25:00Z |
| underdog|3d1d6047-acac-47b2-a581-0b04d6d6af41 | underdog | Jahmyr Gibbs | Receiving Yards | under | 0.10531923406206589 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16238617 | prizepicks | Chig Okonkwo | Rec Yards | under | 0.1051404094349585 | 2026-10-27T05:05:06Z | 2026-11-01T20:20:00.000-05:00 |
| underdog|3f22f66a-41b9-480a-b6ab-5a45545197f6 | underdog | Pat Freiermuth | Receiving Yards | under | 0.10495785987094197 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|52153e62-3c40-4a3a-8e5d-2d6b3a11d1e2 | underdog | Ezekiel Avit | Receptions | under | 0.1046184272727968 | 2026-10-30T05:46:05Z | 2026-11-01T03:00:00Z |
| underdog|c50769bd-316a-45db-80cc-9539cf17da54 | underdog | Dohnte Meyers | Receptions | under | 0.10460151770038284 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|70c7a07b-fba3-43c1-83ba-7905926fef67 | underdog | Jayden Mandal | Pass Yards | under | 0.10433928305204221 | 2026-10-29T05:46:21Z | 2026-11-01T03:00:00Z |
| underdog|b3a0a70e-deb2-431c-ba76-e51c54c8ae54 | underdog | Tommy Carr | Pass TDs | under | 0.10424275021194063 | 2026-10-30T05:46:05Z | 2026-10-31T16:30:00Z |
| underdog|9c49082a-6082-48bd-a624-5fb9a4843e9d | underdog | Bhayshul Tuten | Receptions | under | 0.10402814965460072 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|b99e96ea-5ec2-4c4e-a95e-abcf30e876f2 | underdog | Quinshon Judkins | Rush Yards | under | 0.1037066913938336 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|9f0f4774-c8ae-4fca-86b3-7e8949f6bded | underdog | Kirk Cousins | Rush Yards | over | 0.10334335183039561 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|7ca72607-5f5c-45be-becf-726a9827d1f1 | underdog | Ethan Moczulski | FG Made | over | 0.10328978596060573 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| underdog|35b2d5a2-c766-4bbf-bed6-1c678f5cead2 | underdog | Mark Andrews | Receptions | under | 0.10321357999549285 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|137e2104-c54e-41e9-800b-00dd98ceacaf | underdog | Elic Ayomanor | Receptions | under | 0.10297226753174415 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|c0598871-0e46-45cb-a292-b08201065429 | underdog | Hank Brown | Pass Yards | under | 0.10282986712856834 | 2026-10-30T05:46:05Z | 2026-10-31T16:00:00Z |
| underdog|59905fd2-4d5c-4646-a528-93b6094e86bb | underdog | Jaxon Smith-Njigba | Receptions | under | 0.10234847580734763 | 2026-10-27T05:05:06Z | 2026-11-03T01:15:00Z |
| underdog|6a8df612-85c8-48c6-9495-ad384554b4e5 | underdog | Rece Verhoff | FG Made | under | 0.10231534646673801 | 2026-10-29T05:46:21Z | 2026-10-31T23:30:00Z |
| underdog|69633668-600e-45d5-9f40-8c2dc88d92a7 | underdog | Greg Dulcich | Receptions | under | 0.10220882757054206 | 2026-10-29T05:46:21Z | 2026-11-01T21:25:00Z |
| prizepicks|16344699 | prizepicks | Connor Heyward | Rush+Rec Yds | over | 0.10154012747091701 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|dba955cf-89ee-43b5-ad32-57eccdde7426 | underdog | Rome Odunze | Receiving Yards | under | 0.10135838550360621 | 2026-10-28T05:43:27Z | 2026-11-03T01:15:00Z |
| underdog|a4f90109-232f-4dd5-83b1-359e0555887e | underdog | Bear Bachmeier | Pass Yards | under | 0.10074287452487363 | 2026-10-29T05:46:21Z | 2026-10-31T19:30:00Z |
| underdog|c2a40e0b-c299-4609-bb2a-f82e0e98ec53 | underdog | Kendrick Raphael | Rush Yards | under | 0.09978120029490634 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| prizepicks|16364206 | prizepicks | Caleb Douglas | Rec Targets | under | 0.0996362260043121 | 2026-10-29T05:46:21Z | 2026-11-01T16:25:00.000-05:00 |
| underdog|f7f80b3b-52f5-4cdd-8a54-58bda6446c0a | underdog | Tait Reynolds | Pass Yards | under | 0.09947450960567161 | 2026-10-29T05:46:21Z | 2026-10-31T23:00:00Z |
| underdog|105d8407-4e6c-46f1-a211-6c4c6ce595cc | underdog | Devon Dampier | Rush Yards | under | 0.09932108598689937 | 2026-10-30T05:46:05Z | 2026-10-31T19:45:00Z |
| underdog|bf1470be-563b-42d9-8a74-2acc5a6ec09e | underdog | Wan'Dale Robinson | Receptions | under | 0.09927862778998076 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|b56d5ed0-60ba-41a0-b75a-ebe65699a89f | underdog | Keenan Allen | Receptions | under | 0.09922585316086519 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| underdog|d6d8f19d-e78e-4df1-8240-469070b06ea3 | underdog | Emeka Egbuka | Receptions | under | 0.09907031765655117 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| prizepicks|16249073 | prizepicks | Jesse Legree | Recs | under | 0.09819846081803829 | 2026-10-28T05:43:27Z | 2026-10-31T23:00:00.000-04:00 |
| underdog|76b5aa06-8807-4e89-85c0-c0c44906ccba | underdog | Caleb Hawkins | Rush Yards | under | 0.09753569878992885 | 2026-10-30T05:46:05Z | 2026-10-31T23:00:00Z |
| underdog|92104ca3-c72f-4130-a984-6a172a0ccbc8 | underdog | Deone Walker | Sacks | over | 0.09744195523504662 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| underdog|a05e4b72-b938-48e3-ab9b-f27a9e585232 | underdog | KJ Jackson | Pass TDs | under | 0.09731975952553418 | 2026-10-30T05:46:05Z | 2026-10-31T23:45:00Z |
| prizepicks|16364209 | prizepicks | Malik Washington | Rec Targets | under | 0.09706503307304815 | 2026-10-29T05:46:21Z | 2026-11-01T16:25:00.000-05:00 |
| underdog|9e1d3567-3f8f-4d49-b463-e39fb8dfe8eb | underdog | Harrison Butker | FG Made | under | 0.09638494838462963 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|dc401604-435d-4ccd-929e-0824b3d3fe33 | underdog | Tyler Loop | Kicking Points | under | 0.09614829307553385 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| underdog|ab4e51ec-c1b4-4eab-95db-5dc65960c1d0 | underdog | Kyren Williams | Rush + Rec Yards | under | 0.0956441431882935 | 2026-10-27T05:05:06Z | 2026-11-01T21:05:00Z |
| underdog|0ae2b107-e8a1-4f19-9af0-6abe299e4671 | underdog | CeeDee Lamb | Receiving Yards | under | 0.09554776768839468 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|5998434f-948d-4ce6-a07a-c8ea7f5d1c65 | underdog | Jaylen Warren | Receiving Yards | over | 0.09533361799515139 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16364223 | prizepicks | Chig Okonkwo | Rec Targets | under | 0.09483291694542273 | 2026-10-29T05:46:21Z | 2026-11-01T20:20:00.000-05:00 |
| underdog|223193e3-6ce7-477b-b905-e8f6d82bac72 | underdog | Malik Washington | Pass Yards | under | 0.09472666328192059 | 2026-10-30T05:46:05Z | 2026-10-31T16:00:00Z |
| underdog|1c6ce00d-0aa3-40f6-a491-fc85e8b2bde3 | underdog | CJ Bailey | Pass Yards | under | 0.09433327949890413 | 2026-10-30T05:46:05Z | 2026-10-31T16:00:00Z |
| underdog|e10b87ae-c6a6-4551-bb87-d585e77e9965 | underdog | Brian Thomas | Receptions | over | 0.09404550627475516 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|72447f28-a5ca-42bb-9be7-031e0f4620c2 | underdog | Joe McFadden | FG Made | under | 0.09390907363785272 | 2026-10-29T05:46:21Z | 2026-10-31T20:15:00Z |
| underdog|d17ab225-e529-4428-a9aa-ea656ecb35e5 | underdog | Tyler Robles | XP Made | over | 0.0937394398844259 | 2026-10-29T05:46:21Z | 2026-11-01T00:00:00Z |
| underdog|6207f1a3-38b0-4a82-bcbc-e8c63e0a7181 | underdog | TreVeyon Henderson | Receiving Yards | over | 0.09364324694734338 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| prizepicks|16402341 | prizepicks | Bo Nix | Pass TDs | under | 0.09346583106389361 | 2026-10-30T05:46:05Z | 2026-11-01T16:25:00.000-05:00 |
| underdog|d9dc7ba2-a251-4962-8c61-3e0c7834b8a8 | underdog | Xavier Worthy | Receiving Yards | under | 0.09325701746823656 | 2026-10-30T05:46:05Z | 2026-11-01T21:25:00Z |
| underdog|c029fdf4-7e5d-46dc-a036-35090710b7c2 | underdog | Noah Gray | Receptions | under | 0.09316272997174746 | 2026-10-30T05:46:05Z | 2026-11-01T21:25:00Z |
| underdog|a7c11a4c-519b-4ffe-8595-86ffd84f2d9d | underdog | TreVeyon Henderson | Receptions | under | 0.09305154250073311 | 2026-10-29T05:46:21Z | 2026-11-01T21:25:00Z |
| underdog|4e50ec4a-dc6c-4856-a0b5-b6d28d2cfee4 | underdog | Jakobi Meyers | Receptions | under | 0.09288375907862756 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|b22a6f88-4281-4cb7-9112-901cbb528b99 | underdog | Will Bettridge | FG Made | under | 0.0928484830083991 | 2026-10-29T05:46:21Z | 2026-10-31T19:45:00Z |
| underdog|b9fd522c-e790-46b8-b35b-88e54e06e1ed | underdog | Hunter Henry | Receiving Yards | under | 0.09271224325362548 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|61a5de04-06b8-46e3-8ae4-8af1690f6227 | underdog | Will Stone | FG Made | under | 0.09268440319370341 | 2026-10-28T05:43:27Z | 2026-10-30T23:30:00Z |
| underdog|c05032a7-2043-4657-8d3f-b6bb70553a2b | underdog | Legend Glasker | Receptions | under | 0.0925166652282855 | 2026-10-30T05:46:05Z | 2026-10-31T19:30:00Z |
| underdog|ed29d33f-b4cd-4c85-95e3-61ba3606a315 | underdog | Darian Mensah | Pass Yards | under | 0.0918747633899134 | 2026-10-28T05:43:27Z | 2026-10-31T23:30:00Z |
| underdog|32141e2b-baf9-4032-b5f0-32fc2265c1c3 | underdog | Noah Jennings | Receiving Yards | over | 0.09180485638454461 | 2026-10-29T05:46:21Z | 2026-10-31T19:30:00Z |
| underdog|d8053318-9e77-41f4-a87c-da664ca47279 | underdog | James Cook | Rush Yards | under | 0.09180295647498382 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|9a46a485-3da9-4f86-8955-c9b5de57d559 | underdog | Evan McPherson | Kicking Points | under | 0.09179779856180803 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| prizepicks|16364191 | prizepicks | KC Concepcion Jr. | Rec Targets | under | 0.09171087847629222 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| prizepicks|16352536 | prizepicks | Ashton Daniels | Pass Attempts | under | 0.09138425718851007 | 2026-10-29T05:46:21Z | 2026-10-31T19:00:00.000-04:00 |
| underdog|ef0f3c3c-48ff-482a-a3bf-4e4a444d4d0c | underdog | Jauan Jennings | Receptions | under | 0.09119904435326343 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16346147 | prizepicks | Carnell Tate | Rec Targets | under | 0.09109040404588509 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|177547b5-94a6-4d78-91a9-2199205a3905 | underdog | Khalil Shakir | Receiving Yards | under | 0.0909398055872559 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|1c9849b9-498b-4812-a326-0b21293c7620 | underdog | Bradley Chubb | Sacks | over | 0.09044365561197065 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| underdog|489a27f6-b223-4f4e-ac5a-5842df306940 | underdog | Tyler Goodson | Rush Yards | under | 0.09036048124885299 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|55fd36c1-44eb-4a41-9840-cc6e130d6018 | underdog | Wayne Harris | Receiving Yards | under | 0.09032867137881329 | 2026-10-30T05:46:05Z | 2026-10-31T02:30:00Z |
| underdog|412561be-c077-41b5-ad1f-cbccfa5800d2 | underdog | Jaylen Warren | Receptions | under | 0.09013968720518872 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| prizepicks|16300984 | prizepicks | Rome Odunze | Rec Targets | under | 0.09000083847025231 | 2026-10-28T05:43:27Z | 2026-11-02T20:15:00.000-05:00 |
| prizepicks|16238614 | prizepicks | Hunter Henry | Rec Yards | under | 0.08957307565733919 | 2026-10-27T05:05:06Z | 2026-11-01T16:25:00.000-05:00 |
| underdog|c0199a09-88d6-41bd-a286-a771e0428d9e | underdog | Luther Burden | Receiving Yards | under | 0.0891800401053029 | 2026-10-28T05:43:27Z | 2026-11-03T01:15:00Z |
| underdog|13846bc7-88af-4fcd-a779-ff4cc952913a | underdog | Dane Pizzaro | FG Made | under | 0.08871500576729063 | 2026-10-30T05:46:05Z | 2026-10-31T16:30:00Z |
| prizepicks|16414645 | prizepicks | Nicolas Kristof | Goalie Fantasy Score | under | 0.08853974278881471 | 2026-10-30T05:46:05Z | 2026-10-30T15:30:00.000-04:00 |
| prizepicks|16284250 | prizepicks | Jordan Addison | Rec Targets | under | 0.08846730165489147 | 2026-10-28T05:43:27Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|b9df65cc-b761-4559-a23d-251a85407bdc | underdog | Kendrick Bourne | Receiving Yards | under | 0.08801198338315153 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|89bf8626-6b97-4a03-a269-6d447eed5ea7 | underdog | Pat Freiermuth | Receptions | under | 0.08793132623164612 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|9368aed3-4724-4cf4-b2b2-be4450c012a0 | underdog | Justice Hill | Receptions | under | 0.08757492719763116 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|761a7056-48b7-4ff1-9fe8-28d951711ce5 | underdog | Kyle Williams | Receiving Yards | under | 0.08737770695349356 | 2026-10-30T05:46:05Z | 2026-11-01T21:25:00Z |
| underdog|3f930467-8a52-4789-9773-32d7aae9ef2a | underdog | Breece Hall | Receptions | under | 0.08717951934279633 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| underdog|dddbc903-2c87-42d2-bf02-333cee694469 | underdog | Jason Sanders | FG Made | under | 0.08716403013921992 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16364213 | prizepicks | Omar Cooper Jr. | Rec Targets | under | 0.08710714459591429 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|ccfdb87b-471b-414b-8ba7-0b9c179dcf09 | underdog | Jacobo Echeverria Lozano | XP Made | over | 0.08688210812533287 | 2026-10-30T05:46:05Z | 2026-10-31T20:15:00Z |
| underdog|dd854f60-738f-4bb6-805b-dc73c82b60c5 | underdog | Mike Green | Sacks | over | 0.08668149788413282 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| underdog|f2c69c86-fa80-4b67-a398-58825285244c | underdog | Jake Ferguson | Receptions | under | 0.08623693827268275 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|cc091e15-6bc3-40aa-a886-17453738b517 | underdog | Sean O'Haire | FG Made | over | 0.08607263612268956 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| underdog|c094618b-d9f7-4fdf-806e-add690a369a1 | underdog | DeMario Douglas | Receptions | under | 0.08587440528378754 | 2026-10-29T05:46:21Z | 2026-11-01T21:25:00Z |
| underdog|a57bf8a6-36db-4e69-be1f-971f6a09a619 | underdog | Caleb Douglas | Receptions | under | 0.08550150897075826 | 2026-10-29T05:46:21Z | 2026-11-01T21:25:00Z |
| prizepicks|16364200 | prizepicks | Travis Kelce | Rec Targets | under | 0.08541097265923969 | 2026-10-29T05:46:21Z | 2026-11-01T16:25:00.000-05:00 |
| underdog|ce0094b8-608a-4f57-8db8-91acfa4ebf67 | underdog | D'Andre Swift | Receptions | under | 0.08536310216644005 | 2026-10-29T05:46:21Z | 2026-11-03T01:15:00Z |
| underdog|1497d69e-8103-40c3-b01e-1dd71bcad55e | underdog | Gavin Freeman | Receiving Yards | under | 0.08513651550396206 | 2026-10-30T05:46:05Z | 2026-10-30T23:30:00Z |
| underdog|00fa635b-a085-487f-969e-9364f8522ac4 | underdog | Andre Szmyt | FG Made | under | 0.08496316251445146 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|f0e7b026-20f3-4734-bde6-a27d613292ca | underdog | Eli Raridon | Receptions | under | 0.08461052536501124 | 2026-10-30T05:46:05Z | 2026-11-01T21:25:00Z |
| underdog|0247c7be-a564-4aa3-a694-6199240b618c | underdog | Hunter Henry | Receptions | under | 0.08384245014413438 | 2026-10-29T05:46:21Z | 2026-11-01T21:25:00Z |
| prizepicks|16397378 | prizepicks | Caleb Williams | Pass+Rush+Rec TDs | under | 0.08370139667072873 | 2026-10-30T05:46:05Z | 2026-11-02T20:15:00.000-05:00 |
| prizepicks|16364170 | prizepicks | DJ Moore | Rec Targets | under | 0.0836818295883065 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|edc65d80-633a-49d5-b568-467b9dc26c82 | underdog | Chris Rodriguez | Rush + Rec Yards | under | 0.08351399754029376 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|1de4b590-c9a8-4590-ada7-552bf50550c5 | underdog | Ollie Gordon | Rush Yards | under | 0.08331726721322741 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|329814f9-a9e2-4cca-97a5-37a6a9d98a3d | underdog | Greg Dulcich | Receiving Yards | under | 0.08331303954427971 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|eaa25ed0-e5d7-4624-8e8a-365bff379b84 | underdog | DeJuan Williams | Rush Yards | under | 0.08326092363828907 | 2026-10-30T05:46:05Z | 2026-10-31T16:00:00Z |
| underdog|9bf96da1-b640-416c-9d74-efbdc0a699f1 | underdog | Byrum Brown | Pass Yards | under | 0.08325122002724061 | 2026-10-29T05:46:21Z | 2026-10-31T16:45:00Z |
| underdog|cc8cfbb1-e058-4e01-aaa4-4a08f7cd9394 | underdog | Aaron Rodgers | Rush Yards | over | 0.08323621946349369 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|16ee5833-fd42-4e71-b971-e39932752a8b | underdog | TreVeyon Henderson | Rush Yards | under | 0.08316140798485938 | 2026-10-29T05:46:21Z | 2026-11-01T21:25:00Z |
| underdog|f5fb0096-59fa-4789-a394-7e24fc7af77c | underdog | Dylan Sampson | Rush Yards | under | 0.08309472817308283 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| underdog|c124caa4-7f08-4fa3-b0a7-647244cf531a | underdog | Harrison Butker | Kicking Points | under | 0.08302378472777494 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|c75e0dd3-62c9-4e7d-9000-09a60033a0f1 | underdog | Cade Otton | Receptions | under | 0.08248886329987637 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| underdog|390c24f1-9c5b-46f7-a624-c955bdc8a4ea | underdog | Michael Salgado-Medina | FG Made | under | 0.08238079086671868 | 2026-10-28T05:43:27Z | 2026-10-31T16:00:00Z |
| underdog|3a30cff4-d8ec-4ab9-8f65-8bbc2beee55c | underdog | Dylan Sampson | Receptions | under | 0.08223274785027812 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| prizepicks|16237753 | prizepicks | Derrick Henry | Rush Yards | under | 0.08183379413197434 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|e3f2d3d4-40fc-41c4-a46f-fb13d7c0b757 | underdog | Geno Smith | Pass TDs | under | 0.0817951993038919 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|c4834b91-d688-4ab8-8927-69031c8efbc4 | underdog | Deuce Alexander | Receiving Yards | under | 0.08169099115486911 | 2026-10-29T05:46:21Z | 2026-10-31T16:45:00Z |
| prizepicks|16237756 | prizepicks | Ashton Jeanty | Rush Yards | under | 0.0816051738093021 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|ce1fe404-32bc-42d9-9b49-cab4bf747245 | underdog | Daniel Jones | Rush Yards | under | 0.08156509285685742 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|06d12339-a07f-421f-9db1-b57631721f57 | underdog | Noah Fifita | Pass TDs | over | 0.0809828208650083 | 2026-10-28T05:43:27Z | 2026-10-31T16:00:00Z |
| underdog|68246aad-20fd-405d-80db-3ad12ff7a40b | underdog | Kenyon Sadiq | Receptions | under | 0.0809538714276471 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|7b607118-d03a-475d-958d-71068c7dc831 | underdog | Trech Kekahuna | Receiving Yards | over | 0.08084359976015487 | 2026-10-28T05:43:27Z | 2026-10-31T23:30:00Z |
| underdog|2779b258-103f-4447-bbd2-4e32de9a6119 | underdog | Kyler Murray | Rush Yards | under | 0.0807146302213625 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|ad7f9e03-363a-4d30-9b4d-da66aee9eab6 | underdog | Josiah Freeman | Receiving Yards | under | 0.08070091626777509 | 2026-10-29T05:46:21Z | 2026-11-01T03:00:00Z |
| underdog|87384d05-6b0b-41cc-be57-65b4a4195a0c | underdog | Chris Boswell | FG Made | under | 0.08060150764940355 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|97fde5b2-0cea-4e84-a60d-314c45f15458 | underdog | Jordon Davison | Rush Yards | under | 0.08026516089841285 | 2026-10-30T05:46:05Z | 2026-10-31T19:30:00Z |
| underdog|688fd0a0-84a8-4fdc-b3e6-73d725d6651c | underdog | Matt Gay | Kicking Points | under | 0.08017488408939388 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| underdog|af47f3d7-7a13-4d4c-a07e-e37440eb8e97 | underdog | Jauan Jennings | Receiving Yards | under | 0.0801424432343455 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16364215 | prizepicks | Mason Taylor | Rec Targets | under | 0.08004599703900439 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|7e319885-fcd1-4795-a071-d187bfa430d0 | underdog | Kimani Vidal | Rush Yards | under | 0.07989167102913353 | 2026-10-30T05:46:05Z | 2026-11-01T21:05:00Z |
| underdog|dfac3d0b-440d-455f-9db9-be3be785ebbc | underdog | Daniel Bellinger | Receptions | under | 0.07970721189223906 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|ebfdac74-66b1-4b80-8af0-a406ffc1ad26 | underdog | Dohnte Meyers | Receiving Yards | under | 0.07961527812463143 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|a5e8c666-ecef-4176-8b5a-c79039669f0d | underdog | Patrick Mahomes | Rush Yards | under | 0.07958627648203864 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|e1246340-c9ea-4250-920c-2e90410c9b6b | underdog | Noah Jennings | Receptions | over | 0.07941850478767742 | 2026-10-29T05:46:21Z | 2026-10-31T19:30:00Z |
| underdog|fa42f53d-e6a1-4c4d-8911-c514b6f5cb65 | underdog | JJ Buchanan | Receptions | under | 0.07926362941120768 | 2026-10-30T05:46:05Z | 2026-10-31T16:30:00Z |
| underdog|e2692ca9-45cb-4e9d-ae48-bd8f36e8f770 | underdog | Kenneth Walker III | Receiving Yards | under | 0.07925791496494905 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| prizepicks|16364218 | prizepicks | Germie Bernard | Rec Targets | under | 0.07924997261919642 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|97184200-5077-4667-bd97-4bf6317675c2 | underdog | Isaac TeSlaa | Receptions | under | 0.07907295172171624 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|44e07250-7779-42a1-b2e8-3c713e3952c7 | underdog | Conner Harrell | Pass Yards | under | 0.07895703031570889 | 2026-10-30T05:46:05Z | 2026-10-30T23:00:00Z |
| underdog|29a57594-563b-446e-b1a8-c3d405a95378 | underdog | Sam Darnold | Pass TDs | under | 0.07875391297959822 | 2026-10-27T05:05:06Z | 2026-11-03T01:15:00Z |
| underdog|e9b8475b-f2fe-46f7-8e1c-42d4ee8076e4 | underdog | Devontez Walker | Receiving Yards | over | 0.0786942765304709 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| prizepicks|16364174 | prizepicks | Khalil Shakir | Rec Targets | under | 0.07852934480886664 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|e668407d-ff94-4b31-997a-5ed12d2e722f | underdog | Ty Dieffenbach | Pass Yards | under | 0.0783780964967764 | 2026-10-30T05:46:05Z | 2026-10-31T20:15:00Z |
| underdog|e451e337-fb60-4fc0-8043-f8588253f0d2 | underdog | Adonai Mitchell | Receptions | under | 0.07829765351425 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|13ace0db-24aa-4c7e-bfba-119a3d9610f0 | underdog | Brayden Trimble | Receptions | over | 0.07771464243106052 | 2026-10-30T05:46:05Z | 2026-10-31T16:00:00Z |
| underdog|29a958df-a2b1-41e5-9344-22b37cb26cb1 | underdog | Mason Taylor | Receiving Yards | under | 0.07765735031426335 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|b18a1790-47a1-4ae1-9f32-50eff0e7df43 | underdog | Tony Pollard | Rush Yards | under | 0.07758154832244912 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|cf19f1c6-7f81-468a-9f2a-a3aac48c989f | underdog | Jonah Coleman | Receiving Yards | under | 0.07739998615627042 | 2026-10-30T05:46:05Z | 2026-11-01T21:25:00Z |
| underdog|d1d78185-1dc9-4c46-acca-78125906daae | underdog | Trevor Lawrence | Rush Yards | under | 0.07734924110519159 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|dafba547-ae3a-4db2-9d1c-8ffd7b568456 | underdog | Jaylen Raynor | Rush Yards | over | 0.07687940560688156 | 2026-10-30T05:46:05Z | 2026-10-31T23:00:00Z |
| underdog|3c514266-18c3-470f-84b1-da3e8396317d | underdog | Sam LaPorta | Receptions | under | 0.07679022400127311 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|f86416a6-4bb5-437a-8801-cb5cb0c98823 | underdog | Theo Melin Ohrstrom | Receiving Yards | over | 0.0766365795758529 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| underdog|1219f959-0903-4377-a0bc-a328a24db1b9 | underdog | Arch Manning | Pass TDs | under | 0.07609166857256278 | 2026-10-29T05:46:21Z | 2026-10-31T23:30:00Z |
| underdog|0ebcf308-a8de-44ee-97cc-b2c9a347875b | underdog | Drake London | Receiving Yards | under | 0.07608032624515215 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|68e22951-6601-471d-a12e-fbaea9277356 | underdog | Rashod Bateman | Receiving Yards | under | 0.07606275380805294 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|86034be6-d3b2-4841-b0a3-7cadb61884fc | underdog | D'Andre Swift | Receiving Yards | under | 0.07598977212251534 | 2026-10-29T05:46:21Z | 2026-11-03T01:15:00Z |
| underdog|ab4c4291-4fa3-4224-8f91-f1a8fb579e07 | underdog | J.K. Dobbins | Receptions | under | 0.07588074058074556 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|b037b060-0b36-453f-b439-cb56fc8c7c95 | underdog | LaNorris Sellers | Pass TDs | under | 0.07551757439260098 | 2026-10-30T05:46:05Z | 2026-10-31T20:15:00Z |
| underdog|a471fcf1-a2a9-4bc8-95ee-33ca13fe3d7d | underdog | Jason Sanders | Kicking Points | under | 0.07535210830958228 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|447ef2be-9aed-498c-b0c9-a847a6c755d8 | underdog | Michael Mayer | Receiving Yards | under | 0.07524277884476527 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|a01ec37f-65ba-4176-afa3-c518f1b0c6e6 | underdog | Spencer Shrader | FG Made | over | 0.07516924076136433 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16238615 | prizepicks | Travis Kelce | Rec Yards | under | 0.07491212238443534 | 2026-10-27T05:05:06Z | 2026-11-01T16:25:00.000-05:00 |
| underdog|56a4d7d4-8693-4dc6-a6d5-34c61c34a58d | underdog | Fame Ijeboi | Receiving Yards | over | 0.07468539042408706 | 2026-10-30T05:46:05Z | 2026-10-31T20:15:00Z |
| underdog|3fc8d997-eb3f-4f2c-b357-e382ac030bca | underdog | Oronde Gadsden | Receptions | under | 0.0746522401153541 | 2026-10-30T05:46:05Z | 2026-11-01T21:05:00Z |
| underdog|3fa9f698-dc94-42d7-af28-813a420a9671 | underdog | Tyler Bass | Kicking Points | under | 0.07460791620015661 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| underdog|643ee736-d3da-4ff9-9257-7e6362eb9b8c | underdog | Keyone Jenkins | Pass TDs | over | 0.07442111817748337 | 2026-10-29T05:46:21Z | 2026-10-30T23:30:00Z |
| underdog|fda16c4d-dd48-4c72-a947-2a99435c8fb1 | underdog | Ahmad Miller | Rush Yards | under | 0.07428768813807607 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| underdog|d66a9fd2-3ad4-49d8-b430-b68d20eb4789 | underdog | Treylon Burks | Receptions | under | 0.07415346242378762 | 2026-10-29T05:46:21Z | 2026-11-02T01:20:00Z |
| underdog|b032f2ce-db4e-444c-a5ac-dbdf92013a50 | underdog | Devon Dampier | Pass TDs | over | 0.07411677035665121 | 2026-10-30T05:46:05Z | 2026-10-31T19:45:00Z |
| underdog|c1b8e741-c488-4ec2-ba8a-ade9f6427194 | underdog | Trey Butkowski | XP Made | under | 0.07393229451427985 | 2026-10-27T05:05:06Z | 2026-10-31T16:30:00Z |
| underdog|93ae2a44-e3eb-4055-8da9-44a422173f58 | underdog | Ashton Daniels | Pass TDs | over | 0.07381214411367737 | 2026-10-29T05:46:21Z | 2026-10-31T23:00:00Z |
| underdog|f1e7b9c6-fe0f-4cff-82bb-7ded830f76bf | underdog | Darian Mensah | Pass TDs | under | 0.07373742700667696 | 2026-10-28T05:43:27Z | 2026-10-31T23:30:00Z |
| underdog|fe265920-0a79-4445-ac94-cf5adefc9a32 | underdog | KJ Jackson | Pass Yards | under | 0.07361809926670371 | 2026-10-30T05:46:05Z | 2026-10-31T23:45:00Z |
| underdog|e3acb9f2-7432-44a2-bf81-850b5cdc7560 | underdog | Nate Frazier | Rush Yards | under | 0.07360069900144839 | 2026-10-30T05:46:05Z | 2026-10-31T19:30:00Z |
| prizepicks|16414643 | prizepicks | Nicolas Kristof | Goalie Saves | under | 0.07355997970979267 | 2026-10-30T05:46:05Z | 2026-10-30T15:30:00.000-04:00 |
| underdog|8c68b206-fe37-4e90-910e-3da1474752b1 | underdog | Kevin Jennings | Pass TDs | under | 0.07353953321120899 | 2026-10-30T05:46:05Z | 2026-10-31T16:00:00Z |
| underdog|ce6e4bca-e4dd-4f39-a2d2-f5726f2e0057 | underdog | KC Concepcion | Receptions | under | 0.07353629953328678 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|e7ecbdd2-92b1-40d0-a848-792abd490475 | underdog | Kanoah Vinesett | XP Made | under | 0.07341237547890234 | 2026-10-28T05:43:27Z | 2026-10-31T16:00:00Z |
| underdog|5f43a823-dd6d-4c89-bf05-ef74ff4611d7 | underdog | Mateen Bhaghani | XP Made | under | 0.07329546297206535 | 2026-10-30T05:46:05Z | 2026-10-31T20:15:00Z |
| underdog|e435f6f0-ffa3-490c-b17d-c06d52fc20f9 | underdog | Samaje Perine | Rush Yards | under | 0.07258371600193658 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|c3f6dbbe-f79d-4e3d-adc2-755392988b2a | underdog | Drake Maye | Pass TDs | under | 0.07237975805283348 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|ce99f8b4-299c-4c0e-bbdd-253733297a38 | underdog | Davis Allen | Receptions | under | 0.07229700088471258 | 2026-10-29T05:46:21Z | 2026-11-01T21:05:00Z |
| underdog|9b2b29fd-8436-4314-bca5-b436ff8e7d0c | underdog | Matt Gay | FG Made | under | 0.07218937725081309 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| underdog|e70899ec-2d6f-45a9-ba4c-3bd042d99cd0 | underdog | Harold Fannin | Receptions | under | 0.07210251211434926 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|0d036f46-6344-47bb-b2fa-bb6fd25e685f | underdog | Spencer Porath | FG Made | over | 0.07189003660273241 | 2026-10-28T05:43:27Z | 2026-10-31T16:00:00Z |
| underdog|45b2cebd-3957-48e7-8e14-9609e517784f | underdog | J.K. Dobbins | Receiving Yards | over | 0.07179068462409405 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|cf85c65e-45c3-4d84-b8cc-3cd5505c494f | underdog | Rayshon Luke | Receiving Yards | over | 0.07176712569482835 | 2026-10-29T05:46:21Z | 2026-11-01T03:00:00Z |
| underdog|e89a00be-6b2d-4715-a707-311078b1b78c | underdog | Jaylen Raynor | Pass TDs | under | 0.07107031689002485 | 2026-10-30T05:46:05Z | 2026-10-31T23:00:00Z |
| prizepicks|16265143 | prizepicks | Jonathan Taylor | Rush TDs | over | 0.07100695487408926 | 2026-10-28T05:43:27Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|347e949c-aed0-4263-80b1-bf253386ea34 | underdog | Ashton Jeanty | Rush Yards | under | 0.07098329396922187 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|aa32bf3e-4612-4433-960c-77abf50aeff0 | underdog | Brenton Strange | Receiving Yards | under | 0.07082871978056027 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|f5f09c2b-d42e-4593-8b2e-04388906b880 | underdog | Tuli Tuipulotu | Sacks | over | 0.07078839526651426 | 2026-10-30T05:46:05Z | 2026-11-01T21:05:00Z |
| underdog|9eb907ba-1f51-4385-a30b-efb9c1576b37 | underdog | Chase McLaughlin | FG Made | under | 0.0707192810705145 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|bc55e1f6-d719-4289-9222-36036ee542e4 | underdog | Kimani Vidal | Rush + Rec Yards | under | 0.07038688746847677 | 2026-10-30T05:46:05Z | 2026-11-01T21:05:00Z |
| underdog|4500d890-3567-488f-9563-71b7701fd49f | underdog | Jourdin Houston | Receptions | under | 0.07006649700306788 | 2026-10-30T05:46:05Z | 2026-10-31T16:30:00Z |
| underdog|510c8b69-a281-4f57-a69c-06edc72e891f | underdog | Cardae Mack | Rush Yards | under | 0.07006477470331085 | 2026-10-29T05:46:21Z | 2026-10-31T19:30:00Z |
| underdog|38c65ada-bd72-4a24-bba7-9cc1ccafd67f | underdog | Darnell Washington | Receiving Yards | under | 0.07003063145156818 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|a28a3a92-e695-4545-be4d-7f20f3c2cf85 | underdog | Dalton Kincaid | Receptions | under | 0.07001654956510595 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|dd1a8b64-c7cb-4bf4-a2b1-e409957fec6d | underdog | KC Concepcion | Receiving Yards | under | 0.06928901838504875 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|dfb17af9-2896-4370-8339-084dbd1d4c6c | underdog | Rico Dowdle | Rush + Rec Yards | under | 0.06917085030388226 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| underdog|dde18465-41fa-4ad3-bf99-92dfca5f0c27 | underdog | Will Hammond | Pass Yards | under | 0.06909809056296401 | 2026-10-30T05:46:05Z | 2026-10-31T16:00:00Z |
| underdog|6fe0a657-a357-46a4-b61b-3a443ee8b65d | underdog | Xavier Worthy | Receptions | under | 0.06903034280333475 | 2026-10-30T05:46:05Z | 2026-11-01T21:25:00Z |
| underdog|bab2e456-d14b-4bcb-967b-e23f2075580c | underdog | JC French | Rush Yards | over | 0.06883016771534489 | 2026-10-28T05:43:27Z | 2026-10-31T19:45:00Z |
| underdog|9ed7260e-5dc4-42c7-bc30-3f6c06622b59 | underdog | Omarion Hampton | Rush Yards | under | 0.06873439780196144 | 2026-10-30T05:46:05Z | 2026-11-01T21:05:00Z |
| underdog|92c45e5f-3130-4b0e-afaa-ac9694c178e7 | underdog | Ty Dieffenbach | Pass TDs | under | 0.06870975528808276 | 2026-10-29T05:46:21Z | 2026-10-31T20:15:00Z |
| underdog|aba44f6a-ac37-4b29-b8d0-3fab5f02a392 | underdog | Cameron Dicker | FG Made | under | 0.06821873845342952 | 2026-10-30T05:46:05Z | 2026-11-01T21:05:00Z |
| underdog|e4878992-a217-45a6-bb86-6dfac4ba8732 | underdog | Claire Liu | Double Faults | under | 0.06803809942362371 | 2026-10-30T05:46:05Z | 2026-10-30T07:30:00Z |
| underdog|fa3227f7-0e90-4d5c-9dcf-60a9f239ca3b | underdog | Davis Warren | Pass TDs | under | 0.0680220232331813 | 2026-10-30T05:46:05Z | 2026-10-31T19:15:00Z |
| prizepicks|16284249 | prizepicks | T.J. Hockenson | Rec Targets | under | 0.06775761944636594 | 2026-10-28T05:43:27Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|9493e7e9-c152-47ef-87d7-61177aa97a8a | underdog | J'Koby Williams | Receiving Yards | over | 0.06766110762216271 | 2026-10-28T05:43:27Z | 2026-10-31T16:00:00Z |
| underdog|fe6bba3b-8459-4bbf-a47e-291158c32d72 | underdog | Charlie Kolar | Receptions | under | 0.06751407843238566 | 2026-10-30T05:46:05Z | 2026-11-01T21:05:00Z |
| prizepicks|16346097 | prizepicks | Colton Joseph | Rush Atts | under | 0.06747059490915996 | 2026-10-30T05:46:05Z | 2026-10-31T12:00:00.000-04:00 |
| underdog|81caa087-4032-4f09-9276-eb7bc36d98b0 | underdog | Omar Cooper | Receiving Yards | under | 0.0664932335028362 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|6e8bf6ec-2b38-4eb5-b173-123fa25c963f | underdog | Bear Bachmeier | Pass TDs | under | 0.06644653594672256 | 2026-10-30T05:46:05Z | 2026-10-31T19:30:00Z |
| underdog|be4fd996-1cea-4e75-8595-443722f13a37 | underdog | Elijah Higgins | Receiving Yards | under | 0.06637495876969224 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|929bd902-5f8f-4e6b-8e6b-cbc968bb5973 | underdog | Kenneth Walker III | Rush Yards | under | 0.06618140649978566 | 2026-10-29T05:46:21Z | 2026-11-01T21:25:00Z |
| prizepicks|16242137 | prizepicks | Geno Smith | Pass TDs | under | 0.06607907021257264 | 2026-10-30T05:46:05Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|986fa224-9b7f-4eb5-86dd-0cef3ced7364 | underdog | Michael Mayer | Receptions | under | 0.0659709433914546 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|7211bbab-3ebc-4e19-9e96-9c2a27597daa | underdog | Keyone Jenkins | Rush Yards | over | 0.06544558902888675 | 2026-10-30T05:46:05Z | 2026-10-30T23:30:00Z |
| underdog|d9748f27-33c1-421f-b4bd-628dfde46f04 | underdog | Joe Burrow | Pass TDs | under | 0.06535420680993409 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|df8c742e-8d93-4945-b85f-845fd4ef194e | underdog | Keaton Mitchell | Receptions | over | 0.06525920681963904 | 2026-10-30T05:46:05Z | 2026-11-01T21:05:00Z |
| underdog|16d6e48b-3948-4277-8e98-69bfeda676cb | underdog | Ethan Moczulski | XP Made | over | 0.0651666116104308 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| underdog|be951d23-9c40-4420-9798-c030643ac47e | underdog | Lincoln Kienholz | Pass Yards | under | 0.06507048976779117 | 2026-10-30T05:46:05Z | 2026-10-31T19:15:00Z |
| underdog|871e8884-fa18-487f-b450-0777f6363fe3 | underdog | Quinshon Judkins | Receptions | under | 0.06475719636482524 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| underdog|435727be-5fbd-4cc1-b670-c8b031bf34d3 | underdog | Aidan Birr | XP Made | over | 0.06436112010722028 | 2026-10-29T05:46:21Z | 2026-10-31T23:30:00Z |
| underdog|d0b88cd8-3cb3-4478-b523-f64597760969 | underdog | Geno Smith | Rush Yards | under | 0.06435089670437177 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16414644 | prizepicks | Alexander Schwolow | Goalie Fantasy Score | under | 0.06408836571406518 | 2026-10-30T05:46:05Z | 2026-10-30T15:30:00.000-04:00 |
| underdog|8a2fb24e-2c14-439e-8095-f65f9680a486 | underdog | Justin Herbert | Rush Yards | under | 0.06397214605753254 | 2026-10-30T05:46:05Z | 2026-11-01T21:05:00Z |
| underdog|74927ffa-b169-4a9c-91c5-62a545d3c2b8 | underdog | Evan Stewart | Receiving Yards | under | 0.06372674950165025 | 2026-10-30T05:46:05Z | 2026-10-31T19:30:00Z |
| underdog|64143154-aadc-45c7-a747-3bd0fa9821f1 | underdog | Jahmyr Gibbs | Rush Yards | under | 0.06350630569074456 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| prizepicks|16300983 | prizepicks | Luther Burden III | Rec Targets | under | 0.06341229986208663 | 2026-10-28T05:43:27Z | 2026-11-02T20:15:00.000-05:00 |
| underdog|846c8bc8-36cc-4c1a-8c70-e6ec2d66bc55 | underdog | Jadon Porter | Receiving Yards | over | 0.06335100923993253 | 2026-10-28T05:43:27Z | 2026-10-30T23:30:00Z |
| underdog|280d3d15-f8c9-44e8-9ba8-58789a2423a8 | underdog | Javonte Williams | Receptions | under | 0.06330301619118184 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|883b23cb-c9d9-4c70-9559-19170502bb28 | underdog | Ryan Wingo | Receiving Yards | under | 0.06329325454658252 | 2026-10-29T05:46:21Z | 2026-10-31T23:30:00Z |
| underdog|5b41b251-f891-4866-baa6-3172a85b6f42 | underdog | Kendrick Bourne | Receptions | under | 0.06320028651530141 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|f5da7c08-3e81-4bb2-be0c-434189abf482 | underdog | Austin Simmons | Pass Yards | under | 0.06317704021369397 | 2026-10-30T05:46:05Z | 2026-10-31T23:45:00Z |
| underdog|baca9197-ba8b-4663-bd53-90146e8b84f9 | underdog | Jelani Thurman | Receiving Yards | under | 0.06300225759475764 | 2026-10-29T05:46:21Z | 2026-10-31T23:30:00Z |
| underdog|5932e1ec-a6a4-4366-9d3f-44ac49e2a35d | underdog | Trey Butkowski | FG Made | over | 0.0629815277565291 | 2026-10-30T05:46:05Z | 2026-10-31T16:30:00Z |
| underdog|829af19d-6d7a-4c67-ad2d-e7700466a300 | underdog | Ashton Jeanty | Receiving Yards | over | 0.06284370429834163 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|bc60efaf-67b4-484e-9e42-509e3c2b1a20 | underdog | Isaiah Marshall | Pass TDs | over | 0.06280985702197284 | 2026-10-30T05:46:05Z | 2026-10-31T19:30:00Z |
| underdog|484e2d7f-a4f8-4997-9d77-d2b39cbc54e4 | underdog | Tyler Goodson | Receiving Yards | over | 0.06257273013966114 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|c2ee8575-a516-49ad-b97c-0da52c295e72 | underdog | Rome Odunze | Receptions | under | 0.06252906711956707 | 2026-10-28T05:43:27Z | 2026-11-03T01:15:00Z |
| underdog|0b57f038-177b-4d34-b93a-95816320778a | underdog | Bo Nix | Rush Yards | under | 0.06252452212354309 | 2026-10-29T05:46:21Z | 2026-11-01T21:25:00Z |
| underdog|bbb87a92-fdcb-4e0a-a501-3a3cbe524779 | underdog | Chris Rodriguez | Receiving Yards | over | 0.06234948855341682 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|e18a38b1-b957-45f7-b383-192e33d64f2e | underdog | Dalton Kincaid | Receiving Yards | under | 0.06147912296713087 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| prizepicks|16402739 | prizepicks | Kendrick Bourne | Rec Targets | under | 0.06142371690223092 | 2026-10-30T05:46:05Z | 2026-11-01T13:00:00.000-05:00 |
| prizepicks|16237751 | prizepicks | Tony Pollard | Rush Yards | under | 0.06140796389369363 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|fd4366fd-78b4-40b1-b496-5a19769c9c2d | underdog | Beau Pribula | Pass TDs | under | 0.06127018961469988 | 2026-10-30T05:46:05Z | 2026-10-31T19:45:00Z |
| underdog|7725104f-bdb6-4a8b-b4dd-872d39f95400 | underdog | T.J. Hockenson | Receptions | under | 0.06125765068766775 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|d2a15f31-50f0-4ddb-9713-63caf82b161f | underdog | Bijan Robinson | Receiving Yards | under | 0.0608263421986458 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|8b6205f2-d917-417d-8d91-90bc4720c882 | underdog | Kyren Williams | Receiving Yards | over | 0.06069220762746541 | 2026-10-27T05:05:06Z | 2026-11-01T21:05:00Z |
| underdog|30294e8f-fb09-4591-8fec-13229ecc3549 | underdog | Kedrick Reescano | Rush Yards | under | 0.06056997571899836 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| underdog|492a0eb0-1afe-4583-8a5f-bfd40286ec64 | underdog | Michael Wilson | Receptions | under | 0.06055213759724276 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| underdog|8a35e2b8-8a79-44ef-a7ee-9d7b234fea7e | underdog | Chris Durr | Receiving Yards | under | 0.06005053443881847 | 2026-10-30T05:46:05Z | 2026-10-31T16:00:00Z |
| underdog|ab18cec1-7142-4b7d-8dce-144cda4aba39 | underdog | T.J. Moore | Receiving Yards | under | 0.059983705190083 | 2026-10-29T05:46:21Z | 2026-10-31T23:00:00Z |
| underdog|08301f8a-0c44-4f66-8a15-9438be96f70d | underdog | Jake Bates | Kicking Points | under | 0.059904580386489825 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|0229aa5c-f68a-4aa4-a654-01431e2231fd | underdog | Carson Hilbert | FG Made | under | 0.05986076657907846 | 2026-10-29T05:46:21Z | 2026-10-31T19:15:00Z |
| underdog|98460ef2-8588-4d82-b1cc-829c58ae2a96 | underdog | Evan Engram | Receiving Yards | under | 0.05960359227256917 | 2026-10-30T05:46:05Z | 2026-11-01T21:25:00Z |
| underdog|c8a12fa6-241d-4a08-bc61-0bf8b13c9579 | underdog | Chris Boswell | Kicking Points | under | 0.05954211907427087 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| underdog|3026976c-9e97-4ac0-b388-38122ef04d9e | underdog | Bijan Robinson | Rush Yards | under | 0.0593041313288305 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|99475b75-f813-42b6-9fae-93d3ef6f713d | underdog | Chad Ryland | FG Made | over | 0.059292701651925794 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|9ac2c0bd-2c7f-4975-956e-724b7e1d2f9a | underdog | Bijan Robinson | Rush + Rec Yards | under | 0.059219928329845684 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|a0707940-d2db-45d7-9750-4ad46cf7ade6 | underdog | Drake Maye | Rush Yards | under | 0.0591966971934933 | 2026-10-28T05:43:27Z | 2026-11-01T21:25:00Z |
| underdog|17522f98-2927-48ee-aacf-7ac5feaad8e0 | underdog | Turbo Richard | Rush Yards | under | 0.0591882117234237 | 2026-10-29T05:46:21Z | 2026-10-31T19:30:00Z |
| underdog|560d900e-4621-4c12-b7f6-7d0d0012d93d | underdog | Kevin Jennings | Pass Yards | under | 0.059041531185534346 | 2026-10-30T05:46:05Z | 2026-10-31T16:00:00Z |
| prizepicks|16364189 | prizepicks | Harold Fannin Jr. | Rec Targets | under | 0.0590162864584155 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|87117233-842c-4838-a347-1a7c15e78741 | underdog | Jaylen Warren | Rush + Rec Yards | under | 0.05900955861265822 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| underdog|15c359f6-49f6-417e-af04-7e3ac4910b59 | underdog | Treylon Burks | Receiving Yards | under | 0.058859686754247575 | 2026-10-29T05:46:21Z | 2026-11-02T01:20:00Z |
| underdog|21ccbd33-65c8-4adb-baf0-d54b8a99dde6 | underdog | Keon Coleman | Receiving Yards | under | 0.05861593824490208 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|ef62bc82-4c74-4ede-9833-155fc6973382 | underdog | Rhamondre Stevenson | Receptions | under | 0.05823816560303874 | 2026-10-30T05:46:05Z | 2026-11-01T21:25:00Z |
| underdog|42560f07-aca9-43b2-928f-1bfb83e542e0 | underdog | Quinshon Judkins | Receiving Yards | over | 0.05823237905245848 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| underdog|93c810d4-eed9-451e-b6a9-e26c9603244b | underdog | Kenny Gainwell | Rush Yards | under | 0.05790583094214585 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| prizepicks|16388729 | prizepicks | Leylah Fernandez | Double Faults | over | 0.05789032281642037 | 2026-10-30T05:46:05Z | 2026-10-30T01:30:00.000-04:00 |
| underdog|5fa14172-7c66-47e9-8a7f-b35ba67f8050 | underdog | Cayden Lee | Receiving Yards | under | 0.05745362784993435 | 2026-10-30T05:46:05Z | 2026-10-31T23:45:00Z |
| underdog|c668a8b3-ccff-4ad0-b4dc-c40c2039f950 | underdog | Hank Brown | Pass TDs | under | 0.0573573096766804 | 2026-10-30T05:46:05Z | 2026-10-31T16:00:00Z |
| underdog|b189f37d-6901-401b-b1ed-4366151f439b | underdog | Drew Mestemaker | Pass TDs | over | 0.05725353954029 | 2026-10-30T05:46:05Z | 2026-10-31T23:00:00Z |
| prizepicks|16238596 | prizepicks | Carnell Tate | Rec Yards | under | 0.05717982684838552 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|5fb87bff-c80d-4e34-8b35-ec63017df3e3 | underdog | Gunnar Helm | Receptions | under | 0.056747951711855205 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|c06b6e08-a754-472c-8fe4-515ba410c057 | underdog | Bo Jackson | Receiving Yards | over | 0.056513335530451236 | 2026-10-30T05:46:05Z | 2026-10-31T23:30:00Z |
| underdog|c93c54b7-e461-409c-abe5-98bb72a80e11 | underdog | Jake Weinberg | FG Made | under | 0.05647385732766519 | 2026-10-29T05:46:21Z | 2026-10-31T23:30:00Z |
| underdog|1c4b412a-02d9-4d64-b73c-9c532f02117b | underdog | Keshaun Singleton | Receiving Yards | under | 0.056254835798307146 | 2026-10-29T05:46:21Z | 2026-10-31T16:45:00Z |
| underdog|534639cf-dfef-43e9-a654-d0e1df93574f | underdog | Cairo Santos | Kicking Points | under | 0.056155326916546455 | 2026-10-27T05:05:06Z | 2026-11-03T01:15:00Z |
| underdog|84f851cb-cc37-4d00-8260-116ed42334ff | underdog | Will Reichard | FG Made | under | 0.05615139676343428 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|6d42c914-27c3-438c-acbe-78fb08aa843b | underdog | Samaje Perine | Rush + Rec Yards | under | 0.05609614725030898 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|e43e01d6-98b5-4008-b8a0-38a770fa134f | underdog | Colton Joseph | Pass TDs | over | 0.05595494235457177 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| underdog|528c499e-db42-48d1-898d-e58bd3de0b73 | underdog | Jeremiah Smith | Receptions | under | 0.055928804962394274 | 2026-10-30T05:46:05Z | 2026-10-31T23:30:00Z |
| underdog|a17857df-2c1f-4280-a440-863e34119dbb | underdog | Davis Warren | Pass Yards | under | 0.05590172090257528 | 2026-10-30T05:46:05Z | 2026-10-31T19:15:00Z |
| underdog|ebc69be6-3a46-4e34-8584-954dd8983fdf | underdog | Dezmen Roebuck | Receptions | under | 0.055655550474911664 | 2026-10-30T05:46:05Z | 2026-11-01T00:00:00Z |
| prizepicks|16402338 | prizepicks | Deshaun Watson | Pass TDs | under | 0.055343575858828875 | 2026-10-30T05:46:05Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|4f579d9d-5e1f-4254-af57-b079cbe6a8f1 | underdog | Abu Sama | Rush Yards | under | 0.054633465022213445 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| underdog|8230f1a8-97f9-4a79-b2fb-a7b30eaff15f | underdog | Bhayshul Tuten | Receiving Yards | under | 0.05432255572250255 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16238620 | prizepicks | Rome Odunze | Rec Yards | under | 0.054258843532627 | 2026-10-27T05:05:06Z | 2026-11-02T20:15:00.000-05:00 |
| underdog|f0a19a7f-3b51-4560-ac6e-749bf9bd2956 | underdog | Brenton Strange | Receptions | under | 0.054233780136315524 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|13afd78d-483b-4e75-b3c0-86232c4a56fc | underdog | Luke Lindenmeyer | Receiving Yards | over | 0.05382823148497251 | 2026-10-30T05:46:05Z | 2026-11-01T00:00:00Z |
| underdog|33e68115-ab5b-4e1d-bb9a-664c224799ac | underdog | Jil Teichmann | Double Faults | under | 0.0536446208404342 | 2026-10-30T05:46:05Z | 2026-10-30T06:10:00Z |
| underdog|1db0b382-7e86-4a18-890b-8f15c9278bfe | underdog | Carnell Tate | Receptions | under | 0.05308052318584133 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|8e491b01-8afc-4d86-9c1c-0899190e9b1a | underdog | Zion Ragins | Receiving Yards | over | 0.0527251106251867 | 2026-10-30T05:46:05Z | 2026-10-31T23:30:00Z |
| underdog|5951bf0f-9641-4fe5-9ea3-d9ded8f398d2 | underdog | Kyle Cunanan | XP Made | over | 0.05267788600146506 | 2026-10-29T05:46:21Z | 2026-11-01T00:00:00Z |
| prizepicks|16237752 | prizepicks | James Cook III | Rush Yards | under | 0.05257854707589438 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|6ebd4b62-13f5-47f3-b4ee-fd9243bc5544 | underdog | Byrum Brown | Rush Yards | under | 0.05253156112731816 | 2026-10-30T05:46:05Z | 2026-10-31T16:45:00Z |
| underdog|3490b0b5-7478-48ca-952a-8f7eb444d492 | underdog | TreVeyon Henderson | Rush + Rec Yards | under | 0.052478082271637194 | 2026-10-29T05:46:21Z | 2026-11-01T21:25:00Z |
| underdog|a688a6ab-bc4f-4c7b-b534-3f83979f56ab | underdog | Jameson Williams | Receptions | under | 0.05226576102064362 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16364217 | prizepicks | Darnell Washington | Rec Targets | under | 0.052041384305656635 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| prizepicks|16364179 | prizepicks | Rashod Bateman | Rec Targets | under | 0.051487447508205886 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|2213c610-5cc7-447a-a9d9-35da100d0a78 | underdog | Chad Ryland | Kicking Points | under | 0.05147593653628735 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|e2a75902-39bd-484e-a689-4b91f339a732 | underdog | Ezekiel Avit | Receiving Yards | under | 0.05141946070686243 | 2026-10-29T05:46:21Z | 2026-11-01T03:00:00Z |
| prizepicks|16394006 | prizepicks | Diana Shnaider | Break Points Won | under | 0.05133852111295989 | 2026-10-30T05:46:05Z | 2026-10-30T04:00:00.000-04:00 |
| underdog|025c12db-56b2-4ddb-8c79-3abf440f1e88 | underdog | Ashton Daniels | Pass Yards | under | 0.05127908443137885 | 2026-10-29T05:46:21Z | 2026-10-31T23:00:00Z |
| underdog|eae32ced-5562-4171-9153-d6f892a851d8 | underdog | Jonah Coleman | Receptions | under | 0.05108606262017712 | 2026-10-28T05:43:27Z | 2026-11-01T21:25:00Z |
| underdog|8c6a2b69-3c72-4ca4-b012-907d8d700ba4 | underdog | Sean O'Haire | XP Made | under | 0.050970613562157374 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| underdog|527b6de2-ee73-45c1-83a6-8d18b7884caf | underdog | AJ Newberry | Receiving Yards | over | 0.05084450786730932 | 2026-10-29T05:46:21Z | 2026-11-01T03:00:00Z |
| underdog|1f7e9822-c406-4313-b611-dc7f4ec099b2 | underdog | Gavin Lahm | XP Made | over | 0.0506435068891391 | 2026-10-28T05:43:27Z | 2026-10-31T16:00:00Z |
| prizepicks|16282267 | prizepicks | Jared Goff | Fantasy Score | under | 0.050640325067197955 | 2026-10-28T05:43:27Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|74ef8b28-abe0-49ef-9c0b-31d23d58b6b7 | underdog | Gianni Spetic | FG Made | over | 0.05052028789972679 | 2026-10-29T05:46:21Z | 2026-10-31T23:30:00Z |
| underdog|05973e5c-c64d-495b-afe2-bc2861b239b1 | underdog | Tre Tucker | Receiving Yards | under | 0.050201006752433996 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|9c7d8b40-56c2-433a-9611-e4c290a5c546 | underdog | Dierre Hill | Receiving Yards | over | 0.04996519105846309 | 2026-10-30T05:46:05Z | 2026-10-31T19:30:00Z |
| underdog|779ccae0-cd52-4c27-aeb5-6d2736e6178b | underdog | Kayden Dixon-Wyatt | Receiving Yards | over | 0.04982422068205983 | 2026-10-28T05:43:27Z | 2026-10-31T23:30:00Z |
| underdog|c4d26403-1bcc-48a3-9003-8c1a083495fe | underdog | Eli Raridon | Receiving Yards | under | 0.04979590063652606 | 2026-10-30T05:46:05Z | 2026-11-01T21:25:00Z |
| underdog|1932ca44-7aa4-4eb5-87a9-a049f89d1500 | underdog | Spencer Shrader | Kicking Points | over | 0.049734803311562326 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|8fdc408a-29d2-451e-b1ad-f4ae68023071 | underdog | T.J. Hockenson | Receiving Yards | under | 0.04970792234126764 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16402745 | prizepicks | Brevyn Spann-Ford | Rec Targets | under | 0.04933674260445342 | 2026-10-30T05:46:05Z | 2026-11-01T13:00:00.000-05:00 |
| prizepicks|16414642 | prizepicks | Alexander Schwolow | Goalie Saves | under | 0.04931417703510821 | 2026-10-30T05:46:05Z | 2026-10-30T15:30:00.000-04:00 |
| underdog|16da61a8-68ed-4f43-a9cc-3a5ff016a453 | underdog | Jayden Mandal | Pass TDs | over | 0.04927710339745611 | 2026-10-29T05:46:21Z | 2026-11-01T03:00:00Z |
| underdog|69fc930a-4c03-4d4b-a6c9-d40b78a5d898 | underdog | KJ Jackson | Rush Yards | over | 0.04916289873244073 | 2026-10-30T05:46:05Z | 2026-10-31T23:45:00Z |
| underdog|18baf2c3-c45c-4f7a-9620-c0ccecf70cf5 | underdog | Chris Brooks Jr. | Receiving Yards | over | 0.04905589340720118 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| underdog|6735a668-2023-4b6b-ab9e-4d20931dd3f0 | underdog | Noah Bennee | Receptions | under | 0.04896750451664933 | 2026-10-29T05:46:21Z | 2026-10-31T19:45:00Z |
| underdog|f66180a3-212e-41e1-bba2-9340d8085da7 | underdog | Diana Shnaider | Double Faults | over | 0.04872362457074347 | 2026-10-30T05:46:05Z | 2026-10-30T08:00:00Z |
| underdog|de0945a1-afd6-4ffb-88f2-2b3a29d378ec | underdog | Caleb Williams | Rush Yards | under | 0.04850594420248733 | 2026-10-28T05:43:27Z | 2026-11-03T01:15:00Z |
| underdog|9c429295-348b-4e15-aa45-a34d7a58d78d | underdog | Jesse Legree | Receiving Yards | under | 0.048162633826316026 | 2026-10-29T05:46:21Z | 2026-11-01T03:00:00Z |
| underdog|8c5ae168-2fb7-4426-a1b4-ba3dc88d6e04 | underdog | RJ Harvey | Rush Yards | under | 0.04813187243949535 | 2026-10-29T05:46:21Z | 2026-11-01T21:25:00Z |
| underdog|b53d0902-7dac-4964-a15d-0a80ea884841 | underdog | Kalif Raymond | Receiving Yards | over | 0.048116048113270304 | 2026-10-28T05:43:27Z | 2026-11-03T01:15:00Z |
| underdog|30a83c24-84d5-41fd-8aff-52b353da4607 | underdog | Elic Ayomanor | Receiving Yards | under | 0.04801195329933672 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|50c47c24-28ca-49c3-9979-a5ba89e91038 | underdog | DJ Vonnahme | Receptions | under | 0.0479938812111137 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| underdog|0f765643-8169-4741-a28e-d9b60a95fe70 | underdog | Tate Sandell | XP Made | under | 0.047953647080236195 | 2026-10-29T05:46:21Z | 2026-10-31T20:15:00Z |
| prizepicks|16416000 | prizepicks | Anthony Lopes | Goalie Saves | under | 0.04769819348916582 | 2026-10-30T05:46:05Z | 2026-10-31T15:45:00.000-04:00 |
| prizepicks|16415998 | prizepicks | Anthony Lopes | Goalie Saves | under | 0.04769819348916582 | 2026-10-30T05:46:05Z | 2026-10-31T15:45:00.000-04:00 |
| underdog|23b119b5-d925-452f-8e3e-8db85ad920d8 | underdog | Kaleb Webb | Receiving Yards | under | 0.047692692906041056 | 2026-10-30T05:46:05Z | 2026-10-31T16:00:00Z |
| underdog|1926ebcc-980c-4e75-8fe5-11620cbeeb75 | underdog | Beau Pribula | Pass Yards | under | 0.047653453453809225 | 2026-10-30T05:46:05Z | 2026-10-31T19:45:00Z |
| underdog|d5f3d1ed-165b-44a8-a8b5-8618cb9266b0 | underdog | Nolan Hauser | XP Made | over | 0.04757407443121031 | 2026-10-29T05:46:21Z | 2026-10-31T23:00:00Z |
| prizepicks|16237001 | prizepicks | Jared Goff | Rush Yards | over | 0.04739043004803156 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|41490ebf-7cdd-41eb-9b66-e2d19e7deb83 | underdog | Jake Ferguson | Receiving Yards | under | 0.0472991412481123 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|e44b5b57-b2a3-412d-9a94-e5caa236902c | underdog | Chris Bell | Receiving Yards | under | 0.047142394731641835 | 2026-10-28T05:43:27Z | 2026-11-01T21:25:00Z |
| underdog|606af54f-68bc-4f75-b3c3-3f62234232b2 | underdog | Elijah Higgins | Receptions | under | 0.04707934818798154 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|708bf473-ef2b-4551-bc19-c8f8e0500602 | underdog | Gavin Lahm | FG Made | under | 0.0470405683254459 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| prizepicks|16364193 | prizepicks | George Pickens | Rec Targets | under | 0.046942158355769203 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|eb27b957-08f3-4db1-a024-d2e6a932cccb | underdog | Evan Engram | Receptions | under | 0.046757074584347746 | 2026-10-30T05:46:05Z | 2026-11-01T21:25:00Z |
| underdog|5771b8de-ccc4-49f6-9282-a0844b232188 | underdog | Conner Harrell | Pass TDs | under | 0.04655397010697582 | 2026-10-30T05:46:05Z | 2026-10-30T23:00:00Z |
| underdog|d38d4943-2dba-4a2a-90bc-bdc04608ef33 | underdog | Yannick Smith | Receiving Yards | under | 0.04639267680093917 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| underdog|c2f97104-371e-4697-92a6-5020d37f6679 | underdog | Cam Coleman | Receptions | under | 0.04636948619488379 | 2026-10-30T05:46:05Z | 2026-10-31T23:30:00Z |
| underdog|51cead8d-b0ba-4fc4-be88-69aeddb1c444 | underdog | Jacob Harris | Receiving Yards | over | 0.04633601742818927 | 2026-10-30T05:46:05Z | 2026-10-31T16:00:00Z |
| prizepicks|16415339 | prizepicks | Tatjana Maria | 1st Set Total Games | over | 0.04606460198283813 | 2026-10-30T05:46:05Z | 2026-10-30T16:00:00.000-04:00 |
| underdog|82aa032b-8775-48cf-8168-6d399a862334 | underdog | Jamal Roberts | Rush Yards | under | 0.04592301000005228 | 2026-10-30T05:46:05Z | 2026-10-31T23:45:00Z |
| prizepicks|16283726 | prizepicks | Jameson Williams | Rec Targets | under | 0.04588546580195274 | 2026-10-28T05:43:27Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|0d2e90ec-252a-4b26-9d26-73e24dee3447 | underdog | Wyatt Young | Receiving Yards | under | 0.04587596073839573 | 2026-10-30T05:46:05Z | 2026-10-31T23:00:00Z |
| underdog|c9e24606-be31-4cdf-92ac-aa2d5838555c | underdog | Aidan Chiles | Pass Yards | under | 0.045784942343087165 | 2026-10-30T05:46:05Z | 2026-10-31T19:30:00Z |
| underdog|2c10d59f-2805-4247-b3a9-7f132630e8b7 | underdog | Caleb Douglas | Receiving Yards | under | 0.04572395459474321 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| prizepicks|16402744 | prizepicks | Ryan Flournoy | Rec Targets | under | 0.04560777298675278 | 2026-10-30T05:46:05Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|ccf764a6-e25c-4a47-801c-bbf244f5ec13 | underdog | Colston Loveland | Receptions | under | 0.04553104131701269 | 2026-10-28T05:43:27Z | 2026-11-03T01:15:00Z |
| underdog|830f369c-f207-4c9d-a288-ea0d11258ba3 | underdog | DK Metcalf | Receptions | under | 0.04537863534296749 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|c22f89a3-d617-447a-a58e-cd99f746e9de | underdog | Nolan Bartley | FG Made | over | 0.045360020231472564 | 2026-10-28T05:43:27Z | 2026-10-31T16:00:00Z |
| underdog|8429bc0f-426c-4934-97df-fb2cebdf0209 | underdog | Ty Clark | Rush Yards | under | 0.04527711641873777 | 2026-10-30T05:46:05Z | 2026-10-31T19:45:00Z |
| underdog|b610bf87-5fe8-4609-a169-6a3823d87fcc | underdog | Rashod Bateman | Receptions | under | 0.045179537492164634 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|b6337f9a-8703-4ca4-8011-f8414f84dffa | underdog | Gunner Stockton | Pass TDs | under | 0.04503800078880826 | 2026-10-30T05:46:05Z | 2026-10-31T19:30:00Z |
| underdog|e13649e5-fba3-4ab7-8e62-437ce584f560 | underdog | Mike Gesicki | Receiving Yards | under | 0.04487689705356923 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|6f538e31-bd0b-442f-a0c6-c806526a0af6 | underdog | Derrick Henry | Receiving Yards | over | 0.044786350412196085 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|c000965f-9220-48af-a50e-e406a9b82207 | underdog | Patrick Mahomes | Pass TDs | under | 0.044605755569356864 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|07c9159e-953d-4ca9-8a3d-7f2c24f3b622 | underdog | Konata Mumpfield | Receiving Yards | under | 0.04449810098666451 | 2026-10-27T05:05:06Z | 2026-11-01T21:05:00Z |
| underdog|a59eab77-29bf-422a-8460-35c449cac12a | underdog | Kirk Cousins | Pass TDs | under | 0.044346815076756196 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|3be5851f-dea0-40b3-9bb0-9f568d8723b4 | underdog | Samaje Perine | Receiving Yards | over | 0.04427871151764762 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| prizepicks|16402748 | prizepicks | Charlie Kolar | Rec Targets | under | 0.04401764507846051 | 2026-10-30T05:46:05Z | 2026-11-01T16:05:00.000-05:00 |
| prizepicks|16415341 | prizepicks | Tatjana Maria | Total Games | over | 0.043912578008937 | 2026-10-30T05:46:05Z | 2026-10-30T16:00:00.000-04:00 |
| underdog|198884fe-d6ca-4b36-ae25-b5ac648d7ba6 | underdog | Isaac TeSlaa | Receiving Yards | over | 0.04387998320763925 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|fdf0e9c3-6e6b-478e-8aa9-6b45b8e1f195 | underdog | Tyler Goodson | Receptions | under | 0.04381326256994522 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|3240a9a9-a7e7-4cfa-9591-2bcad0bdb937 | underdog | Chris Bell | Receptions | under | 0.043709873908828745 | 2026-10-29T05:46:21Z | 2026-11-01T21:25:00Z |
| underdog|76b1c95e-f2da-413c-bfdf-08dc4716e96d | underdog | Bryant Wesco | Receiving Yards | under | 0.04364958858262513 | 2026-10-29T05:46:21Z | 2026-10-31T23:00:00Z |
| underdog|f9073931-b033-47be-b4c0-c21ae3da3381 | underdog | Duce Robinson | Receiving Yards | under | 0.043544683185050226 | 2026-10-29T05:46:21Z | 2026-10-31T23:00:00Z |
| underdog|a9e53d2d-0c20-48d4-84e0-0095d4f19b93 | underdog | Brayden Trimble | Receiving Yards | over | 0.04345370651861802 | 2026-10-30T05:46:05Z | 2026-10-31T16:00:00Z |
| underdog|d3cc7358-d7be-4564-b99a-af1f66ccb50f | underdog | Blake Corum | Receptions | over | 0.04322925578199588 | 2026-10-29T05:46:21Z | 2026-11-01T21:05:00Z |
| underdog|f2fc4cdc-f3c4-4e80-b227-07da35d3b98c | underdog | Dwight Phillips | Rush Yards | under | 0.04320118602607115 | 2026-10-30T05:46:05Z | 2026-10-31T19:30:00Z |
| underdog|eac19390-9b3f-47b1-9bad-ca5de4286ce7 | underdog | Will Hammond | Rush Yards | over | 0.04314212104682347 | 2026-10-30T05:46:05Z | 2026-10-31T16:00:00Z |
| prizepicks|16364216 | prizepicks | DK Metcalf | Rec Targets | under | 0.04294350532078739 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|78fe307a-7e17-4bd9-9d8e-fd56b5fcaa2d | underdog | Dyami Brown | Receptions | over | 0.04281344784836044 | 2026-10-29T05:46:21Z | 2026-11-02T01:20:00Z |
| underdog|7e034eac-4fcf-4384-9c19-bb34f59fe697 | underdog | Malachi Toney | Receiving Yards | under | 0.04269661126756763 | 2026-10-30T05:46:05Z | 2026-10-31T23:30:00Z |
| underdog|31b6cd09-6d41-4dce-bfef-ef128d55cad2 | underdog | Anthony Evans III | Receptions | under | 0.042671576227215735 | 2026-10-29T05:46:21Z | 2026-10-31T23:30:00Z |
| underdog|455ce973-4d39-4aa0-9282-173bf65e60d1 | underdog | Destyn Hill | Receiving Yards | under | 0.042638739173543216 | 2026-10-30T05:46:05Z | 2026-10-30T23:00:00Z |
| underdog|03de3a38-04de-414a-b7a5-843d90fdf6d0 | underdog | Malik Willis | Rush Yards | under | 0.042608298491113694 | 2026-10-28T05:43:27Z | 2026-11-01T21:25:00Z |
| underdog|21ec210e-8d38-4fb5-8cea-ec22dc7def12 | underdog | Charlie Becker | Receptions | under | 0.04239973318552892 | 2026-10-29T05:46:21Z | 2026-10-31T19:30:00Z |
| underdog|19251325-4557-42e1-bc95-30a7ef0f2d87 | underdog | Jack Foley | Receiving Yards | over | 0.04212913026875664 | 2026-10-30T05:46:05Z | 2026-10-31T19:45:00Z |
| underdog|51d46586-a523-4495-90f8-ba3a7a79a2ca | underdog | Will Kacmarek | Receiving Yards | over | 0.042084427220204 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|c15e674d-1cff-45ca-856b-4c480e003161 | underdog | Josh Cameron | Receiving Yards | over | 0.04200192948698528 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|b4dedce4-c003-49dd-9798-feada7e5d80f | underdog | RJ Harvey | Receptions | over | 0.041882620116427405 | 2026-10-28T05:43:27Z | 2026-11-01T21:25:00Z |
| underdog|644bad07-55f1-487c-b577-d7c58207a680 | underdog | Omarion Hampton | Receiving Yards | over | 0.041868529547130606 | 2026-10-30T05:46:05Z | 2026-11-01T21:05:00Z |
| underdog|3b28befe-ffab-48de-94a7-aec131ad5e79 | underdog | Harold Fannin | Receiving Yards | under | 0.04179548726493032 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16364175 | prizepicks | Ty Johnson | Rec Targets | under | 0.04178599301145003 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|32ef8c61-1230-4d06-951d-a61e3c6731db | underdog | Fluff Bothwell | Rush Yards | under | 0.04173798115979499 | 2026-10-30T05:46:05Z | 2026-10-31T23:30:00Z |
| underdog|8dd20ddf-9d01-4078-8e3c-311b59ce525a | underdog | Nate Boerkircher | Receiving Yards | under | 0.04155813247968276 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|9b7821ea-2e53-461c-b921-cb3f9b0a8766 | underdog | Kenny Johnson | Receiving Yards | under | 0.041462374613398856 | 2026-10-28T05:43:27Z | 2026-10-31T16:00:00Z |
| prizepicks|16364197 | prizepicks | Brenton Strange | Rec Targets | under | 0.041443366540232285 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|32416c79-0be8-4aff-a916-63447d4e4b6e | underdog | Oronde Gadsden | Receiving Yards | under | 0.04140175073017738 | 2026-10-30T05:46:05Z | 2026-11-01T21:05:00Z |
| underdog|e5d8e1c9-e08e-4e30-9779-e89a1ccad2d8 | underdog | James Cook | Receptions | under | 0.04119703252365636 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| prizepicks|16402340 | prizepicks | Joe Burrow | Pass TDs | under | 0.04078667402858949 | 2026-10-30T05:46:05Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|5606a896-094d-4881-8dc0-335fec3d998c | underdog | Mike Washington | Rush Yards | under | 0.04074539618844153 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|b600adee-02bd-4b47-a48c-a83c1bf9ba2d | underdog | Aidan Birr | FG Made | under | 0.040671745804310544 | 2026-10-30T05:46:05Z | 2026-10-31T23:30:00Z |
| underdog|e79cbf75-3522-461e-a424-eea0877fd852 | underdog | Josh Cuevas | Receiving Yards | over | 0.040617425881482316 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|30b2d4f9-6c5e-4bc6-8b2c-1d4427e03d96 | underdog | Efton Chism | Receptions | over | 0.04045962303919298 | 2026-10-29T05:46:21Z | 2026-11-01T21:25:00Z |
| underdog|ee4c0f1f-53cc-4980-be71-16dae58dce29 | underdog | Creed Whittemore | Receiving Yards | under | 0.04040288390758162 | 2026-10-30T05:46:05Z | 2026-10-31T19:45:00Z |
| underdog|61afb864-4e07-4a48-bd41-c4eb74160900 | underdog | Reed Harris | Receiving Yards | under | 0.04036453470122037 | 2026-10-29T05:46:21Z | 2026-10-31T19:30:00Z |
| underdog|7b1fdfdd-16de-4bc2-b22a-83c16c063a84 | underdog | Jaron-Keawe Sagapolutele | Pass TDs | under | 0.04024553158153066 | 2026-10-30T05:46:05Z | 2026-10-31T16:00:00Z |
| underdog|fac6134d-822d-44dc-9f73-a71adfd62ab0 | underdog | Kyren Williams | Receptions | over | 0.03984826894881116 | 2026-10-27T05:05:06Z | 2026-11-01T21:05:00Z |
| underdog|8cc04c26-0f61-4d4b-9342-06cb3930c956 | underdog | Tony Pollard | Receptions | under | 0.039626209780273536 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| prizepicks|16364221 | prizepicks | Emeka Egbuka | Rec Targets | under | 0.03957168775040509 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|7f01a8a1-7362-4713-9044-e7b15105374a | underdog | RJ Harvey | Receiving Yards | over | 0.039525740504224194 | 2026-10-28T05:43:27Z | 2026-11-01T21:25:00Z |
| underdog|b6d94039-076e-4d23-94d9-b0ea1abc0b69 | underdog | Ashton Daniels | Rush Yards | under | 0.03941215066956005 | 2026-10-29T05:46:21Z | 2026-10-31T23:00:00Z |
| underdog|2f7514c5-2b88-4864-88b6-649131ebb46e | underdog | Wayshawn Parker | Receiving Yards | over | 0.03934486821897232 | 2026-10-29T05:46:21Z | 2026-10-31T19:45:00Z |
| underdog|c1d72897-6bd9-4c39-9000-60649b1e219a | underdog | Dylan Raiola | Pass TDs | under | 0.03925748763552139 | 2026-10-30T05:46:05Z | 2026-10-31T19:30:00Z |
| underdog|d06eb894-124b-4188-9763-d586cc1def8f | underdog | Tyler Warren | Receptions | under | 0.039251759862195756 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|4192d51e-49c7-433a-892e-6c32daf1a68a | underdog | Luther Burden | Receptions | under | 0.03905790770780704 | 2026-10-28T05:43:27Z | 2026-11-03T01:15:00Z |
| underdog|1634f3b6-c4a5-4bbd-9664-8ef480aed4c0 | underdog | Malachi Henry | Receiving Yards | over | 0.03899346384567681 | 2026-10-30T05:46:05Z | 2026-10-31T19:45:00Z |
| prizepicks|16401837 | prizepicks | Alexander Zverev | Total Games | over | 0.03876653104365624 | 2026-10-30T05:46:05Z | 2026-10-30T12:30:00.000-04:00 |
| underdog|c5abd3f3-5040-4527-abe0-b0722e85e0cc | underdog | Dezmen Roebuck | Receiving Yards | under | 0.03871084003360692 | 2026-10-30T05:46:05Z | 2026-11-01T00:00:00Z |
| underdog|5e1335c5-ac9f-4444-8e0d-eb1495cf8f51 | underdog | Ryan Flournoy | Receiving Yards | under | 0.03866220721623803 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|ba5b752c-a956-46bc-8f78-425674b1c328 | underdog | Josh Downs | Receptions | under | 0.038610418627245346 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|362485ef-3b59-4c1d-bcd8-5a9aac1de2ce | underdog | Gabe Panikowski | XP Made | over | 0.03851576024535286 | 2026-10-30T05:46:05Z | 2026-10-31T23:00:00Z |
| underdog|3793166b-1152-486d-8937-fd0ff5c31b01 | underdog | Emmett Mosley | Receiving Yards | over | 0.038249689959863664 | 2026-10-30T05:46:05Z | 2026-10-31T23:30:00Z |
| underdog|178431a1-f0fe-4939-bf64-ca52aeaf6d23 | underdog | Michael Penix | Pass TDs | under | 0.03824422373301384 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|02d88dd0-0193-43d5-ac9b-4721fa50221e | underdog | Tony Diaz | Receptions | over | 0.03799071741717408 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| underdog|7ecdc2be-8a03-41cf-a4a6-70b7ea77d4a2 | underdog | Craig Dandridge | Receiving Yards | under | 0.037959336678760836 | 2026-10-29T05:46:21Z | 2026-10-31T19:30:00Z |
| underdog|bf6ca6da-af3f-4713-b41b-c325c3778b5a | underdog | Kenyon Sadiq | Receiving Yards | under | 0.0379541272976508 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|c0277dcb-affc-4063-a8a1-e39df4980e10 | underdog | Javon Tracy | Receiving Yards | over | 0.03785441979554416 | 2026-10-30T05:46:05Z | 2026-10-31T19:30:00Z |
| underdog|ce994eba-a6a8-45f5-b850-da23fb0d4bbd | underdog | Jaylen Warren | Rush Yards | under | 0.03784363197833929 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|5d02b860-79d7-44a4-ad10-fc9a11ad352d | underdog | Jonathan Taylor | Receiving Yards | over | 0.03782774826923374 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|e2ff7b1d-1771-4ea6-a5fc-6484aff55b14 | underdog | Dakorien Moore | Receiving Yards | under | 0.03779054988380326 | 2026-10-30T05:46:05Z | 2026-10-31T19:30:00Z |
| prizepicks|16385690 | prizepicks | Claire Liu | Total Games | over | 0.03778923839977921 | 2026-10-30T05:46:05Z | 2026-10-30T03:30:00.000-04:00 |
| underdog|009648c8-a8e6-4e1f-b73c-2db8a09d8d94 | underdog | Alberto Mendoza | Pass TDs | under | 0.03766539666977964 | 2026-10-29T05:46:21Z | 2026-10-31T23:30:00Z |
| underdog|ea1ca778-0c1f-41f0-aa6d-ee49d30fc0c6 | underdog | Eric Olsen | Receptions | under | 0.037652007406090426 | 2026-10-29T05:46:21Z | 2026-11-01T03:00:00Z |
| prizepicks|16300981 | prizepicks | Colston Loveland | Rec Targets | under | 0.03749133938696103 | 2026-10-28T05:43:27Z | 2026-11-02T20:15:00.000-05:00 |
| underdog|7525ad0c-f287-466e-b74b-abe50990475b | underdog | Donovan Olugbode | Receptions | over | 0.03746905328714911 | 2026-10-30T05:46:05Z | 2026-10-31T23:45:00Z |
| underdog|80a89004-6a11-40e7-982e-15d5b2dac1f9 | underdog | Chris Marshall | Receiving Yards | under | 0.03734732861392476 | 2026-10-30T05:46:05Z | 2026-10-31T23:45:00Z |
| underdog|54cf05e2-86ba-4145-9c8a-43035b15a415 | underdog | Chase Brown | Receiving Yards | under | 0.03733610239343621 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|2e7942ca-9587-4276-b7a4-c2d60df5e093 | underdog | DeMario Douglas | Receiving Yards | under | 0.037301755521942925 | 2026-10-28T05:43:27Z | 2026-11-01T21:25:00Z |
| underdog|4c920fbd-dddb-478f-9f99-942b5eefcbb9 | underdog | Miles Coleman | Receiving Yards | over | 0.037198098052761974 | 2026-10-30T05:46:05Z | 2026-10-31T23:00:00Z |
| underdog|a6465eb4-f35b-4df3-96fa-5fb54b912ba0 | underdog | Josh Cameron | Receptions | over | 0.03708353453092156 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|6ae9a9f4-242a-41a5-99f7-33be84335919 | underdog | Rhamondre Stevenson | Receiving Yards | over | 0.03707786261961721 | 2026-10-30T05:46:05Z | 2026-11-01T21:25:00Z |
| prizepicks|16402747 | prizepicks | Jalen Nailor | Rec Targets | under | 0.0370239629128748 | 2026-10-30T05:46:05Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|c202626d-b120-4dcb-b6f5-f780fcc05670 | underdog | Chase McLaughlin | Kicking Points | under | 0.036936611973116484 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|c890ac2e-c745-461a-a6b7-916637b34aef | underdog | Blake Corum | Rush Yards | under | 0.03677885970822303 | 2026-10-28T05:43:27Z | 2026-11-01T21:05:00Z |
| underdog|2c820b65-e81a-450f-8e20-ae08f2f5cbd1 | underdog | Drew Sample | Receptions | over | 0.03661347158895961 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| underdog|0f7137e7-3b40-440d-941f-5b78b8664539 | underdog | Omarion Hampton | Receptions | over | 0.03636444534129746 | 2026-10-30T05:46:05Z | 2026-11-01T21:05:00Z |
| underdog|5c4d4242-97a0-43dc-9262-319033e766a5 | underdog | Drake Lindsey | Pass Yards | over | 0.036344697021042816 | 2026-10-29T05:46:21Z | 2026-10-31T19:30:00Z |
| underdog|b813491c-788b-4736-a5c6-73ef18465a85 | underdog | Trent Mosley | Receiving Yards | under | 0.03630113995308826 | 2026-10-28T05:43:27Z | 2026-10-31T23:30:00Z |
| underdog|0e97bc61-f4c9-43bf-ac33-cc721a44ae2c | underdog | Jaden Barnes | Receiving Yards | under | 0.03625717023537589 | 2026-10-30T05:46:05Z | 2026-10-30T23:00:00Z |
| underdog|def7e19b-34f0-48f0-9fe7-90b650851a32 | underdog | AJ Newberry | Receptions | over | 0.036203441209521625 | 2026-10-29T05:46:21Z | 2026-11-01T03:00:00Z |
| underdog|e7fb2bbb-1d1d-4e90-999d-7d2bf0bdf4d5 | underdog | Eric Olsen | Receiving Yards | under | 0.03607044045465946 | 2026-10-29T05:46:21Z | 2026-11-01T03:00:00Z |
| underdog|60dcd824-4333-4248-9adb-7a2d45a8e21d | underdog | Aaron Rodgers | Pass TDs | over | 0.035917777674994156 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|e9ea3ccc-b510-4ea3-b57a-97315d2504f7 | underdog | Blake Corum | Rush + Rec Yards | under | 0.03571791060606555 | 2026-10-30T05:46:05Z | 2026-11-01T21:05:00Z |
| underdog|0863baa7-e79f-40da-bcfe-599e123a6e11 | underdog | Emmett Mosley | Receptions | under | 0.03571704252129171 | 2026-10-30T05:46:05Z | 2026-10-31T23:30:00Z |
| underdog|2be7e738-53f7-4351-87dd-3388416e0910 | underdog | CeeDee Lamb | Receptions | under | 0.035657182557574885 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| prizepicks|16364198 | prizepicks | Jakobi Meyers | Rec Targets | under | 0.03556814695217747 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|579466c0-c1f1-4bb6-bade-551753e538f0 | underdog | Bucky Irving | Receiving Yards | under | 0.035277747501728185 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|f3938f50-0ad5-46d6-8905-53a081b714ed | underdog | Jayden Mandal | Rush Yards | over | 0.03520194592809056 | 2026-10-29T05:46:21Z | 2026-11-01T03:00:00Z |
| prizepicks|16332054 | prizepicks | Aidan Chiles | Pass Comp | under | 0.035035949799829935 | 2026-10-29T05:46:21Z | 2026-10-31T15:30:00.000-04:00 |
| underdog|dc3a0b69-19ee-45aa-8d80-0719aac57a06 | underdog | Caleb Hawkins | Receiving Yards | over | 0.0350114322402898 | 2026-10-30T05:46:05Z | 2026-10-31T23:00:00Z |
| underdog|87f9bdf4-f40f-4b04-9ebd-add8492f187a | underdog | Jerry Jeudy | Receiving Yards | under | 0.03475932480352539 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|c629e073-546f-4206-a875-39ce3682f009 | underdog | Mike Gesicki | Receptions | under | 0.034662618407678036 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|38be05a8-f1e4-46f7-a5d7-641d48560923 | underdog | Chris Rodriguez | Receptions | over | 0.034641968529540934 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|b3751b87-dfa3-4115-a41b-40fefe555ef3 | underdog | Chauncey Magwood | Receiving Yards | under | 0.0342908503820849 | 2026-10-30T05:46:05Z | 2026-10-31T20:15:00Z |
| underdog|bfc06dd7-40ab-4a2a-8625-e8be732febf5 | underdog | Omarion Miller | Receiving Yards | over | 0.034223888783094125 | 2026-10-29T05:46:21Z | 2026-10-31T19:30:00Z |
| underdog|54b3491a-ed4a-4622-b92f-743a9dfcba0f | underdog | Breece Hall | Receiving Yards | over | 0.03418871155142866 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| prizepicks|16236993 | prizepicks | Aaron Rodgers | Rush Yards | over | 0.03417868452026862 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|560d1c3b-e4d8-482b-bd34-a9ff0cb53ee6 | underdog | Jacoby Brissett | Rush Yards | under | 0.03413392339426191 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|4eb41d96-5f3c-4117-8b19-2648249e89b6 | underdog | Dylan Sampson | Rush + Rec Yards | over | 0.0340965503154389 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| underdog|7f1a08bd-53b5-4e67-8cc1-7a1fbc88ead7 | underdog | Nyziah Hunter | Receiving Yards | under | 0.0340593554925851 | 2026-10-30T05:46:05Z | 2026-11-01T00:00:00Z |
| underdog|e65eb02e-d60d-468f-a975-5ee41aa5b8ef | underdog | Duke Watson | Rush Yards | under | 0.03404499786728077 | 2026-10-28T05:43:27Z | 2026-10-30T23:30:00Z |
| underdog|0f681c42-8f76-4cb8-9522-05ec95d04f05 | underdog | Justice Hill | Rush Yards | under | 0.0339590282720027 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|a08c6057-39f2-45de-a1f6-14d94390ada6 | underdog | Charlie Becker | Receiving Yards | under | 0.03387812144126445 | 2026-10-29T05:46:21Z | 2026-10-31T19:30:00Z |
| underdog|998f5136-7f56-4e49-8f7e-9c4a62dd80c7 | underdog | Drew Sample | Receiving Yards | over | 0.03381014984609054 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| underdog|a74ebe4a-43ea-44ea-bb1f-775ec2f098de | underdog | Traylon Ray | Receiving Yards | over | 0.03376854226977788 | 2026-10-30T05:46:05Z | 2026-10-31T16:45:00Z |
| underdog|b6d0b727-a1c5-4b46-a33f-d1812b1d91ea | underdog | Josh Downs | Receiving Yards | under | 0.0335880037665488 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|c247c38e-8847-4570-8f76-f033c195a0d7 | underdog | Ashton Jeanty | Receptions | under | 0.033565625285393086 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|69370026-9515-4c28-94a7-7b9ed03c4bdc | underdog | Derrick Henry | Receptions | over | 0.033424548277637356 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|c97a21be-74a7-497c-944c-4ddacac7dd6f | underdog | Kayden Dixon-Wyatt | Receptions | over | 0.03325325310824867 | 2026-10-28T05:43:27Z | 2026-10-31T23:30:00Z |
| underdog|c94fca32-9311-4c26-b4a0-04ea9a61b58d | underdog | Keon Coleman | Receptions | over | 0.03273798327050681 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|95e3287a-859c-45f6-b5b3-d38de81f9186 | underdog | Lawson Luckie | Receiving Yards | over | 0.03260831179607715 | 2026-10-28T05:43:27Z | 2026-10-31T19:30:00Z |
| underdog|a2dcdbe2-6b4c-4403-ad8a-75f4896fffa4 | underdog | Michael Salgado-Medina | XP Made | over | 0.03255890755952284 | 2026-10-30T05:46:05Z | 2026-10-31T16:00:00Z |
| underdog|1f68e0f5-4758-426a-a308-b5c68e1c8048 | underdog | Sam Darnold | Rush Yards | over | 0.0325476533253789 | 2026-10-27T05:05:06Z | 2026-11-03T01:15:00Z |
| underdog|254bd294-909f-4b6a-bfbb-dd5313c81151 | underdog | Gabe Panikowski | FG Made | over | 0.032531030009363526 | 2026-10-29T05:46:21Z | 2026-10-31T23:00:00Z |
| underdog|b9a41163-712b-4516-b471-5bfa5ecae2d1 | underdog | Braden Pegan | Receiving Yards | under | 0.032292065704640605 | 2026-10-29T05:46:21Z | 2026-10-31T19:45:00Z |
| underdog|7399aede-c517-452b-bf90-398652b085c6 | underdog | Dyami Brown | Receiving Yards | under | 0.03201524823912261 | 2026-10-29T05:46:21Z | 2026-11-02T01:20:00Z |
| underdog|31c29fbb-9913-48cf-8fbb-3dcf69104679 | underdog | Tee Higgins | Receiving Yards | under | 0.031976149300329104 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| underdog|c6aebee3-7d3b-41c5-9c55-6221488a8d26 | underdog | Nyck Harbor | Receiving Yards | over | 0.03195356480209599 | 2026-10-30T05:46:05Z | 2026-10-31T20:15:00Z |
| underdog|3c7d6af2-24a4-4712-868a-a3ddc96c35d6 | underdog | Bucky Irving | Receptions | over | 0.031934092041214335 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|a973e2a4-34d4-4bb0-bf44-199878fc388c | underdog | Cooper Barkate | Receptions | under | 0.031905349719951404 | 2026-10-28T05:43:27Z | 2026-10-31T23:30:00Z |
| underdog|68231f2d-2350-4cf6-aa11-1eb8922ae8bc | underdog | Chase Brown | Receptions | under | 0.03177557054308333 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|22562c6b-9f93-4984-a0a4-9c04583211de | underdog | Drew Wagner | Receiving Yards | over | 0.031739949607593076 | 2026-10-30T05:46:05Z | 2026-10-31T19:30:00Z |
| underdog|ea50e946-5a1f-4248-a186-6a00b37d7eee | underdog | Justice Hill | Receiving Yards | under | 0.0317235807676185 | 2026-10-28T05:43:27Z | 2026-11-01T18:00:00Z |
| prizepicks|16236999 | prizepicks | Kyler Murray | Rush Yards | under | 0.031657095278137426 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|33f46818-cddb-41ab-a9fb-25a59017fa7e | underdog | Reece Vander Zee | Receptions | under | 0.031621174892085824 | 2026-10-29T05:46:21Z | 2026-10-31T16:00:00Z |
| underdog|67df3123-52a6-49f6-abdd-cc6b817ff9cc | underdog | Devontez Walker | Receptions | over | 0.03138105929047941 | 2026-10-29T05:46:21Z | 2026-11-01T18:00:00Z |
| underdog|3135e7cd-eb18-4f9f-b4f6-04a0850bcc31 | underdog | Sione Vaki | Rush Yards | over | 0.03133578693096406 | 2026-10-30T05:46:05Z | 2026-11-01T18:00:00Z |
| underdog|193613f4-ecf6-4d47-a1a4-8eb577ac8fad | underdog | Puka Nacua | Receptions | under | 0.031332412754902395 | 2026-10-28T05:43:27Z | 2026-11-01T21:05:00Z |
| prizepicks|16364187 | prizepicks | Mike Gesicki | Rec Targets | under | 0.031142143077535156 | 2026-10-29T05:46:21Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|9225533e-66a4-4713-8948-41cc19e76055 | underdog | Colton Joseph | Pass Yards | over | 0.031033154598217205 | 2026-10-30T05:46:05Z | 2026-10-31T16:00:00Z |
| underdog|82eb77cc-0d7d-4a88-81ca-87976f624ba3 | underdog | Kenneth Walker III | Receptions | under | 0.030962031950642066 | 2026-10-29T05:46:21Z | 2026-11-01T21:25:00Z |
| underdog|5124882c-f8a6-4e78-a04d-110145a51a3c | underdog | Arch Manning | Rush Yards | under | 0.030956685466541622 | 2026-10-29T05:46:21Z | 2026-10-31T23:30:00Z |
| underdog|7ec1e3c1-12a5-44b7-a8c4-b1243ccb2016 | underdog | Andre Szmyt | Kicking Points | under | 0.03089301505307862 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|f07ce707-ea65-4fc6-a916-e38e40a044ef | underdog | Kimani Vidal | Receptions | under | 0.03077803679508595 | 2026-10-30T05:46:05Z | 2026-11-01T21:05:00Z |
| underdog|82b555cc-848d-4e23-b158-85217a0cb986 | underdog | Konata Mumpfield | Receptions | over | 0.03054904013493953 | 2026-10-29T05:46:21Z | 2026-11-01T21:05:00Z |
| underdog|8c835faa-8b75-4c85-a171-041dfd067b47 | underdog | Tyler Robles | FG Made | under | 0.030444708444404167 | 2026-10-29T05:46:21Z | 2026-11-01T00:00:00Z |
| underdog|7df467c5-d3c1-4873-926c-4da5c0ac0815 | underdog | Cam Coleman | Receiving Yards | under | 0.03041173081752835 | 2026-10-30T05:46:05Z | 2026-10-31T23:30:00Z |
| underdog|838a86da-33a6-4072-a43a-84084793ee97 | underdog | Gideon Davidson | Rush Yards | under | 0.030286308383850602 | 2026-10-29T05:46:21Z | 2026-10-31T23:00:00Z |
| underdog|c3a160f3-b4fa-4a9c-9b5a-8e19501e21e9 | underdog | Ardell Banks | Receiving Yards | over | 0.03026172523410775 | 2026-10-30T05:46:05Z | 2026-10-31T02:30:00Z |
| underdog|a0747203-74c4-4185-b2bc-0ec6dea596f8 | underdog | Keaton Mitchell | Rush Yards | under | 0.030173522156285992 | 2026-10-30T05:46:05Z | 2026-11-01T21:05:00Z |
