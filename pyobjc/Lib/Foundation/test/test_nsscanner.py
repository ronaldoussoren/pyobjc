import unittest
import objc

from Foundation import *

class TestNSScannerUsage(unittest.TestCase):

    # Python 2.2 doesn't have this one:
    def assertAlmostEquals(self, val1, val2, message=None):
        self.assert_ (abs (val1 - val2) < 0.00001, message)

    def testUsage(self):
        obj = NSScanner.scannerWithString_("1.2 2.4")

        didConvert, value = obj.scanDouble_()
        self.assert_(didConvert)
        self.assertAlmostEquals(value, 1.2)

        didConvert, value = obj.scanFloat_()
        self.assert_(didConvert)
        self.assertAlmostEquals(value, 2.4)

if __name__ == '__main__':
    unittest.main( )
