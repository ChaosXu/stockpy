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


class Expr:

    def eval(self, stock: ExprCtx, year: int, quarter: int):
        pass

