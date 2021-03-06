from fastapi import APIRouter
from currencyRate.services.scraper import get_occidente_currency_rates, get_ficohsa_currency_rates, \
    get_banpais_currency_rates, get_atlantida_currency_rates

from currencyRate.api.responses.models import BankResponse

router = APIRouter(
    tags=["Currency Rates"],
    prefix="/currency_rates"
)


@router.get("/occ", response_model=BankResponse)
async def get_occidente_currency_rate():
    return await get_occidente_currency_rates()


@router.get("/fic", response_model=BankResponse)
async def get_ficohsa_currency_rate():
    return await get_ficohsa_currency_rates()


@router.get("/bnp", response_model=BankResponse)
async def get_banpais_currency_rate():
    return await get_banpais_currency_rates()


@router.get("/atl", response_model=BankResponse)
async def get_atlantida_currency_rate():
    return await get_atlantida_currency_rates()


@router.get("/get_all", response_model=list[BankResponse])
async def get_all_banks_currency_rates():
    occidente = await get_occidente_currency_rates()
    ficohsa = await get_ficohsa_currency_rates()
    banpais = await get_banpais_currency_rates()
    atlantida = await get_atlantida_currency_rates()

    return [occidente, ficohsa, banpais, atlantida]
