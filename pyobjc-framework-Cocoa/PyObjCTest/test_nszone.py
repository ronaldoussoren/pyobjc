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
        self.assertEquals(zone.__pointer__, zone2.__pointer__)

        self.assertRaises(TypeError, NSObject.allocWithZone_, 10)
        #self.assertRaises(TypeError, NSObject.allocWithZone_, objc.NULL)


    def testNoMallocAndFriends(self):
        import Foundation
        self.failIf(hasattr(Foundation, 'NSZoneMalloc'))
        self.failIf(hasattr(Foundation, 'NSZoneCalloc'))
        self.failIf(hasattr(Foundation, 'NSZoneRealloc'))
        self.failIf(hasattr(Foundation, 'NSZoneFree'))
        self.failIf(hasattr(Foundation, 'NSZoneFromPointer'))
        self.failIf(hasattr(Foundation, 'NSAllocateCollectable'))
        self.failIf(hasattr(Foundation, 'NSReallocateCollectable'))
        self.failIf(hasattr(Foundation, 'NSAllocateMemoryPages'))
        self.failIf(hasattr(Foundation, 'NSDeallocateMemoryPages'))
        self.failIf(hasattr(Foundation, 'NSCopyMemoryPages'))

    def testConstants(self):
        self.assertEquals(NSScannedOption, (1<<0))
        self.assertEquals(NSCollectorDisabledOption, (1<<1))

    def testMakeCollectable(self):
        v = NSMakeCollectable
        
        o = NSObject.alloc().init()
        CFRetain(o)
        v = NSMakeCollectable(o)
        self.failUnless(v is o)

        v = NSMakeCollectable(None)
        self.failUnless(v is None)

    def testInfoFunctions(self):
        v = NSPageSize()
        self.failUnless(isinstance(v, (int, long)))
        v = NSLogPageSize()
        self.failUnless(isinstance(v, (int, long)))
        v = NSRoundUpToMultipleOfPageSize(500)
        self.failUnless(isinstance(v, (int, long)))
        v = NSRoundDownToMultipleOfPageSize(500)
        self.failUnless(isinstance(v, (int, long)))
        v = NSRealMemoryAvailable()
        self.failUnless(isinstance(v, (int, long)))

    def testZoneCreation(self):
        z = NSDefaultMallocZone()
        self.failUnless(z is None or isinstance(z, NSZonePtr))

        z = NSCreateZone(5000, 100, True)
        self.failUnless(isinstance(z, NSZonePtr))

        NSSetZoneName(z, u"Hello World")
        nm = NSZoneName(z)
        self.assertEquals(nm, u"Hello World")

        NSRecycleZone(z); z = None


if __name__ == "__main__":
    main()
