-- that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT DISTINCT `name`
  FROM `tv_genres` AS m
       INNER JOIN `tv_show_genres` AS n
       ON m.`id` = n.`genre_id`

       INNER JOIN `tv_shows` AS r
       ON n.`show_id` = r.`id`
       WHERE m.`name` NOT IN
             (SELECT `name`
                FROM `tv_genres` AS m
	             INNER JOIN `tv_show_genres` AS n
		     ON m.`id` = n.`genre_id`

		     INNER JOIN `tv_shows` AS r
		     ON n.`show_id` = r.`id`
		     WHERE r.`title` = "Dexter")
 ORDER BY m.`name`;
