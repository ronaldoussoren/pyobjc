from PyObjCTools.TestSupport import TestCase
import Quartz


class TestPDFAnnotationLink(TestCase):
    def test_methods(self):
        self.assertArgIsBOOL(Quartz.PDFAnnotationLink.setHighlighted_, 0)
