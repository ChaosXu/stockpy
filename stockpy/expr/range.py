from stockpy.expr.base import Expr
from stockpy.expr.base import ExprCtx
from stockpy.expr.get import Get


class Range(Expr):
    '''range metrics of the last n years'''

    def __init__(self, metrics: Get, count: int):
        self._metrics = metrics
        self._count = count

    def eval(self, stock: ExprCtx, year: int, quarter: int):
        begin = year-self._count+1
        end = year+1
        ms = []
        for y in range(begin, end):
            ms.append(self._metrics.eval(stock, y, quarter))
        raise ms
