from clients.user_client import UsersAPIClient


def test_deduplicate_users():

    client = UsersAPIClient()

    users = [
        {
            "id": 1,
            "name": "Alice",
            "updated_at": "2026-08-21T10:00:00",
        },
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

    result = client.deduplicate_users(users)

    assert result == [
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