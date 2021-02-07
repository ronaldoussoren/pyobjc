from PyObjCTools.TestSupport import TestCase
import Quartz


class TestPDFAnnotationLink(TestCase):
    def testMethods(self):
        self.assertArgIsBOOL(Quartz.PDFAnnotationLink.setHighlighted_, 0)
