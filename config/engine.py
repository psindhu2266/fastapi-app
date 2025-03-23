from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.constraints import DATABASE_URL

def get_db_url():
    return DATABASE_URL

#create database engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

#create local session 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()