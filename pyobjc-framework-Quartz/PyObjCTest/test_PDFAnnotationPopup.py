from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestPDFAnnotationPopup(TestCase):
    @min_os_level("10.5")
    def testMethods(self):
        self.assertResultIsBOOL(Quartz.PDFAnnotationPopup.isOpen)
        self.assertArgIsBOOL(Quartz.PDFAnnotationPopup.setIsOpen_, 0)
