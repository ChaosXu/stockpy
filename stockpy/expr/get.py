from stockpy.expr.base import Expr
from stockpy.expr.base import ExprCtx
from stockpy.expr.base import trace


class Get(Expr):
    '''Get a metrics value  from the ExprCtx'''

    def __init__(self, name: str,
                 period_begin: bool = False,
                 period: str = 'q',
                 increment: bool = False,
                 var_type: str = 's'):
        '''
        Args:
            name: metrics name.
            period: returns quarter data or year data.
            increment: Get the increment value bettwen two quarters if true.
            var_type: economic variable. stock of flow. default is stock
        '''
        self._name = name
        self._period_begin = period_begin
        self._increment = increment
        self._period = period
        self._var_type = var_type

    @trace
    def eval(self, stock: ExprCtx, year: int, quarter: int):
        if self._period_begin is True:
            return self._eval_prev_y(stock, year)
        if self._increment is True:
            return self.__eval_inc(stock, year, quarter)

        if self._period == 'y':
            return self.__eval_last_y(stock, year, quarter)

        # default is q
        return stock.get_metrics(self._name, year, quarter)

    def _eval_prev_y(self, stock: ExprCtx, year: int):
        return stock.get_metrics(self._name, year-1, 4)

    def __eval_inc(self, stock: ExprCtx, year: int, quarter: int):
        v2 = stock.get_metrics(self._name, year, quarter)
        q1 = quarter
        y1 = year
        if quarter == 1:
            if self._var_type == 'f':
                return v2
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

    def __str__(self):
        if self._period_begin is True:
            return "Get('{}', period_begin={})".format(self._name,
                                                       self._period_begin)
        if self._increment is True:
            return "Get('{}', increment={})".format(self._name, self._increment)

        if self._period == 'y':
            return "Get('{}', period={})".format(self._name, self._period)

        # default is q
        return "Get('{}')".format(self._name)
