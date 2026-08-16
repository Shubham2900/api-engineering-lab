"""
Pydantic schemas for user-related API operations.

Schemas define the structure and validation rules for data entering
or leaving the API.

This module currently contains the request schema used when creating
a user.
"""

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserCreate(BaseModel):
    """
    Request model for creating a user.

    The model defines the API contract for POST /users.

    Validation performed here ensures that the endpoint receives
    structurally and semantically valid data before application logic
    is executed.
    """

    # Reject fields that are not explicitly defined by this model.
    #
    # For example, sending:
    #
    #     {"name": "Shubham", "email": "...", "age": 28, "salary": 2333}
    #
    # will result in a validation error for `salary`.
    model_config = ConfigDict(extra="forbid")

    # User's name must contain between 2 and 100 characters.
    name: str = Field(
        min_length=2,
        max_length=100,
    )

    # EmailStr performs semantic email validation rather than merely
    # checking that the value is a string.
    email: EmailStr

    # Age must be between 18 and 100, inclusive.
    age: int = Field(
        ge=18,
        le=100,
    )