import json
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models import models
from app.schemas import BookCreate, BookResponse, ReviewCreate, ReviewResponse
from app.core.redis import redis_client

router = APIRouter()

# ✅ GET /api/books (via /books + "/api" in main.py)
@router.get("/books", response_model=List[BookResponse])
def get_books(db: Session = Depends(get_db)):
    try:
        cached_books = redis_client.get("books")
        if cached_books:
            return json.loads(cached_books)
    except Exception as e:
        print(f"⚠️ Redis GET error: {e}")

    books = db.query(models.Book).all()
    result = [BookResponse.from_orm(book).dict() for book in books]

    try:
        redis_client.setex("books", 60, json.dumps(result))
    except Exception as e:
        print(f"⚠️ Redis SET error: {e}")

    return result

# ✅ POST /api/books - Add new book
@router.post("/books", response_model=BookResponse, status_code=201)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)

    try:
        redis_client.delete("books")
    except Exception as e:
        print(f"⚠️ Redis DELETE error: {e}")

    return db_book

# ✅ POST /api/books/{book_id}/reviews - Add review to book
@router.post("/books/{book_id}/reviews", response_model=ReviewResponse, status_code=201)
def create_review(book_id: int, review: ReviewCreate, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    db_review = models.Review(**review.dict(), book_id=book_id)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review
