from model.meta import Expr
from model.meta import ExprCtx
from model.meta import Value


class ArithmeticExpr(Expr):

    def __init__(self, left: Expr, right: Expr):
        self.left = left
        self.right = right

    def eval(self, stock: ExprCtx, year: int, quarter: int):
        pass


class Sum(Expr):

    def __init__(self, *opds: Expr):
        self.opds = opds

    def eval(self, stock: ExprCtx, year: int, quarter: int):
        sum = 0
        for opd in self.opds:
            sum += opd.eval(stock, year, quarter)
        return sum


class Sub(ArithmeticExpr):

    def __init__(self, left: Expr, right: Expr):
        super().__init__(left, right)

    def eval(self, stock: ExprCtx, year: int, quarter: int):
        return self.left.eval(stock, year, quarter) - self.right.eval(stock, year, quarter)


class Multi(ArithmeticExpr):

    def __init__(self, left: Expr, right: Expr):
        super().__init__(left, right)

    def eval(self, stock: ExprCtx, year: int, quarter: int):
        return self.left.eval(stock, year, quarter) * self.right.eval(stock, year, quarter)


class Div(ArithmeticExpr):

    def __init__(self, left: Expr, right: Expr):
        super().__init__(left, right)

    def eval(self, stock: ExprCtx, year: int, quarter: int):
        return self.left.eval(stock, year, quarter) / self.right.eval(stock, year, quarter)
