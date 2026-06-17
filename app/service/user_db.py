from typing import List, Optional

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_db
from app.models import User
from app.schemas.user import UserCreate, UserUpdate
from app.service.base import BaseUserRepository


class UserServiceDB(BaseUserRepository):
    def __init__(self, db: AsyncSession = Depends(get_db)):
        self.db = db

    async def get_user_by_id(self, id: int) -> Optional[User]:
        result = await self.db.execute(select(User).filter(User.id == id))
        return result.scalar_one_or_none()

    async def create(self, user_in: UserCreate) -> User:
        user = User(
            FIO=user_in.FIO,
        )
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def update(self, user: User, user_in: UserUpdate) -> User:
        if user_in.FIO is not None:
            user.FIO = user_in.FIO
        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def delete(self, user: User) -> None:
        # if user:
        await self.db.delete(user)
        await self.db.commit()
