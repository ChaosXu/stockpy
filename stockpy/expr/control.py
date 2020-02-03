from stockpy.expr.base import Expr
from stockpy.expr.base import ExprCtx
from stockpy.expr.base import trace


class Switch(Expr):

    def __init__(self, *cases: Expr, default=None):
        self._cases = cases
        self._default = default

    @trace
    def eval(self, stock: ExprCtx, year: int, quarter: int):
        for case in self._cases:
            v = case.eval(stock, year, quarter)
            if v is not None:
                return v

        if self._default is None:
            return None
        return self._default.eval(stock, year, quarter)

    def __str__(self):
        cs = []
        for case in self._cases:
            cs.append('{}'.case.format(case))

        if self._default is not None:
            ds = '{}'.format(self._default)
        return 'Switch({}, default({}))'.format(', '.join(cs), ds)


class Case(Expr):

    def __init__(self, condition: Expr, v: Expr):
        self._condition = condition
        self._v = v

    def eval(self, stock: ExprCtx, year: int, quarter: int):
        if self._condition.eval(stock, year, quarter):
            return self._v.eval(stock, year, quarter)

        return None

    def __str__(self):
        return 'Case({}:{})'.format(self._condition, self._v)
