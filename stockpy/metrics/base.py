from stockpy.expr import ExprCtx
from stockpy.expr import Expr, Name, Sub, Get, Before, Div, Sum, Value


g_metrics = {}


def metrics_def(name: str, expr: Expr, display: str):
    return MetricsMeta(name, expr, display)


def metrics_y(name: str, display: str):
    '''年度值'''
    return MetricsMeta(f'{name}_y', Get(name, period='y'), display=display)


def metrics_y_y2y(name: str, display: str):
    '''年度同比增长值'''
    name_y = f'{name}_y'
    return MetricsMeta(f'{name}_y.y2y',
                       Sub(Get(name_y), Before(Get(name_y), past_year=1)),
                       display=display)


def metrics_y_r_y2y(name: str, display: str):
    '''年度同比增长率'''
    return MetricsMeta(f'{name}_y.r_y2y',
                       Div(Get(f'{name}_y.y2y'),
                           Before(Get(f'{name}_y'), past_year=1)),
                       display=display)


def metrics_y2y(name: str, display: str):
    '''季度累计同比增长值'''
    return MetricsMeta(f'{name}.y2y',
                       Sub(Get(name), Before(Get(name), past_quarter=4)),
                       display=display)


def metrics_r_y2y(name: str, display: str):
    '''季度累计同比增长率'''
    return MetricsMeta(f'{name}.r_y2y',
                       Div(Get(f'{name}.y2y'),
                           Before(Get(name), past_quarter=4)),
                       display=display)


def metrics_ratio(name: str, a: str, b: str, display: str, period: str = None):
    '''name = a / b
    Arg:
        period: y
    '''
    if period == 'y':
        return MetricsMeta(f'{name}_y.r',
                           Div(Get(f'{a}_y'),
                               Get(f'{b}_y')),
                           display=display)
    return MetricsMeta(f'{name}.r',
                       Div(Get(a),
                           Get(b)),
                       display=display)


def expr_for_list(expr: Expr, *names: str):
    return expr([Get(name) for name in names])


def expr_for_past(expr: Expr, *names: str):
    return expr([Get(name) for name in names])


def expr_div_ave_y(a, b):
    ''' name = a/ ((b1 + b2)/2)
    '''
    return Div(Get(a, period='y'),
               Div(Sum(Get(b, period='y'),
                       Before(Get(b, period='y'), past_year=1)),
                   Value(2)))


def expr_div_ave(a, b, past_quarter):
    ''' name = a/ ((b1 + b2)/2)
    '''
    return Div(Get(a),
               Div(Sum(Get(b),
                       Before(Get(b), past_quarter)),
                   Value(2)))


class MetricsMeta:

    def __init__(self, name: str, expr: Expr, display: str = ''):
        self._name = name
        self._expr = Name(f'm:{name}', expr)
        self._d_namne = display

    @property
    def name(self):
        return self._name

    @property
    def expr(self):
        return self._expr

    @property
    def display_name(self):
        if self._d_namne == '':
            return self._name
        return self._d_namne


class MetricsMetas:
    pass


class MetricsMixin:

    def __init__(self):
        self.__metrics = {}

    def eval(self, stock: ExprCtx, name: str, year: int, quarter: int):
        return self.__metrics[name].expr.eval(stock, year, quarter)

    def load_metrics(self, industry: str):
        # TBD
        self.__metrics = g_metrics

    def get_meta(self, name: str):
        return self.__metrics[name]
