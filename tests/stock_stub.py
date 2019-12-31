from stockpy.expr import ExprCtx


class StockStub(ExprCtx):

    def __init__(self, data):
        self.__data = data

    def get_metrics(self, name: str, year: int, quarter: int):
        return self.__data[year][quarter]
