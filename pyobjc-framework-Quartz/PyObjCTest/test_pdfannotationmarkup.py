from PyObjCTools.TestSupport import TestCase
import Quartz


class TestPDFAnnotationMarkup(TestCase):
    def testConstants(self):
        self.assertEqual(Quartz.kPDFMarkupTypeHighlight, 0)
        self.assertEqual(Quartz.kPDFMarkupTypeStrikeOut, 1)
        self.assertEqual(Quartz.kPDFMarkupTypeUnderline, 2)
