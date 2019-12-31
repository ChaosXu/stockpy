from stockpy.metrics.base import MetricsMeta
from stockpy import expr


def metrics():
    metas = [
        # 季度应收账款增长(同比)
        MetricsMeta('f_accounts_receiv_q.y2y',
                    expr.Sub(expr.Get('accounts_receiv'),
                             expr.Before(expr.Get('accounts_receiv'),
                                         past_quarter=4))),
        # 年度应收账款增长(同比)
        MetricsMeta('f_accounts_receiv_y.y2y',
                    expr.Sub(expr.Get('accounts_receiv'),
                             expr.Before(expr.Get('accounts_receiv'),
                                         past_year=1))),
        # 季度存货增长
        MetricsMeta('f_inventories_q.y2y',
                    expr.Sub(expr.Get('inventories'),
                             expr.Before(expr.Get('inventories'),
                                         past_quarter=4))),
        # 年度存货增长
        MetricsMeta('f_inventories_y.y2y',
                    expr.Sub(expr.Get('inventories'),
                             expr.Before(expr.Get('inventories'),
                                         past_year=1))),

        # 流动比率 = 流动资产 / 流动负债
        # 流动比率 (CR) 基准值=2
        MetricsMeta('f_current_y.r',
                    expr.Div(expr.Get('total_cur_assets'),
                             expr.Get('total_cur_liab')))
    ]
    return metas
