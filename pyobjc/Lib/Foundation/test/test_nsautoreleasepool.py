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

        # The actual test will issue a DeprecationWarning, the warnings code
        # below surpresses that warning.
        import warnings
        warnings.filterwarnings('ignore', category=DeprecationWarning)
        try:
            NSAutoreleasePool.pyobjcPushPool()
            bar = NSMutableArray.array()
            NSAutoreleasePool.pyobjcPopPool()
            bar.addObject_( "a" ) # should still exist because of python GC
        finally:
            del warnings.filters[0]

if __name__ == '__main__':
    unittest.main( )
