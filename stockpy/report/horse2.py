from stockpy.model.stock import Stock
from stockpy.report.base import ReportBase


class Report(ReportBase):

    def __init__(self, stock: Stock):
        ReportBase.__init__(self, stock)

    def _get_metrics(self):
        return [
            {
                'metrics': 'f_roe_ttm',
                'years': 10,
                'group': ('盈利分析', 'ROE')
            },
            {
                'metrics': 'f_roe_y',
                'years': 10,
                'group': ('盈利分析', 'ROE')
            },
            {
                'metrics': 'f_revenue_y.r_y2y',
                'years': 10,
                'group': ('盈利分析', '营业收入')
            },
            {
                'metrics': 'f_income_attr_p_y.r_y2y',
                'years': 10,
                'group': ('盈利分析', '净利润')
            },
            {
                'metrics': 'f_cashflow_free_pay_10_y.r',
                'group': ('现金流分析', '投资')
            },
            {
                'metrics': 'f_n_income_attr_p_pay_10_y.r',
                'group': ('现金流分析', '投资')
            },
            {
                'metrics': 'f_cashflow_free_y',
                'years': 10,
                'group': ('现金流分析', '投资')
            },
            {
                'metrics': 'f_sale_cash_y.r',
                'years': 10,
                'group': ('现金流分析', '销售')
            },
            {
                'metrics': 'f_sale_credit_y.r',
                'years': 10,
                'group': ('现金流分析', '销售')
            },
            {
                'metrics': 'f_adv_receipt_y.r',
                'years': 10,
                'group': ('现金流分析', '销售')
            },
            {
                'metrics': 'f_net_op_cycle_y',
                'years': 10,
                'group': ('现金流分析', '运营')
            },
            {
                'metrics': 'f_sale_net_profit_y.r',
                'years': 10,
                'group': ('盈利结构', '销售净利率分析')
            },
            {
                'metrics': 'f_gross_profit_y.r',
                'years': 10,
                'group': ('盈利结构', '销售净利率分析')
            },
            {
                'metrics': 'f_sell_revenue_y.r',
                'years': 10,
                'group': ('盈利结构', '销售净利率分析')
            },
            {
                'metrics': 'f_revadmin_revenue_y.r',
                'years': 10,
                'group': ('盈利结构', '销售净利率分析')
            },
            {
                'metrics': 'f_fin_exp_revenue_y.r',
                'years': 10,
                'group': ('盈利结构', '销售净利率分析')
            },
            {
                'metrics': 'f_income_tax_y.r',
                'years': 10,
                'group': ('盈利结构', '销售净利率分析')
            },
            {
                'metrics': 'f_total_assets_tunrover_y.r',
                'years': 10,
                'group': ('盈利结构', '周转率分析')
            },
            {
                'metrics': 'f_revenue_y',
                'years': 10,
                'group': ('盈利结构', '周转率分析')
            },
            {
                'metrics': 'f_total_assets_y',
                'years': 10,
                'group': ('盈利结构', '周转率分析')
            },
            {
                'metrics': 'f_leverage_y',
                'years': 10,
                'group': ('盈利结构', '杠杆分析')
            },
            {
                'metrics': 'f_interest_bearing_liab_y.r',
                'years': 10,
                'group': ('盈利结构', '杠杆分析')
            }
        ]
