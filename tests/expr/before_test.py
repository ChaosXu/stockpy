import unittest
from stockpy.expr import ExprCtx, Get, Before


class BeforeGet(unittest.TestCase):

    def test_past_q1_prev_year(self):
        class StockStub(ExprCtx):

            def get_metrics(self, name: str, year: int, quarter: int):
                d = {
                    2018: {4: 1}
                }
                return d[year][quarter]

        stock = StockStub()

        past = Before(Get('m'), 1)
        v = past.eval(stock, 2019, 1)
        self.assertEqual(1, v)

    def test_past_q3_current_year(self):
        class StockStub(ExprCtx):

            def get_metrics(self, name: str, year: int, quarter: int):
                d = {
                    2019: {1: 1}
                }
                return d[year][quarter]

        stock = StockStub()

        past = Before(Get('m'), 3)
        v = past.eval(stock, 2019, 4)
        self.assertEqual(1, v)

    def test_past_q4_prev_year(self):
        class StockStub(ExprCtx):

            def get_metrics(self, name: str, year: int, quarter: int):
                d = {
                    2018: {4: 1}
                }
                return d[year][quarter]

        stock = StockStub()

        past = Before(Get('m'), 4)
        v = past.eval(stock, 2019, 4)
        self.assertEqual(1, v)

    def test_past_5q_before_last(self):
        class StockStub(ExprCtx):

            def get_metrics(self, name: str, year: int, quarter: int):
                d = {
                    2017: {4: 1}
                }
                return d[year][quarter]

        stock = StockStub()

        past = Before(Get('m'), 5)
        v = past.eval(stock, 2019, 1)
        self.assertEqual(1, v)
