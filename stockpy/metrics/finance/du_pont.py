from stockpy.meta import MetricsMeta
from stockpy.expr.value import Value
from stockpy.expr.arithmetic import Sum
from stockpy.expr.arithmetic import Div
from stockpy.expr.arithmetic import Sub
from stockpy.expr.range import Range
from stockpy.expr.get import Get


def metrics():
    '''du pont analysis'''

    metas = [
        # ROE
        # =净利润/净资产
        # =归母净利润/（期初+期末归母净资产）/2
        # =每股净利润/每股净资产
        # =销售净利率*总资产周转率*杠杆系数
        # MetricsMeta('roe',
        #             Div(Get('净利润'), Get('净资产'))),

        # 销售净利率=（毛利率-三费-所得税）/营业收入=毛利率-三费占比-所得税占比
        MetricsMeta('f_net_profit.r',
                    Sub(Get('f_gross_profit.r'), Get('三费占比'), Get('所得税占比'))),
        # 毛利率 = 1 - 营业成本 / 营业收入
        MetricsMeta('f_gross_profit.r',
                    Sub(Value(1), Div(Get('revenue'), Get('oper_cost')))),

        # 三费占比=(销售费用+管理费用+财务费用+研发费用,2018年起增加研发费用)/营业收入
        MetricsMeta('f_3_exp.r',
                    Div(Sum(Get('sell_exp'), Get('admin_exp'), Get('fin_exp')),
                        Get('revenue'))),

        # 总资产周转率=营业收入/总资产
        MetricsMeta('f_total_assets_tunrover.r',
                    Div(Get('revenue'), Get('f_total_assets'))),
        # 杠杆倍数
        # =资产/所有者权益=资产/（资产-负债）
        # =1/（1-资产负债率）
        MetricsMeta('f_leverage',
                    Div(Get('f_total_assets'), Get('total_hldr_eqy_exc_min_int'))),

        # 资产负债率 = 负债合计 / 总资产 (＞50%需小心，同行比较，越高风险越大)
        MetricsMeta('f_liab_assets.r',
                    Div(Get('total_liab'), Get('f_total_assets'))),

        # 有息负债率 = 有息负债 / 总资产
        # 同行比较，越高风险越大
        MetricsMeta('f_interest_bearing_debt.r',
                    Div(Get('f_interest_bearing'), Get('f_total_assets'))),

        # 有息负债 = 短期借款 + 1年内到期的长期负债 + 长期借款 + 应付债券 + 长期应付款
        MetricsMeta('f_interest_bearing_debt',
                    Sum(Get('lt_borr'), Get('st_borr'), Get('bond_payable'), Get('lt_payable'), Get('non_cur_liab_due_1y'))),

        # 流动比率 = 流动资产 / 流动负债
        # 流动比率 (CR) 基准值=2
        MetricsMeta('f_current.r',
                    Div(Get('total_cur_assets'), Get('total_cur_liab'))),

        # 速动比率 = 速动资产 / 流动负债
        # 速动资产 = 流动资产 - 存货
        # 速动比率 (QR) 基准值=1
        MetricsMeta('f_quick.r',
                    Div(Sub(Get('total_cur_assets'), Get('inventories')), Get('total_cur_liab')))

    ]
    return metas
