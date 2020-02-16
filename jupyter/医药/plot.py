from stockpy.cli.stock import Stock
import logging


class Plot:

    def __init__(self, ts_code: str, config_path: str = None):
        logging.basicConfig(
            filename='stockpy.log',
            format='%(levelname)s:%(asctime)s %(message)s',
            level=logging.DEBUG)
        if config_path is None:
            config_path = '../config.json'
        self.stock = Stock(config_path)
        self._ts_code = ts_code

    def show(self, y: int, q: int, metrics: []):
        self.stock.show(self._ts_code,
                        y, q,
                        metrics)
