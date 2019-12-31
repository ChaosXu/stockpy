from stockpy.model.meta import StockMeta
from stockpy.model.statement import Statement, StatementMixin
from stockpy.metrics import MetricsMixin
from stockpy.expr import ExprCtx, BooleanExpr
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

    def get_metrics(self, name: str, year, quarter):
        # TBD
        if name.index('i_') == 0:
            return self.__info[name[2:]]
        else:
            return self.eval(self, name, year, quarter)

    def crawl_metrics(self, stat, name, year, quarter):
        # TBD
        try:
            return self.statement.metrics(self.__info['ts_code'], stat, name, year, quarter)[0]
        except IndexError:
            return None

    def valuate(self):
        pass


class Stocks:

    def __init__(self, stat: Statement, data: pd.DataFrame):
        self.__data = data
        self.__stat = stat

    def __iter__(self):
        for index, row in self.__data.iterrows():
            yield Stock(self.__stat, row)

    def __getitem__(self, index):
        return Stock(self.__stat, self.__data.iloc[index])

    def __len__(self):
        return len(self.__data.iterrows())

    def to_excel(self, file_path: str):

        def to_file():
            with pd.ExcelWriter(file_path,
                                date_format='YYYY-MM-DD',
                                datetime_format='YYYY-MM-DD HH:MM:SS') as writer:
                self.__data.to_excel(writer)
        try:
            to_file()
        except FileNotFoundError:
            os.makedirs(os.path.dirname(file_path))
            to_file()

    def queryByInfo(self, filter: BooleanExpr):
        '''filter by stock's info'''
        rs = []
        for stock in self:
            if filter.eval(stock, None, None) is True:
                rs.append(stock)
        return rs

    def queryByMetrics(self, year: int, quarter: int, filter: BooleanExpr):
        '''filter by stock's metrics'''
        rs = []
        for stock in self:
            if filter.eval(stock, year, quarter) is True:
                rs.append(stock)
        return rs
