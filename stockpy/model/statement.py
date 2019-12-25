class Statement:

    def metrics(self, ts_code: str, stat: str, name: str,
                year: int, quarter: int):
        pass

    def to_excel(self, path: str, ts_code: str, year: int, quarter: int):
        pass


class StatementMixin:

    def __init__(self, stat: Statement, ts_code: str):
        self.__stat = stat
        self.__ts_code = ts_code

    @property
    def statement(self):
        return self.__stat

    def to_excel(self, path: str, year: int, quarter: int):
        self.__stat.to_excel(path, self.__ts_code, year, quarter)
