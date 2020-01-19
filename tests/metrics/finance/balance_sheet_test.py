import unittest
from tests import StockStub, StockMapStub
from stockpy.metrics.finance import balance_sheet
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
