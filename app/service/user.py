from typing import List, Optional

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_db
from app.models import User
from app.schemas import UserCreate, UserUpdate

class UserService:
    def __init__(self, db: AsyncSession = Depends(get_db)):
        self.db = db
    
    async def get_user_by_id()->Optional[User]:
        pass
    async def create()->User:
        pass
    async def update()->User:
        pass
    async def delete()->None:
        pass