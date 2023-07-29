from sqlalchemy import Column, Integer, String, DateTime, func
from app.database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    
    # Add the created_date column with the default value as the current timestamp
    created_date = Column(DateTime(timezone=True), server_default=func.now(), index=True)
