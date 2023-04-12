from database import BaseDAO
from .models import Transaction


class TransactionDAO(BaseDAO):
    model = Transaction
