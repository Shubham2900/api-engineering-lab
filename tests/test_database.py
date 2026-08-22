from db.database import get_connection, create_tables, upsert_user, get_users


def test_database_connection():
    connection = get_connection()
    assert connection is not None
    connection.close()

def test_insert_new_user(sample_user, test_db):
    create_tables(test_db)

    upsert_user(sample_user, test_db)

    connection = get_connection(test_db)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, updated_at
        FROM users
        WHERE id = ?
    """, (100,))

    result = cursor.fetchone()

    connection.close()

    assert result == (
        100,
        "Test User",
        "2026-08-21T10:00:00",
    )

def test_newer_user_updates_existing_user(test_db):
    create_tables(test_db)

    old_user = {
        "id": 200,
        "name": "Old Name",
        "updated_at": "2026-08-21T10:00:00",
    }

    new_user = {
        "id": 200,
        "name": "New Name",
        "updated_at": "2026-08-21T11:00:00",
    }

    upsert_user(old_user, test_db)
    upsert_user(new_user, test_db)

    users = get_users(test_db)

    assert users == [
        (
            200,
            "New Name",
            "2026-08-21T11:00:00",
        )
    ]

def test_existing_user_rejects_older_user(test_db):
    create_tables(test_db)

    old_user = {
        "id": 200,
        "name": "Old Name",
        "updated_at": "2026-08-21T10:00:00",
    }

    new_user = {
        "id": 200,
        "name": "New Name",
        "updated_at": "2026-08-21T09:00:00",
    }

    upsert_user(old_user, test_db)
    upsert_user(new_user, test_db)

    users = get_users(test_db)

    assert users == [
        (
            200,
            "Old Name",
            "2026-08-21T10:00:00",
        )
    ]