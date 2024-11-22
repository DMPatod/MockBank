from datetime import datetime

from sqlalchemy.orm import Session
from src.domain.currencies.Currency import Currency

class CurrencyRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, currency: Currency):
        pass

    async def add_range(self, currencies: list[Currency], time: datetime):
        for item in currencies:
            print(item.rate)