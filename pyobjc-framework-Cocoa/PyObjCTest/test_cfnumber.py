import CoreFoundation
import Foundation
from PyObjCTools.TestSupport import TestCase, NoObjCClass


class TestCFNumber(TestCase):
    def test_cfnumber_get_value(self):
        number = 42

        with self.assertRaisesRegex(TypeError, "expected 3 arguments, got 0"):
            CoreFoundation.CFNumberGetValue()

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            CoreFoundation.CFNumberGetValue(
                NoObjCClass(), CoreFoundation.kCFNumberSInt8Type, None
            )
        with self.assertRaisesRegex(
            ValueError, "depythonifying 'long long', got 'str'"
        ):
            CoreFoundation.CFNumberGetValue(number, "byte", None)
        with self.assertRaisesRegex(ValueError, "'buffer' must be None"):
            CoreFoundation.CFNumberGetValue(
                number, CoreFoundation.kCFNumberSInt8Type, bytearray(4)
            )
        with self.assertRaisesRegex(ValueError, "invalid CFNumberType value"):
            CoreFoundation.CFNumberGetValue(number, -1, None)

        ok, v = CoreFoundation.CFNumberGetValue(
            number, CoreFoundation.kCFNumberSInt8Type, None
        )
        self.assertTrue(ok)
        self.assertTrue(isinstance(v, int))
        self.assertEqual(v, 42)

        ok, v = CoreFoundation.CFNumberGetValue(
            number, CoreFoundation.kCFNumberSInt16Type, None
        )
        self.assertTrue(ok)
        self.assertTrue(isinstance(v, int))
        self.assertEqual(v, 42)

        ok, v = CoreFoundation.CFNumberGetValue(
            number, CoreFoundation.kCFNumberSInt32Type, None
        )
        self.assertTrue(ok)
        self.assertTrue(isinstance(v, int))
        self.assertEqual(v, 42)

        ok, v = CoreFoundation.CFNumberGetValue(
            number, CoreFoundation.kCFNumberSInt64Type, None
        )
        self.assertTrue(ok)
        self.assertTrue(isinstance(v, int))
        self.assertEqual(v, 42)

        ok, v = CoreFoundation.CFNumberGetValue(
            number, CoreFoundation.kCFNumberCharType, None
        )
        self.assertTrue(ok)
        self.assertTrue(isinstance(v, int))
        self.assertEqual(v, 42)

        ok, v = CoreFoundation.CFNumberGetValue(
            number, CoreFoundation.kCFNumberShortType, None
        )
        self.assertTrue(ok)
        self.assertTrue(isinstance(v, int))
        self.assertEqual(v, 42)

        ok, v = CoreFoundation.CFNumberGetValue(
            number, CoreFoundation.kCFNumberIntType, None
        )
        self.assertTrue(ok)
        self.assertTrue(isinstance(v, int))
        self.assertEqual(v, 42)

        ok, v = CoreFoundation.CFNumberGetValue(
            number, CoreFoundation.kCFNumberLongType, None
        )
        self.assertTrue(ok)
        self.assertTrue(isinstance(v, int))
        self.assertEqual(v, 42)

        ok, v = CoreFoundation.CFNumberGetValue(
            number, CoreFoundation.kCFNumberNSIntegerType, None
        )
        self.assertTrue(ok)
        self.assertTrue(isinstance(v, int))
        self.assertEqual(v, 42)

        ok, v = CoreFoundation.CFNumberGetValue(
            number, CoreFoundation.kCFNumberLongLongType, None
        )
        self.assertTrue(ok)
        self.assertTrue(isinstance(v, int))
        self.assertEqual(v, 42)

        ok, v = CoreFoundation.CFNumberGetValue(
            number, CoreFoundation.kCFNumberCFIndexType, None
        )
        self.assertTrue(ok)
        self.assertTrue(isinstance(v, int))
        self.assertEqual(v, 42)

        ok, v = CoreFoundation.CFNumberGetValue(
            number, CoreFoundation.kCFNumberFloat32Type, None
        )
        self.assertTrue(ok)
        self.assertTrue(isinstance(v, float))
        self.assertEqual(v, 42.0)

        ok, v = CoreFoundation.CFNumberGetValue(
            number, CoreFoundation.kCFNumberFloat64Type, None
        )
        self.assertTrue(ok)
        self.assertTrue(isinstance(v, float))
        self.assertEqual(v, 42.0)

        ok, v = CoreFoundation.CFNumberGetValue(
            number, CoreFoundation.kCFNumberFloatType, None
        )
        self.assertTrue(ok)
        self.assertTrue(isinstance(v, float))
        self.assertEqual(v, 42.0)

        ok, v = CoreFoundation.CFNumberGetValue(
            number, CoreFoundation.kCFNumberDoubleType, None
        )
        self.assertTrue(ok)
        self.assertTrue(isinstance(v, float))
        self.assertEqual(v, 42.0)

        ok, v = CoreFoundation.CFNumberGetValue(
            number, CoreFoundation.kCFNumberCGFloatType, None
        )
        self.assertTrue(ok)
        self.assertTrue(isinstance(v, float))
        self.assertEqual(v, 42.0)

        ok, v = CoreFoundation.CFNumberGetValue(
            Foundation.NSNumber.numberWithDouble_(50.5),
            CoreFoundation.kCFNumberShortType,
            None,
        )
        self.assertFalse(ok)
        self.assertIs(v, None)

    def test_boolean(self):
        self.assertIsInstance(CoreFoundation.CFBooleanGetTypeID(), int)
        self.assertIs(
            CoreFoundation.CFBooleanGetValue(CoreFoundation.kCFBooleanTrue), True
        )
        self.assertIs(
            CoreFoundation.CFBooleanGetValue(CoreFoundation.kCFBooleanFalse), False
        )
        self.assertTrue(CoreFoundation.CFBooleanGetValue(True))
        self.assertFalse(CoreFoundation.CFBooleanGetValue(False))

    def test_creation(self):
        self.assertIsInstance(CoreFoundation.CFNumberGetTypeID(), int)

        with self.assertRaisesRegex(TypeError, "expected 3 arguments, got 0"):
            CoreFoundation.CFNumberCreate()

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            CoreFoundation.CFNumberCreate(
                NoObjCClass(), CoreFoundation.kCFNumberSInt8Type, 1
            )

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'long long', got 'str'"
        ):
            CoreFoundation.CFNumberCreate(None, "int", 1)
        with self.assertRaisesRegex(ValueError, "depythonifying 'char', got 'str'"):
            CoreFoundation.CFNumberCreate(
                None, CoreFoundation.kCFNumberSInt8Type, "one"
            )

        # Add cases for all number types
        num = CoreFoundation.CFNumberCreate(None, CoreFoundation.kCFNumberSInt8Type, 1)
        self.assertIsInstance(num, CoreFoundation.CFNumberRef)
        self.assertFalse(CoreFoundation.CFNumberIsFloatType(num))
        self.assertEqual(num, 1)
        num = CoreFoundation.CFNumberCreate(None, CoreFoundation.kCFNumberSInt8Type, 1)
        self.assertIsInstance(num, CoreFoundation.CFNumberRef)
        self.assertFalse(CoreFoundation.CFNumberIsFloatType(num))
        self.assertEqual(num, 1)
        num = CoreFoundation.CFNumberCreate(None, CoreFoundation.kCFNumberSInt16Type, 1)
        self.assertIsInstance(num, CoreFoundation.CFNumberRef)
        self.assertFalse(CoreFoundation.CFNumberIsFloatType(num))
        self.assertEqual(num, 1)
        num = CoreFoundation.CFNumberCreate(None, CoreFoundation.kCFNumberSInt32Type, 1)
        self.assertIsInstance(num, CoreFoundation.CFNumberRef)
        self.assertFalse(CoreFoundation.CFNumberIsFloatType(num))
        self.assertEqual(num, 1)
        num = CoreFoundation.CFNumberCreate(None, CoreFoundation.kCFNumberSInt64Type, 1)
        self.assertIsInstance(num, CoreFoundation.CFNumberRef)
        self.assertFalse(CoreFoundation.CFNumberIsFloatType(num))
        self.assertEqual(num, 1)
        num = CoreFoundation.CFNumberCreate(
            None, CoreFoundation.kCFNumberFloat32Type, 1
        )
        self.assertIsInstance(num, CoreFoundation.CFNumberRef)
        self.assertTrue(CoreFoundation.CFNumberIsFloatType(num))
        self.assertEqual(num, 1)
        num = CoreFoundation.CFNumberCreate(
            None, CoreFoundation.kCFNumberFloat64Type, 1
        )
        self.assertIsInstance(num, CoreFoundation.CFNumberRef)
        self.assertTrue(CoreFoundation.CFNumberIsFloatType(num))
        self.assertEqual(num, 1)
        num = CoreFoundation.CFNumberCreate(None, CoreFoundation.kCFNumberCharType, 1)
        self.assertIsInstance(num, CoreFoundation.CFNumberRef)
        self.assertFalse(CoreFoundation.CFNumberIsFloatType(num))
        self.assertEqual(num, 1)
        num = CoreFoundation.CFNumberCreate(None, CoreFoundation.kCFNumberShortType, 1)
        self.assertIsInstance(num, CoreFoundation.CFNumberRef)
        self.assertFalse(CoreFoundation.CFNumberIsFloatType(num))
        self.assertEqual(num, 1)
        num = CoreFoundation.CFNumberCreate(None, CoreFoundation.kCFNumberIntType, 1)
        self.assertIsInstance(num, CoreFoundation.CFNumberRef)
        self.assertFalse(CoreFoundation.CFNumberIsFloatType(num))
        self.assertEqual(num, 1)
        num = CoreFoundation.CFNumberCreate(None, CoreFoundation.kCFNumberLongType, 1)
        self.assertIsInstance(num, CoreFoundation.CFNumberRef)
        self.assertFalse(CoreFoundation.CFNumberIsFloatType(num))
        self.assertEqual(num, 1)
        num = CoreFoundation.CFNumberCreate(
            None, CoreFoundation.kCFNumberLongLongType, 1
        )
        self.assertIsInstance(num, CoreFoundation.CFNumberRef)
        self.assertFalse(CoreFoundation.CFNumberIsFloatType(num))
        self.assertEqual(num, 1)
        num = CoreFoundation.CFNumberCreate(None, CoreFoundation.kCFNumberFloatType, 1)
        self.assertIsInstance(num, CoreFoundation.CFNumberRef)
        self.assertTrue(CoreFoundation.CFNumberIsFloatType(num))
        self.assertEqual(num, 1)
        num = CoreFoundation.CFNumberCreate(None, CoreFoundation.kCFNumberDoubleType, 1)
        self.assertIsInstance(num, CoreFoundation.CFNumberRef)
        self.assertTrue(CoreFoundation.CFNumberIsFloatType(num))
        self.assertEqual(num, 1)
        num = CoreFoundation.CFNumberCreate(
            None, CoreFoundation.kCFNumberCFIndexType, 1
        )
        self.assertIsInstance(num, CoreFoundation.CFNumberRef)
        self.assertFalse(CoreFoundation.CFNumberIsFloatType(num))
        self.assertEqual(num, 1)
        num = CoreFoundation.CFNumberCreate(
            None, CoreFoundation.kCFNumberNSIntegerType, 1
        )
        self.assertIsInstance(num, CoreFoundation.CFNumberRef)
        self.assertFalse(CoreFoundation.CFNumberIsFloatType(num))
        self.assertEqual(num, 1)
        num = CoreFoundation.CFNumberCreate(
            None, CoreFoundation.kCFNumberCGFloatType, 1
        )
        self.assertIsInstance(num, CoreFoundation.CFNumberRef)
        self.assertTrue(CoreFoundation.CFNumberIsFloatType(num))
        self.assertEqual(num, 1)

        with self.assertRaisesRegex(ValueError, "number type not supported"):
            CoreFoundation.CFNumberCreate(None, -1, 1)

    def test_number_types(self):
        v = CoreFoundation.CFNumberGetType(44)
        self.assertIn(
            v, (CoreFoundation.kCFNumberLongLongType, CoreFoundation.kCFNumberLongType)
        )
        v = CoreFoundation.CFNumberGetType(2.5)
        self.assertEqual(v, CoreFoundation.kCFNumberDoubleType)
        v = CoreFoundation.CFNumberGetByteSize(44)

        self.assertEqual(v, 8)

        v = CoreFoundation.CFNumberGetByteSize(44.0)
        self.assertEqual(v, 8)
        self.assertFalse(CoreFoundation.CFNumberIsFloatType(44))
        self.assertTrue(CoreFoundation.CFNumberIsFloatType(1.0))

        r = CoreFoundation.CFNumberCompare(44, 45, 0)
        self.assertLess(r, 0)

    def test_constants(self):
        self.assertIs(CoreFoundation.kCFBooleanTrue, True)
        self.assertIs(CoreFoundation.kCFBooleanFalse, False)
        self.assertEqual(CoreFoundation.kCFNumberSInt8Type, 1)
        self.assertEqual(CoreFoundation.kCFNumberSInt16Type, 2)
        self.assertEqual(CoreFoundation.kCFNumberSInt32Type, 3)
        self.assertEqual(CoreFoundation.kCFNumberSInt64Type, 4)
        self.assertEqual(CoreFoundation.kCFNumberFloat32Type, 5)
        self.assertEqual(CoreFoundation.kCFNumberFloat64Type, 6)
        self.assertEqual(CoreFoundation.kCFNumberCharType, 7)
        self.assertEqual(CoreFoundation.kCFNumberShortType, 8)
        self.assertEqual(CoreFoundation.kCFNumberIntType, 9)
        self.assertEqual(CoreFoundation.kCFNumberLongType, 10)
        self.assertEqual(CoreFoundation.kCFNumberLongLongType, 11)
        self.assertEqual(CoreFoundation.kCFNumberFloatType, 12)
        self.assertEqual(CoreFoundation.kCFNumberDoubleType, 13)
        self.assertEqual(CoreFoundation.kCFNumberCFIndexType, 14)
        self.assertEqual(CoreFoundation.kCFNumberNSIntegerType, 15)
        self.assertEqual(CoreFoundation.kCFNumberCGFloatType, 16)
        self.assertEqual(CoreFoundation.kCFNumberMaxType, 16)
        self.assertIsInstance(CoreFoundation.kCFNumberPositiveInfinity, float)
        self.assertIsInstance(CoreFoundation.kCFNumberNegativeInfinity, float)
        self.assertIsInstance(CoreFoundation.kCFNumberNaN, float)
