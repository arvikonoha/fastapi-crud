from .base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Boolean


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), index=True)
    password = Column(String(255))
    first_name = Column(String(50))
    last_name = Column(String(50))
    active = Column(Boolean, default=False)

    books = relationship("Book", back_populates="author")
