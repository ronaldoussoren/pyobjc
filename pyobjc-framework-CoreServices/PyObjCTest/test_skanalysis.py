
from PyObjCTools.TestSupport import *
import CoreServices

class TestSKAnalysis (TestCase):
    def testConstants(self):
        self.assertIsInstance(CoreServices.kSKLanguageTypes, unicode)
        self.assertIsInstance(CoreServices.kSKMinTermLength, unicode)
        self.assertIsInstance(CoreServices.kSKSubstitutions, unicode)
        self.assertIsInstance(CoreServices.kSKStopWords, unicode)
        self.assertIsInstance(CoreServices.kSKProximityIndexing, unicode)
        self.assertIsInstance(CoreServices.kSKMaximumTerms, unicode)
        self.assertIsInstance(CoreServices.kSKTermChars, unicode)
        self.assertIsInstance(CoreServices.kSKStartTermChars, unicode)
        self.assertIsInstance(CoreServices.kSKEndTermChars, unicode)

if __name__ == "__main__":
    main()
