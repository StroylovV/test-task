from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base

class User(Base):
    __tablename__="user"

    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    FIO : Mapped[str] = mapped_column(String(255), nullable=False)
    

    