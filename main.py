"""
Application entry point.

Creates the FastAPI application and registers the API routers.
"""

from fastapi import FastAPI

from routes.basic import router as basic_router


app = FastAPI(
    title="API Learning Project",
    description="Hands-on API engineering with FastAPI.",
    version="0.1.0",
)


# Register the basic API routes.
#
# Keeping routes in separate modules prevents main.py from becoming
# a large collection of endpoint implementations.
app.include_router(basic_router)