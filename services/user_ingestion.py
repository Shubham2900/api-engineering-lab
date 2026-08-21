from db.database import upsert_user

class UserIngestionService:
    def upsert_users(self, users):
        for user in users:
            upsert_user(user)