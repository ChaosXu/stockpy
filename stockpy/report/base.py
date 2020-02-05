from stockpy.model.stock import Stock
from stockpy.util import pandas as pd_util
import pandas as pd


class ReportBase(pd_util.DataFrameToExcelMixin):
    '''The base class of report'''

    def __init__(self, stock: Stock):
        self.__stock = stock

    def _get_metrics(self):
        pass

    def eval(self, year: int, quarter: int):
        self.__df = self.__load_data(year, quarter)
        print(self.__df.head())

    @property
    def data_frame(self) -> pd.DataFrame:
        if self.__df is None:
            raise Exception('Must do eval(path,year,quarter) first')

        return self.__df

    def __load_data(self, y: int, q: int):
        ms = self._get_metrics()
        ss = {}
        for m in ms:
            name = m['metrics']
            display = self.__stock.get_meta(name).display_name
            years = 1
            if 'years' in m:
                years = m['years']
            ss[m['group']+(display,)] = self.__load_series(name, y, q, years)

        return pd.DataFrame(ss)

    def __load_series(self, metrics: str, y: int, q: int, count: int):
        data = {}
        for y in range(y, y-count, -1):
            v = self.__stock.get_metrics(metrics, y, q)
            data[f'{v.year}Q{v.quarter}'] = v.data
        return data
