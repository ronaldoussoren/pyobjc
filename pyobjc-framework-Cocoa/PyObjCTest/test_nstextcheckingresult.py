import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSTextCheckingResult(TestCase):
    @min_os_level("10.6")
    def testConstants(self):
        self.assertEqual(Foundation.NSTextCheckingTypeOrthography, 1 << 0)
        self.assertEqual(Foundation.NSTextCheckingTypeSpelling, 1 << 1)
        self.assertEqual(Foundation.NSTextCheckingTypeGrammar, 1 << 2)
        self.assertEqual(Foundation.NSTextCheckingTypeDate, 1 << 3)
        self.assertEqual(Foundation.NSTextCheckingTypeAddress, 1 << 4)
        self.assertEqual(Foundation.NSTextCheckingTypeLink, 1 << 5)
        self.assertEqual(Foundation.NSTextCheckingTypeQuote, 1 << 6)
        self.assertEqual(Foundation.NSTextCheckingTypeDash, 1 << 7)
        self.assertEqual(Foundation.NSTextCheckingTypeReplacement, 1 << 8)
        self.assertEqual(Foundation.NSTextCheckingTypeCorrection, 1 << 9)

        self.assertEqual(Foundation.NSTextCheckingAllSystemTypes, 0xFFFFFFFF)
        self.assertEqual(Foundation.NSTextCheckingAllCustomTypes, (0xFFFFFFFF << 32))
        self.assertEqual(
            Foundation.NSTextCheckingAllTypes,
            (
                Foundation.NSTextCheckingAllSystemTypes
                | Foundation.NSTextCheckingAllCustomTypes
            ),
        )

        self.assertIsInstance(Foundation.NSTextCheckingNameKey, str)
        self.assertIsInstance(Foundation.NSTextCheckingJobTitleKey, str)
        self.assertIsInstance(Foundation.NSTextCheckingOrganizationKey, str)
        self.assertIsInstance(Foundation.NSTextCheckingStreetKey, str)
        self.assertIsInstance(Foundation.NSTextCheckingCityKey, str)
        self.assertIsInstance(Foundation.NSTextCheckingStateKey, str)
        self.assertIsInstance(Foundation.NSTextCheckingZIPKey, str)
        self.assertIsInstance(Foundation.NSTextCheckingCountryKey, str)
        self.assertIsInstance(Foundation.NSTextCheckingPhoneKey, str)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertEqual(Foundation.NSTextCheckingTypeRegularExpression, 1 << 10)
        self.assertEqual(Foundation.NSTextCheckingTypePhoneNumber, 1 << 11)
        self.assertEqual(Foundation.NSTextCheckingTypeTransitInformation, 1 << 12)

        self.assertIsInstance(Foundation.NSTextCheckingAirlineKey, str)
        self.assertIsInstance(Foundation.NSTextCheckingFlightKey, str)

    @min_os_level("10.6")
    def testMethods(self):
        self.assertResultHasType(
            Foundation.NSTextCheckingResult.range, Foundation.NSRange.__typestr__
        )

        self.assertArgHasType(
            Foundation.NSTextCheckingResult.orthographyCheckingResultWithRange_orthography_,
            0,
            Foundation.NSRange.__typestr__,
        )
        self.assertArgHasType(
            Foundation.NSTextCheckingResult.spellCheckingResultWithRange_,
            0,
            Foundation.NSRange.__typestr__,
        )
        self.assertArgHasType(
            Foundation.NSTextCheckingResult.grammarCheckingResultWithRange_details_,
            0,
            Foundation.NSRange.__typestr__,
        )
        self.assertArgHasType(
            Foundation.NSTextCheckingResult.dateCheckingResultWithRange_date_,
            0,
            Foundation.NSRange.__typestr__,
        )
        self.assertArgHasType(
            Foundation.NSTextCheckingResult.dateCheckingResultWithRange_date_timeZone_duration_,
            0,
            Foundation.NSRange.__typestr__,
        )
        self.assertArgHasType(
            Foundation.NSTextCheckingResult.addressCheckingResultWithRange_components_,
            0,
            Foundation.NSRange.__typestr__,
        )
        self.assertArgHasType(
            Foundation.NSTextCheckingResult.linkCheckingResultWithRange_URL_,
            0,
            Foundation.NSRange.__typestr__,
        )
        self.assertArgHasType(
            Foundation.NSTextCheckingResult.quoteCheckingResultWithRange_replacementString_,
            0,
            Foundation.NSRange.__typestr__,
        )
        self.assertArgHasType(
            Foundation.NSTextCheckingResult.dashCheckingResultWithRange_replacementString_,
            0,
            Foundation.NSRange.__typestr__,
        )
        self.assertArgHasType(
            Foundation.NSTextCheckingResult.replacementCheckingResultWithRange_replacementString_,  # noqa: B950
            0,
            Foundation.NSRange.__typestr__,
        )
        self.assertArgHasType(
            Foundation.NSTextCheckingResult.correctionCheckingResultWithRange_replacementString_,  # noqa: B950
            0,
            Foundation.NSRange.__typestr__,
        )

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertArgHasType(
            Foundation.NSTextCheckingResult.regularExpressionCheckingResultWithRanges_count_regularExpression_,  # noqa: B950
            0,
            b"n^" + Foundation.NSRange.__typestr__,
        )
        self.assertArgSizeInArg(
            Foundation.NSTextCheckingResult.regularExpressionCheckingResultWithRanges_count_regularExpression_,  # noqa: B950
            0,
            1,
        )
