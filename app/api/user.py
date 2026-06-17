from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Response, status
from starlette.status import HTTP_201_CREATED

from app.schemas import UserCreate, UserResponse, UserUpdate
from app.service import UserService

router = APIRouter()

@router.post("/", response_model=UserResponse, status_code=HTTP_201_CREATED)
async def create_user(
    user_in: UserCreate,
    user_service: UserService = Depends()
)->Any:
    user = await user_service.create(user_in)
    return user

@router.get("/me", response_model=UserResponse)
async def get_user(
    user_id: int,
    user_service: UserService = Depends(),
    
)->Any:
    user = await user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/me", response_model=UserResponse)
async def update_user(
    user_id: int,
    user_in: UserUpdate,
    user_service: UserService = Depends()
)->Any:
    user = await user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user = await user_service.update(user, user_in)
    return user
@router.delete("/me")
async def delete_user(
    user_id: int,
    user_service: UserService = Depends()
)->Any:
    user = await user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    await user_service.delete(user)
    return {"detail": "Пользователь удален"}
