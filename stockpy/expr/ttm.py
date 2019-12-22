from stockpy.expr.base import Expr
from stockpy.expr.base import ExprCtx
from stockpy.expr.get import Get


class TTM(Expr):
    '''Sum of the last 4 quarters'''

    def __init__(self, metrics: Get):
        self._metrics = metrics

    def eval(self, stock: ExprCtx, year: int, quarter: int):
        yq = self._quarters(year, quarter)
        sum = 0.0
        for y, qs in yq.items():
            for q in qs:
                sum += self._metrics.eval(stock, y, q)
        return sum

    def _quarters(self, year: int, quarter: int):
        yq = {year: [q for q in range(1, quarter+1)]}
        if quarter < 4:
            yq[year-1] = [q for q in range(4, quarter, -1)]
        return yq
