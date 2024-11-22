from datetime import datetime


class Rate:
    def __init__(self, currency: str, rate: float, time: datetime):
        self.currency = currency
        self.rate = rate
        self.time = time