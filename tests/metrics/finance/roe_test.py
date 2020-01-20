import unittest
from tests import StockMapStub
from stockpy.metrics.finance import roe
from stockpy import expr


class RoeTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        data = {
            'n_income_attr_p': {
                2019: {
                    1: 2
                },
                2018: {
                    1: 4,
                    2: 5,
                    3: 7,
                    4: 8,
                }
            },
            'total_hldr_eqy_exc_min_int': {
                2019: {
                    1: 1
                },
                2018: {
                    1: 1,
                    4: 3,
                },
                2017: {
                    4: 1
                }
            },
        }
        cls.stock = StockMapStub(data)

    def test_roe_y(self):
        m = roe.roe_y()

        # n_income_arrt_p(2019.1) / ((total_hldr_eqy_exc_min_int(2018.4)
        #                            +total_hldr_eqy_exc_min_int(2019.1))
        #                           /2)
        v = m.expr.eval(self.stock, 2019, 1)
        s1 = expr.Get('n_income_attr_p').eval(self.stock, 2018, 4)
        s2 = expr.Get('total_hldr_eqy_exc_min_int').eval(self.stock, 2018, 4)
        s3 = expr.Get('total_hldr_eqy_exc_min_int').eval(self.stock, 2017, 4)
        self.assertEqual(s1/((s2+s3)/2), v)

    def test_roe_ttm(self):
        m = roe.roe_ttm()

        # n_income_arrt_p(2019.1) / ((total_hldr_eqy_exc_min_int(2018.4)
        #                            +total_hldr_eqy_exc_min_int(2019.1))
        #                           /2)
        v = m.expr.eval(self.stock, 2019, 1)
        s1 = expr.Get('f_income_attr_p_ttm').eval(self.stock, 2019, 1)
        s2 = expr.Get('total_hldr_eqy_exc_min_int').eval(self.stock, 2019, 1)
        s3 = expr.Get('total_hldr_eqy_exc_min_int').eval(self.stock, 2018, 1)

        self.assertEqual(s1/(s2+s3)*2, v)
