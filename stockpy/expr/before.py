from stockpy.expr.base import Expr
from stockpy.expr.base import ExprCtx
from stockpy.expr.get import Get
import math


class Before(Expr):
    '''the value before past_quarter'''

    def __init__(self, metrics: Get, past_quarter: int):
        '''
        Args:
            metrics: Get expr
            past_quarter:  the count of the quarters before current
        '''
        self._metrics = metrics
        self._qc = past_quarter

    def eval(self, stock: ExprCtx, year: int, quarter: int):
        q = quarter-self._qc
        if q > 0:
            return self._metrics.eval(stock, year, q)
        else:
            qc = -q
            first_y = year - math.ceil((qc+1) / 4)
            first_qc = 4 - qc % 4
            return self._metrics.eval(stock, first_y, first_qc)
