# app/schemas/review.py
from pydantic import BaseModel, ConfigDict

# Input model for creating a review
class ReviewCreate(BaseModel):
    reviewer: str
    text: str
    rating: int  # ✅ This was missing

# Output model for returning review data
class ReviewOut(ReviewCreate):
    id: int
    book_id: int

    model_config = ConfigDict(from_attributes=True)

# Response model (can be used for consistency)
class ReviewResponse(ReviewCreate):
    id: int
    book_id: int

    model_config = ConfigDict(from_attributes=True)


# app/schemas/review.py

from pydantic import BaseModel, ConfigDict

class ReviewCreate(BaseModel):
    reviewer: str
    text: str

class ReviewOut(ReviewCreate):
    id: int
    book_id: int

    model_config = ConfigDict(from_attributes=True)

from pydantic import BaseModel, ConfigDict

class ReviewCreate(BaseModel):
    reviewer: str   # matches the POST payload in tests
    text: str       # matches the POST payload in tests

class ReviewOut(ReviewCreate):
    id: int
    book_id: int

    model_config = ConfigDict(from_attributes=True)
