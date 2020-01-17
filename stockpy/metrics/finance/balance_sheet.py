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
        current_y()
    ]
    return metas
