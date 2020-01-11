import os
import simplejson as json
import pandas as pd
import threading as th
from stockpy.db import util


class Cache:

    def __init__(self, **opts):
        self.__data_path = opts['data_path']

    def get(self, type: str):
        try:
            with open(self._file_path(type), 'r') as f:
                s = f.read()
                if s is None:
                    return s
                return json.loads(s)
        except FileNotFoundError:
            return None

    def save(self, type: str, data):
        file_path = self._file_path(type)

        def do_save():
            with open(file_path, 'w+') as f:
                jd = json.dumps(data, ensure_ascii=False,
                                encoding="utf-8", indent=4 * ' ')
                return f.write(jd)

        try:
            do_save()
        except FileNotFoundError:
            os.makedirs(os.path.dirname(file_path))
            do_save()

    def _file_path(self, type: str):
        return util.file_path(self.__data_path, type)


class DataFrameCache(Cache):

    def __init__(self, **opts):
        super().__init__(**opts)
        self.__lock = th.Lock()

    def get(self, type: str) -> pd.DataFrame:
        with self.__lock:
            try:
                return pd.read_csv(self._file_path(type))
            except FileNotFoundError:
                return None

    def save(self, type: str, data: pd.DataFrame):
        file_path = self._file_path(type)

        def do_save():
            data.to_csv(file_path)

        with self.__lock:
            try:
                do_save()
            except FileNotFoundError:
                os.makedirs(os.path.dirname(file_path))
                do_save()
