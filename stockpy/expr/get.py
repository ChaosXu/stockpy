from stockpy.expr.base import Expr
from stockpy.expr.base import ExprCtx


class Get(Expr):
    '''Get a metrics value  from the ExprCtx'''

    def __init__(self, name: str,
                 period: str = 'q',
                 increment: bool = False):
        '''
        Args:
            name: metrics name.
            period: returns quarter data or year data.
            increment: Get the increment value bettwen two quarters if true.
        '''
        self._name = name
        self._increment = increment
        self._period = period

    def eval(self, stock: ExprCtx, year: int, quarter: int):
        if self._increment is True:
            return self.__eval_inc(stock, year, quarter)

        if self._period == 'y':
            return self.__eval_last_y(stock, year, quarter)

        # default is q
        return stock.get_metrics(self._name, year, quarter)

    def __eval_inc(self, stock: ExprCtx, year: int, quarter: int):
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

    def __eval_last_y(self, stock: ExprCtx, year: int, quarter: int):
        if quarter != 4:
            year -= 1
        return stock.get_metrics(self._name, year, 4)
