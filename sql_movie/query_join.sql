SELECT m.title, d.first_name, d.last_name
FROM movies m
INNER JOIN directors d ON m.director_id = d.director_id;
