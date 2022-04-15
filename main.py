from fastapi import FastAPI
from fastapi import APIRouter
from currencyRate.api import controller as currency_rate

app = FastAPI(title="Currency Rates HN API", version="1.0.0")

router = APIRouter(
    prefix="/api/v1"
)

router.include_router(currency_rate.router)

app.include_router(router)
