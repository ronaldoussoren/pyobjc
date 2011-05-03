
from PyObjCTools.TestSupport import *
from Quartz.PDFKit import *

class TestPDFAnnotation (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(PDFAnnotation.shouldDisplay)
        self.assertArgIsBOOL(PDFAnnotation.setShouldDisplay_, 0)
        self.assertResultIsBOOL(PDFAnnotation.shouldPrint)
        self.assertArgIsBOOL(PDFAnnotation.setShouldPrint_, 0)
        self.assertResultIsBOOL(PDFAnnotation.hasAppearanceStream)

if __name__ == "__main__":
    main()
