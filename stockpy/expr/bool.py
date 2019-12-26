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

    def __init__(self, left: BooleanExpr, right: BooleanExpr):
        super().__init__(left, right)

    def eval(self, stock: ExprCtx, year: int, quarter: int):
        lv = self._left.eval(stock, year, quarter)
        rv = self._right.eval(stock, year, quarter)
        return lv and rv


class Or(BooleanExpr):

    def __init__(self, left: BooleanExpr, right: BooleanExpr):
        super().__init__(left, right)

    def eval(self, stock: ExprCtx, year: int, quarter: int):
        lv = self._left.eval(stock, year, quarter)
        rv = self._right.eval(stock, year, quarter)
        return lv or rv
