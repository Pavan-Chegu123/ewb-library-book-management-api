"""Pydantic request/response validation schemas."""
from pydantic import BaseModel, ConfigDict, Field, field_validator


class BookBase(BaseModel):
    title: str = Field(min_length=1, max_length=150)
    author: str = Field(min_length=2, max_length=100)
    isbn: str = Field(min_length=10, max_length=20)
    publication_year: int | None = Field(default=None, ge=1000, le=2100)
    category: str | None = Field(default=None, max_length=60)
    available: bool = True

    @field_validator("title", "author", "isbn")
    @classmethod
    def strip_required_text(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("This field cannot be blank.")
        return value


class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    pass


class BookResponse(BookBase):
    book_id: int
    model_config = ConfigDict(from_attributes=True)
