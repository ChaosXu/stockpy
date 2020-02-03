from stockpy.expr import ExprCtx
from stockpy.expr import Expr, Name


g_metrics = {}


class MetricsMeta:

    def __init__(self, name: str, expr: Expr):
        self._name = name
        self._expr = Name(f'm:{name}', expr)

    @property
    def name(self):
        return self._name

    @property
    def expr(self):
        return self._expr


class MetricsMetas:
    pass


class MetricsMixin:

    def __init__(self):
        self.__metrics = {}

    def eval(self, stock: ExprCtx, name: str, year: int, quarter: int):
        return self.__metrics[name].expr.eval(stock, year, quarter)

    def load_metrics(self, industry: str):
        # TBD
        self.__metrics = g_metrics
