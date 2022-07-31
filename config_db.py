# Project imports
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# To create a database engine
SQLALCHEMY_DATABASE_URL = "sqlite:///./chinook.db" 
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
# connect_args={"check_same_thread": False} its onyly used for sqlite

# To create a local database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# To create an instance of DeclarativeMeta
Base = declarative_base()

