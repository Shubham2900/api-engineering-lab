from services.user_ingestion import UserIngestionService
from db.database import create_tables, get_users
from clients.user_client import UsersAPIClient


def test_user_ingestion_pipeline(test_db):

    create_tables(test_db)

    client = UsersAPIClient()
    service = UserIngestionService()

    users = client.get_users(
        updated_after="2026-08-19T00:00:00",
        overlap_minutes=5,
    )

    users = client.deduplicate_users(users)

    service.upsert_users(users, test_db)

    result = get_users(test_db)

    assert result == [
        (
            2,
            "Robert",
            "2026-08-19T12:00:00",
        ),
        (
            3,
            "Charlie",
            "2026-08-21T08:00:00",
        ),
    ]