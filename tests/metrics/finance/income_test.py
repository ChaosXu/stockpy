import unittest
from tests import StockStub, StockMapStub
from stockpy.metrics.finance import income
from stockpy.expr import Get


class IncomeTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = {
            'revenue': {
                2019: {
                    1: 10,
                    4: 20
                },
                2018: {
                    1: 6,
                    2: 7,
                    3: 8,
                    4: 10
                },
                2017: {
                    4: 5
                }
            },
            'n_income_attr_p': {
                2019: {
                    1: 5,
                    4: 10
                },
                2018: {
                    1: 3,
                    2: 4,
                    3: 4.5,
                    4: 5
                },
                2017: {
                    4: 5
                }
            }
        }
        cls.stock = StockMapStub(cls.data)

    def test_f_revenue_q_y2y(self):
        m = income.revenue_q_y2y()

        # 2019.1 - 2018.1
        v = m.expr.eval(self.stock, 2019, 1)
        self.assertEqual(4, v)

        # 2019.4 - 2018.4
        v = m.expr.eval(self.stock, 2019, 4)
        self.assertEqual(10, v)

    def test_f_revenue_q_r_y2y(self):
        m = income.revenue_q_r_y2y()

        # (2019.1 - 2018.1)/2018.1
        v = m.expr.eval(self.stock, 2019, 1)
        s1 = Get('revenue').eval(self.stock, 2019, 1)
        s2 = Get('revenue').eval(self.stock, 2018, 1)
        self.assertEqual((s1-s2)/s2, v)

        # (2019.4 - 2018.4)/2018.4
        v = m.expr.eval(self.stock, 2019, 4)
        self.assertEqual((8-4)/4, v)

    def test_f_revenue_y_y2y(self):
        m = income.revenue_y_y2y()

        # 2019.4 - 2018.4
        v = m.expr.eval(self.stock, 2019, 4)
        self.assertEqual(10, v)

    def test_f_revenue_y_r_y2y(self):
        m = income.revenue_y_r_y2y()

        # (2019.4 - 2018.4)/2018.4
        v = m.expr.eval(self.stock, 2019, 4)
        self.assertEqual((8-4)/4, v)

    def test_f_income_attr_p_q_y2y(self):
        m = income.income_attr_p_q_y2y()

        # 2019.1 - 2018.1
        v = m.expr.eval(self.stock, 2019, 1)
        s1 = Get('n_income_attr_p').eval(self.stock, 2019, 1)
        s2 = Get('n_income_attr_p').eval(self.stock, 2018, 1)
        self.assertEqual(s1-s2, v)

        # 2019.4 - 2018.4
        v = m.expr.eval(self.stock, 2019, 4)
        s1 = Get('n_income_attr_p').eval(self.stock, 2019, 4)
        s2 = Get('n_income_attr_p').eval(self.stock, 2018, 4)
        self.assertEqual(s1-s2, v)

    def test_f_income_attr_p_q_r_y2y(self):
        m = income.income_attr_p_q_r_y2y()

        # (2019.1 - 2018.1)/2018.1
        v = m.expr.eval(self.stock, 2019, 1)
        s1 = Get('n_income_attr_p').eval(self.stock, 2019, 1)
        s2 = Get('n_income_attr_p').eval(self.stock, 2018, 1)
        self.assertEqual((s1-s2)/s2, v)

        # (2019.4 - 2018.4)/2018.4
        v = m.expr.eval(self.stock, 2019, 4)
        s1 = Get('n_income_attr_p').eval(self.stock, 2019, 4)
        s2 = Get('n_income_attr_p').eval(self.stock, 2018, 4)
        self.assertEqual((s1-s2)/s2, v)

    def test_f_income_attr_p_y_y2y(self):
        m = income.income_attr_p_y_y2y()

        # 2019.1 - 2018.1
        v = m.expr.eval(self.stock, 2019, 1)
        s1 = Get('n_income_attr_p').eval(self.stock, 2018, 4)
        s2 = Get('n_income_attr_p').eval(self.stock, 2017, 4)
        self.assertEqual(s1-s2, v)

        # 2019.4 - 2018.4
        v = m.expr.eval(self.stock, 2019, 4)
        s1 = Get('n_income_attr_p').eval(self.stock, 2019, 4)
        s2 = Get('n_income_attr_p').eval(self.stock, 2018, 4)
        self.assertEqual(s1-s2, v)

    def test_f_income_attr_p_y_r_y2y(self):
        m = income.income_attr_p_y_r_y2y()

        # (2019.1 - 2018.1)/2018.1
        v = m.expr.eval(self.stock, 2019, 1)
        s1 = Get('n_income_attr_p').eval(self.stock, 2018, 4)
        s2 = Get('n_income_attr_p').eval(self.stock, 2017, 4)
        self.assertEqual((s1-s2)/s2, v)

        # (2019.4 - 2018.4)/2018.4
        v = m.expr.eval(self.stock, 2019, 4)
        s1 = Get('n_income_attr_p').eval(self.stock, 2019, 4)
        s2 = Get('n_income_attr_p').eval(self.stock, 2018, 4)
        self.assertEqual((s1-s2)/s2, v)

    def test_income_attr_p_ttm(self):
        m = income.income_attr_p_ttm()

        # (2019.1 - 2018.1)/2018.1
        v = m.expr.eval(self.stock, 2019, 1)
        s1 = Get('n_income_attr_p',
                 increment=True,
                 var_type='f').eval(self.stock, 2019, 1)
        s2 = Get('n_income_attr_p',
                 increment=True,
                 var_type='f').eval(self.stock, 2018, 4)
        s3 = Get('n_income_attr_p',
                 increment=True,
                 var_type='f').eval(self.stock, 2018, 3)
        s4 = Get('n_income_attr_p',
                 increment=True,
                 var_type='f').eval(self.stock, 2018, 2)
        self.assertEqual(s1+s2+s3+s4, v)
