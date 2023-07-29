from pydantic import BaseModel
from datetime import datetime

class ItemCreate(BaseModel):
    name: str
    description: str

class ItemRead(ItemCreate):
    id: int
    created_date: datetime  # Add the created_date field

class ItemUpdate(BaseModel):
    name: str
    description: str
