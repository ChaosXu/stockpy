from stockpy.expr.base import Expr
from stockpy.expr.base import ExprCtx


class Crawl(Expr):
    '''Crawl the metrics from stockpy.the outer source'''

    def __init__(self, name: str):
        '''
        Args:
            name: the name of the metrics to be crawled
        '''
        self.name = name

    def eval(self, stock: ExprCtx, year: int, period: int):
        return 10
        # raise NotImplementedError("TBD")
