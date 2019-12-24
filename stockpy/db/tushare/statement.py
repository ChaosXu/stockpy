from stockpy.db.cache import DataFrameCache
from stockpy.db.tushare.client import Client
from stockpy.model.statement import Statement as IStat
import pandas as pd


class Statement(IStat):
    __q_date = {
        1: "0331",
        2: "0630",
        3: "0930",
        4: "1231",
    }

    __stat_name = {
        'balancesheet': 'balancesheet',
        'cashflow': 'cashflow',
        'income': 'income'
    }

    def __init__(self, **opts):
        self.__client = Client(**opts['data_provider'])
        self.__cache = DataFrameCache(**opts['data_cache'])

    def metrics(self, ts_code: str, stat: str, name: str,
                year: int, quarter: int):
        data = self.__load_data(ts_code, stat, year, quarter)
        return data[name]

    def __load_data(self, ts_code, stat, year, quarter) -> pd.DataFrame:
        data = self.__cache.get(self.__file(ts_code, stat, year, quarter))
        if data is None:
            data = self.__client.query(
                self.__stat(stat), ts_code=ts_code,
                period=self.__period(year, quarter))
            self.__cache.save(self.__file(ts_code, stat, year, quarter), data)
        return data

    def __index_of_name(self, stat, name):
        i = 0
        for f in self.__fields(stat):
            if f == name:
                return i
            else:
                i += 1
        return -1

    def __period(self, year: int, quarter: int):
        return '{}{}'.format(year, self.__q_date[quarter])

    def __stat(self, stat: str):
        return self.__stat_name[stat]

    def __file(self, ts_code, stat, year, quarter):
        return 'statements/{}/{}/{}/{}'.format(ts_code, year, quarter, stat)

    # def __fields(self, stat):
    #     if stat == 'balancesheet':
    #         return balancesheet_fields()
    #     elif stat == 'cashflow':
    #         return cashflow_fields()
    #     return income_fields()
