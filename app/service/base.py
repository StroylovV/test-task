from abc import ABC, abstractmethod
from typing import Optional
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate


class BaseUserRepository(ABC):
    @abstractmethod
    async def get_user_by_id(self, id: int) -> Optional[User]:
        pass

    @abstractmethod
    async def create(self, user_in: UserCreate) -> User:
        pass

    @abstractmethod
    async def update(self, user: User, user_in: UserUpdate) -> User:
        pass

    @abstractmethod
    async def delete(self, user: User) -> None:
        pass
