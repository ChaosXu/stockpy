import sys
import time
from stockpy.util import json as util
from stockpy.db.stock import StockDb
from stockpy import expr


class Stock():
    '''Stock Module
    '''

    def __init__(self, config_path=''):
        if config_path == '':
            config_path = sys.path[0]+'/config.json'
        self.__cfg = util.load_json(config_path)

    def list(self, year: int, quarter: int,
             date: str = None,
             filter: str = 'w',
             cache: bool = True):
        '''Returns all stocks that match filter.
        Args:
            filter:
                w Filter by white horse. This is default filter.
                g Filter by gold goose.
        '''
        if date is not None:
            year, quarter = date_to_y_q(date)

        if cache:
            try:
                return self.__list_from_cache(self.__cfg['cli']['cache'],
                                              year, quarter)
            except FileNotFoundError:
                # query
                pass

        filter = self.__get_filter(filter)

        db = StockDb(**self.__cfg)
        stocks = db.list()
        sub_stocks = stocks.query_by_merics(year, quarter, filter)
        data = []
        for sub_stock in sub_stocks:
            data.append(
                {'ts_code': sub_stock['ts_code'], 'name': sub_stock['name']})
        self.__list_to_cache(self.__cfg['cli']['cache'], year, quarter, data)
        return data

    def eval(self, ts_code: str, year: int, quarter: int, path: str,
             report='w'):
        '''Evalute the value of a stock.
        Args:
            ts_code: stock code
            year: report year
            quarter: report quarter
            path: the path to be
            report: report type. w=white horse.default is w.
        '''
        db = StockDb(**self.__cfg)
        stocks = db.list()
        filter = expr.Eq(expr.Get('i_ts_code'), expr.Value(ts_code))
        stock = stocks.query_by_basic_info(filter)[0]
        Report = self.__get_report(report)
        report = Report(stock)
        report.eval_and_save(path, year, quarter)

    def __list_from_cache(self, cache_root: str, y: int, q: int):
        return util.load_json(f'{cache_root}/list_white_horses_{y}_{q}.json')

    def __list_to_cache(self, cache_root: str, y: int, q: int, data):
        util.save_json(f'{cache_root}/list_white_horses_{y}_{q}.json', data)

    def __get_filter(self, filter: str):
        if filter == 'g':
            from stockpy.filter.goose import gooseFilter
            return gooseFilter()

        from stockpy.filter import horse
        return horse.horseFilter()
        # return {
        #     'roe_ge_15_pct_last_7_year': horse.roe_ge_15_pct_last_7_year(),
        #     'revenue_r_gt_0': horse.revenue_r_gt_0(),
        #     'income_attr_p_r_gt_0': horse.income_attr_p_r_gt_0(),
        #     'revenue_y_gt_accounts_receive_3_years': horse.revenue_y_gt_accounts_receive_3_years(),
        #     'revenue_y_gt_inventoires_3_years': horse.revenue_y_gt_inventoires_3_years(),
        #     'current_y_gt_1_3_years': horse.current_y_gt_1_3_years()
        # }

    def __get_report(self, report: str):
        from stockpy.report import horse
        return horse.Report


def date_to_y_q(date: str):
    '''split date to year and quarter when the report has been published
    20200101
    '''
    if date == '' or date is None:
        date = time.strftime("%Y%m%d", time.localtime())
    quarter = 1
    year = int(date[0:4])
    month = int(date[4:6])
    day = int(date[6:])

    if month <= 4 and day < 30:
        year -= 1
    if month >= 4 and day >= 30:
        quarter = 1
    if month >= 8 and day >= 31:
        quarter = 2
    if month >= 10 and day >= 31:
        quarter = 3
    return year, quarter
