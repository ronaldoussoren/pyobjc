# Place holder for real tests.
import unittest
import objc

from Foundation import NSLocalizedString

class TestNSLocalizedString(unittest.TestCase):
    def testBasic(self):
        # This is mostly a regression tests, the function used to crash on
        # this...
        if objc.runtime.NSBundle.mainBundle() is None:
            # This is true on GNUstep, that sucks but this test is not
            # important enough to look for a work-around.
            return

        s = NSLocalizedString("hello world", "")
        objc.recycleAutoreleasePool()
        self.assertEquals (s, "hello world")
        self.assertEquals (s.nsstring().description(), "hello world")

if __name__ == '__main__':
    unittest.main( )
