from stockpy.meta import MetricsMeta
from stockpy.expr.value import Value
from stockpy.expr.arithmetic import Sum
from stockpy.expr.arithmetic import Div
from stockpy.expr.arithmetic import Sub
from stockpy.expr.range import Range
from stockpy.expr.get import Get

def metrics():
    '''inventoris'''
    # TBD: 计算周期
    # 存货周转率 = 营业成本 /（（期初存货+期末存货）/2）
    inv_turnover_ratio = Div(Get('oper_cost'),
                             Div(Sum(Get('inventories',), Get('inventories')),
                                 Value(2)))
    metas = [
        # 存货周转天数=360/存货周转率
        MetricsMeta('f_inv_to_days',
                    Div(Value(360), inv_turnover_ratio)),

        # 总资产 = 流动资产合计 + 非流动资产合计
        MetricsMeta('f_total_assets',
                    Sum(Get('total_nca'), Get('total_cur_assets')))
    ]
    return metas
