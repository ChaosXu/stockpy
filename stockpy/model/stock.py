from stockpy.model.meta import StockMeta
from stockpy.model.statement import Statement, StatementMixin
from stockpy.metrics import MetricsMixin
from stockpy.expr.base import ExprCtx
import pandas as pd
import os


class Stock(ExprCtx, MetricsMixin, StatementMixin, metaclass=StockMeta):

    def __init__(self, stat: Statement, info: pd.Series):
        ExprCtx.__init__(self)
        MetricsMixin.__init__(self)
        StatementMixin.__init__(self, stat, info['ts_code'])
        self.__info = info

    def __getitem__(self, key):
        try:
            return self.__info[key]
        except KeyError:
            raise AttributeError('Stock has no field "%s"' % key)

    def get_metrics(self, name, year, quarter):
        return self.eval(self, name, year, quarter)

    def crawl_metrics(self, stat, name, year, quarter):
        return self.statement.metrics(self.__info['ts_code'], stat, name, year, quarter)


class Stocks():

    def __init__(self, stat: Statement, data: pd.DataFrame):
        self.__data = data
        self.__stat = stat

    def __iter__(self):
        for index, row in self.__data.iterrows():
            yield Stock(self.__stat, row)

    def __getitem__(self, index):
        return Stock(self.__stat, self.__data.iloc[index])

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
