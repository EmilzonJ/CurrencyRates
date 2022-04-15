# parser service
from currencyRate.services.parsers import parse_bank_web as html_parser
from currencyRate.services.parsers import parse_text_that_contains_money_info_from_atlantida as atlantida_html_parser

# banks
from currencyRate.data.dicts import banks

OCC: dict = list(filter(lambda item: item['code'] == 'OCC', banks))[0]
FIC: dict = list(filter(lambda item: item['code'] == 'FIC', banks))[0]
ATL: dict = list(filter(lambda item: item['code'] == 'ATL', banks))[0]
BNP: dict = list(filter(lambda item: item['code'] == 'BNP', banks))[0]

# banks webs
OCC_WEB: str = OCC['web']
FIC_WEB: str = FIC['web']
ATL_WEB: str = ATL['web']
BNP_WEB: str = BNP['web']

# Bank rates sale xpaths
OCC_RATES_SALE_XPATHS = OCC['rates']['sale']
FIC_RATES_SALE_XPATHS = FIC['rates']['sale']
BNP_RATES_SALE_XPATHS = BNP['rates']['sale']

# Bank rates buy xpaths
OCC_RATES_BUY_XPATHS = OCC['rates']['buy']
FIC_RATES_BUY_XPATHS = FIC['rates']['buy']
BNP_RATES_BUY_XPATHS = BNP['rates']['buy']


# Currency rates of banks
async def get_occidente_currency_rates() -> dict:
    usd_sale: float = await scrap(OCC_WEB, OCC_RATES_SALE_XPATHS['usd'])
    usd_buy: float = await scrap(OCC_WEB, OCC_RATES_BUY_XPATHS['usd'])

    eur_sale: float = await scrap(OCC_WEB, OCC_RATES_SALE_XPATHS['eur'])
    eur_buy: float = await scrap(OCC_WEB, OCC_RATES_BUY_XPATHS['eur'])

    return {"name": f"{OCC['name']}", "usd": {"sale": usd_sale, "buy": usd_buy},
            "eur": {"sale": eur_sale, "buy": eur_buy}, "web": f"{OCC_WEB}"}


async def get_ficohsa_currency_rates() -> dict:
    usd_sale: float = await scrap(FIC_WEB, FIC_RATES_SALE_XPATHS['usd'])
    usd_buy: float = await scrap(FIC_WEB, FIC_RATES_BUY_XPATHS['usd'])

    eur_sale: float = await scrap(FIC_WEB, FIC_RATES_SALE_XPATHS['eur'])
    eur_buy: float = await scrap(FIC_WEB, FIC_RATES_BUY_XPATHS['eur'])

    return {"name": f"{FIC['name']}", "usd": {"sale": usd_sale, "buy": usd_buy},
            "eur": {"sale": eur_sale, "buy": eur_buy}, "web": f"{FIC_WEB}"}


async def get_banpais_currency_rates() -> dict:
    usd_sale: float = await scrap(BNP_WEB, BNP_RATES_SALE_XPATHS['usd'])
    usd_buy: float = await scrap(BNP_WEB, BNP_RATES_BUY_XPATHS['usd'])

    eur_sale: float = await scrap(BNP_WEB, BNP_RATES_SALE_XPATHS['eur'])
    eur_buy: float = await scrap(BNP_WEB, BNP_RATES_BUY_XPATHS['eur'])

    return {"name": f"{BNP['name']}", "usd": {"sale": usd_sale, "buy": usd_buy},
            "eur": {"sale": eur_sale, "buy": eur_buy}, "web": f"{BNP_WEB}"}


async def get_atlantida_currency_rates() -> dict:
    request_text = await atlantida_html_parser(ATL_WEB)

    usd_sale: float = float(request_text[1215:1222])
    usd_buy: float = float(request_text[1186:1193])

    eur_sale: float = float(request_text[1278:1285])
    eur_buy: float = float(request_text[1250:1257])

    return {"name": f"{ATL['name']}", "usd": {"sale": usd_sale, "buy": usd_buy},
            "eur": {"sale": eur_sale, "buy": eur_buy}, "web": f"{ATL_WEB}"}


# scraper
async def scrap(web: str, xpath: str) -> float:
    parsed = await html_parser(web)
    result: float = float(parsed.xpath(xpath)[0])
    return result
