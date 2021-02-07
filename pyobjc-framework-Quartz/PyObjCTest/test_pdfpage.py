from PyObjCTools.TestSupport import TestCase
import Quartz


class TestPDFPage(TestCase):
    def testConstants(self):
        self.assertEqual(Quartz.kPDFDisplayBoxMediaBox, 0)
        self.assertEqual(Quartz.kPDFDisplayBoxCropBox, 1)
        self.assertEqual(Quartz.kPDFDisplayBoxBleedBox, 2)
        self.assertEqual(Quartz.kPDFDisplayBoxTrimBox, 3)
        self.assertEqual(Quartz.kPDFDisplayBoxArtBox, 4)

    def testMethods(self):
        self.assertResultIsBOOL(Quartz.PDFPage.displaysAnnotations)
        self.assertArgIsBOOL(Quartz.PDFPage.setDisplaysAnnotations_, 0)
