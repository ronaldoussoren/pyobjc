from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSNumberFormatter (TestCase):
    def testConstants(self):
        self.assertEqual(NSNumberFormatterNoStyle, kCFNumberFormatterNoStyle)
        self.assertEqual(NSNumberFormatterDecimalStyle, kCFNumberFormatterDecimalStyle)
        self.assertEqual(NSNumberFormatterCurrencyStyle, kCFNumberFormatterCurrencyStyle)
        self.assertEqual(NSNumberFormatterPercentStyle, kCFNumberFormatterPercentStyle)
        self.assertEqual(NSNumberFormatterScientificStyle, kCFNumberFormatterScientificStyle)
        self.assertEqual(NSNumberFormatterSpellOutStyle, kCFNumberFormatterSpellOutStyle)

        self.assertEqual(NSNumberFormatterBehaviorDefault, 0)
        self.assertEqual(NSNumberFormatterBehavior10_0, 1000)
        self.assertEqual(NSNumberFormatterBehavior10_4, 1040)

        self.assertEqual(NSNumberFormatterPadBeforePrefix, kCFNumberFormatterPadBeforePrefix)
        self.assertEqual(NSNumberFormatterPadAfterPrefix, kCFNumberFormatterPadAfterPrefix)
        self.assertEqual(NSNumberFormatterPadBeforeSuffix, kCFNumberFormatterPadBeforeSuffix)
        self.assertEqual(NSNumberFormatterPadAfterSuffix, kCFNumberFormatterPadAfterSuffix)

        self.assertEqual(NSNumberFormatterRoundCeiling, kCFNumberFormatterRoundCeiling)
        self.assertEqual(NSNumberFormatterRoundFloor, kCFNumberFormatterRoundFloor)
        self.assertEqual(NSNumberFormatterRoundDown, kCFNumberFormatterRoundDown)
        self.assertEqual(NSNumberFormatterRoundUp, kCFNumberFormatterRoundUp)
        self.assertEqual(NSNumberFormatterRoundHalfEven, kCFNumberFormatterRoundHalfEven)
        self.assertEqual(NSNumberFormatterRoundHalfDown, kCFNumberFormatterRoundHalfDown)
        self.assertEqual(NSNumberFormatterRoundHalfUp, kCFNumberFormatterRoundHalfUp)


    def testOutput(self):
        self.assertResultIsBOOL(NSNumberFormatter.getObjectValue_forString_range_error_)
        self.assertArgIsOut(NSNumberFormatter.getObjectValue_forString_range_error_, 0)
        self.assertArgIsInOut(NSNumberFormatter.getObjectValue_forString_range_error_, 2)
        self.assertArgIsOut(NSNumberFormatter.getObjectValue_forString_range_error_, 3)

        self.assertResultIsBOOL(NSNumberFormatter.generatesDecimalNumbers)
        self.assertArgIsBOOL(NSNumberFormatter.setGeneratesDecimalNumbers_, 0)
        self.assertResultIsBOOL(NSNumberFormatter.allowsFloats)
        self.assertArgIsBOOL(NSNumberFormatter.setAllowsFloats_, 0)
        self.assertResultIsBOOL(NSNumberFormatter.alwaysShowsDecimalSeparator)
        self.assertArgIsBOOL(NSNumberFormatter.setAlwaysShowsDecimalSeparator_, 0)
        self.assertResultIsBOOL(NSNumberFormatter.usesGroupingSeparator)
        self.assertArgIsBOOL(NSNumberFormatter.setUsesGroupingSeparator_, 0)
        self.assertResultIsBOOL(NSNumberFormatter.isLenient)
        self.assertArgIsBOOL(NSNumberFormatter.setLenient_, 0)
        self.assertResultIsBOOL(NSNumberFormatter.usesSignificantDigits)
        self.assertArgIsBOOL(NSNumberFormatter.setUsesSignificantDigits_, 0)
        self.assertResultIsBOOL(NSNumberFormatter.isPartialStringValidationEnabled)
        self.assertArgIsBOOL(NSNumberFormatter.setPartialStringValidationEnabled_, 0)
        self.assertResultIsBOOL(NSNumberFormatter.hasThousandSeparators)
        self.assertArgIsBOOL(NSNumberFormatter.setHasThousandSeparators_, 0)
        self.assertResultIsBOOL(NSNumberFormatter.localizesFormat)
        self.assertArgIsBOOL(NSNumberFormatter.setLocalizesFormat_, 0)



if __name__ == "__main__":
    main()
