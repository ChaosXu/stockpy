from stockpy.expr.base import Expr
from stockpy.expr.base import ExprCtx
from stockpy.expr.base import trace


class BooleanExpr(Expr):

    def __init__(self, left: Expr, right: Expr):
        self._left = left
        self._right = right

    @trace
    def eval(self, stock: ExprCtx, year: int, quarter: int):
        lv = self._left.eval(stock, year, quarter)
        rv = self._right.eval(stock, year, quarter)

        if isinstance(lv, list):
            return self._eval_list_v(lv, rv)
        elif isinstance(rv, list):
            return self._eval_v_list(lv, rv)
        else:
            return self._eval_v(lv, rv)
        raise Exception('bad lv or rv,lv={},rv={}'.format(lv, rv))

    def _eval_v(self, lv, rv):
        raise Exception('abstract method to be implemented')

    def _eval_list_v(self, ls, v):
        for lv in ls:
            r = self._eval_v(lv, v)
            if not r:
                return False
        return True

    def _eval_v_list(self, v, ls):
        for rv in ls:
            if not self._eval_v(v, rv):
                return False
        return True

    def __str__(self):
        return '({} {} {})'.format(self._left, self._str_op(), self._right)

    def _str_op(self):
        return 'op'


class Lt(BooleanExpr):

    def __init__(self, left: Expr, right: Expr):
        super().__init__(left, right)

    def _eval_v(self, lv, rv):
        return lv < rv

    def _str_op(self):
        return '<'


class Le(BooleanExpr):

    def __init__(self, left: Expr, right: Expr):
        super().__init__(left, right)

    def _eval_v(self, lv, rv):
        return lv <= rv

    def _str_op(self):
        return '<='


class Eq(BooleanExpr):

    def __init__(self, left: Expr, right: Expr):
        super().__init__(left, right)

    def _eval_v(self, lv, rv):
        return lv == rv

    def _str_op(self):
        return '=='


class Ne(BooleanExpr):

    def __init__(self, left: Expr, right: Expr):
        super().__init__(left, right)

    def _eval_v(self, lv, rv):
        return lv != rv

    def _str_op(self):
        return '!='


class Gt(BooleanExpr):

    def __init__(self, left: Expr, right: Expr):
        super().__init__(left, right)

    def _eval_v(self, lv, rv):
        return lv > rv

    def _str_op(self):
        return '>'


class Ge(BooleanExpr):

    def __init__(self, left: Expr, right: Expr):
        super().__init__(left, right)

    def _eval_v(self, lv, rv):
        return lv >= rv

    def _str_op(self):
        return '>='


class And(BooleanExpr):

    def __init__(self, *opds: BooleanExpr):
        self.__opds = opds

    @trace
    def eval(self, stock: ExprCtx, year: int, quarter: int):
        for opd in self.__opds:
            if isinstance(opd, list):
                for opd2 in opd:
                    if not opd2.eval(stock, year, quarter):
                        return False
            elif not opd.eval(stock, year, quarter):
                return False

        return True

    def __str__(self):
        ss = []
        for opd in self.__opds:
            if isinstance(opd, list):
                for opd2 in opd:
                    ss.append('{}'.format(opd2))
            else:
                ss.append('{}'.format(opd))
        return 'And({})'.format(' '.join(ss))


class Or(BooleanExpr):

    def __init__(self, *opds: BooleanExpr):
        self.__opds = opds

    @trace
    def eval(self, stock: ExprCtx, year: int, quarter: int):
        for opd in self.__opds:
            if isinstance(opd, list):
                for opd2 in opd:
                    if opd2.eval(stock, year, quarter) is True:
                        return True
            elif opd.eval(stock, year, quarter) is True:
                return True

        return False

    def __str__(self):
        ss = []
        for opd in self.__opds:
            if isinstance(opd, list):
                for opd2 in opd:
                    ss.append('{}'.format(opd2))
            else:
                ss.append('{}'.format(opd))
        return 'Or({})'.format(' '.join(ss))
