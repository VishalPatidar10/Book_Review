import json
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.models.review import Review
from app.models.book import Book
from app.schemas.review import ReviewOut

router = APIRouter()

# ✅ GET /api/books/{book_id}/reviews - Get all reviews for a book
@router.get("/books/{book_id}/reviews", response_model=List[ReviewOut])
def get_reviews(book_id: int, db: Session = Depends(get_db)):
    # ✅ Check if the book exists
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"❌ Book with ID {book_id} not found."
        )

    # ✅ Fetch and return all reviews for the book
    reviews = db.query(Review).filter(Review.book_id == book_id).all()
    return [ReviewOut.from_orm(r) for r in reviews]
