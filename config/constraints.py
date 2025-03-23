from dotenv import load_dotenv
import os

#load variable from .env file
load_dotenv()

#set the database url
DATABASE_URL = os.getenv("DATABASE_URL")
