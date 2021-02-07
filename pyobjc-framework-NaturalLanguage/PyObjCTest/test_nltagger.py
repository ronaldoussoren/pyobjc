from PyObjCTools.TestSupport import TestCase, min_os_level
import objc
import NaturalLanguage


class TestNLTagger(TestCase):
    def test_constants(self):
        self.assertEqual(NaturalLanguage.NLTaggerOmitWords, 1 << 0)
        self.assertEqual(NaturalLanguage.NLTaggerOmitPunctuation, 1 << 1)
        self.assertEqual(NaturalLanguage.NLTaggerOmitWhitespace, 1 << 2)
        self.assertEqual(NaturalLanguage.NLTaggerOmitOther, 1 << 3)
        self.assertEqual(NaturalLanguage.NLTaggerJoinNames, 1 << 4)
        self.assertEqual(NaturalLanguage.NLTaggerJoinContractions, 1 << 5)

        self.assertEqual(NaturalLanguage.NLTaggerAssetsResultAvailable, 0)
        self.assertEqual(NaturalLanguage.NLTaggerAssetsResultNotAvailable, 1)
        self.assertEqual(NaturalLanguage.NLTaggerAssetsResultError, 2)

    def test_methods(self):
        self.assertArgIsBlock(
            NaturalLanguage.NLTagger.enumerateTagsInRange_unit_scheme_options_usingBlock_,
            4,
            objc._C_VOID
            + objc._C_ID
            + NaturalLanguage.NSRange.__typestr__
            + objc._C_OUT
            + objc._C_PTR
            + objc._C_NSBOOL,
        )

    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertArgIsBlock(
            NaturalLanguage.NLTagger.requestAssetsForLanguage_tagScheme_completionHandler_,
            2,
            b"v" + objc._C_NSInteger + b"@",
        )

    @min_os_level("10.16")
    def test_methods10_16(self):
        self.assertArgIsOut(
            NaturalLanguage.NLTagger.tagHypothesesAtIndex_unit_scheme_maximumCount_tokenRange_,
            4,
        )
