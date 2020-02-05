from stockpy.model.stock import Stock
from stockpy.util import json
from stockpy import expr


class Report:

    def __init__(self, stock: Stock):
        self.__stock = stock

    def eval_and_save(self, path: str, year: int, quarter: int):
        data = {
            '基本信息': {
                '股票代码': self.__stock['ts_code'],
                '名称': self.__stock['name']
            }
        }
        self.__get_filter_metrics(data, year, quarter)
        self.__get_cash_flow_portrait(data, year, quarter)
        self.__get_profit_analysis(data, year, quarter)
        json.save_json(
            f'{path}/{self.__stock["ts_code"]}_{year}_{quarter}_report.json',
            data)

    def __get_filter_metrics(self, data: {}, y: int, q: int):
        c = {}
        c['连续7年ROE>=15%'] = self.__roe_last_7_year(y, q),
        c['最近1年和1季度营业收增长率(同比)>0'] = self.__revenue_r(y, q),
        c['最近1年和1季度净利润增长率(同比)>0'] = self.__income_attr_p_r(y, q),
        c['最近3年营业收入连续2年>应收账款增长'] = self.__revenue_y_accounts_receive_3_years(
            y, q),
        c['最近3年营业收入连续2年>存货增长'] = self.__revenue_y_inventoires_3_years(y, q),
        c['最近3年流动率>1'] = self.__current_y_3_years(y, q)
        data['筛选条件'] = c

    def __roe_last_7_year(self, y: int, q: int):
        data = {}
        data[y] = expr.Get('f_roe').eval(self.__stock, y, q)
        p = expr.Range(expr.Before(
            expr.Get('f_roe_y'), past_year=1), year_count=6)
        ms = p.eval(self.__stock, y, q)
        i = 1
        for m in ms:
            data[y-i] = m
            i += 1

        return data

    def __revenue_r(self,  y: int, q: int):
        data = {
            '最近1年': expr.Before(expr.Get('f_revenue_y.r_y2y'),
                                past_year=1).eval(self.__stock, y, q),
            '最近1季度': expr.Get('f_revenue_q.r_y2y').eval(
                self.__stock, y, q)
        }
        return data

    def __income_attr_p_r(self, y: int, q: int):
        data = {
            '最近1年': expr.Before(expr.Get('f_income_attr_p_y.r_y2y'),
                                past_year=1).eval(self.__stock, y, q),
            '最近1季度': expr.Get('f_income_attr_p_q.r_y2y').eval(
                self.__stock, y, q)
        }
        return data

    def __revenue_y_accounts_receive_3_years(self, y: int, q: int):
        data = {
            y: {
                '营业收入增长': expr.Get('f_revenue_y.y2y').eval(self.__stock, y, q),
                '应收账款增长': expr.Get('f_accounts_receiv_y.y2y').eval(
                    self.__stock, y, q)
            },
            y-1: {
                '营业收入增长': expr.Before(expr.Get('f_revenue_y.y2y'),
                                      past_year=1).eval(self.__stock, y, q),
                '应收账款增长': expr.Before(expr.Get('f_accounts_receiv_y.y2y'),
                                      past_year=1).eval(self.__stock, y, q)
            },
            y-2: {
                '营业收入增长': expr.Before(expr.Get('f_revenue_y.y2y'),
                                      past_year=2).eval(self.__stock, y, q),
                '应收账款增长': expr.Before(expr.Get('f_accounts_receiv_y.y2y'),
                                      past_year=2).eval(self.__stock, y, q)
            }}
        return data

    def __revenue_y_inventoires_3_years(self, y: int, q: int):
        data = {
            y: {
                '营业收入增长': expr.Get('f_revenue_y.y2y').eval(self.__stock, y, q),
                '存货增长': expr.Get('f_inventories_y.y2y').eval(
                    self.__stock, y, q)
            },
            y-1: {
                '营业收入增长': expr.Before(expr.Get('f_revenue_y.y2y'),
                                      past_year=1).eval(self.__stock, y, q),
                '存货增长': expr.Before(expr.Get('f_inventories_y.y2y'),
                                    past_year=1).eval(self.__stock, y, q)
            },
            y-2: {
                '营业收入增长': expr.Before(expr.Get('f_revenue_y.y2y'),
                                      past_year=2).eval(self.__stock, y, q),
                '存货增长': expr.Before(expr.Get('f_inventories_y.y2y'),
                                    past_year=2).eval(self.__stock, y, q)
            }}
        return data

    def __current_y_3_years(self, y: int, q: int):
        data = {
            y: expr.Get('f_current_y.r').eval(self.__stock, y, q),

            y-1: expr.Before(expr.Get('f_current_y.r'),
                             past_year=1).eval(self.__stock, y, q),
            y-2: expr.Before(expr.Get('f_current_y.r'),
                             past_year=2).eval(self.__stock, y, q),
        }
        return data

    def __get_cash_flow_portrait(self, data: {}, y: int, q: int):

        data['现金流分析'] = {
            '投资': self.__get_cash_flow_portrait_invs(y, q),
            '销售': self.__get_cash_flow_portrait_sell(y, q),
            '净营业周期': self.__stock.get_metrics('f_net_op_cycle_y', y, q)
        }

    def __get_cash_flow_portrait_invs(self, y: int, q: int):
        c1 = c1 = self.__stock.get_metrics(
            'f_cashflow_free_pay_10_y.r', y, q)
        c1_l = 4
        if c1 > 2:
            c1_l = 4
        elif c1 > 1:
            c1_l = 3
        elif c1 <= 1:
            c1_l = 2  # 成长阶段，需要投资，或确实不行
        if c1 < 0.5:
            c1_l = 1

        c2 = self.__stock.get_metrics(
            'f_n_income_attr_p_pay_10_y.r', y, q)
        c2_l = 2
        if c2 >= 0.3:
            c2_l = 4
        elif c1 >= 0.1:
            c1_l = 3
        elif c1 <= 0.01:
            c1_l = 1

        c = {
            '10年自由现金流/10年资本开支比': {
                '等级': c1_l,
                '数值': c1
            },
            '10年净利润增长/10年资本开支比': {
                '等级': c2_l,
                '数值': c2
            }
        }

        return c

    def __get_cash_flow_portrait_sell(self, y: int, q: int):
        c = {
            '收现率': self.__stock.get_metrics('f_sale_cash.r', y, q),
            '赊销率': self.__stock.get_metrics('f_sale_credit.r', y, q),
            '预收率': self.__stock.get_metrics('f_adv_receipt.r', y, q)
        }

        return c

    def __get_profit_analysis(self, data: {}, y: int, q: int):

        data['盈利分析'] = {
            '销售净利率分析': self.__get_sell_net_profit(y, q),
            '总资产周转率分析': self.__get_total_assets_tunrover_rate(y, q),
            '杠杆倍数分析': self.__get_leverage(y, q),
        }

    def __get_sell_net_profit(self, y, q):
        c = {
            '销售净利率': self.__get_metrics('f_sale_net_profit_y.r', y, q, 10),
            '毛利率': self.__get_metrics('f_gross_profit_y.r', y, q, 10),
            '销售费用占比': self.__get_metrics('f_sell_revenue_y.r', y, q, 10),
            '管理费用占比': self.__get_metrics('f_revadmin_revenue_y.r', y, q, 10),
            '财务费用占比': self.__get_metrics('f_fin_exp_revenue_y.r', y, q, 10),
            '所得税占比': self.__get_metrics('f_income_tax_y.r', y, q, 10)
        }
        return c

    def __get_total_assets_tunrover_rate(self, y, q):
        c = {
            '总资产周转率': self.__get_metrics(
                'f_total_assets_tunrover_y.r', y, q, 10),
            '营业收入': self.__get_metrics(
                'f_revenue_y', y, q, 10),
            '总资产': self.__get_metrics(
                'f_total_assets_y', y, q, 10)
        }
        return c

    def __get_leverage(self, y, q):
        c = {
            '杠杆倍数': self.__get_metrics('f_sale_net_profit_y.r', y, q, 10),
            '有息负债率': self.__get_metrics('f_interest_bearing_liab_y.r', y, q, 10),
        }
        return c

    def __get_metrics(self, metrics: str, y: int, q: int, year_count: int):
        '''获取连续N年的指标'''
        d = []
        offset = 0
        if q != 4:
            offset = 1
        for y in range(y, y-year_count, -1):
            d.append({y-offset: self.__stock.get_metrics(metrics, y, q)})
        return d
