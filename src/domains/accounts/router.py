from fastapi import APIRouter

from .schema import AccountResponse, AccountFilterRequest
from .dao import AccountDAO

router = APIRouter(prefix="/accounts", tags=["Accounts"])


@router.post("/get")
async def get_accounts(body: AccountFilterRequest) -> list[AccountResponse]:
    print(body.dict(exclude_none=True))
    results = await AccountDAO.find_all(**(body.dict(exclude_none=True)))
    return results
