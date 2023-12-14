-- This script Write a script that lists all shows contained in the database hbtn_0d_tvshows.
-- Use the hbtn_0d_tvshows database
USE hbtn_0d_tvshows;

-- Select all shows with their genre_id, displaying NULL for shows without a genre
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;

