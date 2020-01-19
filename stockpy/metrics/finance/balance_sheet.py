from stockpy.metrics.base import MetricsMeta
from stockpy import expr


def accounts_receiv_q_y2y():
    '''季度应收账款增长(同比) '''
    return MetricsMeta('f_accounts_receiv_q.y2y',
                       expr.Sub(expr.Get('accounts_receiv'),
                                expr.Before(expr.Get('accounts_receiv'),
                                            past_quarter=4)))


def accounts_receiv_y_y2y():
    '''年度应收账款增长(同比)'''
    return MetricsMeta('f_accounts_receiv_y.y2y',
                       expr.Sub(expr.Get('accounts_receiv', period='y'),
                                expr.Before(expr.Get('accounts_receiv',
                                                     period='y'),
                                            past_year=1)))


def inventories_q_y2y():
    '''季度存货增长'''
    return MetricsMeta('f_inventories_q.y2y',
                       expr.Sub(expr.Get('inventories'),
                                expr.Before(expr.Get('inventories'),
                                            past_quarter=4)))


def inventories_y_y2y():
    '''年度存货增长'''
    return MetricsMeta('f_inventories_y.y2y',
                       expr.Sub(expr.Get('inventories', period='y'),
                                expr.Before(expr.Get('inventories', period='y'),
                                            past_year=1)))


def assets_liab_ratio_y():
    ''' 资产负债率
        ＞50%需小心
        同行比较，越高风险越大
    '''
    return MetricsMeta('f_assets_liab_y.r',
                       expr.Div(expr.Get('total_liab', period='y'),
                                expr.Get('f_total_assets_y')))


def interest_bearing_liab_y():
    ''' 有息负债
        = 短期借款 + 1年内到期的长期负债 + 长期借款 + 应付债券 + 长期应付款
    '''
    return MetricsMeta('f_interest_bearing_liab_y',
                       expr.Sum(
                           expr.Get('lt_borr', period='y'),
                           expr.Get('st_borr', period='y'),
                           expr.Get('bond_payable', period='y'),
                           expr.Get('lt_payable', period='y'),
                           expr.Get('non_cur_liab_due_1y', period='y')))


def interest_bearing_liab_ratio():
    ''' 有息负债率 = 有息负债 / 总资产
        同行比较，越高风险越大
    '''
    MetricsMeta('f_interest_bearing_liab_y.r',
                expr.Div(expr.Get('f_interest_bearing_y'),
                         expr.Get('f_total_assets_y')))


def current_ratio_y():
    ''' 流动比率 = 流动资产 / 流动负债
        流动比率 (CR) 基准值=2
    '''
    return MetricsMeta('f_current_y.r',
                       expr.Div(expr.Get('total_cur_assets', period='y'),
                                expr.Get('total_cur_liab', period='y')))


def quick_ratio_y():
    ''' 速动比率 = 速动资产 / 流动负债
        速动资产 = 流动资产 - 存货 - 预付账款 - 待摊费用
        速动比率 (QR) 基准值=1
    '''
    return MetricsMeta('f_quick_y.r',
                       expr.Div(
                           expr.Get('f_quick_y'),
                           expr.Get('total_cur_liab', period='y')))


def quick_y():
    ''' 速动资产
        = 流动资产 - 存货 - 预付账款
        注：待摊费用忽略不扣除
    '''
    return MetricsMeta('f_quick_y',
                       expr.Sub(expr.Get('total_cur_assets', period='y'),
                                expr.Get('inventories', period='y'),
                                expr.Get('prepayment', period='y')))


def metrics():
    metas = [
        accounts_receiv_q_y2y(),
        accounts_receiv_y_y2y(),
        inventories_q_y2y(),
        inventories_y_y2y(),
        assets_liab_ratio_y(),
        interest_bearing_liab_y(),
        current_ratio_y(),
        quick_ratio_y(),
        quick_y()

    ]
    return metas
