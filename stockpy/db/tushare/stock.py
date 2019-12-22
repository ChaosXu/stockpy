from stockpy.db.tushare.client import Client
from stockpy.db.cache import Cache
from stockpy.model.stock import Stock
from stockpy.db.tushare.statement import Statement


class StockDb:
    __fields = '''
        ts_code,
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
        is_hs'''

    def __init__(self, **opts):
        self.__client = Client(**opts['data_provider'])
        self.__cache = Cache(**opts['data_cache'])
        self.__statement = Statement(**opts)

    def list(self):
        data = self.__cache.get('stock_basic')
        if data == None:
            data = self.__client.query(
                'stock_basic', fields=self.__fields, list_stauts='L')
            self.__cache.save('stock_basic', data)
        return Stocks(self.__statement, data)

    @property
    def statement(self):
        return self.__statement


class Stocks():

    def __init__(self, stat, data):
        self.__data = data
        self.__stat = stat

    def __iter__(self):
        for item in self.__data['items']:
            yield Stock(self.__stat, **self.__map(self.__data['fields'], item))

    def __map(self, fields, item):
        kv = {}
        for i in range(len(item)):
            kv[fields[i]] = item[i]
        return kv
