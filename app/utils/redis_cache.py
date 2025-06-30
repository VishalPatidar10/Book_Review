import redis
import os
from dotenv import load_dotenv

load_dotenv()  # Load env vars from .env file

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
ENV = os.getenv("ENV", "dev")

# ⚠️ Don't connect Redis in test environment
if ENV != "test":
    redis_client = redis.Redis.from_url(REDIS_URL, decode_responses=True)
else:
    redis_client = None  # Skip Redis in test mode


def get_cache(key: str):
    if redis_client:
        try:
            return redis_client.get(key)
        except Exception as e:
            print(f"⚠️ Redis GET error: {e}")
    return None


def set_cache(key: str, value: str, expire: int = 60):
    if redis_client:
        try:
            redis_client.setex(key, expire, value)
        except Exception as e:
            print(f"⚠️ Redis SET error: {e}")
