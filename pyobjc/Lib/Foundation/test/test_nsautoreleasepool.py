import unittest
import objc

from Foundation import *

class TestNSAutoreleasePoolInteraction(unittest.TestCase):
    def testNSAutoreleasePoolPlain(self):
        pool = NSAutoreleasePool.alloc().init()
        bar = NSMutableArray.array()
        pool.release()
        bar.addObject_( "a" ) # should still exist because of python GC

    def testNSAutoreleasePool(self):
        NSAutoreleasePool.pyobjcPushPool()
        bar = NSMutableArray.array()
        NSAutoreleasePool.pyobjcPopPool()
        bar.addObject_( "a" ) # should still exist because of python GC

if __name__ == '__main__':
    unittest.main( )
