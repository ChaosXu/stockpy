from stockpy.cli.stock import Stock
import logging
import unittest
import os
import sys
print(os.getcwd())
print(sys.path)




class StockTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging.basicConfig(
            filename='stockpy.log',
            format='%(levelname)s:%(asctime)s %(message)s',
            level=logging.DEBUG)
        cls.stock = Stock('tests/config/config.json')

    def list_by_white_horse(self):
        stocks = self.stock.list(year=2019, quarter=3, filter='w')

        print('total count', len(stocks))

        self.print_verify(stocks)

    def print_verify(self, stocks):
        ts_codes = {'600612.SH': False,
                    # '600660.SH': False,
                    '600690.SH': False,
                    '000049.SZ': False,
                    # '600885.SH': False,
                    '600887.SH': False,
                    '000596.SZ': False,
                    '600763.SH': False,
                    '000651.SZ': False,
                    '000661.SZ': False,
                    # '000848.SZ': False,
                    # '000895.SZ': False,
                    '600167.SH': False,
                    # '000921.SZ': False,
                    '000963.SZ': False,
                    '600276.SH': False,
                    # '600338.SH': False,
                    # '600566.SH': False,
                    '600519.SH': False,
                    '600036.SH': False,
                    # '600563.SH': False,
                    '600436.SH': False,
                    # '600340.SH': False,
                    '002007.SZ': False,
                    '002032.SZ': False,
                    '002081.SZ': False,
                    '601318.SH': False,
                    '002142.SZ': False,
                    '601009.SH': False,
                    # '002146.SZ': False,
                    '002236.SZ': False,
                    '002242.SZ': False,
                    '002262.SZ': False,
                    '002271.SZ': False,
                    # '002275.SZ': False,
                    '002287.SZ': False,
                    '002304.SZ': False,
                    '601877.SH': False,
                    '002372.SZ': False,
                    '002415.SZ': False,
                    '002508.SZ': False,
                    '002572.SZ': False,
                    '601515.SH': False,
                    '000333.SZ': False,
                    '300357.SZ': False,
                    '603288.SH': False,
                    '603369.SH': False,
                    '300406.SZ': False
                    }
        oks = []
        additional = []

        for stock in stocks:
            ok = None
            for k in ts_codes.keys():
                if stock['ts_code'] == k:
                    oks.append(stock)
                    ok = stock
                    ts_codes[k] = True
            if ok is None:
                additional.append(stock)

        for ok in oks:
            print(ok['ts_code'], ok['name'])
        print('oks count', len(oks))

        for add in additional:
            print(add['ts_code'], add['name'])
        print('add count', len(additional))

        kc = 0
        for k, v in ts_codes.items():
            if not v:
                kc += 1
                print(k)
        print('miss count', kc)

    def get_white_horse(self):
        self.stock.eval(None,
                        2019, 3,
                        f'{os.path.curdir}/out',
                        report='w')

    def test_get_test(self):
        self.stock.eval('002236.SZ',
                        2019, 3,
                        f'{os.path.curdir}/out',
                        report='w')
