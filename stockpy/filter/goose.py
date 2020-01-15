from stockpy.model.stock import Stocks
from stockpy import expr


def gooseFilter():
    pass


class Goose:

    filter = gooseFilter()

    def perform(self, stocks: Stocks, year: int, quarter: int):
        filter = self.filter
        return stocks.queryByMetrics(year, quarter, filter)
