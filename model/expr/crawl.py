from model.meta import Expr
from model.meta import Value

class Crawl(Expr):
    """Crawl the metrics from the outer source"""

    def __init__(self, name: str):
        """
        Args:
            name: the name of the metrics to be crawled
        """
        self.name = name

    def eval(self, stock, year: int, period: int):
        return 10
        # raise NotImplementedError("TBD")
