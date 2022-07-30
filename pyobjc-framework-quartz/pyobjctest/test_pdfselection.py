from PyObjCTools.TestSupport import TestCase
import Quartz


class TestPDFSelection(TestCase):
    def testMethods(self):
        self.assertArgIsBOOL(Quartz.PDFSelection.drawForPage_withBox_active_, 2)
