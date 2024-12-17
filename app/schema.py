# schemas.py
from sqlalchemy import Column, Integer, String
from database import Base

# Define the books table
class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)  # Primary key
    title = Column(String(100), nullable=False)        # Title column
    author = Column(String(100), nullable=False)       # Author column
    year = Column(Integer, nullable=True)              # Year column

