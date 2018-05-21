from PyObjCTools.TestSupport import *
import sys
from Foundation import *



class TestNSObjCRuntime (TestCase):
    def testConstants(self):
        self.assertEqual(NSQualityOfServiceUserInteractive, 0x21)
        self.assertEqual(NSQualityOfServiceUserInitiated, 0x19)
        self.assertEqual(NSQualityOfServiceUtility, 0x11)
        self.assertEqual(NSQualityOfServiceBackground, 0x09)
        self.assertEqual(NSQualityOfServiceDefault, -1)
        self.assertEqual(NSFoundationVersionNumber10_0,   397.40)
        self.assertEqual(NSFoundationVersionNumber10_1,   425.00)
        self.assertEqual(NSFoundationVersionNumber10_1_1, 425.00)
        self.assertEqual(NSFoundationVersionNumber10_1_2, 425.00)
        self.assertEqual(NSFoundationVersionNumber10_1_3, 425.00)
        self.assertEqual(NSFoundationVersionNumber10_1_4, 425.00)
        self.assertEqual(NSFoundationVersionNumber10_2,   462.00)
        self.assertEqual(NSFoundationVersionNumber10_2_1, 462.00)
        self.assertEqual(NSFoundationVersionNumber10_2_2, 462.00)
        self.assertEqual(NSFoundationVersionNumber10_2_3, 462.00)
        self.assertEqual(NSFoundationVersionNumber10_2_4, 462.00)
        self.assertEqual(NSFoundationVersionNumber10_2_5, 462.00)
        self.assertEqual(NSFoundationVersionNumber10_2_6, 462.00)
        self.assertEqual(NSFoundationVersionNumber10_2_7, 462.70)
        self.assertEqual(NSFoundationVersionNumber10_2_8, 462.70)
        self.assertEqual(NSFoundationVersionNumber10_3,   500.00)
        self.assertEqual(NSFoundationVersionNumber10_3_1, 500.00)
        self.assertEqual(NSFoundationVersionNumber10_3_2, 500.30)
        self.assertEqual(NSFoundationVersionNumber10_3_3, 500.54)
        self.assertEqual(NSFoundationVersionNumber10_3_4, 500.56)
        self.assertEqual(NSFoundationVersionNumber10_3_5, 500.56)
        self.assertEqual(NSFoundationVersionNumber10_3_6, 500.56)
        self.assertEqual(NSFoundationVersionNumber10_3_7, 500.56)
        self.assertEqual(NSFoundationVersionNumber10_3_8, 500.56)
        self.assertEqual(NSFoundationVersionNumber10_3_9, 500.58)
        self.assertEqual(NSFoundationVersionNumber10_4,   567.00)
        self.assertEqual(NSFoundationVersionNumber10_4_1, 567.00)
        self.assertEqual(NSFoundationVersionNumber10_4_2, 567.12)
        self.assertEqual(NSFoundationVersionNumber10_4_3, 567.21)
        self.assertEqual(NSFoundationVersionNumber10_4_4_Intel,   567.23)
        self.assertEqual(NSFoundationVersionNumber10_4_4_PowerPC, 567.21)
        self.assertEqual(NSFoundationVersionNumber10_4_5, 567.25)
        self.assertEqual(NSFoundationVersionNumber10_4_6, 567.26)
        self.assertEqual(NSFoundationVersionNumber10_4_7, 567.27)
        self.assertEqual(NSFoundationVersionNumber10_4_8, 567.28)
        self.assertEqual(NSFoundationVersionNumber10_4_9, 567.29)
        self.assertEqual(NSFoundationVersionNumber10_4_10, 567.29)
        self.assertEqual(NSFoundationVersionNumber10_4_11, 567.36)
        self.assertEqual(NSFoundationVersionNumber10_5, 677.00)
        self.assertEqual(NSFoundationVersionNumber10_5_1, 677.10)
        self.assertEqual(NSFoundationVersionNumber10_5_2, 677.15)
        self.assertEqual(NSFoundationVersionNumber10_5_3, 677.19)
        self.assertEqual(NSFoundationVersionNumber10_5_4, 677.19)
        self.assertEqual(NSFoundationVersionNumber10_5_5, 677.21)
        self.assertEqual(NSFoundationVersionNumber10_5_6, 677.22)
        self.assertEqual(NSFoundationVersionNumber10_5_7, 677.24)
        self.assertEqual(NSFoundationVersionNumber10_5_8, 677.26)
        self.assertEqual(NSFoundationVersionNumber10_6, 751.00)
        self.assertEqual(NSFoundationVersionNumber10_6_1, 751.00)
        self.assertEqual(NSFoundationVersionNumber10_6_2, 751.14)
        self.assertEqual(NSFoundationVersionNumber10_6_3, 751.21)
        self.assertEqual(NSFoundationVersionNumber10_6_4, 751.29)
        self.assertEqual(NSFoundationVersionNumber10_6_5, 751.42)
        self.assertEqual(NSFoundationVersionNumber10_6_6, 751.53)
        self.assertEqual(NSFoundationVersionNumber10_6_7, 751.53)
        self.assertEqual(NSFoundationVersionNumber10_6_8, 751.62)
        self.assertEqual(NSFoundationVersionNumber10_8, 945.00)
        self.assertEqual(NSFoundationVersionNumber10_8_1, 945.00)
        self.assertEqual(NSFoundationVersionNumber10_8_2, 945.11)
        self.assertEqual(NSFoundationVersionNumber10_8_3, 945.16)
        self.assertEqual(NSFoundationVersionNumber10_8_4, 945.18)
        self.assertEqual(NSFoundationVersionNumber10_9, 1056)
        self.assertEqual(NSFoundationVersionNumber10_9_1, 1056)
        self.assertEqual(NSFoundationVersionNumber10_9_2, 1056.13)
        self.assertEqual(NSFoundationVersionNumber10_10, 1151.16)
        self.assertEqual(NSFoundationVersionNumber10_10_1, 1151.16)
        self.assertEqual(NSFoundationVersionNumber10_10_2, 1152.14)
        self.assertEqual(NSFoundationVersionNumber10_10_3, 1153.20)
        self.assertEqual(NSFoundationVersionNumber10_10_4, 1153.20)
        self.assertEqual(NSFoundationVersionNumber10_10_5, 1154)
        self.assertEqual(NSFoundationVersionNumber10_10_Max, 1199)
        self.assertEqual(NSFoundationVersionNumber10_11,   1252)
        self.assertEqual(NSFoundationVersionNumber10_11_1, 1255.1)
        self.assertEqual(NSFoundationVersionNumber10_11_2, 1256.1)
        self.assertEqual(NSFoundationVersionNumber10_11_3, 1256.1)
        self.assertEqual(NSFoundationVersionNumber10_11_4, 1258)
        self.assertEqual(NSFoundationVersionNumber10_11_Max, 1299)


        self.assertIsInstance(NSFoundationVersionNumber, float)
        self.assertIsInstance(NSIntegerMax, (int, long))
        self.assertIsInstance(NSIntegerMin, (int, long))
        self.assertIsInstance(NSUIntegerMax, (int, long))
        if sys.maxsize > 2 ** 32:
            self.assertEqual(NSIntegerMax, 2 ** 63 -1)
            self.assertEqual(NSIntegerMin, -(2 ** 63))
            self.assertEqual(NSUIntegerMax, 2**64-1)

        else:
            self.assertEqual(NSIntegerMax, 2 ** 31 -1)
            self.assertEqual(NSIntegerMin, -(2 ** 31))
            self.assertEqual(NSUIntegerMax, 2**32-1)

        self.assertTrue(YES)
        self.assertFalse(NO)

        self.assertEqual(NSOrderedAscending, -1)
        self.assertEqual(NSOrderedSame, 0)
        self.assertEqual(NSOrderedDescending, 1)

        self.assertEqual(NSNotFound, NSIntegerMax)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(NSFoundationVersionNumber10_5, 677.00)
        self.assertEqual(NSFoundationVersionNumber10_5_1, 677.10)
        self.assertEqual(NSFoundationVersionNumber10_5_2, 677.15)
        self.assertEqual(NSFoundationVersionNumber10_5_3, 677.19)
        self.assertEqual(NSFoundationVersionNumber10_5_4, 677.19)
        self.assertEqual(NSFoundationVersionNumber10_5_5, 677.21)
        self.assertEqual(NSFoundationVersionNumber10_5_6, 677.22)

        self.assertEqual(NSEnumerationConcurrent, 1<<0)
        self.assertEqual(NSEnumerationReverse, 1<<1)
        self.assertEqual(NSSortConcurrent, 1<<0)
        self.assertEqual(NSSortStable, 1<<4)

    @min_os_level('10.7')
    def testConstants10_7(self):
        self.assertEqual(NSFoundationVersionNumber10_7, 833.10)
        self.assertEqual(NSFoundationVersionNumber10_7_1, 833.10)
        self.assertEqual(NSFoundationVersionNumber10_7_2, 833.20)
        self.assertEqual(NSFoundationVersionNumber10_7_3, 833.24)
        self.assertEqual(NSFoundationVersionNumber10_7_4, 833.25)

    def testSelectorAccess(self):
        v = NSStringFromSelector('description')
        self.assertIsInstance(v, unicode)
        self.assertEqual(v, 'description')

        v = NSSelectorFromString(b"description".decode('ascii'))
        self.assertIsInstance(v, str)
        self.assertEqual(v, 'description')

    def testClassAccess(self):
        v = NSStringFromClass(NSObject)
        self.assertIsInstance(v, unicode)
        self.assertEqual(v, 'NSObject')

        v = NSClassFromString('NSDictionary')
        self.assertIsInstance(v, objc.objc_class)
        self.assertEqual(v, NSDictionary)

    def testProtocolAccess(self):
        p = NSProtocolFromString('NSObject')
        self.assertIsInstance(p, objc.formal_protocol)
        v = NSStringFromProtocol(p)
        self.assertIsInstance(v, unicode)
        self.assertEqual(v, 'NSObject')

    def testTypeInfo(self):
        rest, size, align = NSGetSizeAndAlignment(b"ii", None, None)
        self.assertEqual(rest, b"i")
        self.assertIsInstance(size, (int, long))
        self.assertIsInstance(align, (int, long))

    def testMinMax(self):
        self.assertEqual(MAX(1, 2), 2)
        self.assertEqual(MAX(2, 1), 2)
        self.assertEqual(MAX("a", "b"), "b")
        self.assertEqual(MIN(1, 2), 1)
        self.assertEqual(MIN(2, 1), 1)
        self.assertEqual(MIN("a", "b"), "a")
        self.assertEqual(ABS(1), 1)
        self.assertEqual(ABS(-1), 1)
        self.assertEqual(ABS(-1.0), 1.0)

    def testFunctions(self):
        self.assertArgIsPrintf(NSLog, 0)

if __name__ == "__main__":
    main()
