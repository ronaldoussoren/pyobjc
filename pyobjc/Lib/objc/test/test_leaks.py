"""
Check if we manage retainCounts correctly.
"""
import unittest
import objc

# Most usefull systems will at least have 'NSObject'.
NSObject = objc.lookUpClass('NSObject')
NSMutableArray = objc.lookUpClass('NSMutableArray')

LeaksDel = 0

class LeaksClass (NSObject):
    def __del__(self):
        global LeaksDel 

        LeaksDel = 1

class TestRetains(unittest.TestCase):
    def testPyClass(self):

        global LeaksDel

        LeaksDel = 0
        self.assertEquals(LeaksDel, 0)

        o = LeaksClass.alloc().init()
        self.assert_(o is not None)
        self.assertEquals(LeaksDel, 0)
        del o
        self.assertEquals(LeaksDel, 1)

    def testOCClass1(self):
        global LeaksDel

        LeaksDel = 0
        self.assertEquals(LeaksDel, 0)
        c = NSMutableArray.arrayWithArray_([ LeaksClass.alloc().init() ])
        objc.recyleAutoreleasePool()

        self.assert_(c is not None)
        self.assertEquals(LeaksDel, 0)
        del c
        self.assertEquals(LeaksDel, 1)

    def testOCClass2(self):
        global LeaksDel

        LeaksDel = 0
        self.assertEquals(LeaksDel, 0)
        c = NSMutableArray.alloc()
        c = c.initWithArray_(
            [ LeaksClass.alloc().init() ])
        objc.recyleAutoreleasePool()

        self.assert_(c is not None)
        self.assertEquals(LeaksDel, 0)
        del c
        self.assertEquals(LeaksDel, 1)


if __name__ == '__main__':
    unittest.main()
