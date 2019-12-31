import unittest
from tests import StockStub
from stockpy.metrics.finance import cash_flow


class CashFlowTest(unittest.TestCase):

    def test_f_income_attr_p_y2y(self):
        data = {
            2019: {
                1: 5,
                4: 8
            },
            2018: {
                1: 1,
                4: 4
            }
        }
        stock = StockStub(data)
        m = cash_flow.metrics()[0]

        # 2019.1 - 2018.1
        v = m.expr.eval(stock, 2019, 1)
        self.assertEqual(4, v)

        # 2019.4 - 2018.4
        v = m.expr.eval(stock, 2019, 4)
        self.assertEqual(4, v)

    def test_f_revenue_r_y2y(self):
        data = {
            2019: {
                1: 5,
                4: 8
            },
            2018: {
                1: 1,
                4: 4
            }
        }
        stock = StockStub(data)
        m = cash_flow.metrics()[1]

        # (2019.1 - 2018.1)/2018.1
        v = m.expr.eval(stock, 2019, 1)
        self.assertEqual((5-1)/1, v)

        # (2019.4 - 2018.4)/2018.4
        v = m.expr.eval(stock, 2019, 4)
        self.assertEqual((8-4)/4, v)
