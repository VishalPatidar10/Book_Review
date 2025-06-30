from sqlalchemy.orm import Session
from app.models.models import Book
from app.schemas.book_schema import BookCreate

def create_book(db: Session, book_data: BookCreate):
    new_book = Book(**book_data.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book
