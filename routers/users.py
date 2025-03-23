from fastapi import APIRouter, Depends
from models.models import UserCreate, UserResponse
from sqlalchemy.orm import Session
from config.engine import get_db
from services.user_service import UserService
from typing import List

router = APIRouter()
user_service = UserService()

@router.get("/users/",response_model=list[UserResponse])
async def get_all_users(db: Session = Depends(get_db)):
    out = UserService.get_all_users(db)
    return out

@router.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    out = UserService.get_user(user_id, db)
    return out

@router.post("/users",response_model= UserResponse)
async def create_user(user : UserCreate, db: Session = Depends(get_db)):
    out = UserService.create_user(user, db)
    return out

@router.delete("/users/")
async def delete_all_users(db: Session = Depends(get_db)):
    out = UserService.delete_all_users(db)
    return out

@router.delete("/users/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    out = UserService.delete_user(user_id, db)
    return out

@router.patch("/users/{user_id}")
async def partially_update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    out = UserService.partially_update_user(user_id, user, db)
    return out