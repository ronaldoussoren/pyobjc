import CoreServices
from PyObjCTools.TestSupport import TestCase
import objc


class TestSKSummary(TestCase):
    def testTypes(self):
        self.assertIsInstance(CoreServices.SKSummaryRef, objc.objc_class)

    def testFunctions(self):
        self.assertIsInstance(CoreServices.SKSummaryGetTypeID(), int)

        ref = CoreServices.SKSummaryCreateWithString("hello world.  and you too.")
        self.assertIsInstance(ref, CoreServices.SKSummaryRef)

        v = CoreServices.SKSummaryGetSentenceCount(ref)
        self.assertIsInstance(v, int)

        v = CoreServices.SKSummaryGetParagraphCount(ref)
        self.assertIsInstance(v, int)

        self.assertResultIsCFRetained(CoreServices.SKSummaryCopySentenceAtIndex)
        v = CoreServices.SKSummaryCopySentenceAtIndex(ref, 0)
        self.assertIsInstance(v, str)

        self.assertResultIsCFRetained(CoreServices.SKSummaryCopyParagraphAtIndex)
        v = CoreServices.SKSummaryCopyParagraphAtIndex(ref, 0)
        self.assertIsInstance(v, str)

        self.assertResultIsCFRetained(CoreServices.SKSummaryCopySentenceSummaryString)
        v = CoreServices.SKSummaryCopyParagraphAtIndex(ref, 0)
        self.assertIsInstance(v, str)

        self.assertResultIsCFRetained(CoreServices.SKSummaryCopyParagraphSummaryString)
        v = CoreServices.SKSummaryCopyParagraphSummaryString(ref, 1)
        self.assertIsInstance(v, str)

        v, o1, o2, o3 = CoreServices.SKSummaryGetSentenceSummaryInfo(
            ref, 1, None, None, None
        )
        self.assertIsInstance(v, int)
        self.assertIsInstance(o1, int)
        self.assertIsInstance(o2, int)
        self.assertIsInstance(o3, int)

        v, o1, o2 = CoreServices.SKSummaryGetParagraphSummaryInfo(ref, 1, None, None)
        self.assertIsInstance(v, int)
        self.assertIsInstance(o1, int)
        self.assertIsInstance(o2, int)
