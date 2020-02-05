from stockpy.expr.base import Expr
from stockpy.expr.base import ExprCtx
from stockpy.expr.base import ExprValue
from stockpy.expr.base import trace
from math import isnan


class Crawl(Expr):
    '''Crawl the metrics from stockpy.the outer source'''

    def __init__(self, stat: str, name: str):
        '''
        Args:
            stat: the name of the statement
            name: the name of the metrics to be crawled
        '''
        self.__stat = stat
        self.__name = name

    @trace
    def eval(self, stock: ExprCtx, year: int, quarter: int):
        v = stock.crawl_metrics(self.__stat, self.__name, year, quarter)
        if v is None:
            raise Exception(
                f'crawl_metrics {stock["ts_code"]}({stock["name"]}) {self.__stat} {self.__name} {year} {quarter} None')
        if isnan(v):
            v = 0
        return ExprValue(year, quarter, v)

    def __str__(self):
        return "Crawl('{}', '{}')".format(self.__stat, self.__name)
