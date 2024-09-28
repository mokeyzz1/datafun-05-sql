# Movie Database Project

## Overview
This project uses Python and SQL to analyze a movie database consisting of movies, actors, directors, and genres. The database is built using SQLite and populated with real-world data to provide insights on various aspects of the film industry, such as actor participation, director influence, and genre trends.

## Technologies Used
- **Python**: For scripting and automation.
- **SQLite**: As the relational database management system.
- **Pandas**: For data manipulation and CSV handling.
- **Matplotlib/Seaborn**: (Optional, for data visualization)

## Features
- Automated creation of SQLite database.
- Insertion of data from CSV files into relational tables.
- Basic SQL operations: Insert, Update, Delete, and Query data.
- Data aggregation and filtering.
- Joins between different tables for more complex queries.

## Project Structure

- `movie_data/`: Contains CSV files for movies, actors, directors, and genres.
- `sql_movie/`: Contains SQL scripts for creating tables, inserting, updating, deleting, and querying data.
- `project_movie.db`: SQLite database file.
- `movie_manager.py`: Python script for managing the database (creating tables and inserting data).
- `analysis.py`: (Optional) Python script for data exploration and analysis.

## Getting Started

### Prerequisites
- Python 3.x
- SQLite
- Pandas library

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mokeyzz1/datafun-05-sql
   cd datafun-05-sql
   ```
2. Create a virtual environment and activate it:
    ```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
```
3. Install the required packages:
    ```bash
pip install -r requirements.txt
```
4. Run the movie_manager.py script to set up the database:
    ```bash
python movie_manager.py

## SQL Operations

The project includes several SQL operations, organized into separate files in the sql_movie/ folder:

- create_tables.sql: Defines the schema for the database (movies, actors, directors, genres).
- insert_records.sql: Inserts additional records into the database.
- update_records.sql: Updates records in the database.
- delete_records.sql: Deletes records from the database.
- query_aggregation.sql: Aggregation queries (e.g., COUNT, SUM, AVG).
- query_filter.sql: Queries with WHERE clause to filter data.
- query_sorting.sql: Queries with ORDER BY for sorting.
- query_group_by.sql: GROUP BY queries for aggregation.
- query_join.sql: INNER JOIN and LEFT JOIN operations to combine data from different tables.

## Stage and Push Files to GitHub

- Use the following Git commands to stage and commit changes:
````
git add .
git commit -m "message: commit message"
git push origin main
````


