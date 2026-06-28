from PyObjCTools.TestSupport import TestCase
import Quartz


class TestPDFAnnotationTextWidget(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(Quartz.PDFAnnotationTextWidget.isMultiline)
        self.assertArgIsBOOL(Quartz.PDFAnnotationTextWidget.setIsMultiline_, 0)
