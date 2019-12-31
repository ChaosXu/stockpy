from stockpy.expr.base import Expr
from stockpy.expr.base import ExprCtx


class BooleanExpr(Expr):

    def __init__(self, left: Expr, right: Expr):
        self._left = left
        self._right = right


class Lt(BooleanExpr):

    def __init__(self, left: Expr, right: Expr):
        super().__init__(left, right)

    def eval(self, stock: ExprCtx, year: int, quarter: int):
        lv = self._left.eval(stock, year, quarter)
        rv = self._right.eval(stock, year, quarter)
        return lv < rv


class Le(BooleanExpr):

    def __init__(self, left: Expr, right: Expr):
        super().__init__(left, right)

    def eval(self, stock: ExprCtx, year: int, quarter: int):
        lv = self._left.eval(stock, year, quarter)
        rv = self._right.eval(stock, year, quarter)
        return lv <= rv


class Eq(BooleanExpr):

    def __init__(self, left: Expr, right: Expr):
        super().__init__(left, right)

    def eval(self, stock: ExprCtx, year: int, quarter: int):
        lv = self._left.eval(stock, year, quarter)
        rv = self._right.eval(stock, year, quarter)
        return lv == rv


class Ne(BooleanExpr):

    def __init__(self, left: Expr, right: Expr):
        super().__init__(left, right)

    def eval(self, stock: ExprCtx, year: int, quarter: int):
        lv = self._left.eval(stock, year, quarter)
        rv = self._right.eval(stock, year, quarter)
        return lv != rv


class Gt(BooleanExpr):

    def __init__(self, left: Expr, right: Expr):
        super().__init__(left, right)

    def eval(self, stock: ExprCtx, year: int, quarter: int):
        lv = self._left.eval(stock, year, quarter)
        rv = self._right.eval(stock, year, quarter)
        return lv > rv


class Ge(BooleanExpr):

    def __init__(self, left: Expr, right: Expr):
        super().__init__(left, right)

    def eval(self, stock: ExprCtx, year: int, quarter: int):
        lv = self._left.eval(stock, year, quarter)
        rv = self._right.eval(stock, year, quarter)
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
