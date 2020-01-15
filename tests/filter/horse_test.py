import unittest
from stockpy.filter import horse
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
                },
                2016: {
                    4: 2
                }
            },
            'accounts_receiv': {
                2018: {
                    4: 1
                },
                2017: {
                    4: 1
                },
                2016: {
                    4: 1
                },
            },
            'inventories': {
                2018: {
                    4: 1
                },
                2017: {
                    4: 1
                },
                2016: {
                    4: 1
                }
            },
            'total_cur_assets': {
                2018: {
                    4: 2
                },
                2017: {
                    4: 2
                },
                2016: {
                    4: 2
                }
            },
            'total_cur_liab': {
                2018: {
                    4: 1
                },
                2017: {
                    4: 1
                },
                2016: {
                    4: 1
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
                },
                2016: {
                    4: 6,
                    3: 5
                },
                2015: {
                    4: 5
                },
                2014: {
                    4: 4
                },
                2013: {
                    4: 3
                },
                2012: {
                    4: 2
                },
                2011: {
                    4: 1
                },
                2010: {
                    4: 0.5
                }
            },
            'total_hldr_eqy_exc_min_int': {
                2016: {
                    3: 9
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
                },
                2010: {
                    4: 3
                },
                2009: {
                    4: 2
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

        # (2018.4 - 2017.4)/2017.4
        v = m.eval(self.stock, 2019, 2)
        self.assertEqual((8-4)/4, v)

    def test_last_quarter_f_income_attr_p_q_r_y2y(self):
        m = horse.last_quarter_f_income_attr_p_q_r_y2y()

        # (2019.2 - 2018.2)/2018.2
        v = m.eval(self.stock, 2019, 2)
        self.assertEqual((2-1)/1, v)

    def test_revenue_r_gt_0(self):
        m = horse.revenue_r_gt_0()
        v = m.eval(self.stock, 2019, 2)
        self.assertTrue(v)

    def test_income_attr_p_r_gt_0(self):
        m = horse.income_attr_p_r_gt_0()
        v = m.eval(self.stock, 2019, 2)
        self.assertTrue(v)

    def test_roe_ge_15_pct(self):
        m = horse.roe_ge_15_pct_last_7_year()
        v = m.eval(self.stock, 2016, 3)
        self.assertTrue(v)

    def test_revenue_y_gt_accounts_receive_3_years(self):
        m = horse.revenue_y_gt_accounts_receive_3_years()
        v = m.eval(self.stock, 2019, 2)
        self.assertTrue(v)

    def test_revenue_y_gt_inventoires_3_years(self):
        m = horse.revenue_y_gt_inventoires_3_years()
        v = m.eval(self.stock, 2019, 2)
        self.assertTrue(v)

    def test_current_y_gt_1_3_years(self):
        m = horse.current_y_gt_1_3_years()
        v = m.eval(self.stock, 2019, 2)
        self.assertTrue(v)
