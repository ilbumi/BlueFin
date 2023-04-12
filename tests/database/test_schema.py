from tests.utils import open_mock_json
from domains.transactions.dao import TransactionDAO


async def test_dao_find_all():
    transactions_data = open_mock_json("transactions")

    stored_transactions_data = await TransactionDAO.find_all()

    assert len(transactions_data) == len(stored_transactions_data)
