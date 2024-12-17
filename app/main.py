# main.py
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from schemas import Base
from models import BookCreate, BookRead
import crud

# Initialize FastAPI app
app = FastAPI(title="Book Management System")

# Create database tables
Base.metadata.create_all(bind=engine)

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route: Create a new book
@app.post("/books/", response_model=BookRead)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db=db, book=book)

# Route: Get all books
@app.get("/books/", response_model=list[BookRead])
def get_books(db: Session = Depends(get_db)):
    return crud.get_books(db=db)

# Route: Delete a book
@app.delete("/books/{book_id}", response_model=BookRead)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.delete_book(db=db, book_id=book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

