"""
Check if we manage retainCounts correctly.
"""
from PyObjCTools.TestSupport import *
import objc, gc
from PyObjCTest.fnd import *

LeaksDel = 0

class LeaksClass (NSObject):
    def init(self):
        self = super(LeaksClass, self).init()
        return self

    def __del__(self):
        global LeaksDel

        LeaksDel = 1

class SlottedClass (NSObject):
    __slots__ = ('slot1',)

    def init(self):
        NSObject.pyobjc_instanceMethods.init(self)
        self.slot1 = LeaksClass.alloc().init()
        return self

class MemberClass (NSObject):

    def init(self):
        self = NSObject.pyobjc_instanceMethods.init(self)
        self.slot1 = LeaksClass.alloc().init()
        return self

class TestRetains(TestCase):
    def testPyClass(self):

        global LeaksDel

        LeaksDel = 0
        self.assertEquals(LeaksDel, 0)

        o = LeaksClass.alloc().init()
        self.assertIsNotNone(o)
        self.assertEquals(LeaksDel, 0)
        del o
        self.assertEquals(LeaksDel, 1)

    def testOCClass1(self):
        global LeaksDel

        LeaksDel = 0
        self.assertEquals(LeaksDel, 0)
        pool = NSAutoreleasePool.alloc().init()
        c = NSMutableArray.arrayWithArray_([ LeaksClass.alloc().init() ])
        del pool

        pool = NSAutoreleasePool.alloc().init()
        self.assertIsNotNone(c)
        self.assertEquals(LeaksDel, 0)
        del c
        del pool
        self.assertEquals(LeaksDel, 1)

    def testOCClass2(self):
        global LeaksDel

        LeaksDel = 0
        self.assertEquals(LeaksDel, 0)
        pool = NSAutoreleasePool.alloc().init()
        c = NSMutableArray.alloc()
        c = c.initWithArray_(
            [ LeaksClass.alloc().init() ])
        del pool

        pool = NSAutoreleasePool.alloc().init()
        self.assertIsNotNone(c)
        self.assertEquals(LeaksDel, 0)
        del c
        del pool
        self.assertEquals(LeaksDel, 1)

    def testSlots(self):
        global LeaksDel

        LeaksDel = 0
        pool = NSAutoreleasePool.alloc().init()

        o = SlottedClass.alloc().init()
        self.assertEquals(LeaksDel, 0)
        del o
        del pool
        self.assertEquals(LeaksDel, 1)

    def testMembers(self):
        global LeaksDel

        LeaksDel = 0
        pool = NSAutoreleasePool.alloc().init()

        o = MemberClass.alloc().init()
        self.assertEquals(LeaksDel, 0)
        del o
        del pool
        gc.collect()
        self.assertEquals(LeaksDel, 1)



if __name__ == '__main__':
    main()
