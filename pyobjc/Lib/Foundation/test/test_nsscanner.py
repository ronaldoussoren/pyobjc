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

        obj = NSScanner.scannerWithString_("abcd1234 efgh")

        didConvert, value = obj.scanCharactersFromSet_intoString_(
                NSCharacterSet.lowercaseLetterCharacterSet())
        self.assert_(didConvert)
        self.assertEquals(value, "abcd")

        didConvert, value = obj.scanInt_()
        self.assert_(didConvert)
        self.assertEquals(value, 1234)

        obj = NSScanner.scannerWithString_("1234 efgh")

        didConvert, value = obj.scanLongLong_()
        self.assert_(didConvert)
        self.assertEquals(value, 1234)

        didConvert, value = obj.scanString_intoString_("efgh")
        self.assert_(didConvert)
        self.assertEquals(value, "efgh")

        obj = NSScanner.scannerWithString_("1234 efgh")
        didConvert, value = obj.scanUpToCharactersFromSet_intoString_(
                NSCharacterSet.lowercaseLetterCharacterSet())
        self.assert_(didConvert)
        self.assertEquals(value, "1234 ")


if __name__ == '__main__':
    unittest.main( )
