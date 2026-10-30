from PyObjCTools.TestSupport import TestCase
import Quartz


class TestCGPDFOperatorTable(TestCase):
    def test_types(self):
        self.assertIsOpaquePointer(Quartz.CGPDFOperatorTableRef)

    def test_functions(self):
        Quartz.CGPDFOperatorCallback = b"v^{CGPDFScanner=}^v"

        self.assertArgIsIn(Quartz.CGPDFOperatorTableSetCallback, 1)
        self.assertArgIsNullTerminated(Quartz.CGPDFOperatorTableSetCallback, 1)
        self.assertArgIsFunction(
            Quartz.CGPDFOperatorTableSetCallback, 2, Quartz.CGPDFOperatorCallback, True
        )

        Quartz.CGPDFOperatorTableRetain
        Quartz.CGPDFOperatorTableRelease
