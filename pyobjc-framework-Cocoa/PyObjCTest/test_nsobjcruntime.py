from PyObjCTools.TestSupport import *
import sys
from Foundation import *


class TestNSObjCRuntime (TestCase):
    def testConstants(self):
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
        self.assertEqual(NSFoundationVersionNumber10_4_10,        567.29)
        self.assertEqual(NSFoundationVersionNumber10_4_11,        567.36)

        self.assertIsInstance(NSFoundationVersionNumber, float)
        self.assertIsInstance(NSIntegerMax, (int, long))
        self.assertIsInstance(NSIntegerMin, (int, long))
        self.assertIsInstance(NSUIntegerMax, (int, long))
        if sys.maxint > 2 ** 32:
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



    def testSelectorAccess(self):
        v = NSStringFromSelector('description')
        self.assertIsInstance(v, unicode)
        self.assertEqual(v, 'description')

        v = NSSelectorFromString(u"description")
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
        self.assertEqual(MAX("a", "b"), "b")
        self.assertEqual(MIN(1, 2), 1)
        self.assertEqual(MIN("a", "b"), "a")
        self.assertEqual(ABS(-1), 1)
        self.assertEqual(ABS(-1.0), 1.0)

if __name__ == "__main__":
    main()
