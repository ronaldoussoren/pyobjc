from PyObjCTools.TestSupport import *
import objc
from Foundation import *

# HACK
import Foundation
NSZonePtr = getattr(Foundation, 'NSZone*')

class TestNSZone (TestCase):
    def testWithZones(self):
        obj = NSObject.allocWithZone_(None).init()
        zone = obj.zone()
        self.assert_(zone is not None)
        self.assert_(zone.__pointer__ != 0)
        
        obj2 = NSObject.allocWithZone_(zone).init()
        zone2 = obj2.zone()
        self.assertEqual(zone.__pointer__, zone2.__pointer__)

        self.assertRaises(TypeError, NSObject.allocWithZone_, 10)
        #self.assertRaises(TypeError, NSObject.allocWithZone_, objc.NULL)


    def testNoMallocAndFriends(self):
        import Foundation
        self.assertNotHasAttr(Foundation, 'NSZoneMalloc')
        self.assertNotHasAttr(Foundation, 'NSZoneCalloc')
        self.assertNotHasAttr(Foundation, 'NSZoneRealloc')
        self.assertNotHasAttr(Foundation, 'NSZoneFree')
        self.assertNotHasAttr(Foundation, 'NSZoneFromPointer')
        self.assertNotHasAttr(Foundation, 'NSAllocateCollectable')
        self.assertNotHasAttr(Foundation, 'NSReallocateCollectable')
        self.assertNotHasAttr(Foundation, 'NSAllocateMemoryPages')
        self.assertNotHasAttr(Foundation, 'NSDeallocateMemoryPages')
        self.assertNotHasAttr(Foundation, 'NSCopyMemoryPages')
    def testConstants(self):
        self.assertEqual(NSScannedOption, (1<<0))
        self.assertEqual(NSCollectorDisabledOption, (1<<1))

    def testMakeCollectable(self):
        v = NSMakeCollectable
        
        o = NSObject.alloc().init()
        CFRetain(o)
        v = NSMakeCollectable(o)
        self.assertIs(v, o)
        v = NSMakeCollectable(None)
        self.assertIs(v, None)
    def testInfoFunctions(self):
        v = NSPageSize()
        self.assertIsInstance(v, (int, long))
        v = NSLogPageSize()
        self.assertIsInstance(v, (int, long))
        v = NSRoundUpToMultipleOfPageSize(500)
        self.assertIsInstance(v, (int, long))
        v = NSRoundDownToMultipleOfPageSize(500)
        self.assertIsInstance(v, (int, long))
        v = NSRealMemoryAvailable()
        self.assertIsInstance(v, (int, long))
    def testZoneCreation(self):
        z = NSDefaultMallocZone()
        if z is not None:
            self.assertIsInstance(z, NSZonePtr)
        z = NSCreateZone(5000, 100, True)
        self.assertIsInstance(z, NSZonePtr)
        NSSetZoneName(z, u"Hello World")
        nm = NSZoneName(z)
        self.assertEqual(nm, u"Hello World")

        NSRecycleZone(z); z = None


if __name__ == "__main__":
    main()
