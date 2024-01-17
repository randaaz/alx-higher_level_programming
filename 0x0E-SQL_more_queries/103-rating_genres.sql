-- lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT `name`, SUM(`rate`) AS `rating`
  FROM `tv_genres` AS n
       INNER JOIN `tv_show_genres` AS m
       ON m.`genre_id` = n.`id`

       INNER JOIN `tv_show_ratings` AS h
       ON h.`show_id` = m.`show_id`
 GROUP BY `name`
 ORDER BY `rating` DESC;
