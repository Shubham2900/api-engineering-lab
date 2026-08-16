"""
User-related API endpoints.

This module contains endpoints for:
- Retrieving a user by ID
- Searching users using query parameters
- Retrieving orders belonging to a specific user

The endpoints in this module are intentionally simple and use
in-memory/dummy responses while we learn API fundamentals.
"""

from fastapi import APIRouter
from schemas.users import UserCreate


# APIRouter allows us to group related endpoints into a separate
# module instead of putting every endpoint inside main.py.
#
# The router is registered with the main FastAPI application in
# app/main.py.
router = APIRouter()


@router.get("/users/{user_id}")
def get_user(user_id: int):
    """
    Retrieve a user by their unique ID.

    `user_id` is a path parameter because it identifies the specific
    user resource being requested.

    Example:
        GET /users/42

    FastAPI validates the path parameter according to its type
    annotation. Since `user_id` is declared as `int`, requests such as
    `/users/abc` are rejected before this function is executed.
    """
    return {
        "user_id": user_id,
        "name": "Shubham",
    }


@router.get("/users")
def search_users(name: str):
    """
    Search users by name.

    `name` is a query parameter because it is used to filter/search
    the users collection rather than identify a specific user.

    Example:
        GET /users?name=Shubham
    """
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
    """
    Retrieve orders belonging to a specific user.

    Parameters:
        user_id:
            Path parameter identifying the user.

        limit:
            Optional query parameter controlling the maximum number
            of orders to return. Defaults to 10.

        status:
            Optional query parameter used to filter orders by status.

    Examples:
        GET /users/42/orders
        GET /users/42/orders?limit=5
        GET /users/42/orders?limit=5&status=delivered

    FastAPI validates `user_id` and `limit` according to their type
    annotations before executing this function.
    """
    return {
        "user_id": user_id,
        "limit": limit,
        "status": status,
    }

@router.post("/users")
def create_user(user: UserCreate):
    return {
        "name": user.name,
        "email": user.email,
        "age": user.age
    }