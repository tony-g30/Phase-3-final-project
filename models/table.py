from sqlalchemy import Column, Integer
from models.database import Base

class Table(Base):
    __tablename__ = 'tables'

    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, unique=True, nullable=False)
    capacity = Column(Integer, nullable=False)
