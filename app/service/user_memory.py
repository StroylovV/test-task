from typing import Optional
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.service.base import BaseUserRepository


class UserServiceMemory(BaseUserRepository):
    def __init__(self):
        self._storage: dict[int, User] = {}
        self._current_id: int = 1

    async def get_user_by_id(self, id: int) -> Optional[User]:
        return self._storage.get(id)

    async def create(self, user_in: UserCreate) -> User:
        user = User(id=self._current_id, FIO=user_in.FIO)
        self._storage[self._current_id] = user
        self._current_id += 1
        return user

    async def update(self, user: User, user_in: UserUpdate) -> User:
        if user_in.FIO is not None:
            user.FIO = user_in.FIO
        self._storage[user.id] = user
        return user

    async def delete(self, user: User) -> None:
        if user.id in self._storage:
            del self._storage[user.id]


in_memory_repo = UserServiceMemory()
