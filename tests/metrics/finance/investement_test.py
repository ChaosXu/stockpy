import unittest
from tests import StockStub, StockMapStub
from stockpy.metrics.finance.cashflow import investment as inv
from stockpy.expr import Get


class InvestementTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = {
            'n_income_attr_p': {
                2018: {
                    4: 40
                },
                2009: {
                    4: 4
                },
            },
            'n_cashflow_act': {
                2018: {
                    4: 2
                },
                2017: {
                    4: 2
                },
                2016: {
                    4: 2
                },
                2015: {
                    4: 2
                },
                2014: {
                    4: 2
                },
                2013: {
                    4: 2
                },
                2012: {
                    4: 2
                },
                2011: {
                    4: 2
                },
                2010: {
                    4: 2
                },
                2009: {
                    4: 2
                }
            },
            'c_pay_acq_const_fiolta': {
                2018: {
                    4: 1
                },
                2017: {
                    4: 1
                },
                2016: {
                    4: 1
                },
                2015: {
                    4: 1
                },
                2014: {
                    4: 1
                },
                2013: {
                    4: 1
                },
                2012: {
                    4: 1
                },
                2011: {
                    4: 1
                },
                2010: {
                    4: 1
                },
                2009: {
                    4: 1
                }
            }
        }
        cls.stock = StockMapStub(cls.data)

    def test_cash_flow_free_y(self):
        m = inv.cashflow_free_y().expr
        v = m.eval(self.stock, 2019, 1)
        s1 = Get('n_cashflow_act', period='y').eval(self.stock, 2019, 1)
        s2 = Get('c_pay_acq_const_fiolta',
                 period='y').eval(self.stock, 2019, 1)
        self.assertEqual(s1-s2, v)

    def test_cashflow_free_10_years_ratio(self):
        m = inv.cashflow_free_pay_10_years_ratio().expr
        v = m.eval(self.stock, 2019, 1)
        self.assertEqual(1, v)

    def test_net_profit_10_years_growth_ratio(self):
        m = inv.net_profit_growth_pay_10_years_ratio().expr
        v = m.eval(self.stock, 2019, 1)
        self.assertEqual(3.6, v)
