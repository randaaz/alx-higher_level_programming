-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT n.`title`, m.`name`
  FROM `tv_shows` AS n
       LEFT JOIN `tv_show_genres` AS r
       ON n.`id` = r.`show_id`

       LEFT JOIN `tv_genres` AS m
       ON r.`genre_id` = m.`id`
 ORDER BY n.`title`, m.`name`;
