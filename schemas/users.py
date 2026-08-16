"""
Pydantic schemas for user request and response data.
"""

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserCreate(BaseModel):
    """Schema for validating POST /users request data."""

    # Reject fields not defined in the schema.
    model_config = ConfigDict(extra="forbid")

    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    age: int = Field(ge=18, le=100)


class UserResponse(BaseModel):
    """Schema defining the response returned by the user API."""

    id: int
    name: str
    email: EmailStr
    age: int