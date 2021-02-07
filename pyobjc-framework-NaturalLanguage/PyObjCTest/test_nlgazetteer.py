from PyObjCTools.TestSupport import TestCase, min_os_level
import NaturalLanguage


class TestNLEmbedding(TestCase):
    @min_os_level("10.15")
    def test_methods(self):
        self.assertArgIsOut(
            NaturalLanguage.NLGazetteer.gazetteerWithContentsOfURL_error_, 1
        )
        self.assertArgIsOut(NaturalLanguage.NLGazetteer.initWithContentsOfURL_error_, 1)
        self.assertArgIsOut(NaturalLanguage.NLGazetteer.initWithData_error_, 1)
        self.assertArgIsOut(
            NaturalLanguage.NLGazetteer.initWithDictionary_language_error_, 2
        )

        self.assertResultIsBOOL(
            NaturalLanguage.NLGazetteer.writeGazetteerForDictionary_language_toURL_error_
        )
        self.assertArgIsOut(
            NaturalLanguage.NLGazetteer.writeGazetteerForDictionary_language_toURL_error_,
            3,
        )
