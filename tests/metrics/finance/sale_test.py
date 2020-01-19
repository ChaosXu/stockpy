import unittest
from stockpy.metrics.finance.cashflow import sale
from tests import StockMapStub


class CashFlowTest(unittest.TestCase):

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
                }
            },
            'sell_exp': {
                2019: {
                    1: 1
                }
            },
            'revadmin_expenue': {
                2019: {
                    1: 1
                }
            },
            'fin_exp': {
                2019: {
                    1: 1
                }
            },
            'income_tax': {
                2019: {
                    1: 1
                }
            },
            'total_nca': {
                2019: {
                    1: 20
                }
            },
            'total_cur_assets': {
                2019: {
                    1: 10
                }
            },
            'total_hldr_eqy_exc_min_int': {
                2019: {
                    1: 3
                }
            }
        }
        cls.stock = StockMapStub(cls.data)

    def test_sale_cash_ratio(self):
        m = sale.sale_cash_ratio().expr
        v = m.eval(self.stock, 2019, 1)
        self.assertEqual(self.data['c_fr_sale_sg'][2019][1] /
                         self.data['revenue'][2019][1], v)

    def test_sale_credit_ratio(self):
        m = sale.sale_cash_ratio().expr
        v = m.eval(self.stock, 2019, 1)
        f_receiv = sale.receivables().expr.eval(self.stock, 2019, 1)
        self.assertEqual(f_receiv /
                         self.data['revenue'][2019][1], v)

    def test_receivables(self):
        m = sale.receivables().expr
        v = m.eval(self.stock, 2019, 1)
        self.assertEqual(self.data['notes_receiv'][2019][1] +
                         self.data['accounts_receiv'][2019][1], v)

    def test_adv_receipt_ratio(self):
        m = sale.adv_receipt_ratio().expr
        v = m.eval(self.stock, 2019, 1)
        self.assertEqual(self.data['adv_receipts'][2019][1] -
                         self.data['revenue'][2019][1], v)
