-- Lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in MY MySQL server.
SELECT `score`, `name` FROM `second_table` WHERE score >= 10 OEDER BY `score` DESC;