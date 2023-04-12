from database import BaseDAO
from .models import Instrument


class InstrumentDAO(BaseDAO):
    model = Instrument
