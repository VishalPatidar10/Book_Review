from sqlalchemy import create_engine, text

# Replace with your actual password
DATABASE_URL = "postgresql+psycopg2://postgres:123@localhost/book_review_db"

engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT current_database();"))
        print("✅ Connected to DB:", result.scalar())
except Exception as e:
    print("❌ Failed to connect:", e)
