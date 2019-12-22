from stockpy.meta import MetricsMeta
from stockpy.expr.value import Value
from stockpy.expr.arithmetic import Sum
from stockpy.expr.arithmetic import Div
from stockpy.expr.arithmetic import Sub
from stockpy.expr.range import Range
from stockpy.expr.get import Get


def metrics():
    '''net operating cycle'''

    metas = [
        # 净营业周期=存货周转天数+应收账款周转天数+预付账款周转天数-应付账款周转天数-预收账款周转天数
        # 存货周转天数
        # 应收账款周转天数
        # 预付账款周转天数
        # 应付账款周转天数
        # 预收账款周转天数
        # MetricsMeta("净营业周期",
        #             Sub(Sum(Get('f_inv_to_days'), Get('应收账款周转天数'), Get('预付账款周转天数')),
        #                 Get('应付账款周转天数'), Get('预收账款周转天数'))),

        # 销售收现率=销售产品劳务获得的现金/营业收入
        MetricsMeta('f_c_fr_sale_sg.r',
                    Div(Get('c_fr_sale_sg'), Get('revenue'))),

        # 白条率=应收款项/营业收入
        MetricsMeta('f_acc_receivable.r',
                    Div(Get('acc_receivable'), Get('revenue'))),
        # 预收率=预收款项/营业收入
        MetricsMeta('f_adv_receipts.r',
                    Div(Get('adv_receipts'), Get('revenue')))

    ]
    return metas
