from pydantic import BaseModel
from .user import User


class BookBase(BaseModel):
    title: str
    description: str
    author_id: int


class BookCreate(BookBase):
    pass


class Book(BookBase):
    author: User

    class Config:
        orm_mode = True
