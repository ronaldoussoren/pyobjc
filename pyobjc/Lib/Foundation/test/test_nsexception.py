import unittest
import objc

from Foundation import *

class TestNSExceptionInteraction(unittest.TestCase):
    def testRepeatedAllocInit(self):
        for i in range(1,1000):
            a = NSException.alloc().initWithName_reason_userInfo_( u"Bogus", u"A bad reason", { u"foo" : u"bar" } )

if __name__ == '__main__':
    unittest.main( )
