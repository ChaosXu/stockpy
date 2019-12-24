from stockpy.db.tushare.client import Client
from stockpy.db.cache import DataFrameCache
from stockpy.model.stock import Stocks
from stockpy.db.tushare.statement import Statement


class StockDb:
    __fields = ''' ts_code,
        symbol,
        name,
        area,
        industry,
        fullname,
        enname,
        market,
        exchange,
        curr_type,
        list_status,
        list_date,
        delist_date,
        is_hs
    '''

    def __init__(self, **opts):
        self.__client = Client(**opts['data_provider'])
        self.__cache = DataFrameCache(**opts['data_cache'])
        self.__statement = Statement(**opts)

    def list(self):
        data = self.__cache.get('stock_basic')
        if data is None:
            data = self.__client.query(
                'stock_basic', fields=self.__fields, list_stauts='L')
            self.__cache.save('stock_basic', data)
        return Stocks(self.__statement, data)

    @property
    def statement(self):
        return self.__statement
