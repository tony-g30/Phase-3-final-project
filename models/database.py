from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://audo:password@localhost/restaurant_reservation"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

Base = declarative_base()

def init_db():
    from models.customer import Customer
    from models.table import Table
    from models.reservation import Reservation
    Base.metadata.create_all(bind=engine)
