from pydantic import BaseModel


class Rates(BaseModel):
    sale: float
    buy: float


class BankResponse(BaseModel):
    name: str
    usd: Rates
    eur: Rates
    web: str
