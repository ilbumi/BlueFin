from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column
from database import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    source_operation_id: Mapped[int] = mapped_column(ForeignKey("operations.id"))
    target_operation_id: Mapped[int] = mapped_column(ForeignKey("operations.id"))
    fee_operation_id: Mapped[int] = mapped_column(ForeignKey("operations.id"))
