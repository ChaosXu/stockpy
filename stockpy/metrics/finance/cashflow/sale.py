from stockpy.metrics.base import MetricsMeta
from stockpy import expr


def sale_cash_ratio():
    '''营销:销售收现率'''
    return MetricsMeta('f_sale_cash.r',
                       expr.Div(expr.Get('c_fr_sale_sg'),
                                expr.Get('revenue')))


def sale_credit_ratio():
    '''营销:赊销率(白条率)'''
    return MetricsMeta('f_sale_credit.r',
                       expr.Div(expr.Get('f_receivables'),
                                expr.Get('revenue')))


def receivables():
    '''营销:应收款项 = 应收票据 + 应收账款'''
    return MetricsMeta('f_receivables',
                       expr.Sum(expr.Get('notes_receiv'),
                                expr.Get('accounts_receiv')))


def adv_receipt_ratio():
    '''营销:预收率'''
    return MetricsMeta('f_adv_receipt.r',
                       expr.Sub(expr.Get('adv_receipts'),
                                expr.Get('revenue')))


def metrics():
    metas = [
        sale_cash_ratio(),
        sale_credit_ratio(),
        receivables(),
        adv_receipt_ratio()
    ]
    return metas
