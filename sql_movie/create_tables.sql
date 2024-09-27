DROP TABLE IF EXISTS movies;
DROP TABLE IF EXISTS actors;
DROP TABLE IF EXISTS directors;
DROP TABLE IF EXISTS genres;

CREATE TABLE genres (
    genre_id INTEGER PRIMARY KEY,
    genre_name TEXT
);

CREATE TABLE directors (
    director_id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    birth_year INTEGER
);

CREATE TABLE actors (
    actor_id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    birth_year INTEGER
);

CREATE TABLE movies (
    movie_id INTEGER PRIMARY KEY,
    title TEXT,
    release_year INTEGER,
    genre_id INTEGER,
    director_id INTEGER,
    FOREIGN KEY (genre_id) REFERENCES genres(genre_id),
    FOREIGN KEY (director_id) REFERENCES directors(director_id)
);
