from PyObjCTools.TestSupport import *
from CoreFoundation import *
import CoreFoundation


class TestBase (TestCase):
    def testConstants(self):
        self.assertEqual(TRUE, 1)
        self.assertEqual(FALSE, 0)

        self.assertEqual(kCFCoreFoundationVersionNumber10_0,      196.40)
        self.assertEqual(kCFCoreFoundationVersionNumber10_0_3,    196.50)
        self.assertEqual(kCFCoreFoundationVersionNumber10_1,      226.00)
        self.assertEqual(kCFCoreFoundationVersionNumber10_1_1,    226.00)
        self.assertEqual(kCFCoreFoundationVersionNumber10_1_2,    227.20)
        self.assertEqual(kCFCoreFoundationVersionNumber10_1_3,    227.20)
        self.assertEqual(kCFCoreFoundationVersionNumber10_1_4,    227.30)
        self.assertEqual(kCFCoreFoundationVersionNumber10_2,      263.00)
        self.assertEqual(kCFCoreFoundationVersionNumber10_2_1,    263.10)
        self.assertEqual(kCFCoreFoundationVersionNumber10_2_2,    263.10)
        self.assertEqual(kCFCoreFoundationVersionNumber10_2_3,    263.30)
        self.assertEqual(kCFCoreFoundationVersionNumber10_2_4,    263.30)
        self.assertEqual(kCFCoreFoundationVersionNumber10_2_5,    263.50)
        self.assertEqual(kCFCoreFoundationVersionNumber10_2_6,    263.50)
        self.assertEqual(kCFCoreFoundationVersionNumber10_2_7,    263.50)
        self.assertEqual(kCFCoreFoundationVersionNumber10_2_8,    263.50)
        self.assertEqual(kCFCoreFoundationVersionNumber10_3,      299.00)
        self.assertEqual(kCFCoreFoundationVersionNumber10_3_1,    299.00)
        self.assertEqual(kCFCoreFoundationVersionNumber10_3_2,    299.00)
        self.assertEqual(kCFCoreFoundationVersionNumber10_3_3,    299.30)
        self.assertEqual(kCFCoreFoundationVersionNumber10_3_4,    299.31)
        self.assertEqual(kCFCoreFoundationVersionNumber10_3_5,    299.31)
        self.assertEqual(kCFCoreFoundationVersionNumber10_3_6,    299.32)
        self.assertEqual(kCFCoreFoundationVersionNumber10_3_7,    299.33)
        self.assertEqual(kCFCoreFoundationVersionNumber10_3_8,    299.33)
        self.assertEqual(kCFCoreFoundationVersionNumber10_3_9,    299.35)
        self.assertEqual(kCFCoreFoundationVersionNumber10_4,      368.00)
        self.assertEqual(kCFCoreFoundationVersionNumber10_4_1,    368.10)
        self.assertEqual(kCFCoreFoundationVersionNumber10_4_2,    368.11)
        self.assertEqual(kCFCoreFoundationVersionNumber10_4_3,    368.18)
        self.assertEqual(kCFCoreFoundationVersionNumber10_4_4_Intel,      368.26)
        self.assertEqual(kCFCoreFoundationVersionNumber10_4_4_PowerPC,    368.25)
        self.assertEqual(kCFCoreFoundationVersionNumber10_4_5_Intel,      368.26)
        self.assertEqual(kCFCoreFoundationVersionNumber10_4_5_PowerPC,    368.25)
        self.assertEqual(kCFCoreFoundationVersionNumber10_4_6_Intel,      368.26)
        self.assertEqual(kCFCoreFoundationVersionNumber10_4_6_PowerPC,    368.25)
        self.assertEqual(kCFCoreFoundationVersionNumber10_4_7,    368.27)
        self.assertEqual(kCFCoreFoundationVersionNumber10_4_8,    368.27)
        self.assertEqual(kCFCoreFoundationVersionNumber10_4_9,    368.28)
        self.assertEqual(kCFCoreFoundationVersionNumber10_4_10,   368.28)
        self.assertEqual(kCFCoreFoundationVersionNumber10_4_11,   368.31)

        self.assertEqual(kCFCompareLessThan, -1)
        self.assertEqual(kCFCompareEqualTo, 0)
        self.assertEqual(kCFCompareGreaterThan, 1)

        self.assertEqual(kCFNotFound, -1)


    def testStructs(self):

        o = CFRange()
        self.assertHasAttr(o, 'location')
        self.assertHasAttr(o, 'length')

    def testCFRangeMake(self):
        r = CFRangeMake(42, 99)
        self.assertIsInstance(r, CFRange)
        self.assertEqual(r.location, 42)
        self.assertEqual(r.length, 99)

    def testCFNull(self):
        self.assertIsInstance(CFNullGetTypeID(), (int, long))
        self.assertIsInstance(kCFNull, CFNullRef)
        self.assertIsCFType(CFNullRef)

    def testCFAllocator(self):
        self.assertIsCFType(CFAllocatorRef)

        self.assertIsInstance(CFAllocatorGetTypeID(), (int, long))
        self.assertIsInstance(kCFAllocatorDefault, (CFAllocatorRef, type(None)))
        self.assertIsInstance(kCFAllocatorSystemDefault, CFAllocatorRef)
        self.assertIsInstance(kCFAllocatorMalloc, CFAllocatorRef)
        self.assertIsInstance(kCFAllocatorMallocZone, CFAllocatorRef)
        self.assertIsInstance(kCFAllocatorNull, CFAllocatorRef)
        self.assertIsInstance(kCFAllocatorUseContext, CFAllocatorRef)
        r = CFAllocatorGetDefault()
        self.assertIsInstance(r, CFAllocatorRef)
        CFAllocatorSetDefault(kCFAllocatorMalloc)
        r2 = CFAllocatorGetDefault()
        self.assertIsInstance(r2, CFAllocatorRef)
        self.assertIs(r2, kCFAllocatorMalloc)
        # Restore default allocator
        CFAllocatorSetDefault(r)

        self.assertNotHasAttr(CoreFoundation, 'CFAllocatorCreate')
        self.assertNotHasAttr(CoreFoundation, 'CFAllocatorAllocate')
        self.assertNotHasAttr(CoreFoundation, 'CFAllocatorReallocate')
        self.assertNotHasAttr(CoreFoundation, 'CFAllocatorDeallocate')
        self.assertNotHasAttr(CoreFoundation, 'CFAllocatorGetContext')
        r = CFAllocatorGetPreferredSizeForSize(kCFAllocatorDefault, 15, 0)
        self.assertIsInstance(r, (int, long))
        self.assertGreaterEqual(r , 15)
    def testGenericFunctions(self):
        id = CFGetTypeID(kCFAllocatorMalloc)
        self.assertEqual(id, CFAllocatorGetTypeID())

        v = CFCopyTypeIDDescription(CFAllocatorGetTypeID())
        self.assertIsInstance(v, unicode)
        obj = CFURLCreateWithString(None, u"http://www.apple.com/", None)
        i = CFGetRetainCount(obj)
        self.assertIsInstance(i, (int, long))
        CFRetain(obj)
        self.assertEqual(CFGetRetainCount(obj), i + 1)
        CFRelease(obj)
        self.assertEqual(CFGetRetainCount(obj), i)

        CFRetain(obj)
        CFMakeCollectable(obj)

        del obj

        i = CFEqual(kCFAllocatorMalloc, kCFAllocatorNull)
        self.assertIs(i, False)
        i = CFEqual(kCFAllocatorMalloc, kCFAllocatorMalloc)
        self.assertIs(i, True)
        i = CFHash(kCFAllocatorMalloc)
        self.assertTrue(i, (int, long))

        v = CFCopyDescription(kCFAllocatorMalloc)
        self.assertIsInstance(v, unicode)
        v = CFGetAllocator(kCFAllocatorMalloc)
        if v is not None:
            self.assertIsInstance(v, CFAllocatorRef)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(kCFCoreFoundationVersionNumber10_5, 476.00)
        self.assertEqual(kCFCoreFoundationVersionNumber10_5_1, 476.00)
        self.assertEqual(kCFCoreFoundationVersionNumber10_5_2, 476.10)
        self.assertEqual(kCFCoreFoundationVersionNumber10_5_3, 476.13)
        self.assertEqual(kCFCoreFoundationVersionNumber10_5_4, 476.14)
        self.assertEqual(kCFCoreFoundationVersionNumber10_5_5, 476.15)
        self.assertEqual(kCFCoreFoundationVersionNumber10_5_6, 476.17)


if __name__ == "__main__":
    main()
