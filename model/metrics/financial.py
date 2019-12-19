from model.meta import MetricsMeta
from model.meta import Value
from model.expr.arithmetic import Sum
from model.expr.arithmetic import Div
from model.expr.ttm import TTM
from model.expr.range import Range
from model.expr.get import Get


def metrics():
    metas = [
        # 自由现金流 = 经营活动产生的现金流净额-购建固定资产、无形资产和其他长期资产支付的现金
        MetricsMeta("n_cashflow_free",
                    Div(Get('n_cashflow_act'), Get('c_pay_acq_const_fiolta'))),
        # 十年自由现金流
        MetricsMeta("n_cashflow_free.10y",
                    Sum(Range('n_cashflow_free', 10))),
        # 十年资本开支总和
        MetricsMeta("c_pay_acq_const_fiolta.10y",
                    Sum(Range('c_pay_acq_const_fiolta', 10))),
        MetricsMeta("xx_basic",
                    Div(Sum('n_cashflow_act'), Sum('c_pay_acq_const_fiolta'))),
        # ttm(n_income)
        MetricsMeta('n_income.ttm', TTM(Get('n_income'))),
        # get(n_income_ttm) / ((get(total_hldr_eqy_inc_min_int) + get(total_hldr_eqy_inc_min_int,-4))/2)
        MetricsMeta('roe.ttm', Div(Get('n_income.ttm'),
                                   Div(Sum(Get('total_hldr_eqy_inc_min_int'), Get('total_hldr_eqy_inc_min_int', 1)), Value(2))))
    ]
    return metas
