# models.py
from pydantic import BaseModel, Field
from typing import Optional

# Schema for creating a new book
class BookCreate(BaseModel):
    title: str = Field(..., min_length=1, description="Title of the book")
    author: str = Field(..., min_length=1, description="Author of the book")
    year: Optional[int] = Field(None, description="Year of publication")

# Schema for reading book data
class BookRead(BookCreate):
    id: int

    class Config:
        orm_mode = True  # Enables ORM compatibility

