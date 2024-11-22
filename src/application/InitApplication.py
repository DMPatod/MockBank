from src.application.currencies.commands.RangeUpdateCurrency import RangeUpdateCurrencyRequest, \
    range_update_currency_handler
from src.domain.core.Mediator import Mediator

mediator = Mediator()

mediator.register(RangeUpdateCurrencyRequest, range_update_currency_handler)
