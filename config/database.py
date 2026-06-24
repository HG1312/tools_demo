"""Database settings, read from environment (no secrets in code)."""
import os

DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://localhost/orders")
POOL_SIZE = int(os.environ.get("DB_POOL_SIZE", "10"))
