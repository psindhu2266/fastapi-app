from fastapi import FastAPI, HTTPException, Depends
from services.base import DbConnection
from models.models import UserCreate, UserResponse
from config.tables import Base, engine, User
from sqlalchemy.orm import Session
from config.engine import get_db

class UserService(DbConnection):
    def __init__(self):
        super().__init__()
    
    def create_user(user : UserCreate, db: Session = Depends(get_db)):
        db_user = User(Name=user.Name, DOB=user.DOB, City=user.City)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def get_all_users(db: Session = Depends(get_db)):
        users = db.query(User).all()
        return users

    def get_user(user_id: int, db: Session = Depends(get_db)):
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    def delete_user(user_id: int, db: Session = Depends(get_db)):
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
         raise HTTPException(status_code=404, detail="User not found")
        db.delete(user)
        db.commit()
        return {"message": "User deleted successfully"}

    def delete_all_users(db: Session = Depends(get_db)):
        user = db.query(User).all()
        db.delete(user)
        db.commit()
        return {"message": "All Users deleted successfully"}
    
    def partially_update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
        db_user = db.query(User).filter(User.id == user_id).first()
        if not db_user:
          raise HTTPException(status_code=404, detail="User not found")
        db_user.Name = user.Name
        db_user.DOB = user.DOB
        db_user.City = user.City
        db.commit()
        db.refresh(db_user)
        return db_user