from stockpy.meta import MetricsMeta
from stockpy.expr import Value, Sum, Div, Get, Range


def metrics():
    metas = [
        # 滚动净利润：连续12个月
        MetricsMeta('f_income.ttm', Sum(
            Range(Get('n_income'), quarter=4))),
        # 滚动ROE get(n_income_ttm) / ((get(total_hldr_eqy_inc_min_int) + get(total_hldr_eqy_inc_min_int,-4))/2)
        MetricsMeta('roe.ttm',
                    Div(Get('f_income.ttm'),
                        Div(
                            Sum(Get('total_hldr_eqy_inc_min_int'),
                                Get('total_hldr_eqy_inc_min_int', 1)
                                ),
                            Value(2))))
    ]
    return metas
