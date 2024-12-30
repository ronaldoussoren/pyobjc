"""
Tests for the NSDecimal wrapper type
"""

import decimal
import warnings

import objc
from objc import super  # noqa: A004
from PyObjCTest.decimal import OC_TestDecimal
from PyObjCTools.TestSupport import TestCase, expectedFailure


class TestNSDecimalWrapper(TestCase):
    def test_creation(self):
        for value in (0, 5, (2**62) + 5):
            d = objc.NSDecimal(value)
            self.assertIsInstance(d, objc.NSDecimal)
            self.assertEqual(str(d), str(value))

            d = objc.NSDecimal(-value)
            self.assertIsInstance(d, objc.NSDecimal)
            self.assertEqual(str(d), str(-value))

        value = 2**63 + 2
        d = objc.NSDecimal(value)
        self.assertIsInstance(d, objc.NSDecimal)
        self.assertEqual(str(d), str(value))

        with self.assertRaisesRegex(OverflowError, "int too big to convert"):
            objc.NSDecimal(1 << 66)

        d = objc.NSDecimal(0.0)
        self.assertIsInstance(d, objc.NSDecimal)
        self.assertEqual(str(d), "0")

        d = objc.NSDecimal(0.5)
        self.assertIsInstance(d, objc.NSDecimal)
        self.assertEqual(str(d), "0.5")

        d = objc.NSDecimal("1.24")
        self.assertIsInstance(d, objc.NSDecimal)
        self.assertEqual(str(d), "1.24")

        d = objc.NSDecimal(500, 3, False)
        self.assertEqual(str(d), str(500 * 10**3))

        d = objc.NSDecimal(500, -6, True)
        self.assertEqual(str(d), str(500 * 10**-6 * -1))

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned long long', got 'str'"
        ):
            objc.NSDecimal("a", -6, True)

        with self.assertRaisesRegex(ValueError, "depythonifying 'short', got 'str'"):
            objc.NSDecimal(500, "a", True)

        with self.assertRaisesRegex(
            TypeError,
            r"NSDecimal\(value\) or NSDecimal\(mantissa, exponent, isNegative\)",
        ):
            objc.NSDecimal(500, -6, True, False)

        with self.assertRaisesRegex(
            TypeError, "cannot convert instance of NSObject to NSDecimal"
        ):
            objc.NSDecimal(objc.lookUpClass("NSObject").new())

        d = objc.NSDecimal("invalid")
        self.assertEqual(str(d), "NaN")

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
        self.assertTrue(d1 < d4)

        self.assertFalse(d1 > d1)
        self.assertFalse(d1 > d2)
        self.assertTrue(d1 > d3)
        self.assertFalse(d1 > d4)

        self.assertTrue(d1 >= d1)
        self.assertTrue(d1 >= d2)
        self.assertTrue(d1 >= d3)
        self.assertFalse(d1 >= d4)

        self.assertEqual(objc.NSDecimal("1.50"), objc.NSDecimal("1.500"))

        # Comparison with other types is possible when
        # they can be casted to NSDecimal without loosing
        # precision.
        d5 = objc.NSDecimal("5")
        i5 = 5
        f5 = 5.0
        D5 = decimal.Decimal(5)

        self.assertTrue(d5 == i5)
        self.assertTrue(d5 == f5)
        self.assertFalse(d5 == D5)
        self.assertFalse(d5 != i5)
        self.assertFalse(d5 != f5)
        self.assertTrue(d5 != D5)
        self.assertFalse(d5 < i5)
        self.assertFalse(d5 < f5)
        with self.assertRaisesRegex(
            TypeError, "Cannot compare NSDecimal and decimal.Decimal"
        ):
            d5 < D5  # noqa: B015
        self.assertFalse(d5 > i5)
        self.assertFalse(d5 > f5)
        with self.assertRaisesRegex(
            TypeError, "Cannot compare NSDecimal and decimal.Decimal"
        ):
            d5 > D5  # noqa: B015
        self.assertTrue(d5 >= i5)
        self.assertTrue(d5 >= f5)
        with self.assertRaisesRegex(
            TypeError, "Cannot compare NSDecimal and decimal.Decimal"
        ):
            d5 >= D5  # noqa: B015
        self.assertTrue(d5 <= i5)
        self.assertTrue(d5 <= f5)
        with self.assertRaisesRegex(
            TypeError, "Cannot compare NSDecimal and decimal.Decimal"
        ):
            d5 <= D5  # noqa: B015

    def test_hash(self):
        self.assertEqual(hash(objc.NSDecimal("1.50")), hash(objc.NSDecimal("1.500")))

    def test_conversion(self):
        d1 = objc.NSDecimal("1.5")
        d2 = objc.NSDecimal("25")

        self.assertEqual(d1.as_int(), 1)
        self.assertEqual(d2.as_int(), 25)

        self.assertEqual(d1.as_float(), 1.5)
        self.assertEqual(d2.as_float(), 25.0)

        with self.assertRaisesRegex(
            TypeError, r"int\(\) argument must .*, not 'objc.NSDecimal'"
        ):
            int(d1)
        with self.assertRaisesRegex(
            TypeError, r"float\(\) argument must be .*, not 'objc.NSDecimal'"
        ):
            float(d1)

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

        with self.assertRaisesRegex(
            TypeError, r"function takes at most 1 argument \(2 given\)"
        ):
            d1.__round__(1, 2)

    def test_pow(self):
        with self.assertRaisesRegex(
            TypeError, r"pow\(\) and \*\* are not supported for NSDecimal"
        ):
            pow(objc.NSDecimal("3.5"), 3, 1)
        with self.assertRaisesRegex(
            TypeError, r"pow\(\) and \*\* are not supported for NSDecimal"
        ):
            pow(objc.NSDecimal("3.5"), 3)
        with self.assertRaisesRegex(
            TypeError, r"pow\(\) and \*\* are not supported for NSDecimal"
        ):
            objc.NSDecimal("3.5") ** 3
        with self.assertRaisesRegex(
            TypeError, r"pow\(\) and \*\* are not supported for NSDecimal"
        ):
            objc.NSDecimal("3.5") ** objc.NSDecimal("2")

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

        with self.assertRaisesRegex(OverflowError, "Numeric overflow"):
            prod = d1
            for _ in range(10):
                prod = prod * prod

        with self.assertRaisesRegex(ZeroDivisionError, "Division by zero"):
            objc.NSDecimal(1) / 0

        with self.assertRaisesRegex(
            TypeError,
            r"unsupported operand type\(s\) for \+: 'objc.NSDecimal' and 'float'",
        ):
            d1 + 0.5
        with self.assertRaisesRegex(
            TypeError,
            r"unsupported operand type\(s\) for -: 'objc.NSDecimal' and 'float'",
        ):
            d1 - 0.5
        with self.assertRaisesRegex(
            TypeError,
            r"unsupported operand type\(s\) for \*: 'objc.NSDecimal' and 'float'",
        ):
            d1 * 0.5
        with self.assertRaisesRegex(
            TypeError,
            r"unsupported operand type\(s\) for /: 'objc.NSDecimal' and 'float'",
        ):
            d1 / 0.5

        with self.assertRaisesRegex(
            TypeError,
            r"unsupported operand type\(s\) for \+: 'float' and 'objc.NSDecimal'",
        ):
            0.5 + d1
        with self.assertRaisesRegex(
            TypeError,
            r"unsupported operand type\(s\) for -: 'float' and 'objc.NSDecimal'",
        ):
            0.5 - d1
        with self.assertRaisesRegex(
            TypeError,
            r"unsupported operand type\(s\) for \*: 'float' and 'objc.NSDecimal'",
        ):
            0.5 * d1
        with self.assertRaisesRegex(
            TypeError,
            r"unsupported operand type\(s\) for /: 'float' and 'objc.NSDecimal'",
        ):
            0.5 / d1

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


