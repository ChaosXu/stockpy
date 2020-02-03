from stockpy.expr.base import Expr
from stockpy.expr.base import ExprCtx
from stockpy.expr.get import Get
from stockpy.expr.base import trace
import math


class Range(Expr):
    '''range metrics from current to past'''

    def __init__(self, metrics: Get,
                 quarter_count: int = 0,
                 year_count: int = 0):
        '''
        Args:
            metrics: Get expr
            quarter_count:  the count of the quarters in which get values
                            from current to past
            year_count: the coun of the years in which get values
                        from current to past
        '''
        self._metrics = metrics
        self._qc = quarter_count
        self._yc = year_count
        if self._qc == 0 and self._yc == 0:
            raise Exception('quarer_count and year_count can not be zero')

    @trace
    def eval(self, stock: ExprCtx, year: int, quarter: int):
        if self._qc > 0:
            return self.__eval_qc(stock, year, quarter)

        return self.__eval_yc(stock, year, quarter)

    def __eval_qc(self, stock: ExprCtx, year: int, quarter: int):
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

    def __eval_yc(self, stock: ExprCtx, year: int, quarter: int):
        '''returns the values in the Q4 if range by year_count'''
        vs = []
        if quarter == 1:
            year -= 1
        for y in range(year, year-self._yc, -1):
            vs.append(self._metrics.eval(stock, y, 4))
        return vs

    def __str__(self):
        if self._qc > 0:
            return 'Range({},quarter_count={})'.format(self._metrics, self._qc)

        return 'Range({},year_count={})'.format(self._metrics, self._yc)
