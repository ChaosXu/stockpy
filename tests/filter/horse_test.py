import unittest
from stockpy.db.mock.driver import Driver
from stockpy.db.stock import StockDb
from stockpy.filter import horse
from stockpy import expr
from tests.filter import config
from tests import StockMapStub


class HorseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        data = {
            'revenue': {
                2019: {
                    2: 2
                },
                2018: {
                    2: 1,
                    4: 8
                },
                2017: {
                    4: 4
                }
            },
            'n_income_attr_p': {
                2019: {
                    2: 2,
                    4: 3
                },
                2018: {
                    2: 1,
                    4: 8
                },
                2017: {
                    4: 4
                }
            },
            'total_hldr_eqy_exc_min_int': {
                2016: {
                    4: 9
                },
                2015: {
                    4: 8
                },
                2014: {
                    4: 7
                },
                2013: {
                    4: 6
                },
                2012: {
                    4: 5
                },
                2011: {
                    4: 4
                }
            }
        }
        cls.stock = StockMapStub(data)

    def test_last_year_f_revenue_y_r_y2y(self):
        m = horse.last_year_f_revenue_y_r_y2y()
        # (2018.4'8' - 2017.4'4')/2017.4'4'
        v = m.eval(self.stock, 2019, 2)
        self.assertEqual((8-4)/4, v)

    def test_last_quarter_f_revenue_q_r_y2y(self):
        m = horse.last_quarter_f_revenue_q_r_y2y()

        # (2019.2 - 2018.2) / 2018.2
        v = m.eval(self.stock, 2019, 2)
        self.assertEqual((2-1)/1, v)

    def test_last_year_f_income_attr_p_y_r_y2y(self):
        m = horse.last_year_f_income_attr_p_y_r_y2y()

        # (2018.8 - 2017.4)/2017.4
        v = m.eval(self.stock, 2019, 2)
        self.assertEqual((8-4)/4, v)

    def test_last_quarter_f_income_attr_p_q_r_y2y(self):
        m = horse.last_quarter_f_income_attr_p_q_r_y2y()

        # (2019.2 - 2018.2)/2018.2
        v = m.eval(self.stock, 2019, 2)
        self.assertEqual((2-1)/1, v)

    def test_revenue_gt_0(self):
        m = horse.revenue_gt_0()
        v = m.eval(self.stock, 2019, 2)
        self.assertTrue(v)

    def test_income_attr_p_gt_0(self):
        m = horse.income_attr_p_gt_0()
        v = m.eval(self.stock, 2019, 2)
        self.assertTrue(v)

    def test_roe_ge_15_pct(self):
        pass
