from PyObjCTools.TestSupport import *
import sys
from CoreFoundation import *

class TestCFNumber (TestCase):
    def testCFNumberGetValue(self):
        number = 42

        ok, v = CFNumberGetValue(number, kCFNumberSInt8Type, None);
        self.assert_(ok)
        self.assert_(isinstance(v, (int, long)))
        self.assertEquals(v, 42)

        ok, v = CFNumberGetValue(number, kCFNumberSInt16Type, None);
        self.assert_(ok)
        self.assert_(isinstance(v, (int, long)))
        self.assertEquals(v, 42)

        ok, v = CFNumberGetValue(number, kCFNumberSInt32Type, None);
        self.assert_(ok)
        self.assert_(isinstance(v, (int, long)))
        self.assertEquals(v, 42)

        ok, v = CFNumberGetValue(number, kCFNumberSInt64Type, None);
        self.assert_(ok)
        self.assert_(isinstance(v, (int, long)))
        self.assertEquals(v, 42)

        ok, v = CFNumberGetValue(number, kCFNumberCharType, None);
        self.assert_(ok)
        self.assert_(isinstance(v, (int, long)))
        self.assertEquals(v, 42)

        ok, v = CFNumberGetValue(number, kCFNumberShortType, None);
        self.assert_(ok)
        self.assert_(isinstance(v, (int, long)))
        self.assertEquals(v, 42)

        ok, v = CFNumberGetValue(number, kCFNumberIntType, None);
        self.assert_(ok)
        self.assert_(isinstance(v, (int, long)))
        self.assertEquals(v, 42)

        ok, v = CFNumberGetValue(number, kCFNumberLongType, None);
        self.assert_(ok)
        self.assert_(isinstance(v, (int, long)))
        self.assertEquals(v, 42)

        ok, v = CFNumberGetValue(number, kCFNumberLongLongType, None);
        self.assert_(ok)
        self.assert_(isinstance(v, (int, long)))
        self.assertEquals(v, 42)

        ok, v = CFNumberGetValue(number, kCFNumberCFIndexType, None);
        self.assert_(ok)
        self.assert_(isinstance(v, (int, long)))
        self.assertEquals(v, 42)

        ok, v = CFNumberGetValue(number, kCFNumberFloat32Type, None)
        self.assert_(ok)
        self.assert_(isinstance(v, float))
        self.assertEquals(v, 42.0)

        ok, v = CFNumberGetValue(number, kCFNumberFloat64Type, None)
        self.assert_(ok)
        self.assert_(isinstance(v, float))
        self.assertEquals(v, 42.0)

        ok, v = CFNumberGetValue(number, kCFNumberFloatType, None)
        self.assert_(ok)
        self.assert_(isinstance(v, float))
        self.assertEquals(v, 42.0)

        ok, v = CFNumberGetValue(number, kCFNumberDoubleType, None)
        self.assert_(ok)
        self.assert_(isinstance(v, float))
        self.assertEquals(v, 42.0)

        ## Don't test this, the wrapper shouldn't range-check 
        ## arguments and CFNumberGetValue will crash when the
        ## number type is invalid
        #ok, v = CFNumberGetValue(number, kCFNumberMaxType+2)
        #self.assert_(not ok)

    def testBoolean(self):
        self.failUnless(isinstance(CFBooleanGetTypeID(), (int, long)))

        self.failUnless(CFBooleanGetValue(kCFBooleanTrue) is True)
        self.failUnless(CFBooleanGetValue(kCFBooleanFalse) is False)
        self.failUnless(CFBooleanGetValue(True))
        self.failIf(CFBooleanGetValue(False))

    def no_testNumber(self):
        self.failUnless(isinstance(CFNumberGetTypeID(), (int, long)))

        # Add cases for all number types
        num = CFNumberCreate(None, kCFNumberSInt8Type, 1)
        self.failUnless(isinstance(num, CFNumberRef))
        self.failIf(CFNumberIsFloatType(num))
        self.failUnless(num == 1)
        
        num = CFNumberCreate(None, kCFNumberSInt8Type, 1)
        self.failUnless(isinstance(num, CFNumberRef))
        self.failIf(CFNumberIsFloatType(num))
        self.failUnless(num == 1)

        num = CFNumberCreate(None, kCFNumberSInt16Type, 1)
        self.failUnless(isinstance(num, CFNumberRef))
        self.failIf(CFNumberIsFloatType(num))
        self.failUnless(num == 1)

        num = CFNumberCreate(None, kCFNumberSInt32Type, 1)
        self.failUnless(isinstance(num, CFNumberRef))
        self.failIf(CFNumberIsFloatType(num))
        self.failUnless(num == 1)

        num = CFNumberCreate(None, kCFNumberSInt64Type, 1)
        self.failUnless(isinstance(num, CFNumberRef))
        self.failIf(CFNumberIsFloatType(num))
        self.failUnless(num == 1)

        num = CFNumberCreate(None, kCFNumberFloat32Type, 1)
        self.failUnless(isinstance(num, CFNumberRef))
        self.failUnless(CFNumberIsFloatType(num))
        self.failUnless(num == 1)

        num = CFNumberCreate(None, kCFNumberFloat64Type, 1)
        self.failUnless(isinstance(num, CFNumberRef))
        self.failUnless(CFNumberIsFloatType(num))
        self.failUnless(num == 1)

        num = CFNumberCreate(None, kCFNumberCharType, 1)
        self.failUnless(isinstance(num, CFNumberRef))
        self.failIf(CFNumberIsFloatType(num))
        self.failUnless(num == 1)

        num = CFNumberCreate(None, kCFNumberShortType, 1)
        self.failUnless(isinstance(num, CFNumberRef))
        self.failIf(CFNumberIsFloatType(num))
        self.failUnless(num == 1)

        num = CFNumberCreate(None, kCFNumberIntType, 1)
        self.failUnless(isinstance(num, CFNumberRef))
        self.failIf(CFNumberIsFloatType(num))
        self.failUnless(num == 1)

        num = CFNumberCreate(None, kCFNumberLongType, 1)
        self.failUnless(isinstance(num, CFNumberRef))
        self.failIf(CFNumberIsFloatType(num))
        self.failUnless(num == 1)

        num = CFNumberCreate(None, kCFNumberLongLongType, 1)
        self.failUnless(isinstance(num, CFNumberRef))
        self.failIf(CFNumberIsFloatType(num))
        self.failUnless(num == 1)

        num = CFNumberCreate(None, kCFNumberFloatType, 1)
        self.failUnless(isinstance(num, CFNumberRef))
        self.failUnless(CFNumberIsFloatType(num))
        self.failUnless(num == 1)

        num = CFNumberCreate(None, kCFNumberDoubleType, 1)
        self.failUnless(isinstance(num, CFNumberRef))
        self.failUnless(CFNumberIsFloatType(num))
        self.failUnless(num == 1)

        num = CFNumberCreate(None, kCFNumberCFIndexType, 1)
        self.failUnless(isinstance(num, CFNumberRef))
        self.failIf(CFNumberIsFloatType(num))
        self.failUnless(num == 1)

        num = CFNumberCreate(None, kCFNumberNSIntegerType, 1)
        self.failUnless(isinstance(num, CFNumberRef))
        self.failIf(CFNumberIsFloatType(num))
        self.failUnless(num == 1)

        num = CFNumberCreate(None, kCFNumberCGFloatType, 1)
        self.failUnless(isinstance(num, CFNumberRef))
        self.failUnless(CFNumberIsFloatType(num))
        self.failUnless(num == 1)



    def testNumberTypes(self):
        v = CFNumberGetType(44)
        self.failUnless(v == kCFNumberLongType)

        v = CFNumberGetType(2.5)
        self.failUnless(v == kCFNumberDoubleType)

        v = CFNumberGetByteSize(44)
        if sys.maxint > 2 ** 32:
            self.failUnless(v == 8)
        else:
            self.failUnless(v == 4)

        v = CFNumberGetByteSize(44.0)
        self.failUnless(v == 8)

        self.failIf(CFNumberIsFloatType(44))
        self.failUnless(CFNumberIsFloatType(1.0))

        r = CFNumberCompare(44, 45, 0)
        self.failUnless(r < 0)


    def testConstants(self):
        self.failUnless(kCFBooleanTrue is True)
        self.failUnless(kCFBooleanFalse is False)

        self.failUnless(kCFNumberSInt8Type == 1)
        self.failUnless(kCFNumberSInt16Type == 2)
        self.failUnless(kCFNumberSInt32Type == 3)
        self.failUnless(kCFNumberSInt64Type == 4)
        self.failUnless(kCFNumberFloat32Type == 5)
        self.failUnless(kCFNumberFloat64Type == 6)
        self.failUnless(kCFNumberCharType == 7)
        self.failUnless(kCFNumberShortType == 8)
        self.failUnless(kCFNumberIntType == 9)
        self.failUnless(kCFNumberLongType == 10)
        self.failUnless(kCFNumberLongLongType == 11)
        self.failUnless(kCFNumberFloatType == 12)
        self.failUnless(kCFNumberDoubleType == 13)
        self.failUnless(kCFNumberCFIndexType == 14)
        self.failUnless(kCFNumberNSIntegerType == 15)
        self.failUnless(kCFNumberCGFloatType == 16)
        self.failUnless(kCFNumberMaxType == 16)

        self.failUnless(isinstance(kCFNumberPositiveInfinity, float))
        self.failUnless(isinstance(kCFNumberNegativeInfinity, float))
        self.failUnless(isinstance(kCFNumberNaN, float))


if __name__ == "__main__":
    main()
