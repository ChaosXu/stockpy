from stockpy.metrics.base import MetricsMeta
from stockpy import expr


def metrics():
    metas = [
        # 年度ROE(平均)
        # =净利润/净资产
        # =归母净利润/（期初+期末归母净资产）/2
        # =每股净利润/每股净资产
        # =销售净利率*总资产周转率*杠杆系数
        MetricsMeta('f_roe_y',
                    expr.Div(
                        expr.Get('n_income_attr_p',
                                 period='y'),
                        expr.Div(
                            expr.Sum(
                                expr.Get('total_hldr_eqy_exc_min_int',
                                         period='y'),
                                expr.Before(
                                    expr.Get('total_hldr_eqy_exc_min_int',
                                             period='y'),
                                    past_year=1)),
                            expr.Value(2))))

        # 年度ROE(加权平均)
        # 根据中国证监会发布的《公开发行证券公司信息披露编报规则》第9号的通知的规定：加权平均净资产收益率(ROE)的计算公式如下：ROE= P/（E0 + NP÷2 + Ei×Mi÷M0 - Ej×Mj÷M0）
        # 其中：
        # P为报告期利润；
        # NP为报告期净利润；
        # E0为期初净资产；
        # Ei为报告期发行新股或债转股等新增净资产；
        # Ej为报告期回购或现金分红等减少净资产；
        # M0为报告期月份数；
        # Mi为新增净资产下一月份起至报告期期末的月份数；
        # Mj为减少净资产下一月份起至报告期期末的月份数。

    ]
    return metas
