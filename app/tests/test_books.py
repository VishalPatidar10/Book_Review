import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app
from app.db.database import Base, get_db

# Use an in-memory SQLite DB so no files to clean up and schema persists across connections
SQLALCHEMY_TEST_URL = "sqlite:///:memory:"
engine = create_engine(
    SQLALCHEMY_TEST_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# This fixture runs *before each test* to drop+recreate all tables
@pytest.fixture(autouse=True)
def prepare_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield

# Override the normal get_db dependency to use our in-memory DB
@pytest.fixture
def client():
    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    return TestClient(app)

def test_get_books_empty(client):
    response = client.get("/api/books")
    assert response.status_code == 200
    assert response.json() == []

def test_create_book(client):
    response = client.post("/api/books", json={"title": "FastAPI Guide", "author": "Vishal"})
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "FastAPI Guide"
    assert data["author"] == "Vishal"

def test_get_books_with_data(client):
    client.post("/api/books", json={"title": "FastAPI Guide", "author": "Vishal"})
    response = client.get("/api/books")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list) and len(data) == 1
    assert data[0]["title"] == "FastAPI Guide"

def test_add_review(client):
    # create a book
    book = client.post("/api/books", json={"title": "Review Me", "author": "Author X"}).json()
    book_id = book["id"]

    # add a review
    review = client.post(
        f"/api/books/{book_id}/reviews",
        json={"reviewer": "Vishal", "text": "Excellent read!"}
    )
    assert review.status_code == 201
    rev_data = review.json()
    assert rev_data["reviewer"] == "Vishal"
    assert rev_data["text"] == "Excellent read!"
    assert rev_data["book_id"] == book_id
