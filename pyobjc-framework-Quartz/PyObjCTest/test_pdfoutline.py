from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestPDFOutline(TestCase):
    @min_os_level("10.5")
    def testMethods(self):
        self.assertResultIsBOOL(Quartz.PDFOutline.isOpen)
        self.assertArgIsBOOL(Quartz.PDFOutline.setIsOpen_, 0)
