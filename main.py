import fire
from stockpy.cli import stock
import base64
import sys


def main():
    # fire.Fire({
    #     'stock': stock.Stock
    # })
    print(sys.getdefaultencoding())

    print(base64.b64encode(bytes('上市读书节',encoding='utf8')))
    #b = bytes('5LiK5a6e6K+75Lmm6lqC', encoding='utf8')
    s = base64.b64decode('5LiK5a6e6K+75Lmm6IqC')
    print(type(s))
    print(s)
    print(str(s, encoding='utf8', errors='ignore'))


if __name__ == '__main__':
    main()
