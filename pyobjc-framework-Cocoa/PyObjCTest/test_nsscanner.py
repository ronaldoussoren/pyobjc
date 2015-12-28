from PyObjCTools.TestSupport import *
import objc

from Foundation import *

class TestNSScannerUsage(TestCase):
    def testUsage(self):
        obj = NSScanner.scannerWithString_(b"1.2 2.5".decode('ascii'))

        didConvert, value = obj.scanDouble_(None)
        self.assertTrue(didConvert)
        self.assertAlmostEqual(value, 1.2)

        didConvert, value = obj.scanFloat_(None)
        self.assertTrue(didConvert)
        self.assertAlmostEqual(value, 2.5)

        obj = NSScanner.scannerWithString_(b"abcd1234 efgh".decode('ascii'))

        didConvert, value = obj.scanCharactersFromSet_intoString_(
                NSCharacterSet.lowercaseLetterCharacterSet(), None)
        self.assertTrue(didConvert)
        self.assertEqual(value, b"abcd".decode('ascii'))

        didConvert, value = obj.scanInt_(None)
        self.assertTrue(didConvert)
        self.assertEqual(value, 1234)

        obj = NSScanner.scannerWithString_(b"1234 efgh".decode('ascii'))

        didConvert, value = obj.scanLongLong_(None)
        self.assertTrue(didConvert)
        self.assertEqual(value, 1234)

        didConvert, value = obj.scanString_intoString_(b"efgh".decode('ascii'), None)
        self.assertTrue(didConvert)
        self.assertEqual(value, b"efgh".decode('ascii'))

        obj = NSScanner.scannerWithString_(b"1234 efgh".decode('ascii'))
        didConvert, value = obj.scanUpToCharactersFromSet_intoString_(
                NSCharacterSet.lowercaseLetterCharacterSet(), None)
        self.assertTrue(didConvert)
        self.assertEqual(value, b"1234 ".decode('ascii'))

    def testMethods(self):
        self.assertArgIsBOOL(NSScanner.setCaseSensitive_, 0)
        self.assertResultIsBOOL(NSScanner.caseSensitive)
        self.assertResultIsBOOL(NSScanner.scanInt_)
        self.assertArgIsOut(NSScanner.scanInt_, 0)
        self.assertResultIsBOOL(NSScanner.scanInteger_)
        self.assertArgIsOut(NSScanner.scanInteger_, 0)
        self.assertResultIsBOOL(NSScanner.scanHexLongLong_)
        self.assertArgIsOut(NSScanner.scanHexLongLong_, 0)
        self.assertResultIsBOOL(NSScanner.scanHexFloat_)
        self.assertArgIsOut(NSScanner.scanHexFloat_, 0)
        self.assertResultIsBOOL(NSScanner.scanHexDouble_)
        self.assertArgIsOut(NSScanner.scanHexDouble_, 0)
        self.assertResultIsBOOL(NSScanner.scanHexInt_)
        self.assertArgIsOut(NSScanner.scanHexInt_, 0)
        self.assertResultIsBOOL(NSScanner.scanLongLong_)
        self.assertArgIsOut(NSScanner.scanLongLong_, 0)
        self.assertResultIsBOOL(NSScanner.scanFloat_)
        self.assertArgIsOut(NSScanner.scanFloat_, 0)
        self.assertResultIsBOOL(NSScanner.scanDouble_)
        self.assertArgIsOut(NSScanner.scanDouble_, 0)
        self.assertResultIsBOOL(NSScanner.scanString_intoString_)
        self.assertArgIsOut(NSScanner.scanString_intoString_, 1)
        self.assertResultIsBOOL(NSScanner.scanCharactersFromSet_intoString_)
        self.assertArgIsOut(NSScanner.scanCharactersFromSet_intoString_, 1)
        self.assertResultIsBOOL(NSScanner.scanUpToString_intoString_)
        self.assertArgIsOut(NSScanner.scanUpToString_intoString_, 1)
        self.assertResultIsBOOL(NSScanner.scanUpToCharactersFromSet_intoString_)
        self.assertArgIsOut(NSScanner.scanUpToCharactersFromSet_intoString_, 1)
        self.assertResultIsBOOL(NSScanner.isAtEnd)

    @min_os_level('10.9')
    def testMethods10_9(self):
        self.assertResultIsBOOL(NSScanner.scanUnsignedLongLong_)
        self.assertArgIsOut(NSScanner.scanUnsignedLongLong_, 0)

if __name__ == '__main__':
    main( )
