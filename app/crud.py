# crud.py
from sqlalchemy.orm import Session
from app.schema import Book
from app.models import BookCreate

# Create a new book
def create_book(db: Session, book: BookCreate):
    new_book = Book(**book.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

# Get all books
def get_books(db: Session):
    return db.query(Book).all()

# Get a single book by ID
def get_book_by_id(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

# Delete a book by ID
def delete_book(db: Session, book_id: int):
    book = get_book_by_id(db, book_id)
    if book:
        db.delete(book)
        db.commit()
    return book

