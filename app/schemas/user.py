from pydantic import BaseModel, Field
from typing import Optional


class User(BaseModel):
    id: Optional[int] = None
    FIO: str = Field(..., min_length=3, max_length=100)
    model_config = {
        "json_schema_extra":{
            "example": {
                "FIO": "Иванов Иван Иванович"
            }
        }
    }

class CreateUser(BaseModel):
    FIO: str = Field(..., min_length=3, max_length=100)

class UserUpdate(BaseModel):
    FIO: str = Field(..., min_length=3, max_length=100)
    