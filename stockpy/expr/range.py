from stockpy.expr.base import Expr
from stockpy.expr.base import ExprCtx
from stockpy.expr.get import Get
import math


class Range(Expr):
    '''range metrics from current to past'''

    def __init__(self, metrics: Get, quarter_count: int):
        '''
        Args:
            metrics: Get expr
            quarter_count:  the count of the quarters in which get values
                            from current to past
        '''
        self._metrics = metrics
        self._qc = quarter_count

    def eval(self, stock: ExprCtx, year: int, quarter: int):
        vs = []
        for q in range(quarter, 0, -1):
            vs.append(self._metrics.eval(stock, year, q))

        qc = self._qc - quarter
        if qc > 0:
            last_year = year - 1
            first_y = last_year - (math.ceil(qc / 4) - 1)

            for y in range(last_year, first_y, -1):
                for q in range(4, 0, -1):
                    vs.append(self._metrics.eval(stock, y, q))

            first_qc = qc % 4
            if first_qc == 0:
                first_qc = 4
            for q in range(4, 4 - first_qc, -1):
                vs.append(self._metrics.eval(stock, first_y, q))

        return vs
