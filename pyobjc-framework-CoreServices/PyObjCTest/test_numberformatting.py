import CoreServices
from PyObjCTools.TestSupport import TestCase


class TestNumberFormatting(TestCase):
    def assert_not_wrapped(self, name):
        self.assertTrue(
            not hasattr(CoreServices, name), f"{name!r} exposed in bindings"
        )

    def test_not_wrapped(self):
        self.assert_not_wrapped("NumFormatString")
        self.assert_not_wrapped("fVNumber")
        self.assert_not_wrapped("fPositive")
        self.assert_not_wrapped("fNegative")
        self.assert_not_wrapped("fZero")
        self.assert_not_wrapped("fFormatOK")
        self.assert_not_wrapped("fBestGuess")
        self.assert_not_wrapped("fOutOfSynch")
        self.assert_not_wrapped("fSpuriousChars")
        self.assert_not_wrapped("fMissingDelimiter")
        self.assert_not_wrapped("fExtraDecimal")
        self.assert_not_wrapped("fMissingLiteral")
        self.assert_not_wrapped("fExtraExp")
        self.assert_not_wrapped("fFormatOverflow")
        self.assert_not_wrapped("fFormStrIsNAN")
        self.assert_not_wrapped("fBadPartsTable")
        self.assert_not_wrapped("fExtraPercent")
        self.assert_not_wrapped("fExtraSeparator")
        self.assert_not_wrapped("fEmptyFormatString")
        self.assert_not_wrapped("FVector")
        self.assert_not_wrapped("numtostring")
        self.assert_not_wrapped("StringToNum")
        self.assert_not_wrapped("NumToString")
        self.assert_not_wrapped("ExtendedToString")
        self.assert_not_wrapped("StringToExtended")
        self.assert_not_wrapped("StringToFormatRec")
        self.assert_not_wrapped("FormatRecToString")
        self.assert_not_wrapped("FormatX2Str")
        self.assert_not_wrapped("FormatStr2X")
        self.assert_not_wrapped("Str2Format")
        self.assert_not_wrapped("Format2Str")
        self.assert_not_wrapped("")
