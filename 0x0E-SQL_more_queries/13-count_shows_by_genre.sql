-- lists all shows contained in the database hbtn_0d_tvshows.
SELECT tv_genres.`name` AS genre, COUNT(*) AS number_of_shows FROM `tv_shows` INNER JOIN `tv_show_genres` ON tv_genres.`id` = tv_show_genres.`genre_id` GROUP BY tv_genres.`name` ORDER BY tv_genres.`name` DESC;
