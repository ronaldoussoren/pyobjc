from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestPDFAnnotationTextWidget(TestCase):
    @min_os_level("10.9")
    def testMethods(self):
        self.assertResultIsBOOL(Quartz.PDFAnnotationTextWidget.isMultiline)
        self.assertArgIsBOOL(Quartz.PDFAnnotationTextWidget.setIsMultiline_, 0)
