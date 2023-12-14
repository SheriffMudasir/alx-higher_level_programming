-- This script lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- Use the hbtn_0d_tvshows database
USE hbtn_0d_tvshows;

-- Select genres and count of shows linked to each genre
SELECT genre, COUNT(*) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;

