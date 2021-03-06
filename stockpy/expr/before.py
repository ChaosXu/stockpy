from stockpy.expr.base import Expr
from stockpy.expr.base import ExprCtx
from stockpy.expr.get import Get
from stockpy.expr.base import trace
import math


class Before(Expr):
    '''the value before past time'''

    def __init__(self, metrics: Get,
                 past_year: int = 0,
                 past_quarter: int = 0):
        '''
        Args:
            metrics: Get expr
            past_quarter:  returns the value before the past quarters
            past_year:  returns the value in the Q4 before the past years
        '''
        self._metrics = metrics
        self._qc = past_quarter
        self._yc = past_year

    @trace
    def eval(self, stock: ExprCtx, year: int, quarter: int):
        if self._yc != 0:
            return self.__eval_y(stock, year, quarter)
        if self._qc != 0:
            return self.__eval_q(stock, year, quarter)
        raise Exception('past_year and past_quarter can not be zero')

    def __eval_y(self, stock: ExprCtx, year: int, quarter: int):

        if quarter < 4:
            return self._metrics.eval(stock, year-self._yc-1, 4)
        return self._metrics.eval(stock, year-self._yc, 4)

    def __eval_q(self, stock: ExprCtx, year: int, quarter: int):
        q = quarter-self._qc
        if q > 0:
            return self._metrics.eval(stock, year, q)
        else:
            qc = -q
            first_y = year - math.ceil((qc+1) / 4)
            first_qc = 4 - qc % 4
            return self._metrics.eval(stock, first_y, first_qc)

    def __str__(self):
        if self._qc != 0:
            return 'Befor({}, past_quarter={})'.format(self._metrics, self._qc)
        if self._yc != 0:
            return 'Befor({}, past_year={})'.format(self._metrics, self._yc)
        return 'past_year and past_quarter can not be zero'
