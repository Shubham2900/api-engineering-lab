"""
Basic API routes.

This module contains the initial endpoints used to understand
HTTP GET requests, routing, and basic JSON responses.
"""

from fastapi import APIRouter


router = APIRouter()


@router.get("/")
def home():
    """
    Health/root endpoint.

    Returns a simple response confirming that the API is running.
    """
    return {"message": "API is running!"}


@router.get("/hello")
def hello():
    """
    Basic demonstration endpoint.

    Returns a simple JSON response to an HTTP GET request.
    """
    return {"message": "Hello World!"}