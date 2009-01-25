
from PyObjCTools.TestSupport import *
from SearchKit import *

class TestSKAnalysis (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(kSKLanguageTypes, unicode)
        self.failUnlessIsInstance(kSKMinTermLength, unicode)
        self.failUnlessIsInstance(kSKSubstitutions, unicode)
        self.failUnlessIsInstance(kSKStopWords, unicode)
        self.failUnlessIsInstance(kSKProximityIndexing, unicode)
        self.failUnlessIsInstance(kSKMaximumTerms, unicode)
        self.failUnlessIsInstance(kSKTermChars, unicode)
        self.failUnlessIsInstance(kSKStartTermChars, unicode)
        self.failUnlessIsInstance(kSKEndTermChars, unicode)

if __name__ == "__main__":
    main()
