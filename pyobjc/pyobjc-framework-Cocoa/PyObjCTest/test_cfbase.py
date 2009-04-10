from PyObjCTools.TestSupport import *
from CoreFoundation import *
import CoreFoundation


class TestBase (TestCase):
    def testConstants(self):
        self.assertEquals(TRUE, 1)
        self.assertEquals(FALSE, 0)

        self.assertEquals(kCFCoreFoundationVersionNumber10_0,      196.40)
        self.assertEquals(kCFCoreFoundationVersionNumber10_0_3,    196.50)
        self.assertEquals(kCFCoreFoundationVersionNumber10_1,      226.00)
        self.assertEquals(kCFCoreFoundationVersionNumber10_1_1,    226.00)
        self.assertEquals(kCFCoreFoundationVersionNumber10_1_2,    227.20)
        self.assertEquals(kCFCoreFoundationVersionNumber10_1_3,    227.20)
        self.assertEquals(kCFCoreFoundationVersionNumber10_1_4,    227.30)
        self.assertEquals(kCFCoreFoundationVersionNumber10_2,      263.00)
        self.assertEquals(kCFCoreFoundationVersionNumber10_2_1,    263.10)
        self.assertEquals(kCFCoreFoundationVersionNumber10_2_2,    263.10)
        self.assertEquals(kCFCoreFoundationVersionNumber10_2_3,    263.30)
        self.assertEquals(kCFCoreFoundationVersionNumber10_2_4,    263.30)
        self.assertEquals(kCFCoreFoundationVersionNumber10_2_5,    263.50)
        self.assertEquals(kCFCoreFoundationVersionNumber10_2_6,    263.50)
        self.assertEquals(kCFCoreFoundationVersionNumber10_2_7,    263.50)
        self.assertEquals(kCFCoreFoundationVersionNumber10_2_8,    263.50)
        self.assertEquals(kCFCoreFoundationVersionNumber10_3,      299.00)
        self.assertEquals(kCFCoreFoundationVersionNumber10_3_1,    299.00)
        self.assertEquals(kCFCoreFoundationVersionNumber10_3_2,    299.00)
        self.assertEquals(kCFCoreFoundationVersionNumber10_3_3,    299.30)
        self.assertEquals(kCFCoreFoundationVersionNumber10_3_4,    299.31)
        self.assertEquals(kCFCoreFoundationVersionNumber10_3_5,    299.31)
        self.assertEquals(kCFCoreFoundationVersionNumber10_3_6,    299.32)
        self.assertEquals(kCFCoreFoundationVersionNumber10_3_7,    299.33)
        self.assertEquals(kCFCoreFoundationVersionNumber10_3_8,    299.33)
        self.assertEquals(kCFCoreFoundationVersionNumber10_3_9,    299.35)
        self.assertEquals(kCFCoreFoundationVersionNumber10_4,      368.00)
        self.assertEquals(kCFCoreFoundationVersionNumber10_4_1,    368.10)
        self.assertEquals(kCFCoreFoundationVersionNumber10_4_2,    368.11)
        self.assertEquals(kCFCoreFoundationVersionNumber10_4_3,    368.18)
        self.assertEquals(kCFCoreFoundationVersionNumber10_4_4_Intel,      368.26)
        self.assertEquals(kCFCoreFoundationVersionNumber10_4_4_PowerPC,    368.25)
        self.assertEquals(kCFCoreFoundationVersionNumber10_4_5_Intel,      368.26)
        self.assertEquals(kCFCoreFoundationVersionNumber10_4_5_PowerPC,    368.25)
        self.assertEquals(kCFCoreFoundationVersionNumber10_4_6_Intel,      368.26)
        self.assertEquals(kCFCoreFoundationVersionNumber10_4_6_PowerPC,    368.25)
        self.assertEquals(kCFCoreFoundationVersionNumber10_4_7,    368.27)
        self.assertEquals(kCFCoreFoundationVersionNumber10_4_8,    368.27)
        self.assertEquals(kCFCoreFoundationVersionNumber10_4_9,    368.28)
        self.assertEquals(kCFCoreFoundationVersionNumber10_4_10,   368.28)
        self.assertEquals(kCFCoreFoundationVersionNumber10_4_11,   368.31)

        self.assertEquals(kCFCompareLessThan, -1)
        self.assertEquals(kCFCompareEqualTo, 0)
        self.assertEquals(kCFCompareGreaterThan, 1)

        self.assertEquals(kCFNotFound, -1)


    def testStructs(self):

        o = CFRange()
        self.failUnless(hasattr(o, 'location'))
        self.failUnless(hasattr(o, 'length'))

    def testCFRangeMake(self):
        r = CFRangeMake(42, 99)
        self.failUnless(isinstance(r, CFRange))
        self.assertEquals(r.location, 42)
        self.assertEquals(r.length, 99)

    def testCFNull(self):
        self.failUnless(isinstance(CFNullGetTypeID(), (int, long)))

        self.failUnless(isinstance(kCFNull, CFNullRef))
        self.failUnlessIsCFType(CFNullRef)

    def testCFAllocator(self):
        self.failUnlessIsCFType(CFAllocatorRef)

        self.failUnless(isinstance(CFAllocatorGetTypeID(), (int, long)))

        self.failUnless(isinstance(kCFAllocatorDefault, (CFAllocatorRef, type(None))))
        self.failUnless(isinstance(kCFAllocatorSystemDefault, CFAllocatorRef))
        self.failUnless(isinstance(kCFAllocatorMalloc, CFAllocatorRef))
        self.failUnless(isinstance(kCFAllocatorMallocZone, CFAllocatorRef))
        self.failUnless(isinstance(kCFAllocatorNull, CFAllocatorRef))
        self.failUnless(isinstance(kCFAllocatorUseContext, CFAllocatorRef))

        r = CFAllocatorGetDefault()
        self.failUnless(isinstance(r, CFAllocatorRef))

        CFAllocatorSetDefault(kCFAllocatorMalloc)
        r2 = CFAllocatorGetDefault()
        self.failUnless(isinstance(r2, CFAllocatorRef))
        self.failUnless(r2 is kCFAllocatorMalloc)

        # Restore default allocator
        CFAllocatorSetDefault(r)

        self.failIf(hasattr(CoreFoundation, 'CFAllocatorCreate'))
        self.failIf(hasattr(CoreFoundation, 'CFAllocatorAllocate'))
        self.failIf(hasattr(CoreFoundation, 'CFAllocatorReallocate'))
        self.failIf(hasattr(CoreFoundation, 'CFAllocatorDeallocate'))
        self.failIf(hasattr(CoreFoundation, 'CFAllocatorGetContext'))

        r = CFAllocatorGetPreferredSizeForSize(kCFAllocatorDefault, 15, 0)
        self.failUnless(isinstance(r, (int, long)))
        self.failUnless(r >= 15)


    def testGenericFunctions(self):
        id = CFGetTypeID(kCFAllocatorMalloc)
        self.assertEquals(id, CFAllocatorGetTypeID())

        v = CFCopyTypeIDDescription(CFAllocatorGetTypeID())
        self.failUnless(isinstance(v, unicode))

        obj = CFURLCreateWithString(None, u"http://www.apple.com/", None)
        i = CFGetRetainCount(obj)
        self.failUnless(isinstance(i, (int, long)))
        CFRetain(obj)
        self.assertEquals(CFGetRetainCount(obj), i + 1)
        CFRelease(obj)
        self.assertEquals(CFGetRetainCount(obj), i)

        CFRetain(obj)
        CFMakeCollectable(obj)

        del obj

        i = CFEqual(kCFAllocatorMalloc, kCFAllocatorNull)
        self.failUnless(i is False)
        i = CFEqual(kCFAllocatorMalloc, kCFAllocatorMalloc)
        self.failUnless(i is True)

        i = CFHash(kCFAllocatorMalloc)
        self.failUnless(i, (int, long))

        v = CFCopyDescription(kCFAllocatorMalloc)
        self.failUnless(isinstance(v, unicode))

        v = CFGetAllocator(kCFAllocatorMalloc)
        self.failUnless((v is None) or (isinstance(v, CFAllocatorRef)))


if __name__ == "__main__":
    main()
