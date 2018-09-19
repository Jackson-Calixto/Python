from sqlalchemy import Column
from sqlalchemy.types import Integer, Unicode
from myrestproj.model import DeclarativeBase
class car(DeclarativeBase):
    __tablename__ = 'car'

    carid = Column(Integer, primary_key=True)
    make = Column(Unicode(40), nullable=False, default='')
    model = Column(Unicode(40), nullable=False, default='')
    year = Column(Integer, nullable=False, default='')
    transmission = Column(Unicode(10), nullable=False, default='')
