from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.models import User
from app.database import SessionLocal
from typing import List
from app.database import get_db

router = APIRouter()


@router.post("/", status_code=201, response_model=schemas.UserRead)
def registerUser(user_data: schemas.UserBase, db: Session = Depends(get_db)):
    existing_user = crud.get_user_by_email(db, email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = crud.create_user(db, user_data)
    return new_user
