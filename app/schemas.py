from pydantic import BaseModel,EmailStr, constr
from datetime import datetime


#items
class ItemCreate(BaseModel):
    name: str
    description: str

class ItemRead(ItemCreate):
    id: int
    created_date: datetime  # Add the created_date field

class ItemUpdate(BaseModel):
    name: str
    description: str



#users

class UserBase(BaseModel):
    email: EmailStr
    password: constr(min_length=8, max_length=16)


class UserRead(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True

