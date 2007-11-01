import unittest
import objc

from Foundation import *

class TestNSExceptionInteraction(unittest.TestCase):
    def testRepeatedAllocInit(self):
        for i in range(1,1000):
            a = NSException.alloc().initWithName_reason_userInfo_( u"Bogus", u"A bad reason", { u"foo" : u"bar" } )

    def testFormat(self):
        try:
            NSException.raise_format_('ExceptionName', 'Format: %s %d', 'hello', 42)

        except TypeError:
            raise

        except objc.error, e:
            self.assertEquals(e._pyobjc_info_['name'], 'ExceptionName')
            self.assertEquals(e._pyobjc_info_['reason'], 'Format: hello 42')

        self.assertRaises(TypeError, NSException.raise_format_arguments_, "FooError", "foo", [])

if __name__ == '__main__':
    unittest.main( )
