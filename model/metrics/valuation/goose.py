from model.meta import MetricsMeta
from model.meta import Value
from model.expr.arithmetic import Sum
from model.expr.arithmetic import Div
from model.expr.arithmetic import Sub
from model.expr.ttm import TTM
from model.expr.range import Range
from model.expr.get import Get


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
