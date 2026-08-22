from services.user_ingestion import UserIngestionService
from unittest.mock import patch


def test_upsert_users_calls_database_for_each_user():

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

    with patch("services.user_ingestion.upsert_user") as mock_upsert:
        service = UserIngestionService()
        service.upsert_users(
            users,
            "test.db",
        )

        assert mock_upsert.call_count == 2