class TestUsingNSDecimalNumber(TestCase):
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
        self.assertIsInstance(v, objc.NSDecimal)
        self.assertEqual(d, v)

        v2 = objc.NSDecimal(n)
        self.assertIsInstance(v2, objc.NSDecimal)
        self.assertEqual(d, v2)
        self.assertEqual(v, v2)

        with self.assertRaisesRegex(TypeError, "expected 1 arguments, got 2"):
            cls.decimalNumberWithDecimal_(d, 1)

        with self.assertRaisesRegex(
            TypeError, "Expecting an NSDecimal, got instance of 'str'"
        ):
            cls.decimalNumberWithDecimal_("42.5")

        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=objc.UninitializedDeallocWarning)

            with self.assertRaisesRegex(TypeError, "expected 1 arguments, got 2"):
                cls.alloc().initWithDecimal_(d, 1)

            with self.assertRaisesRegex(
                TypeError, "Expecting an NSDecimal, got instance of 'str'"
            ):
                cls.alloc().initWithDecimal_("42.5")

    @expectedFailure
    def test_subclassing(self):
        # At least on macOS 13 subclassing of NSDecimalNumber basically doesn't work,
        # leaving the test here as a reminder of that.
        NSDecimalNumber = objc.lookUpClass("NSDecimalNumber")

        class OC_DecimalNumberPlusOne(NSDecimalNumber):
            @objc.objc_method(signature=NSDecimalNumber.initWithDecimal_.signature)
            def initWithDecimal_(self, value):
                return super().initWithDecimal_(value)

            def decimalValue(self):
                return super().decimalValue() + 1

        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=objc.UninitializedDeallocWarning)
            o = OC_DecimalNumberPlusOne.alloc().initWithDecimal_(objc.NSDecimal("1.5"))
            v = objc.NSDecimal(o)
            print(v)


