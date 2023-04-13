from sqlalchemy import Integer, String
from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base


class Instrument(Base):
    __tablename__ = "instruments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    operations: Mapped[List["Operation"]] = relationship(back_populates="instrument")
