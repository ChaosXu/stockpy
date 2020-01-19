from stockpy.meta import MetricsMeta
from stockpy import expr


def market_cap():
    ''' 估算总市值
    '''
    return MetricsMeta('e_market_cap.goose',
                       expr.Multi(expr.Get('total_hldr_eqy_exc_min_int'),
                                  expr.Sum(expr.Value(1),
                                           expr.Get('f_roe_ttm'))))


def moat_factor():
    ''' 护城河等级系数
    '''
    return 1


def safety_factor():
    '''安全边际系数
        50%到90%
    '''
    return 1


def price_share():
    '''估算单价'''
    return MetricsMeta('e_price_share.goose',
                       expr.Div(expr.Get('e_market_cap.goose'),
                                expr.Get('total_share')))


def metrics():
    metas = [
        market_cap(),
        price()
    ]
    return metas
