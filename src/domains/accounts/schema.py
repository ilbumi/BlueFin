from pydantic import BaseModel
from typing import Optional


class AccountResponse(BaseModel):
    id: int
    name: str

    class Config:
        schema_extra = {"example": {"id": 0, "name": "Example name"}}
        orm_mode = True


class AccountFilterRequest(BaseModel):
    id: Optional[int]
    name: Optional[str]

    class Config:
        schema_extra = {"example": {"name": "Example name"}}
        orm_mode = True
