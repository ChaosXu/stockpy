import unittest
from tests import StockStub
from stockpy.metrics.finance import income


class IncomeTest(unittest.TestCase):

    def test_f_revenue_q_y2y(self):
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
        m = income.metrics()[0]

        # 2019.1 - 2018.1
        v = m.expr.eval(stock, 2019, 1)
        self.assertEqual(4, v)

        # 2019.4 - 2018.4
        v = m.expr.eval(stock, 2019, 4)
        self.assertEqual(4, v)

    def test_f_revenue_q_r_y2y(self):
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
        m = income.metrics()[1]

        # (2019.1 - 2018.1)/2018.1
        v = m.expr.eval(stock, 2019, 1)
        self.assertEqual((5-1)/1, v)

        # (2019.4 - 2018.4)/2018.4
        v = m.expr.eval(stock, 2019, 4)
        self.assertEqual((8-4)/4, v)

    def test_f_revenue_y_y2y(self):
        data = {
            2019: {
                4: 8
            },
            2018: {
                4: 4
            }
        }
        stock = StockStub(data)
        m = income.metrics()[2]

        # 2019.4 - 2018.4
        v = m.expr.eval(stock, 2019, 4)
        self.assertEqual(4, v)

    def test_f_revenue_y_r_y2y(self):
        data = {
            2019: {
                4: 8
            },
            2018: {
                4: 4
            }
        }
        stock = StockStub(data)
        m = income.metrics()[3]

        # (2019.4 - 2018.4)/2018.4
        v = m.expr.eval(stock, 2019, 4)
        self.assertEqual((8-4)/4, v)

    def test_f_income_attr_p_q_y2y(self):
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
        m = income.metrics()[4]

        # 2019.1 - 2018.1
        v = m.expr.eval(stock, 2019, 1)
        self.assertEqual(4, v)

        # 2019.4 - 2018.4
        v = m.expr.eval(stock, 2019, 4)
        self.assertEqual(4, v)

    def test_f_income_attr_p_q_r_y2y(self):
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
        m = income.metrics()[5]

        # (2019.1 - 2018.1)/2018.1
        v = m.expr.eval(stock, 2019, 1)
        self.assertEqual((5-1)/1, v)

        # (2019.4 - 2018.4)/2018.4
        v = m.expr.eval(stock, 2019, 4)
        self.assertEqual((8-4)/4, v)

    def test_f_income_attr_p_y_y2y(self):
        data = {
            2019: {
                4: 8
            },
            2018: {
                4: 4
            }
        }
        stock = StockStub(data)
        m = income.metrics()[6]

        # 2019.4 - 2018.4
        v = m.expr.eval(stock, 2019, 4)
        self.assertEqual(4, v)

    def test_f_income_attr_p_y_r_y2y(self):
        data = {
            2019: {
                4: 8
            },
            2018: {
                4: 4
            }
        }
        stock = StockStub(data)
        m = income.metrics()[7]

        # (2019.4 - 2018.4)/2018.4
        v = m.expr.eval(stock, 2019, 4)
        self.assertEqual((8-4)/4, v)
