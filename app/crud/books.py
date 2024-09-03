from app.db.models.user import User
from sqlalchemy.orm import Session
from app.schemas.book import BookCreate
from app.db.models.book import Book


def get_books(db: Session):
    return db.query(Book)


def create_book(book: BookCreate, db: Session):
    db_book = Book(title=book.title, description=book.description, author_id=book.author_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book
