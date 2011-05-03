from PyObjCTools.TestSupport import *
import objc

from Foundation import *

class TestNSAutoreleasePoolInteraction(TestCase):

    def testNSAutoreleasePoolPlain(self):
        pool = NSAutoreleasePool.alloc().init()
        bar = NSMutableArray.array()
        del pool # Always use 'del pool' instead of 'pool.release()'!
        bar.addObject_( u"a" ) # should still exist because of python GC

if __name__ == '__main__':
    main( )
