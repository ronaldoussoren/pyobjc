
from PyObjCTools.TestSupport import *
from Quartz.PDFKit import *

class TestPDFPage (TestCase):
    def testConstants(self):
        self.failUnlessEqual(kPDFDisplayBoxMediaBox, 0)
        self.failUnlessEqual(kPDFDisplayBoxCropBox, 1)
        self.failUnlessEqual(kPDFDisplayBoxBleedBox, 2)
        self.failUnlessEqual(kPDFDisplayBoxTrimBox, 3)
        self.failUnlessEqual(kPDFDisplayBoxArtBox, 4)

    def testMethods(self):
        self.failUnlessResultIsBOOL(PDFPage.displaysAnnotations)
        self.failUnlessArgIsBOOL(PDFPage.setDisplaysAnnotations_, 0)

if __name__ == "__main__":
    main()
