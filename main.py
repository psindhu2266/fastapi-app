from fastapi import FastAPI, HTTPException, Depends

#import modules from other py files
from config.engine import SessionLocal, engine
from config.tables import Base
from routers import users
from config.engine import engine

fapp = FastAPI()
@fapp.get("/")
def read_root():
    return {"message": "My First FastAPI app"}

Base.metadata.create_all(bind=engine)

fapp.include_router(users.router)