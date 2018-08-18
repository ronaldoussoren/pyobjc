
from PyObjCTools.TestSupport import *
import CoreServices

class TestSKSummary (TestCase):
    def testTypes(self):
        self.assertIsInstance(CoreServices.SKSummaryRef, objc.objc_class)

    def testFunctions(self):
        self.assertIsInstance(CoreServices.SKSummaryGetTypeID(), (int, long))

        ref = CoreServices.SKSummaryCreateWithString(b"hello world.  and you too.".decode('latin1'))
        self.assertIsInstance(ref, CoreServices.SKSummaryRef)

        v = CoreServices.SKSummaryGetSentenceCount(ref)
        self.assertIsInstance(v, (int, long))

        v = CoreServices.SKSummaryGetParagraphCount(ref)
        self.assertIsInstance(v, (int, long))

        self.assertResultIsCFRetained(CoreServices.SKSummaryCopySentenceAtIndex)
        v = CoreServices.SKSummaryCopySentenceAtIndex(ref, 0)
        self.assertIsInstance(v, unicode)

        self.assertResultIsCFRetained(CoreServices.SKSummaryCopyParagraphAtIndex)
        v = CoreServices.SKSummaryCopyParagraphAtIndex(ref, 0)
        self.assertIsInstance(v, unicode)

        self.assertResultIsCFRetained(CoreServices.SKSummaryCopySentenceSummaryString)
        v = CoreServices.SKSummaryCopyParagraphAtIndex(ref, 0)
        self.assertIsInstance(v, unicode)

        self.assertResultIsCFRetained(CoreServices.SKSummaryCopyParagraphSummaryString)
        v = CoreServices.SKSummaryCopyParagraphSummaryString(ref, 1)
        self.assertIsInstance(v, unicode)

        v, o1, o2, o3 = CoreServices.SKSummaryGetSentenceSummaryInfo(ref, 1, None, None, None)
        self.assertIsInstance(v, (int, long))
        self.assertIsInstance(o1, (int, long))
        self.assertIsInstance(o2, (int, long))
        self.assertIsInstance(o3, (int, long))

        v, o1, o2 = CoreServices.SKSummaryGetParagraphSummaryInfo(ref, 1, None, None)
        self.assertIsInstance(v, (int, long))
        self.assertIsInstance(o1, (int, long))
        self.assertIsInstance(o2, (int, long))



if __name__ == "__main__":
    main()
