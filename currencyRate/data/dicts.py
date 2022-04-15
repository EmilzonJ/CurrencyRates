banks = [
    {
        "name": "Banco de Occidente S.A.",
        "code": "OCC",
        "web": "https://www.bancodeoccidente.hn/",
        "rates": {
            "sale": {
                "usd": "//div[@id='dollar-panel-1']//div[@class='cell currency-block grid-y auto'][1]//span["
                       "@class='forest']/strong[2]/text()",
                "eur": "//div[@id='euro-panel-2']//div[@class='cell currency-block grid-y auto'][1]//span["
                       "@class='forest']/strong[2]/text()"
            },
            "buy": {
                "usd": "//div[@id='dollar-panel-1']//div[@class='cell currency-block grid-y auto'][2]//span["
                       "@class='forest']/strong[2]/text()",
                "eur": "//div[@id='euro-panel-2']//div[@class='cell currency-block grid-y auto'][2]//span["
                       "@class='forest']/strong[2]/text()"
            }
        }
    },
    {
        "name": "Banco FICOHSA'",
        "code": "FIC",
        "web": "https://www.ficohsa.com/hn/honduras/tipo-cambio/",
        "rates": {
            "sale": {
                "usd": "/html/body/div[2]/div[1]/article[1]/p[2]/span[2]/span/span/text()",
                "eur": "/html/body/div[2]/div[1]/article[1]/p[7]/span[3]/span[2]/text()"
            },
            "buy": {
                "usd": "/html/body/div[2]/div[1]/article[1]/p[1]/span[2]/span/span/text()",
                "eur": "/html/body/div[2]/div[1]/article[1]/p[6]/span[4]/span/span/text()"
            }
        }
    },
    {
        "name": "Banco Atlántida'",
        "code": "ATL",
        "web": "https://www.bancatlan.hn/js/moneda.js"
    },
    {
        "name": "BANPAIS",
        "code": "BNP",
        "web": "https://www.banpais.hn/divisas/barradolar.php",
        "rates": {
            "sale": {
                "usd": "//div[@class='frameTasa-container-tasa-item'][1]//div["
                       "@class='frameTasa-container-tasa-item-prices'][1]//div[@class='conteTasa']/p[2]/text()",
                "eur": "//div[@class='frameTasa-container-tasa-item'][1]//div["
                       "@class='frameTasa-container-tasa-item-prices'][2]//div[@class='conteTasa']/p[2]/text()"
            },
            "buy": {
                "usd": "//div[@class='frameTasa-container-tasa-item'][1]//div["
                       "@class='frameTasa-container-tasa-item-prices'][1]//div[@class='conteTasa']/p[1]/text()",
                "eur": "//div[@class='frameTasa-container-tasa-item'][1]//div["
                       "@class='frameTasa-container-tasa-item-prices'][2]//div[@class='conteTasa']/p[1]/text() "
            }
        }
    }
]

currencies = [
    {
        "name": "US Dollar",
        "code": "usd",
        "symbol": "$"
    },
    {
        "name": "euro",
        "code": "eur",
        "symbol": "€"
    }
]
