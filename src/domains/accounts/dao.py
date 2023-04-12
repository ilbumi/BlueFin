from database import BaseDAO
from .models import Account


class AccountDAO(BaseDAO):
    model = Account
