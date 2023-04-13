from sqlalchemy import Column, ForeignKey, Integer, Double
from database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Operation(Base):
    __tablename__ = "operations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"))
    account: Mapped["Account"] = relationship(back_populates="operations")

    instrument_id: Mapped[int] = mapped_column(ForeignKey("instruments.id"))
    instrument: Mapped["Instrument"] = relationship(back_populates="operations")

    amount = Column(Double, nullable=False)
