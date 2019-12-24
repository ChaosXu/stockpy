from stockpy.model.meta import StockMeta
from stockpy.model.statement import Statement
from stockpy.expr.base import ExprCtx
import pandas as pd
import os


class ExprCtxMixin(ExprCtx):

    def __init__(self):
        self.meta = None

    def eval(self, stock: ExprCtx, year: int, quarter: int):
        pass


class Stock(ExprCtxMixin, metaclass=StockMeta):

    def __init__(self, state: Statement, info: pd.Series):
        super().__init__()
        self.__state = state
        self.__info = info

    def __getattr__(self, key):
        try:
            return self.__info[key]
        except KeyError:
            raise AttributeError('Stock has no field "%s"' % key)

    def __getitem__(self, key):
        try:
            return self.__info[key]
        except KeyError:
            raise AttributeError('Stock has no field "%s"' % key)


class Stocks():

    def __init__(self, stat: Statement, data: pd.DataFrame):
        self.__data = data
        self.__stat = stat

    def __iter__(self):
        for index, row in self.__data.iterrows():
            yield Stock(self.__stat, row)

    def to_excel(self, path: str):

        def to_file():
            with pd.ExcelWriter(path+r'/stocks.xlsx',
                                date_format='YYYY-MM-DD',
                                datetime_format='YYYY-MM-DD HH:MM:SS') as writer:
                self.__data.to_excel(writer)
        try:
            to_file()
        except FileNotFoundError:
            os.makedirs(path)
            to_file()
