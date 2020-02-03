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
                logger.error('EXPR:%s(%s) %s %s %s [%s]', stock['ts_code'],
                             stock['name'], y, q, e, func_self, exc_info=e)
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
