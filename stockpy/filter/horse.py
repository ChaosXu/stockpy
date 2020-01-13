from stockpy.model.stock import Stocks
from stockpy import expr


def last_year_f_revenue_y_r_y2y():
    return expr.Before(expr.Get('f_revenue_y.r_y2y'), past_year=1)


def last_quarter_f_revenue_q_r_y2y():
    return expr.Get('f_revenue_q.r_y2y')


def last_year_f_income_attr_p_y_r_y2y():
    return expr.Before(expr.Get('f_income_attr_p_y.r_y2y'), past_year=1)


def last_quarter_f_income_attr_p_q_r_y2y():
    return expr.Get('f_income_attr_p_q.r_y2y')


def horseFilter():
    return expr.And(
        # roe(),
        revenue_gt_0(),
        income_attr_p_gt_0()
        # bear1(),
        # bear2(),
        # bear3()
    )


def roe_ge_15_pct_last_7_year():
    return expr.Ge(
        expr.Range(expr.Get('f_roe'), 6*4),
        expr.Value(0.15)
    )


def revenue_gt_0():
    return expr.And(
        expr.Gt(last_year_f_revenue_y_r_y2y(),
                expr.Value(0)),
        expr.Gt(last_quarter_f_revenue_q_r_y2y(),
                expr.Value(0))
    )


def income_attr_p_gt_0():
    return expr.And(
        expr.Gt(last_year_f_income_attr_p_y_r_y2y(),
                expr.Value(0)),
        expr.Gt(last_quarter_f_income_attr_p_q_r_y2y(),
                expr.Value(0))
    )


def bear1_accounts_receive():
    return expr.And(
        expr.Gt(
            expr.Before(expr.Get('f_revenue_y.y2y'), past_year=1),
            expr.Before(expr.Get('f_accounts_receiv_y.y2y')), past_year=1),
        expr.Gt(
            expr.Before(expr.Get('f_revenue_y.y2y'), past_year=2),
            expr.Before(expr.Get('f_accounts_receiv_y.y2y')), past_year=2)
    )


def bear2_inventories():
    return expr.And(
        expr.Gt(
            expr.Before(expr.Get('f_revenue_y.y2y'), past_year=1),
            expr.Before(expr.Get('f_inventories_y.y2y')), past_year=1),
        expr.Gt(
            expr.Before(expr.Get('f_revenue_y.y2y'), past_year=2),
            expr.Before(expr.Get('f_inventories_y.y2y')), past_year=2)
    )

# def bear3():
#     pass


# def pe_quantile():
#     pass


# def pb_quantile():
#     pass


class Horse:

    filter = horseFilter()

    def perform(self, stocks: Stocks, year: int, quarter: int):
        filter = self.filter
        return stocks.queryByMetrics(year, quarter, filter)
