from stockpy.metrics.base import MetricsMeta
from stockpy import expr


def sale_net_profit_ratio():
    '''销售净利率'''
    return MetricsMeta('f_sale_net_profit_y.r',
                       expr.Sub(expr.Get('f_gross_profit_y.r'),
                                expr.Get('f_exp_3_y.r'),
                                expr.Get('f_income_tax_y.r')),
                       display='销售净利率')


def gross_profit_ratio():
    '''毛利率'''
    return MetricsMeta('f_gross_profit_y.r',
                       expr.Sub(expr.Value(1),
                                expr.Div(expr.Get('oper_cost', period='y'),
                                         expr.Get('revenue', period='y'))),
                       display='毛利率')


def exp_3_ratio():
    '''三费占比'''
    return MetricsMeta('f_exp_3_y.r',
                       expr.Div(expr.Sum(expr.Get('sell_exp', period='y'),
                                         expr.Get(
                                             'admin_exp', period='y'),
                                         expr.Get('fin_exp', period='y')),
                                expr.Get('revenue', period='y')),
                       display='三费占比')


def sell_revenue_ratio():
    '''销售费用占比'''
    return MetricsMeta('f_sell_revenue_y.r',
                       expr.Div(expr.Get('sell_exp', period='y'),
                                expr.Get('revenue', period='y')),
                       display='销售费用占比')


def admin_revenue_ratio():
    '''管理费用占比'''
    return MetricsMeta('f_admin_revenue_y.r',
                       expr.Div(expr.Get('admin_exp', period='y'),
                                expr.Get('revenue', period='y')),
                       display='管理费用占比')


def fin_exp_revenue_ratio():
    '''财务费用占比'''
    return MetricsMeta('f_fin_exp_revenue_y.r',
                       expr.Div(expr.Get('fin_exp', period='y'),
                                expr.Get('revenue', period='y')),
                       display='财务费用占比')


def income_tax_ratio():
    '''所得税占比'''
    return MetricsMeta('f_income_tax_y.r',
                       expr.Div(expr.Get('income_tax', period='y'),
                                expr.Get('revenue', period='y')),
                       display='所得税占比')


def total_assets_tunrover_rate():
    '''总资产周转率=营业收入/总资产'''
    return MetricsMeta('f_total_assets_tunrover_y.r',
                       expr.Div(expr.Get('revenue', period='y'),
                                expr.Div(expr.Sum(expr.Get('f_total_assets_y'),
                                                  expr.Before(expr.Get(
                                                      'f_total_assets_y',
                                                      period='y'), past_year=1)),
                                         expr.Value(2))
                                ),
                       display='总资产周转率')


def total_assets():
    '''总资产 = 流动资产合计 + 非流动资产合计'''
    return MetricsMeta('f_total_assets_y',
                       expr.Sum(expr.Get('total_nca', period='y'),
                                expr.Get('total_cur_assets', period='y')),
                       display='总资产')


def leverage():
    ''' 杠杆倍数
        = 资产/所有者权益=资产/(资产-负债)
        = 1/(1-资产负债率)
    '''
    return MetricsMeta('f_leverage_y',
                       expr.Div(expr.Get('f_total_assets_y'),
                                expr.Get('total_hldr_eqy_exc_min_int',
                                         period='y')),
                       display='杠杆倍数')


def metrics():
    metas = [
        # roe = sale_net_profit_ratio * total_assets_tunrover_ratio * leverage
        sale_net_profit_ratio(),
        total_assets_tunrover_rate(),
        leverage(),

        gross_profit_ratio(),
        exp_3_ratio(),
        sell_revenue_ratio(),
        admin_revenue_ratio(),
        fin_exp_revenue_ratio(),
        income_tax_ratio(),
        total_assets()
    ]
    return metas
