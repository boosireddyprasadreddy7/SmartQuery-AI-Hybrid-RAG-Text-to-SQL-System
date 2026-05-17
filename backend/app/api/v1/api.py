from fastapi import APIRouter

from app.api.v1.routes import (
    health,
    query,
    database
)

api_router = APIRouter()

api_router.include_router(
    health.router,
    tags=["Health"]
)

api_router.include_router(
    query.router,
    tags=["Query"]
)

api_router.include_router(
    database.router,
    tags=["Database"]
)