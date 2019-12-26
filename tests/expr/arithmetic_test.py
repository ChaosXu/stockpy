import unittest
from stockpy.expr import Sum, Sub, Div, Multi, Value


class ArithmeticTest(unittest.TestCase):

    def test_sum(self):
        sum = Sum(Value(1), Value(1), Value(1))
        v = sum.eval(None, None, None)
        self.assertEqual(3, v)

    def test_sub(self):
        sub = Sub(Value(1), Value(1), Value(1))
        v = sub.eval(None, None, None)
        self.assertEqual(-1, v)

    def test_div(self):
        div = Div(Value(2), Value(1))
        v = div.eval(None, None, None)
        self.assertEqual(2, v)

    def test_multi(self):
        div = Multi(Value(3), Value(2))
        v = div.eval(None, None, None)
        self.assertEqual(6, v)
