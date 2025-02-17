from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session

import os

from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

SECRECT_KEY = os.getenv("SECRET_KEY")
#db = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

db = "sqlite:////media/databases/myshop.db"

engine = create_engine(db, echo = False)

Base = declarative_base()

session = Session(engine)
