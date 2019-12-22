import unittest
from stockpy.model.stock import Stock
from stockpy.db.tushare.stock import StockDb
from config import config
import datetime

class TestStatement(unittest.TestCase):

    def test_balancesheet(self):
        print(datetime.__file__)
        print(datetime.datetime_CAPI)
        db = StockDb(**config.opts)
        stocks = db.list()
        data = db.statement.metrics('000001.SZ', 'balancesheet', 'report_type', 2019, 3)
        
        print(data)

    def test_cashflow(self):
        db = StockDb(**config.opts)
        stocks = db.list()
        data = db.statement.metrics('000001.SZ', 'cashflow', 'report_type', 2019, 3)
        print(data)

    def test_income(self):
        db = StockDb(**config.opts)
        stocks = db.list()
        data = db.statement.metrics('000001.SZ', 'income', 'report_type', 2019, 3)

        print(data)
