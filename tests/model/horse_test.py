import unittest
from tests import StockStub
from stockpy.model import horse


class HorseTest(unittest.TestCase):

    def test_last_year_f_revenuen_y_r_y2y(self):
        data = {
            2018: {
                1: 5,
                2: 6,
                3: 7,
                4: 8
            },
            2017: {
                1: 1,
                2: 2,
                3: 3,
                4: 4
            },
        }
        stock = StockStub(data)
        m = horse.last_year_f_revenuen_y_r_y2y()

        # (2018.8 - 2017.4)/4
        v = m.eval(stock, 2019, 2)
        self.assertEqual((8-4)/4, v)

    # def test_last_quarter_f_revenuen_q_r_y2y(self):
    #     data = {
    #         2019: {
    #             2: 6
    #         },
    #         2018: {
    #             2: 2
    #         },
    #     }
    #     stock = StockStub(data)
    #     m = horse.last_quarter_f_income_attr_p_q_r_y2y()

    #     # 2019.2 - 2018.2
    #     v = m.eval(stock, 2019, 2)
    #     self.assertEqual(6-4, v)

    # def test_last_year_f_income_attr_p_y_r_y2y(self):
    #     data = {
    #         2018: {
    #             1: 5,
    #             2: 6,
    #             3: 7,
    #             4: 8
    #         },
    #         2017: {
    #             1: 1,
    #             2: 2,
    #             3: 3,
    #             4: 4
    #         },
    #     }
    #     stock = StockStub(data)
    #     m = horse.last_year_f_income_attr_p_y_r_y2y()

    #     # (2018.8 - 2017.4)/4
    #     v = m.eval(stock, 2019, 2)
    #     self.assertEqual((8-4)/4, v)

    # def test_last_quarter_f_income_attr_p_q_r_y2y(self):
    #     data = {
    #         2019: {
    #             2: 6
    #         },
    #         2018: {
    #             2: 2
    #         },
    #     }
    #     stock = StockStub(data)
    #     m = horse.last_quarter_f_income_attr_p_q_r_y2y()

    #     # 2019.2 - 2018.2
    #     v = m.eval(stock, 2019, 2)
    #     self.assertEqual(6-4, v)
