"""
Tests for the NSDecimal wrapper type
"""
from PyObjCTools.TestSupport import *

from PyObjCTest.decimal import OC_TestDecimal

import sys
import operator
import objc
import decimal

try:
    unicode
except NameError:
    unicode = str

class TestNSDecimalWrwapper (TestCase):
    def test_creation(self):
        d = objc.NSDecimal(0)
        self.assertEqual(str(d), "0")

        d = objc.NSDecimal(-5)
        self.assertEqual(str(d), "-5")

        self.assertRaises(OverflowError, objc.NSDecimal, 1<<66)

        d = objc.NSDecimal(0.0)
        self.assertEqual(str(d), "0")

        d = objc.NSDecimal(0.5)
        self.assertEqual(str(d), "0.5")

        d = objc.NSDecimal("1.24")
        self.assertEqual(str(d), "1.24")

        d = objc.NSDecimal(500, 3, False)
        self.assertEqual(str(d), str(500 * 10**3))

        d = objc.NSDecimal(500, -6, True)
        self.assertEqual(str(d), str(500 * 10**-6 * -1))

    def test_comparing(self):
        d1 = objc.NSDecimal("1.500")
        d2 = objc.NSDecimal("1.500")
        d3 = objc.NSDecimal("1.4")
        d4 = objc.NSDecimal("1.6")

        self.assertTrue(d1 == d1)
        self.assertTrue(d1 == d2)
        self.assertFalse(d1 != d1)
        self.assertFalse(d1 != d2)
        self.assertTrue(d1 != d3)
        self.assertFalse(d1 != d2)
        self.assertFalse(d1 != d1)

        self.assertTrue(d1 <= d1)
        self.assertTrue(d1 <= d2)
        self.assertFalse(d1 <= d3)
        self.assertTrue(d1 <= d4)

        self.assertFalse(d1 < d1)
        self.assertFalse(d1 < d2)
        self.assertFalse(d1 < d3)
        self.assertTrue(d1  < d4)

        self.assertFalse(d1 > d1)
        self.assertFalse(d1 > d2)
        self.assertTrue(d1 > d3)
        self.assertFalse(d1  > d4)

        self.assertTrue(d1 >= d1)
        self.assertTrue(d1 >= d2)
        self.assertTrue(d1 >= d3)
        self.assertFalse(d1  >= d4)

        self.assertEqual(objc.NSDecimal("1.50"), objc.NSDecimal("1.500"))



        # It is not possible to compare with other numeric types:
        d5 = objc.NSDecimal("5")
        i5 = 5
        f5 = 5.0
        D5 = decimal.Decimal(5)

        self.assertFalse(d5 == i5)
        self.assertFalse(d5 == f5)
        self.assertFalse(d5 == D5)
        self.assertTrue(d5 != i5)
        self.assertTrue(d5 != f5)
        self.assertTrue(d5 != D5)
        self.assertRaises(TypeError, operator.lt, d5, i5)
        self.assertRaises(TypeError, operator.lt, d5, f5)
        self.assertRaises(TypeError, operator.lt, d5, D5)
        self.assertRaises(TypeError, operator.gt, d5, i5)
        self.assertRaises(TypeError, operator.gt, d5, f5)
        self.assertRaises(TypeError, operator.gt, d5, D5)
        self.assertRaises(TypeError, operator.ge, d5, i5)
        self.assertRaises(TypeError, operator.ge, d5, f5)
        self.assertRaises(TypeError, operator.ge, d5, D5)
        self.assertRaises(TypeError, operator.le, d5, i5)
        self.assertRaises(TypeError, operator.le, d5, f5)
        self.assertRaises(TypeError, operator.le, d5, D5)

    def test_hash(self):
        self.assertEqual(hash(objc.NSDecimal("1.50")), hash(objc.NSDecimal("1.500")))

    def test_conversion(self):
        d1 = objc.NSDecimal("1.5")
        d2 = objc.NSDecimal("25")

        self.assertEqual(d1.as_int(), 1)
        self.assertEqual(d2.as_int(), 25)

        self.assertEqual(d1.as_float(), 1.5)
        self.assertEqual(d2.as_float(), 25.0)


        self.assertRaises(TypeError, int, d1)
        self.assertRaises(TypeError, float, d1)

    @onlyPython3
    def test_rounding(self):
        d1 = objc.NSDecimal("1.5781")

        d2 = round(d1)
        self.assertEqual(d2, objc.NSDecimal("2"))

        d2 = round(d1, 2)
        self.assertEqual(d2, objc.NSDecimal("1.58"))

        d2 = round(d1, 3)
        self.assertEqual(d2, objc.NSDecimal("1.578"))

        d1 = objc.NSDecimal("15.44")
        d2 = round(d1, -1)
        self.assertEqual(d2, objc.NSDecimal("20"))


    def test_pow(self):
        self.assertRaises(TypeError, pow, objc.NSDecimal("3.5"), 3, 1)
        self.assertRaises(TypeError, pow, objc.NSDecimal("3.5"), 3)
        self.assertRaises(TypeError, operator.pow, objc.NSDecimal("3.5"), 3)
        self.assertRaises(TypeError, operator.pow, objc.NSDecimal("3.5"), objc.NSDecimal("2"))


    def test_operators(self):
        d1 = objc.NSDecimal("1.5")
        self.assertEqual(+d1, d1)
        self.assertEqual(-d1, objc.NSDecimal("-1.5"))

        d2 = objc.NSDecimal("0.5")

        o = d1 + d2
        self.assertEqual(o, objc.NSDecimal("2"))

        o = d1 - d2
        self.assertEqual(o, objc.NSDecimal("1.0"))

        o = d1 / d2
        self.assertEqual(o, objc.NSDecimal("3.0"))

        o = d1 * d2
        self.assertEqual(o, objc.NSDecimal("0.75"))

        o = d1 + 1
        self.assertEqual(o, objc.NSDecimal("2.5"))

        o = d1 - 1
        self.assertEqual(o, objc.NSDecimal("0.5"))

        o = d1 * 2
        self.assertEqual(o, objc.NSDecimal("3"))

        o = d1 / 2
        self.assertEqual(o, objc.NSDecimal("0.75"))

        o = d1 // 2
        self.assertEqual(o, objc.NSDecimal("0"))

        self.assertRaises(TypeError, operator.add, d1, 0.5)
        self.assertRaises(TypeError, operator.sub, d1, 0.5)
        self.assertRaises(TypeError, operator.mul, d1, 0.5)
        self.assertRaises(TypeError, operator.truediv, d1, 0.5)


    def test_inplace_ro(self):
        d1 = objc.NSDecimal("1.5")
        d2 = objc.NSDecimal("0.5")


        orig = d1
        d1 += d2
        self.assertEqual(d1, objc.NSDecimal("2.0"))
        self.assertEqual(orig, objc.NSDecimal("1.5"))

        d1 = orig
        d1 -= d2
        self.assertEqual(d1, objc.NSDecimal("1.0"))
        self.assertEqual(orig, objc.NSDecimal("1.5"))

        d1 = orig
        d1 /= d2
        self.assertEqual(d1, objc.NSDecimal("3.0"))
        self.assertEqual(orig, objc.NSDecimal("1.5"))

        d1 = orig
        d1 *= d2
        self.assertEqual(d1, objc.NSDecimal("0.75"))
        self.assertEqual(orig, objc.NSDecimal("1.5"))


