from db.database import upsert_user

class UserIngestionService:
    def upsert_users(self, users, db_path):
        for user in users:
            upsert_user(user, db_path)