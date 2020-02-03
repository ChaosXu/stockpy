from stockpy.model.meta import StockMeta
from stockpy.model.statement import Statement, StatementMixin
from stockpy.metrics import MetricsMixin
from stockpy.expr import ExprCtx, BooleanExpr
import pandas as pd
import os
import logging
import concurrent

logger = logging.getLogger(__name__)


class Stock(ExprCtx, MetricsMixin, StatementMixin, metaclass=StockMeta):

    def __init__(self, stat: Statement, info: pd.Series):
        ExprCtx.__init__(self)
        MetricsMixin.__init__(self)
        StatementMixin.__init__(self, stat, info['ts_code'])
        self.__info = info

    def __getitem__(self, key):
        try:
            return self.__info[key]
        except KeyError:
            raise AttributeError('Stock has no field "%s"' % key)

    def get_metrics(self, name: str, year, quarter):
        # TBD
        if name.find('i_') == 0:
            return self.__info[name[2:]]
        else:
            v = self.eval(self, name, year, quarter)
            # logger.info('Get %s(%s) %s %s %s: %s',
            #             self.__info['ts_code'], self.__info['name'], name,
            #             year, quarter, v)
            return v

    def crawl_metrics(self, stat, name, year, quarter):
        # TBD
        try:
            return self.statement.metrics(self.__info['ts_code'], stat, name,
                                          year, quarter)[0]
        except IndexError:
            return None

    def valuate(self):
        pass


class Stocks:

    def __init__(self, stat: Statement, data: pd.DataFrame):
        self.__data = data
        self.__stat = stat

    def __iter__(self):
        for index, row in self.__data.iterrows():
            yield Stock(self.__stat, row)

    def __getitem__(self, index):
        return Stock(self.__stat, self.__data.iloc[index])

    def __len__(self):
        count = 0
        for i in self.__data.iterrows():
            count += 1
        return count

    def to_excel(self, file_path: str):

        def to_file():
            with pd.ExcelWriter(file_path,
                                date_format='YYYY-MM-DD',
                                datetime_format='YYYY-MM-DD HH:MM:SS') as writer:
                self.__data.to_excel(writer)
        try:
            to_file()
        except FileNotFoundError:
            os.makedirs(os.path.dirname(file_path))
            to_file()

    def query_by_basic_info(self, filter: BooleanExpr):
        '''filter by stock's info'''
        rs = []
        for stock in self:
            if filter.eval(stock, None, None) is True:
                rs.append(stock)
        return rs

    def query_by_merics(self, year: int, quarter: int, filter: BooleanExpr):
        # if logger.isEnabledFor(logging.DEBUG):
        #     logger.debug('query_by_metrics(%s, %s, %s)', year, quarter, filter)
        '''filter by stock's metrics'''
        def do_filter(stock: Stock, year: int, quarter: int,
                      filter: BooleanExpr):
            def exec():
                try:
                    if logger.isEnabledFor(logging.INFO):
                        logger.info('do_filter %s(%s) %s %s',
                                    stock['ts_code'], stock['name'],
                                    year, quarter)
                    if filter.eval(stock, year, quarter) is True:
                        return stock
                    return None
                except Exception as e:
                    logger.error('filter error: %s %s',
                                 stock['name'], stock['ts_code'], exc_info=e)
            return exec

        fs = []
        for stock in self:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                fs.append(executor.submit(
                    do_filter(stock, year, quarter, filter)))
        stocks = []
        for f in fs:
            s = f.result()
            if s is not None:
                stocks.append(s)
        return stocks

    def query_by_merics_test(self, year: int, quarter: int, filter: {}):
        '''filter by stock's metrics'''
        def do_filter(stock: Stock, year: int, quarter: int,
                      filter: {}):
            def exec():
                try:
                    logger.info('do_filter %s(%s) %s %s',
                                stock['ts_code'], stock['name'], year, quarter)
                    r = {}
                    for k, v in filter.items():
                        try:
                            r[k] = v.eval(stock, year, quarter)
                        except Exception as e:
                            logger.error('filter k error: %s %s',
                                         stock['name'], stock['ts_code'],
                                         exc_info=e)
                            r[k] = 'Error'
                    r['stock'] = stock
                    return r
                except Exception as e:
                    logger.error('filter error: %s %s',
                                 stock['name'], stock['ts_code'], exc_info=e)
            return exec

        fs = []
        for stock in self:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                fs.append(executor.submit(
                    do_filter(stock, year, quarter, filter)))
        stocks = []
        for f in fs:
            r = f.result()
            if r is not None:
                logger.info('%s %s', r['stock']['name'], r['stock']['ts_code'])
                s = ''
                for k, v in r.items():
                    if k != 'stock':
                        s += k+':'+str(v)+','
                logger.info(s)

        return stocks
