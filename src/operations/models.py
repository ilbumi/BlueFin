from sqlalchemy import Column, ForeignKey, Integer, Double
from ..database.db import Base


class Operation(Base):
    __tablename__ = "operations"

    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey("accounts.id"))
    instrument_id = Column(Integer, ForeignKey("instruments.id"))
    amount = Column(Double, nullable=False)
