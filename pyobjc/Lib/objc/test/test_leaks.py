"""
Check if we manage retainCounts correctly.
"""
import unittest
import objc

# Most usefull systems will at least have 'NSObject'.
NSObject = objc.lookUpClass('NSObject')
NSMutableArray = objc.lookUpClass('NSMutableArray')

Level1Del = 0

class Level1Class (NSObject):
    def __del__(self):
        global Level1Del 

        Level1Del = 1

class TestRetains(unittest.TestCase):
    def testPyClass(self):

        global Level1Del

        Level1Del = 0
        self.assertEquals(Level1Del, 0)

        o = Level1Class.alloc().init()
        self.assert_(o is not None)
        self.assertEquals(Level1Del, 0)
        del o
        self.assertEquals(Level1Del, 1)

    def testOCClass1(self):
        global Level1Del

        Level1Del = 0
        self.assertEquals(Level1Del, 0)
        c = NSMutableArray.arrayWithArray_([ Level1Class.alloc().init() ])
        objc.recycle_autorelease_pool()

        self.assert_(c is not None)
        self.assertEquals(Level1Del, 0)
        del c
        self.assertEquals(Level1Del, 1)

    def testOCClass2(self):
        global Level1Del

        Level1Del = 0
        self.assertEquals(Level1Del, 0)
        c = NSMutableArray.alloc()
        c = c.initWithArray_(
            [ Level1Class.alloc().init() ])
        objc.recycle_autorelease_pool()

        self.assert_(c is not None)
        self.assertEquals(Level1Del, 0)
        del c
        self.assertEquals(Level1Del, 1)


if __name__ == '__main__':
    unittest.main()
