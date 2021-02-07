import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSAutoreleasePoolInteraction(TestCase):
    def testNSAutoreleasePoolPlain(self):
        pool = Foundation.NSAutoreleasePool.alloc().init()
        bar = Foundation.NSMutableArray.array()
        del pool  # Always use 'del pool' instead of 'pool.release()'!
        bar.addObject_("a")  # should still exist because of python GC
