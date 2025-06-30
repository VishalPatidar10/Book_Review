from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    description = Column(String, nullable=True)  # Optional field if needed

    # ✅ One-to-many relationship with Review
    reviews = relationship("Review", back_populates="book", cascade="all, delete")
