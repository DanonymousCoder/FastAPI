from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import controllers, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()