from database import BaseDAO
from .models import Operation


class OperationDAO(BaseDAO):
    model = Operation
