"""Database operations for books."""
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from . import models, schemas


def create_book(db: Session, book: schemas.BookCreate) -> models.Book:
    db_book = models.Book(**book.model_dump())
    db.add(db_book)
    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        raise ValueError("A book with this ISBN already exists.") from exc
    db.refresh(db_book)
    return db_book


def get_books(
    db: Session,
    title: str | None = None,
    author: str | None = None,
    category: str | None = None,
    available: bool | None = None,
) -> list[models.Book]:
    query = db.query(models.Book)
    if title:
        query = query.filter(models.Book.title.ilike(f"%{title.strip()}%"))
    if author:
        query = query.filter(models.Book.author.ilike(f"%{author.strip()}%"))
    if category:
        query = query.filter(models.Book.category.ilike(f"%{category.strip()}%"))
    if available is not None:
        query = query.filter(models.Book.available == available)
    return query.order_by(models.Book.book_id).all()


def get_book(db: Session, book_id: int) -> models.Book | None:
    return db.query(models.Book).filter(models.Book.book_id == book_id).first()


def update_book(db: Session, book_id: int, book: schemas.BookUpdate) -> models.Book | None:
    db_book = get_book(db, book_id)
    if db_book is None:
        return None
    for field, value in book.model_dump().items():
        setattr(db_book, field, value)
    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        raise ValueError("A book with this ISBN already exists.") from exc
    db.refresh(db_book)
    return db_book


def delete_book(db: Session, book_id: int) -> bool:
    db_book = get_book(db, book_id)
    if db_book is None:
        return False
    db.delete(db_book)
    db.commit()
    return True
