from PyObjCTools.TestSupport import TestCase
import Quartz


class TestPDFOutline(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(Quartz.PDFOutline.isOpen)
        self.assertArgIsBOOL(Quartz.PDFOutline.setIsOpen_, 0)
