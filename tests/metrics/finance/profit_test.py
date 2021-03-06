import unittest
from stockpy.metrics.finance import (
    profit as pf
)
from stockpy import expr
from tests import StockMapStub


class ProfitTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = {
            'n_cashflow_act': {
                2019: {
                    1: 2
                }
            },
            'c_pay_acq_const_fiolta': {
                2019: {
                    1: 1
                }
            },
            'c_fr_sale_sg': {
                2019: {
                    1: 2
                }
            },
            'revenue': {
                2019: {
                    1: 100
                },
                2018: {
                    4: 100
                }
            },
            'notes_receiv': {
                2019: {
                    1: 1
                }
            },
            'accounts_receiv': {
                2019: {
                    1: 1
                }
            },
            'adv_receipts': {
                2019: {
                    1: 1
                }
            },
            'oper_cost': {
                2019: {
                    1: 1
                },
                2018: {
                    4: 1
                }
            },
            'sell_exp': {
                2019: {
                    1: 1
                },
                2018: {
                    4: 1
                }
            },
            'revadmin_expenue': {
                2019: {
                    1: 1
                },
                2018: {
                    4: 1
                }
            },
            'fin_exp': {
                2019: {
                    1: 1
                },
                2018: {
                    4: 1
                }
            },
            'income_tax': {
                2019: {
                    1: 1
                },
                2018: {
                    4: 1
                }
            },
            'total_nca': {
                2019: {
                    1: 20
                },
                2018: {
                    4: 20
                }
            },
            'total_cur_assets': {
                2019: {
                    1: 10
                },
                2018: {
                    4: 10
                }
            },
            'total_hldr_eqy_exc_min_int': {
                2019: {
                    1: 3
                },
                2018: {
                    4: 3
                }
            }
        }
        cls.stock = StockMapStub(cls.data)

    def test_sale_net_profit_ratio(self):
        m = pf.sale_net_profit_ratio().expr
        v = m.eval(self.stock, 2019, 1)
        s1 = pf.gross_profit_ratio().expr.eval(self.stock, 2019, 1)
        s2 = pf.exp_3_ratio().expr.eval(self.stock, 2019, 1)
        s3 = pf.income_tax_ratio().expr.eval(self.stock, 2019, 1)
        self.assertEqual(s1-s2-s3, v)

    def test_total_assets_tunrover_ratio(self):
        v = pf.total_assets_tunrover_rate().expr.eval(self.stock, 2019, 1)
        s1 = expr.Get('revenue', period='y').eval(self.stock, 2019, 1)
        s2 = expr.Get('f_total_assets_y').eval(self.stock, 2019, 1)
        self.assertEqual(s1/s2, v)

    def test_leverage(self):
        v = pf.leverage().expr.eval(self.stock, 2019, 1)
        s1 = expr.Get('f_total_assets_y').eval(self.stock, 2019, 1)
        s2 = expr.Get('total_hldr_eqy_exc_min_int',
                      period='y').eval(self.stock, 2019, 1)
        self.assertEqual(s1/s2, v)
