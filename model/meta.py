from util.singleton import SingletonMeta


class ExprCtx:

    def get_metrics(self, name: str, year: int, quarter: int):
        """get metrics value
        Args:
            name: metrics name
            year: report year
            quarter: report quarter.from 1 to 4
        Returns:
            metrics value
        """
        pass


class Expr:

    def eval(self, stock: ExprCtx, year: int, quarter: int):
        pass


class Value(Expr):

    def __init__(self, v):
        self._v = v

    def eval(self, stock: ExprCtx, year: int, quarter: int):
        return self._v


class MetricsMeta:

    def __init__(self, name: str, expr):
        self._name = name
        self._expr = expr

    def get_name(self):
        return self._name

    def get_expr(self):
        return self._expr


class StockMeta(metaclass=SingletonMeta):

    def __init__(self):
        self._metrics = {}

    def addmetrics(self, meta: MetricsMeta):
        self._metrics[meta.get_name()] = meta

    def allmetrics(self):
        return self._metrics

    def getmetrics(self, name: str) -> MetricsMeta:
        return self._metrics[name]
