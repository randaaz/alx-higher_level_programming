-- lists all shows contained in the database hbtn_0d_tvshows.
SELECT m.`name` AS `genre`, COUNT(*) AS `number_of_shows` FROM `tv_genres` AS m INNER JOIN `tv_show_genres` AS r ON m.`id` = r.`genre_id` GROUP BY m.`name` ORDER BY `number_of_shows` DESC;
