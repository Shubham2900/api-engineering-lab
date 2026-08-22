from unittest.mock import Mock

from clients.user_client import UsersAPIClient
from services.user_ingestion import UserIngestionService
from services.user_pipeline import UserPipeline
from state.watermark import WatermarkManager


def test_watermark_updates_after_successful_write():

    client = Mock(spec=UsersAPIClient)
    ingestion_service = Mock(spec=UserIngestionService)
    watermark_manager = Mock(spec=WatermarkManager)

    watermark_manager.get.return_value = "2026-08-19T00:00:00"

    users = [
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

    client.get_users.return_value = users
    client.deduplicate_users.return_value = users

    pipeline = UserPipeline(
        client=client,
        ingestion_service=ingestion_service,
        watermark_manager=watermark_manager,
    )

    pipeline.run()

    watermark_manager.set.assert_called_once_with(
        "users",
        "2026-08-21T11:00:00",
    )

def test_watermark_not_updated_when_write_fails():

    client = Mock(spec=UsersAPIClient)
    ingestion_service = Mock(spec=UserIngestionService)
    watermark_manager = Mock(spec=WatermarkManager)

    watermark_manager.get.return_value = "2026-08-19T00:00:00"

    users = [
        {
            "id": 1,
            "name": "Alice",
            "updated_at": "2026-08-21T10:00:00",
        }
    ]

    client.get_users.return_value = users
    client.deduplicate_users.return_value = users

    ingestion_service.upsert_users.side_effect = Exception(
        "Database write failed"
    )

    pipeline = UserPipeline(
        client=client,
        ingestion_service=ingestion_service,
        watermark_manager=watermark_manager,
    )

    try:
        pipeline.run()
    except Exception:
        pass

    watermark_manager.set.assert_not_called()

def test_watermark_not_updated_when_no_users():

    client = Mock(spec=UsersAPIClient)
    ingestion_service = Mock(spec=UserIngestionService)
    watermark_manager = Mock(spec=WatermarkManager)

    watermark_manager.get.return_value = "2026-08-21T11:00:00"

    client.get_users.return_value = []
    client.deduplicate_users.return_value = []

    pipeline = UserPipeline(
        client=client,
        ingestion_service=ingestion_service,
        watermark_manager=watermark_manager,
    )

    pipeline.run()

    ingestion_service.upsert_users.assert_called_once_with([])

    watermark_manager.set.assert_not_called()