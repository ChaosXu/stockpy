from stockpy.metrics import MetricsMixin


class StockMeta(type):

    def __call__(cls, *args, **kwargs):
        obj = cls.__new__(cls, *args, **kwargs)
        cls.__init__(obj, *args, **kwargs)
        cls.__load_metrics(obj['industry'], obj)
        return obj

    def __load_metrics(cls, industry: str, metrics_mixin: MetricsMixin):
        metrics_mixin.load_metrics(industry)
