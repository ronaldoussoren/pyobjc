from PyObjCTools.TestSupport import *
from CoreFoundation import *


class TestNumberFormatter (TestCase):
    def testTypes(self):
        self.failUnlessIsCFType(CFNumberFormatterRef)

    def testTypeID(self):
        self.failUnless(isinstance(CFNumberFormatterGetTypeID(), (int, long)))

    def testFuncs(self):
        locale = CFLocaleCopyCurrent()
        fmt = CFNumberFormatterCreate(None, locale, kCFNumberFormatterDecimalStyle)
        self.failUnless(isinstance(fmt, CFNumberFormatterRef))

        v = CFNumberFormatterGetLocale(fmt)
        self.failUnless(v is locale)

        v = CFNumberFormatterGetStyle(fmt)
        self.failUnless(v == kCFNumberFormatterDecimalStyle)

        v = CFNumberFormatterGetFormat(fmt)
        self.failUnless(isinstance(v, unicode))

        CFNumberFormatterSetFormat(fmt, v[:-2])
        v2 = CFNumberFormatterGetFormat(fmt)
        self.failUnless(v2 == v[:-2])

        v = CFNumberFormatterCreateStringWithNumber(None, fmt, 42.5)
        self.failUnless(isinstance(v, unicode))
        self.failUnless(v == u'42.5')

        num, rng = CFNumberFormatterCreateNumberFromString(None, fmt, u"42.0a", (0, 5), 0)
        self.failUnless(num == 42.0)
        self.failUnless(rng == (0, 4))

        num, rng = CFNumberFormatterCreateNumberFromString(None, fmt, u"42.0a", (0, 5), kCFNumberFormatterParseIntegersOnly)
        self.failUnless(num == 42)
        self.failUnless(rng == (0, 2))

        v = CFNumberFormatterCopyProperty(fmt, kCFNumberFormatterCurrencyCode)
        self.failUnless(isinstance(v, unicode))

        CFNumberFormatterSetProperty(fmt, kCFNumberFormatterCurrencyCode, u"HFL")

        self.failUnlessResultIsCFRetained(CFNumberFormatterCopyProperty)
        v = CFNumberFormatterCopyProperty(fmt, kCFNumberFormatterCurrencyCode)
        self.failUnless(v == u"HFL")

        self.failUnlessArgIsOut(CFNumberFormatterGetDecimalInfoForCurrencyCode, 1)
        self.failUnlessArgIsOut(CFNumberFormatterGetDecimalInfoForCurrencyCode, 2)
        ok, frac, rnd = CFNumberFormatterGetDecimalInfoForCurrencyCode("EUR", None, None)
        self.assertEquals(ok, True)
        self.assertEquals(frac, 2)
        self.assertEquals(rnd, 0.0)



    def testConstants(self):
        self.failUnless(kCFNumberFormatterNoStyle == 0)
        self.failUnless(kCFNumberFormatterDecimalStyle == 1)
        self.failUnless(kCFNumberFormatterCurrencyStyle == 2)
        self.failUnless(kCFNumberFormatterPercentStyle == 3)
        self.failUnless(kCFNumberFormatterScientificStyle == 4)
        self.failUnless(kCFNumberFormatterSpellOutStyle == 5)
        self.failUnless(kCFNumberFormatterParseIntegersOnly == 1)
        self.failUnless(kCFNumberFormatterRoundCeiling == 0)
        self.failUnless(kCFNumberFormatterRoundFloor == 1)
        self.failUnless(kCFNumberFormatterRoundDown == 2)
        self.failUnless(kCFNumberFormatterRoundUp == 3)
        self.failUnless(kCFNumberFormatterRoundHalfEven == 4)
        self.failUnless(kCFNumberFormatterRoundHalfDown == 5)
        self.failUnless(kCFNumberFormatterRoundHalfUp == 6)
        self.failUnless(kCFNumberFormatterPadBeforePrefix == 0)
        self.failUnless(kCFNumberFormatterPadAfterPrefix == 1)
        self.failUnless(kCFNumberFormatterPadBeforeSuffix == 2)
        self.failUnless(kCFNumberFormatterPadAfterSuffix == 3)

        self.failUnless(isinstance(kCFNumberFormatterCurrencyCode, unicode))
        self.failUnless(isinstance(kCFNumberFormatterDecimalSeparator, unicode))
        self.failUnless(isinstance(kCFNumberFormatterCurrencyDecimalSeparator, unicode))
        self.failUnless(isinstance(kCFNumberFormatterAlwaysShowDecimalSeparator, unicode))
        self.failUnless(isinstance(kCFNumberFormatterGroupingSeparator, unicode))
        self.failUnless(isinstance(kCFNumberFormatterUseGroupingSeparator, unicode))
        self.failUnless(isinstance(kCFNumberFormatterPercentSymbol, unicode))
        self.failUnless(isinstance(kCFNumberFormatterZeroSymbol, unicode))
        self.failUnless(isinstance(kCFNumberFormatterNaNSymbol, unicode))
        self.failUnless(isinstance(kCFNumberFormatterInfinitySymbol, unicode))
        self.failUnless(isinstance(kCFNumberFormatterMinusSign, unicode))
        self.failUnless(isinstance(kCFNumberFormatterPlusSign, unicode))
        self.failUnless(isinstance(kCFNumberFormatterCurrencySymbol, unicode))
        self.failUnless(isinstance(kCFNumberFormatterExponentSymbol, unicode))
        self.failUnless(isinstance(kCFNumberFormatterMinIntegerDigits, unicode))
        self.failUnless(isinstance(kCFNumberFormatterMaxIntegerDigits, unicode))
        self.failUnless(isinstance(kCFNumberFormatterMinFractionDigits, unicode))
        self.failUnless(isinstance(kCFNumberFormatterMaxFractionDigits, unicode))
        self.failUnless(isinstance(kCFNumberFormatterGroupingSize, unicode))
        self.failUnless(isinstance(kCFNumberFormatterSecondaryGroupingSize, unicode))
        self.failUnless(isinstance(kCFNumberFormatterRoundingMode, unicode))
        self.failUnless(isinstance(kCFNumberFormatterRoundingIncrement, unicode))
        self.failUnless(isinstance(kCFNumberFormatterFormatWidth, unicode))
        self.failUnless(isinstance(kCFNumberFormatterPaddingPosition, unicode))
        self.failUnless(isinstance(kCFNumberFormatterPaddingCharacter, unicode))
        self.failUnless(isinstance(kCFNumberFormatterDefaultFormat, unicode))
        self.failUnless(isinstance(kCFNumberFormatterMultiplier, unicode))
        self.failUnless(isinstance(kCFNumberFormatterPositivePrefix, unicode))
        self.failUnless(isinstance(kCFNumberFormatterPositiveSuffix, unicode))
        self.failUnless(isinstance(kCFNumberFormatterNegativePrefix, unicode))
        self.failUnless(isinstance(kCFNumberFormatterNegativeSuffix, unicode))
        self.failUnless(isinstance(kCFNumberFormatterPerMillSymbol, unicode))
        self.failUnless(isinstance(kCFNumberFormatterInternationalCurrencySymbol, unicode))

    @min_os_level('10.5')
    def testConstants10_5(self):
        self.failUnless(isinstance(kCFNumberFormatterCurrencyGroupingSeparator, unicode))
        self.failUnless(isinstance(kCFNumberFormatterIsLenient, unicode))
        self.failUnless(isinstance(kCFNumberFormatterUseSignificantDigits, unicode))
        self.failUnless(isinstance(kCFNumberFormatterMinSignificantDigits, unicode))
        self.failUnless(isinstance(kCFNumberFormatterMaxSignificantDigits, unicode))





if __name__ == "__main__":
    main()
