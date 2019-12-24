import unittest
from stockpy.db.tushare.stock import StockDb
from tests.config import config


class TestStatement(unittest.TestCase):

    def test_balancesheet(self):
        db = StockDb(**config.opts)
        stocks = db.list()
        for stock in stocks:
            # print(stock['ts_code'])
            print(stock.ts_code)
        data = db.statement.metrics(
            '000001.SZ', 'balancesheet', 'report_type', 2019, 3)

        print(data)

    def test_cashflow(self):
        db = StockDb(**config.opts)
        # stocks = db.list()
        data = db.statement.metrics(
            '000001.SZ', 'cashflow', 'report_type', 2019, 3)
        print(data)

    def test_income(self):
        db = StockDb(**config.opts)
        # stocks = db.list()
        data = db.statement.metrics(
            '000001.SZ', 'income', 'report_type', 2019, 3)

        print(data)
