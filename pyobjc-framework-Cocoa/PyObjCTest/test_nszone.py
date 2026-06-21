import Foundation
import CoreFoundation
from PyObjCTools.TestSupport import TestCase

# Foundation.NSZonePtr = getattr(Foundation, 'NSZone*')


class TestNSZone(TestCase):
    def test_with_zones(self):
        obj = Foundation.NSObject.allocWithZone_(None).init()
        zone = obj.zone()
        self.assertIsNot(zone, None)
        self.assertNotEqual(zone.__pointer__, 0)

        obj2 = Foundation.NSObject.allocWithZone_(zone).init()
        zone2 = obj2.zone()
        self.assertEqual(zone.__pointer__, zone2.__pointer__)

        self.assertRaises(TypeError, Foundation.NSObject.allocWithZone_, 10)
        # self.assertRaises(TypeError, Foundation.NSObject.allocWithZone_, objc.NULL)

    def test_no_malloc_and_friends(self):
        import Foundation

        self.assertNotHasAttr(Foundation, "NSZoneMalloc")
        self.assertNotHasAttr(Foundation, "NSZoneCalloc")
        self.assertNotHasAttr(Foundation, "NSZoneRealloc")
        self.assertNotHasAttr(Foundation, "NSZoneFree")
        self.assertNotHasAttr(Foundation, "NSZoneFromPointer")
        self.assertNotHasAttr(Foundation, "NSAllocateCollectable")
        self.assertNotHasAttr(Foundation, "NSReallocateCollectable")
        self.assertNotHasAttr(Foundation, "NSAllocateMemoryPages")
        self.assertNotHasAttr(Foundation, "NSDeallocateMemoryPages")
        self.assertNotHasAttr(Foundation, "NSCopyMemoryPages")

    def test_constants(self):
        self.assertEqual(Foundation.NSScannedOption, (1 << 0))
        self.assertEqual(Foundation.NSCollectorDisabledOption, (1 << 1))

    def test_make_collectable(self):
        v = Foundation.NSMakeCollectable

        o = Foundation.NSObject.alloc().init()
        CoreFoundation.CFRetain(o)
        v = Foundation.NSMakeCollectable(o)
        self.assertIs(v, o)
        v = Foundation.NSMakeCollectable(None)
        self.assertIs(v, None)

    def test_functions_info(self):
        v = Foundation.NSPageSize()
        self.assertIsInstance(v, int)
        v = Foundation.NSLogPageSize()
        self.assertIsInstance(v, int)
        v = Foundation.NSRoundUpToMultipleOfPageSize(500)
        self.assertIsInstance(v, int)
        v = Foundation.NSRoundDownToMultipleOfPageSize(500)
        self.assertIsInstance(v, int)
        v = Foundation.NSRealMemoryAvailable()
        self.assertIsInstance(v, int)

    def test_zone_creation(self):
        z = Foundation.NSDefaultMallocZone()
        if z is not None:
            self.assertIsInstance(z, Foundation.NSZonePtr)
        z = Foundation.NSCreateZone(5000, 100, True)
        self.assertIsInstance(z, Foundation.NSZonePtr)
        Foundation.NSSetZoneName(z, "Hello World")
        nm = Foundation.NSZoneName(z)
        self.assertEqual(nm, "Hello World")

        Foundation.NSRecycleZone(z)
        z = None
