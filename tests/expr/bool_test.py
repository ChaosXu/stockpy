import unittest
from stockpy import expr
from tests.stock_stub import StockMapStub


class BoolTest(unittest.TestCase):

    def test_ge(self):
        f = expr.Ge(expr.Value(10), expr.Value(2))
        v = f.eval(None, None, None)
        self.assertEqual(True, v)

        f = expr.Ge(expr.Value(1), expr.Value(2))
        v = f.eval(None, None, None)
        self.assertEqual(False, v)

        print(f, '\r\n')

    def test_ge_range(self):
        data = {
            'revenue': {
                2019: {
                    4: 2
                },
                2018: {
                    4: 1
                },
                2017: {
                    4: 4
                },
                2016: {
                    4: 0.1
                },
            }
        }
        stock = StockMapStub(data)
        f = expr.Ge(
            expr.Range(expr.Before(expr.Get('revenue'), past_year=1),
                       year_count=1),
            expr.Value(0.15)
        )
        v = f.eval(stock, 2019, 4)
        self.assertEqual(True, v)

        print(f, '\r\n')
