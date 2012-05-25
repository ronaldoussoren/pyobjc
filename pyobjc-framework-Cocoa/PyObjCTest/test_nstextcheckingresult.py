from PyObjCTools.TestSupport import *
from Foundation import *

try:
    unicode
except NameError:
    unicode = str

class TestNSTextCheckingResult (TestCase):
    @min_os_level('10.6')
    def testConstants(self):
        self.assertEqual(NSTextCheckingTypeOrthography, 1 << 0)
        self.assertEqual(NSTextCheckingTypeSpelling, 1 << 1)
        self.assertEqual(NSTextCheckingTypeGrammar, 1 << 2)
        self.assertEqual(NSTextCheckingTypeDate, 1 << 3)
        self.assertEqual(NSTextCheckingTypeAddress, 1 << 4)
        self.assertEqual(NSTextCheckingTypeLink, 1 << 5)
        self.assertEqual(NSTextCheckingTypeQuote, 1 << 6)
        self.assertEqual(NSTextCheckingTypeDash, 1 << 7)
        self.assertEqual(NSTextCheckingTypeReplacement, 1 << 8)
        self.assertEqual(NSTextCheckingTypeCorrection, 1 << 9)

        self.assertEqual(NSTextCheckingAllSystemTypes, 0xffffffff)
        self.assertEqual(NSTextCheckingAllCustomTypes, (0xffffffff << 32))
        self.assertEqual(NSTextCheckingAllTypes, (NSTextCheckingAllSystemTypes | NSTextCheckingAllCustomTypes))

        self.assertIsInstance(NSTextCheckingNameKey, unicode)
        self.assertIsInstance(NSTextCheckingJobTitleKey, unicode)
        self.assertIsInstance(NSTextCheckingOrganizationKey, unicode)
        self.assertIsInstance(NSTextCheckingStreetKey, unicode)
        self.assertIsInstance(NSTextCheckingCityKey, unicode)
        self.assertIsInstance(NSTextCheckingStateKey, unicode)
        self.assertIsInstance(NSTextCheckingZIPKey, unicode)
        self.assertIsInstance(NSTextCheckingCountryKey, unicode)
        self.assertIsInstance(NSTextCheckingPhoneKey, unicode)

    @min_os_level('10.7')
    def testConstants10_7(self):
        self.assertEqual(NSTextCheckingTypeRegularExpression, 1 << 10)
        self.assertEqual(NSTextCheckingTypePhoneNumber, 1 << 11)
        self.assertEqual(NSTextCheckingTypeTransitInformation, 1 << 12)

        self.assertIsInstance(NSTextCheckingAirlineKey, unicode)
        self.assertIsInstance(NSTextCheckingFlightKey, unicode)


    @min_os_level('10.6')
    def testMethods(self):
        self.assertResultHasType(NSTextCheckingResult.range, NSRange.__typestr__)

        self.assertArgHasType(NSTextCheckingResult.orthographyCheckingResultWithRange_orthography_, 0, NSRange.__typestr__)
        self.assertArgHasType(NSTextCheckingResult.spellCheckingResultWithRange_, 0, NSRange.__typestr__)
        self.assertArgHasType(NSTextCheckingResult.grammarCheckingResultWithRange_details_, 0, NSRange.__typestr__)
        self.assertArgHasType(NSTextCheckingResult.dateCheckingResultWithRange_date_, 0, NSRange.__typestr__)
        self.assertArgHasType(NSTextCheckingResult.dateCheckingResultWithRange_date_timeZone_duration_, 0, NSRange.__typestr__)
        self.assertArgHasType(NSTextCheckingResult.addressCheckingResultWithRange_components_, 0, NSRange.__typestr__)
        self.assertArgHasType(NSTextCheckingResult.linkCheckingResultWithRange_URL_, 0, NSRange.__typestr__)
        self.assertArgHasType(NSTextCheckingResult.quoteCheckingResultWithRange_replacementString_, 0, NSRange.__typestr__)
        self.assertArgHasType(NSTextCheckingResult.dashCheckingResultWithRange_replacementString_, 0, NSRange.__typestr__)
        self.assertArgHasType(NSTextCheckingResult.replacementCheckingResultWithRange_replacementString_, 0, NSRange.__typestr__)
        self.assertArgHasType(NSTextCheckingResult.correctionCheckingResultWithRange_replacementString_, 0, NSRange.__typestr__)

    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertArgHasType(NSTextCheckingResult.regularExpressionCheckingResultWithRanges_count_regularExpression_, 0, b'n^' + NSRange.__typestr__)
        self.assertArgSizeInArg(NSTextCheckingResult.regularExpressionCheckingResultWithRanges_count_regularExpression_, 0, 1)

if __name__ == "__main__":
    main()
