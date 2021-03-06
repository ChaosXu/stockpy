from stockpy.metrics.base import (MetricsMeta,
                                  metrics_def,
                                  metrics_ratio)
from stockpy import expr


# def sale_net_profit_ratio():
#     '''销售净利率%'''
#     return MetricsMeta('f_sale_net_profit_y.r',
#                        expr.Sub(expr.Get('f_gross_profit_y.r'),
#                                 expr.Get('f_exp_3_y.r'),
#                                 expr.Get('f_income_tax_y.r')),
#                        display='销售净利率')


def gross_profit_ratio_y():
    '''毛利率%'''
    return MetricsMeta('f_gross_profit_y.r',

                       expr.Sub(expr.Value(1),
                                expr.Div(expr.Get('oper_cost', period='y'),
                                         expr.Get('revenue', period='y'))),
                       display='毛利率')


def gross_profit_ratio():
    '''毛利率%'''
    return MetricsMeta('f_gross_profit.r',

                       expr.Sub(expr.Value(1),
                                expr.Div(expr.Get('oper_cost'),
                                         expr.Get('revenue'))),
                       display='毛利率')


# def oper_cost_y_ratio():
#     '''成本率'''
#     return MetricsMeta('f_oper_cost_y.r',
#                        expr.Sub(expr.Value(100), expr.Get(
#                            'f_gross_profit_y.r')),
#                        display='成本率')


def exp_3_ratio_y():
    '''三费占比'''
    return MetricsMeta('f_exp_3_y.r',
                       expr.Div(expr.Sum(expr.Get('sell_exp', period='y'),
                                         expr.Get(
                           'admin_exp', period='y'),
                           expr.Get('fin_exp', period='y')),
                           expr.Get('revenue', period='y')),
                       display='三费占比')


def exp_3_ratio():
    '''三费占比'''
    return MetricsMeta('f_exp_3.r',
                       expr.Div(expr.Sum(expr.Get('sell_exp'),
                                         expr.Get(
                           'admin_exp'),
                           expr.Get('fin_exp')),
                           expr.Get('revenue')),
                       display='三费占比')


def sell_revenue_ratio_y():
    '''销售费用占比'''
    return MetricsMeta('f_sell_revenue_y.r',
                       expr.Div(expr.Get('sell_exp', period='y'),
                                expr.Get('revenue', period='y')),
                       display='销售费用占比')


def sell_revenue_ratio():
    '''销售费用占比'''
    return MetricsMeta('f_sell_revenue.r',
                       expr.Div(expr.Get('sell_exp'),
                                expr.Get('revenue')),
                       display='销售费用占比')


def admin_revenue_ratio_y():
    '''管理费用占比'''
    return MetricsMeta('f_admin_revenue_y.r',
                       expr.Div(expr.Get('admin_exp', period='y'),
                                expr.Get('revenue', period='y')),
                       display='管理费用占比')


def admin_revenue_ratio():
    '''管理费用占比'''
    return MetricsMeta('f_admin_revenue.r',
                       expr.Div(expr.Get('admin_exp'),
                                expr.Get('revenue')),
                       display='管理费用占比')


def fin_exp_revenue_ratio_y():
    '''财务费用占比'''
    return MetricsMeta('f_fin_exp_revenue_y.r',
                       expr.Div(expr.Get('fin_exp', period='y'),
                                expr.Get('revenue', period='y')),
                       display='财务费用占比')


def fin_exp_revenue_ratio():
    '''财务费用占比'''
    return MetricsMeta('f_fin_exp_revenue.r',
                       expr.Div(expr.Get('fin_exp'),
                                expr.Get('revenue')),
                       display='财务费用占比')


def income_tax_ratio():
    '''所得税占比'''
    return MetricsMeta('f_income_tax.r',
                       expr.Div(expr.Get('income_tax'),
                                expr.Get('revenue')),
                       display='所得税占比')


def income_tax_ratio_y():
    '''所得税占比'''
    return MetricsMeta('f_income_tax_y.r',
                       expr.Div(expr.Get('income_tax', period='y'),
                                expr.Get('revenue', period='y')),
                       display='所得税占比')


def total_assets():
    '''总资产 = 流动资产合计 + 非流动资产合计'''
    return MetricsMeta('f_total_assets',
                       expr.Sum(expr.Get('total_nca'),
                                expr.Get('total_cur_assets')),
                       display='总资产')


def total_assets_y():
    '''总资产 = 流动资产合计 + 非流动资产合计'''
    return MetricsMeta('f_total_assets_y',
                       expr.Sum(expr.Get('total_nca', period='y'),
                                expr.Get('total_cur_assets', period='y')),
                       display='总资产')


def leverage():
    ''' 杠杆倍数
        = 资产/所有者权益 = 资产/(资产-负债)
        = 1/(1-资产负债率)
    '''
    return MetricsMeta('f_leverage',
                       expr.Div(expr.Get('f_total_assets'),
                                expr.Get('total_hldr_eqy_exc_min_int')),
                       display='杠杆倍数')


def leverage_y():
    ''' 杠杆倍数
        = 资产/所有者权益 = 资产/(资产-负债)
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
        # sale_net_profit_ratio(),
        # total_assets_tunrover_rate(),
        leverage(),
        leverage_y(),

        gross_profit_ratio(),
        gross_profit_ratio_y(),
        exp_3_ratio(),
        exp_3_ratio_y(),
        sell_revenue_ratio(),
        sell_revenue_ratio_y(),
        admin_revenue_ratio(),
        admin_revenue_ratio_y(),
        fin_exp_revenue_ratio(),
        fin_exp_revenue_ratio_y(),
        income_tax_ratio(),
        income_tax_ratio_y(),
        total_assets(),
        total_assets_y()
        # oper_cost_y_ratio()
    ]
    return metas
