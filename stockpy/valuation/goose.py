from stockpy import expr


def market_cap(base: int, moat: int):
    ''' 估算总市值
        = 净资产 * (1+滚动roe) ^ (基本因子+护城河因子+成长因子)
    '''
    return expr.Multi(expr.Get('total_hldr_eqy_exc_min_int'),
                      expr.Power(expr.Sum(expr.Value(1),
                                          expr.Get('f_roe_ttm')),
                                 expr.Sum(base_factor(base),
                                          moat_factor(moat),
                                          growth_factor())))


def market_cap_moat_n1():
    return market_cap(7, -1)


def market_cap_moat_0():
    return market_cap(7, 0)


def market_cap_moat_p1():
    return market_cap(7, 1)


def market_cap_moat_p2():
    return market_cap(7, 2)


def base_factor(c: int):
    ''' 基本因子
    '''
    return expr.Value(c)


def moat_factor(c: int):
    ''' 护城河等级系数
        -1 负
        0  无
        1  弱
        2  强
    '''
    return expr.Value(c)


def growth_factor():
    ''' 成长等级系数,最近5年同比增长率
        -1 负增长, 净利润同比 < 5%
        1  慢速增长, 5 <= 净利润同比 <= 20%
        2  快速增长，净利润同比 > 20%
    '''
    income_attr_p_y = expr.Range(
        expr.Get('f_income_attr_p_y.r_y2y'), year_count=5)
    return expr.Switch(
        expr.Case(
            expr.Gt(income_attr_p_y, expr.Value(0.2)),
            expr.Value(2)),
        expr.Case(
            expr.Ge(income_attr_p_y, expr.Value(0.05)),
            expr.Value(1)),
        expr.Case(
            expr.Le(income_attr_p_y, expr.Value(0.05)),
            expr.Value(-1)),
        default=expr.Value(0))


def safety_factor():
    '''安全边际系数
        50%到90%
    '''
    return expr.Value(0.9)


def premium_rate():
    '''溢价率'''
    return expr.Value(1)


def price_share(market_cap: expr.Expr):
    '''估算单价'''
    return expr.Div(market_cap,
                    expr.Get('total_share'))


def price_buying(price_share: expr.Expr):
    '''买入价'''
    return expr.Multi(price_share,
                      safety_factor())


def price_selling(price_share: expr.Expr):
    '''卖出价'''
    return expr.Multi(price_share,
                      premium_rate())


def metrics():
    metas = [
    ]
    return metas
