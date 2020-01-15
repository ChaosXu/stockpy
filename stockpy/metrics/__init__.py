from stockpy.metrics.base import MetricsMeta, MetricsMixin, g_metrics
from stockpy.metrics.statements import balance_sheet, income, cash_flow
from stockpy.metrics.finance import (
    income as f_income,
    balance_sheet as f_balance_sheet,
    cash_flow as f_cash_flow,
    roe
)


def load_metrics(metrics_metas, metrics: [MetricsMeta]):
    for m in metrics:
        metrics_metas[m.name] = m


load_metrics(g_metrics, income.metrics())
load_metrics(g_metrics, balance_sheet.metrics())
load_metrics(g_metrics, cash_flow.metrics())
load_metrics(g_metrics, f_income.metrics())
load_metrics(g_metrics, f_balance_sheet.metrics())
load_metrics(g_metrics, f_cash_flow.metrics())
load_metrics(g_metrics, roe.metrics())


# load_metrics(StockMeta(), inventory.metrics())
# load_metrics(StockMeta(), goose.metrics())
