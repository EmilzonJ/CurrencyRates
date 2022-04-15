from fastapi import FastAPI
from fastapi import APIRouter
from currencyRate.api import controller as currency_rate

app = FastAPI()

router = APIRouter(
    prefix="/api/v1"
)

router.include_router(currency_rate.router)

app.include_router(router)
