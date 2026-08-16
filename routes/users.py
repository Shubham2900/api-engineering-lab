"""
User-related API endpoints.

Includes examples of path parameters, query parameters,
request validation, and response models.
"""

from fastapi import APIRouter
from schemas.users import UserCreate, UserResponse


router = APIRouter()


@router.get("/users/{user_id}")
def get_user(user_id: int):
    """Retrieve a user by ID. `user_id` is a path parameter."""
    return {
        "user_id": user_id,
        "name": "Shubham",
    }


@router.get("/users")
def search_users(name: str):
    """Search users by name using a query parameter."""
    return {
        "name": name,
        "message": f"Searching users with name: {name}",
    }


@router.get("/users/{user_id}/orders")
def get_user_orders(
    user_id: int,
    limit: int = 10,
    status: str | None = None,
):
    """Retrieve a user's orders using path and query parameters."""
    return {
        "user_id": user_id,
        "limit": limit,
        "status": status,
    }


@router.post("/users", response_model=UserResponse)
def create_user(user: UserCreate):
    """Create a user and return the response defined by UserResponse."""
    return {
        "id": 1,
        "name": user.name,
        "email": user.email,
        "age": user.age,
        "password_hash": "secret",
    }