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
    '''应收账款周转天数(年)'''
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
    '''预付账款周转天数(年)'''
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
    '''预收账款周转天数(年)'''
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
    '''应付账款周转天数(年)'''
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
    '''营销:净营业周期(年)'''
    return MetricsMeta('f_net_op_cycle_y',
                       expr.Sub(expr.Sum(expr.Get('f_days_inventory_y'),
                                         expr.Get('f_days_accounts_receiv_y'),
                                         expr.Get('f_days_prepayment_y')),
                                expr.Get('f_days_acct_payable_y'),
                                expr.Get('f_days_adv_receipts_y')))


def metrics():
    metas = [
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
