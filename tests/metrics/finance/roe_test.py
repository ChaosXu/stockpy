import unittest
from tests import StockMapStub
from stockpy.metrics.finance import roe
from stockpy import expr
from stockpy.filter import horse


class RoeTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        data = {
            'n_income_attr_p': {
                2019: {
                    1: 2,
                    3: 53413057.75
                },
                2018: {
                    1: 4,
                    2: 5,
                    3: 7,
                    4: 58366455.95,
                },
                2017: {
                    4: 42248863.96,
                },
                2016: {
                    4: 32708951.81,
                },
                2015: {
                    4: 18219460.42,
                },
                2014: {
                    4: 18906255.13,
                },
                2013: {
                    4: 14239832.62,
                }
            },
            'total_hldr_eqy_exc_min_int': {
                2019: {
                    1: 318311778.58,
                    3: 357482918.8
                },
                2018: {
                    1: 4,
                    2: 5,
                    3: 7,
                    4: 319545061.05,
                },
                2017: {
                    4: 192981208.87,
                },
                2016: {
                    4: 162728344.91,
                },
                2015: {
                    4: 23332404.42,
                },
                2014: {
                    4: 96162944.0,
                },
                2013: {
                    4: 77256688.87,
                },
                2012: {
                    4: 123016856.25,
                }
            },
        }
        cls.stock = StockMapStub(data)

    def test_roe_y(self):
        m = roe.roe_y()

        # n_income_arrt_p(2019.1) / ((total_hldr_eqy_exc_min_int(2018.4)
        #                            +total_hldr_eqy_exc_min_int(2019.1))
        #                           /2)
        def run(y, q):
            v = m.expr.eval(self.stock, y, 4)
            s1 = expr.Get('n_income_attr_p').eval(self.stock, y, q)
            s2 = expr.Get('total_hldr_eqy_exc_min_int').eval(self.stock, y, q)
            s3 = expr.Get('total_hldr_eqy_exc_min_int').eval(
                self.stock, y-1, q)
            a = s1/((s2+s3)/2)
            print(y, q, a, v)
            self.assertEqual(a, v, '{} {}'.format(y, q))

        run(2018, 4)
        run(2017, 4)  # 42248863.96/((192981208.87+162728344.91)/2)
        run(2016, 4)
        run(2015, 4)
        run(2014, 4)
        run(2013, 4)

    def test_range_roe(self):
        # n_income_arrt_p(2019.1) / ((total_hldr_eqy_exc_min_int(2018.4)
        #                            +total_hldr_eqy_exc_min_int(2019.1))
        #                           /2)
        def run(y, q):
            rm = expr.Range(expr.Before(expr.Get('f_roe_y'), past_year=1),
                            year_count=6)
            nm = self.roe_ge_15_pct_now()

            v = rm.eval(self.stock, y, 4)

            v2 = expr.Ge(rm, expr.Value(0.15)).eval(self.stock, y, 4)
            print('last 6 years', v, v2)

            v3 = nm.eval(self.stock, y, q)
            print('current', v3, expr.Get('f_roe').eval(self.stock, y, q))

            v4 = expr.And(expr.Ge(rm, expr.Value(0.15)),
                          nm).eval(self.stock, y, q)
            print('last 7 years', v4)

        run(2019, 3)

        m = horse.roe_ge_15_pct_last_7_year()
        v = m.eval(self.stock, 2019, 3)
        print('last 7 years 2', v)

    def roe_ge_15_pct_now(self):
        def fv(stock: expr.ExprCtx, year: int, quarter: int):
            v = {
                4: 0.15,
                3: 0.15/4*3,
                2: 0.15/4*2,
                1: 0.15/4,
            }
            return v[quarter]

        return expr.Ge(
            expr.Get('f_roe'),
            expr.FuncValue(fv)
        )

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
