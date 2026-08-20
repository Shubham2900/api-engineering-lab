from datetime import datetime, timedelta


class UsersAPIClient:
    """
    Client responsible for communicating with the external Users API.
    """

    def __init__(self):
        self.users = [
            {
                "id": 1,
                "name": "Alice",
                "updated_at": "2026-08-18T10:00:00",
            },
            {
                "id": 2,
                "name": "Robert",
                "updated_at": "2026-08-19T12:00:00",
            },
            {
                "id": 2,
                "name": "Robert",
                "updated_at": "2026-08-19T12:00:00",
            },
            {
                "id": 3,
                "name": "Charlie",
                "updated_at": "2026-08-21T08:00:00",
            },
        ]

    def get_users(self, updated_after = None, overlap_minutes=5):
        if updated_after:
            watermark = datetime.fromisoformat(updated_after)
            start_time = watermark - timedelta(minutes=overlap_minutes)

            return [
                user
                for user in self.users
                if datetime.fromisoformat(user["updated_at"]) > start_time
            ]

        return self.users

    def deduplicate_users(self, users):
        unique_users = {}

        for user in users:
            if user["id"] not in unique_users:
                unique_users[user["id"]] = user

        return list(unique_users.values())