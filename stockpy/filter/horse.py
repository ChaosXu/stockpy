from stockpy.model.stock import Stocks
from stockpy import expr


def last_year_f_revenue_y_r_y2y():
    return expr.Before(expr.Get('f_revenue_y.r_y2y'), past_year=1)


def last_quarter_f_revenue_q_r_y2y():
    return expr.Get('f_revenue_q.r_y2y')


def last_year_f_income_attr_p_y_r_y2y():
    return expr.Get('f_income_attr_p_y.r_y2y')


def last_quarter_f_income_attr_p_q_r_y2y():
    return expr.Get('f_income_attr_p_q.r_y2y')


def roe_ge_15_pct_last_7_year():
    return expr.And(
        roe_ge_15_pct_before_6_years(),
        roe_ge_15_pct_now()
    )


def roe_ge_15_pct_before_6_years():
    return expr.Ge(
        expr.Range(expr.Before(expr.Get('f_roe_y'), past_year=1),
                   year_count=6),
        expr.Value(0.15)
    )


def roe_ge_15_pct_now():
    def fv(stock: expr.ExprCtx, year: int, quarter: int):
        v = {
            4: 0.15,
            3: 0.15/4*3,
            2: 0.15/4*2,
            1: 0.15/4,
        }
        return v[quarter]

    return expr.Ge(
        expr.Get('f_roe'),
        expr.FuncValue(fv)
    )


def revenue_r_gt_0():
    return expr.And(
        expr.Gt(last_year_f_revenue_y_r_y2y(),
                expr.Value(0)),
        expr.Gt(last_quarter_f_revenue_q_r_y2y(),
                expr.Value(0))
    )


def income_attr_p_r_gt_0():
    return expr.And(
        expr.Gt(last_year_f_income_attr_p_y_r_y2y(),
                expr.Value(0)),
        expr.Gt(last_quarter_f_income_attr_p_q_r_y2y(),
                expr.Value(0))
    )


def revenue_y_gt_accounts_receive_3_years():
    return expr.Or(
        expr.And(
            expr.Gt(
                expr.Get('f_revenue_y.y2y'),
                expr.Get('f_accounts_receiv_y.y2y')),
            expr.Gt(
                expr.Before(expr.Get('f_revenue_y.y2y'),
                            past_year=1),
                expr.Before(expr.Get('f_accounts_receiv_y.y2y'),
                            past_year=1))),
        expr.And(
            expr.Gt(
                expr.Before(expr.Get('f_revenue_y.y2y'),
                            past_year=1),
                expr.Before(expr.Get('f_accounts_receiv_y.y2y'),
                            past_year=1)),
            expr.Gt(
                expr.Before(expr.Get('f_revenue_y.y2y'),
                            past_year=2),
                expr.Before(expr.Get('f_accounts_receiv_y.y2y'),
                            past_year=2))),
        expr.And(
            expr.Gt(
                expr.Before(expr.Get('f_revenue_y.y2y'),
                            past_year=2),
                expr.Before(expr.Get('f_accounts_receiv_y.y2y'),
                            past_year=2)),
            expr.Gt(
                expr.Before(expr.Get('f_revenue_y.y2y'),
                            past_year=3),
                expr.Before(expr.Get('f_accounts_receiv_y.y2y'),
                            past_year=3))))


def revenue_y_gt_inventoires_3_years():
    return expr.Or(
        expr.And(
            expr.Gt(
                expr.Get('f_revenue_y.y2y'),
                expr.Get('f_inventories_y.y2y')),
            expr.Gt(
                expr.Before(expr.Get('f_revenue_y.y2y'),
                            past_year=1),
                expr.Before(expr.Get('f_inventories_y.y2y'),
                            past_year=1))),
        expr.And(
            expr.Gt(
                expr.Before(expr.Get('f_revenue_y.y2y'),
                            past_year=1),
                expr.Before(expr.Get('f_inventories_y.y2y'),
                            past_year=1)),
            expr.Gt(
                expr.Before(expr.Get('f_revenue_y.y2y'),
                            past_year=2),
                expr.Before(expr.Get('f_inventories_y.y2y'),
                            past_year=2))),
        expr.And(
            expr.Gt(
                expr.Before(expr.Get('f_revenue_y.y2y'),
                            past_year=2),
                expr.Before(expr.Get('f_inventories_y.y2y'),
                            past_year=2)),
            expr.Gt(
                expr.Before(expr.Get('f_revenue_y.y2y'),
                            past_year=3),
                expr.Before(expr.Get('f_inventories_y.y2y'),
                            past_year=3))))


def current_y_gt_1_3_years():
    return expr.Or(
        expr.And(
            expr.Gt(
                expr.Get('f_current_y.r'),
                expr.Value(1)),
            expr.Gt(
                expr.Before(expr.Get('f_current_y.r'), past_year=1),
                expr.Value(1))),
        expr.And(
            expr.Gt(
                expr.Before(expr.Get('f_current_y.r'), past_year=1),
                expr.Value(1)),
            expr.Gt(
                expr.Before(expr.Get('f_current_y.r'), past_year=2),
                expr.Value(1))),
        expr.And(
            expr.Gt(
                expr.Before(expr.Get('f_current_y.r'), past_year=2),
                expr.Value(1)),
            expr.Gt(
                expr.Before(expr.Get('f_current_y.r'), past_year=3),
                expr.Value(1))))


# def pe_quantile():
#     pass


# def pb_quantile():
#     pass

def horseFilter():
    return expr.Name('f:horse_filter', expr.And(
        expr.Name('f:roe_ge_15_pct_last_7_year', roe_ge_15_pct_last_7_year()),
        expr.Name('f:revenue_r_gt_0', revenue_r_gt_0()),
        expr.Name('f:income_attr_p_r_gt_0', income_attr_p_r_gt_0()),
        expr.Name('f:revenue_y_gt_accounts_receive_3_years',
                  revenue_y_gt_accounts_receive_3_years()),
        expr.Name('f:revenue_y_gt_inventoires_3_years',
                  revenue_y_gt_inventoires_3_years()),
        expr.Name('f:current_y_gt_1_3_years', current_y_gt_1_3_years())
    ))
