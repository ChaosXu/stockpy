from stockpy.expr.base import Expr
from stockpy.expr.base import ExprCtx
import math


class ArithmeticExpr(Expr):

    def __init__(self, *opds: Expr):
        self._opds = opds

    def eval(self, stock: ExprCtx, year: int, quarter: int):
        v = None
        for opd in self._opds:
            if isinstance(opd, list):
                for opd2 in opd:
                    v = self._op(stock, year, quarter, opd2, v)
            else:
                v = self._op(stock, year, quarter, opd, v)
        return v

    def _op(self, stock: ExprCtx, year: int, quarter: int, opd: Expr, v):
        pass


class Sum(ArithmeticExpr):

    def __init__(self, *opds: Expr):
        super().__init__(*opds)

    def _op(self, stock: ExprCtx, year: int, quarter: int, opd: Expr, v):
        if v is None:
            return opd.eval(stock, year, quarter)

        return v + opd.eval(stock, year, quarter)


class Sub(ArithmeticExpr):

    def __init__(self, *opds: Expr):
        super().__init__(*opds)

    def _op(self, stock: ExprCtx, year: int, quarter: int, opd: Expr, v):
        if v is None:
            return opd.eval(stock, year, quarter)

        return v - opd.eval(stock, year, quarter)


class Multi(ArithmeticExpr):

    def __init__(self, *opds: Expr):
        super().__init__(*opds)

    def _op(self, stock: ExprCtx, year: int, quarter: int, opd: Expr, v):
        if v is None:
            return opd.eval(stock, year, quarter)

        return v * opd.eval(stock, year, quarter)


class Div(ArithmeticExpr):

    def __init__(self, *opds: Expr):
        super().__init__(*opds)

    def _op(self, stock: ExprCtx, year: int, quarter: int, opd: Expr, v):
        if v is None:
            return opd.eval(stock, year, quarter)

        return v / opd.eval(stock, year, quarter)


class Power(ArithmeticExpr):

    def __init__(self, *opds: Expr):
        super().__init__(*opds)

    def _op(self, stock: ExprCtx, year: int, quarter: int, opd: Expr, v):
        if v is None:
            return opd.eval(stock, year, quarter)

        return math.pow(v, opd.eval(stock, year, quarter))
