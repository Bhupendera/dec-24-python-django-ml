import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
    if not SQLALCHEMY_DATABASE_URI:
        raise ValueError("No DATABASE_URI set for SQLAlchemy database.")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
