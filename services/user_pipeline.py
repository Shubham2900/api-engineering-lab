from clients.user_client import UsersAPIClient
from services.user_ingestion import UserIngestionService
from state.watermark import WatermarkManager


class UserPipeline:
    def __init__(self):
        self.client = UsersAPIClient()
        self.ingestion_service = UserIngestionService()
        self.watermark_manager = WatermarkManager()

    def run(self):
        watermark = self.watermark_manager.get("users")
        users = self.client.get_users(
            updated_after=watermark
        )
        self.ingestion_service.upsert_users(users)

        if users:
            latest_updated_at = max(
                user["updated_at"]
                for user in users
            )
            self.watermark_manager.set(
                "users",
                latest_updated_at
            )

if __name__ == "__main__":
    pipeline = UserPipeline()
    pipeline.run()