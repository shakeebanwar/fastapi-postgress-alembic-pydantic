import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Item
from app.database import Base, SQLALCHEMY_DATABASE_URL

# Connect to the database
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Item Table seeder
def create_item(name, description):
    item = Item(name=name, description=description)
    session = SessionLocal()
    session.add(item)
    session.commit()
    session.close()

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)  #is line ka faida ya ha ka agar database ma ya table nhi bana hoa tu phala ya usko create karaga then data populate honga

    # Read data from the JSON file
    with open("seed_data.json", "r") as file:
        items_data = json.load(file)

    # Seed the database with the data from the JSON file
    for item_data in items_data:
        create_item(name=item_data["name"], description=item_data["description"])
