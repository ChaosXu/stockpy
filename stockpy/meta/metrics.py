from stockpy.expr.base import Expr


class MetricsMeta:

    def __init__(self, name: str, expr: Expr):
        self._name = name
        self._expr = expr

    def get_name(self):
        return self._name

    def get_expr(self):
        return self._expr
