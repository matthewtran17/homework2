# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Database connection details
DATABASE_URL = "mysql+mysqlconnector://root:@localhost:127.0.0.1/bookdb"

# Create the engine (responsible for database connection)
engine = create_engine(DATABASE_URL, echo=True)

# Session for interacting with the database
SessionLocal = sessionmaker(bind=engine)

# Base class for models
Base = declarative_base()
