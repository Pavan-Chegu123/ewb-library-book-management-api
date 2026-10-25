"""HTTP endpoints for the Book resource."""
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from . import crud, schemas
from .database import get_db

router = APIRouter(prefix="/books", tags=["Books"])


@router.post("/", response_model=schemas.BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_book(db, book)
    except ValueError as exc:
        raise HTTPException(status_code=409, detail=str(exc)) from exc


@router.get("/", response_model=list[schemas.BookResponse])
def list_books(
    title: str | None = Query(default=None, description="Filter by part of a title"),
    author: str | None = Query(default=None, description="Filter by part of an author name"),
    category: str | None = Query(default=None, description="Filter by category"),
    available: bool | None = Query(default=None, description="Filter by availability"),
    db: Session = Depends(get_db),
):
    return crud.get_books(db, title=title, author=author, category=category, available=available)


@router.get("/{book_id}", response_model=schemas.BookResponse)
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found.")
    return book


@router.put("/{book_id}", response_model=schemas.BookResponse)
def replace_book(book_id: int, book: schemas.BookUpdate, db: Session = Depends(get_db)):
    try:
        updated = crud.update_book(db, book_id, book)
    except ValueError as exc:
        raise HTTPException(status_code=409, detail=str(exc)) from exc
    if updated is None:
        raise HTTPException(status_code=404, detail="Book not found.")
    return updated


@router.delete("/{book_id}")
def remove_book(book_id: int, db: Session = Depends(get_db)):
    if not crud.delete_book(db, book_id):
        raise HTTPException(status_code=404, detail="Book not found.")
    return {"message": f"Book {book_id} deleted successfully."}
