from sqlalchemy import Column, Integer, String
from pydantic import BaseModel

class UserCreate(BaseModel):
    Name: str
    DOB: str
    City: str

class UserResponse(UserCreate):
    id: int