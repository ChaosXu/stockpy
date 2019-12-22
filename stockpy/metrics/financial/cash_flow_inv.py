from stockpy.meta import MetricsMeta
from stockpy.expr.value import Value
from stockpy.expr.arithmetic import Sum
from stockpy.expr.arithmetic import Div
from stockpy.expr.arithmetic import Sub
from stockpy.expr.range import Range
from stockpy.expr.get import Get


def metrics():
    '''Cash flow from stockpy.investing activities'''
    metas = [
        # 自由现金流 = 经营活动产生的现金流净额-购建固定资产、无形资产和其他长期资产支付的现金
        MetricsMeta("f_cashflow_free",
                    Sub(Get('n_cashflow_act'), Get('c_pay_acq_const_fiolta'))),
        # 十年自由现金流
        MetricsMeta("f_cashflow_free.sum_10y",
                    Sum(Range('n_cashflow_free', 10))),
        # 十年资本开支总和
        MetricsMeta("f_pay_acq_const_fiolta.sum_10y",
                    Sum(Range('c_pay_acq_const_fiolta', 10))),

        # 小熊基本值 = 十年自由现金流总和/十年资本开支总和*100%
        MetricsMeta("xx_basic_cf_pacf.r",
                    Div(Get('n_cashflow_free.sum_10y'), Get('f_pay_acq_const_fiolta.sum_10y'))),

        # 小熊增长值 =（第十年归母净利润-第一年归母净利润）/ 十年资本开支总和*100% TBD：需用扣非净利润计算
        MetricsMeta("xx_basic_cf_pacf.r",
                    Div(Sub(Get('n_income_attr_p'), Get('n_income_attr_p', 9)), Get('f_pay_acq_const_fiolta.sum_10y'))),
    ]
    return metas
