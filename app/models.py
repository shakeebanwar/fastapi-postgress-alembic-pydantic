from sqlalchemy import Column, Integer, String, DateTime, func
from app.database import Base
from datetime import datetime
import bcrypt

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    created_date = Column(DateTime(timezone=True), server_default=func.now(), index=True)



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    last_login = Column(DateTime, default=datetime.utcnow)


    def set_password(self, password: str):
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.password = password_hash.decode('utf-8')