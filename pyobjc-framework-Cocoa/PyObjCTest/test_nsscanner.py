import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSScannerUsage(TestCase):
    def testUsage(self):
        obj = Foundation.NSScanner.scannerWithString_("1.2 2.5")

        didConvert, value = obj.scanDouble_(None)
        self.assertTrue(didConvert)
        self.assertAlmostEqual(value, 1.2)

        didConvert, value = obj.scanFloat_(None)
        self.assertTrue(didConvert)
        self.assertAlmostEqual(value, 2.5)

        obj = Foundation.NSScanner.scannerWithString_("abcd1234 efgh")

        didConvert, value = obj.scanCharactersFromSet_intoString_(
            Foundation.NSCharacterSet.lowercaseLetterCharacterSet(), None
        )
        self.assertTrue(didConvert)
        self.assertEqual(value, "abcd")

        didConvert, value = obj.scanInt_(None)
        self.assertTrue(didConvert)
        self.assertEqual(value, 1234)

        obj = Foundation.NSScanner.scannerWithString_("1234 efgh")

        didConvert, value = obj.scanLongLong_(None)
        self.assertTrue(didConvert)
        self.assertEqual(value, 1234)

        didConvert, value = obj.scanString_intoString_("efgh", None)
        self.assertTrue(didConvert)
        self.assertEqual(value, "efgh")

        obj = Foundation.NSScanner.scannerWithString_("1234 efgh")
        didConvert, value = obj.scanUpToCharactersFromSet_intoString_(
            Foundation.NSCharacterSet.lowercaseLetterCharacterSet(), None
        )
        self.assertTrue(didConvert)
        self.assertEqual(value, "1234 ")

    def testMethods(self):
        self.assertArgIsBOOL(Foundation.NSScanner.setCaseSensitive_, 0)
        self.assertResultIsBOOL(Foundation.NSScanner.caseSensitive)
        self.assertResultIsBOOL(Foundation.NSScanner.scanInt_)
        self.assertArgIsOut(Foundation.NSScanner.scanInt_, 0)
        self.assertResultIsBOOL(Foundation.NSScanner.scanInteger_)
        self.assertArgIsOut(Foundation.NSScanner.scanInteger_, 0)
        self.assertResultIsBOOL(Foundation.NSScanner.scanHexLongLong_)
        self.assertArgIsOut(Foundation.NSScanner.scanHexLongLong_, 0)
        self.assertResultIsBOOL(Foundation.NSScanner.scanHexFloat_)
        self.assertArgIsOut(Foundation.NSScanner.scanHexFloat_, 0)
        self.assertResultIsBOOL(Foundation.NSScanner.scanHexDouble_)
        self.assertArgIsOut(Foundation.NSScanner.scanHexDouble_, 0)
        self.assertResultIsBOOL(Foundation.NSScanner.scanHexInt_)
        self.assertArgIsOut(Foundation.NSScanner.scanHexInt_, 0)
        self.assertResultIsBOOL(Foundation.NSScanner.scanLongLong_)
        self.assertArgIsOut(Foundation.NSScanner.scanLongLong_, 0)
        self.assertResultIsBOOL(Foundation.NSScanner.scanFloat_)
        self.assertArgIsOut(Foundation.NSScanner.scanFloat_, 0)
        self.assertResultIsBOOL(Foundation.NSScanner.scanDouble_)
        self.assertArgIsOut(Foundation.NSScanner.scanDouble_, 0)
        self.assertResultIsBOOL(Foundation.NSScanner.scanString_intoString_)
        self.assertArgIsOut(Foundation.NSScanner.scanString_intoString_, 1)
        self.assertResultIsBOOL(Foundation.NSScanner.scanCharactersFromSet_intoString_)
        self.assertArgIsOut(Foundation.NSScanner.scanCharactersFromSet_intoString_, 1)
        self.assertResultIsBOOL(Foundation.NSScanner.scanUpToString_intoString_)
        self.assertArgIsOut(Foundation.NSScanner.scanUpToString_intoString_, 1)
        self.assertResultIsBOOL(
            Foundation.NSScanner.scanUpToCharactersFromSet_intoString_
        )
        self.assertArgIsOut(
            Foundation.NSScanner.scanUpToCharactersFromSet_intoString_, 1
        )
        self.assertResultIsBOOL(Foundation.NSScanner.isAtEnd)

    @min_os_level("10.9")
    def testMethods10_9(self):
        self.assertResultIsBOOL(Foundation.NSScanner.scanUnsignedLongLong_)
        self.assertArgIsOut(Foundation.NSScanner.scanUnsignedLongLong_, 0)
