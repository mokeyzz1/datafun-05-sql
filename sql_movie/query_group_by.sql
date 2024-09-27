SELECT genre_id, COUNT(*) AS movie_count
FROM movies
GROUP BY genre_id
HAVING movie_count > 2;
