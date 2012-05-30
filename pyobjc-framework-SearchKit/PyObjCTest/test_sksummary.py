
from PyObjCTools.TestSupport import *
from SearchKit import *

try:
    unicode
except NameError:
    unicode = str

try:
    long
except NameError:
    long = int

class TestSKSummary (TestCase):
    def testTypes(self):
        self.assertIsInstance(SKSummaryRef, objc.objc_class)

    def testFunctions(self):
        self.assertIsInstance(SKSummaryGetTypeID(), (int, long))

        ref = SKSummaryCreateWithString(b"hello world.  and you too.".decode('latin1'))
        self.assertIsInstance(ref, SKSummaryRef)

        v = SKSummaryGetSentenceCount(ref)
        self.assertIsInstance(v, (int, long))

        v = SKSummaryGetParagraphCount(ref)
        self.assertIsInstance(v, (int, long))

        self.assertResultIsCFRetained(SKSummaryCopySentenceAtIndex)
        v = SKSummaryCopySentenceAtIndex(ref, 0)
        self.assertIsInstance(v, unicode)

        self.assertResultIsCFRetained(SKSummaryCopyParagraphAtIndex)
        v = SKSummaryCopyParagraphAtIndex(ref, 0)
        self.assertIsInstance(v, unicode)

        self.assertResultIsCFRetained(SKSummaryCopySentenceSummaryString)
        v = SKSummaryCopyParagraphAtIndex(ref, 0)
        self.assertIsInstance(v, unicode)

        self.assertResultIsCFRetained(SKSummaryCopyParagraphSummaryString)
        v = SKSummaryCopyParagraphSummaryString(ref, 1)
        self.assertIsInstance(v, unicode)

        v, o1, o2, o3 = SKSummaryGetSentenceSummaryInfo(ref, 1, None, None, None)
        self.assertIsInstance(v, (int, long))
        self.assertIsInstance(o1, (int, long))
        self.assertIsInstance(o2, (int, long))
        self.assertIsInstance(o3, (int, long))

        v, o1, o2 = SKSummaryGetParagraphSummaryInfo(ref, 1, None, None)
        self.assertIsInstance(v, (int, long))
        self.assertIsInstance(o1, (int, long))
        self.assertIsInstance(o2, (int, long))



if __name__ == "__main__":
    main()
