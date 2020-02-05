from stockpy.expr.base import Expr
from stockpy.expr.base import ExprCtx
from stockpy.expr.base import trace
import math


class ArithmeticExpr(Expr):

    def __init__(self, *opds: Expr):
        self._opds = opds

    @trace
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

    def __str__(self):
        ss = []
        for opd in self._opds:
            ss.append('{}'.format(opd))
        return '{}({})'.format(self._str_op(), ' '.join(ss))


class Sum(ArithmeticExpr):

    def __init__(self, *opds: Expr):
        super().__init__(*opds)

    def _op(self, stock: ExprCtx, year: int, quarter: int, opd: Expr, v):
        if v is None:
            return opd.eval(stock, year, quarter)

        return v + opd.eval(stock, year, quarter)

    def _str_op(self):
        return '+'


class Sub(ArithmeticExpr):

    def __init__(self, *opds: Expr):
        super().__init__(*opds)

    def _op(self, stock: ExprCtx, year: int, quarter: int, opd: Expr, v):
        if v is None:
            return opd.eval(stock, year, quarter)

        return v - opd.eval(stock, year, quarter)

    def _str_op(self):
        return '-'


class Multi(ArithmeticExpr):

    def __init__(self, *opds: Expr):
        super().__init__(*opds)

    def _op(self, stock: ExprCtx, year: int, quarter: int, opd: Expr, v):
        if v is None:
            return opd.eval(stock, year, quarter)

        return v * opd.eval(stock, year, quarter)

    def _str_op(self):
        return '*'


class Div(ArithmeticExpr):

    def __init__(self, *opds: Expr):
        super().__init__(*opds)

    def _op(self, stock: ExprCtx, year: int, quarter: int, opd: Expr, v):
        if v is None:
            return opd.eval(stock, year, quarter)

        v = v / opd.eval(stock, year, quarter)
        v.set_data(round(v.data, 2))
        return v

    def _str_op(self):
        return '/'


class Power(ArithmeticExpr):

    def __init__(self, *opds: Expr):
        super().__init__(*opds)

    def _op(self, stock: ExprCtx, year: int, quarter: int, opd: Expr, v):
        if v is None:
            return opd.eval(stock, year, quarter)

        return math.pow(v, opd.eval(stock, year, quarter))

    def _str_op(self):
        return '^'
