from stockpy.metrics.base import MetricsMeta
from stockpy import expr


def days_inventory_y():
    '''存货周转天数(年)'''
    return MetricsMeta('f_days_inventory_y',
                       expr.Div(expr.Multi(expr.Get('f_inventory_ave_y'),
                                           expr.Value(360)),
                                expr.Get('oper_cost', period='y')))


def inventroy_ave_y():
    '''平均存货(年)'''
    return MetricsMeta('f_inventory_ave_y',
                       expr.Div(
                           expr.Sum(
                               expr.Get('inventories', period='y'),
                               expr.Before(expr.Get('inventories', period='y'), past_year=1)),
                           expr.Value(2)))


def days_accounts_receiv_y():
    '''应收账款周转天数'''
    return MetricsMeta('f_days_accounts_receiv_y',
                       expr.Div(expr.Multi(expr.Get('f_accounts_receiv_ave_y'),
                                           expr.Value(360)),
                                expr.Get('c_fr_sale_sg', period='y')))


def accounts_receiv_ave_y():
    '''平均应收账款(年)'''
    return MetricsMeta('f_accounts_receiv_ave_y',
                       expr.Div(
                           expr.Sum(
                               expr.Get('accounts_receiv', period='y'),
                               expr.Before(expr.Get('accounts_receiv', period='y'), past_year=1)),
                           expr.Value(2)))


def days_prepayment_y():
    '''预付账款周转天数'''
    return MetricsMeta('f_days_prepayment_y',
                       expr.Div(expr.Multi(expr.Get('f_prepayment_ave_y'),
                                           expr.Value(360)),
                                expr.Get('oper_cost', period='y')))


def prepayment_ave_y():
    '''平均预付账款(年)'''
    return MetricsMeta('f_prepayment_ave_y',
                       expr.Div(
                           expr.Sum(
                               expr.Get('prepayment', period='y'),
                               expr.Before(expr.Get('prepayment', period='y'),
                                           past_year=1)),
                           expr.Value(2)))


def days_adv_receipts_y():
    '''预收账款周转天数'''
    return MetricsMeta('f_days_adv_receipts_y',
                       expr.Div(expr.Multi(expr.Get('f_adv_receipts_ave_y'),
                                           expr.Value(360)),
                                expr.Get('c_fr_sale_sg', period='y')))


def adv_receipts_ave_y():
    '''平均预收账款(年)'''
    return MetricsMeta('f_adv_receipts_ave_y',
                       expr.Div(
                           expr.Sum(
                               expr.Get('adv_receipts', period='y'),
                               expr.Before(expr.Get('adv_receipts', period='y'), past_year=1)),
                           expr.Value(2)))


def days_acct_payable_y():
    '''应付账款周转天数'''
    return MetricsMeta('f_days_acct_payable_y',
                       expr.Div(expr.Multi(expr.Get('f_acct_payable_ave_y'),
                                           expr.Value(360)),
                                expr.Get('oper_cost', period='y')))


def acct_payable_ave_y():
    '''平均应付账款(年)'''
    return MetricsMeta('f_acct_payable_ave_y',
                       expr.Div(
                           expr.Sum(
                               expr.Get('acct_payable', period='y'),
                               expr.Before(expr.Get('acct_payable', period='y'), past_year=1)),
                           expr.Value(2)))


def net_operating_cycle():
    '''营销:净营业周期'''
    return MetricsMeta('f_net_op_cycle',
                       expr.Sub(expr.Sum(expr.Get('f_days_inventory_y'),
                                         expr.Get('f_days_accounts_receiv_y'),
                                         expr.Get('f_days_prepayment_y')),
                                expr.Get('f_days_acct_payable_y'),
                                expr.Get('f_days_adv_receipts_y')))


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


def current_y():
    ''' 流动比率 = 流动资产 / 流动负债 '''
    ''' 流动比率 (CR) 基准值=2 '''
    return MetricsMeta('f_current_y.r',
                       expr.Div(expr.Get('total_cur_assets', period='y'),
                                expr.Get('total_cur_liab', period='y')))


def metrics():
    metas = [
        accounts_receiv_q_y2y(),
        accounts_receiv_y_y2y(),
        inventories_q_y2y(),
        inventories_y_y2y(),
        current_y(),

        days_inventory_y(),
        inventroy_ave_y(),

        days_accounts_receiv_y(),
        accounts_receiv_ave_y(),

        days_prepayment_y(),
        prepayment_ave_y(),

        days_adv_receipts_y(),
        adv_receipts_ave_y(),

        days_acct_payable_y(),
        acct_payable_ave_y(),

        net_operating_cycle()
    ]
    return metas
