import unittest
import objc

from Foundation import *

class TestNSExceptionInteraction(unittest.TestCase):
    def testRepeatedAllocInit(self):
        for i in range(1,1000):
            a = NSException.alloc().initWithName_reason_userInfo_( u"Bogus", u"A bad reason", { u"foo" : u"bar" } )

    def testFormat(self):
        # We don't support varargs, use python's '%' operator to format
        # the message.
        self.assertRaises(TypeError, NSException.raise_format_, "FooError", "foo")
        self.assertRaises(TypeError, NSException.raise_format_arguments_, "FooError", "foo", [])

if __name__ == '__main__':
    unittest.main( )
