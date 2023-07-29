from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import crud, schemas
from app.models import User
from app.database import get_db

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserRead)
def registerUser(user_data: schemas.UserBase, db: Session = Depends(get_db)):
    existing_user = crud.get_user_by_email(db, email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    new_user = crud.create_user(db, user_data)
    return new_user

@router.post("/login/")
def login_user(login_data: schemas.UserBase, db: Session = Depends(get_db)):
    user = crud.get_user_by_email(db, email=login_data.email)
    if not user or not crud.verify_password(login_data.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    return {"status": True, "message": "Login Successfully", "data": {"id": user.id, "email": user.email}}
