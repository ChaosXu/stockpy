import unittest
from stockpy.model.crawler import Crawler
from stockpy.db.stock import StockDb
from stockpy import expr
from tests.config import config


class TestCrawler(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        db = StockDb(**config.opts)
        cls.stocks = db.list()

    def test_crawl(self):
        filter = expr.Eq(expr.Get('i_ts_code'), expr.Value('688399.SH'))
        # filter = expr.Eq(expr.Get('i_ts_code'), expr.Value('000001.SZ'))
        ts = self.stocks.query_by_basic_info(filter)
        crawler = Crawler()
        crawler.crawl(ts, 2019, 2018)
