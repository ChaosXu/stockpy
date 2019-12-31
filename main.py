from stockpy.db.tushare.stock import StockDb
from tests.config import config
from stockpy.model.crawler import Crawler
from stockpy.model.horse import Horse
import fire


def horse(year: int, quarter: int):
    db = StockDb(**config.opts)
    stocks = db.list()
    horse = Horse()
    rs = horse.perform(stocks, year, quarter)
    file_path = config.opts['to_excel_path']+r'/horse.xlsx'
    rs.to_execl(file_path)


def crawl(last_year: int, firs_year: int):
    db = StockDb(**config.opts)
    stocks = db.list()
    crawler = Crawler()
    crawler.crawl(stocks, 2019, 2003)


def main():
    fire.Fire({
        'hello': hello,
        'crawl': crawl
    })


if __name__ == '__main__':
    main()
