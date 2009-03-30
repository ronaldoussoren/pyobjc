from PyObjCTools.TestSupport import *
import objc

from Foundation import *

class TestNSScannerUsage(TestCase):

    # Python 2.2 doesn't have this one:
    def assertAlmostEquals(self, val1, val2, message=None):
        self.assert_ (abs (val1 - val2) < 0.00001, message)

    def testUsage(self):
        obj = NSScanner.scannerWithString_(u"1.2 2.4")

        didConvert, value = obj.scanDouble_(None)
        self.assert_(didConvert)
        self.assertAlmostEquals(value, 1.2)

        didConvert, value = obj.scanFloat_(None)
        self.assert_(didConvert)
        self.assertAlmostEquals(value, 2.4)

        obj = NSScanner.scannerWithString_(u"abcd1234 efgh")

        didConvert, value = obj.scanCharactersFromSet_intoString_(
                NSCharacterSet.lowercaseLetterCharacterSet(), None)
        self.assert_(didConvert)
        self.assertEquals(value, u"abcd")

        didConvert, value = obj.scanInt_(None)
        self.assert_(didConvert)
        self.assertEquals(value, 1234)

        obj = NSScanner.scannerWithString_(u"1234 efgh")

        didConvert, value = obj.scanLongLong_(None)
        self.assert_(didConvert)
        self.assertEquals(value, 1234)

        didConvert, value = obj.scanString_intoString_(u"efgh", None)
        self.assert_(didConvert)
        self.assertEquals(value, u"efgh")

        obj = NSScanner.scannerWithString_(u"1234 efgh")
        didConvert, value = obj.scanUpToCharactersFromSet_intoString_(
                NSCharacterSet.lowercaseLetterCharacterSet(), None)
        self.assert_(didConvert)
        self.assertEquals(value, u"1234 ")

    def testMethods(self):
        self.failUnlessArgIsBOOL(NSScanner.setCaseSensitive_, 0)
        self.failUnlessResultIsBOOL(NSScanner.caseSensitive)
        self.failUnlessResultIsBOOL(NSScanner.scanInt_)
        self.failUnlessArgIsOut(NSScanner.scanInt_, 0)
        self.failUnlessResultIsBOOL(NSScanner.scanInteger_)
        self.failUnlessArgIsOut(NSScanner.scanInteger_, 0)
        self.failUnlessResultIsBOOL(NSScanner.scanHexLongLong_)
        self.failUnlessArgIsOut(NSScanner.scanHexLongLong_, 0)
        self.failUnlessResultIsBOOL(NSScanner.scanHexFloat_)
        self.failUnlessArgIsOut(NSScanner.scanHexFloat_, 0)
        self.failUnlessResultIsBOOL(NSScanner.scanHexDouble_)
        self.failUnlessArgIsOut(NSScanner.scanHexDouble_, 0)
        self.failUnlessResultIsBOOL(NSScanner.scanHexInt_)
        self.failUnlessArgIsOut(NSScanner.scanHexInt_, 0)
        self.failUnlessResultIsBOOL(NSScanner.scanLongLong_)
        self.failUnlessArgIsOut(NSScanner.scanLongLong_, 0)
        self.failUnlessResultIsBOOL(NSScanner.scanFloat_)
        self.failUnlessArgIsOut(NSScanner.scanFloat_, 0)
        self.failUnlessResultIsBOOL(NSScanner.scanDouble_)
        self.failUnlessArgIsOut(NSScanner.scanDouble_, 0)
        self.failUnlessResultIsBOOL(NSScanner.scanString_intoString_)
        self.failUnlessArgIsOut(NSScanner.scanString_intoString_, 1)
        self.failUnlessResultIsBOOL(NSScanner.scanCharactersFromSet_intoString_)
        self.failUnlessArgIsOut(NSScanner.scanCharactersFromSet_intoString_, 1)
        self.failUnlessResultIsBOOL(NSScanner.scanUpToString_intoString_)
        self.failUnlessArgIsOut(NSScanner.scanUpToString_intoString_, 1)
        self.failUnlessResultIsBOOL(NSScanner.scanUpToCharactersFromSet_intoString_)
        self.failUnlessArgIsOut(NSScanner.scanUpToCharactersFromSet_intoString_, 1)
        self.failUnlessResultIsBOOL(NSScanner.isAtEnd)


if __name__ == '__main__':
    main( )
