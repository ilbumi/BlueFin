from fastapi import FastAPI
from domains.accounts.router import router as router_accounts

app = FastAPI()
app.include_router(router_accounts)
