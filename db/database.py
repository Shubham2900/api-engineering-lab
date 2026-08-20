import sqlite3
from pathlib import Path


DB_PATH = Path(__file__).resolve().parent.parent / "users.db"


def get_connection():
    return sqlite3.connect(DB_PATH)

connection = get_connection()
connection.close()