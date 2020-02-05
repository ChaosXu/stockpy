import functools
import logging

logger = logging.getLogger(__name__)


class ExprCtx:

    def get_metrics(self, name: str, year: int, quarter: int):
        '''get metrics value
        Args:
            name: metrics name
            year: report year
            quarter: report quarter.from stockpy.1 to 4
        Returns:
            metrics value
        '''
        pass

    def crawl_metrics(self, stat: str, name: str, year: int, quarter: int):
        '''crawl metrics value from outer source
        Args:
            stat: statement name
            name: metrics name
            year: report year
            quarter: report quarter.from stockpy.1 to 4
        Returns:
            metrics value
        '''
        pass


class Expr:

    def eval(self, stock: ExprCtx, year: int, quarter: int):
        pass


def trace(func):
    '''trace expr execution '''

    @functools.wraps(func)
    def wrap_eval(*args, **kwargs):
        try:
            v = func(*args, **kwargs)
            if logger.isEnabledFor(logging.DEBUG):
                func_self = args[0]
                stock = args[1]
                y = args[2]
                q = args[3]
                logger.debug('EXPR:%s(%s) %s %s %s [%s]', stock['ts_code'],
                             stock['name'], y, q, v, func_self)
            return v
        except Exception as e:
            if logger.isEnabledFor(logging.ERROR):
                func_self = args[0]
                stock = args[1]
                y = args[2]
                q = args[3]
                logger.error('EXPR:%s(%s) %s %s [%s]', stock['ts_code'],
                             stock['name'], y, q, func_self, exc_info=e)
            raise
    return wrap_eval


class Name(Expr):

    def __init__(self, name: str, expr: Expr):
        self.__name = name
        self.__expr = expr

    @trace
    def eval(self, stock: ExprCtx, year: int, quarter: int):
        return self.__expr.eval(stock, year, quarter)

    def __str__(self):
        return f'{self.__name}:{self.__expr}'


class Percent(Expr):

    def __init__(self, expr: Expr):
        self.__expr = expr

    @trace
    def eval(self, stock: ExprCtx, year: int, quarter: int):
        v = self.__expr.eval(stock, year, quarter)
        v.set_data(round(v.data*100, 2))
        return v

    def __str__(self):
        return f'%{self.__expr}'


class ExprValue:

    def __init__(self, y: int, q: int, v):
        self.__y = y
        self.__q = q
        self.__v = v

    @property
    def year(self):
        return self.__y

    @property
    def quarter(self):
        return self.__q

    @property
    def data(self):
        return self.__v

    def set_data(self, v):
        self.__v = v

    def __eq__(self, value):
        return self.__v == value.__v

    def __ne__(self, value):
        return self.__v != value.__v

    def __lt__(self, value):
        return self.__v < value.__v

    def __le__(self, value):
        return self.__v <= value.__v

    def __gt__(self, value):
        return self.__v > value.__v

    def __ge__(self, value):
        return self.__v >= value.__v

    def __add__(self, value):
        return ExprValue(self.__get_return_y(value),
                         self.__get_return_q(value),
                         self.__v + value.__v)

    def __sub__(self, value):
        return ExprValue(self.__get_return_y(value),
                         self.__get_return_q(value),
                         self.__v - value.__v)

    def __mul__(self, value):
        return ExprValue(self.__get_return_y(value),
                         self.__get_return_q(value),
                         self.__v * value.__v)

    def __truediv__(self, value):
        return ExprValue(self.__get_return_y(value),
                         self.__get_return_q(value),
                         self.__v / value.__v)

    def __str__(self):
        return f'{self.__y}Q{self.__q}:{self.__v}'

    def __get_return_y(self, v):
        if self.__y < v.__y:
            return v.__y
        return self.__y

    def __get_return_q(self, v):
        if self.__y < v.__y and self.__q < v.__q:
            return v.__q
        return self.__q
