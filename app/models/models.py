from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()  # ✅ Use declarative_base() from sqlalchemy.orm (modern syntax)

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)

    reviews = relationship("Review", back_populates="book", cascade="all, delete-orphan")  # ✅ Add cascade for cleanup

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    reviewer = Column(String, nullable=False)     # ✅ Present and required by test
    text = Column(Text, nullable=False)           # ✅ Correctly named to match your ReviewCreate schema
    rating = Column(Integer, nullable=False)
    book_id = Column(Integer, ForeignKey("books.id", ondelete="CASCADE"))  # ✅ Safer deletion

    book = relationship("Book", back_populates="reviews")


# app/models/models.py

from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    reviews = relationship("Review", back_populates="book")

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    reviewer = Column(String, nullable=False)
    text = Column(Text, nullable=False)
    book_id = Column(Integer, ForeignKey("books.id"))
    book = relationship("Book", back_populates="reviews")


# app/models/models.py

from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Book(Base):
    __tablename__ = "books"
    id     = Column(Integer, primary_key=True, index=True)
    title  = Column(String,  nullable=False)
    author = Column(String,  nullable=False)
    reviews = relationship("Review", back_populates="book")

class Review(Base):
    __tablename__ = "reviews"
    id       = Column(Integer, primary_key=True, index=True)
    reviewer = Column(String,  nullable=False)    # ← new
    text     = Column(Text,    nullable=False)    # ← renamed from `content`
    rating   = Column(Integer, nullable=False)
    book_id  = Column(Integer, ForeignKey("books.id"))
    book     = relationship("Book", back_populates="reviews")

from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)

    reviews = relationship("Review", back_populates="book")


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    reviewer = Column(String, nullable=False)     # ✅ matches test JSON
    text = Column(Text, nullable=False)            # ✅ matches test JSON
    book_id = Column(Integer, ForeignKey("books.id"))

    # book = relationship("Book", back_populates="reviews")
