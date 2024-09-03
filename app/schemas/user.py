from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    email: str
    first_name: str
    last_name: str
    active: bool = False


class UserUpdate(BaseModel):
    email: Optional[str] = False
    first_name: Optional[str] = False
    last_name: Optional[str] = False
    active: Optional[bool] = False


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
