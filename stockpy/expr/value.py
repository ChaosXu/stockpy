from stockpy.expr.base import Expr
from stockpy.expr.base import ExprCtx
from stockpy.expr.base import trace


class Value(Expr):

    def __init__(self, v):
        self._v = v

    @trace
    def eval(self, stock: ExprCtx, year: int, quarter: int):
        return self._v

    def __str__(self):
        return 'Value({})'.format(self._v)


class FuncValue(Expr):

    def __init__(self, func):
        self.__func = func

    @trace
    def eval(self, stock: ExprCtx, year: int, quarter: int):
        return self.__func(stock, year, quarter)

    def __str__(self):
        return 'FuncValue({})'.format(self.__func.__name__)
