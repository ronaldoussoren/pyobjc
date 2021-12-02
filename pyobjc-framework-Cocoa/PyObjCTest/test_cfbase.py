import CoreFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestBase(TestCase):
    def testConstants(self):
        self.assertEqual(CoreFoundation.TRUE, 1)
        self.assertEqual(CoreFoundation.FALSE, 0)

        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_0, 196.40)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_0_3, 196.50)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_1, 226.00)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_1_1, 226.00)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_1_2, 227.20)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_1_3, 227.20)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_1_4, 227.30)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_2, 263.00)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_2_1, 263.10)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_2_2, 263.10)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_2_3, 263.30)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_2_4, 263.30)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_2_5, 263.50)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_2_6, 263.50)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_2_7, 263.50)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_2_8, 263.50)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_3, 299.00)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_3_1, 299.00)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_3_2, 299.00)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_3_3, 299.30)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_3_4, 299.31)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_3_5, 299.31)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_3_6, 299.32)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_3_7, 299.33)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_3_8, 299.33)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_3_9, 299.35)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_4, 368.00)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_4_1, 368.10)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_4_2, 368.11)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_4_3, 368.18)
        self.assertEqual(
            CoreFoundation.kCFCoreFoundationVersionNumber10_4_4_Intel, 368.26
        )
        self.assertEqual(
            CoreFoundation.kCFCoreFoundationVersionNumber10_4_4_PowerPC, 368.25
        )
        self.assertEqual(
            CoreFoundation.kCFCoreFoundationVersionNumber10_4_5_Intel, 368.26
        )
        self.assertEqual(
            CoreFoundation.kCFCoreFoundationVersionNumber10_4_5_PowerPC, 368.25
        )
        self.assertEqual(
            CoreFoundation.kCFCoreFoundationVersionNumber10_4_6_Intel, 368.26
        )
        self.assertEqual(
            CoreFoundation.kCFCoreFoundationVersionNumber10_4_6_PowerPC, 368.25
        )
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_4_7, 368.27)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_4_8, 368.27)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_4_9, 368.28)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_4_10, 368.28)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_4_11, 368.31)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_5, 476.00)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_5_1, 476.00)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_5_2, 476.10)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_5_3, 476.13)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_5_4, 476.14)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_5_5, 476.15)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_5_6, 476.17)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_5_7, 476.18)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_5_8, 476.19)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_6, 550.00)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_6_1, 550.00)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_6_2, 550.13)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_6_3, 550.19)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_6_4, 550.29)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_6_5, 550.42)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_6_6, 550.42)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_6_7, 550.42)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_6_8, 550.43)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_7, 635.00)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_7_1, 635.00)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_7_2, 635.15)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_7_3, 635.19)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_7_4, 635.21)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_7_5, 635.21)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_8, 744.00)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_8_1, 744.00)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_8_2, 744.12)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_8_3, 744.18)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_8_4, 744.19)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_9, 855.11)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_9_1, 855.11)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_9_2, 855.14)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_10, 1151.16)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_10_1, 1151.16)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_10_2, 1152)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_10_3, 1153.18)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_10_4, 1153.18)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_10_5, 1153.18)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_10_Max, 1199)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_11, 1253)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_11_1, 1255.1)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_11_2, 1256.14)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_11_3, 1256.14)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_11_4, 1258.1)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_11_Max, 1299)

        self.assertEqual(CoreFoundation.kCFCompareLessThan, -1)
        self.assertEqual(CoreFoundation.kCFCompareEqualTo, 0)
        self.assertEqual(CoreFoundation.kCFCompareGreaterThan, 1)

        self.assertEqual(CoreFoundation.kCFNotFound, -1)

    def testStructs(self):
        o = CoreFoundation.CFRange()
        self.assertHasAttr(o, "location")
        self.assertHasAttr(o, "length")

        self.assertPickleRoundTrips(o)

    def testCFRangeMake(self):
        r = CoreFoundation.CFRangeMake(42, 99)
        self.assertIsInstance(r, CoreFoundation.CFRange)
        self.assertEqual(r.location, 42)
        self.assertEqual(r.length, 99)

    def testCFNull(self):
        self.assertIsInstance(CoreFoundation.CFNullGetTypeID(), int)
        self.assertIsInstance(CoreFoundation.kCFNull, CoreFoundation.CFNullRef)

        cls = objc.lookUpClass("NSNull")
        if cls is not CoreFoundation.CFNullRef:
            self.assertIsCFType(CoreFoundation.CFNullRef)

    def testCFAllocator(self):
        self.assertIsCFType(CoreFoundation.CFAllocatorRef)

        self.assertIsInstance(CoreFoundation.CFAllocatorGetTypeID(), int)
        self.assertIsInstance(
            CoreFoundation.kCFAllocatorDefault,
            (CoreFoundation.CFAllocatorRef, type(None)),
        )
        self.assertIsInstance(
            CoreFoundation.kCFAllocatorSystemDefault, CoreFoundation.CFAllocatorRef
        )
        self.assertIsInstance(
            CoreFoundation.kCFAllocatorMalloc, CoreFoundation.CFAllocatorRef
        )
        self.assertIsInstance(
            CoreFoundation.kCFAllocatorMallocZone, CoreFoundation.CFAllocatorRef
        )
        self.assertIsInstance(
            CoreFoundation.kCFAllocatorNull, CoreFoundation.CFAllocatorRef
        )
        self.assertIsInstance(
            CoreFoundation.kCFAllocatorUseContext, CoreFoundation.CFAllocatorRef
        )
        r = CoreFoundation.CFAllocatorGetDefault()
        self.assertIsInstance(r, CoreFoundation.CFAllocatorRef)
        CoreFoundation.CFAllocatorSetDefault(CoreFoundation.kCFAllocatorMalloc)
        r2 = CoreFoundation.CFAllocatorGetDefault()
        self.assertIsInstance(r2, CoreFoundation.CFAllocatorRef)
        self.assertIs(r2, CoreFoundation.kCFAllocatorMalloc)
        # Restore default allocator
        CoreFoundation.CFAllocatorSetDefault(r)

        self.assertNotHasAttr(CoreFoundation, "CFAllocatorCreate")
        self.assertNotHasAttr(CoreFoundation, "CFAllocatorAllocate")
        self.assertNotHasAttr(CoreFoundation, "CFAllocatorReallocate")
        self.assertNotHasAttr(CoreFoundation, "CFAllocatorDeallocate")
        self.assertNotHasAttr(CoreFoundation, "CFAllocatorGetContext")
        r = CoreFoundation.CFAllocatorGetPreferredSizeForSize(
            CoreFoundation.kCFAllocatorDefault, 15, 0
        )
        self.assertIsInstance(r, int)
        self.assertGreaterEqual(r, 15)

    def testGenericFunctions(self):
        value = CoreFoundation.CFGetTypeID(CoreFoundation.kCFAllocatorMalloc)
        self.assertEqual(value, CoreFoundation.CFAllocatorGetTypeID())

        v = CoreFoundation.CFCopyTypeIDDescription(
            CoreFoundation.CFAllocatorGetTypeID()
        )
        self.assertIsInstance(v, str)
        obj = CoreFoundation.CFURLCreateWithString(None, "http://www.apple.com/", None)
        i = CoreFoundation.CFGetTypeID(obj)
        self.assertIsInstance(i, int)
        i = CoreFoundation.CFGetRetainCount(obj)
        self.assertIsInstance(i, int)
        CoreFoundation.CFRetain(obj)
        self.assertEqual(CoreFoundation.CFGetRetainCount(obj), i + 1)
        CoreFoundation.CFRelease(obj)
        self.assertEqual(CoreFoundation.CFGetRetainCount(obj), i)

        CoreFoundation.CFRetain(obj)
        CoreFoundation.CFMakeCollectable(obj)

        del obj

        i = CoreFoundation.CFEqual(
            CoreFoundation.kCFAllocatorMalloc, CoreFoundation.kCFAllocatorNull
        )
        self.assertIs(i, False)
        i = CoreFoundation.CFEqual(
            CoreFoundation.kCFAllocatorMalloc, CoreFoundation.kCFAllocatorMalloc
        )
        self.assertIs(i, True)
        i = CoreFoundation.CFHash(CoreFoundation.kCFAllocatorMalloc)
        self.assertTrue(i, int)

        v = CoreFoundation.CFCopyDescription(CoreFoundation.kCFAllocatorMalloc)
        self.assertIsInstance(v, str)
        v = CoreFoundation.CFGetAllocator(CoreFoundation.kCFAllocatorMalloc)
        if v is not None:
            self.assertIsInstance(v, CoreFoundation.CFAllocatorRef)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_5, 476.00)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_5_1, 476.00)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_5_2, 476.10)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_5_3, 476.13)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_5_4, 476.14)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_5_5, 476.15)
        self.assertEqual(CoreFoundation.kCFCoreFoundationVersionNumber10_5_6, 476.17)

    @min_os_level("10.9")
    def testFunctions10_9(self):
        obj = CoreFoundation.CFURLCreateWithString(None, "http://www.apple.com/", None)
        CoreFoundation.CFRetain(obj)
        CoreFoundation.CFAutorelease(obj)
        del obj
