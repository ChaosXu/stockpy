from stockpy.metrics.base import MetricsMeta
from stockpy import expr


def sale_cash_ratio():
    '''营销:销售收现率%'''
    return MetricsMeta(
        'f_sale_cash.r',
        expr.Div(expr.Get('c_fr_sale_sg'),
                 expr.Get('revenue')),
        display='销售收现率')


def sale_cash_y_ratio():
    '''营销:销售收现率%'''
    return MetricsMeta('f_sale_cash_y.r',
                       expr.Get('f_sale_cash.r', period='y'),
                       display='销售收现率')


def sale_credit_ratio():
    '''营销:赊销率(白条率)'''
    return MetricsMeta(
        'f_sale_credit.r',
        expr.Div(expr.Get('f_receivables'),
                 expr.Get('revenue')),
        display='赊销率')


def sale_credit_y_ratio():
    '''营销:赊销率(白条率)'''
    return MetricsMeta(
        'f_sale_credit_y.r',
        expr.Get('f_sale_credit.r', period='y'),
        display='赊销率')


def receivables():
    '''营销:应收款项 = 应收票据 + 应收账款'''
    return MetricsMeta('f_receivables',
                       expr.Sum(expr.Get('notes_receiv'),
                                expr.Get('accounts_receiv')))


def adv_receipt_ratio():
    '''营销:预收率%'''
    return MetricsMeta(
        'f_adv_receipt.r',
        expr.Div(expr.Get('adv_receipts'),
                 expr.Get('revenue')),
        display='预收率')


def adv_receipt_y_ratio():
    '''营销:预收率%'''
    return MetricsMeta('f_adv_receipt_y.r',
                       expr.Get('f_adv_receipt.r', period='y'),
                       display='预收率')


def metrics():
    metas = [
        sale_cash_ratio(),
        sale_cash_y_ratio(),
        sale_credit_ratio(),
        sale_credit_y_ratio(),
        receivables(),
        adv_receipt_ratio(),
        adv_receipt_y_ratio()
    ]
    return metas
