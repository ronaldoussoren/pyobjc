from PyObjCTools.TestSupport import *
from Foundation import *

class TestNSTextCheckingResult (TestCase):
    @min_os_level('10.6')
    def testConstants(self):
        self.failUnlessEqual(NSTextCheckingTypeOrthography, 1 << 0)
        self.failUnlessEqual(NSTextCheckingTypeSpelling, 1 << 1)
        self.failUnlessEqual(NSTextCheckingTypeGrammar, 1 << 2)
        self.failUnlessEqual(NSTextCheckingTypeDate, 1 << 3)
        self.failUnlessEqual(NSTextCheckingTypeAddress, 1 << 4)
        self.failUnlessEqual(NSTextCheckingTypeLink, 1 << 5)
        self.failUnlessEqual(NSTextCheckingTypeQuote, 1 << 6)
        self.failUnlessEqual(NSTextCheckingTypeDash, 1 << 7)
        self.failUnlessEqual(NSTextCheckingTypeReplacement, 1 << 8)
        self.failUnlessEqual(NSTextCheckingTypeCorrection, 1 << 9)

        self.failUnlessEqual(NSTextCheckingAllSystemTypes, 0xffffffff)
        self.failUnlessEqual(NSTextCheckingAllCustomTypes, 0xffffffff << 32)
        self.failUnlessEqual(NSTextCheckingAllTypes, (NSTextCheckingAllSystemTypes | NSTextCheckingAllCustomTypes))

        self.failUnlessIsInstance(NSTextCheckingNameKey, unicode)
        self.failUnlessIsInstance(NSTextCheckingJobTitleKey, unicode)
        self.failUnlessIsInstance(NSTextCheckingOrganizationKey, unicode)
        self.failUnlessIsInstance(NSTextCheckingStreetKey, unicode)
        self.failUnlessIsInstance(NSTextCheckingCityKey, unicode)
        self.failUnlessIsInstance(NSTextCheckingStateKey, unicode)
        self.failUnlessIsInstance(NSTextCheckingZIPKey, unicode)
        self.failUnlessIsInstance(NSTextCheckingCountryKey, unicode)
        self.failUnlessIsInstance(NSTextCheckingPhoneKey, unicode)


    @min_os_level('10.6')
    def testMethods(self):
        self.failUnlessResultHasType(NSTextCheckingResult.range, NSRange.__typestr__)

        self.failUnlessArgHasType(NSTextCheckingResult.orthographyCheckingResultWithRange_orthography_, 0, NSRange.__typestr__)
        self.failUnlessArgHasType(NSTextCheckingResult.spellCheckingResultWithRange_, 0, NSRange.__typestr__)
        self.failUnlessArgHasType(NSTextCheckingResult.grammarCheckingResultWithRange_details_, 0, NSRange.__typestr__)
        self.failUnlessArgHasType(NSTextCheckingResult.dateCheckingResultWithRange_date_, 0, NSRange.__typestr__)
        self.failUnlessArgHasType(NSTextCheckingResult.dateCheckingResultWithRange_date_timeZone_duration_, 0, NSRange.__typestr__)
        self.failUnlessArgHasType(NSTextCheckingResult.addressCheckingResultWithRange_components_, 0, NSRange.__typestr__)
        self.failUnlessArgHasType(NSTextCheckingResult.linkCheckingResultWithRange_URL_, 0, NSRange.__typestr__)
        self.failUnlessArgHasType(NSTextCheckingResult.quoteCheckingResultWithRange_replacementString_, 0, NSRange.__typestr__)
        self.failUnlessArgHasType(NSTextCheckingResult.dashCheckingResultWithRange_replacementString_, 0, NSRange.__typestr__)
        self.failUnlessArgHasType(NSTextCheckingResult.replacementCheckingResultWithRange_replacementString_, 0, NSRange.__typestr__)
        self.failUnlessArgHasType(NSTextCheckingResult.correctionCheckingResultWithRange_replacementString_, 0, NSRange.__typestr__)



if __name__ == "__main__":
    main()
