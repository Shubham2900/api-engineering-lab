import pytest


@pytest.fixture
def sample_user():
    return {
        "id": 100,
        "name": "Test User",
        "updated_at": "2026-08-21T10:00:00",
    }


@pytest.fixture
def test_db(tmp_path):
    return tmp_path / "test_users.db"