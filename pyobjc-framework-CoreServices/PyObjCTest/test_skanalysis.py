import CoreServices
from PyObjCTools.TestSupport import TestCase


class TestSKAnalysis(TestCase):
    def testConstants(self):
        self.assertIsInstance(CoreServices.kSKLanguageTypes, str)
        self.assertIsInstance(CoreServices.kSKMinTermLength, str)
        self.assertIsInstance(CoreServices.kSKSubstitutions, str)
        self.assertIsInstance(CoreServices.kSKStopWords, str)
        self.assertIsInstance(CoreServices.kSKProximityIndexing, str)
        self.assertIsInstance(CoreServices.kSKMaximumTerms, str)
        self.assertIsInstance(CoreServices.kSKTermChars, str)
        self.assertIsInstance(CoreServices.kSKStartTermChars, str)
        self.assertIsInstance(CoreServices.kSKEndTermChars, str)
