from PyObjCTools.TestSupport import TestCase
import Quartz


class TestPDFAnnotationPopup(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(Quartz.PDFAnnotationPopup.isOpen)
        self.assertArgIsBOOL(Quartz.PDFAnnotationPopup.setIsOpen_, 0)
