
from PyObjCTools.TestSupport import *
from Quartz.PDFKit import *

class TestPDFPage (TestCase):
    def testConstants(self):
        self.assertEqual(kPDFDisplayBoxMediaBox, 0)
        self.assertEqual(kPDFDisplayBoxCropBox, 1)
        self.assertEqual(kPDFDisplayBoxBleedBox, 2)
        self.assertEqual(kPDFDisplayBoxTrimBox, 3)
        self.assertEqual(kPDFDisplayBoxArtBox, 4)

    def testMethods(self):
        self.assertResultIsBOOL(PDFPage.displaysAnnotations)
        self.assertArgIsBOOL(PDFPage.setDisplaysAnnotations_, 0)

if __name__ == "__main__":
    main()
