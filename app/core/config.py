from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0

    class Config:
        env_file = ".env"   # this tells it to load from .env

settings = Settings()

print("✅ Loaded DATABASE_URL:", settings.DATABASE_URL)
