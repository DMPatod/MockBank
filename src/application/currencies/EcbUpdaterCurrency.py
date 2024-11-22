from src.application.InitApplication import mediator
from src.application.currencies.commands.RangeUpdateCurrency import RangeUpdateCurrencyRequest
from src.infrastructure.ecbClient.apis.RatesApi import RatesApi
from src.domain.currencies.Currency import Currency

class EcbUpdaterCurrency:
    async def invoke(self):
        currencies = await RatesApi().api_currency_get_async()
        await mediator.send(
            RangeUpdateCurrencyRequest(
                currencies=map(lambda c: Currency(name=c.currency, rate=c.rate),currencies),
                time=currencies[0].time
            ))