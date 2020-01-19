import unittest
from tests import StockStub, StockMapStub
from stockpy.metrics.finance import balance_sheet
from stockpy.expr import Get


class BalanceSheetTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = {
            'inventories': {
                2019: {
                    1: 10
                },
                2018: {
                    1: 10,
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
                2019: {
                    1: 10
                },
                2018: {
                    1: 10,
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
            },
            'total_liab': {
                2018: {
                    4: 11
                }
            },
            'total_nca': {
                2018: {
                    4: 1
                }
            },
            'total_cur_assets': {
                2018: {
                    4: 1
                }
            },
            'bt_borr': {
                2018: {
                    4: 1
                }
            },
            'lt_borr': {
                2018: {
                    4: 1
                }
            },
            'st_borr': {
                2018: {
                    4: 1
                }
            },
            'bond_payable': {
                2018: {
                    4: 1
                }
            },
            'lt_payable': {
                2018: {
                    4: 1
                }
            },
            'non_cur_liab_due_1y': {
                2018: {
                    4: 1
                }
            },
            'total_cur_liab': {
                2018: {
                    4: 1
                }
            }
        }
        cls.stock = StockMapStub(cls.data)

    def test_accounts_receiv_q_y2y(self):
        v = balance_sheet.accounts_receiv_q_y2y().expr.eval(self.stock, 2019, 1)
        s1 = Get('accounts_receiv').eval(self.stock, 2019, 1)
        s2 = Get('accounts_receiv').eval(self.stock, 2018, 1)
        self.assertEqual(s1-s2, v)

    def test_accounts_receiv_y_y2y(self):
        v = balance_sheet.accounts_receiv_y_y2y().expr.eval(self.stock, 2019, 1)
        s1 = Get('accounts_receiv').eval(self.stock, 2018, 4)
        s2 = Get('accounts_receiv').eval(self.stock, 2017, 4)
        self.assertEqual(s1-s2, v)

    def test_inventories_q_y2y(self):
        v = balance_sheet.inventories_q_y2y().expr.eval(self.stock, 2019, 1)
        s1 = Get('inventories').eval(self.stock, 2019, 1)
        s2 = Get('inventories').eval(self.stock, 2018, 1)
        self.assertEqual(s1-s2, v)

    def test_inventories_y_y2y(self):
        v = balance_sheet.inventories_q_y2y().expr.eval(self.stock, 2019, 1)
        s1 = Get('inventories').eval(self.stock, 2018, 4)
        s2 = Get('inventories').eval(self.stock, 2018, 4)
        self.assertEqual(s1-s2, v)

    def test_assets_liab_ratio_y(self):
        v = balance_sheet.assets_liab_ratio_y().expr.eval(self.stock, 2019, 1)
        s1 = Get('total_liab', period='y').eval(self.stock, 2019, 1)
        s2 = Get('f_total_assets_y', period='y').eval(self.stock, 2019, 1)
        self.assertEqual(s1/s2, v)

    def test_interest_bearing_liab_y(self):
        v = balance_sheet.interest_bearing_liab_y().expr.eval(self.stock, 2019, 1)
        s1 = Get('lt_borr', period='y').eval(self.stock, 2019, 1)
        s2 = Get('st_borr', period='y').eval(self.stock, 2019, 1)
        s3 = Get('bond_payable', period='y').eval(self.stock, 2019, 1)
        s4 = Get('lt_payable', period='y').eval(self.stock, 2019, 1)
        s5 = Get('non_cur_liab_due_1y', period='y').eval(self.stock, 2019, 1)
        self.assertEqual(s1+s2+s3+s4+s5, v)

    def test_current_ratio_y(self):
        v = balance_sheet.current_ratio_y().expr.eval(self.stock, 2019, 1)
        s1 = Get('total_cur_assets', period='y').eval(self.stock, 2019, 1)
        s2 = Get('total_cur_liab', period='y').eval(self.stock, 2019, 1)
        self.assertEqual(s1/s2, v)

    def test_quick_ratio_y(self):
        v = balance_sheet.quick_ratio_y().expr.eval(self.stock, 2019, 1)
        s1 = Get('f_quick_y').eval(self.stock, 2019, 1)
        s2 = Get('total_cur_liab', period='y').eval(self.stock, 2019, 1)
        self.assertEqual(s1/s2, v)

    def test_quick_y(self):
        v = balance_sheet.quick_y().expr.eval(self.stock, 2019, 1)
        s1 = Get('total_cur_assets', period='y').eval(self.stock, 2019, 1)
        s2 = Get('inventories', period='y').eval(self.stock, 2019, 1)
        s3 = Get('prepayment', period='y').eval(self.stock, 2019, 1)
        self.assertEqual(s1-s2-s3, v)
