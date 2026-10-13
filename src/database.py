import sqlite3
from pathlib import Path

# Find the project folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Database location
DATABASE_PATH = BASE_DIR / "data" / "olist.db"

# Connect to the database
def get_connection():
    return sqlite3.connect(DATABASE_PATH)


# Run a SQL query and return the results
def run_query(sql):
    connection = get_connection()

    try:
        cursor = connection.cursor()
        cursor.execute(sql)

        results = cursor.fetchall()
        columns = [column[0] for column in cursor.description]

        return columns, results

    finally:
        connection.close()