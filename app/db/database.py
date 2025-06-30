from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings  # Ensure settings.DATABASE_URL exists

# ✅ SQLAlchemy connection URL from settings
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

# ✅ Create SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# ✅ Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ✅ Updated Base using new import (removes deprecation warning)
Base = declarative_base()

# ✅ Dependency for getting DB session (used in FastAPI routes)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# app/database.py
from sqlalchemy.orm import declarative_base

Base = declarative_base()

