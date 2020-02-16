import math
import pandas as pd
import os
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


class DataFrameToExcelMixin:

    def to_excel(self, file_path: str):

        def to_file():
            with pd.ExcelWriter(file_path,
                                date_format='YYYY-MM-DD',
                                datetime_format='YYYY-MM-DD HH:MM:SS') as writer:
                self.data_frame.to_excel(writer, sheet_name='sheet1')
        try:
            to_file()
        except FileNotFoundError:
            os.makedirs(os.path.dirname(file_path))
            to_file()

    @property
    def data_frame(self) -> pd.DataFrame:
        pass


class DataFrameToChartMixin:

    def to_chart(self, file_path: str, title: str):
        self.__draw_plots(title)
        plt.savefig(file_path, dpi=600)

    def show(self, title: str):
        self.__draw_plots(title)
        plt.show()

    def __draw_plots(self, title: str):
        charts = self._get_charts()
        col = 4
        if len(charts) == 1:
            col = 1
        c = math.ceil(len(charts)/4)
        # fig, axs = plt.subplots(c, col, figsize=(14, 8.5))
        fig, axs = plt.subplots(c, col)
        # fig.suptitle(title, fontsize=10)
        # fig.subplots_adjust(top=0.93, right=0.93, left=0.07,
        #                     wspace=0.3, hspace=0.15*c)
        i = 0
        for k, chart in charts.items():
            row = int(i/col)
            col = i % col
            scale = None
            unit = None
            if 'scale' in chart:
                scale = chart['scale']
            if 'unit' in chart:
                unit = chart['unit']
                title = f'{k}({unit})'
            else:
                title = k
            if row == 0 and col == 0:
                ax = axs
            else:
                ax = axs[row][col]
            self.__draw_plot(ax,
                             title,
                             chart['group'],
                             scale,
                             unit)
            i += 1

    def __draw_plot(self, ax, title: str, metrics: [], scale: int, unit: str):

        df = self.data_frame[metrics]

        for col in df.columns:
            ax.plot(df[col], label=col)

        ax.set_title(title, fontsize=9)
        if scale is not None or unit is not None:
            ax.yaxis.set_major_formatter(self.__axis_scale(scale, unit))
        ax.grid()

        for label in ax.xaxis.get_ticklabels():
            label.set_rotation(45)

        leg = ax.legend(loc=2, prop={'size': 7.5})
        leg.get_frame().set_alpha(0.6)

    @property
    def data_frame(self) -> pd.DataFrame:
        pass

    @property
    def _get_charts(self):
        pass

    def __axis_scale(self, scale: int, unit):
        def do_format(v, pos):
            if unit == '%':
                return round(v * 100, 2)
            return v/scale
        return plt.FuncFormatter(do_format)
