from sqlalchemy import Column, ForeignKey, Integer
from ..database.db import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    source_operation_id = Column(Integer, ForeignKey("operations.id"))
    target_operation_id = Column(Integer, ForeignKey("operations.id"))
    fee_operation_id = Column(Integer, ForeignKey("operations.id"))