class TestUsingNSDecimalNumber (TestCase):
    def test_creation(self):
        cls = objc.lookUpClass("NSDecimalNumber")

        d = objc.NSDecimal("1.5")

        n = cls.decimalNumberWithDecimal_(d)
        self.assertIsInstance(n, cls)
        self.assertEqual(str(n), str(d))

        n = cls.alloc().initWithDecimal_(d)
        self.assertIsInstance(n, cls)
        self.assertEqual(str(n), str(d))

        v = n.decimalValue()
        self.assertEqual(d, v)

class TestDecimalByReference (TestCase):
    def test_byref_in(self):
        d = objc.NSDecimal("1.5")

        o = OC_TestDecimal.alloc().init()
        self.assertArgIsIn(o.stringFromDecimal_, 0)
        r = o.stringFromDecimal_(d)

        self.assertIsInstance(r, unicode)
        self.assertEqual(r, "1.5")

    def test_byref_out(self):
        o = OC_TestDecimal.alloc().init()
        self.assertArgIsOut(o.getDecimal_, 0)
        r = o.getDecimal_(None)

        self.assertIsInstance(r, tuple)
        self.assertEqual(r[0], 1)
        d = r[1]
        self.assertIsInstance(d, objc.NSDecimal)
        self.assertEqual(str(d), "2.5")

    def test_byref_inout(self):
        d1 = objc.NSDecimal("1.25")
        o = OC_TestDecimal.alloc().init()
        self.assertArgIsInOut(o.doubleDecimal_, 0)

        d2 = o.doubleDecimal_(d1)
        self.assertIsNot(d1, d2)
        self.assertEqual(str(d1), "1.25")
        self.assertIsInstance(d2, objc.NSDecimal)
        self.assertEqual(str(d2), "2.5")

if __name__ == "__main__":
    main()
