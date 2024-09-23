from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = 'postgresql://oleng:audo@localhost/restaurant_reservation_db'

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()

def init_db():
    from models.customer import Customer
    from models.reservation import Reservation
    from models.table import Table
    Base.metadata.create_all(bind=engine)
def get_session():
    return Session() 