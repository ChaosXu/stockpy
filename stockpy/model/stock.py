from stockpy.model.meta import StockMeta
from stockpy.model.statement import Statement
import pandas as pd


class Stock(metaclass=StockMeta):

    def __init__(self, state: Statement, info: pd.Series):
        self.__state = state
        self.__info = info

    def __getattr__(self, key):
        try:
            return self.__info[key]
        except KeyError:
            raise AttributeError('Stock has no attribute "%s"' % key)

    def __index__(self, key):
        try:
            return self.__info[key]
        except KeyError:
            raise AttributeError('Stock has no attribute "%s"' % key)
