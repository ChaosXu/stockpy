from stockpy.expr.base import Expr
from stockpy.expr.base import ExprCtx


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

    def eval(self, stock: ExprCtx, year: int, quarter: int):
        return stock.crawl_metrics(self.__stat, self.__name, year, quarter)
