"""SQLAlchemy table definitions."""
from sqlalchemy import Boolean, Column, Integer, String
from .database import Base


class Book(Base):
    __tablename__ = "books"

    book_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(150), nullable=False, index=True)
    author = Column(String(100), nullable=False, index=True)
    isbn = Column(String(20), unique=True, index=True, nullable=False)
    publication_year = Column(Integer, nullable=True)
    category = Column(String(60), nullable=True)
    available = Column(Boolean, nullable=False, default=True)
