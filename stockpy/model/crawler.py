
from stockpy.model.stock import Stock
import concurrent
import logging

logger = logging.getLogger(__name__)


class Crawler:

    def crawl(self, stocks, last_year, first_year):
        if last_year < first_year:
            raise ValueError(
                'first_year {} do not greater than last_year {}'.format(
                    first_year, last_year))
        for stock in stocks:
            self.__crawl(stock, last_year, first_year)

    def __crawl(self, stock, last_year, first_year):
        fus = []
        with concurrent.futures.ThreadPoolExecutor() as executor:
            for y in range(last_year, first_year-1, -1):
                for q in range(4, 0, -1):
                    fus.append(self.__submit(
                        executor, 'balancesheet', stock, y, q))
                    fus.append(self.__submit(executor,
                                             'cashflow', stock, y, q))
                    fus.append(self.__submit(executor,
                                             'income', stock, y, q))

        for fu in fus:
            try:
                fu['future'].result()
            except Exception as e:
                logger.error('crawl %s %s %s %s failed',
                             fu['stock']['ts_code'],
                             fu['type'],
                             fu['y'],
                             fu['q'],
                             exc_info=e)

    def __submit(self, executor, stat: str, stock, y, q):
        return {
            'future': executor.submit(self.__crawl_task, stat, stock, y, q),
            'type': stat,
            'stock': stock,
            'y': y,
            'q': q
        }

    def __crawl_task(self, stat: str, stock: Stock, y: int, q: int):
        stock.crawl_metrics(stat, 'ts_code', y, q)
