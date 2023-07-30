from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import usablecrud, schemas
from app.database import SessionLocal
from typing import List
from app.database import get_db
from app.api.permission import jwtVerify


router = APIRouter()

@router.get("/", response_model=List[schemas.ItemRead])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db),user_id: int = Depends(jwtVerify)):
    items = usablecrud.get_items(db, skip=skip, limit=limit)
    return items

@router.get("/{item_id}", response_model=schemas.ItemRead)
def read_item(item_id: int, db: Session = Depends(get_db),user_id: int = Depends(jwtVerify)):
    db_item = usablecrud.get_item(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.post("/", response_model=schemas.ItemRead)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db),user_id: int = Depends(jwtVerify)):
    return usablecrud.create_item(db, item)

@router.put("/{item_id}", response_model=schemas.ItemRead)
def update_item(item_id: int, item: schemas.ItemUpdate, db: Session = Depends(get_db),user_id: int = Depends(jwtVerify)):
    db_item = usablecrud.get_item(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return usablecrud.update_item(db, item_id, item)

@router.delete("/{item_id}", response_model=schemas.ItemRead)
def delete_item(item_id: int, db: Session = Depends(get_db),user_id: int = Depends(jwtVerify)):
    db_item = usablecrud.get_item(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return usablecrud.delete_item(db, item_id)
