from stockpy.model.stock import Stock
from stockpy.report.base import ReportBase


class Report(ReportBase):

    def __init__(self, stock: Stock):
        ReportBase.__init__(self, stock)

    def set_metrics(self, metrics: []):
        self._metrics = metrics

    def _get_metrics(self):
        return self._metrics

    def _get_charts(self):
        charts = {}
        ms = self._get_metrics()
        for m in ms:
            group = m['group']
            charts[group[0]] = m
        return charts
