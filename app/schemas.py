from pydantic import BaseModel, ConfigDict
from typing import Optional


# 📘 Book creation schema (used in POST /api/books)
class BookCreate(BaseModel):
    title: str
    author: str
    description: Optional[str] = None


# 📘 Book response schema (used in GET /api/books)
class BookResponse(BookCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)


# 📝 Review creation schema (used in POST /api/books/{id}/reviews)
class ReviewCreate(BaseModel):
    reviewer: str
    text: str
    rating: int


# ✅ Review response schema (used in GET /api/books/{id}/reviews)
class ReviewOut(ReviewCreate):
    id: int
    book_id: int
    model_config = ConfigDict(from_attributes=True)
