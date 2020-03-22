from stockpy.metrics.base import (MetricsMeta,
                                  metrics_def,
                                  metrics_ratio,
                                  metrics_y,
                                  expr_for_list,
                                  expr_div_ave_y,
                                  expr_div_ave)
from stockpy import expr


def assets_liab_ratio_y():
    ''' 资产负债率
        ＞50%需小心
        同行比较，越高风险越大
    '''
    return MetricsMeta('f_assets_liab_y.r',
                       expr.Div(expr.Get('total_liab', period='y'),
                                expr.Get('f_total_assets_y')))


def interest_bearing_liab_y():
    ''' 有息负债
        = 短期借款 + 1年内到期的长期负债 + 长期借款 + 应付债券 + 长期应付款
    '''
    return MetricsMeta(
        'f_interest_bearing_liab_y',
        expr.Sum(
            expr.Get('lt_borr', period='y'),
            expr.Get('st_borr', period='y'),
            expr.Get('bond_payable', period='y'),
            expr.Get('lt_payable', period='y'),
            expr.Get('non_cur_liab_due_1y', period='y')))


def interest_bearing_liab():
    ''' 有息负债
        = 短期借款 + 1年内到期的长期负债 + 长期借款 + 应付债券 + 长期应付款
    '''
    return MetricsMeta(
        'f_interest_bearing_liab',
        expr.Sum(
            expr.Get('lt_borr'),
            expr.Get('st_borr'),
            expr.Get('bond_payable'),
            expr.Get('lt_payable'),
            expr.Get('non_cur_liab_due_1y')))


def interest_bearing_liab_ratio():
    ''' 有息负债率 = 有息负债 / 总资产
        同行比较，越高风险越大
    '''
    return MetricsMeta(
        'f_interest_bearing_liab.r',
        expr.Div(expr.Get('f_interest_bearing_liab'),
                 expr.Get('f_total_assets')),
        display='有息负债率')


def interest_bearing_liab_ratio_y():
    ''' 有息负债率 = 有息负债 / 总资产
        同行比较，越高风险越大
    '''
    return MetricsMeta(
        'f_interest_bearing_liab_y.r',
        expr.Div(expr.Get('f_interest_bearing_liab_y'),
                 expr.Get('f_total_assets_y')),
        display='有息负债率')


def metrics():
    metas = [
        assets_liab_ratio_y(),
        interest_bearing_liab(),
        interest_bearing_liab_y(),
        interest_bearing_liab_ratio(),
        interest_bearing_liab_ratio_y(),
        metrics_def('f_debt_assets_y.r', expr_for_list(
            expr.Div, 'total_liab_y', 'total_assets_y'),
            '资产负债率'),
        metrics_def('f_debt_assets.r', expr_for_list(
            expr.Div, 'total_liab', 'total_assets'),
            '资产负债率'),
        metrics_def('f_fix_assets_tunrover_y.r',
                    expr_div_ave_y('revenue',
                                   'fix_assets_y'),
                    '固定资产周转率'),
        metrics_def('f_fix_assets_tunrover.r',
                    expr_div_ave('revenue',
                                 'fix_assets', past_quarter=4),
                    '固定资产周转率'),

        metrics_def('f_total_cur_assets_tunrover_y.r',
                    expr_div_ave_y('revenue',
                                   'total_cur_assets_y'),
                    '流动资产周转率'),
        metrics_def('f_total_cur_assets_tunrover.r',
                    expr_div_ave('revenue',
                                 'total_cur_assets', past_quarter=4),
                    '流动资产周转率'),

        metrics_def('f_total_assets_tunrover_y.r',
                    expr_div_ave_y('revenue',
                                   'f_total_assets_y'),
                    '总资产周转率(次)'),
        metrics_def('f_total_assets_tunrover.r',
                    expr_div_ave('revenue',
                                 'f_total_assets', past_quarter=4),
                    '总资产周转率(次)'),

        metrics_def('f_roe_y',
                    expr_div_ave_y('n_income_attr_p',
                                   'total_hldr_eqy_exc_min_int'),
                    'ROE'),
        metrics_def('f_roa_y',
                    expr_div_ave_y('n_income_attr_p',
                                   'total_assets'),
                    'ROA'),

        metrics_ratio('f_current', 'total_cur_assets', 'total_cur_liab',
                      '流动比'),
        metrics_ratio('f_current', 'total_cur_assets', 'total_cur_liab',
                      '流动比', period='y'),
        metrics_def('f_quick', expr_for_list(expr.Div,
                                             'total_cur_assets',
                                             'inventories',
                                             'prepayment'),
                    '速动资产'),
        metrics_y('f_quick', '速动资产'),
        metrics_ratio('f_quick', 'f_quick', 'total_cur_liab', '速动比'),
        metrics_ratio('f_quick', 'f_quick',
                      'total_cur_liab', '速动比', period='y'),
    ]
    return metas
