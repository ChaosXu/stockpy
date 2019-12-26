from stockpy.expr.base import Expr
from stockpy.expr.base import ExprCtx


class Get(Expr):
    '''Get a metrics value  from the ExprCtx'''

    def __init__(self, name: str, increment=False):
        '''
        Args:
            name: metrics name
            past_year: metrcs value before the past n year.
            increment: Get the increment value if true.
        '''
        self._name = name
        self._increment = increment

    def eval(self, stock: ExprCtx, year: int, quarter: int):
        if self._increment is True:
            v2 = stock.get_metrics(self._name, year, quarter)
            q1 = quarter
            y1 = year
            if quarter == 1:
                q1 = 4
                y1 = y1 - 1
            else:
                q1 = q1-1
            v1 = stock.get_metrics(self._name, y1, q1)
            return v2-v1
        else:
            return stock.get_metrics(self._name, year, quarter)
