from pydantic import BaseModel, Field
from typing import Optional


class UserBase(BaseModel):
    FIO: str = Field(..., min_length=3, max_length=100)

    model_config = {"json_schema_extra": {"example": {"FIO": "Иванов Иван Иванович"}}}


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):

    FIO: Optional[str] = Field(None, min_length=3, max_length=100)


class UserResponse(UserBase):
    id: int

    model_config = {"from_attributes": True}
