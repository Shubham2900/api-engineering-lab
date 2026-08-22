from clients.user_client import UsersAPIClient
from services.user_ingestion import UserIngestionService
from state.watermark import WatermarkManager


class UserPipeline:

    def __init__(
        self,
        client=None,
        ingestion_service=None,
        watermark_manager=None,
    ):
        self.client = client or UsersAPIClient()
        self.ingestion_service = (
            ingestion_service or UserIngestionService()
        )
        self.watermark_manager = (
            watermark_manager or WatermarkManager()
        )

    def run(self):

        # 1. Read watermark
        watermark = self.watermark_manager.get("users")

        # 2. Incremental extraction
        users = self.client.get_users(
            updated_after=watermark,
            overlap_minutes=5,
        )

        # 3. Deduplicate
        users = self.client.deduplicate_users(users)

        # 4. Write target
        self.ingestion_service.upsert_users(users)

        # 5. Update watermark only after successful write
        if users:
            latest_updated_at = max(
                user["updated_at"]
                for user in users
            )

            self.watermark_manager.set(
                "users",
                latest_updated_at,
            )


if __name__ == "__main__":
    pipeline = UserPipeline()
    pipeline.run()