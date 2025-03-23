from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from config.engine import get_db_url

Base = declarative_base()

class User(Base):
    __tablename__ = "users_data"
    id = Column(Integer, primary_key=True, index=True)
    Name = Column(String, index=True)
    DOB = Column(String)
    City = Column(String)

engine = create_engine(get_db_url())
Base.metadata.create_all(bind=engine)