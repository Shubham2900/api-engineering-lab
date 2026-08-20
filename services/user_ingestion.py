from data.target import target_users
from datetime import datetime

class UserIngestionService:

    def upsert_users(self, users):
        for user in users:
            user_id = user["id"]

            if user_id not in target_users:
                target_users[user_id] = user

            elif (
                datetime.fromisoformat(user["updated_at"])
                > datetime.fromisoformat(
                    target_users[user_id]["updated_at"]
                )
            ):
                target_users[user_id].update(user)