import asyncio
import json
import pytest
from sqlalchemy import insert
from src.database.db import Base, engine, async_session_maker

from src.accounts.models import Account
from src.instruments.models import Instrument
from src.operations.models import Operation
from src.transactions.models import Transaction


@pytest.fixture(scope="session", autouse=True)
async def prepare_database():
    """Prepare database by importing all the test data."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    def open_mock_json(model: str):
        with open(f"tests/mock_{model}.json") as file:
            return json.load(file)

    async with async_session_maker() as session:
        insert_accounts = insert(Account).values(open_mock_json("accounts"))
        insert_instruments = insert(Instrument).values(open_mock_json("instruments"))
        insert_operations = insert(Operation).values(open_mock_json("operations"))
        insert_transactions = insert(Transaction).values(open_mock_json("transactions"))

        await session.execute(insert_accounts)
        await session.execute(insert_instruments)
        await session.execute(insert_operations)
        await session.execute(insert_transactions)


@pytest.fixture(scope="session")
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()
