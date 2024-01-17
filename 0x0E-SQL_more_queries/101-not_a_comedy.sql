-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT DISTINCT `title`
  FROM `tv_shows` AS r
       LEFT JOIN `tv_show_genres` AS n
       ON n.`show_id` = r.`id`

       LEFT JOIN `tv_genres` AS m
       ON m.`id` = n.`genre_id`
       WHERE r.`title` NOT IN
             (SELECT `title`
                FROM `tv_shows` AS r
	             INNER JOIN `tv_show_genres` AS n
		     ON n.`show_id` = r.`id`

		     INNER JOIN `tv_genres` AS m
		     ON m.`id` = n.`genre_id`
		     WHERE m.`name` = "Comedy")
 ORDER BY `title`;
