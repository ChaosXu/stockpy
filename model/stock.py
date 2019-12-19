from model.meta import MetricsMeta
from model.meta import StockMeta
from model.meta import ExprCtx
from model import metrics


class Stock(ExprCtx):

    def __init__(self, code: str, meta: StockMeta):
        self._code = code
        self._meta = meta

    def get_meta(self) -> StockMeta:
        return self._meta

    def get_metrics(self, name: str, year: int, quarter: int):
        """get metrics value
        Args:
            name: metrics name
            year: report year
            quarter: report quarter.from 1 to 4
        Returns:
            metrics value
        """
        return self.get_meta().get_Metrics(name).get_expr().eval(self, year, quarter)
