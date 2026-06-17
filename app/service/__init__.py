from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.db.base import get_db

from app.service.base import BaseUserRepository
from app.service.user_db import UserServiceDB
from app.service.user_memory import UserServiceMemory

in_memory_repo = UserServiceMemory()


def get_user_repository(db: AsyncSession = Depends(get_db)) -> BaseUserRepository:
    if settings.REPOSITORY_TYPE == "memory":
        return in_memory_repo
    elif settings.REPOSITORY_TYPE == "db":
        return UserServiceDB(db=db)
    else:
        raise ValueError("Unknown REPOSITORY_TYPE in config")

__all__ = [
    "BaseUserRepository",
    "UserServiceDB",
    "UserServiceMemory",
    "get_user_repository"
]