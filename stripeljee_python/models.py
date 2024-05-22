from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship

from stripeljee_python.db import Base


class TimestampsMixin:
    inserted_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())


class Serie(Base, TimestampsMixin):
    __tablename__ = "series"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)

    comics = relationship("Comic", back_populates="serie")


class Comic(Base, TimestampsMixin):
    __tablename__ = "comics"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    serie_number = Column(Integer, nullable=False)
    isbn = Column(String)
    serie_id = Column(Integer, ForeignKey("series.id"), nullable=False)

    serie = relationship("Serie", back_populates="comics")
