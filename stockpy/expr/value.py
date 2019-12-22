from stockpy.expr.base import Expr
from stockpy.expr.base import ExprCtx


class Value(Expr):

    def __init__(self, v):
        self._v = v

    def eval(self, stock: ExprCtx, year: int, quarter: int):
        return self._v
