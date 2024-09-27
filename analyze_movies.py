import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect("project.db")

# Load data from tables into DataFrames
movies_df = pd.read_sql_query("SELECT * FROM movies;", conn)
actors_df = pd.read_sql_query("SELECT * FROM actors;", conn)
directors_df = pd.read_sql_query("SELECT * FROM directors;", conn)
genres_df = pd.read_sql_query("SELECT * FROM genres;", conn)

# Close the connection
conn.close()

# Display the first few rows of each DataFrame
print("Movies Data:")
print(movies_df.head())
print("\nActors Data:")
print(actors_df.head())
print("\nDirectors Data:")
print(directors_df.head())
print("\nGenres Data:")
print(genres_df.head())

# Analyze Genre Distribution
genre_counts = movies_df['genre_id'].value_counts()
genre_names = genres_df.set_index('genre_id').loc[genre_counts.index]['genre_name']
genre_distribution = pd.DataFrame({'Count': genre_counts, 'Genre': genre_names}).reset_index()
print("\nGenre Distribution:")
print(genre_distribution)

# List Movies by Director
movies_with_directors = movies_df.merge(directors_df, on='director_id', how='left')
print("\nMovies with Directors:")
print(movies_with_directors[['title', 'first_name', 'last_name']])
