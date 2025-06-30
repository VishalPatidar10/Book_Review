from pydantic import BaseModel, ConfigDict


# ✅ Input Schema for POST /api/books
class BookCreate(BaseModel):
    title: str
    author: str


# ✅ Output Schema for GET/POST responses
class BookResponse(BaseModel):
    id: int
    title: str
    author: str

    model_config = ConfigDict(from_attributes=True)  # SQLAlchemy support
