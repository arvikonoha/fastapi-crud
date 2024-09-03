from .base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Text, String, ForeignKey


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    description = Column(Text)
    genre = Column(String(50))

    author_id = Column(Integer, ForeignKey("users.id"))

    author = relationship("User", back_populates="books")
