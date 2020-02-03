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
        self.__get_metrics(data, year, quarter)
        json.save_json(
            f'{path}/{self.__stock["ts_code"]}_{year}_{quarter}_report.json',
            data)

    def __get_metrics(self, data: {}, y: int, q: int):
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
