# Pipeline Digest -- 2026-10-27T04:52:33Z

## Run summary
- Ingestion: 30555 rows (PrizePicks OK, Underdog OK)
- Estimation: 30555 rows estimated (from 30555 ingested props)
- CLV logging: 448 newly flagged, 0 newly closed, 460 still open (105876 total ever logged)

## Currently open flags
Sizing is a manual step (sizing_engine.py, Session 2.6) -- this table is what to scan to pick a pair worth sizing.

| flag_id | platform | player_name | stat_type | flagged_side | first_flagged_edge | first_flagged_at | game_start_time |
|---|---|---|---|---|---|---|---|
| underdog|b6dddb16-db76-4006-862c-f709e2c28ab8 | underdog | Baker Mayfield | Pass Yards | under | 0.46923076923076923 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|2f5aaa24-7fb0-41f8-a373-c3b035aa8e86 | underdog | Malik Willis | Pass Yards | under | 0.44253845031977934 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|12009851-2423-4ab3-91bd-f13fd4301a82 | underdog | Josh Allen | Pass Yards | under | 0.42261306532663323 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|2a6bed3b-c7b3-4711-a725-7549471b16c3 | underdog | Bryce Young | Pass Yards | under | 0.4114535454340761 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| underdog|3fafb547-a80e-4119-b750-f8178a9ec1d1 | underdog | Geno Smith | Pass Yards | under | 0.40697585543065895 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|551de737-4ed8-4f82-8609-b1e2a3e0c17e | underdog | Trevor Lawrence | Pass Yards | under | 0.4 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|3c8a224d-a083-4783-83ce-39c3dcbaf581 | underdog | Michael Penix | Pass Yards | under | 0.4 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|0e0c0fdf-9c1f-448a-b3b8-b28c6caefb26 | underdog | Caleb Williams | Pass Attempts | under | 0.4 | 2026-10-27T05:05:06Z | 2026-11-03T01:15:00Z |
| underdog|57dc1a66-d2ad-4f66-ac14-140c57409976 | underdog | Tommy Carr | Pass Yards | under | 0.4 | 2026-10-27T05:05:06Z | 2026-10-31T16:30:00Z |
| underdog|448c0ea7-0f12-4637-b576-8f1f4227331a | underdog | Brice Turang | RBIs | over | 0.3788676236044657 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|87da43a0-1884-4911-b9fa-cc92f8d15e16 | underdog | Bo Nix | Pass Yards | under | 0.3761948122970198 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|8d3d9ebf-754f-45c8-bc75-2547a71fb3ac | underdog | Dawson Knox | Receiving Yards | under | 0.3642857142857143 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|7b31b809-c2af-4bb7-b306-9fadeadd490b | underdog | Aaron Rodgers | Pass Yards | under | 0.3642857142857143 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|51026806-71eb-47e0-b24c-3e735dc9face | underdog | Michael Penix | Pass Attempts | under | 0.36083693901821556 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|e8447c46-2f12-4277-9482-c265cc5c3240 | underdog | Josh Allen | Pass Attempts | under | 0.360606362987979 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|73220374-6ec4-4fac-ab5b-63d5214a74cc | underdog | Kirk Cousins | Pass Yards | under | 0.3573233184784108 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|1da921ec-5da0-4919-8730-2e8848794803 | underdog | Jordan Love | Pass Yards | under | 0.3553322024024601 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| underdog|3c898aa0-cf88-40c7-8f3e-bccf4eb2a341 | underdog | A.J. Brown | Receiving Yards | under | 0.35177664974619294 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|d36d1c96-b26a-46ec-b5e9-46fda3a31296 | underdog | Bhayshul Tuten | Rush + Rec Yards | under | 0.3516191305406252 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16237035 | prizepicks | Josh Allen | Pass Yards | under | 0.35094246505677495 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| prizepicks|16237058 | prizepicks | Michael Penix Jr. | Pass Yards | under | 0.35094246505677495 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| prizepicks|16237032 | prizepicks | Jacoby Brissett | Pass Yards | under | 0.35094246505677495 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| prizepicks|16237034 | prizepicks | Cam Ward | Pass Yards | under | 0.35094246505677495 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| prizepicks|16237064 | prizepicks | Malik Willis | Pass Yards | under | 0.35094246505677495 | 2026-10-27T05:05:06Z | 2026-11-01T16:25:00.000-05:00 |
| prizepicks|16237044 | prizepicks | Justin Herbert | Pass Yards | under | 0.35094246505677495 | 2026-10-27T05:05:06Z | 2026-11-01T16:05:00.000-05:00 |
| prizepicks|16237056 | prizepicks | Baker Mayfield | Pass Yards | under | 0.35094246505677495 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|08c8881f-e513-4c2b-8aa1-aecd77e8918a | underdog | Deshaun Watson | Pass Attempts | under | 0.339509344658637 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|c6b45392-15a5-4784-9f7e-de4a0ccd50be | underdog | Jared Goff | Pass Yards | under | 0.33718592964824123 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16237054 | prizepicks | Jared Goff | Pass Yards | under | 0.33657212623176713 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|86c0f981-7496-4227-9196-e2f09e3cc959 | underdog | Kyler Murray | Pass Yards | under | 0.3360431449180866 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|9774f98f-74a5-4e9d-8086-0b8f1394f05e | underdog | Deshaun Watson | Pass Yards | under | 0.3339921704274391 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|ef658ea7-9d52-4403-a6b4-a380dd35a774 | underdog | Bo Nix | Pass Attempts | under | 0.33329082638649865 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| prizepicks|16237068 | prizepicks | Caleb Williams | Pass Yards | under | 0.32839021953788883 | 2026-10-27T05:05:06Z | 2026-11-02T20:15:00.000-05:00 |
| underdog|132adaf1-78d8-4a53-8003-3d4a67669ae6 | underdog | Drake Maye | Pass Yards | under | 0.326440744778141 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| prizepicks|16237067 | prizepicks | Jayden Daniels | Pass Yards | under | 0.32372482407821346 | 2026-10-27T05:05:06Z | 2026-11-01T20:20:00.000-05:00 |
| underdog|a9c098a9-5051-4b9c-9177-f98d2f838c81 | underdog | Caleb Williams | Pass Yards | under | 0.3207245998457888 | 2026-10-27T05:05:06Z | 2026-11-03T01:15:00Z |
| underdog|41cd46eb-3a8a-4dd5-b1a6-c2b98317813f | underdog | Baker Mayfield | Pass TDs | under | 0.31870442998094306 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|9004081f-ef3d-4c65-b67e-631ef9e307b1 | underdog | Jaylen Wright | Rush Yards | under | 0.31482810842807696 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|39f3f7fc-6c39-444a-897e-8dfbc45427fa | underdog | Sam Darnold | Pass Yards | under | 0.3143741598167539 | 2026-10-27T05:05:06Z | 2026-11-03T01:15:00Z |
| prizepicks|16237026 | prizepicks | Joe Burrow | Pass Yards | under | 0.30244576837217985 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| prizepicks|16237060 | prizepicks | Geno Smith | Pass Yards | under | 0.3012472919929988 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|f0925bda-0452-45bf-b5cb-e99abb959340 | underdog | Daniel Jones | Pass Yards | under | 0.30049745428740415 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|1445d2eb-4f92-4463-b3a1-9d20893d02f3 | underdog | Brice Turang | Batter Walks | over | 0.29519094766619514 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|036b2b4a-4c13-4a88-98c4-08c2f91b6f5b | underdog | Malik Willis | Pass Attempts | under | 0.2950573943673964 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| prizepicks|16239378 | prizepicks | Savion Williams | Rec Targets | under | 0.29408939080290064 | 2026-10-27T05:05:06Z | 2026-10-29T20:15:00.000-04:00 |
| underdog|688d08a6-db4b-4741-9b64-3f2d4083db4c | underdog | Rhamondre Stevenson | Rush Yards | under | 0.29100110024273373 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|e92e5f3e-a2e1-483b-84b1-3fb32369fec3 | underdog | Ollie Gordon | Receiving Yards | under | 0.2898420818744093 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|77134685-90f4-4cf7-b654-07f91bf45e2b | underdog | Jordan Love | Pass TDs | under | 0.28932884359695743 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| underdog|3e004d77-31b6-42d3-b335-ec61b9c5ca37 | underdog | Drake Maye | Pass Attempts | under | 0.28783365045991505 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|0e7ea5ff-7f3e-4fde-8d82-c1f54d190285 | underdog | Bryce Young | Pass Attempts | under | 0.28326692275863596 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| underdog|96197cf8-42ed-46d7-9dc6-75ce2b734496 | underdog | Bhayshul Tuten | Rush Yards | under | 0.2830925953549398 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16237065 | prizepicks | Patrick Mahomes | Pass Yards | under | 0.27446569007052457 | 2026-10-27T05:05:06Z | 2026-11-01T16:25:00.000-05:00 |
| underdog|17dc7cec-3c82-4150-80af-68ab4e38fdf7 | underdog | Patrick Mahomes | Pass Yards | under | 0.27297421579815784 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|cca6f0ed-7d80-4eab-9b96-4203558b22d3 | underdog | Trevor Lawrence | Pass Attempts | under | 0.26915975627016686 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16238609 | prizepicks | Puka Nacua | Rec Yards | under | 0.26601067771574083 | 2026-10-27T05:05:06Z | 2026-11-01T16:05:00.000-05:00 |
| prizepicks|16238598 | prizepicks | Ja'Marr Chase | Rec Yards | under | 0.2595902767393615 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|d11a4e9c-a4c2-4797-af01-622070bdd555 | underdog | Kyler Murray | Pass TDs | under | 0.25843685929932236 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|afcd7eec-7f59-4600-86a0-e8d31c1cade8 | underdog | Geno Smith | Pass Attempts | under | 0.25769563677306406 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|bc54eae1-89f4-4873-956f-e47f7a9c475b | underdog | Matthew Stafford | Pass Yards | under | 0.2573107992331636 | 2026-10-27T05:05:06Z | 2026-11-01T21:05:00Z |
| prizepicks|16237046 | prizepicks | Matthew Stafford | Pass Yards | under | 0.2569273033549908 | 2026-10-27T05:05:06Z | 2026-11-01T16:05:00.000-05:00 |
| underdog|a54a7eda-4c35-4f46-bf44-de48ff2fbb7a | underdog | Taylor Walls | Runs | over | 0.25266615882689003 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|18196574-1ee1-46ca-84b5-d74b3f6018a7 | underdog | Caden Veltkamp | Pass Yards | under | 0.24681744078157286 | 2026-10-27T05:05:06Z | 2026-10-29T23:30:00Z |
| prizepicks|16237069 | prizepicks | Sam Darnold | Pass Yards | under | 0.23929351518982844 | 2026-10-27T05:05:06Z | 2026-11-02T20:15:00.000-05:00 |
| underdog|714c4e03-5b55-4f5c-949c-b056d52f89c5 | underdog | Aaron Rodgers | Pass Attempts | under | 0.23899560341545345 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|d2fab134-e62c-406c-ba21-9462b8717dcc | underdog | Jake Bauers | Batter Walks | over | 0.23843888070692187 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|b871d24e-b512-49bf-af0d-87e4256afb83 | underdog | Jared Goff | Pass Attempts | under | 0.23810199295358325 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|0964d4fd-2061-4374-9c1c-0aa1d0d2e8fd | underdog | Jahmyr Gibbs | Receptions | under | 0.23462427954615162 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|8c6af8a7-19e0-4e82-a98e-88769fe47232 | underdog | Tucker Kraft | Receiving Yards | under | 0.22870157798154256 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| underdog|28b552af-0b9a-4f7a-8167-90e11dd3b5f6 | underdog | Kyle Pitts | Receiving Yards | under | 0.22471131955490853 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|a2b5c67e-ab5a-4ced-98dd-d529549b3670 | underdog | Daniel Jones | Pass Attempts | under | 0.22282919941189783 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|d3529e40-391b-42c2-ada3-d6f7e3d476c0 | underdog | Jaxon Smith-Njigba | Receiving Yards | under | 0.2207891416703074 | 2026-10-27T05:05:06Z | 2026-11-03T01:15:00Z |
| underdog|30c4939c-5645-40ae-8353-daea4cad9a36 | underdog | Savion Williams | Receptions | under | 0.22006641268961324 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| underdog|8fe6381c-70d0-44c4-840e-e579b9212e6b | underdog | Justin Herbert | Pass TDs | under | 0.2167420814479638 | 2026-10-27T05:05:06Z | 2026-11-01T21:05:00Z |
| underdog|0230d4b8-6276-4bfa-aec4-84b8e4d068c2 | underdog | Puka Nacua | Receiving Yards | under | 0.2160146989591477 | 2026-10-27T05:05:06Z | 2026-11-01T21:05:00Z |
| prizepicks|16238606 | prizepicks | Brock Bowers | Rec Yards | under | 0.2140636967499886 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|4cf31bac-ff07-4f85-8c66-eba7199c3f28 | underdog | Baker Mayfield | Pass Attempts | under | 0.21047912545465675 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|0512867b-b0d8-43bd-a2bf-3abc9ca097b0 | underdog | Junior Caminero | Total Bases | over | 0.20944751381215465 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|6a748d90-5fb9-4ae4-87d9-be1bb9b4eef7 | underdog | Josh Allen | Pass TDs | under | 0.20834299379221988 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|27893231-fb65-490d-a9b8-2391c00c9302 | underdog | Savion Williams | Receiving Yards | under | 0.20661248735369653 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| prizepicks|16238594 | prizepicks | Trey McBride | Rec Yards | under | 0.20630682894084595 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|df2a3fc6-9e81-46b9-af61-854f6add8fb5 | underdog | Kyler Murray | Pass Attempts | under | 0.20522682934822212 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|5db3d8d7-75cf-4394-9019-9ddc53548361 | underdog | Brice Turang | Runs | over | 0.2036922823897041 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|4ee9541f-6c2f-4b94-ba5c-93343fafe356 | underdog | Drake London | Receptions | under | 0.20268125700133366 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16237760 | prizepicks | Rhamondre Stevenson | Rush Yards | under | 0.20003838369682592 | 2026-10-27T05:05:06Z | 2026-11-01T16:25:00.000-05:00 |
| underdog|08f11ef5-5c40-4e39-97a6-24d83cfdeb7a | underdog | Liam Hicks | RBIs | over | 0.1987220135603141 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|0631e5d6-eab6-465f-a56e-d362d91226c9 | underdog | Jordan Love | Pass Attempts | under | 0.19733015924696584 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| underdog|50469855-5b2f-44cf-8413-7e8a99d15cd2 | underdog | Bryce Young | Rush Yards | under | 0.19504980897098123 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| underdog|09a6542e-f25f-48dd-9d53-85ac48fa25c1 | underdog | Matthew Golden | Receptions | under | 0.1933475355920763 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| underdog|396fa408-0a5f-4be5-b9a7-b20f30dbd908 | underdog | Parker Washington | Receptions | under | 0.18996406742376704 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|aef90bee-1be6-442e-b1dc-05773d4154a4 | underdog | Jonathan Taylor | Rush Yards | under | 0.18970208620720153 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|9dbda850-eb66-42fe-8b90-11cd826d933e | underdog | Victor Mesa | Runs | over | 0.1890472618154539 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|a2d78b33-b8d2-49cf-8105-3babfaacf592 | underdog | Adam Damante | Pass Yards | under | 0.18833003342862276 | 2026-10-27T05:05:06Z | 2026-10-29T00:00:00Z |
| underdog|db7df02f-c054-41a9-aa50-0fd66fb3afa1 | underdog | Amon-Ra St. Brown | Receiving Yards | under | 0.18760906654565868 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|db576673-9182-47ee-9e98-3b8ef987c596 | underdog | Daniel Jones | Pass TDs | under | 0.18692400580495838 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|2199dc81-1de7-4455-8fe0-745e7215821b | underdog | Richie Palacios | RBIs | over | 0.1850121516717397 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|488ea756-0608-47dc-97ab-7c246ce970a6 | underdog | Kyah Francone | XP Made | under | 0.1782126683184836 | 2026-10-27T05:05:06Z | 2026-10-29T00:00:00Z |
| underdog|684c3765-0511-4cc7-9d8a-5be14ac8cd71 | underdog | Germie Bernard | Receiving Yards | under | 0.17801647476795757 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|3d490363-93ab-4d8d-a549-bf27345b8f62 | underdog | Brock Bowers | Receiving Yards | under | 0.1777841853536105 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|45da0550-9d7c-4ccb-8748-f53598c1778d | underdog | Yandy Díaz | Runs | over | 0.17768595041322277 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|103605f2-9b72-4426-885b-0238715e9ac0 | underdog | Matthew Stafford | Rush Yards | over | 0.17706361202904009 | 2026-10-27T05:05:06Z | 2026-11-01T21:05:00Z |
| underdog|f4157ec2-fa4a-4f3f-b735-c61512d8af08 | underdog | Jonathan Aranda | RBIs | over | 0.17698026147141754 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|cf672a90-aa86-4cd8-8f8b-dd0d13229542 | underdog | Tyler Warren | Receiving Yards | under | 0.17652993569650421 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|74483afd-94fb-455a-93cd-fac3ab6bd4e1 | underdog | Jackson Chourio | Runs | over | 0.17602040816326536 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|a0020a56-eca9-42bc-b548-2457584b7982 | underdog | Parker Washington | Receiving Yards | under | 0.17427174460304196 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|5b0fbf58-2d38-4bfa-a85d-c5ec591d6220 | underdog | Kyle Pitts | Receptions | under | 0.1729010034408106 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|d40fbb26-ef06-498b-a5ce-8c44c352ebb2 | underdog | Garrett Mitchell | Runs | over | 0.1723206568712186 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| prizepicks|16238621 | prizepicks | Jaxon Smith-Njigba | Rec Yards | under | 0.17173160672708232 | 2026-10-27T05:05:06Z | 2026-11-02T20:15:00.000-05:00 |
| underdog|3dbc5709-72cb-4f99-ba9c-fb4babe76cf0 | underdog | Junior Caminero | Runs | over | 0.17028368794326254 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|4b334497-079e-4edb-89d2-f1aab306023d | underdog | Jameson Williams | Receiving Yards | under | 0.17002164741431403 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|263dd844-c611-4d93-9aab-8f0330aea916 | underdog | Nick Minicucci | Pass TDs | under | 0.16869042861255346 | 2026-10-27T05:05:06Z | 2026-10-27T23:00:00Z |
| underdog|8236f68a-f5a5-4ec5-b167-6881a5388e3a | underdog | Taylor Walls | Total Bases | over | 0.16867828304292393 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|ee98fa9b-f145-4378-bf39-5088e377c6f1 | underdog | Christian Yelich | Runs | over | 0.16832388894828765 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|d8ec05fd-5588-43fa-8385-85f5f7c51cb3 | underdog | Chuba Hubbard | Rush + Rec Yards | under | 0.16479397916260208 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| underdog|da678e58-505a-41e6-887a-a2ae327a7148 | underdog | Yandy Díaz | RBIs | over | 0.16397167617839775 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|d3ade481-5528-4676-af9d-75c6d7e2009b | underdog | Trey Smack | Kicking Points | under | 0.16350082484356843 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| underdog|2cf26b57-0452-47fb-9a95-cac7cef34370 | underdog | Colby Parkinson | Receiving Yards | under | 0.16302930851970687 | 2026-10-27T05:05:06Z | 2026-11-01T21:05:00Z |
| underdog|f2a2c26e-ec05-40c1-a275-77c42ff47726 | underdog | Gunner Stockton | Pass Yards | under | 0.1624059560161013 | 2026-10-27T05:05:06Z | 2026-10-31T19:30:00Z |
| underdog|617ee341-d437-4af1-8b70-7876c8ae1ba2 | underdog | Brock Glenn | Pass Yards | under | 0.161719872775533 | 2026-10-27T05:05:06Z | 2026-10-27T23:00:00Z |
| underdog|78c25b5c-13b6-4a3e-99f5-da975e3655e3 | underdog | Tayven Jackson | Pass TDs | under | 0.16170501448583652 | 2026-10-27T05:05:06Z | 2026-10-29T23:30:00Z |
| underdog|39bbd93a-c47e-49d9-8688-d284b1bba708 | underdog | Malik Willis | Pass TDs | under | 0.15983936929525455 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| prizepicks|16238595 | prizepicks | Michael Wilson | Rec Yards | under | 0.1584241015647775 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| prizepicks|16239377 | prizepicks | Tucker Kraft | Rec Targets | under | 0.15579549797772507 | 2026-10-27T05:05:06Z | 2026-10-29T20:15:00.000-04:00 |
| underdog|eaad8225-0b13-489d-9dfb-6a7415e9a871 | underdog | John Metchie III | Receptions | under | 0.15296044248863871 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| underdog|9c22de23-db25-429d-a765-1cacefce1e34 | underdog | Jake Bauers | RBIs | over | 0.15289858987519583 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|301f45d5-2a5a-449b-b397-68ad730d1370 | underdog | Garrett Wilson | Receiving Yards | under | 0.1515587767143275 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|4211182d-42bf-4f3c-b039-1593e4f2effe | underdog | Taylor Walls | Hits | over | 0.15044279275446176 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|35b4ff00-f9b2-4698-b7b7-96e7a724f887 | underdog | Cooper Pratt | RBIs | over | 0.15024867848865975 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|eebe204a-45c0-403b-be16-321a9d1f6a5a | underdog | Rico Dowdle | Rush Yards | under | 0.1502305033665604 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|9566880e-8490-456d-b73a-5984e9ca91ff | underdog | Mark Andrews | Receiving Yards | under | 0.14977065038209925 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|5cb4098b-5bb4-45ef-ba4d-f91a68625257 | underdog | Jalen Coker | Receptions | under | 0.1495115674735762 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| prizepicks|16238597 | prizepicks | Wan'Dale Robinson | Rec Yards | under | 0.1474324804852314 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|f780a01f-c8b0-43bf-8692-d52c6d212ee0 | underdog | J.K. Dobbins | Rush Yards | under | 0.1453612703056476 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|56955058-de76-456b-ac8e-8e0ae8753edd | underdog | Jared Goff | Rush Yards | over | 0.14467131524506371 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|f6910e01-bfc1-4849-9d3d-899b8ee77c6f | underdog | Jahan Dotson | Receptions | under | 0.14404445231008522 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|669e82a1-1b72-4aba-a6c4-9620b6db6fd1 | underdog | David Hamilton | Total Bases | over | 0.1425947219339821 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|8ff5bc02-2292-40f0-9db8-4cf4a53c7659 | underdog | Jake Bauers | Runs | over | 0.14191634100448708 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|b0d1d3de-f70f-4269-8112-3726934f8345 | underdog | Tucker Kraft | Receptions | under | 0.14139810535310193 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| underdog|0f992d93-b9cd-4f6c-937b-e8ec92e61ea8 | underdog | Rhamondre Stevenson | Rush + Rec Yards | under | 0.14121892024690386 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|59da26a9-80c7-4a40-a23b-3757e949b385 | underdog | Jason Myers | FG Made | under | 0.14119220966516732 | 2026-10-27T05:05:06Z | 2026-11-03T01:15:00Z |
| underdog|58f2e2e3-3fa4-4c2a-a63e-0141b379bbe5 | underdog | Dylan Sampson | Receptions | under | 0.14093524678562463 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|9195957f-1ebf-4bf6-a3bd-adb9cf97e092 | underdog | Jonathan Taylor | Rush + Rec Yards | under | 0.14066112038149825 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|42591778-9863-4716-ac27-664fad6b01d1 | underdog | Jackson Chourio | Total Bases | over | 0.1402638403427669 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|ffde9a69-74c0-4fcd-b91d-4e08847ea69f | underdog | Jahiem White | Rush Yards | under | 0.14003704075299583 | 2026-10-27T05:05:06Z | 2026-10-29T23:30:00Z |
| underdog|901aade2-41f4-474e-ac1e-38f6de6f2a7b | underdog | Tetairoa McMillan | Receiving Yards | under | 0.13970313847498894 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| underdog|2e6751e5-b59e-449e-93a3-dd53367f0f2a | underdog | Claire Liu | Double Faults | under | 0.1394666708521951 | 2026-10-27T05:05:06Z | 2026-10-27T06:20:00Z |
| underdog|b2e7b5dc-0058-4dcb-ad3c-df98a1c058e3 | underdog | Malik Washington | Receiving Yards | under | 0.13931606450895906 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|b3e983ff-85d7-4d51-8ed3-8a2d17aa7262 | underdog | MarShawn Lloyd | Receptions | over | 0.13835587367388102 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| underdog|49741af2-ae69-4808-ae58-e77b538cf6d7 | underdog | Denzel Boston | Receptions | under | 0.1380439810510421 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|6aafb4ed-173e-4c20-aa50-9b0737004ea2 | underdog | Mason Taylor | Receptions | under | 0.13759993099979895 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16213266 | prizepicks | Bianca Andreescu | Total Games | over | 0.1372669847131578 | 2026-10-27T05:05:06Z | 2026-10-27T19:00:00.000-04:00 |
| underdog|e6cccaac-edfe-4e89-9a96-bf74eb360ebd | underdog | Camden Coleman | Pass Yards | under | 0.13677399959438263 | 2026-10-27T05:05:06Z | 2026-10-29T23:30:00Z |
| underdog|fa79c358-9169-4e40-b21d-e3f07d1cc7b6 | underdog | Amon-Ra St. Brown | Receptions | under | 0.1362761656863153 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|3f9c4476-78f4-4ad8-95a2-5c8764a4d76e | underdog | Trevor Lawrence | Pass TDs | under | 0.136123979306918 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|96d46b4c-b749-4ea6-a273-6a5e3c236dd5 | underdog | Jonny DeLuca | RBIs | over | 0.13439542483660127 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|b6b37aba-828b-4b2e-a2c1-ca8d4da057c8 | underdog | Wil Lutz | FG Made | under | 0.13416279453077506 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|4fafc90c-1967-429c-bde6-5442a20cdd77 | underdog | Christian Watson | Receptions | under | 0.13380819871657856 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| underdog|2b10ed02-5ce7-457b-bfdf-a82287ccc77c | underdog | William Contreras | RBIs | over | 0.13375725122713072 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| prizepicks|16238619 | prizepicks | Colston Loveland | Rec Yards | under | 0.13325049933820377 | 2026-10-27T05:05:06Z | 2026-11-02T20:15:00.000-05:00 |
| underdog|abe5bb36-eded-4179-8a4d-309e349e055f | underdog | Jordan Addison | Receptions | under | 0.1331259361407876 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16237758 | prizepicks | Kyren Williams | Rush Yards | under | 0.13309444803499015 | 2026-10-27T05:05:06Z | 2026-11-01T16:05:00.000-05:00 |
| underdog|4a64f376-b1b8-4a3d-9825-68f412cc4c63 | underdog | Derrick Henry | Rush Yards | under | 0.1326688171906789 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|66138e31-9fdc-459d-9c38-8c73d6599cd2 | underdog | Easton Messer | Receiving Yards | under | 0.13253386922806 | 2026-10-27T05:05:06Z | 2026-10-29T23:30:00Z |
| underdog|4c9eea8b-78fc-4981-96d9-686ced57e5f9 | underdog | Jordan Addison | Receiving Yards | under | 0.13128005851765068 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|d271bee3-dfd7-48f4-bdce-0cdea8ce8784 | underdog | Matthew Golden | Receiving Yards | under | 0.13021113286631225 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| underdog|a0a1cd84-7140-4b79-94bb-c5dc8cffb254 | underdog | Cairo Santos | FG Made | under | 0.12940227002797755 | 2026-10-27T05:05:06Z | 2026-11-03T01:15:00Z |
| underdog|2adcc255-6e68-4788-bc5f-b4edfe5ca07a | underdog | Jonathan Taylor | Receptions | under | 0.1291779235770657 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|26816d38-8d29-4abd-b2ab-7b69286e6333 | underdog | Brock Glenn | Rush Yards | under | 0.1284973443520998 | 2026-10-27T05:05:06Z | 2026-10-27T23:00:00Z |
| underdog|86bae6e8-dec3-4993-9b03-980cc9218653 | underdog | Jared Goff | Pass TDs | under | 0.12848407209017498 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|216bba8c-5f85-4f2c-ba23-026137213b20 | underdog | Bijan Robinson | Rush + Rec Yards | under | 0.12843905999598837 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|0dced936-2ae8-4afd-8e2c-f1dca49a6ecd | underdog | John Metchie III | Receiving Yards | under | 0.12828215795417186 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| underdog|7f72e2c6-df7e-4077-beda-8d2c7e8cfdcd | underdog | Victor Mesa | RBIs | over | 0.12791783380018673 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|fede6610-0ae3-461a-a528-c9311a69e416 | underdog | Jakobi Meyers | Receiving Yards | under | 0.1270159615157731 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|f8a636b3-6ae2-4531-a6b9-0fe7dc88cee8 | underdog | Sam LaPorta | Receiving Yards | under | 0.12631099432236537 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|b295a429-a121-4509-9517-84f4b7c0a5b8 | underdog | Matthew Stafford | Pass TDs | under | 0.12550262949094826 | 2026-10-27T05:05:06Z | 2026-11-01T21:05:00Z |
| underdog|0ee97bba-0118-41e3-a313-318a402ca03c | underdog | Tayven Jackson | Pass Yards | under | 0.12524863859868518 | 2026-10-27T05:05:06Z | 2026-10-29T23:30:00Z |
| prizepicks|16154947 | prizepicks | Karen Khachanov | Total Games Won | over | 0.1250905288721501 | 2026-10-25T04:41:09Z | 2026-10-26T08:00:00.000-04:00 |
| underdog|431b5ced-46f0-4e85-8666-1a06aeb0cf58 | underdog | Kyren Williams | Rush Yards | under | 0.12457556808536618 | 2026-10-27T05:05:06Z | 2026-11-01T21:05:00Z |
| underdog|b1e653a4-0502-4a31-ad46-4e77f4afec75 | underdog | Ollie Gordon | Rush + Rec Yards | under | 0.12456444308077563 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|1a5870c8-2bf8-45e9-b218-a22be43cc0a0 | underdog | Deshaun Watson | Pass TDs | under | 0.12431385225063618 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|8cdb77cd-3925-4ee5-beb4-812a75583348 | underdog | Colby Parkinson | Receptions | under | 0.12334116882740842 | 2026-10-27T05:05:06Z | 2026-11-01T21:05:00Z |
| underdog|c39f39b8-4b4a-4b41-8cf0-f4aa53094b04 | underdog | Jackson Chourio | RBIs | over | 0.12294760437097224 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|2b7e72b5-e503-4272-8f85-2766fdb25eec | underdog | Bijan Robinson | Receptions | under | 0.12266143699231591 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|7c07455a-f277-48cd-ad69-7b2adac84d3e | underdog | Jake Bates | FG Made | under | 0.1226061500869009 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16237750 | prizepicks | Chase Brown | Rush Yards | under | 0.12258460001677673 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|d10381ad-9fbf-493f-9e41-1adbd4d0c80c | underdog | Liam Hicks | Total Bases | over | 0.12223119520073822 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|d2a26131-d51a-4469-8dbd-f867d7315dcc | underdog | Kenneth Walker III | Receptions | under | 0.12185832046335965 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|cf3f87f9-0fe4-478d-b7bf-b213f8709c04 | underdog | James Cook | Rush + Rec Yards | under | 0.12131404815287872 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|3d64f587-37b5-4075-b4ed-d119e585f6d7 | underdog | Nick Folk | Kicking Points | under | 0.12062606085130745 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|3cb2102b-836e-4cca-af02-d3d30532f4dd | underdog | Blake Corum | Rush Yards | under | 0.11918877358070257 | 2026-10-27T05:05:06Z | 2026-11-01T21:05:00Z |
| underdog|1b2e7691-909c-42f1-93bb-d1d1b80760a3 | underdog | Liam Hicks | Runs | over | 0.11794871794871797 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|0b5a1927-8417-4f0b-9dee-918925f4d70b | underdog | Garrett Mitchell | RBIs | over | 0.11767511010126508 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|a8d65e72-cdf2-46c9-ad06-25735b026521 | underdog | Sam Darnold | Pass Attempts | under | 0.1167625142367642 | 2026-10-27T05:05:06Z | 2026-11-03T01:15:00Z |
| prizepicks|16258952 | prizepicks | Tatjana Maria | 1st Set Total Games | over | 0.11610605024697873 | 2026-10-27T05:05:06Z | 2026-10-27T11:30:00.000-04:00 |
| underdog|cb84333c-b246-4493-acec-acedce99822c | underdog | Caleb Williams | Pass TDs | under | 0.11529745995363427 | 2026-10-27T05:05:06Z | 2026-11-03T01:15:00Z |
| underdog|40e1e8b9-936e-4e15-97c8-77ac12b78573 | underdog | Wil Lutz | Kicking Points | under | 0.11496311756471889 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|7a5b7659-ed00-4f2c-83a5-ad36e76fccec | underdog | Kenny Gainwell | Receiving Yards | under | 0.11453813158973425 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|b7d6662c-6b16-43a0-9c59-996b95142c12 | underdog | Bo Nix | Pass TDs | under | 0.11391526566253873 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|668a4a02-2699-4b23-a66f-b4d78c0ca876 | underdog | Nick Folk | FG Made | under | 0.11296010544794233 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|013d2644-8497-4318-8b71-476975fd8baf | underdog | William Contreras | Runs | over | 0.11270527225583404 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| prizepicks|16195723 | prizepicks | Ben Shelton | Total Games | over | 0.11212453963706981 | 2026-10-25T22:36:01Z | 2026-10-27T07:00:00.000-04:00 |
| underdog|9d23e8da-486f-4cfb-a22c-af77417bfb29 | underdog | Kelby Valsin | Receiving Yards | under | 0.11196392078648598 | 2026-10-27T05:05:06Z | 2026-10-29T23:30:00Z |
| underdog|bf37da89-27eb-43ae-9504-0d71abe11bd5 | underdog | Christian Yelich | RBIs | over | 0.1113691090471276 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|b3804246-c8f4-41b4-a84c-339e80aecf03 | underdog | Travis Kelce | Receiving Yards | under | 0.11127440846014769 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|a76e2c22-fc99-4f26-b305-5156349b714d | underdog | Adonai Mitchell | Receiving Yards | under | 0.11108671220946464 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|0e0d8788-5bca-4091-b00b-dd5e538cb621 | underdog | J.K. Dobbins | Rush + Rec Yards | under | 0.11044817951618235 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|96a403f1-e2ec-4619-a6a4-a3bf0dc3c0b2 | underdog | James Jones | Rush Yards | under | 0.11031009917641377 | 2026-10-27T05:05:06Z | 2026-10-29T00:00:00Z |
| underdog|4b5de504-44f6-404c-a652-b2bb55e1f558 | underdog | Nick Minicucci | Pass Yards | under | 0.10998170440832122 | 2026-10-27T05:05:06Z | 2026-10-27T23:00:00Z |
| underdog|eb4c2d14-178e-431f-801d-2f408a5d44dd | underdog | Kenny Gainwell | Receptions | under | 0.1091654247547108 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|09eea5ba-9827-4e98-8555-effba1bc088d | underdog | Jalen Coker | Receiving Yards | under | 0.10854321201559791 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| underdog|ed014d75-2493-42b8-a5c4-7920bb03f5c7 | underdog | Ajay Allen | Receiving Yards | over | 0.1079223904587191 | 2026-10-27T05:05:06Z | 2026-10-27T23:00:00Z |
| underdog|70a830b9-8d24-44e8-89db-49acb9f4a74c | underdog | Garrett Wilson | Receptions | under | 0.10773634557836387 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|3efdb3f2-4b15-4713-bf57-daa7e4d301a3 | underdog | Bucky Irving | Rush Yards | under | 0.10696383842535351 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|b3275ed5-993c-4333-a20b-2bd31bdee83a | underdog | DK Metcalf | Receiving Yards | under | 0.1066260005770654 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|fe8330d1-90f5-4987-8f6c-074981a6e8d4 | underdog | Ashton Jeanty | Rush + Rec Yards | under | 0.10650003436626809 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|0e2db8a8-b6f9-4bc2-9e45-20958820a5ea | underdog | Brice Turang | Hits + Runs + RBIs | over | 0.10617053564326223 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|182ee136-96d6-4d81-bfe6-e1a26c6e772f | underdog | Jahmyr Gibbs | Rush + Rec Yards | under | 0.10607821147759788 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|f05d8cc4-2b31-433f-8284-73733be5eae0 | underdog | Jordan Love | Rush Yards | under | 0.10597023269085659 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| underdog|3d1d6047-acac-47b2-a581-0b04d6d6af41 | underdog | Jahmyr Gibbs | Receiving Yards | under | 0.10531923406206589 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|8c28b7dc-6bba-47a9-b6ca-fadf53928f3f | underdog | Yandy Díaz | Total Bases | over | 0.10531137798687606 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| prizepicks|16238617 | prizepicks | Chig Okonkwo | Rec Yards | under | 0.1051404094349585 | 2026-10-27T05:05:06Z | 2026-11-01T20:20:00.000-05:00 |
| underdog|3f22f66a-41b9-480a-b6ab-5a45545197f6 | underdog | Pat Freiermuth | Receiving Yards | under | 0.10495785987094197 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|f885c520-71a7-4289-bcc5-e3d8a2d7497e | underdog | Derrick Henry | Rush + Rec Yards | under | 0.10463660855881451 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16258955 | prizepicks | Tatjana Maria | Total Games | over | 0.10442508098452985 | 2026-10-27T05:05:06Z | 2026-10-27T11:30:00.000-04:00 |
| underdog|1f4903f8-0125-4105-8a38-3ebc53d85349 | underdog | Jake Bauers | Hits + Runs + RBIs | over | 0.10420811297651722 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|9c49082a-6082-48bd-a624-5fb9a4843e9d | underdog | Bhayshul Tuten | Receptions | under | 0.10402814965460072 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|b5af50d2-3e3f-462e-9e39-9e89b010076d | underdog | Sal Frelick | Batter Walks | over | 0.10349282296650719 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|f987ad0b-1bba-4f81-b518-b5c3bd202a0f | underdog | Liam Hicks | Hits | over | 0.10258768440272259 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|59905fd2-4d5c-4646-a528-93b6094e86bb | underdog | Jaxon Smith-Njigba | Receptions | under | 0.10234847580734763 | 2026-10-27T05:05:06Z | 2026-11-03T01:15:00Z |
| underdog|fb0ebb52-5cd0-446a-a730-0d6d78e89d20 | underdog | Chuba Hubbard | Rush Yards | under | 0.10227682296643859 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| underdog|068cce30-1352-4c2c-8fe9-0276a711c417 | underdog | Junior Caminero | RBIs | over | 0.10206209453197401 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|74e6cac7-eab2-4c02-822a-1566aa9f481d | underdog | Christian Watson | Receiving Yards | under | 0.10161071542179834 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| underdog|cbb9e39c-6734-4825-b1f9-30470f5f4d46 | underdog | Cooper Pratt | Hits + Runs + RBIs | over | 0.10158832306469467 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|2d16673b-5702-4c4b-aeef-b404eeee834a | underdog | Matthew Stafford | Pass Attempts | under | 0.10135608367717097 | 2026-10-27T05:05:06Z | 2026-11-01T21:05:00Z |
| underdog|ac542ae6-08fd-421e-9c44-a97c3afaa514 | underdog | Jake Bauers | Total Bases | over | 0.10122377622377621 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|2f86a6f0-a4f0-4454-88f1-cb0134e8c932 | underdog | Darnell Washington | Receptions | under | 0.10029195709249383 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|8b4746c7-cb72-4ecb-a00e-935e7143b817 | underdog | Rico Dowdle | Rush + Rec Yards | under | 0.09981514620881438 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|3ea51477-16fc-42a7-9f4e-2a4518606d45 | underdog | Antonia Ruzic | Double Faults | over | 0.09919936493894155 | 2026-10-27T05:05:06Z | 2026-10-27T06:20:00Z |
| underdog|a4ea9448-e18b-4cc5-9365-2d3d1f667e78 | underdog | Justice Hill | Rush + Rec Yards | under | 0.09814132823847843 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|2e0a010a-70b8-4d0d-a210-17287ae2730c | underdog | Ryan Fitzgerald | FG Made | under | 0.09744756346959127 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| underdog|d2c38a60-a480-4c5b-b9cd-6143d0b96db4 | underdog | Jonathan Aranda | Hits + Runs + RBIs | over | 0.09712446211495085 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|4049d15f-3848-4607-8394-ebb7fd28e2c8 | underdog | Jackson Chourio | Hits | over | 0.09660151500649095 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|9e1d3567-3f8f-4d49-b463-e39fb8dfe8eb | underdog | Harrison Butker | FG Made | under | 0.09638494838462963 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|2e1cd42f-d29f-4f32-9a84-351262f050c6 | underdog | Trey Butkowski | FG Made | under | 0.09591456930328557 | 2026-10-27T05:05:06Z | 2026-10-31T16:30:00Z |
| underdog|c58fc0c5-58bb-4a01-8661-2959fdc1a9a1 | underdog | Garrett Mitchell | Hits + Runs + RBIs | over | 0.09575573524648107 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|ab4e51ec-c1b4-4eab-95db-5dc65960c1d0 | underdog | Kyren Williams | Rush + Rec Yards | under | 0.0956441431882935 | 2026-10-27T05:05:06Z | 2026-11-01T21:05:00Z |
| prizepicks|16239374 | prizepicks | Christian Watson | Rec Targets | under | 0.09551948790177134 | 2026-10-27T05:05:06Z | 2026-10-29T20:15:00.000-04:00 |
| underdog|5998434f-948d-4ce6-a07a-c8ea7f5d1c65 | underdog | Jaylen Warren | Receiving Yards | over | 0.09533361799515139 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16154936 | prizepicks | Martin Landaluce | Total Games Won | over | 0.09489887458140489 | 2026-10-25T04:41:09Z | 2026-10-26T08:00:00.000-04:00 |
| underdog|d390a460-936d-4870-9045-5ac203310343 | underdog | William Contreras | Total Bases | over | 0.09484609878310668 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|8e01a8a3-1dbb-4c70-b185-97c0b614f2e7 | underdog | Jonny DeLuca | Hits + Runs + RBIs | over | 0.09442762300745688 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|430e3456-7d0b-428b-91bf-63ce50a18b89 | underdog | Taylor Walls | Hits + Runs + RBIs | over | 0.094209080703896 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|fec089b1-2003-40c0-a50f-ebdc1a159192 | underdog | Trey Smack | FG Made | under | 0.09392813482019169 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| underdog|6207f1a3-38b0-4a82-bcbc-e8c63e0a7181 | underdog | TreVeyon Henderson | Receiving Yards | over | 0.09364324694734338 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|4cdf1787-e3ad-4574-8ffc-e22dc354a7ab | underdog | Jaylen Warren | Rush Yards | under | 0.09328640659838583 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|19796921-ca2c-46b5-8e8a-bb9ee869d6fa | underdog | MarShawn Lloyd | Rush Yards | under | 0.09319042148452561 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| underdog|4e50ec4a-dc6c-4856-a0b5-b6d28d2cfee4 | underdog | Jakobi Meyers | Receptions | under | 0.09288375907862756 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|b9fd522c-e790-46b8-b35b-88e54e06e1ed | underdog | Hunter Henry | Receiving Yards | under | 0.09271224325362548 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|d8053318-9e77-41f4-a87c-da664ca47279 | underdog | James Cook | Rush Yards | under | 0.09180295647498382 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|f2e6ce7c-31af-4d5c-9b37-2d526f4b1656 | underdog | Garrett Mitchell | Batter Walks | over | 0.09162821357943313 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|77dc371f-f1e2-4307-9353-a2e180a8cf09 | underdog | Chris Rodriguez | Rush Yards | under | 0.09130943359892696 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|ef0f3c3c-48ff-482a-a3bf-4e4a444d4d0c | underdog | Jauan Jennings | Receptions | under | 0.09119904435326343 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|ef86a9ad-396b-4897-9f54-3736119b2bcf | underdog | Josh Allen | Rush Yards | under | 0.09109572455919612 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|177547b5-94a6-4d78-91a9-2199205a3905 | underdog | Khalil Shakir | Receiving Yards | under | 0.0909398055872559 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|83f6ee49-29a8-4018-8905-b2b577cb5915 | underdog | Donovan Lewis | Receiving Yards | under | 0.09089595799695926 | 2026-10-27T05:05:06Z | 2026-10-27T23:00:00Z |
| prizepicks|16238614 | prizepicks | Hunter Henry | Rec Yards | under | 0.08957307565733919 | 2026-10-27T05:05:06Z | 2026-11-01T16:25:00.000-05:00 |
| underdog|60cd7c6e-236a-4181-bdb2-3449f79a4cf0 | underdog | Gunner Stockton | Pass TDs | under | 0.08897563769126926 | 2026-10-27T05:05:06Z | 2026-10-31T19:30:00Z |
| underdog|efc3bcd7-af4f-4404-be62-f825c37d4578 | underdog | Laquon Treadwell | Receptions | under | 0.08815905241749789 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|89bf8626-6b97-4a03-a269-6d447eed5ea7 | underdog | Pat Freiermuth | Receptions | under | 0.08793132623164612 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|81d4c33e-1f06-4735-a636-605083d4df90 | underdog | Jonathan Aranda | Batter Walks | over | 0.08737053123955901 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|dddbc903-2c87-42d2-bf02-333cee694469 | underdog | Jason Sanders | FG Made | under | 0.08716403013921992 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|3965f2ed-1638-41cc-b688-55416a871f29 | underdog | Brice Turang | Total Bases | over | 0.0868839998310883 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|9fe9f8ae-c191-46af-84a9-3f490f646600 | underdog | Jonny DeLuca | Total Bases | over | 0.08583916083916088 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|3e230038-0ab6-491b-b0a1-711018ff1dc3 | underdog | Yandy Díaz | Hits | over | 0.08546114296228924 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|00fa635b-a085-487f-969e-9364f8522ac4 | underdog | Andre Szmyt | FG Made | under | 0.08496316251445146 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|4649b523-4c6c-46f6-bbd1-51ca56a68570 | underdog | Polina Kudermetova | Double Faults | under | 0.0843013895975887 | 2026-10-27T05:05:06Z | 2026-10-27T06:20:00Z |
| underdog|edc65d80-633a-49d5-b568-467b9dc26c82 | underdog | Chris Rodriguez | Rush + Rec Yards | under | 0.08351399754029376 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|1de4b590-c9a8-4590-ada7-552bf50550c5 | underdog | Ollie Gordon | Rush Yards | under | 0.08331726721322741 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|329814f9-a9e2-4cca-97a5-37a6a9d98a3d | underdog | Greg Dulcich | Receiving Yards | under | 0.08331303954427971 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|4de8b3a6-4885-404f-ada8-f2e7d9d31db5 | underdog | Garrison Rippa | FG Made | over | 0.08330886964560835 | 2026-10-27T05:05:06Z | 2026-10-29T00:00:00Z |
| underdog|cc8cfbb1-e058-4e01-aaa4-4a08f7cd9394 | underdog | Aaron Rodgers | Rush Yards | over | 0.08323621946349369 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|c124caa4-7f08-4fa3-b0a7-647244cf531a | underdog | Harrison Butker | Kicking Points | under | 0.08302378472777494 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|2d43e549-49ba-4c44-b72c-094dee5d71b6 | underdog | Christian Yelich | Hits + Runs + RBIs | over | 0.08300680661685089 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|d547dbec-c8b5-4eac-bd69-94b4f32957e3 | underdog | David Hamilton | Runs | over | 0.0821917808219178 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|c9b773db-4828-4e5e-9487-5c2a7256c2f9 | underdog | Richie Palacios | Batter Walks | over | 0.08184312131680552 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| prizepicks|16237753 | prizepicks | Derrick Henry | Rush Yards | under | 0.08183379413197434 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|9cb03ee4-ac87-42d2-98ac-d531fdd9ca53 | underdog | Junior Caminero | Hits | over | 0.08170070725203682 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| prizepicks|16237756 | prizepicks | Ashton Jeanty | Rush Yards | under | 0.0816051738093021 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|ce1fe404-32bc-42d9-9b49-cab4bf747245 | underdog | Daniel Jones | Rush Yards | under | 0.08156509285685742 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|68246aad-20fd-405d-80db-3ad12ff7a40b | underdog | Kenyon Sadiq | Receptions | under | 0.0809538714276471 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|2779b258-103f-4447-bbd2-4e32de9a6119 | underdog | Kyler Murray | Rush Yards | under | 0.0807146302213625 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|87384d05-6b0b-41cc-be57-65b4a4195a0c | underdog | Chris Boswell | FG Made | under | 0.08060150764940355 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|af47f3d7-7a13-4d4c-a07e-e37440eb8e97 | underdog | Jauan Jennings | Receiving Yards | under | 0.0801424432343455 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|2809e781-f54d-46a4-ad79-f81f9117d4a0 | underdog | Keon Coleman | Receiving Yards | under | 0.07975433948078203 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|17c26024-188c-4c83-b07f-02d0bbe0431a | underdog | Ryan Fitzgerald | Kicking Points | under | 0.07963366790517856 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| underdog|a5e8c666-ecef-4176-8b5a-c79039669f0d | underdog | Patrick Mahomes | Rush Yards | under | 0.07958627648203864 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|e2692ca9-45cb-4e9d-ae48-bd8f36e8f770 | underdog | Kenneth Walker III | Receiving Yards | under | 0.07925791496494905 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|53a76285-9d03-4715-95bd-32f92c38b675 | underdog | Cooper Pratt | Runs | over | 0.0790784557907846 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|97184200-5077-4667-bd97-4bf6317675c2 | underdog | Isaac TeSlaa | Receptions | under | 0.07907295172171624 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|29a57594-563b-446e-b1a8-c3d405a95378 | underdog | Sam Darnold | Pass TDs | under | 0.07875391297959822 | 2026-10-27T05:05:06Z | 2026-11-03T01:15:00Z |
| underdog|29a958df-a2b1-41e5-9344-22b37cb26cb1 | underdog | Mason Taylor | Receiving Yards | under | 0.07765735031426335 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|3e1c51e0-a50c-46a5-a434-67b4c8ad9c63 | underdog | Jonathan Aranda | Total Bases | over | 0.07683374857480685 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|3c514266-18c3-470f-84b1-da3e8396317d | underdog | Sam LaPorta | Receptions | under | 0.07679022400127311 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|125c65b2-289f-43f2-9892-bf7f177aba07 | underdog | Chandler Simpson | RBIs | under | 0.07657657657657657 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|a74d04f7-9182-4e32-bbfa-53dc7368a303 | underdog | William Contreras | Hits + Runs + RBIs | over | 0.07655586118126945 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|0ebcf308-a8de-44ee-97cc-b2c9a347875b | underdog | Drake London | Receiving Yards | under | 0.07608032624515215 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|68e22951-6601-471d-a12e-fbaea9277356 | underdog | Rashod Bateman | Receiving Yards | under | 0.07606275380805294 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|8089a9db-637f-4e3d-8276-c18af2133a7e | underdog | Zay Flowers | Receiving Yards | under | 0.07602980799376313 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|ab4c4291-4fa3-4224-8f91-f1a8fb579e07 | underdog | J.K. Dobbins | Receptions | under | 0.07588074058074556 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|a471fcf1-a2a9-4bc8-95ee-33ca13fe3d7d | underdog | Jason Sanders | Kicking Points | under | 0.07535210830958228 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|447ef2be-9aed-498c-b0c9-a847a6c755d8 | underdog | Michael Mayer | Receiving Yards | under | 0.07524277884476527 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|a01ec37f-65ba-4176-afa3-c518f1b0c6e6 | underdog | Spencer Shrader | FG Made | over | 0.07516924076136433 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16238615 | prizepicks | Travis Kelce | Rec Yards | under | 0.07491212238443534 | 2026-10-27T05:05:06Z | 2026-11-01T16:25:00.000-05:00 |
| prizepicks|16238380 | prizepicks | Tereza Valentova | Break Points Won | under | 0.07456322157528728 | 2026-10-27T05:05:06Z | 2026-10-27T02:00:00.000-04:00 |
| underdog|c1b8e741-c488-4ec2-ba8a-ade9f6427194 | underdog | Trey Butkowski | XP Made | under | 0.07393229451427985 | 2026-10-27T05:05:06Z | 2026-10-31T16:30:00Z |
| underdog|d3216838-f5d5-4e96-8309-3e1a56cefd4a | underdog | Sal Frelick | Hits + Runs + RBIs | over | 0.07388935881551223 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|ba1915d1-b85d-4e78-8f60-fc7531250479 | underdog | David Hamilton | RBIs | under | 0.07379134860050895 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|d86ec519-b0e8-4c86-bcf2-513b73e4a29e | underdog | Christian Yelich | Batter Walks | over | 0.07373532068654026 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|ce6e4bca-e4dd-4f39-a2d2-f5726f2e0057 | underdog | KC Concepcion | Receptions | under | 0.07353629953328678 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16237020 | prizepicks | Patrick Mahomes | Rush Yards | under | 0.07352649265323374 | 2026-10-27T05:05:06Z | 2026-11-01T16:25:00.000-05:00 |
| underdog|902cbe97-9332-4c6a-a902-03593cb46651 | underdog | Rico Dowdle | Receptions | under | 0.07313092583642589 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|395572e4-c981-494f-a90b-5c2589fd35b2 | underdog | Brice Turang | Hits | over | 0.0729286800896759 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|20499aa2-4d98-407b-b27e-d0df2a75eb06 | underdog | Tereza Valentova | Double Faults | over | 0.07279861763519457 | 2026-10-27T05:05:06Z | 2026-10-27T06:20:00Z |
| underdog|491a6e6b-b107-4a93-a23b-fcbc90a1dec2 | underdog | Justice Hill | Rush Yards | under | 0.07278975670400667 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|c3f6dbbe-f79d-4e3d-adc2-755392988b2a | underdog | Drake Maye | Pass TDs | under | 0.07237975805283348 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|e70899ec-2d6f-45a9-ba4c-3bd042d99cd0 | underdog | Harold Fannin | Receptions | under | 0.07210251211434926 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|127149bb-3491-47d8-a424-a412b2859785 | underdog | Blake Corum | Rush + Rec Yards | under | 0.0718580976652794 | 2026-10-27T05:05:06Z | 2026-11-01T21:05:00Z |
| underdog|45b2cebd-3957-48e7-8e14-9609e517784f | underdog | J.K. Dobbins | Receiving Yards | over | 0.07179068462409405 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| prizepicks|16239373 | prizepicks | Tetairoa McMillan | Rec Targets | under | 0.07177953528082537 | 2026-10-27T05:05:06Z | 2026-10-29T20:15:00.000-04:00 |
| underdog|c46b5924-22eb-404f-aaa1-b518e6d87289 | underdog | Dylan Sampson | Receiving Yards | under | 0.07158252096444151 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|d5c94eed-cb63-496b-a373-37c5050d6502 | underdog | Caden Creel | Pass Yards | under | 0.07107631370772871 | 2026-10-27T05:05:06Z | 2026-10-29T00:00:00Z |
| underdog|347e949c-aed0-4263-80b1-bf253386ea34 | underdog | Ashton Jeanty | Rush Yards | under | 0.07098329396922187 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16195673 | prizepicks | Taylor Fritz | Total Games | over | 0.07095837171967034 | 2026-10-25T22:36:01Z | 2026-10-27T07:00:00.000-04:00 |
| underdog|aa32bf3e-4612-4433-960c-77abf50aeff0 | underdog | Brenton Strange | Receiving Yards | under | 0.07082871978056027 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|9eb907ba-1f51-4385-a30b-efb9c1576b37 | underdog | Chase McLaughlin | FG Made | under | 0.0707192810705145 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|a28a3a92-e695-4545-be4d-7f20f3c2cf85 | underdog | Dalton Kincaid | Receptions | under | 0.07001654956510595 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|3deaf994-ff56-4ada-a24b-c50218707c10 | underdog | Jaylen Warren | Receptions | under | 0.06981076975127332 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|59692063-d40c-4df7-9fd8-c1285ce2abad | underdog | Christian Yelich | Total Bases | over | 0.06944444444444442 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|dd1a8b64-c7cb-4bf4-a2b1-e409957fec6d | underdog | KC Concepcion | Receiving Yards | under | 0.06928901838504875 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|08d643d4-34f9-4e3a-93f5-0849e2aabe4e | underdog | Jahmyr Gibbs | Rush Yards | under | 0.06841277821264247 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|00c24b9b-5ce5-4981-a2eb-9584c4e5b498 | underdog | Brock Glenn | Pass TDs | under | 0.06778029902931004 | 2026-10-27T05:05:06Z | 2026-10-27T23:00:00Z |
| underdog|19132c17-768e-4303-9c35-b68803bdb8f7 | underdog | Kyah Francone | FG Made | under | 0.06771290196103996 | 2026-10-27T05:05:06Z | 2026-10-29T00:00:00Z |
| underdog|b622aa2c-0d12-462c-afde-e9cdc8be719d | underdog | Malik Willis | Rush Yards | under | 0.06729655324879846 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|79184041-e32c-4b52-abe2-42ccb845e454 | underdog | Justice Hill | Receiving Yards | under | 0.06727835725008147 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16239375 | prizepicks | Matthew Golden | Rec Targets | under | 0.06649919849969588 | 2026-10-27T05:05:06Z | 2026-10-29T20:15:00.000-04:00 |
| prizepicks|16152548 | prizepicks | Lilli Tagger | 1st Set Total Games | over | 0.06532227291338599 | 2026-10-25T04:41:09Z | 2026-10-25T23:00:00.000-04:00 |
| underdog|e6349dd0-105e-4e72-bea2-3b232bbbd579 | underdog | Ajay Allen | Rush Yards | under | 0.06510000303533636 | 2026-10-27T05:05:06Z | 2026-10-27T23:00:00Z |
| underdog|92264686-c923-4e85-9a8f-33000e19184e | underdog | Chandler Simpson | Total Bases | over | 0.06460839457513923 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|d0b88cd8-3cb3-4478-b523-f64597760969 | underdog | Geno Smith | Rush Yards | under | 0.06435089670437177 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|46ae5717-8bfd-406a-80ca-d4bf7968641d | underdog | Richie Palacios | Total Bases | over | 0.06373322809786897 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|eb706701-7752-42c9-b941-d781701160a7 | underdog | MarShawn Lloyd | Rush + Rec Yards | under | 0.06296971700294285 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| underdog|829af19d-6d7a-4c67-ad2d-e7700466a300 | underdog | Ashton Jeanty | Receiving Yards | over | 0.06284370429834163 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|bbb87a92-fdcb-4e0a-a501-3a3cbe524779 | underdog | Chris Rodriguez | Receiving Yards | over | 0.06234948855341682 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|5e3a8576-196b-476b-ae73-9ea4dbc90082 | underdog | Adam Damante | Pass TDs | under | 0.062140738439557364 | 2026-10-27T05:05:06Z | 2026-10-29T00:00:00Z |
| prizepicks|16237751 | prizepicks | Tony Pollard | Rush Yards | under | 0.06140796389369363 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|7725104f-bdb6-4a8b-b4dd-872d39f95400 | underdog | T.J. Hockenson | Receptions | under | 0.06125765068766775 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16207831 | prizepicks | Susan Bandecchi | Total Games | over | 0.06123552648341468 | 2026-10-27T05:05:06Z | 2026-10-27T11:20:00.000-04:00 |
| underdog|44d5b677-09cd-41a2-8a09-7bde4a19229b | underdog | DeMario Douglas | Receiving Yards | under | 0.06108729984830874 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|d2a15f31-50f0-4ddb-9713-63caf82b161f | underdog | Bijan Robinson | Receiving Yards | under | 0.0608263421986458 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|8b6205f2-d917-417d-8d91-90bc4720c882 | underdog | Kyren Williams | Receiving Yards | over | 0.06069220762746541 | 2026-10-27T05:05:06Z | 2026-11-01T21:05:00Z |
| underdog|08301f8a-0c44-4f66-8a15-9438be96f70d | underdog | Jake Bates | Kicking Points | under | 0.059904580386489825 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|3026976c-9e97-4ac0-b388-38122ef04d9e | underdog | Bijan Robinson | Rush Yards | under | 0.0593041313288305 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|5fa63acb-82d9-454b-aa06-0b1b0ea67bb5 | underdog | Keenan Allen | Receiving Yards | under | 0.059092087872505084 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|1909e47a-8882-45fe-a5ac-4ca977f1cf90 | underdog | Bryce Young | Pass TDs | under | 0.05906568723340133 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| underdog|98e2ad2f-6b25-437a-afa5-a57e1542c04f | underdog | Tommy Carr | Pass TDs | under | 0.05855747102412334 | 2026-10-27T05:05:06Z | 2026-10-31T16:30:00Z |
| underdog|99435ce0-ecc7-48a1-9d38-2afa8a4d9c9a | underdog | Victor Mesa | Hits | over | 0.05783726822620139 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| prizepicks|16238596 | prizepicks | Carnell Tate | Rec Yards | under | 0.05717982684838552 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|07105652-51cb-4873-af22-74071f594dd2 | underdog | Caden Creel | Pass TDs | over | 0.05688253277316674 | 2026-10-27T05:05:06Z | 2026-10-29T00:00:00Z |
| underdog|45215d0f-586b-451b-ba64-13fad422b3b6 | underdog | Jonathan Aranda | Hits | over | 0.05683144448695099 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|a8727970-24f6-4fd7-a35c-483314966427 | underdog | William Contreras | Batter Walks | over | 0.0564674604092012 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|92511c19-28cc-42f0-9b37-6fa09efdc07b | underdog | Junior Caminero | Batter Walks | over | 0.0564674604092012 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|082236d5-b4c7-49e8-9bd7-efd0f4950cc2 | underdog | Victor Mesa | Total Bases | over | 0.05630030569032729 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|534639cf-dfef-43e9-a654-d0e1df93574f | underdog | Cairo Santos | Kicking Points | under | 0.056155326916546455 | 2026-10-27T05:05:06Z | 2026-11-03T01:15:00Z |
| underdog|84f851cb-cc37-4d00-8260-116ed42334ff | underdog | Will Reichard | FG Made | under | 0.05615139676343428 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|3612e26d-dc02-4174-8e0e-e28e06793eac | underdog | MarShawn Lloyd | Receiving Yards | over | 0.055857262958305065 | 2026-10-27T05:05:06Z | 2026-10-30T00:15:00Z |
| underdog|53bcebff-e936-4c39-b65f-3e098f1c4c2d | underdog | Kenneth Walker III | Rush + Rec Yards | under | 0.055551810824034376 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|04cbfc07-1377-4529-aac1-6d98f0c97753 | underdog | Junior Caminero | Hits + Runs + RBIs | over | 0.055311426932114216 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| prizepicks|16256997 | prizepicks | Oksana Selekhmeteva | Total Games | over | 0.05496417504404205 | 2026-10-27T05:05:06Z | 2026-10-27T09:00:00.000-04:00 |
| underdog|e86eedcd-1459-4214-9c2c-57d157c06064 | underdog | Griffin Jax | Strikeouts | under | 0.054697030970244476 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| prizepicks|16239372 | prizepicks | Jalen Coker | Rec Targets | under | 0.05453440832411327 | 2026-10-27T05:05:06Z | 2026-10-29T20:15:00.000-04:00 |
| underdog|8230f1a8-97f9-4a79-b2fb-a7b30eaff15f | underdog | Bhayshul Tuten | Receiving Yards | under | 0.05432255572250255 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16238620 | prizepicks | Rome Odunze | Rec Yards | under | 0.054258843532627 | 2026-10-27T05:05:06Z | 2026-11-02T20:15:00.000-05:00 |
| underdog|f0a19a7f-3b51-4560-ac6e-749bf9bd2956 | underdog | Brenton Strange | Receptions | under | 0.054233780136315524 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|9002cffa-4e07-4cd9-9f79-3deca961e530 | underdog | Cooper Pratt | Hits | over | 0.053844564679588314 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| prizepicks|16237752 | prizepicks | James Cook III | Rush Yards | under | 0.05257854707589438 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|a688a6ab-bc4f-4c7b-b534-3f83979f56ab | underdog | Jameson Williams | Receptions | under | 0.05226576102064362 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|f8133e41-57ff-4289-9536-c545549e15b1 | underdog | Sean Wilson | Receiving Yards | under | 0.052107191756475046 | 2026-10-27T05:05:06Z | 2026-10-27T23:00:00Z |
| prizepicks|16151763 | prizepicks | Himeno Sakatsume | Total Games Won | over | 0.051990749745927656 | 2026-10-25T04:41:09Z | 2026-10-25T21:30:00.000-04:00 |
| underdog|1b308860-c3aa-4d2c-b859-533c8ad7c678 | underdog | Adonai Mitchell | Receptions | under | 0.05122663560872576 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|5d7629c0-a113-4329-965d-7d12b1b4e24d | underdog | Chandler Simpson | Runs | over | 0.05110642781875657 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|679e49b0-e69f-4a68-9ca8-8914edf87705 | underdog | Cooper Pratt | Batter Walks | over | 0.05046635576282482 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|dc92b219-5a6a-4fab-b0b2-58555215ae32 | underdog | William Contreras | Hits | over | 0.0503142001248339 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|6ccba608-8e28-479b-9ef2-d4419ed32b0d | underdog | Deshaun Watson | Rush Yards | under | 0.05015785585134336 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|8fdc408a-29d2-451e-b1ad-f4ae68023071 | underdog | T.J. Hockenson | Receiving Yards | under | 0.04970792234126764 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|e7d713d1-85ad-4d75-bf34-127d6f414297 | underdog | Baker Mayfield | Rush Yards | under | 0.04958866075240009 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16238616 | prizepicks | Kenneth Walker III | Rec Yards | under | 0.04880478274953093 | 2026-10-27T05:05:06Z | 2026-11-01T16:25:00.000-05:00 |
| underdog|012e961f-94bf-4ec0-b8c3-6ea94968be2d | underdog | Jake Bauers | Hits | over | 0.04767377255721439 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| prizepicks|16196601 | prizepicks | Giovanni Mpetshi Perricard | Total Games Won | over | 0.047423431354667755 | 2026-10-26T04:44:02Z | 2026-10-27T07:00:00.000-04:00 |
| prizepicks|16237001 | prizepicks | Jared Goff | Rush Yards | over | 0.04739043004803156 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|321222b5-60cd-4361-8aea-73fc2575843a | underdog | Camden Coleman | Pass TDs | under | 0.047231747567130555 | 2026-10-27T05:05:06Z | 2026-10-29T23:30:00Z |
| underdog|2c10d59f-2805-4247-b3a9-7f132630e8b7 | underdog | Caleb Douglas | Receiving Yards | under | 0.04572395459474321 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|852a343a-05c9-4733-9211-ab46e393abdc | underdog | Dalton Kincaid | Receiving Yards | under | 0.045660027494306754 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|029089b4-5105-4892-89af-b14744e8cfb5 | underdog | Jonathan Stafford | Receiving Yards | under | 0.04565336534325959 | 2026-10-27T05:05:06Z | 2026-10-27T23:00:00Z |
| underdog|81094c7f-e00a-4afa-8d0b-e73ba3a843db | underdog | Davis Allen | Receiving Yards | under | 0.045594359540911955 | 2026-10-27T05:05:06Z | 2026-11-01T21:05:00Z |
| underdog|a711ba7a-ddac-4e28-a617-94d38559239c | underdog | Efton Chism | Receiving Yards | under | 0.045430132367579756 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|c000965f-9220-48af-a50e-e406a9b82207 | underdog | Patrick Mahomes | Pass TDs | under | 0.044605755569356864 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|07c9159e-953d-4ca9-8a3d-7f2c24f3b622 | underdog | Konata Mumpfield | Receiving Yards | under | 0.04449810098666451 | 2026-10-27T05:05:06Z | 2026-11-01T21:05:00Z |
| underdog|a59eab77-29bf-422a-8460-35c449cac12a | underdog | Kirk Cousins | Pass TDs | under | 0.044346815076756196 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|198884fe-d6ca-4b36-ae25-b5ac648d7ba6 | underdog | Isaac TeSlaa | Receiving Yards | over | 0.04387998320763925 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|7db7fbf5-59dc-48bb-a58a-82abe396aa29 | underdog | Jaylen Warren | Rush + Rec Yards | under | 0.0436668571974157 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|24c3f91c-86a7-4dda-9598-84626220e5fa | underdog | Sal Frelick | Total Bases | over | 0.04332506483256282 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|7c53d42e-f09c-4fce-849f-486c8dfe6d2b | underdog | Jonny DeLuca | Hits | over | 0.042978548076292644 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|51d46586-a523-4495-90f8-ba3a7a79a2ca | underdog | Will Kacmarek | Receiving Yards | over | 0.042084427220204 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|c15e674d-1cff-45ca-856b-4c480e003161 | underdog | Josh Cameron | Receiving Yards | over | 0.04200192948698528 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|3b28befe-ffab-48de-94a7-aec131ad5e79 | underdog | Harold Fannin | Receiving Yards | under | 0.04179548726493032 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|8dd20ddf-9d01-4078-8e3c-311b59ce525a | underdog | Nate Boerkircher | Receiving Yards | under | 0.04155813247968276 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16172817 | prizepicks | Alejandro Tabilo | Total Games Won | over | 0.04147539456045368 | 2026-10-25T22:36:01Z | 2026-10-27T07:00:00.000-04:00 |
| underdog|5606a896-094d-4881-8dc0-335fec3d998c | underdog | Mike Washington | Rush Yards | under | 0.04074539618844153 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|fac6134d-822d-44dc-9f73-a71adfd62ab0 | underdog | Kyren Williams | Receptions | over | 0.03984826894881116 | 2026-10-27T05:05:06Z | 2026-11-01T21:05:00Z |
| underdog|823c1fe8-6645-4f60-af72-b25f78028db7 | underdog | Kenneth Walker III | Rush Yards | under | 0.03980442229081527 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| prizepicks|16197727 | prizepicks | Rinky Hijikata | Total Games Won | over | 0.039454046045379165 | 2026-10-26T04:44:02Z | 2026-10-27T07:00:00.000-04:00 |
| underdog|a8c69f5c-737a-4372-8f7b-61d4588c6428 | underdog | Taylor Walls | Batter Walks | under | 0.03925468864171466 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|d06eb894-124b-4188-9763-d586cc1def8f | underdog | Tyler Warren | Receptions | under | 0.039251759862195756 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|ba5b752c-a956-46bc-8f78-425674b1c328 | underdog | Josh Downs | Receptions | under | 0.038610418627245346 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|996d35bb-4073-4821-88e5-aae87e2c71d7 | underdog | TreVeyon Henderson | Rush + Rec Yards | under | 0.038604363743593106 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|178431a1-f0fe-4939-bf64-ca52aeaf6d23 | underdog | Michael Penix | Pass TDs | under | 0.03824422373301384 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|9b0235e9-f2ea-409d-9c8f-a93274da2a07 | underdog | Jonathan Aranda | Runs | over | 0.03803697300172887 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|5d02b860-79d7-44a4-ad10-fc9a11ad352d | underdog | Jonathan Taylor | Receiving Yards | over | 0.03782774826923374 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16151769 | prizepicks | Leylah Fernandez | Total Games | over | 0.037775107846283684 | 2026-10-25T04:41:09Z | 2026-10-25T21:30:00.000-04:00 |
| underdog|5abeb1de-f3da-498b-996e-31744969aabe | underdog | Jackson Chourio | Batter Walks | over | 0.03764302059496566 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|a6465eb4-f35b-4df3-96fa-5fb54b912ba0 | underdog | Josh Cameron | Receptions | over | 0.03708353453092156 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16203523 | prizepicks | Fiona Ferro | Total Games | over | 0.03706510911307881 | 2026-10-27T05:05:06Z | 2026-10-27T12:40:00.000-04:00 |
| underdog|c202626d-b120-4dcb-b6f5-f780fcc05670 | underdog | Chase McLaughlin | Kicking Points | under | 0.036936611973116484 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|ad0ab0a2-d9e4-4e95-a294-1e3d5a21bc4a | underdog | Caden Veltkamp | Pass TDs | over | 0.03693271208921112 | 2026-10-27T05:05:06Z | 2026-10-29T23:30:00Z |
| prizepicks|16151745 | prizepicks | Jasmine Paolini | Total Games Won | over | 0.036710637312866834 | 2026-10-25T22:36:01Z | 2026-10-26T21:30:00.000-04:00 |
| underdog|331fd1c9-ac63-4ce8-b35f-6a26d2bc3576 | underdog | Keenan Allen | Receptions | under | 0.03657607896715964 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|9655fee3-9390-413f-9bdb-e9d4b1f221d8 | underdog | Liam Hicks | Batter Walks | over | 0.03637094920707884 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|c7e7a148-f8c4-4cad-88bc-76bcb8c8e203 | underdog | Jason Myers | Kicking Points | under | 0.03595495125259396 | 2026-10-27T05:05:06Z | 2026-11-03T01:15:00Z |
| underdog|1c8521fd-b3ef-4aa5-a25f-e726ba7aa98b | underdog | Garrison Rippa | XP Made | under | 0.03594720993511191 | 2026-10-27T05:05:06Z | 2026-10-29T00:00:00Z |
| underdog|5af6ae2a-fc2f-4ccd-abc6-278d69a148a4 | underdog | Yandy Díaz | Hits + Runs + RBIs | over | 0.03593870036632851 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|60dcd824-4333-4248-9adb-7a2d45a8e21d | underdog | Aaron Rodgers | Pass TDs | over | 0.035917777674994156 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|1320bb10-fdb7-48f5-80be-a63f6fd45f5e | underdog | Germie Bernard | Receptions | under | 0.03586978319845402 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|df4eddf1-d62b-4626-8513-2321a74e6be2 | underdog | Drake Maye | Rush Yards | under | 0.03560607974517194 | 2026-10-27T05:05:06Z | 2026-11-01T21:25:00Z |
| underdog|579466c0-c1f1-4bb6-bade-551753e538f0 | underdog | Bucky Irving | Receiving Yards | under | 0.035277747501728185 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|87f9bdf4-f40f-4b04-9ebd-add8492f187a | underdog | Jerry Jeudy | Receiving Yards | under | 0.03475932480352539 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|2210b671-ac1d-49a1-8793-a4f2b60527b4 | underdog | Katie Volynets | Double Faults | over | 0.034363058855489736 | 2026-10-27T05:05:06Z | 2026-10-27T05:10:00Z |
| underdog|a5dbbd3f-374b-43e1-b649-fa353744f714 | underdog | Deondre Johnson | Receiving Yards | under | 0.0341940966911346 | 2026-10-27T05:05:06Z | 2026-10-29T00:00:00Z |
| prizepicks|16236993 | prizepicks | Aaron Rodgers | Rush Yards | over | 0.03417868452026862 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| underdog|86e0c8b8-63e2-4815-a726-0c209fdb2751 | underdog | Caden Creel | Rush Yards | under | 0.03416203911054905 | 2026-10-27T05:05:06Z | 2026-10-29T00:00:00Z |
| underdog|b6d0b727-a1c5-4b46-a33f-d1812b1d91ea | underdog | Josh Downs | Receiving Yards | under | 0.0335880037665488 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|7f1d485a-b569-49f9-96ce-84f9a6aa133c | underdog | Yandy Díaz | Batter Walks | under | 0.03305209698558331 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|5f2d19d8-4bbb-4ea1-a272-1c7cdd003398 | underdog | Dylan Sampson | Rush + Rec Yards | under | 0.03267139201557545 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|1f68e0f5-4758-426a-a308-b5c68e1c8048 | underdog | Sam Darnold | Rush Yards | over | 0.0325476533253789 | 2026-10-27T05:05:06Z | 2026-11-03T01:15:00Z |
| prizepicks|16172840 | prizepicks | Stan Wawrinka | Total Games Won | over | 0.03250845234094224 | 2026-10-27T05:05:06Z | 2026-10-27T14:10:00.000-04:00 |
| underdog|6a5075b4-051f-4846-8678-2e4983400ece | underdog | Richie Palacios | Hits | over | 0.03236397920058531 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
| underdog|3c7d6af2-24a4-4712-868a-a3ddc96c35d6 | underdog | Bucky Irving | Receptions | over | 0.031934092041214335 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| prizepicks|16230430 | prizepicks | Karl Hein | Goalie Saves | under | 0.03183380071870601 | 2026-10-27T05:05:06Z | 2026-10-27T15:45:00.000-04:00 |
| prizepicks|16236999 | prizepicks | Kyler Murray | Rush Yards | under | 0.031657095278137426 | 2026-10-27T05:05:06Z | 2026-11-01T13:00:00.000-05:00 |
| prizepicks|16154930 | prizepicks | Alexander Zverev | Total Games | over | 0.031487431646138764 | 2026-10-25T22:36:01Z | 2026-10-27T08:30:00.000-04:00 |
| underdog|7ec1e3c1-12a5-44b7-a8c4-b1243ccb2016 | underdog | Andre Szmyt | Kicking Points | under | 0.03089301505307862 | 2026-10-27T05:05:06Z | 2026-11-01T18:00:00Z |
| underdog|79b5ec63-5db4-4bd0-a37d-a96523bc79d1 | underdog | Cooper Pratt | Total Bases | under | 0.030136518285478364 | 2026-10-27T05:05:06Z | 2026-10-28T00:00:00Z |
