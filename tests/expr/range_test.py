import unittest
from stockpy.expr import ExprCtx, Range, Get


class TestRange(unittest.TestCase):

    def test_q1(self):
        class StockStub(ExprCtx):

            def get_metrics(self, name: str, year: int, quarter: int):
                if year == 2019 and quarter == 1:
                    return 1

        stock = StockStub()

        rg = Range(Get('m'), quarter_count=1)
        v = rg.eval(stock, 2019, 1)
        self.assertEqual(1, len(v))
        self.assertEqual(1, v[0])
        print(rg, '\r\n')

    def test_q2(self):
        class StockStub(ExprCtx):
            d = {
                2019: {1: 1, 2: 2}
            }

            def get_metrics(self, name: str, year: int, quarter: int):
                return self.d[year][quarter]

        stock = StockStub()

        rg = Range(Get('m'), quarter_count=2)
        v = rg.eval(stock, 2019, 2)
        self.assertEqual(2, len(v))
        self.assertEqual(2, v[0])
        self.assertEqual(1, v[1])

    def test_q4(self):
        class StockStub(ExprCtx):
            d = {
                2019: {1: 1, 2: 2, 3: 3, 4: 4}
            }

            def get_metrics(self, name: str, year: int, quarter: int):
                return self.d[year][quarter]

        stock = StockStub()

        rg = Range(Get('m'), quarter_count=4)
        v = rg.eval(stock, 2019, 4)
        self.assertEqual(4, len(v))
        self.assertEqual(4, v[0])
        self.assertEqual(3, v[1])
        self.assertEqual(2, v[2])
        self.assertEqual(1, v[3])

    def test_q8(self):
        class StockStub(ExprCtx):
            d = {
                2018: {1: -1, 2: -2, 3: -3, 4: -4},
                2019: {1: 1, 2: 2, 3: 3, 4: 4}
            }

            def get_metrics(self, name: str, year: int, quarter: int):
                return self.d[year][quarter]

        stock = StockStub()

        rg = Range(Get('m'), quarter_count=8)
        v = rg.eval(stock, 2019, 4)
        self.assertEqual(8, len(v))
        self.assertEqual(4, v[0])
        self.assertEqual(3, v[1])
        self.assertEqual(2, v[2])
        self.assertEqual(1, v[3])
        self.assertEqual(-4, v[4])
        self.assertEqual(-3, v[5])
        self.assertEqual(-2, v[6])
        self.assertEqual(-1, v[7])

    def test_q5(self):
        class StockStub(ExprCtx):
            d = {
                2018: {4: -4},
                2019: {1: 1, 2: 2, 3: 3, 4: 4}
            }

            def get_metrics(self, name: str, year: int, quarter: int):
                return self.d[year][quarter]

        stock = StockStub()

        rg = Range(Get('m'), quarter_count=5)
        v = rg.eval(stock, 2019, 4)
        self.assertEqual(5, len(v))
        self.assertEqual(4, v[0])
        self.assertEqual(3, v[1])
        self.assertEqual(2, v[2])
        self.assertEqual(1, v[3])
        self.assertEqual(-4, v[4])

    def test_q10(self):
        class StockStub(ExprCtx):
            d = {
                2016: {4: -5},
                2017: {1: -1, 2: -2, 3: -3, 4: -4},
                2018: {1: -1, 2: -2, 3: -3, 4: -4},
                2019: {1: 1}
            }

            def get_metrics(self, name: str, year: int, quarter: int):
                return self.d[year][quarter]

        stock = StockStub()

        rg = Range(Get('m'), quarter_count=10)
        v = rg.eval(stock, 2019, 1)
        self.assertEqual(10, len(v))
        self.assertEqual(1, v[0])
        self.assertEqual(-4, v[1])
        self.assertEqual(-3, v[2])
        self.assertEqual(-2, v[3])
        self.assertEqual(-1, v[4])
        self.assertEqual(-4, v[5])
        self.assertEqual(-3, v[6])
        self.assertEqual(-2, v[7])
        self.assertEqual(-1, v[8])
        self.assertEqual(-5, v[9])

    def test_q6(self):
        class StockStub(ExprCtx):
            d = {
                2017: {4: -4},
                2018: {1: -1, 2: -2, 3: -3, 4: -4},
                2019: {1: 1}
            }

            def get_metrics(self, name: str, year: int, quarter: int):
                return self.d[year][quarter]

        stock = StockStub()

        rg = Range(Get('m'), quarter_count=6)
        v = rg.eval(stock, 2019, 1)
        self.assertEqual(6, len(v))
        self.assertEqual(1, v[0])
        self.assertEqual(-4, v[1])
        self.assertEqual(-3, v[2])
        self.assertEqual(-2, v[3])
        self.assertEqual(-1, v[4])
        self.assertEqual(-4, v[5])
