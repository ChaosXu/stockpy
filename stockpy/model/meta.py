
# from stockpy import dpi


class StockMeta(type):

    def __new__(cls, *args, **kwargs):
        return type.__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        obj = cls.__new__(cls, *args, **kwargs)
        cls.__init__(obj, *args)
        # cls.load_metrics(obj)
        return obj

    # def load_metrics(cls, obj):
        obj.metrics = {}


# def addmetrics(self, meta: MetricsMeta):
#     self._metrics[meta.get_name()] = meta

# def allmetrics(self):
#     return self._metrics

# def getmetrics(self, name: str) -> MetricsMeta:
#     return self._metrics[name]
