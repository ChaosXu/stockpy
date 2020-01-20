from stockpy.expr.base import Expr
from stockpy.expr.base import ExprCtx


class Switch(Expr):

    def __init__(self, *cases: Expr, default=None):
        self._cases = cases
        self._default = default

    def eval(self, stock: ExprCtx, year: int, quarter: int):
        for case in self._cases:
            v = case.eval(stock, year, quarter)
            if v is not None:
                return v

        if self._default is None:
            return None
        return self._default.eval(stock, year, quarter)


class Case(Expr):

    def __init__(self, condition: Expr, v: Expr):
        self._condition = condition
        self._v = v

    def eval(self, stock: ExprCtx, year: int, quarter: int):
        if self._condition.eval(stock, year, quarter):
            return self._v.eval(stock, year, quarter)

        return None
