import unittest

import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)
    def test_subtract(self):
        result = rpn.calculate("5 3 -")
        self.assertEqual(2, result)
    def test_multiply(self):
        result = rpn.calculate("5 3 *")
        self.assertEqual(15, result)
    def test_divide(self):
        result = rpn.calculate("6 3 /")
        self.assertEqual(2, result)
    def test_exp_regular(self):
        result = rpn.calculate(3 5 ^)
        self.assertEqual(243, result)
    def test_exp_0(self):
        result = rpn.calculate("5 0 ^")
        self.assertEqual(1, result)
    def test_exp_neg(self):
        result = rpn.calculate("2 -2 ^")
        self.assertEqual(-0.25, result)
    def test_exp_frac(self):
        result = rpn.calculate("9 0.5 ^")
        self.assertEqual(3, result)
