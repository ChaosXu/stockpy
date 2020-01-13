from stockpy.expr.base import Expr
from stockpy.expr.base import ExprCtx


class BooleanExpr(Expr):

    def __init__(self, left: Expr, right: Expr):
        self._left = left
        self._right = right

    def eval(self, stock: ExprCtx, year: int, quarter: int):
        lv = self._left.eval(stock, year, quarter)
        rv = self._right.eval(stock, year, quarter)
        if isinstance(lv, list):
            self._eval_list_v(lv, rv)
        if isinstance(rv, list):
            self._eval_v_list(lv, rv)
        return self._eval_v(lv, rv)

    def _eval_v(self, lv, rv):
        pass

    def _eval_list_v(self, ls, v):
        for lv in ls:
            if self._eval_v(lv, v) is False:
                return False
        return True

    def _eval_v_list(self, v, ls):
        for rv in ls:
            if self._eval_v(v, rv) is False:
                return False
        return True


class Lt(BooleanExpr):

    def __init__(self, left: Expr, right: Expr):
        super().__init__(left, right)

    def _eval_v(self, lv, rv):
        return lv < rv


class Le(BooleanExpr):

    def __init__(self, left: Expr, right: Expr):
        super().__init__(left, right)

    def _eval_v(self, lv, rv):
        return lv <= rv


class Eq(BooleanExpr):

    def __init__(self, left: Expr, right: Expr):
        super().__init__(left, right)

    def _eval_v(self, lv, rv):
        return lv == rv


class Ne(BooleanExpr):

    def __init__(self, left: Expr, right: Expr):
        super().__init__(left, right)

    def _eval_v(self, lv, rv):
        return lv != rv


class Gt(BooleanExpr):

    def __init__(self, left: Expr, right: Expr):
        super().__init__(left, right)

    def _eval_v(self, lv, rv):
        return lv > rv


class Ge(BooleanExpr):

    def __init__(self, left: Expr, right: Expr):
        super().__init__(left, right)

    def _eval_v(self, lv, rv):
        return lv >= rv


class And(BooleanExpr):

    def __init__(self, *opds: BooleanExpr):
        self.__opds = opds

    def eval(self, stock: ExprCtx, year: int, quarter: int):
        for opd in self.__opds:
            if opd.eval(stock, year, quarter) is False:
                return False

        return True


class Or(BooleanExpr):

    def __init__(self, *opds: BooleanExpr):
        self.__opds = opds

    def eval(self, stock: ExprCtx, year: int, quarter: int):
        for opd in self.__opds:
            if opd.eval(stock, year, quarter) is True:
                return True

        return False
