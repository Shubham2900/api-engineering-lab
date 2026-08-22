from services.user_ingestion import UserIngestionService
from db.database import create_tables, get_users
from clients.user_client import UsersAPIClient


def test_user_ingestion_pipeline(test_db):

    create_tables(test_db)

    users = [
        {
            "id": 1,
            "name": "Alice",
            "updated_at": "2026-08-21T10:00:00",
        },
        {
            "id": 2,
            "name": "Bob",
            "updated_at": "2026-08-21T11:00:00",
        },
    ]

    service = UserIngestionService()

    service.upsert_users(users, test_db)

    result = get_users(test_db)

    assert result == [
        (
            1,
            "Alice",
            "2026-08-21T10:00:00",
        ),
        (
            2,
            "Bob",
            "2026-08-21T11:00:00",
        ),
    ]