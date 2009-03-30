from PyObjCTools.TestSupport import *
import sys
from Foundation import *


class TestNSObjCRuntime (TestCase):
    def testConstants(self):
        self.assertEquals(NSFoundationVersionNumber10_0,   397.40)
        self.assertEquals(NSFoundationVersionNumber10_1,   425.00)
        self.assertEquals(NSFoundationVersionNumber10_1_1, 425.00)
        self.assertEquals(NSFoundationVersionNumber10_1_2, 425.00)
        self.assertEquals(NSFoundationVersionNumber10_1_3, 425.00)
        self.assertEquals(NSFoundationVersionNumber10_1_4, 425.00)
        self.assertEquals(NSFoundationVersionNumber10_2,   462.00)
        self.assertEquals(NSFoundationVersionNumber10_2_1, 462.00)
        self.assertEquals(NSFoundationVersionNumber10_2_2, 462.00)
        self.assertEquals(NSFoundationVersionNumber10_2_3, 462.00)
        self.assertEquals(NSFoundationVersionNumber10_2_4, 462.00)
        self.assertEquals(NSFoundationVersionNumber10_2_5, 462.00)
        self.assertEquals(NSFoundationVersionNumber10_2_6, 462.00)
        self.assertEquals(NSFoundationVersionNumber10_2_7, 462.70)
        self.assertEquals(NSFoundationVersionNumber10_2_8, 462.70)
        self.assertEquals(NSFoundationVersionNumber10_3,   500.00)
        self.assertEquals(NSFoundationVersionNumber10_3_1, 500.00)
        self.assertEquals(NSFoundationVersionNumber10_3_2, 500.30)
        self.assertEquals(NSFoundationVersionNumber10_3_3, 500.54)
        self.assertEquals(NSFoundationVersionNumber10_3_4, 500.56)
        self.assertEquals(NSFoundationVersionNumber10_3_5, 500.56)
        self.assertEquals(NSFoundationVersionNumber10_3_6, 500.56)
        self.assertEquals(NSFoundationVersionNumber10_3_7, 500.56)
        self.assertEquals(NSFoundationVersionNumber10_3_8, 500.56)
        self.assertEquals(NSFoundationVersionNumber10_3_9, 500.58)
        self.assertEquals(NSFoundationVersionNumber10_4,   567.00)
        self.assertEquals(NSFoundationVersionNumber10_4_1, 567.00)
        self.assertEquals(NSFoundationVersionNumber10_4_2, 567.12)
        self.assertEquals(NSFoundationVersionNumber10_4_3, 567.21)
        self.assertEquals(NSFoundationVersionNumber10_4_4_Intel,   567.23)
        self.assertEquals(NSFoundationVersionNumber10_4_4_PowerPC, 567.21)
        self.assertEquals(NSFoundationVersionNumber10_4_5, 567.25)
        self.assertEquals(NSFoundationVersionNumber10_4_6, 567.26)
        self.assertEquals(NSFoundationVersionNumber10_4_7, 567.27)
        self.assertEquals(NSFoundationVersionNumber10_4_8, 567.28)
        self.assertEquals(NSFoundationVersionNumber10_4_9, 567.29)
        self.assertEquals(NSFoundationVersionNumber10_4_10,        567.29)
        self.assertEquals(NSFoundationVersionNumber10_4_11,        567.36)

        self.failUnless(isinstance(NSFoundationVersionNumber, float))
        self.failUnless(isinstance(NSIntegerMax, (int, long)))
        self.failUnless(isinstance(NSIntegerMin, (int, long)))
        self.failUnless(isinstance(NSUIntegerMax, (int, long)))

        if sys.maxint > 2 ** 32:
            self.assertEquals(NSIntegerMax, 2 ** 63 -1)
            self.assertEquals(NSIntegerMin, -(2 ** 63))
            self.assertEquals(NSUIntegerMax, 2**64-1)

        else:
            self.assertEquals(NSIntegerMax, 2 ** 31 -1)
            self.assertEquals(NSIntegerMin, -(2 ** 31))
            self.assertEquals(NSUIntegerMax, 2**32-1)

        self.failUnless(YES)
        self.failIf(NO)

        self.assertEquals(NSOrderedAscending, -1)
        self.assertEquals(NSOrderedSame, 0)
        self.assertEquals(NSOrderedDescending, 1)

        self.assertEquals(NSNotFound, NSIntegerMax)


    def testSelectorAccess(self):
        v = NSStringFromSelector('description')
        self.failUnless(isinstance(v, unicode))
        self.assertEquals(v, 'description')

        v = NSSelectorFromString(u"description")
        self.failUnless(isinstance(v, str))
        self.assertEquals(v, 'description')

    def testClassAccess(self):
        v = NSStringFromClass(NSObject)
        self.failUnless(isinstance(v, unicode))
        self.assertEquals(v, 'NSObject')

        v = NSClassFromString('NSDictionary')
        self.failUnless(isinstance(v, objc.objc_class))
        self.assertEquals(v, NSDictionary)
    
    def testProtocolAccess(self):
        p = NSProtocolFromString('NSObject')
        self.failUnless(isinstance(p, objc.formal_protocol))

        v = NSStringFromProtocol(p)
        self.failUnless(isinstance(v, unicode))
        self.assertEquals(v, 'NSObject')

    def testTypeInfo(self):
        rest, size, align = NSGetSizeAndAlignment("ii", None, None)
        self.assertEquals(rest, "i")
        self.failUnless(isinstance(size, (int, long)))
        self.failUnless(isinstance(align, (int, long)))

    def testMinMax(self):
        self.assertEquals(MAX(1, 2), 2)
        self.assertEquals(MAX("a", "b"), "b")
        self.assertEquals(MIN(1, 2), 1)
        self.assertEquals(MIN("a", "b"), "a")
        self.assertEquals(ABS(-1), 1)
        self.assertEquals(ABS(-1.0), 1.0)

if __name__ == "__main__":
    main()
