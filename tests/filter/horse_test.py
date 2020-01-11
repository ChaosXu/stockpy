import unittest
from stockpy.db.mock.driver import Driver
from stockpy.db.stock import StockDb
from stockpy.filter import horse
from stockpy import expr
from tests.filter import config


class HorseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        info_filter = expr.Eq(expr.Get('i_ts_code'), expr.Value('999999.TS'))
        cls.stock = StockDb(driver=Driver(**config.opts), **
                            config.opts).list().queryByInfo(info_filter)[0]

    def test_last_year_f_revenue_y_r_y2y(self):
        m = horse.last_year_f_revenue_y_r_y2y()
        # (2018.4'8' - 2017.4'4')/2017.4'4'
        v = m.eval(self.stock, 2019, 2)
        self.assertEqual((8-4)/4, v)

    def test_last_quarter_f_revenue_q_r_y2y(self):
        m = horse.last_quarter_f_revenue_q_r_y2y()

        # (2019.2 - 2018.2) / 2018.1
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
