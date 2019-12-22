from stockpy.model.meta import StockMeta


class Stock(dict, metaclass=StockMeta):
    
    def __init__(self, **kwargs):
        super(Stock, self).__init__(**kwargs)

    # @property
    # def metrics(self):
    #     return self._metrics

    # @metrics.setter
    # def metrics(self, value):
    #     self._metrics = value

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError('Stock has no attribute "%s"' % key)

    def __setattr__(self, key, value):
        self[key] = value

