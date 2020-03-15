import Foundation
import CoreFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSNumberFormatter(TestCase):
    def testConstants(self):
        self.assertEqual(
            Foundation.NSNumberFormatterNoStyle,
            CoreFoundation.kCFNumberFormatterNoStyle,
        )
        self.assertEqual(
            Foundation.NSNumberFormatterDecimalStyle,
            CoreFoundation.kCFNumberFormatterDecimalStyle,
        )
        self.assertEqual(
            Foundation.NSNumberFormatterCurrencyStyle,
            CoreFoundation.kCFNumberFormatterCurrencyStyle,
        )
        self.assertEqual(
            Foundation.NSNumberFormatterPercentStyle,
            CoreFoundation.kCFNumberFormatterPercentStyle,
        )
        self.assertEqual(
            Foundation.NSNumberFormatterScientificStyle,
            CoreFoundation.kCFNumberFormatterScientificStyle,
        )
        self.assertEqual(
            Foundation.NSNumberFormatterSpellOutStyle,
            CoreFoundation.kCFNumberFormatterSpellOutStyle,
        )

        self.assertEqual(Foundation.NSNumberFormatterBehaviorDefault, 0)
        self.assertEqual(Foundation.NSNumberFormatterBehavior10_0, 1000)
        self.assertEqual(Foundation.NSNumberFormatterBehavior10_4, 1040)

        self.assertEqual(
            Foundation.NSNumberFormatterPadBeforePrefix,
            CoreFoundation.kCFNumberFormatterPadBeforePrefix,
        )
        self.assertEqual(
            Foundation.NSNumberFormatterPadAfterPrefix,
            CoreFoundation.kCFNumberFormatterPadAfterPrefix,
        )
        self.assertEqual(
            Foundation.NSNumberFormatterPadBeforeSuffix,
            CoreFoundation.kCFNumberFormatterPadBeforeSuffix,
        )
        self.assertEqual(
            Foundation.NSNumberFormatterPadAfterSuffix,
            CoreFoundation.kCFNumberFormatterPadAfterSuffix,
        )

        self.assertEqual(
            Foundation.NSNumberFormatterRoundCeiling,
            CoreFoundation.kCFNumberFormatterRoundCeiling,
        )
        self.assertEqual(
            Foundation.NSNumberFormatterRoundFloor,
            CoreFoundation.kCFNumberFormatterRoundFloor,
        )
        self.assertEqual(
            Foundation.NSNumberFormatterRoundDown,
            CoreFoundation.kCFNumberFormatterRoundDown,
        )
        self.assertEqual(
            Foundation.NSNumberFormatterRoundUp,
            CoreFoundation.kCFNumberFormatterRoundUp,
        )
        self.assertEqual(
            Foundation.NSNumberFormatterRoundHalfEven,
            CoreFoundation.kCFNumberFormatterRoundHalfEven,
        )
        self.assertEqual(
            Foundation.NSNumberFormatterRoundHalfDown,
            CoreFoundation.kCFNumberFormatterRoundHalfDown,
        )
        self.assertEqual(
            Foundation.NSNumberFormatterRoundHalfUp,
            CoreFoundation.kCFNumberFormatterRoundHalfUp,
        )

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertEqual(
            Foundation.NSNumberFormatterOrdinalStyle,
            CoreFoundation.kCFNumberFormatterOrdinalStyle,
        )
        self.assertEqual(
            Foundation.NSNumberFormatterCurrencyISOCodeStyle,
            CoreFoundation.kCFNumberFormatterCurrencyISOCodeStyle,
        )
        self.assertEqual(
            Foundation.NSNumberFormatterCurrencyPluralStyle,
            CoreFoundation.kCFNumberFormatterCurrencyPluralStyle,
        )
        self.assertEqual(
            Foundation.NSNumberFormatterCurrencyAccountingStyle,
            CoreFoundation.kCFNumberFormatterCurrencyAccountingStyle,
        )

    def testOutput(self):
        self.assertResultIsBOOL(
            Foundation.NSNumberFormatter.getObjectValue_forString_range_error_
        )
        self.assertArgIsOut(
            Foundation.NSNumberFormatter.getObjectValue_forString_range_error_, 0
        )
        self.assertArgIsInOut(
            Foundation.NSNumberFormatter.getObjectValue_forString_range_error_, 2
        )
        self.assertArgIsOut(
            Foundation.NSNumberFormatter.getObjectValue_forString_range_error_, 3
        )

        self.assertResultIsBOOL(Foundation.NSNumberFormatter.generatesDecimalNumbers)
        self.assertArgIsBOOL(
            Foundation.NSNumberFormatter.setGeneratesDecimalNumbers_, 0
        )
        self.assertResultIsBOOL(Foundation.NSNumberFormatter.allowsFloats)
        self.assertArgIsBOOL(Foundation.NSNumberFormatter.setAllowsFloats_, 0)
        self.assertResultIsBOOL(
            Foundation.NSNumberFormatter.alwaysShowsDecimalSeparator
        )
        self.assertArgIsBOOL(
            Foundation.NSNumberFormatter.setAlwaysShowsDecimalSeparator_, 0
        )
        self.assertResultIsBOOL(Foundation.NSNumberFormatter.usesGroupingSeparator)
        self.assertArgIsBOOL(Foundation.NSNumberFormatter.setUsesGroupingSeparator_, 0)
        self.assertResultIsBOOL(Foundation.NSNumberFormatter.isLenient)
        self.assertArgIsBOOL(Foundation.NSNumberFormatter.setLenient_, 0)
        self.assertResultIsBOOL(Foundation.NSNumberFormatter.usesSignificantDigits)
        self.assertArgIsBOOL(Foundation.NSNumberFormatter.setUsesSignificantDigits_, 0)
        self.assertResultIsBOOL(
            Foundation.NSNumberFormatter.isPartialStringValidationEnabled
        )
        self.assertArgIsBOOL(
            Foundation.NSNumberFormatter.setPartialStringValidationEnabled_, 0
        )
        self.assertResultIsBOOL(Foundation.NSNumberFormatter.hasThousandSeparators)
        self.assertArgIsBOOL(Foundation.NSNumberFormatter.setHasThousandSeparators_, 0)
        self.assertResultIsBOOL(Foundation.NSNumberFormatter.localizesFormat)
        self.assertArgIsBOOL(Foundation.NSNumberFormatter.setLocalizesFormat_, 0)
