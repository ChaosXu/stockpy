import sys
import time
from stockpy.cli import cfg
from stockpy.db.stock import StockDb


class Stock():
    '''Stock Module
    '''

    def __init__(self, config_path=''):
        if config_path == '':
            config_path = sys.path[0]+'/config.json'
        self.__cfg = cfg.load_cfg(config_path)

    def list(self, year: int, quarter: int,
             date: str = None,
             filter: str = 'w'):
        '''Returns all stocks that match filter.
        Args:
            filter:
                w Filter by white horse. This is default filter.
                g Filter by gold goose.
        '''
        if date is not None:
            year, quarter = date_to_y_q(date)
        filter = self.__get_filter(filter)

        db = StockDb(**self.__cfg)
        stocks = db.list()
        sub_stocks = stocks.query_by_merics(year, quarter, filter)
        return sub_stocks

    def evaluate(self, code: str):
        '''Evalute the value of a stock.
        Args:
            code: stock code
        '''
        pass

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
