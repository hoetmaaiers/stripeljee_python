from typing import Any, Generator

from config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session() -> Generator[Session, Any, None]:
    # Dependency

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
