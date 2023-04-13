from tests.utils import open_mock_json
from domains.transactions.dao import TransactionDAO
from domains.operations.dao import OperationDAO
from domains.accounts.dao import AccountDAO


async def test_dao_find_all():
    transactions_data = open_mock_json("transactions")

    stored_transactions_data = await TransactionDAO.find_all()

    assert transactions_data == stored_transactions_data


async def test_dao_filters():
    operations_data = [
        op for op in open_mock_json("operations") if op["account_id"] == 0
    ]
    stored_operations_data = await OperationDAO.find_all(account_id=0)
    assert len(operations_data) == len(stored_operations_data)


async def test_dao_create():
    await AccountDAO.create(id=2, name="account2")
    stored_operations_data = await AccountDAO.find_all(name="account2")
    assert stored_operations_data[0].name == "account2"
