# Place holder for real tests.
import unittest
import objc

from Foundation import NSLocalizedString

class TestNSLocalizedString(unittest.TestCase):
    def testBasic(self):
        # This is mostly a regression tests, the function used to crash on 
        # this...

        s = NSLocalizedString("hello world", "")
        objc.recycle_autorelease_pool()
        self.assertEquals (s, "hello world")
        self.assertEquals (s.nsstring().description(), "hello world")

        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestNSLocalizedString))
    return suite

if __name__ == '__main__':
    unittest.main( )

