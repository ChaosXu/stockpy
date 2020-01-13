import unittest
from tests import StockMapStub
from stockpy.metrics.finance import roe
from stockpy import expr


class RoeTest(unittest.TestCase):

    def test_f_roe(self):
        data = {
            'n_income_attr_p': {
                2019: {
                    1: 8,
                }
            },
            'total_hldr_eqy_exc_min_int': {
                2019: {
                    1: 3,
                },
                2018: {
                    4: 1
                }
            },
        }
        stock = StockMapStub(data)
        m = roe.metrics()[0]  # f_roe_y

        # n_income_arrt_p(2019.1) / ((total_hldr_eqy_exc_min_int(2018.4)
        #                            +total_hldr_eqy_exc_min_int(2019.1))
        #                           /2)
        v = m.expr.eval(stock, 2019, 1)
        self.assertEqual(8/((1+3)/2), v)

    def test_f_roe_prev_1_year(self):
        data = {
            'n_income_attr_p': {
                2019: {
                    4: 8,
                }
            },
            'total_hldr_eqy_exc_min_int': {
                2019: {
                    4: 3,
                },
                2018: {
                    4: 1
                }
            },
        }
        stock = StockMapStub(data)
        m = expr.Before(expr.Get('f_roe_y'), past_year=1)

        v = m.eval(stock, 2020, 1)
        self.assertEqual(8/((1+3)/2), v)
