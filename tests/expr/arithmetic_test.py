import unittest
from stockpy.expr import Sum, Sub, Div, Multi, Value, Power


class ArithmeticTest(unittest.TestCase):

    def test_sum(self):
        sum = Sum(Value(1), Value(1), Value(1))
        v = sum.eval(None, None, None)
        self.assertEqual(3, v)
        print(sum, '\r\n')

    def test_sub(self):
        sub = Sub(Value(1), Value(1), Value(1))
        v = sub.eval(None, None, None)
        self.assertEqual(-1, v)
        print(sub, '\r\n')

    def test_div(self):
        div = Div(Value(2), Value(1))
        v = div.eval(None, None, None)
        self.assertEqual(2, v)
        print(div, '\r\n')

    def test_multi(self):
        multi = Multi(Value(3), Value(2))
        v = multi.eval(None, None, None)
        self.assertEqual(6, v)
        print(multi, '\r\n')

    def test_power(self):
        power = Power(Value(3), Value(2))
        v = power.eval(None, None, None)
        self.assertEqual(9, v)
        print(power, '\r\n')
