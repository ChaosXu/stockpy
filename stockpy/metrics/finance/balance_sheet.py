from stockpy.metrics.base import MetricsMeta
from stockpy import expr


def metrics():
    metas = [
        # 应收账款增长
        MetricsMeta('f_accounts_receiv.y2y',
                    expr.Sub(expr.Get('accounts_receiv'),
                             expr.Before(expr.Get('accounts_receiv'),
                                         past_quarter=4))),
        # 存货增长
        MetricsMeta('f_inventories.y2y',
                    expr.Sub(expr.Get('inventories'),
                             expr.Before(expr.Get('inventories'),
                                         past_quarter=4)))
    ]
    return metas
