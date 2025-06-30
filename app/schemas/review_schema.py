from pydantic import BaseModel

class ReviewOut(BaseModel):
    id: int
    rating: int
    comment: str

    class Config:
        orm_mode = True
