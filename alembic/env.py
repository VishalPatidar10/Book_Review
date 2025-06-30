import sys
import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

# ✅ Load .env file so settings.DATABASE_URL is available
from dotenv import load_dotenv
load_dotenv(".env")  # 👈 VERY IMPORTANT

# ✅ Fix path so Alembic finds your app
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# ✅ Now import app settings & models
from app.core.config import settings
from app.db.database import Base
from app.models.book import Book
from app.models.review import Review

# ✅ Alembic Config object
config = context.config

# ✅ Logging setup
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# ✅ Set target metadata for migrations
target_metadata = Base.metadata
