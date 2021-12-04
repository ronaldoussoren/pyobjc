import CoreFoundation
from PyObjCTools.TestSupport import TestCase


class TestCFNumber(TestCase):
    def testCFNumberGetValue(self):
        number = 42

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

    def testBoolean(self):
        self.assertIsInstance(CoreFoundation.CFBooleanGetTypeID(), int)
        self.assertIs(
            CoreFoundation.CFBooleanGetValue(CoreFoundation.kCFBooleanTrue), True
        )
        self.assertIs(
            CoreFoundation.CFBooleanGetValue(CoreFoundation.kCFBooleanFalse), False
        )
        self.assertTrue(CoreFoundation.CFBooleanGetValue(True))
        self.assertFalse(CoreFoundation.CFBooleanGetValue(False))

    def no_testNumber(self):
        self.assertIsInstance(CoreFoundation.CFNumberGetTypeID(), int)
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

    def testNumberTypes(self):
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

    def testConstants(self):
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
