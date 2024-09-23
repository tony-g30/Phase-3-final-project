from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Reservation(Base):
    __tablename__ = 'reservations'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    table_id = Column(Integer, ForeignKey('tables.id'), nullable=False)
    reservation_time = Column(String, nullable=False)  
    guests = Column(Integer, nullable=False)

    customer = relationship('Customer', back_populates='reservations')
    table = relationship('Table')  # Define the relationship to Table
