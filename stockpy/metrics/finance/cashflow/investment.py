from stockpy.metrics import MetricsMeta
from stockpy import expr


def cashflow_free_y():
    '''投资:自由现金流(年)'''
    return MetricsMeta('f_cashflow_free_y',
                       expr.Sub(
                           expr.Get('n_cashflow_act', period='y'),
                           expr.Get('c_pay_acq_const_fiolta', period='y')))


def cashflow_free_pay_10_years_ratio():
    '''10年自由现金流/10年资本开支比'''
    return MetricsMeta('f_cashflow_free_pay_10_y.r',
                       expr.Div(
                           expr.Sum(
                               expr.Get('f_cashflow_free_y'), [expr.Before(
                                   expr.Get('f_cashflow_free_y'),
                                   past_year=n)
                                   for n in range(1, 10)]),
                           expr.Sum(
                               expr.Get('c_pay_acq_const_fiolta', period='y'),
                               [expr.Before(
                                   expr.Get(
                                       'c_pay_acq_const_fiolta', period='y'),
                                   past_year=n)
                                   for n in range(1, 10)])))


def net_profit_growth_pay_10_years_ratio():
    '''10年净利润增长/10年资本开支比'''
    return MetricsMeta('f_n_income_attr_p_pay_10_y.r',
                       expr.Div(
                           expr.Sub(
                               expr.Get('n_income_attr_p', period='y'),
                               expr.Before(
                                   expr.Get('n_income_attr_p', period='y'),
                                   past_year=9)),
                           expr.Sum(
                               expr.Get('c_pay_acq_const_fiolta', period='y'),
                               [expr.Before(
                                   expr.Get(
                                       'c_pay_acq_const_fiolta', period='y'),
                                   past_year=n)
                                   for n in range(1, 10)])))


def metrics():
    metas = [
        cashflow_free_y(),
        cashflow_free_pay_10_years_ratio(),
        net_profit_growth_pay_10_years_ratio()
    ]
    return metas
