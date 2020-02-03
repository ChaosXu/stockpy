import unittest
from stockpy.expr import ExprCtx, Get


class TestGet(unittest.TestCase):

    def test_cumulative(self):
        class StockStub(ExprCtx):

            def get_metrics(self, name: str, year: int, quarter: int):
                return 1

        stock = StockStub()

        get = Get('cumulative')
        v = get.eval(stock, 2019, 1)
        self.assertEqual(1, v)
        print(get, '\r\n')

    def test_increment_q1(self):
        class StockStub(ExprCtx):

            def get_metrics(self, name: str, year: int, quarter: int):
                if year == 2019 and quarter == 1:
                    return 3
                elif year == 2018 and quarter == 4:
                    return 1

        stock = StockStub()

        get = Get('increment', increment=True)
        v = get.eval(stock, 2019, 1)
        self.assertEqual(2, v)
        print(get, '\r\n')

    def test_increment_q4(self):
        class StockStub(ExprCtx):

            def get_metrics(self, name: str, year: int, quarter: int):
                if year == 2019 and quarter == 4:
                    return 3
                elif year == 2019 and quarter == 3:
                    return 1

        stock = StockStub()

        get = Get('increment', increment=True)
        v = get.eval(stock, 2019, 4)
        self.assertEqual(2, v)
        print(get, '\r\n')
