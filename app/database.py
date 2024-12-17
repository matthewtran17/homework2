import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Load environment variables from .env file
load_dotenv()

# Database connection details from environment variables
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST", "127.0.0.1")  # Default to localhost
MYSQL_PORT = os.getenv("MYSQL_PORT", "3306")       # Default MySQL port
MYSQL_DB = os.getenv("MYSQL_DB")

# Construct the DATABASE_URL
DATABASE_URL = (
    f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}"
    f"@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
)

# Create the engine (responsible for database connection)
engine = create_engine(DATABASE_URL, echo=True)

# Session for interacting with the database
SessionLocal = sessionmaker(bind=engine)

# Base class for models
Base = declarative_base()
