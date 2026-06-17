from app.api.user import router as user_router
from fastapi import APIRouter

api_router = APIRouter(prefix="/api")

api_router.include_router(user_router, prefix="/user", tags=["User"])