from stockpy.model.stock import Stocks
from stockpy import expr


def roe_ge_15_pct_last_3_years():
    pass


def gooseFilter():
    return expr.And(
        roe_ge_15_pct_last_3_years()
    )
