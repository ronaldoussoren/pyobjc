
from PyObjCTools.TestSupport import *
from SearchKit import *

class TestSKAnalysis (TestCase):
    def testConstants(self):
        self.assertIsInstance(kSKLanguageTypes, unicode)
        self.assertIsInstance(kSKMinTermLength, unicode)
        self.assertIsInstance(kSKSubstitutions, unicode)
        self.assertIsInstance(kSKStopWords, unicode)
        self.assertIsInstance(kSKProximityIndexing, unicode)
        self.assertIsInstance(kSKMaximumTerms, unicode)
        self.assertIsInstance(kSKTermChars, unicode)
        self.assertIsInstance(kSKStartTermChars, unicode)
        self.assertIsInstance(kSKEndTermChars, unicode)

if __name__ == "__main__":
    main()
