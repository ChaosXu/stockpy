from stockpy.metrics.base import MetricsMeta
from stockpy import expr


def revenue_q_y2y():
    # 季度营业收入增长(同比)
    return MetricsMeta('f_revenue_q.y2y',
                       expr.Sub(expr.Get('revenue'),
                                expr.Before(expr.Get('revenue'),
                                            past_quarter=4)))


def revenue_q_r_y2y():
    # 季度营业收入增长率((同比)
    return MetricsMeta('f_revenue_q.r_y2y',
                       expr.Div(
                           expr.Sub(expr.Get('revenue'),
                                    expr.Before(
                                        expr.Get('revenue'), past_quarter=4)),
                           expr.Before(expr.Get('revenue'),
                                       past_quarter=4)))


def revenue_y_y2y():
    # 年度营业收入增长(同比)
    return MetricsMeta('f_revenue_y.y2y',
                       expr.Sub(expr.Get('revenue', period='y'),
                                expr.Before(expr.Get('revenue', period='y'),
                                            past_year=1)))


def revenue_y_r_y2y():
    # 年度营业收入增长率((同比)
    return MetricsMeta('f_revenue_y.r_y2y',
                       expr.Div(
                           expr.Sub(expr.Get('revenue', period='y'),
                                    expr.Before(expr.Get('revenue', period='y'),
                                                past_year=1)),
                           expr.Before(expr.Get('revenue', period='y'),
                                       past_year=1)))


def income_attr_p_q_y2y():
    # 季度净利润增长(同比)
    return MetricsMeta('f_income_attr_p_q.y2y',
                       expr.Sub(expr.Get('n_income_attr_p'),
                                expr.Before(expr.Get('n_income_attr_p'),
                                            past_quarter=4)))


def income_attr_p_q_r_y2y():
    # 季度净利润增长率(同比)
    return MetricsMeta('f_income_attr_p_q.r_y2y',
                       expr.Div(
                           expr.Sub(expr.Get('n_income_attr_p'),
                                    expr.Before(expr.Get('n_income_attr_p'),
                                                past_quarter=4)),
                           expr.Before(expr.Get('n_income_attr_p'),
                                       past_quarter=4)))


def income_attr_p_y_y2y():
    # 年度净利润增长(同比)
    return MetricsMeta('f_income_attr_p_y.y2y',
                       expr.Sub(expr.Get('n_income_attr_p', period='y'),
                                expr.Before(expr.Get('n_income_attr_p',
                                                     period='y'),
                                            past_year=1)))


def income_attr_p_y_r_y2y():
    # 年度净利润增长率(同比)
    return MetricsMeta('f_income_attr_p_y.r_y2y',
                       expr.Div(
                           expr.Sub(expr.Get('n_income_attr_p', period='y'),
                                    expr.Before(expr.Get('n_income_attr_p',
                                                         period='y'),
                                                past_year=1)),
                           expr.Before(expr.Get('n_income_attr_p', period='y'),
                                       past_year=1)))


def income_attr_p_ttm():
    # 滚动净利润：最近连续4个季度
    ttm_q3 = [expr.Before(expr.Get('n_income_attr_p', increment=True),
                          past_quarter=i)
              for i in range(1, 4)]
    return MetricsMeta('f_income_attr_p_ttm',
                       expr.Sum(expr.Get('n_income_attr_p',
                                         increment=True,
                                         var_type='f'),
                                ttm_q3))


def metrics():
    metas = [
        revenue_q_y2y(),
        revenue_q_r_y2y(),
        revenue_y_y2y(),
        revenue_y_r_y2y(),

        income_attr_p_q_y2y(),
        income_attr_p_q_r_y2y(),
        income_attr_p_y_y2y(),
        income_attr_p_y_r_y2y(),

        income_attr_p_ttm()
    ]
    return metas
