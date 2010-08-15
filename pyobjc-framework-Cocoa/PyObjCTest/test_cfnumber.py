from PyObjCTools.TestSupport import *
import sys
from CoreFoundation import *

class TestCFNumber (TestCase):
    def testCFNumberGetValue(self):
        number = 42

        ok, v = CFNumberGetValue(number, kCFNumberSInt8Type, None);
        self.assert_(ok)
        self.assert_(isinstance(v, (int, long)))
        self.assertEqual(v, 42)

        ok, v = CFNumberGetValue(number, kCFNumberSInt16Type, None);
        self.assert_(ok)
        self.assert_(isinstance(v, (int, long)))
        self.assertEqual(v, 42)

        ok, v = CFNumberGetValue(number, kCFNumberSInt32Type, None);
        self.assert_(ok)
        self.assert_(isinstance(v, (int, long)))
        self.assertEqual(v, 42)

        ok, v = CFNumberGetValue(number, kCFNumberSInt64Type, None);
        self.assert_(ok)
        self.assert_(isinstance(v, (int, long)))
        self.assertEqual(v, 42)

        ok, v = CFNumberGetValue(number, kCFNumberCharType, None);
        self.assert_(ok)
        self.assert_(isinstance(v, (int, long)))
        self.assertEqual(v, 42)

        ok, v = CFNumberGetValue(number, kCFNumberShortType, None);
        self.assert_(ok)
        self.assert_(isinstance(v, (int, long)))
        self.assertEqual(v, 42)

        ok, v = CFNumberGetValue(number, kCFNumberIntType, None);
        self.assert_(ok)
        self.assert_(isinstance(v, (int, long)))
        self.assertEqual(v, 42)

        ok, v = CFNumberGetValue(number, kCFNumberLongType, None);
        self.assert_(ok)
        self.assert_(isinstance(v, (int, long)))
        self.assertEqual(v, 42)

        ok, v = CFNumberGetValue(number, kCFNumberLongLongType, None);
        self.assert_(ok)
        self.assert_(isinstance(v, (int, long)))
        self.assertEqual(v, 42)

        ok, v = CFNumberGetValue(number, kCFNumberCFIndexType, None);
        self.assert_(ok)
        self.assert_(isinstance(v, (int, long)))
        self.assertEqual(v, 42)

        ok, v = CFNumberGetValue(number, kCFNumberFloat32Type, None)
        self.assert_(ok)
        self.assert_(isinstance(v, float))
        self.assertEqual(v, 42.0)

        ok, v = CFNumberGetValue(number, kCFNumberFloat64Type, None)
        self.assert_(ok)
        self.assert_(isinstance(v, float))
        self.assertEqual(v, 42.0)

        ok, v = CFNumberGetValue(number, kCFNumberFloatType, None)
        self.assert_(ok)
        self.assert_(isinstance(v, float))
        self.assertEqual(v, 42.0)

        ok, v = CFNumberGetValue(number, kCFNumberDoubleType, None)
        self.assert_(ok)
        self.assert_(isinstance(v, float))
        self.assertEqual(v, 42.0)

        ## Don't test this, the wrapper shouldn't range-check 
        ## arguments and CFNumberGetValue will crash when the
        ## number type is invalid
        #ok, v = CFNumberGetValue(number, kCFNumberMaxType+2)
        #self.assert_(not ok)

    def testBoolean(self):
        self.assertIsInstance(CFBooleanGetTypeID(), (int, long))
        self.assertIs(CFBooleanGetValue(kCFBooleanTrue), True)
        self.assertIs(CFBooleanGetValue(kCFBooleanFalse), False)
        self.assertTrue(CFBooleanGetValue(True))
        self.assertFalse(CFBooleanGetValue(False))

    def no_testNumber(self):
        self.assertIsInstance(CFNumberGetTypeID(), (int, long))
        # Add cases for all number types
        num = CFNumberCreate(None, kCFNumberSInt8Type, 1)
        self.assertIsInstance(num, CFNumberRef)
        self.assertFalse(CFNumberIsFloatType(num))
        self.assertEqual(num , 1)
        num = CFNumberCreate(None, kCFNumberSInt8Type, 1)
        self.assertIsInstance(num, CFNumberRef)
        self.assertFalse(CFNumberIsFloatType(num))
        self.assertEqual(num , 1)
        num = CFNumberCreate(None, kCFNumberSInt16Type, 1)
        self.assertIsInstance(num, CFNumberRef)
        self.assertFalse(CFNumberIsFloatType(num))
        self.assertEqual(num , 1)
        num = CFNumberCreate(None, kCFNumberSInt32Type, 1)
        self.assertIsInstance(num, CFNumberRef)
        self.assertFalse(CFNumberIsFloatType(num))
        self.assertEqual(num , 1)
        num = CFNumberCreate(None, kCFNumberSInt64Type, 1)
        self.assertIsInstance(num, CFNumberRef)
        self.assertFalse(CFNumberIsFloatType(num))
        self.assertEqual(num , 1)
        num = CFNumberCreate(None, kCFNumberFloat32Type, 1)
        self.assertIsInstance(num, CFNumberRef)
        self.assertTrue(CFNumberIsFloatType(num))
        self.assertEqual(num , 1)
        num = CFNumberCreate(None, kCFNumberFloat64Type, 1)
        self.assertIsInstance(num, CFNumberRef)
        self.assertTrue(CFNumberIsFloatType(num))
        self.assertEqual(num , 1)
        num = CFNumberCreate(None, kCFNumberCharType, 1)
        self.assertIsInstance(num, CFNumberRef)
        self.assertFalse(CFNumberIsFloatType(num))
        self.assertEqual(num , 1)
        num = CFNumberCreate(None, kCFNumberShortType, 1)
        self.assertIsInstance(num, CFNumberRef)
        self.assertFalse(CFNumberIsFloatType(num))
        self.assertEqual(num , 1)
        num = CFNumberCreate(None, kCFNumberIntType, 1)
        self.assertIsInstance(num, CFNumberRef)
        self.assertFalse(CFNumberIsFloatType(num))
        self.assertEqual(num , 1)
        num = CFNumberCreate(None, kCFNumberLongType, 1)
        self.assertIsInstance(num, CFNumberRef)
        self.assertFalse(CFNumberIsFloatType(num))
        self.assertEqual(num , 1)
        num = CFNumberCreate(None, kCFNumberLongLongType, 1)
        self.assertIsInstance(num, CFNumberRef)
        self.assertFalse(CFNumberIsFloatType(num))
        self.assertEqual(num , 1)
        num = CFNumberCreate(None, kCFNumberFloatType, 1)
        self.assertIsInstance(num, CFNumberRef)
        self.assertTrue(CFNumberIsFloatType(num))
        self.assertEqual(num , 1)
        num = CFNumberCreate(None, kCFNumberDoubleType, 1)
        self.assertIsInstance(num, CFNumberRef)
        self.assertTrue(CFNumberIsFloatType(num))
        self.assertEqual(num , 1)
        num = CFNumberCreate(None, kCFNumberCFIndexType, 1)
        self.assertIsInstance(num, CFNumberRef)
        self.assertFalse(CFNumberIsFloatType(num))
        self.assertEqual(num , 1)
        num = CFNumberCreate(None, kCFNumberNSIntegerType, 1)
        self.assertIsInstance(num, CFNumberRef)
        self.assertFalse(CFNumberIsFloatType(num))
        self.assertEqual(num , 1)
        num = CFNumberCreate(None, kCFNumberCGFloatType, 1)
        self.assertIsInstance(num, CFNumberRef)
        self.assertTrue(CFNumberIsFloatType(num))
        self.assertEqual(num , 1)

    def testNumberTypes(self):
        v = CFNumberGetType(44)
        self.assertIsIn(v, (kCFNumberLongLongType, kCFNumberLongType))
        v = CFNumberGetType(2.5)
        self.assertEqual(v , kCFNumberDoubleType)
        v = CFNumberGetByteSize(44)

        if sys.maxint >= 2**32:
            self.assertEqual(v , 8)
        else:
            self.assertEqual(v , 4)
        v = CFNumberGetByteSize(44.0)
        self.assertEqual(v , 8)
        self.assertFalse(CFNumberIsFloatType(44))
        self.assertTrue(CFNumberIsFloatType(1.0))

        r = CFNumberCompare(44, 45, 0)
        self.assertLessThan(r , 0)
    def testConstants(self):
        self.assertIs(kCFBooleanTrue, True)
        self.assertIs(kCFBooleanFalse, False)
        self.assertEqual(kCFNumberSInt8Type , 1)
        self.assertEqual(kCFNumberSInt16Type , 2)
        self.assertEqual(kCFNumberSInt32Type , 3)
        self.assertEqual(kCFNumberSInt64Type , 4)
        self.assertEqual(kCFNumberFloat32Type , 5)
        self.assertEqual(kCFNumberFloat64Type , 6)
        self.assertEqual(kCFNumberCharType , 7)
        self.assertEqual(kCFNumberShortType , 8)
        self.assertEqual(kCFNumberIntType , 9)
        self.assertEqual(kCFNumberLongType , 10)
        self.assertEqual(kCFNumberLongLongType , 11)
        self.assertEqual(kCFNumberFloatType , 12)
        self.assertEqual(kCFNumberDoubleType , 13)
        self.assertEqual(kCFNumberCFIndexType , 14)
        self.assertEqual(kCFNumberNSIntegerType , 15)
        self.assertEqual(kCFNumberCGFloatType , 16)
        self.assertEqual(kCFNumberMaxType , 16)
        self.assertIsInstance(kCFNumberPositiveInfinity, float)
        self.assertIsInstance(kCFNumberNegativeInfinity, float)
        self.assertIsInstance(kCFNumberNaN, float)
if __name__ == "__main__":
    main()