class TestDecimalByReference(TestCase):
    def test_byref_in(self):
        d = objc.NSDecimal("1.5")

        o = OC_TestDecimal.alloc().init()
        self.assertArgIsIn(o.stringFromDecimal_, 0)
        r = o.stringFromDecimal_(d)

        self.assertIsInstance(r, str)
        self.assertEqual(r, "1.5")

        with self.assertRaisesRegex(
            TypeError, "Expecting an NSDecimal, got instance of 'str'"
        ):
            o.stringFromDecimal_("42.5")

    def test_byref_out(self):
        o = OC_TestDecimal.alloc().init()
        self.assertArgIsOut(o.getDecimal_, 0)
        r = o.getDecimal_(None)

        self.assertIsInstance(r, tuple)
        self.assertEqual(r[0], 1)
        d = r[1]
        self.assertIsInstance(d, objc.NSDecimal)
        self.assertEqual(str(d), "2.5")

        objc._updatingMetadata(True)
        objc.registerMetaDataForSelector(
            b"OC_TestDecimal",
            b"getDecimal:",
            {
                "arguments": {
                    2
                    + 0: {
                        "type_modifier": objc._C_OUT,
                        "type": b"^{_NSDecimal=b8b4b1b1b18[8S]}",
                        "null_accepted": False,
                    }
                }
            },
        )
        objc._updatingMetadata(False)
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

    def test_to_id(self):
        v = objc.NSDecimal("2.75")
        a = objc.lookUpClass("NSArray").arrayWithArray_([v])

        o = a[0]
        self.assertIsInstance(o, objc.lookUpClass("NSDecimalNumber"))
        self.assertEqual(o, v)

        b = objc.NSDecimal(o)
        self.assertIsInstance(b, objc.NSDecimal)
        self.assertIsNot(b, v)
        self.assertEqual(b, v)

    def test_create_no_args(self):
        v = objc.NSDecimal()
        self.assertEqual(v, objc.NSDecimal("0.0"))

    def test_bool_context(self):
        v = objc.NSDecimal("0")
        self.assertIs(bool(v), False)

        v = objc.NSDecimal("0.0001")
        self.assertIs(bool(v), True)
