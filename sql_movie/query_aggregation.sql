SELECT COUNT(*) AS total_movies FROM movies;

SELECT AVG(birth_year) AS average_birth_year FROM actors;

SELECT genre_id, COUNT(*) AS movie_count FROM movies
GROUP BY genre_id;
