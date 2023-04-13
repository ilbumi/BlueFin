from sqlalchemy import Column, ForeignKey, Integer, Double
from database import Base
from sqlalchemy.orm import Mapped, mapped_column


class Operation(Base):
    __tablename__ = "operations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"))
    instrument_id: Mapped[int] = mapped_column(ForeignKey("instruments.id"))
    amount = Column(Double, nullable=False)
