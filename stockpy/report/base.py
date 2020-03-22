from stockpy.model.stock import Stock
from stockpy.util import pandas as pd_util
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


class ReportBase(pd_util.DataFrameToExcelMixin, pd_util.DataFrameToChartMixin):
    '''The base class of report'''

    def __init__(self, stock: Stock):
        self.__stock = stock

    def _get_metrics(self):
        pass

    def _get_charts(self):
        pass

    def eval(self, year: int, quarter: int):
        self.__df = self.__load_data(year, quarter)
        # self.__to_chart(
        #     f'{self.__stock["ts_code"]} {self.__stock["name"]} {year}年{quarter}季')

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
            ss[m['group']+(display,)] = self.__load_series(m, y, q, years)

        return pd.DataFrame(ss)

    def __load_series(self, metrics: {}, y: int, q: int, count: int):
        name = metrics['metrics']
        data = {}
        for y in range(y-count+1, y+1):
            v = self.__stock.get_metrics(name, y, q)
            data[f'{v.year}Q{v.quarter}'] = v.data
        if q < 4:
            if 'metrics_q' in metrics:
                self.__load_metrics_q(data, metrics['metrics_q'], y, q)
        return data

    def __load_metrics_q(self, data, name, y: int, q: int):
        v = self.__stock.get_metrics(name, y, q)
        data[f'{v.year}Q{v.quarter}'] = v.data
