from stockpy.metrics.base import MetricsMeta, MetricsMixin, g_metrics
from stockpy.metrics.statements import balance_sheet, income, cash_flow
from stockpy.metrics.finance import (
    income as f_income,
    balance_sheet as f_balance_sheet,
    profit as f_profit,
    roe
)
from stockpy.metrics.finance.cashflow import (
    investment as f_cash_flow_inv,
    operating as f_op,
    sale as f_sale
)


def load_metrics(metrics_metas, metrics: [MetricsMeta]):
    for m in metrics:
        metrics_metas[m.name] = m


load_metrics(g_metrics, income.metrics())
load_metrics(g_metrics, balance_sheet.metrics())
load_metrics(g_metrics, cash_flow.metrics())
load_metrics(g_metrics, f_income.metrics())
load_metrics(g_metrics, f_balance_sheet.metrics())
load_metrics(g_metrics, f_profit.metrics())
load_metrics(g_metrics, f_cash_flow_inv.metrics())
load_metrics(g_metrics, f_sale.metrics())
load_metrics(g_metrics, f_op.metrics())
load_metrics(g_metrics, roe.metrics())


# load_metrics(StockMeta(), inventory.metrics())
# load_metrics(StockMeta(), goose.metrics())
