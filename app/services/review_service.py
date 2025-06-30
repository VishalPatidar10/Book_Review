from sqlalchemy.orm import Session
from app.models.models import Review

def get_reviews_by_book_id(db: Session, book_id: int):
    return db.query(Review).filter(Review.book_id == book_id).all()
