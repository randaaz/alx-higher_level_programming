-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT m.`name`
  FROM `tv_genres` AS m
       INNER JOIN `tv_show_genres` AS r
       ON m.`id` = r.`genre_id`

       INNER JOIN `tv_shows` AS n
       ON n.`id` = r.`show_id`
       WHERE n.`title` = "Dexter"
 ORDER BY m.`name`;
