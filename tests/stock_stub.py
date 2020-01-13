from stockpy.expr import ExprCtx
from stockpy.metrics import g_metrics


class StockStub(ExprCtx):

    def __init__(self, data):
        self.__data = data

    def get_metrics(self, name: str, year: int, quarter: int):
        return self.__data[year][quarter]


class StockMapStub(ExprCtx):

    def __init__(self, data: dict):
        self.__data = data

    def get_metrics(self, name: str, year: int, quarter: int):
        if name in self.__data is not None:
            try:
                return self.__data[name][year][quarter]
            except Exception as e:
                raise Exception('get_metrics failed. name={},year={},quarter={}\r\n inner_err:={}'.format(
                    name, year, quarter, e))
        else:
            return g_metrics[name].expr.eval(self, year, quarter)
