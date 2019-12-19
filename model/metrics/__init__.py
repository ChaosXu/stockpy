from model.meta import StockMeta
from model.meta import MetricsMeta
from model.metrics import income
from model.metrics import balance_sheet
from model.metrics import cash_flow
from model.metrics import financial


def load_metrics(stock_meta: StockMeta, metrics: [MetricsMeta]):
    for m in metrics:
        stock_meta.add_Metrics(m)


load_metrics(StockMeta(), income.metrics())
load_metrics(StockMeta(), balance_sheet.metrics())
load_metrics(StockMeta(), cash_flow.metrics())
load_metrics(StockMeta(), financial.metrics())
