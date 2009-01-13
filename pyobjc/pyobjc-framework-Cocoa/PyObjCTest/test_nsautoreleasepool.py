from PyObjCTools.TestSupport import *
import objc

from Foundation import *

class TestNSAutoreleasePoolInteraction(TestCase):

    def testNSAutoreleasePoolPlain(self):
        pool = NSAutoreleasePool.alloc().init()
        bar = NSMutableArray.array()
        pool.release()
        bar.addObject_( u"a" ) # should still exist because of python GC

if __name__ == '__main__':
    main( )
