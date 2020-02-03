import unittest
import logging
from stockpy.db.stock import StockDb
from stockpy.filter import horse
from stockpy import expr
from tests.config import config


class TestStock(unittest.TestCase):

    # def test_list(self):
    #     db = StockDb(**config.opts)
    #     stocks = db.list()
    #     for stock in stocks:
    #         self.assertIsNotNone(stock['ts_code'])

    # def test_where(self):
    #     db = StockDb(**config.opts)
    #     stocks = db.list()
    #     filter = Eq(Get('i_ts_code'), Value('000001.SZ'))
    #     horses = stocks.where(filter)

    #     self.assertEqual(1, len(horses))

    # def test_balancesheet(self):
    #     db = StockDb(**config.opts)
    #     stocks = db.list()
    #     stocks.to_excel(config.opts['to_excel_path'])
    #     # for stock in stocks:
    #     #     print(stock['ts_code'])

    #     data = db.statement.metrics(
    #         '000001.SZ', 'balancesheet', 'report_type', 2019, 3)
    #     print(data)

    #     stock = stocks[0]
    #     stock.to_excel(config.opts['to_excel_path'], 2019, 3)
    #     v = stock.get_metrics('total_share', 2019, 3)
    #     print('total_share:')
    #     print(v)

    def test_cashflow(self):
        pass
        # db = StockDb(**config.opts)
        # # stocks = db.list()
        # data = db.statement.metrics(
        #     '000001.SZ', 'cashflow', 'report_type', 2017, 3)
        # print(data)

    # def test_income(self):
    #     db = StockDb(**config.opts)
    #     # stocks = db.list()
    #     data = db.statement.metrics(
    #         '000001.SZ', 'income', 'report_type', 2019, 3)

    #     print(data)

    def test_verify_white_horse(self):
        # ts_codes = ['600612.SH',
        #             '600660.SH',
        #             '600690.SH',
        #             '000049.SZ',
        #             '600885.SH',
        #             '600887.SH',
        #             '000596.SZ',
        #             '600763.SH',
        #             '000651.SZ',
        #             '000661.SZ',
        #             '000848.SZ',
        #             '000895.SZ',
        #             '600167.SH',
        #             '000921.SZ',
        #             '000963.SZ',
        #             '600276.SH',
        #             '600338.SH',
        #             '600566.SH',
        #             '600519.SH',
        #             '600036.SH',
        #             '600563.SH',
        #             '600436.SH',
        #             '600340.SH',
        #             '002007.SZ',
        #             '002032.SZ',
        #             '002081.SZ',
        #             '601318.SH',
        #             '002142.SZ',
        #             '601009.SH',
        #             '002146.SZ',
        #             '002236.SZ',
        #             '002242.SZ',
        #             '002262.SZ',
        #             '002271.SZ',
        #             '002275.SZ',
        #             '002287.SZ',
        #             '002304.SZ',
        #             '601877.SH',
        #             '002372.SZ',
        #             '002415.SZ',
        #             '002508.SZ',
        #             '002572.SZ',
        #             '601515.SH',
        #             '000333.SZ',
        #             '300357.SZ',
        #             '603288.SH',
        #             '603369.SH',
        #             '300406.SZ']
        ts_codes = ['688399.SH']
        logging.basicConfig(
            filename='stockpy.log',
            format='%(levelname)s:%(asctime)s %(message)s',
            level=logging.DEBUG)

        def eq_ts_code(ts_code: str):
            return expr.Eq(expr.Get('i_ts_code'), expr.Value(ts_code))
        db = StockDb(**config.opts)
        stocks = db.list()
        in_filter = expr.Or([eq_ts_code(ts_code) for ts_code in ts_codes])
        wh_stocks = stocks.query_by_basic_info(in_filter)
        horse_filter = horse.horseFilter()

        verify_stocks = []
        failed_stocks = []
        for stock in wh_stocks:
            v = horse_filter.eval(stock, 2019, 3)
            if v:
                verify_stocks.append(stock)
            else:
                failed_stocks.append(stock)

        for stock in verify_stocks:
            print(stock['name'], stock['ts_code'])
        print('verify:', len(verify_stocks), len(ts_codes))

        for stock in failed_stocks:
            print(stock['name'], stock['ts_code'])
        print('failed:', len(failed_stocks), len(ts_codes))
