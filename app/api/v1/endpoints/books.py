from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.book import Book, BookCreate
from app.db.session import get_db
from app.crud.books import create_book, get_books
from typing import List

router = APIRouter()


@router.post("/", response_model=Book)
def create_new_book(book: BookCreate, db: Session = Depends(get_db)):
    return create_book(book=book, db=db)


@router.get("/", response_model=List[Book])
def get_all_books(db: Session = Depends(get_db)):
    return get_books(db=db)
