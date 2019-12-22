from stockpy.meta import MetricsMeta
from stockpy.expr.value import Value
from stockpy.expr.arithmetic import Sum
from stockpy.expr.arithmetic import Div
from stockpy.expr.arithmetic import Sub
from stockpy.expr.ttm import TTM
from stockpy.expr.range import Range
from stockpy.expr.get import Get


def metrics():
    metas = [
        
        # 滚动净利润：ttm(n_income)
        MetricsMeta('f_income.ttm', TTM(Get('n_income'))),
        # 滚动ROE get(n_income_ttm) / ((get(total_hldr_eqy_inc_min_int) + get(total_hldr_eqy_inc_min_int,-4))/2)
        MetricsMeta('roe.ttm',
                    Div(Get('f_income.ttm'),
                        Div(Sum(Get('total_hldr_eqy_inc_min_int'), Get('total_hldr_eqy_inc_min_int', 1)), Value(2))))
    ]
    return metas
