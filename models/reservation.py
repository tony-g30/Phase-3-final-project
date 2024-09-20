from sqlalchemy import Column, Integer, ForeignKey, DateTime
from models.database import Base

class Reservation(Base):
    __tablename__ = 'reservations'

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    table_number = Column(Integer, ForeignKey('tables.number'), nullable=False)
    time = Column(DateTime, nullable=False)
