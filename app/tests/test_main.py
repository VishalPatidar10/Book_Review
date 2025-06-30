from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_get_books():
    # Create a book
    response = client.post("/api/books", json={
        "title": "Test Book",
        "author": "Vishal",
        "description": "Test description"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Book"
    assert "id" in data

    # Fetch all books
    response = client.get("/api/books")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_add_review():
    # First, create a book
    book_resp = client.post("/api/books", json={
        "title": "Book With Review",
        "author": "Tester",
        "description": "To test review endpoint"
    })
    book_id = book_resp.json()["id"]

    # Post a review
    review_resp = client.post(f"/api/books/{book_id}/reviews", json={
        "reviewer": "John",
        "rating": 5,
        "comment": "Excellent book!"
    })
    assert review_resp.status_code == 201
    review_data = review_resp.json()
    assert review_data["reviewer"] == "John"

def test_get_reviews_empty():
    # Create a new book with no reviews
    book_resp = client.post("/api/books", json={
        "title": "Book With No Reviews",
        "author": "Vishal",
        "description": "Empty reviews test"
    })
    book_id = book_resp.json()["id"]

    # Fetch reviews (should be empty)
    review_resp = client.get(f"/api/books/{book_id}/reviews")
    assert review_resp.status_code == 200
    assert review_resp.json() == []
