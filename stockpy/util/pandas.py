import pandas as pd
import os


class DataFrameToExcelMixin:

    def to_excel(self, file_path: str):

        def to_file():
            with pd.ExcelWriter(file_path,
                                date_format='YYYY-MM-DD',
                                datetime_format='YYYY-MM-DD HH:MM:SS') as writer:
                self.data_frame.to_excel(writer,sheet_name='sheet1')
        try:
            to_file()
        except FileNotFoundError:
            os.makedirs(os.path.dirname(file_path))
            to_file()

    @property
    def data_frame(self) -> pd.DataFrame:
        pass
