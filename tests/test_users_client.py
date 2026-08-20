from clients.user_client import UsersAPIClient
from services.user_ingestion import UserIngestionService
from state.watermark import WatermarkManager


client = UsersAPIClient()
ingestion_service = UserIngestionService()
watermark_manager = WatermarkManager()


# 1. Read watermark
watermark = watermark_manager.get("users")

print("Current watermark:", watermark)


# 2. Extract
users = client.get_users(
    updated_after=watermark,
    overlap_minutes=5,
)


# 3. Deduplicate
users = client.deduplicate_users(users)

print("Users extracted:", users)


try:

    # 4. Write target
    ingestion_service.upsert_users(users)

    print("Target write successful")

    # 5. Only after successful write
    # update watermark

    if users:
        new_watermark = max(
            user["updated_at"]
            for user in users
        )

        watermark_manager.set(
            "users",
            new_watermark,
        )

        print(
            "Watermark updated:",
            new_watermark,
        )

except Exception as e:

    print("Pipeline failed:", e)
    print("Watermark NOT updated")