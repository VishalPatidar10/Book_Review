from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import book_routes, review_routes

app = FastAPI(
    title="📚 Book Review API",
    version="1.0.0",
    description="An API for managing books and their reviews.",
)

# ✅ CORS for frontend or Postman testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Register routes
app.include_router(book_routes.router, prefix="/api", tags=["Books"])
app.include_router(review_routes.router, prefix="/api", tags=["Reviews"])

# Optional root path for Render health check
@app.get("/")
def root():
    return {"message": "Hello, Render!"}
