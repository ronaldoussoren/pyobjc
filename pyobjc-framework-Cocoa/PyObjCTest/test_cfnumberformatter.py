import CoreFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNumberFormatter(TestCase):
    def testTypes(self):
        self.assertIsCFType(CoreFoundation.CFNumberFormatterRef)

    def testTypeID(self):
        self.assertIsInstance(CoreFoundation.CFNumberFormatterGetTypeID(), int)

    def testFuncs(self):
        locale = CoreFoundation.CFLocaleCreate(None, "en_US")
        fmt = CoreFoundation.CFNumberFormatterCreate(
            None, locale, CoreFoundation.kCFNumberFormatterDecimalStyle
        )
        self.assertIsInstance(fmt, CoreFoundation.CFNumberFormatterRef)
        v = CoreFoundation.CFNumberFormatterGetLocale(fmt)
        self.assertIs(v, locale)
        v = CoreFoundation.CFNumberFormatterGetStyle(fmt)
        self.assertEqual(v, CoreFoundation.kCFNumberFormatterDecimalStyle)
        v = CoreFoundation.CFNumberFormatterGetFormat(fmt)
        self.assertIsInstance(v, str)
        CoreFoundation.CFNumberFormatterSetFormat(fmt, v[:-2])
        v2 = CoreFoundation.CFNumberFormatterGetFormat(fmt)
        self.assertEqual(v2, v[:-2])
        v = CoreFoundation.CFNumberFormatterCreateStringWithNumber(None, fmt, 42.5)
        self.assertIsInstance(v, str)
        self.assertEqual(v, "42.5")

        v = CoreFoundation.CFNumberFormatterCreateStringWithValue(
            None, fmt, CoreFoundation.kCFNumberDoubleType, 42.5
        )
        self.assertIsInstance(v, str)
        self.assertEqual(v, "42.5")
        num, rng = CoreFoundation.CFNumberFormatterCreateNumberFromString(
            None, fmt, "42.0a", (0, 5), 0
        )
        self.assertEqual(num, 42.0)
        self.assertEqual(rng, (0, 4))
        ok, rng, num = CoreFoundation.CFNumberFormatterGetValueFromString(
            fmt, "42.0a", (0, 5), CoreFoundation.kCFNumberDoubleType, None
        )
        self.assertEqual(ok, True)
        self.assertEqual(num, 42.0)
        self.assertEqual(rng, (0, 4))
        num, rng = CoreFoundation.CFNumberFormatterCreateNumberFromString(
            None,
            fmt,
            "42.0a",
            (0, 5),
            CoreFoundation.kCFNumberFormatterParseIntegersOnly,
        )
        self.assertEqual(num, 42)
        self.assertEqual(rng, (0, 2))
        v = CoreFoundation.CFNumberFormatterCopyProperty(
            fmt, CoreFoundation.kCFNumberFormatterCurrencyCode
        )
        self.assertIsInstance(v, str)
        CoreFoundation.CFNumberFormatterSetProperty(
            fmt, CoreFoundation.kCFNumberFormatterCurrencyCode, "HFL"
        )

        self.assertResultIsCFRetained(CoreFoundation.CFNumberFormatterCopyProperty)
        v = CoreFoundation.CFNumberFormatterCopyProperty(
            fmt, CoreFoundation.kCFNumberFormatterCurrencyCode
        )
        self.assertEqual(v, "HFL")
        self.assertArgIsOut(
            CoreFoundation.CFNumberFormatterGetDecimalInfoForCurrencyCode, 1
        )
        self.assertArgIsOut(
            CoreFoundation.CFNumberFormatterGetDecimalInfoForCurrencyCode, 2
        )
        ok, frac, rnd = CoreFoundation.CFNumberFormatterGetDecimalInfoForCurrencyCode(
            "EUR", None, None
        )
        self.assertEqual(ok, True)
        self.assertEqual(frac, 2)
        self.assertEqual(rnd, 0.0)

    def testConstants(self):
        self.assertEqual(CoreFoundation.kCFNumberFormatterNoStyle, 0)
        self.assertEqual(CoreFoundation.kCFNumberFormatterDecimalStyle, 1)
        self.assertEqual(CoreFoundation.kCFNumberFormatterCurrencyStyle, 2)
        self.assertEqual(CoreFoundation.kCFNumberFormatterPercentStyle, 3)
        self.assertEqual(CoreFoundation.kCFNumberFormatterScientificStyle, 4)
        self.assertEqual(CoreFoundation.kCFNumberFormatterSpellOutStyle, 5)

        self.assertEqual(CoreFoundation.kCFNumberFormatterParseIntegersOnly, 1)

        self.assertEqual(CoreFoundation.kCFNumberFormatterRoundCeiling, 0)
        self.assertEqual(CoreFoundation.kCFNumberFormatterRoundFloor, 1)
        self.assertEqual(CoreFoundation.kCFNumberFormatterRoundDown, 2)
        self.assertEqual(CoreFoundation.kCFNumberFormatterRoundUp, 3)
        self.assertEqual(CoreFoundation.kCFNumberFormatterRoundHalfEven, 4)
        self.assertEqual(CoreFoundation.kCFNumberFormatterRoundHalfDown, 5)
        self.assertEqual(CoreFoundation.kCFNumberFormatterRoundHalfUp, 6)

        self.assertEqual(CoreFoundation.kCFNumberFormatterPadBeforePrefix, 0)
        self.assertEqual(CoreFoundation.kCFNumberFormatterPadAfterPrefix, 1)
        self.assertEqual(CoreFoundation.kCFNumberFormatterPadBeforeSuffix, 2)
        self.assertEqual(CoreFoundation.kCFNumberFormatterPadAfterSuffix, 3)

        self.assertIsInstance(CoreFoundation.kCFNumberFormatterCurrencyCode, str)
        self.assertIsInstance(CoreFoundation.kCFNumberFormatterDecimalSeparator, str)
        self.assertIsInstance(
            CoreFoundation.kCFNumberFormatterCurrencyDecimalSeparator, str
        )
        self.assertIsInstance(
            CoreFoundation.kCFNumberFormatterAlwaysShowDecimalSeparator, str
        )
        self.assertIsInstance(CoreFoundation.kCFNumberFormatterGroupingSeparator, str)
        self.assertIsInstance(
            CoreFoundation.kCFNumberFormatterUseGroupingSeparator, str
        )
        self.assertIsInstance(CoreFoundation.kCFNumberFormatterPercentSymbol, str)
        self.assertIsInstance(CoreFoundation.kCFNumberFormatterZeroSymbol, str)
        self.assertIsInstance(CoreFoundation.kCFNumberFormatterNaNSymbol, str)
        self.assertIsInstance(CoreFoundation.kCFNumberFormatterInfinitySymbol, str)
        self.assertIsInstance(CoreFoundation.kCFNumberFormatterMinusSign, str)
        self.assertIsInstance(CoreFoundation.kCFNumberFormatterPlusSign, str)
        self.assertIsInstance(CoreFoundation.kCFNumberFormatterCurrencySymbol, str)
        self.assertIsInstance(CoreFoundation.kCFNumberFormatterExponentSymbol, str)
        self.assertIsInstance(CoreFoundation.kCFNumberFormatterMinIntegerDigits, str)
        self.assertIsInstance(CoreFoundation.kCFNumberFormatterMaxIntegerDigits, str)
        self.assertIsInstance(CoreFoundation.kCFNumberFormatterMinFractionDigits, str)
        self.assertIsInstance(CoreFoundation.kCFNumberFormatterMaxFractionDigits, str)
        self.assertIsInstance(CoreFoundation.kCFNumberFormatterGroupingSize, str)
        self.assertIsInstance(
            CoreFoundation.kCFNumberFormatterSecondaryGroupingSize, str
        )
        self.assertIsInstance(CoreFoundation.kCFNumberFormatterRoundingMode, str)
        self.assertIsInstance(CoreFoundation.kCFNumberFormatterRoundingIncrement, str)
        self.assertIsInstance(CoreFoundation.kCFNumberFormatterFormatWidth, str)
        self.assertIsInstance(CoreFoundation.kCFNumberFormatterPaddingPosition, str)
        self.assertIsInstance(CoreFoundation.kCFNumberFormatterPaddingCharacter, str)
        self.assertIsInstance(CoreFoundation.kCFNumberFormatterDefaultFormat, str)
        self.assertIsInstance(CoreFoundation.kCFNumberFormatterMultiplier, str)
        self.assertIsInstance(CoreFoundation.kCFNumberFormatterPositivePrefix, str)
        self.assertIsInstance(CoreFoundation.kCFNumberFormatterPositiveSuffix, str)
        self.assertIsInstance(CoreFoundation.kCFNumberFormatterNegativePrefix, str)
        self.assertIsInstance(CoreFoundation.kCFNumberFormatterNegativeSuffix, str)
        self.assertIsInstance(CoreFoundation.kCFNumberFormatterPerMillSymbol, str)
        self.assertIsInstance(
            CoreFoundation.kCFNumberFormatterInternationalCurrencySymbol, str
        )

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertIsInstance(
            CoreFoundation.kCFNumberFormatterCurrencyGroupingSeparator, str
        )
        self.assertIsInstance(CoreFoundation.kCFNumberFormatterIsLenient, str)
        self.assertIsInstance(
            CoreFoundation.kCFNumberFormatterUseSignificantDigits, str
        )
        self.assertIsInstance(
            CoreFoundation.kCFNumberFormatterMinSignificantDigits, str
        )
        self.assertIsInstance(
            CoreFoundation.kCFNumberFormatterMaxSignificantDigits, str
        )

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertEqual(CoreFoundation.kCFNumberFormatterOrdinalStyle, 6)
        self.assertEqual(CoreFoundation.kCFNumberFormatterCurrencyISOCodeStyle, 8)
        self.assertEqual(CoreFoundation.kCFNumberFormatterCurrencyPluralStyle, 9)
        self.assertEqual(CoreFoundation.kCFNumberFormatterCurrencyAccountingStyle, 10)
