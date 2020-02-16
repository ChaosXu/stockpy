from stockpy.metrics.base import (MetricsMeta,
                                  expr_for_list,
                                  metrics_ratio,
                                  metrics_def,
                                  metrics_y,
                                  metrics_y_y2y,
                                  metrics_y_r_y2y,
                                  metrics_r_y2y)
from stockpy import expr


# def revenue_q_y2y():
#     # 季度营业收入增长(同比)
#     return MetricsMeta('f_revenue_q.y2y',
#                        expr.Sub(expr.Get('revenue'),
#                                 expr.Before(expr.Get('revenue'),
#                                             past_quarter=4)))


# def revenue_q_r_y2y():
#     # 季度营业收入增长率%(同比)
#     return MetricsMeta('f_revenue_q.r_y2y',
#                        expr.Div(
#                            expr.Sub(expr.Get('revenue'),
#                                     expr.Before(
#                                         expr.Get('revenue'), past_quarter=4)),
#                            expr.Before(expr.Get('revenue'),
#                                        past_quarter=4)))


# def revenue_y_y2y():
#     # 年度营业收入增长(同比)
#     return MetricsMeta('f_revenue_y.y2y',
#                        expr.Sub(expr.Get('revenue', period='y'),
#                                 expr.Before(expr.Get('revenue', period='y'),
#                                             past_year=1)),
#                        display='年度营业收入增长(同比)')


# def revenue_y():
#     # 年度营业收入
#     return MetricsMeta('f_revenue_y', expr.Get('revenue', period='y'),
#                        display='营业收入')


# def gross_profit():
#     '''毛利润'''
#     return MetricsMeta('f_gross_profit',
#                        expr.Sub(expr.Get('revenue'), expr.Get('oper_cost')),
#                        display='毛利润')


# def gross_profit_y():
#     '''毛利润'''
#     return MetricsMeta('f_gross_profit_y',
#                        expr.Get('f_gross_profit', period='y'),
#                        display='毛利润')


# def gross_profit_y_r_y2y():
#     '''毛利润'''
#     return MetricsMeta('f_gross_profit_y.r_y2y',
#                        expr.Div(expr.Get('f_gross_profit_y'),
#                                 expr.Sub(expr.Get('f_gross_profit_y'),
#                                          expr.Before(
#                                              expr.Get('f_gross_profit_y'),
#                                              past_year=1))),
#                        display='毛利润增长率')


# def income_attr_p_y():
#     # 年度净利润
#     return MetricsMeta('f_income_attr_p_y', expr.Get('n_income_attr_p', period='y'),
#                        display='净利润')


# def revenue_y_r_y2y():
#     # 年度营业收入增长
#     return MetricsMeta(
#         'f_revenue_y.r_y2y',
#         expr.Div(
#             expr.Sub(expr.Get('revenue', period='y'),
#                      expr.Before(expr.Get('revenue', period='y'),
#                                  past_year=1)),
#             expr.Before(expr.Get('revenue', period='y'),
#                         past_year=1)),
#         display='营业收入增长率')


# def income_attr_p_q_y2y():
#     # 季度净利润增长(同比)
#     return MetricsMeta('f_income_attr_p_q.y2y',
#                        expr.Sub(expr.Get('n_income_attr_p'),
#                                 expr.Before(expr.Get('n_income_attr_p'),
#                                             past_quarter=4)))


# def income_attr_p_q_r_y2y():
#     # 季度净利润增长率%同比)
#     return MetricsMeta('f_income_attr_p_q.r_y2y',
#                        expr.Div(
#                            expr.Sub(expr.Get('n_income_attr_p'),
#                                     expr.Before(expr.Get('n_income_attr_p'),
#                                                 past_quarter=4)),
#                            expr.Before(expr.Get('n_income_attr_p'),
#                                        past_quarter=4)))


# def income_attr_p_y_y2y():
#     # 年度净利润增长(同比)
#     return MetricsMeta('f_income_attr_p_y.y2y',
#                        expr.Sub(expr.Get('n_income_attr_p', period='y'),
#                                 expr.Before(expr.Get('n_income_attr_p',
#                                                      period='y'),
#                                             past_year=1)),
#                        display='净利润增长(同比)')


# def income_attr_p_y_r_y2y():
#     # 年度净利润增长率%同比)
#     return MetricsMeta(
#         'f_income_attr_p_y.r_y2y',
#         expr.Div(
#             expr.Sub(expr.Get('n_income_attr_p', period='y'),
#                      expr.Before(expr.Get('n_income_attr_p',
#                                           period='y'),
#                                  past_year=1)),
#             expr.Before(expr.Get('n_income_attr_p', period='y'),
#                         past_year=1)),
#         display='净利润增长率')


def income_attr_p_ttm():
    # 滚动净利润：最近连续4个季度
    ttm_q3 = [expr.Before(expr.Get('n_income_attr_p',
                                   increment=True,
                                   var_type='f'),
                          past_quarter=i)
              for i in range(1, 4)]
    return MetricsMeta('f_income_attr_p_ttm',
                       expr.Sum(expr.Get('n_income_attr_p',
                                         increment=True,
                                         var_type='f'),
                                ttm_q3))


def metrics():
    metas = [
        income_attr_p_ttm(),

        metrics_def('f_gross_profit',
                    expr_for_list(expr.Sub, 'revenue', 'oper_cost'), '毛利润'),
        metrics_y('f_gross_profit', '毛利润'),
        metrics_y_y2y('f_gross_profit', '毛利润'),
        metrics_y_r_y2y('f_gross_profit', '毛利润增长率'),

        metrics_ratio('f_oper_cost',
                      'oper_cost', 'revenue', '成本率', period='y'),
        metrics_ratio('f_oper_cost',
                      'oper_cost', 'revenue', '成本率'),

        metrics_ratio('f_sale_net_profit',
                      'n_income_attr_p', 'revenue', '销售净利率', period='y'),
        metrics_ratio('f_sale_net_profit',
                      'n_income_attr_p', 'revenue', '销售净利率'),

        # gross_profit_y_r_y2y()
    ]
    return metas
