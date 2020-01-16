from stockpy.metrics.base import MetricsMeta
from stockpy import expr


def sale_net_profit_ratio():
    '''销售净利率'''
    return MetricsMeta('f_sale_net_profit.r',
                       expr.Sub(expr.Get('f_gross_profit.r'),
                                expr.Get('f_exp_3.r'),
                                expr.Get('f_income_tax.r')))


def gross_profit_ratio():
    '''毛利率'''
    return MetricsMeta('f_gross_profit.r',
                       expr.Sub(expr.Value(1),
                                expr.Div(expr.Get('oper_cost'),
                                         expr.Get('revenue'))))


def exp_3_ratio():
    '''三费占比'''
    return MetricsMeta('f_exp_3.r',
                       expr.Div(expr.Sum(expr.Get('sell_exp'),
                                         expr.Get('revadmin_expenue'),
                                         expr.Get('fin_exp')),
                                expr.Get('revenue')))


def income_tax_ratio():
    '''所得税占比'''
    return MetricsMeta('f_income_tax.r',
                       expr.Div(expr.Get('income_tax'), expr.Get('revenue')))


def total_assets_tunrover_ratio():
    '''总资产周转率=营业收入/总资产'''
    return MetricsMeta('f_total_assets_tunrover.r',
                       expr.Div(expr.Get('revenue'),
                                expr.Get('f_total_assets')))


def total_assets():
    '''总资产 = 流动资产合计 + 非流动资产合计'''
    return MetricsMeta('f_total_assets',
                       expr.Sum(expr.Get('total_nca'),
                                expr.Get('total_cur_assets')))


def leverage():
    ''' 杠杆倍数
        = 资产/所有者权益=资产/(资产-负债)
        = 1/(1-资产负债率)
    '''
    return MetricsMeta('f_leverage',
                       expr.Div(expr.Get('f_total_assets'),
                                expr.Get('total_hldr_eqy_exc_min_int')))


def metrics():
    metas = [
        sale_net_profit_ratio(),
        gross_profit_ratio(),
        exp_3_ratio(),
        income_tax_ratio(),
        total_assets_tunrover_ratio(),
        total_assets(),
        leverage()
    ]
    return metas
