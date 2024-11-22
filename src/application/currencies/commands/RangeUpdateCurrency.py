from datetime import datetime
from typing import List

from fastapi.params import Depends
from sqlalchemy.orm import Session

from src.domain.currencies.Currency import Currency

from src.domain.core.Mediator import Request, Response
from src.infrastructure.dataPersistence.DbContext import get_context
from src.infrastructure.dataPersistence.repositories.CurrencyRepository import CurrencyRepository


class RangeUpdateCurrencyRequest(Request):
    currencies: List[Currency]
    time: datetime

class RangeUpdateCurrencyResponse(Response):
    entities: List[Currency]

async def range_update_currency_handler(request: RangeUpdateCurrencyRequest, db_context: Session = Depends(get_context)) -> RangeUpdateCurrencyResponse:
    currency_repository = CurrencyRepository(db_context)
    entities = await currency_repository.add_range(request.currencies, request.time)
    return RangeUpdateCurrencyResponse(entities=[])