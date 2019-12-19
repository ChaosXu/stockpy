from model.meta import Expr
from model.meta import ExprCtx


class Get(Expr):
    """Get a metrics value  from the statements in the local stock cache"""

    def __init__(self, name: str, past_year=0):
        """
        Args:
            name: metrics name
            past_year: metrcs value before the past n year. 
        """
        self._name = name
        self._past_year = past_year

    def eval(self, stock: ExprCtx, year: int, quarter: int):
        return stock.get_metrics(self._name, year-self._past_year, quarter)
