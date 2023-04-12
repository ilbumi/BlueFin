from sqlalchemy import Column, Integer, String
from ..database.db import Base


class Instrument(Base):
    __tablename__ = "instruments"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
