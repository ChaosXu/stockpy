import unittest
from stockpy.db.tushare.stock import StockDb
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
        db = StockDb(**config.opts)
        # stocks = db.list()
        data = db.statement.metrics(
            '000001.SZ', 'cashflow', 'report_type', 2017, 3)
        print(data)

    # def test_income(self):
    #     db = StockDb(**config.opts)
    #     # stocks = db.list()
    #     data = db.statement.metrics(
    #         '000001.SZ', 'income', 'report_type', 2019, 3)

    #     print(data)