"""
User-related API endpoints.

Includes examples of path parameters, query parameters,
request validation, and response models.
"""

from fastapi import APIRouter, HTTPException, status
from data.users import users_db
from schemas.users import UserCreate, UserResponse, UserUpdate, UserPatch

router = APIRouter()


@router.get("/users", response_model=list[UserResponse])
def get_users(name: str | None = None):
    """Retrieve all users or filter them by name."""
    if name:
        return [
            user
            for user in users_db.values()
            if user["name"].lower() == name.lower()
        ]

    return list(users_db.values())


@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    """Retrieve a user by ID."""
    user = users_db.get(user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user


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
    new_id = max(users_db.keys(), default=0) + 1
    new_user = {
        "id": new_id,
        "name": user.name,
        "email": user.email,
        "age": user.age,
    }
    users_db[new_id] = new_user
    return new_user


@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    if user_id not in users_db.keys():
        raise HTTPException(status_code=404, detail="User not found")
    del users_db[user_id]


@router.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserUpdate):
    """Replace an existing user."""

    if user_id not in users_db.keys():
        raise HTTPException(status_code=404, detail="User not found")

    updated_user = {
        "id": user_id,
        "name": user.name,
        "email": user.email,
        "age": user.age,
    }

    users_db[user_id] = updated_user

    return updated_user


@router.patch("/users/{user_id}", response_model=UserResponse)
def patch_user(user_id: int, user: UserPatch):
    if user_id not in users_db.keys():
        raise HTTPException(status_code=404, detail="User not found")

    updates = user.model_dump(exclude_unset=True)

    users_db[user_id].update(updates)

    return users_db[user_id]