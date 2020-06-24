from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestPDFAnnotationButtonStamp(TestCase):
    @min_os_level("10.12")
    def testMethods(self):
        self.assertResultIsBOOL(Quartz.PDFAnnotationStamp.isSignature)
