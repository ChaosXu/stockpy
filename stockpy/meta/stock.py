
from stockpy.meta import MetricsMeta


class StockMeta(type):

    # def __new__(cls, name, bases, attrs):
    #     print('StockMeta.__new__', cls)
    #     # attrs['add'] = lambda self, value: self.append(value)
    #     return type.__new__(cls, name, bases, attrs)

    def __new__(cls, *args, **kwargs):
        print('StockMeta.__new__', cls)
        # attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        print('StockMeta.__init__', self)
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        print('StockMeta.__call__', cls)
        obj = cls.__new__(cls, *args, **kwargs)
        cls.__init__(obj, *args, **kwargs)
        return obj

# def addmetrics(self, meta: MetricsMeta):
#     self._metrics[meta.get_name()] = meta

# def allmetrics(self):
#     return self._metrics

# def getmetrics(self, name: str) -> MetricsMeta:
#     return self._metrics[name]
