import unittest
from tests import StockStub, StockMapStub
from stockpy.metrics.finance import (
    balance_sheet,
    operating as op
)
from stockpy.expr import Get


class BalanceSheetTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = {
            'inventories': {
                2018: {
                    4: 10
                },
                2017: {
                    4: 5
                }
            },
            'oper_cost': {
                2018: {
                    4: 5
                },
                2017: {
                    4: 3
                }
            },
            'accounts_receiv': {
                2018: {
                    4: 10
                },
                2017: {
                    4: 5
                }
            },
            'c_fr_sale_sg': {
                2018: {
                    4: 5
                },
                2017: {
                    4: 3
                }
            },
            'prepayment': {
                2018: {
                    4: 5
                },
                2017: {
                    4: 3
                }
            },
            'adv_receipts': {
                2018: {
                    4: 5
                },
                2017: {
                    4: 3
                }
            },
            'acct_payable': {
                2018: {
                    4: 5
                },
                2017: {
                    4: 3
                }
            }
        }
        cls.stock = StockMapStub(cls.data)

    def test_f_accounts_receiv_y2y(self):
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
        m = balance_sheet.metrics()[0]

        # 2019.1 - 2018.1
        v = m.expr.eval(stock, 2019, 1)
        self.assertEqual(4, v)

        # 2019.4 - 2018.4
        v = m.expr.eval(stock, 2019, 4)
        self.assertEqual(4, v)

    def test_f_current_y_r(self):
        data = {
            'total_cur_assets': {
                2018: {
                    4: 2
                }
            },
            'total_cur_liab': {
                2018: {
                    4: 1
                }
            }
        }
        stock = StockMapStub(data)
        m = balance_sheet.metrics()[4]

        # 2019.1 - 2018.1
        v = m.expr.eval(stock, 2019, 1)
        self.assertEqual(2/1, v)

    def test_days_inventory_y(self):
        m = op.days_inventory_y().expr
        v = m.eval(self.stock, 2019, 1)
        s1 = Get('f_inventory_ave_y').eval(self.stock, 2019, 1)
        s2 = Get('oper_cost', period='y').eval(self.stock, 2019, 1)
        self.assertEqual(360*s1/s2, v)

    def test_days_accounts_receiv_y(self):
        m = op.days_accounts_receiv_y().expr
        v = m.eval(self.stock, 2019, 1)
        s1 = Get('f_accounts_receiv_ave_y').eval(self.stock, 2019, 1)
        s2 = Get('c_fr_sale_sg', period='y').eval(self.stock, 2019, 1)
        self.assertEqual(360*s1/s2, v)

    def test_days_prepayment_y(self):
        m = op.days_prepayment_y().expr
        v = m.eval(self.stock, 2019, 1)
        s1 = Get('f_prepayment_ave_y').eval(self.stock, 2019, 1)
        s2 = Get('oper_cost', period='y').eval(self.stock, 2019, 1)
        self.assertEqual(360*s1/s2, v)

    def test_days_adv_receipts_y(self):
        m = op.days_adv_receipts_y().expr
        v = m.eval(self.stock, 2019, 1)
        s1 = Get('f_adv_receipts_ave_y').eval(self.stock, 2019, 1)
        s2 = Get('c_fr_sale_sg', period='y').eval(self.stock, 2019, 1)
        self.assertEqual(360*s1/s2, v)

    def test_days_acct_payable_y(self):
        m = op.days_acct_payable_y().expr
        v = m.eval(self.stock, 2019, 1)
        s1 = Get('f_acct_payable_ave_y').eval(self.stock, 2019, 1)
        s2 = Get('oper_cost', period='y').eval(self.stock, 2019, 1)
        self.assertEqual(360*s1/s2, v)

    def test_net_operating_cycle(self):
        m = op.net_operating_cycle().expr
        v = m.eval(self.stock, 2019, 1)
        s1 = Get('f_days_inventory_y').eval(self.stock, 2019, 1)
        s2 = Get('f_days_accounts_receiv_y',
                 period='y').eval(self.stock, 2019, 1)
        s3 = Get('f_days_prepayment_y',
                 period='y').eval(self.stock, 2019, 1)
        s4 = Get('f_days_acct_payable_y',
                 period='y').eval(self.stock, 2019, 1)
        s5 = Get('f_days_adv_receipts_y',
                 period='y').eval(self.stock, 2019, 1)
        self.assertEqual(s1+s2+s3-s4-s5, v)
