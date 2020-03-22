from stockpy.model.stock import Stock
from stockpy.report.base import ReportBase


class Report(ReportBase):

    def __init__(self, stock: Stock):
        ReportBase.__init__(self, stock)

    def _get_metrics(self):
        y = 7
        g = 10000000
        u = '千万'
        r = '%'
        return [
            {
                'metrics': 'f_roe_y',
                'years': y,
                'unit': r,
                'group': ('盈利分析', '回报率')
            },
            {
                'metrics': 'f_roa_y',
                'years': y,
                'unit': r,
                'group': ('盈利分析', '回报率')
            },
            {
                'metrics': 'revenue_y',
                'metrics_q': 'revenue',
                'years': y,
                'scale': g,
                'unit': u,
                'group': ('盈利分析', '主营业务')
            },
            {
                'metrics': 'f_gross_profit_y',
                'metrics_q': 'f_gross_profit',
                'years': y,
                'scale': g,
                'unit': u,
                'group': ('盈利分析', '主营业务')
            },
            {
                'metrics': 'n_income_attr_p_y',
                'metrics_q': 'n_income_attr_p',
                'years': y,
                'scale': g,
                'unit': u,
                'group': ('盈利分析', '主营业务')
            },
            {
                'metrics': 'accounts_receiv_y',
                'metrics_q': 'accounts_receiv',
                'years': y,
                'scale': g,
                'unit': u,
                'group': ('盈利分析', '主营业务')
            },
            {
                'metrics': 'inventories_y',
                'metrics_q': 'inventories',
                'years': y,
                'scale': g,
                'unit': u,
                'group': ('盈利分析', '主营业务')
            },
            {
                'metrics': 'total_assets_y',
                'metrics_q': 'total_assets',
                'years': y,
                'scale': g,
                'unit': u,
                'group': ('资产分析', '资产负债')
            },
            {
                'metrics': 'money_cap_y',
                'metrics_q': 'money_cap',
                'years': y,
                'scale': g,
                'unit': u,
                'group': ('资产分析', '资产负债')
            },
            {
                'metrics': 'fix_assets_y',
                'metrics_q': 'fix_assets',
                'years': y,
                'group': ('资产分析', '资产负债')
            },
            {
                'metrics': 'total_hldr_eqy_exc_min_int_y',
                'metrics_q': 'total_hldr_eqy_exc_min_int',
                'years': y,
                'scale': g,
                'unit': u,
                'group': ('资产分析', '资产负债')
            },
            {
                'metrics': 'total_cur_liab_y',
                'metrics_q': 'total_cur_liab',
                'years': y,
                'scale': g,
                'unit': u,
                'group': ('资产分析', '资产负债')
            },
            {
                'metrics': 'total_ncl_y',
                'metrics_q': 'total_ncl',
                'years': y,
                'scale': g,
                'unit': u,
                'group': ('资产分析', '资产负债')
            },
            {
                'metrics': 'revenue_y.r_y2y',
                'metrics_q': 'revenue.r_y2y',
                'years': y,
                'unit': r,
                'group': ('盈利分析', '增长率')
            },
            {
                'metrics': 'f_gross_profit_y.r_y2y',
                'metrics_q': 'f_gross_profit.r_y2y',
                'years': y,
                'unit': r,
                'group': ('盈利分析', '增长率')
            },
            {
                'metrics': 'n_income_attr_p_y.r_y2y',
                'metrics_q': 'n_income_attr_p.r_y2y',
                'years': y,
                'unit': r,
                'group': ('盈利分析', '增长率')
            },
            {
                'metrics': 'total_hldr_eqy_exc_min_int_y.r_y2y',
                'metrics_q': 'total_hldr_eqy_exc_min_int.r_y2y',
                'years': y,
                'unit': r,
                'group': ('盈利分析', '增长率')
            },
            # {
            #     'metrics': 'accounts_receiv_y.r_y2y',
            #     'years': y,
            #     'unit': r,
            #     'group': ('盈利分析', '增长率')
            # },
            # {
            #     'metrics': 'inventories_y.r_y2y',
            #     'years': y,
            #     'unit': r,
            #     'group': ('盈利分析', '增长率')
            # },
            {
                'metrics': 'total_assets_y.r_y2y',
                'metrics_q': 'total_assets.r_y2y',
                'years': y,
                'unit': r,
                'group': ('盈利分析', '增长率')
            },

            # {
            #     'metrics': 'f_cashflow_free_pay_10_y.r',
            #     'group': ('现金流分析', '投资')
            # },
            # {
            #     'metrics': 'f_n_income_attr_p_pay_10_y.r',
            #     'group': ('现金流分析', '投资')
            # },

            {
                'metrics': 'n_cashflow_act_y',
                'metrics_q': 'n_cashflow_act',
                'years': y,
                'scale': g,
                'unit': u,
                'group': ('现金流分析', '投资')
            },
            {
                'metrics': 'n_cash_flows_fnc_act_y',
                'metrics_q': 'n_cash_flows_fnc_act',
                'years': y,
                'scale': g,
                'unit': u,
                'group': ('现金流分析', '投资')
            },
            {
                'metrics': 'n_cashflow_inv_act_y',
                'metrics_q': 'n_cashflow_inv_act',
                'years': y,
                'scale': g,
                'unit': u,
                'group': ('现金流分析', '投资')
            },
            {
                'metrics': 'n_income_attr_p_y',
                'metrics_q': 'n_income_attr_p',
                'years': y,
                'scale': g,
                'unit': u,
                'group': ('现金流分析', '投资')
            },
            {
                'metrics': 'f_cashflow_free_y',
                'metrics_q': 'f_cashflow_free',
                'years': y,
                'scale': g,
                'unit': u,
                'group': ('现金流分析', '投资')
            },
            {
                'metrics': 'f_pay_acq_const_fiolta_y',
                'metrics_q': 'c_pay_acq_const_fiolta',
                'years': y,
                'scale': g,
                'unit': u,
                'group': ('现金流分析', '投资')
            },
            {
                'metrics': 'f_sale_cash_y.r',
                'metrics_q': 'f_sale_cash.r',
                'years': y,
                'unit': r,
                'group': ('现金流分析', '销售')
            },
            {
                'metrics': 'f_sale_credit_y.r',
                'metrics_q': 'f_sale_credit.r',
                'years': y,
                'unit': r,
                'group': ('现金流分析', '销售')
            },
            {
                'metrics': 'f_adv_receipt_y.r',
                'metrics_q': 'f_adv_receipt.r',
                'years': y,
                'unit': r,
                'group': ('现金流分析', '销售')
            },
            {
                'metrics': 'f_net_op_cycle_y',
                'years': y,
                'group': ('现金流分析', '运营')
            },
            {
                'metrics': 'f_days_inventory_y',
                'years': y,
                'group': ('现金流分析', '运营')
            },
            {
                'metrics': 'f_days_accounts_receiv_y',
                'years': y,
                'group': ('现金流分析', '运营')
            },
            {
                'metrics': 'f_days_prepayment_y',
                'years': y,
                'group': ('现金流分析', '运营')
            },
            {
                'metrics': 'f_days_acct_payable_y',
                'years': y,
                'group': ('现金流分析', '运营')
            },
            {
                'metrics': 'f_days_adv_receipts_y',
                'years': y,
                'group': ('现金流分析', '运营')
            },
            {
                'metrics': 'f_sale_net_profit_y.r',
                'metrics_q': 'f_sale_net_profit.r',
                'years': y,
                'unit': r,
                'group': ('盈利分析', '销售净利率分析')
            },
            {
                'metrics': 'f_gross_profit_y.r',
                'metrics_q': 'f_gross_profit.r',
                'years': y,
                'unit': r,
                'group': ('盈利分析', '销售净利率分析')
            },
            {
                'metrics': 'f_exp_3_y.r',
                'metrics_q': 'f_exp_3.r',
                'years': y,
                'unit': r,
                'group': ('盈利分析', '销售净利率分析')
            },
            {
                'metrics': 'f_income_tax_y.r',
                'metrics_q': 'f_income_tax.r',
                'years': y,
                'unit': r,
                'group': ('盈利分析', '销售净利率分析')
            },
            {
                'metrics': 'f_gross_profit_y.r',
                'metrics_q': 'f_gross_profit.r',
                'years': y,
                'unit': r,
                'group': ('盈利分析', '毛利率分析')
            },
            {
                'metrics': 'f_oper_cost_y.r',
                'metrics_q': 'f_oper_cost.r',
                'years': y,
                'unit': r,
                'group': ('盈利分析', '毛利率分析')
            },
            {
                'metrics': 'f_sell_revenue_y.r',
                'metrics_q': 'f_sell_revenue.r',
                'years': y,
                'unit': r,
                'group': ('盈利分析', '三费分析')
            },
            {
                'metrics': 'f_admin_revenue_y.r',
                'metrics_q': 'f_admin_revenue.r',
                'years': y,
                'unit': r,
                'group': ('盈利分析', '三费分析')
            },
            {
                'metrics': 'f_fin_exp_revenue_y.r',
                'metrics_q': 'f_fin_exp_revenue.r',
                'years': y,
                'unit': r,
                'group': ('盈利分析', '三费分析')
            },
            {
                'metrics': 'f_total_assets_tunrover_y.r',
                'metrics_q': 'f_total_assets_tunrover.r',
                'years': y,
                'group': ('盈利分析', '资产周转率分析')
            },
            {
                'metrics': 'f_fix_assets_tunrover_y.r',
                'metrics_q': 'f_fix_assets_tunrover.r',
                'years': y,
                'group': ('盈利分析', '资产周转率分析')
            },
            {
                'metrics': 'f_total_cur_assets_tunrover_y.r',
                'metrics_q': 'f_total_cur_assets_tunrover.r',
                'years': y,
                'group': ('盈利分析', '资产周转率分析')
            },
            {
                'metrics': 'f_leverage_y',
                'metrics_q': 'f_leverage',
                'years': y,
                'unit': r,
                'group': ('盈利分析', '杠杆分析')
            },
            {
                'metrics': 'f_interest_bearing_liab_y.r',
                'metrics_q': 'f_interest_bearing_liab.r',
                'years': y,
                'unit': r,
                'group': ('盈利分析', '杠杆分析')
            },
            {
                'metrics': 'f_debt_assets_y.r',
                'metrics_q': 'f_debt_assets.r',
                'years': y,
                'unit': r,
                'group': ('盈利分析', '杠杆分析')
            }

        ]

    def _get_charts(self):
        charts = {}
        ms = self._get_metrics()
        for m in ms:
            group = m['group']
            charts[group[1]] = m
        return charts
