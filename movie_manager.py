import sqlite3
import pathlib
import pandas as pd

# Define paths using joinpath
db_file_path = pathlib.Path("project_movie.dp")  # Updated database name
sql_file_path = pathlib.Path("sql_movie").joinpath("create_tables.sql")
actor_data_path = pathlib.Path("movie_data").joinpath("actors.csv")
movie_data_path = pathlib.Path("movie_data").joinpath("movies.csv")
director_data_path = pathlib.Path("movie_data").joinpath("directors.csv")
genre_data_path = pathlib.Path("movie_data").joinpath("genres.csv")

def verify_and_create_folders(paths):
    """Verify and create folders if they don't exist."""
    for path in paths:
        folder = path.parent
        if not folder.exists():
            print(f"Creating folder: {folder}")
            folder.mkdir(parents=True, exist_ok=True)
        else:
            print(f"Folder already exists: {folder}")

def create_database(db_path):
    """Create a new SQLite database file if it doesn't exist."""
    try:
        conn = sqlite3.connect(db_path)
        conn.close()
        print("Database created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating the database: {e}")

def create_tables(db_path, sql_file_path):
    """Read and execute SQL statements to create tables."""
    try:
        with sqlite3.connect(db_path) as conn:
            with open(sql_file_path, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Tables created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")

def insert_data_from_csv(db_path, actor_data_path, movie_data_path, director_data_path, genre_data_path):
    """Read data from CSV files and insert the records into their respective tables."""
    try:
        print(f"Actor data path: {actor_data_path}")
        print(f"Movie data path: {movie_data_path}")
        print(f"Director data path: {director_data_path}")
        print(f"Genre data path: {genre_data_path}")

        actors_df = pd.read_csv(actor_data_path)
        movies_df = pd.read_csv(movie_data_path)
        directors_df = pd.read_csv(director_data_path)
        genres_df = pd.read_csv(genre_data_path)
        
        with sqlite3.connect(db_path) as conn:
            actors_df.to_sql("actors", conn, if_exists="replace", index=False)
            movies_df.to_sql("movies", conn, if_exists="replace", index=False)
            directors_df.to_sql("directors", conn, if_exists="replace", index=False)
            genres_df.to_sql("genres", conn, if_exists="replace", index=False)
            
            print("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print(f"Error inserting data: {e}")

def main():
    paths_to_verify = [sql_file_path, actor_data_path, movie_data_path, director_data_path, genre_data_path]
    verify_and_create_folders(paths_to_verify)   

    create_database(db_file_path)
    create_tables(db_file_path, sql_file_path)
    insert_data_from_csv(db_file_path, actor_data_path, movie_data_path, director_data_path, genre_data_path)

if __name__ == "__main__":
    main()
