from .database import engine, Base, SessionLocal

Base.metadata.create_all(bind=engine)
