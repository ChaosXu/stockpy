import fire
from stockpy.cli import stock


def main():
    fire.Fire({
        'stock': stock.Stock
    })


if __name__ == '__main__':
    main()
