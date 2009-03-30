from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSNumberFormatter (TestCase):
    def testConstants(self):
        self.assertEquals(NSNumberFormatterNoStyle, kCFNumberFormatterNoStyle)
        self.assertEquals(NSNumberFormatterDecimalStyle, kCFNumberFormatterDecimalStyle)
        self.assertEquals(NSNumberFormatterCurrencyStyle, kCFNumberFormatterCurrencyStyle)
        self.assertEquals(NSNumberFormatterPercentStyle, kCFNumberFormatterPercentStyle)
        self.assertEquals(NSNumberFormatterScientificStyle, kCFNumberFormatterScientificStyle)
        self.assertEquals(NSNumberFormatterSpellOutStyle, kCFNumberFormatterSpellOutStyle)

        self.assertEquals(NSNumberFormatterBehaviorDefault, 0)
        self.assertEquals(NSNumberFormatterBehavior10_0, 1000)
        self.assertEquals(NSNumberFormatterBehavior10_4, 1040)

        self.assertEquals(NSNumberFormatterPadBeforePrefix, kCFNumberFormatterPadBeforePrefix)
        self.assertEquals(NSNumberFormatterPadAfterPrefix, kCFNumberFormatterPadAfterPrefix)
        self.assertEquals(NSNumberFormatterPadBeforeSuffix, kCFNumberFormatterPadBeforeSuffix)
        self.assertEquals(NSNumberFormatterPadAfterSuffix, kCFNumberFormatterPadAfterSuffix)

        self.assertEquals(NSNumberFormatterRoundCeiling, kCFNumberFormatterRoundCeiling)
        self.assertEquals(NSNumberFormatterRoundFloor, kCFNumberFormatterRoundFloor)
        self.assertEquals(NSNumberFormatterRoundDown, kCFNumberFormatterRoundDown)
        self.assertEquals(NSNumberFormatterRoundUp, kCFNumberFormatterRoundUp)
        self.assertEquals(NSNumberFormatterRoundHalfEven, kCFNumberFormatterRoundHalfEven)
        self.assertEquals(NSNumberFormatterRoundHalfDown, kCFNumberFormatterRoundHalfDown)
        self.assertEquals(NSNumberFormatterRoundHalfUp, kCFNumberFormatterRoundHalfUp)


    def testOutput(self):
        self.failUnlessResultIsBOOL(NSNumberFormatter.getObjectValue_forString_range_error_)
        self.failUnlessArgIsOut(NSNumberFormatter.getObjectValue_forString_range_error_, 0)
        self.failUnlessArgIsInOut(NSNumberFormatter.getObjectValue_forString_range_error_, 2)
        self.failUnlessArgIsOut(NSNumberFormatter.getObjectValue_forString_range_error_, 3)

        self.failUnlessResultIsBOOL(NSNumberFormatter.generatesDecimalNumbers)
        self.failUnlessArgIsBOOL(NSNumberFormatter.setGeneratesDecimalNumbers_, 0)
        self.failUnlessResultIsBOOL(NSNumberFormatter.allowsFloats)
        self.failUnlessArgIsBOOL(NSNumberFormatter.setAllowsFloats_, 0)
        self.failUnlessResultIsBOOL(NSNumberFormatter.alwaysShowsDecimalSeparator)
        self.failUnlessArgIsBOOL(NSNumberFormatter.setAlwaysShowsDecimalSeparator_, 0)
        self.failUnlessResultIsBOOL(NSNumberFormatter.usesGroupingSeparator)
        self.failUnlessArgIsBOOL(NSNumberFormatter.setUsesGroupingSeparator_, 0)
        self.failUnlessResultIsBOOL(NSNumberFormatter.isLenient)
        self.failUnlessArgIsBOOL(NSNumberFormatter.setLenient_, 0)
        self.failUnlessResultIsBOOL(NSNumberFormatter.usesSignificantDigits)
        self.failUnlessArgIsBOOL(NSNumberFormatter.setUsesSignificantDigits_, 0)
        self.failUnlessResultIsBOOL(NSNumberFormatter.isPartialStringValidationEnabled)
        self.failUnlessArgIsBOOL(NSNumberFormatter.setPartialStringValidationEnabled_, 0)
        self.failUnlessResultIsBOOL(NSNumberFormatter.hasThousandSeparators)
        self.failUnlessArgIsBOOL(NSNumberFormatter.setHasThousandSeparators_, 0)
        self.failUnlessResultIsBOOL(NSNumberFormatter.localizesFormat)
        self.failUnlessArgIsBOOL(NSNumberFormatter.setLocalizesFormat_, 0)



if __name__ == "__main__":
    main()
