import asyncio
import pytest
from sqlalchemy import insert
from database.database import Base, engine, async_session_maker

from domains.accounts.models import Account
from domains.instruments.models import Instrument
from domains.operations.models import Operation
from domains.transactions.models import Transaction
from tests.utils import open_mock_json


@pytest.fixture(scope="session", autouse=True)
async def prepare_database():
    """Prepare database by importing all the test data."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    async with async_session_maker() as session:
        insert_accounts = insert(Account).values(open_mock_json("accounts"))
        insert_instruments = insert(Instrument).values(open_mock_json("instruments"))
        insert_operations = insert(Operation).values(open_mock_json("operations"))
        insert_transactions = insert(Transaction).values(open_mock_json("transactions"))

        await session.execute(insert_accounts)
        await session.execute(insert_instruments)
        await session.execute(insert_operations)
        await session.execute(insert_transactions)
        await session.commit()


@pytest.fixture(scope="session")
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()
