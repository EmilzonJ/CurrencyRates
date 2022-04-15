class Bank:
    def __init__(self, name: str, code: str, website: str):
        self.name: str = name
        self.code: str = code
        self.website: str = website


class Rate:
    def __init__(self, bank: Bank, currency: str, rate: float):
        self.bank: Bank = bank
        self.currency: str = currency
        self.rate: float = rate


class Currency:
    def __init__(self, name: str, code: str, symbol: str):
        self.name: str = name
        self.code: str = code
        self.symbol: str = symbol



