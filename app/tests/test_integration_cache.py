import os
import json
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.database import Base, get_db
from app.main import app

# ✅ Use SQLite for integration testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_cache.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(bind=engine)

# ✅ Dependency override
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

# ✅ Setup and teardown for test DB
@pytest.fixture(scope="module", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

# ✅ Integration Test: Cache miss for GET /api/books
def test_cache_miss_get_books(monkeypatch):
    # 👇 Simulate Redis cache miss
    monkeypatch.setattr("app.utils.redis_cache.get_cache", lambda key: None)
    monkeypatch.setattr("app.utils.redis_cache.set_cache", lambda k, v, e=60: None)

    # 👇 Add book via API
    client.post("/api/books", json={"title": "Cache Miss Book", "author": "Test Author"})

    # 👇 First GET /api/books (should hit DB, not cache)
    res = client.get("/api/books")
    assert res.status_code == 200
    data = res.json()
    assert isinstance(data, list)
    assert any(book["title"] == "Cache Miss Book" for book in data)
