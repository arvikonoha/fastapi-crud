from fastapi import APIRouter
from .endpoints import users, books

api_router = APIRouter()

api_router.include_router(users.router, prefix="/users")
api_router.include_router(books.router, prefix="/books")
