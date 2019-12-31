
from stockpy.model.stock import Stock
import concurrent


class Crawler:

    def crawl(self, stocks, last_year, first_year):
        for stock in stocks:
            self.__crawl(stock, last_year, first_year)

    def __crawl(self, stock, last_year, first_year):
        fus = []
        with concurrent.futures.ThreadPoolExecutor() as executor:
            for y in range(last_year, first_year-1, -1):
                for q in range(4, 0, -1):
                    fus.append(executor.submit(self.__crawl_task,
                                               'balancesheet', stock, y, q))
                    fus.append(executor.submit(self.__crawl_task,
                                               'cashflow', stock, y, q))
                    fus.append(executor.submit(self.__crawl_task,
                                               'income', stock, y, q))

        for fu in fus:
            try:
                fu.result()
            except Exception as e:
                print(e)

    def __crawl_task(self, stat: str, stock: Stock, y: int, q: int):
        print('__crawl_task', stock['ts_code'], y, q)
        stock.crawl_metrics(stat, 'ts_code', y, q)
