-- lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT n.`title`
  FROM `tv_shows` AS n
       INNER JOIN `tv_show_genres` AS m
       ON n.`id` = m.`show_id`

       INNER JOIN `tv_genres` AS r
       ON r.`id` = m.`genre_id`
       WHERE r.`name` = "Comedy"
 ORDER BY n.`title`;
