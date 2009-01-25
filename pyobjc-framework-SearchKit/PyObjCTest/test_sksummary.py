
from PyObjCTools.TestSupport import *
from SearchKit import *

class TestSKSummary (TestCase):
    def testTypes(self):
        self.failUnlessIsInstance(SKSummaryRef, objc.objc_class)

    def testFunctions(self):
        self.failUnlessIsInstance(SKSummaryGetTypeID(), (int, long))

        ref = SKSummaryCreateWithString(u"hello world.  and you too.")
        self.failUnlessIsInstance(ref, SKSummaryRef)

        v = SKSummaryGetSentenceCount(ref)
        self.failUnlessIsInstance(v, (int, long))

        v = SKSummaryGetParagraphCount(ref)
        self.failUnlessIsInstance(v, (int, long))

        self.failUnlessResultIsCFRetained(SKSummaryCopySentenceAtIndex)
        v = SKSummaryCopySentenceAtIndex(ref, 0)
        self.failUnlessIsInstance(v, unicode)

        self.failUnlessResultIsCFRetained(SKSummaryCopyParagraphAtIndex)
        v = SKSummaryCopyParagraphAtIndex(ref, 0)
        self.failUnlessIsInstance(v, unicode)

        self.failUnlessResultIsCFRetained(SKSummaryCopySentenceSummaryString)
        v = SKSummaryCopyParagraphAtIndex(ref, 0)
        self.failUnlessIsInstance(v, unicode)

        self.failUnlessResultIsCFRetained(SKSummaryCopyParagraphSummaryString)
        v = SKSummaryCopyParagraphSummaryString(ref, 1)
        self.failUnlessIsInstance(v, unicode)

        v, o1, o2, o3 = SKSummaryGetSentenceSummaryInfo(ref, 1, None, None, None)
        self.failUnlessIsInstance(v, (int, long))
        self.failUnlessIsInstance(o1, (int, long))
        self.failUnlessIsInstance(o2, (int, long))
        self.failUnlessIsInstance(o3, (int, long))

        v, o1, o2 = SKSummaryGetParagraphSummaryInfo(ref, 1, None, None)
        self.failUnlessIsInstance(v, (int, long))
        self.failUnlessIsInstance(o1, (int, long))
        self.failUnlessIsInstance(o2, (int, long))



if __name__ == "__main__":
    main()
