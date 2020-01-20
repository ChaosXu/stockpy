import unittest
from tests import StockMapStub
from stockpy.valuation import goose
from stockpy import expr
import math


class GooseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        data = {
            'total_hldr_eqy_exc_min_int': {
                2019: {
                    1: 20
                },
                2018: {
                    1: 3
                }
            },
            'n_income_attr_p': {
                2019: {
                    1: 10,
                    4: 20
                },
                2018: {
                    1: 2,
                    2: 3,
                    3: 5,
                    4: 10
                },
                2017: {
                    4: 10/1.3
                },
                2016: {
                    4: 10/1.3/1.3
                },
                2015: {
                    4: 10/1.3/1.3/1.3
                },
                2014: {
                    4: 10/1.3/1.3/1.3/1.3
                },
                2013: {
                    4: 10/1.3/1.3/1.3/1.3/1.3
                },
                2012: {
                    4: 10/1.3/1.3/1.3/1.3/1.3/1.1
                },
                2011: {
                    4: 10/1.3/1.3/1.3/1.3/1.3/1.1/1.04
                }
            },
            'total_share': {
                2019: {
                    1: 100
                }
            }
        }
        cls.stock = StockMapStub(data)

    def test_market_cap(self):
        m = goose.market_cap(7, 2)

        v = m.eval(self.stock, 2019, 1)
        s1 = expr.Get('total_hldr_eqy_exc_min_int').eval(self.stock, 2019, 1)
        s2 = expr.Get('f_roe_ttm').eval(self.stock, 2019, 1)
        s3 = goose.growth_factor().eval(self.stock, 2019, 1)
        self.assertEqual(s1*math.pow((1+s2), (7+2+s3)), v)

    def test_price_share(self):
        mc = goose.market_cap(7, 2)
        ps = goose.price_share(mc)

        v = ps.eval(self.stock, 2019, 1)
        s1 = mc.eval(self.stock, 2019, 1)
        s2 = expr.Get('total_share').eval(self.stock, 2019, 1)
        self.assertEqual(s1/s2, v)

    def test_price_buying(self):
        mc = goose.market_cap(7, 2)
        p = goose.price_share(mc)
        pb = goose.price_buying(p)

        v = pb.eval(self.stock, 2019, 1)
        s1 = p.eval(self.stock, 2019, 1)
        s2 = goose.safety_factor().eval(self.stock, 2019, 1)
        self.assertEqual(s1*s2, v)

    def test_price_selling(self):
        mc = goose.market_cap(7, 2)
        p = goose.price_share(mc)
        ps = goose.price_selling(p)

        v = p.eval(self.stock, 2019, 1)
        s1 = ps.eval(self.stock, 2019, 1)
        s2 = goose.premium_rate().eval(self.stock, 2019, 1)
        self.assertEqual(s1*s2, v)

    def test_growth_factor(self):
        g = goose.growth_factor()
        v = g.eval(self.stock, 2019, 1)
        self.assertEqual(2, v)

        v = g.eval(self.stock, 2018, 1)
        self.assertEqual(1, v)

        v = g.eval(self.stock, 2017, 1)
        self.assertEqual(0, v)
