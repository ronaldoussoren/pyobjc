# Place holder for real tests.
import unittest
import objc

from Foundation import NSLocalizedString

class TestNSLocalizedString(unittest.TestCase):
    def testBasic(self):
        # This is mostly a regression tests, the function used to crash on
        # this...
        if objc.platform != 'MACOSX':
            return

        s = NSLocalizedString(u"hello world", u"")
        objc.recycleAutoreleasePool()
        self.assertEquals (s, u"hello world")
        # XXX : Since we get the same object back, it's still unicode
        #self.assertEquals (s.nsstring().description(), u"hello world")

if __name__ == '__main__':
    unittest.main( )
