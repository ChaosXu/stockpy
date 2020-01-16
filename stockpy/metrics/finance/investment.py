from stockpy.metrics.base import MetricsMeta
from stockpy import expr


def free_cash_flow():
    '''投资:自由现金流'''
    return MetricsMeta('f_cashflow_free',
                       expr.Sub(expr.Get('n_cashflow_act'),
                                expr.Get('c_pay_acq_const_fiolta')))


def metrics():
    metas = [
        free_cash_flow()
    ]
    return metas
