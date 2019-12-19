import unittest
from model.stock import StockMeta
from model.stock import Stock


class TestStock(unittest.TestCase):

    def test_stock(self):
        stock = Stock('000000', StockMeta())
        print(stock.get_metrics('roe.ttm', 2019, 4))
