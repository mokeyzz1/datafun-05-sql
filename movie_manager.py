import sqlite3
import pathlib
import pandas as pd
import logging

# Configure logging to write to log.txt
logging.basicConfig(
    filename='log.txt',           
    level=logging.DEBUG,          
    filemode='a',                 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Define paths using joinpath
db_file_path = pathlib.Path("project_movie.db")  # Update to your new database name
sql_file_path = pathlib.Path("sql_movie").joinpath("create_tables.sql")
insert_records_file_path = pathlib.Path("sql_movie").joinpath("insert_records.sql")  # Optional, if you decide to create this
update_records_file_path = pathlib.Path("sql_movie").joinpath("update_records.sql")
delete_records_file_path = pathlib.Path("sql_movie").joinpath("delete_records.sql")
query_aggregation_file_path = pathlib.Path("sql_movie").joinpath("query_aggregation.sql")
query_filter_file_path = pathlib.Path("sql_movie").joinpath("query_filter.sql")
query_sorting_file_path = pathlib.Path("sql_movie").joinpath("query_sorting.sql")
query_group_by_file_path = pathlib.Path("sql_movie").joinpath("query_group_by.sql")
query_join_file_path = pathlib.Path("sql_movie").joinpath("query_join.sql")

def verify_and_create_folders(paths):
    """Verify and create folders if they don't exist."""
    for path in paths:
        folder = path.parent
        if not folder.exists():
            logging.info(f"Creating folder: {folder}")
            folder.mkdir(parents=True, exist_ok=True)
        else:
            logging.info(f"Folder already exists: {folder}")

def create_database(db_path):
    """Create a new SQLite database file if it doesn't exist."""
    try:
        conn = sqlite3.connect(db_path)
        conn.close()
        logging.info("Database created successfully.")
    except sqlite3.Error as e:
        logging.exception(f"Error creating the database: {e}")

def create_tables(db_path, sql_file_path):
    """Read and execute SQL statements to create tables."""
    try:
        with sqlite3.connect(db_path) as conn:
            with open(sql_file_path, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            logging.info("Tables created successfully.")
    except sqlite3.Error as e:
        logging.exception(f"Error creating tables: {e}")

def insert_data_from_csv(db_path, actor_data_path, movie_data_path, director_data_path, genre_data_path):
    """Read data from CSV files and insert the records into their respective tables."""
    try:
        logging.debug(f"Actor data path: {actor_data_path}")
        logging.debug(f"Movie data path: {movie_data_path}")
        logging.debug(f"Director data path: {director_data_path}")
        logging.debug(f"Genre data path: {genre_data_path}")

        actors_df = pd.read_csv(actor_data_path)
        movies_df = pd.read_csv(movie_data_path)
        directors_df = pd.read_csv(director_data_path)
        genres_df = pd.read_csv(genre_data_path)
        
        with sqlite3.connect(db_path) as conn:
            actors_df.to_sql("actors", conn, if_exists="replace", index=False)
            movies_df.to_sql("movies", conn, if_exists="replace", index=False)
            directors_df.to_sql("directors", conn, if_exists="replace", index=False)
            genres_df.to_sql("genres", conn, if_exists="replace", index=False)
            
            logging.info("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        logging.exception(f"Error inserting data: {e}")

def execute_sql_file(db_path, sql_file_path):
    """Execute SQL statements from a file."""
    try:
        with sqlite3.connect(db_path) as conn:
            with open(sql_file_path, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            logging.info(f"Executed SQL file: {sql_file_path.name}")
    except sqlite3.Error as e:
        logging.exception(f"Error executing SQL file {sql_file_path.name}: {e}")

def main():
    logging.info("Program started.")
    
    paths_to_verify = [
        sql_file_path, 
        update_records_file_path,
        delete_records_file_path,
        query_aggregation_file_path,
        query_filter_file_path,
        query_sorting_file_path,
        query_group_by_file_path,
        query_join_file_path,
        pathlib.Path("movie_data").joinpath("actors.csv"),
        pathlib.Path("movie_data").joinpath("movies.csv"),
        pathlib.Path("movie_data").joinpath("directors.csv"),
        pathlib.Path("movie_data").joinpath("genres.csv"),
    ]
    
    verify_and_create_folders(paths_to_verify)   

    create_database(db_file_path)
    create_tables(db_file_path, sql_file_path)
    insert_data_from_csv(db_path=db_file_path,
                          actor_data_path=pathlib.Path("movie_data").joinpath("actors.csv"),
                          movie_data_path=pathlib.Path("movie_data").joinpath("movies.csv"),
                          director_data_path=pathlib.Path("movie_data").joinpath("directors.csv"),
                          genre_data_path=pathlib.Path("movie_data").joinpath("genres.csv"))

    # Execute additional SQL files
    execute_sql_file(db_file_path, update_records_file_path)
    execute_sql_file(db_file_path, delete_records_file_path)
    execute_sql_file(db_file_path, query_aggregation_file_path)
    execute_sql_file(db_file_path, query_filter_file_path)
    execute_sql_file(db_file_path, query_sorting_file_path)
    execute_sql_file(db_file_path, query_group_by_file_path)
    execute_sql_file(db_file_path, query_join_file_path)

    logging.info("Program ended.")

if __name__ == "__main__":
    main()
