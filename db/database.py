import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "users.db"

def get_connection(db_path=DB_PATH):
    return sqlite3.connect(db_path)

def create_tables(db_path=DB_PATH):
    connection = get_connection(db_path)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            updated_at TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()

def get_tables(db_path=DB_PATH):
    connection = get_connection(db_path)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type = 'table'
    """)

    tables = cursor.fetchall()
    connection.close()
    return tables

def upsert_user(user, db_path=DB_PATH):
    connection = get_connection(db_path)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO users (id, name, updated_at)
        VALUES (?, ?, ?)

        ON CONFLICT(id)
        DO UPDATE SET
            name = excluded.name,
            updated_at = excluded.updated_at

        WHERE excluded.updated_at > users.updated_at
    """, (
        user["id"],
        user["name"],
        user["updated_at"],
    ))

    connection.commit()
    connection.close()

def get_users(db_path=DB_PATH):
    connection = get_connection(db_path)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, updated_at
        FROM users
    """)

    users = cursor.fetchall()
    connection.close()
    return users

if __name__ == "__main__":
    # create_tables()
    # print(get_tables())
    # upsert_user(
    #     3,
    #     "Shabnam",
    #     "2026-08-21T13:00:00"
    # )
    print(get_users())