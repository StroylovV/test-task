from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Response, status
from starlette.status import HTTP_201_CREATED

from app.schemas import UserCreate, UserResponse, UserUpdate
from app.service import get_user_repository
from app.service.base import BaseUserRepository

router = APIRouter()


@router.post("/", response_model=UserResponse, status_code=HTTP_201_CREATED)
async def create_user(
    user_in: UserCreate, repo: BaseUserRepository = Depends(get_user_repository)
) -> Any:
    user = await repo.create(user_in)
    return user


@router.get("/me", response_model=UserResponse)
async def get_user(
    user_id: int, repo: BaseUserRepository = Depends(get_user_repository)
) -> Any:
    user = await repo.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/me", response_model=UserResponse)
async def update_user(
    user_id: int,
    user_in: UserUpdate,
    repo: BaseUserRepository = Depends(get_user_repository),
) -> Any:
    user = await repo.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user = await repo.update(user, user_in)
    return user


@router.delete("/me")
async def delete_user(
    user_id: int, repo: BaseUserRepository = Depends(get_user_repository)
) -> Any:
    user = await repo.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    await repo.delete(user)
    return {"detail": "Пользователь удален"}
