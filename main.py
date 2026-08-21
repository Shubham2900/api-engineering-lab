from services.user_ingestion import UserIngestionService


users = [
    {
        "id": 10,
        "name": "Test User",
        "updated_at": "2026-08-21T14:00:00",
    }
]

service = UserIngestionService()

service.upsert_users(users)